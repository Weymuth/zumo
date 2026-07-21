# LIVE_ZUMO_TEXTBOOK.md

**Date:** July 20, 2026 (Session 58 — site-wide favicon + tutor logo/favicon).
**Status:** ⚠️ **STAGED, NOT PUSHED.** The AI Tutor rebuild is LIVE (worker deployed; `tutor/tutor.html` up with the Mercersburg logo). This batch adds the **favicon** across the site (`index.html` + all 16 lessons + the tutor page) via an explicit `<link rel="icon">`, because GitHub Pages *project* sites don't auto-discover `/favicon.ico` at a subpath.

**Lesson versions — grepped after the bump (all +1 patch for the favicon link):**
L01 v03.4.3 · L02 v02.4.3 · L03 v03.6.3 · L04 v04.1.5 · L05 v04.2.5 · L06 v04.7.3 · L07 v04.3.13 · L08 v04.1.10 · L09 v05.0.12 · L10 v02.1.15 · L11 v02.2.5 · L12 v01.2.6 · L13 v02.2.5 · L14 v02.4.5 · L15 v02.2.6 · L16 v02.2.5 · Bible v8.36.2 · Maker v2.39 · Gate v1.6 · Harness v3.0.

---

## AI TUTOR — LIVE (recap)

Worker v3 deployed (Cloudflare, curriculum-free, reads live lessons, Sonnet + caching) · every `<details>` typed (tutor strips `solution`) · 88 challenges tagged (`data-challenge`) · `tutor/tutor.html` live with the dynamic per-challenge picker and the Mercersburg dark logo in the header + welcome. The tutor updates itself whenever a lesson is edited.

---

## WHAT SHIPPED THIS BATCH — favicon site-wide

`<link rel="icon" href="…favicon.ico">` added to the `<head>` of every page: `index.html` (`href="favicon.ico"`), the 16 lessons (`href="../favicon.ico"`), and `tutor/tutor.html` (`href="../favicon.ico"`). The `favicon.ico` already lives in the repo root — this just points each page at it. The tutor page in this batch also carries the header/welcome logo (its live copy didn't yet have the favicon link).

---

## VERIFICATION

- Favicon links present: index 1, lessons 16/16, tutor 1.
- Diff-audit: every lesson changed **only** its favicon line + its version line; index changed only the favicon line — zero other edits.
- Lesson markers intact: `data-reveal` 347, `data-challenge` 88.
- Version bump: hidden comment +1 patch each (§5b); visible banners untouched (cosmetic change).
- Tutor JS re-validated; logo refs still 2.

---

## PUSH BATCH (S58, favicon)

1. **`index.html`** → repo root.
2. **16 lessons (L01–L16)** → repo `lessons/`.
3. **`tutor.html`** → repo **`tutor/tutor.html`** (overwrite — it adds the favicon to the already-live logo version).

**Canvas is optional for this one.** The favicon link lives in the `<head>`, which Canvas strips when it renders a lesson, so the Canvas view is unchanged and the favicon won't show there regardless (Canvas uses its own). Push lessons to Canvas only if you want the repo and Canvas versions to stay numerically identical; otherwise repo-only is enough for the favicon to work on the Pages site.

Verify by fresh clone after (~20–30 s cache). Tab icons cache hard — hard-reload (Ctrl/Cmd-Shift-R) to see them.

---

## STILL QUEUED

- **Project B — full goal→logic→template card redesign, book-wide** (authoring, separate session).
- **Syllabus/Canvas entry for the AI Tutor** (students need to be told it exists).
- `.DS_Store` cleanup · `millis()`/`map()` notes · L03_C05 learner mode · L04 C03/C04/C05 · C06 reorder to #1 · whole-template starters L08/L09/L10 · Maker batch · L01 VS Code multi-root.

**BENCH:** C06 · C11 · Q017 L09 six numbers · Q044 calibration-spin · Q046 gyro-bias · L02 §5 green-LED · Constrain RUN_MS.

**PARKED:** solution-disclosure · monetization/ebook · "Know Your Zumo" · day-by-day grid + syllabus · TDP template v3 · §9 difficulty grouping.

---
*Written S58, July 20 2026. Tutor LIVE; favicon batch (index + 16 lessons + tutor) staged, not pushed.*
