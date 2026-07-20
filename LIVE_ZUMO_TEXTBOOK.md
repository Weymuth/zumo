# LIVE_ZUMO_TEXTBOOK.md

**Date:** July 20, 2026 (Session 58 — challenge markup normalization, project A).
**Status:** ⚠️ **STAGED, NOT PUSHED.** Prior S58 batches are LIVE (commit `086aa87`): Bible v8.36.2, and the `data-reveal` retrofit on all 16 lessons. This batch adds **invisible challenge markers** to **L01–L15** (88 challenge units) so the AI Tutor can offer a per-challenge picker. Nothing students see changes. L16 unchanged (its §9 is project tiers, left lesson-level).

**Lesson versions — grepped after the bump:**
L01 v03.4.2 · L02 v02.4.2 · L03 v03.6.2 · L04 v04.1.4 · L05 v04.2.4 · L06 v04.7.2 · L07 v04.3.12 · L08 v04.1.9 · L09 v05.0.11 · L10 v02.1.14 · L11 v02.2.4 · L12 v01.2.5 · L13 v02.2.4 · L14 v02.4.4 · L15 v02.2.5 · L16 v02.2.4 (unchanged) · Bible v8.36.2 · Maker v2.39 · Gate v1.6 · Harness v3.0.

---

## AI TUTOR REBUILD — PROGRESS

1. **Worker v3** — curriculum-free, reads live lessons, Sonnet + prompt caching. **DEPLOYED** to Cloudflare. Source-of-record copy to `tutor/worker.js` still pending.
2. **`data-reveal` retrofit** — LIVE. Every `<details>` typed so the tutor strips solutions.
3. **Challenge markup normalization (A)** — THIS batch. 88 challenges uniformly tagged so the tutor's per-challenge picker can parse them. (Project **B** — the full goal→logic→template card redesign — is committed for a later, separate session.)
4. **`tutor.html`** — NEXT. Live fetch + strip + the (now-parseable) challenge picker; moves to `tutor/`.

---

## WHAT SHIPPED THIS BATCH — challenge markup A

Every challenge across L01–L15 carries a uniform, invisible marker: `data-challenge="LL.N"` (canonical id) + `id="challenge-N"` (in-page anchor) + `data-kind="challenge|mystery"` + `data-difficulty` where a pill exists. **88 units, all unique.** The book had ~5 conventions (id-divs, strong-labels, `Challenge 9.N` headings, `🎯 Challenge N` h3, bare `9.N` h3); this normalizes the *marker* without touching any visible number, title, difficulty, or card structure.

Rulings folded in: L11's 4 "🕵️ Mystery" bonuses tagged too (`11.m1`–`11.m4`, `data-kind="mystery"`) so students can get tutor help on them; L15 tagged (7 challenges, `<h3>9.N</h3>`); L16 left lesson-level (project tiers, not challenges). Visible numbering untouched — L13/L14/L15 still read "9.N"; only the machine id is `LL.N`.

---

## VERIFICATION

- Per-lesson marker counts match the inventory exactly (11/6/8/5/5/8/6/5/6/5/7/3/3/3/7 = **88**); zero duplicate ids.
- Diff audit: **176 changed lines, all anchor tags** (88 removed bare + 88 added tagged); every added line reduces to its removed line plus only the inserted attributes — **zero content changed**.
- Payload **GATE: PASS**, advisory unchanged at 635 (markers sit on challenge headings/divs, never inside `<pre>`).
- `data-reveal` (347) and `data-challenge` (88) coexist cleanly — different elements.
- Version bump: hidden comment +1 patch on the 15 changed lessons (§5b); visible banners untouched.

---

## PUSH BATCH (S58, batch 3)

1. **15 lessons (L01–L15)** → repo `lessons/` (Pages) **and** Canvas.

No images, no Maker, no Bible, no L16. Verify by fresh clone (§12.4) — allow ~20–30 s for cache.

_Optional/whenever: commit `tutor/worker.js` source-of-record; `git rm .DS_Store` + `.gitignore` line._

---

## STILL QUEUED

**AI Tutor (active):** build `tutor.html` (live fetch + strip + per-challenge picker, → `tutor/`); commit worker source-of-record; syllabus entry. · **Project B — full goal→logic→template card redesign, book-wide (~80–100 challenges, authoring project, separate session).** · `millis()`/`map()` taught-notes · L03_C05 learner mode · L04 C03/C04/C05 · C06 reorder to #1 · whole-template starters L08/L09/L10 · Maker batch (bulk DL · `?lesson=N` · C## labels) · L01 VS Code multi-root.

**BENCH:** C06 · C11 · Q017 L09 six numbers · Q044 calibration-spin · Q046 gyro-bias · L02 §5 green-LED · Constrain RUN_MS.

**PARKED:** solution-disclosure · monetization/ebook · "Know Your Zumo" · day-by-day grid + syllabus · TDP template v3 (A5 Lab Log) · §9 difficulty grouping.

---
*Written S58, July 20 2026. Bible v8.36.2 + data-reveal LIVE (`086aa87`); challenge markers on L01–L15 staged, not pushed.*
