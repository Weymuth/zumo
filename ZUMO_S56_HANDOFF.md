# ZUMO — S56 Handoff (written at S55 close, Jul 19 · paste at top of Session 56)

**S55 was a DIAGNOSIS + INFRASTRUCTURE session.** It took **four attempts**, none of which
failed on the build — all four failed on *reading the state*. Both causes are now fixed in
canon and in the toolchain. **S56's job is to build L01 §9. The design is locked. Do not re-open it.**

---

## SESSION OPEN — run the drift check FIRST (Bible §12.6-C)

```
git clone --depth 1 https://github.com/Weymuth/zumo.git
cd zumo
grep -o "Lesson version: v[0-9.]*" lessons/Lesson_01.html
grep -oE "Project Maker v2\.[0-9]+" newproject.html | head -1
grep -oE "Bible version: v[0-9.]+" ZUMO_SUPER_BIBLE.md
```

⚠️ **`sort -u` is WRONG for the Maker version** — it sorts alphabetically and returns `v2.9`
over `v2.38`. Use the badge-anchored grep above, or `sort -V`.

**Expected if the S55 batch was pushed:** L01 `v03.3.0` · Maker `v2.38` · Bible **`v8.34`** · Gate **v1.4**.
**If Bible reads v8.33.1 or gate reads v1.3, the S55 push did not land — say so in your first message.**

**The files win over LIVE.md, always.** If they disagree: **ask DJ for a newer LIVE.md first**
(a prior session may have written one that never got pushed), and only regenerate if none exists.
Do not enter queued work on a known-stale LIVE.md.

---

## 🎯 THE ONE JOB — L01 §9, landed as a single bump to v03.4.0

### Why it must happen
The Maker serves eleven L01 challenge files containing **132 lines of executable code that
appear nowhere in `Lesson_01.html`** — chiefly the EEPROM robot-name reader. **C01 Part 5 asks
students to find their robot's name; the book never shows the code that reads it.** The payload
gate fails 900 checks on L01 for exactly this reason.

**This is the gate working, not a gate defect.** Three earlier S55 takes proposed exempting it —
all three were reading a truncated 20-line display that showed only comments.

### The locked design (DJ-approved, S55)

