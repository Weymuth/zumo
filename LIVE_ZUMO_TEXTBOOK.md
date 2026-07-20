# LIVE_ZUMO_TEXTBOOK.md

**Date:** July 20, 2026 (Session 57 — L16 EEPROM · the `for` hole · the layout nobody explained · **`if` taught at last**).
**Status (S57, third batch):** ⚠️ **STAGED, NOT PUSHED.** Batches one and two are **LIVE** at commit `f638539`. This batch changes **five files**: **L02 v02.2.4 → v02.3.0** · **L03 v03.4.7 → v03.5.0** · **L04 v04.1.0 → v04.1.2** · `L04_LEARNMODE_LOG.md` (annotated) · LIVE.md. No images, no Maker, no Bible, no gate change.

**Lesson versions — every one grepped from its own file, not carried forward:**
L01 v03.4.0 · L02 **v02.3.0** · L03 **v03.5.0** · L04 **v04.1.2** · L05 v04.2.0 · L06 v04.5.9 · L07 v04.3.10 · L08 v04.1.7 · L09 v05.0.9 · L10 v02.1.12 · L11 v02.2.2 · L12 v01.2.3 · L13 v02.2.2 · L14 v02.4.2 · L15 v02.2.3 · L16 v02.2.3 · Bible v8.36.1 · Maker v2.39 · Gate v1.6 · Harness v3.0.

---

## THE HEADLINE — THE NEW BIBLE RULE FIRED ON ITS FIRST SWEEP, AND `if` WAS WORSE THAN `for`

Bible v8.36.1 §11 says a construct the §9 challenges ask students to **write** must be taught in that lesson. Running that audit across L01–L05 found the same defect as the `for` loop, two lessons earlier:

| | L01 | L02 | L03 | L04 |
|---|---|---|---|---|
| `if (` in code | 3 | **20** | **18** | 26 |
| `else` | 1 | 5 | 5 | 11 |
| prose "if statement" | 0 | **0** | **0** | 15 |

L02 and L03 used conditionals **38 times between them and explained them zero times.** The only pre-L04 appearances of the vocabulary were a glossary definition of *Code Block* mentioning "conditionals" in passing and a challenge hint saying "trace the if/else."

Their challenges did not merely show ifs — they required writing them. **L03 C02 Battery Warning, rated EASY:** *"Make the OLED display 'LOW BATTERY!' if voltage drops below 4200 mV."* That challenge **is** an `if`; that is the whole task. L02 asks for three more (Battery Screen on A+B, Master Reset Combo, Backwards LED), two of them needing `&&`.

**This was worse than the `for` case in one specific way.** `for` sat behind a HARD-rated challenge, so a stuck student could reasonably blame the difficulty. **EASY** tells a student the opposite — *this should take five minutes* — while withholding the only tool the task needs. The label itself does the damage.

DJ ruling: **all three lessons get fixed** — first contact, first writing, full treatment.

---

## WHAT SHIPPED — ONE CONSTRUCT, THREE RUNGS

### 1. L02 §3.2c — *Making a Choice: the if Statement* (v02.2.4 → **v02.3.0**)

Placed immediately after §3.2b's data-types callout, which ends on `bool` — *"questions the robot answers yes or no … once the robot starts making decisions."* The new subsection picks that up in the next breath: **a bool holds the answer; an if is what does something about it.**

Deliberately small. It teaches reading, not writing: the condition as a yes/no question, the braces as the block they already met in §3.1, `else` as optional. It reads the exact if from this lesson's own first warm-up (`buttonC.isPressed()`), and it says plainly what it is *not* yet — enough to read every program in L02, not enough to write one from a blank line. Coach's Tip: say the condition in plain English out loud before looking inside the braces.

### 2. L03 §5.5 — *Writing a Decision: if, Comparison, and the One-Character Trap* (v03.4.7 → **v03.5.0**)

The rung that was missing under C02. Three moves: **start with the sentence** ("if the test speed is above 400, print a warning") and translate left to right, since the sentence and the code are in the same order; the **six comparison operators** in a table, with the note that `>` and `>=` differ by exactly one case — the value sitting on the line, which is where robot bugs live; then `else` / `else if` chains, checked top to bottom with exactly one branch firing.

The centrepiece is **the `=` vs `==` trap**, the top-rated item in `L04_LEARNMODE_LOG.md` ("highest-value item from this session; hit repeatedly and never errors"). Both failure directions, each with its silent symptom:

- `if (trimValue = 5)` — assigns 5 **and** tests 5, which C++ treats as true, so the block runs forever and TRIM is quietly overwritten.
- `trimValue == 5;` — compares, throws the answer away, changes nothing. *You will swear you set it, and the robot will swear you did not, and the robot is right.*

Closing habit: when a condition seems stuck — always firing or never firing — **count the equals signs before questioning your logic.**

Examples deliberately use speed, not battery: C02 is a battery `if`, and the section teaches the skill without handing over the challenge.

