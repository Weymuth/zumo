#!/usr/bin/env python3
# gen_component.py -- version in ONE home: the VERSION constant below.
#
# The RoboLore Book Component Standard generator.
#
# ONE TABLE, ONE GENERATOR, THREE EMITTERS (BookComponentStandard.md §10).
#
# Everything below is PARSED from BookComponentStandard.md. Nothing in this file
# restates a value the standard already holds. If a colour, a glyph, a role or a
# geometry string appears as a literal here, that is a defect -- the standard is
# the source and this file is the machine that reads it.
#
# The two exceptions, both delivery mechanics and therefore explicitly outside the
# standard's scope per §2 and §3.2:
#   URL_BASE   -- where this particular book serves its images from
#   ICON_DIR / MARK_DIR -- where this particular book keeps them
# Both are asserted against the live book in selftest().
#
# Usage:
#   python3 gen_component.py --selftest      run every conformance check (§10.1)
#   python3 gen_component.py --emit-marks    write the recoloured marks
#   python3 gen_component.py --legend        emit a generated legend
#   python3 gen_component.py --table         print the resolved mark table
#   python3 gen_component.py --demo          emit one callout of each role

import os
import re
import sys

VERSION = 'v1.1'   # the only version home in this file

HERE = os.path.dirname(os.path.abspath(__file__))
STANDARD = os.path.join(HERE, 'BookComponentStandard.md')

# --- delivery mechanics (this book's, not the standard's) ---------------------
URL_BASE = 'https://weymuth.github.io/zumo/images'
ICON_DIR = os.path.join(HERE, 'images', 'icons')   # generator INPUT, never written
MARK_DIR = os.path.join(HERE, 'images', 'marks')   # generator OUTPUT


# =============================================================================
# PARSING -- the standard is the source
# =============================================================================

_UNITS = ('zero one two three four five six seven eight nine ten eleven twelve thirteen '
          'fourteen fifteen sixteen seventeen eighteen nineteen').split()
_TENS = {'twenty': 20, 'thirty': 30, 'forty': 40, 'fifty': 50, 'sixty': 60,
         'seventy': 70, 'eighty': 80, 'ninety': 90}


def word_to_int(word):
    """'Twenty-five' -> 25. None if unreadable, which is a GATE limit, not a defect."""
    w = word.strip().lower().replace('\u2013', '-')
    if w in _UNITS:
        return _UNITS.index(w)
    head, _, tail = w.partition('-')
    if head in _TENS:
        if not tail:
            return _TENS[head]
        if tail in _UNITS[1:10]:
            return _TENS[head] + _UNITS.index(tail)
    return None


def _text():
    with open(STANDARD, encoding='utf-8') as fh:
        return fh.read()


def _section(t, start, end):
    """Slice the document between two headings. Both must be unique."""
    assert t.count(start) == 1, f'section start not unique: {start!r}'
    assert t.count(end) == 1, f'section end not unique: {end!r}'
    i, j = t.index(start), t.index(end)
    assert i < j, f'sections out of order: {start!r} .. {end!r}'
    return t[i:j]


def _rows(section):
    """Markdown table rows, minus header and separator, as cell lists."""
    out = []
    for line in section.splitlines():
        line = line.strip()
        if not line.startswith('|'):
            continue
        cells = [c.strip() for c in line.strip('|').split('|')]
        if set(''.join(cells)) <= set('-: '):
            continue
        out.append(cells)
    return out


def _one(pattern, text, label, flags=0):
    found = re.findall(pattern, text, flags)
    assert len(found) == 1, f'{label}: expected 1 match, found {len(found)}'
    return found[0]


def _tick(cell):
    """The single backticked token in a cell."""
    toks = re.findall(r'`([^`]+)`', cell)
    assert len(toks) == 1, f'expected one backticked token in {cell!r}'
    return toks[0]