| Item | Decision |
|---|---|
| §9 listing | **P1** — the shared 88-line body, **markerless**, plain framing, at the TOP of §9 before the cards |
| File markers | **M1** — exactly as S54 shipped, `CH1 PART N` / `CHALLENGE N:` prefixes **KEPT** |
| Cards | Keep existing prose location **AND** name the marker (C01's existing pattern), all eleven |
| C06 | Current numbers, **no bench**, no regeneration |
| C06 markers | markerless — measure-only, nothing to edit |

**Why markers stay in the files — do NOT "simplify":** C01's header refers to its markers by
name six times (*"Find `<<< CH1 PART 1` below"*). The marker text is a **lookup key the
instructions depend on.** A proposal to drop the redundant `CHALLENGE N:` prefix was raised and
**withdrawn** for this reason — C03 can spare it, C01 cannot, and the pattern must hold book-wide.

**Why the §9 listing is markerless — structurally forced:** the listing is ONE program shared by
eleven challenges, and **the markers are precisely what differ between them** (strip markers and
nine of eleven bodies collapse to one hash). No marker set is correct for more than one challenge.
One body in the listing, eleven headers in the cards — the same architecture as the files.

**⚠️ The listing needs ONE framing sentence.** §5.5's listing is **56 lines**; the challenge body
is **88**. The 32-line gap is the name-reader, `buttonC` and the section scaffold. Without a note,
a student watches the program grow by 32 lines with no explanation. **Draft the sentence for DJ
before inserting it.**

### Definition of done
- Gate v1.4 on L01: **FAIL(900) → PASS**, and the **CATEGORY CENSUS shows 0 EXECUTABLE CODE**
- L01 v03.3.0 → **v03.4.0** (moderate: new listing + eleven rewritten cards)
- §5b two homes: hidden comment full `v03.4.0`, visible banner `Version 03.4`
- Full diff audit; L02–L16 must still PASS

---

## VERIFIED FACTS (S55 — reproduce, don't re-derive)

- **Maker payloads ↔ repo `L01_CHALLENGES/` files: 11/11 match.** Option B intact.
- **All eleven share ONE 55-statement executable body.** Differences are markers and comments only.
- ⚠️ **"All eleven byte-identical" is FALSE** — all eleven differ. The recorded proof
  (*"all compile to exactly 10,208 B"*) does not establish it. Identical compiled size proves
  nothing — **already Bible §11 canon**, from the S27 `bonus_b3_unspenttrim` sabotage that
  compiled byte-identical to the correct build. Verify source by comparing statements, not sizes.
- ✅ **`ZUMO_NAME_WRITER_main.cpp` IS in the repo** (4 EEPROM writes, magic `0x5A`, addr 512).
  The S55 handoff's "not in the repo" note was stale. **The September dependency is DONE.**
- L01 §5.5 listing = 56 lines · challenge body = 88 lines · gap = 32.

---

## WHAT S55 SHIPPED (staged at close — confirm these landed)

**Bible v8.33.1 → v8.34 — NEW §12.6.** §12.3 already ruled that *"remember to update LIVE.md"*
is too weak; §12.6 covers the case it missed — the session that **ends before reaching step 3**.
(A) write LIVE.md when the last version-changing edit lands, re-verify at close; (B) a push that
bumps a version and omits LIVE.md is an **INCOMPLETE PUSH**; (C) session open runs a **drift check**,
files win, ask DJ for a newer LIVE.md before regenerating.
⚠️ **Part A deliberately softens §12.3.** If it ever produces a ghost version in LIVE.md, part A
is the thing to revisit.

**Gate v1.3 → v1.4 — reporting fix.** v1.3 stacked two truncations: `missing[0]` per chunk
(line 135) and `fails[:20]` on print (line 200). L01 reported **FAIL (148)** against a true **900**,
with all 20 visible lines being comments. v1.4 records every missing line, caps printing at 200
with an explicit `... N more`, and prints a **CATEGORY CENSUS** (boxed comments / `<<<` markers /
other comments / **EXECUTABLE CODE**). **Regression-tested: L02–L16 PASS on both v1.3 and v1.4** —
verdicts unchanged, reporting only. **Read the census, not the raw count.**

---

## PUSH BATCH (S55) — root docs only
`ZUMO_SUPER_BIBLE.md` (v8.34) · `gate_payload_match.py` (v1.4) · `LIVE_ZUMO_TEXTBOOK.md` ·
`ZUMO_S56_HANDOFF.md`
No lessons, no Maker, no SVGs. Verify by fresh clone and check **which version** landed (§12.4).

---

## STILL QUEUED
L16 EEPROM prose fix + the 512 address-map note (L16's *"this book has never touched it"* becomes
false once L01 ships) · **L04 `setLayout21x8` — the ONLY lesson of 16 missing it** · L04 C03 `for`
primer (option b) + `L04_LEARNMODE_LOG.md` correction · **extend the gate to cover L01 challenge
bodies** (required by the option-B ruling) · the 6 syntax-gap prose candidates + "out-of-range
values don't error."

**BENCH (need robot):** C06 · C11 · Q017 L09 six numbers · Q044 calibration-spin · Q046 gyro-bias ·
L02 §5 green-LED · Constrain RUN_MS.

**PARKED:** solution-disclosure · monetization/ebook · "Know Your Zumo" · day-by-day grid + syllabus ·
TDP template v3 (A5 Lab Log) · §9 difficulty grouping · L06 card pattern.

**⚠️ AI TUTOR** — students get API access, the syllabus has no entry for it, `tutor.html` is stale
with no L12+ content. **Term starts Sept 8.**

---
*Written S55, July 19 2026. Bible v8.34 + gate v1.4 + LIVE.md staged, not pushed.*
