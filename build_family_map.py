#!/usr/bin/env python3
# VERSION is the ONE home, and it sits ABOVE the changelog so a plain grep of this file
# lands on the live version, not on a changelog line (S98). The block below is prose,
# not __doc__ — nothing in the repo reads __doc__ (checked).
VERSION = 'v1.3.7'
# v1.3.7 (S119): baseline 1065 -> 1069. L15 converted to the four Brain Check exit
#   blocks; controlled at an identical generator version pre-tree against post-tree,
#   exactly ONE family moving, BRAIN CHECK 52 -> 56, the other 29 byte-identical.
# v1.3.6 (S118): baseline 1061 -> 1065. L13 converted to the four Brain Check exit
#   blocks; controlled at an identical generator version pre-tree against post-tree,
#   exactly ONE family moving, BRAIN CHECK 48 -> 52, the other 29 byte-identical.
# v1.3.5 (S117): baseline 1057 -> 1061. L12 converted to the four Brain Check exit
#   blocks. Controlled at an identical generator version, pre-tree against post-tree:
#   exactly ONE family moves, BRAIN CHECK 44 -> 48, the other 29 byte-identical.
# v1.3.4 (S116): baseline 1053 -> 1057. L11 converted to the four Brain Check exit
#   blocks. Controlled at an identical generator version, pre-tree against post-tree:
#   exactly ONE family moves, BRAIN CHECK 40 -> 44, and the other 29 are byte-identical.
#   The total alone is not evidence (S114) - the per-family delta is.
# v1.3.3 (S115): baseline 1049 -> 1053. L10 converted to the four Brain Check exit
#   blocks, which are four callout wrappers. CONTROLLED BEFORE THE LITERAL MOVED, at an
#   identical generator version, pre-edit tree against post-edit: exactly ONE family count
#   changes, BRAIN CHECK 36 -> 40. The other 27 are byte-identical, so the delta is the
#   four new blocks and nothing else - the total alone would not have proven that.
#   Still a FROZEN BASELINE, not a count (Bible §24.14). Reading it as a count is the
#   S114 defect; the printed line says 1053 of 1053 and means 'still the book S115 left'.
# v1.3.2 (S113): baseline 1048 -> 1049. L03's [IMAGE 3.4] placeholder became a real
#   WHAT YOU SHOULD SEE callout carrying a §22 terminal block, so the book has one more
#   callout than it did. Control-run against the pre-edit tree with this same version:
#   the ONLY lines that move are WHAT YOU SHOULD SEE 27 -> 28 and the total; the other
#   29 family counts are byte-identical, so the delta is the one added block and nothing
#   else. NOTE FOR DJ: this denominator is a FROZEN BASELINE, not a parse of the book -
#   the label 'assigned 1049 / 1048' reads like a count and is not one. Every future
#   callout added anywhere in the book will fail gate 47 until this literal is edited.
#   Parsing the true total (assigned + len(unk)) and asserting the baseline separately
#   is the obvious fix and is NOT taken here - it changes what gate 47 means, and that
#   is DJ's ruling to make.
# v1.1.3 (S98): version home moved above the docstring changelog (same defect as book_gates;
#   a plain grep returned v1.0.0). Output asserted byte-identical before and after.
"""build_family_map.py - assigns every callout block to a family.
The lines beginning vN below are changelog, not version homes.

Reproducible from a clean clone: run it from repo root, no prior step. It builds its
own inventory by calling lesson_inventory.build() on all 16 lessons (v1.0.0 replaces
a read of /tmp/inv.json, which meant a fresh session got FileNotFoundError).

v1.1.1: reference renamed - the map is maintained, not a session artifact, so it is
ZUMO_FAMILY_MAP.md. No behaviour change; the reference was always prose.

v1.1.0: the 15 blocks the S94 map assigned but this script did not are now ruled (DJ, S96).
assigned 1048/1048, unassigned 0, and every one of the 30 family counts equals
ZUMO_FAMILY_MAP.md exactly - the script now reproduces the document. Rules match on
label PREFIX, never line number. Control-run: routing one block to the wrong family leaves
the 1048 total untouched and shows up only in the per-family diff, so the total is not
evidence on its own.

v1.0.2: the glyph+scheme fallback map emitted its family names as literals, and two of
them carried the curly apostrophe (ENGINEER\u2019S LOG) that norm() folds on the INPUT
side only. Map VALUES never pass back through norm(), so the one header-less block that
resolves by scheme landed in a second bucket: 16 + 1 instead of 17, and 31 families
instead of 30. Values now written straight, matching CANON. Control-run: only the two
ENGINEER rows and the family count moved; assigned stayed 1033, unassigned stayed 15.

v1.0.1: INSIGHT left the shared blue for teal #e9f7f5/#2da99d (S95, DJ ruling). The old
🔍-on-blue key is REPLACED, not kept: after the split, a magnifier on LEARN's blue is a
defect to surface, not a block to silently classify as INSIGHT.

Label matching unescapes TWICE and normalises the curly apostrophe before comparing:
§24.11 - an entity is not the character it encodes. ENGINEER'S LOG carries &rsquo;
and read as ZERO blocks in S94 until this was fixed. It has 17.
"""
import json,re,html,collections,glob,os,sys

