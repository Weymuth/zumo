# ZUMO — FLAGGED CHECKS FOR DJ
### The bench sheet. **Nine open rows in L01–L04**, in the order that lets one evening close them.

**Flagged checks version: v1.6** — increment on every substantive edit
(moderate change → `v1.x`; minor → `v1.x.y`). The version lives ONLY in this line.

> **THE COUNT CHANGED AT S198, AND THE OLD ONE WAS THE DEFECT.** This sheet said *18 open rows*
> and kept saying it after the S196 bench answered six of them and half-answered three. The
> results were appended in a new section at the bottom while **every Result cell in the station
> tables stayed blank**, so anyone working from the tables would have re-run six rows already
> measured. The file's own rule — *a row leaves this file the moment its Result is written* —
> was written and then not followed, which is the failure it exists to prevent.
>
> **THE ROWS WERE NOT DELETED, DELIBERATELY.** `ZUMO_BENCH_TESTS.md` was checked at S198 and
> **does not carry a single one of the measured numbers** — not 59.4 cm, not the slam/ramp pair,
> not the battery readings. The rule assumed the tracker keeps the record and the tracker does
> not. **Measured data is the most expensive thing in this repo and it has exactly one home**, so
> the results stay here in full until they are migrated, and the migration is its own job.
>
> **HOW TO USE IT.** Run a row, write what happened in the **Result** column in your own words,
> and say so in the next session. A number measured here goes into the book; a number that has
> not been measured here does not.
>
> **F1, F2 AND F3 KEEP THEIR NUMBERS.** They have been cited as F1/F2/F3 since S179, here and in
> `ZUMO_BENCH_TESTS.md`. Renumbering them to fit the run order would silently change what an
> existing citation points at, so the order changes and the IDs never do.
>
> **THIS COUNT IS SCOPED TO THIS SHEET, WHICH IS L01–L04 ONLY.** *Nine* is the number of open rows
> **here**. It is not the book's number. This clause was added at S189 because the then-current
> figure was read off this sheet and generalised to the whole book, and it was dropped by the S198
> rewrite and restored the same session by the triple check — **which is the second time the same
> sentence has had to be put back.** The book-wide ranked list lives at the top of
> `ZUMO_BENCH_TESTS.md` (**v1.5**), and the most consequential row in it is not here: it is
> **`L10-B1`, §16.12's perpendicular arrival, unruled since S143** and carrying a falsifiable
> prediction of its own.
>
> **NOTHING ON THIS LIST CAN NOW FALSIFY PRINTED PROSE.** The two rows that could — **F10** and
> **F14** — were run at S196 and both **failed**, and both paragraphs came out at S197. That is
> what this sheet is for. The remaining nine test claims the book states without evidence rather
> than claims it states wrongly; the cost of leaving them is a student hitting something the book
> did not warn about, not a student reading something false.

---

## RUN THESE — the nine open rows

Ordered so one sitting closes as many as possible. **F1, F3, F4, F6, F7 and F8 need only a desk,
the robot and a laptop** — six rows, one battery, no floor. F7 is the only row needing a second
machine. F2 needs floor; F15 needs the tape, which is now in the room.

