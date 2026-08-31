# ZUMO — S199 HANDOFF (written at S198 close · paste at top of Session 199)

## READ THIS FIRST

**NOTHING FROM S198 IS PUSHED. 20 ENTRIES: 18 MODIFIED, 1 DELETED, 1 NEW.**
**THE DELETION IS `ZUMO_S198_HANDOFF.md` AND THE NEW FILE IS THIS ONE.** GitHub Desktop shows a
deletion as its own checkbox and it is the one most often missed — tick it. No new directories.

**`newproject.html` IS NOT IN THIS BATCH.** S198 changed no payload. If you see it in the diff,
something is wrong — stop and look.

**THE SEATING DEBT IS PAID. Do not carry it forward.** Thirty-three rules seated, none unseated, and every `§16.x`
named anywhere in the tree resolves to a body.

**WORKLIST TALLY — derived by `census.worklist()`, unmoved: 103 closed / 96 fixed / 2 parked /
140 open of 245.** S198 touched no worklist row.

---

# 1. WHAT S198 DID

Full narrative is in LIVE.md's `WHAT SHIPPED IN S198`. The short version:

- **§16 SEATING IS PAID — and the queue was never twenty-six.** Thirty-three unseated at session open. The delta is exactly
  the seven rules born since S187 (§16.52a, §16.53–§16.58): **the queue grew for eleven sessions
  while being described as static.** Third time this list has been counted low, same cause each
  time — the window moved and the family did not.
- **GATE 81 WIDENED to the worklist colophon** — a fourth, unguarded tally home. A wrong figure
  planted there passed every gate. Figure deleted rather than priced. `book_gates` **v1.76.7**.
- **`session_versions` v1.34.0 — SECOND_HOMES + the comparator.** Eight handoffs called the
  worklist's two version homes a disagreement; **they agree**, and the comparator was what was
  missing.
- **L04's figures note stopped typing a live figure tag.** IMAGE 4.1 had been counted outstanding
  since S138, the session that retired it. Planned 145 → 144; **outstanding unmoved at 14**.
- **L03 NOTE 3.121 — one run gives direction, not size.** L03 **v03.47.4**, L04 **v04.29.7**,
  six bank pins, all read before bumping.
- **BENCH SHEET REBUILT** to the nine genuinely open rows. `ZUMO_FLAGGED_CHECKS.md` **v1.6**.
- **F5 RULED BY DJ** — bands stand as printed, adjustable later. **RULED, NOT CLOSED.**

## THE THINGS S198 LEARNED THE HARD WAY — READ THESE
- **A CONTROL THAT FAILS TO PLANT READS EXACTLY LIKE A CONTROL THAT PASSED.** Hit TWICE in one
  session: a `str.replace` whose anchor did not exist returned a clean tree and a green result both
  times. **Assert the plant landed before you believe the result.**
- **A SET DIFFERENCE CANNOT SEE ONE OF SIX OCCURRENCES VANISH.** The triple check's loss detector
  was wrong when first controlled and had to be rebuilt as a MULTISET — and only then did it find
  that the bench-sheet rewrite had dropped the S189 scope clause. **That clause has now had to be
  restored twice**, both times for the same reason: a count read off one sheet being generalised
  to the book.
- **AN ARM THAT ONLY WORKS INSIDE A GIT CHECKOUT HAS A HIDDEN PRECONDITION.** `second_homes()` used
  `git ls-files` and went red inside `--selftest`, whose fixture is a tempdir copy.
- **FIX THE PROSE, NOT THE INSTRUMENT, WHEN THE BOOK IS WHAT IS ODD.** The IMAGE 4.1 exclusion was
  built, controlled, and then REVERTED — an exclusion must be taught to every reader of that syntax
  and remembered forever (rule 20); dropping the brackets made all of them agree at once.
- **A CORRECTED DENOMINATOR IS NOT IMPROVED COVERAGE.** Say which one happened, and prove it: the
  outstanding count was UNMOVED at 14 across the change (S135).

---

# 2. S199 OPENS HERE

**DJ HAS NOT NAMED S199's WORK.** The first class meeting is **Friday, September 4** — S199 is
inside the last week. What is measured and waiting:

- **NINE FIGURES ARE UNSHOT IN L01–L08** of fourteen book-wide: L03 IMAGE 3.2 / 3.5 / 3.6 and
  VIDEO 3.1 · L04 IMAGE 4.3 and VIDEO 4.1 · L06 VIDEO 6.1 · L08 VIDEO 8.1. Five stills, four
  videos. **The lesson prints the tag and the caption and there is no picture under it.** Shoot or
  cut — cutting is a content ruling and **NEEDS DJ**.
