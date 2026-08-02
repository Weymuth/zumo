#!/usr/bin/env python3
"""strip_inline.py - convert a lesson's inline style="" attributes into class="" against
the generated css/book.css, and restore them again.

WHY THIS EXISTS. S104 converted Lesson 01 by hand and did not commit the tool, so the
15-lesson pass had nothing to run. This is that tool, written once and controlled, because
a hand conversion repeated fifteen times is fifteen chances to differ.

READ THIS BEFORE WIDENING build_css.SOURCES. build_css names rules by frequency ACROSS the
corpus, so widening SOURCES renames them: at S105, 46 of L01's 167 names kept their spelling
and changed their MEANING, and 11 disappeared. Only the 11 were visible to gate 41 - the 46
resolve to a rule, so every gate stays green while the page silently repaints.

AND THE ORDER MATTERS, because the wrong one destroys information. expand_classes reads the
stylesheet FROM DISK and leaves an unresolvable class untouched rather than failing. Once a
regenerated book.css no longer defines a name, every element carrying it is unrecoverable -
at S105 that was 74 elements in L01. So:

    1. --restore every ALREADY-CONVERTED lesson   (old book.css still on disk)
    2. python3 build_css.py                       (regenerate from inline sources)
    3. --apply every lesson                       (against the new map)

Step 1 is not optional and is not a rollback. It is how the conversion is made re-runnable.

THE HOLD. Four block types are compared BYTE-EXACT ACROSS LESSONS by gates §6.5a, §25.6 and
§6.8, and are converted book-wide in a separate generated pass, not here. Converting them one
lesson at a time is exactly what those gates exist to catch. Located by marker, never offset:

  strip   <!-- LESSON STRIP v.. -->  ...  <!-- /LESSON STRIP -->
  hero    the innermost <div> enclosing the "LESSON NN" label and its dated Version line
  footer  the <p> carrying the RoboLore credits line
  PART    each §6.8 divider block, matched whole

NOTHING IS EVER INVENTED. Every replacement comes from build_css's map; an attribute whose
declarations have no rule is LEFT ALONE and REPORTED. Silence is not success: --plan prints
what it could not convert, and a non-zero unmapped count is exit 1.

usage:
  python3 strip_inline.py --plan    [files...]   report, write nothing
  python3 strip_inline.py --apply   [files...]   style="" -> class="" (atomic)
  python3 strip_inline.py --restore [files...]   class="" -> style="" (atomic, step 1)
  python3 strip_inline.py --verify  [files...]   every class in the file resolves to a rule
  python3 strip_inline.py --selftest            controls, both directions
exit 0 = clean. exit 1 = a control failed, or an attribute had no rule, or a class is dead.
"""
import re, os, sys, glob, collections

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import lesson_inventory as LI
import build_css as BC

VERSION = 'v1.0'          # the only version home in this file (S105)

LESSONS = sorted(glob.glob('lessons/Lesson_*.html'))
LINK = '<link rel="stylesheet" href="../css/book.css">'

_STYLE = re.compile(r'\sstyle="([^"]*)"')
_CLASS = re.compile(r'\sclass="([^"]*)"')
_STRIP = re.compile(r'<!-- LESSON STRIP v[^>]*?-->.*?<!-- /LESSON STRIP -->', re.S)
_PART = re.compile(
    r'<div style="background-color: #[0-9a-fA-F]{6}; color: white; padding: 12px 20px; '
    r'border-radius: 8px 8px 0 0; margin: 22px 0 0;">\s*'
    r'<div style="font-size: 18px[^"]*">PART (\d+)[^<]*</div>\s*'
    r'<div style="font-size: 12px[^"]*">[^<]*</div>\s*</div>', re.S)


def _close_of(s, st, tag):
    """End offset of the tag opened at st, by depth. Mirrors book_gates §25.6."""
    d = 0
    for m in re.finditer(rf'<{tag}\b|</{tag}>', s[st:]):
        d += 1 if m.group(0) != f'</{tag}>' else -1
        if d == 0:
            return st + m.end()
    return -1


def held_spans(s, label):
    """-> sorted [(start, end)] the strip must not touch. Located by marker only."""
    spans = []
    m = _STRIP.search(s)
    if m:
        spans.append((m.start(), m.end()))
    lm = re.search(r'>\s*' + re.escape(label) + r'\s*<', s)
    if lm:
        v = re.search(r'Version \d+\.\d+ &mdash; \w+ \d{4}', s[lm.start():lm.start() + 2500])
        if v:
            vpos = lm.start() + v.start()
            st = lm.start()
            while True:
                st = s.rfind('<div', 0, st)
                if st < 0:
                    break
                en = _close_of(s, st, 'div')
                if en > vpos:
                    spans.append((st, en))
                    break
    i = s.find('&copy; 2026 RoboLore')
    if i >= 0:
        spans.append((s.rfind('<p', 0, i), s.find('</p>', i) + 4))
    for m in _PART.finditer(s):
        spans.append((m.start(), m.end()))
    return sorted(spans)


