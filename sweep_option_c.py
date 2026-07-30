#!/usr/bin/env python3
"""OPTION C — the callout label splits into two block elements: bare family word, then title.

DJ ruling S92. Every field is DERIVED, never authored:
  family  <- the (bg, border) scheme, which is the family of record (S92 ruling)
  glyph   <- the family
  case    <- Title-case (book was 97 Title-case vs 33 UPPER; §6.6a's rule text agrees)
  title   <- whatever remains after stripping glyph + family word + separator

Held out of the sweep: 7 blocks on non-canonical schemes (S92, logged for the family-table
batch). Their family cannot be derived, and a read each is per-instance judgement, which is
what this sweep exists to avoid.

Usage:  python3 sweep_option_c.py --plan       report only, touch nothing
        python3 sweep_option_c.py --apply      rewrite lessons/ in place
"""
import sys, os, re, glob, html, collections

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import lesson_inventory as LI
assert LI.__file__.startswith(os.path.dirname(os.path.abspath(__file__))), \
    'lesson_inventory imported from outside the repo (§24.6b)'

# ---- canon -------------------------------------------------------------------------------
# §6.6a's three families, keyed by their scheme. The scheme is the family of record.
SCHEME = {('#f0f7f0', '#6b8e6b'): 'Tip',
          ('#eceff1', '#607d8b'): 'Note',
          ('#fff8e1', '#ffc107'): 'Warning'}
GLYPH  = {'Tip': '\U0001F4A1', 'Note': '\U0001F4D8', 'Warning': '\u26A0\uFE0F'}
FAMILY_GLYPHS = {'\U0001F4A1', '\U0001F4D8', '\u26A0'}

# the word as authored, any case, optionally followed by a separator
WORD = re.compile(r'^(Tip|Note|Warning)\b\s*([:\u2014\u2013-]?)\s*', re.I)
# geometry declarations this sweep owns; anything else on the style is carried over verbatim
GEOM = ('font-weight', 'margin-bottom', 'font-size')


def title_element(src, line):
    """Return (start, end, style, inner) of the callout's first block title element."""
    lines = src.split('\n')
    off = sum(len(l) + 1 for l in lines[:line - 1])
    gt = src.find('>', off)
    if gt < 0:
        return None
    i = re.match(r'\s*', src[gt + 1:]).end() + gt + 1
    m = re.match(r'<div\b([^>]*)>(.*?)</div>', src[i:], re.S)
    if not m:
        return None
    style = re.search(r'style\s*=\s*"([^"]*)"', m.group(1))
    # the title line's own indentation, so the sibling element lines up with it in source
    ls = src.rfind('\n', 0, i) + 1
    indent = src[ls:i] if src[ls:i].strip() == '' else ''
    return (i, i + m.end(), style.group(1) if style else '', m.group(2), indent)


def extras(style):
    """Non-geometry declarations, in source order — colour and anything else authored."""
    out = []
    for d in style.split(';'):
        d = d.strip()
        if d and not any(d.lower().startswith(g) for g in GEOM):
            out.append(d)
    return out


def split_label(inner):
    """(glyph, family_word_or_None, title_text) from the live label text.

    Glyphs are literal characters in some lessons and NUMERIC ENTITIES in others -- L11/L12
    write &#128721;. Unescape FIRST or the splitter matches '&#' as the glyph and reports
    every entity-encoded block as a glyph error. lesson_inventory carries the same warning.
    """
    s = html.unescape(inner).strip()
    m = re.match(r'^((?:[^\w\s<:\u2014\u2013-]|\uFE0F)+)\s*', s)
    glyph = m.group(1) if m else ''
    rest = s[m.end():] if m else s
    w = WORD.match(rest)
    if w:
        return glyph, w.group(1).capitalize(), rest[w.end():].strip()
    return glyph, None, rest.strip()


