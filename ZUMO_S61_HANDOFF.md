# ZUMO — S61 Handoff (written at S60 close, Jul 21 · paste at top of Session 61)

## Session-open ritual (do automatically, no upload needed)
1. `git clone --depth 1 https://github.com/Weymuth/zumo.git` — the repo is source of truth.
2. Read `LIVE_ZUMO_TEXTBOOK.md` from the clone — verify date / status / currently-working-on.
3. `grep -oE "Bible version: v[0-9.]+" ZUMO_SUPER_BIBLE.md` — confirm internal version.
4. LIVE.md always wins over memory and over any pasted version. Grep the actual file; never trust a pasted number.

## LIVE STATE — verified by fresh clone, Jul 21, commit `88ee6af` ("wrapping up s60")
Bible **v8.38** · Maker **v2.42** · Gate v1.6 · Harness v3.0
L01 v03.4.3 · L02 v02.7.0 · L03 v03.8.0 · L04 v04.3.0 · L05 v04.3.0 · L06 v04.7.3 · L07 v04.3.13 · L08 v04.2.0 · L09 v05.1.0 · L10 v02.2.0 · L11 v02.3.0 · L12 v01.3.0 · L13 v02.3.1 · L14 v02.5.0 · L15 v02.3.0 · L16 v02.2.5

## HEADLINE — Project B is COMPLETE and clean across L01–L16
Every challenge card uses the canonical §6.12a shell (plum box · gradient header with **sequential "Challenge N"** · five-tier pill · pale-yellow Work-in bar · flush solution). Sequential headers now match their solution comments **and** Maker payloads everywhere. Card **bodies are type-correct**: 🎯 Goal / 🧠 Logic / 🧩 Template panels on algorithmic challenges; prose on debug / observation / tuning / open ones.
**Intentional exceptions (not gaps):** L01 = canonical shells with prose bodies (its challenges are simple guided-edit); L16 = tier-cards (project tiers, no challenge cards); L11's 4 "mysteries" = a separate bonus construct, not challenges.

## DONE IN S60 (all pushed & fresh-clone/md5 verified)
- **Challenge-card conversions:** L08, L09, L10, L11, L14, L15 → canonical cards + panels.
- **L02 / L03 / L04:** shell repair (stripped white/gray body wrappers → pale-yellow Work-in bar; dropped the "📝 Plan first:" line — their Maker templates already carry MY PLAN, confirmed `mainCpp()` adds it for lesson>1) **then full Goal/Logic/Template panels**. Built with a **preserve-everything rebuild** after a first attempt (L02 v02.6.0) dropped middle prose — triple-checked vs the original pre-shell files: zero prose/code/image/anchor/Maker-link loss, gate PASS, div balance 0. L02 v02.6.0 was superseded by v02.7.0.
- **L13 comment sync (last loose end):** L13 cards said "Challenge 1/2/3" but its solution comments + payloads (c1_sweep/c2_report/c3_rowzero) still said `// CHALLENGE 9.x` → synced to 1/2/3 in lesson + Maker (count-guarded, no L09 collision). L13 v02.3.1, Maker v2.42.
- LIVE.md kept current throughout.

## S61 QUEUE (in rough priority order)
1. **Difficulty-progression audit (DJ-requested).** Book-wide check that L01→L16 ramps consistently — easy at L01–L03, steadily harder after. Project B is done, so this is the natural next pass. Deliverable: a per-lesson difficulty read + any re-rates/reorders needed (each reorder is a coordinated lesson+Maker edit: renumber cards, move `kind=` ids + reveal blocks + cross-refs, re-rate pills).
2. **Login / identity / tracking** (DJ "back burner," architecture confirmed S60). The Robot-Trainer shell authenticates via Cloudflare Worker `zumoauth.weymuthd.workers.dev` (`/me`→`{username}` = lastname+firstinitial; `/track` logs events). The zumo book/Maker share origin `weymuth.github.io`, so the Worker already trusts them and the cookie already flows — **no backend change needed to read `/me`**. Deferred pieces: (a) wire the Maker to `/me` to auto-fill the folder from login and drop the name prompt (~10 lines JS, keep manual fallback); (b) a shared tracking snippet on book/Maker/tutor posting to `/track` — including **read-quality (scroll-depth + focus-time)**, which DJ said "definitely do" when we do it — this needs the Worker to actually **persist** the event stream queryably per student. Soft-gate posture only; hard-gating only worth it if monetizing. Caveat: minors' behavioral data — keep minimal.
3. **L03_C05 Variable Speed** learner-mode build (DJ paused mid-way in an earlier session; starter saved) — resume if DJ wants to keep coaching himself.

## PARKED (do not reopen unprompted)
- **Timers — LOW priority, down-the-road.** Consider a **selective** rollout to short/bounded "quick attempt" challenges only (not heavy multi-step builds); decide after the fall classroom run. They're online-only (iframe) → solve the Canvas-display wrinkle first.
- Solution-disclosure policy (DJ rules after classroom use) · monetization/ebook (after book done) · "Know Your Zumo" reference page (after book done) · AI Tutor further polish (rebuilt & live; discoveries not yet in the picker) · day-by-day grid + syllabus finalization · TDP template v3 (add A5 Lab Log) · full richer-card redesign for any remaining challenges (most are done).

## WORKING DRAFTS (DJ's folder, NOT repo — keep building)
`ZUMO_Syllabus_WORKING.md` · `ZUMO_Teacher_Daily_Grid_WORKING.md` · `ZUMO_Resource_Section_WORKING.md` · `ZUMO_TDP_Template_v2.md` (repo root has the live TDP template).

## BENCH ITEMS (need the robot; carried)
Q017 L09 green-tape six numbers · Q044 calibration-spin stopwatch · Q046 gyro-bias · L02 §5 green-LED bench check · Constrain RUN_MS.

## Process reminders that paid off in S60
- **Preserve the WHOLE card body** when restyling — extract only the piece you're relabeling (the Goal), keep everything else in order; a selective "Goal + solution only" rebuild silently drops middle prose (hit twice).
- **Verify every "pushed"** with a fresh `--depth 1` clone + md5 vs staged, and check WHICH version landed. Allow ~30–40 s for GitHub propagation before declaring a push failed (a clone caught a push seconds early twice this session).
- Depth-match card spans; `h[i:nxt]` where nxt = next challenge's marker runs into the next card's opening tag.
- `<div\b` in Python regex needs a single backslash — `<div\\b` matches nothing and reports phantom imbalance.
- Scoped comment/payload syncs: use the specific full strings, never a bare `9.x` global-replace (L09 uses "9.x" legitimately; changelog notes reference it too).
- LIVE.md at the push point: grep versions, never hand-type; regenerate after every version-bumping push (a version bump without LIVE.md is an incomplete push).
