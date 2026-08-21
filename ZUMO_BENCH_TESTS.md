# ZUMO — BENCH TEST TRACKER
### Everything in this book that only a robot and a floor can settle · one file, by lesson

**Bench tracker version: v1.2** — increment on every substantive edit
(moderate change → `v1.x`; minor → `v1.x.y`). The version lives ONLY in this line.

> **WHY THIS FILE EXISTS.** No instrument in this repo can see a floor. `book_gates` reads
> structure, `byte_audit` compiles, `gate_payload_match` derives — **not one of them can tell you
> whether the robot actually did the thing.** Bench items have been scattered across session
> handoffs since S40 and re-reported as open by every reader since (rule 72). This is their home.
>
> **HOW TO USE IT.** Work a lesson's block at the bench with the robot in front of you. Put the
> result in the **Result** column in your own words. **A number you measure goes in the book only
> after it is written here** — that is the whole point of the file.
>
> **STATUS LEGEND:** `OPEN` needs the robot · `PASS` behaved as the book says · `FAIL` did not,
> and the book owes a fix · `N/A` superseded or withdrawn.

---

## HOW TO RUN ANY FLOOR TEST — the ritual, once, here

This is the ritual Lesson 1 Challenge 4 now teaches. Everything in this file that involves the
robot moving under its own power uses it.

1. Rest the robot on a **stand or an overturned cup**, wheels clear of the bench.
2. Upload from there. Wait for **SUCCESS**.
3. **Close the Serial Monitor.** (Leave it open and the next upload fails *Resource busy*.)
4. **Unplug the USB cable.** Never pull it while an upload is running.
5. Switch the robot's power **ON**.
6. Set it down, hands clear, then press the button.

**You lose the Serial Monitor the moment you unplug.** Anything that needs Serial has to be run
tethered and propped, and cannot be a floor test. That trade is real from Lesson 11 onward.

---

# LESSON 01 — Sense, Decide, Act

**Whole-lesson pass requested by DJ (S177): L01 was rewritten this session and DJ is testing all
of it.** Ten findings closed, none of them bench-verified.

| # | What to check | Where | Status | Result |
|---|---|---|---|---|
| L01-B1 | **Unplug the cable, then click Upload. Write the error text down verbatim.** Unplug FIRST — this is an upload with no port, not an interrupted transfer. | §6 *Break It On Purpose* | **OPEN — ROUTED to `ZUMO_FLAGGED_CHECKS.md` F1 (S179, DJ will run)** | |
| L01-B2 | **The counter-check: cable IN, robot power OFF, upload.** | §6 | **CLOSED — DJ ruled S179** | **It succeeds. The cable powers the chip and the display; the power switch feeds the motors.** Seated as canon in Bible §16.48 so it stops being re-asked. |
| L01-B3 | **Challenge 4 on the floor.** Change the FIRST `delay(350)` to 700 only. Does the robot finish roughly one nudge **ahead** of where it started? | §9 C4 | **OPEN — ROUTED to `ZUMO_FLAGGED_CHECKS.md` F2 (S179, DJ will run)** | |
| L01-B4 | **Challenge 11's solution as printed** — `setLayout21x8()`, then voltage, 1.5 s, then the `< 4500` branch. Does the number read on the OLED before §6's setup reprints *Press A*? | §9 C11 | **OPEN — ROUTED to `ZUMO_FLAGGED_CHECKS.md` F3 (S179, DJ will run)** | |
| L01-B5 | **Challenge 9 propped up.** Delete the three-line wait. Does the show start the instant power comes on, with no button? | §9 C9 | OPEN | |
| L01-B6 | **Battery bands.** Read `readBatteryMillivolts()` on a fresh pack and a tired one. Book says ~5,400 fresh / ~4,800 working / ~4,200 low. | §9 C11 hint | OPEN | |
| L01-B7 | **Does USB alone really read low and strange?** The hint says so. Read the pack with the switch OFF and the cable in. | §9 C11 hint | OPEN | |
| L01-B8 | **First-connection behaviour on a Mac AND on Windows.** Book now says a chime, a dialog, or nothing are all normal. Confirm both machines. | §6 Step 4 | OPEN | |
| L01-B9 | **Git on a fresh Mac.** | §4.2 | **CLOSED — DJ ruled S179** | **Git is required on a Mac because asking for it triggers Apple's Command Line Tools installer, which is where the compiler lives.** NOT because PlatformIO fetches the Zumo library over git — it does not. Seated as canon in Bible §16.48; closes worklist row `L01-03`, open since S137. |
| L01-B10 | **Bootloader port change.** Does the robot really show one port running and a different one with the bootloader awake? | §8 | OPEN | |

