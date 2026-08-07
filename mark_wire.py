#!/usr/bin/env python3
# VERSION is the ONE home and sits ABOVE the changelog, so a plain grep of this file
# returns the version and not a changelog line (S98).
VERSION = 'v1.0'
# v1.0 (S128): first release. Swaps the leading emoji for the family's ruled mark.
"""mark_wire.py - replaces a callout's leading emoji with its family's MARK (§24.14b).

THE DIRECTION IS THE RULE (§24.14). Family comes from CONTENT and is carried in the
markup as data-family (gate 59). The mark is an OUTPUT of the family, looked up here
through BookComponentStandard §7 - the table DJ approved at S91 and amended at S93.
Nothing in this tool reads a glyph to decide a family, and nothing anywhere may read
a mark filename back to recover one.

WHY A NAME-MATCH MAPPING WAS REJECTED, WITH A NUMBER ON IT. The bullseye emoji carries
THIRTEEN distinct labels across its 125 uses (THE GOAL 100, TRY IT 12, FINISHED EARLY?
2, OBJECTIVES 1, and nine more), and NOTE's 133 blocks wear thirteen different emoji.
Glyph-to-mark is not a function in either direction. Matching the bullseye to
bullseye.svg by name would be right 100 times and wrong 25.

SCOPE IS A NAMED SET, NOT A COUNT (§25.2a).
  - BRAIN CHECK is HELD. All 56 of its blocks already carry the purpose-built two-state
    BrainGear emblem, which is exactly the two-state behaviour §7.1 specifies for this
    family. Wiring bookmark.svg would give them a SECOND mark. Every one of the 22
    non-leading-glyph blocks in the book is a BRAIN CHECK, so holding this family also
    disposes of that whole shape.
  - NO_GLYPH blocks are HELD. 17 mapped blocks carry no leading emoji at all. Putting a
    mark there is not a swap, it is ADDING decoration to a block that never had any -
    a different act, and one nobody has ruled. They are named, not silently skipped.
  - Families with no §7 row are out of scope by construction: they have no mark.

Offsets come from lesson_inventory (v1.3.1) and are FILE offsets. Edits run back to
front so an earlier write cannot move a later one, and every file is read back.
"""
import glob
import html as _html
import io
import os
import re
import sys
import contextlib

import lesson_inventory

with contextlib.redirect_stdout(io.StringIO()):
    import build_mark_index as BMI

# The §7 roster, read from the module that transcribes BookComponentStandard - never
# re-typed here (S83: import the definition, do not write a second copy).
#
# THE TWO-STATE KEY IS NORMALISED, AND CONTROL E IS WHY. §7.1 gives BRAIN CHECK two
# rows - `BRAIN CHECK · open` and `BRAIN CHECK · done` - while the book's family map
# knows one family called `BRAIN CHECK`. Left alone, the lookup misses on the middot
# and the family falls out of scope by ACCIDENT, which makes HELD_FAMILIES below look
# load-bearing while doing nothing: delete the hold and the behaviour is identical.
# Normalising makes the hold real, so the control can prove it (§24.8).
ROLE_TO_MARK = {}
for _mark, _role in BMI.FAMILY.items():
    ROLE_TO_MARK.setdefault(_role.split(' \u00b7 ')[0], _mark)

# HELD BY NAME, with the reason, so a later session cannot mistake either for an
# oversight and "fix" it (§25.2a).
HELD_FAMILIES = {
    'BRAIN CHECK': 'already carries the two-state BrainGear emblem (§7.1)',
}

MARK_DIR = 'images/marks'
# data-mark, NOT class="mark". build_css rewrites class attributes and would re-derive
# the semantic rule into a value-named one (§27.15b); it never touches data attributes.
# The value is the mark NAME, for a human reading the source - nothing reads it back to
# recover a family, which §24.14 forbids.
_IMG = '<img src="../%s/%s.svg" alt="" data-mark="%s">'


def mark_for(family):
    """The ruled mark file for a family, or None if §7 gives it no row."""
    if family in HELD_FAMILIES:
        return None
    return ROLE_TO_MARK.get(family)


def plan(path):
    """[(kind, start, open_end, family, mark, glyph)] for every callout in one file.

    kind is one of: SWAP (leading emoji, wire it), NO_GLYPH (held, nothing to swap),
    HELD (family held by name), NO_MARK (family has no §7 row).
    """
    raw = open(path, encoding='utf-8').read()
    out = []
    for c in lesson_inventory.build(path)['callouts']:
        fam = c.get('family_attr')
        glyph = (c.get('glyph') or '').strip()
        label = c.get('label') or ''
        if fam in HELD_FAMILIES:
            kind = 'HELD'
        elif fam not in ROLE_TO_MARK:
            kind = 'NO_MARK'
        elif not glyph:
            kind = 'NO_GLYPH'
        elif label[:1] != glyph:
            kind = 'NOT_LEADING'
        else:
            kind = 'SWAP'
        out.append((kind, c['start'], c['open_end'], fam, mark_for(fam), glyph))
    return out, raw


