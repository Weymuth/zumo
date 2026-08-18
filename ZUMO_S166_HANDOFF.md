# ZUMO — S166 HANDOFF (written at S165 close · paste at top of Session 166)

## READ THIS FIRST

**S165's work IS PUSHABLE and DJ verifies the push himself (standing ruling, S158).**
`git rm ZUMO_S165_HANDOFF.md` is part of that push. **If `__pycache__/` or `quizzes/__pycache__/`
exist in your tree, delete them LAST, immediately before pushing** — they REGENERATE on every gate run.

**77/77 gates** · `gate_payload_match` **PASS both ends** · `callout_id` **1125/0** ·
`keyterm_prefix` **0 to convert** · 16 banks valid, 1,241 questions · `quiz_bank --selftest`
**ALL 24 CONTROLS PASS** · census **40,889 unchanged** · `site_parity` PARITY ·
`build_css --check` current at 574 rules · `image_audit --check` current · `next_pointer` clean.

**`byte_audit --check` WAS NOT RUN.** The harness is not in the repo. S165 touched no payload and
recompiled nothing — **A06's corrected figures were READ OUT OF THE LESSON, not compiled** — so
nothing it audits could have moved. **That is a stated omission, not a pass** (rule 78). Rebuild the
harness before any session that edits a payload or moves a byte figure.

**`UNREAD_PINS` 37 → 30.** Remaining, named not counted:
L11 ×5 · L12 ×4 · L13 ×6 · L14 ×5 · L15 ×5 · L16 ×5

**7 files changed** (derived from `git status --porcelain`, not typed): `LIVE_ZUMO_TEXTBOOK.md` ·
`ZUMO_SUPER_BIBLE.md` · `book_gates.py` · `lessons/Lesson_09.html` · `quizzes/ZUMO_QUIZ_L09.yaml` ·
`quizzes/ZUMO_QUIZ_L10.yaml` · `quizzes/quiz_bank.py`. Plus **`ZUMO_S166_HANDOFF.md`** new and
**`ZUMO_S165_HANDOFF.md`** deleted.

---

# THE THREE THINGS TO CARRY OUT OF S165

## 1. A CHARACTER ESCAPE IS NOT A SPELLING, AND §27.16 WAS RIGHT THE WHOLE TIME.

`Lesson_09.html` rendered `Section 7\u2019s Green Survey` and `the robot\u2019s centre` to every
reader from S160 to S165 — eight literal characters each, a Python `repr` written into prose by the
C2 pass. **§27.16 is not broken and needed no widening.** It rules ONE SPELLING PER CHARACTER and
has exactly two cases, literal and entity, because nothing in this book had ever written a character
a third way. **An escape is not a second spelling of a character the gate knows about — it is a
character the gate has never met wearing seven others as a costume**, every one of them ordinary and
legal. `entity_sweep` sweeps CHARACTERS and a backslash is a legal one; `glyph_scan` reads GLYPH
fields. **A rule stated over spellings of a character is blind to a construct that is not a
character at all.**

**GATE 77 / §27.16a** covers `\uXXXX`, `\UXXXXXXXX` and `\xNN` in rendered text and in the banks,
with `<script>`/`<style>` excluded by property. Population measured script-aware BEFORE the gate was
written: exactly two, both in one lesson, against a nine-per-lesson baseline that is entirely inside
the Brain Check button script and correct.

**TWO HARNESS FAILURES, BOTH CAUGHT BY md5 AND NEITHER BY A GATE.** The first bank-field plant broke
the YAML and fired four gates — it measured *malformed bank*, not the property. And the batched
five-control harness timed out mid-run and left a plant on disk in `Lesson_05.html`. **A batch is not
a control harness, because a batch that dies leaves the tree in a state nothing declared.** One
control per invocation, with an explicit timeout, and md5 both ends.

## 2. NOTHING GATES A BANK FIGURE AGAINST ITS LESSON, AND ONE WAS COSTING STUDENTS MARKS.

`QUIZ_L10`'s **A06 keyed *+50 bytes over Step 3* as its CORRECT answer.** S157 recompiled L10's
chain and the lesson has read **+44** since v02.30.0. **Both numeric distractors were stale too** —
*+660* is **+710**, *+194* is **+176** — so all three figures in one item were superseded and a
student reading the live lesson and answering +44 was marked wrong.

**`byte_audit` ARM 2 asserts the LESSON's figures against a compile and has never read a bank;
§24.18 compares a `source:` PIN and is silent on what the questions say.** The S162 backlog is what
carried this in — the defect was invisible until the pin forced the read. **That is a live gate
candidate and it was deliberately not built this session**, because the honest predicate needs a
compile and the harness is not in the repo.