---

# LESSON 02 — Read Code

| # | What to check | Where | Status | Result |
|---|---|---|---|---|
| L02-B1 | **The green LED bench check.** Carried since S41. | §5 | OPEN | |
| L02-B2 | **Challenge 2 screen overwrite — now a FALSIFIABLE PREDICTION, not a question.** S180 shipped a release-wait (`while (buttonA.isPressed() || buttonB.isPressed()) { }`) and derived the old behaviour from Pololu's own `PushbuttonStateMachine`, transcribed and run: **with the wait REMOVED, hold A and B and pass 1 draws BATTERY, pass 2 flashes ABOUT then CONTROLS, pass 3 onward is BATTERY again — so you should see ONE flash of the Controls screen and then the battery screen settle.** With the wait IN, no flash at all. **Run it both ways.** If the flash does not appear with the wait removed, the reasoning in §9 C2's *Why it takes two trips and not one* is wrong and the paragraph comes out. | §9 C2 | OPEN | |

---

# LESSON 03 — Motors & TRIM

| # | What to check | Where | Status | Result |
|---|---|---|---|---|
| L03-B1 | **How far does one TRIM test run actually go?** `TEST_DURATION` is 2000 ms at `BASE_SPEED` 200. Tape a start line, press B, measure. **The *6+ feet* figure is DELETED, not corrected** — DJ ruled S179 that students do not need that space, and rule 50 gives an underived number two fates. This row exists so the book can one day state a MEASURED distance instead of describing the run as *short*. | §4.4, §7 | OPEN | |
| L03-B3 | **Bonus Challenge 4 (Braking vs. Coasting) asks for *about 3 meters of clear floor and a catcher*.** That figure has no pedigree either, and unlike the TRIM run this one really is full speed (400) for 1.5 s each way. Measure it before ruling. The card already offers `delay(800)` as the short-floor escape, so nothing is blocked. | §9 Bonus 4 | OPEN (raised S179) | |
| L03-B2 | **What TRIM value does a real robot need?** Record yours, and the spread across the fleet. Feeds the TDP's *your TRIM number and why it exists*. | §5 | OPEN | |

---

# LESSON 04 — Line Sensors

| # | What to check | Where | Status | Result |
|---|---|---|---|---|
| L04-B1 | **Calibration min/max on the classroom floor.** Record the numbers and the room's lighting. Feeds TDP table A4. | §5 | OPEN | |
| L04-B2 | **The 600 threshold.** Book-wide canon is 600, with 500 taught as the midpoint. Does 600 separate your tape from your floor? | §8A | OPEN | |
| L04-B3 | **Learner-mode L04 build is BLOCKED on materials** — needs a white surface and **matte black electrical tape** (IR-absorbing; marker or print is unreliable). Carried since S51. | learner mode | OPEN | |
| L04-B4 | **The wave-test direction** and **Act Two's row-1 overflow** — both deliberately unasked in the quiz bank because they are open bench findings. | §7 | OPEN | |

---

# LESSON 05 — Proximity Sensors

| # | What to check | Where | Status | Result |
|---|---|---|---|---|
| L05-B1 | **The blind wedge.** Book says roughly 19°–72° off each side has nothing aimed into it. Put a box at 45° and confirm both side receivers read 0. Observation Experiment 3 was rewritten at S140 to demonstrate this. | §3.4a, Exp 3 | OPEN | |
| L05-B2 | **The 5-sensor jumper move.** Pin 20 → DN2 and pin 4 → DN4. Confirm the physical move and that software agrees. | §5 | OPEN | |

