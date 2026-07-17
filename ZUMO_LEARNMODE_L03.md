# ZUMO — Learning-Mode Record · Lesson 03 (Motors & TRIM)

> **What this file is.** A durable record of the Socratic learner-mode walkthrough of every L03 challenge (C01–C06), captured so it can (a) feed the AI Tutor rebuild, (b) surface the concepts students will need explicitly taught, and (c) flag the specific places a student is likely to stall.
>
> **Bible reference:** the Bible points here for L03 learner-mode detail (see Bible §-entry for the learning-mode file convention). This file holds the *teaching path + difficulty detail*; the **Code Templates and solutions live separately** in `ZUMO_L03_TEMPLATES.md`.
>
> **Naming:** exchanges follow the `L##_C##_W##` canon (Lesson-Challenge-Walkthrough-step).
>
> **Status:** learner-mode reconstruction, DJ walked C01–C06 in Session 47. NOT a book edit — nothing here is pushed. The findings below are QUEUED for a future L03 edit pass.

---

## ⚠️ STUDENT-DIFFICULTY ROLL-UP (scan this first)

Every stall DJ hit in the walkthrough, flagged by how likely a student is to hit the same thing. These are the places to pre-empt in prose, a Coach's Tip, or the live demo.

| # | Challenge | The stall | Student-likely? | Pre-empt with |
|---|---|---|---|---|
| 1 | C01 | `runSpinTest ()` vs `runSpinTest()` — space before `()`; case typo `runSpintest` vs `runSpinTest` | ⚠️ HIGH | note C++ is case-sensitive; names must match exactly |
| 2 | C01 | **Call placed before the definition → no prototype → won't compile.** "Prototype" is used in the template but never taught. | ⚠️⚠️ VERY HIGH | **used-but-never-taught: add a prototype explainer to L03** |
| 3 | C01 | Missing `Zumo32U4Motors motors;` in the downloaded starter → `'motors' was not declared` | ⚠️⚠️ VERY HIGH (starter defect, hits everyone) | **fix the starter payload** (see TEMPLATES file) |
| 4 | C02 | Wrote `int readBatteryMillivolts();` (a prototype) instead of `int mv = readBatteryMillivolts();` (a call that stores the result) | ⚠️ HIGH | show the "call + catch the return value" shape explicitly |
| 5 | C02 | `if` syntax: parens around the wrong thing, `{` inside the condition parens, stray `;` after `)` | ⚠️⚠️ VERY HIGH | teach the `if (cond) { }` anatomy as a unit |
| 6 | C02 | `Print` vs `display.print`; missing `F()` wrapper on strings | ⚠️ MEDIUM | reinforce the display-print + `F()` convention |
| 7 | C02 | `display.clear()` placement — clear-always vs clear-only-when-warning | ⚠️ MEDIUM (design, not compile) | draw out the placement tradeoff in the card |
| 8 | C03 | **`const` vs `constrain()` confusion** — used the wrong one repeatedly even with the amber callout present | ⚠️⚠️ VERY HIGH | the amber callout may not be landing; consider goal→logic→template card |
| 9 | C03 | **Nesting `constrain()` inside `setSpeeds()`** — floated the calls on their own lines instead of as arguments | ⚠️⚠️ VERY HIGH | name the pattern: "a function call goes where the number would go" |
| 10 | C03 | comma rules (between args, none after the last) + closing `;` | ⚠️ HIGH | recurring across every multi-arg call |
| 11 | C04 | `set.Motors` / `motor.setSpeed` vs `motors.setSpeeds` (object `s`, method `s`) | ⚠️ HIGH | the object is `motors`, the method is `setSpeeds` |
| 12 | C04 | Ramped past the cap (250) — card says stop AT MAX_SPEED | ⚠️ MEDIUM | reinforce "up to the cap, not past" |
| 13 | C04 | **"It compiled" was a STALE BUILD** — deleted a `;`, still showed SUCCESS | ⚠️⚠️ VERY HIGH (toolchain) | **Coach's Tip: Clean → Build before trusting a result** |
| 14 | C04 | **Editor buffer vs file on disk drifted** — pasted code ≠ compiled code | ⚠️⚠️ VERY HIGH (toolchain) | **Coach's Tip: the compiler judges the file on disk** |
| 15 | C04 | **Errors surface one at a time** — `motor` typo masked the missing `;` | ⚠️ HIGH (toolchain) | **Coach's Tip: fix the top error, rebuild, next appears** |
| 16 | C05 | **Modulo misunderstood** — hand-wrote 5 lines changing `% 0,1,2,3` instead of ONE line `% NUM_SPEEDS` | ⚠️⚠️ VERY HIGH | the modulo explainer (S46) helps; watch it still lands |
| 17 | C05 | **Zero-indexing** — arrays start at slot 0; reveal starts index at 1 (=200) without explaining why 1 isn't first | ⚠️ HIGH | used-but-not-stated: add a one-liner on 0-based slots |
| 18 | C05 | `int speedIndex ();` — parens make it look like a function, not a variable | ⚠️ HIGH | same parens-vs-`=` trap as C03/C06 |
| 19 | C06 | `constant` (not a keyword) / `(10)` parens / line commented out | ⚠️ HIGH | same declare-shape trap; a commented line is invisible |
| 20 | C06 | **Scope** — declared `int trimValue` a SECOND time inside `setup()`, shadowing the global | ⚠️⚠️ VERY HIGH | teach global-vs-local: declare shared state ONCE, globally |
| 21 | C06 | case mismatch `TrimValue` vs `trimValue` | ⚠️ MEDIUM | case-sensitivity again |

