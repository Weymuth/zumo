# ZUMO — Shelved Challenge Cards

**Status:** proposals, never authored. Nothing in this file was ever live in the book, and nothing
was removed to create it. These are card specs that were researched, verified, and then shelved by
a design ruling. Everything here is recoverable without re-doing the source research.

**Shelved at:** S67, Jul 24 2026.
**Shelved because:** DJ ruled the L12–L14 problem is the **difficulty ramp (Job B)**, not the
challenge count (Job A). All six cards below are Easy/Medium notebook or measurement work — they
raise N but lower the lesson's doing mean. Under Job B that is the wrong direction. Under Job A
(count parity) they are ready to build as written.

**Reopen this file if:** the ruling flips to count parity, or L12–L14's N=3 becomes a problem on
its own terms (the rest of the book runs N=5–11).

---

## Context at time of shelving

Both-axes means, recomputed from the files on the canonical scale
(doing: Easy 1 / Medium 2 / Tough 3 / Hard 4 / Advanced 5 · grasp: Light 1 / Moderate 2 / Deep 3):

| L | N | doing | grasp | | L | N | doing | grasp |
|---|---|---|---|---|---|---|---|---|
| 01 | 11 | 1.36 | 1.36 | | 09 | 6 | 2.50 | 2.17 |
| 02 | 6 | 1.67 | 1.50 | | 10 | 5 | 2.60 | 1.80 |
| 03 | 8 | 1.88 | 1.62 | | 11 | 5 | 2.00 | 2.20 |
| 04 | 5 | 2.00 | 2.20 | | 12 | 3 | **2.67** | 2.33 |
| 05 | 5 | 2.20 | 1.80 | | 13 | 3 | **3.00** | 2.00 |
| 06 | 8 | 2.62 | 1.88 | | 14 | 3 | **2.67** | 2.33 |
| 07 | 6 | 1.83 | 1.50 | | 15 | 7 | 3.29 | 2.57 |
| 08 | 5 | 2.00 | 2.00 | | 16 | 0 | — | — |

Projected effect had all six shipped: L12 2.67→2.20 · L13 3.00→2.20 · L14 2.67→2.40.

**All six cards are zero Maker / zero payload impact** — verified against each lesson's own kind
list. They either ride an existing `cal_7*` kind or are notebook-only with no Maker link.

---

# L12 — Wheels Lie (Gyro)

Existing cards: 12.1 Medium/Deep · 12.2 Medium/Moderate · 12.3 Hard/Moderate
Available kinds: `b1_spinning_cal b2_no_update b3_reset_hoisted b4_trim_in_turn c1_heading
c2_slipalarm c3_stuckguard cal_7a–cal_7e finished step_1–step_7`

## L12 C4 — The Square, Measured
- **Marker:** `12.4` · **format:** prose (measurement) · **tiers:** Medium / Deep
- **Rides:** `cal_7e` (existing — no new payload)
- **Source prose:** §7E "The Lesson 6 Square." Already ships the A/C button sketch: Button A turns
  corners with `turnDegrees()` (encoder), Button C with `turnDegreesGyro()` (gyro), four 30 cm
  sides, everything else identical.
- **What the card adds:** §7E is currently qualitative — "the square collapses" / "the square
  closes." The card makes the student **quantify** it. Four runs: encoder on carpet, gyro on carpet,
  encoder on delrin, gyro on delrin. For each, measure (a) distance from the finish point back to
  the start point, (b) heading error at finish.
- **Why it matters:** the TDP template's A4 table already has an **"Encoder vs. Gyro (L12) — turn
  90°, record both, on two surfaces / Carpet / Slick floor / Which I trust"** block, and **no card
  in the book currently feeds it.** This card fills a table the TDP already asks for.