def _in(spans, pos):
    return any(a <= pos < b for a, b in spans)


def convert(src, label, name_of):
    """-> (text, converted, held, unmapped). Value-only; nothing else moves."""
    s = LI.expand_classes(src)
    spans = held_spans(s, label)
    conv = held = 0
    unmapped = []

    def one(m):
        nonlocal conv, held
        if _in(spans, m.start()):
            held += 1
            return m.group(0)
        c = BC.canon(m.group(1))
        cls = name_of.get(c)
        if cls is None:
            unmapped.append(c)
            return m.group(0)
        conv += 1
        return f' class="{cls}"'

    return _STYLE.sub(one, s), conv, held, unmapped


def dead_classes(src, css=None):
    """-> sorted list of class names in src that resolve to no rule. The ordering trap:
    expand_classes leaves these untouched, so they are silent everywhere but gate 41."""
    css = LI.load_css() if css is None else css
    return sorted({c for m in _CLASS.finditer(src) for c in m.group(1).split()
                   if c not in css})


def link(s):
    """Ensure exactly one stylesheet <link>, placed as L01 places it: before </head>."""
    if LINK in s:
        return s
    i = s.find('</head>')
    return s if i < 0 else s[:i] + LINK + '\n' + s[i:]


def label_of(path):
    m = re.search(r'Lesson_(\d+)', path)
    return 'LESSON ' + m.group(1) if m else ''


def build(paths=None):
    """ENTRYPOINT. -> {path: (text, converted, held, unmapped)}. Writes nothing."""
    paths = paths or LESSONS
    _, _, chosen = BC.build(BC.SOURCES)
    out = {}
    for p in paths:
        src = open(p, encoding='utf-8').read()
        t, c, h, u = convert(src, label_of(p), chosen)
        out[p] = (link(t), c, h, u)
    return out


def _write(p, text):
    tmp = p + '.tmp'
    with open(tmp, 'w', encoding='utf-8') as fh:
        fh.write(text)
    os.replace(tmp, p)