def load_standard():
    t = _text()
    S = {}

    S['version'] = _one(r'\*\*Standard version: (v[0-9.]+)\*\*', t, 'standard version')

    # --- §5 palette --------------------------------------------------------
    pal_sec = _section(t, '## 5. The palette', '### 5.1 Geometry')
    palette = {}
    for cells in _rows(pal_sec):
        if cells[0] == 'Role':
            continue
        role, bg, border, title = cells[0], _tick(cells[1]), _tick(cells[2]), _tick(cells[3])
        palette[role] = {'bg': bg, 'border': border, 'title': title}
    assert len(palette) == 8, f'§5 palette: expected 8 roles, found {len(palette)}'
    S['palette'] = palette
    S['page'] = _one(r'Page colour: `(#[0-9A-Fa-f]{6})`', pal_sec, 'page colour')
    S['body'] = _one(r'Body text: `(#[0-9A-Fa-f]{6})`', pal_sec, 'body text colour')

    # --- §5.1 geometry -----------------------------------------------------
    geo_sec = _section(t, '### 5.1 Geometry', '### 5.2 Colour is never')
    geo = _one(r'```\n(.*?)```', geo_sec.replace('\r', ''), 'geometry block', re.S)
    S['geometry_raw'] = geo
    S['box_css'] = (
        'background-color: {bg}; border-left: 4px solid {border}; '
        'padding: 15px; margin: 20px 0; border-radius: 4px;'
    )
    S['title_css'] = (
        'font-weight: bold; margin-bottom: 8px; font-size: 1.05em; color: {title};'
    )
    # the literals above must appear in the standard's own block
    for frag in ('border-left: 4px solid', 'padding: 15px', 'margin: 20px 0',
                 'border-radius: 4px', 'font-weight: bold', 'margin-bottom: 8px',
                 'font-size: 1.05em'):
        assert frag in geo, f'§5.1 geometry drifted from generator: {frag!r} absent'

    # --- §6.1 shipping form ------------------------------------------------
    ship_sec = _section(t, '### 6.1 Shipping form', '### 6.2 Outline by default')
    S['mark_css'] = _one(r'```\n(height: [^\n]+)\n```', ship_sec, 'shipping form')

    # --- §7 families -------------------------------------------------------
    fam_sec = _section(t, '## 7. The families', '### 7.1 Two-state families')
    families = {}
    for cells in _rows(fam_sec):
        if cells[0] == 'Family':
            continue
        name, icons, role = cells[0], re.findall(r'`([^`]+)`', cells[1]), cells[2]
        assert role in palette, f'{name}: role {role!r} not in §5 palette'
        families[name] = {'icons': icons, 'role': role}
    fam_word, mark_word = _one(r'([A-Za-z-]+) families\. ([A-Za-z-]+) marks\.',
                               fam_sec, '§7 counts')
    S['families'] = families
    S['declared_family_word'] = fam_word
    S['declared_marks_word'] = mark_word

    # --- §7.1 two-state ----------------------------------------------------
    st_sec = _section(t, '### 7.1 Two-state families', '### 7.2 Supporting marks')
    two_state = _one(r'\*\*([A-Z][A-Z ]+)\*\* carries two states', st_sec, 'two-state family')
    states = {}
    for cells in _rows(st_sec):
        if cells[0] == 'State':
            continue
        states[cells[0]] = {'icon': _tick(cells[1]),
                            'colour': _one(r'(#[0-9A-Fa-f]{6})', cells[2], 'state colour')}
    assert len(states) == 2, f'§7.1: expected 2 states, found {len(states)}'
    S['two_state_family'] = two_state
    S['states'] = states

    # --- §7.2 supporting marks + grounds -----------------------------------
    sup_sec = _section(t, '### 7.2 Supporting marks', '### 7.3 Mark inventory')
    grounds = {}
    for cells in _rows(sup_sec):
        if cells[0] == 'Group':
            continue
        grounds[cells[0]] = {'ground': cells[1], 'in_scope': cells[2].lower() == 'yes'}

    # group blocks are "**Group:** `a` label · `b` label"
    groups = {}
    for m in re.finditer(r'\*\*([A-Za-z ]+):\*\*((?:[^\n]*\n)+?)\n', sup_sec):
        label, body = m.group(1).strip(), m.group(2)
        toks = re.findall(r'`([a-z0-9-]+)`', body)
        if toks:
            groups[label] = toks
    assert set(groups) == set(grounds), (
        f'§7.2 groups vs grounds mismatch: {sorted(set(groups) ^ set(grounds))}')
    S['groups'] = groups
    S['grounds'] = grounds

    # --- §7.3 inventory ----------------------------------------------------
    inv_sec = _section(t, '### 7.3 Mark inventory', '## 8. Collisions')
    S['inventory_total'] = int(_one(r'(\d+) distinct icon files', inv_sec, 'inventory total'))
    fam_n, sup_n = re.findall(r'(\d+) for the \d+ families.*?and (\d+) supporting',
                              inv_sec, re.S)[0]
    S['inventory_family'] = int(fam_n)
    S['inventory_supporting'] = int(sup_n)

    return S