### 3. L04 §8A — the spiral's top rung (v04.1.0 → **v04.1.2**)

§8A carried a **🔁 Builds on:** marker naming both sources in words with ⭐2 and ⭐3 stars, and two claims were corrected. The intro no longer promises to make you own the if *first* — it makes you own it *completely*. And §8A.1 opened with *"Until now, your programs have been a straight road"* — false for a reader who has been writing conditionals since Lesson 3. It now names the actual escalation: **Lesson 3 had you writing them against a number you typed yourself; from here the number arrives from a sensor and changes while the robot is moving.**

*(This batch also carries L04 v04.1.1 from earlier today — the `setLayout21x8` layout-choice work and the index-order repair — since it had not been pushed yet.)*

### 4. `L04_LEARNMODE_LOG.md` — annotated, not rewritten

A teaching record (Bible §19), so what DJ hit stays as observed and resolutions are appended and dated. The §5.13 → **§5.15** citation error corrected in place and marked. The C03 finding now carries its ruling — **none of options a–d; option (e), teach it in L04** — and records why (c) died: unrolling C03's loop would have stripped `for` from two challenges while it stayed in eight places elsewhere in the same lesson. C03 drops "misscoped" and stays **HARD**; the next learner-mode session is marked **unblocked**.

---

## VERIFICATION

- `count==1` asserts on every edit across four files; L04's visible banners asserted **unchanged** (minor bump), L02 and L03 banners moved with their moderate bumps (§5b).
- Normalized diffs: L02 39 changed lines / 2 removed · L03 118 / 3 · L04 9 / 3 · log 26 / 5 — every removal an intended in-place replacement.
- Structure: L02 div 342/342, pre 84/84 · L03 div 315/315, pre 51/51, tables 20/20 · L04 div 158/158 — zero dup ids, zero dead anchors anywhere.
- L02's new code block re-read after extraction to confirm no escaped-tag artifact: 1 `<pre>`, 1 `</pre>`, zero `&lt;pre`.
- **Payload gate: PASS**, ADVISORY 635 — unchanged. Prose only; no code or payload touched.
- Every `<img>` in L02, L03 and L04 resolves against `images/`, including `spiral_star_02.svg` and `spiral_star_03.svg`.

---

## PUSH BATCH (S57, third batch)

1. **`lessons/Lesson_02.html`** (v02.3.0) · **`lessons/Lesson_03.html`** (v03.5.0) · **`lessons/Lesson_04.html`** (v04.1.2) → repo + Canvas.
2. **Root docs:** `L04_LEARNMODE_LOG.md` · `LIVE_ZUMO_TEXTBOOK.md`.

No images, no Maker, no Bible. Verify by fresh clone and check **which version** landed (§12.4).

_Housekeeping: a stray `.DS_Store` is still committed — `git rm .DS_Store` + a `.gitignore` line whenever, not urgent._

---

## THE AUDIT IS NOT FINISHED

Two constructs have now been run through the §11 rule — `for` and `if`. **The sweep covered L01–L05 only.** L06–L16 have never been checked against it, and the log's own list names more candidates that were never traced to a teaching home: the three spellings of increment (`x = x + 1` / `x++` / `x += 1`, used across the book, taught nowhere), `;` vs `}`, the stray-semicolon killer, `&&` and `||`, and `switch`/`case` (L05 uses it). Finish the sweep before assuming the class of defect is closed.

---

## STILL QUEUED

Finish the construct sweep L06–L16 (above) · L03_C05 Variable Speed learner mode · L04 C03 learner mode (**unblocked**) · L04 C04/C05 walkthroughs (log rows still empty) · the remaining syntax-gap candidates + "out-of-range values don't error" · C06 reorder to #1 · whole-template starters L08/L09/L10 · Maker batch (bulk DL · `?lesson=N` soft gate · C## labels) · L01 VS Code multi-root step.

**DONE, removed from queue:** L16 EEPROM prose + address map · L04 `for` primer (became §8A.6/8A.7) · L04 `setLayout21x8` (not a defect — now a stated choice) · L04 image index (false alarm) · `L04_LEARNMODE_LOG.md` correction · **`=` vs `==`** (now L03 §5.5).

**BENCH (need robot):** C06 · C11 · Q017 L09 six numbers · Q044 calibration-spin · Q046 gyro-bias · L02 §5 green-LED · Constrain RUN_MS.

**PARKED:** solution-disclosure · monetization/ebook · "Know Your Zumo" · day-by-day grid + syllabus · TDP template v3 (A5 Lab Log) · §9 difficulty grouping · L06 card pattern.

**⚠️ AI TUTOR** — students get API access, the syllabus has no entry for it, `tutor.html` is stale with no L12+ content. **Term starts Sept 8.**

---
*Written S57, July 20 2026. Batches 1–2 LIVE (`f638539`); L02 v02.3.0 + L03 v03.5.0 + L04 v04.1.2 + the annotated log staged, not pushed.*
