# ZUMO — S191 HANDOFF (written at S190 close · paste at top of Session 191)

## READ THIS FIRST

**S190's work IS PUSHABLE and DJ verifies the push himself (standing ruling, S158).**
`git rm ZUMO_S190_HANDOFF.md` is part of that push and **`ZUMO_S191_HANDOFF.md` IS A NEW FILE** —
both are checkboxes in GitHub Desktop, which is where the deletion and the new file get missed.
If `__pycache__/` exists, delete it LAST; it regenerates on every gate run.

**`site_parity` IS OWED AFTER THIS PUSH.** Build floor is **10m57s**. Run it past the floor, **twice**,
and believe the repeat. It was discharged at S190 OPEN (PARITY twice, plus a direct fetch of four
published pages) and that discharge does NOT cover this push.

**`byte_audit` IS OWED NOTHING.** Every code edit this session is lesson prose. **Maker payloads did
not move** — the only Maker change is four label strings on the `trapezoidal` row, which keeps its ID.

**80/80 gates** · `gate_payload_match` **PASS**, advisory unmoved at **635** · `retired_claims`
**CLEAN, 17 registered** · `prose_canon` **0 new / 7 pinned / 0 orphan** · `quiz_bank --check`
**16 banks valid** · `callout_id` **1134/0** · `strip_inline --verify` **0 dead** · `build_css`
**574 rules** · `image_audit` current · `build_worklist --check` current.

---

# 1. WHAT S190 DID

**22 GPT ROWS CLOSED: L06 ×1 · L07 ×10 · L08 ×11.** Plus an eight-site code defect nobody filed.

## THE DEFECT NOBODY FILED
`L06-01` was CLOSED at S181 and **its defect was live in two lessons for nine sessions.** S181 keyed on
`speed + TRIM` where `speed` carried the sign; these write `currentSpeed * direction + TRIM`. **L06 ×4
(Smooth Acceleration/Stopping) · L07 ×4 (Challenge 7) · Maker ×0.** **§24.6c: sweep the arithmetic a
correction PRODUCES, not the identifier's spelling.**

## THE SAME SHAPE THREE TIMES IN ONE LESSON
`L07-04` fixed in Error 5b, **survived in §8A.2**. `L07-02` fixed in §3.5 prose, **survived in the KEY
TERM GLOSSARY** — the reference students actually consult. **A retired claim outlives its fix in the
register nobody re-reads.** Five retirements now registered in `retired_claims`, **each plant-tested 5/5**.

## `extern` IS UNCHANGED — SAY SO IF ASKED
2,015 Maker sites · 149 lesson sites · 27 bank questions (42 occurrences), all untouched. Only the false claim that the
LANGUAGE forbids `extern` in a .cpp was retired. The house rule stands.

## TWO COSTS I ASSERTED WITHOUT MEASURING, BOTH CAUGHT BY DJ OR BY A CONTROL
1. **The Parameter glossary twin.** I said insertion renumbers every downstream `data-callout`.
   **`callout_id.py`'s docstring says the opposite** — insertion takes the next free number and nothing
   renumbers. DJ asked *why not*, which is the only reason it was caught. Twin added as **6.69**;
   three baselines moved as ONE event (callout 1134 · glossary 152 · images 1,210), blinding-controlled.
2. **The CSS delta reported as COUNT-ONLY. It is COUNT AND RANK.** The name SET is identical; the
   ORDERED list is not. **A set comparison says count-only and is wrong.** Three digest moves this
   session, each measured with an ordered diff.

---

# 2. S191 OPENS HERE


## `census.py` v1.0.1 IS NEW AND IT IS THE ANSWER TO A QUESTION DJ ASKED FOURTEEN TIMES
**Use it. Do not reach for `grep -c` to produce a number that reaches DJ.**
```
import census
census.questions('extern').report()       # QUESTION IDS, not lines
census.payloads('followLine', filename='main.cpp')   # payload ENTRIES, not tokens
census.occurrences(pat, files) / census.lines(pat, files)   # you must say which
census.agree(a, b)                        # rules 83/84 - disagreement IS the finding
python3 census.py --selftest              # 11 controls
```
**`int(Population)` RAISES on purpose.** A number with no population is how a LINE count gets
reported as a DEFECT count. `len()` works; `report()` names the members.
**It cannot see a terminal (rule 78)** — same hole §24.16 records for checksums.

## RULINGS OWED — BOTH PRICED
1. **`L08-02`** — move `followLine()` into `RobotMotion.cpp`. **135 Maker `main.cpp` payloads**, 461
   Maker sites, 8 lessons. `L08-14`'s clean fix depends on it and the lesson says so.
2. **`L08-06`** — delete dead `lastPosition`. **145 Maker `RobotSensors.cpp` payloads**, 434 sites, and
   the subject of two bank questions about `static`.
