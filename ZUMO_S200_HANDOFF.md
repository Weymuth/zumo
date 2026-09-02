# ZUMO — S200 HANDOFF (written at S199 close · paste at top of Session 200)

## READ THIS FIRST

**NOTHING FROM S199 IS PUSHED. 13 ENTRIES: 6 MODIFIED, 4 ADDED, 2 DELETED, 1 RENAMED.**

**THE TWO DELETIONS ARE `ZUMO_S199_HANDOFF.md` AND `ZUMO_DAY1_Sep4.md`.** GitHub Desktop shows a
deletion as its own checkbox and it is the one most often missed — tick both. **Only ONE of the two
file moves scores as a rename:** `ZUMO_Teacher_Daily_Grid_WORKING.md` → `ZUMO_Teacher_Daily_Grid_F26.md`.
The other, `ZUMO_DAY1_Sep4.md` → `ZUMO_DAY1_F26_Sep4.md`, changed enough content to fall below git's
similarity threshold, so **it appears as an unrelated add and delete rather than as a move.** Counted
from `git status --porcelain`, not from intent. No new directories.

Added: `ZUMO_DAY1_F26_Sep4.md` · `ZUMO_DAY1_SIGNOUT_F26.md` · `ZUMO_TALKING_POINTS_F26_Wk1-2.md` ·
`ZUMO_S200_HANDOFF.md`. Modified: `GPT_WORKLIST.md` · `LIVE_ZUMO_TEXTBOOK.md` · `ZUMO_SUPER_BIBLE.md` ·
`ZUMO_L01_Reading_Quiz.md` · `ZUMO_L01_Reading_Quiz_CANVAS_QTI.zip` (binary, no visible diff) ·
`session_versions.py`.

**`newproject.html` IS NOT IN THIS BATCH. NO LESSON IS IN THIS BATCH.** S199 changed no lesson, no
payload and no byte. If you see a `lessons/` file or `newproject.html` in the diff, stop and look.

**THE FIRST CLASS MEETS FRIDAY SEPTEMBER 4.** Everything Friday needs is written and in the tree.
What is NOT done is on Canvas, and it is DJ's hands: **import the QTI package and set the quiz to
close Wednesday 9:50 AM.** Until that field is set the syllabus's promise is not true.

---

# 1. WHAT S199 DID

Full narrative is in LIVE.md's `WHAT SHIPPED IN S199`. The short version:

- **THE S198 BATCH WAS ALREADY PUSHED** at `3fcdad2` when the session opened — twenty entries, the
  deletion ticked, `newproject.html` correctly absent. The S199 handoff's "NOTHING IS PUSHED" was
  true when written. **The artefact is the answer** (S197), and the diff was read, not the sentence.
- **THE L01 CANVAS QUIZ WAS TESTING WORK NOBODY HAD ASSIGNED.** Q7 cited §6 Step 1 and Q8 §7.2 —
  building and uploading — while Assignment 1 read *§1–§5, no build*. **25% of the points were
  unanswerable by a student who did exactly what was asked.** Swapped for `L01_B17` (§5.1) and
  `L01_B32` (§5.5, a loop trace). Both packages re-parsed to prove the six survivors identical.
- **DJ RULED THE CLASS MODEL:** reading is flipped and gated by a graded quiz; **building, practice
  and challenges are class work**, closing on an ungraded check. This SUPERSEDES the S194 full-flip
  ruling that put the first upload at home.
- **THE GRID HELD THE OLD MODEL AT ROWS 1–2** and `ZUMO_DAY1_Sep4.md` held the new one; both were
  written in S194. **Rows 4–28 already scheduled practice in class**, so the cascade was three lines
  — an early reading called it a whole-term restructure and that was wrong.
- **L02 GIVEN A SECOND PERIOD** (DJ). About 8,300 words on one period was the worst ratio in the term.
  **Paid for out of five-student demo slack**, so every pinned milestone date held.
- **NO FALL MIDTERM** (DJ: no tests). Oct 9 is a normal period, inside the stretch the grid already
  flags as most likely to break.
- **THE YEAR LAYER IS NAMED FOR ITS YEAR.** Four `_F26` files; Bible §3.1's pointer moved and names
  the predecessor. `session_versions` **v1.35.0** registers the grid so it cannot ship unbumped.
