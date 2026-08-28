# ZUMO — S193 HANDOFF (written at S192 close · paste at top of Session 193)

## READ THIS FIRST

**NOTHING FROM S192 IS PUSHED.** 26 paths differ from HEAD (`db04d7f`) — 24 modified, one deletion,
one new file. 0 unbumped.
`git rm ZUMO_S192_HANDOFF.md` is part of this push and **`ZUMO_S193_HANDOFF.md` IS A NEW FILE** —
both are checkboxes in GitHub Desktop, which is where the deletion and the new file get missed.
**`newproject.html` was NOT touched this session** — no Maker upload, no rename-on-disk dance.
If `__pycache__/` exists, delete it LAST; it regenerates on every gate run.

**`site_parity` IS DISCHARGED AND OWES NOTHING FOR S192's OWN WORK, BUT IT IS OWED AFTER THE PUSH.**
S191's push (`db04d7f`, 19:06 EDT) was verified at S192 open: **PARITY twice, 23:49 and 23:52 UTC**,
43 and 46 minutes past the 10m57s build floor. **No lesson, image, or CSS byte changed in S192**, so
the asset arm cannot move — run it anyway, twice past the floor, and believe the repeat.

**`byte_audit` OWES NOTHING.** **Zero payloads moved this session and zero bytes.** The harness was
never stood up, and `--check` correctly refused rather than guessing: *no harness at
/home/claude/harness*. Standing control is **20,592**, not 20,516.

**81/81 gates** — gate 81 is NEW · `gate_payload_match` **PASS**, advisory unmoved at **635** ·
`retired_claims` **CLEAN, 17 registered** · `prose_canon` **0 new / 7 pinned / 0 orphan** ·
`quiz_bank --check` **16 banks valid** · `callout_id` **1134** · `strip_inline --verify` **0 dead** ·
`build_worklist --check` current (regenerated on the Bible bump) · `census --selftest` **19 controls,
was 14**.

---

# 1. WHAT S192 DID

**ONE THING: DJ RULED *"build it"* AND THE CENSUS-BACKED ASSERTION GATE WAS BUILT.** Priced at S190
at 250 lines, unruled for two sessions. It is now `census.worklist()` + **GATE 81**, and **four of
its eleven controls found defects in the gate itself before it landed.**

## `census.worklist()` — THE TALLY FINALLY HAS AN OWNER
Seven Populations: `total`, `closed`, `fixed`, `parked`, `open`, `headings`, `out_of_scope`. It
reproduces every published figure exactly — **245 / 95 / 2 / 148 / 89** — and the six ❌ rows it
finds are the exact six S191 reconciled by hand. `out_of_scope` isolates **`L03-B1`** (seated in
Part 0, never in Part 2) instead of dropping it silently.
**TWO INDEPENDENT READERS OF THE TOTAL** (rules 83/84): Part 2's ID rows, and the sixteen section
headings expanded to the rows they declare, so `agree()` compares like with like.
**IT RAISES RATHER THAN SHRINKING.** A missing PART boundary, an ID seated twice, or a closed/parked
overlap all raise. That is v1.1.0's lesson applied: an unknown reported as a number is the class.

## THE BLINDING CONTROLS ARE WHAT MAKE L1 EVIDENCE
| sabotage | L1 | L2 | L3 | L4 | L5 |
|---|---|---|---|---|---|
| `worklist()` returns five typed constants | **PASS** | FAIL | FAIL | FAIL | — |
| `fixed` collapsed into `closed` | PASS | PASS | PASS | PASS | **FAIL** |

**Row one is the point: L1 passes against a fabricated constant**, so L1 alone was never evidence.
Row two prints `(closed 95, fixed 95)` — **the nine-session defect, reproduced and caught.**

## GATE 81 — ELEVEN CONTROLS, ALL FIRING
A1/A2/A3 plant a wrong figure in each home INDEPENDENTLY; each fires and names the right home and
population. **B1** a home drops the tally → *states no tally at all*. **B2** a new lone-pair
assertion → unpinned site. **B3 the S191 defect replayed**: flip one closed row to ❌, truth moves
89→88, and the gate names **all three homes** still saying 89. **C1/C2** FORM C and FORM B.
**D1** a dead pin → orphan arm. **D2** `census.worklist()` raises → *no truth to assert against*.