**The figures were re-derived from the artefact and mapped to their own steps** — +44 Step 4, +44
Step 6b, +176 Step 7, +710 Step 8, 20,592 Step 9. **L10 now prints +44 TWICE**, so a swap driven off
the changelog had one chance in two of landing on the wrong one.

## 3. AN `<h2>/<h3>` WALK IS NOT A SECTION MAP IN THIS BOOK.

Mapping L09's changed lines put NOTE 9.59 and the troubleshooting table in §7.2, which read as B31
and B32 citing a §8 that does not contain their answers — a §24.18-shaped finding that was not one.
**§8's banner is a `<div>`, not a heading**, so the parser's last-heading-seen was two sections
stale. The citations were correct and the instrument was not. **Any section mapping in this book has
to read the banner divs, not just the heading tags.**

---

# S166 NEXT

- **THREE MORE STALE FIGURES ARE NAMED AND UNFIXED, ALL IN `QUIZ_L16`** (S165 double check, ARM 3).
  `L16_B03`'s `why` calls **24,694** *Lesson 12 finished* where the live L12 says **24,790** in six
  places; `L16_A10` and `L16_A25` both carry **26,928** as *what cutting the buzzer would give*, a
  figure consistent with a baseline S148 superseded; and `L16_A25`'s extra_answer offers **20,516 —
  the Lesson 10 finished build**, which is A06's defect in a second bank (live: 20,592). **All three
  appear in no lesson in the book.** Two are derivable and **26,928 is not** — it needs the finished
  build minus a buzzer nobody has recompiled since S148 — so v8.136's ruling applies: **fix a bank's
  figures whole or not at all.** They belong to the `QUIZ_L16` arc, and that arc needs the harness.
- **GATE 77 DOES NOT EXCLUDE `<pre>`, AND THAT IS RECORDED RATHER THAN EXCUSED.** A backslash census
  of rendered text returns 16, all correct — `\n`, `\t`, `\0` in printed C code and one Windows
  path — and none matches the predicate today. A lesson that legitimately prints a `\xNN` or
  `\uXXXX` escape in a code block WILL fire it. **No exemption was written for a population of zero
  (rule 20). When it first fires, the answer is a ruling.**
- **THE 30 UNREAD PINS, ONE BANK AT A TIME, CHEAPEST FIRST.** The cheapest remaining is
  **`QUIZ_L12` ×4** and **`QUIZ_L11` ×5**; L11's l03/l06/l08/l10/l11 and L12's l06/l09/l11/l12 both
  reuse diffs already mapped in S164 and S165, so the marginal cost per bank is one or two new diffs
  plus the bank read. **The method, unchanged and worth restating:** resolve each pinned version to
  the commit that held it, diff that commit against HEAD, map every changed line to its enclosing
  section *by banner*, then read IN FULL every question that ASSERTS the changed material — not
  merely every question whose `cite` lands there.
- **A `--depth 1` clone cannot do that read.** `git fetch --filter=blob:none --unshallow` gives the
  history cheaply and takes seconds; the GitHub API rate-limits from this container.
- **READ THE `why` AND THE OPTION TEXT, NOT JUST THE STEM.** Three of the last four content edits
  across S164 and S165 were `why` fields or distractor text. The fourth was a correct answer's
  number. **Nothing gates a rationale against its section and nothing gates a figure against its
  lesson.**
- **A BANK-FIGURE GATE IS OWED AND UNBUILT** (see item 2). It needs the harness, so it belongs to a
  session that is rebuilding it anyway.
- **`ZUMO_AFTER_LAUNCH.md`** — read at every session open alongside this handoff. Three items, all
  still open; its footer names the CURRENT handoff and must be re-aimed at every close.
