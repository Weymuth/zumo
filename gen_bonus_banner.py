#!/usr/bin/env python3
"""gen_bonus_banner.py — generate the bonus-block banner + nav pill from one table.
VERSION below is the only version home.

Bible §4.5: three families, one mark and one word each.
  practice    &#128296; (hammer)     "Extra Practice"
  observation &#128269; (magnifier)  "Observation"
  sabotage    &#128373;&#65039;      "Sabotage"

Per Bible §24.6b: build bytes, assert, write .tmp, os.replace. Never open(path,'w').
"""
import os, re, sys
import lesson_inventory as LI

VERSION = 'v1.4.1'   # the only version home in this file (S108; v1.4.0 S110; v1.4.1 S111 -
                     # CAP repainted to the §10+ band, S111 repaint)

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

# S108, banner scheme F1: the family MARK is gone from the cap. Bible §4.5 ruled the mark
# derived from the family; S107 ruled NO ICONS ON ANY OF THE 237 CAPS, bonus included, and
# supersedes it. The three families survive in the WORD, which is what carried §4.5's harm
# argument anyway -- a student sent hunting a defect that isn't there is misled by
# "Sabotage", not by a magnifying glass. MARK is kept below, unused, for provenance.
BANNER = ('<div id="bonus-challenges">'
          '<span style="display: block; font-size: 0.78em; font-weight: 600; letter-spacing: 0.1em; text-transform: uppercase; opacity: 0.8; margin-bottom: 3px;">{word}</span>'
          '<span style="display: block; font-size: 1.28em; font-weight: 700; letter-spacing: -0.021em;">{count} {noun}</span></div>')

# The CAP is the gray div the banner is seated in.  It is family-independent and
# identical in all 15 bonus blocks.  It lived outside this generator until S87,
# when L03 was found shipping a `linear-gradient(135deg, #6f7582, #4d535f)` cap
# with 12px padding and a 40px top margin -- which passed gate 30 for its whole
# life because the check was a SUBSTRING test for '#6f7582', and a gradient
# containing #6f7582 satisfies it.  Generated and byte-gated from here on.
CAP = ('<div style="background-color: #6f7582; color: white; padding: 13px 18px; '
       'border-radius: 8px 8px 0 0; margin-top: 24px;">')

def banner_for(lg):
    fam, count, noun, _ = TABLE[lg]
    return BANNER.format(word=WORD[fam], count=count, noun=noun)

def rewrite(path, lg, dry=True):
    # S110: read through the SAME expander book_gates uses. This tool matched the bonus
    # nav pill by an INLINE-STYLE signature ('text-decoration: none; padding: 5px 12px'),
    # which the S103 class migration deleted from every lesson -- so every run since then
    # ended in `L02: expected exactly 1 nav pill, found 0`. Nothing in the ritual runs this
    # file, so the crash was never seen. Same defect and same cause as gen_part_banners.
    s = LI.expand_classes(open(path, encoding='utf-8').read())
    orig = s
    fam = TABLE[lg][0]
    notes = []

    # 1. the banner div
    m = re.search(r'<div id="bonus-challenges"[^>]*>.*?</div>', s, re.S)
    assert m, f'L{lg}: no bonus-challenges banner div'

    # 1a. the cap div the banner sits in (locate from the banner's START, not from
    #     the id= offset -- searching back from id= lands on the banner's own <div)
    cw = s.rfind('<div', 0, m.start())
    cap_open = s[cw:s.find('>', cw) + 1]
    if cap_open != CAP:
        s = s[:cw] + CAP + s[s.find('>', cw) + 1:]
        notes.append(f'cap: {cap_open} -> canonical')
        m = re.search(r'<div id="bonus-challenges"[^>]*>.*?</div>', s, re.S)
        assert m, f'L{lg}: banner lost after cap rewrite'
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
    _cw = s.rfind('<div', 0, re.search(r'<div id="bonus-challenges"', s).start())
    assert s[_cw:s.find('>', _cw) + 1] == CAP, f'L{lg}: cap did not land byte-exact'
    m2 = re.search(r'<div id="bonus-challenges"[^>]*>(.*?)</div>', s, re.S)
    assert m2 and m2.group(0) == new_banner, f'L{lg}: banner did not land byte-exact'
    txt = m2.group(1)
    # S108: the mark assert INVERTS. It used to demand the family glyph was present; the
    # cap now carries none, so it demands none survived -- entity or raw, any family.
    assert WORD[fam] in txt, f'L{lg}: family word missing'
    for stray in ['&#128296;', '&#128269;', '&#128373;', '&#65039;',
                  '🔨', '🔍', '🕵', '🧩']:
        assert stray not in txt, f'L{lg}: a mark survived the cap: {stray}'
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

def selftest():
    ok = True

    def rep(label, passed, detail=''):
        nonlocal ok
        ok = ok and passed
        print('   %-5s %s%s' % ('OK' if passed else 'FAIL', label, ('  ' + detail) if detail else ''))

    print('CONTROL A (it runs at all): every run since S103 died on the first lesson')
    err = None
    try:
        for lg in sorted(TABLE):
            rewrite(f'lessons/Lesson_{lg}.html', lg, dry=True)
    except Exception as e:
        err = e
    rep('rewrite() completes on all %d table lessons' % len(TABLE), err is None,
        repr(err) if err else '')

    print('CONTROL B (the fix CHANGED something): the pill signature must be absent from')
    print('  the raw file and present once in the expanded one')
    raw = open('lessons/Lesson_02.html', encoding='utf-8').read()
    exp = LI.expand_classes(raw)
    sig = 'text-decoration: none; padding: 5px 12px'
    rep('signature raw 0, expanded >0', raw.count(sig) == 0 and exp.count(sig) > 0,
        'raw %d expanded %d' % (raw.count(sig), exp.count(sig)))

    print('CONTROL C (--write is refused): emitting the inline form breaches 27.12')
    import subprocess
    r = subprocess.run([sys.executable, __file__, '--write'], capture_output=True, text=True)
    rep('--write exits non-zero and says why',
        r.returncode != 0 and 'REFUSED' in r.stdout, 'exit %d' % r.returncode)

    print('CONTROL D (the corpus is already canonical): nothing should want changing')
    changed = sum(rewrite(f'lessons/Lesson_{lg}.html', lg, dry=True)[1] for lg in sorted(TABLE))
    rep('0 of %d lessons differ' % len(TABLE), changed == 0, '%d differ' % changed)

    print('\n%s' % ('ALL CONTROLS PASS' if ok else 'CONTROLS FAILED'))
    return 0 if ok else 1


if __name__ == '__main__':
    if '--selftest' in sys.argv:
        sys.exit(selftest())
    if '--write' in sys.argv:
        print('REFUSED. --write emits inline style="" attributes, which Bible 27.12 forbids\n'
              'in any page that links css/book.css and gate 41 catches. Repair a bonus\n'
              'banner through restore -> regenerate -> apply. This tool is a CHECKER now.')
        sys.exit(1)
    dry = True
    print(f'gen_bonus_banner {VERSION} — {"DRY RUN" if dry else "WRITING"}\n')
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
