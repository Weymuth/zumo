# Technical Description Paper — [YOUR NAME]
### RoboCupJunior Rescue Line · Mercersburg Academy Robotics

> **This document is your engineering notebook AND your competition TDP — they are the same thing.** Do not start a separate paper at the end. Each lesson's Engineer's Log entry drops into the section marked for it. Fill your section the week you finish that lesson; by Lesson 16 the paper is written and you only assemble it and add the Abstract.
>
> Make **one copy** (File → Make a copy), put your name and the date on every entry, keep it in your own Drive all semester.
>
> Target 5–10 pages. **No source code** — diagrams and prose only. The TDP is weighted more than the video and the poster combined. Judges reward **graphics, tables, and real measured data** over adjectives — that is what the running tables below are for.

---

# PART A — STANDING LOGS
*Add to these all semester, not just once. They feed the hardest-to-fake TDP sections.*

## A1. Hats I Wore
*You are a team of one, so document the different KINDS of engineering work you did. Add a line whenever you do something new.*

| Date | What I worked on (mechanical / sensors / code / calibration / documentation) |
|---|---|
| | |
| | |

## A2. Improvement Ideas — one line every lesson
*End of each lesson, one sentence: what would you improve after today? By Lesson 16 you pick your Showcase enhancement from this list — and every idea already has a reason behind it.*

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
*Every time something breaks, log it. Hiding failures reads as inexperience; documenting them reads as an engineer. This feeds "Lessons Learned."*

| Date | What broke | What I learned / how I fixed it |
|---|---|---|
| | | |
| | | |

## A4. Measured Data — fill the cells as you go
*These are the numbers your robot shows on the OLED. Read them ONCE and they're gone; write them here and they become your charts. Judges love real data.*

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

**Wheel-base verify (L06 / L07)** — *the book gives you 85 mm; check it.* Command four 90° turns and see if the robot faces home. If it doesn't, back-calculate your true wheel-base from the heading error.

| | Value |
|---|---|
| Book value (WHEEL_BASE_MM) | 85.0 |
| Four-turn heading error (°) | |
| My calculated wheel-base (mm) | |
| Why 85 was close but not exact | |

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

---

# PART B — THE TDP
*Each section is filled by the log entry named under it. The prompt itself lives in the lesson — this just tells you where the entry goes.*

## Abstract
*(150–250 words. Write this LAST, in Lesson 16, with everything else in front of you. An abstract written first is a wish; written last it is a summary.)*

> _[Lesson 16 — leave blank until the end]_

---

## 1. Introduction — Robot & Author
*This is a solo project. Introduce yourself and the "before" state of the robot. (Your A1 "Hats I Wore" table shows the range of work you did.)*

**Feeds from → Engineer's Log #01 (Lesson 1):**
> The "before" paragraph — what board, what processor, what's on it, what it can do *today*. Dated. You'll write the "after" in L16; the gap between them is your Abstract.

> _[L01 entry — do NOT edit later]_

---

## 2. Project Planning
*Your MVP definition, your schedule, and the design tradeoffs you were forced to make.*

**Feeds from → Log #05 (L5) + #10 (L10):**

**The shared-pin tradeoff (L05):**
> Five line sensors OR three proximity sensors — pins 20 and 4 are shared. State the constraint, defend your choice. (The most TDP-shaped decision in the course.)
> _[L05 entry]_

**What the obstacle maneuver costs (L10):**
> Every capability has a price — seconds, distance, risk. Name yours. (Obstacle = 20 points.)
> _[L10 entry]_

**My four-week plan / MVP:**
> _[your own]_

---

## 3. Hardware
*A preconfigured Pololu Zumo 32U4. Document what you actually own — judges reward honesty about the platform over pretending you built one.*

**Feeds from → Log #02 (L2) + #03 (L3) + #06 (L6):**

**Labeled board figure (L02):**
> Every sensor and actuator, labeled, one page, no code.
> _[embed your L02 drawing]_

**Your TRIM number and why it exists (L03):**
> What's physically different between your two motors? The number, and why it isn't zero.
> _[L03 entry]_

