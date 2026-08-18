# ZUMO — S170 HANDOFF (written at S169 close · paste at top of Session 170)

## READ THIS FIRST

**S169's work IS PUSHABLE and DJ verifies the push himself (standing ruling, S158).**
`git rm ZUMO_S169_HANDOFF.md` is part of that push. **If `__pycache__/` or `quizzes/__pycache__/`
exist in your tree, delete them LAST, immediately before pushing** — they REGENERATE on every gate run.

**77/77 gates** · `gate_payload_match` **PASS** · **`byte_audit --check` PASS across SEVEN arms
(ARM 7 is new), `--selftest` ALL CONTROLS PASS** on a harness built from scratch by the script
(`objects: 41`, standing control **20,592** reproduced first) · `quiz_bank --selftest` all controls ·
`session_versions --selftest` EIGHT CONTROLS · `callout_id` **1127/0** · `keyterm_prefix` 0 to
convert · 16 banks valid, **1,245** questions · census **40,980** · `site_parity` PARITY on two
consecutive runs · `build_css --check` current at 574 rules · `image_audit --check` current ·
`next_pointer` clean.

**6 files changed, 0 new, 0 deleted** — verified by whole-tree md5 against a fresh clone (ARM 3):
`newproject.html` · `lessons/Lesson_16.html` · `quizzes/ZUMO_QUIZ_L16.yaml` · `css/book.css` ·
`book_gates.py` · `harness_setup.sh` · `byte_audit.py` — plus `ZUMO_SUPER_BIBLE.md`,
`ZUMO_AFTER_LAUNCH.md`, `LIVE_ZUMO_TEXTBOOK.md`, **`ZUMO_S170_HANDOFF.md` new** and
**`ZUMO_S169_HANDOFF.md` deleted**.

**RUN THE HARNESS FIRST — AND THE TOOLCHAIN IS NOT ON THE BOX.** A fresh container has no
`avr-gcc` at all. `harness_setup.sh` **v1.1** now checks and tells you; the install is
`apt-get install -y gcc-avr avr-libc`, then `sh harness_setup.sh` (**`objects: 41`**).

---

# THE FOUR THINGS TO CARRY OUT OF S169

## 1. THE DESCRIPTION WAS A LEAD AND THE ARTEFACT ENLARGED THE JOB — SECOND SESSION RUNNING.

`28,780` was handed forward as *a mid-trade checkpoint with no payload*. Read, `16/finished`
differs from `16/step_5_serial_traded` by **two** things — the WEAVE trade **and** the Step 6
enhancement socket — so **the mid-trade state was never reachable by a diff of the two existing
payloads.** That is the real reason it had no door, and it is not what the description implied.
The socket is byte-free, which is what lets the chain close: 28,936 − 156 − 162 = 28,618.

**BOTH INFERRED FIGURES ARE NOW MEASURED AND BOTH WERE RIGHT.** `step_5_zn_traded` is its sibling
minus **exactly** the Ziegler–Nichols hunk the lesson prints, and compiles to **28,780**, the cut
costing exactly the **156** bytes the lesson advertises. `finished` minus all twelve `playNote()`
calls weighs **26,790** exactly — buzzer **1,828**, spare **1,882**. **26,790 keeps no payload
deliberately:** §7.4 hands that cut to the student, so it is a hypothetical the book offers, not a
build it ships. **An inference that turns out right is still worth measuring, because until you
measure it you cannot tell it from one that is wrong.**

## 2. MY FIRST SCAN RETURNED ZERO ON A BANK THAT PLAINLY CONTAINS THE FIGURE.

The `QUIZ_L16` read opened with a predicate that walked the wrong YAML structure and reported **no
questions asserting Step 5 material** — on a bank whose `B44` rationale states 28,780 outright.
**A zero from an uncontrolled instrument is not a measurement.** Rebuilt and **controlled against
that known site before it was trusted**, it returned sixteen. S167's rule turned on my own tooling
rather than on the book's.

**THREE STALE FIGURES, ALL SURVIVORS OF S168's +54 REBASELINE:**
`L16_A07` keyed *still 210 over* as its **CORRECT** answer while its own distractor rationale said
**264** — a question disagreeing with itself (rule 51), and v8.130's punish-the-attentive shape.
`L16_B44`'s rationale carried the same *210*, and **the hand read missed it; ARM 7 named it.**
`Lesson_16` §7.4 promised *108 bytes* of reserve where §5 of the same lesson says *Green. 54 to
spare* and the compiled build leaves **54**.

