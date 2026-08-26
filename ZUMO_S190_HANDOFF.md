# ZUMO — S190 HANDOFF (written at S189 close · paste at top of Session 190)

## READ THIS FIRST

**S189's work IS PUSHABLE and DJ verifies the push himself (standing ruling, S158).**
`git rm ZUMO_S189_HANDOFF.md` is part of that push and **`ZUMO_S190_HANDOFF.md` IS A NEW FILE** —
both are checkboxes in GitHub Desktop, which is where the deletion and the new file get missed.
If `__pycache__/` exists, delete it LAST; it regenerates on every gate run.

**`site_parity` IS OWED AFTER THIS PUSH.** Build floor is **10m57s**. Run it past the floor at
S190 open, **twice**, and believe the repeat. Inside the window a PASS can be the OLD site
agreeing with itself.

**`byte_audit` IS OWED NOTHING.** It was RUN this session on a harness built from scratch
(`objects: 41`, core stderr clean) because a payload VALUE changed. **All eight standing controls
reproduced EXACT, control first (rule 30):** `11/after_step_1` **20,592** · `11/finished` **20,778** ·
`12/finished` **24,790** · `12/c2_slipalarm` **21,334** · `13/finished` **25,248** ·
`14/finished` **26,002** · `15/finished` **28,406** · `16/finished` **28,626**. 221 payloads
compiled, `--check` PASS, `--selftest` ALL CONTROLS PASS, `--discards` **15 over 7 of 110,
7 adjudicated, 0 unexplained**. **The 85.0 → 98.0 revalue moved zero bytes — measured, not assumed.**

**80/80 gates** · `gate_payload_match` **PASS**, advisory unmoved at **635** · `retired_claims`
**CLEAN**, 12 registered · `prose_canon` **0 new / 7 pinned / 0 orphan** · `quiz_bank --check`
**16 banks valid** · `callout_id` **1133/0** · `strip_inline --verify` **0 dead** · `build_css`
**574 rules** · `image_audit` current · `build_worklist --check` current ·
`session_versions --check` agrees, `--currency` **0 unbumped**.

---

# 1. WHAT S189 DID

## `L06-07` CLOSED — AND THE VALUE WAS WRONG ON THE SAME AXIS AS THE NAME

GPT filed a terminology objection. Measured, **`WHEEL_BASE_MM = 85.0` was the FORE-AFT
drive-to-idler sprocket spacing being used as the SIDE-TO-SIDE pivot width.** DJ named it:
*"96 is the width. I was saying 85 or 86 for the distance between front of track and back of
track."* **Bible §16.10's table is where it was canonised**, sourced to *"Pololu product pages"*.
**A wrong name over a wrong value is internally consistent — that is why it survived 189 sessions.**

**THE RULING COULD NOT BE EXECUTED AS FIRST STATED, AND SAYING SO IS THE POINT.** Pololu publishes
no figure for this quantity: their library carries **ZERO dimension constants** and turns by GYRO;
the guide gives only the 98 × 86 × 39 mm envelope. **98 is a CALIBRATION DEFAULT, not a geometry
claim** — Pololu-published AND the floor of the book's own tuned range. **DO NOT RESTORE 85.**

**372 sites.** Maker 328 · L06 ×13 · L07 ×15 · L08 ×4 · L09 ×5 · banks · TDP · Bible.
Cascade DERIVED (π cancels): 267.0 → **307.9 mm**, 5.50744 → **6.34976**, L12 496 → **571**.

**Students no longer measure it.** TDP A4's verification is now a tuning record; the four-turn
square survives as a CHECK, so M3a is untouched.

## §24.6c THREE TIMES IN ONE SESSION

Keying on `WHEEL_BASE_MM` missed five L06 prose sites written *wheel base* / *85mm*. The concept
sweep that caught those still missed `5.5 counts/degree` and `(85 × π × 909.7)`. **Only a
DERIVED-ARITHMETIC sweep closed it**, and it found `L06_B19` — a keyed correct answer of *About
5.5* unreachable by any keyword predicate. **When a constant changes, sweep the values its
arithmetic PRODUCES, not the identifier's spelling.**

## TWO BANK RULINGS

**`L06_B20` DROPPED** (premise deleted by the ruling; concept graded 4× elsewhere). Bank 78 → 77.
**`L07_B47` RE-STEMMED** — it keyed FALSE on *98–115 is the value to type in*, and once 98 IS the
default a student answering TRUE reads correctly and is marked wrong. **v8.130 from a new
direction: a correct edit can falsify a fair question.**

