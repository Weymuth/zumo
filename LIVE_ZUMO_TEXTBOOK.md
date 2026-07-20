# LIVE_ZUMO_TEXTBOOK.md

**Date:** July 20, 2026 (Session 57 — the construct sweep CLOSES: increments + `switch`).
**Status (S57, sixth batch):** ⚠️ **STAGED, NOT PUSHED.** Batches 1–5 are **LIVE** at commit `93de63a`. This batch changes **two files**: **L03 v03.5.0 → v03.6.0** (new §5.6) and **L05 v04.2.1 → v04.2.2** (`switch` forward-pointer). No images, no Maker, no Bible, no gate change.

**Lesson versions — every one grepped from its own file, not carried forward:**
L01 v03.4.0 · L02 v02.4.0 · L03 **v03.6.0** · L04 v04.1.2 · L05 **v04.2.2** · L06 v04.6.0 · L07 v04.3.10 · L08 v04.1.7 · L09 v05.0.9 · L10 v02.1.12 · L11 v02.2.2 · L12 v01.2.3 · L13 v02.2.2 · L14 v02.4.2 · L15 v02.2.3 · L16 v02.2.3 · Bible v8.36.1 · Maker v2.39 · Gate v1.6 · Harness v3.0.

---

## THE HEADLINE — THE CONSTRUCT SWEEP IS COMPLETE

Every control-flow and operator construct the challenges ask students to write now has a teaching home at or before first write. The last two were the mildest, and each was a different kind of gap:

- **The increment spellings were never reconciled.** `x++` *is* taught — one line inside L01's for-loop walkthrough. But `x += 1` (used L03, L08, L09, L15 heavily, L16) and `x = x + 1` (L04, L12, L15) are used across the book and **never once tied back to it.** A student who writes `count = count + 1` and meets `count += 1` in a reveal has no way to know they are identical. This is not a missing tool — it is three names for one tool, never introduced as such.
- **`switch` was a four-lesson forward gap.** Used once in L05 §5.13 (the display-mode dispatch), taught properly in L09. Students copy it in L05 with no idea what it is for four lessons.

---

## WHAT SHIPPED

### 1. L03 §5.6 — *Three Ways to Say "Add One"* (v03.5.0 → **v03.6.0**)

A single table putting all three spellings side by side against `testCount` going 4 → 5: `testCount = testCount + 1` (the long form, spells out every piece), `testCount += 1` (shorthand, takes any number), `testCount++` (shortest, only ever adds 1). Then the tie-back — *you already used the last one: `i++` is what steps a for loop* — and a rule of thumb: `++` for exactly 1, `+= n` for any other amount, long form when learning the line. Closes with the two things that trip people: there is no `++` for adding 5 (it is `+= 5`), and subtraction mirrors all three (`-= `, `--`).

Placed at the end of §5, after §5.5's if/comparison material — the same "writing statements" territory, and L03 is the first lesson to use `+=` in code.

### 2. L05 §5.13 — the `switch` forward-pointer (v04.2.1 → **v04.2.2**)

A one-paragraph note before the `loop()` block that contains the switch: what it does (picks one block based on a value), how to read it (a stack of `if` checks about the same variable, each `case` an answer, `break` ends it), and where it gets taught — *"Lesson 9 takes switch apart properly when the robot needs to choose between intersection types."* Copy-as-written for now. Same shape as the L05→L06 `while` pointer from the last batch.

---

## VERIFICATION

- `count==1` asserts on every edit; L03 banners moved (moderate), L05 banner held (minor) — §5b.
- Normalized diff: L03 51 changed lines / 3 removed (version strings), L05 4 changed / 1 removed.
- Structure: L03 div 316/316, pre 51/51, tables 21/21 · L05 div 142/142, pre 44/44, tables 16/16 — zero dup ids, zero dead anchors.
- **Payload gate: PASS**, ADVISORY 635 — unchanged. Prose only.
- Both new blocks re-read as rendered; no stray tags.

---

## PUSH BATCH (S57, sixth batch)

1. **`lessons/Lesson_03.html`** (v03.6.0) · **`lessons/Lesson_05.html`** (v04.2.2) → repo + Canvas.
2. **`LIVE_ZUMO_TEXTBOOK.md`** → repo root.

No images, no Maker, no Bible. Verify by fresh clone (§12.4). **Note:** the shallow clone can serve the *prior* commit for a minute or two after a push — if verify shows the old version, wait ~20 s and re-clone before concluding the push failed.

_Housekeeping: a stray `.DS_Store` is still committed — clean up whenever, not urgent._

---

## THE SWEEP — CLOSED

Every construct a §9 challenge asks students to WRITE now has a teaching home at or before first write:

| construct | taught in | first write |
|---|---|---|
| `if` | L02 §3.2c → L03 §5.5 → L04 §8A | L03 C02 |
| `for` | L04 §8A.6 / §8A.7 | L04 C03 |
| `&&` `\|\|` `!` | L02 §3.2d | L02 §9 |
| `while` | L06 §5.3 | L06 Step 7 |
| `=` vs `==` | L03 §5.5 | L03 C02 |
| `++` / `+=` / `= x+1` | L01 (++) + L03 §5.6 (reconciled) | L02 §9 |
| `switch` | L09, pointer from L05 §5.13 | L09 |

**Scope limit — read before assuming this class of defect is fully closed:** the sweep covered **control-flow and operators in code blocks only.** It did NOT audit **library-call vocabulary** — `map()`, `constrain()`, `millis()`, `abs()`, the `(cond) ? a : b` ternary (L06 Step 7 calls it "worth learning today" but nothing teaches it), `struct`/`enum` (L09/L16), arrays and indexing. Any of those could be the next used-before-taught finding; a second sweep would be its own session.

---

## STILL QUEUED

Library-vocabulary sweep (above) — ternary is the strongest lead · L03_C05 Variable Speed learner mode · L04 C03 learner mode (**unblocked**) · L04 C04/C05 walkthroughs · "out-of-range values don't error" · C06 reorder to #1 · whole-template starters L08/L09/L10 · Maker batch (bulk DL · `?lesson=N` soft gate · C## labels) · L01 VS Code multi-root step.

**DONE this session:** L16 EEPROM · L04 `for` · L04 `setLayout21x8` · L04 index (false alarm) · learnmode-log correction · `if` · `=` vs `==` · `&&`/`||`/`!` · `while` · **increments (L03 §5.6) · `switch` pointer (L05 §5.13).** Construct sweep CLOSED.

**BENCH (need robot):** C06 · C11 · Q017 L09 six numbers · Q044 calibration-spin · Q046 gyro-bias · L02 §5 green-LED · Constrain RUN_MS.

**PARKED:** solution-disclosure · monetization/ebook · "Know Your Zumo" · day-by-day grid + syllabus · TDP template v3 (A5 Lab Log) · §9 difficulty grouping · L06 card pattern.

**⚠️ AI TUTOR** — students get API access, syllabus has no entry, `tutor.html` stale (no L12+). **Term starts Sept 8.**

---
*Written S57, July 20 2026. Batches 1–5 LIVE (`93de63a`); L03 v03.6.0 + L05 v04.2.2 staged, not pushed.*
