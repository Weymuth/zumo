# ZUMO — S201 HANDOFF (written at S200 close · paste at top of Session 201)

## READ THIS FIRST

**NOTHING FROM S200 IS PUSHED — AND READ THE DIFF, NOT THIS SENTENCE.** It has been wrong three
sessions running (S198, S199, S200), because it is written before the push and can therefore never be
evidence of anything. **The artefact is the answer** (S197).

**14 ENTRIES: 5 MODIFIED, 7 ADDED, 2 DELETED, 0 RENAMED.** Counted from `git status --porcelain`,
not from intent. No new directories.

**THERE ARE TWO DELETIONS AND ONE OF THEM IS EASY TO TICK WRONG.** `quizzes/ZUMO_L01_Reading_Quiz.md`
is the STALE second copy; `ZUMO_L01_Reading_Quiz.md` at the repo root is the LIVE one and is
MODIFIED, not deleted. **Same filename, different paths.** The other deletion is the usual
`ZUMO_S200_HANDOFF.md`. GitHub Desktop shows each deletion as its own checkbox and they are the ones
most often missed — tick both.

Added: `ZUMO_L03_Reading_Quiz.md` · `ZUMO_L03_Reading_Quiz_CANVAS_QTI.zip` · `ZUMO_L04_Reading_Quiz.md` · `ZUMO_L04_Reading_Quiz_CANVAS_QTI.zip` · `ZUMO_S201_HANDOFF.md` · `ZUMO_TALKING_POINTS_F26_Wk3-4.md` · `quizzes/reading_quiz.py`.
**Two of the added files are binary zips with no visible diff.**

Modified: `GPT_WORKLIST.md` · `LIVE_ZUMO_TEXTBOOK.md` · `ZUMO_L01_Reading_Quiz.md` · `ZUMO_SUPER_BIBLE.md` · `session_versions.py`.

**NO LESSON, NO PAYLOAD AND NO BYTE OF THE BOOK IS IN THIS BATCH. `newproject.html` IS NOT IN IT.**
If you see a `lessons/` file or `newproject.html` in the diff, stop and look.

**THE BIBLE IS IN IT — v8.198, §25.3a NEW — AND SO IS `GPT_WORKLIST.md`, WHICH THE BUMP OBLIGES
(S175).** S200 first ruled AGAINST the bump; `session_versions`' SESSION arm reported that LIVE.md
said Session 200 while the newest Bible entry said S199, and the ruling was reversed. **A session
that ships work and writes no Bible entry breaks the ledger.**

---

# 1. WHAT S200 DID

Full narrative is in LIVE.md's `WHAT SHIPPED IN S200`. The short version:

- **THE S199 BATCH WAS ALREADY PUSHED** at `a1b267b` when the session opened. Third in a row.
- **THE HANDOFF PLACED S200 AFTER FRIDAY AND IT WAS BEFORE IT.** S200 opened Tuesday Sep 1; first
  class is Friday Sep 4. Every pre-Friday item written up as retrospective was still live. **DJ
  confirmed the Canvas import is done and a pre-quiz added.**
- **TALKING POINTS FOR PERIODS 5–8** — `ZUMO_TALKING_POINTS_F26_Wk3-4.md` v1.0. Note that the S200
  handoff called this block "L03 and its M1 demo"; **periods 7–8 are L04**, and the file covers both.
- **THE THIRD HAND-BUILD BECAME AN INSTRUMENT.** `quizzes/reading_quiz.py` v1.0 builds a reading quiz
  from an explicit bank-id selection and **REFUSES an id whose cite reaches outside §1–§5**. Eleven
  controls, both directions. **It caught its own author on the first run** (`L03_B12` cites
  `§3.3, Glossary`).
- **THE L03 AND L04 POOLS CARRIED S199's DEFECT, UNSHIPPED.** 45 of L03's 61 `before` questions are
  in scope; 29 of L04's 51. Now a refusal instead of a remembered rule.
- **A RETIRED SELECTION WAS STILL LIVE IN A SECOND COPY.** `quizzes/ZUMO_L01_Reading_Quiz.md` still
  named `L01_B43` (§6) and `L01_B48` (§7) as the quiz, in the present tense, and still told the
  reader to keep one from §6 or §7. Deleted. **The root copy had no version home at all** — it is
  now v1.1.
- **`session_versions` v1.36.0** registers the `ZUMO_L##_Reading_Quiz.md` and
  `ZUMO_TALKING_POINTS_F26_*` families, and the ROSTER arm named `reading_quiz.py` unprompted on its
  first run.

## THE THINGS S200 LEARNED THE HARD WAY — READ THESE
- **TWO FILES WITH THE SAME NAME AND DIFFERENT PATHS ARE TWO FILES.** Every search for
  `ZUMO_L01_Reading_Quiz.md` matched both and the stale one hid behind the fixed one for a full
  session. **Search by path, and when a name resolves twice, ask which one is canon.**
- **`retired_claims` COULD NOT SEE IT.** Its scope is 122 pages and 16 banks. A loose markdown file
  at the repo root carrying retired canon in the present tense is in no instrument's population.
  **An instrument's scope is a claim about what it does NOT cover.**
- **A REGISTRATION CANNOT ASSERT ON THE COMMIT THAT INTRODUCES IT.** `--currency` compares the
  working tree against HEAD, and HEAD has no version home to compare against for a file that just
  gained one. It reports "no version home" and asserts nothing. **It starts working at the NEXT
  commit** — so the control has to be run against a tracked sibling, which is what S200 did.
