# ZUMO — S168 HANDOFF (written at S167 close · paste at top of Session 168)

## READ THIS FIRST

**S167's work IS PUSHABLE and DJ verifies the push himself (standing ruling, S158).**
`git rm ZUMO_S167_HANDOFF.md` is part of that push. **If `__pycache__/` or `quizzes/__pycache__/`
exist in your tree, delete them LAST, immediately before pushing** — they REGENERATE on every gate run.

**77/77 gates** · `gate_payload_match` **PASS both ends** · **`byte_audit --check` PASS across six arms,
`--selftest` ALL NINE CONTROLS PASS** (harness rebuilt from scratch by the script, `objects: 41`,
standing control **20,592** first) · `quiz_bank --selftest` all controls · `session_versions --selftest`
EIGHT CONTROLS · `callout_id` **1125/0** · `keyterm_prefix` 0 to convert · 16 banks valid,
**1,242** questions · census **40,890** · `site_parity` PARITY on two consecutive runs ·
`build_css --check` current at 574 rules · `image_audit --check` current · `next_pointer` clean.

**12 files changed on the post-push pass** (L15 · ten banks · `newproject.html`), plus `ZUMO_SUPER_BIBLE.md`, `LIVE_ZUMO_TEXTBOOK.md` and this handoff. Fifteen lessons (all but L12) · sixteen banks · `newproject.html` ·
`ZUMO_SUPER_BIBLE.md` · `ZUMO_AFTER_LAUNCH.md` · `LIVE_ZUMO_TEXTBOOK.md` · **`ZUMO_S168_HANDOFF.md` new**
and **`ZUMO_S167_HANDOFF.md` deleted**.

---

# THE THREE THINGS TO CARRY OUT OF S167

## 1. THE FIRST MEASUREMENT SAID 19 AND THE TRUE POPULATION WAS 477.

DJ ruled **US spelling book-wide**, then ruled `center` for L14's RCJ transcription too. Scoping the
sweep to `centre` returned 19 lesson sites. The axis is a SPELLING SYSTEM, and the whole British set
returned **72 lesson sites, 130 bank strings and 274 in the Maker**. §24.6c on a predicate: scoping the
instrument to the lead's own vocabulary guarantees you measure only what you were already told.

**And the Maker's entire 274 is ONE WORD that is not a spelling — it is an IDENTIFIER.** `centre`
appears **zero** times in `newproject.html`; all 274 are `travelled`, of which 89 are the local in
L11's `blindDistanceCm()`. **Proved zero-byte rather than asserted:** all 215 payloads recompiled,
**0 of 430 stored figures moved.**

## 2. FIFTEEN LESSON BUMPS PUT 57 BANK PINS STALE AT ONCE, AND THE BUMPS WERE EARNED BY A CLOSED DIFF.

Gate 75 fired on every one — §24.18 working as designed with an empty backlog. Rule 37 says a pin bump
asserts a read; here the read is machine-closed and was **ASSERTED rather than claimed**: every changed
file diffed against a pre-sweep snapshot under a normalising transform, and **every one contains nothing
but swept words and its own version line**, L13 alone showing this session's two content edits.

**And the pin regex found S153's defect again: the banks spell their pins BOTH WAYS**, quoted and bare,
so the first pass moved 0 of 57 and reported success on files it had not touched.

## 3. GATE 74 HAS A BLIND REGION IN `newproject.html`, AND MY OWN EDIT EXPOSED IT BY ACCIDENT.

Writing the Maker changelog entry made gate 74 FAIL, naming a retired C1 slogan that had sat in the
**v2.58.4** entry since S162 with the gate GREEN throughout. Cause: gate 74 strips tags with
`re.sub(r'<[^>]+>', ' ', s)`, and `[^>]+` runs from any `<` to the next `>`, so a span of the Maker's
changelog comment is swallowed as one tag. **My entry contained the literal `<pre>`, whose `>` closed
the swallow early; removing it re-hid the slogan and the gate went green again.** The narration was
therefore REWORDED rather than the mask relied on. **NINE gates share the same tag-strip idiom** —
measured, not fixed, because widening nine gates three weeks from launch is a blast radius nobody has
measured (rule 26).