**Cross-cutting patterns worth a single up-front treatment:**
- **parens-vs-`=` for declaration** (`NAME (value)` instead of `NAME = value`) recurred in C03, C05, C06. One explicit rule would kill three stalls.
- **case-sensitivity** recurred in C01, C04, C06.
- **toolchain trust** (C04) cost more time than any language concept — stale builds + editor/disk drift.

---

## THE THREE NEW COACH'S TIPS (from C04 — queued for the book)

Same class as the AI-autocomplete and upload/power-on tips already in L03:

1. **"It compiled" can be a stale build.** If a change seems to have no effect, run **Clean → Build**. PlatformIO reuses the last good build and will show green on code it never recompiled.
2. **The compiler judges the file on disk, not your editor tab.** If the result doesn't match what you wrote, dump the saved file (`type src\main.cpp` / `cat src/main.cpp`) and debug *that*. Save before you build.
3. **Errors surface one at a time.** An early error (e.g. `motor` vs `motors`) hides later ones (a missing `;`). Fix the top error, rebuild, and the next real problem appears.

---

## PER-CHALLENGE WALKTHROUGH DETAIL

### C01 — Add a Spin Test (EASY)
**Concept:** a `void` helper function; opposite-sign wheel speeds = spin; run-then-stop sequence; **the function prototype** (the genuinely new/untaught idea).

**Teaching path that worked:** opposite signs → spin → `delay` holds → `setSpeeds(0,0)` stops → order matters → `void` wrapper → wire the call into `setup()`.

