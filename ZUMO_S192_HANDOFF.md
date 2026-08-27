# ZUMO — S192 HANDOFF (written at S191 close · paste at top of Session 192)

## READ THIS FIRST

**NOTHING FROM S191 IS PUSHED.** 19 files differ from HEAD (`c8a7c42`), 0 unbumped.
`git rm ZUMO_S191_HANDOFF.md` is part of this push and **`ZUMO_S192_HANDOFF.md` IS A NEW FILE** —
both are checkboxes in GitHub Desktop, which is where the deletion and the new file get missed.
**`newproject.html` is ~5.8 MB and must be renamed on disk and uploaded via the desktop client**,
never the GitHub web UI. If `__pycache__/` exists, delete it LAST; it regenerates on every gate run.

**`site_parity` IS OWED AFTER THE PUSH.** Build floor **10m57s**. Run it past the floor, **twice**,
and believe the repeat. It was discharged at S191 OPEN (PARITY twice, 17:26 and 17:28 UTC, ~21 min
past the 17:05 amendment push) and that discharge does NOT cover this push.

**`byte_audit` IS DISCHARGED AND OWES NOTHING FURTHER.** The one payload-moving edit this session
was measured before and after: **0 flash changes and 0 status changes across 221 payloads**,
blinding-controlled with a planted byte. `--check` PASS · `--selftest` ALL CONTROLS PASS ·
`--discards` 7 adjudicated / 0 unexplained.

**80/80 gates** · `gate_payload_match` **PASS**, advisory unmoved at **635** · `retired_claims`
**CLEAN, 17 registered** · `prose_canon` **0 new / 7 pinned / 0 orphan** · `quiz_bank --check`
**16 banks valid** · `callout_id` **1134/0** · `strip_inline --verify` **0 dead** · `build_css`
**574 rules** · `image_audit` current · `build_worklist --check` current (regenerated, stamp line only).

---

# 1. WHAT S191 DID

**THREE RULINGS EXECUTED: `L08-02`, `L08-06`, AND THE WORKLIST RECONCILIATION.** Plus a defect in
`census.py` — the instrument S190 built to stop exactly this.

## `census.py` PRODUCED A CONFIDENT WRONG NUMBER AND IT NEARLY REACHED AN EDIT
`census.occurrences('lastPosition', 'lessons/Lesson_*.html')` returned **`0 MATCHES`** with full
provenance. **A string is iterable** — `sorted(paths)` walked 24 CHARACTERS, every `open()` raised,
`except: continue` ate all 24. True figure: **6 lines in L08, 1 in L10.** I had concluded *no lesson
surface* for `L08-06` and was minutes from editing on it.
**This is WORSE than `grep -c`: grep says *No such file*; census attached provenance to a zero.**
Caught by rules 83/84 and by accident — grep and census disagreed on an UNRELATED pattern.
**v1.1.0: a string is a GLOB; an unreadable path RAISES.** Controls K1/K2/K3, and the blinding
control is what makes them evidence — grafted onto unfixed v1.0.1 **all three FAIL**, K1 returning
exactly the `0` that fooled me. **14 controls, was 11.**

## `L08-06` SHIPPED — AND THE VARIABLE WAS NOT THE WHOLE EDIT
145 Maker payloads · 7 lesson sites · 2 bank questions. **Three consequences nobody priced:**
1. `LINE_CENTER` had no other code use in `RobotSensors.cpp`, so the `#include` comment naming it
   would have shipped pointing at a constant the file no longer reads (145 Maker + 2 lesson sites).
2. **`L08_B25`'s CORRECT ANSWER became false.** Found only because rule 37 forced a read of all ten
   questions touching `readLinePosition`/`LINE_CENTER` before eight pins could move. Nine were fine.
3. **§8's troubleshooting entry keyed on `'LINE_CENTER' was not declared`** — found by opening the
   file for an unrelated reason. **I swept for the IDENTIFIER, not the arithmetic the fix PRODUCES.
   §24.6c, in the session that quotes it.**

