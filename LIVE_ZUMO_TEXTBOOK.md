# LIVE_ZUMO_TEXTBOOK.md

**Date:** July 21, 2026 (Session 60 — Project B: L14 + L15 converted to the canonical challenge card).
**Status:** **L14 + L15 are LIVE** (commit `a2238937`, "14 & 15 Update") — fresh-clone + md5 verified. Maker at **v2.41**. This file (LIVE.md) is the only remaining push for the batch → repo root. Bible unchanged (v8.38).

**Versions:** L01 v03.4.3 · L02 v02.4.3 · L03 v03.6.3 · L04 v04.1.5 · L05 v04.3.0 · L06 v04.7.3 · L07 v04.3.13 · L08 v04.1.10 · L09 v05.0.12 · L10 v02.1.15 · L11 v02.2.5 · L12 v01.3.0 · L13 v02.3.0 · L14 **v02.5.0** · L15 **v02.3.0** · L16 v02.2.5 · Bible **v8.38** · Maker **v2.41** · Gate v1.6 · Harness v3.0.

---

## WHAT SHIPPED THIS BATCH — L14 v02.5.0 · L15 v02.3.0 · Maker v2.41

**L14 (Competition Prep) — 3 challenges, hybrid.** C1 Wheel Test (MEDIUM) + C3 LoP Counter (TOUGH) → full Goal→Logic→Template cards; C2 Strict Mode (EASY) → prose card (three-line trick-question answer; panels would be hollow). Blanks verified to fill exactly to each solution.

**L15 (The Present Isn't Enough / PID) — 7 challenges, two groups.** C1–C3 (MEDIUM) → full panel cards, multi-part solutions preserved verbatim in the reveal (all three templates fill exactly to solution). C4–C7 (HARD ×3 / ADVANCED) → canonical shell + **prose, no panels** — preserving their deliberately-open, no-solution design (the §9 intro states it: "the first three ship with solutions, the last four do not"). Two internal cross-refs to "Challenge 9.2" updated → "Challenge 2".

**Both:** headings "9.x" → **sequential "Challenge N"**; the `// CHALLENGE 9.x` solution comments synced to `1/2/3/…` in the lesson **and** the matching Maker payloads (L14: `c1_wheeltest/c2_strict/c3_lop`; L15: `c1_gainsched/c2_dfilter/c3_worstdt`). Comment-only; executable bodies unchanged. L13's `9.x` comments deliberately left (see queue). Old inline `[TIER]` text tags → canonical five-tier pills. Full payload gate PASS; diff-audit clean on both.

---

## PUSH BATCH (S60)

1. **`LIVE_ZUMO_TEXTBOOK.md`** → repo root. *(Lessons L14/L15 + `newproject.html` v2.41 already pushed in `a2238937`.)*

Verify by fresh clone (~30–40 s cache lag).

---

## STILL QUEUED (S61)

- **Project B — continue the rollout** against §6.12a: **L11 next** (3 challenges + 4 mysteries — mysteries stay prose), then L08/L09 (add Template + show solution — open case), L10 (green-callout → purple-card convert), L02/L03/L04 (per-challenge hybrid + shell repair). L06/L07 already conform. L05/L12/L13/L14/L15 done.
- **L13 solution-comment fix (carried from S59):** L13 cards say "Challenge 1/2/3" but the revealed-solution comments + `c1_sweep/c2_report/c3_rowzero` payloads still read `// CHALLENGE 9.x` — coordinated lesson+Maker sync, same operation just applied to L14/L15. Bumps L13 + Maker.
- **Difficulty-progression audit (NEW, DJ-requested S60):** book-wide check that L01→L16 actually ramps consistently — easy at L01–L03, steadily harder after. Run once the Project B rollout is complete; verify we're doing what we set out to do.

**LOGIN / TRACKING (parked, DJ "back burner" S60 — architecture confirmed):** The Robot-Trainer shell (`weymuth.github.io/Robot-Trainer/`) authenticates via a Cloudflare Worker `zumoauth.weymuthd.workers.dev` (session cookie; `/me` returns `{username}` = lastname+firstinitial, e.g. `weymuthd`; `/track` logs events; `home.html` already fires both). The zumo book/Maker share the origin `weymuth.github.io`, so the Worker already trusts them and the cookie already flows — no backend change needed to read `/me`. Deferred pieces, in order of appetite: (1) wire the Maker to `/me` to auto-fill the folder from the login and drop the name prompt (folder = the username directly; ~10 lines JS; keep a manual fallback for no-session opens); (2) a shared tracking snippet on the book/Maker/tutor pages (lesson-opened, key clicks, and — DJ: **definitely** — read-quality: scroll-depth + focus-time) posting to `/track`; this needs the Worker to actually **persist** the event stream somewhere queryable per student. Soft posture only (identity + logging, book stays readable without a session); hard-gating the book is a separate hosting change that only earns its keep if monetizing. Note: minors' behavioral data — keep minimal.

**BENCH:** C06 · C11 · Q017 L09 six numbers · Q044 calibration-spin · Q046 gyro-bias · L02 §5 green-LED · Constrain RUN_MS.

**PARKED:** solution-disclosure · monetization/ebook · "Know Your Zumo" · day-by-day grid + syllabus · TDP template v3 · §9 difficulty grouping · challenge-card full goal→logic→template redesign for the ~80 challenges that lack it (Project B pass B).

---
*Written S60, July 21 2026. L14 v02.5.0 + L15 v02.3.0 + Maker v2.41 live (`a2238937`); this LIVE.md is the batch's final push.*