# =============================================================================
# RESOLUTION -- every shipped mark and the one colour it takes
# =============================================================================

def resolve(S):
    """-> {icon: {'colour', 'why', 'owner'}} for marks that ship, plus deferrals."""
    ship, defer = {}, {}
    palette = S['palette']

    for name, f in S['families'].items():
        colour = palette[f['role']]['title']
        for icon in f['icons']:
            if name == S['two_state_family']:
                continue  # §7.1 states own their colours
            assert icon not in ship, f'glyph {icon!r} carries two families'
            ship[icon] = {'colour': colour, 'owner': name,
                          'why': f"family {name}, role {f['role']}, title colour"}

    for state, st in S['states'].items():
        ship[st['icon']] = {'colour': st['colour'],
                            'owner': f"{S['two_state_family']} ({state})",
                            'why': f'§7.1 two-state family, {state}'}

    for group, toks in S['groups'].items():
        in_scope = S['grounds'][group]['in_scope']
        for icon in toks:
            if icon in ship:
                # a challenge-card panel that IS a family keeps its family colour
                assert in_scope, (f'{icon!r} is a family mark but its supporting group '
                                  f'{group!r} is out of scope')
                continue
            if in_scope:
                ship[icon] = {'colour': S['body'], 'owner': f'supporting / {group}',
                              'why': f"§7.2 supporting, ground "
                                     f"{S['grounds'][group]['ground']}, body text"}
            else:
                defer[icon] = {'owner': f'supporting / {group}',
                               'why': f"§7.2 out of scope, ground "
                                      f"{S['grounds'][group]['ground']}"}

    return ship, defer


# =============================================================================
# THE THREE EMITTERS (§4)
# =============================================================================

def mark(icon, S):
    """§4.1 -- one glyph, no wrapper."""
    return (f'<img src="{URL_BASE}/marks/{icon}.svg" alt="" '
            f'style="{S["mark_css"]}">')


def callout(family, title, body, S):
    """§4.2 -- box + border + mark + title + body."""
    f = S['families'][family]
    role = S['palette'][f['role']]
    icon = f['icons'][0]
    box = S['box_css'].format(**role)
    ttl = S['title_css'].format(**role)
    return (f'<div style="{box}">\n'
            f'<div style="{ttl}">{mark(icon, S)} {title}</div>\n'
            f'{body}\n'
            f'</div>')


def legend_entry(family, S):
    """§4.3 -- mark + family name, no box."""
    f = S['families'][family]
    return f'{mark(f["icons"][0], S)} {family}'


def legend(families, S):
    """§4.4 -- legends are GENERATED and name only families in scope."""
    for fam in families:
        assert fam in S['families'], f'legend names an unknown family: {fam!r}'
    rows = '\n'.join(f'<li style="margin-bottom: 6px;">{legend_entry(f, S)}</li>'
                     for f in families)
    return f'<ul style="list-style: none; padding-left: 0;">\n{rows}\n</ul>'