## `L08-02` — GPT'S FIX REFUTED BY MEASUREMENT, THE CONTRADICTION FIXED IN PROSE
Every symbol `followLine()` touches is `main.cpp`-private or a `RobotConfig.h` constant, and two are
deliberately shared inside `main.cpp`: `lastError` → `runSample()`, `dtSec` → `updateSpeedLoop()`
(*One clock, two loops*). `currentKp`/`currentKd`/`currentBase` are the OLED menu's live knobs.
**Moving it either `extern`s six mutable globals — three sections after L08 Step 4 teaches module
state is `static` and private — or puts the tuning UI behind accessors and grows L15's signature to
five parameters.** The defect is **one sentence in L07's vocabulary NOTE**. Fixed there, with L08
Step 7 now stating why. **0 payloads, 0 bytes.**
**`L08-14` does NOT depend on this** — the S190 handoff said it did. It is a `main.cpp`-local
question about sharing one observation, either way.

## THE WORKLIST COUNT IS RECONCILED — **95 closed / 89 fixed / 2 parked / 148 open of 245**
Both predicates were right about different things. S190's 87 dropped **six rows carrying ❌**
(`L02-12`, `L02-19` STRUCK; `L02-07`, `L04-01`, `L04-03`, `L13-17` REFUTED) — the whole of the L02,
L04 and L13 gaps — and **`L08-13` was seated TWICE** (MEASURED S154, SHIPPED S190), a live
exactly-once violation, now merged. **S190 closed 21 rows, not 22: 72 + 21 = 93.**
The `fixed` column now sits beside `closed` in Part 0b, **because a headline showing one of the two
numbers is how this survived nine sessions.**

---

# 2. S192 OPENS HERE

## `L08` HAS TWO OPEN ROWS AND S190 SAID ZERO
**`L08-08`** — the closed-loop-TRIM C1 claim. **`L08-15`** — Challenge 6 "Racing Line" calls the
speed rule a second closed-loop controller; it maps error to a speed command and measures nothing.
Neither is named in any closed or parked table, or in any other file in the repo. **These are the
last two in-scope rows before L09.** L01–L07 are done.

## THE CENSUS-BACKED ASSERTION GATE IS STILL UNBUILT AND S191 STRENGTHENED THE CASE
S190 argued it and priced it at **250 lines, 125 of them code**, on gate 78's existing machinery.
**S191 is the argument's second data point:** census closed the HAND and the wrong zero still came
out, because the hole was in the instrument rather than the caller. A gate asserting population
claims in the session documents against `census` would not have caught this one — **say so in its
docstring (rule 78)** rather than letting the next reader assume it covers everything.
**DJ has still not ruled on priority.** Fall launch is September 8.

## STANDING CONTROL — THE HANDOFF HAD IT WRONG
**It is 20,592, not 20,516.** `byte_audit.STANDING_CONTROL`, CONTROL A and the live compile of
`11/after_step_1` all agree. The S191 handoff carried 20,516; do not propagate it.

## STILL OWED, UNCHANGED
- **The 7 pinned `prose_canon` residue sites** — three L05/L06 lesson headings and four Maker labels,
  **ONE fix, not two**. Untouched a fifth session.
- **`prose_canon` arms 1, 2 and 4** — unbuilt. No arm without a control per direction.
- **Seat the §16 debt.** Still 26 rules, untouched a sixth session.
- **`L07_GRAPHIC_7-15`'s one real overflow** — `RobotSensors.h`, 14.5 units.
- **`ZUMO_BENCH_TESTS.md` ranks itself.** Run **1 `L10-B1` · 2 `L02-B2` · 7 `L10-B2`** in one sitting.
- **Syllabus dates still `[TBD]`; the day-by-day period grid is unbuilt.**
- **`ZUMO_GPT_REVIEW_WORKLIST.md` footer carries a second version token** (`Worklist v1.2`) that
  disagrees with the header home `session_versions` reads (v1.12). Not touched — flagged, not ruled.

