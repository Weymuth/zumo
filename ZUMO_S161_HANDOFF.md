# ZUMO — S161 HANDOFF (written at S160 close · paste at top of Session 161)

## READ THIS FIRST

**S160's work IS PUSHABLE and DJ verifies the push himself (standing ruling, S158).**
`git rm ZUMO_S160_HANDOFF.md` is part of that push. Delete `__pycache__/` and
`quizzes/__pycache__/` first — they are not in the repo.

73/73 gates · `gate_payload_match` **PASS** · `byte_audit --check` **PASS** (215 compiled) ·
`callout_id` 1125/0 · 16 banks valid.

Files changed against the pushed clone (`a0c836e`):
`lessons/Lesson_02.html` · `_06` · `_09` · `_10` · `_11` · `_12` · `_13` · `_15` · `_16` ·
`newproject.html` · `css/book.css` · `book_gates.py` · `ZUMO_SUPER_BIBLE.md` ·
`quizzes/ZUMO_QUIZ_L06.yaml` · `L09` · `L10` · `L11` · `L12` · `L13` · `LIVE_ZUMO_TEXTBOOK.md`.
**L01, L03, L04, L05, L07, L08 and L14 lesson files are untouched.**

---

# THE ONE THING TO CARRY OUT OF S160

**C2 IS DONE, AND THE TAGGED ROWS WERE A FLOOR RATHER THAN THE LIST.**

Fourteen worklist rows carry a C2 tag. The worklist header's own lesson list disagrees with them
— it names L04 and L08, which carry no C2 row, and omits L02, L15 and L16, which do. A book-wide
phrase sweep then found instances no tag marked: **Sabotage Mystery 1's answer**, **a variable
literally named `truth`** in L12's Challenge 2, and **three `why` fields in quiz banks**, which is
where these claims survive longest because nothing cites a distractor rationale.

**AND I REPORTED FOURTEEN OF FOURTEEN CLOSED WHILE L06-02 WAS STILL OPEN.** The sweep is what
caught it, not a re-read. Its fix turned out to be the best one in the pass: `driveDistance()` is
**closed-loop on DISTANCE and open-loop on HEADING**, which is why §3.6's table and Step 13's
*OPEN LOOP needs TRIM* were both correct and read as a contradiction for 150 sessions.

Full canon, with the nine replacement phrasings in a table so nobody re-derives them:
**Bible §16.30**.

---

# WHAT THE TRIPLE CHECK ESTABLISHED (do not re-derive; these are properties)

**`gate_payload_match` IS ONE-DIRECTIONAL.** It asks whether every PAYLOAD line appears in the
lesson corpus, never the reverse. **A line a lesson PRINTS that lives in no payload is invisible
to it** — which is exactly where a half-applied edit hid this session: a challenge SOLUTION was
renamed while its TEMPLATE was not, and the gate stayed green. Aim controls accordingly: one
payload character → FAIL(1); both lesson sites → FAIL(14).

**A BATCH THAT ASSERTS ON ITS LAST ITEM DISCARDS THE ONES THAT ALREADY SUCCEEDED**, because the
file write comes after the loop. A printed match count records that a string was FOUND, not that
the file was SAVED. Write and read back after each replacement.

**A PRINTED COMMENT LINE WEARS A `tok-` SPAN.** Growing a comment block by two lines moved
`.tok-7cbf6e` ×1501 → ×1503 and the `book.css` header census 22,462 → 22,464 — rules and
declarations UNCHANGED at 574/2,033, not even a usage rank. Baseline moved, blinding-controlled
after the move, restored md5-exact.

**A DUPLICATE QUESTION ID IS SILENT TO `quiz_bank.py --status` AND LOUD IN GATE §24.2.** The hold
exists; the hand-run tool will tell you a broken bank is fine. S153's shape one layer along.
**Recorded, not fixed** — it is a real candidate.

---

# S161 NEXT

- **C1 — TRIM justification backwards in L08** (practice correct, reason wrong; 2 occurrences).
  Small, ruled, and now the only adjudicated canon statement left unbuilt.
- **A-Star hardware identity fix** in L01 and L03 prose (KEY TERM `term-a-star`) — GPT P0,
  confirmed defect per the S154 fleet ruling, not yet built. **§16.25 carries the inventory**
  (L01 15 hits: 5 wrong-claim / 6 legitimate build target / 2 ids / 2 checklist; L03 10: 8
  wrong-claim / 2 asset filename). `board = a-star32U4` in `platformio.ini` is CORRECT and must
  survive.
- **L03's photograph `L03_IMAGE_3-14_astar_board.jpg`** names a board the robot does not contain.
  Unruled.
- **§16.25's BODY IS STALE BY ONE SESSION** (Bible ~line 2662 region, present tense about
  lowercase `a-star32u4`; S155 made and applied that ruling). DJ ruled: RECORD IT. Doc-only.
- **Remaining GPT worklist items** beyond the six canon statements — 245 findings in
  `ZUMO_GPT_REVIEW_WORKLIST.md`, most still unadjudicated. **L13-05** (the wall/victim classifier
  presented as definitive) and **L13-11** (byte-match the quoted `readCalibrated()` source against
  the bundled QTR in `Zumo32U4@2.0.1` — marked VERIFY, cheap and important) are the strongest.
- **THE MAKER CHANGELOG RECORDS NOTHING BETWEEN v2.49 AND v2.58** — eight releases bumped with no
  entry. Recorded, deliberately not back-filled.