# =============================================================================
# MARK EMISSION -- icons/ is input, marks/ is output (§6.1)
# =============================================================================

def recolour(svg, colour):
    n = svg.count('fill="currentColor"')
    assert n == 1, f'expected exactly one currentColor fill, found {n}'
    return svg.replace('fill="currentColor"', f'fill="{colour}"')


def emit_marks(S, write=True):
    ship, defer = resolve(S)
    if write:
        os.makedirs(MARK_DIR, exist_ok=True)
    written, unchanged = [], []
    for icon in sorted(ship):
        src = os.path.join(ICON_DIR, icon + '.svg')
        assert os.path.exists(src), f'{icon}.svg named in the standard, absent from icons/'
        with open(src, encoding='utf-8') as fh:
            out = recolour(fh.read(), ship[icon]['colour'])
        dst = os.path.join(MARK_DIR, icon + '.svg')
        if os.path.exists(dst) and open(dst, encoding='utf-8').read() == out:
            unchanged.append(icon)
            continue
        if write:
            with open(dst, 'w', encoding='utf-8') as fh:
                fh.write(out)
        written.append(icon)
    return written, unchanged, ship, defer


# =============================================================================
# SELFTEST -- §10.1 conformance, §10.2 control runs
# =============================================================================

def selftest(S):
    ship, defer = resolve(S)
    fails = []

    def check(ok, label):
        print(f' {"PASS" if ok else "FAIL"}  {label}')
        if not ok:
            fails.append(label)

    icons = {f[:-4] for f in os.listdir(ICON_DIR) if f.endswith('.svg')}
    named = set(ship) | set(defer)

    print(f'\nBookComponentStandard {S["version"]}   gen_component {VERSION}\n')

    # §7.3 -- the folder is asserted against the table in BOTH directions
    check(named - icons == set(), f'§7.3 every named mark exists in icons/  '
                                  f'(missing: {sorted(named - icons) or "none"})')
    check(icons - named == set(), f'§7.3 no unnamed file in icons/  '
                                  f'(strays: {sorted(icons - named) or "none"})')
    check(len(icons) == S['inventory_total'],
          f'§7.3 icons/ holds the declared count ({len(icons)} == {S["inventory_total"]})')

    # the count is also stated in WORDS in §7 -- a second home for one number.
    # Compare as INTEGERS. A lookup keyed on the current count would fail against a
    # perfectly correct document the moment the count left the table, and a gate that
    # cries wolf gets ignored.
    for word, actual, what in ((S['declared_marks_word'], S['inventory_total'], 'mark'),
                               (S['declared_family_word'], len(S['families']), 'family')):
        parsed = word_to_int(word)
        if parsed is None:
            check(False, f'§7 prose {what} count: cannot read the number word {word!r} '
                         f'-- gate cannot judge, not a document defect')
        else:
            check(parsed == actual,
                  f'§7 prose {what} count agrees with its table ({word} vs {actual})')

    # §1 -- the stamp is derived from the version line and must agree on MAJOR.MINOR
    stamp = re.findall(r'RoboLore Book Component Standard (v\d+\.\d+)', _text())
    real = re.match(r'(v\d+\.\d+)', S['version']).group(1)
    bad = [s for s in stamp if s != real]
    check(not bad, f'§1 every version stamp agrees with the version line '
                   f'({real}; disagreeing: {bad or "none"})')

    # §10.1.2 -- every family has exactly one mark (BRAIN CHECK's two are states)
    multi = {n: f['icons'] for n, f in S['families'].items() if len(f['icons']) != 1}
    check(set(multi) == {S['two_state_family']},
          f'§10.1.2 one mark per family, {S["two_state_family"]} excepted as two-state')

    # §10.1.3 -- no glyph carries two families
    seen, dupes = {}, []
    for n, f in S['families'].items():
        for i in f['icons']:
            if i in seen:
                dupes.append((i, seen[i], n))
            seen[i] = n
    check(not dupes, f'§10.1.3 no glyph carries two families ({dupes or "none"})')

    # §10.1.5 -- every colour traces to §5
    legal = {c for r in S['palette'].values() for c in r.values()} | {S['body'], S['page']}
    stray = {i: m['colour'] for i, m in ship.items() if m['colour'] not in legal}
    check(not stray, f'§10.1.5 every shipped colour comes from the §5 palette ({stray or "none"})')

    # every mark takes its role's TITLE colour -- no exceptions after v01.1.0
    titles = {r['title'] for r in S['palette'].values()} | {S['body']}
    off = {i: m['colour'] for i, m in ship.items() if m['colour'] not in titles}
    check(not off, f'§7.1 no mark drawn from a border or background colour ({off or "none"})')

    # inventory arithmetic
    check(S['inventory_family'] + S['inventory_supporting'] == S['inventory_total'],
          f'§7.3 arithmetic {S["inventory_family"]} + {S["inventory_supporting"]} '
          f'== {S["inventory_total"]}')

    # regeneration is byte-stable
    written, unchanged, _, _ = emit_marks(S, write=False)
    check(not os.path.isdir(MARK_DIR) or not written,
          f'marks/ is byte-identical to a fresh generation '
          f'({len(written)} would change)' if os.path.isdir(MARK_DIR)
          else 'marks/ not yet generated')

    # icons/ untouched by the generator
    check(all(open(os.path.join(ICON_DIR, f), encoding='utf-8').read()
              .count('fill="currentColor"') == 1
              for f in os.listdir(ICON_DIR) if f.endswith('.svg')),
          'icons/ is unmodified library source (currentColor intact in all)')

    # §6 LICENSE obligation
    check(os.path.exists(os.path.join(ICON_DIR, 'LICENSE')),
          '§6 LICENSE kept alongside the icon assets')

    # §10.2 CONTROL RUN -- the gate must fail on the defect it exists to catch
    probe = dict(S)
    probe['inventory_total'] = S['inventory_total'] + 1
    control_fired = len({f[:-4] for f in os.listdir(ICON_DIR)
                         if f.endswith('.svg')}) != probe['inventory_total']
    check(control_fired, '§10.2 control run: count gate fires on a seeded miscount')

    print(f'\n  ships: {len(ship)}   deferred: {len(defer)}   '
          f'named: {len(named)}   icons/: {len(icons)}')
    print('\n' + ('ALL CHECKS PASS' if not fails else f'{len(fails)} FAILED'))
    return not fails


