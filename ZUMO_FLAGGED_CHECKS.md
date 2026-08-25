# ZUMO — FLAGGED CHECKS FOR DJ
### The bench sheet. Every open L01–L04 row, grouped by what you have to set up.

**Flagged checks version: v1.1** — increment on every substantive edit
(moderate change → `v1.x`; minor → `v1.x.y`). The version lives ONLY in this line.

> **WHY THIS FILE EXISTS.** `ZUMO_BENCH_TESTS.md` is the complete tracker — 53 rows across 15
> lesson blocks — and it is the right home for everything that needs the robot. But a 53-row
> file is a file nobody works from at the bench. **This is the working sheet: the 18 open rows
> in L01–L04, in the order that lets one evening close them.** A row leaves this file the
> moment its Result is written; the full tracker keeps the record.
>
> **HOW TO USE IT.** Run it, write what happened in the **Result** column in your own words,
> and say so in the next session. A number measured here goes into the book; a number that has
> not been measured here does not.
>
> **F1, F2 AND F3 KEEP THEIR NUMBERS.** They have been cited as F1/F2/F3 since S179, in this
> file and in `ZUMO_BENCH_TESTS.md`. Renumbering them to fit the station order would silently
> change what an existing citation points at, so the stations reorder the RUN and never the IDs.
>
> **TWO ROWS CAN FALSIFY PRINTED PROSE** — **F10** and **F14**. Both carry a stated prediction.
> If the prediction fails, a paragraph in the live book is wrong and comes out. Run those two
> even if you run nothing else.

---

## What to bring

| Station | What you need |
|---|---|
| **A — Desk** | Robot · USB cable · your Mac · **a Windows machine** (F7 needs both) |
| **B — Battery** | A **freshly charged** pack and a **run-down** pack |
| **C — Floor** | ~4 m of clear floor · painter's tape for a start line · tape measure · a catcher for F13 |
| **D — Tape** | A white surface · **matte black electrical tape** (IR-absorbing — marker or print is unreliable) |

Station D's materials are the thing that has blocked the L04 learner-mode build since S51. Buying
the tape closes F17 by itself and unblocks F15, F16 and F18 in the same sitting.

---

## STATION A — desk, robot and laptop, no floor

| # | Row | What to do | Where | Why it matters | Result |
|---|---|---|---|---|---|
| **F1** | `L01-B1` | **Unplug the USB cable FIRST, then click Upload.** Not a cable pulled mid-transfer — an upload with no port at all. **Write the error text down verbatim**, exactly as PlatformIO prints it. | §6 *Break It On Purpose* | The exercise's whole payoff is the student recognizing the error when it happens for real on a build day. The book currently describes the failure without quoting it. | |
| **F3** | `L01-B4` | **Challenge 11's solution exactly as printed.** `setLayout21x8()`, then the voltage, 1.5 s, then the `< 4500` branch. **Can you read the number on the OLED** before §6's setup reprints *Press A* over it? | §9 Challenge 11 | If the number is overwritten before it is readable, the printed solution does not do what the challenge asks, and the student will think their code is broken. | |
| **F4** | `L01-B5` | **Challenge 9, propped up.** Delete the three-line wait. Does the show start the instant power comes on, with no button press? | §9 Challenge 9 | The card claims the wait is what holds the show back. Deleting it is the only way to see whether that is the whole story. | |
| **F7** | `L01-B8` | **First-connection behaviour on a Mac AND on Windows.** The book now says a chime, a dialog, or nothing at all are all normal. Confirm on both machines. | §6 Step 4 | Day-one support load. A student on the machine the book did not describe assumes their robot is broken. | |
| **F8** | `L01-B10` | **Bootloader port change.** Does the robot really show one port while running and a different one with the bootloader awake? | §8 | §8 troubleshooting tells students to look for exactly this. Nobody has confirmed the fleet does it. | |
| **F9** | `L02-B1` | **The green LED bench check.** Carried since S41 — the oldest open row in L01–L04. | §5 | | |
| **F10** | `L02-B2` | **Challenge 2 screen overwrite — run it BOTH ways.** With the release-wait REMOVED, hold A and B: **you should see ONE flash of the Controls screen, then the battery screen settles.** With the wait IN, no flash at all. | §9 Challenge 2 | **FALSIFIABLE.** The prediction was derived from Pololu's own `PushbuttonStateMachine`, transcribed and run — never observed. **If the flash does not appear with the wait removed, the reasoning in §9 C2's *Why it takes two trips and not one* is wrong and the paragraph comes out.** | |

---

## STATION B — battery, two packs

