# ZUMO — S171 HANDOFF (written at S170 close · paste at top of Session 171)

## READ THIS FIRST

**S170's work IS PUSHABLE and DJ verifies the push himself (standing ruling, S158).**
`git rm ZUMO_S170_HANDOFF.md` is part of that push. **If `__pycache__/` or `quizzes/__pycache__/`
exist in your tree, delete them LAST, immediately before pushing** — they REGENERATE on every gate run.

**77/77 gates** · `gate_payload_match` **PASS** · **`byte_audit --check` PASS across EIGHT arms
(ARM 8 is new), `--selftest` ALL CONTROLS PASS** on a harness built from scratch by the script
(`objects: 41`, standing control **20,592** reproduced first) · `quiz_bank --selftest` all controls ·
`session_versions --selftest` EIGHT CONTROLS · `callout_id` **1127/0** · `keyterm_prefix` 0 to
convert · 16 banks valid, **1,245** questions · census **40,980** · `site_parity` PARITY ·
`build_css --check` current at 574 rules · `image_audit --check` current · `next_pointer` clean.

**5 changed, 1 new, 1 deleted** — 448 tracked files, verified by whole-tree md5 against a fresh
clone. Changed: `pio_harness.sh` · `byte_audit.py` · `ZUMO_SUPER_BIBLE.md` ·
`LIVE_ZUMO_TEXTBOOK.md` · `ZUMO_AFTER_LAUNCH.md`. New: **`ZUMO_S171_HANDOFF.md`**.
Deleted: **`ZUMO_S170_HANDOFF.md`**.

