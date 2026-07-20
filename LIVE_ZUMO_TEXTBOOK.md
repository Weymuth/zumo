# LIVE_ZUMO_TEXTBOOK.md

**Date:** July 20, 2026 (Session 57 — three batches: L16 EEPROM · the `for`-loop hole · the layout that was never explained).
**Status (S57, third batch):** ⚠️ **STAGED, NOT PUSHED.** Batches one and two are **LIVE and verified** by fresh clone at commit `f638539` (L16 v02.2.3, L04 v04.1.0, L05 v04.2.0, GRAPHIC 4.6, Bible v8.36.1). This batch changes **one file**: **L04 v04.1.0 → v04.1.1**. No images, no Maker, no Bible, no gate change.

**Lesson versions — every one grepped from its own file, not carried forward:**
L01 v03.4.0 · L02 v02.2.4 · L03 v03.4.7 · L04 **v04.1.1** · L05 v04.2.0 · L06 v04.5.9 · L07 v04.3.10 · L08 v04.1.7 · L09 v05.0.9 · L10 v02.1.12 · L11 v02.2.2 · L12 v01.2.3 · L13 v02.2.2 · L14 v02.4.2 · L15 v02.2.3 · L16 v02.2.3 · Bible v8.36.1 · Maker v2.39 · Gate v1.6 · Harness v3.0.

---

## THE HEADLINE — THE "MISSING" setLayout21x8 WAS A DELIBERATE CHOICE NOBODY WROTE DOWN

The queue flagged L04 as *"the ONLY lesson of 16 missing `setLayout21x8`."* True — zero occurrences, in the lesson and in its payloads. But the investigation reversed the verdict:

- Every L04 display string is **≤ 8 characters**; every `gotoXY` is (0,0) or (0,1).
- §5.8 engineers its dashboard to fit exactly: three values scaled to two digits plus two spaces = **8 characters**.
- §8A.4 explains trailing spaces as overwriting *"leftover letters … on the 8-character row."*
- The Quick Reference documents `gotoXY` as *"row 0 = top, row 1 = bottom"* — a two-row screen.
- **C03's whole design** — squash 0–2000 into a column 0–7, print 8 characters — only works on an 8-wide row.

L04 is built for the startup 8 × 2 layout from end to end. The call isn't missing; it was never wanted.

**What was actually wrong was the reason the lesson gave.** §5.8 said the OLED *"only has 8 characters per row."* That is false about the hardware — the screen has 21 when asked, and Lessons 2, 3 and 5 ask. A student coming from L03's dense display met a lesson asserting the opposite, and the book never reconciled it.

---

## WHAT SHIPPED (L04 v04.1.0 → **v04.1.1**)

1. **The false claim, corrected.** "because it only has 8 characters per row" → "because this lesson runs the screen in its **8-characters-by-2-rows layout**." Same sentence, now true.

2. **A Coach's Tip naming the choice** — *why this lesson's screen looks different.* Lessons 2 and 3 called `setLayout21x8()`; Lesson 4 leaves it out and falls back to 8 big characters on 2 rows. **That is a choice, not an oversight.** The reasoning is the part worth having: today you are not reading at a desk, you are sliding a robot across tape and watching numbers from a foot away — big wins, and three two-digit values fill the row exactly. Lesson 5 asks for 21 characters again because bar graphs need room more than size. *Match the layout to the reading distance.*

3. **Quick Reference → Display gains the row** for `display.setLayout21x8();`, marked **not used in this lesson** with the pointer to §5.8 and the note that Lessons 2, 3 and 5 do call it. The tool is now documented in L04 without pretending L04 uses it.

4. **Index order repaired.** The GRAPHIC 4.6 row added earlier this session landed between 4.3 and 4.4. Moved to follow 4.5. Index now reads IMAGE 4.1–4.4, GRAPHIC 4.1–4.6, VIDEO 4.1.

---

## ONE CORRECTION TO CARRY FORWARD

Earlier this session I reported the **L04 image index as incomplete**, missing rows for 4.5 and the if-anatomy figure. **That was wrong** — the index carries all eleven tokens and always did. My row-counting regex matched only one of the two `<tr>` variants in that table (the zebra-striped rows carry a `style` attribute) and I read the short count as a gap. Same failure mode as S56's unescaped-`<` false alarm: **the inspection tool was broken, not the file.** When auditing a table, count the tokens in the rendered text, not the rows matched by one hand-written pattern. Removed from the queue; nothing was fixed because nothing was broken.

---

## VERIFICATION

- `count==1` asserts on all five edits; both visible banners asserted **unchanged** (minor bump — §5b).
- **Nesting caught and fixed mid-build:** the Coach's Tip first anchored on a sentence *inside* §5.8's paragraph, which would have put a `<div>` inside a `<p>` and split the paragraph on screen. Re-anchored to the paragraph's closing tag and re-verified — no `<div>` inside any `<p>` in the edited region.
- Normalized diff: 32 changed lines, all reconciling to the five intended edits.
- Structure: div 157/157, tables 18/18, zero dup ids, zero dead anchors.
- Payload gate: **PASS**, ADVISORY 635 — unchanged.
- Index order re-read from the rendered table, not from the edit script.

---

## PUSH BATCH (S57, third batch)

1. **`lessons/Lesson_04.html`** (v04.1.1) → repo + Canvas.
2. **`LIVE_ZUMO_TEXTBOOK.md`** → repo root.

No images, no Maker, no Bible this time. Verify by fresh clone and check **which version** landed (§12.4).

_Housekeeping: a stray `.DS_Store` is still committed — `git rm .DS_Store` + a `.gitignore` line whenever, not urgent._

---

## STILL QUEUED

L04 C03/C04 — re-read the cards now that §8A teaches the tool; the "misscoped HARD" rating in `L04_LEARNMODE_LOG.md` was based on a prerequisite that now exists · `L04_LEARNMODE_LOG.md` correction (it cites L05 §5.13; the tutorial is §5.15) · the 6 syntax-gap prose candidates + "out-of-range values don't error" · L03_C05 Variable Speed learner mode · C06 reorder to #1 · whole-template starters L08/L09/L10 · Maker batch (bulk DL · `?lesson=N` soft gate · C## labels) · L01 VS Code multi-root step.

**DONE, removed from queue:** L16 EEPROM prose + address map · L04 `for` primer (became the §8A build) · L04 `setLayout21x8` (was not a defect — now a stated choice) · L04 image index (false alarm, see correction above).

**BENCH (need robot):** C06 · C11 · Q017 L09 six numbers · Q044 calibration-spin · Q046 gyro-bias · L02 §5 green-LED · Constrain RUN_MS.

**PARKED:** solution-disclosure · monetization/ebook · "Know Your Zumo" · day-by-day grid + syllabus · TDP template v3 (A5 Lab Log) · §9 difficulty grouping · L06 card pattern.

**⚠️ AI TUTOR** — students get API access, the syllabus has no entry for it, `tutor.html` is stale with no L12+ content. **Term starts Sept 8.**

---
*Written S57, July 20 2026. Batches 1–2 LIVE (`f638539`); L04 v04.1.1 staged, not pushed.*
