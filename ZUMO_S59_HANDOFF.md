# ZUMO — S59 Handoff (written at S58 close, Jul 20 · paste at top of Session 59)

**S58 was the AI-TUTOR REBUILD session — and it's DONE and LIVE.** The tutor that was queued "LAST" for a dozen sessions is now rebuilt end-to-end and running. Everything below is pushed and verified by fresh clone.

## SESSION OPEN — auto-run, no upload needed (repo is source of truth)
```
git clone --depth 1 https://github.com/Weymuth/zumo.git && cd zumo
grep -o "Lesson version: v[0-9.]*" lessons/Lesson_06.html
grep -oE "Project Maker v2\.[0-9]+" newproject.html | sort -V -u | tail -1
grep -oE "Bible version: v[0-9.]+" ZUMO_SUPER_BIBLE.md
grep -oE "GATE \(Bible §11\) — v1\.[0-9]+" gate_payload_match.py
```
⚠️ **Shallow-clone cache lag is REAL and bit repeatedly in S58** — for ~1–2 min after a push the clone serves the PRIOR commit (looked like a failed push twice; both were just lag). Always `sleep 40` and re-clone before concluding a push didn't land. `sort -V` for the Maker version.

**Expected at open:** commit past `4c57e20` (the Bible push landed after S58 content) · Bible **v8.37** · Maker **v2.39** · Gate **v1.6** · Harness v3.0.

## LIVE STATE at S58 close (all grepped from files)
L01 v03.4.3 · L02 v02.4.3 · L03 v03.6.3 · L04 v04.1.5 · L05 v04.2.5 · L06 v04.7.3 · L07 v04.3.13 ·
L08 v04.1.10 · L09 v05.0.12 · L10 v02.1.15 · L11 v02.2.5 · L12 v01.2.6 · L13 v02.2.5 · L14 v02.4.5 ·
L15 v02.2.6 · L16 v02.2.5 · Bible v8.37 · Maker v2.39 · Gate v1.6 · Harness v3.0.

---

## 🎉 WHAT S58 SHIPPED (all live, do NOT redo)