import lesson_inventory

ROOT=sys.argv[1] if len(sys.argv)>1 and not sys.argv[1].startswith('-') else '.'
_files=sorted(glob.glob(os.path.join(ROOT,'lessons','Lesson_*.html')))
assert len(_files)==16, 'expected 16 lesson files under %s/lessons, found %d - run from repo root' % (ROOT,len(_files))
d=[lesson_inventory.build(f) for f in _files]
def norm(s):
    s=html.unescape(html.unescape(s or '')).replace('\u2019',"'").replace('\u2014','-')
    return re.sub(r'^[^A-Za-z"\u201c]+','',s).strip()

CANON=["HOW THIS SECTION WORKS","IF YOU'RE STUCK","COMMON PITFALLS","ENGINEER'S LOG","WHERE THIS GOES",
"FINISHED EARLY","GOING DEEPER","BRAIN CHECK","BUILDS ON","THE LOGIC","KEY TERM","CHECKPOINT",
"GLOSSARY","THE GOAL","THE WALL","DO THIS NOW","MY PLAN","WRITE IT","WARNING","INSIGHT","ANSWER",
"LEARN","NOTE","TIP","HINT"]
CANON.sort(key=len,reverse=True)

# S94 rulings, checked in order. (matcher, family)
RULE=[
 (lambda l,g,s: l.upper().startswith('MYSTERY'),                        'MYSTERY'),
 (lambda l,g,s: 'WHAT YOU SHOULD SEE' in l.upper(),                     'WHAT YOU SHOULD SEE'),
 (lambda l,g,s: l.upper().startswith('WHAT YOU NEED') or 'PREREQUISIT' in l.upper(),'WHAT YOU NEED'),
 (lambda l,g,s: l.upper().startswith('COMPILE CHECK') or 'CALIBRATION IS A CONTRACT' in l.upper(),'STILL GREEN'),
 (lambda l,g,s: re.match(r'TRY (IT|THIS)|BREAK IT ON PURPOSE|FUNCTIONALITY TEST|CODE SWAP|TEST IT|THE GREEN SURVEY',l.upper()),'TRY THIS'),
 (lambda l,g,s: re.match(r'PREDICT FIRST|ASK YOURSELF|DISCUSSION QUESTIONS',l.upper()),'THINK ABOUT IT'),
 (lambda l,g,s: 'FELL BEHIND' in l.upper(),                             "IF YOU'RE STUCK"),
 (lambda l,g,s: re.match(r"NEXT LESSON|WHAT'S NEXT",l.upper()) or l.startswith('Preview:') or 'Coming in Lesson' in l or 'Lesson 8 Preview' in l or 'Looking Ahead' in l,'WHERE THIS GOES'),
 (lambda l,g,s: re.match(r'WORK IN|WHERE TO LOOK',l.upper()),           '(card header)'),
 (lambda l,g,s: 'YOU MIGHT WONDER' in l.upper() or l.startswith('"If the robot can tell') or l.startswith('Wait - TRIM'),'YOU MIGHT WONDER'),
 (lambda l,g,s: 'ARRIVE EARLY' in l.upper() or l.upper().startswith('DO THIS') or 'THE TUNING RITUAL' in l.upper(),'DO THIS NOW'),
 (lambda l,g,s: re.match(r'FINAL CHECKLIST|VERIFICATION CHECKLIST|FINAL CHECKPOINT',l.upper()),'CHECKPOINT'),
 (lambda l,g,s: 'REAL-WORLD' in l.upper() or l.startswith('RoboCup Connection'),'REAL-WORLD CONNECTION'),
 (lambda l,g,s: re.match(r'TURN OFF AI AUTOCOMPLETE|ALWAYS STOP YOUR MOTORS|THE DANGER EVERY WHILE|THE EIGHT MINUTES|THE ONE-CHARACTER TRAP',l.upper()) or l.startswith('The one-character trap'),'WARNING'),
 (lambda l,g,s: 'THE BUTTERFLY ERROR' in l.upper(),                     'COMMON PITFALLS'),
 (lambda l,g,s: re.match(r'THE ONE IDEA|THE TRADE YOU JUST MADE|THE KEY INSIGHT',l.upper()) or l.startswith('The rule, for the rest'),'INSIGHT'),
 (lambda l,g,s: 'NEW IN THIS LESSON' in l.upper(),                      'HOW THIS SECTION WORKS'),
 (lambda l,g,s: 'YOU ALREADY OWN THIS TOOL' in l.upper() or l.startswith('The desk and the bookshelf') or l.startswith('Reminder -') or l.startswith('INFO:') or l.startswith('The recipe, written out') or l.startswith('Recipe:'),'NOTE'),
 (lambda l,g,s: l.startswith('The rule that saves you') or l.startswith('The rule of thumb') or l.startswith('Clamp the memory'),'TIP'),
 (lambda l,g,s: l.startswith('OBJECTIVES'),                             'OBJECTIVES'),
 # --- S96 rulings (DJ). Closes the 15 blocks the S94 map assigned but the generator did not.
 # Matched on label prefix, not line number, so an edit above them does not break the rule.
 (lambda l,g,s: l.startswith('A new kind of label'),                     'HOW THIS SECTION WORKS'),
 (lambda l,g,s: l.startswith('Unit Conversion'),                         'NOTE'),
 (lambda l,g,s: l.startswith('Which cells'),                             'NOTE'),
 (lambda l,g,s: l.startswith('Watch your scope'),                        'NOTE'),
 (lambda l,g,s: l.startswith("Why Today's Work Matters"),                'NOTE'),
 (lambda l,g,s: l.startswith('Why TRIM here'),                           'NOTE'),
 (lambda l,g,s: l.startswith('Where Does constrain()'),                  'KEY TERM'),
 (lambda l,g,s: l.startswith('New operator'),                            'KEY TERM'),
 (lambda l,g,s: l.startswith('Accuracy Note'),                           'TIP'),
 (lambda l,g,s: l.startswith('Best Practice: Naming'),                   'TIP'),
 (lambda l,g,s: l.startswith('Working Backward'),                        'THINK ABOUT IT'),
 (lambda l,g,s: l.startswith('About PROTOTYPE'),                         'YOU MIGHT WONDER'),
 (lambda l,g,s: l.startswith('Header vs Implementation'),                'INSIGHT'),
 (lambda l,g,s: l.startswith('Why Signed Errors Matter'),                'LEARN'),
 (lambda l,g,s: l.startswith('Did Your Robot Wiggle'),                   'CHECKPOINT'),
 # ===== S112: the 39 blocks that used to be resolved by HEX =====
 # DJ ruling, from reading every one of them. Each is placed by WHAT IT SAYS.
 #
 # The colour table these replace is DELETED below. It had resolved 252 blocks, and it
 # concealed a real split: thirteen L12 blocks wore one glyph and one green and were THREE
 # families - eight conceptual payoffs, three byte-count build reports, two observed-
 # behaviour blocks. S94 had already ruled a byte-count report is STILL GREEN and 16
 # elsewhere are filed that way; these three read as INSIGHT purely because they shared
 # paint with their neighbours. The ruling was right, the colour overrode it, and nothing
 # but reading them would ever have shown it.
 #
 # Every prefix below was checked to match EXACTLY ONE block book-wide before being written.
 # Family comes from CONTENT, so the mark and the colour are both OUTPUTS of the family -
 # which is the order that survives the emoji-to-mark conversion.
 # --- KEY TERM  (10) ---
 (lambda l,g,s,_p='IMU (Inertial Measurement Unit) The chip on ': l.startswith(_p), 'KEY TERM'), # L12:1352
 (lambda l,g,s,_p='Gyroscope Measures rotation rate - how fast ': l.startswith(_p), 'KEY TERM'), # L12:1353
 (lambda l,g,s,_p='Bias / Drift The rotation a gyro reports whe': l.startswith(_p), 'KEY TERM'), # L12:1354
 (lambda l,g,s,_p='Calibration (of a gyro) Measuring the bias b': l.startswith(_p), 'KEY TERM'), # L12:1355
 (lambda l,g,s,_p='Integration (accumulation) Adding up a rate ': l.startswith(_p), 'KEY TERM'), # L12:1356
 (lambda l,g,s,_p='Dead reckoning Working out where you are fro': l.startswith(_p), 'KEY TERM'), # L12:1357
 (lambda l,g,s,_p='Wheel slip The wheel turns but the robot doe': l.startswith(_p), 'KEY TERM'), # L12:1358
 (lambda l,g,s,_p='Open loop / Closed loop Open: command it and': l.startswith(_p), 'KEY TERM'), # L12:1359
 (lambda l,g,s,_p='I2C A two-wire bus ( SDA , SCL ) that chips ': l.startswith(_p), 'KEY TERM'), # L12:1360
 (lambda l,g,s,_p='Fixed-point Storing a fractional value in an': l.startswith(_p), 'KEY TERM'), # L12:1361
 # --- LEARN  (4) ---
 (lambda l,g,s,_p="The five data types you'll meet A data type ": l.startswith(_p), 'LEARN'), # L02:691
 (lambda l,g,s,_p='A bool that outlives one trip through the lo': l.startswith(_p), 'LEARN'), # L04:1301
 (lambda l,g,s,_p='abs() - throw away the sign, keep the size a': l.startswith(_p), 'LEARN'), # L04:1342
 (lambda l,g,s,_p='The deadband - a band where the robot does n': l.startswith(_p), 'LEARN'), # L04:1354
 # --- CHECKPOINT  (5) ---
 (lambda l,g,s,_p='Setup & Display ☐ Robot power is ON ☐ OLED s': l.startswith(_p), 'CHECKPOINT'), # L03:2494
 (lambda l,g,s,_p='Serial Monitor ☐ Welcome banner appears the ': l.startswith(_p), 'CHECKPOINT'), # L03:2514
 (lambda l,g,s,_p='Button Tests ☐ Button A: Each press decrease': l.startswith(_p), 'CHECKPOINT'), # L03:2530
 (lambda l,g,s,_p='Motor Test (Button B) ☐ Press shows test par': l.startswith(_p), 'CHECKPOINT'), # L03:2548
 (lambda l,g,s,_p='Motor Behavior ☐ Both motors spin when test ': l.startswith(_p), 'CHECKPOINT'), # L03:2572
 # --- INSIGHT  (14) ---
 (lambda l,g,s,_p='The lesson worth keeping. Sometimes the corr': l.startswith(_p), 'INSIGHT'), # L11:205
 (lambda l,g,s,_p='The function kept its name, its call site, a': l.startswith(_p), 'INSIGHT'), # L11:464
 (lambda l,g,s,_p='The stopwatch has no readers left. Retire it': l.startswith(_p), 'INSIGHT'), # L11:520
 (lambda l,g,s,_p='Leaving the state IS the reset. The odometer': l.startswith(_p), 'INSIGHT'), # L11:636
 (lambda l,g,s,_p='The track did not change. The battery did. O': l.startswith(_p), 'INSIGHT'), # L11:680
 (lambda l,g,s,_p='This is what arithmetic is FOR. It did not j': l.startswith(_p), 'INSIGHT'), # L11:798
 (lambda l,g,s,_p='This is the deepest idea in the lesson. You ': l.startswith(_p), 'INSIGHT'), # L12:281
 (lambda l,g,s,_p='The IMU is the only free sensor on this robo': l.startswith(_p), 'INSIGHT'), # L12:325
 (lambda l,g,s,_p='You just upgraded every turn in the entire b': l.startswith(_p), 'INSIGHT'), # L12:455
 (lambda l,g,s,_p='You have written the truth. The robot is sti': l.startswith(_p), 'INSIGHT'), # L12:671
 (lambda l,g,s,_p='Neither sensor can detect slip. Together, th': l.startswith(_p), 'INSIGHT'), # L12:948
 (lambda l,g,s,_p='The overflow bug IS the feature. Turn 360° a': l.startswith(_p), 'INSIGHT'), # L12:967
 (lambda l,g,s,_p='Read that code again and notice what it is d': l.startswith(_p), 'INSIGHT'), # L12:1154
 (lambda l,g,s,_p='The one sentence to walk out with A sensor c': l.startswith(_p), 'INSIGHT'), # L12:1334
 # --- STILL GREEN  (3) ---
 (lambda l,g,s,_p='Build it now. The binary just grew by 800 by': l.startswith(_p), 'STILL GREEN'), # L12:598
 (lambda l,g,s,_p='Build it. 21,342 → 24,534 bytes. +3,192. Tha': l.startswith(_p), 'STILL GREEN'), # L12:705
 (lambda l,g,s,_p='And look at the byte count: 20,626 → 20,422.': l.startswith(_p), 'STILL GREEN'), # L12:780
 # --- WHAT YOU SHOULD SEE  (2) ---
 (lambda l,g,s,_p='The robot turns 90 degrees. On the slick sur': l.startswith(_p), 'WHAT YOU SHOULD SEE'), # L12:844
 (lambda l,g,s,_p='Button C on delrin: the square closes. Same ': l.startswith(_p), 'WHAT YOU SHOULD SEE'), # L12:890
 # --- THINK ABOUT IT  (1) ---
 # DJ ruling S112. The last block in the book resolved by neither label nor glyph. It had
 # been filed STILL GREEN since the map existed, by COLOUR alone, and STILL GREEN is the
 # byte-count-report family - a rhetorical question is not a byte-count report. The S111
 # repaint did not break this assignment, it exposed that the assignment was never earned.
 (lambda l,g,s,_p='How long does one pass through your loop act': l.startswith(_p), 'THINK ABOUT IT'), # L15:295
 # --- REAL-WORLD CONNECTION  (1) ---
 (lambda l,g,s,_p='The Triple Crown. Fastest, champion, AND bes': l.startswith(_p), 'REAL-WORLD CONNECTION'), # L16:1212
]
# The glyph+scheme COLOUR fallback was DELETED at S112. It resolved 252 of 1,048 blocks by
# HEX, so a quarter of this map moved whenever the book was repainted - and at S111 it did:
# one block fell out silently and no gate could say so. Its 39 survivors are content rules
# above; the other 213 are settled by the GLYPH tier, itself a stopgap until the 41
# generated marks replace the emoji.
# GLYPH-ONLY fallback for the 213 header-less blocks the content rules do not name.
# Measured: each of these thirteen glyphs resolves to exactly ONE family across every block
# that reaches this tier, so the hex was never evidence for them - only corroboration, and
# corroboration that breaks on repaint is a liability. This tier is a STOPGAP: 41 marks are
# generated in images/marks/ and none are wired in yet, so when the emoji are replaced the
# family must already be known from content and the mark must follow from the family.
GLYPH = {
    '🔑': 'KEY TERM', '🛑': 'THE WALL', '⚠': 'WARNING',
    '🔬': 'GOING DEEPER', '📘': 'NOTE', '📖': 'LEARN',
    '🎯': 'TRY THIS', '👀': 'WHAT YOU SHOULD SEE',
    '📓': "ENGINEER'S LOG", '🔍': 'INSIGHT',
    '🔌': "IF YOU'RE STUCK", '💾': 'NOTE', '💡': 'TIP',
}
res=collections.Counter(); unk=[]
for inv in d:
    for c in inv['callouts']:
        lab=norm(c.get('label')); g=(c.get('glyph') or '').strip()
        bg=c['bg'] or 'none'; bd=c['border']
        f=next((fam for fam in CANON if lab.upper().startswith(fam)),None)
        if not f:
            for fn,fam in RULE:
                if fn(lab,g,(bg,bd)): f=fam; break
        if not f: f=GLYPH.get(g)
        if f: res[f]+=1
        else: unk.append((inv['lesson'],c['line'],g,bg,bd,lab[:52]))
print(f"{'FAMILY':26} BLK")
for f,n in res.most_common(): print(f"{f:26} {n:4}")
print(f"\nassigned {sum(res.values())} / 1069   families {len(res)}")
print(f"UNASSIGNED: {len(unk)}")
for u in unk[:40]: print("   L%s %s %s [%s/%s] %s"%u)
json.dump({'counts':res.most_common(),'unk':unk},open('/tmp/final.json','w'))