## FOUR DEFECTS THE CONTROLS FOUND IN THE GATE, AND ONE IN THE HARNESS
1. **The under-reach detector was built as `re.compile(_PAIR81)` — the pricer's own predicate.** A
   planted lone assertion sailed through a green gate. **A detector with the pricer's blind spot is
   the pricer agreeing with itself.** Widened to three connecting words.
2. **The session guard was defeated by BACKTRACKING.** `(?<![A-Za-z])` on `S190` matched `90`,
   because `9` is preceded by a DIGIT. A guard that can be stepped around is not a guard.
3. **Four of six pins were ORPHANS** — killed by guards added later in the same session. Added an
   orphan arm: a pin over a site nothing produces reads as coverage it does not have.
4. **FORM C priced the DENOMINATOR** of `148 of 245 rows are OPEN` and failed the gate on correct
   prose. FORM B and FORM C are NESTED, not alternatives; the wider one wins where they overlap.
5. **THE CONTROL HARNESS ITSELF.** `D2` passed when it should have failed. `sys.path[0]` is the
   probe's own directory — which was also the restore-snapshot directory — so a backup `census.py`
   **shadowed the repo's** and the sabotage control imported a clean copy. **A control that stays
   quiet for the wrong reason is not a control (rule 59), and this time it was the harness.**

## THE PREDICATE IS THE RUN, AND THAT WAS MEASURED, NOT ASSUMED
A digit-near-a-status-word form was built first and priced against all three homes. It manufactured
**`TOTAL = 110`** out of gate 78's own discard sentence, **`TOTAL = 18`** out of *intake of 18 GPT
feedback documents*, **`FIXED = 68,123`** out of the intake word count, and **`CLOSED = 0`** out of
the heading `# PART 0 — CLOSED ROWS`. All four are correct prose. **A lone pair is ambiguous by
nature; the tally is always a RUN.**

## BIBLE §24.24a SEATED
*A derived count has homes too, and unlike a version nobody notices when they drift.* Both homes
filed (version line + standalone changelog entry); `current_session()` returns **192**.
`GPT_WORKLIST.md` regenerated on the bump (S175 coupling).

---

# 2. S193 OPENS HERE

## `L08-08` AND `L08-15` ARE STILL OPEN AND UNTOUCHED
**These are the last two in-scope rows before L09.** L01–L07 are done.
**`L08-08` IS PRICED: exactly ONE lesson site**, `Lesson_08.html:1325`, the *Why TRIM here — and NOT
in `followLine()`* box. **It is spelled `CLOSED loop` — uppercase, UNHYPHENATED.** `closed-loop`,
`closed loop` and `Closed-Loop` each return **0** against that file. **A sweep on the hyphenated
spelling would have reported the row already dead.** Sweep the ARITHMETIC — TRIM inside a feedback
loop — across all 16 lessons, the Maker and the banks, never the identifier's spelling (§24.6c).
**`L08-15` is unpriced.** **`L08-08` is priced above and is a FIVE-ROW, five-lesson pass.**

## THE C1 RESIDUE PASS SHIPPED — FIVE ROWS, FIVE LESSONS, ELEVEN BANKS
**`L08-08` IS NOT AN L08 ROW.** Sweeping the PHENOMENON — TRIM opposing a feedback loop, or a loop
already doing TRIM's job — returns **12 real prose sites across FIVE lessons**, plus 4 bank
questions. **ALL TWELVE SITES AND FIVE BANK QUESTIONS ARE FIXED. Zero Maker payloads, zero bytes** (all 179 `newproject.html`
hits are the benign `// NO TRIM here - the wheels are fighting on purpose` turn comment).

