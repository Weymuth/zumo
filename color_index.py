#!/usr/bin/env python3
"""color_index.py v1.0 — index every colour in the book BY VALUE, not by spelling.

WHY THIS EXISTS (S112)
----------------------
A colour has many legal spellings and a text search matches only the one you typed.
Two sessions paid for that:

  * S111 — `build_palette` emits UPPERCASE, every value parsed out of the book is
    lowercase. Five constructs read as NEW off-canon blocks, the first diagnosis went
    the wrong way entirely, and 1,809 occurrences had to be normalised.
  * S112 — an off-palette `#666` was logged as `#666666`. A search for the long form
    returns nothing, and a blank result is indistinguishable from a clean one. The
    same value was then changed in ONE page while seventeen shared it, and only
    §25.6 caught it.

The fix is not a better search string. It is to stop comparing spellings and start
comparing VALUES. `#666`, `#666666`, `#666666`, `rgb(102,102,102)` and the class
family `.p-c-666` are one colour; this tool says so.

ENTRYPOINT IS `index(paths)` — not `audit()`, not `main()`.
Returns {canonical_hex: Value}. Every other mode is a view over that dict.

WHAT IT PARSES (§24.10 — parse, do not grep)
--------------------------------------------
Colours are read out of DECLARATION VALUES only, never out of raw text. A naive
`#[0-9a-f]{6}` sweep over a page also matches href fragments and — worse — nothing at
all in `.p-c-666 {` or `class="tok-569cd6"`, where the hex carries no `#`. Sources:

  1. `.css` files          — rule bodies, one declaration at a time.
  2. `<style>` blocks      — same parse.
  3. `style="..."` attrs   — same parse.
  4. presentation attrs    — fill= / stroke= / stop-color= (SVG inlined in HTML).

REACH is computed separately, on `lesson_inventory.expand_classes` output, so a value
delivered to a page through a class counts as reaching that page. This is the number
that would have shown `#666` on seventeen pages before anyone edited one of them.

A SPELLING IS NOT A DEFECT. `--check` fails only on VARIANCE: one value written more
than one way. That is the case trap, and it is mechanical. Whether a value is off
palette is a RULING and is reported, never failed.
"""

import glob
import os
import re
import sys
import collections

VERSION = 'v1.0'

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import lesson_inventory as LI  # noqa: E402

# The 16 CSS named colours that actually appear in hand-written book source, plus the
# few greys. Deliberately NOT the full 148-name list: a name the book never uses is a
# name this tool should not silently canonicalise, because doing so invents a finding.
NAMED = {
    'white': '#ffffff', 'black': '#000000', 'red': '#ff0000', 'green': '#008000',
    'blue': '#0000ff', 'gray': '#808080', 'grey': '#808080', 'silver': '#c0c0c0',
    'orange': '#ffa500', 'yellow': '#ffff00', 'purple': '#800080', 'navy': '#000080',
    'teal': '#008080', 'maroon': '#800000', 'olive': '#808000', 'lime': '#00ff00',
}

# Properties whose value can carry a colour. Parsing by property name keeps `content:`
# and `font-family:` strings out of the index.
COLOR_PROPS = re.compile(
    r'^(color|background|background-color|border|border-[a-z]+|border-[a-z]+-color|'
    r'outline|outline-color|fill|stroke|stop-color|box-shadow|text-shadow|'
    r'text-decoration-color|caret-color|column-rule|column-rule-color|accent-color)$'
)

HEX = re.compile(r'#([0-9a-fA-F]{3,8})\b')
RGBF = re.compile(r'rgba?\(\s*([0-9]{1,3})\s*,\s*([0-9]{1,3})\s*,\s*([0-9]{1,3})\s*'
                  r'(?:,\s*([0-9.]+)\s*)?\)', re.I)
NAMEF = re.compile(r'\b(' + '|'.join(NAMED) + r')\b', re.I)

STYLE_BLOCK = re.compile(r'<style[^>]*>(.*?)</style>', re.S | re.I)
STYLE_ATTR = re.compile(r'style\s*=\s*"([^"]*)"', re.I)
PRES_ATTR = re.compile(r'\b(fill|stroke|stop-color)\s*=\s*"([^"]*)"', re.I)
CSS_RULE = re.compile(r'([^{}]+)\{([^{}]*)\}', re.S)


class Value:
    """One canonical colour and everywhere it comes from."""

    def __init__(self, canon):
        self.canon = canon
        self.spellings = collections.Counter()   # raw text -> times written
        self.sites = []                          # (file, kind, selector_or_prop, raw)
        self.reach = set()                       # pages the value actually paints

    @property
    def n(self):
        return sum(self.spellings.values())