**THE FIRST DRAFT OF THAT LINE SAID *2 changed, 0 new, 0 deleted* ABOVE A LIST CONTAINING A NEW FILE
AND A DELETED ONE, AND OMITTED `ZUMO_AFTER_LAUNCH.md` ENTIRELY** — a file DJ would then not have
pushed. Caught by the double check's whole-tree arm, not by any gate. **S163's defect verbatim**
(*the handoff's file count said six above a list of seven*), which this Bible records at v8.155.1:
the count was carried in the head while the list was typed, and **the number that is typed is the
number that is wrong** (rule 50). The count is now the arm's own output.

**NO LESSON, NO BANK AND NO GATE CHANGED. Census unchanged at 40,980.**

**RUN THE HARNESS FIRST — AND THE TOOLCHAIN IS NOT ON THE BOX.** A fresh container has no
`avr-gcc` at all. `harness_setup.sh` **v1.1** checks and tells you; the install is
`apt-get install -y gcc-avr avr-libc`, then `sh harness_setup.sh` (**`objects: 41`**).
Run apt in the FOREGROUND — backgrounding it silently died twice this session.

---

# ONE THING RULED, ONE THING WAITING ON DJ

## 1. THE HARNESS COMPILED WITH `-w` WHILE ITS OWN HEADER CLAIMED `-Wall`, FOR 170 SESSIONS.

S167 named the debt and handed it forward twice. `pio_harness.sh` is **v3.1** and the compiler can
speak. **Three things were measured before the flag moved (rule 34), and the first one killed the
obvious instrument:**

- **THE `.elf` IS NOT REPRODUCIBLE BUILD-TO-BUILD.** Three identical `-w` builds of the standing
  control gave three different md5s — LTO embeds build state. An elf comparison would have reported
  a difference that was pure noise. **`avr-objcopy -O binary` — the flash image itself — IS stable,
  and IS identical under both flags.** A hash of the wrong artefact is not a weaker control; it
  reports the opposite of the truth.
- **THE VENDOR CORE IS SILENT.** ArduinoCore-avr plus all eight Pololu libraries compile under
  `-Wall` with **ZERO** warnings. `-w` was never shielding anyone from third-party noise — the
  reason everybody assumes such a flag exists, measured and false here.
- **POPULATION: 113 warning lines over 70 of 216 payloads, TWO classes, FOURTEEN sites.**
  109 are the build-up model working as designed; one points at `11/b1_onewheel`'s deliberate
  `// <-- PLANTED` bug, **so a student's real PlatformIO has been handing them that hint all along.**

Also fixed: `--setup` no longer sends both core loops to `/dev/null` (a library that failed to
compile was as silent as one that succeeded; the only guard was a human reading `objects: 41`), and
the payload error file moved off the fixed global path `/tmp/pio_err.txt` — **`byte_audit` makes a
fresh `mkdtemp` per payload precisely so no two builds can see each other's state, and that one line
handed it back.** `warn=` is APPENDED to the PASS/OVER line, never inserted: `byte_audit` reads it
with `startswith("PASS")` and a `flash=(\d+)` search, and both survive a trailing field where
neither survives a reordering. **Keep it last.**

## 2. `SWEEP_DONE` — FOUR WARNINGS THE BUILD-UP MODEL CANNOT EXPLAIN. **DJ HAS NOT RULED.**

`SWEEP_DONE` is the one `RobotState` member with **no case in the `loop()` dispatch switch**, in the
terminal build of **L13, L14, L15 AND L16**. Half-wired: a `showStatus()` line so the screen can say
SWEPT, and nothing dispatching on it.

**L13 argues for the state explicitly and well** — *at nine o'clock at night in the lab, a motionless
robot is the most ambiguous object* — so this is **not a wrong decision. It is a decision that
acquired a second consequence two lessons downstream:**

- **BUTTON B IS DEAD THERE.** `case STOPPED` is what reads B to restart. L13 spends a paragraph
  fixing *that is why B does nothing* through the corner, then routes the success ending into a
  state where B does nothing permanently.
- **THE SUCCESSFUL ENDING IS THE ONE THAT SCORES NOTHING.** From L15 every other ending routes
  through `endRun()` → `RUN_REPORT`, where L16 keeps `saveBaseline()` and the baseline-versus-enhanced
  comparison. **The run that sweeps every row to the far wall — the BEST outcome — yields no
  scorecard.** L15 names the state only in its enum; **L16 never names it at all.**

**Not fixed, deliberately:** a change moves byte figures across four lessons and every downstream
figure — course content plus §24.17's recoverability carve-out. **ARM 8's baseline holds the current
behaviour, so movement is loud in EITHER direction:** fix it and the arm reports the surplus; let it
drift further and the arm reports the addition.

---

# `byte_audit` ARM 8 — WHAT IT DOES AND WHAT IT DOES NOT

**It asserts ONLY the `finished` payloads** — the terminal, student-facing program of each lesson,
where nothing is coming later to use the thing being warned about. Intermediate steps are counted
and REPORTED and asserted by nothing. **An arm that cried at correct work would get switched off.**

**FOUR STATED BLIND SPOTS (rule 78), one demonstrated in `--selftest`:**
1. A genuinely wrong warning in an intermediate step is printed and asserted by nothing. **The
   build-up model is an explanation, not a proof, and this arm takes it on trust.**
2. It reads only what the compiler chose to say.
3. It cannot tell a signature that MOVED from one fixed and a new one raised — line numbers are
   dropped on purpose.
4. **IT COUNTS SIGNATURES, NOT LINES, AND THE TWO NUMBERS DISAGREE.** Raw population is **113
   lines**; ARM 8 reports **99 signatures**, over the same **70 payloads**. The gap is 14 lines in 6
   payloads where the same enum value is unhandled in TWO switches in one file — the `showStatus()`
   display switch and the `loop()` dispatch switch. **Both numbers are right; quote the payload
   count, 70, because it agrees across both.**

**CONTROL K ships in `--selftest`, EIGHT assertions, synthetic** — ARM 8 takes a table and touches no
file, which is worth keeping: *a control that has to compile is a control somebody eventually skips.*
Both ANCHORS are ASSERTIONS, not conditions (S169's lesson). A NEW warning is LOUD; **a baseline
warning that VANISHED is LOUD too, because a stale baseline is a defect the same way a stale figure
is**; the same plant in an intermediate step is SILENT; an EMPTY table does not pass; and a table
with NO warning data anywhere does not pass — the shape an older harness produces, and the exact
condition under which *no warnings* is a lie.

---

# `grep_trap` CAUGHT MY OWN EDIT, INSIDE THE SESSION THAT WROTE ARM 8

`session_versions --selftest` went **RED on the clean tree**. My new ARM 8 docstring named
*pio_harness v3.1* **above `byte_audit.py`'s own `VERSION` home**, so a plain grep of that file
returned v3.1 where the file is v1.6. **The tooling was never wrong — a person at a terminal would
have been**, which is the entire reason that control exists. The token is gone and the reason is
recorded in its place so nobody restores it.

**A LATENT TRAP WORTH KNOWING, PRE-EXISTING AND NOT A DEFECT:** `grep -o "Bible version: v[0-9.]*"`
returns **three** lines against `ZUMO_SUPER_BIBLE.md`, two of them bare `Bible version: v` from prose
about the convention. **The session-open ritual uses `-oE` with `[0-9.]+`, which requires a digit and
correctly returns one line.** Do not relax that `+` to `*`.

---

# S171 OPENS HERE — WHAT IS ACTUALLY LEFT

- **`SWEEP_DONE` NEEDS A RULING** (above). It is the only open item this session created.
- **THE `-Wunused-result` HALF OF S167's DEBT IS STILL UNBUILT.** Marking the `StopReason`
  declarations `warn_unused_result` is a `RobotMotion.h` edit reaching every payload from L10 on.
  **The cheap half is now done** — stderr is no longer swallowed and the population is measured — so
  what remains is the declaration edit and its recompiled chain.
- **`byte_audit` ARM 2 STILL CANNOT SEE A FIGURE IN PROSE.** L13's `25,198` sites remain the
  unreachable class. ARM 7 closed headroom claims; ARM 8 closes warnings; **a wrong FIGURE in prose
  is still nobody's.**
- **L16 STILL NEVER STATES ITS MATCH-MODE FIGURE** (S166, unchanged).
- **`strip_inline --restore` DOES NOT RESPECT THE HELD LESSON STRIP** (S168, unchanged). The
  SCRATCH-COPY workaround works and was verified independently at S169.
- **`build_css.py --help` IS NOT A FLAG — IT RUNS AND WRITES THE STYLESHEET** (S169).
- **THE TAG-STRIP BLIND REGION IS MEASURED AND SEVEN RAW USES REMAIN** (S168). Exposure is zero
  today: only 2 of 583 comments can diverge. Do not widen until that changes.
- **`BookComponentStandard.md` CARRIES 44 BRITISH FORMS AND IS DELIBERATELY UNSWEPT** (S167) —
  `gen_component.py` pins the literal anchor `'### 5.2 Colour is never'`, rule 56.
- **GATE 77 DOES NOT EXCLUDE `<pre>`** (S165). When it first fires, the answer is a ruling.
- **THE REMAINING GPT WORKLIST** — 245 findings, most unadjudicated.
- L12 BONUS B4's bench measurement · L15 Challenge 3's `turnDegreesGyroSafe()` · L03 queued content ·
  `ZUMO_L03_TEMPLATES.md` staging · Bible §14 TDP-canon entry · day-by-day grid + syllabus.
- **The poster is a GRADED deliverable** (DJ, S159). **Photography is OFF the critical path** (DJ, S156).
- **Fall launch Sept 8 — under three weeks out. L13 is the last in-scope lesson and it is whole.**

---

# HARNESS — IT IS NOT IN THE REPO. RUN THE SCRIPT.

```
apt-get install -y gcc-avr avr-libc     # foreground; the box has no toolchain
sh harness_setup.sh                     # prints objects: 41  AND  core stderr: clean
```
**Invoke it through `sh`, not `./`** — the file is tracked 100644 and the executable bit does not
survive GitHub Desktop. `core stderr: clean` is NEW in v3.1; anything else means read
`$H/core_build.err`. Then, in order:

```
python3 byte_audit.py --sizes     # compiles every payload the Maker defines (~3 min)
python3 byte_audit.py --check     # EIGHT arms
python3 byte_audit.py --selftest  # run this before trusting --check
```

**CONTROLS — RE-VERIFIED AT S170 ON A HARNESS BUILT FROM SCRATCH UNDER `-Wall`. ALL EIGHT UNMOVED,
and that is this session's own headline control: turning warnings on moved NOTHING.**
L11 `after_step_1` **20,592** · `11/finished` **20,778** · `12/finished` **24,790** ·
`12/c2_slipalarm` **21,334** · `13/finished` **25,246** · `14/finished` **26,000** ·
`15/finished` **28,402** · `16/finished` **28,618**.
**Reproduce 20,592 before trusting the rest** (rule 30).

**216 payloads, FOUR declared overflows** — `16/after_step_3` **29,004** · `16/after_step_4`
**29,640** · `16/step_5_serial_traded` **28,936** · `16/step_5_zn_traded` **28,780**.

**THE TIGHTEST PASSING BUILD IN THE BOOK IS `16/after_step_2` AT 28,644, WITH 28 BYTES SPARE.**
Not `16/finished`, which has 54. Anything L16 ever gains again is priced against 28.

**`--sizes` WAS RUN THREE TIMES THIS SESSION AND 0 OF 216 FIGURES MOVED EACH TIME.** Snapshot
`/tmp/zumo_byte_sizes.json` and diff; the table now carries a `warn` key per payload as well.

---

# STANDING AUTHORITY — §24.17 AND §24.19

**Decide and report; do not ask.** Three carve-outs: facts about the ROOM no instrument can see;
moves that are irreversible or expensive to undo (the test is recoverability); and RoboLore brand
and course scope. **Delegation removes the question, never the disclosure.** Full text: Bible §24.17.

**§24.19 IS THE TIEBREAKER:** *what is best for learning, accuracy and the student*. S170's worked
example is `SWEEP_DONE` — measured, priced, and handed up rather than fixed, because it is course
content four lessons wide and the arm can hold the line meanwhile.

---
<!-- VERSION BLOCK: emitted by session_versions.py --handoff. Never hand-typed. -->
Fresh-clone verified at **`9fbc697`**. Census **40,980**.
Bible **v8.163** · `BookComponentStandard` **v01.13.0** · Maker **v2.60** ·
`marks/` **41** · `icons/` **49** incl. LICENSE.
`ZUMO_Syllabus_WORKING.md` **v1.3**.

Instruments: `book_gates` **v1.72.3** · `lesson_inventory` **v1.3.5** ·
`gen_component` **v1.6.1** · `pill_sweep` **v1.1** · `gate_payload_match` **v1.8.0** ·
`build_family_map` **v1.6.6.1** · `callout_id` **v1.0** · `keyterm_prefix` **v1.0.1** · `build_mark_index` **v1.1.0** · `gen_bonus_banner` **v1.4.1** ·
`gen_part_banners` **v1.2** · `session_versions` **v1.28.0** · `fit_raster_svg` **v1.2** ·
`flatten_alpha` **v1.2** · `svg_layout_audit` **v1.20** · `site_parity` **v1.1** ·
`build_css` **v1.3.0** ·
`image_audit` **v1.2** ·
`strip_inline` **v1.2** ·
`build_worklist` **v1.1** ·
`regex_audit` **v1.0** ·
`byte_audit` **v1.6** ·
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

Lessons: L01 v03.30.1 · L02 v03.21.5 · L03 v03.43.2 · L04 v04.29.2 · L05 v04.29.1 · L06 v04.32.4 · L07 v04.31.5 · L08 v04.32.1 · L09 v05.27.4 · L10 v02.30.3 · L11 v02.31.1 · L12 v01.33.1 · L13 v02.33.0 · L14 v02.35.2 · L15 v02.31.8 · L16 v02.27.0.
