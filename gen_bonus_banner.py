#!/usr/bin/env python3
"""gen_bonus_banner.py v1.1 — generate the bonus-block banner + nav pill from one table.

Bible §4.5: three families, one mark and one word each.
  practice    &#128296; (hammer)     "Extra Practice"
  observation &#128269; (magnifier)  "Observation"
  sabotage    &#128373;&#65039;      "Sabotage"

Per Bible §24.6b: build bytes, assert, write .tmp, os.replace. Never open(path,'w').
"""
import os, re, sys

MARK = {'practice': '&#128296;', 'observation': '&#128269;', 'sabotage': '&#128373;&#65039;'}
WORD = {'practice': 'Extra Practice', 'observation': 'Observation', 'sabotage': 'Sabotage'}

# lesson -> (family, count word, noun, card count for the count assert)
TABLE = {
    '02': ('practice',    'Six',   'Code Challenges',           6),
    '03': ('practice',    'Six',   'Motor Challenges',          6),
    '04': ('observation', 'Five',  'Sensor Experiments',        5),
    '05': ('observation', 'Six',   'Proximity Experiments',     6),
    '06': ('observation', 'Five',  'Encoder Experiments',       5),
    '07': ('observation', 'Five',  'Multi-File Experiments',    5),
    '08': ('sabotage',    'Five',  'Line-Following Mysteries',  5),
    '09': ('sabotage',    'Five',  'State-Machine Mysteries',   5),
    '10': ('sabotage',    'Five',  'Obstacle Mysteries',        5),
    '11': ('sabotage',    'Four',  'Gap Mysteries',             4),
    '12': ('sabotage',    'Four',  'Gyro Mysteries',            4),
    '13': ('sabotage',    'Four',  'Messed Up Files',           4),
    '14': ('sabotage',    'Four',  'Messed Up Files',           4),
    '15': ('sabotage',    'Four',  'Messed Up Files',           4),
    # L16 HELD OUT by DJ ruling: 2 cards, revisit when it has 4.
}

BANNER = ('<div id="bonus-challenges" style="font-size: 1.15em; font-weight: bold;">'
          '{mark} {word}: {count} {noun}</div>')

def banner_for(lg):
    fam, count, noun, _ = TABLE[lg]
    return BANNER.format(mark=MARK[fam], word=WORD[fam], count=count, noun=noun)

def rewrite(path, lg, dry=True):
    s = open(path, encoding='utf-8').read()
    orig = s
    fam = TABLE[lg][0]
    notes = []

    # 1. the banner div
    m = re.search(r'<div id="bonus-challenges"[^>]*>.*?</div>', s, re.S)
    assert m, f'L{lg}: no bonus-challenges banner div'
    new_banner = banner_for(lg)
    if m.group(0) != new_banner:
        s = s[:m.start()] + new_banner + s[m.end():]
        notes.append(f'banner: {m.group(0)[m.group(0).find(">")+1:-6]!r} -> {WORD[fam]}: {TABLE[lg][1]} {TABLE[lg][2]!r}')

    # 2. every anchor pointing at the block gets the family word
    def fix_pill(mm):
        head, label = mm.group(1), mm.group(2)
        return f'{head}{WORD[fam]}</a>'
    NAVSIG = 'text-decoration: none; padding: 5px 12px'
    hits = [mm for mm in re.finditer(r'<a href="#bonus-challenges"([^>]*)>([^<]*)</a>', s)
            if NAVSIG in mm.group(1)]
    assert len(hits) == 1, f'L{lg}: expected exactly 1 nav pill, found {len(hits)}'
    mm = hits[0]
    s = s[:mm.start()] + f'<a href="#bonus-challenges"{mm.group(1)}>{WORD[fam]}</a>' + s[mm.end():]
    notes.append(f'nav pill {mm.group(2)!r} -> {WORD[fam]!r}')

    # ---- asserts: re-parse and read back (§24.6b, the S84 lesson)
    assert s.count('id="bonus-challenges"') == 1, f'L{lg}: banner id count != 1'
    m2 = re.search(r'<div id="bonus-challenges"[^>]*>(.*?)</div>', s, re.S)
    assert m2 and m2.group(0) == new_banner, f'L{lg}: banner did not land byte-exact'
    txt = m2.group(1)
    assert MARK[fam] in txt and txt.count('&#128373;') <= 1, f'L{lg}: mark wrong or doubled'
    assert WORD[fam] in txt, f'L{lg}: family word missing'
    for stray in ['🔨', '🔍', '🧩', '&#128296;&#128296;']:
        assert stray not in txt, f'L{lg}: raw/duplicate mark survived: {stray}'
    navs = [mm for mm in re.finditer(r'<a href="#bonus-challenges"([^>]*)>([^<]*)</a>', s)
            if NAVSIG in mm.group(1)]
    assert len(navs) == 1 and navs[0].group(2) == WORD[fam], \
        f'L{lg}: nav pill did not land as {WORD[fam]!r}'
    assert s.count('id="bonus-challenges"') == 1

    if not dry:
        tmp = path + '.tmp'
        with open(tmp, 'w', encoding='utf-8') as fh:
            fh.write(s)
        os.replace(tmp, path)
    return notes, s != orig

if __name__ == '__main__':
    dry = '--write' not in sys.argv
    print(f'gen_bonus_banner v1.1 — {"DRY RUN" if dry else "WRITING"}\n')
    changed = 0
    for lg in sorted(TABLE):
        p = f'lessons/Lesson_{lg}.html'
        notes, did = rewrite(p, lg, dry=dry)
        print(f'L{lg}  {"CHANGED" if did else "already canonical"}')
        for x in notes:
            print(f'      {x}')
        changed += did
    print(f'\n{changed} of {len(TABLE)} lessons changed.')
    print('NOT in the table: L16 (held by ruling, 2 cards) · L01 (no bonus block)')
