# ZUMO — FLAGGED CHECKS FOR DJ
### The bench sheet. Every open L01–L04 row, grouped by what you have to set up.

**Flagged checks version: v1.5** — increment on every substantive edit
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
> **TWO ROWS ON THIS SHEET CAN FALSIFY PRINTED PROSE** — **F10** and **F14**. Both carry a stated
> prediction. If the prediction fails, a paragraph in the live book is wrong and comes out. Run
> those two even if you run nothing else.
>
> **BOTH WERE REWRITTEN AT S196 BECAUSE NEITHER PROCEDURE COULD TEST THE CLAIM IT NAMED**, and both
> were found the same way — by reading the lesson instead of the row. **F10** said *one flash of the
> Controls screen*; §9 C2 prints a **three-screen sequence in a fixed order**, and a run watching for
> one flash records an ambiguous result on a sequence that may not match. **F14** asked for two runs;
> Bonus 2's claim is a **RATIO** — a wrongly-aimed TRIM is *roughly twice as bad as having none* —
> and a ratio needs the no-TRIM baseline the two-run procedure never produces. **A row is a
> description of an artefact; the artefact is the answer** (S195). Neither row was corrupt: both are
> the original authored summaries, drifted from the prose they summarise.
>
> **THAT COUNT IS SCOPED TO THIS SHEET, WHICH IS L01–L04 ONLY. BOOK-WIDE THERE ARE SEVEN**, and
> the most consequential of them is not here — it is `L10-B1`, §16.12's perpendicular arrival.
> **The full ranked list lives at the top of `ZUMO_BENCH_TESTS.md` (v1.5).** This scope clause was
> added at S189 because the two-row figure was read off this sheet and generalised to the whole
> book, which is wrong: the footer of this very file already named `L10-B1` as a third.

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
| **F10** | `L02-B2` | **Challenge 2 screen overwrite — run it BOTH ways.** With the release-wait REMOVED, hold A and B: the lesson predicts **THREE screens in this exact order** — the battery screen appears, then About **and** Controls flash over it, then the battery screen returns and stays. With the wait IN, no flash at all. **Record the ORDER, not merely whether a flash happened** — the order is what tests the mechanism. | §9 Challenge 2 | **FALSIFIABLE.** The prediction was derived from Pololu's own `PushbuttonStateMachine`, transcribed and run — never observed. **If the sequence does not appear with the wait removed, the reasoning in §9 C2's *Why it takes two trips and not one* is wrong and the paragraph comes out.** | |

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
| **F14** | `L03-B3b` | **Is the motor mismatch direction-symmetric? THREE runs, not two.** Same start line, same distance, same pack. **(1) BASELINE:** `TRIM = 0`, both speeds negated, backward. **(2) NAIVE:** your tuned TRIM, both speeds negated, TRIM math untouched. **(3) FIXED:** TRIM sign reversed for backward. Measure lateral drift at the finish each time. | §9 Bonus 2, L06 Step 13 | **FALSIFIABLE, AND IT CARRIES TWO SEPARATE PREDICTIONS.** The electrical half is proved (`setLeftSpeed` writes `\|speed\|` to `OCR1B` and puts the sign on a GPIO pin). **(a)** Bonus 2 prints that a wrongly-aimed TRIM is *roughly twice as bad as having none* — **run 2 ≈ 2 × run 1**, which is why run 1 exists: a two-run procedure cannot test a claim stated as a ratio. **(b)** Fix the sign and the big curve goes, leaving a small mechanical residual. **If run 3's residual is as large as run 1, the symmetry premise is wrong and Bonus 2's reveal must put gearbox asymmetry back as the headline.** | |
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

---

## BENCH-FOUND DEFECTS — S196 (found at the robot, not by an instrument)

These were found by DJ running the book's own code at the bench on Aug 30. They are
**book defects, not bench results**: no measurement is pending, the fix is known, and
each needs a code edit in a payload plus whatever prose describes it.

| # | Where | Defect | Fix | Status |
|---|---|---|---|---|
| **BD1** | Maker `L3/braking_test` (§9 Bonus 4) | Launches at **speed 400 with no countdown and no wait** — motors start on the button press, so the press itself nudges the robot at the instant the run begins, and the nudge lands inside the distance being measured. L03's own TRIM Finder in the same lesson has a 3-second countdown; this does not. | Add a countdown before `setSpeeds(400,400)` in BOTH the A and C branches. Bench version used 5 s with a per-second LED blink, since at 400 you need time to set down AND get clear. Add a battery line to the ready screen while there. | OPEN |
| **BD2** | Maker `L2/speed_limit` | **Same defect, different lesson, not yet hit at the bench.** Found by sweeping all 221 payloads for `setSpeeds` ≥300 with no `Starting in` / `waitForButton` guard. Only these two exist book-wide. | Same fix. Check whether L02 is the right lesson to be running at 400 at all. | OPEN |

**RULE THIS ESTABLISHES.** A payload that launches at high speed must not start on the
button edge. The countdown is not decoration — at speed 400 the robot covers roughly
90 cm before the stop command even fires (derived from F11: 59.4 cm at speed 200 in
2000 ms), so a hand still on the robot is both a safety issue and a measurement error.

**HOW BD2 WAS FOUND, AND THE RULE THAT FOUND IT.** DJ reported BD1 from the bench. The
sweep for other homes of the same phenomenon was run over the PAYLOADS structure, not
over lesson prose — a prose search for the launch pattern returns ZERO, because the
code lives in the Maker and the lessons only describe it. Searching where the symptom
was reported would have found one of two.

