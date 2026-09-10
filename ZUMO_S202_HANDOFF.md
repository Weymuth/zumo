# ZUMO — S202 HANDOFF (written at S201 close · paste at top of Session 202)

## READ THIS FIRST

**THIS SENTENCE CANNOT TELL YOU WHETHER S201 IS PUSHED — READ THE DIFF.** It has now been wrong
FOUR sessions running (S198, S199, S200, S201). It is written before the push and can therefore
never be evidence. **The artefact is the answer** (S197). At S201 open the S200 batch was already
live at `cff7475`.

**41 ENTRIES: 39 MODIFIED, 2 ADDED, 1 DELETED (this file's predecessor), 0 RENAMED.** Counted from
`git status --porcelain`, not from intent. No new directories.

**THIS IS A WHOLE-BOOK BATCH AND THAT IS THE POINT — EVERY LESSON IS IN IT.** All 16 lessons,
`going_deeper.html` and `index.html` changed, because the book was named. **THIRTEEN LESSONS
CHANGED BY EXACTLY 10 LINES EACH** (2 title sites × 2 lines, 1 copyright, 2 version homes ×2). The
four that differ: **L01 = 14** (its `<h1>` was vacated), **L08 = 12**, **L04 = 37**, **L09 = 66**.
**If a lesson you did not expect shows more than 10 changed lines, stop and look.**

Added: `ROBOLORE_BRAND_CARD_S201.md` · `ZUMO_SHOOT_LIST_F26_Sep3.md`. Deleted: `ZUMO_S201_HANDOFF.md`.

---

# 1. WHAT S201 DID

**THE BOOK HAS A TITLE.** DJ ruled it: ***Sense, Decide, Act***, imprint **RoboLore**, copyright
**DJ Weymuth**. Recorded at Bible **§3.2 (v8.199)**.

- **34 title sites across 17 files, 18 copyright sites across 18.** The slot already existed and
  read `Zumo 32U4 Robotics • PlatformIO Edition` — **the first answer to "what is the book called"
  said it had no title**, because it read `<title>` and `<h1>` and not the masthead. **Look for the
  SLOT, not the tag.**
- **L01's `<h1>` was the title.** Vacated to `Hello, Robot!`, matching its own `<title>` as ten of
  the sixteen lessons already do. **Promoting a phrase means taking it from wherever it was.**
- **The © line no longer names Claude as a holder** — `with Claude AI`, not `by … and Claude AI`.
  And **RoboLore is an imprint, never `LLC` or `Inc`**: no entity is registered.
- ***Mastering C++ and the Pololu Zumo Robot* was rejected on measurement**, not taste: zero
  `std::`, templates, classes, `virtual`, `try` or dynamic allocation anywhere in the book's code.

**§25.6's GATE WAS WEAKER THAN ITS NAME AND A CONTROL FOUND IT.** The arm anchored on
`© 2026 RoboLore` and correctly fired on 17 files when the ruling landed. Re-anchored on the
**copyright holder**. Then the control — reword the credits in ONE lesson — **did not fire**,
because the comparison ran through `_skel()`, which compares MARKUP (rule 44). `book_gates`
**v1.77.0** adds a TEXT arm plus a book-title presence check. **The new arm's first cut was wrong
in the opposite direction**, scoped to the whole colophon block, which also carries each lesson's
own name and subtitle; it reported all 17 as distinct. Rescoped from the © symbol. Both arms
control-run both ways.

**THREE COURSE-SCOPE RULINGS, ALL DJ's:**
1. **TILES.** The room has course tiles and students place them. **L04 §4.3 no longer has students
   build a surface** — it has them choose and check one. Poster board **7 → 0** in L04, electrical
   tape 4 → 2 (both survivors are physics and true on a tile). **Five sites, not one**: the
   §3.4 contrast sentence read *"on poster board or on a competition mat"*, which stops being a
   contrast when the classroom surface IS a competition tile. L08's track line follows.
2. **THE GREEN IS THE RCJ §3.6 25 mm COMPETITION MARKER.** Twelve `tape` sites in L09, now zero —
   including the §2 objective and its Brain Check mirror, which must stay character-exact. **The
   rulebook gives a size and a word your EYE understands and says nothing about infrared**, so the
   old *not all greens are equal* shopping tip became **§7.1a**: survey the competition marker
   against a green marker on paper and one other green. **The prediction to test is that marker ink
   is IR-transparent and will read near white** — that is a prediction, not a measurement.
3. **THE MATERIALS PURCHASE IS CLOSED.** The S201 handoff's five poster boards and five tape rolls
   for period 7 are not needed.

**`ZUMO_BENCH_TESTS.md` v1.5.1 — Q017 IS NO LONGER SIX NUMBERS.** `L09-B1`, open since **S41**, the
oldest bench row in the project, now wants white, black, the competition marker and each comparison
green, plus both gaps. **A null result (all greens alike) is a finding that changes §7.1a, not a
failed test.**

## THE THINGS S201 LEARNED THE HARD WAY
- **A `git checkout` IS NOT A RESTORE ON A TREE WITH UNCOMMITTED WORK.** Restoring a control
  specimen with `git checkout -- lessons/Lesson_11.html` reverted it to HEAD and discarded that
  lesson's title, copyright and version edits. The suite read 80/82 and named the file. **Restore
  from the byte backup taken before the injection.**
- **AN EDIT SCRIPT THAT DIES ON AN ASSERT WRITES NOTHING — AND THE GREEN RUN AFTER IT MEANS
  NOTHING.** A `book_gates` edit failed its last assert before the `open(…,'w')`; the suite then
  read 82/82, which was the UNEDITED file passing. **A control that fails to plant reads exactly
  like one that passed.**
- **A RESIDUE CHECK FAILS WHEN THE NEW STRING CONTAINS THE OLD ONE.** Counting the old title after
  the sweep returned 34, because `Sense, Decide, Act • Zumo 32U4 Robotics • PlatformIO Edition`
  contains `Zumo 32U4 Robotics • PlatformIO Edition`. Use a negative lookbehind or count the new.
- **THE CSS DIGEST MOVES WHEN NO RULE CHANGES.** §7.1a used only existing classes, so `book.css`
  came back at the same **574 rules / 2,033 declarations** with none born, died or altered — the
  whole diff is the usage census. **Digest moved, counts held: that pair is what makes it benign.**
- **BUMPING A LESSON REPINS ITS BANKS, AND A REPINNED BANK IS AN UNBUMPED EDIT.** `--currency`
  caught every one. Sixteen lessons bumped → all sixteen banks repinned and bumped.

---

# 2. S202 OPENS HERE

**DJ HAS NOT NAMED S202's WORK.** What is measured and waiting:

- **THE SHOOT LIST IS LIVE AND DATED FOR THURSDAY SEP 3 AM.** `ZUMO_SHOOT_LIST_F26_Sep3.md` v1.2 —
  **six photos and two videos**, closing 8 of the 14 outstanding tags and **all six in L01–L08**.
  DJ confirmed the walled rescue zone and the delrin sheet are in the room. **If the files arrived,
  wiring them is S202's first job**; filenames must be `L##_IMAGE_#-0#_snake_name.jpg` or
  `image_audit` will not see them. **Derive the outstanding list, do not read it from this sentence.**
- **§25.3 IS CLOSED — ALL THREE FLAGS RESOLVED IN S201, IN THREE DIFFERENT DIRECTIONS.** DJ ruled
  the graded reading quiz **CLOSED BOOK** and the ungraded Post-Build Check **OPEN NOTE**
  (§25.3b NEW, Bible v8.200, syllabus v1.6). The *quizzes do not exist yet* line was stale and is
  corrected. **And the 20% was never a contradiction** — it is the CATEGORY weight and the syllabus
  says the same 20%. **S200, S201 and S201's own handoff all carried it as a defect without
  re-deriving it; a figure repeated in three documents is still not a finding.**
- **CANVAS, DJ's HANDS.** L03 QTI closes **Wed Sep 16, 9:50 AM**; L04 QTI closes **Mon Sep 21,
  1:15 PM**. Until those are set the syllabus's promise is not true for L03 or L04.
- **THE LESSON `<title>` TAGS STILL END `— Zumo 32U4 Robotics`** and are gate-71 territory. The
  book title now lives in the mastheads, colophons and front door. **Whether the tabs should carry
  the title is undecided and is DJ's.**
- **`ROBOLORE_BRAND_CARD_S201.md` NAMES TWO STALE FILES AND NEITHER IS FIXED.**
  `BookComponentStandard.md` v01.13.0 §5.0 still prints the five Heritage Blue hexes that
  **S102 explicitly withdrew**, and `ROBOLORE_GRAPHICS_CHAT_HANDOFF.md` §7 still carries the
  palette park that S102 released. **Approved five: `#0B1A2E` · `#3D5266` · `#7B6240` · `#C9A463` ·
  `#F5F2E9`** — confirmed independently by `build_palette.py`'s `CANON`. **DJ was asked whether to
  fix them or cite around them and has not ruled.**
- **TALKING POINTS EXIST FOR PERIODS 1–8.** Periods 9–12 are next: the Sep 25 buffer, L05 with the
  **M2 demo**, and L06 Encoders ⭐ where the course turns closed-loop.
- **NINE BENCH ROWS REMAIN, SIX NEED ONLY A DESK** — F1, F3, F4, F6, F7 (Windows), F8. F2 needs
  floor. **F15 needed tape and the tile ruling may have retired it — check before running it.**
- **`F9` HAS NEVER HAD A WHY COLUMN.** Carried since S41. State it or rule it out.

## AND THESE ARE OWED, UNCHANGED
- **THE FOUR L05 ORPHANS — NEEDS DJ (irreversible).** 31 unreferenced files total.
- **The `(none needed)` ruling (S183) is unbuilt** — 133 sites, every one L01–L07. **NEEDS DJ.**
- **The notebook Google Doc link** (`ZUMO_Syllabus_WORKING.md` line 103). **NEEDS DJ.**
- **`ZUMO_BENCH_TESTS.md` CARRIES NONE OF THE MEASURED NUMBERS.** Migrating the S196 results is a
  real job and is not done. Until it is, do not delete a closed row from the flagged-checks sheet.
- **F10's wait-OUT half wants serial timestamps. F16's calibrated half waits on DJ's own L04 build
  BY DESIGN** — do NOT hand him a calibration sketch. **The same constraint now gates Q017.**
- **WORKLIST TALLY — derived by `census.worklist()`, unmoved: 103 closed / 96 fixed / 2 parked /
  140 open of 245.** S201 touched no worklist row.
- **`going_deeper.html` AND `index.html` REPORT "no version home"** to `session_versions` although
  both carry one in a comment. Registering them is a small job nobody has done.

---

# 3. STANDING
- **INSTALL THE TRIPWIRE AT SESSION OPEN:** `bash tools/no_text_match.sh install` then `selftest`.
  It does NOT survive a container rebuild.
- **USE THE PARSER, NOT A TEXT MATCH** (§24.22). **A count comes with its population or it does not come.**
- **A NAME THAT RESOLVES TWICE IS TWO FILES (S200).** Search by path.
- **THE YEAR LAYER IS `_F26` (S199).** The book carries no calendar (Bible §3.1).
- **THE READING QUIZ DRAWS FROM §1–§5 ONLY (S200).** Edit `SELECTIONS` in `quizzes/reading_quiz.py`
  and an out-of-scope id refuses to build. **L01 IS `--check` ONLY AND CANNOT BE REBUILT.**
- **THE BOOK IS *SENSE, DECIDE, ACT* (S201).** Imprint RoboLore, © DJ Weymuth. §25.6 asserts both
  the title's presence and the credits TEXT in all 17 pages — it will fire if one drifts.
- **A FLAG OUTLIVES ITS RESOLUTION UNLESS THE RESOLUTION EDITS IT (S201).** Retiring the flag is
  part of resolving the thing it flags. §25.3's S200 flag sat two paragraphs above §25.3b still
  asserting the reversed position, in the same file.
- **NO FIGURE CAN BE WIRED ANYWHERE IN THE BOOK RIGHT NOW (S201).** `build_css.py` reads the
  lessons through `expand_classes`, which reads `css/book.css` from disk, so a rule whose usage
  count ties sends the stylesheet into a two-cycle with no fixed point. The documented remedy
  (`strip_inline --restore` → `build_css` → `--apply`) **breaks an untouched clone** — 39 inline
  styles into L01, two gates red, zero edits. Reproduce before believing anything else about it.
- **`gate_payload_match` IS NOT ONE OF THE GATES** and **TAKES ARGUMENTS**.
- **`--update-census` PRINTS a replacement table; it does not write one.**
- **`pio_harness.sh` NEEDS `bash`, NOT `sh`.** It takes a **DIRECTORY**, not a file.
- **`--live` and `--handoff` PRINT, they do not WRITE** (§24.20). LIVE.md carries TWO
  `**Versions:**` lines — **line 6 is current**. Keep Status to ONE line.
- **A BIBLE BUMP IS A REGENERATION OBLIGATION** (S175) and **HAS TWO HOMES** (S185) — plus a line
  in the running changelog at the top. S201 needed all three.
- **A BANK VERSION HAS TWO HOMES** — the comment AND the `bank_version` field. **A SOURCE PIN IS
  READ BEFORE IT IS BUMPED** (rule 37).
- **A PROJECT-FILE COPY IS NOT THE TREE** (rule 32). `/mnt/project` still carries `_v2` of the TDP
  template, an S41 handoff, and the pre-rename `_WORKING` grid and syllabus.
- **SESSION OPEN:** `git ls-remote` → fresh clone → verify the Bible's internal version **with the
  parser** → read LIVE.md → `book_gates` → `session_versions --check` and `--selftest` →
  `census --selftest` → `lesson_inventory --selftest` → `svg_layout_audit --selftest` →
  `gate_payload_match newproject.html lessons/Lesson_*.html` → `callout_id` → `retired_claims` →
  `quiz_bank --check` → `reading_quiz --check` and `--selftest` → `build_css --check` →
  `build_worklist --check` → `build_syllabus_html --check` → `prose_canon --check` and `--selftest`
  → `image_audit --check` → `site_parity` twice past the 10m57s floor.

# STANDING AUTHORITY — §24.17, §24.19, §24.21
**Decide and report; do not ask.** Carve-outs: facts about the ROOM · irreversible moves · RoboLore
brand and course scope. **§24.19 is the tiebreaker.**

---
<!-- VERSION BLOCK: emitted by session_versions.py --handoff. Never hand-typed. -->
Fresh-clone verified at **`cff7475`**. Census **41,869**.
Bible **v8.200** · `BookComponentStandard` **v01.13.0** · Maker **v2.72** ·
`marks/` **41** · `icons/` **49** incl. LICENSE.
`ZUMO_Syllabus_WORKING.md` **v1.6** · `ZUMO_Teacher_Daily_Grid_F26.md` **v2.1**.

Instruments: `book_gates` **v1.77.1** · `lesson_inventory` **v1.4.1** ·
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
`going_deeper` **v01.7.0**.

Lessons: L01 v03.33.0 · L02 v03.27.0 · L03 v03.48.0 · L04 v04.31.0 · L05 v04.31.0 · L06 v04.38.0 · L07 v04.34.0 · L08 v04.35.0 · L09 v05.30.0 · L10 v02.31.0 · L11 v02.32.0 · L12 v01.36.0 · L13 v02.40.0 · L14 v02.37.0 · L15 v02.33.0 · L16 v02.29.0.