**Where DJ stalled (inline):**
- `runSpinTest ()` had a space before `()`; the call `runSpintest()` had a lowercase-t typo mismatching the definition `runSpinTest`. → **case-sensitivity, names must match.** [W-flag #1]
- Wrote the header as `void runSpinTest{` (missing `()`). [W-flag #1]
- **The real blocker:** the call sat in `setup()` *above* the definition, with no prototype → won't compile. DJ didn't remember what a prototype was. → **"prototype" is used in the template's `FUNCTION PROTOTYPES` section but never explained in L03 prose.** [W-flag #2 — VERY HIGH]
- The downloaded starter was missing `Zumo32U4Motors motors;`, causing `'motors' was not declared`. → **starter payload defect.** [W-flag #3]

**Finding:** the prototype concept needs an explicit L03 explainer (return type + name + `()` + `;` = a promise the function exists below). Same class as the modulo/1000ms finds.

---

### C02 — Battery Warning System (EASY)
**Concept:** a decision — `if (condition)`; read a sensor value into a variable; act only when true; `return` to skip; clean display sequence.

**Teaching path that worked:** read voltage into a variable → build the `if` frame (parens around the condition, braces after) → put the action inside → clean the screen before printing.

**Where DJ stalled (inline):**
- Wrote `int readBatteryMillivolts();` — a prototype, not a call. Needed `int mv = readBatteryMillivolts();` (box + `=` + call). → **declare-vs-call confusion.** [W-flag #4]
- `if` syntax tangled: `if mv <4200 (Print "LOW BATT");` then `if (mv <4200 {Print...})` — parens around the wrong thing, brace inside the condition, stray `;`. → **teach `if (cond) { }` anatomy as one unit.** [W-flag #5 — VERY HIGH]
- `Print` (wrong) vs `display.print`; missing `F()`. [W-flag #6]
- Placed `display.clear()` before the `if` (clears every loop) vs the reveal's inside-the-`if` placement (clear only when warning). Ended up matching the reveal. → **design teaching point not currently drawn out.** [W-flag #7]

**Finding:** C02 card hint says "add a check at the start of `updateDisplay()`" — assumes the *finished* program. The clean Code Template has no `updateDisplay()`; the check goes directly in `loop()`. Card hint is finished-program-path only.

---

### C03 — Clamp the Speed with constrain() (EASY)
**Concept:** `const` (declare) vs `constrain()` (clamp) — the lookalike trap; nesting a function call as an argument; the "past the cap, bigger numbers do nothing" aha.

**Teaching path that worked:** declare three `const int` speeds → then use `constrain()` INSIDE `setSpeeds()` where the number would go → run/stop → prove 250 == 200.

**Where DJ stalled (inline):**
- **The big one:** repeatedly mixed `const` and `constrain()` — wrote `constrain LEFT_SPEED (150,100,200)` trying to *declare*. Even with the amber callout present. → **the callout may not be landing; candidate for the goal→logic→template card treatment.** [W-flag #8 — VERY HIGH]
- Used parens to declare: `const int LEFT_SPEED (150);` instead of `= 150`. → **parens-vs-`=` trap.** [W-flag #cross]
- **Floated the `constrain()` calls on their own lines** below an empty `setSpeeds ()` instead of nesting them as its arguments. Took several rounds to land "the constrain goes INSIDE setSpeeds, in the slot where a speed number sits." [W-flag #9 — VERY HIGH]
- comma between args / no comma after the last / closing `;`. [W-flag #10]

**Finding:** "a function call goes where a value would go" (nesting as argument) is a genuine, unnamed pattern in the prose. The reveal shows it; nothing names it.

---

### C04 — Ramp Up to Speed (MEDIUM)
**Concept:** changing a value over time; hand-unrolled fixed steps (Ramp Option C — NO `for` loop, that's L05); stop AT the cap. *(DJ first did this in S45.)*

**Teaching path that worked:** two constants (MAX_SPEED, STEP_MS) → hand-write the climb 50→100→150→MAX_SPEED, one setSpeeds+delay per rung → stop at the cap → setSpeeds(0,0).

**Where DJ stalled (inline):**
- `set.Motors` / `motor.setSpeed` vs `motors.setSpeeds` (missing the `s` on both object and method). [W-flag #11]
- Ramped to 250 — past the 200 cap the card says to stop at. [W-flag #12]
- **The toolchain saga (cost the most time):** deleted a `;`, build still said SUCCESS. Chased it down to (a) **stale build cache** — Clean→Build was needed; (b) **editor buffer ≠ file on disk** — pasted code differed from compiled code; (c) the `motor` typo was an EARLIER error **masking** the missing `;` — errors surface one at a time. [W-flags #13, #14, #15 — all VERY HIGH toolchain]
- Skipped declaring MAX_SPEED / STEP_MS as constants (used literals).

**Finding:** produced the three Coach's Tips above. These will cost students more time than any C++ rule in a self-paced flipped class.

---

### C05 — Variable Speed Test (MEDIUM — the hardest rung)
**Concept:** array (list of speeds) + index (which slot) + modulo `%` (wrap the index). Three new ideas at once.

**Teaching path that worked (good model for the AI Tutor):** isolate each of the three ideas before combining. Array first → index second (as a global, NOT const, because it changes) → then use them in `loop()`: wait for B → read `TEST_SPEEDS[speedIndex]` → run → advance with `% NUM_SPEEDS`. Trace the modulo BY HAND.

**Where DJ stalled (inline):**
- **Modulo misunderstanding:** wrote FIVE lines, each changing the divisor `% 0, % 1, % 2, % 3, % 0` — thinking he had to hand-write each step. The insight: it's ONE line, run repeatedly; the same `% NUM_SPEEDS` produces different results because `speedIndex` carries over. `% 0` would crash (divide by zero). [W-flag #16 — VERY HIGH]
- **Zero-indexing** not internalized — reveal starts index at 1 (=200) without explaining why 1 isn't the first slot. [W-flag #17]
- `int speedIndex ();` — parens made it look like a function. [W-flag #18]
- A stray `int speedIndex ();` leaked into FUNCTION PROTOTYPES, redeclaring the variable as a function → redeclaration error.

**DJ's own note:** "I like how you structured that learn mode for 05. Learned stuff, but not frustrated." → the isolate-each-idea-then-combine + trace-by-hand structure is the model to reuse.

**Finding:** C05 starter refs `finished` (same defect as C01). Zero-indexing is used-but-not-stated.

---

### C06 — Save TRIM to Code (EASY)
**Concept:** persistence (hard-code a bench-found value); name your magic numbers (`const` + a working variable that starts from it); **variable scope** (global vs local).

**Teaching path that worked:** `const int MY_TRIM = <found value>;` → `int trimValue = MY_TRIM;` (global, starts from the constant) → the drive code uses `trimValue`.

**Where DJ stalled (inline):**
- `constant` (not a keyword) instead of `const int`; `(10)` parens instead of `= 10`; the whole line commented out (invisible to compiler). [W-flag #19]
- **Scope:** declared `int trimValue` a SECOND time INSIDE `setup()`, shadowing the global. The rule that fixed it: declare shared state ONCE, globally, so every function sees the same one; a re-declaration inside a function is a separate local copy. [W-flag #20 — VERY HIGH]
- case mismatch `TrimValue` vs `trimValue`. [W-flag #21]
- `setup()` used `myTrimValue` directly instead of `trimValue` — compiles and drives straight, but sidesteps the point (trimValue declared-but-unused).

**Finding:** C06 starter refs `finished` (same defect). Scope (global vs local) is a big concept that arrives implicitly here; worth an explicit note since later lessons rely on shared globals heavily.

---

## QUEUED L03 EDIT TASKS (consolidated from all findings above)

1. **Fix the L03 challenge starters.** C01/C05/C06 (and per handoff, L08/L09/L10) reference a `finished` payload that does not exist for L03 → the Maker emits the blank scaffold while the cards claim "preloaded with the finished lesson program." Repoint to the whole-template Code Templates (staged in `ZUMO_L03_TEMPLATES.md`), and fix the card text. Coordinated Maker + card edit; bumps L03 + Maker.
2. **Add a prototype explainer** to L03 (used-but-never-taught). [C01]
3. **Add the three Coach's Tips** (stale build / disk-not-editor / errors-one-at-a-time). [C04]
4. **Add a one-liner on zero-based array slots.** [C05]
5. **Consider a global-vs-local scope note.** [C06]
6. **Watch whether the `const` vs `constrain()` amber callout lands** — candidate for the goal→logic→template card pattern if students keep tripping. [C03]
7. **Adopt "Code Template"** as the standard term (retire "scaffold") — pending DJ's project-wide-vs-walkthrough-only ruling.

---
*Learner-mode record · Lesson 03 · Session 47 · staging, not pushed · templates in ZUMO_L03_TEMPLATES.md*
