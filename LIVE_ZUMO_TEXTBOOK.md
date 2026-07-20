# LIVE_ZUMO_TEXTBOOK.md

**Date:** July 20, 2026 (Session 58 — AI Tutor rebuild COMPLETE).
**Status:** ⚠️ **STAGED, NOT PUSHED.** All prior S58 batches are LIVE (commit `cadda00`): Bible v8.36.2, the `data-reveal` retrofit, and the challenge-markup normalization. This batch ships the rebuilt tutor front-end. Repo-only — no lesson/Bible/Maker version changes.

**Lesson versions (unchanged this batch):**
L01 v03.4.2 · L02 v02.4.2 · L03 v03.6.2 · L04 v04.1.4 · L05 v04.2.4 · L06 v04.7.2 · L07 v04.3.12 · L08 v04.1.9 · L09 v05.0.11 · L10 v02.1.14 · L11 v02.2.4 · L12 v01.2.5 · L13 v02.2.4 · L14 v02.4.4 · L15 v02.2.5 · L16 v02.2.4 · Bible v8.36.2 · Maker v2.39 · Gate v1.6 · Harness v3.0.

---

## 🎉 AI TUTOR REBUILD — COMPLETE (all four pieces)

The old tutor embedded the whole curriculum in a Cloudflare Worker prompt, frozen at the pre-S28 15-lesson book (taught the cut cliff feature, wrong lesson numbers, no L15/L16). The rebuild makes the tutor **read the live lessons**, so it never rots again.

1. **Worker v3** (`tutor/worker.js`) — curriculum stripped out; accepts live lesson text from the browser and injects it as authoritative context; model Haiku→**Sonnet**; prompt caching for cost; coach-don't-reveal stance in the prompt. **DEPLOYED to Cloudflare** ("Version Saved"). `tutor/worker.js` is the version-controlled source-of-record — the live copy runs on Cloudflare.
2. **`data-reveal` retrofit** — LIVE. Every `<details>` typed; the tutor strips `solution` blocks so it never holds the answer key.
3. **Challenge markup normalization** — LIVE. 88 challenges uniformly tagged (`data-challenge`).
4. **`tutor.html`** — THIS batch. Rebuilt front-end (goes in `tutor/`): on lesson-select it fetches the live `Lesson_NN.html` from Pages, strips `data-reveal="solution"`, sends the clean text to the worker, and builds a **dynamic per-challenge picker** from the `data-challenge` markers (L11 mysteries included; L16 lesson-level). Keeps the code-file upload, welcome screen, typing indicator, and clear. Dropped the dead 3Pi+/Zircon platform buttons.

`index.html`'s two tutor links repointed to `tutor/tutor.html`.

---

## PUSH BATCH (S58, batch 4 — repo only)

1. **`tutor/tutor.html`** (the new page) → repo.
2. **`tutor/worker.js`** (worker source-of-record) → repo.
3. **`index.html`** (links repointed) → repo.

No Canvas, no lessons, no Bible/Maker. The worker is already live on Cloudflare. The tutor reads lessons from Pages (already live), so the whole pipeline works once these land.

**Test after pushing:** open `weymuth.github.io/zumo/tutor/tutor.html`, pick a lesson (watch "✓ reading Lesson N…"), confirm the challenge dropdown fills, send a message, and confirm the reply reflects the lesson and does NOT paste a full challenge solution. If a reply errors, the likely spots are the fetch path or the worker response shape — both easy to check.

---

## STILL QUEUED

- **Project B — full goal→logic→template card redesign, book-wide** (~80–100 challenges, authoring project, separate session).
- **Syllabus/Canvas entry for the AI Tutor** (students need to be told it exists and how to use it — the syllabus has no entry yet).
- `.DS_Store` still committed — `git rm` + `.gitignore`.
- `millis()`/`map()` taught-notes · L03_C05 learner mode · L04 C03/C04/C05 · C06 reorder to #1 · whole-template starters L08/L09/L10 · Maker batch (bulk DL · `?lesson=N` · C## labels) · L01 VS Code multi-root.

**BENCH:** C06 · C11 · Q017 L09 six numbers · Q044 calibration-spin · Q046 gyro-bias · L02 §5 green-LED · Constrain RUN_MS.

**PARKED:** solution-disclosure · monetization/ebook · "Know Your Zumo" · day-by-day grid + syllabus · TDP template v3 (A5 Lab Log) · §9 difficulty grouping.

---
*Written S58, July 20 2026. Prior batches LIVE (`cadda00`); tutor front-end + worker source + index staged, not pushed.*