---

# LESSON 06 — Encoders

| # | What to check | Where | Status | Result |
|---|---|---|---|---|
| L06-B1 | **Q044 — the calibration spin, with a stopwatch.** Carried since S41. | | OPEN | |
| L06-B2 | **COUNTS_PER_CM derived vs. measured.** Command 30 cm; measure what you get. Feeds TDP table A4. | §5 | OPEN | |
| L06-B3 | **The wheel-base four-turn test.** Book gives 85 mm and asks the student to check it. **Nobody has ever run this on this fleet.** Back-calculate from the heading error. | §7D, TDP A4 | OPEN | |
| L06-B4 | **The 39 mm question (§16.10).** Is travel governed by the outer track surface or the track's pitch line? Both land inside §7's ±2 cm tolerance, so this is curiosity, not a defect. | §16.10 | OPEN | |
| L06-B5 | **Experiment 3's two drags.** Drag the LEFT track: the number moves. Drag the RIGHT: the heading bends and no encoder can see it. Rewritten at S141 — never run. | Exp 3 | OPEN | |

---

# LESSON 08 — Line Following

| # | What to check | Where | Status | Result |
|---|---|---|---|---|
| L08-B1 | **The Kp range.** Canon is 0.1–0.3 starting at 0.10, ruled for the 75:1 fleet. Find yours; record what oscillates and what is too slow. Feeds TDP A4. | §7.3 | OPEN | |
| L08-B2 | **Challenge 5's three adaptive gains** (0.10 / 0.20 / 0.30) moved with the range at S142 and have never been driven. | §9 C5 | OPEN | |

---

# LESSON 09 — Intersections

| # | What to check | Where | Status | Result |
|---|---|---|---|---|
| L09-B1 | **Q017 — the green-tape six numbers.** Carried since S41. The single oldest open bench item in the project. | §7 | OPEN | |

---

# LESSON 10 — Obstacles

| # | What to check | Where | Status | Result |
|---|---|---|---|---|
| L10-B1 | **THE BIG ONE (§16.12, unruled since S143).** The rebuilt seven-phase box arrives at the line **perpendicular**, and there is no realigning turn anywhere in the tree. Prediction: the robot crosses the line and drives off the far side. **Watch the two seconds after `SEEKING` flips to `FOLLOWING`.** | §3.3, §7.7 | OPEN | |
| L10-B2 | **Challenge 6's wedge** meets the line at 30°, which a P-controller can pull out of. Run both and compare. **If the wedge works and the box does not, that is the ruling.** | §9 C6 | OPEN | |
| L10-B3 | **`AVOID_OUT_CM = 15.0`** and the 20 cm along / 15 cm out finishing pose — simulated at S143, never driven. | §3.3 | OPEN | |

---

# LESSON 11 — Gaps

| # | What to check | Where | Status | Result |
|---|---|---|---|---|
| L11-B1 | **The cliff reads BLACK (§16.14).** Three readings, same run: white mat, black tape, **open air**. Rows two and three should agree at ~1000. This is the ONE-MINUTE EXPERIMENT that replaced the old arithmetic at S144. | §8A.4 | OPEN | |
| L11-B2 | **Constrain RUN_MS.** Carried since S52. | | OPEN | |
| L11-B3 | **The battery failure.** A maneuver that works on a fresh pack and fails on a tired one — the whole thesis of the lesson, and the TDP's *Lessons Learned* entry. | §3 | OPEN | |
| L11-B4 | **Challenge 4 "Prove Your TRIM."** Book predicts a symmetric result from doubling TRIM. GPT (`L11-13`) says plausible but not guaranteed. **Treat it as a prediction to test — an unexpected result is data.** | §9 C4 | OPEN | |

---

# LESSON 12 — Gyro

