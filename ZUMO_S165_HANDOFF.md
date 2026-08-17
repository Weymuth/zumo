# ZUMO — S165 HANDOFF (written at S164 close · paste at top of Session 165)

## READ THIS FIRST

**S164's work IS PUSHABLE and DJ verifies the push himself (standing ruling, S158).**
`git rm ZUMO_S164_HANDOFF.md` is part of that push. **If `__pycache__/` or `quizzes/__pycache__/`
exist in your tree, delete them LAST, immediately before pushing** — they REGENERATE on every gate run.

**76/76 gates** · `gate_payload_match` **PASS both ends** · `callout_id` **1125/0** ·
`keyterm_prefix` **0 to convert** · 16 banks valid, 1,241 questions · `quiz_bank --selftest`
**ALL 24 CONTROLS PASS** · census **40,889 unchanged** · `site_parity` PARITY ·
`build_css --check` current at 574 rules · `image_audit --check` current · `next_pointer` clean.

**`byte_audit --check` WAS NOT RUN.** The harness is not in the repo and S164's work touched no
payload, no lesson file and no byte figure, so nothing it audits could have moved. **That is a
stated omission, not a pass** (rule 78). Rebuild the harness before any session that edits a payload.

**`UNREAD_PINS` 45 → 37.** Remaining, named not counted:
L09 ×3 · L10 ×4 · L11 ×5 · L12 ×4 · L13 ×6 · L14 ×5 · L15 ×5 · L16 ×5

**9 files changed** (derived from `git status --porcelain`, not typed): `LIVE_ZUMO_TEXTBOOK.md` · `ZUMO_AFTER_LAUNCH.md` · `ZUMO_SUPER_BIBLE.md` · `quizzes/ZUMO_QUIZ_L03.yaml` · `quizzes/ZUMO_QUIZ_L04.yaml` · `quizzes/ZUMO_QUIZ_L06.yaml` · `quizzes/ZUMO_QUIZ_L07.yaml` · `quizzes/ZUMO_QUIZ_L08.yaml` · `quizzes/quiz_bank.py`.
Plus **`ZUMO_S165_HANDOFF.md`** new and **`ZUMO_S164_HANDOFF.md`** deleted. **THE FIRST DERIVATION OF THIS LINE RETURNED EIGHT AND DROPPED
`LIVE_ZUMO_TEXTBOOK.md`** — the script called `.strip()` on the whole `git status` output, which ate the
leading space of the FIRST record's status column, so ` M` became `M` and the filter missed it. **A
generated count is only as good as the parse under it**, and the tell was that the one file every session
changes was absent. Redone without stripping the status columns.

---

# THE THREE THINGS TO CARRY OUT OF S164

## 1. A PROVENANCE LINE IS A CLAIM ABOUT A READ, NOT A READ.

Three of the four arcs found a `Verified against:` header naming a lesson version the gated
`source:` pin never reached — `QUIZ_L08` at v04.31.4/v04.31.3, `QUIZ_L07` at v04.31.4/v04.31.2,
`QUIZ_L06` at v04.32.2/v04.32.1. **And in each case the evidence beside the claim was aimed
elsewhere:** S149's sentence for `QUIZ_L08` describes Lesson_08's §5.4, and its `QUIZ_L07` twin puts
that lesson's changes in §5.3 where the diff is §6 and Challenge 4.

**The population was measured, not left at three: EIGHT header-newer pairs across seven banks**, and
the sweep separated them from **three pin-newer pairs** (L02/l01, L04/l04, L08/l08) which are **not
defects** — that is S162's ruling working as designed. Seven remain open, all in the backlog:
`QUIZ_L09`/l09 · `QUIZ_L09`/l08 · `QUIZ_L10`/l10 · `QUIZ_L10`/l08 · `QUIZ_L11`/l11 ·
`QUIZ_L12`/l12 · `QUIZ_L13`/l13.

**THEY ARE NOT AUTHORITY TO BUMP.** Every bump in S164 was earned by a read performed in S164.
A header claim tells you where somebody looked; it does not tell you they looked at the right file.

**NO GATE IS OWED, AND THAT WAS CONTROLLED.** The recurrence puts a pin below live with no backlog
entry, which gate 75's drift arm already catches — planted in `QUIZ_L05`, it FAILS §24.18 ALONE
naming *NEW drift*. The seven survive only because the S162 backlog absorbed them at creation, so the
condition can only shrink.

## 2. GATE 74 FIRED ON THIS SESSION'S OWN PROVENANCE AND WAS NOT WIDENED.

Writing the retired C1 wording into the `QUIZ_L03` and `QUIZ_L04` headers, to record what had
changed, made §16.31 FAIL naming both banks. **S163 gave gate 76 a structural comment-exemption for
exactly this — the honest record of a retired claim quotes it.**

**The disposition here is the opposite, and the reason is the population.** `L01_B14`'s distractor
IS the retired claim and cannot be reworded without destroying the question. My narration is prose
and reworded losslessly. Creating an exemption to accommodate my own sentence is rule 20 for no gain.

**If a future session needs to quote a retired form inside a bank comment, that is the moment to
revisit gate 74 — not before.**

## 3. THE HANDOFF'S QUEUED ITEM FOR `QUIZ_L03` RESTED ON A FALSE PREMISE.

