# Teacher Daily Planning Grid — Zumo, Fall Trimester
### One row per class period · ~23 periods + 3 buffers · Mr. Weymuth
<!-- ZUMO_Teacher_Daily_Grid_WORKING.md v1.0 — S97, Jul 30 2026 -->

> **Working draft in RELATIVE time.** Periods are numbered, not dated — pin real dates once the class schedule is set (class meets 3×/week one week, 2× the next). **Blocked until ~Aug 24.**
>
> **Fall ends at the silver line.** The trimester runs L01 through **Lesson 13, Step 3** — the robot drives the full course and stops at the edge of the rescue zone. It does not go inside. L13 Steps 4–6 (the sweep, the victim, the witness), L13's challenges, its Mysteries, and its Engineer's Log all open Winter.
>
> Legend: **Flip** = read + reading-quiz before class · **Key Concept** = the core idea that period teaches (your bell-ringer + live-demo target) · **Task** = the in-class build focus · **⭐** = live concept demo at open · **DEMO** = milestone check-off day (video or live) · **S** rows are unassigned safety/buffer periods.

| Pd | Wk | Flip (read before class) | Key Concept(s) | In-Class Task | Milestone / Countdown |
|----|----|--------------------------|----------------|---------------|------------------------|
| 1  | 1  | *(none — first day)* | How this class works | **Handout day:** distribute Zumos, syllabus, USB cords, jumpers; Canvas + Maker walkthrough; make TDP notebook copy; PlatformIO check | M1 in 2 |
| 2  | 1  | L01 Hello, Robot! | Upload/compile cycle; the robot as a computer | Build + upload first program; L02 read-code intro | M1 in 1 |
| 3  | 1  | L02 Read Code / L03 Motors ⭐ | TRIM; no two motors are the same; open-loop driving | TRIM: drive straight + measured distance | **M1 DEMO** (straight + measured) |
| 4  | 2  | L03 Motors & TRIM | setSpeeds; TRIM polarity; delay vs. distance | Finish TRIM tuning; catch-up buffer for M1 stragglers | M2 in 2 |
| 5  | 2  | L04 Line Sensors | Reflectance sensing; calibration; the sensor measures, it doesn't see | Calibrate line sensors; live sensor readout | M2 in 1 |
| 6  | 2  | L05 Proximity Sensors | IR proximity; the shared-pin tradeoff; 5-sensor jumper config | Proximity + the 5-sensor jumper move | **M2 DEMO** (calibrate + live values) |
| 7  | 3  | L06 Encoders ⭐ | Encoders count rotation; COUNTS_PER_CM derivation | counts/cm derivation; drive an accurate 30 cm | M3a in 1 |
| 8  | 3  | L06 Encoders (cont.) | Averaging both wheels; deriving wheel-base from turn error | Close a square; verify wheel-base (four-turn test) | **M3a DEMO** (30 cm + square) |
| S1 | 3  | *(buffer)* | — | Safety period — re-teach counts/cm / catch up | M3b in 4 |
| 9  | 4  | L07 Code Organization ⭐ | Why one program becomes 8 files; headers vs. source; extern | 8-file architecture; split the project | M3b in 3 |
| 10 | 4  | L07 (cont.) | The architectural contract; compiling a multi-file project | Wire the files together; project compiles clean | M3b in 2 |
| 11 | 4  | L08 Line Following ⭐ | Proportional control; why bang-bang fails; the P term | P-control; robot follows a line | M3b in 1 |
| 12 | 5  | L08 (cont.) | Tuning Kp; closed-loop control vs. open-loop | Tune Kp; follow a full course | **M3b DEMO** (follows line) |
| 13 | 5  | L09 Intersections ⭐ | State machines; states as boxes, transitions as arrows | State machine; handle a T / turn | M4 in 1 |
| 14 | 5  | L09 (cont.) | Dead ends; the kill switch; turnDegrees wrappers | Dead ends + kill switch; full decision logic | **M4 DEMO** (T / turn / dead end) |
| S2 | 6  | *(buffer)* | — | Safety period — M3b/M4 are the tight stretch | M5 in 4 |
| 15 | 6  | L10 Obstacles | Front-prox only under 5-down; priority arbitration | Front-prox obstacle avoidance | M5 in 3 |
| 16 | 6  | L10 (cont.) / L11 Gaps | Integrating behaviors; time vs. distance for blindness | Integrate avoidance; begin gap crossing | M5 in 2 |
| 17 | 7  | L11 Time Lies, Distance Doesn't | The odometer, not the stopwatch; measuring in cm | Encoder-based gap crossing (odometer) | M5 in 1 |
| 18 | 7  | L11 (cont.) | Battery-independent behavior; why time lies on a tired battery | Full course: line + intersection + obstacle + gap | **M5 DEMO** (obstacle + gap) |
| 19 | 7  | L12 Wheels Lie (Gyro) ⭐ | The gyro measures the robot, not the wheels; heading vs. encoders | IMU object; the four gyro functions; gyro heading | M6 in 4 |
| 20 | 8  | L12 (cont.) | The honest turn; the zero is a lie — calibrate at boot | The honest turn; switch the turns; calibrate at boot | M6 in 3 |
| 21 | 8  | L13 Rescue Zone §1–§4 | **Silver is invisible to `readCalibrated()`** — calibration clamps it to the same 0 as plain white; to see outside the calibrated world you drop to the raw channel | L13 Step 1 (the numbers, the names, the reasons) + Step 2 (`silverDetected()` — the doorman) | M6 in 2 |
| 22 | 8  | L13 (cont.) | Wiring a new sensor question into an existing state machine | L13 Step 3 (wire the door); full course run stopping at the silver line | M6 in 1 |
| 23 | 9  | *(none — assemble)* | The full run; TDP assembly | Full run + stop at silver; TDP assembly push | **M6 DEMO** (full run, stop at zone edge) |
| S3 | 9  | *(buffer)* | — | Safety period — final catch-up / re-demos / notebook | — |

