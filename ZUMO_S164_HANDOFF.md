# ZUMO — S164 HANDOFF (written at S163 close · paste at top of Session 164)

## READ THIS FIRST

**S163's work IS PUSHABLE and DJ verifies the push himself (standing ruling, S158).**
`git rm ZUMO_S163_HANDOFF.md` is part of that push. **If `__pycache__/` or `quizzes/__pycache__/`
exist in your tree, delete them LAST, immediately before pushing** — they REGENERATE on every gate run.

**76/76 gates** (was 75) · `gate_payload_match` **PASS both ends** · `callout_id` **1125/0** ·
`keyterm_prefix` **0 to convert** · 16 banks valid, 1,241 questions · `quiz_bank --selftest`
**ALL 24 CONTROLS PASS** — the S163 handoff said 14, which was 8 + 6 carried as arithmetic rather than
read off the run (rule 50) · census **40,889 unchanged** · `byte_audit --check` **PASS**, all eight
carried controls reproduced exactly on a harness rebuilt from scratch.

**`UNREAD_PINS` 48 → 45.** Remaining, named not counted:
L03 ×2 · L04 ×2 · L06 ×1 · L07 ×2 · L08 ×1 · L09 ×3 · L10 ×4 · L11 ×5 · L12 ×4 · L13 ×6 ·
L14 ×5 · L15 ×5 · L16 ×5.

**7 files changed** at the S163 push (`2899729`): `LIVE_ZUMO_TEXTBOOK.md` · `ZUMO_SUPER_BIBLE.md` ·
`book_gates.py` · `lessons/Lesson_01.html` · `quizzes/quiz_bank.py` ·
`quizzes/ZUMO_QUIZ_L01.yaml` · `quizzes/ZUMO_QUIZ_L02.yaml`, plus `ZUMO_S164_HANDOFF.md` new and
`ZUMO_S163_HANDOFF.md` deleted. **THE FIRST DRAFT OF THIS LINE SAID SIX AND THEN LISTED SEVEN**, in
the clause claiming the count came off the generator — rule 50 committed in the sentence citing it,
and it shipped. Caught at the post-push verification, not by re-reading. **A follow-up push
(`book_gates` v1.70.1 · Bible v8.155.1 · this file · LIVE.md) corrects it and hardens gate 76.**

---

# THE THREE THINGS TO CARRY OUT OF S163

## 1. AN INVENTORY OF A TERM IS NOT AN INVENTORY OF THE CLAIM'S HOMES.

§16.25 shipped at S162 off an inventory of the word *A-Star*, re-derived row for row, and the inventory
was **complete**. Two sentences restate the retired claim and **contain no A-Star at all**:

- **L01 §3.3's NOTE** made *"controller board"* a synonym for the chip — **two lines under the new KEY
  TERM that separates board from chip.** That NOTE is a better-evidenced mechanism for DJ's post-fix
  restatement (`ZUMO_AFTER_LAUNCH.md` item 1) than "the KEY TERM sits too deep in the page": the page
  licensed the wrong reading in prose.
- **L01 §5.0's `board` bullet** glossed the build-target line as *"the exact board, so the compiler knows
  its memory size and pin layout"* — which §3.3 and §5.5 now contradict **in the same file.**

Both corrected. **`"controller board"` existed in exactly two places in the whole tree** — that sentence
and `QUIZ_L01` B56, which graded it TRUE — so the fix was two lines and the population was measured
before either moved.

**AND §5.0's BULLET LIST HAS NOW DONE THIS TWICE.** `QUIZ_L01`'s own header records S141 finding the same
list contradicting §8 about `monitor_speed`, S136 having fixed §8 and missed §5.0. **Same section, same
construct, same failure, two rulings apart.** If a third correction ever touches §3.3 or §5.5, read §5.0's
bullet list in the same pass.