def canon(raw):
    """Every legal spelling of one colour collapses to lowercase #rrggbb[aa].

    Returns None for anything that is not a colour, so callers can tell 'not a
    colour' from 'a colour I could not read' — a distinction the S112 bug ate.
    """
    t = raw.strip().lower()
    m = HEX.fullmatch(t)
    if m:
        h = m.group(1)
        if len(h) in (3, 4):                      # #rgb / #rgba -> #rrggbb / #rrggbbaa
            h = ''.join(c * 2 for c in h)
        if len(h) in (6, 8):
            if len(h) == 8 and h[6:] == 'ff':     # fully opaque is just the colour
                h = h[:6]
            return '#' + h
        return None
    m = RGBF.fullmatch(t)
    if m:
        r, g, b = (int(m.group(i)) for i in (1, 2, 3))
        if max(r, g, b) > 255:
            return None
        a = m.group(4)
        out = '#%02x%02x%02x' % (r, g, b)
        if a is not None and float(a) < 1:
            out += '%02x' % round(float(a) * 255)
        return out
    return NAMED.get(t)


def _decls(body):
    """Split a declaration body into (prop, value) pairs. Semicolons inside url() or
    a quoted string do not split a declaration, so those are masked first."""
    body = re.sub(r'url\([^)]*\)', lambda m: 'url()' + '_' * (len(m.group(0)) - 5), body)
    for d in body.split(';'):
        if ':' not in d:
            continue
        p, _, v = d.partition(':')
        yield p.strip().lower(), v.strip()


def _harvest(value, into, where):
    """Pull every colour token out of one declaration value."""
    for rx in (HEX, RGBF, NAMEF):
        for m in rx.finditer(value):
            c = canon(m.group(0))
            if c:
                into.setdefault(c, Value(c))
                into[c].spellings[m.group(0)] += 1
                into[c].sites.append(where + (m.group(0),))


def index(paths):
    """THE ENTRYPOINT. paths = list of .html and .css files. -> {canon: Value}"""
    out = {}
    for f in paths:
        try:
            src = open(f, encoding='utf-8').read()
        except OSError:
            continue
        if f.endswith('.css'):
            for m in CSS_RULE.finditer(src):
                sel = ' '.join(m.group(1).split())[:60]
                for p, v in _decls(m.group(2)):
                    if COLOR_PROPS.match(p) or p.startswith('--'):
                        _harvest(v, out, (f, 'css-rule', sel))
            continue
        for m in STYLE_BLOCK.finditer(src):
            for r in CSS_RULE.finditer(m.group(1)):
                sel = ' '.join(r.group(1).split())[:60]
                for p, v in _decls(r.group(2)):
                    if COLOR_PROPS.match(p) or p.startswith('--'):
                        _harvest(v, out, (f, 'style-block', sel))
        for m in STYLE_ATTR.finditer(src):
            for p, v in _decls(m.group(1)):
                if COLOR_PROPS.match(p) or p.startswith('--'):
                    _harvest(v, out, (f, 'inline', p))
        for m in PRES_ATTR.finditer(src):
            _harvest(m.group(2), out, (f, 'attr', m.group(1).lower()))
    return out


def reach(idx, pages):
    """Which pages each value actually paints, read through the class expander.

    This is the number that matters before an edit. A value can live in ONE css rule
    and paint SEVENTEEN pages; the site list alone will never say so.
    """
    for f in pages:
        try:
            src = LI.expand_classes(open(f, encoding='utf-8').read())
        except OSError:
            continue
        seen = set()
        for m in STYLE_ATTR.finditer(src):
            for p, v in _decls(m.group(1)):
                if COLOR_PROPS.match(p) or p.startswith('--'):
                    for rx in (HEX, RGBF, NAMEF):
                        for t in rx.finditer(v):
                            c = canon(t.group(0))
                            if c:
                                seen.add(c)
        for m in STYLE_BLOCK.finditer(src):
            for t in HEX.finditer(m.group(1)):
                c = canon(t.group(0))
                if c:
                    seen.add(c)
        for c in seen:
            idx.setdefault(c, Value(c)).reach.add(f)
    return idx


def variants(idx):
    """Values written more than one way. The case trap, mechanically.

    NOTE the absence of .lower() here, and why. The first version of this function
    normalised the spellings before comparing them — which folded `#3A7D5C` and
    `#3a7d5c` into one and reported NO variance, on the exact defect the tool was
    written for. Control B caught it. An instrument that normalises before it
    compares cannot see a normalisation defect.
    """
    return {c: v for c, v in idx.items()
            if len({s.strip() for s in v.spellings}) > 1}


