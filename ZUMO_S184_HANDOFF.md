# ZUMO — S184 HANDOFF (written at S183 close · paste at top of Session 184)

## READ THIS FIRST

**S183's work IS PUSHABLE and DJ verifies the push himself (standing ruling, S158).**
`git rm ZUMO_S183_HANDOFF.md` is part of that push. If `__pycache__/` exists, delete it LAST —
it regenerates on every gate run.

**78/78 gates** · `gate_payload_match` **PASS**, advisory unmoved at **635** · `quiz_bank --check`
**16 banks valid** · `byte_audit` **0 of 221 figures moved across TWO independent recompiles**, all
eight standing controls exact, `--selftest` ALL CONTROLS, `--check` and `--discards` PASS (15 over
7, all adjudicated) · `build_css`/`image_audit`/`build_worklist --check` current · `callout_id`
**1133** · `strip_inline --verify` **0 dead** · `session_versions --currency` **0 unbumped**.

**AFTER THE PUSH, WAIT PAST THE LONGEST RECENT BUILD BEFORE BELIEVING A STALE READING.** See §2.

---

# 1. WHAT S183 DID

**§18.3b — A RETIRED-NAME LIST IS AN ALLOWLIST.** S182 retired `STATE VARIABLES` and swept for that
spelling. **`LINE FOLLOWING STATE` and `ROBOT STATE` ARE that section** — both hold only mutable
file-scope declarations in the pre-`SETUP` slot — **and neither contains the string the sweep looked
for.** S167's word-list rule in a new costume: a predicate enumerated from the vocabulary you
already have cannot report the members you never named.

**THE POPULATION IS WHAT FOUND IT (§24.22).** 208 banner occurrences across 81 blocks in 13 lessons
(L11, L14, L15 print none), enumerated TAG-STRIPPED — every banner wears a `tok-` span and L10's
wears a *different* one, so a markup-keyed predicate would have measured its own assumption.
**57 of 57 canon-banner blocks in canon ORDER, 0 repeats, 0 printed retired names** — a real zero
over an enumerated denominator.

**140 SITES RENAMED** (136 payload + 4 lesson), 0 leftover, Maker closing on 67 + 136 = **203**.
**DJ ruled it book-wide**, which overrides the L13–L16 freeze for this pass: only 8 of 136 sites are
in L01–L08, and a partial rename moves the inconsistency one lesson later instead of removing it.

**§18.3c — EVERY FILE NAMES ITS PROJECT, ITS FILE AND ITS AUTHOR (DJ ruling).** ONE generator change
(`idFields()` + `stampBox()` in `extraFiles()`), **not 1,295 payload edits**. DJ ruled KEEP THE
CURRENT BOX, so the stamp splices in and each file's own description stays where its author put it.
1,074 of 1,074 verified, idempotent, and the real functions were **executed headlessly against the
real payloads** — a port of the logic is not the logic.

**THE INSERTION POINT IS THE CLOSING DIVIDER, FOUND FROM THE END OF THE BLOCK COMMENT.**
`RobotSensors.cpp` opens with `#include <Wire.h>` ABOVE its box; a top-down divider count lands in
the wrong place on precisely that file.

---

# 2. WHAT WAS WRONG AND HOW IT WAS CAUGHT — ALL FOUR BY CONTROLS, NONE BY RE-READING

**1. A BOX CENSUS REPORTED 79 MISSING HEADER BOXES. THE TRUE FIGURE IS ZERO.** The predicate
required the box at offset 0. Re-predicated on the box appearing anywhere in the opening region and
**controlled both ways** — known-good positive, box-stripped negative — 1,074 of 1,074 have one.

**2. `INCLUDES` APPEARS ONCE IN THE MAKER AGAINST 67 FOR `GLOBAL VARIABLES`**, which read as 220
missing banners. `mainCpp()` GENERATES it unconditionally and hoists payload-leading includes into
it. **The count was measuring the generator.**

**3. L01's ELEVEN CHALLENGE FILES CARRY A `┌───` BOX AND ALSO RECEIVE THE GENERATED HEAD.** Not a
double header — that is the CHALLENGE INSTRUCTION box (§11, S56), the same content
`gate_payload_match` already carries as its 635 advisory.