| lesson | sites | where |
|---|---|---|
| L06 | 1 | § prose |
| L08 | 2 | Step box + a second site |
| **L10** | **4** | prose ×2, **glossary entry**, **Quick Reference table row** (`followLine() ❌ never · TRIM would fight it`) |
| L11 | 2 | §8A.1 + §7C |
| L12 | 3 | prose ×2 + **KEY TERM glossary entry** |

**L01 IS CLEAN** — *"Lesson 3 gives you TRIM, whose entire job is fixing it"* describes TRIM's job,
not the controller's. Three L10 hits were the lesson TITLE, *When the Course Fights Back*.
**A hit is not a defect; reading is what said so (rule 34 / §16.15).**

**THE SWEEP WIDENED THREE TIMES IN ONE SESSION: 6 → 7 → 13 → 12 adjudicated.** `fight...controller`
found 6. `fight` alone found L12's KEY TERM (§16.56 — *the glossary is where it survives*). The
phenomenon predicate found all of L10. **Each widening closed the CASE it was aimed at, not the
PROPERTY** — gate 78's S175/S178 finding, third recurrence, this time in my own hands.

**FIVE ROWS, NOT ONE — FOUR OF THEM ALREADY OPEN AND UNREAD:**
`L08-08` · **`L10-12`** · **`L11-08`** · **`L12-18`** · **`L15-08`**. Closing `L08-08` alone leaves four
rows describing work already done — the `L06-02` shape, open 28 sessions after its fix.
**Do NOT open a new row; the total stays 245.** Closing all five moves the tally to
all three homes are updated and gate 81 agrees. **The projected figures are written in WORDS on purpose: gate 81 asserts DIGITS
beside a status word, so writing a future tally as digits fails the gate on a claim that is not yet
true. It caught exactly that in this paragraph.**

**THE CLAIM IS BACKWARDS, NOT MERELY LOOSE, AND IT WAS TRIPLE-CHECKED.**
ARM 1 (the book's own `driveDistanceAccel` carrying TRIM inside a `while` loop) **FAILED to refute** —
that loop is closed on DISTANCE, which §16.31 already distinguishes. Discarded, not hidden.
ARM 2 — **L15 §3.4**: *"P settles at the point where its correction exactly cancels the bias, and that
point has a non-zero error... P structurally cannot remove it."* Same disturbance, same controller.
ARM 3 — **`Lesson_15.html:1449`**, found by a control built to BREAK arm 2: the troubleshooting table
prescribes, for a permanent line-loop offset, *"On the line loop: **check TRIM** and your calibration
first."* The book already prescribes TRIM for the loop the other five lessons forbid it in.
ARM 4 — simulation of the shipped arithmetic: mismatch 12 / TRIM 0 → **error 75**; TRIM +12 → **0**.
Blinding: no mismatch + TRIM → **−75** (the sim CAN call TRIM harmful); wrong-sign TRIM → **150**.
Signature: `error × Kp` constant at **6.000** across a 4× Kp sweep — steady-state error, not an artifact.

**`L15-08` ALREADY SAID THIS AT S154 AND NOBODY READ IT:** *"I is the only term that can remove
steady-state error — true within the P/I/D feedback terms, but the robot already has feed-forward."*
**Four arms re-derived a finding sitting in the worklist the whole time. Read the row before measuring.**
So **L15 is NOT already correct** — an earlier claim in this session that it was is withdrawn.

**RULED THIS SESSION (DJ):** L06/L10/L11 get the SHORT reason, no mechanism. **L08 gets the short
reason plus a forward question to L15 §3.4** (pose it, do not answer it — L08 already says *today stops
here*). L12 keeps its correct reason (*the gyro is watching*) and loses the false half.
**L15 §3.4 gets the back-pointer to L08 — DJ approved — and it must carry `L15-08`'s CORRECTION, not
just a cross-reference.** `L11_B44`'s stem IS the false claim with `correct: True` and needs
restructuring, not rewording (the `L08_B25` shape from S191).

**REGISTER IN `retired_claims` AFTER, NOT BEFORE.** I ruled register-first and the file refuted it in
its own header: *"EVERY ENTRY WAS MEASURED AT ZERO BEFORE IT WAS ADDED. An entry that is already
firing is not a gate, it is a backlog."* Fix to zero, then register **several spellings** (as `L07-04`
does) so the registry does not inherit one predicate's blind spot.