- **ARM 2 IS STILL BLIND TO A FIGURE STATED IN PROSE** (S159's stated blind spot, still unbuilt):
  §7C states its match-mode figure in prose rather than in a COMPILE CHECK, and **L16 never states
  its match-mode figure at all** — 28,504 lives in the Maker, the Bible and LIVE.md and appears
  nowhere in `Lesson_16.html`.
- **THE MAKER CHANGELOG STILL RECORDS NOTHING BETWEEN v2.49 AND v2.58** — eight releases,
  deliberately un-back-filled.
- **L12 BONUS B4's bench measurement** — how far a Zumo walks sideways over a 90° and a 180° gyro
  turn with TRIM applied to one motor. The reveal deliberately states no number.
- `bonus_b5`'s deliberate sabotage — positive `turnDegrees(AVOID_TURN_DEGREES)` under a comment
  reading *"Negative = left"* — **survived S165 untouched. Keep it that way.**
- **L15 Challenge 3 reads differently now** (S158, unchanged): it asks the student to invent
  `turnDegreesGyroSafe()`, which is what the book's own turns now do. Recorded, not ruled.
- **Remaining GPT worklist** — 245 findings, most unadjudicated. **L13-05** (wall/victim classifier
  presented as definitive) and **L13-11** (byte-match the quoted `readCalibrated()` against the
  bundled QTR in `Zumo32U4@2.0.1` — marked VERIFY, cheap and important) remain the strongest.
- **FREE LEAD, MEASURED AND NOT CHASED:** `centre` appears in prose across at least eight lessons
  beside `center`. US-versus-British spelling has never been ruled and was not treated as S165's
  business.
- L03 queued content (ms unit, modulo explainer, Coach's Tips) · `ZUMO_L03_TEMPLATES.md` staging ·
  Bible §14 TDP-canon entry · day-by-day period grid + syllabus.
- **The poster is a GRADED deliverable** (DJ, S159), folded into the existing 25% row.
- **Photography is OFF the critical path** (DJ, S156).
- **Fall launch Sept 8** — three weeks out.

---

# HARNESS — IT IS NOT IN THE REPO, REBUILD IT

```
apt-get install -y gcc-avr avr-libc binutils-avr     # no sudo on this box
```
**`apt-get` sat on *Reading package lists…* for ~5 minutes in the background at S163 and finished in
seconds in the foreground. Run it in the foreground.**

Clone FLAT into `/home/claude/harness` (read `LIBDIRS` out of the script, never from a handoff):
the eight Pololu repos plus `ArduinoCore-avr`, with `zumo-32u4-arduino-library` at
`--branch 2.0.1`. **`ArduinoCore-avr` goes at the TOP LEVEL of `/home/claude/harness`, not under
an `arduino/` subdirectory.** Correct setup prints **`objects: 41`**. Copy `pio_harness.sh` INTO the
harness dir, then `bash pio_harness.sh --setup`. `shim.cpp` is referenced and does not exist; the
`[ -f ]` guard makes it optional. Run `byte_audit.py --sizes` before `--check`.

**CONTROLS — ALL EIGHT LAST RE-VERIFIED AT S163 ON A HARNESS BUILT FROM SCRATCH, NOT RE-RUN SINCE:**
L11 `after_step_1` **20,592** · `11/finished` **20,778** · `12/finished` **24,790** ·
`12/c2_slipalarm` **21,334** · `13/finished` **25,198** · `14/finished` **25,942** ·
`15/finished` **28,340** · `16/finished` **28,564**. **Reproduce the first one before trusting the
rest** (rule 30). The three declared overflows are `16/after_step_3` 28,950 · `16/after_step_4` 29,586 ·
`16/step_5_serial_traded` 28,882 — deliberate, and the lesson's own premise.

**To price a payload edit without touching the Maker:** `extract_project.py <maker> <lesson>
<kind> <outdir>` writes the resolved files; run `pio_harness.sh` on the dir.

---

# STANDING AUTHORITY — §24.17

**Decide and report; do not ask.** Three carve-outs: facts about the ROOM no instrument can see;
moves that are irreversible or expensive to undo (the test is recoverability); and RoboLore brand
and course scope. **Delegation removes the question, never the disclosure.** Full text: Bible §24.17.

**S165's worked example:** the session opened on a routine pin arc and the first diff contained a
student-visible defect. **The fix, the gate, the five controls and the Bible section were decided and
reported, not asked** — none of them touches the room, none is expensive to undo, and every one was
settled by measurement. The one thing NOT decided was the bank-figure gate item 2 calls for, because
its honest predicate needs a compile and the harness is not in the repo: **an instrument built on
what you can reach today, rather than on what the property requires, is the wrong instrument.**

---

<!-- VERSION BLOCK: emitted by session_versions.py --handoff. Never hand-typed. -->
Fresh-clone verified at **`564fd7e`**. Census **40,889**.
Bible **v8.158.1** · `BookComponentStandard` **v01.13.0** · Maker **v2.58.4** ·
`marks/` **41** · `icons/` **49** incl. LICENSE.
`ZUMO_Syllabus_WORKING.md` **v1.3**.

Instruments: `book_gates` **v1.71.0** · `lesson_inventory` **v1.3.5** ·
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
`quiz_bank` **v1.4.7** ·
`timer.html` **v1.3.2** ·
`going_deeper` **v01.6.1**.

Lessons: L01 v03.30.0 · L02 v03.21.4 · L03 v03.43.0 · L04 v04.29.1 · L05 v04.29.0 · L06 v04.32.3 · L07 v04.31.4 · L08 v04.32.0 · L09 v05.27.3 · L10 v02.30.2 · L11 v02.31.0 · L12 v01.33.0 · L13 v02.31.2 · L14 v02.35.0 · L15 v02.31.5 · L16 v02.26.1.
