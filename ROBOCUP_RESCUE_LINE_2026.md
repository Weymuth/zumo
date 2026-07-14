# RoboCupJunior Rescue Line — 2026 Rules Reference

**Source:** RoboCupJunior Rescue Line Rules 2026, official English edition, RoboCupJunior Rescue Committee.
**PDF:** https://junior.robocup.org/wp-content/uploads/2026/02/RCJRescueLine2026-final.pdf
**Rules last updated:** 2026-03-29 · **This extract compiled:** Session 34

> The English rules published by the RoboCupJunior Rescue Committee are the only official rules.
> Corrections and clarifications may be posted on the forum before the rule file is updated. Teams are
> responsible for checking the forum: https://junior.forum.robocup.org
>
> **Regional, SuperRegional, and local tournaments may vary these rules.** Confirm with the organizers of
> the tournament you are actually entering. This document is the *international* rule set.

**This file is the single source of truth for every competition claim in the textbook.**
Nothing in any lesson may state a point value, a time limit, or a field dimension that contradicts it.

---

## 1. The Clock — §5.3

**Each team has a maximum of 8 minutes for a game. The game includes the time for calibration AND the
scoring run.**

- Calibration = taking sensor readings and modifying the robot's programming to accommodate them. It is
  not pre-mapping and it is allowed — but **the clock runs the whole time.**
- Teams may calibrate in as many locations on the field as they like. The clock keeps running.
- Once a scoring run begins, **no more calibration** — including changing code or code selection.
- A team may skip calibration entirely and start the scoring run immediately.
- The game ends when: the 8 minutes expire, the captain calls it, or the robot reaches the goal tile and
  stops completely for 5 seconds.

> **Curriculum consequence:** any time budget in the book must subtract boot, self-test, and line-sensor
> calibration from the same 8 minutes. There is no separate setup window.

---

## 2. Scoring — §5.6

### 2.1 Hazard points (awarded once per hazard, per intended direction)

Points are awarded per hazard **when the robot has reached the next tile in sequence.**

| Hazard | Points |
|---|---|
| Tile with one or more **gaps** | **10** |
| Tile with one or more **speed bumps** | **10** |
| **Intersection** or **dead end** (correct path) | **10** |
| **Ramp** — per ramp *tile* | **10** |
| **Obstacle** (bricks, blocks, weights) | **20** |
| **Seesaw** tile | **20** |

Hazards inside the evacuation zone are **not** scored.

### 2.2 Tile points — and how a Lack of Progress decays them

When the robot reaches a checkpoint tile or stops on the goal tile, it earns points for each tile passed
since the previous checkpoint. **The value depends on how many attempts it took:**

| Attempt | Points per tile |
|---|---|
| 1st | **5** |
| 2nd | **3** |
| 3rd | **1** |
| Beyond 3rd | **0** |

### 2.3 Victims are MULTIPLIERS, not points

A **successful victim rescue (SVR)** occurs when the victim is entirely inside its designated evacuation
point and **no part of the robot is touching it.**

| Multiplier | Value | Condition |
|---|---|---|
| **SLVR** — living victim | **× 1.4** each | there are exactly **two** living victims |
| **SDVR** — dead victim | **× 1.4** | **only if both living victims have already been evacuated** |
| **EZLP** — penalty | **− 0.05** | per lack of progress in the area containing the evacuation zone |

- Earned multipliers **never fall below 1.25.**
- They compound: `(SLVR+EZLP)₁ × (SLVR+EZLP)₂ × (SDVR+EZLP)`
- **All three victims rescued cleanly = 1.4 × 1.4 × 1.4 ≈ 2.74×** applied to the entire field score.

### 2.4 Exit bonus — §5.6.11

Awarded when the robot reaches the goal tile and has **completely stopped for more than 5 seconds**
(that time counts against the 8 minutes).

```
EXIT BONUS = 60 − 5 × (total number of lack of progress)
```

It is a **non-negative** number — it floors at 0.

### 2.5 The final formula

```
FIELD SCORE = (LINE TRACING SCORE + EXIT BONUS) × (EVACUATION ZONE MULTIPLIER)
```

> **Curriculum consequence:** the evacuation zone multiplies *everything else*. A team that skips the
> zone keeps its line score and forfeits a multiplier worth up to 2.74×. "Play it safe and skip the
> rescue" is not a viable strategy under these rules.

---

## 3. The Field — §3

| Element | Specification |
|---|---|
| Tiles | 30 cm × 30 cm · minimum 8 tiles per field (excluding start and goal) |
| Floor | White; smooth or textured; steps of up to 3 mm between tiles |
| Line | Black, **1–2 cm wide** |
| Gaps | **No more than 20 cm long**; at least 5 cm of straight line before each gap |
| Line clearance | At least 10 cm from any field edge, wall, or pillar |
| Goal tile | 25 mm × 300 mm **red** tape strip, perpendicular to the incoming line |
| Speed bump | Up to one tile in size, **≤ 1 cm high**, white |
| Debris | **≤ 3 mm** high, not fixed down (toothpicks, dowels) |
| Obstacle | **≥ 15 cm high**, may be fixed to the floor; the robot is expected to go **around** |
| Ramps | **≤ 25°** incline |
| Seesaw | Pivots at the tile centre; **< 20°** when tilted |
| Bridged tiles | ≥ 25 cm of clearance underneath |
| All measurements | **± 10 % tolerance** |