**THREE MORE UNDER-REACHES DURING THE PASS ITSELF, AND INSTRUMENTS CAUGHT ALL THREE.**
1. **`L10_B21`** — a FIFTH bank question, found only by an assertive-register sweep AFTER the first four
   were fixed. A bank sweep run before the edits would have missed it.
2. **`ZUMO_QUIZ_L13.yaml` pins lesson_10/11/12 UNQUOTED** (`lesson_10: v02.30.6`, no quotes). My exact
   -string predicate matched only the quoted form. **Gate 75 caught it.** Fixed the PREDICATE, not the
   three instances.
3. **A status glyph quoted as prose corrupts the tally.** The `L10-12` closure row quoted L10's Quick
   Reference cell verbatim, and the ❌ inside it is the structural marker `census.worklist()` reads as
   REFUTED — `fixed` silently went to 93 instead of 94. **Caught in one run because the tally is derived
   now.** Do not quote a status glyph inside a row.

**A FOURTH UNDER-REACH, FOUND ONLY BY READING THE RENDERED RESULT (S192 triple check).** The prose
residue sweep returned ZERO and two L11 sentences were still broken: I had replaced the second half of
each and left the first half saying the same thing twice — *"deliberately does not — because we leave it
out deliberately"*. **A predicate reaching zero proves the old string is gone, never that what replaced
it reads.** The arm that caught it was reading all fourteen replacements in RENDERED form, and its
control is that the other twelve came back clean. **Add a read-the-replacement arm to any claim sweep.**

**RETIREMENTS REGISTERED AFTER reaching zero, FOUR SPELLINGS not one** (`L08-08`, `L10-12`, `L11-08`,
`L12-18`, S192) — 21 registered, was 17. **Blinding-controlled: each spelling planted into L08 in turn,
and each fires naming its OWN row.** Four spellings because the predicate widened three times in one
session and a single pattern would inherit whichever blind spot the last widening left.

## THE TALLY IS NOW GATED, SO A WORKLIST EDIT IS A THREE-HOME EDIT
The worklist stands at **100 closed / 94 fixed / 2 parked / 143 open of 245**. **S192 closed five rows**
— `L08-08`, `L10-12`, `L11-08`, `L12-18`, `L15-08` — in one C1 residue pass. **GATE 81 CAUGHT THIS FILE ON ITS FIRST REAL USE:** the handoff was
drafted with no tally in it at all, and the gate refused it. That is §24.24a firing in the
session that wrote §24.24a.
Close a row and `census` moves; **gate 81 then fails on LIVE.md and this handoff until both are
updated.** That is the gate working, not a nuisance. **Absence also fails** — do not "simplify" the
tally out of a home.

## STILL OWED, UNCHANGED
- **The 7 pinned `prose_canon` residue sites** — three L05/L06 lesson headings and four Maker labels,
  **ONE fix, not two**. Untouched a sixth session.
- **`prose_canon` arms 1, 2 and 4** — unbuilt. No arm without a control per direction.
- **Seat the §16 debt.** Still 26 rules, untouched a seventh session.
- **`L07_GRAPHIC_7-15`'s one real overflow** — `RobotSensors.h`, 14.5 units.
- **`ZUMO_BENCH_TESTS.md` ranks itself.** Run **1 `L10-B1` · 2 `L02-B2` · 7 `L10-B2`** in one sitting.
- **Syllabus dates still `[TBD]`; the day-by-day period grid is unbuilt.** **Launch is September 8.**
- **`ZUMO_GPT_REVIEW_WORKLIST.md` footer carries a second version token** (`Worklist v1.2`) that
  disagrees with the header home `session_versions` reads (v1.12). Flagged three sessions, not ruled.

## THE NEXT INSTRUMENT ARGUMENT, IF THERE IS ONE
Gate 81 covers the worklist tally **and nothing else** (rule 78, in its docstring). Callout, bank,
mark, icon and payload figures written in ordinary prose are still unwatched — `session_versions`
owns the emitted version block and gate 78 owns the discard figure, and between them is open ground.
**Priority is DJ's, and the launch is 12 days out.**