- **Measurement method (unruled — needs a DJ ruling like L11 C4's post-it method got):** the L11 C4
  precedent is a post-it at the start point with the robot's FRONT BLADE lined to its edge, a second
  post-it at the stop point, measure between. Same approach should work here but was never ruled.
- **Solution shape:** on carpet both close and roughly agree — both instruments are good and the
  disagreement is small. On delrin the encoder square opens out (each corner short of 90°, errors
  add and do not cancel) while the gyro square still closes. The gap between the two numbers on the
  same surface IS the slip, which is the §8A.2 point made with the student's own data.

## L12 C5 — What 2^29 Is Doing In There
- **Marker:** `12.5` · **format:** prose (notebook-only, no Maker link) · **tiers:** Easy / Deep
- **Source prose:** §8A.3 "The Fixed-Point Angle." §4.4 sets it up and explicitly points forward:
  "(Curious what 2^29 is doing there? Section 8A.3 opens the door.)"
- **What the card asks:** verify by hand that the lesson's conversion function is exact.
  The function, from §4.4:
  ```c
  int getTurnAngle() { return (((int32_t)turnAngle >> 16) * 360) >> 16; }
  ```
  Feed it 2^29 and 2^30 and show the output is exactly 45 and exactly 90 — no rounding, no
  truncation. Then show why 2^32 units = 360° and 2^29 units = 45° are the same scale.

- **VERIFIED ARITHMETIC** (computed, not recalled — safe to put in a solution):
  - 2^29 = 536,870,912 → `>>16` = 8,192 → ×360 = 2,949,120 → `>>16` = **45.0 exactly**
  - 2^30 = 1,073,741,824 → `>>16` = 16,384 → ×360 = 5,898,240 → `>>16` = **90.0 exactly**
  - 2^29 / 45 = 11,930,464.71… units per degree
  - 2^32 / 360 = 11,930,464.71… units per degree — **identical**, which is the proof the two
    statements describe one scale
  - (The library's integer `turnAngle1` truncates this to 11,930,464.)
- **The payoff line:** a `uint32_t` holds exactly 2^32 values and then rolls to zero — which is what
  an angle does. The overflow is the feature: 360° wraps to 0 (correct), −10° wraps to just under
  the top (correct). Free exact angle-wrapping with no `if`, no modulo, nobody's code. Choosing the
  unit well made a class of bug impossible to write.

---

# L13 — Rescue Zone

Existing cards: 13.1 Medium/Deep · 13.2 Tough/Light · 13.3 Hard/Moderate
Available kinds: `b1_corkscrew b2_unspent b3_stripes b4_door c1_sweep c2_report c3_rowzero
cal_7a–cal_7e finished step_1–step_5`

## L13 C4 — The Clamp, With Your Numbers
- **Marker:** `13.4` · **format:** prose (notebook-only) · **tiers:** Easy / Deep
- **Source prose:** §8A.1 "The Clamp, With Numbers."
- **What the card asks:** rerun §8A.1's arithmetic with the student's **own** numbers from the 7A
  Surface Meter — their calibration min, their calibration max, their measured silver raw reading —
  and show what the library's calibrated channel does to it. Then set their own `SILVER_RAW_MAX`
  and justify the placement.
- **VERIFIED — the lesson's worked example is arithmetically correct:**
  cal min 400 (white, raw), cal max 2400 (black tape), silver reads raw 250.
  x = (250 − 400) × 1000 / 2000 = −150,000 / 2000 = **−75**. Then `if (x < 0) x = 0` fires.
- **The point:** the subtraction knew (−75 carries "brighter than anything you showed me"); the
  clamp forgot. White floor also computes to 0, so on the calibrated channel silver and white are
  indistinguishable. On the raw channel they were 250 and 400 — a gulf you can drive a threshold
  through, which is exactly what `SILVER_RAW_MAX` is for.
- **CONFLICT CHECK — this card is clear, but a neighbouring one is not.** A "measure your surfaces"
  card is **not available** for L13: §5.3 "Four Blanks, Four Measurements" already requires the
  student to fill `SILVER_RAW_MAX`, `WALL_STOP_COUNT`, `ROW_STEP_CM` and `VICTIM_SHORT_CM` from
  7A's measurements as part of the main build. A card asking for the same measurements would
  duplicate the build. C4 above survives because it asks for the *arithmetic and the reasoning*,
  not the data collection.

## L13 C5 — What Would See the Black Ball?
- **Marker:** `13.5` · **format:** prose (notebook-only) · **tiers:** Easy / Deep
- **Source prose:** §8A.3 "What Would See the Black Ball?"
- **What the card asks:** the prox fails on the black ball because it measures reflected infrared
  and the ball's job is to absorb exactly that. Given that, evaluate the alternatives on cost,
  wiring, and what each would actually buy: camera (sees ambient light, so a black ball on a light
  floor is high-contrast — this is *why* real rescue robots carry cameras), time-of-flight (times a
  laser pulse rather than counting reflected intensity, less fooled by colour, though dark targets
  still shorten range), whisker/bumper (honest, cheap, finds the victim by running it over).
  Then: what would carrying a victim out actually require, and why can't this robot do it?
  (Answer: gripper + servo + a driver channel to spare — and both DRV8838 drivers are already
  committed, one per tread.)
- **Feeds:** TDP §8 "Version 2 — If I Built the Next One," which demands improvements justified by
  reasoning rather than "I'd make it cooler."
- **HONEST WEAKNESS:** this is the weakest of the six. It's prose reasoning with no number in it,
  and the book's card canon leans on measured or computed evidence. If only one L13 card is ever
  built, build C4.

---

# L14 — Competition Prep

Existing cards: 14.1 Medium/Moderate · 14.2 Medium/Deep · 14.3 Hard/Moderate
Available kinds: `b1_alwayspass b2_loose b3_zero b4_kill c1_wheeltest c2_strict c3_lop
cal_7a–cal_7e finished step_1–step_3`

## L14 C4 — Your Reliability Number
- **Marker:** `14.4` · **format:** prose (measurement + arithmetic) · **tiers:** Medium / Deep
- **Rides:** `cal_7d` (existing — no new payload)
- **Source prose:** §3.1 "The Reliability Equation" + §7D "The Full Ritual, Ten Times."
  §7D already prescribes ten consecutive boot→self-test→calibrate→full-course runs with a tally of
  clean runs, LoPs and failures, plus what the self-test said before each.
- **What the card adds:** §3.1 runs the math **forward** (assume 90% per behaviour, get 35% overall).
  The card runs it **backward** from the student's own tally: if you completed c of 10 runs, your
  observed course success is p = c/10, and your implied per-behaviour reliability across 10
  behaviours is r = p^(1/10). Compare r against the 99% that §3.1 says a 90% course demands.
- **VERIFIED ARITHMETIC** (the lesson's own figures check out, and the worked examples are computed):
  - 0.9^10 = 0.34867844… — lesson's **0.35 is correct**
  - 0.9^(1/10) = 0.98953… — lesson's **"about 99%" is correct**
  - Worked example for the card, 7 of 10 clean: p = 0.7 → r = 0.7^(1/10) = **0.9650**, i.e. ~96.5%
    per behaviour. Feels excellent. Produces a robot that finishes the course 7 times in 10.
  - 9 of 10 clean: p = 0.9 → r = **0.98953**, ~99% per behaviour.
  - The gut-punch the card is built around: the difference between a 96.5% behaviour and a 99%
    behaviour is 2.5 percentage points, and it is the difference between 7 runs and 9.
- **Ties to:** §8.4's intermittent-failure hunt. §7D already says nine-for-ten means that hunt
  starts a week early, with data — this card is what turns the tally into the data.

## L14 C5 — The Clock
- **Marker:** `14.5` · **format:** prose (procedure drill) · **tiers:** Medium / Moderate
- **Rides:** `cal_7e` (existing — no new payload)
- **Source prose:** §7E "The Clock." Set a timer for the inter-match interval the competition
  allows (five minutes typical) and run the whole pit cycle against it: battery swap, boot,
  self-test, calibration, robot staged at the start line, hands off. Then repeat with a planted
  surprise — a teammate covers one line sensor with a finger of tape, so the clock is running and
  the self-test says LINE FAIL. Practice the failure, not just the success.
- **Ties to:** §3.4's champion's-mindset material and §8's morning routine — boring under pressure.
- **BLOCKER IF BUILT — timer canon.** This card involves a five-minute clock, and the standing queue
  carries a rule that a timer is an **IFRAME (`timer.html`), not a text label**. If this card ships
  it must embed the real timer with proper params and a lesson-unique label, or be written so the
  student uses their own external clock and no timed construct appears in the card at all. The
  book_gates timer gate will catch a text-label fake. This was flagged and never ruled.

---

## Open items this thread surfaced (logged, not lost)

1. **L12–L14 remain at N=3** against a book running N=5–11. Real, just not this session's job.
2. **L16 has zero challenge cards** — the only zero in the book. Reads as deliberate (the whole
   lesson is the capstone) but was never ruled, and any count-based audit will trip on it.
3. **The L11 precedent.** S66 took the Job A trade at L11 — N 3→5, doing 2.33→2.00 — which is why
   L11 now shows as a dip between L10 (2.60) and L12 (2.67). If Job B holds, that dip is a known
   cost of a good decision, not a defect to fix by removing L11's new cards.

---
*Written S67, Jul 24 2026. Six proposals, verified and shelved. No book file was modified.*