| # | Row | What to do | Where | Why it matters | Result |
|---|---|---|---|---|---|
| **F7** | `L01-B8` | **First-connection behaviour on a Mac AND on Windows.** The book now says a chime, a dialog, or nothing at all are all normal. Confirm on both machines. | §6 Step 4 | Day-one support load, and it lands on every student at once in period 2. A student on the machine the book did not describe assumes their robot is broken. | |
| **F1** | `L01-B1` | **Unplug the USB cable FIRST, then click Upload.** Not a cable pulled mid-transfer — an upload with no port at all. **Write the error text down verbatim**, exactly as PlatformIO prints it. | §6 *Break It On Purpose* | The exercise's whole payoff is the student recognizing the error when it happens for real on a build day. The book currently describes the failure without quoting it. | |
| **F8** | `L01-B10` | **Bootloader port change.** Does the robot really show one port while running and a different one with the bootloader awake? | §8 | §8 troubleshooting tells students to look for exactly this. Nobody has confirmed the fleet does it. | |
| **F3** | `L01-B4` | **Challenge 11's solution exactly as printed.** `setLayout21x8()`, then the voltage, 1.5 s, then the `< 4500` branch. **Can you read the number on the OLED** before §6's setup reprints *Press A* over it? | §9 Challenge 11 | If the number is overwritten before it is readable, the printed solution does not do what the challenge asks, and the student will think their code is broken. | |
| **F4** | `L01-B5` | **Challenge 9, propped up.** Delete the three-line wait. Does the show start the instant power comes on, with no button press? | §9 Challenge 9 | The card claims the wait is what holds the show back. Deleting it is the only way to see whether that is the whole story. | |
| **F6** | `L01-B7` | **Does USB alone really read low and strange?** The hint says so. Read the pack with the switch OFF and the cable in. | §9 C11 hint | Pairs with F5, same station, same pack — and F5's own reading is now known to disagree with the book, so this hint's *low and strange* has nothing behind it either. | |
| **F9** | `L02-B1` | **The green LED bench check.** Carried since S41 — the oldest open row in L01–L04. | §5 | **This row has never had a Why column.** Fifty-seven sessions of being carried without anyone writing down what it would prove. Either state what it tests when you run it, or rule it out. | |
| **F2** | `L01-B3` | **Challenge 4 on the floor.** Change the **FIRST** `delay(350)` to 700 and nothing else. Does the robot finish roughly one nudge **ahead** of where it started? | §9 Challenge 4 | S177 corrected the revealed solution from *twice as long in each direction* to *twice as far out as it comes back*. That correction is reasoned, not observed. If the robot ends up behind or level, the new reveal is wrong too. | |
| **F15** | `L04-B1` | **Calibration min/max on the classroom floor.** Record the numbers and the room's lighting. | §5 | Feeds TDP table A4, and the room's lighting is the variable RCJ §3.11 warns about. Unblocked since S196 — the tape exists. | |

---

## OPEN, BUT NOT RUNNABLE ON DEMAND

These three are not on the run list, and each for a different reason. **None of them is closed.**

| # | State | Why it is not a run |
|---|---|---|
| **F5** | **RULED S198 — canon stands, contradiction recorded** | DJ's ruling: the three bands in L01–L03 stay as printed, to be adjusted later if they are found in error. **The contradiction is on the record and is not withdrawn** — measured fresh is ~201 mV BELOW canon *fresh*, and a hard session ends ~292 mV ABOVE canon *working*. The tired reading cannot be taken on demand anyway: twelve hard runs moved the pack about 2%, so the low band is not reachable at a bench. **What would settle it is a pack run flat in normal use, logged — not a bench sitting.** |
| **F10** | **Wait-OUT half uncited** | The wait-IN half is observed and shipped. The wait-OUT half was an eyeball on a persistence claim and wants **serial timestamps** before it is cited. Not a rerun of the same procedure. |
| **F16** | **Calibrated half waits by design** | The raw half is measured and §8A's premise is safe (~26× separation). The calibrated 0–1000 half stays open until DJ's own L04 build runs its calibration — handing him a calibration sketch would spoil the deliberate RED build at L04 Step 5. |

---

## CLOSED — DO NOT RE-RUN

Full numbers are in **BENCH RESULTS** below; this table exists so nobody works from a blank cell.

| # | Row | Verdict |
|---|---|---|
| **F11** | `L03-B1` | ✅ **59.4 cm** in 2000 ms at speed 200 → 29.7 cm/s. Landed in L03 §4.4 at S197. |
| **F12** | `L03-B2` | ✅ TRIM **+5**, curves left untrimmed — polarity canon CONFIRMED. ~0.6 cm lateral per TRIM unit. |
| **F13** | `L03-B3` | ✅ Slam 44.88 cm, ramp 74.23 cm (n=6 each). Predicted from F11 within 1%. |
| **F14** | `L03-B3b` | ❌ **FAILED** — the `2x` prediction was wrong (observed 0.37×). Bonus 2's reveal rewritten S197. |
| **F17** | `L04-B3` | ✅ Materials present. Had blocked F15/F16/F18 and the L04 learner build since **S51**. |
| **F18** | `L04-B4` | ✅ Wave order matches physical left-to-right; row-1 overflow closed by arithmetic. |

