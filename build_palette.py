#!/usr/bin/env python3
"""build_palette.py v1.0 — the ruled palette is DERIVED, never typed.

Entrypoint is build() — not palette(), not main().     (S110)

The H2 palette ruled in S110 comes from RoboLore Heritage canon by a stated
transform. Nothing here contains a band hex; every one is computed, floor-checked
against WCAG 4.5:1, and emitted. `--check` re-derives and compares against the
table published in ZUMO_S110_VISUAL_RULING.md, so the document cannot drift away
from the generator the way a hand-typed list would.

  python3 build_palette.py --selftest      six controls, loud on a real defect
  python3 build_palette.py --check         does the ruling doc match the derivation
  python3 build_palette.py --emit          print the markdown table
  python3 build_palette.py --css           print the CSS custom properties
"""
import math, re, sys, os

VERSION = 'v1.0'

# ---------------------------------------------------------------- canon INPUTS
# RoboLore Heritage Blue, DJ-stated, Bible §26.4 item 1. These five plus Forge
# Red are the ONLY colour literals in this file that are not derived.
CANON = {
    'Deep Navy':      '#0B1A2E',
    'Slate Blue':     '#3D5266',
    'Antique Bronze': '#7B6240',
    'Warm Brass':     '#C9A463',
    'Parchment':      '#F5F2E9',
}
FORGE_RED = '#D46554'          # sixth palette colour, §26.4, DJ-named
WARNING = ('#C0392B', '#FCEBE9', '#5C1A13')   # never reassigned, §26 / S109
BODY_TEXT = '#1D1D1F'
CODE_PANEL = '#1E1E1E'         # §22, the editor background
FLOOR = 4.5

# ------------------------------------------------------- the ruled transform
# S110: bands are canon colours re-lit. Six groups out of two hue families means
# the six separate by LIGHTNESS, not hue — §5.0.1's ramp principle.
GROUPS = ['Theory & Concepts', 'Hardware & Code', 'Testing',
          'Troubleshoot', 'Challenges', 'Wrap Up & Reference']
SOURCE = {
    'Theory & Concepts':   ('Deep Navy',        CANON['Deep Navy']),
    'Hardware & Code':     ('Antique Bronze',   CANON['Antique Bronze']),
    'Testing':             ('Slate Blue',       CANON['Slate Blue']),
    'Troubleshoot':        ('Forge Red',        FORGE_RED),
    'Challenges':          ('Warm Brass',       CANON['Warm Brass']),
    'Wrap Up & Reference': ('Deep Navy +18\u00b0', CANON['Deep Navy']),
}
BAND_L0, BAND_STEP, BAND_CX = 35.0, 4.6, 0.62
TINT_L, TINT_CX = 93.5, 0.32
TEXT_L, TEXT_CX = 31.0, 0.80
WRAP_HUE_SHIFT = 18.0          # keeps Wrap Up off Theory; see ruling §3

PAGE = CANON['Parchment']
HEADINGS = CANON['Antique Bronze']
CAP_TEXT = '#FFFFFF'

# ---------------------------------------------------------------- colour maths
def _lin(c):
    c /= 255.0
    return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4

def _unlin(c):
    c = 12.92 * c if c <= 0.0031308 else 1.055 * (c ** (1 / 2.4)) - 0.055
    return max(0, min(255, round(c * 255)))

def luminance(rgb):
    r, g, b = (_lin(v) for v in rgb)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b

def contrast(a, b):
    la, lb = luminance(a), luminance(b)
    return (max(la, lb) + 0.05) / (min(la, lb) + 0.05)

def hex_to_rgb(h):
    h = h.lstrip('#')
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))

def rgb_to_hex(rgb):
    return '#%02X%02X%02X' % tuple(rgb)

_WP = (0.95047, 1.0, 1.08883)

def _f(t):
    return t ** (1 / 3) if t > 216 / 24389 else (841 / 108) * t + 4 / 29

def _fi(t):
    return t ** 3 if t ** 3 > 216 / 24389 else (t - 4 / 29) * 108 / 841

def rgb_to_lab(rgb):
    r, g, b = (_lin(v) for v in rgb)
    x = r * .4124564 + g * .3575761 + b * .1804375
    y = r * .2126729 + g * .7151522 + b * .0721750
    z = r * .0193339 + g * .1191920 + b * .9503041
    fx, fy, fz = _f(x / _WP[0]), _f(y / _WP[1]), _f(z / _WP[2])
    return (116 * fy - 16, 500 * (fx - fy), 200 * (fy - fz))

