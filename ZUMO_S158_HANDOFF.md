# ZUMO — S158 HANDOFF (written at S157 close · paste at top of Session 158)

## READ THIS FIRST

**S157's work IS PUSHABLE.** 73/73 gates, `byte_audit --check` PASS, every instrument clean.
`gate_payload_match` reports **FAIL(306) and that is the correct state** — see below before you
"fix" it.

Three files changed against the pushed clone, verified file by file:
`lessons/Lesson_10.html` · `newproject.html` · `css/book.css` — plus `book_gates.py`,
`build_family_map.py`, `ZUMO_SUPER_BIBLE.md` and `LIVE_ZUMO_TEXTBOOK.md`.

---

# THE ONE THING TO CARRY OUT OF S157

**`gate_payload_match` IS GREEN AT BOTH ENDS OF THE OPTION-C ROLLOUT AND RED EVERYWHERE BETWEEN.**

The gate carries *v1.1 inheritance: the prior lesson's finished payload is canonical for lesson N*.
L11 never printed the primitive declarations, the definitions or the `EXECUTING_TURN` dispatch — it
has always **inherited** them from L10's `finished`. Convert L10 and L11's 17 payloads go red at
**306 findings = 18 distinct lines × 17 payloads**, every one an unconverted `void` form.

L12–L16 were checked the same way and **none of them prints those lines either.** So each lesson
breaks its successor as it converts, and the suite cannot be green again until L16 lands.

**THE CHECKPOINT TO READ, NOT THE VERDICT: FAIL(306) with ZERO L10 findings.**
If L10 findings are anything but zero, something regressed. If the total is not 306, a lesson other
than L11 moved. **Do not scope the gate and do not compare its counts across argument sets.**

---

# S157's RULINGS AND WHY

**STEP 6 SPLITS. `Step 6b — Make Every Move Report Back` IS NEW.**
DJ ruled *"do whatever is best… what's best long term and for the kids"*, so the seam was chosen on
evidence rather than on shape.

**The bank decided it.** L10 bank A10 explains a distractor with *"It costs +2 bytes. It is nearly
the smallest thing in the lesson."* Absorbing the reporting contract into Step 6 puts its checkpoint
at **+46** and marks the students who read carefully wrong. Split, the figures re-derive as:

| payload | flash | delta | door |
|---|---|---|---|
| `after_step_5` | 19,560 | — | Step 5 |
| `after_step_6` | **19,562** | **+2** | Step 6 (kill switch only) |
| `after_step_6b` | **19,606** | **+44** | Step 6b (the contract) |
| `after_step_7` | 19,782 | +176 | Step 7 |

**The +2 the lesson has always printed is true again and the bank needed no edit.**

**THE `b` SUFFIX WAS CHOSEN TO AVOID RENUMBERING.** L11 already ships `📁 Step 2b`. A real Step 7
would have moved Steps 7/8/9, five catch-up links, five `KINDS` rows, both ARM 3 rows and every bank
citation. `Step 6b` moves none of them.

**`after_step_6` WAS RE-CUT BYTE-EXACT FROM THE PUSHED CLONE** (§11 extraction, never
reconstructed); the converted state became the new `after_step_6b`; `step_7`'s `KINDS` row was
repointed `after_step_6` → `after_step_6b`.

---

# WHAT S157 FOUND (all instrument-derived, none carried)

**STEP 6 TAUGHT `StopReason` AND SHIPPED NONE OF ITS CODE.** Derived by DOM parse of the step
region: two `<pre>` blocks, both `main.cpp`, and `RobotConfig.h` / `RobotMotion.h` /
`RobotMotion.cpp` named **zero times**. The Maker's payload had all of it. **The catch-up door was
silently repairing a hole the prose created** — the S152 shape with the polarity reversed.

**AND THE HEADER DECLARATIONS COULD NEVER HAVE BEEN INHERITED.** They reach the student from L09's
`finished`, which stays `void`. The gate was naming content the book owed, not complaining.