# ----------------------------------------------------------------- controls
def selftest():
    ok = True

    def check(label, got, want):
        nonlocal ok
        good = got == want
        ok &= good
        print(f"   {'OK  ' if good else 'FAIL'}  {label}")
        if not good:
            print(f"          got  {got!r}\n          want {want!r}")

    NAMES = {'color: red': 'tok-red', 'font-weight: bold': 'b'}
    CSS = {'tok-red': 'color: red', 'b': 'font-weight: bold'}

    print('CONTROL A (round trip): expanding the output must restore the input')
    src = '<p style="color: red">x</p><b style="font-weight: bold">y</b>'
    out, c, h, u = convert(src, 'LESSON 01', NAMES)
    check('A: both converted', (c, h, u), (2, 0, []))
    check('A: expansion restores every declaration',
          [BC.canon(v) for v in _STYLE.findall(LI.expand_classes(out, CSS))],
          ['color: red', 'font-weight: bold'])
    check('A: visible text is untouched',
          re.sub(r'<[^>]*>', '', out), re.sub(r'<[^>]*>', '', src))

    print('CONTROL B (the hold): a held block is left byte-identical')
    strip = '<!-- LESSON STRIP v1 --><a style="color: red">L1</a><!-- /LESSON STRIP -->'
    part = ('<div style="background-color: #3498db; color: white; padding: 12px 20px; '
            'border-radius: 8px 8px 0 0; margin: 22px 0 0;">'
            '<div style="font-size: 18px; font-weight: 500;">PART 1 &mdash; T</div>'
            '<div style="font-size: 12px; color: #fff;">S</div></div>')
    foot = '<p style="color: red">&copy; 2026 RoboLore</p>'
    body = strip + '<p style="color: red">free</p>' + part + foot
    out_b, c_b, h_b, _ = convert(body, 'LESSON 01', NAMES)
    check('B: exactly one attribute converted, five held', (c_b, h_b), (1, 5))
    for name, block in (('strip', strip), ('PART divider', part), ('footer', foot)):
        check(f'B: {name} survives byte-identical', block in out_b, True)

    print('CONTROL C (no rule = no change): an unmapped block is reported, not dropped')
    out_c, c_c, _, u_c = convert('<p style="color: lime">x</p>', 'LESSON 01', NAMES)
    check('C: nothing converted', c_c, 0)
    check('C: the attribute is still there', 'style="color: lime"' in out_c, True)
    check('C: and it is reported', u_c, ['color: lime'])

    print('CONTROL D (idempotence): a second pass over converted text is a no-op')
    twice, c_d, _, _ = convert(LI.expand_classes(out, CSS), 'LESSON 01', NAMES)
    check('D: same bytes, same count', (twice, c_d), (out, 2))

    print('CONTROL E (the link): added once, never twice')
    once = link('<head><title>t</title></head><body></body>')
    check('E: link inserted before </head>', once.count(LINK), 1)
    check('E: a second call adds nothing', link(once), once)

    print('CONTROL F (loud on a real change): a wrong map must be visible')
    out_f, _, _, _ = convert(src, 'LESSON 01', {'color: red': 'WRONG',
                                                'font-weight: bold': 'b'})
    check('F: a different map yields different bytes', out_f != out, True)

    print('CONTROL G (the ORDERING trap): a class the stylesheet dropped must be REPORTED,')
    print('          because expand_classes silently leaves it in place')
    orphan = '<p class="tok-red">a</p><p class="gone-2">b</p>'
    check('G: expansion leaves the dead class untouched, unflagged',
          'class="gone-2"' in LI.expand_classes(orphan, CSS), True)
    check('G: dead_classes names it', dead_classes(orphan, CSS), ['gone-2'])
    check('G: and does not cry wolf on a live one',
          dead_classes('<p class="tok-red">a</p>', CSS), [])

    print('CONTROL H (the hold is derived, not counted): L01 lives and holds 39')
    if os.path.exists('lessons/Lesson_01.html'):
        s = LI.expand_classes(open('lessons/Lesson_01.html', encoding='utf-8').read())
        spans = held_spans(s, 'LESSON 01')
        n = sum(1 for m in _STYLE.finditer(s) if _in(spans, m.start()))
        check("H: the locators find L01's 39 held attributes", n, 39)
    else:
        print('   SKIP  no lessons/ in cwd')

    print('\n' + ('ALL CONTROLS PASS - loud on a wrong map and a dead class, '
                  'silent on a held block.' if ok else '*** CONTROLS FAILED ***'))
    return 0 if ok else 1


def main(argv):
    if '--selftest' in argv:
        return selftest()
    paths = [a for a in argv[1:] if not a.startswith('-')] or LESSONS

    if '--verify' in argv:
        css = LI.load_css()
        bad = 0
        print(f'strip_inline {VERSION}   mode: VERIFY   {len(paths)} file(s)\n')
        for p in paths:
            d = dead_classes(open(p, encoding='utf-8').read(), css)
            bad += len(d)
            print(f'  {os.path.basename(p):26} {len(d):3} dead'
                  + (f'   {d[:5]}' if d else ''))
        print(f'\n  {bad} dead class name(s)')
        return 1 if bad else 0

    if '--restore' in argv:
        print(f'strip_inline {VERSION}   mode: RESTORE   {len(paths)} file(s)\n')
        bad = 0
        for p in paths:
            src = open(p, encoding='utf-8').read()
            d = dead_classes(src)
            bad += len(d)
            out = LI.expand_classes(src)
            n = len(_CLASS.findall(src)) - len(_CLASS.findall(out))
            print(f'  {os.path.basename(p):26} {n:5} class -> style'
                  + (f'   *** {len(d)} DEAD, NOT RESTORED: {d[:4]}' if d else ''))
            _write(p, out)
        print(f'\n  {bad} class name(s) could not be restored')
        return 1 if bad else 0

    apply = '--apply' in argv
    res = build(paths)
    print(f'strip_inline {VERSION}   mode: {"APPLY" if apply else "PLAN"}   '
          f'{len(paths)} file(s)\n')
    print(f'  {"file":26} {"convert":>8} {"held":>6} {"unmapped":>9}   bytes')
    tot = collections.Counter()
    bad = 0
    for p in paths:
        text, c, h, u = res[p]
        before = os.path.getsize(p)
        tot['c'] += c
        tot['h'] += h
        bad += len(u)
        print(f'  {os.path.basename(p):26} {c:8} {h:6} {len(u):9}   '
              f'{before:,} -> {len(text.encode()):,}')
        for d in sorted(set(u))[:4]:
            print(f'      NO RULE: {d[:88]}')
        if apply:
            _write(p, text)
    print(f'\n  {tot["c"]:,} converted   {tot["h"]} held   {bad} unmapped')
    return 1 if bad else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