def lab_to_rgb(lab):
    L, a, b = lab
    fy = (L + 16) / 116
    fx, fz = fy + a / 500, fy - b / 200
    x, y, z = _WP[0] * _fi(fx), _WP[1] * _fi(fy), _WP[2] * _fi(fz)
    r = x * 3.2404542 + y * -1.5371385 + z * -.4985314
    g = x * -.9692660 + y * 1.8760108 + z * .0415560
    bb = x * .0556434 + y * -.2040259 + z * 1.0572252
    return tuple(_unlin(v) for v in (r, g, bb))

def rgb_to_lch(rgb):
    L, a, b = rgb_to_lab(rgb)
    return L, math.hypot(a, b), math.degrees(math.atan2(b, a)) % 360

def lch_to_rgb(L, C, h):
    r = math.radians(h)
    return lab_to_rgb((L, C * math.cos(r), C * math.sin(r)))

def de76(a, b):
    return math.dist(rgb_to_lab(a), rgb_to_lab(b))

def hue_gap(a, b):
    d = abs(a - b) % 360
    return min(d, 360 - d)

# --------------------------------------------------------------- THE ENTRYPOINT
def build(wrap_shift=WRAP_HUE_SHIFT, band_l0=BAND_L0, floor=FLOOR):
    """Derive the ruled palette. Returns an ordered list of dicts, one per group.
    Parameters exist so the selftest can perturb the transform; production callers
    pass nothing."""
    out = []
    for i, g in enumerate(GROUPS):
        label, src = SOURCE[g]
        L, C, h = rgb_to_lch(hex_to_rgb(src))
        if g == 'Wrap Up & Reference':
            h = (h + wrap_shift) % 360
        chroma = max(6.0, C * BAND_CX)
        band = None
        target = band_l0 + (i - 2.5) * BAND_STEP
        for step in range(600):                      # darken until the floor is met
            cand = lch_to_rgb(target - step * 0.25, chroma, h)
            if contrast(cand, hex_to_rgb(CAP_TEXT)) >= floor:
                band = cand
                break
        if band is None:
            raise AssertionError('no band clears the floor for %s' % g)
        tint = lch_to_rgb(TINT_L, max(3.0, C * BAND_CX * TINT_CX), h)
        text = None
        for step in range(600):
            cand = lch_to_rgb(TEXT_L - step * 0.25, max(7.0, C * BAND_CX * TEXT_CX), h)
            if contrast(cand, tint) >= floor:
                text = cand
                break
        if text is None:
            raise AssertionError('no callout text clears the floor for %s' % g)
        out.append(dict(group=g, source=label, band=rgb_to_hex(band),
                        tint=rgb_to_hex(tint), text=rgb_to_hex(text),
                        cap_contrast=contrast(band, hex_to_rgb(CAP_TEXT)),
                        text_contrast=contrast(text, tint)))
    return out


def metrics(pal):
    bands = [hex_to_rgb(p['band']) for p in pal]
    canon_hues = [rgb_to_lch(hex_to_rgb(v))[2] for k, v in CANON.items()
                  if k != 'Parchment']
    gaps = [min(hue_gap(rgb_to_lch(b)[2], ch) for ch in canon_hues) for b in bands]
    return dict(
        cap_floor=min(p['cap_contrast'] for p in pal),
        text_floor=min(p['text_contrast'] for p in pal),
        body=contrast(hex_to_rgb(BODY_TEXT), hex_to_rgb(PAGE)),
        headings=contrast(hex_to_rgb(HEADINGS), hex_to_rgb(PAGE)),
        band_sep=min(de76(a, b) for i, a in enumerate(bands) for b in bands[i + 1:]),
        warn_sep=min(de76(hex_to_rgb(WARNING[0]), b) for b in bands),
        code_sep=min(de76(b, hex_to_rgb(CODE_PANEL)) for b in bands),
        chroma=sum(rgb_to_lch(b)[1] for b in bands) / len(bands),
        hue_gap=sum(gaps) / len(gaps),
        within20=sum(1 for x in gaps if x <= 20),
    )


def verify(pal, floor=FLOOR):
    """Every pair a reader actually sees. Raises on the first failure."""
    for p in pal:
        assert p['cap_contrast'] >= floor, ('cap', p['group'], p['cap_contrast'])
        assert p['text_contrast'] >= floor, ('text', p['group'], p['text_contrast'])
    m = metrics(pal)
    assert m['body'] >= floor, ('body', m['body'])
    assert m['headings'] >= floor, ('headings', m['headings'])
    assert contrast(hex_to_rgb(WARNING[2]), hex_to_rgb(WARNING[1])) >= floor, 'warning'
    return m


