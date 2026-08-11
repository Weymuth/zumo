#!/usr/bin/env python3
# VERSION is the ONE home, and it sits ABOVE the changelog so a plain grep of this file
# lands on the live version, not on a changelog line (S98). The block below is prose,
# not __doc__ — nothing in the repo reads __doc__ (checked).
VERSION = 'v1.6.3'
# v1.6.3 (S144): the L11 8A.4 INSIGHT tier pinned 'This is what arithmetic is FOR' - and
#   S144 REPLACED that arithmetic, because §3.5's cliff premise was wrong. Repointed to the
#   new headline. No tier logic changed. Second time this session that a literal content
#   tier owed an edit because the SPELLING it pinned was the thing being corrected.
# v1.6.2 (S144): the L11 INSIGHT content rule pinned the headline 'The stopwatch has no
#   readers left' - a SPELLING, and S144 corrected that headline because the claim under it
#   was false (two writes survived, so deleting the declaration broke the build). Repointed,
#   no tier logic changed. The tier is literal by design (last resort, per-block), so a
#   prose fix in a lesson owes this file an edit - that coupling is the cost of the tier.
# v1.6.1 (S141): DENOMINATOR 1119 -> 1120. L06 gained TIP 6.68, the caliper-technique
#   callout in §3.4, when the 35 mm sprocket / 39 mm over-the-track distinction was
#   written in. One legitimate addition, one family (TIP), nothing reclassified.
# v1.5.0 (S132): THE STRUCTURE TIER. A callout inside the GLOSSARY REGION is a KEY TERM.
#   Seated ABOVE the pin, below the content rules, and it is the FIRST tier since S112
#   that is not a content rule and not authored — so the distinction it stands on has to
#   be stated: A SECTION ID IS STRUCTURE, NOT DECORATION. Colour died (S112) and the
#   glyph died (S130) because both were presentation that happened to correlate with
#   family; either could be repainted or reskinned without the family changing, so
#   reading them backwards let a repaint re-family the book. A banner id cannot be
#   repainted. Moving a block out of the glossary is not a restyle, it is a move, and if
#   it moves it SHOULD stop being a KEY TERM. The tier reads what the block IS, not what
#   it looks like — which is §24.14, not an exception to it.
#   MEASURED, and the probe could fail: 97 callouts sit in a glossary region, 97 of 97
#   are KEY TERM, ZERO exceptions. An earlier probe that closed the region at EOF instead
#   of at the next banner returned NINE exceptions (GOING DEEPER and two NOTE blocks
#   sitting past the glossary), so the predicate is discriminating and not vacuous.
#   SUFFICIENT, NOT NECESSARY: 72 KEY TERM blocks live in lesson bodies and this tier
#   says nothing about them. It resolves the glossary side only.
#   WHY IT IS WORTH A TIER: it makes 87 of the pin's 159 KEY TERM rows redundant and it
#   means the 54 non-callout glossary entries can be converted to canon term cards
#   WITHOUT authoring 54 new pin rows. Pin today 212; with the glossary-side rows
#   retired 125; convert with no tier and it is 266. A 141-row swing.
#   BASELINE 1123 -> 1119 (S132, second push). L11's four ANSWER blocks were the only
#   reveals wearing a callout skin; DJ ruled the WORD stays and the box matches every other
#   reveal (§27.15f), so they stop being callouts. CONTROLLED at an identical generator
#   version: exactly ONE family moves, ANSWER 4 -> 0, and the other 29 are byte-identical.
#   The ANSWER family is retired - it had four members in one lesson doing the job L08's six
#   Mystery answers already did as ordinary reveals.
#   BASELINE 1069 -> 1123. The glossary conversion (glossary_convert v1.0) turned 54
#   non-callout entries - L04 bare divs, L13/L14 <dl> pairs, L11/L15 table rows - into
#   canon term cards, so they are callouts now and the map sees them. DERIVED: 1069 + 54.
#   RETIRING THOSE 87 ROWS IS A SEPARATE RULING and is NOT done here — the pin is a
#   preserved layer and this version only makes the rows unnecessary, not absent.
# v1.3.8 (S128): the data-family attribute is read AHEAD of the three inference tiers.
#   Baseline UNMOVED at 1069 - the attribute is written FROM these same tiers, so on the
#   day it landed the table came back byte-identical, which is the correctness proof.
#   What changed is the future: blinding the GLYPH tier now still returns 1069/1069, so
#   the 209 blocks it used to resolve no longer depend on a decorative emoji and the
#   marks arc can replace it. S112 predicted this exact moment in the tier's own comment.
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

