# ZUMO — S167 HANDOFF (written at S166 close · paste at top of Session 167)

## READ THIS FIRST

**S166's work IS PUSHABLE and DJ verifies the push himself (standing ruling, S158).**
`git rm ZUMO_S166_HANDOFF.md` is part of that push. **If `__pycache__/` or `quizzes/__pycache__/`
exist in your tree, delete them LAST, immediately before pushing** — they REGENERATE on every gate run.

**77/77 gates** · `gate_payload_match` **PASS both ends** · **`byte_audit --check` PASS across SIX
arms, all NINE controls** · `quiz_bank --selftest` **25 CONTROLS PASS** · `session_versions --selftest`
**EIGHT CONTROLS PASS** · `callout_id` **1125/0** · `keyterm_prefix` **0 to convert** · 16 banks valid,
1,241 questions · census **40,889 unchanged** · `site_parity` PARITY · `build_css --check` current at
574 rules · `image_audit --check` current · `next_pointer` clean.

**`UNREAD_PINS` 30 → 0. THE S162 BACKLOG IS EMPTY.** All six remaining arcs were read this session.
**§24.18 still earns its keep** — the gate now catches NEW drift with nothing to absorb it, which is a
stricter tree than the one that had a backlog, not a looser one.

**13 files changed, 1 new** (derived from `git status --porcelain`, not typed): `ZUMO_AFTER_LAUNCH.md` ·
`ZUMO_SUPER_BIBLE.md` · `byte_audit.py` · `lessons/Lesson_12.html` · `lessons/Lesson_16.html` ·
`quizzes/ZUMO_QUIZ_L11.yaml` · `quizzes/ZUMO_QUIZ_L12.yaml` · `quizzes/ZUMO_QUIZ_L13.yaml` ·
`quizzes/ZUMO_QUIZ_L14.yaml` · `quizzes/ZUMO_QUIZ_L15.yaml` · `quizzes/ZUMO_QUIZ_L16.yaml` ·
`quizzes/quiz_bank.py` · `session_versions.py` · `LIVE_ZUMO_TEXTBOOK.md`. Plus **`harness_setup.sh`
NEW**, **`ZUMO_S167_HANDOFF.md`** new and **`ZUMO_S166_HANDOFF.md`** deleted.

---

# THE THREE THINGS TO CARRY OUT OF S166

## 1. THE NUMBERS GET MAINTAINED. THE SENTENCES AROUND THEM DO NOT.

Every byte figure in `QUIZ_L13`, `QUIZ_L14`, `QUIZ_L15` and `QUIZ_L16` was **already correct** —
re-verified against a compile, not read — while the PROSE those figures sit inside was stale in all
four. `byte_audit` ARM 2 asserts a figure and ARM 5 asserts the arithmetic around it; **nothing
asserts the sentence that explains it.** So a re-baseline pass fixes what it can see and silently
leaves what it cannot, and the residue reads as consistent because each surviving sentence agrees
with itself.

`QUIZ_L16` still taught **two trades** where S158 shipped three — and `A01`, `A03`, `A10` and `A25`
were **already at three**, which is exactly why nobody noticed. `QUIZ_L14` taught one job where S159
gave `COMPETITION_MODE` two. `QUIZ_L13`'s `A09` asked *why does `RobotMotion.h` need an include it
never needed before* where the live Step 4 says the opposite. **A question's PREMISE can go stale
while its answer stays true, and no instrument in this repo reads a premise.**

## 2. A SWEEP FOR A PHRASE IS BLIND TO THE PHRASE WEARING MARKUP.

L12's BRAIN CHECK 01 answer carried the retired *measures intent, not result* two hundred lines from
§3.1's corrected NOTE, and it survived S160's book-wide C2 sweep **because it writes the phrase split
across `<em>` tags in lowercase**. The sweep matched the uppercase headline and could not match its
own twin. S165's escape finding in a new costume: **the string is there, wearing markup.** Any future
phrase sweep over this book has to strip tags before matching, or it is measuring source rather than
prose.

## 3. TWO CONTROL SUITES WERE RED OR BLIND, AND `--check` SAID PASS THROUGHOUT.

**`byte_audit --selftest` had been failing since S158** and nobody ran it. CONTROL A pinned
**20,516** where the standing control moved to **20,592**; CONTROL E seeded a literal string L16
stopped printing, so **the seed could not land**; CONTROL B compared against a bare 28,600. Three
spellings pinned inside the suite written to enforce rule 19. All three now derive.

**Then the triple check's own new arm went blind and its blinding control caught it.** A line-level
authorship arm reported 0 unclassified out of 279 changed lines; seeded with an undeclared
`points: 2` it stayed **SILENT**, because its `continuation` category was a catch-all matching every
indented line. **Rule 59, third firing this session: ask what your control reports when the property
does not hold.**

---

# S167 NEXT

