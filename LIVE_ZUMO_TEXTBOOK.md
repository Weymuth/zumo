# LIVE_ZUMO_TEXTBOOK.md

**Date:** July 20, 2026 (Session 57 — the library-vocabulary sweep: `abs()` + the ternary).
**Status (S57, seventh batch):** ⚠️ **STAGED, NOT PUSHED.** Batches 1–6 are **LIVE** at commit `b8f7c1b`. This batch changes **one file**: **L06 v04.6.0 → v04.7.0** (new §5.4 + a repointed Step 7 aside). No images, no Maker, no Bible, no gate change.

**Lesson versions — every one grepped from its own file, not carried forward:**
L01 v03.4.0 · L02 v02.4.0 · L03 v03.6.0 · L04 v04.1.2 · L05 v04.2.2 · L06 **v04.7.0** · L07 v04.3.10 · L08 v04.1.7 · L09 v05.0.9 · L10 v02.1.12 · L11 v02.2.2 · L12 v01.2.3 · L13 v02.2.2 · L14 v02.4.2 · L15 v02.2.3 · L16 v02.2.3 · Bible v8.36.1 · Maker v2.39 · Gate v1.6 · Harness v3.0.

---

## THE HEADLINE — A SECOND SWEEP, TWO MORE REAL GAPS, BOTH IN THE SAME FUNCTION

The first sweep covered control-flow and operators. This one covered **library calls and language features** — `map`, `constrain`, `abs`, `millis`, the ternary `?:`, `enum`, `array`, `struct`. Reading every "taught" hit by hand (the prose-keyword regex produced **four more false positives**, matching the word `milliseconds` for `millis`, a stray `?:` in prose for the ternary, `abs(` inside code for `abs`, and a challenge hint for `array`), the picture came out clean except for two genuine gaps — and they land in the same place.

**`abs()` and the ternary `?:` are both first used in `driveDistance()`, the function students write at L06 Step 7, and both are taught nowhere.** Worse, each is a dangling promise inside L06 itself: the §9 challenge hint says *"Use abs() to convert negative changes to positive values"* (the challenge fails without it), and Step 7 prose calls the ternary *"the (condition) ? a : b pick — worth learning today"* and then never delivers.

---

## WHAT SHIPPED — L06 §5.4 (v04.6.0 → **v04.7.0**)

Placed immediately after §5.3 (the `while` rung from the last batch) and immediately before Step 7 — *Two Small Tools This Function Needs: `abs()` and `?:`.*

- **`abs()`** taught as "how far from zero, direction thrown away," then the bug that makes it non-optional: drive `-30`, and `targetCounts = -30 * COUNTS_PER_CM` is a *negative* target that the encoder count (starting at 0) is already past, so the `while` exits before the wheels turn. Wrap it in `abs()` and the target is always reachable whichever way the robot drives. Forward-links to Step 13, where `abs()` on each wheel's change keeps a measurement positive.
- **The ternary `?:`** taught as *an if that hands back a value* — question at `?`, yes-answer and no-answer split by `:` — shown against the exact `int speed = (distanceCm > 0) ? DRIVE_SPEED : -DRIVE_SPEED;` line from the function, then written out as the identical four-line `if/else` so the equivalence is concrete. Guidance: reach for `?:` only when choosing between two values for one variable; anything longer, use the full `if/else`. Coach's Tip: if `?:` makes your head hurt, write the `if/else` — it compiles to the same thing.
- **Step 7's dangling aside repointed:** *"worth learning today"* now reads *"both it and the abs() on the line above are unpacked in Section 5.4, just above,"* linking to `#code-6-4`.

---

## VERIFICATION

- `count==1` asserts on every edit; L06 banners moved (moderate bump) — §5b.
- Normalized diff: 58 changed lines / 4 removed (3 version strings + the repointed aside line).
- Structure: div 208/208, pre 75/75, tables 14/14, zero dup ids, **zero dead anchors** — the new `#code-6-4` link resolves.
- **Payload gate: PASS**, ADVISORY 635 — unchanged. Prose only; `abs()` and the ternary were already in the reveal code.
- §5.4 re-read as rendered; no stray tags.

---

## PUSH BATCH (S57, seventh batch)

1. **`lessons/Lesson_06.html`** (v04.7.0) → repo + Canvas.
2. **`LIVE_ZUMO_TEXTBOOK.md`** → repo root.

No images, no Maker, no Bible. Verify by fresh clone (§12.4) — allow ~20 s for the shallow-clone cache after pushing before concluding a version didn't land.

_Housekeeping: a stray `.DS_Store` is still committed — clean up whenever, not urgent._

---

## BOTH SWEEPS — WHERE THEY STAND

**Control-flow / operators (sweep 1): CLOSED.** `if` · `for` · `&&`/`||`/`!` · `while` · `=` vs `==` · increments · `switch` — all taught at or before first write.

**Library vocabulary (sweep 2): the two real gaps are now closed.** Verified-clean: `constrain()` (L03 §3.9), `enum` (L09), `array` (L03). Fixed this batch: `abs()`, ternary `?:` (L06 §5.4).

**Still thin, deliberately left as queued minor notes:**
- **`millis()`** — has a real Quick-Reference row ("milliseconds since power-on — the robot's stopwatch") from L02, so it is *documented*, but never taught as a concept before L14/L15 lean on it for timing. A QR row is genuine coverage; promote it to a short taught note only if a challenge is found that requires *writing* millis-based timing.
- **`map()`** — used once (L08 `map(pos,0,4000,0,20)` for the position bar), taught nowhere. Genuinely minor; one L08 note closes it. First-use is in given code, not a student-write, so it is the lowest priority of everything found.

Neither is a challenge-blocking gap; both are recorded so they are not rediscovered as phantoms.

---

## STILL QUEUED

`millis()` taught-note + `map()` note (above, minor) · L03_C05 Variable Speed learner mode · L04 C03 learner mode (**unblocked**) · L04 C04/C05 walkthroughs · "out-of-range values don't error" · C06 reorder to #1 · whole-template starters L08/L09/L10 · Maker batch (bulk DL · `?lesson=N` soft gate · C## labels) · L01 VS Code multi-root step.

**DONE this session:** L16 EEPROM · L04 `for` · L04 `setLayout21x8` · L04 index (false alarm) · learnmode-log correction · `if` · `=` vs `==` · `&&`/`||`/`!` · `while` · increments · `switch` pointer · **`abs()` + ternary (L06 §5.4).** Both construct sweeps effectively closed.

**BENCH (need robot):** C06 · C11 · Q017 L09 six numbers · Q044 calibration-spin · Q046 gyro-bias · L02 §5 green-LED · Constrain RUN_MS.

**PARKED:** solution-disclosure · monetization/ebook · "Know Your Zumo" · day-by-day grid + syllabus · TDP template v3 (A5 Lab Log) · §9 difficulty grouping · L06 card pattern.

**⚠️ AI TUTOR** — students get API access, syllabus has no entry, `tutor.html` stale (no L12+). **Term starts Sept 8.**

---
*Written S57, July 20 2026. Batches 1–6 LIVE (`b8f7c1b`); L06 v04.7.0 staged, not pushed.*