**S156's CONVERSION CARRIED A STRUCTURAL DEFECT NO BYTE FIGURE COULD SEE.** The `StopReason` enum
sat **between `// ===== AVOIDANCE PHASES =====` and `enum AvoidPhase`** in all ten payloads, so the
header labelled the wrong enum. Comments and enum ordering emit nothing — **rule 85 from the far
side: a binary IDENTITY is not a code identity either.** Fixed at zero cost, proved by disassembly
with addresses stripped: **two differing lines, the filename and one compiler temp symbol.**

**A STALE BYTE FIGURE THAT PREDATES THE ROLLOUT.** Step 4's *"+50 bytes over Step 3"* — compiled
**from the clean clone**, 18,202 − 18,158 = **44**. S143 corrected four of L10's byte claims and
this was not among them: **the four it fixed were the four it was looking at.**

**§8A.2 CLAIMED TO BE THE REAL CODE AND WAS NOT.** *"This is the real code from your project"* sat
above a simplified unguarded excerpt. The excerpt was made real rather than the claim softened.

**ALL FIVE L10 BYTE FIGURES SWEPT FROM THE RAW SOURCE**, not the rendered text:
**+50→+44 · +2 stays +2 · +194→+176 · +660→+710 · 20,516→20,592.**

**A PIN HAS TWO HOMES.** §21's denominator was moved in the message and not in the comparison, so
the gate failed reading *1207, expected 1,207*. Editing the readable home is editing the wrong one.

---

# S158 NEXT — CONVERT L11

L11 is **17 of 17** payloads (all carry `killSwitchPressed`). The method is proven:

1. Locate each payload key inside its lesson span, brace-match its byte range, replace only within
   it, **DESCENDING by position**. Lessons are **not** in numeric order — file order is
   1, 15, 14, 13, 12, 11, 8, 9, 7, 6, 4, 3, 5, 2, 10, 16.
2. `#include "RobotMotion.h"` appears **twice** per payload; the unique landmark is
   `#include "RobotMotion.h"\n\n// ===== FUNCTION IMPLEMENTATIONS =====`.
3. **The Maker cannot be round-tripped through `json.dumps`** — closest indent is off by 6,070
   characters (rule 69).
4. Then read L11's own `<pre>` blocks: the same *does the lesson print what the payload holds*
   question that made Step 6b necessary. **Ask it before converting, not after.**
5. Expect L11 findings → 0 and L12 findings → nonzero. That is the chain advancing, not a defect.

**THE REST OF THE ROLLOUT:** L12 21/21 · L13 **17 of 19** (`ladder_7a_surface_meter` and
`ladder_7c_leg_and_turn` have no kill switch) · L14 12/12 · L15 16/16 · L16 9/9.

**L16 IS THE CONSTRAINT AND IT MUST BE LAST.** `finished` ships with **72 bytes spare**;
primitives-only puts it at 28,664, fitting with **8**. Its Step 1 IS L15's finished build, so it
cannot be re-plotted until L15's number is final. Precedent for the re-plot is S148.

**MEASURED COST, PER LESSON — DO NOT EXTRAPOLATE ONE LESSON'S FIGURE TO ANOTHER.**
Primitives-only: **L10 +40 · L13/L14/L15/L16 +64.**

---

# HARNESS — IT IS NOT IN THE REPO, REBUILD IT

`pio_harness.sh --setup` needs the toolchain and the libraries first, neither of which ship here:

```
apt-get install -y gcc-avr avr-libc binutils-avr     # no sudo on this box
```
Clone FLAT into `/home/claude/harness` (read `LIBDIRS` out of the script, never from a handoff):
the eight Pololu repos plus `arduino/ArduinoCore-avr`, with
`zumo-32u4-arduino-library` at `--branch 2.0.1`. **Copy `pio_harness.sh` INTO `/home/claude/harness`** —
`byte_audit` invokes it from there and CONTROL A fails opaquely if it is missing.
`shim.cpp` is referenced and does not exist; the `[ -f ]` guard makes it optional.

**CONTROL: L11 `after_step_1` = 20,516.** Reproduced at S157 from a **seventh** clone.
`objects: 41`. Run `byte_audit.py --sizes` before `--selftest`, or CONTROL H fails on an empty table.

---

# STANDING AUTHORITY — §24.17, RULED S157