## THE RED GATE WAS §24.18 AND MY HYPOTHESIS WAS WRONG

I predicted §27.11 and labelled it a hypothesis. It was **§24.18**: 22 `source:` pins stale across
10 banks. **The read was MACHINE-CLOSED (rule 37):** 63 hits, **45 of them `§5.5` — a SECTION
NUMBER, not the figure** (§16.15); bare numeric `5.5` **zero**. Twelve banks assert nothing, so
their pins were EARNED.

## THE STALE-COUNT DEBT FROM SESSION OPEN, CLOSED

`ZUMO_GPT_REVIEW_WORKLIST.md` held the row count in **THREE homes at three different numbers** —
header 66/177, prose **186 (stale since S182)**, table 64/179 (stale since S188). **§24.24 on the
worklist itself.** Derived: 245 ids, 68 Part 0 rows less two untagged = 66. Now **67 / 2 / 176**
everywhere, TOTAL re-derived from its own rows.

---

# 2. S190 OPENS HERE

**THE GPT LIST IS THE ASSIGNMENT. DJ: *"I can't ship a book with errors in it."***
**DJ's S182 scope ruling stands: L01–L08 before L13–L16. Fall launch is September 8.**

## THE IN-SCOPE REMAINDER
**L06 ×6 · L07 ×10 · L08 ×14.** Part 0 reads **67 closed / 176 open**.

## THE OBVIOUS NEXT MOVES
1. **L06's remaining ×6**, including `L06-08` (§8A re-teaches *what IS a function?* — DJ's call,
   GPT's reframe is strong) and `L06-05` / `L06-06`, both marked AGREE.
2. **The 7 pinned `prose_canon` residue sites** — three L05/L06 lesson headings and four Maker
   labels, **ONE fix, not two**. Untouched again this session.
3. **APPEND TO THE REGISTRY WHEN YOU CLOSE A ROW**, measuring the claim at zero in the assertive
   register first. **`retired_claims` gained nothing this session and arguably should have** —
   *wheel base* as a turning term is exactly a retirement.
4. **`prose_canon` arms 1, 2 and 4** — still unbuilt. No arm without a control per direction.
5. **Seat the §16 debt.** Still 26 rules, untouched for a third session.
6. **`L07_GRAPHIC_7-15`'s one real overflow** — `RobotSensors.h`, 14.5 units.

## THE BENCH SHEET NOW RANKS ITSELF — AND A CLAIM I MADE TO DJ WAS WRONG

**`ZUMO_BENCH_TESTS.md` v1.5 opens with the SEVEN rows whose failure deletes or rewrites live
prose.** Every other row records a number. A bench session that runs only those seven is worth
more than one that fills in twenty.

**THE ERROR, RECORDED BECAUSE IT IS THE REUSABLE PART.** I told DJ that `L02-B2` and `L03-B3b`
were **the only** rows where a failure deletes prose. That figure comes from
`ZUMO_FLAGGED_CHECKS.md`, which is **the L01–L04 working sheet** — and I generalised a
sheet-scoped count to the whole book without re-measuring. **The footer of that very file, eleven
lines below the sentence I quoted, already named `L10-B1` as a third.** I read the claim and not
the end of the document. A scope clause is now in that file so the next reader cannot repeat it.

**TRIPLE-CHECKED, THREE INDEPENDENT ARMS (rule 83/84 — not three readings of one predicate):**
(1) a semantic read of all **49** open rows; (2) an independent linguistic predicate for
falsifiability, **with a blinding control proving it does not fire on any record-a-number row**;
(3) a cross-check against `ZUMO_FLAGGED_CHECKS.md`. **Arms 2 and 3 agree at seven.** Arm 1 raised
two more — `L13-B3` and `L15-B4` — which are listed as BORDERLINE and deliberately not ranked,
because they expose a CODE defect rather than a false sentence.

**RANKED: 1 `L10-B1` (THE BIG ONE, §16.12, unruled since S143) · 2 `L02-B2` · 3 `L03-B3b` ·
4 `L15-B3` · 5 `L11-B1` · 6 `L11-B4` · 7 `L10-B2`.** Run 1, 2 and 7 in one sitting — `L10-B1` and
`L10-B2` are the same question asked two ways.

