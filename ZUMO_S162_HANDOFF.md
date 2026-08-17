# ZUMO — S162 HANDOFF (written at S161 close · paste at top of Session 162)

## READ THIS FIRST

**S161's work IS PUSHABLE and DJ verifies the push himself (standing ruling, S158).**
`git rm ZUMO_S161_HANDOFF.md` is part of that push. Delete `__pycache__/` and
`quizzes/__pycache__/` first — they are not in the repo and eleven of them are sitting in the
working tree right now.

73/73 gates · `gate_payload_match` **PASS** · `callout_id` **1125/0** · 16 banks valid ·
`quiz_bank --selftest` ALL CONTROLS PASS · census **40,889** unchanged.

Files changed against the pushed clone (`4a9e1d1`), verified by md5 whole-tree diff:
`lessons/Lesson_06.html` · `_08` · `_10` · `book_gates.py` · `quizzes/quiz_bank.py` ·
`quizzes/ZUMO_QUIZ_L06.yaml` · `L07` · `L08` · `L09` · `L10` · `L11` · `L12` · `L13` · `L14` ·
`L15` · `L16` · `ZUMO_SUPER_BIBLE.md` · `LIVE_ZUMO_TEXTBOOK.md`.
**`byte_audit --check` WAS NOT RUN THIS SESSION AND DID NOT NEED TO BE** — no payload changed and
no `<pre>` was touched, asserted independently (see ARM 5 below). Run it at S162 open anyway.

---

# THE ONE THING TO CARRY OUT OF S161

**C1 IS RULED AND HALF-APPLIED, AND THE SLOGAN WAS THE DEFECT RATHER THAN THE ARGUMENT.**

*"Open loop needs TRIM. Closed loop does not"* fails on the book's own central function:
`driveDistance()` has encoders in its loop, so something IS watching, and the one-question test run
honestly returns *no TRIM* — while the book correctly puts TRIM on every straight line it drives.
**The practice was right in every lesson and the reason was wrong in every lesson.** That is why it
survived 150 sessions: nobody following the practice was ever contradicted by the robot.

**Read in full, the surrounding prose was ALREADY heading-scoped almost everywhere** — L10's KEY
TERM, L11's Quick Reference and L10's BC03 answer each explain it correctly and then end with the
unqualified slogan. **A correct argument with a false headline reads as canon, because the headline
is the part that gets quoted.** So this is a slogan sweep at four sentences per lesson, not a
rewrite, and it costs zero bytes.

Full canon with the six ruled phrasings in a table so nobody re-derives them: **Bible §16.31**.

**AND I SHIPPED L08 AND REPORTED IT COMPLETE WHILE ITS BANK STILL GRADED THE RETIRED RULE.**
`L08_B21`'s CORRECT ANSWER was the old one-question test verbatim, citing the section that had just
been corrected. Nothing gates a bank against the lesson version it keys, so 73 gates were green.
**A second predicate — sweeping the SLOGAN vocabulary instead of the co-occurrence window — is what
found it**, not a re-read. §24.6c, and the same shape as S160's *reported fourteen of fourteen.*

---

# WHAT THE DOUBLE CHECK ESTABLISHED (do not re-derive; these are properties)

**THE CO-OCCURRENCE COUNT IS NOT THE DEFECT COUNT.** TRIM within 120 chars of open/closed-loop
returns **150 windows** across 9 lessons, 6 banks and the Maker. A co-occurrence is not a claim
(§16.15). **The Maker's 89 collapse to exactly TWO comment blocks** — L11 `handleGap()` at **87**
payloads, L13 `driveUntil()` at **52** — re-derived by exact-string count, not by the dedup key that
first produced the figure. Both have a lesson `<pre>` twin and the gate holds them in lockstep, so
**they move WITH their lessons and are not a separate population.**

**THE SWEEP PREDICATE DOES NOT REACH THE TAGGED POPULATION.** Worklist **L15-08** — *"I is the only
term that can remove steady-state error"* — is tagged C1 and returns **ZERO** hits at any window
width, because it shares no vocabulary with the predicate. It is the sharpest instance in the whole
review (TRIM is feed-forward and CAN compensate a known bias, so *only* is false). **A second
predicate is owed before the population is claimed whole.**

**`gate_payload_match` PASS WAS NEVER EVIDENCE HERE.** It is one-directional (S160), so a line a
lesson prints that lives in no payload is invisible to it. Containment had to be checked separately:
**ARM 5 asserted that none of the eleven new strings landed inside any `<pre>`.** Do this whenever a
prose edit sits near printed code.