## STANDING, UNCHANGED
- **`gate_payload_match` IS NOT ONE OF THE GATES** (S137) and **TAKES ARGUMENTS** — pass
  `newproject.html lessons/Lesson_*.html`, or it reports a COVERAGE failure on a subset.
- **`--live` and `--handoff` PRINT, they do not WRITE** (§24.20). **LIVE.md carries TWO `**Versions:**`
  lines** — line 6 is current. **Keep the Status line to ONE line.**
- **The visible §5b banner is spelled `Version 04.31` — BARE.** A `v`-prefixed grep cannot see it.
- **`quiz_bank.py` LIVES IN `quizzes/`, NOT THE REPO ROOT.**
- **A BIBLE SESSION BUMP IS A REGENERATION OBLIGATION** (S175) — fired, `GPT_WORKLIST.md` regenerated.
- **A BIBLE BUMP HAS TWO HOMES** (S185): the version line AND the standalone changelog entry
  `current_session()` reads. Both filed; `current_session()` returns **191**.

# HARNESS — NOT IN THE REPO. RUN THE SCRIPT.

```
apt-get install -y gcc-avr avr-libc
sh harness_setup.sh                     # objects: 41  AND  core stderr: clean
python3 byte_audit.py --sizes           # ~4 min at 221 payloads
python3 byte_audit.py --selftest ; --check ; --discards
```
**`--selftest` CANNOT RUN BEFORE `--sizes`** — CONTROL K dies with a `KeyError`.
**A backgrounded `harness_setup.sh` died silently at `== core build ==` with 0 objects this session.
Run it in the FOREGROUND and read `objects: 41` before trusting anything downstream.**

# STANDING AUTHORITY — §24.17, §24.19, §24.21
**Decide and report; do not ask.** Carve-outs: facts about the ROOM · irreversible moves ·
RoboLore brand and course scope. **§24.19 is the tiebreaker** — what is best for student learning.

---
<!-- VERSION BLOCK: emitted by session_versions.py --handoff. Never hand-typed. -->
Fresh-clone verified at **`c8a7c42`**. Census **41,801**.
Bible **v8.187** · `BookComponentStandard` **v01.13.0** · Maker **v2.70** ·
`marks/` **41** · `icons/` **49** incl. LICENSE.
`ZUMO_Syllabus_WORKING.md` **v1.3**.

Instruments: `book_gates` **v1.74.7** · `lesson_inventory` **v1.3.5** ·
`gen_component` **v1.6.1** · `pill_sweep` **v1.1** · `gate_payload_match` **v1.9.5** ·
`build_family_map` **v1.6.6.5** · `callout_id` **v1.0** · `keyterm_prefix` **v1.0.1** · `build_mark_index` **v1.1.0** · `gen_bonus_banner` **v1.4.1** ·
`gen_part_banners` **v1.2** · `session_versions` **v1.32.2** · `fit_raster_svg` **v1.2** ·
`flatten_alpha` **v1.2** · `svg_layout_audit` **v1.21.2** · `site_parity` **v1.2.1** ·
`build_css` **v1.4.0** ·
`image_audit` **v1.3** ·
`strip_inline` **v1.2** ·
`build_worklist` **v1.2** ·
`prose_canon` **v1.1.0** ·
`retired_claims` **v1.0.2** ·
`census` **v1.1.0** ·
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

Lessons: L01 v03.32.1 · L02 v03.26.1 · L03 v03.47.0 · L04 v04.29.6 · L05 v04.30.0 · L06 v04.37.1 · L07 v04.33.1 · L08 v04.34.2 · L09 v05.27.6 · L10 v02.30.6 · L11 v02.31.3 · L12 v01.35.3 · L13 v02.39.0 · L14 v02.36.2 · L15 v02.32.0 · L16 v02.28.1.