- **A BANK-FIGURE GATE EXISTS NOW, AND ITS SCOPE IS STATED RATHER THAN EXCUSED.** `byte_audit`
  **ARM 6** asserts that a figure a bank LABELS as a named build equals that build's compile —
  5 claims across 3 banks, clean, six controls including a blinding one and a real-defect replay
  that fires it alone. **It reaches only *Lesson N finished* labels.** `L11_A09` says *"20,592 —
  the Lesson 10 project you started from"*, which is correct and which ARM 6 cannot see; that is
  the first evidence about where the vocabulary's edge sits. **Do not widen it until a real miss
  forces it** — a predicate widened against a population of zero defects is a guess.
- **`26,736` IS CORRECT BY MEASUREMENT AND GATED BY NOTHING.** It is labelled *what cutting the
  buzzer would give*, and the Maker defines no such payload. Recorded, not papered over.
- **THE HARNESS IS NOT IN THE REPO AND THE RECIPE NOW IS.** `sh harness_setup.sh` clones all nine
  repos at pinned SHAs, derives `LIBDIRS` out of `pio_harness.sh`, and fails if that script declares
  a library it does not clone. Rebuild takes minutes. **Vendoring is priced and NOT taken:** 746
  files / 27 MB, ~24 MB of it firmwares and drivers this build never opens, deletions need GitHub
  Desktop, and **ArduinoCore-avr ships no licence file at its root.** That last one is DJ's call,
  not an engineering one.
- **NOTHING GATES A BANK'S PROSE AGAINST ITS LESSON, AND THIS SESSION IS THE EVIDENCE.** Six arcs,
  fifteen content edits, and **every one was a sentence rather than a number.** If a gate is owed
  anywhere next, it is here — but the honest predicate is not obvious, and an instrument built on
  what you can reach rather than on what the property requires is the wrong instrument.
- **THE REMAINING GPT WORKLIST** — 245 findings, most unadjudicated. **L13-05** (wall/victim
  classifier presented as definitive) and **L13-11** (byte-match the quoted `readCalibrated()`
  against the bundled QTR in `Zumo32U4@2.0.1` — marked VERIFY, cheap, and **the harness is up**)
  remain the strongest.
- **`ZUMO_AFTER_LAUNCH.md`** — read at every session open alongside this handoff. Three items, all
  still open; its footer names the CURRENT handoff and must be re-aimed at every close. **It named a
  deleted file at S164 and again at S166.**
- **`site_parity` IS NOT TRUSTWORTHY ON ITS FIRST RUN AFTER A PUSH** (S166 post-push). The first
  run reported 1 MISMATCH; three runs after it reported PARITY, tree untouched — Pages was
  mid-rebuild. **Both directions are unsafe alone: a first-run MISMATCH is a phantom, and a
  first-run PARITY can be the OLD site agreeing with itself before the new content deploys.**
  That second case is the dangerous one because it passes. **Run it at least twice and believe
  the repeat.** Not gated — the honest predicate would have to poll the deployment.
- **FREE LEAD, MEASURED AND NOT CHASED:** `centre` appears in prose across at least eight lessons
  beside `center`. US-versus-British spelling has never been ruled.
- **GATE 77 DOES NOT EXCLUDE `<pre>`** (S165, unchanged). A lesson that legitimately prints a
  `\uXXXX` escape in a code block WILL fire it. No exemption written for a population of zero
  (rule 20); when it first fires, the answer is a ruling.
- **ARM 2 IS STILL BLIND TO A FIGURE STATED IN PROSE — AND S166 MEASURED IT RATHER THAN RESTATING
  IT.** L16 §7.4's stale *72 bytes* was invisible at 77/77 with `byte_audit` PASS; restoring it as a
  control is **SILENT**. **L16 still never states its match-mode figure at all** — 28,504 lives in
  the Maker, the Bible and LIVE.md and appears nowhere in `Lesson_16.html`.
- **THE MAKER CHANGELOG STILL RECORDS NOTHING BETWEEN v2.49 AND v2.58** — eight releases,
  deliberately un-back-filled.
- **L12 BONUS B4's bench measurement** — how far a Zumo walks sideways over a 90° and a 180° gyro
  turn with TRIM applied to one motor. The reveal deliberately states no number.
- `bonus_b5`'s deliberate sabotage — positive `turnDegrees(AVOID_TURN_DEGREES)` under a comment
  reading *"Negative = left"* — **survived S166 untouched. Keep it that way.**
- **L15 Challenge 3 reads differently now** (S158, unchanged): it asks the student to invent
  `turnDegreesGyroSafe()`, which is what the book's own turns now do. Recorded, not ruled.
