# LIVE_ZUMO_TEXTBOOK.md

**Date:** July 21, 2026 (Session 60 — Project B part A / shell normalization: L02–L05, L08–L15 all on canonical shells).
**Status:** **Every lesson now on a canonical challenge-card shell.** L02 v02.5.0 / L03 v03.7.0 / L04 v04.2.0 shell-repaired & LIVE (`46187dc`); prior conversions L08–L15 also live. Maker **v2.41**, Bible **v8.38**. This file (LIVE.md) is the only remaining push.

**Versions:** L01 v03.4.3 · L02 **v02.5.0** · L03 **v03.7.0** · L04 **v04.2.0** · L05 v04.3.0 · L06 v04.7.3 · L07 v04.3.13 · L08 **v04.2.0** · L09 **v05.1.0** · L10 **v02.2.0** · L11 **v02.3.0** · L12 v01.3.0 · L13 v02.3.0 · L14 **v02.5.0** · L15 **v02.3.0** · L16 v02.2.5 · Bible **v8.38** · Maker **v2.41** · Gate v1.6 · Harness v3.0.

---

## WHAT SHIPPED THIS BATCH — L14 v02.5.0 · L15 v02.3.0 · Maker v2.41

**L14 (Competition Prep) — 3 challenges, hybrid.** C1 Wheel Test (MEDIUM) + C3 LoP Counter (TOUGH) → full Goal→Logic→Template cards; C2 Strict Mode (EASY) → prose card (three-line trick-question answer; panels would be hollow). Blanks verified to fill exactly to each solution.