**Decide and report; do not ask.** Anything the repo can
answer is yours to settle. Three carve-outs only: facts about the ROOM no instrument can see (e.g.
whether every student gets floor time, which decides §7E's locked rung); moves that are irreversible
or expensive to undo (the test is recoverability, not size); and RoboLore brand and course scope.
**Delegation removes the question, never the disclosure** — report what was decided, on what
evidence, and what it cost. Full text: Bible §24.17, seated with a numbered body.

---

# STILL OPEN, CARRIED FORWARD

- **C2 — SENSOR-AS-TRUTH LANGUAGE. RULED: ADOPT.** *A sensor answers its own question, not yours.*
  L04–L13 prose plus the quiz re-keying it forces. **The strongest item in the review.**
- **C6 — COMPETITION RULE vs ROBOLORE POLICY.** Still the cheapest move in the queue and it needs
  no ruling — 8 findings, one read of `RCJRescueLine2026-final.pdf`, which is in the repo root.
- **C1 — TRIM justification backwards in L08** (practice correct, reason wrong; 2 occurrences).
- **C3 — kill-switch fix for blocking loops.** Confirmed; L10 is now done, L11–L16 follow the rollout.
- **§16.25's BODY IS STALE BY ONE SESSION.** Bible line ~2662 still says in the present tense that
  lessons and Maker ship `a-star32u4` lowercase "in six places". **S155 made and applied that
  ruling.** DJ ruled: RECORD IT. Doc-only, minor bump. The two changelog hits are correct as past tense.
- **A-Star hardware identity fix** in L01 and L03 prose (KEY TERM `term-a-star`) — GPT P0, confirmed
  defect per the S154 fleet ruling, not yet built.
- **L03's photograph `L03_IMAGE_3-14_astar_board.jpg`** names a board the robot does not contain. Unruled.
- `bonus_b5`'s deliberate sabotage — positive `turnDegrees(AVOID_TURN_DEGREES)` under a comment
  reading *"Negative = left"* — **survived S157 intact and is assert-guarded. Keep it that way.**
- L03 queued content (ms unit, modulo explainer, Coach's Tips) · `ZUMO_L03_TEMPLATES.md` staging ·
  TDP template v3 A5 Lab Log · Bible §14 TDP-canon entry · day-by-day period grid + syllabus.
- **Photography is OFF the critical path** (DJ, S156).

---

<!-- VERSION BLOCK: emitted by session_versions.py --handoff. Never hand-typed. -->
Fresh-clone verified at **`a71401b`**. Census **40,778**.
Bible **v8.147** · `BookComponentStandard` **v01.13.0** · Maker **v2.52** ·
`marks/` **41** · `icons/` **49** incl. LICENSE.
`ZUMO_Syllabus_WORKING.md` **v1.2**.

Instruments: `book_gates` **v1.68.2** · `lesson_inventory` **v1.3.5** ·
`gen_component` **v1.6.1** · `pill_sweep` **v1.1** · `gate_payload_match` **v1.8.0** ·
`build_family_map` **v1.6.5** · `callout_id` **v1.0** · `keyterm_prefix` **v1.0.1** · `build_mark_index` **v1.1.0** · `gen_bonus_banner` **v1.4.1** ·
`gen_part_banners` **v1.2** · `session_versions` **v1.26.0** · `fit_raster_svg` **v1.2** ·
`flatten_alpha` **v1.2** · `svg_layout_audit` **v1.20** · `site_parity` **v1.1** ·
`build_css` **v1.3.0** ·
`image_audit` **v1.2** ·
`strip_inline` **v1.2** ·
`build_worklist` **v1.1** ·
`regex_audit` **v1.0** ·
`byte_audit` **v1.2** ·
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
`quiz_bank` **v1.0.1** ·
`timer.html` **v1.3.2** ·
`going_deeper` **v01.6.1**.

Lessons: L01 v03.28.5 · L02 v03.21.3 · L03 v03.41.1 · L04 v04.29.1 · L05 v04.29.0 · L06 v04.32.1 · L07 v04.31.4 · L08 v04.31.1 · L09 v05.27.0 · L10 v02.30.0 · L11 v02.30.0 · L12 v01.31.3 · L13 v02.29.0 · L14 v02.34.0 · L15 v02.31.2 · L16 v02.24.0.
