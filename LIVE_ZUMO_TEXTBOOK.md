# LIVE_ZUMO_TEXTBOOK.md

**Date:** July 19, 2026 (Session 56 — L01 §9 BUILD: the payload gate goes green).
**Status (S56):** ⚠️ **STAGED, NOT PUSHED.** Live tree verified by fresh clone at open, commit `5c82406`; the S55 batch (Bible v8.34, gate v1.4) had landed. Four files changed this session: **L01 v03.3.0 → v03.4.0** · **Maker v2.38 → v2.39** · **Bible v8.34 → v8.35** · **Gate v1.4 → v1.6**. One repo challenge file edited: `L01_CHALLENGES/C01_Hello_World/src/main.cpp`.

**Lesson versions — every one grepped from its own file, not carried forward:**
L01 **v03.4.0** · L02 v02.2.4 · L03 v03.4.7 · L04 v04.0.12 · L05 v04.1.9 · L06 v04.5.9 · L07 v04.3.10 · L08 v04.1.7 · L09 v05.0.9 · L10 v02.1.12 · L11 v02.2.2 · L12 v01.2.3 · L13 v02.2.2 · L14 v02.4.2 · L15 v02.2.3 · L16 v02.2.2 · **Bible v8.35** · **Maker v2.39** · **Gate v1.6** · Harness v3.0.

---

## 🟢 THE HEADLINE — GATE: PASS, WITH ZERO EXEMPTIONS

L01 had been failing the payload gate on **900 lines, 132 of them executable code** — chiefly an EEPROM robot-name reader that the Maker served in eleven challenge files and that appeared **nowhere in `Lesson_01.html`**, while C01 Part 5 asked students to go find their robot's name.

**DJ's ruling settled it:** *if it's in the payload, it goes in the book.* No exemptions, no marker-stripping, no gate logic routed around the gap. The content went into the book because it belonged there.

| Census category | Before | After |
|---|---|---|
| **EXECUTABLE CODE** | **132** | **0** |
| other comments | 122 | 0 |
| `<<<` markers | 14 | 0 |
| boxed header art | 632 | 632 → now **ADVISORY**, fingerprinted |

Three earlier S55 takes proposed *exempting* this failure as comment-only scaffolding. They were reading a truncated list. The correct fix was never an exemption.

---

## WHAT SHIPPED

### 1. L01 §9 — the shared listing + eleven rewritten cards (v03.3.0 → **v03.4.0**)

- **The Challenge Program** listing added at the top of §9, after the John Williams LEARN callout and before Challenge 1. 87 lines, **markerless**, canon dark `<pre>`.
- Two framing paragraphs (DJ-approved): the first explains the 32-line gap vs. §5.5 — the name-reader that pulls the robot's name out of permanent memory; the second explains that markers differ per challenge, so each card quotes its own.
- **All eleven cards** gained a marker-naming sentence + a `<pre>` quoting **their own exact target line(s), verbatim**. 26 quoted lines total: C03 gets three, C01 four, C10 two, C06 ten (its drive block), the rest one each.
- C06 is markerless by design (measure-only) and says so; it shows the block being measured.
- **Removed:** C01's old generic sentence *"The file marks each landing zone with a `<<<` comment"* — superseded and contradicted by the new precise one.

### 2. C01 markers made symmetric — the asymmetry was fixed, not explained

C01 had **five parts and three markers**. A student following *"each landing zone"* would hunt for two that did not exist. DJ: *"can we get rid of the asymmetry instead of explaining it."*

- **Part 3** edits the same line Part 1 does → the shared marker became `<<< CH1 PART 1, PART 3 and PART 4`.
- **Part 5** has nothing to edit (it reads Serial output) → the name-reader block gained `<<< CH1 PART 5 — READ ONLY, do not edit`.
- The boxed header was updated to name both, so all five parts are now findable by name.
- ✅ **Executable body unchanged — md5 `90880545`, identical to all eleven.** Comment-only: no compile risk, no byte-chain impact.

### 3. Maker v2.38 → **v2.39**

`PAYLOADS["1"]["c01"]` only — the two body markers + the two boxed-header additions, mirrored byte-for-byte from the repo file. Badge + changelog both bumped (the badge-without-changelog omission was caught in audit). Both JS blocks `node --check` clean. **No other payload touched** (diff: 8 added, 2 deleted).

### 4. Gate v1.4 → **v1.6** — two changes, in two steps

**v1.5 — boxed instruction headers are ADVISORY.** A challenge file's boxed header is the student's working instructions, deliberately kept in the file. DJ's reasoning: *"if we can take a step out of their workload they are more likely to do the work… lots of file skipping back and forth."* The book's card carries the same instructions as prose (better form for reading) plus the exact target line. So a non-matching boxed line is a **format** difference, not missing content — reported under ADVISORY, not failed.

**v1.6 — but fingerprinted.** v1.5 left a hole: an advisory line could be *edited* and the gate still said PASS, so file instructions could drift from card prose unseen. DJ: *"adding the md5 fingerprint would help avoid drift and doesn't really have a downside except you having to work a little harder."* Every boxed header is now pinned by line count + md5 in `BOXED_FP`. **Advisory means "not required to appear in the book" — never "unchecked."** Intentional changes go through `--update-fp`.