- **A RANDOM IDENT MAKES AN ARTEFACT UNREBUILDABLE.** L01's QTI package cannot be regenerated,
  because identical questions under new idents import as a different quiz. L03's and L04's idents
  hash from (lesson, bank id) and the zip timestamps are pinned, so a rebuild is byte-identical.

---

# 2. S201 OPENS HERE

**DJ HAS NOT NAMED S201's WORK.** What is measured and waiting:

- **CANVAS, DJ's HANDS.** Import `ZUMO_L03_Reading_Quiz_CANVAS_QTI.zip` (one attempt, closes **Wed
  Sep 16, 9:50 AM**) and `ZUMO_L04_Reading_Quiz_CANVAS_QTI.zip` (one attempt, closes **Mon Sep 21,
  1:15 PM**). Until those close fields are set, the syllabus's promise is not true for L03 or L04.
- **§25.3 CONTRADICTS THE COURSE IN THREE PLACES — NEEDS DJ.** The new §25.3a records the §1–§5 rule,
  and the subsection directly above it still says *the quizzes do not exist yet* (sixteen banks exist,
  L01 is imported), still says **CLOSED BOOK** against a model that is open book and notes, and still
  prices the quizzes at **20%** against a per-quiz weight nearer 1%. **Two of the three are grading and
  course-scope decisions and are DJ's under §24.17**, so S200 flagged them rather than rewriting them.
  One ruling closes all three.
- **TALKING POINTS EXIST FOR PERIODS 1–8.** Periods 9–12 are the next block: the Sep 25 short buffer
  period, L05 Proximity with the **M2 demo**, and L06 Encoders ⭐ — which is where the course turns
  from open-loop to closed-loop.
- **EIGHT FIGURES ARE UNSHOT IN L01–L08**, not nine. **The S200 handoff said nine and then listed
  eight** — a count that disagreed with its own population, carried forward unchecked, and repeated
  once more in S200's opening report before it was derived. `image_audit --check` says **14
  outstanding book-wide**; `IMAGE_WORKLIST.md` is the population and it is generated. **SIX OF THE
  EIGHT ARE IN L03 AND L04** — L03 VIDEO 3.1, IMAGE 3.2, 3.5, 3.6 · L04 VIDEO 4.1, IMAGE 4.3 — and
  **four of those are read at home on Sep 15**. The other two are L06 VIDEO 6.1 and L08 VIDEO 8.1.
  **Derive the list, do not read it from this sentence.** Shoot or cut — cutting **NEEDS DJ**.
- **PERIOD 7 HAS A MATERIALS DEPENDENCY.** L04 §4.3 has every student build a test surface: **white
  poster board and 3/4-inch black electrical tape, at least two feet**, five of each, away from
  windows. A marker or printed line does not work — the sensors read infrared. **Room fact, NEEDS DJ.**
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
  140 open of 245.** S200 touched no worklist row.

---

# 3. STANDING
- **INSTALL THE TRIPWIRE AT SESSION OPEN:** `bash tools/no_text_match.sh install` then `selftest`.
  It does NOT survive a container rebuild.
- **USE THE PARSER, NOT A TEXT MATCH** (§24.22). **A count comes with its population or it does not
  come.**
- **A NAME THAT RESOLVES TWICE IS TWO FILES (S200).** Search by path.
- **THE YEAR LAYER IS `_F26` (S199).** A file carrying dates, a period count or a roster size is
  rewritten every August and says so in its filename. The book carries no calendar (Bible §3.1).
- **THE READING QUIZ DRAWS FROM §1–§5 ONLY (S200).** You do not have to remember this: edit
  `SELECTIONS` in `quizzes/reading_quiz.py` and an out-of-scope id refuses to build.
  **L01 IS REGISTERED FOR `--check` ONLY AND CANNOT BE REBUILT** — S194's idents were random.
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
  `quiz_bank --check` → **`reading_quiz --check` and `--selftest`** → `build_css --check` →
  `build_worklist --check` → `build_syllabus_html --check` → `prose_canon --check` and `--selftest` →
  `image_audit --check` → `site_parity` twice past the 10m57s floor.

# STANDING AUTHORITY — §24.17, §24.19, §24.21
**Decide and report; do not ask.** Carve-outs: facts about the ROOM · irreversible moves · RoboLore
brand and course scope. **§24.19 is the tiebreaker.**

---
<!-- VERSION BLOCK: emitted by session_versions.py --handoff. Never hand-typed. -->
Fresh-clone verified at **`a1b267b`**. Census **41,848**.
Bible **v8.198** · `BookComponentStandard` **v01.13.0** · Maker **v2.72** ·
`marks/` **41** · `icons/` **49** incl. LICENSE.
`ZUMO_Syllabus_WORKING.md` **v1.5** · `ZUMO_Teacher_Daily_Grid_F26.md` **v2.1**.

Instruments: `book_gates` **v1.76.7** · `lesson_inventory` **v1.4.1** ·
`gen_component` **v1.6.1** · `pill_sweep` **v1.1** · `gate_payload_match` **v1.9.6** ·
`build_family_map` **v1.6.6.8** · `callout_id` **v1.0** · `keyterm_prefix` **v1.0.1** · `build_mark_index` **v1.1.0** · `gen_bonus_banner` **v1.4.1** ·
`gen_part_banners` **v1.2** · `session_versions` **v1.36.0** · `fit_raster_svg` **v1.2** ·
`flatten_alpha` **v1.2** · `svg_layout_audit` **v1.23** · `site_parity` **v1.2.1** ·
`build_css` **v1.4.0** · `build_syllabus_html` **1.1** ·
`image_audit` **v1.3** ·
`strip_inline` **v1.2** ·
`build_worklist` **v1.2** ·
`qti_export` **1.2** ·
`reading_quiz` **v1.0** ·
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