---

## BENCH RESULTS — S196, Aug 30 (DJ at the robot, one sitting)

Recorded as OBSERVED, not as interpreted. Where a claim failed, the prose it deletes is named.

| Row | Result | Numbers |
|---|---|---|
| **F5** | **HALF CLOSED — canon contradicted** | fresh idle **5199 mV**; under button load **5177**; after ~12 speed-400 runs plus tuning **5092**. Total sag across a hard session **107 mV (2.1%)**. Book canon is ~5400 / ~4800 / ~4200 — measured fresh is **201 mV BELOW** canon "fresh", and a hard session leaves it still **292 mV ABOVE** canon "working". **The three-band scheme does not map onto what a student will see**, and those figures appear in 34 figures across L01–L03. The genuinely tired reading remains OPEN: twelve hard runs moved the pack 2%, so the low band cannot be reached at a bench on demand. |
| **F10** | **❌ FAILED — deletes prose** | Wait IN: battery screen visible only while held, gone on release. Wait OUT: battery screen appears and persists until next press. **Neither run showed the predicted three-screen sequence.** The wait-IN result contradicts the book outright and cannot be explained by a flash too fast to see — a fast flash cannot make a screen vanish and stay vanished. **§9 C2's "Why it takes two trips and not one" paragraph comes out.** Wait-OUT half wants a serial-timestamp confirmation rather than an eyeball before it is cited. |
| **F11** | ✅ MEASURED | **59.4 cm** in 2000 ms at speed 200 → **29.7 cm/s**. The book only ever called this run "short"; 59.4 cm is most of a desk and the prose undersells the floor a student needs. |
| **F12** | ✅ MEASURED | TRIM **+5**, curves LEFT untrimmed, so positive TRIM is the correction — polarity canon CONFIRMED. Derived sensitivity ≈ **0.6 cm of lateral correction per TRIM unit** (from the −5 run: 7 cm at −5, 2.75 cm mean at 0). Motors are well matched; +5 is one TRIM_STEP and slightly overshoots straight. |
| **F13** | ✅ **PASSED — and validated F11** | Slam **44.88 cm** (n=6, sd 0.17). Ramp **74.23 cm** (n=6, sd 0.73). Difference **+29.35 cm**, ranges nowhere near overlapping. Predicted from F11's own rate (20 steps × 50 ms = 1000 ms at mean speed 200 → 29.7 cm): **agreement within 1%**. Two independent tests on two programs agree, which also demonstrates motor speed is near-linear over 0–400 — asserted in the book, never shown. |
| **F14** | **❌ FAILED — deletes prose** | Baseline forward TRIM 0, **n=8: mean 2.75 cm** left, 95% CI 2.13–3.37. Backward with TRIM +5 naively negated, **n=7: mean 1.01 cm**, 95% CI 0.49–1.53. Book predicts ~5.5 cm (2× baseline); observed **0.37×**. The wrongly-aimed TRIM did not double the error — **it left the robot straighter than having no TRIM at all**. No evidence of direction asymmetry on this robot. **§9 Bonus 2's reveal must be rewritten.** Sign-flip run (run 3) not taken: with run 1 at 1 cm it had nothing left to demonstrate. |
| **F16** | ✅ RAW HALF CLOSED | Three-sensor config, raw reflectance. White L46 / C26 / R46. Tape L1164 / C692 / R1200. **~26× separation on every sensor** — §8A's premise is safe. Lifted control: L1256 / C728 / R1276, i.e. **tape reads within 8% of no-surface**, confirming matte black tape is the right material. Per-sensor offset is **multiplicative, not additive** (absolute values differ ~2×, ratios identical) — a good specimen for why calibration normalises per sensor. Calibrated 0–1000 half stays OPEN, by design, until DJ's own L04 build runs its calibration. |
| **F17** | ✅ CLOSED | Materials present. Blocked F15/F16/F18 and the L04 learner build since **S51 — fifty-one sessions**. |
| **F18** | ✅ CLOSED | Wave test: index order **matches physical left-to-right**, no reversal. Act Two row-1 overflow closed by arithmetic, not hardware — row 0 prints five sensors as single digits (`/101`), row 1 prints `P:` plus position; neither approaches the 21-column width. |

### CROSS-ROW FINDINGS (not owned by any single row)

- **A settling trend appeared in THREE unrelated programs.** Forward TRIM runs, backward TRIM runs and the first slam runs all drift downward over repeated runs. Cause UNKNOWN — candidates are pack sag, motors warming, surface. Not claimed, because battery was not logged per run. **Log battery with every run next bench session.**
- **Distance is repeatable; lateral drift is not.** Six slam runs spanned **5 mm** on 45 cm (~1%); TRIM-0 drift spanned **2.2×** run to run. **L03 asks students to judge TRIM from a single run.** Direction survives that — left every time. Magnitude does not. Any prose implying you can read the size of the error off one run is wrong.
- **The robot tracks straighter at speed 400 than at 200.** ~1 cm lateral over 45 cm untrimmed at 400, vs 2.75 cm over 59.4 cm at 200. **TRIM is tuned at 200 and may not correct the same mismatch at 400.**
- **TRIM_STEP resolution.** +5 is one step and slightly overshoots straight on a well-matched robot. Eight students may land on 0, 5 or 10 and see no difference they can distinguish — some will hunt for a right answer that is not resolvable.