def case_variants(idx):
    """Values whose spellings differ ONLY by case. This is the S111 trap and nothing
    else: same characters, different shift key, and every raw-string comparison in the
    book reads them as two values.

    Kept separate from `variants` on purpose. `white` / `#fff` / `#ffffff` is also
    variance, but it is a HOUSE-STYLE question with a defensible answer either way,
    and a gate that fails on `white` is a gate that gets switched off. Only case is
    mechanical, so only case is gateable.
    """
    out = {}
    for c, v in idx.items():
        raw = {s.strip() for s in v.spellings}
        if len(raw) > 1 and len({s.lower() for s in raw}) < len(raw):
            out[c] = v
    return out


def _sources():
    pages = sorted(glob.glob('lessons/Lesson_*.html'))
    pages += [p for p in ('going_deeper.html', 'index.html', 'newproject.html',
                          'timer.html', 'tutor/tutor.html') if os.path.exists(p)]
    css = sorted(glob.glob('css/*.css'))
    return pages, css


def _report(idx, only=None, show_sites=False):
    rows = sorted(idx.values(), key=lambda v: (-v.n, v.canon))
    if only:
        want = canon(only)
        if not want:
            print(f'  "{only}" is not a colour this tool can read.')
            return 1
        rows = [v for v in rows if v.canon == want]
        if not rows:
            print(f'  {want} does not appear in any declaration in the book.')
            return 0
        show_sites = True
    print(f'{"VALUE":11} {"USES":>5} {"PAGES":>6}  SPELLINGS')
    for v in rows:
        sp = ', '.join(f'{s}×{n}' for s, n in v.spellings.most_common())
        print(f'{v.canon:11} {v.n:>5} {len(v.reach):>6}  {sp[:64]}')
        if show_sites:
            by = collections.Counter((f, k, s) for f, k, s, _ in v.sites)
            for (f, k, s), n in by.most_common(40):
                print(f'      {f:34} {k:12} {s}  ×{n}')
            if v.reach:
                print(f'      REACHES {len(v.reach)} page(s): '
                      f'{", ".join(sorted(os.path.basename(p) for p in v.reach))[:150]}')
    return 0