Both move bytes and need the `byte_audit` harness.

## THE WORKLIST COUNT MUST BE RECONCILED AND FILED
Deriving over Part 0's ✅ rows gives **87 closed / 2 parked / 156 open of 245**, which **disagrees with
the standing table on L02 (14 vs 17), L04 (3 vs 5) and L13 (14 vs 0)**. The rows are seated and the
discrepancy is written into the file. **Reconcile the two predicates and file ONE derived answer in all
three homes (§24.24, rule 50).** Do this before quoting any remainder figure to DJ.

## THE REMAINDER, AS FAR AS IT IS TRUSTED
**L01–L08 in scope for Fall are DONE except `L08-02` and `L08-06`.** L09–L16 untouched by the sweep.
DJ's S182 scope ruling stands. Fall launch is September 8.

## STILL OWED, UNCHANGED
- **The 7 pinned `prose_canon` residue sites** — three L05/L06 lesson headings and four Maker labels,
  **ONE fix, not two**. Untouched a fourth session.
- **`prose_canon` arms 1, 2 and 4** — unbuilt. No arm without a control per direction.
- **Seat the §16 debt.** Still 26 rules, untouched a fifth session.
- **`L07_GRAPHIC_7-15`'s one real overflow** — `RobotSensors.h`, 14.5 units.
- **`ZUMO_BENCH_TESTS.md` ranks itself.** Run **1 `L10-B1` · 2 `L02-B2` · 7 `L10-B2`** in one sitting.
- **Syllabus dates still `[TBD]`; the day-by-day period grid is unbuilt.**

## L06's GLOSSARY IS NOW ALPHABETICAL — THE OTHERS MAY NOT BE
*Dead Reckoning* and *Track Width* had been appended rather than filed. Fixed line-wise, file length
byte-identical. **No other lesson's glossary was checked.**

## STANDING, UNCHANGED
- **`gate_payload_match` IS NOT ONE OF THE GATES** (S137) and **TAKES ARGUMENTS** — pass
  `newproject.html lessons/Lesson_*.html`, or it reports a COVERAGE failure on a subset.
- **`--live` and `--handoff` PRINT, they do not WRITE** (§24.20). **LIVE.md carries TWO `**Versions:**`
  lines** — line 6 is current. **Keep the Status line to ONE line** or Versions leaves line 6 and
  `session_versions` says so.
- **The visible §5b banner is spelled `Version 04.31` — BARE.** A `v`-prefixed grep cannot see it.
- **`quiz_bank.py` LIVES IN `quizzes/`, NOT THE REPO ROOT.**
- **A BIBLE SESSION BUMP IS A REGENERATION OBLIGATION** (S175) — fired, `GPT_WORKLIST.md` regenerated.
- **A BIBLE BUMP HAS TWO HOMES** (S185): the version line AND the standalone changelog entry
  `current_session()` reads. Both filed; `current_session()` returns **190**.

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
Fresh-clone verified at **`b3f0169`**. Census **41,801**.
Bible **v8.186** · `BookComponentStandard` **v01.13.0** · Maker **v2.69** ·
`marks/` **41** · `icons/` **49** incl. LICENSE.
`ZUMO_Syllabus_WORKING.md` **v1.3**.

Instruments: `book_gates` **v1.74.6** · `lesson_inventory` **v1.3.5** ·
`gen_component` **v1.6.1** · `pill_sweep` **v1.1** · `gate_payload_match` **v1.9.4** ·
`build_family_map` **v1.6.6.5** · `callout_id` **v1.0** · `keyterm_prefix` **v1.0.1** · `build_mark_index` **v1.1.0** · `gen_bonus_banner` **v1.4.1** ·
`gen_part_banners` **v1.2** · `session_versions` **v1.32.2** · `fit_raster_svg` **v1.2** ·
`flatten_alpha` **v1.2** · `svg_layout_audit` **v1.21.2** · `site_parity` **v1.2.1** ·
`build_css` **v1.4.0** ·
`image_audit` **v1.3** ·
`strip_inline` **v1.2** ·
`build_worklist` **v1.2** ·
`prose_canon` **v1.1.0** ·
`retired_claims` **v1.0.2** ·
`census` **v1.0.1** ·
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

Lessons: L01 v03.32.1 · L02 v03.26.1 · L03 v03.47.0 · L04 v04.29.6 · L05 v04.30.0 · L06 v04.37.1 · L07 v04.33.0 · L08 v04.34.0 · L09 v05.27.6 · L10 v02.30.5 · L11 v02.31.3 · L12 v01.35.3 · L13 v02.39.0 · L14 v02.36.2 · L15 v02.32.0 · L16 v02.28.1.
