# LIVE_ZUMO_TEXTBOOK.md

**Date:** July 20, 2026 (Session 58 — AI Tutor rebuild: reveal-tagging retrofit).
**Status:** ⚠️ **STAGED, NOT PUSHED.** The S58 Bible entry (v8.36.2) is already **LIVE** (commit `b04d431`). This batch bumps **all 16 lessons** — it tags every `<details>` reveal with a `data-reveal` type so the new AI Tutor can strip solutions while keeping hints, troubleshooting, and taught code. Invisible to students (the click-to-reveal UI is unchanged); the tag is inert in the browser.

**Lesson versions — grepped from each file after the bump:**
L01 v03.4.1 · L02 v02.4.1 · L03 v03.6.1 · L04 v04.1.3 · L05 v04.2.3 · L06 v04.7.1 · L07 v04.3.11 · L08 v04.1.8 · L09 v05.0.10 · L10 v02.1.13 · L11 v02.2.3 · L12 v01.2.4 · L13 v02.2.3 · L14 v02.4.3 · L15 v02.2.4 · L16 v02.2.4 · Bible **v8.36.2** · Maker v2.39 · Gate v1.6 · Harness v3.0.

---

## THE AI TUTOR REBUILD — WHERE THIS FITS

The old tutor embedded the whole curriculum in a Cloudflare Worker prompt, frozen at the pre-S28 15-lesson book (taught the cut cliff feature, wrong lesson numbers, no L15/L16). The rebuild makes the tutor **read the live lessons** instead of memorizing them, so it never rots.

Pieces:
1. **Worker v3** (`tutor_worker_v3.js`) — curriculum stripped out; accepts live lesson text from the browser; model Haiku→**Sonnet**; prompt caching for cost. **DEPLOYED to Cloudflare** ("Version Saved"). Source-of-record copy to `tutor/worker.js` is a pending optional commit.
2. **Reveal-tagging retrofit** — THIS batch. Every `<details>` typed so the tutor's stripper keys on a declared type, not guesswork.
3. **`tutor.html`** — NEXT. Fetches the live lesson from Pages, strips `data-reveal="solution"` blocks, sends the rest to the worker; rebuilt 16-lesson challenge picker; moves into `tutor/`.

---

## WHAT SHIPPED THIS BATCH — the `data-reveal` retrofit

All **347** `<details>` blocks across 16 lessons tagged `data-reveal="TYPE"`. The dial (tutor strips `solution` only; everything else is kept and reversible with a one-line stripper change):

| Type | Count | Tutor | What it is |
|---|---|---|---|
| `solution` | 132 | **STRIP** | worked answer code + the L10/L13/L14 sabotage-mystery bug reveals |
| `catchup` | 77 | keep | the lesson's own build states / Maker pointers |
| `hint` | 65 | keep | nudges |
| `check` | 32 | keep | "check your work" / expected output |
| `troubleshoot` | 24 | keep | "Problem:" diagnostic playbook |
| `quiz` | 13 | keep | conceptual review-question answers |
| `mechanism` | 4 | keep | conceptual "how it works" (1 gyro + 3 L03 measurement) |

DJ rulings folded in: strip `solution`; keep `quiz`; the 6 L10 "what is actually wrong" bonus reveals → strip; the 7 L13/L14 sabotage `mechanism` reveals → strip (retyped `solution`) for book-wide consistency; the 1 conceptual gyro block + 3 L03 measurement explanations → keep as `mechanism`.

---

## VERIFICATION

- Retrofit is idempotent (skips a block already carrying `data-reveal`).
- Diff audit: **694 changed lines in lessons, every one a `<details>` tag** + 16 version-comment lines; **0** stray changes. Per-lesson changed-line counts each equal 2×(details) + 2.
- Payload **GATE: PASS** — every payload byte-derives from lesson pres + Maker templates; advisory unchanged at 635. (Tags sit on `<details>`, never inside `<pre>` code, so the gate is untouched.)
- Version bump: hidden comment +1 patch on each lesson (§5b); visible banners deliberately unchanged (cosmetic/infra bump).

---

## PUSH BATCH (S58, batch 2)

1. **16 lessons** → repo `lessons/` (Pages — the tutor reads them from here) **and** Canvas.

No images, no Maker, no Bible in this batch. Verify by fresh clone (§12.4) — allow ~20–30 s for shallow-clone cache. The tagged lessons must be live on Pages before the new `tutor.html` can strip against them.

_Optional/whenever: commit `tutor/worker.js` as the worker's source-of-record; `git rm .DS_Store` + `.gitignore` line._

---

## STILL QUEUED

**AI Tutor rebuild (active):** build `tutor.html` (live fetch + strip + 16-lesson picker, move to `tutor/`); commit worker source-of-record; syllabus entry for the tutor. · `millis()` / `map()` taught-notes (minor) · L03_C05 Variable Speed learner mode · L04 C03 learner mode · L04 C04/C05 walkthroughs · C06 reorder to #1 · whole-template starters L08/L09/L10 · Maker batch (bulk DL · `?lesson=N` gate · C## labels) · L01 VS Code multi-root step.

**BENCH (need robot):** C06 · C11 · Q017 L09 six numbers · Q044 calibration-spin · Q046 gyro-bias · L02 §5 green-LED · Constrain RUN_MS.

**PARKED:** solution-disclosure · monetization/ebook · "Know Your Zumo" · day-by-day grid + syllabus · TDP template v3 (A5 Lab Log) · §9 difficulty grouping · L06 card pattern.

---
*Written S58, July 20 2026. Bible v8.36.2 LIVE (`b04d431`); 16 lessons + reveal tags staged, not pushed.*