**ALSO CORRECTED: `L06-B3`'s premise was falsified by S189's own work** and was found only when
DJ asked for the centreline row. It read *"Book gives 85 mm and asks the student to check it."*
Re-premised as a tuning check. **Closing a claim in the lessons does not close it in the
trackers (rule 72).** New row **`L06-B6`** carries DJ's centreline measurement.

## OPEN, RECORDED NOT FIXED
- **`ZUMO_QUIZ_L12`'s header note now says the truncation artifact is 6.35 × 90 = 571.5 vs an int
  cast of 571.** The OLD note claimed the lesson's 496 was right where 85 gives 495.67 — a
  round-UP the C++ int cast does not do. **The book's 571 matches the cast; the pre-existing
  rounding convention was not re-litigated.** If DJ wants the lesson to state 571.48 or to teach
  the truncation, that is a ruling.
- **L12 was fixed though it is out of Fall scope** (DJ: *"fix both"*), so the arithmetic is
  consistent book-wide rather than L14-style stale.

## STANDING, UNCHANGED
- **`gate_payload_match` IS NOT ONE OF THE GATES** (S137) and **TAKES ARGUMENTS**.
- **`--live` and `--handoff` PRINT, they do not WRITE** (§24.20). **LIVE.md carries TWO
  `**Versions:**` lines** — line 6 is current, line 4742 is history. Edit line 6 only.
- **The visible §5b banner is spelled `Version 04.31` — BARE, where the hidden comment carries the
  `v`.** A `v`-prefixed grep cannot see it. `session_versions --check` can.
- **`quiz_bank.py` LIVES IN `quizzes/`, NOT THE REPO ROOT.**
- **A BIBLE SESSION BUMP IS A REGENERATION OBLIGATION** (S175) — fired, and measured: the
  `GPT_WORKLIST.md` diff was the stamp line alone, S188 → S189.
- **Syllabus dates still `[TBD]`; the day-by-day period grid is unbuilt.**

# HARNESS — NOT IN THE REPO. RUN THE SCRIPT.

```
apt-get install -y gcc-avr avr-libc
sh harness_setup.sh                     # objects: 41  AND  core stderr: clean
python3 byte_audit.py --sizes           # ~4 min at 221 payloads
python3 byte_audit.py --selftest ; --check ; --discards
```
**`--selftest` CANNOT RUN BEFORE `--sizes`** — CONTROL K dies with a `KeyError`.

# STANDING AUTHORITY — §24.17, §24.19, §24.21
**Decide and report; do not ask.** Carve-outs: facts about the ROOM · irreversible moves ·
RoboLore brand and course scope. **§24.19 is the tiebreaker** — what is best for student learning.

---
<!-- VERSION BLOCK: emitted by session_versions.py --handoff. Never hand-typed. -->
Fresh-clone verified at **`95349b5`**. Census **41,712**.
Bible **v8.185** · `BookComponentStandard` **v01.13.0** · Maker **v2.68** ·
`marks/` **41** · `icons/` **49** incl. LICENSE.
`ZUMO_Syllabus_WORKING.md` **v1.3**.

Instruments: `book_gates` **v1.74.2** · `lesson_inventory` **v1.3.5** ·
`gen_component` **v1.6.1** · `pill_sweep` **v1.1** · `gate_payload_match` **v1.9.4** ·
`build_family_map` **v1.6.6.3** · `callout_id` **v1.0** · `keyterm_prefix` **v1.0.1** · `build_mark_index` **v1.1.0** · `gen_bonus_banner` **v1.4.1** ·
`gen_part_banners` **v1.2** · `session_versions` **v1.32.1** · `fit_raster_svg` **v1.2** ·
`flatten_alpha` **v1.2** · `svg_layout_audit` **v1.21.2** · `site_parity` **v1.2.1** ·
`build_css` **v1.4.0** ·
`image_audit` **v1.3** ·
`strip_inline` **v1.2** ·
`build_worklist` **v1.2** ·
`prose_canon` **v1.1.0** ·
`retired_claims` **v1.0.1** ·
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

Lessons: L01 v03.32.1 · L02 v03.26.1 · L03 v03.47.0 · L04 v04.29.6 · L05 v04.30.0 · L06 v04.36.0 · L07 v04.32.0 · L08 v04.33.0 · L09 v05.27.6 · L10 v02.30.4 · L11 v02.31.1 · L12 v01.35.3 · L13 v02.39.0 · L14 v02.36.2 · L15 v02.32.0 · L16 v02.28.1.