### 5. Bible v8.34 → **v8.35** — three new §11 entries

- **IF IT IS IN THE PAYLOAD, IT GOES IN THE BOOK.** An unmatched line is a gap in the book, not a gate defect. Executable code is never exempt under any framing. Test: *would a student need to read this line to do the work?* Corollary: when a shared listing serves N challenges, publish the ONE common body and let each card quote its OWN target line.
- **BOXED INSTRUCTION HEADERS ARE ADVISORY BUT FINGERPRINTED.**
- **READ THE CENSUS, NOT THE RAW COUNT.**

---

## VERIFICATION — 21-CHECK FINE-TOOTH AUDIT, PLUS FIVE-WAY REGRESSION

Every check passed. Two items were **found and fixed during the audit**, which is the audit working:

1. C01's card carried both the old generic marker sentence and the new precise one — the vague one contradicted the specific one. Removed.
2. The Maker had a badge bump with **no changelog entry**. Added.

**Gate regression — five ways:**

| Test | Result |
|---|---|
| Current build (L01–L16) | **PASS** |
| L02–L16 alone | PASS, zero advisory (no boxed headers exist outside L01) |
| Unmodified tree under v1.6 | FAIL — still reports **132 executable** + C01 header mismatch |
| Sabotage: inject executable code into a payload | **Caught** (1 executable) |
| Sabotage: tamper a boxed header, same line count | **Caught by fingerprint** — v1.5 missed this |

Other verified: C01 file ↔ Maker payload byte-identical · all **11/11** payloads ↔ repo files (Option B intact) · every card quote verbatim in its own file, correct file each · all five C01 header lookup keys resolve in the body · 11 cards / 11 KINDS / 11 repo folders · all 11 deep links resolve · div/pre/p/code balance 0 · no dup ids, no dead anchors · 19/19 images resolve · Canvas-safe (0 `<style>`, 0 `class=`) · §5b two homes agree (`v03.4.0` hidden / `Version 03.4` visible) · L01 diff **132 added / 4 deleted**, every deletion intentional.

**⚠️ Correction to the record:** mid-session an unescaped-`<` corruption was reported in C03's reveal-solution block. **That was wrong** — the inspection regex was eating `&lt;`. Audit #18 confirms all escaping is correct. No such defect existed; nothing was "fixed."

---

## PUSH BATCH (S56) — ORDERED

No SVGs this batch, so the image step is skipped.

1. **`newproject.html`** (Maker v2.39) → GitHub Pages. ⚠️ **5.19 MB — rename ON DISK, never via the GitHub web UI** (the web editor truncates >1 MB renames to 2 bytes).
2. **`L01_CHALLENGES/C01_Hello_World/src/main.cpp`** → repo.
3. **`lessons/Lesson_01.html`** (v03.4.0) → repo + Canvas.
4. **Root docs:** `ZUMO_SUPER_BIBLE.md` (v8.35) · `gate_payload_match.py` (v1.6) · `LIVE_ZUMO_TEXTBOOK.md` · `ZUMO_S57_HANDOFF.md`.

Verify by fresh clone and check **which version** landed (§12.4). A push that bumps a version and omits LIVE.md is an INCOMPLETE PUSH (§12.6).

_Housekeeping: a stray `.DS_Store` is still committed — `git rm .DS_Store` + a `.gitignore` line whenever, not urgent._

---

## STILL QUEUED

L16 EEPROM prose fix + the 512 address-map note (L16's *"this book has never touched it"* is now **false** — L01 ships the name-reader; this is a real consequence of today's work) · **L04 `setLayout21x8` — the ONLY lesson of 16 missing it** · L04 C03 `for` primer (option b) + `L04_LEARNMODE_LOG.md` correction · the 6 syntax-gap prose candidates + "out-of-range values don't error" · L03_C05 Variable Speed learner mode · C06 reorder to #1 · whole-template starters L08/L09/L10 · Maker batch (bulk DL · `?lesson=N` gate · C## labels) · L01 VS Code multi-root step.

**Note — one queued item is now DONE:** *"extend the gate to cover L01 challenge bodies"* was required by the option-B ruling and is satisfied by v1.6 (bodies gate-covered via the §9 listing; headers pinned by fingerprint).

**BENCH (need robot):** C06 · C11 · Q017 L09 six numbers · Q044 calibration-spin · Q046 gyro-bias · L02 §5 green-LED · Constrain RUN_MS.

**PARKED:** solution-disclosure · monetization/ebook · "Know Your Zumo" · day-by-day grid + syllabus · TDP template v3 (A5 Lab Log) · §9 difficulty grouping · L06 card pattern.

**⚠️ AI TUTOR** — students get API access, the syllabus has no entry for it, `tutor.html` is stale with no L12+ content. **Term starts Sept 8.**

---
*Written S56, July 19 2026. L01 v03.4.0 + Maker v2.39 + Bible v8.35 + gate v1.6 staged, not pushed.*