- **NINE BENCH ROWS REMAIN AND SIX NEED ONLY A DESK** — F1, F3, F4, F6, F7, F8. **DJ said a
  Windows machine would be available the morning after S198**, which is what F7 needs. F2 needs
  floor; F15 needs the tape, already in the room.
- **`F9` HAS NEVER HAD A WHY COLUMN.** Carried since S41 with nobody writing down what it proves.
  State it or rule it out.
- **L01–L08 CARRIES NO OPEN WORKLIST ROW.** Eighty-four findings, all but two shut and those two
  parked — the only band in the book at zero.

## AND THESE ARE OWED, UNCHANGED
- **THE FOUR L05 ORPHANS — NEEDS DJ (irreversible).** All four have a named reason. Tracked,
  committed, serving HTTP 200. Delete, or leave staged? 31 unreferenced files total.
- **The `(none needed)` ruling (S183) is unbuilt** — 133 sites, every one L01–L07. Priced as an ADD,
  not an edit. **NEEDS DJ.**
- **The notebook Google Doc link** (`ZUMO_Syllabus_WORKING.md` line 103). **NEEDS DJ.**
- **`ZUMO_BENCH_TESTS.md` CARRIES NONE OF THE MEASURED NUMBERS.** The flagged-checks sheet is the
  ONLY home for the S196 bench data, and its own rule assumes otherwise. **Migrating the results is
  a real job and it is not done.** Until it is, do not delete a closed row from that sheet.
- **F10's wait-OUT half wants serial timestamps.** **F16's calibrated half waits on DJ's own L04
  build BY DESIGN** — do NOT hand him a calibration sketch; stock `LineFollower` contains
  `calibrateSensors()`, the exact identifier whose absence is his deliberate RED build at L04 Step 5.

---

# 3. STANDING
- **INSTALL THE TRIPWIRE AT SESSION OPEN:** `bash tools/no_text_match.sh install` then `selftest`.
  It does NOT survive a container rebuild, and it does NOT cover Python `re` on raw bytes.
- **USE THE PARSER, NOT A TEXT MATCH** (§24.22). **A count comes with its population or it does not
  come** — S198's ARM 3 returned two findings and both were its own scoping, not the tree (§16.15).
- **`gate_payload_match` IS NOT ONE OF THE GATES** and **TAKES ARGUMENTS**. Its census watches the
  PAYLOAD, not the lesson `<pre>`; editing a lesson listing alone leaves it GREEN.
- **`--update-census` PRINTS a replacement table; it does not write one.** Move the one pin by hand.
- **`pio_harness.sh` NEEDS `bash`, NOT `sh`** — line 94 uses a `<<<` here-string. The harness takes
  a **DIRECTORY**, not a file.
- **`--live` and `--handoff` PRINT, they do not WRITE** (§24.20). LIVE.md carries TWO `**Versions:**`
  lines — **line 6 is current**. Keep Status to ONE line.
- **A BIBLE BUMP IS A REGENERATION OBLIGATION** (S175) and **HAS TWO HOMES** (S185) — both live on
  line 17 and both were moved at S198.
- **A BANK VERSION HAS TWO HOMES** — the comment AND the `bank_version` field; `--status` reads the
  FIELD. **A SOURCE PIN IS READ BEFORE IT IS BUMPED** (rule 37): six pins in S198, none of them
  touched the changed claims, and that is a result rather than a formality.
- **A PROJECT-FILE COPY IS NOT THE TREE** (rule 32). `/mnt/project` still carries `_v2` of the TDP
  template and an S41 handoff; the live template is `ZUMO_TDP_Template_v3.md`.
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
**FROM S197, CONFIRMED TWICE MORE IN S198:** **a handoff instruction is a description of an
artefact, and the artefact is the answer.** The §16 count was stale by seven; the worklist's
"disagreeing" version homes agreed. Neither line was careless; both were written without the file
in front of them.

---
<!-- VERSION BLOCK: emitted by session_versions.py --handoff. Never hand-typed. -->
Fresh-clone verified at **`6b341e6`**. Census **41,848**.
Bible **v8.196** · `BookComponentStandard` **v01.13.0** · Maker **v2.72** ·
`marks/` **41** · `icons/` **49** incl. LICENSE.
`ZUMO_Syllabus_WORKING.md` **v1.5**.

Instruments: `book_gates` **v1.76.7** · `lesson_inventory` **v1.4.1** ·
`gen_component` **v1.6.1** · `pill_sweep` **v1.1** · `gate_payload_match` **v1.9.6** ·
`build_family_map` **v1.6.6.8** · `callout_id` **v1.0** · `keyterm_prefix` **v1.0.1** · `build_mark_index` **v1.1.0** · `gen_bonus_banner` **v1.4.1** ·
`gen_part_banners` **v1.2** · `session_versions` **v1.34.0** · `fit_raster_svg` **v1.2** ·
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
