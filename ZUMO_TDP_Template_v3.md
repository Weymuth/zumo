# Technical Description Paper — [YOUR NAME]
### RoboCupJunior Rescue Line · Mercersburg Academy Robotics

> **This document is your engineering notebook AND your competition TDP — they are the same thing.** Do not start a separate paper at the end. Add each lesson's Engineer's Log entry to the marked section when you finish the lesson. By Lesson 16, the paper is written; you only need to assemble it and add the Abstract.
>
> Make **one copy** (File → Make a copy), add your name and the date to every entry, and keep it in your own Drive all semester.
>
> Target 5–10 pages. **No source code** — use diagrams and prose. The TDP is weighted more than the video and poster combined (RCJ Rescue Line 2026 §6 scores the rubrics at TDP 0.6, video 0.2, poster 0.2). **Official RoboCupJunior rule:** §7.3 requires all three documents, and §7.3.4 scores a TDP **0** if it does not strictly follow the official template. This outline is the RoboLore class version; rebuild the same content inside the official template if you submit to a real event. Judges reward **graphics, tables, and measured data** over adjectives; the running tables below give you that evidence.

---

# PART A — STANDING LOGS
*Add to these all semester. They supply evidence for the hardest-to-fake TDP sections, and A5 is graded on its own.*

## A1. Hats I Wore
*You are a team of one. Record each new kind of engineering work you do.*

| Date | What I worked on (mechanical / sensors / code / calibration / documentation) |
|---|---|
| | |
| | |

## A2. Improvement Ideas — one line every lesson
*End each lesson with one sentence: what would you improve next? In Lesson 16, choose your Showcase enhancement from this list.*

| Lesson | "After today, I'd improve…" |
|---|---|
| L01 | |
| L02 | |
| L03 | |
| L04 | |
| L05 | |
| L06 | |
| L07 | |
| L08 | |
| L09 | |
| L10 | |
| L11 | |
| L12 | |
| L13 | |
| L14 | |
| L15 | |

## A3. Failure Log
*Log every failure. Record what broke, what you learned, and how you responded. This becomes your “Lessons Learned” evidence.*

| Date | What broke | What I learned / how I fixed it |
|---|---|---|
| | | |
| | | |

## A4. Measured Data — fill the cells as you go
*Record measurements when you take them. A value left on the OLED disappears; a value entered here can become a chart.*

**Calibration (L04)**

| | Value | Room / lighting |
|---|---|---|
| Minimum | | |
| Maximum | | |

**Distance calibration (L06)**

| | Value |
|---|---|
| Wheel diameter (mm) | |
| Derived COUNTS_PER_CM | |
| Commanded 30 cm → measured | |
| Agree? (Y/N + gap) | |

**Track-width tuning (L06 / L07)** — *the book ships 98 mm; tune it.* This is not a dimension you measure. A tracked robot skids when it pivots, so no ruler reading predicts the turn. Command four 90° turns, see whether the robot faces home, and nudge the constant until it does.

| | Value |
|---|---|
| Shipped default (TRACK_WIDTH_MM) | 98.0 |
| Four-turn heading error (°) | |
| My tuned TRACK_WIDTH_MM | |
| Surface I tuned on | |

**P-control gain search (L08)**

| Kp tried | Result (too slow / oscillates / good) |
|---|---|
| | |
| | |

**Encoder vs. Gyro (L12)** — turn 90°, record both, on two surfaces

| Surface | Encoder said | Gyro said | Which I trust |
|---|---|---|---|
| Carpet | | | |
| Slick floor | | | |

**PID tuning bench (L15)** — four gain sets, three scores each

| Gain set (Kp / Ki / Kd) | MAE | PEAK | WEAVE |
|---|---|---|---|
| | | | |
| | | | |
| | | | |
| | | | |

**Baseline vs. Enhanced (L16)**

| Run | Score | Notes |
|---|---|---|
| Baseline | | |
| Enhanced | | |
| Delta | | |

## A5. Lab Log — every session outside of class
*This table **is** your Outside Work grade (5%). Add one row per session with your arrival time, departure time, and the specific task you worked on. “Worked on robot” is too vague — name the thing. A log with 14 specific rows is worth more than a log with 40 vague ones, and it is the only proof you did the hours.*

*The lab is open Monday–Thursday evenings; free periods count too. Log both the same way.*

| Date | In | Out | What I worked on |
|---|---|---|---|
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |

*Running total of outside hours: ______*

> **Why this belongs in the TDP.** Judges and graders want evidence that the work is yours. A dated log provides it. It also preserves the sessions and failures worth discussing in **Lessons Learned**.

---

# PART B — THE TDP
*Each section names the log entry that feeds it. The full prompt remains in the lesson.*

## Abstract
*(150–250 words. Write this LAST in Lesson 16, after the rest of the paper is complete. Then summarize what you actually built, tested, and learned.)*

> _[Lesson 16 — leave blank until the end]_

---

## 1. Introduction — Robot & Author
*Introduce yourself, the robot, and its starting condition. Use A1 to show the range of work you completed.*

**Feeds from → Engineer's Log #01 (Lesson 1):**
> Write the dated “before” paragraph: the board, processor, installed hardware, and what the robot can do today. Write the “after” in L16. The difference between them becomes the basis of your Abstract.

> _[L01 entry — do NOT edit later]_

---

## 2. Project Planning
*Define your MVP, show your schedule, and explain the tradeoffs that shaped the project.*