# ------------------------------------------------------------------ selftest
def _selftest():
    """Control-run: loud on planted defects, silent on innocent shapes.

    Every control here failed once against a deliberately broken build before it was
    trusted (§24.6b). An assert that cannot fail is not evidence.
    """
    bad = []

    def ck(cond, msg):
        if not cond:
            bad.append(msg)

    # --- canonicalisation: the spellings that cost S111 and S112 ---
    ck(canon('#666') == '#666666', 'shorthand #666 must canonicalise to #666666')
    ck(canon('#666666') == '#666666', 'long form must canonicalise to itself')
    ck(canon('#3A7D5C') == '#3a7d5c', 'THE S111 CASE TRAP: uppercase must fold')
    ck(canon('#3a7d5c') == canon('#3A7D5C'), 'case must not split one value in two')
    ck(canon('rgb(102, 102, 102)') == '#666666', 'rgb() must reach the same value')
    ck(canon('rgba(102,102,102,1)') == '#666666', 'fully opaque rgba is the colour')
    ck(canon('white') == '#ffffff', 'named colours must fold')
    ck(canon('#ffffffff') == '#ffffff', 'an ff alpha is opaque, not a second value')
    ck(canon('#66666680') == '#66666680', 'a real alpha must NOT be discarded')

    # --- NOT colours: the tool must say so rather than guess ---
    ck(canon('inherit') is None, 'inherit is not a colour')
    ck(canon('#sec-3') is None, 'an href fragment is not a colour')
    ck(canon('rgb(300,0,0)') is None, 'out-of-range rgb is not a colour')
    ck(canon('') is None, 'empty is not a colour')

    import tempfile
    d = tempfile.mkdtemp()
    cwd = os.getcwd()
    try:
        os.chdir(d)
        os.makedirs('css')

        # CONTROL A — clean tree, one value, one spelling. Must be SILENT.
        open('a.html', 'w').write(
            '<style>.x{color:#3a7d5c;}</style><p style="color: #3a7d5c;">hi</p>')
        i = index(['a.html'])
        ck(set(i) == {'#3a7d5c'}, f'control A: expected one value, got {sorted(i)}')
        ck(i['#3a7d5c'].n == 2, 'control A: both occurrences must be counted')
        ck(variants(i) == {}, 'control A: one spelling is not variance')

        # CONTROL B — the S111 defect. Same value, two cases. Must be LOUD.
        open('b.html', 'w').write(
            '<style>.x{color:#3A7D5C;}</style><p style="color: #3a7d5c;">hi</p>')
        i = index(['b.html'])
        ck(len(i) == 1, 'control B: case must NOT split one value into two')
        ck(list(variants(i)) == ['#3a7d5c'], 'control B: variance must be reported')

        # CONTROL C — the S112 defect. Shorthand vs long form. Must be LOUD.
        open('c.html', 'w').write(
            '<style>.p-c-666{color:#666666;}</style><p style="color: #666;">hi</p>')
        i = index(['c.html'])
        ck(len(i) == 1, 'control C: #666 and #666666 are one value')
        ck(list(variants(i)) == ['#666666'], 'control C: variance must be reported')

        # CONTROL B2 — the split. `white` vs `#fff` is variance but NOT case variance;
        # a gate that fails on it is a gate that gets switched off.
        open('b2.html', 'w').write(
            '<style>.x{color:white;}</style><p style="color: #fff;">hi</p>')
        i = index(['b2.html'])
        ck(list(variants(i)) == ['#ffffff'], 'control B2: format variance IS variance')
        ck(case_variants(i) == {}, 'control B2: format variance is NOT case variance')
        open('b3.html', 'w').write(
            '<style>.x{color:#FFF;}</style><p style="color: #fff;">hi</p>')
        ck(list(case_variants(index(['b3.html']))) == ['#ffffff'],
           'control B3: same characters, different case, must be LOUD')

        # CONTROL D — innocent shapes that must NOT enter the index.
        open('d.html', 'w').write(
            '<a href="#sec-3">x</a><p class="tok-569cd6-c-569cd6">y</p>'
            '<style>.z{font-family:"Courier New";content:"#abcdef";}</style>')
        i = index(['d.html'])
        ck(i == {}, f'control D: no colour should be found, got {sorted(i)}')

        # CONTROL D2 — a class NAME carrying a hex is not a declaration.
        # This is the shape a naive grep gets wrong in BOTH directions.
        open('d2.html', 'w').write('<p class="p-c-666">no declaration here</p>')
        ck(index(['d2.html']) == {}, 'control D2: a class name is not a colour use')

        # CONTROL E — a semicolon inside url() must not split a declaration.
        open('e.html', 'w').write(
            '<p style="background: url(a;b.png); color: #123456;">x</p>')
        i = index(['e.html'])
        ck('#123456' in i, 'control E: url() semicolon must not eat the next decl')

        # CONTROL F — REACH. One css rule, two pages, and the pages carry no hex of
        # their own. The whole point of the tool: reach is not visible in the source.
        open('css/book.css', 'w').write('.p-c-666 {\n  color: #666666;\n}\n')
        open('f1.html', 'w').write('<p class="p-c-666">one</p>')
        open('f2.html', 'w').write('<p class="p-c-666">two</p>')
        i = index(['css/book.css'])
        ck(i['#666666'].reach == set(), 'control F: reach is empty before it is computed')
        reach(i, ['f1.html', 'f2.html'])
        ck(len(i['#666666'].reach) == 2,
           f'control F: value must reach BOTH pages, got {i["#666666"].reach}')
    finally:
        os.chdir(cwd)

    print(f'color_index.py {VERSION} — selftest')
    if bad:
        for b in bad:
            print('  FAIL', b)
        print(f'{len(bad)} CONTROL(S) FAILED')
        return 1
    print('ALL CONTROLS PASS - loud on both spelling traps, silent on four innocent '
          'shapes, and reach is proven to cross files.')
    return 0


def main(argv):
    if '--selftest' in argv:
        return _selftest()
    pages, css = _sources()
    idx = index(pages + css)
    reach(idx, pages)

    if '--variants' in argv or '--check' in argv:
        allv, cv = variants(idx), case_variants(idx)
        fmt = {c: v for c, v in allv.items() if c not in cv}
        print(f'color_index.py {VERSION} — {len(idx)} distinct colour(s)')
        if cv:
            print(f'\n  CASE VARIANCE — {len(cv)} value(s). Mechanical, and the S111 trap:')
            for c, val in sorted(cv.items()):
                sp = ', '.join(f'{s}×{n}' for s, n in val.spellings.most_common())
                print(f'    {c}  {sp}')
        if fmt:
            print(f'\n  FORMAT VARIANCE — {len(fmt)} value(s). A RULING, not a defect:')
            for c, val in sorted(fmt.items()):
                sp = ', '.join(f'{s}×{n}' for s, n in val.spellings.most_common())
                print(f'    {c}  {sp}')
        if '--check' in argv:
            if cv:
                print(f'\n{len(cv)} value(s) differ only by case.')
                return 1
            print('\n  no colour in the book is spelled two ways that differ only by case')
            return 0
        if not allv:
            print('  no value is spelled more than one way')
        return 0

    only = None
    for i, a in enumerate(argv):
        if a == '--value' and i + 1 < len(argv):
            only = argv[i + 1]
    print(f'color_index.py {VERSION} — {len(idx)} distinct colours across '
          f'{len(pages)} page(s) + {len(css)} stylesheet(s)')
    print('ENUMERATION, NOT A VERDICT (§24.6a). Off-palette is a RULING; only spelling '
          'variance is mechanical — see --check.\n')
    return _report(idx, only=only, show_sites='--sites' in argv)


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