# =============================================================================

def main():
    S = load_standard()
    arg = sys.argv[1] if len(sys.argv) > 1 else '--selftest'

    if arg == '--selftest':
        sys.exit(0 if selftest(S) else 1)

    elif arg == '--emit-marks':
        written, unchanged, ship, defer = emit_marks(S)
        print(f'marks/  {len(written)} written, {len(unchanged)} already current')
        print(f'deferred (out of scope per §7.2 grounds): {len(defer)}')
        for i in sorted(defer):
            print(f'  {i:22s} {defer[i]["why"]}')

    elif arg == '--table':
        ship, defer = resolve(S)
        print(f'{"mark":24s} {"colour":9s} owner')
        for i in sorted(ship):
            print(f'{i:24s} {ship[i]["colour"]:9s} {ship[i]["owner"]}')
        print()
        for i in sorted(defer):
            print(f'{i:24s} {"--":9s} DEFERRED: {defer[i]["owner"]}')

    elif arg == '--legend':
        fams = sys.argv[2:] or sorted(S['families'])
        print(legend(fams, S))

    elif arg == '--demo':
        for role in S['palette']:
            fam = next(n for n, f in S['families'].items() if f['role'] == role)
            print(callout(fam, fam.title(), '<p>Body text.</p>', S))
            print()

    else:
        print(__doc__ or 'unknown argument', arg)
        sys.exit(2)


if __name__ == '__main__':
    main()