| # | Row | What to do | Where | Why it matters | Result |
|---|---|---|---|---|---|
| **F5** | `L01-B6` | **Battery bands.** Read `readBatteryMillivolts()` on a fresh pack and on a tired one. The book says ~5,400 fresh / ~4,800 working / ~4,200 low. | §9 C11 hint | These three numbers are canon in **34 figures across L01–L03**. They are correct by agreement and have never been read off a real pack. | |
| **F6** | `L01-B7` | **Does USB alone really read low and strange?** The hint says so. Read the pack with the switch OFF and the cable in. | §9 C11 hint | | |

---

## STATION C — floor, start line and tape measure

| # | Row | What to do | Where | Why it matters | Result |
|---|---|---|---|---|---|
| **F2** | `L01-B3` | **Challenge 4 on the floor.** Change the **FIRST** `delay(350)` to 700 and nothing else. Does the robot finish roughly one nudge **ahead** of where it started? | §9 Challenge 4 | S177 corrected the revealed solution from *twice as long in each direction* to *twice as far out as it comes back*. That correction is reasoned, not observed. If the robot ends up behind or level, the new reveal is wrong too. | |
| **F11** | `L03-B1` | **How far does one TRIM test run actually go?** `TEST_DURATION` is 2000 ms at `BASE_SPEED` 200. Tape a start line, press B, measure. | §4.4, §7 | The *6+ feet* figure was DELETED rather than corrected (S179, rule 50). This row exists so the book can one day state a MEASURED distance instead of calling the run *short*. | |
| **F12** | `L03-B2` | **What TRIM value does a real robot need?** Record yours, and the spread across the fleet. | §5 | Feeds the TDP's *your TRIM number and why it exists*. Data collection, not verification — nothing in the book is wrong if it goes unrun. | |
| **F14** | `L03-B3b` | **Is the motor mismatch direction-symmetric?** Tune TRIM straight forward, then drive the same robot **backward** with the fixed code. | §9 Bonus 2, L06 Step 13 | **FALSIFIABLE.** The book now claims: fix the sign and the big reverse curve goes away, leaving a small mechanical residual. The electrical half is proved (`setLeftSpeed` writes `\|speed\|` to `OCR1B` and puts the sign on a GPIO pin). **If the residual reverse curve is as large as the original error, the symmetry premise is wrong and Bonus 2's reveal must put gearbox asymmetry back as the headline.** | |
| **F13** | `L03-B3` | **Bonus Challenge 4 (Braking vs. Coasting)** asks for *about 3 meters of clear floor and a catcher*. Measure what it really needs. | §9 Bonus 4 | That figure has no pedigree, and unlike the TRIM run this one is full speed (400) for 1.5 s each way. **The card already offers `delay(800)` as the short-floor escape, so nothing is blocked** — run it last, it needs the most room. | |

---

## STATION D — white surface and matte black tape

| # | Row | What to do | Where | Why it matters | Result |
|---|---|---|---|---|---|
| **F17** | `L04-B3` | **Bring the materials.** A white surface and **matte black electrical tape**. This row closes the moment they exist in the room. | learner mode | Carried since S51. It is the blocker under F15, F16 and F18, and under the L04 learner-mode build. | |
| **F15** | `L04-B1` | **Calibration min/max on the classroom floor.** Record the numbers and the room's lighting. | §5 | Feeds TDP table A4, and the room's lighting is the variable RCJ §3.11 warns about. | |
| **F16** | `L04-B2` | **The 600 threshold.** Book-wide canon is 600, with 500 taught as the midpoint. **Does 600 separate your tape from your floor?** | §8A | If it does not, every threshold argument downstream of L04 is tuned to a number this room does not support. | |
| **F18** | `L04-B4` | **The wave-test direction** and **Act Two's row-1 overflow.** | §7 | Both are deliberately NOT asked in `QUIZ_L04`, because they are open bench findings. Closing this row is what lets them be graded. | |

---

## What is NOT on this list, and why

- **`L01-B2` (cable in, power off, upload succeeds)** — **CLOSED by DJ's ruling, S179.** The cable
  powers the chip, the switch feeds the motors. Bible §16.48.
- **`L01-B9` (Git on a fresh Mac)** — **CLOSED by DJ's ruling, S179.** Git is required because it
  triggers Apple's Command Line Tools installer, which is where the compiler lives. Bible §16.48.
  This also closes worklist row `L01-03`, open since S137.
- **L05–L16** — still in `ZUMO_BENCH_TESTS.md`, which stays the complete tracker. The most
  consequential row there is `L10-B1`, §16.12's perpendicular arrival, unruled since S143 and
  carrying a falsifiable prediction of its own.

---
*Flagged checks · the L01–L04 working sheet · the full tracker is `ZUMO_BENCH_TESTS.md`*