1. **Bible v8.36.1 → v8.36.2** — §11 AUDIT FALSE-POSITIVE DISCIPLINE (a regex reports candidates, not verdicts; separate code from prose before counting; verify against rendered text before acting).
2. **`data-reveal` retrofit** — every one of the 347 `<details>` across 16 lessons typed `data-reveal="TYPE"`. Types: `solution` (132, STRIPPED by the tutor), `catchup` (77), `hint` (65), `check` (32), `troubleshoot` (24), `quiz` (13), `mechanism` (4). Keep-set = everything except `solution`. Reversible — the tutor's strip rule is one line.
3. **Challenge markup normalization (project A)** — 88 challenge units across L01–L15 tagged with a uniform machine marker: `data-challenge="LL.N"` + `id="challenge-N"` + `data-kind="challenge|mystery"` + `data-difficulty`. L11's 4 mysteries tagged (`11.m1`–`11.m4`). L16 left lesson-level (project tiers, not challenges).
4. **AI Tutor front-end (`tutor/tutor.html`)** — rebuilt; header + welcome carry the Mercersburg dark logo; favicon linked.
5. **Site-wide favicon** — `<link rel="icon">` in `index.html` + all 16 lessons + tutor (Pages project sites don't auto-discover `/favicon.ico` at a subpath).
6. **Bible v8.36.2 → v8.37** — **§20 AI TUTOR & MACHINE MARKERS** (canonizes the tutor + the `data-reveal`/`data-challenge` rules so future content can't silently break it), **§12.4** verification-caches-lie discipline, and §12.1/§19 accuracy fixes.

---

## 🤖 THE AI TUTOR — HOW IT WORKS NOW (reference for future edits)

The old tutor embedded the whole curriculum in a hardcoded Cloudflare Worker prompt — it rotted (taught the cut cliff feature, wrong lesson numbers, no L15/L16). The rebuild makes it **read the live lessons**, so it self-updates whenever a lesson is edited.

- **Worker** (`zumosupport.weymuthd.workers.dev`, Cloudflare — source-of-record at `tutor/worker.js`): curriculum-free coaching prompt; accepts `{messages, currentChallenge, lessonContent, lessonTitle}` from the browser and injects `lessonContent` as authoritative "CURRENT LESSON" context; model **`claude-sonnet-5`**; **prompt caching** on the system block for cost. Holds the ANTHROPIC_API_KEY server-side (students never see it). To edit the worker: dash.cloudflare.com → Workers & Pages → `zumosupport` → Edit code → paste → Deploy, AND update `tutor/worker.js` in the repo.
- **Front-end** (`tutor/tutor.html`): on lesson-select it fetches `../lessons/Lesson_NN.html` from Pages, **removes every `<details data-reveal="solution">`** (so the model never holds the answer key), fences `<pre>` as code, sends the clean text to the worker, and builds a **dynamic per-challenge picker** from the `[data-challenge]` markers (challenges + L11 mysteries; L16 = lesson-level). Keeps code-file upload, welcome, typing, clear. Links: `index.html` → `tutor/tutor.html`.
- **The spoiler dial is data-driven and reversible:** the tutor strips only `data-reveal="solution"`. Want it to also withhold `catchup`, or start showing `mechanism`? One line in the front-end's strip step — no lesson edits. Nothing was ever deleted from the lessons; students still see all reveals via click-to-reveal.

**DJ confirmed the live tutor works** (picked a lesson, sent a message, looked good; logo + favicon showing).

---

## S59 — LIKELY FRONT TASKS

- **Syllabus / Canvas entry for the AI Tutor** — students need to be TOLD it exists and how to use it (pick your lesson, describe the problem, it coaches). The syllabus still has no entry. Low-effort, high-value before Sept 8.
- **Project B — FULL goal→logic→template card redesign, book-wide** (DJ's committed "do it twice" second pass). Apply L06's rich card pattern (🎯 GOAL / 🧠 LOGIC+pseudocode / 🧩 TEMPLATE) to ALL ~80–100 challenges. This is a LARGE **authoring** project (most challenges lack that content — it must be WRITTEN, not scripted), its own multi-session arc. See memory entry "CHALLENGE-CARD STANDARDIZATION."

## HOLDING PATTERN (DJ parked S58, not closed)
- **Discoveries in the tutor picker** — the in-lesson practice builds (Discovery N.1, N.2…) were NOT tagged in project A, so they aren't picker entries. The tutor already helps with them (it reads the whole lesson); adding them as their own dropdown group = tag each with `data-challenge` + `data-kind="discovery"`, a small clean pass. DJ said "holding pattern."
- **A different image for the tutor top-left** — DJ may later provide a raster to replace/augment the logo; drop it in `images/`, wire `../images/...`. Header/welcome currently on `Mercersburg_Academy_Robotics_dark.svg`.

## STANDING QUEUE (carried forward)
`.DS_Store` cleanup (`git rm` + `.gitignore`) · `millis()`/`map()` taught-notes · L03_C05 Variable Speed learner mode · L04 C03/C04/C05 walkthroughs · C06 reorder to #1 · whole-template starters L08/L09/L10 · Maker batch (bulk DL · `?lesson=N` soft gate · C## labels) · L01 VS Code multi-root step.

**BENCH (need robot):** C06 · C11 · Q017 L09 six numbers · Q044 calibration-spin · Q046 gyro-bias · L02 §5 green-LED · Constrain RUN_MS.

**PARKED (do not reopen unprompted):** solution-disclosure · monetization/ebook · "Know Your Zumo" · day-by-day grid + syllabus · TDP template v3 (A5 Lab Log) · §9 difficulty grouping.

---

## PROCESS NOTES FROM S58 (worth keeping)

- **`git show --stat HEAD` on a `--depth 1` clone LIES about what a commit changed** — with no parent commit present, it lists the ENTIRE repo tree as "added." In S58 this produced a false "200 files were over-committed" alarm; the files were pre-existing. To see what a commit actually changed, don't trust shallow `git show --stat`. (Textbook case of the S58 Bible entry: a tool reports candidates, not verdicts.)
- **Verification caching, three layers:** (1) shallow clones lag ~1–2 min after a push (`sleep 40`, re-clone); (2) `raw.githubusercontent.com` caches ~5 min; (3) `api.github.com` rate-limits unauthenticated. `weymuth.github.io` is NOT in the bash allowlist, so the live Pages URL can't be fetched from bash — the reliable check is a fresh clone with an adequate wait, or ask DJ to eyeball the live page.
- **Favicon on a GitHub Pages project site** needs an explicit `<link rel="icon">` per page — browsers auto-request `/favicon.ico` at the DOMAIN root (`weymuth.github.io/favicon.ico`), never the repo subpath (`weymuth.github.io/zumo/favicon.ico`).
- **Write-order held all session:** every batch = fix → gate → diff-audit → structure/img check → regenerate LIVE.md LAST → present_files. Marker retrofits verified by per-lesson count + "every changed line is an anchor tag" + "each added line = removed line + inserted attrs."
- **Upload-location trap:** when DJ uploads a file for a subfolder, it can land in the repo root instead (happened with `tutor.html` → root). If a `tutor/` change seems not to take, check for a stray root copy.

---
*Written S58, July 20 2026. AI Tutor LIVE and complete. Commit `4c57e20`.*
