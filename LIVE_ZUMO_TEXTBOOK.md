# LIVE_ZUMO_TEXTBOOK.md

**Date:** July 20, 2026 (Session 57 — the construct sweep continues: `&&` `||` `!`).
**Status (S57, fourth batch):** ⚠️ **STAGED, NOT PUSHED.** Batches 1–3 are **LIVE** at commit `559831e`. This batch changes **one file**: **L02 v02.3.0 → v02.4.0**. No images, no Maker, no Bible, no gate change.

**Lesson versions — every one grepped from its own file, not carried forward:**
L01 v03.4.0 · L02 **v02.4.0** · L03 v03.5.0 · L04 v04.1.2 · L05 v04.2.0 · L06 v04.5.9 · L07 v04.3.10 · L08 v04.1.7 · L09 v05.0.9 · L10 v02.1.12 · L11 v02.2.2 · L12 v01.2.3 · L13 v02.2.2 · L14 v02.4.2 · L15 v02.2.3 · L16 v02.2.3 · Bible v8.36.1 · Maker v2.39 · Gate v1.6 · Harness v3.0.

---

## THE HEADLINE — `&&` WAS THE `if` DEFECT AGAIN, ONE SYMBOL DOWN

The full construct sweep (L01–L16, code blocks only) surfaced five more used-before-taught constructs. `&&` is the most urgent by the rule's own trigger — *do the §9 challenges ask students to write it?* — and it is a near-exact repeat of the `if` finding:

- **L02's own published challenge solutions use it:** `if (buttonA.isPressed() && buttonB.isPressed())` in Battery Screen, and `buttonA && buttonC` in Master Reset Combo.
- **`&&` is explained in none of the sixteen lessons.** Neither is `||` (first needed in L04 C04 Edge Guard — "any sensor sees the line") nor `!` (used 30+ times from L03 onward).

Two L02 challenges depend on a symbol the book never defines. Fixed at first contact, in the lesson that first needs it.

---

## WHAT SHIPPED — L02 §3.2d (v02.3.0 → **v02.4.0**)

**"Asking More Than One Question: `&&`, `||` and `!`"** — placed immediately after §3.2c's if statement, because that section teaches asking *one* question and this one teaches joining them. It follows the same read-it-aloud spine as 3.2c and 5.5:

- A three-row table mapping each operator to its English word: `&&` = *and* (both true), `||` = *or* (either true), `!` = *not* (flips the answer).
- **`&&`** taught through a range check (`count > 0 && count < 10`), with the warning students actually trip on: each side must be a whole question — `count > 0 && < 10` is an error, because `< 10` alone asks *below what?* Noted as the *loud* mistake, unlike the silent `=` trap in L03.
- **`||`** through two buttons, with the note that code's "or" is more generous than conversation's — it accepts both.
- **`!`** through the `bool foundLine` from §3.2b — "if we have NOT found the line" — with the debugging habit: when a condition behaves backwards, look for a `!` you missed.
- Keyboard note (`&&` is two ampersands, `||` is two pipes / shift-backslash) so the symbols can actually be typed.
- Coach's Tip: read the whole condition aloud as one sentence; if it doesn't make sense out loud it won't make sense to the robot. Points at this lesson's own challenges needing two buttons held at once.

Examples use buttons and counts, never a challenge's exact combo — the skill is taught without handing over the §9 answers.

**Coverage is now satisfied book-wide with this one addition:** §3.2d precedes every lesson that uses these operators (L02 §9, L04, L05, L08, L13, L15, L16). No spiral markers added elsewhere — there is no deep-dive section for the logical operators, so marking each use would be noise. No Bible change: this is an application of the existing v8.36.1 §11 rule, not a new one.

---

## VERIFICATION

- `count==1` asserts on all three edits; the moved banner (moderate bump) verified.
- Normalized diff: 99 changed lines, 2 removed (both the version strings).
- Structure: div 347/347, pre 87/87, tables 13/13, zero dup ids, zero dead anchors.
- The new `&&` table re-validated in isolation: 9/9 `<td>`, 4/4 `<tr>`, 3/3 `<th>`, renders with no stray tags.
- **Payload gate: PASS**, ADVISORY 635 — unchanged. Prose only.

---

## PUSH BATCH (S57, fourth batch)

1. **`lessons/Lesson_02.html`** (v02.4.0) → repo + Canvas.
2. **`LIVE_ZUMO_TEXTBOOK.md`** → repo root.

No images, no Maker, no Bible. Verify by fresh clone (§12.4).

_Housekeeping: a stray `.DS_Store` is still committed — clean up whenever, not urgent._

---

## THE SWEEP — WHERE IT STANDS

Constructs run through the §11 rule so far: **`if` ✅, `for` ✅, `&&`/`||`/`!` ✅.** Still open, in order of severity:

- **`while` — NEXT.** Used from L01, and **L06 leans on it 23 times** (`while (averageCounts() < target)` is the spine of every measured move). Taught nowhere. Worse: L05 §5.15 tells students *"You'll explore while loops in advanced behaviors later!"* — a forward-pointer to a lesson that never delivers, same defect class as L16's EEPROM claim. Wants a rung in L06 where it does real work.
- **`+=` / the three increment spellings** (`x = x + 1` / `x++` / `x += 1`) — used across the book, reconciled nowhere. Log candidate #7. Fits L03 §5.5.
- **`switch`** — mildest: one L05 use, properly taught in L09. A single forward-pointer in L05 closes it.

**Method note for the sweep:** prose-keyword matching finds *words*, not *teaching* — this session it falsely reported `while` as taught in L03 (all 14 hits were the English word) and mis-flagged the L04 image index. Verify every "taught" hit by reading it before trusting the column.

---

## STILL QUEUED

Finish the sweep (`while` → increments → `switch`, above) · L03_C05 Variable Speed learner mode · L04 C03 learner mode (**unblocked**) · L04 C04/C05 walkthroughs · "out-of-range values don't error" · C06 reorder to #1 · whole-template starters L08/L09/L10 · Maker batch (bulk DL · `?lesson=N` soft gate · C## labels) · L01 VS Code multi-root step.

**DONE this session:** L16 EEPROM · L04 `for` (§8A.6/8A.7) · L04 `setLayout21x8` (stated choice) · L04 image index (false alarm) · learnmode-log correction · `if` (L02 §3.2c / L03 §5.5 / L04 §8A) · `=` vs `==` (L03 §5.5) · **`&&`/`||`/`!` (L02 §3.2d).**

**BENCH (need robot):** C06 · C11 · Q017 L09 six numbers · Q044 calibration-spin · Q046 gyro-bias · L02 §5 green-LED · Constrain RUN_MS.

**PARKED:** solution-disclosure · monetization/ebook · "Know Your Zumo" · day-by-day grid + syllabus · TDP template v3 (A5 Lab Log) · §9 difficulty grouping · L06 card pattern.

**⚠️ AI TUTOR** — students get API access, syllabus has no entry, `tutor.html` stale (no L12+). **Term starts Sept 8.**

---
*Written S57, July 20 2026. Batches 1–3 LIVE (`559831e`); L02 v02.4.0 staged, not pushed.*
