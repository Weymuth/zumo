# LIVE_ZUMO_TEXTBOOK.md

**Date:** July 20, 2026 (Session 58 — the deferred audit false-positive Bible entry).
**Status (S58):** ⚠️ **STAGED, NOT PUSHED.** Everything through S57 is now **LIVE** at commit `5f69546` — including **L06 v04.7.0**, which the S57 tracker still marked "staged" but which a fresh clone confirms is live. This session stages **one file**: **`ZUMO_SUPER_BIBLE.md` v8.36.1 → v8.36.2**. No lessons, no images, no Maker, no gate change.

**Lesson versions — every one grepped from its own file, not carried forward:**
L01 v03.4.0 · L02 v02.4.0 · L03 v03.6.0 · L04 v04.1.2 · L05 v04.2.2 · L06 v04.7.0 · L07 v04.3.10 · L08 v04.1.7 · L09 v05.0.9 · L10 v02.1.12 · L11 v02.2.2 · L12 v01.2.3 · L13 v02.2.2 · L14 v02.4.2 · L15 v02.2.3 · L16 v02.2.3 · Bible **v8.36.2** · Maker v2.39 · Gate v1.6 · Harness v3.0.

---

## THE HEADLINE — S57'S PROSE-KEYWORD FALSE POSITIVES ARE NOW CANON

S57's two construct sweeps leaned on a prose-keyword grep, and that grep repeatedly cried wolf — `milliseconds` read as `millis`, a stray `?:` in prose read as the ternary, a changelog `v04.6.0` read as a version mismatch — each one evaporating on a human read. The discipline that caught them is now a §11 checklist rule so it is not relearned next session.

---

## WHAT SHIPPED — Bible v8.36.1 → **v8.36.2**

**New §11 checklist bullet — AUDIT FALSE-POSITIVE DISCIPLINE — A REGEX REPORTS CANDIDATES, NOT VERDICTS.** Three rules: (1) separate code from prose before counting — strip to `<pre>` for usage, strip tags for teaching, never count a token that spans both (`abs(` inside a `while` is a use, not a lesson); (2) a keyword near a heading is a lead, not proof — surface the candidate heading and read it; (3) verify every finding against rendered text before acting. Placed with the two S57 §11 entries, immediately before the ASCII-sweep bullet.

Changelog line 3: header and `Current:` bumped to v8.36.2, the new parenthetical prepended, the S57 entry demoted to `Prior:`, trailing paren-run closed (13 → 14).

**Count deliberately omitted from the entry.** The S58 handoff headline said "five," its own parenthetical summed to six, and the S57 tracker said "four" for the second sweep — the rule holds at any count, so no disputed number is written into canon.

---

## VERIFICATION

- `str_replace count==1` on all three edits (version line, closing paren, checklist bullet).
- `git diff --stat`: 1 file, 2 insertions / 1 deletion — line 3 replaced + one bullet added, no collateral.
- Version grep: `Bible version: v8.36.2`. Entry present ×2 (changelog + checklist).
- Markdown only — no lessons, payloads, or HTML touched; no gate or harness run applicable.

---

## PUSH BATCH (S58)

1. **`ZUMO_SUPER_BIBLE.md`** (v8.36.2) → repo root.
2. **`LIVE_ZUMO_TEXTBOOK.md`** → repo root.

No lessons, no images, no Maker, no Canvas. Verify by fresh clone (§12.4) — allow ~20–30 s for the shallow-clone cache after pushing before concluding a version did not land.

_Housekeeping: a stray `.DS_Store` is still committed — `git rm .DS_Store` + a `.gitignore` line whenever, not urgent._

---

## STILL QUEUED

`millis()` taught-note + `map()` note (minor) · L03_C05 Variable Speed learner mode · L04 C03 learner mode (**unblocked**) · L04 C04/C05 walkthroughs · "out-of-range values don't error" · C06 reorder to #1 · whole-template starters L08/L09/L10 · Maker batch (bulk DL · `?lesson=N` soft gate · C## labels) · L01 VS Code multi-root step.

**BENCH (need robot):** C06 · C11 · Q017 L09 six numbers · Q044 calibration-spin · Q046 gyro-bias · L02 §5 green-LED · Constrain RUN_MS.

**PARKED:** solution-disclosure · monetization/ebook · "Know Your Zumo" · day-by-day grid + syllabus · TDP template v3 (A5 Lab Log) · §9 difficulty grouping · L06 card pattern.

**⚠️ AI TUTOR — the one real deadline.** Students get API access, the syllabus has no entry for it, `tutor.html` is stale (no L12+ content). **Term starts Sept 8.** Biggest open item; the natural front task now that the Bible entry is in. Raw material: the S57 learner-mode §8A walkthroughs.

---
*Written S58, July 20 2026. All of S57 LIVE (`5f69546`); Bible v8.36.2 staged, not pushed.*
