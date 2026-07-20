# LIVE_ZUMO_TEXTBOOK.md

**Date:** July 20, 2026 (Session 57 — L16 EEPROM, then the `for`-loop hole in L04).
**Status (S57, second batch):** ⚠️ **STAGED, NOT PUSHED.** The first S57 batch (L16 v02.2.3, Bible v8.36) is **LIVE and verified** by fresh clone at commit `622f8c6`. This second batch changes three files and adds one image: **L04 v04.0.12 → v04.1.0** · **L05 v04.1.9 → v04.2.0** · **Bible v8.36 → v8.36.1** · **NEW** `images/L04_GRAPHIC_4-06_for_anatomy.svg`. No Maker change, no gate change.

**Lesson versions — every one grepped from its own file, not carried forward:**
L01 v03.4.0 · L02 v02.2.4 · L03 v03.4.7 · L04 **v04.1.0** · L05 **v04.2.0** · L06 v04.5.9 · L07 v04.3.10 · L08 v04.1.7 · L09 v05.0.9 · L10 v02.1.12 · L11 v02.2.2 · L12 v01.2.3 · L13 v02.2.2 · L14 v02.4.2 · L15 v02.2.3 · L16 v02.2.3 · **Bible v8.36.1** · Maker v2.39 · Gate v1.6 · Harness v3.0.

---

## THE HEADLINE — L04 HAD A HOLE WHERE ITS SECOND TUTORIAL BELONGED

The queue called this "L04 C03 `for` primer — missing prerequisite." Investigation found something different and worse:

- L04 **uses** `for` in its own taught code — **8 times in the lesson, 5 times in its Maker payloads** — and has students type one in Step 4.
- L04 **explains** it in exactly one sentence, in passing.
- L04 §9 then requires it twice: **C03**'s published solution runs a `for` loop, and **C04**'s card tells students to use one.
- The formal tutorial sits in **L05 §5.15** — analogy, anatomy figure, worked examples, checkpoint — opening with *"Before tackling the challenges, make sure you understand for loops."* First contact, one lesson too late.

So this was never an untaught construct sneaking into a challenge. **L04 has a §8A that teaches `if` and stops.** Its own §8A intro states the rule it then half-follows: *"the challenges in Section 9 use it immediately; this section makes sure you own it first."* The `if` half was built. The `for` half never was.

That also explains the art: `L04_GRAPHIC_4-01_if_anatomy.svg` and `L05_GRAPHIC_5-04_for_anatomy.svg` are one figure family split across two lessons — the designed pair drifted when L04's code started using loops.

---

## WHAT SHIPPED

### 1. L04 §8A gains its second half (v04.0.12 → **v04.1.0**)

**§8A.6 — Doing It Three Times Without Writing It Three Times.** Opens with the loop the student *already typed* in Step 4, then makes the argument no other lesson in the book can make: Act One reads 3 sensors, Act Two reads 5, and the loop is the reason that switch cost one character instead of a rewrite. A lap-by-lap trace table (i = 0, 1, 2, then the failing test at i = 3) ties the loop's stopping point back to §5.5's zero-counting rule. Closes on the two loops that never end — a missing `i++`, and the stray semicolon after the parentheses. Both compile clean; neither is the compiler's problem.

**§8A.7 — A Loop with a Decision Inside.** Teaches the loop-plus-if shape the two challenges need, using `showReadings()` from §5.8 — code the student already owns. The `if (i < NUM_SENSORS - 1)` line is the teaching moment: the loop decides *how many times*, the if decides *what happens this time*. No challenge answers are given away.

Also: section retitled *"Deciding and Repeating — If Statements and For Loops"* (nav pill → `8A. If & For`), Step 4's aside now points forward to §8A, the Exit Ticket gains a for-loop line, and the "Where this goes next" callout covers both tools.

### 2. New figure — `L04_GRAPHIC_4-06_for_anatomy.svg`

Drawn in the same three-card family as L05's 5-04 so the spiral back-reference is recognizable on sight, but with **L04's own example** (`i < NUM_SENSORS`, walking the sensor array) instead of borrowed pushups. Bottom strip carries the payoff: *Act One has 3 sensors. Act Two has 5. NUM_SENSORS changes — this loop does not.* Rendered and eyeballed before staging.

### 3. L05 §5.15 becomes the spiral's second rung (v04.1.9 → **v04.2.0**)

Retitled *"The For Loop, Second Look."* The first-contact framing is replaced by a **🔁 Builds on:** marker with the ⭐4 star (§18.2 canon) and prose that says plainly: you took this apart in Lesson 4; here is what this lesson asks of it that Lesson 4 never did.