**COUNTS_PER_CM — derived and verified (L06):**
> Wheel diameter → circumference → counts/rev → counts/cm. Then: did 30 cm come out 30 cm? (Pull the numbers from table A4.)
> _[L06 entry]_

**Wheel-base — check the book's number (L06/L07):**
> The book gives 85 mm. You verified it with the four-turn test (table A4). Report your calculated value and why 85 was close but not exact. *A number you checked is evidence; a number you were handed is a guess.*
> _[your verification]_

---

## 4. Software
*The 8-file architecture (draw it — NO source dumps) and your innovation: what it does, what it cost in bytes, what you removed to afford it.*

**Feeds from → Log #07 (L7) + #08 (L8) + #09 (L9) + #13 (L13):**

**Eight-file architecture diagram (L07):**
> Which file owns what, who calls whom. No source. Highest-value entry in the book.
> _[embed your L07 diagram]_

**P-control in plain English (L08):**
> Explain it with no equations first. Then your Kp and how you found it (table A4).
> _[L08 entry]_

**State machine diagram (L09):**
> States as boxes, transitions as labeled arrows, one page.
> _[embed your L09 diagram]_

**How the robot knows (L13):**
> How it knows it's in the zone / found a victim / is finished. Your false-victim threshold and what happens on either side.
> _[L13 entry]_

**Your enhancement (L16 Showcase):**
> Chosen from your A2 Improvement Ideas list. What it does, byte cost, what you removed to afford it.
> _[Lesson 16]_

---

## 5. Performance Evaluation
*Baseline row, enhanced row, same instrument, what the delta means. Explain how test results were analyzed and how they changed the robot. Use your A4 tables — this section is mostly charts.*

**Feeds from → Log #04 (L4) + #12 (L12) + #15 (L15):**

**Calibration min/max (L04):**
> The numbers (table A4), what calibration is, and why they change in a different room (RCJ 3.11: venue lighting ≠ home).
> _[L04 entry]_

**Encoder vs. gyro (L12):**
> Your carpet-vs-slick table (A4). Which do you trust, and when?
> _[L12 entry]_

**PID tuning bench (L15):**
> Your four gain sets and their MAE/PEAK/WEAVE (table A4). What you tried, what you kept, when you stopped and why.
> _[L15 entry — this IS your performance-evaluation method]_

---

## 6. Lessons Learned
*What failed and what the failure taught you. Draw straight from your A3 Failure Log.*

**Feeds from → Log #11 (L11) + your A3 log:**

**The battery failure (L11):**
> A maneuver that worked fresh and failed tired. What replaced it, and why the replacement is immune.
> _[L11 entry]_

**Other documented failures:**
> _[pull the best ones from A3]_

---

## 7. Competition Deliverables
*Rules-mandated. Not optional at a real event.*

**Feeds from → Log #14 (L14):**

**LoP procedure + self-test card (L14):**
> RCJ rule 4.3.7: you must tell the referee your Lack-of-Progress procedure before each scoring run. Write it here.
> _[L14 entry]_

---

## 8. Version 2 — If I Built the Next One
*Two or three improvements, each justified by your own data or failure log. "I'd add a compass because my dead reckoning drifted 4 cm per lap" is engineering. "I'd make it cooler" is not. Pull the best from your A2 Improvement Ideas.*

**Feeds from → Log #16 (L16):**
> _[write in L16, each item citing a number from Part A or Section 5–6]_

---

## Assembly checklist (Lesson 16)
- [ ] All 15 prior log entries pasted into their sections
- [ ] L01 "before" and L16 "after" both present and unedited
- [ ] Every diagram is a drawing — **zero source code**
- [ ] A4 data tables filled and turned into charts
- [ ] Delta row filled in Performance Evaluation
- [ ] Lessons Learned discusses what did NOT work (from A3)
- [ ] Version 2 items each cite a number (from A2)
- [ ] Abstract written LAST, 150–250 words
- [ ] 5–10 pages total

---
*Mercersburg Academy Robotics · Zumo 32U4 curriculum · TDP template derived from the 16 Engineer's Log prompts. v2.*