## 3. §16.38 — A HEADROOM CLAIM IS CHECKABLE BY ITS RELATION, NOT BY ITS SHAPE.

**210, 108 and 54 carry no comma and sit below the byte band**, so every figure-shaped predicate in
this repo — ARM 2, ARM 6, ARM 2b's band sweep, every comma sweep S168 built — is **structurally
blind to them.** What makes a headroom claim checkable is that it IS the ceiling minus a build.

**`byte_audit` ARM 7 NEW, AND ITS CONTROLS SHIP.** S167 and S168 each wrote a claim-audit arm, each
paid for it, and each threw it away; this is the third build. The controls now live in
`--selftest`, not in a transcript. **Population measured before a line was written (rule 34): 17
claims book-wide, 4 leads, and TWO OF THE FOUR WERE FALSE POSITIVES** — a loose `By N.` pattern
matching *0.9 divided by 10.* and *divided by 12.25*. Narrowed; that form stays ARM 5's, where a
COMPILE CHECK window makes it unambiguous. **The conditional exclusion is a PROPERTY, not a name
list:** *what cutting the buzzer WOULD give* is skipped, and **removing the subjunctive makes it
fire** — controlled, so the skip is not a hole. **Both blind spots ship stated (rule 78) and one is
demonstrated:** seeded with *270* — a real headroom of a real build, but the wrong one — the arm is
correctly SILENT.

## 4. A GUARD THAT SKIPS SILENTLY READS EXACTLY LIKE A CONTROL THAT PASSED — AND I COMMITTED IT INSIDE THE CONTROL SUITE.

ARM 7's conditional control was guarded by `count == 1` on a bare phrase that **my own provenance
note, written minutes earlier, had just made occur three times.** The control printed nothing and
the suite read green. **v8.109's trap in a new costume: a session broke its own instrument with the
sentence describing it.** Every guard in CONTROL J is now an ASSERTION on a uniquely-anchored
string, and a failed anchor is loud.

**THE SAME SHAPE, TWICE MORE, BOTH CAUGHT BY READING THE DETAIL RATHER THAN THE VERDICT:** the
first blinding control on the moved §27.11 baseline **PASSED and was not accepted**, because the
injection landed in the hand-authored semantic layer the gate deliberately does not hash (S154's
trap verbatim) — re-aimed at the generated block, it fires. And ARM 7's first COVERAGE control
pointed at an empty quiz dir, which **could never reach zero** because the lessons still supply
claims; it blinds the patterns instead.

---

# S170 OPENS HERE — WHAT IS ACTUALLY LEFT

- **THE HARNESS FLAG IS THE LAST S167 INSTRUMENT FIX STILL UNBUILT.** `pio_harness.sh` still
  compiles with `-w` and `2>/dev/null`, so the compiler still cannot speak. **Population
  measurement comes first** (rule 34): S167 measured L10–L16 *finished* builds only, and the other
  ~180 payloads are a stated gap. The separable cheap half is to stop swallowing stderr and read
  one clean build. **The prose half of that debt is now CLOSED by ARM 7** — but only for headroom
  claims; a wrong FIGURE in prose is still ARM 2's blind spot.
- **`byte_audit` ARM 2 STILL CANNOT SEE A FIGURE IN PROSE.** L13's `25,198` sites remain the
  unreachable class. L16's `28,780` and `26,790` have left it: the first has a payload and a
  gated KINDS label, the second is measured and correctly scoped out as conditional.
- **L16 STILL NEVER STATES ITS MATCH-MODE FIGURE** (S166, unchanged) — the number lives in the
  Maker, the Bible and LIVE.md and appears nowhere in `Lesson_16.html`.
- **`strip_inline --restore` DOES NOT RESPECT THE HELD LESSON STRIP** (S168, unchanged). The
  SCRATCH-COPY workaround was used again this session and it works: copy the tree, run
  restore → build → apply there, bring back only `css/book.css`. **Verified independently this
  session** — a direct `build_css.py` run on the class-based tree produced a **byte-identical**
  stylesheet, so the two routes agree. **Measured, still not fixed.**
- **`build_css.py --help` IS NOT A FLAG — IT RUNS AND WRITES THE STYLESHEET.** Found by walking
  into it. Harmless here because the output was verified against the documented cycle, but a tool
  whose help text is an action is a trap for the next reader.
- **THE TAG-STRIP BLIND REGION IS MEASURED AND SEVEN RAW USES REMAIN** (S168, unchanged).
  Exposure is zero today: only 2 of 583 comments can diverge. Do not widen until that changes.
