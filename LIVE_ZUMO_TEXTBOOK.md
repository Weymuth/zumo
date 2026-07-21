# LIVE_ZUMO_TEXTBOOK.md

**Date:** July 20, 2026 (Session 59 — Project B begins: challenge-card standardization).
**Status:** ⚠️ **STAGED, NOT PUSHED.** Three lessons converted to the canonical Goal→Logic→Template card format. Push = lessons → repo + Canvas. No SVGs, no Maker (every referenced `kind=` is already live).

**Versions:** L01 v03.4.3 · L02 v02.4.3 · L03 v03.6.3 · L04 v04.1.5 · L05 **v04.3.0** · L06 v04.7.3 · L07 v04.3.13 · L08 v04.1.10 · L09 v05.0.12 · L10 v02.1.15 · L11 v02.2.5 · L12 **v01.3.0** · L13 **v02.3.0** · L14 v02.4.5 · L15 v02.2.6 · L16 v02.2.5 · Bible v8.37 · Maker v2.39 · Gate v1.6 · Harness v3.0.

---

## WHAT SHIPPED THIS BATCH — Project B rollout (3 lessons)

Project B (make every lesson's §9 challenge cards consistent) begins. Three lessons converted to the L06 canonical card:

- **L05 v04.2.5 → v04.3.0** — the pilot. 5 challenges reshaped into Work-in bar → 🎯 Goal → 🧠 Logic → 🧩 Template → solution. Hint folded into Logic; Plan-first dropped. DJ-approved format.
- **L12 v01.2.6 → v01.3.0** — 3 bare-heading challenges converted. YOUR-NUMBER two-level scaffold (Template blanks the concept; the solution keeps the tuning blank). Difficulty inferred (M/M/H). Solved-build Maker links kept inside the solution.
- **L13 v02.2.5 → v02.3.0** — 3 challenges converted. Renumbered "Challenge 9.x" → sequential "Challenge N" (canon §6.12) + 2 prose cross-refs. First use of the TOUGH tier (rising M/TOUGH/H, inferred). Solution code comments kept `// CHALLENGE 9.x` (they byte-match the Maker payloads).

**Verified before push:** structure (panels/tags/versions agree), correctness (all blanks fill to their solutions), payload gate **PASS full book** (L12 168 bodies, L13 152), pill census clean (73 pills, all §6.12, zero retired EXPERT/COMPETITION).

**Rulings locked (→ Bible spec, not yet written):** the shell is uniform on every card; the inner format fits the challenge type (algorithmic → 3 panels; guided-edit/debug/observation → prose); hint→Logic; no Plan-first; **L01 stays as-is** (guided-edit). Provisional pending DJ's student runthrough: L08/L09 get Template + solution shown; YOUR-NUMBER two-level scaffold; difficulty/QR/starter handling.

---

## PUSH BATCH (S59)

1. **lessons/Lesson_05.html** (v04.3.0) · **lessons/Lesson_12.html** (v01.3.0) · **lessons/Lesson_13.html** (v02.3.0) → repo + Canvas.
2. **LIVE_ZUMO_TEXTBOOK.md** → repo root.

No SVGs, no Maker, no Bible this batch. Verify by fresh clone (~30–40 s cache lag).

---

## STILL QUEUED (S60)

- **WRITE THE BIBLE SPEC FIRST** — canonical challenge-card spec (shell mandatory; inner-fits-type; §6.12 pills by reference; open-case resolutions marked provisional). Do this before more conversions.
- **Project B — continue:** L14 next (verify format), then L15, L11 (+4 mysteries), L08/L09 (add Template + show solution), L10 (green-callout → purple-card convert). L02/L03/L04 = per-challenge hybrid + shell repair. L06/L07 already canonical.
- **Maker follow-ups (new, from S59):** L12 challenges have no starter payloads (Work-in bars name the build only) → add starters; L13 solution comments `// CHALLENGE 9.x` should sync to `1/2/3` in the `c1_sweep`/`c2_report`/`c3_rowzero` payloads (coordinated lesson+Maker edit).
- Syllabus/Canvas entry for the AI Tutor · discoveries in tutor picker (`data-kind="discovery"`) · `.DS_Store` cleanup · `millis()`/`map()` notes · learner-mode L03_C05 + L04 C03/C04/C05 · C06 reorder to #1 · whole-template starters L08/L09/L10 · Maker batch · L01 VS Code multi-root.

**BENCH:** C06 · C11 · Q017 L09 six numbers · Q044 calibration-spin · Q046 gyro-bias · L02 §5 green-LED · Constrain RUN_MS.

**PARKED:** solution-disclosure · monetization/ebook · "Know Your Zumo" · day-by-day grid + syllabus · TDP template v3 · §9 difficulty grouping.

---
*Written S59, July 20 2026. Project B begins — L05/L12/L13 converted, staged not pushed.*