**The hoist in `ZUMO_AFTER_LAUNCH.md` item 1 was NOT taken** — it is deferred past Sept 8 by DJ ruling,
and this was a correctness fix rather than the polish that was declined. Item 1's evidence paragraph is
now weaker than it was: the mechanism may have been the NOTE, which is gone.

## 2. GATE 76's EXEMPTIONS ARE STRUCTURAL, AND ITS FIRST RUN FIRED ON THIS SESSION'S OWN RECORDS.

Six retired identity forms are forbidden **outright** in all sixteen lessons and the Maker. In the banks
they are forbidden **only where a question ASSERTS them**: a `#` comment is provenance and a
`correct: false` option is the trap being taught. That is not a name list and not an exemption anybody has
to remember — it is a property of where the string sits (rule 20).

**This matters because the honest record of a retired claim quotes it.** The first run of gate 76 flagged
the very provenance comments this session wrote into `QUIZ_L01`'s header, and `L01_B14`'s new distractor
*is* the retired claim, deliberately.

**AND ITS COVERAGE ARM WAS BLIND WHEN IT SHIPPED, WHICH A CONTROL FOUND AFTER THE PUSH.** It
compared SCANNED against FOUND — both from its own globs — so an **empty** population left both at
zero and passed. Measured rather than argued: with every bank moved aside, gate 76 printed **PASS**
while §24.2 and §24.18 fired. **`book_gates` v1.70.1** adds a POPULATION arm whose denominator is the
suite's own lesson list (rule 29): every lesson plus the Maker, and one bank per lesson. Controlled
three ways — banks emptied is now LOUD naming *asserted 17 pages and 0 banks against 16 lessons* ·
the Maker removed is LOUD on the original coverage arm · the untouched tree PASSES at 76 of 76.
**Rule 27 committed inside the arm written to satisfy rule 27.**