| # | What to check | Where | Status | Result |
|---|---|---|---|---|
| L12-B1 | **Q046 — the gyro bias measurement.** Carried since S41. | | OPEN | |
| L12-B2 | **Encoder vs. gyro on two surfaces.** Turn 90°, record both, on carpet and on a slick floor. Feeds TDP table A4 directly. | §8A | OPEN | |
| L12-B3 | **BONUS B4's measurement.** The sabotage keeps the angle right and makes the robot **arc instead of pivot**, walking out of position. **The DISPLACEMENT MAGNITUDE is deliberately not stated in the book** (DJ, S162) — direction is derivable, magnitude is a bench number. Measure it or leave it unstated. | §9 B4 | OPEN | |

---

# LESSON 13 — Rescue Zone

| # | What to check | Where | Status | Result |
|---|---|---|---|---|
| L13-B1 | **Every §7A measurement.** The 7A table ships BLANK on purpose — no raw reading and no prox count has ever been taken on this fleet, and the quiz bank names them as deliberately unasked. | §7A | OPEN | |
| L13-B2 | **The false-victim threshold.** `VICTIM_SHORT_CM = 2` — §7D makes the student manufacture a false victim on purpose. Confirm both failure directions. | §7D | OPEN | |
| L13-B3 | **Step 6b, the blind corner.** Does the sweep now END rather than walking into the wall? Shipped S168, never driven. | Step 6b | OPEN | |
| L13-B4 | **`SWEEP_DONE` is escapable.** Fixed at S171 — press B in `SWEEP_DONE` and confirm the robot returns to `STOPPED` instead of needing the power switch. | §5 | OPEN | |

---

# LESSON 14 — Competition Day

| # | What to check | Where | Status | Result |
|---|---|---|---|---|
| L14-B1 | **`COMPETITION_MODE` guards the calibration motor calls** (RCJ §5.3.6 — a robot may not move while calibrating). Confirm the robot is genuinely still in match mode. | §5.2 | OPEN | |
| L14-B2 | **`selfTest()` end to end** against a real low pack. Book judges against `BATTERY_LOW` = 4200. | §4.3 | OPEN | |

---

# LESSON 15 — PID

| # | What to check | Where | Status | Result |
|---|---|---|---|---|
| L15-B1 | **The PID tuning bench** — four gain sets, three scores each (MAE / PEAK / WEAVE). This IS the TDP's performance-evaluation method; table A4 is built for it. | §7 | OPEN | |
| L15-B2 | **Challenge 3's `turnDegreesGyroSafe()`.** Carried forward unrun. | §9 C3 | OPEN | |
| L15-B3 | **The doorway derivative reset (`L15-03`, GPT, AGREE-must-fix).** Prose says the doorway makes re-entry flinch impossible; the code does not guarantee it. **Does the robot flinch?** | §5 | OPEN | |
| L15-B4 | **The hill climb's fixed ±50% steps** can stop far from a good setting (`L15-18`). Does it converge on your floor? | §7 | OPEN | |

---

# LESSON 16 — Showcase

| # | What to check | Where | Status | Result |
|---|---|---|---|---|
| L16-B1 | **Baseline vs. enhanced, same instrument, three runs each.** The delta row in the TDP is the deliverable. | §7 | OPEN | |
| L16-B2 | **The ten-percent benchmark spread** — (slowest − fastest) ÷ fastest. Ours, not the rulebook's. Does a real fleet hit it? | §7 | OPEN | |
| L16-B3 | **`16/after_step_2` is the tightest passing build in the book at 28,648 — 24 bytes spare.** It compiles. **Confirm it FLASHES and RUNS.** | §6 | OPEN | |

---

# NOT A BENCH ITEM — recorded so it stops being re-raised

- **PlatformIO is NOT installed in the container** and `pio_harness.sh` is a misnomer running raw
  `avr-gcc`/`avr-g++`. Anything needing a real PlatformIO run is a bench item by construction.
- **The compile harness reproduces all eight standing byte controls**, so byte figures are NOT
  bench items. They are measured, and re-measured every session that moves a payload.
- **Photography is OFF the critical path** (S156). Shot-list items live in `IMAGE_SHOT_LIST.md`.

---
*Bench tracker · created S177 · one row per thing only the floor can answer*