### 3.1 Intersections — §3.6

- Intersection markers are **green, 25 mm × 25 mm**, placed **just before** the intersection.
- **No green marker → go straight.**
- **Two green markers (one each side) → dead end → turn around.**
- Intersections are always perpendicular; 3 or 4 branches.
- Never placed inside the evacuation zone.

### 3.2 Evacuation zone — §3.9

| | |
|---|---|
| Size | **120 cm × 90 cm**, walls **≥ 10 cm** high |
| Wall colour | Any colour **except red, green, or black** |
| **Entrance** | **25 mm × 250 mm strip of reflective SILVER tape** on the floor |
| **Exit** | 25 mm × 250 mm strip of **BLACK** tape on the floor |
| Evacuation points | Right-angled triangles, 30 cm × 30 cm, **6 cm walls**, hollow centre |
| → **Green** triangle | living victims |
| → **Red** triangle | the dead victim |
| Placement | any non-entry/exit corner; **may be moved after a Lack of Progress** |

**NEW for 2026:**
- Organizers **may place white LED lights** mounted perpendicular to the wall, on the upper part — but
  not in the corners where the triangles are.
- Organizers **may place fake victims** (objects or images) that resemble real victims. **Robots should
  ignore them.**

### 3.3 Victims — §3.10

- Spheres, **4–5 cm diameter**, off-centre centre of mass, **max 80 g**.
- **Living victims: silver, reflective, electrically conductive.**
- **Dead victim: black, not electrically conductive.**
- **Exactly two living and one dead**, placed randomly in the zone.

---

## 4. Lack of Progress — §5.5

A LoP occurs when the captain declares one, **or** the robot loses the black line without regaining it by
the next tile, **or** the robot reaches a line that is not in the intended sequence.

- The robot is placed back on the **previous checkpoint tile**, facing the goal.
- **There is no limit** to the number of LoPs in a round.
- After **three failed attempts** to reach a checkpoint, the robot may proceed to the next checkpoint.
- Only the LoP procedure declared to the referee before the run may be performed.
- In the evacuation zone: victims stay where they are; victims held by the robot are placed at the
  robot's location.

**A LoP costs three ways:** tile points decay (5 → 3 → 1 → 0), the exit bonus drops 5, and any evacuation
multiplier loses 0.05.

---

## 5. The Robot — §4

| Requirement | Rule |
|---|---|
| Control | **Fully autonomous.** No remote control, no external sensors, no information passed in. |
| Start | Started **manually by the team captain**. |
| **Handle** | **Robots must be equipped with a handle** to pick them up during the scoring run. §4.2.7 |
| **Start button** | **A single physical binary switch/button**, clearly visible to the referee, for starting and for LoP recovery. At most one additional switch, for cutting power. §4.2.8 |
| LoP procedure | Must be declared to the referee **before each scoring run**. |
| **Pre-mapped dead reckoning** | **PROHIBITED.** §4.1.3 — no movements preprogrammed from known field locations. |
| Pre-mapping | Any pre-mapping **immediately disqualifies the robot for the round**. §5.2.5 |
| Lasers | Class 1 and 2 only. |
| Kits | No commercial kit or sensor component marketed to solve a primary Rescue task. |

> **Curriculum consequence — §4.1.3.** Dead reckoning *itself* is legal and the book teaches it heavily
> (Lessons 6, 11, 12, 13). What is banned is **pre-mapped** dead reckoning — hard-coding a route from
> knowledge of the field. Lesson 13's lawnmower sweep is legal precisely because it **discovers** the
> room rather than assuming it.

---

## 6. Environmental conditions — §3.11

- Lighting and magnetic conditions **vary** at the venue.
- The field may suffer camera flashes from spectators.
- The field may sit over under-floor wiring or metal.
- **Teams must come prepared to adjust their robots to the conditions at the venue.**

---

## 7. What this Zumo can and cannot score

An honest accounting, for the textbook's own claims:

| Scoring element | Can our Zumo earn it? |
|---|---|
| Tile points (5/3/1) | ✅ Yes — line following, Lesson 8 |
| Gaps (10) | ✅ Yes — Lesson 11 |
| Intersections / dead ends (10) | ✅ Yes — Lesson 9 |
| Speed bumps (10) | ⚠️ Untested — ≤ 1 cm, likely driveable |
| Ramps (10/tile) | ⚠️ Untested — up to 25° |
| Obstacles (20) | ✅ Yes — Lesson 10 |
| Seesaws (20) | ⚠️ Untested |
| Entering the evacuation zone | ✅ Yes — silver detection, Lesson 13 |
| **Finding** a silver victim | ✅ Yes — Lesson 13 |
| **Finding** the black victim | ❌ **No.** The prox sensor cannot see it. Lesson 13 §4.3 — taught as a limitation, not a bug. |
| **Rescuing** a victim (the multiplier) | ❌ **No.** A rescue requires the victim to be moved *into the evacuation point*. The Zumo has no gripper — both DRV8838 drivers are spoken for, one per tread. Lesson 13 §8A.3. |
| Exit bonus (60 − 5×LoP) | ✅ Yes — reach the goal tile and stop for 5 s |

**The multiplier is the one thing out of reach**, and it is the most valuable thing on the field. That is
an honest and useful thing for a student to know before they walk into a venue.