## 4. THREE PREDICATES, THREE UNDER-REACHES, AND EVERY ONE WAS A WORD LIST.

The sweep was declared complete three times and was wrong three times. The first list missed the `-ise`
family and `defence` (**33 survivors**). The second missed **its own words' INFLECTIONS** — `organises`,
`summarises`, `generalises`, `recognises`, `normalises`, the `-ises` forms of words already fixed bare —
found only by an arm run in the PUSHED clone. Only the fourth predicate closed it, and it closed because
it **derives** candidates instead of enumerating them: any `\w*is(e|es|ed|ing|er|ation)` whose `-iz` twin
is a real word, plus the non-`-ise` British set.

**THE RULE, IN ITS STRONG FORM: a spelling sweep's predicate must be MORPHOLOGICAL, never enumerated,
because a word list is the one instrument that cannot report what it omits.** §24.6c stated it about a
lead's vocabulary; this is the same rule about the sweeper's own.

**And two survivors were written by this session's own prose** — the Maker changelog spelled `centre` and
`travelled` inside the sentence asserting the Maker contained neither, v8.109's trap verbatim. Reworded.

**READING did the last mile, not the predicate.** 27 real sites separated from **15 false positives that
are US spelling too** — `compromise` ×7, `premise`, `advertised` ×2, `improvising`, `imprecise`,
`specialist` (§16.15). **DJ ruled `grey` STAYS**: four sites, all prose, read as a colour word rather than
a spelling. 23 shipped.


---

# S168 OPENS HERE — L13-03 AND L13-01, DESIGN RULED, COST MEASURED

**DJ ruled candidate D at S167 close, and the expensive half is already done: the design is settled and
the byte cost is compiled rather than estimated. S168 opens on BUILDING, not on re-deciding.**


## THE TRIPLE CHECK CHANGED THE ARC — READ THIS BEFORE BUILDING

**The defect is THREE MOVES WIDE AND FOUR LESSONS DEEP, not one move in one lesson.** Verifying a
proposed step title against the artefact killed a superlative and enlarged the finding (§16.16).

```
turnDegreesGyro(90.0 * sweepDir);   <- returns StopReason, DISCARDED
driveDistance(ROW_STEP_CM);          <- returns StopReason, DISCARDED
turnDegreesGyro(90.0 * sweepDir);   <- returns StopReason, DISCARDED
```

**THE KILL SWITCH IS DEAD FOR THE WHOLE CORNER** — press B during either turn or the sidestep and the
robot finishes the maneuver anyway. That is C3's subject, live, in the last in-scope lesson.

**TWO INDEPENDENT INSTRUMENTS AGREE (§24.13, a DIFFERENT METHOD).** A parser deriving the
returning-function set out of `RobotMotion.h` finds **9 calls using the return and 3 discarding it**, at
lines 495-497. The COMPILER, with every `StopReason` declaration marked `warn_unused_result`, names the
same three. **ARM 2 WAS BLIND ON ITS FIRST RUN AND REPORTED PASS** — `pio_harness.sh` compiles with `-w`
and `2>/dev/null`, so the instrument could not speak. Re-run directly with warnings on, it fires; a
SEEDED fourth discard takes it **3 -> 4** (rule 59: a control that cannot fail is not evidence).

**AND THE THIRD ARM IS WHAT CHANGED THE ARC:**

| lesson | StopReason fns | discarded |
|---|---|---|
| L10 / L11 / L12 | 5 / 5 / 6 | **0** |
| L13 / L14 / L15 / L16 | 7 | **3 each, same three lines** |

**The corner is not an L13 defect. L13 introduces it and L14, L15 and L16 INHERIT it unchanged**, so the
kill switch is dead through the corner in every build from L13 to the capstone. **One fix propagates by
inheritance** — but so does its byte cost.

**PRICED BEFORE IT IS RULED (rule 70), compiled not estimated:**

| build | before | after | delta | spare after |
|---|---|---|---|---|
| `13/finished` | 25,198 | 25,244 | **+46** | 3,428 |
| `16/finished` | 28,564 | **28,642** | **+78** | **30** |