## STANDING, UNCHANGED
- **`gate_payload_match` IS NOT ONE OF THE GATES** (S137) and **TAKES ARGUMENTS** — pass
  `newproject.html lessons/Lesson_*.html`, or it reports a COVERAGE failure on a subset.
- **`--live` and `--handoff` PRINT, they do not WRITE** (§24.20). **LIVE.md carries TWO `**Versions:**`
  lines** — line 6 is current. **Keep the Status line to ONE line.**
- **The visible §5b banner is spelled `Version 04.31` — BARE.** A `v`-prefixed grep cannot see it.
- **`quiz_bank.py` LIVES IN `quizzes/`, NOT THE REPO ROOT.**
- **A BIBLE SESSION BUMP IS A REGENERATION OBLIGATION** (S175) — fired, `GPT_WORKLIST.md` regenerated.
- **A BIBLE BUMP HAS TWO HOMES** (S185): the version line AND the standalone changelog entry
  `current_session()` reads. **The version line also appears MID-LINE at line 17**, so a naive
  unique-anchor replace asserts and stops — anchor on the LINE-START form.

# HARNESS — NOT IN THE REPO. RUN THE SCRIPT.

```
apt-get install -y gcc-avr avr-libc
sh harness_setup.sh                     # objects: 41  AND  core stderr: clean
python3 byte_audit.py --sizes           # ~4 min at 221 payloads
python3 byte_audit.py --selftest ; --check ; --discards
```
**`--selftest` CANNOT RUN BEFORE `--sizes`** — CONTROL K dies with a `KeyError`.
**Run `harness_setup.sh` in the FOREGROUND and read `objects: 41` before trusting anything
downstream** — backgrounded, it has died silently at `== core build ==` with 0 objects.

# STANDING AUTHORITY — §24.17, §24.19, §24.21
**Decide and report; do not ask.** Carve-outs: facts about the ROOM · irreversible moves ·
RoboLore brand and course scope. **§24.19 is the tiebreaker** — what is best for student learning.

---
<!-- VERSION BLOCK: emitted by session_versions.py --handoff. Never hand-typed. -->
Fresh-clone verified at **`db04d7f`**. Census **41,811**.
Bible **v8.188** · `BookComponentStandard` **v01.13.0** · Maker **v2.70** ·
`marks/` **41** · `icons/` **49** incl. LICENSE.
`ZUMO_Syllabus_WORKING.md` **v1.3**.

Instruments: `book_gates` **v1.75.0** · `lesson_inventory` **v1.3.5** ·
`gen_component` **v1.6.1** · `pill_sweep` **v1.1** · `gate_payload_match` **v1.9.5** ·
`build_family_map` **v1.6.6.5** · `callout_id` **v1.0** · `keyterm_prefix` **v1.0.1** · `build_mark_index` **v1.1.0** · `gen_bonus_banner` **v1.4.1** ·
`gen_part_banners` **v1.2** · `session_versions` **v1.32.2** · `fit_raster_svg` **v1.2** ·
`flatten_alpha` **v1.2** · `svg_layout_audit` **v1.21.2** · `site_parity` **v1.2.1** ·
`build_css` **v1.4.0** ·
`image_audit` **v1.3** ·
`strip_inline` **v1.2** ·
`build_worklist` **v1.2** ·
`prose_canon` **v1.1.0** ·
`retired_claims` **v1.1.0** ·
`census` **v1.2.0** ·
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

Lessons: L01 v03.32.1 · L02 v03.26.1 · L03 v03.47.0 · L04 v04.29.6 · L05 v04.30.0 · L06 v04.37.2 · L07 v04.33.1 · L08 v04.34.3 · L09 v05.27.6 · L10 v02.30.7 · L11 v02.31.4 · L12 v01.35.4 · L13 v02.39.0 · L14 v02.36.2 · L15 v02.32.1 · L16 v02.28.1.