**A SESSION THAT CLOSES WITHOUT A `WHAT SHIPPED` BLOCK LOSES ITS NARRATIVE TO THE NEXT SESSION'S
HEADER.** S160 wrote no such block, so its whole narrative lived only in LIVE.md's Date/Status
header — and S161 overwrote that header. **Measured against the pushed clone: `C2 IS DONE` appeared
once there and zero times here.** Recovered VERBATIM from `4a9e1d1`, never reconstructed, and seated
as `## WHAT SHIPPED IN S160`. **This is the S151 defect recorded in v8.143, committed again one
session later by the operator who had just read that entry** — writing the rule down did not prevent
it; the third check did. **No gate can see this**: LIVE.md's history is prose and nothing counts it.
S161's own block exists, so the chain is intact — but the close-out step *write the block before you
touch the header* is now mandatory, not customary.

**A LINE-COUNT DELTA OF ZERO IS A REAL CHECK.** Every S161 edit landed inside an existing line, so
the census held at 40,889 and the clone-vs-work lesson line delta is **0** — independent
corroboration that nothing structural moved, obtained without trusting any gate.

---

# S162 NEXT

- **FINISH C1** (§16.31 lists the ruled phrasings). Remaining, derived not tagged:
  **L11 ×6** (§5.2, §7C, §8A.1 NOTE, BC answer, Glossary, Quick Reference *The TRIM Rule* table —
  the heaviest lesson) · **L03 ×2** (§5.3 and §8A.3 call manual TRIM tuning *closed-loop tuning*;
  worklist L03-05 says use *manual iterative tuning* / *human-in-the-loop* and keep *closed-loop
  control* pristine for L06/L08) · **L12 ×1** (§5.2 *TRIM is for open loops*) ·
  **`ZUMO_QUIZ_L11.yaml` ×2** · the two Maker-coupled comment blocks WITH their lesson twins ·
  **L15-08 under a predicate not yet written.**
- **L12 BONUS B4 IS NOT A SLOGAN FIX AND IS UNRULED** (worklist L12-18). Its premise is unsound: it
  claims adding TRIM makes the gyro turn *wrong*, but the gyro still supplies the stopping
  criterion, so TRIM changes pivot rate and overshoot rather than the final angle. GPT offers better
  sabotage candidates (a negative target without `abs()`; a reversed motor sign so the robot drives
  instead of spinning while the angle barely moves). **DJ ruling needed: re-premise inside C1, or
  split out after the slogan sweep closes.**
- **A-Star hardware identity fix** in L01 and L03 prose (KEY TERM `term-a-star`) — GPT P0, confirmed
  defect per the S154 fleet ruling, still not built. **§16.25 carries the inventory** (L01 15 hits:
  5 wrong-claim / 6 legitimate build target / 2 ids / 2 checklist; L03 10: 8 wrong-claim / 2 asset
  filename). `board = a-star32U4` in `platformio.ini` is CORRECT and must survive.
- **L03's photograph `L03_IMAGE_3-14_astar_board.jpg`** names a board the robot does not contain.
  Unruled.
- **§16.25's BODY IS STALE BY ONE SESSION** (present tense about lowercase `a-star32u4`; S155 made
  and applied that ruling). DJ ruled: RECORD IT. Doc-only. **Still not done.**