---

## What changed from the previous draft

**1. The old Pd 20 taught the wrong lesson.** It read *"L12 (cont.) — Silver-strip detection; the calibrated-scale clamp."* Both belong to **Lesson 13**, not Lesson 12. L12 contains the word "silver" zero times; its §3–§5 are gyro end to end. L13 holds `7B — The Silver Brake` and `8A.1 The Clamp, With Numbers` — the old grid's phrase verbatim. Pd 20 is now genuine L12 continuation (the honest turn, boot calibration).

**2. Fall now runs through Lesson 13, Step 3.** M6 as the syllabus defines it — *"run the full course and stop at the rescue zone"* — requires `silverDetected()`, which is L13 Step 2. The old grid ended at L12 and could not deliver its own last milestone. **No syllabus edit is needed**: its M6 wording already describes stopping *at* the zone, not entering it.

**3. Two periods for L13, not four.** L13 Steps 1–3 measure **191 lines** of build; Lesson 11's *entire* build is 188 lines and already gets two periods. Same lesson shape, too — both open by copying the previous project and editing it. Measured with `lesson_inventory.build()` section boundaries, not by searching.

**4. 21 periods → 23.** L12 keeps its two, L13 takes two, assembly/demo keeps one. All three buffers survive.

**5. The countdown column was recomputed.** The old one disagreed with its own demo rows in several places (S1 read "M3b in ~2" with the M3b demo four periods later). **Convention now stated: the countdown counts every scheduled meeting, buffers included, and the "~" is dropped** — these are exact period counts in relative time. They become approximate again only when you pin real dates and the 3×/2× alternation shifts them.

---

## Notes on this grid

- **~23 periods + 3 buffers.** If the term runs short, S1–S3 are the first thing to cut; if it runs long, they absorb slippage. Don't plan to *spend* them — plan to have them.
- **The L13 reading splits at §5.** Fall assigns **§1–§4**. Section 5.1 introduces `driveUntil()`, a primitive built for the sweep, and 5.2–5.3 are the lawnmower sweep itself — all Winter material. Don't assign the whole lesson in Pd 21.
- **Winter opens mid-lesson, on purpose.** It picks up at L13 Step 4 (the Watchful Leg) with the robot already parked at the silver line. Nothing in the book or the 35 gates governs a lesson split across terms — this is a calendar seam, not a book seam, and requires no file change.
- **Every non-buffer row assumes the flip happened** — the reading quiz gated entry, so in-class time is build time. The bell-ringer (first ~5–10 min) isn't a column because it happens *every* row; it's driven by that day's quiz results.
- **The tight stretch is periods 9–14 (M3b + M4).** Two heavy lessons (L07, L08) plus the state machine, squeezed into weeks 4–5. S2 sits right after on purpose. Watch this in the first run.
- **Exit ticket + one notebook line close every build period** — also not a column because it's universal.

---

## Still To Add _[working notes — not student-facing]_
- **Pin to real dates** — blocked until ~Aug 24 (which weekdays, and where the 3×/2× alternation lands)
- **⭐ heavy-lesson list needs a ruling.** It currently reads L03, L06, L07, L08, L09, L12 — carried forward unchanged from the previous draft. **L13 is now a Fall lesson and carries a genuinely counter-intuitive idea** (a sensor reading of 0 that means "too bright" rather than "white"), which is the profile of every other ⭐ lesson. It is deliberately left unmarked pending your call.
- Whether Pd 23 needs a partner period for M6 re-demos, or S3 covers it

---
*Working draft · relative time · pin to real dates when the schedule is set · Fall Trimester · Zumo 32U4 · v1.0*