- Bible **v8.197**. Grid **v2.1**. New: sign-out sheet, four-period talking points.

## THE THINGS S199 LEARNED THE HARD WAY — READ THESE
- **A CONTRADICTION BETWEEN TWO FILES WRITTEN IN THE SAME SESSION IS NOT A STALE FILE.** The grid and
  the Day-1 script were both S194 and both confident. Neither was careless; the ruling moved between
  them and only one was updated. **Check the sibling, not just the date.**
- **THE BANKS ALREADY ENCODED THE ANSWER AND NOBODY HAD READ THEM.** Every bank's `before` set says
  *"Pre-class reading gate. Answerable from the text alone"* and its `after` set *"Post-build check."*
  The design was right for DJ's model all along; two questions were filed on the wrong side of it.
  **Read the artefact's own description before designing a fix for it.**
- **THREE PRINTED WORD COUNTS DID NOT REPRODUCE, ONE BY 41%**, and **no instrument in the tree derives
  a word count** — which is exactly why they survived. A figure with no instrument has no home.
- **THE OBVIOUS FIX WAS THE FORBIDDEN ONE.** L02 §1's warm-ups do not survive being read at home, and
  the natural fix is a line in the lesson saying *we do these in class*. **That is calendar canon, and
  Bible §3.1 forbids it.** Fixed in the schedule; the book is untouched.
- **A ROSTER SIZE IS A YEARLY FACT THAT HIDES.** L02's second period exists only because there are
  five students. With eighteen the money is gone and L02 silently returns to one period.

---

# 2. S200 OPENS HERE

**DJ HAS NOT NAMED S200's WORK.** Friday's meeting will have happened. What is measured and waiting:

- **CANVAS IS THE ONLY THING BETWEEN THIS TREE AND FRIDAY WORKING.** Import
  `ZUMO_L01_Reading_Quiz_CANVAS_QTI.zip`, one attempt, close Wed Sep 9 at 9:50 AM.
- **TALKING POINTS EXIST FOR PERIODS 1–4 ONLY.** Periods 5–8 (L03 and its M1 demo) are the next
  block and L03 is the term's longest read at about 8,800 words.
- **NINE FIGURES ARE UNSHOT IN L01–L08** of fourteen book-wide: L03 IMAGE 3.2 / 3.5 / 3.6 and
  VIDEO 3.1 · L04 IMAGE 4.3 and VIDEO 4.1 · L06 VIDEO 6.1 · L08 VIDEO 8.1. **The lesson prints the
  tag and the caption and there is no picture under it.** Shoot or cut — cutting **NEEDS DJ**.
- **NINE BENCH ROWS REMAIN AND SIX NEED ONLY A DESK** — F1, F3, F4, F6, F7, F8. F7 needs Windows.
  F2 needs floor; F15 needs the tape, already in the room.
- **`F9` HAS NEVER HAD A WHY COLUMN.** Carried since S41. State it or rule it out.

## AND THESE ARE OWED, UNCHANGED
- **THE FOUR L05 ORPHANS — NEEDS DJ (irreversible).** 31 unreferenced files total.
- **The `(none needed)` ruling (S183) is unbuilt** — 133 sites, every one L01–L07. **NEEDS DJ.**
- **The notebook Google Doc link** (`ZUMO_Syllabus_WORKING.md` line 103). **NEEDS DJ.**
- **`ZUMO_BENCH_TESTS.md` CARRIES NONE OF THE MEASURED NUMBERS.** Migrating the S196 results is a
  real job and it is not done. Until it is, do not delete a closed row from the flagged-checks sheet.
- **F10's wait-OUT half wants serial timestamps. F16's calibrated half waits on DJ's own L04 build BY
  DESIGN** — do NOT hand him a calibration sketch.
- **WORKLIST TALLY — derived by `census.worklist()`, unmoved: 103 closed / 96 fixed / 2 parked /
  140 open of 245.** S199 touched no worklist row.

---

# 3. STANDING
- **INSTALL THE TRIPWIRE AT SESSION OPEN:** `bash tools/no_text_match.sh install` then `selftest`.
  It does NOT survive a container rebuild.
- **USE THE PARSER, NOT A TEXT MATCH** (§24.22). **A count comes with its population or it does not
  come.**