- **ARM 2 IS BLIND TO A FIGURE STATED IN PROSE** (S159's stated blind spot, unbuilt and now
  queued): §7C states its match-mode figure in prose rather than in a COMPILE CHECK, so ARM 2 was
  silent when it moved. **L16 never states its match-mode figure at all** — 28,504 lives in the
  Maker, the Bible and LIVE.md and appears nowhere in `Lesson_16.html`.
- `bonus_b5`'s deliberate sabotage — positive `turnDegrees(AVOID_TURN_DEGREES)` under a comment
  reading *"Negative = left"* — **survived S160 intact. Keep it that way.**
- **L15 Challenge 3 reads differently now** (S158 note, unchanged): it asks the student to invent
  `turnDegreesGyroSafe()`, which is what the book's own turns now do. Failure mode is a TIMEOUT,
  distinct from the kill switch, so it still teaches something. Recorded, not ruled.
- L03 queued content (ms unit, modulo explainer, Coach's Tips) · `ZUMO_L03_TEMPLATES.md` staging ·
  Bible §14 TDP-canon entry · day-by-day period grid + syllabus.
- **The poster is a GRADED deliverable** (DJ ruling S159), folded into the existing 25% row.
- **Photography is OFF the critical path** (DJ, S156).

---

# HARNESS — IT IS NOT IN THE REPO, REBUILD IT

```
apt-get install -y gcc-avr avr-libc binutils-avr     # no sudo on this box
```
Clone FLAT into `/home/claude/harness` (read `LIBDIRS` out of the script, never from a handoff):
the eight Pololu repos plus `ArduinoCore-avr`, with `zumo-32u4-arduino-library` at
`--branch 2.0.1`. **`ArduinoCore-avr` goes at the TOP LEVEL of `/home/claude/harness`, not under
an `arduino/` subdirectory** — the script builds its includes as `$H/ArduinoCore-avr/...`, and
cloning it one level down yields `objects: 4` and every payload FAILing. Correct setup prints
**`objects: 41`**. Copy `pio_harness.sh` INTO the harness dir, then `bash pio_harness.sh --setup`.
`shim.cpp` is referenced and does not exist; the `[ -f ]` guard makes it optional.
Run `byte_audit.py --sizes` before `--check`.

**CONTROLS, reproduced at S160 from a fresh clone:** L11 `after_step_1` **20,592** ·
`11/finished` **20,778** · `12/finished` **24,790** · `12/c2_slipalarm` **21,334** ·
`13/finished` **25,198** · `14/finished` **25,942** · `15/finished` **28,340** ·
`16/finished` **28,564**.

**To price a payload edit without touching the Maker:** `extract_project.py <maker> <lesson>
<kind> <outdir>` writes the resolved files; run `pio_harness.sh` on the dir.

---

# STANDING AUTHORITY — §24.17

**Decide and report; do not ask.** Three carve-outs: facts about the ROOM no instrument can see;
moves that are irreversible or expensive to undo (the test is recoverability); and RoboLore brand
and course scope. **Delegation removes the question, never the disclosure.** Full text: Bible §24.17.

**S160's worked example of the disclosure half:** I reported five L12 edits as applied on the
strength of their printed match counts. They had never been written to disk. The triple check
found them because it re-derived from the artefact instead of re-reading the report — and the
disclosure is what makes that recoverable in one turn rather than a defect a student meets.

---

<!-- VERSION BLOCK: emitted by session_versions.py --handoff. Never hand-typed. -->
Fresh-clone verified at **`a0c836e`**. Census **40,889**.
Bible **v8.150** · `BookComponentStandard` **v01.13.0** · Maker **v2.58.3** ·
`marks/` **41** · `icons/` **49** incl. LICENSE.
`ZUMO_Syllabus_WORKING.md` **v1.3**.

Instruments: `book_gates` **v1.68.7** · `lesson_inventory` **v1.3.5** ·
`gen_component` **v1.6.1** · `pill_sweep` **v1.1** · `gate_payload_match` **v1.8.0** ·
`build_family_map` **v1.6.6** · `callout_id` **v1.0** · `keyterm_prefix` **v1.0.1** · `build_mark_index` **v1.1.0** · `gen_bonus_banner` **v1.4.1** ·
`gen_part_banners` **v1.2** · `session_versions` **v1.26.0** · `fit_raster_svg` **v1.2** ·
`flatten_alpha` **v1.2** · `svg_layout_audit` **v1.20** · `site_parity` **v1.1** ·
`build_css` **v1.3.0** ·
`image_audit` **v1.2** ·
`strip_inline` **v1.2** ·
`build_worklist` **v1.1** ·
`regex_audit` **v1.0** ·
`byte_audit` **v1.3.2** ·
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
`quiz_bank` **v1.0.1** ·
`timer.html` **v1.3.2** ·
`going_deeper` **v01.6.1**.

Lessons: L01 v03.28.5 · L02 v03.21.4 · L03 v03.41.1 · L04 v04.29.1 · L05 v04.29.0 · L06 v04.32.2 · L07 v04.31.4 · L08 v04.31.1 · L09 v05.27.1 · L10 v02.30.1 · L11 v02.30.2 · L12 v01.32.2 · L13 v02.31.1 · L14 v02.35.0 · L15 v02.31.4 · L16 v02.26.1.