And it now teaches one of those things. **"Counting the Other Way"** is new: the descending loop `for (int i = 3; i >= 1; i--)`, a part-by-part table against the ascending version, and why the test is `>=` and not `>` — *one character, one second, one crashed run*. L05's own challenge solutions already used a countdown loop and pointed at §5.15 for it; §5.15 had never taught it.

### 4. Bible v8.36 → **v8.36.1**

**§11 §8A MUST COVER WHAT §9 REQUIRES.** A construct the challenges ask students to *write* must be taught in that lesson; using it inside the lesson's given code is not teaching it. Gate: list the constructs in every §9 hint and reveal-solution, confirm each has a tutorial at or before that lesson. Fix pattern recorded too — teach at first contact, demote the later tutorial to a §18.1 spiral second rung carrying only what is new there. Never two first contacts.

---

## VERIFICATION

- **Bounded-scope asserts** on all 13 edits (`count==1` exact-string), including the visible banners.
- **Normalized diff audit:** L04 113 changed lines, 8 removed — all eight are the intended in-place replacements (3 version strings, nav pill, section comment, cap title, Step 4 aside, where-next callout). L05 71 changed lines, 11 removed, same character. Bible 3.
- **Structure:** L04 div 153→156 balanced, pre 32→34, tables 17→18, zero dup ids, zero dead anchors. L05 div 141→142 balanced, pre 43→44, tables 15→16, clean.
- **Payload gate after both edits:** PASS, ADVISORY 635 — unchanged. No code or payload was touched; the loops were already in the shipped program.
- **Image audit:** every `<img>` in L04 and L05 resolves against `images/`, including the new 4-06 and `spiral_star_04.svg`.
- **Versions re-grepped from the written files**, not carried from the plan.

---

## PUSH BATCH (S57, second batch) — ORDERED, BLOCKING

1. **`images/L04_GRAPHIC_4-06_for_anatomy.svg`** → `github.com/Weymuth/zumo/images/`. **This goes first** — L04 references it by absolute URL and will show a broken figure until it lands.
2. **`lessons/Lesson_04.html`** (v04.1.0) and **`lessons/Lesson_05.html`** (v04.2.0) → repo + Canvas.
3. **Root docs:** `ZUMO_SUPER_BIBLE.md` (v8.36.1) · `LIVE_ZUMO_TEXTBOOK.md`.

No Maker change, so `newproject.html` stays put. Verify by fresh clone and check **which version** landed (§12.4).

_Housekeeping: a stray `.DS_Store` is still committed — `git rm .DS_Store` + a `.gitignore` line whenever, not urgent._

---

## STILL QUEUED

**L04 `setLayout21x8`** — L04 is the only lesson of 16 with zero occurrences, in the lesson *and* its payloads. Checked this session and it is **benign**: every L04 display string is ≤ 8 characters and every `gotoXY` is (0,0) or (0,1), so the program is correct on the default 8×2 layout. It is a consistency and Quick-Reference gap, not a break — L02, L03, L05 and L06 all carry a Quick Reference row explaining the call and L04 has none. Small pass, not a fire.

**L04 image index is incomplete** (found this session, not fixed): the index lists 4.1, 4.2, 4.3, 4.4 and the new 4.6, but **4.5 and the 4-01 if-anatomy figure are wired into the lesson and absent from the table**. One-pass fix on the next L04 open.

L04 C03/C04 — re-read the cards now that §8A teaches the tool; the "misscoped HARD" rating in `L04_LEARNMODE_LOG.md` was based on the missing prerequisite and should be revisited · `L04_LEARNMODE_LOG.md` correction (it cites L05 §5.13; the tutorial is §5.15) · the 6 syntax-gap prose candidates + "out-of-range values don't error" · L03_C05 Variable Speed learner mode · C06 reorder to #1 · whole-template starters L08/L09/L10 · Maker batch (bulk DL · `?lesson=N` soft gate · C## labels) · L01 VS Code multi-root step.

**BENCH (need robot):** C06 · C11 · Q017 L09 six numbers · Q044 calibration-spin · Q046 gyro-bias · L02 §5 green-LED · Constrain RUN_MS.

**PARKED:** solution-disclosure · monetization/ebook · "Know Your Zumo" · day-by-day grid + syllabus · TDP template v3 (A5 Lab Log) · §9 difficulty grouping · L06 card pattern.

**⚠️ AI TUTOR** — students get API access, the syllabus has no entry for it, `tutor.html` is stale with no L12+ content. **Term starts Sept 8.**

---
*Written S57, July 20 2026. L16 v02.2.3 + Bible v8.36 are LIVE (`622f8c6`); L04 v04.1.0 + L05 v04.2.0 + GRAPHIC 4.6 + Bible v8.36.1 staged, not pushed.*