- L03 queued content (ms unit, modulo explainer, Coach's Tips) · `ZUMO_L03_TEMPLATES.md` staging ·
  Bible §14 TDP-canon entry · day-by-day period grid + syllabus.
- **The poster is a GRADED deliverable** (DJ, S159), folded into the existing 25% row.
- **Photography is OFF the critical path** (DJ, S156).
- **Fall launch Sept 8 — three weeks out.**

---

# HARNESS — IT IS NOT IN THE REPO. RUN THE SCRIPT.

```
sh harness_setup.sh
```
**Invoke it through `sh`, not `./`.** The file is tracked **100644** — the executable bit did not
survive GitHub Desktop, so `./harness_setup.sh` fails on a fresh clone. `sh` works either way, and
that is the reason the instruction is written this way rather than the bit being chased (S166).
That is the whole recipe now. It installs the toolchain if missing, clones the nine repos at PINNED
SHAs, cross-checks them against `pio_harness.sh`'s own `LIBDIRS`, and builds the core. **Correct
setup prints `objects: 41`.** Then, in order:

```
python3 byte_audit.py --sizes     # compiles every payload the Maker defines
python3 byte_audit.py --check     # six arms
python3 byte_audit.py --selftest  # NINE controls - run this before trusting --check
```

**`apt-get` sat on *Reading package lists…* for ~5 minutes in the background at S163 and finished in
seconds in the foreground. The script runs it in the foreground.**

**CONTROLS — ALL EIGHT RE-VERIFIED AT S166 ON A HARNESS BUILT FROM SCRATCH BY THE SCRIPT:**
L11 `after_step_1` **20,592** · `11/finished` **20,778** · `12/finished` **24,790** ·
`12/c2_slipalarm` **21,334** · `13/finished` **25,198** · `14/finished` **25,942** ·
`15/finished` **28,340** · `16/finished` **28,564**. **Reproduce the first one before trusting the
rest** (rule 30) — `byte_audit` CONTROL A does exactly that, off `STANDING_CONTROL`, and its failure
message now names which side to suspect. The three declared overflows are `16/after_step_3` 28,950 ·
`16/after_step_4` 29,586 · `16/step_5_serial_traded` 28,882 — deliberate, and the lesson's own premise.

**To price a payload edit without touching the Maker:** `extract_project.py <maker> <lesson> <kind>
<outdir>` writes the resolved files; run `pio_harness.sh` on the dir.

---

# STANDING AUTHORITY — §24.17

**Decide and report; do not ask.** Three carve-outs: facts about the ROOM no instrument can see;
moves that are irreversible or expensive to undo (the test is recoverability); and RoboLore brand
and course scope. **Delegation removes the question, never the disclosure.** Full text: Bible §24.17.

**S166's worked example is the harness.** Rebuilding it, pinning the recipe into the repo and
registering both scripts were decided and reported — cheap, reversible, settled by measurement.
**Vendoring the harness was NOT decided**, and the reason is both carve-outs at once: 746 files whose
deletion needs DJ's hands, and a missing licence file that makes it a question about rights rather
than about bytes. The measurement was done and handed over; the ruling was not taken.

---

<!-- VERSION BLOCK: emitted by session_versions.py --handoff. Never hand-typed. -->
Fresh-clone verified at **`5d8366d`**. Census **40,889**.
Bible **v8.159.1** · `BookComponentStandard` **v01.13.0** · Maker **v2.58.4** ·
`marks/` **41** · `icons/` **49** incl. LICENSE.
`ZUMO_Syllabus_WORKING.md` **v1.3**.

Instruments: `book_gates` **v1.71.0** · `lesson_inventory` **v1.3.5** ·
`gen_component` **v1.6.1** · `pill_sweep` **v1.1** · `gate_payload_match` **v1.8.0** ·
`build_family_map` **v1.6.6** · `callout_id` **v1.0** · `keyterm_prefix` **v1.0.1** · `build_mark_index` **v1.1.0** · `gen_bonus_banner` **v1.4.1** ·
`gen_part_banners` **v1.2** · `session_versions` **v1.28.0** · `fit_raster_svg` **v1.2** ·
`flatten_alpha` **v1.2** · `svg_layout_audit` **v1.20** · `site_parity` **v1.1** ·
`build_css` **v1.3.0** ·
`image_audit` **v1.2** ·
`strip_inline` **v1.2** ·
`build_worklist` **v1.1** ·
`regex_audit` **v1.0** ·
`byte_audit` **v1.4.0** ·
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
`harness_setup.sh` **v1.0.1** ·
`pio_harness.sh` **v3.0** ·
`going_deeper` **v01.6.1**.

Lessons: L01 v03.30.0 · L02 v03.21.4 · L03 v03.43.0 · L04 v04.29.1 · L05 v04.29.0 · L06 v04.32.3 · L07 v04.31.4 · L08 v04.32.0 · L09 v05.27.3 · L10 v02.30.2 · L11 v02.31.0 · L12 v01.33.1 · L13 v02.31.2 · L14 v02.35.0 · L15 v02.31.5 · L16 v02.26.2.