def emit_markdown(pal):
    rows = ['| group | canon source | band | white on band | tint | text | text on tint |',
            '|---|---|---|---:|---|---|---:|']
    for p in pal:
        rows.append('| %s | %s | `%s` | %.2f | `%s` | `%s` | %.2f |'
                    % (p['group'], p['source'], p['band'], p['cap_contrast'],
                       p['tint'], p['text'], p['text_contrast']))
    return '\n'.join(rows)


def emit_css(pal):
    def slug(g):
        return re.sub(r'[^a-z0-9]+', '-', g.lower()).strip('-')
    lines = [':root {', '  /* generated by build_palette.py %s - do not hand-edit */' % VERSION,
             '  --page: %s;' % PAGE, '  --body: %s;' % BODY_TEXT,
             '  --heading: %s;' % HEADINGS, '  --cap-text: %s;' % CAP_TEXT,
             '  --warn-band: %s;' % WARNING[0], '  --warn-tint: %s;' % WARNING[1],
             '  --warn-text: %s;' % WARNING[2]]
    for p in pal:
        s = slug(p['group'])
        lines += ['  --%s-band: %s;' % (s, p['band']),
                  '  --%s-tint: %s;' % (s, p['tint']),
                  '  --%s-text: %s;' % (s, p['text'])]
    lines.append('}')
    return '\n'.join(lines)

# ------------------------------------------------------------------- the check
RULING = 'ZUMO_S110_VISUAL_RULING.md'

def check(path=RULING):
    """Re-derive and compare against the table published in the ruling document.
    A published palette that no longer matches its generator is the hand-typed
    list this instrument exists to prevent (§24.13)."""
    if not os.path.exists(path):
        return ['%s not found' % path]
    doc = open(path, encoding='utf-8').read()
    pal = build()
    bad = []
    for p in pal:
        row = [l for l in doc.splitlines()
               if l.startswith('| ' + p['group'] + ' |')]
        if not row:
            bad.append('%s: no row in %s' % (p['group'], path))
            continue
        hexes = re.findall(r'`(#[0-9A-Fa-f]{6})`', row[0])
        want = [p['band'], p['tint'], p['text']]
        if [h.upper() for h in hexes] != want:
            bad.append('%s: doc %s  derived %s' % (p['group'], hexes, want))
    for name, val in (('page', PAGE), ('headings', HEADINGS)):
        if val.lower() not in doc.lower():
            bad.append('%s %s absent from %s' % (name, val, path))
    return bad