**L15 (The Present Isn't Enough / PID) — 7 challenges, two groups.** C1–C3 (MEDIUM) → full panel cards, multi-part solutions preserved verbatim in the reveal (all three templates fill exactly to solution). C4–C7 (HARD ×3 / ADVANCED) → canonical shell + **prose, no panels** — preserving their deliberately-open, no-solution design (the §9 intro states it: "the first three ship with solutions, the last four do not"). Two internal cross-refs to "Challenge 9.2" updated → "Challenge 2".

**L02 + L03 + L04 — shell repair, lesson-only.** All 19 challenges: stripped the old white/gray body wrappers, hoisted 📁 Work-in + 🔍 Where-to-look into the pale-yellow bar, dropped the 📝 Plan-first line from L02/L03 (their Maker templates already carry the MY PLAN block — confirmed `mainCpp()` adds it for lesson>1), and reskinned solutions flush. Preserved: L03’s 14 teaching callouts, L04’s timer iframes + hint/solution reveals, all solution code (gate PASS on each). Goal/task stays prose for now — the full Goal/Logic/Template panel bodies are the in-progress next phase. L02 v02.4.3→v02.5.0, L03 v03.6.3→v03.7.0, L04 v04.1.5→v04.2.0.

**L10 (Obstacles) — green callout → canonical card, lesson-only.** All 5 challenges restyled from the old green left-border callout to the plum-box card: gradient header with sequential “Challenge N: Title”, canonical pill, new Work-in bar, and 🎯 Goal / 🧠 Logic / 🧩 Template moved from inline <strong> labels into panels. C1/C2/C4 keep their Template code shown openly (L10 has no separate solutions — disclosure unchanged); C3/C5 stay prose. Word-level diff confirms only the header restyling + Work-in bars changed — all Goal/Logic/Template/hint text byte-preserved. No Maker touch (gate confirms L10’s 20 payloads untouched). L10 v02.1.15 → v02.2.0.

**L08 + L09 — Template panels added, lesson-only.** Both lessons were already canonical cards (shell + Goal + Logic); the only §6.12a gap was the missing 🧩 Template panel. Added 8 Templates: L08 8.4 (Position Bar) + 8.5 (Adaptive Kp); L09 9.1–9.6 (all algorithmic). L08’s 3 bench-tuning challenges (8.1–8.3) correctly stay Goal+Logic — no code answer. Each Template was built by blanking tokens directly in the existing solution (values/identifiers only, structure preserved), so filling the blanks reconstructs the solution byte-for-byte. Solutions, hint ladders, and disclosure untouched — no Maker change, parked disclosure call unaffected. L08 v04.1.10 → v04.2.0, L09 v05.0.12 → v05.1.0.

**L11 (Time Lies, Distance Doesn't) — 3 challenges + 4 mysteries, lesson-only.** The 3 challenges (The Retreat / EASY, The Hunt / MEDIUM, The Speed Budget / HARD) → full Goal→Logic→Template cards; each hint folded into its Logic panel; solutions preserved verbatim (gate confirms they still byte-match). Already sequential with `CHALLENGE 1/2/3` comments, so **no renumber, no comment sync, no Maker touch**. The 4 mysteries (a separate `data-kind="mystery"` construct) left in their own Bonus box. Star-text difficulty → canonical pills. L11 v02.2.5 → v02.3.0.

**Both:** headings "9.x" → **sequential "Challenge N"**; the `// CHALLENGE 9.x` solution comments synced to `1/2/3/…` in the lesson **and** the matching Maker payloads (L14: `c1_wheeltest/c2_strict/c3_lop`; L15: `c1_gainsched/c2_dfilter/c3_worstdt`). Comment-only; executable bodies unchanged. L13's `9.x` comments deliberately left (see queue). Old inline `[TIER]` text tags → canonical five-tier pills. Full payload gate PASS; diff-audit clean on both.

---

## PUSH BATCH (S60)

1. **`LIVE_ZUMO_TEXTBOOK.md`** → repo root. *(All lessons already pushed: L14/L15 + Maker v2.41 `a2238937`; L11 `63abdc3`; L08/L09 `7de0402`; L10 `92e7e31`.)*

Verify by fresh clone (~30–40 s cache lag).

---

## STILL QUEUED (S61)

- **Project B part B — full panels (IN PROGRESS):** author 🎯 Goal / 🧠 Logic / 🧩 Template panels for the ~17 algorithmic challenges in L02 (2.2–2.5), L03 (3.1–3.8), L04 (4.1–4.5); debug/no-solution ones (2.1, 2.6) stay prose. Part A (shell normalization) is DONE book-wide. **Shells canonical: all lessons.**
- **L13 solution-comment fix (carried from S59):** L13 cards say "Challenge 1/2/3" but the revealed-solution comments + `c1_sweep/c2_report/c3_rowzero` payloads still read `// CHALLENGE 9.x` — coordinated lesson+Maker sync, same operation just applied to L14/L15. Bumps L13 + Maker.
- **Difficulty-progression audit (NEW, DJ-requested S60):** book-wide check that L01→L16 actually ramps consistently — easy at L01–L03, steadily harder after. Run once the Project B rollout is complete; verify we're doing what we set out to do.

**LOGIN / TRACKING (parked, DJ "back burner" S60 — architecture confirmed):** The Robot-Trainer shell (`weymuth.github.io/Robot-Trainer/`) authenticates via a Cloudflare Worker `zumoauth.weymuthd.workers.dev` (session cookie; `/me` returns `{username}` = lastname+firstinitial, e.g. `weymuthd`; `/track` logs events; `home.html` already fires both). The zumo book/Maker share the origin `weymuth.github.io`, so the Worker already trusts them and the cookie already flows — no backend change needed to read `/me`. Deferred pieces, in order of appetite: (1) wire the Maker to `/me` to auto-fill the folder from the login and drop the name prompt (folder = the username directly; ~10 lines JS; keep a manual fallback for no-session opens); (2) a shared tracking snippet on the book/Maker/tutor pages (lesson-opened, key clicks, and — DJ: **definitely** — read-quality: scroll-depth + focus-time) posting to `/track`; this needs the Worker to actually **persist** the event stream somewhere queryable per student. Soft posture only (identity + logging, book stays readable without a session); hard-gating the book is a separate hosting change that only earns its keep if monetizing. Note: minors' behavioral data — keep minimal.

**BENCH:** C06 · C11 · Q017 L09 six numbers · Q044 calibration-spin · Q046 gyro-bias · L02 §5 green-LED · Constrain RUN_MS.

**PARKED:** solution-disclosure · monetization/ebook · "Know Your Zumo" · day-by-day grid + syllabus · TDP template v3 · §9 difficulty grouping · challenge-card full goal→logic→template redesign for the ~80 challenges that lack it (Project B pass B).

---
*Written S60, July 21 2026. L02 v02.5.0 + L03 v03.7.0 + L04 v04.2.0 shell-repaired & live (`46187dc`); every lesson now on a canonical shell. Full panels for L02–L04 in progress.*