**4. AND THE SESSION OPENED BY MISDIAGNOSING A CORRECT MEASUREMENT.** Nine changed lessons measured
stale on the published site, **controlled against seven unchanged lessons that matched byte-for-byte
and against the prior commit, which they matched exactly.** The measurement was right; the inference
— *the deploy never ran* — was wrong. `ecf4f62` was pushed at 15:58 EDT and run **#943 took 9m 14s**,
so both readings fell INSIDE the build window and Pages was serving the prior build, as it does.

**S166's *run it twice* CONVENTION DID NOT HELP, AND THE REASON SHARPENS IT: two readings ninety
seconds apart inside a nine-minute build are ONE reading.** Recent deploys run 8m 15s to 9m 14s.
**The convention needs a TIME FLOOR, not a run count** — check the Actions tab for the longest
recent build and wait past it before believing a stale reading.

---

# 3. S184 OPENS HERE

**THE GPT LIST IS STILL THE ASSIGNMENT. DJ: *"I can't ship a book with errors in it."***
**DJ's S182 scope ruling stands: NO further work on L13–L16 until L01–L08 are done** — the S183
rename is the one deliberate exception, mechanical and comment-only, and it is recorded as such.

## THE RULED-BUT-UNBUILT PASS, AND IT CAN MOVE BYTES

**DJ ruled S183: the empty sections keep their banner and NAME THEIR DESTINATION** —
`// ===== CONSTANTS ===== (moved to RobotConfig.h)` — rather than the book's existing
`(none needed)`. The empty banner stops being dead weight and becomes a standing reminder of the
reorganisation L07 spends a whole lesson teaching.

**COUPLED TO IT, AND LARGER: L08, L09 AND L10 DEFINE `showStatus()`, `followLine()` AND
`handleGap()` ABOVE `setup()`** — the exact layout §18.3a reversed — surviving because S182's pass
covered the six SINGLE-FILE lessons. Fixing it moves function bodies below `loop()` and adds the
prototypes that then become load-bearing. **This is the L03 fix again at larger scale.**

**PRICE IT BEFORE RULING IT (rule 70), AND EXPECT RED IN THE MIDDLE:** every intermediate state of a
rollout like this is red by construction — S157 measured 306 findings between two green endpoints.
Do not read that as a defect, and do not open it at the tail of a session.

## `prose_canon.py` IS STILL OWED

**Arm 1 found a real defect this session and found it as a THROWAWAY enumerator**, so the arm that
found it is not repeatable — the same shape §24.22 recorded at S182. The four arms are: printed
banner sequences vs canon · placement claims · retired names · section-count claims.
**Do not ship it without a control per arm** — plant a stale claim and confirm it fires, plant a
legitimate one and confirm it is SILENT (§16.50).

**THE RESIDUE PIN TABLE IS NOW PARTLY DERIVED.** S183's enumeration classified the 20 unclassified
banner names: eighteen are legitimate in two classes — the L07+ multi-file split
(`EXTERN HARDWARE DECLARATIONS`, `HARDWARE OBJECT DEFINITIONS`, `FUNCTION IMPLEMENTATIONS`,
`RobotConfig.h`'s sub-banners) and sub-banners INSIDE `setup()` (`BATTERY REPORT`,
`LINE SENSOR SETUP`, `SAFETY GATE`, `CALIBRATION`). `MY PLAN` and `YOUR CAPSTONE GOES HERE` are the
other two. **Note `MY PLAN` still matches a name-requiring banner regex** — S182's tightening does
not exclude it, so it needs an explicit pin rather than a reliance on that tightening.

**THE GAP IT CLOSES IS UNCHANGED: ALL 78 GATES RUN PAYLOAD → LESSON.** `gate_payload_match` is a
SUBSET test (§16.45). Every S182 defect and S183's rename defect travelled lesson → canon.

## STANDING, UNCHANGED
- **`gate_payload_match` IS STILL NOT ONE OF THE 78** (S137).
- **`byte_audit` ARM 2 CANNOT SEE A FIGURE IN PROSE.**
- **A GATE FOR `GPT_WORKLIST.md`** (S174). **§16.32–§16.44 STILL HAVE NO NUMBERED BODIES.**
- **A BIBLE SESSION BUMP IS A REGENERATION OBLIGATION** (S175) — it fired again at S183 and the
  whole diff was the stamp line, S182 → S183.
