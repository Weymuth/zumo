# LIVE_ZUMO_TEXTBOOK.md

**Date:** July 20, 2026 (Session 57 — L16 EEPROM: closing the defect S56 created).
**Status (S57):** ⚠️ **STAGED, NOT PUSHED.** Live tree verified by fresh clone at open, commit `93cb795` — the full S56 batch (L01 v03.4.0, Maker v2.39, Bible v8.35, gate v1.6) had landed, and the gate re-ran **PASS / ADVISORY 635** on the untouched tree as a control. Two files changed this session: **L16 v02.2.2 → v02.2.3** · **Bible v8.35 → v8.36**. No Maker change, no gate change, no images.

**Lesson versions — every one grepped from its own file, not carried forward:**
L01 v03.4.0 · L02 v02.2.4 · L03 v03.4.7 · L04 v04.0.12 · L05 v04.1.9 · L06 v04.5.9 · L07 v04.3.10 · L08 v04.1.7 · L09 v05.0.9 · L10 v02.1.12 · L11 v02.2.2 · L12 v01.2.3 · L13 v02.2.2 · L14 v02.4.2 · L15 v02.2.3 · L16 **v02.2.3** · **Bible v8.36** · Maker v2.39 · Gate v1.6 · Harness v3.0.

---

## THE HEADLINE — A CORRECT FIX IN L01 MADE L16 WRONG

S56 published the EEPROM robot-name reader in L01 §9, exactly as DJ's *if it's in the payload, it goes in the book* ruling required. That publication silently falsified a sentence in a lesson nobody had opened:

> L16 §4.3: *"The 32U4 has a third memory, and this book **has never touched it**: 1,024 bytes of EEPROM"*

As of L01 v03.4.0 the book touches it in Challenge 1 — `NAME_ADDR = 512`, magic `0x5A`, read before the greeting. The claim was true when written and false by the time it was read. This session closed that, and canonized the class of defect so the next one gets caught by grep rather than by luck.

---

## WHAT SHIPPED

### 1. L16 §4.3 — the false claim becomes a callback (v02.2.2 → **v02.2.3**)

The dead clause came out, and the space it left was spent on the payoff L01 had set up fifteen lessons earlier. L01 Challenge 1 Part 5 tells students their robot's name lives in *"permanent memory, not in this file"* — and never names it. §4.3 now names it:

> You have already read from it… The name sits at address **512**, written once before the robot ever reached you, and it has survived every upload you have done in fifteen lessons since — because an upload replaces *flash*, and the name was never in flash. That was a **read**. Lesson 16 is the first time this book **writes**.

That read/write distinction is the section's actual subject, so the correction pays rent rather than just patching a hole.

### 2. L16 §4.3 — the address map, so the capstone can't collide

The two EEPROM users pass each other with ~480 bytes of slack and neither lesson mentioned the other. A three-row table now states the split, followed by the sentence that makes it matter: *write to 512 and your robot loses its name — and no error message tells you, because to the hardware one byte is exactly as valid as another.*

| Address | Owner | Contents |
|---|---|---|
| 0 – 511 | Lesson 16 | `Saved` — magic `0x16`, gains, baseline |
| 512 – 543 | Lesson 1 / teacher utility | magic `0x5A` + robot name |
| 544 – 1023 | unclaimed | free for §7 enhancements |

The map is not invented here — it is lifted from the header comment of `ZUMO_NAME_WRITER_main.cpp`, which has carried it since the fleet was named.

### 3. Bible v8.35 → **v8.36** — two entries

- **§16.9 EEPROM ADDRESS MAP — NEW.** The map above, as hardware ground truth, with `ZUMO_NAME_WRITER_main.cpp` named as source of truth and a standing rule: any new EEPROM use takes addresses from 544 up and is recorded there.
- **§11 A "THE BOOK HAS NEVER…" CLAIM IS A DEPENDENCY, NOT PROSE.** Any sentence about what the book has never done or will do for the first time is a claim about all sixteen lessons. Grep the tree before trusting it, and re-grep whenever new content introduces one. Same class as the §11 grep-the-code rule — the lesson said one thing, the book did another.

---

## VERIFICATION

- **Control run first.** Gate re-run on the untouched clone before any edit: PASS, ADVISORY 635, `L1=635`. Distinguishes inherited state from edit damage (§11).
- **Bounded-scope asserts.** All three L16 edits and all three Bible edits used exact-string replace with `count==1` guards; the visible-banner strings were asserted *unchanged* (minor bump — §5b).
- **Normalized diff audit:** 38 changed lines in L16, every one reconciling to the three intended edits; nothing removed but the false clause. 18 changed lines in the Bible.
- **Structure:** div balance 0/0 (137/137, unchanged), tables 11 → 12, zero duplicate ids, zero dead anchors.
- **Payload gate after the edit:** PASS, ADVISORY 635 — unchanged, as expected for a prose-only lesson edit.
- **Cross-lesson sweep:** every lesson grepped for `EEPROM`. Only L01 (3), L03 (1) and L16 (53) mention it. L03's line — *"Competition robots store their calibration in EEPROM… this book gets there in its final lesson"* — was checked and is **still true**; L01 reads a name, it does not store calibration. No second defect.

---

## PUSH BATCH (S57) — ORDERED

No SVGs, no Maker, no gate change this batch, so steps 1 and 2 of the standard sequence are skipped.

1. **`lessons/Lesson_16.html`** (v02.2.3) → repo + Canvas.
2. **Root docs:** `ZUMO_SUPER_BIBLE.md` (v8.36) · `LIVE_ZUMO_TEXTBOOK.md`.

Verify by fresh clone and check **which version** landed (§12.4). A push that bumps a version and omits LIVE.md is an INCOMPLETE PUSH (§12.6).

_Housekeeping: a stray `.DS_Store` is still committed — `git rm .DS_Store` + a `.gitignore` line whenever, not urgent._

---

## STILL QUEUED

**L04 `setLayout21x8` — the ONLY lesson of 16 missing it** · L04 C03 `for` primer (option b) + `L04_LEARNMODE_LOG.md` correction · the 6 syntax-gap prose candidates + "out-of-range values don't error" · L03_C05 Variable Speed learner mode (paused S45; starter saved; the three edits are array+index in CONFIG, `TEST_SPEEDS[speedIndex]` in `runMotorTest`, `speedIndex=(speedIndex+1)%NUM_SPEEDS` in the B handler) · C06 reorder to #1 · whole-template starters L08/L09/L10 · Maker batch (bulk DL · `?lesson=N` soft gate · C## labels) · L01 VS Code multi-root step.

**DONE, removed from queue:** *L16 EEPROM prose fix + the 512 address-map note* — this session.

**BENCH (need robot):** C06 · C11 · Q017 L09 six numbers · Q044 calibration-spin · Q046 gyro-bias · L02 §5 green-LED · Constrain RUN_MS.

**PARKED:** solution-disclosure · monetization/ebook · "Know Your Zumo" · day-by-day grid + syllabus · TDP template v3 (A5 Lab Log) · §9 difficulty grouping · L06 card pattern.

**⚠️ AI TUTOR** — students get API access, the syllabus has no entry for it, `tutor.html` is stale with no L12+ content. **Term starts Sept 8.**

---
*Written S57, July 20 2026. L16 v02.2.3 + Bible v8.36 staged, not pushed.*