# ---------------------------------------------------------------- the selftest
def selftest():
    ok = True

    def report(label, passed, detail=''):
        nonlocal ok
        ok = ok and passed
        print('   %-5s %s%s' % ('OK' if passed else 'FAIL', label,
                                ('  ' + detail) if detail else ''))

    print('CONTROL A (known answer from ANOTHER artefact): ColorPalette.md STATES')
    print('  Deep Navy on Parchment at 15.61:1 - this file cannot supply that number.')
    print('  (Bible §26.2 quotes 13.37 for the SUPERSEDED BookComponentStandard hexes,')
    print('   not for canon; expecting 13.37 here was a misreading and this control')
    print('   caught it before the palette shipped.)')
    got = contrast(hex_to_rgb(CANON['Deep Navy']), hex_to_rgb(CANON['Parchment']))
    report('navy/parchment reproduces the stated 15.61', abs(got - 15.61) < 0.01, '%.4f' % got)

    print('CONTROL B (round trip): Lab conversion is lossless to 1 of 255')
    worst = max(max(abs(a - b) for a, b in zip(c, lab_to_rgb(rgb_to_lab(c))))
                for c in [hex_to_rgb(v) for v in CANON.values()] + [(0, 0, 0), (255, 255, 255)])
    report('sRGB -> Lab -> sRGB', worst <= 1, 'worst channel drift %d' % worst)

    print('CONTROL C (the floor search is REACHABLE): raising the floor to 12:1 must')
    print('  darken every band. NOTE THE MEASURED PROPERTY: at the ruled floor of 4.5')
    print('  the search binds on NOTHING - the bands are positioned by the ruling and')
    print('  clear the floor with headroom, so the floor is a guard and not a shaper.')
    print('  That is the opposite of specimen D1, where the floor set the colours.')
    strict, hard = build(), build(floor=12.0)
    n_hard = sum(a['band'] != b['band'] for a, b in zip(strict, hard))
    n_ruled = sum(a['band'] != b['band'] for a, b in zip(strict, build(floor=1.0)))
    report('floor 12 moves all six, floor 4.5 moves none',
           n_hard == 6 and n_ruled == 0,
           'at 12:1 %d of 6 move, at the ruled 4.5 the search binds on %d' % (n_hard, n_ruled))

    print('CONTROL D (the shift is LIVE, not a dead constant): zeroing WRAP_HUE_SHIFT')
    print('  must change the Wrap Up BAND HEX. Tested on the hex, not on band')
    print('  separation - separation here is carried by LIGHTNESS, so it barely moves')
    print('  when the hue does, and testing it would have passed a dead constant.')
    z = build(wrap_shift=0.0)
    a_rgb, z_rgb = hex_to_rgb(strict[5]['band']), hex_to_rgb(z[5]['band'])
    t_rgb = hex_to_rgb(strict[0]['band'])
    report('zeroing the shift changes the Wrap Up band',
           strict[5]['band'] != z[5]['band'],
           '%s -> %s' % (strict[5]['band'], z[5]['band']))
    print('        what the shift BUYS, measured: Theory-vs-WrapUp \u0394E76 %.1f with it,'
          % de76(t_rgb, a_rgb))
    print('        %.1f without. Separation is carried by lightness, not by this hue.'
          % de76(t_rgb, z_rgb))

    print('CONTROL E (the alignment measure can say NO): warm earth, the palette')
    print('  this one replaced, must NOT score as Heritage-aligned')
    warm = ['#844A31', '#6D572A', '#48602B', '#A34A32', '#2E615D', '#824664']
    canon_hues = [rgb_to_lch(hex_to_rgb(v))[2] for k, v in CANON.items() if k != 'Parchment']
    w = sum(1 for b in warm
            if min(hue_gap(rgb_to_lch(hex_to_rgb(b))[2], c) for c in canon_hues) <= 20)
    r = metrics(strict)['within20']
    report('warm earth 1/6, ruled palette 5/6', w == 1 and r == 5,
           'warm %d/6  ruled %d/6' % (w, r))

    print('CONTROL F (determinism): a SECOND derivation emits identical bytes')
    report('two runs agree', emit_markdown(build()) == emit_markdown(build()))

    print('CONTROL G (the check can FAIL): a doctored table must be REPORTED')
    import tempfile
    doc = emit_markdown(strict).replace(strict[0]['band'], '#ABCDEF', 1)
    doc += '\n%s %s\n' % (PAGE, HEADINGS)
    with tempfile.NamedTemporaryFile('w', suffix='.md', delete=False) as f:
        f.write(doc)
        tmp = f.name
    caught = bool(check(tmp))
    clean = emit_markdown(strict) + '\n%s %s\n' % (PAGE, HEADINGS)
    with tempfile.NamedTemporaryFile('w', suffix='.md', delete=False) as f:
        f.write(clean)
        tmp2 = f.name
    silent = not check(tmp2)
    os.unlink(tmp); os.unlink(tmp2)
    report('doctored table reported, clean table silent', caught and silent)

    print('CONTROL H (verify() actually gates): a palette below the floor must RAISE')
    raised = False
    try:
        bad = build()
        bad[0]['cap_contrast'] = 3.9
        verify(bad)
    except AssertionError:
        raised = True
    report('verify raises on a sub-floor pair', raised)

    print('\n%s' % ('ALL CONTROLS PASS - loud on five planted defects, silent when clean.'
                    if ok else 'CONTROLS FAILED'))
    return 0 if ok else 1


def main():
    args = sys.argv[1:]
    if '--selftest' in args:
        return selftest()
    pal = build()
    m = verify(pal)
    if '--emit' in args:
        print(emit_markdown(pal))
        return 0
    if '--css' in args:
        print(emit_css(pal))
        return 0
    if '--check' in args:
        bad = check()
        if bad:
            print('PALETTE DRIFT - %s does not match the derivation:' % RULING)
            for b in bad:
                print('  ' + b)
            return 1
        print('%s matches the derivation (6 groups, 18 hexes)' % RULING)
        return 0
    print('build_palette.py %s - the ruled palette, derived from Heritage canon\n' % VERSION)
    print(emit_markdown(pal))
    print('\npage %s   body %s (%.2f)   headings %s (%.2f)   cap text %s'
          % (PAGE, BODY_TEXT, m['body'], HEADINGS, m['headings'], CAP_TEXT))
    print('white-on-band floor %.2f   text-on-tint floor %.2f' % (m['cap_floor'], m['text_floor']))
    print('band separation dE76 %.1f   nearest band to WARNING %.1f   vs code panel %.1f'
          % (m['band_sep'], m['warn_sep'], m['code_sep']))
    print('mean chroma C* %.1f   mean hue gap to canon %.1f deg   within 20 deg %d/6'
          % (m['chroma'], m['hue_gap'], m['within20']))
    print('\n  --selftest   --check   --emit   --css')
    return 0


if __name__ == '__main__':
    sys.exit(main())
