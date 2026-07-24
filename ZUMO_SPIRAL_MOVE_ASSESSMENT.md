# ZUMO — Book-Wide Challenge-Move Assessment for the Spiral (S67)

**Doc version: v1.1** — v1.0 contained an arithmetic error (L06-after mean stated 2.43; correct
value 2.29) and one loose figure (L08 drop-C1+C2 stated ~2.50; correct 2.67). Both fixed below;
all means in this version are script-computed from the live files, not hand-summed. v1.1 also
adds the dependency-verification results and one newly found move cost (the GRAPHIC 6.11 row).

**Question asked:** starting at L01, which challenges could MOVE to promote the Saxon spiral —
and can moves balance the difficulty ramp (Job B)?

**Answer in one line:** the book has **one clean move** (L06 C8 → L07 capstone). Everything else
that looks like a move candidate is really a **marking** candidate — the spiral substance already
exists across nine identifiable spines, but the markers stop at L06 and the whole back half is
unmarked. Moves are scarce because in almost every spiral pair, **both ends are load-bearing**:
pulling the early card out breaks that lesson's ramp position (several of which S66 just fixed).

All card data below was extracted from the live files (clone `4513e51`); means on the canonical
1–5 / 1–3 scales. Every card text claim was verified against the rendered card, not the extractor
(one extractor false-positive — "L14 C2/C3 duplicate goals" — was caught and killed this way:
14.2 is prose format with no GOAL header and the scraper leaked 14.3's goal into it).

---

## 1. THE ONE CLEAN MOVE

### L06 C8 "Trapezoidal Motion Profile" (Advanced/Deep) → L07 capstone

**Why it's a spiral move and not just a shuffle.** L06 C8 combines Smooth Acceleration (C7) and
Smooth Stopping (C6) into one motion function — in L06's single-file world. L07's entire lesson is
"one program becomes 8 files — which file owns what." Re-landing the trapezoid in L07 turns it
into: *take a known algorithm and decide where every piece lives* — profile logic in
`RobotMotion.cpp`, the speed constants in `RobotConfig.h`, declaration in the header. That is
literally L07's teaching objective, exercised on L06's hardest material. It spirals L06 C6+C7
AND L03 C4 (Ramp Up to Speed — the delay-loop ancestor of the whole motion-profile spine).

**Ramp arithmetic (verified):**

| | L05 | L06 | L07 | L08 |
|---|---|---|---|---|
| before | 2.20 | 2.62 | **1.83** | 2.00 |
| after | 2.20 | **2.29** | **2.29** | 2.00 |

L06-after and L07-after are identical — both 16/7 (doing 2.29, grasp 1.71). The L06→L07 crash is
eliminated entirely, and 2.20 → 2.29 → 2.29 is monotone non-decreasing. The honest cost: L06 pays
−0.33 and stops being the mid-book peak; the middle becomes a plateau, and L08's 2.00 becomes the
visible sag (−0.29) behind it. The ramp's break point moves from L07 (−0.79) to L08 (−0.29) —
a real improvement, smaller than v1.0 claimed. L07 gains a true Advanced/Deep capstone alongside
its existing Hard C6 square.

**Dependency verification (all passed against the live files):**
- L07's finished payload contains `static long averageCounts()` in `RobotMotion.cpp` — the same
  file the moved `driveDistanceTrapezoidal()` lands in, so the static scope is a non-issue — plus
  `TRIM`, `DRIVE_SPEED`, and `COUNTS_PER_CM` in `RobotConfig.h`. Every construct in the solution
  (while, if/else-if, float cast, encoder reset, abs) is taught by L06. §8-covers-§9 holds.
- "Trapezoid" appears nowhere in the book outside L06 except the single Maker kind row — no
  cross-lesson promises break (§24-safe).
- No challenge-count prose in L06 ("eight challenges" appears nowhere) — the count drop is silent.
- The `displayEncoderCounts` function dropped at L07's reorg is not used by this card.

**Honest cost — this is NOT a zero-Maker move.** L06 C8 rides `lesson=6&kind=trapezoidal`, a
single-file payload. Moved to L07 it needs a new `lesson=7` kind with the solution re-authored in
the 8-file architecture. That's a port, not a from-scratch authoring — the algorithm is done —
but it's Maker work: new kind, new payload, gate re-run, Maker version bump. Smaller than the
carried "author a new L07 capstone" task, and it produces the same outcome.

**Secondary effects to rule on if approved:**
- L06 drops 8→7 cards and loses its only Advanced. C6+C7 (both Hard) keep the top of L06 honest.
- Marker renumber: the moved card becomes 7.7 (global-uniqueness gate §4.2); L06's cards keep
  6.1–6.7 with no gap.
- The card's "Work in" changes from fresh-template to "your LastName_L07 build."
- `L06_GRAPHIC_6-11_trapezoid_motion_profile.svg` is referenced in the card AND in L06's
  image-manifest table — both the `<img>` reference and the manifest row travel with the move
  (the filename itself can stay; it is an asset name, not a claim).
- L07 C6's card already applies Challenges 2 and 3 in its capstone build; the moved card should
  slot AFTER C6 so the lesson ends on the port.

---

## 2. MOVES CONSIDERED AND REJECTED (with arithmetic)

**L10 C5 "The Obstacle That Is Really a Wall" (Adv/Deep) → L11.** Topically it IS L11 material
(line lost after a detour). But the move just relocates the dip: L10 2.60→2.00, L11 2.00→2.50 —
and L09 sits at 2.50, so L09→L10 becomes the new crash. A dip-swap, not a fix. **Rejected.**

**L04 C5 "The Centering Game" (Hard/Deep) → L08.** Centering-by-pivot is proto-line-following and
would spiral beautifully into a "redo it with the P term" card. But removing it drops L04 to 1.50 —
directly undoing S66's L04 re-rate that made the opening ramp monotone. Also the redo-with-P
version is a rewrite, i.e. authoring. **Rejected — mark it instead (L08 C2 already spirals it).**

**L08 C1/C2 (Easy tuning cards) → L15.** Raises L08's mean to ~2.25/2.50 by subtraction, but
Kp-tuning belongs in L08 pedagogically and C1/C2 feed the TDP A4 "P-control gain search" table.
Moving them starves the table's home lesson. (Exact figures: drop C1 → 2.25; drop C1+C2 → 2.67.)
**Rejected.**

**L06 C6 "Smooth Stopping" → L08 or L09.** Braking profiles apply to `driveDistance()`, not the
line loop; L09 C4 "Advance to Center" already IS the spiral of this idea in intersection context.
**Rejected — mark L09 C4 as building on L06 C6.**

**Anything out of L01 (N=11, mean 1.36).** L01's excess is deliberate opening volume, and its
cards seed three spines (below). Every candidate exit breaks a spine origin. **Rejected.**

**Conclusion from the rejections:** the ramp's remaining problems (L08 at 2.00, the L11 dip) are
not solvable by moves. L08 needs the carried capstone authoring; L11's dip is the priced-in cost
of S66's count fix.

---

## 3. THE SPINE MAP — what the book already spirals (verified touchpoints)

These exist in the content today. None is marked past L06. This is the marking backlog.

1. **THE SQUARE (marquee — five touchpoints):**
   L01 C6 *Does It Come Home?* (identical open-loop commands don't reproduce) →
   L03 C7 *Drive a Square* (delay-timed, Hard because open-loop turns are hard) →
   L06 C1 *The Square* (encoder-based, now Easy — the instrument did the work) →
   L07 C6 *Square Navigation Using All Modules* (same square, 8-file world) →
   L12 §7E *The Lesson 6 Square* (encoder vs. gyro corners, two surfaces).
   The square's difficulty rating falling 4→1 across L03→L06 while the task stays identical is
   the single best "instruments change what's hard" story in the book — currently untold.

2. **BATTERY:** L01 C11 *Battery Check* → L02 C2 *Battery Screen* → L03 C2 *Battery Warning
   (4200 mV)* → L11 (time lies on a tired battery — the lesson thesis) → L14 §4.3 battery
   management.

3. **MOTION PROFILE:** L03 C4 *Ramp Up* (delay-loop) → L06 C7 *Smooth Acceleration* (encoder) →
   L06 C8 *Trapezoidal* [→ L07 if the move ships] → L11 C3 *The Speed Budget* (deceleration
   mapped to budget-spent — the same profile idea inverted).

4. **PROPORTIONAL:** L05 C3 *Proximity-Based Beep Speed* (`beepInterval = 700 − value·100` — a
   P-term the student has already written, one lesson chapter before anyone says "proportional") →
   L08 (P control) → L15 (PID). L08 never mentions that its students have done this. High-value
   single marker.

5. **COUNTER/TALLY (six touchpoints):** L02 C3 *Button Counter* → L04 C2 *Line Counter* →
   L05 C1 *Detection Counter* → L10 C3 *Count and Report* → L13 C2 *The Sweep Report* →
   L14 C3 *The LoP Counter*. The same pattern (event → increment → display), climbing from
   toy to competition instrument.

6. **STATE CYCLING:** L03 C5 *Variable Speed Test* (B cycles 150→200→250→300→150 — a state
   machine nobody has named yet) → L09 (the state machine, named) → L13 C1 *Keep Sweeping*
   (hand control back to a state).

7. **OBSTACLE:** L05 C4 *Social Distancing* + C5 *Simple Obstacle Avoidance* → L10 (the whole
   lesson is the industrial version of L05 C5).

8. **CENTERING/LINE:** L04 C5 *The Centering Game* (pivot until centered = bang-bang) →
   L08 C2 *Wiggle Test* (oscillation named and tamed) → L09 C3 *Line-Seeking Turns*.

9. **TRUST/DEBOUNCE:** L09 C5 *Debounced Detection* (three consecutive reads) → L10 C4 *The Bump
   Guard* (hysteresis) → L14 (the self-test — don't trust, verify).

**Forward-spiral already in the book:** L07 C5 is literally titled "Prep for Lesson 8!" —
the only place the book currently marks a spiral in either direction past L06.

---

## 4. MARKING STATE (measured)

`Builds on:` + star-image markers: L02 ×2 · L03 ×3 · L04 ×1 · L05 ×1 · L06 ×1 · **L07–L16 ×0.**
All sixteen `spiral_star_NN.svg` files exist in `images/`; only stars 02/03/04 are referenced.
The S66 handoff logged the absence as "L10–L12"; it is actually the entire back half.

Marking does not move a single mean — it is visibility work, not balance work. But it is the
cheap half of "are we spiraling enough": the answer today is *substance yes, signal no.*

---

## 5. RECOMMENDED SEQUENCE (pending rulings)

1. Rule on the L06 C8 → L07 move (the only move that helps the ramp).
2. If approved: port the payload (new L07 kind), renumber to 7.7, bump L06 + L07 + Maker, gates.
3. Marking pass for the nine spines — a bounded, mechanical batch once the marker format for
   the back half is ruled (same `Builds on:` + star convention as L02–L06, or a lighter one).
4. L08 capstone stays an authoring task (carried) — no move reaches it.

---
*S67, Jul 24 2026. Extracted from live files, every quoted card verified against rendered text.*
