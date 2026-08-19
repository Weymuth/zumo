# ZUMO — S172 HANDOFF (written at S171 close · paste at top of Session 172)

## READ THIS FIRST

**S171's work IS PUSHABLE and DJ verifies the push himself (standing ruling, S158).**
`git rm ZUMO_S171_HANDOFF.md` is part of that push. **If `__pycache__/` or `quizzes/__pycache__/`
exist in your tree, delete them LAST, immediately before pushing** — they REGENERATE on every gate run.

**77/77 gates** · `gate_payload_match` **PASS** · **`byte_audit --check` PASS across EIGHT arms,
`--selftest` ALL CONTROLS PASS** on a harness built from scratch by the script (`objects: 41`,
standing control **20,592** reproduced first) · `quiz_bank --selftest` all controls ·
`session_versions --selftest` EIGHT CONTROLS · `callout_id` **1127/0** · `keyterm_prefix` 0 to
convert · 16 banks valid, **1,245** questions · census **40,993** · `site_parity` PARITY ·
`build_css --check` current at 574 rules · `image_audit --check` current · `next_pointer` clean.

**`SWEEP_DONE` IS FIXED. IT WAS THE ONLY OPEN ITEM S170 CREATED AND IT IS CLOSED.**

---

# 1. WHAT S171 DID, AND WHY THE BYTE COST WAS NEVER THE COST

`case SWEEP_DONE:` now exists in the `loop()` dispatch — **read B, return to `STOPPED`, the shape
`LINE_LOST` already uses in the same file** — across **48 payloads**. `13/after_step_6` carries the
corner but NOT the assignment and was deliberately left: the far-wall detection is not born until
the next step, and the build-up model is intact.

**S170's FRAMING WAS TOO STRONG IN ONE CLAIM AND IT IS CORRECTED RATHER THAN CARRIED.** S170 said the
sweep ending was *the one ending that yields no scorecard*. It was not. **`VICTIM_FOUND` routes to
`STOPPED` in L15 and L16 too**, and only TWO paths ever reach `RUN_REPORT` — the kill switch during
`FOLLOWING_LINE`, and the `TUNING_RUN_MS` bell. `SWEEP_DONE` was never uniquely unscored. **It was
uniquely UNRECOVERABLE:** the one member of `RobotState` the program could not leave, whose only exit
was the power switch, in the lesson that spends a paragraph teaching that a dead B is TEMPORARY.

**PRICED ON A SCRATCH TREE BEFORE THE REPO WAS TOUCHED (rule 34)**, and `byte_audit` ENUMERATED the
churn instead of a hand hunt: ARM 2 **17** step figures · ARM 4 **7** KINDS labels · ARM 6 **2** bank
figures · ARM 7 **15** headroom claims · ARM 5 **0 broken**, because a delta is a difference and
differences do not move.

**BYTES: 27 payloads +2, 15 +4, 6 +8.** Standing controls **20,592 / 20,778 / 24,790 / 21,334
UNMOVED**. `13/finished` **25,248** · `14/finished` **26,002** · `15/finished` **28,406** ·
`16/finished` **28,626**. **The tightest build in the book is still `16/after_step_2`, now 28,648,
with 24 SPARE.** Four declared overflows stay declared. **ARM 8's population falls 70 → 22 payloads.**

**ROUTING IT INTO `endRun()` → `RUN_REPORT` WAS REJECTED**: that changes what L15 and L16 TEACH about
scoring, and makes zone endings inconsistent unless `VICTIM_FOUND` moves too. §24.19 points at the
cheap fix that restores the book's own pattern.

**`gate_payload_match` CAUGHT WHAT THE PRICING PASS DID NOT — the case had to be PRINTED.** 40
findings across ten L13 payloads, §16.26 firing on this session's own work. L13 now teaches it.

---

# 2. FOUR THINGS FOUND THAT WERE ON NOBODY'S LIST