def canon_of(lab):
    """The CANON tier, ONE definition (S83). The prefix must end on a WORD BOUNDARY:
    'LEARNING OBJECTIVES' starts with 'LEARN' and is not a LEARN box. Measured inert at
    S133 - across all 1,119 live labels the result changes for zero of them."""
    u = (lab or '').upper()
    return next((f for f in CANON
                 if u.startswith(f) and (len(u) == len(f) or not u[len(f)].isalpha())), None)

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
 # S133: was startswith('OBJECTIVES'), which the S133 rename to 'Learning Objectives'
 # walked straight past. A list of objectives is an OBJECTIVES block whatever adjective
 # precedes the noun - the rule now names the NOUN, which is the content (§24.14).
 (lambda l,g,s: re.search(r'\bOBJECTIVES\b', l.upper()) is not None,      'OBJECTIVES'),
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
 (lambda l,g,s,_p='The stopwatch is retired in three pieces, no': l.startswith(_p), 'INSIGHT'), # L11:520
 (lambda l,g,s,_p='Leaving the state IS the reset. The odometer': l.startswith(_p), 'INSIGHT'), # L11:636
 (lambda l,g,s,_p='The track did not change. The battery did. O': l.startswith(_p), 'INSIGHT'), # L11:680
 (lambda l,g,s,_p='Section 8A.2, four sections early and one wor': l.startswith(_p), 'INSIGHT'), # L11:798
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
# S130: THE GLYPH TIER IS DELETED. IT WAS THE SECOND DECORATION-KEYED TIER TO DIE.
# S112 deleted a COLOUR-keyed fallback when a repaint silently orphaned a block, and the
# replacement was this GLYPH table - decoration standing in for content a second time. The
# marks arc then replaced the emoji and orphaned 212 blocks, the same failure one tier later.
# A tier keyed on decoration is a tier waiting for the next repaint or reskin.
#
# The 212 blocks now resolve from ZUMO_FAMILY_PINS.md, an AUTHORED record keyed on
# `data-callout`. It is READ-ONLY INPUT and must never be regenerated from `data-family`:
# a pin rebuilt from the value it exists to check agrees with any drift by construction.
# ---- THE STRUCTURE TIER (S132). ONE DEFINITION, imported by family_tag rather than
# restated there (S83). The region comes from lesson_inventory v1.3.5, which derives it
# from the banner PROPERTY; nothing here re-parses the file.
STRUCT_REGION = {'glossary': 'KEY TERM'}


def struct(c):
    """The family a callout's REGION implies, or None.

    Returns None for every region but the glossary — a region this table does not name
    is not an assertion that the block has no family, it is silence, and the caller
    falls through to the pin exactly as before.
    """
    return STRUCT_REGION.get(c.get('region'))


PIN_FILE = 'ZUMO_FAMILY_PINS.md'
_PIN_ROW = re.compile(r'^\|\s*`(\d+\.\d+)`\s*\|\s*([^|]+?)\s*\|')


def load_pins(path=PIN_FILE):
    """{data-callout: family} from the preserved pin file.

    A MISSING FILE MUST NOT RAISE. The first draft called SystemExit here, and because
    this module is imported by book_gates (through family_tag), a missing pin killed the
    whole suite MID-RUN and still exited 0 - the run stopped before gates 59 and 60 and
    reported success by exit code. That is the exact failure the session ritual's "read
    the exit code, not the last line" exists to catch, inverted into the exit code itself.
    An absent pin is reported BY GATE 60, which can name it; a library cannot.
    """
    if not os.path.exists(path):
        return {}
    pins = {}
    for line in open(path, encoding='utf-8'):
        m = _PIN_ROW.match(line)
        if m:
            pins[m.group(1)] = m.group(2).strip()
    return pins


PINS = load_pins()
# S128: THE ATTRIBUTE IS READ FIRST, AND IT IS THE REASON THE GLYPH TIER CAN DIE.
# `data-family` is written onto every callout by family_tag.py FROM these same tiers,
# so on the day it landed this changed nothing - proved by the table coming back
# byte-identical. What it changes is the FUTURE: 209 blocks were resolved by the
# decorative emoji alone, and the marks arc replaces that emoji with an <img>. Once
# the glyph goes those blocks would have had no family signal left and gate 47 would
# fail. The family now lives in the markup, where §24.14 says it belongs - CONTENT
# first, mark and colour as OUTPUTS - and the emoji is free to be replaced.
#
# DIRECTION IS LOAD-BEARING: nothing here may ever read the mark filename back to
# recover the family. That would close a loop the canon forbids and would let an icon
# swap silently re-family the book - the S112 colour-table failure in a new costume.
res=collections.Counter(); unk=[]
for inv in d:
    for c in inv['callouts']:
        lab=norm(c.get('label')); g=(c.get('glyph') or '').strip()
        bg=c['bg'] or 'none'; bd=c['border']
        f=c.get('family_attr')
        if not f:
            # S133: the prefix must end on a WORD BOUNDARY. 'LEARNING OBJECTIVES' starts
            # with 'LEARN' and is not a LEARN box - a canon name must match a whole word,
            # not bite into the next one. MEASURED INERT before it was applied: across all
            # 1,119 live labels the result changes for ZERO of them, so this cannot move
            # the map; it only stops a FUTURE label from being claimed by a shorter name.
            f=canon_of(lab)
        if not f:
            for fn,fam in RULE:
                if fn(lab,g,(bg,bd)): f=fam; break
        if not f: f=struct(c)
        if not f: f=PINS.get(c.get('callout_id'))
        if f: res[f]+=1
        else: unk.append((inv['lesson'],c['line'],g,bg,bd,lab[:52]))
print(f"{'FAMILY':26} BLK")
for f,n in res.most_common(): print(f"{f:26} {n:4}")
print(f"\nassigned {sum(res.values())} / 1120   families {len(res)}")
print(f"UNASSIGNED: {len(unk)}")
for u in unk[:40]: print("   L%s %s %s [%s/%s] %s"%u)
json.dump({'counts':res.most_common(),'unk':unk},open('/tmp/final.json','w'))