- **NOTHING COMPARES A BANK'S `source:` PIN AGAINST THE LIVE LESSON — 52 STALE PINS, MEASURED.**
  The strongest new gate candidate in the book, and §24.18 one layer up: a pin nothing compares is a
  version home with no comparator. Derived at S161 close across all 16 banks: **52 stale**, of which
  **only 3 are S161's** (`lesson_08 v04.31.1 → v04.32.0` in banks L11, L14 and L15); the other 49 are
  drift accumulated S148–S160. **All three were then READ and none is load-bearing:** L14's bank
  mentions TRIM zero times, L15's two mentions are a bias magnitude and a refactor precedent, and
  `L11_B44` cites **L11 §8A.1** rather than L08 — its stem is correct and stays, only its `why` tail
  carries the retired slogan, which is C1's own remaining L11 scope.
  **NO PIN WAS BUMPED, AND THAT IS THE RULING:** rewriting a provenance record asserts a read that
  never happened (rule 37, S146), and bumping 3 of 52 yields a tree where some pins are verified and
  some stale **with nothing marking which** — worse than one uniformly out of date and known to be
  (S148's L14 reasoning). The 49 need one ruled pass with the reads actually done, or the gate.
- **Remaining GPT worklist** beyond the canon statements — 245 findings, most unadjudicated.
  **L13-05** (wall/victim classifier presented as definitive) and **L13-11** (byte-match the quoted
  `readCalibrated()` against the bundled QTR in `Zumo32U4@2.0.1` — marked VERIFY, cheap and
  important) remain the strongest.
- **THE MAKER CHANGELOG RECORDS NOTHING BETWEEN v2.49 AND v2.58** — eight releases, no entry.
  Recorded, deliberately not back-filled.
- **ARM 2 IS BLIND TO A FIGURE STATED IN PROSE** (S159's stated blind spot, still unbuilt): §7C
  states its match-mode figure in prose rather than in a COMPILE CHECK. **L16 never states its
  match-mode figure at all** — 28,504 lives in the Maker, the Bible and LIVE.md and appears nowhere
  in `Lesson_16.html`.
- `bonus_b5`'s deliberate sabotage — positive `turnDegrees(AVOID_TURN_DEGREES)` under a comment
  reading *"Negative = left"* — **survived S161 untouched. Keep it that way.**
- **L15 Challenge 3 reads differently now** (S158, unchanged): it asks the student to invent
  `turnDegreesGyroSafe()`, which is what the book's own turns now do. Failure mode is a TIMEOUT,
  distinct from the kill switch, so it still teaches something. Recorded, not ruled.
- L03 queued content (ms unit, modulo explainer, Coach's Tips) · `ZUMO_L03_TEMPLATES.md` staging ·
  Bible §14 TDP-canon entry · day-by-day period grid + syllabus.
- **The poster is a GRADED deliverable** (DJ, S159), folded into the existing 25% row.
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

**CONTROLS, carried from S160 and NOT re-derived this session (no payload changed):**
L11 `after_step_1` **20,592** · `11/finished` **20,778** · `12/finished` **24,790** ·
`12/c2_slipalarm` **21,334** · `13/finished` **25,198** · `14/finished` **25,942** ·
`15/finished` **28,340** · `16/finished` **28,564**. **Reproduce the first one before trusting the
rest** (rule 30).

**To price a payload edit without touching the Maker:** `extract_project.py <maker> <lesson>
<kind> <outdir>` writes the resolved files; run `pio_harness.sh` on the dir.

---

# STANDING AUTHORITY — §24.17

**Decide and report; do not ask.** Three carve-outs: facts about the ROOM no instrument can see;
moves that are irreversible or expensive to undo (the test is recoverability); and RoboLore brand
and course scope. **Delegation removes the question, never the disclosure.** Full text: Bible §24.17.

**S161's worked example of the disclosure half, and it is the session's own defect:** I fixed L08's
prose, ran every instrument green, and reported the lesson COMPLETE. Its bank was still grading the
rule I had just retired. The disclosure is what makes that recoverable in one turn instead of a
defect a student meets in a graded quiz.

**AND A ONE-OFF SCRIPT OWES THE SAME PREDICATE DISCIPLINE AS THE GATE IT SERVES.** The bank bump
pinned DOUBLE QUOTES, died on L13's bare `bank_version: 1.0.1` after writing six files, and left
L13–L16 silently behind. The gate's own regex was quote-agnostic; only my script was not — S153's
finding committed again in the file S153 was written about (§24.18).

---

<!-- VERSION BLOCK: emitted by session_versions.py --handoff. Never hand-typed. -->
Fresh-clone verified at **`4a9e1d1`**. Census **40,889**.
Bible **v8.151** · `BookComponentStandard` **v01.13.0** · Maker **v2.58.3** ·
`marks/` **41** · `icons/` **49** incl. LICENSE.
`ZUMO_Syllabus_WORKING.md` **v1.3**.

Instruments: `book_gates` **v1.68.8** · `lesson_inventory` **v1.3.5** ·
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
`quiz_bank` **v1.1.0** ·
`timer.html` **v1.3.2** ·
`going_deeper` **v01.6.1**.

Lessons: L01 v03.28.5 · L02 v03.21.4 · L03 v03.41.1 · L04 v04.29.1 · L05 v04.29.0 · L06 v04.32.3 · L07 v04.31.4 · L08 v04.32.0 · L09 v05.27.1 · L10 v02.30.2 · L11 v02.30.2 · L12 v01.32.2 · L13 v02.31.1 · L14 v02.35.0 · L15 v02.31.4 · L16 v02.26.1.