- **THE YEAR LAYER IS `_F26` (S199).** A file carrying dates, a period count or a roster size is
  rewritten every August and says so in its filename. The book carries no calendar (Bible §3.1).
- **`gate_payload_match` IS NOT ONE OF THE GATES** and **TAKES ARGUMENTS**.
- **`--update-census` PRINTS a replacement table; it does not write one.**
- **`pio_harness.sh` NEEDS `bash`, NOT `sh`.** It takes a **DIRECTORY**, not a file.
- **`--live` and `--handoff` PRINT, they do not WRITE** (§24.20). LIVE.md carries TWO `**Versions:**`
  lines — **line 6 is current**. Keep Status to ONE line.
- **A BIBLE BUMP IS A REGENERATION OBLIGATION** (S175) and **HAS TWO HOMES** (S185) — both on line 17.
- **A BANK VERSION HAS TWO HOMES** — the comment AND the `bank_version` field; `--status` reads the
  FIELD. **A SOURCE PIN IS READ BEFORE IT IS BUMPED** (rule 37).
- **A PROJECT-FILE COPY IS NOT THE TREE** (rule 32). `/mnt/project` still carries `_v2` of the TDP
  template, an S41 handoff, and **the pre-rename `_WORKING` grid and syllabus**.
- **SESSION OPEN:** `git ls-remote` → fresh clone → verify the Bible's internal version **with the
  parser** → read LIVE.md → `book_gates` → `session_versions --check` and `--selftest` →
  `census --selftest` → `lesson_inventory --selftest` → `svg_layout_audit --selftest` →
  `gate_payload_match newproject.html lessons/Lesson_*.html` → `callout_id` → `retired_claims` →
  `quiz_bank --check` → `build_css --check` → `build_worklist --check` → `build_syllabus_html --check`
  → `prose_canon --check` and `--selftest` → `image_audit --check` → `site_parity` twice past the
  10m57s floor.

# STANDING AUTHORITY — §24.17, §24.19, §24.21
**Decide and report; do not ask.** Carve-outs: facts about the ROOM · irreversible moves · RoboLore
brand and course scope. **§24.19 is the tiebreaker.**
**CONFIRMED AGAIN IN S199:** a handoff instruction is a description of an artefact, and the artefact
is the answer. S199's own handoff said nothing was pushed; everything was.

---
<!-- VERSION BLOCK: emitted by session_versions.py --handoff. Never hand-typed. -->
Fresh-clone verified at **`3fcdad2`**. Census **41,848**.
Bible **v8.197** · `BookComponentStandard` **v01.13.0** · Maker **v2.72** ·
`marks/` **41** · `icons/` **49** incl. LICENSE.
`ZUMO_Syllabus_WORKING.md` **v1.5** · `ZUMO_Teacher_Daily_Grid_F26.md` **v2.1**.

Instruments: `book_gates` **v1.76.7** · `lesson_inventory` **v1.4.1** ·
`gen_component` **v1.6.1** · `pill_sweep` **v1.1** · `gate_payload_match` **v1.9.6** ·
`build_family_map` **v1.6.6.8** · `callout_id` **v1.0** · `keyterm_prefix` **v1.0.1** · `build_mark_index` **v1.1.0** · `gen_bonus_banner` **v1.4.1** ·
`gen_part_banners` **v1.2** · `session_versions` **v1.35.0** · `fit_raster_svg` **v1.2** ·
`flatten_alpha` **v1.2** · `svg_layout_audit` **v1.23** · `site_parity` **v1.2.1** ·
`build_css` **v1.4.0** · `build_syllabus_html` **1.1** ·
`image_audit` **v1.3** ·
`strip_inline` **v1.2** ·
`build_worklist` **v1.2** ·
`qti_export` **1.2** ·
`prose_canon` **v1.4.0** ·
`retired_claims` **v1.3.1** ·
`census` **v1.3.0** ·
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

Lessons: L01 v03.32.2 · L02 v03.26.2 · L03 v03.47.4 · L04 v04.29.7 · L05 v04.30.2 · L06 v04.37.3 · L07 v04.33.1 · L08 v04.34.4 · L09 v05.28.0 · L10 v02.30.7 · L11 v02.31.4 · L12 v01.35.4 · L13 v02.39.0 · L14 v02.36.3 · L15 v02.32.2 · L16 v02.28.1.
