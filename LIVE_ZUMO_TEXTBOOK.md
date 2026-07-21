# LIVE_ZUMO_TEXTBOOK.md

**Date:** July 20, 2026 (Session 58 — Bible §20, the AI-tutor/marker canon).
**Status:** ⚠️ **STAGED, NOT PUSHED.** All S58 content is LIVE (commit `4c57e20`): AI Tutor rebuilt and running, favicon site-wide. This batch is a **Bible-only** update — no lessons, no Maker.

**Versions:** L01 v03.4.3 · L02 v02.4.3 · L03 v03.6.3 · L04 v04.1.5 · L05 v04.2.5 · L06 v04.7.3 · L07 v04.3.13 · L08 v04.1.10 · L09 v05.0.12 · L10 v02.1.15 · L11 v02.2.5 · L12 v01.2.6 · L13 v02.2.5 · L14 v02.4.5 · L15 v02.2.6 · L16 v02.2.5 · Bible **v8.37** · Maker v2.39 · Gate v1.6 · Harness v3.0.

---

## WHAT SHIPPED THIS BATCH — Bible v8.36.2 → v8.37

**§20 AI TUTOR & MACHINE MARKERS (new section)** — locks in everything S58 built so future content can't silently break the tutor:
- The tutor's anti-rot principle (reads live lessons, embeds no curriculum) + architecture + the browser↔worker contract + how to edit the worker.
- **§20.1 `data-reveal` on every `<details>`** — vocabulary; the tutor strips only `solution`, so any graded answer (incl. debugging-mystery bug+fix reveals) must be typed `solution` or it leaks; an open-prose/`<pre>` solution is NOT stripped; safe default = `solution`.
- **§20.2 `data-challenge` on every challenge** — uniform marker + `LL.N` numbering; the picker queries `[data-challenge]`, so an untagged challenge vanishes; L16 tiers exempt.
- **§20.3** both markers mandatory on new content (+ close-gate).
- **§20.4** favicon needs an explicit per-page `<link>` on a Pages project site.

**§12.4 VERIFICATION DISCIPLINE — CACHES LIE** — shallow-clone lag; `git show --stat` on a shallow clone lists the whole tree as "added" (don't judge a commit by it); raw/API caches; the upload-location trap.

**Accuracy fixes:** §12.1 repo list now points at `tutor/tutor.html` + `tutor/worker.js`; §19 no longer calls the tutor "queued LAST" (it's live, → §20).

---

## PUSH BATCH (S58, Bible)

1. **`ZUMO_SUPER_BIBLE.md`** (v8.37) → repo root.
2. **`LIVE_ZUMO_TEXTBOOK.md`** → repo root.

No lessons, no Maker, no Canvas. Verify by fresh clone (allow ~30–40 s for cache).

---

## STILL QUEUED (S59)

- **Syllabus/Canvas entry for the AI Tutor** (tell students it exists — low-effort, high-value before Sept 8).
- **Project B — full goal→logic→template card redesign, book-wide** (authoring, separate session).
- **HOLDING PATTERN:** discoveries in the tutor picker (tag with `data-kind="discovery"`); a future replacement image for the tutor logo.
- `.DS_Store` cleanup · `millis()`/`map()` notes · L03_C05 learner mode · L04 C03/C04/C05 · C06 reorder to #1 · whole-template starters L08/L09/L10 · Maker batch · L01 VS Code multi-root.

**BENCH:** C06 · C11 · Q017 L09 six numbers · Q044 calibration-spin · Q046 gyro-bias · L02 §5 green-LED · Constrain RUN_MS.

**PARKED:** solution-disclosure · monetization/ebook · "Know Your Zumo" · day-by-day grid + syllabus · TDP template v3 · §9 difficulty grouping.

---
*Written S58, July 20 2026. AI Tutor LIVE (`4c57e20`); Bible v8.37 staged, not pushed.*