The S164 handoff said the AFTER-set narration *"hand-tuning vs closed loop"* should move because L03
now says *manual iterative tuning*. **That narration describes BRAIN CHECK 03 Q5, which the diff does
not touch**, and Q5 still reads *"Your hand-tuned TRIM is the open-loop stepping stone … they use
closed-loop control."* The phrase that moved lives in §5.3 and §8A.3 — different sites.

The narration is accurate and STAYS. And S162's fix made Q5 **more** consistent with its lesson, not
less: before it, §5.3 gave that same loop the retired C1 label two sections from Q5 correctly calling
it open. **Rule 32 — a queue entry names a symptom; the artefact answers it.**

---

# S165 NEXT

- **THE 37 UNREAD PINS, ONE BANK AT A TIME, CHEAPEST FIRST.** All the single- and double-pin arcs are
  now closed; the cheapest remaining is **`QUIZ_L09` ×3**, whose l08 and l09 pins are both
  header-claimed. **The method that worked four times at S164:** resolve each pinned version to the
  commit that held it (`git log` per lesson file, match the `Lesson version:` comment), diff that
  commit against HEAD, map every changed line to its enclosing section heading, then read IN FULL
  every bank question that ASSERTS the changed material — not merely every question whose `cite`
  lands there, because an inherited-context pin (L08's `lesson_07`, L04's `lesson_03`) has no cite
  pointing at the other lesson at all.
- **A `--depth 1` clone cannot do that read.** `git fetch --filter=blob:none --unshallow` gives the
  history cheaply and took seconds at S164; the GitHub API rate-limits from this container.
- **THE `why` FIELD IS WHERE THESE DEFECTS LIVE.** Both of S164's content edits were `why` fields
  naming a fact their own `cite` no longer contained. QUIZ_SPEC §4 makes `cite:` a promise about
  where to re-read, and nothing gates a rationale against its section. Read every `why` in a changed
  region, not just every stem.
- **`ZUMO_AFTER_LAUNCH.md`** — read at every session open alongside this handoff. Its footer named
  `ZUMO_S163_HANDOFF.md`, deleted at that session's own push; re-aimed at S164 and it must be
  re-aimed at every close. Three items, all still open. **Absence from it does not mean an item was
  finished.**
- **ARM 2 IS STILL BLIND TO A FIGURE STATED IN PROSE** (S159's stated blind spot, still unbuilt):
  §7C states its match-mode figure in prose rather than in a COMPILE CHECK, and **L16 never states
  its match-mode figure at all** — 28,504 lives in the Maker, the Bible and LIVE.md and appears
  nowhere in `Lesson_16.html`.
- **THE MAKER CHANGELOG STILL RECORDS NOTHING BETWEEN v2.49 AND v2.58** — eight releases,
  deliberately un-back-filled.
- **L12 BONUS B4's bench measurement** — how far a Zumo walks sideways over a 90° and a 180° gyro
  turn with TRIM applied to one motor. The reveal deliberately states no number.
- `bonus_b5`'s deliberate sabotage — positive `turnDegrees(AVOID_TURN_DEGREES)` under a comment
  reading *"Negative = left"* — **survived S164 untouched. Keep it that way.**
- **L15 Challenge 3 reads differently now** (S158, unchanged): it asks the student to invent
  `turnDegreesGyroSafe()`, which is what the book's own turns now do. Failure mode is a TIMEOUT,
  distinct from the kill switch, so it still teaches something. Recorded, not ruled.
- **Remaining GPT worklist** — 245 findings, most unadjudicated. **L13-05** (wall/victim classifier
  presented as definitive) and **L13-11** (byte-match the quoted `readCalibrated()` against the
  bundled QTR in `Zumo32U4@2.0.1` — marked VERIFY, cheap and important) remain the strongest.
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

**CONTROLS — ALL EIGHT LAST RE-VERIFIED AT S163 ON A HARNESS BUILT FROM SCRATCH, NOT RE-RUN AT S164:**
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

**S164's worked example:** DJ answered three questions with *"I have no clue"* and *"I dont know.
What is best?"*, and for two of them the honest answer was **build nothing** and **stop and write
out**. Both were settled by measurement rather than by preference — the gate was declined because a
control proved gate 75 already holds the recurrence, and the session stopped reading pins because
unwritten findings die with the session. **A delegated question still owes a measured answer, not a
confident one.** The third — *should I give you the S163 handoff / AFTER_LAUNCH?* — was answered NO:
`ZUMO_AFTER_LAUNCH.md` is in the repo and was read at open, and the S163 handoff is recoverable from
git history in an unshallowed clone. **Never ask DJ to supply what the repo already holds.**

---

<!-- VERSION BLOCK: emitted by session_versions.py --handoff. Never hand-typed. -->
Fresh-clone verified at **`32e1ef5`**. Census **40,889**.
Bible **v8.156** · `BookComponentStandard` **v01.13.0** · Maker **v2.58.4** ·
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
`quiz_bank` **v1.4.5** ·
`timer.html` **v1.3.2** ·
`going_deeper` **v01.6.1**.

Lessons: L01 v03.30.0 · L02 v03.21.4 · L03 v03.43.0 · L04 v04.29.1 · L05 v04.29.0 · L06 v04.32.3 · L07 v04.31.4 · L08 v04.32.0 · L09 v05.27.2 · L10 v02.30.2 · L11 v02.31.0 · L12 v01.33.0 · L13 v02.31.2 · L14 v02.35.0 · L15 v02.31.5 · L16 v02.26.1.