**IT FITS AND NO TRADE IS OWED — BY THIRTY BYTES**, in the lesson whose entire subject is that thin
margins bite. Verify that figure again on a scratch-built harness before writing a word of L16, and if
it has moved, price the trade before touching the Maker.

## THE DEFECT, IN THE LESSON'S OWN WORDS

`case SWEEPING_ZONE` drives a row, decides wall-or-victim, then fires the sidestep with
`driveDistance(ROW_STEP_CM)` and turns again — **forever**. There is no completion condition, so the
robot eventually sidesteps into the far wall. L14 §8's 10x table already lists *Rescue zone exit — 10
trials* for a behaviour that does not exist. That is **L13-03**, GPT's #1 algorithmic hole in L13, and
it is ADJUDICATED AGREE.

**L13-01 is the same sentence one clause along:** Step 5's `if (reason == STOP_KILL)` is the only
branch on the return, so a leg that ran out `MAX_ROW_CM` because the prox MISSED the wall is recorded
as a wall. `driveUntil()` reports three reasons and the sweep reads one.

## THE RULING — CANDIDATE D, WATCH THE SIDESTEP

```
driveDistance(ROW_STEP_CM);        ->   if (driveUntil(ROW_STEP_CM) == STOP_PROX) {
                                          currentState = SWEEP_DONE;
                                          showStatus();
                                          break;
                                        }
```

**Four candidates were compiled against the live `13/finished` (25,198, 3,474 spare) and ALL FOUR FIT** —
A row count **+42** · B prox-after-the-turn **+42** · C covered area **+72** · **D watched sidestep +34**.
**Byte cost is therefore NOT the discriminator, and that is itself the finding**: this was a teaching
decision, not a budget one.

**D wins on three grounds, in order of weight.** (1) It fixes an inconsistency the lesson ALREADY has
vocabulary for — L13's whole thesis is that an interruptible move must report why it ended, and the
corner's three calls all discard theirs; the completion condition falls out of watching the middle one.
(2) The sensor is already aimed: after the first 90 degree turn the robot faces along the sidestep, front
prox square on the far wall. **B uses the same geometry but checks BEFORE moving**, so it can command a
full `ROW_STEP_CM` into a wall it is already touching; D detects and stops in one call. (3) Cheapest,
and adds no blank — A and C each need a number a student cannot derive without measuring the room, and
**A is open-loop on completion, the exact thinking L11 spends a lesson retiring.**

**KEEP A AS THE STRAWMAN THE LESSON ARGUES AGAINST.** A row counter is what a student reaches for first,
and the reveal is that it stops you short of the wall or marches you into it. Do not delete the idea —
teach against it.

## THE FOUR SEATING DECISIONS (§24.17 and §24.19, decided and reported)

1. **`Step 6b — The Blind Corner`, NOT a challenge and NOT a renumbered Step 7.** The title is the
   complement of Step 4's **The Watchful Leg** — Leg against Corner, Watchful against Blind — so a student
   who met the move that reports two steps ago reads the title and already knows what the step will do. L13 runs Step 1 *The Numbers,
   the Names, the Reasons* / 2 *The Doorman* / 3 *Wire the Door* / 4 *The Watchful Leg* / 5 *The Sweep
   (Walls Only)* / 6 *The Witness*. **A sweep that never ends is not optional polish** — it is a student
   whose robot marches into the wall in front of the class in week 9 of the Fall term. The `b` suffix is
   S157's precedent verbatim: it moves no step numbers, no catch-up doors, no `KINDS` rows and no bank
   citations, where a real Step 7 moves all of them.
2. **THE STUDENT DISCOVERS IT IN §7D. DO NOT HAND IT OVER.** §7D already runs the full sweep and already
   stages a false victim on purpose; it now also says watch what happens AFTER THE LAST ROW. The robot
   sidesteps into the wall in front of them. Then the question, which answers itself because they built
   the tool in Step 1: **"Every move in this program says why it ended. Why is the sidestep the only one
   you fire blind?"** A fill-in-the-blank throws that away.