Six controls, **one per invocation with an explicit timeout** (S162's contaminated-tree lesson):
lesson prose LOUD · retired wording as a `correct: true` option LOUD naming `L01_B14` · two retired forms
inside a `correct: false` option SILENT · retired forms in a YAML comment SILENT · **blinding reword of an
unrelated L05 paragraph SILENT, and the md5 was checked mid-flight to prove the plant landed** — a
blinding control that changes nothing proves nothing.

Gate 75 was also controlled in both directions on this session's own move: pin reverted with the backlog
entry deleted → FAIL as **new drift**; pin bumped with the entry restored → FAIL as an **unearned bump**.

## 3. TWO NUMBERS IN THE INCOMING HANDOFF WERE WRONG, AND BOTH WERE FIXABLE BY READING THE INSTRUMENT.

- **`quiz_bank --selftest` names and passes 24 controls, not 14.** The handoff computed 8 + 6 from the
  session that added Q–V instead of reading the run. Rule 50 on a control count.
- **−162 B is WEAVE, not Ziegler–Nichols.** L16 prices the Z-N hint at **156** and the WEAVE removal at
  **162**. Both chains close: 28,726 − 162 = 28,564 (finished) and 28,726 + 156 = 28,882 (the measured
  `step_5_serial_traded`). Only the label was wrong.
- **And the L16 ceiling item was already closed in the tree.** `16/finished` compiles to **28,564**, 108
  under the 28,672 ceiling; **28,726 is a deliberate mid-Step-5 waypoint** the lesson itself calls *"Still
  over. By 54."* It has been carried as open since S158 — rule 32, third session running.

---

# S164 NEXT

- **THE 45 UNREAD PINS, ONE BANK AT A TIME, CHEAPEST FIRST.** L06 ×1 and L08 ×1 are single-pin arcs;
  L03/L04/L07 are ×2. Each arc bumps its own pin and deletes its `UNREAD_PINS` entries **in the same
  commit** — gate 75 fails if they separate. **The method that worked twice at S163:** resolve each pinned
  version to the commit that held it (`git log` per lesson file, match the `Lesson version:` comment),
  diff that commit against HEAD, map every changed line to its enclosing anchor, then read in full every
  bank question whose `cite` lands in a changed region. Both S163 arcs were one diff each because the pins
  resolved to a single commit.
- **A `--depth 1` clone cannot do that read.** `git fetch --filter=blob:none --unshallow` gives the
  history cheaply; the GitHub API rate-limits from this container.
- **`ZUMO_QUIZ_L03`'s header comment** narrates *"hand-tuning vs closed loop"* as an asked topic; L03 now
  says *manual iterative tuning*. Prose narration, not a graded claim — should move when L03's bank is next
  touched, which is now due (L03 ×2 pins).
- **L12 BONUS B4's bench measurement** — how far a Zumo walks sideways over a 90° and a 180° gyro turn
  with TRIM applied to one motor. The reveal deliberately states no number.
- **`ZUMO_AFTER_LAUNCH.md`** — read at every session open alongside this handoff. Three items: L01 §3.3's
  one-liner hoist (its evidence is now weaker, see above) · the L03 photograph filename · migrating the
  pre-S162 deferred queue in from git history rather than from memory. **Absence from it does not mean an
  item was finished.**
- **ARM 2 IS STILL BLIND TO A FIGURE STATED IN PROSE** (S159's stated blind spot, still unbuilt): §7C
  states its match-mode figure in prose rather than in a COMPILE CHECK, and **L16 never states its
  match-mode figure at all** — 28,504 lives in the Maker, the Bible and LIVE.md and appears nowhere in
  `Lesson_16.html`.
- **THE MAKER CHANGELOG STILL RECORDS NOTHING BETWEEN v2.49 AND v2.58** — eight releases, deliberately
  un-back-filled.
- `bonus_b5`'s deliberate sabotage — positive `turnDegrees(AVOID_TURN_DEGREES)` under a comment reading
  *"Negative = left"* — **survived S163 untouched. Keep it that way.**
- **L15 Challenge 3 reads differently now** (S158, unchanged): it asks the student to invent
  `turnDegreesGyroSafe()`, which is what the book's own turns now do. Failure mode is a TIMEOUT, distinct
  from the kill switch, so it still teaches something. Recorded, not ruled.
- **Remaining GPT worklist** — 245 findings, most unadjudicated. **L13-05** (wall/victim classifier
  presented as definitive) and **L13-11** (byte-match the quoted `readCalibrated()` against the bundled
  QTR in `Zumo32U4@2.0.1` — marked VERIFY, cheap and important) remain the strongest.
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

**CONTROLS — ALL EIGHT RE-VERIFIED AT S163 ON A HARNESS BUILT FROM SCRATCH:**
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

**S163's worked example:** DJ asked which reporting shape he preferred and then delegated the choice.
The L01 prose fix, the three bank edits, the new gate and the version bumps were all decided and
reported rather than asked — and the one thing that WAS surfaced before acting is the thing §24.17
reserves: whether a §3.3 edit should wait for Sept 8 alongside the deferred hoist.

---

<!-- VERSION BLOCK: emitted by session_versions.py --handoff. Never hand-typed. -->
Fresh-clone verified at **`2899729`**. Census **40,889**.
Bible **v8.155.1** · `BookComponentStandard` **v01.13.0** · Maker **v2.58.4** ·
`marks/` **41** · `icons/` **49** incl. LICENSE.
`ZUMO_Syllabus_WORKING.md` **v1.3**.

Instruments: `book_gates` **v1.70.1** · `lesson_inventory` **v1.3.5** ·
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
`quiz_bank` **v1.4.2** ·
`timer.html` **v1.3.2** ·
`going_deeper` **v01.6.1**.

Lessons: L01 v03.30.0 · L02 v03.21.4 · L03 v03.43.0 · L04 v04.29.1 · L05 v04.29.0 · L06 v04.32.3 · L07 v04.31.4 · L08 v04.32.0 · L09 v05.27.2 · L10 v02.30.2 · L11 v02.31.0 · L12 v01.33.0 · L13 v02.31.2 · L14 v02.35.0 · L15 v02.31.5 · L16 v02.26.1.