1. **A WRONG FIGURE IN L16 PROSE THAT ARM 7 COULD NOT SEE.** §6 Step 1 read *28,402 of 28,672.
   **332 bytes of runway***; the correct number is 270 and the COMPILE CHECK one line below said 270.
   **ARM 7 passed it because 332 IS a real headroom number elsewhere** (Step 3's overage) — it
   asserts ceiling-minus-A-compile, never ceiling-minus-THIS-compile. **Now a stated blind spot.**
2. **THE WALL SVG HAD BEEN STALE SINCE S168.** `L16_GRAPHIC_16-02_the_wall.svg` still DREW L13 25,198
   · L14 25,942 · L15 28,340 · Step 3 28,950 · Step 4 29,586 and a banner reading *overflowed by 914
   bytes*, while the caption and `alt` were re-derived three sessions ago. **The caption and the
   picture disagreed for three sessions and nothing in this repo reads inside an SVG.** Redrawn; the
   px/byte scale was re-verified against the six bars that did NOT move first.
3. **`25,198 bytes each` IN L13's B2 REVEAL** — a byte-identical claim carrying a pre-S168 figure.
4. **THE SERIAL CUT FREES 700, NOT 704** — `after_step_4` gained +4 while `step_5_serial_traded`
   gained +8, because Serial's presence changes what LTO can fold. Every other delta held.

---

# 3. THE FIX BROKE ITS OWN CONTROL — READ THIS BEFORE TOUCHING `byte_audit`

**`FINISHED_WARN_BASELINE` IS NOW EMPTY. That is its resting state, not a switched-off arm.**
`arm8()` still fails on an EMPTY TABLE and on a table with no warning data, so *nothing to
adjudicate* and *nothing was measured* cannot be confused.

**CONTROL K leaned on the baseline holding four live entries**, so the day the defect was fixed that
control either fails or gets deleted — **a control whose fixture is borrowed from the population it
audits fails when you succeed** (S166's finding, second occurrence). `arm8()` now takes an
**injectable `baseline`** and CONTROL K plants its own signature in its own fixture, so it tests the
ARM rather than the state of the book. **NEW EIGHTH ASSERTION: with an EMPTY baseline, ANY finished
warning is LOUD.** CONTROL J's two anchors were re-pinned to the S171 figures, because they seed the
exact strings this session moved.

---

# 4. S172 OPENS HERE — WHAT IS ACTUALLY LEFT

- **THE L13 AND L14 BANKS CARRY FIGURES THAT LOOK STALE FROM BEFORE S171, AND I DELIBERATELY DID NOT
  TOUCH THEM.** `20,516` in both (a figure S166 retired), plus `25,942`, `25,886`, `25,906`,
  `25,816`, `25,202` and others in L14. **Some are certainly deliberate wrong-answer distractors**,
  and I have not read those banks this session. **This is a pin arc — READ → FIX → QUIZ — not a
  find-and-replace**, and bulk-rewriting risks turning a correct distractor into a wrong one.
- **THE `-Wunused-result` HALF OF S167's DEBT IS STILL UNBUILT.** Marking the `StopReason`
  declarations `warn_unused_result` is a `RobotMotion.h` edit reaching every payload from L10 on.
- **`byte_audit` ARM 2 STILL CANNOT SEE A FIGURE IN PROSE.** L13's `25,198` sites are gone, but the
  CLASS is not closed — S171 found three prose figures by reading, not by an instrument.
- **L16 STILL NEVER STATES ITS MATCH-MODE FIGURE** (S166, unchanged).
- **`strip_inline --restore` DOES NOT RESPECT THE HELD LESSON STRIP** (S168). SCRATCH-COPY workaround.
- **`build_css.py --help` IS NOT A FLAG — IT RUNS AND WRITES THE STYLESHEET** (S169).
- **THE TAG-STRIP BLIND REGION IS MEASURED AND SEVEN RAW USES REMAIN** (S168). Exposure zero today.
- **`BookComponentStandard.md` CARRIES 44 BRITISH FORMS AND IS DELIBERATELY UNSWEPT** (S167, rule 56).
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
survive GitHub Desktop. Then, in order:

```
python3 byte_audit.py --sizes     # compiles every payload the Maker defines (~3 min)
python3 byte_audit.py --check     # EIGHT arms
python3 byte_audit.py --selftest  # run this before trusting --check
```

**CONTROLS — RE-VERIFIED AT S171 ON A HARNESS BUILT FROM SCRATCH. FOUR UNMOVED, FOUR MOVED BY THE FIX:**
L11 `after_step_1` **20,592** · `11/finished` **20,778** · `12/finished` **24,790** ·
`12/c2_slipalarm` **21,334** — all UNMOVED · `13/finished` **25,248** · `14/finished` **26,002** ·
`15/finished` **28,406** · `16/finished` **28,626**.
**Reproduce 20,592 before trusting the rest** (rule 30).

**216 payloads, FOUR declared overflows** — `16/after_step_3` **29,008** · `16/after_step_4`
**29,644** · `16/step_5_serial_traded` **28,944** · `16/step_5_zn_traded` **28,788**.

**THE TIGHTEST PASSING BUILD IN THE BOOK IS `16/after_step_2` AT 28,648, WITH 24 BYTES SPARE.**
Not `16/finished`, which has 46. Anything L16 ever gains again is priced against 24.

---

# STANDING AUTHORITY — §24.17 AND §24.19

**Decide and report; do not ask.** Three carve-outs: facts about the ROOM no instrument can see;
moves that are irreversible or expensive to undo (the test is recoverability); and RoboLore brand
and course scope. **Delegation removes the question, never the disclosure.** Full text: Bible §24.17.

**§24.19 IS THE TIEBREAKER:** *what is best for learning, accuracy and the student*. S171's worked
example is `SWEEP_DONE` itself — the cheap fix that restores the book's own pattern beat the
semantically richer one that would have moved what two lessons teach about scoring.

---
<!-- VERSION BLOCK: emitted by session_versions.py --handoff. Never hand-typed. -->
Fresh-clone verified at **`8c94416`**. Census **40,993**.
Bible **v8.164** · `BookComponentStandard` **v01.13.0** · Maker **v2.61** ·
`marks/` **41** · `icons/` **49** incl. LICENSE.
`ZUMO_Syllabus_WORKING.md` **v1.3**.

Instruments: `book_gates` **v1.72.4** · `lesson_inventory` **v1.3.5** ·
`gen_component` **v1.6.1** · `pill_sweep` **v1.1** · `gate_payload_match` **v1.8.0** ·
`build_family_map` **v1.6.6.1** · `callout_id` **v1.0** · `keyterm_prefix` **v1.0.1** · `build_mark_index` **v1.1.0** · `gen_bonus_banner` **v1.4.1** ·
`gen_part_banners` **v1.2** · `session_versions` **v1.28.0** · `fit_raster_svg` **v1.2** ·
`flatten_alpha` **v1.2** · `svg_layout_audit` **v1.20** · `site_parity` **v1.1** ·
`build_css` **v1.3.0** ·
`image_audit` **v1.2** ·
`strip_inline` **v1.2** ·
`build_worklist` **v1.1** ·
`regex_audit` **v1.0** ·
`byte_audit` **v1.7** ·
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

Lessons: L01 v03.30.1 · L02 v03.21.5 · L03 v03.43.2 · L04 v04.29.2 · L05 v04.29.1 · L06 v04.32.4 · L07 v04.31.5 · L08 v04.32.1 · L09 v05.27.4 · L10 v02.30.3 · L11 v02.31.1 · L12 v01.33.1 · L13 v02.34.0 · L14 v02.36.0 · L15 v02.32.0 · L16 v02.28.0.