def _swap_one(raw, open_end, glyph, mark):
    """Replace the FIRST occurrence of `glyph` at or after open_end with the mark img.

    The search window is bounded to the block's own header text so a glyph deeper in
    the block cannot be hit instead. The emoji is written literally in the file per
    §27.16, and may be followed by a variation selector U+FE0F which is part of the
    same rendered character and goes with it.
    """
    win = raw[open_end:open_end + 400]
    i = win.find(glyph)
    assert i != -1, 'glyph %r not found in the header window at %d' % (glyph, open_end)
    j = i + len(glyph)
    if win[j:j + 1] == '\ufe0f':          # variation selector rides with the emoji
        j += 1
    while win[j:j + 1] == ' ':            # and so does the single space after it
        j += 1
        break
    a, b = open_end + i, open_end + j
    return raw[:a] + (_IMG % (MARK_DIR, mark, mark)) + raw[b:]


def build(paths, apply=False):
    import collections
    tally = collections.Counter()
    held = []
    for p in sorted(paths):
        rows, raw = plan(p)
        edits = []
        for kind, start, open_end, fam, mark, glyph in rows:
            tally[kind] += 1
            if kind in ('NO_GLYPH', 'NOT_LEADING'):
                held.append((p, fam, kind))
            if kind == 'SWAP':
                edits.append((open_end, glyph, mark))
        if apply and edits:
            for open_end, glyph, mark in sorted(edits, reverse=True):
                raw = _swap_one(raw, open_end, glyph, mark)
            blob = raw.encode('utf-8')
            tmp = p + '.tmp'
            with open(tmp, 'wb') as fh:
                fh.write(blob)
            os.replace(tmp, p)
            # READ BACK (S117). Every SWAP must now be a NO_GLYPH - the emoji is gone.
            back, _ = plan(p)
            still = sum(1 for k, *_r in back if k == 'SWAP')
            assert still == 0, '%s: %d block(s) still carry a leading emoji' % (p, still)
    return tally, held


def selftest():
    ok = True
    # A: the roster is the imported one, not a local copy.
    print('  A  families with a §7 mark ............... %d' % len(ROLE_TO_MARK))

    # B: a swap removes the emoji and inserts exactly one img.
    s = '<div data-family="TIP">\U0001f4a1 TIP</div>'
    r = _swap_one(s, 23, '\U0001f4a1', 'lightbulb')
    if '\U0001f4a1' in r or r.count('<img') != 1:
        print('  B  FAIL: %r' % r); ok = False
    else:
        print('  B  emoji gone, one img in ............. PASS')

    # C: a variation selector rides with the emoji rather than being orphaned.
    s2 = '<div>\u26a0\ufe0f WARNING</div>'
    r2 = _swap_one(s2, 5, '\u26a0', 'exclamation-triangle')
    if '\ufe0f' in r2:
        print('  C  FAIL: orphaned variation selector: %r' % r2); ok = False
    else:
        print('  C  variation selector goes with it .... PASS')

    # D: the locator refuses rather than guessing when the glyph is not there.
    try:
        _swap_one('<div>no emoji here</div>', 5, '\U0001f4a1', 'lightbulb')
        print('  D  FAIL: swapped a glyph that is absent'); ok = False
    except AssertionError:
        print('  D  refuses when the glyph is absent ... PASS')

    # E: BRAIN CHECK is held, and holding it is not an accident of a missing row.
    if 'BRAIN CHECK' not in HELD_FAMILIES or mark_for('BRAIN CHECK') is not None:
        print('  E  FAIL: BRAIN CHECK is not held'); ok = False
    elif ROLE_TO_MARK.get('BRAIN CHECK') is None:
        print('  E  FAIL: held for the wrong reason - §7 gives it no row either'); ok = False
    else:
        print('  E  BRAIN CHECK held BY NAME, not by gap  PASS')

    # F: every mark this tool can emit exists on disk.
    missing = [m for m in ROLE_TO_MARK.values()
               if not os.path.exists(os.path.join(MARK_DIR, m + '.svg'))]
    if missing:
        print('  F  FAIL: marks named but absent: %s' % ', '.join(missing)); ok = False
    else:
        print('  F  every emittable mark is on disk .... PASS')

    print('ALL CONTROLS PASS' if ok else 'CONTROLS FAILED')
    return 0 if ok else 1


def main():
    args = sys.argv[1:]
    print('mark_wire.py %s - the mark is an OUTPUT of the family (§24.14).' % VERSION)
    if '--selftest' in args:
        return selftest()
    tally, held = build(sorted(glob.glob('lessons/Lesson_*.html')), apply='--apply' in args)
    for k in ('SWAP', 'NO_GLYPH', 'NOT_LEADING', 'HELD', 'NO_MARK'):
        if tally[k]:
            print('  %-12s %4d' % (k, tally[k]))
    import collections
    byfam = collections.Counter((f, k) for _p, f, k in held)
    for (f, k), n in byfam.most_common():
        print('  HELD, not swept: %-22s %-12s %d' % (f, k, n))
    return 0


if __name__ == '__main__':
    sys.exit(main())