**Feeds from → Log #05 (L5) + #10 (L10):**

**The shared-pin tradeoff (L05):**
> Five line sensors OR three proximity sensors — pins 20 and 4 are shared. State the constraint and defend your choice.
> _[L05 entry]_

**What the obstacle maneuver costs (L10):**
> Every capability costs time, distance, or risk. Name the cost of yours. (Obstacle = 20 points.)
> _[L10 entry]_

**My four-week plan / MVP:**
> _[your own]_

---

## 3. Hardware
*Document the preconfigured Pololu Zumo 32U4 you actually used. Describe the platform honestly rather than implying that you built it from scratch.*

**Feeds from → Log #02 (L2) + #03 (L3) + #06 (L6):**

**Labeled board figure (L02):**
> Label every sensor and actuator on one page. Include no source code.
> _[embed your L02 drawing]_

**Your TRIM number and why it exists (L03):**
> Record your TRIM number and explain what is physically different between the two motors.
> _[L03 entry]_

**COUNTS_PER_CM — derived and verified (L06):**
> Show wheel diameter → circumference → counts/rev → counts/cm. Then compare the commanded 30 cm with the measured result from A4.
> _[L06 entry]_

**Track width — tune, don't measure (L06/L07):**
> Report your tuned `TRACK_WIDTH_MM` from A4 and the surface you tuned it on. Explain why it sits above the 98 mm the book ships. *A constant you tuned against the robot's behavior is evidence; a dimension you read off a ruler predicts nothing on tracks.*
> _[your tuning record]_

---

## 4. Software
*Show the 8-file architecture as a diagram, not a source dump. Explain your enhancement, its byte cost, and what you removed to make room for it.*

**Feeds from → Log #07 (L7) + #08 (L8) + #09 (L9) + #13 (L13):**

**Eight-file architecture diagram (L07):**
> Show which file owns each responsibility and which files call one another. Include no source code.
> _[embed your L07 diagram]_

**P-control in plain English (L08):**
> Explain P-control without equations first. Then report your Kp and how the A4 tests led you to it.
> _[L08 entry]_

**State machine diagram (L09):**
> Draw states as boxes and transitions as labeled arrows on one page.
> _[embed your L09 diagram]_

**How the robot knows (L13):**
> Explain how the robot decides that it is in the zone, has found a victim, or is finished. Include your false-victim threshold and the behavior on both sides of it.
> _[L13 entry]_

**Your enhancement (L16 Showcase):**
> Choose one idea from A2. Explain what it does, its byte cost, and what you removed to afford it.
> _[Lesson 16]_

---

## 5. Performance Evaluation
*Compare the baseline and enhanced runs with the same instrument. Explain what the change means and how the results changed the robot. Use A4 data and charts.*

**Feeds from → Log #04 (L4) + #12 (L12) + #15 (L15):**

**Calibration min/max (L04):**
> Report the A4 values, explain what calibration changes, and explain why the values change in another room (RCJ 3.11: venue lighting ≠ home).
> _[L04 entry]_

**Encoder vs. gyro (L12):**
> Use the A4 carpet-versus-slick results. State which measurement you trust in each condition and why.
> _[L12 entry]_

**PID tuning bench (L15):**
> Present the four gain sets and their MAE, PEAK, and WEAVE scores from A4. Explain what you tried, what you kept, and why you stopped.
> _[L15 entry — this IS your performance-evaluation method]_

---

## 6. Lessons Learned
*Choose failures from A3 and explain what each one taught you.*

**Feeds from → Log #11 (L11) + your A3 log:**

**The battery failure (L11):**
> Describe a maneuver that worked with a fresh battery and failed with a tired one. Explain what replaced it and why the replacement is immune.
> _[L11 entry]_

**Other documented failures:**
> _[pull the best ones from A3]_

---

## 7. Competition Deliverables
*Include the items required for a real event.*

**Feeds from → Log #14 (L14):**

**LoP procedure + self-test card (L14):**
> RCJ rule §4.2.8 (RCJ Rescue Line 2026) requires you to tell the referee your Lack-of-Progress procedure before each scoring run. Write that procedure here.
> _[L14 entry]_

---

## 8. Version 2 — If I Built the Next One
*Propose two or three improvements. Support each one with data or a documented failure from A2, A3, Section 5, or Section 6.*

**Feeds from → Log #16 (L16):**
> _[write in L16, each item citing a number from Part A or Section 5–6]_

---

## Assembly checklist (Lesson 16)
- [ ] All 15 prior log entries pasted into their sections
- [ ] L01 "before" and L16 "after" both present and unedited
- [ ] Every diagram is a drawing — **zero source code**
- [ ] A4 data tables filled and turned into charts
- [ ] A5 Lab Log has a row for every outside session, with a running total
- [ ] Delta row filled in Performance Evaluation
- [ ] Lessons Learned discusses what did NOT work (from A3)
- [ ] Version 2 items each cite a number (from A2)
- [ ] Abstract written LAST, 150–250 words
- [ ] 5–10 pages total
- [ ] **Poster** distilled from this paper — the graded deliverable rides with the TDP

---
*Mercersburg Academy Robotics · Zumo 32U4 curriculum · TDP template derived from the 16 Engineer's Log prompts. v3.3.0 — A4's wheel-base VERIFICATION replaced by a TRACK_WIDTH_MM tuning record: students no longer measure this constant, because a tracked robot skids when it pivots and no ruler reading predicts the turn (DJ ruling, S189).*