---

## WHAT TO BRING

| Station | What you need |
|---|---|
| **A — Desk** | Robot · USB cable · your Mac · **a Windows machine** (F7 needs both) |
| **B — Battery** | A charged pack (F6 reads it with the switch off) |
| **C — Floor** | ~4 m of clear floor · painter's tape for a start line · tape measure |
| **D — Tape** | A white surface · **matte black electrical tape** — already in the room since S196 |

**Log the battery voltage with every run.** A downward settling trend showed up in three unrelated
programs at S196 and its cause is still unknown, because battery was not logged per run.

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
| **F10** | **❌ FAILED — PROSE DELETED S197** | Wait IN: battery screen visible only while held, gone on release. Wait OUT: battery screen appears and persists until next press. **Neither run showed the predicted three-screen sequence.** The wait-IN result contradicts the book outright and cannot be explained by a flash too fast to see — a fast flash cannot make a screen vanish and stay vanished. **§9 C2's "Why it takes two trips and not one" paragraph comes out.** Wait-OUT half wants a serial-timestamp confirmation rather than an eyeball before it is cited. |
| **F11** | ✅ MEASURED — **LANDED S197** | **59.4 cm** in 2000 ms at speed 200 → **29.7 cm/s**. The book only ever called this run "short"; 59.4 cm is most of a desk and the prose undersells the floor a student needs. |
| **F12** | ✅ MEASURED | TRIM **+5**, curves LEFT untrimmed, so positive TRIM is the correction — polarity canon CONFIRMED. Derived sensitivity ≈ **0.6 cm of lateral correction per TRIM unit** (from the −5 run: 7 cm at −5, 2.75 cm mean at 0). Motors are well matched; +5 is one TRIM_STEP and slightly overshoots straight. |
| **F13** | ✅ **PASSED — and validated F11** | Slam **44.88 cm** (n=6, sd 0.17). Ramp **74.23 cm** (n=6, sd 0.73). Difference **+29.35 cm**, ranges nowhere near overlapping. Predicted from F11's own rate (20 steps × 50 ms = 1000 ms at mean speed 200 → 29.7 cm): **agreement within 1%**. Two independent tests on two programs agree, which also demonstrates motor speed is near-linear over 0–400 — asserted in the book, never shown. |
| **F14** | **❌ FAILED — PROSE REWRITTEN S197** | Baseline forward TRIM 0, **n=8: mean 2.75 cm** left, 95% CI 2.13–3.37. Backward with TRIM +5 naively negated, **n=7: mean 1.01 cm**, 95% CI 0.49–1.53. Book predicts ~5.5 cm (2× baseline); observed **0.37×**. The wrongly-aimed TRIM did not double the error — **it left the robot straighter than having no TRIM at all**. No evidence of direction asymmetry on this robot. **§9 Bonus 2's reveal must be rewritten.** Sign-flip run (run 3) not taken: with run 1 at 1 cm it had nothing left to demonstrate. |