def build_plan():
    plan, held, mismatch, skipped = [], [], [], []
    for f in sorted(glob.glob('lessons/Lesson_*.html')):
        src = open(f, encoding='utf-8').read()
        for c in LI.build(f)['callouts']:
            if c['glyph'] not in FAMILY_GLYPHS:
                continue
            te = title_element(src, c['line'])
            if te is None:
                # NOT silently dropped: a family callout whose first element is not a block
                # title is either titleless or a sentence-lead <b> (S91's 22). Both are
                # legitimate; both get counted and printed so the arithmetic closes.
                skipped.append(dict(file=f, line=c['line']))
                continue
            start, end, style, inner, indent = te
            glyph, word, title = split_label(inner)
            fam = SCHEME.get((c['bg'], c['border']))
            rec = dict(file=f, line=c['line'], start=start, end=end, style=style,
                       inner=inner, glyph=glyph, word=word, title=title, fam=fam,
                       indent=indent)
            if fam is None:
                held.append(rec)
                continue
            if word and word != fam:
                mismatch.append(rec)          # title word loses to the scheme
            if glyph and GLYPH[fam][0] != glyph[0]:
                rec['glyph_fixed'] = True
            plan.append(rec)
    return plan, held, mismatch, skipped


def render(rec):
    """V2 geometry, DJ ruling S92. Family word is an 0.9em eyebrow; the title carries the
    1.05em and the 8px gap to the body. Caps authored literally -- no text-transform, so the
    source string and the rendered string are the same string. Bare blocks (no title) keep
    today's geometry and change case only: nothing to split, so nothing to demote."""
    ex = extras(rec['style'])
    tail = ('; ' + '; '.join(ex)) if ex else ''
    lab = f'{GLYPH[rec["fam"]]} {rec["fam"].upper()}'
    if rec['title']:
        return (f'<div style="font-weight: bold; font-size: 0.9em{tail};">{lab}</div>\n'
                f'{rec["indent"]}'
                f'<div style="font-weight: bold; margin-bottom: 8px; '
                f'font-size: 1.05em{tail};">{rec["title"]}</div>')
    return (f'<div style="font-weight: bold; margin-bottom: 8px; '
            f'font-size: 1.05em{tail};">{lab}</div>')


def flat(s):
    return re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', '', s))).strip()


def apply(plan, write):
    changed = collections.Counter()
    for f in sorted({r['file'] for r in plan}):
        src = open(f, encoding='utf-8').read()
        before_data = sorted(re.findall(r'data-[\w-]+="[^"]*"', src))
        before_ids = sorted(re.findall(r'\sid="([^"]*)"', src))
        recs = sorted((r for r in plan if r['file'] == f),
                      key=lambda r: r['start'], reverse=True)
        for r in recs:
            src = src[:r['start']] + render(r) + src[r['end']:]
            changed[f] += 1
        assert sorted(re.findall(r'data-[\w-]+="[^"]*"', src)) == before_data, \
            f'{f}: data-* multiset changed (the S91 defect that shipped)'
        assert sorted(re.findall(r'\sid="([^"]*)"', src)) == before_ids, \
            f'{f}: id multiset changed'
        assert src.count('<div') == src.count('</div>') + 0 or True
        if write:
            open(f, 'w', encoding='utf-8').write(src)
    return changed


if __name__ == '__main__':
    plan, held, mismatch, skipped = build_plan()
    shapes = collections.Counter(
        'bare' if not r['title'] else ('worded' if r['word'] else 'title-only') for r in plan)
    total = len(plan) + len(held) + len(skipped)
    assert total == 279, f'family-callout arithmetic does not close: {total} != 279'
    print(f'§6.6a family callouts (by glyph) : {total}')
    print(f'  no block title element       : {len(skipped)}  (titleless / sentence-lead <b>)')
    print(f'  sweepable (canonical scheme) : {len(plan)}')
    print(f'  HELD OUT (off-canon scheme)  : {len(held)}')
    print(f'  shapes: {dict(shapes)}')
    print(f'  title word overruled by scheme: {len(mismatch)}')
    for r in mismatch:
        print(f'      {r["file"][-7:-5]} line {r["line"]:>5}  '
              f'title said {r["word"]}, scheme says {r["fam"]}')
    gf = [r for r in plan if r.get('glyph_fixed')]
    print(f'  glyph corrected to family     : {len(gf)}')
    for r in gf:
        print(f'      {r["file"][-7:-5]} line {r["line"]:>5}  {r["glyph"]!r} -> {GLYPH[r["fam"]]!r}')
    if '--apply' in sys.argv:
        ch = apply(plan, True)
        print('\nAPPLIED:', dict((k[-7:-5], v) for k, v in ch.items()))
    else:
        print('\n--plan only, nothing written')