3. **`SWEEP_DONE` IS A NEW STATE.** Reusing `STOPPED` saves an enum value and a display case and loses
   the one distinction that matters at 9pm in the lab: **the robot FINISHED** versus **the robot QUIT**.
   And a state machine gaining a state that names a distinction is on-thesis for the lesson whose subject
   is two outcomes that look identical until you ask the right instrument.
4. **L13-01 FOLDS INTO THE SAME CARD.** D as sketched branches on `STOP_PROX` only, so it kills the kill
   switch during the sidestep — the identical defect as L13-01. **One card, one contract, both fixes:**
   *the leg ended; which of the three reasons was it?* Teaching them apart teaches the same thing twice
   and lets a student fix one and keep the other.

## WHAT S168 OWES

- `after_step_6b` cut from the built state (**§11 EXTRACTION, never reconstructed**), `step_7`'s door
  repointed, and the new `KINDS` row labelled.
- The L13 byte chain **recompiled and every delta RE-DERIVED** — Step 6b's checkpoint becomes a banked
  number, so it must be right before the bank is touched (v8.130: an auto-graded gate that punishes the
  attentive is worse than no gate).
- ~19 L13 payloads; the 37 inheriting L14/L15/L16 payloads move with L13's `finished`. **`gate_payload_match`
  will be RED at every intermediate state by construction** — green at L13-unconverted and green again
  only at L16 (S157's rollout shape). That is the correct checkpoint, not a defect.
- The `QUIZ_L13` arc walked in the SAME session (READ -> FIX -> QUIZ). The bank already grades the guard
  conditions in `L13_A17` and the assumptions in `L13_A17b`; both are touched by this change.
- §8's troubleshooting table gains the row this creates, and L14 §8's *Rescue zone exit* line finally
  names a behaviour that exists.

**BEFORE ANY OF IT: the tag-strip measurement.** ~30 minutes, and it answers whether the gates that will
certify this work can see past their own predicates. **Measure, record, do NOT widen** — a predicate
widened against an unmeasured population is the mistake S167 made four times.

---

# S168 NEXT

- **THE TAG-STRIP BLIND REGION IS THE LARGEST OPEN INSTRUMENT ITEM.** Nine gates use
  `re.sub(r'<[^>]+>', ' ', s)`. The honest predicate strips COMMENTS as comments before stripping tags.
  Population unmeasured: nobody has asked what else is currently invisible inside an HTML comment
  anywhere in the tree. **That measurement is the first move, not the widening.**
- **`BookComponentStandard.md` CARRIES 44 BRITISH FORMS AND IS DELIBERATELY UNSWEPT.**
  `gen_component.py` pins the literal section anchor `'### 5.2 Colour is never'`, so sweeping it edits
  a generator's boundary string — rule 56. If it is ever swept, both move in the same commit.
  `ROBOCUP_RESCUE_LINE_2026.md` is held as the rulebook extract that must match its source (3 hits).
- **L13-05 IS APPLIED AND ITS BANK ARC IS CLOSED** — §5 now names the three assumptions and
  `QUIZ_L13` gains `A17b`. **L13-11 is VERIFIED**: the `readCalibrated()` quote is byte-faithful to
  the QTR bundled in `Zumo32U4@2.0.1` (pinned SHA `f4dfe05`, `git tag --points-at HEAD` → **2.0.1**).
  The defect was the sentence, and *four lines* is now deleted rather than replaced.
- **THE REMAINING GPT WORKLIST** — 245 findings, most unadjudicated. L13-01 (a missed prox stop
  recorded as a wall) and L13-03 (the sweep has no completion condition) are the strongest left, and
  both are ADJUDICATED AGREE with real algorithmic consequences.
- **`ZUMO_AFTER_LAUNCH.md`** — read at every session open alongside this handoff. Three items, all
  still open; its footer names the CURRENT handoff and must be re-aimed at every close.
- **`site_parity` IS NOT TRUSTWORTHY ON ITS FIRST RUN AFTER A PUSH** (S166, unchanged). Run it at
  least twice and believe the repeat.
- **GATE 77 DOES NOT EXCLUDE `<pre>`** (S165, unchanged). When it first fires, the answer is a ruling.
- **ARM 2 IS STILL BLIND TO A FIGURE STATED IN PROSE** (S166, unchanged). **L16 still never states its
  match-mode figure at all** — 28,504 lives in the Maker, the Bible and LIVE.md and appears nowhere in
  `Lesson_16.html`.
- **THE MAKER CHANGELOG STILL RECORDS NOTHING BETWEEN v2.49 AND v2.58** — deliberately un-back-filled.
- **`26,736` IS CORRECT BY MEASUREMENT AND GATED BY NOTHING** (S166, unchanged) — ARM 6 reaches only
  *Lesson N finished* labels. **Do not widen it until a real miss forces it.**
- `bonus_b5`'s deliberate sabotage survived S167 untouched. **Keep it that way.**
- L12 BONUS B4's bench measurement · L15 Challenge 3's `turnDegreesGyroSafe()` · L03 queued content ·
  `ZUMO_L03_TEMPLATES.md` staging · Bible §14 TDP-canon entry · day-by-day grid + syllabus.
- **The poster is a GRADED deliverable** (DJ, S159). **Photography is OFF the critical path** (DJ, S156).
- **Fall launch Sept 8 — three weeks out.**

---

# TWO INSTRUMENT FIXES S167 EARNED — BUILD THEM IN S168

**Both would have prevented what S167 spent a day finding, and neither is speculative: each has a
named defect behind it that this repo actually shipped.**

## 1. `pio_harness.sh` COMPILES WITH `-w` AND `2>/dev/null`, SO THE COMPILER CANNOT SPEAK

Line 21 reads `CCF="$DEF -Os -w …"` and line 31 pipes `2>/dev/null`. **The one instrument in this repo
that could have caught the blind corner was gagged.**

**MEASURED, NOT ARGUED (S167):** marking every `StopReason` declaration `warn_unused_result` and
compiling through the harness printed **PASS and nothing else**. Compiled directly with `-Wall` and
stderr open, the same source names all three discarded returns at lines 495-497, and a SEEDED fourth
takes it **3 -> 4**. The harness was the difference between silence and three warnings.

**AND IT HAD BEEN SILENT FOR FOUR LESSONS.** The corner has been in L13, L14, L15 and L16 since the
S158 rollout gave those primitives a return; nothing surfaced it because nothing was listening.

**THE FIX IS ONE FLAG AND THE SCOPE QUESTION IS THE REAL WORK.** `-Wunused-result` needs the
declarations marked `warn_unused_result` to fire, which is a `RobotMotion.h` edit reaching **every
payload from L10 onward** — so this is NOT a one-line change to a shell script, it is a header change
priced across the Maker. **Measure the population before writing anything** (rule 34): how many call
sites across all payloads discard a `StopReason`, and are they all defects or are some deliberate?
**S167 measured L10-L16 finished builds only** — L10/L11/L12 discard zero, L13-L16 discard three each.
The other ~180 payloads are UNMEASURED and that is a stated gap, not a claim.

**Second question, cheaper and separable:** should the harness stop swallowing stderr regardless? A
build tool that hides warnings is an instrument that cannot report, and **`-w` also hid whatever else
the compiler has been trying to say for 160 sessions.** Turning stderr on and READING one clean build
is the first move — it costs nothing and it may return more than this one finding.

## 2. NOTHING IN THIS REPO CHECKS A NUMBER STATED IN PROSE

S162 recorded that nothing here reads prose; **S167 put five compiled figures into LIVE.md, the Bible
and this handoff, and not one of them is asserted by anything.** The claim-audit arm written at S167
close re-derived all eleven and passed — **and it was thrown away when the session ended.**

**THE PREDICATE IS ALREADY KNOWN AND IT IS NARROW ON PURPOSE (rule 20, rule 78):** a byte-shaped figure
that a session document states ALONGSIDE A NAMED BUILD must equal that build's compile. `byte_audit`
ARM 6 already does exactly this for QUIZ BANKS and its scope limit is written down; **this is ARM 6
pointed at `LIVE_ZUMO_TEXTBOOK.md` and the handoff instead of at a bank.** Do not widen it to every
number in every document — a figure with no named build beside it is not a claim this can check, and
**an instrument built on what you can reach rather than on what the property requires is the wrong
instrument** (S165).

**CONTROLS IT OWES, one per invocation:** a stale figure beside its own build label is LOUD · rewording
a sentence that carries no figure is SILENT (blinding) · zero figures scanned FAILS on coverage
(rule 27) · and a HISTORICAL per-session block is correctly OUT of scope, because **S165's version of
this arm first reported fifteen failures that were all correct as history** — the arm was unscoped, not
the document.

**THE HONEST CAVEAT:** neither of these would have caught most of what S167 actually found. **Four of
five findings this session were wrong SENTENCES, not wrong numbers** — a spelling predicate that could
not report its own omissions, a claim asserted in three files and corrected in one, a section seated in
the wrong place. **Nothing gates a sentence, and these two instruments do not change that.** They close
two named holes; they do not close the class.

---

# HARNESS — IT IS NOT IN THE REPO. RUN THE SCRIPT.

```
sh harness_setup.sh
```
**Invoke it through `sh`, not `./`** — the file is tracked 100644 and the executable bit does not
survive GitHub Desktop. **Correct setup prints `objects: 41`.** Then, in order:

```
python3 byte_audit.py --sizes     # compiles every payload the Maker defines (~3 min)
python3 byte_audit.py --check     # six arms
python3 byte_audit.py --selftest  # NINE controls - run this before trusting --check
```

**CONTROLS — ALL EIGHT RE-VERIFIED AT S167 ON A HARNESS BUILT FROM SCRATCH, AND UNMOVED BY THE SWEEP:**
L11 `after_step_1` **20,592** · `11/finished` **20,778** · `12/finished` **24,790** ·
`12/c2_slipalarm` **21,334** · `13/finished` **25,198** · `14/finished` **25,942** ·
`15/finished` **28,340** · `16/finished` **28,564**. **Reproduce the first one before trusting the
rest** (rule 30). The three declared overflows are `16/after_step_3` 28,950 · `16/after_step_4` 29,586 ·
`16/step_5_serial_traded` 28,882 — deliberate, and the lesson's own premise.

**A ZERO-BYTE CLAIM IS NOW A MEASURED CLAIM, NOT AN ARGUMENT.** S167's rename touched 89 payloads and
moved **0 of 430** figures. The method: snapshot `/tmp/zumo_byte_sizes.json`, re-run `--sizes`, diff.
Do that for any edit claimed to be comment-only or name-only.

---

# STANDING AUTHORITY — §24.17

**Decide and report; do not ask.** Three carve-outs: facts about the ROOM no instrument can see; moves
that are irreversible or expensive to undo (the test is recoverability); and RoboLore brand and course
scope. **Delegation removes the question, never the disclosure.** Full text: Bible §24.17.

**S167's worked example is the spelling ruling and its two halves.** The sweep itself was execution
once DJ ruled. What was NOT decided unilaterally: `BookComponentStandard.md`, because sweeping it
edits a generator's pinned anchor; and widening the nine tag-strip gates, because the population is
unmeasured. **Both were measured and handed over; neither ruling was taken.**

---

<!-- VERSION BLOCK: emitted by session_versions.py --handoff. Never hand-typed. -->
Fresh-clone verified at **`543ca21`**. Census **40,890**.
Bible **v8.160.7** · `BookComponentStandard` **v01.13.0** · Maker **v2.58.7** ·
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

Lessons: L01 v03.30.1 · L02 v03.21.5 · L03 v03.43.2 · L04 v04.29.2 · L05 v04.29.1 · L06 v04.32.4 · L07 v04.31.5 · L08 v04.32.1 · L09 v05.27.4 · L10 v02.30.3 · L11 v02.31.1 · L12 v01.33.1 · L13 v02.32.0 · L14 v02.35.1 · L15 v02.31.7 · L16 v02.26.4.