- **Fall launch Sept 8.**

# HARNESS — NOT IN THE REPO. RUN THE SCRIPT.

```
apt-get install -y gcc-avr avr-libc
sh harness_setup.sh                     # objects: 41  AND  core stderr: clean
python3 byte_audit.py --sizes           # ~4 min at 221 payloads
python3 byte_audit.py --selftest ; --check ; --discards
```
**`--selftest` CANNOT RUN BEFORE `--sizes`** — CONTROL K reaches for `16/finished` in the size table
and dies with a `KeyError`. The setup script's closing text implies otherwise. It does not.

**NOTE: `gate_payload_match.py` TAKES ARGUMENTS.** Bare, it dies with an `IndexError` on `args[0]`.
Run `python3 gate_payload_match.py newproject.html lessons/Lesson_*.html`.

**STANDING CONTROLS, ALL REPRODUCED S183:** `11/after_step_1` **20,592** · `11/finished` **20,778** ·
`12/finished` **24,790** · `12/c2_slipalarm` **21,334** · `13/finished` **25,248** ·
`14/finished` **26,002** · `15/finished` **28,406** · `16/finished` **28,626**.

# STANDING AUTHORITY — §24.17, §24.19, §24.21
**Decide and report; do not ask.** Carve-outs: facts about the ROOM · irreversible moves · RoboLore
brand and course scope. **§24.19 is the tiebreaker** — what is best for student learning.

---
<!-- VERSION BLOCK: emitted by session_versions.py --handoff. Never hand-typed. -->
Fresh-clone verified at **`ecf4f62`**. Census **41,743**.
Bible **v8.178** · `BookComponentStandard` **v01.13.0** · Maker **v2.67** ·
`marks/` **41** · `icons/` **49** incl. LICENSE.
`ZUMO_Syllabus_WORKING.md` **v1.3**.

Instruments: `book_gates` **v1.72.19** · `lesson_inventory` **v1.3.5** ·
`gen_component` **v1.6.1** · `pill_sweep` **v1.1** · `gate_payload_match` **v1.9.2** ·
`build_family_map` **v1.6.6.3** · `callout_id` **v1.0** · `keyterm_prefix` **v1.0.1** · `build_mark_index` **v1.1.0** · `gen_bonus_banner` **v1.4.1** ·
`gen_part_banners` **v1.2** · `session_versions` **v1.30.2** · `fit_raster_svg` **v1.2** ·
`flatten_alpha` **v1.2** · `svg_layout_audit` **v1.20** · `site_parity` **v1.2.1** ·
`build_css` **v1.4.0** ·
`image_audit` **v1.3** ·
`strip_inline` **v1.2** ·
`build_worklist` **v1.2** ·
`regex_audit` **v1.0** ·
`byte_audit` **v1.9.1** ·
`build_palette` **v1.1** ·
`class_sweep` **v1.0** ·
`color_index` **v1.0** ·
`entity_sweep` **v1.0** ·
`font_stack_sweep` **v1.3.0** ·
`next_pointer` **v1.2** ·
`family_tag` **v1.2.1** ·
`glossary_convert` **v1.0** ·
`mark_wire` **v1.0.2** ·
`glyph_scan` **v1.1** ·
`title_feed` **v1.0** ·
`quiz_bank` **v1.6.1** ·
`timer.html` **v1.3.2** ·
`harness_setup.sh` **v1.1** ·
`pio_harness.sh` **v3.1** ·
`going_deeper` **v01.6.1**.

Lessons: L01 v03.31.4 · L02 v03.25.0 · L03 v03.46.1 · L04 v04.29.5 · L05 v04.29.3 · L06 v04.34.0 · L07 v04.31.8 · L08 v04.32.2 · L09 v05.27.5 · L10 v02.30.4 · L11 v02.31.1 · L12 v01.35.2 · L13 v02.39.0 · L14 v02.36.2 · L15 v02.32.0 · L16 v02.28.1.