> **S197 — WHAT THE BENCH ACTUALLY DELETED, AND WHAT SURVIVED.**
> **F10.** L02 §9 C2's three-screen prediction and the two-trips mechanism invented to explain it
> are OUT, registered as retired claim `F10` in `retired_claims.py` v1.2.1 under **two spellings** —
> the observation and the mechanism can be restated independently. Controlled both directions: the
> deleted paragraph fires both entries; the sentence that SURVIVED the edit fires neither. **The
> 15 ms debounce interval is deliberately NOT retired** — it is a real library property. What is
> retired is the claim that it forces a second pass through `loop()`. The replacement paragraph
> states only the wait-IN behaviour, which is what was observed and needs no further support; **the
> wait-OUT half is still uncited and still wants serial timestamps.**
> **F14.** L03 §9 Bonus 2's reveal no longer predicts a magnitude. The sign arithmetic
> (`setSpeeds(215,200)` → `setSpeeds(-185,-200)`) is exact and stays verbatim; the `2x` claim is
> replaced by the measured result and by the reason it came out that way — **a mis-aimed TRIM of 5
> is a 10-count error, small enough that a well-matched robot runs straighter than with no TRIM.**
> `L03_A19`'s `why:` said *the big reverse curve* and was fixed in the same sweep (rule 72 — a
> claim fixed where it was quoted is not fixed where it was repeated).
> **F11.** 59 cm now appears in L03 §4.4 twice, replacing *the test run is short* in the floor
> requirement and in the Post-it NOTE. **§5 Step 3's "too small to see over a short test run" was
> deliberately LEFT** — that sentence is about TRIM resolution, not floor space, and is unaffected.
> **BD1 CLOSED S197 / BD2 RULED NOT THE SAME DEFECT.** `L3/braking_test` now blinks the yellow LED
> five times before the motors start — a `countdown()` helper called from BOTH the A and C branches,
> LED rather than OLED so the challenge gains no hardware object and no vocabulary it has not met.
> Lesson listing and Maker payload edited together; census pin moved 20 → 31 lines; Maker **v2.72**.
> **BD2 `L2/speed_limit` was left alone deliberately, and the handoff's "identical defect" reading
> does not survive reading the challenge.** Three reasons: (1) **it takes no measurement**, so there
> is no reading for a press-nudge to corrupt — the nudge only matters where a distance is being
> recorded; (2) it is **hold-to-run** (`buttonB.isPressed()`), a dead-man switch that stops the
> instant the finger leaves, which is SAFER than countdown-then-autorun — adding a countdown would
> be a regression; (3) the 400 is **the defect the student is asked to fix** — the whole task is
> "cap it at 150" — so removing it removes the challenge. L02 already carries its own WARNING that
> the tracks engage the moment the button is held. **The question "should L02 be running at 400 at
> all" is answered: yes, deliberately, and only while a finger holds it there.**
> **Still open from this sheet: F5 battery canon — needs DJ, a fleet fact, not a text fix.**

| **F16** | ✅ RAW HALF CLOSED | Three-sensor config, raw reflectance. White L46 / C26 / R46. Tape L1164 / C692 / R1200. **~26× separation on every sensor** — §8A's premise is safe. Lifted control: L1256 / C728 / R1276, i.e. **tape reads within 8% of no-surface**, confirming matte black tape is the right material. Per-sensor offset is **multiplicative, not additive** (absolute values differ ~2×, ratios identical) — a good specimen for why calibration normalises per sensor. Calibrated 0–1000 half stays OPEN, by design, until DJ's own L04 build runs its calibration. |
| **F17** | ✅ CLOSED | Materials present. Blocked F15/F16/F18 and the L04 learner build since **S51 — fifty-one sessions**. |
| **F18** | ✅ CLOSED | Wave test: index order **matches physical left-to-right**, no reversal. Act Two row-1 overflow closed by arithmetic, not hardware — row 0 prints five sensors as single digits (`/101`), row 1 prints `P:` plus position; neither approaches the 21-column width. |

### CROSS-ROW FINDINGS (not owned by any single row)

- **A settling trend appeared in THREE unrelated programs.** Forward TRIM runs, backward TRIM runs and the first slam runs all drift downward over repeated runs. Cause UNKNOWN — candidates are pack sag, motors warming, surface. Not claimed, because battery was not logged per run. **Log battery with every run next bench session.**
- **Distance is repeatable; lateral drift is not.** Six slam runs spanned **5 mm** on 45 cm (~1%); TRIM-0 drift spanned **2.2×** run to run. **L03 asks students to judge TRIM from a single run.** Direction survives that — left every time. Magnitude does not. Any prose implying you can read the size of the error off one run is wrong.
- **The robot tracks straighter at speed 400 than at 200.** ~1 cm lateral over 45 cm untrimmed at 400, vs 2.75 cm over 59.4 cm at 200. **TRIM is tuned at 200 and may not correct the same mismatch at 400.**
- **TRIM_STEP resolution.** +5 is one step and slightly overshoots straight on a well-matched robot. Eight students may land on 0, 5 or 10 and see no difference they can distinguish — some will hunt for a right answer that is not resolvable.
