# LIVE_ZUMO_TEXTBOOK.md

**Date:** July 20, 2026 (Session 57 — the construct sweep continues: `while`).
**Status (S57, fifth batch):** ⚠️ **STAGED, NOT PUSHED.** Batches 1–4 are **LIVE** at commit `5592276`. This batch changes **two files**: **L06 v04.5.9 → v04.6.0** (new §5.3) and **L05 v04.2.0 → v04.2.1** (dangling forward-pointer repaired). No images, no Maker, no Bible, no gate change.

**Lesson versions — every one grepped from its own file, not carried forward:**
L01 v03.4.0 · L02 v02.4.0 · L03 v03.5.0 · L04 v04.1.2 · L05 **v04.2.1** · L06 **v04.6.0** · L07 v04.3.10 · L08 v04.1.7 · L09 v05.0.9 · L10 v02.1.12 · L11 v02.2.2 · L12 v01.2.3 · L13 v02.2.2 · L14 v02.4.2 · L15 v02.2.3 · L16 v02.2.3 · Bible v8.36.1 · Maker v2.39 · Gate v1.6 · Harness v3.0.

---

## THE HEADLINE — THE BOOK'S MOST-USED UNTAUGHT CONSTRUCT, PLUS A PROMISE IT NEVER KEPT

`while` was used from Lesson 1 and taught in none of the sixteen lessons — and **L06 leans on it 23 times**, more than any other lesson. `while (abs(encoders.getCountsLeft()) < targetCounts)` is the literal heart of `driveDistance()` and `turnDegrees()`: every measured move in the book waits inside one. Students meet it at L06 Step 7 as a *translate-it-yourself* blueprint — asked to write a function whose body is a construct the book never explained.

And the gap had a second, uglier half. **L05 §5.15 explicitly promised** *"You'll explore while loops in advanced behaviors later!"* — a forward-pointer to a lesson that never delivered, the same defect class as L16's "never touched" EEPROM claim.

---

## WHAT SHIPPED

### 1. L06 §5.3 — *The while Loop: Waiting Until Something Happens* (v04.5.9 → **v04.6.0**)

Placed at the end of §5, immediately before Step 7 asks students to write `driveDistance()`. Carries a **🔁 Builds on:** marker with the ⭐4 star, because the teaching hinges on the contrast:

- **`for` vs `while` stated as two different questions.** `for` repeats a *known number of times* (once per sensor, eight, three); `while` repeats *as long as something stays true*, however many times that turns out to be. *You do not know in advance how many 10-ms checks it takes to roll 30 cm; you only know when to stop.*
- **The exact loop from `driveDistance()`**, walked as a sentence — motors told to run *once* before the loop, the loop itself doing nothing but watch, releasing the instant the count crosses target.
- A two-row decision table (known count → `for`; world-dependent → `while`).
- **The danger every while carries: it must be able to end.** A `for` counts to its own finish line; a `while` only stops when its condition goes false, so something inside must make that happen. Two accidental traps named — forgetting to start the motors, and a target the count can never reach — with the debugging habit: when a robot hangs mid-move, suspect the while condition first.
- Coach's Tip: whenever you write a `while`, answer out loud *what makes this stop?* before moving on. If you can't point at it, you've written an infinite loop and just haven't run it yet.

### 2. L05 §5.15 — the broken promise repaired (v04.2.0 → **v04.2.1**)

*"You'll explore while loops in advanced behaviors later!"* → *"You'll meet the while loop properly in Lesson 6, Section 5.3 — it is the heart of every measured move, driving until the encoders say you have gone far enough."* The forward-pointer now points at something real.

---

## VERIFICATION

- `count==1` asserts on every edit; L06 banners moved (moderate bump), L05 banner held (minor bump) — §5b.
- Normalized diff: L06 62 changed lines / 3 removed (version strings), L05 one-line swap + version.
- Structure: L06 div 207/207, pre 71/71, tables 14/14 · L05 div 142/142 — zero dup ids, zero dead anchors.
- **Payload gate: PASS**, ADVISORY 635 — unchanged. Prose only; the `while` in the reveal code was already there.
- Every `<img>` in L05 and L06 resolves against `images/`, including `spiral_star_04.svg`.

---

## PUSH BATCH (S57, fifth batch)

1. **`lessons/Lesson_05.html`** (v04.2.1) · **`lessons/Lesson_06.html`** (v04.6.0) → repo + Canvas.
2. **`LIVE_ZUMO_TEXTBOOK.md`** → repo root.

No images, no Maker, no Bible. Verify by fresh clone (§12.4).

_Housekeeping: a stray `.DS_Store` is still committed — clean up whenever, not urgent._

---

## THE SWEEP — WHERE IT STANDS

Constructs run through the §11 rule: **`if` ✅, `for` ✅, `&&`/`||`/`!` ✅, `while` ✅.** Still open:

- **`+=` / the three increment spellings** (`x = x + 1` / `x++` / `x += 1`) — used across the book, reconciled nowhere; `+=` first appears L03, heaviest in L15 (13×). Log candidate #7. Fits L03 §5.5.
- **`switch`** — mildest: one L05 use, properly taught in L09. A single forward-pointer in L05 closes it, mirroring the L05→L06 while fix just made.

After those two, every control-flow and operator construct the challenges require will have a teaching home at or before first write. **The sweep has only ever covered code blocks; it has not checked library-call vocabulary** (e.g. `map()`, `constrain()`, `millis()`) — those are a separate audit if wanted.

**Method note:** prose-keyword matching finds words, not teaching — three false readings this session (`while`-taught-in-L03, the L04 index, an L01 corruption false alarm). Read every "taught" hit before trusting it.

---

## STILL QUEUED

Finish the sweep (increments → `switch`) · L03_C05 Variable Speed learner mode · L04 C03 learner mode (**unblocked**) · L04 C04/C05 walkthroughs · "out-of-range values don't error" · C06 reorder to #1 · whole-template starters L08/L09/L10 · Maker batch (bulk DL · `?lesson=N` soft gate · C## labels) · L01 VS Code multi-root step.

**DONE this session:** L16 EEPROM · L04 `for` · L04 `setLayout21x8` · L04 index (false alarm) · learnmode-log correction · `if` · `=` vs `==` · `&&`/`||`/`!` · **`while` (L06 §5.3, L05 pointer repaired).**

**BENCH (need robot):** C06 · C11 · Q017 L09 six numbers · Q044 calibration-spin · Q046 gyro-bias · L02 §5 green-LED · Constrain RUN_MS.

**PARKED:** solution-disclosure · monetization/ebook · "Know Your Zumo" · day-by-day grid + syllabus · TDP template v3 (A5 Lab Log) · §9 difficulty grouping · L06 card pattern.

**⚠️ AI TUTOR** — students get API access, syllabus has no entry, `tutor.html` stale (no L12+). **Term starts Sept 8.**

---
*Written S57, July 20 2026. Batches 1–4 LIVE (`5592276`); L05 v04.2.1 + L06 v04.6.0 staged, not pushed.*
