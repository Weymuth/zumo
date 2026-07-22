# LIVE_ZUMO_TEXTBOOK.md

**Date:** July 22, 2026 (Session 61 — book-wide callout standardization sweep: all 16 lessons now type Tip/Note/Warning by function; L15/L16 de-boxed).
**Status:** **Callout sweep complete, L01–L16.** Every coach callout now types by *function* on canonical colors per Bible §6.6a — Tip 💡 (make it work) / Note 📘 (why/context) / Warning ⚠️ (real caution). Book-wide totals: 77 Tip · 107 Note · 72 Warning. L15/L16 came into the system via **de-boxing**: ~52 rhetorical/analogy/flow boxes flattened to prose, 21 real callouts kept as typed boxes, formal devices (Key Terms, COMPILE CHECK, ENGINEER'S LOG, 🏆 RoboCup Connection) left intact. Triple-checked: div-balanced 16/16, zero content loss (only the bared "Coach" label word removed), formal devices byte-unchanged. **Bible v8.40** (§6.6a callout-by-function + §6.6 13-icon legend) and **Maker v2.43** are on disk. **STAGED, NOT PUSHED.** Robot-icon-family still blocked (S61 — image quality + ChatGPT credits); the single Zumo mark on the Textbook tile (`index.html` + `images/Zumo_Robot_Mark.png`) is in the working tree.

**Versions:** L01 v03.5.0 · L02 v02.9.0 · L03 v03.9.0 · L04 v04.4.0 · L05 v04.4.0 · L06 v04.8.0 · L07 v04.4.0 · L08 v04.3.0 · L09 v05.2.0 · L10 v02.3.0 · L11 v02.4.0 · L12 v01.4.0 · L13 v02.4.0 · L14 v02.6.0 · L15 v02.4.0 · L16 v02.3.0 · Bible **v8.40** · Maker **v2.43** · Gate v1.6 · Harness v3.0.

---

## WHAT SHIPPED THIS BATCH (S61) — book-wide callout standardization · all 16 lessons

**The sweep.** Every "Coach's Tip/Note" and drifted color-coded box across L01–L16 was re-typed by **function** onto the Bible §6.6a canonical system: **Tip 💡** = actionable "make it work / fix it" (`#f0f7f0`), **Note 📘** = enrichment "why / context" (`#eceff1`), **Warning ⚠️** = real caution/safety (`#fff8e1`). Reassignment was by function, not original icon (the book had Tip/Note inverted in places). Bare labels, no "Coach's". Book-wide totals: **77 Tip · 107 Note · 72 Warning.**

**Left alone (formal/distinct devices, not coach callouts):** 🔑 Key Term · 📖 LEARN · 🔍 INSIGHT · 📝 DO-THIS-NOW / rituals · ✅ CHECKPOINT · 👀 WHAT YOU SHOULD SEE · 🎯 CHALLENGE / THE GOAL · 🔮 WHAT'S NEXT · 🔁 Builds on · 📦 Fell behind? · 🏁 FINISHED EARLY? · 📋 PREREQUISITES · 🔨 COMPILE CHECK · 📓 ENGINEER'S LOG · 🏆 RoboCup Connection · type-explainer (`#e3f2fd`).

**L15 / L16 — de-boxed (different treatment).** These two used a bespoke color-coded emphasis-box system (~53 / ~40 boxes, mostly no labels — analogies, verdicts, takeaways). Decision: the typed Tip/Note/Warning system is better for beginners (explicit beats implicit color-code), and 40–53 boxes is bad reading. So rhetorical/analogy/flow boxes were **de-boxed** (styling stripped to `margin: 16px 0;` — content + div kept, zero balance risk) and only genuine callouts kept as canonical typed boxes. L15: 10 Warning / 3 Note / 1 Tip kept, ~39 flattened. L16: 4 Warning / 2 Note / 1 Tip kept, ~13 flattened. Formal devices left intact.

**Verification (triple-checked).** 16/16 div-balanced · zero double-icons · zero malformed styles · zero empty de-boxed divs · every lesson shows balanced +/- edits (in-place swaps, no content deletion) · de-box removed only the bared "Coach" label word · formal devices byte-unchanged vs repo HEAD.

**Also on disk, staged, unpushed:** Bible **v8.40** (§6.6a callout-by-function + §6.6 13-icon legend incl. 📘) · Maker **v2.43** · S61 robot mark on Textbook tile (`index.html` + `Zumo_Robot_Mark.png`). Robot-icon-**family** remains blocked (S61 image quality + ChatGPT credits).

**Next.** Difficulty-progression audit (L01–L03 easy, consistent hardening across all 16 — DJ's stated big goal). Future: expand the 📓 Engineer's Log icon/section (DJ likes it). Standing parked queue unchanged.

**Versions this batch:** L01 v03.5.0 · L02 v02.9.0 · L03 v03.9.0 · L04 v04.4.0 · L05 v04.4.0 · L06 v04.8.0 · L07 v04.4.0 · L08 v04.3.0 · L09 v05.2.0 · L10 v02.3.0 · L11 v02.4.0 · L12 v01.4.0 · L13 v02.4.0 · L14 v02.6.0 · L15 v02.4.0 · L16 v02.3.0.

---

## WHAT SHIPPED THIS BATCH — L14 v02.5.0 · L15 v02.3.0 · Maker v2.41

**L14 (Competition Prep) — 3 challenges, hybrid.** C1 Wheel Test (MEDIUM) + C3 LoP Counter (TOUGH) → full Goal→Logic→Template cards; C2 Strict Mode (EASY) → prose card (three-line trick-question answer; panels would be hollow). Blanks verified to fill exactly to each solution.

**L15 (The Present Isn't Enough / PID) — 7 challenges, two groups.** C1–C3 (MEDIUM) → full panel cards, multi-part solutions preserved verbatim in the reveal (all three templates fill exactly to solution). C4–C7 (HARD ×3 / ADVANCED) → canonical shell + **prose, no panels** — preserving their deliberately-open, no-solution design (the §9 intro states it: "the first three ship with solutions, the last four do not"). Two internal cross-refs to "Challenge 9.2" updated → "Challenge 2".

**L13 — solution-comment sync (lesson + Maker).** L13’s cards read “Challenge 1/2/3” but its revealed-solution comments + payloads (c1_sweep/c2_report/c3_rowzero) still said “// CHALLENGE 9.x” — synced to 1/2/3 in both the lesson and the three Maker payloads (count-guarded; no collision with L09, which uses a different convention). Gate PASS, node --check clean. L13 v02.3.0→v02.3.1 (minor — banner unchanged per §5b), Maker v2.41→v2.42.

**L02 + L03 + L04 — FULL PANELS (lesson-only).** Added 🎯 Goal / 🧠 Logic (Pseudocode) / 🧩 Template panels to every algorithmic challenge: L02 2.2–2.5, L03 3.1–3.7 (3.8 research = Goal+Logic), L04 4.1–4.5. Debug/no-solution types (L02 2.1, 2.6) stay prose. Template blanks fill to the real solution tokens (verified). Built with a preserve-everything rebuild after an early version dropped middle prose — triple-checked vs the original pre-shell files: zero prose/code/image/anchor/Maker-link loss, gate PASS, div balance 0, versions consistent. ⚠️ L02 v02.6.0 (the first panel build) had dropped prose and was superseded by v02.7.0. Versions: L02 v02.5.0→v02.7.0, L03 v03.7.0→v03.8.0, L04 v04.2.0→v04.3.0.

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

- **Project B — DONE.** Shells canonical book-wide; Goal/Logic/Template panels on every algorithmic challenge L02–L15. L01 stays prose, L06/L07 already conformed, L16 = tier-cards (all intentional). Any remaining challenge-card polish is a future pass, not a gap.
- **Difficulty-progression audit (NEW, DJ-requested S60):** book-wide check that L01→L16 actually ramps consistently — easy at L01–L03, steadily harder after. Run once the Project B rollout is complete; verify we're doing what we set out to do.

**LOGIN / TRACKING (parked, DJ "back burner" S60 — architecture confirmed):** The Robot-Trainer shell (`weymuth.github.io/Robot-Trainer/`) authenticates via a Cloudflare Worker `zumoauth.weymuthd.workers.dev` (session cookie; `/me` returns `{username}` = lastname+firstinitial, e.g. `weymuthd`; `/track` logs events; `home.html` already fires both). The zumo book/Maker share the origin `weymuth.github.io`, so the Worker already trusts them and the cookie already flows — no backend change needed to read `/me`. Deferred pieces, in order of appetite: (1) wire the Maker to `/me` to auto-fill the folder from the login and drop the name prompt (folder = the username directly; ~10 lines JS; keep a manual fallback for no-session opens); (2) a shared tracking snippet on the book/Maker/tutor pages (lesson-opened, key clicks, and — DJ: **definitely** — read-quality: scroll-depth + focus-time) posting to `/track`; this needs the Worker to actually **persist** the event stream somewhere queryable per student. Soft posture only (identity + logging, book stays readable without a session); hard-gating the book is a separate hosting change that only earns its keep if monetizing. Note: minors' behavioral data — keep minimal.

**BENCH:** C06 · C11 · Q017 L09 six numbers · Q044 calibration-spin · Q046 gyro-bias · L02 §5 green-LED · Constrain RUN_MS.

**PARKED:** *(low priority, down-the-road)* challenge **countdown timers** — consider a SELECTIVE rollout to short/bounded "quick attempt" challenges only (not the heavy multi-step builds), decide after the fall classroom run; note they’re online-only (iframe), so solve the Canvas-display wrinkle first · solution-disclosure · monetization/ebook · "Know Your Zumo" · day-by-day grid + syllabus · TDP template v3 · §9 difficulty grouping · challenge-card full goal→logic→template redesign for the ~80 challenges that lack it (Project B pass B).

---
*Written S60, July 21 2026. Project B complete and clean across L01–L16; L13 sync (v02.3.1) + Maker v2.42 the final cleanup. This push = L13 + Maker + LIVE.md.*