- **`BookComponentStandard.md` CARRIES 44 BRITISH FORMS AND IS DELIBERATELY UNSWEPT** (S167) —
  `gen_component.py` pins the literal anchor `'### 5.2 Colour is never'`, rule 56.
- **GATE 77 DOES NOT EXCLUDE `<pre>`** (S165, unchanged). When it first fires, the answer is a ruling.
- **THE REMAINING GPT WORKLIST** — 245 findings, most unadjudicated, and the strongest two are
  already built and closed. What is left needs adjudicating before it is worth anything.
- L12 BONUS B4's bench measurement · L15 Challenge 3's `turnDegreesGyroSafe()` · L03 queued content ·
  `ZUMO_L03_TEMPLATES.md` staging · Bible §14 TDP-canon entry · day-by-day grid + syllabus.
- **The poster is a GRADED deliverable** (DJ, S159). **Photography is OFF the critical path** (DJ, S156).
- **Fall launch Sept 8 — three weeks out. L13 is the last in-scope lesson and it is whole.**

---

# HARNESS — IT IS NOT IN THE REPO. RUN THE SCRIPT.

```
apt-get install -y gcc-avr avr-libc     # NEW: the box has no toolchain
sh harness_setup.sh                     # prints objects: 41
```
**Invoke it through `sh`, not `./`** — the file is tracked 100644 and the executable bit does not
survive GitHub Desktop. Then, in order:

```
python3 byte_audit.py --sizes     # compiles every payload the Maker defines (~3 min)
python3 byte_audit.py --check     # SEVEN arms
python3 byte_audit.py --selftest  # run this before trusting --check
```

**CONTROLS — RE-VERIFIED AT S169 ON A HARNESS BUILT FROM SCRATCH. ALL EIGHT UNMOVED, because this
session's edits were a new payload, prose and bank text:**
L11 `after_step_1` **20,592** · `11/finished` **20,778** · `12/finished` **24,790** ·
`12/c2_slipalarm` **21,334** · `13/finished` **25,246** · `14/finished` **26,000** ·
`15/finished` **28,402** · `16/finished` **28,618**.
**Reproduce 20,592 before trusting the rest** (rule 30).

**216 payloads, FOUR declared overflows now** — `16/after_step_3` **29,004** ·
`16/after_step_4` **29,640** · `16/step_5_serial_traded` **28,936** · `16/step_5_zn_traded`
**28,780** (new). Each is deliberate and each is the lesson's own premise.

**THE TIGHTEST PASSING BUILD IN THE BOOK IS `16/after_step_2` AT 28,644, WITH 28 BYTES SPARE.**
Not `16/finished`, which has 54. Anything L16 ever gains again is priced against 28.

**A ZERO-BYTE CLAIM IS A MEASURED CLAIM.** Snapshot `/tmp/zumo_byte_sizes.json`, re-run `--sizes`,
diff.

---

# STANDING AUTHORITY — §24.17 AND §24.19

**Decide and report; do not ask.** Three carve-outs: facts about the ROOM no instrument can see;
moves that are irreversible or expensive to undo (the test is recoverability); and RoboLore brand
and course scope. **Delegation removes the question, never the disclosure.** Full text: Bible §24.17.

**§24.19 IS THE TIEBREAKER:** *what is best for learning, accuracy and the student*. S169's worked
example is the toolchain ruling — **check rather than install**, because provisioning the machine is
a larger and less reversible move than this script's job, and a script that silently mutates the box
is worse than one that names what is missing.

---
<!-- VERSION BLOCK: emitted by session_versions.py --handoff. Never hand-typed. -->
Fresh-clone verified at **`ca141ab`**. Census **40,980**.
Bible **v8.162** · `BookComponentStandard` **v01.13.0** · Maker **v2.60** ·
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
`byte_audit` **v1.5** ·
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
`pio_harness.sh` **v3.0** ·
`going_deeper` **v01.6.1**.

Lessons: L01 v03.30.1 · L02 v03.21.5 · L03 v03.43.2 · L04 v04.29.2 · L05 v04.29.1 · L06 v04.32.4 · L07 v04.31.5 · L08 v04.32.1 · L09 v05.27.4 · L10 v02.30.3 · L11 v02.31.1 · L12 v01.33.1 · L13 v02.33.0 · L14 v02.35.2 · L15 v02.31.8 · L16 v02.27.0.
