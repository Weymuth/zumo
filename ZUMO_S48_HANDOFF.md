# ZUMO — S48 HANDOFF (paste at top of next session)

## Session open ritual (clone-first — everything lives in the repo)
1. `git clone --depth 1 https://github.com/Weymuth/zumo.git` — do NOT wait for an upload.
2. Read `LIVE_ZUMO_TEXTBOOK.md` — verify date / status / currently-working-on.
3. `grep -o "Bible version: v[0-9.]*" ZUMO_SUPER_BIBLE.md` — expect **v8.31**.
4. `grep -o "Lesson version: v[0-9.]*" lessons/Lesson_NN.html` per lesson as needed.
5. Report what's live, then proceed. **LIVE.md wins** over memory and any pasted version.

## What's LIVE (S46 close — unchanged by S47; do NOT re-push)
- L01 v03.2.6 · L02 v02.2.3 · L03 **v03.4.4** · L04 v04.0.9 · L05 v04.1.8 · L06 v04.5.8 · L07 v04.3.8 · L08 v04.1.6 · L09 v05.0.8 · L10 v02.1.11
- L11 v02.2.1 · L12 v01.2.2 · L13 v02.2.1 · L14 v02.4.1 · L15 v02.2.2 · L16 v02.2.1
- Bible **v8.31** · Maker **v2.30** · Gate **v1.3** · Harness **v3.0**
- L11–L16 versions are PROVEN (S46), stamped via §5b — do NOT reconstruct from a floor.

## NEW THIS SESSION (S47) — two files now in repo root (commit f29ae48, verified)
- `ZUMO_LEARNMODE_L03.md` — L03 learner-mode teaching record: 21-row student-difficulty roll-up + per-challenge detail + 3 Coach's Tips + queued tasks.
- `ZUMO_L03_TEMPLATES.md` — six L03 Code Templates + six solutions. ⚠️ **STAGING, not Maker-gated** — source-of-intent, not final payloads.
- S47 was learner-mode only: walked C01–C06. **No lesson / Maker / Bible edits.**

## FIRST UP — DJ rulings pending (nothing built without them)
1. **Bible pointer entry** — establish the per-lesson learning-mode-file convention + point L03 at `ZUMO_LEARNMODE_L03.md`. Drafted on request; bumps Bible. (DJ deferred pending review of the two files.)
2. **"Code Template" term ruling** — DJ renamed "scaffold" → "Code Template." Make it canon project-wide (Bible + cards + Maker labels) or keep to walkthroughs only?

## QUEUED — the L03 starter fix (the big coordinated one)
- **C01/C05/C06 (and L08/L09/L10) starters ref a `finished` payload that doesn't exist for L03** → Maker emits a blank scaffold while the card claims "preloaded with the finished lesson program." Card text AND payloads out of sync. Fix = lift the staged Code Templates in as gate-verified whole-template payloads + correct the card text. Coordinated Maker + card edit; bumps L03 + Maker.

## QUEUED — L03 prose (used-but-never-taught, all found S47)
- Prototype explainer (why a call above its definition fails). [C01]
- Three Coach's Tips: stale build (Clean→Build) · compiler judges file-on-disk not editor · errors surface one at a time. [C04]
- Zero-index one-liner (arrays start at slot 0). [C05]
- Global-vs-local scope note. [C06]
- Watch whether the `const` vs `constrain()` amber callout lands; candidate for goal→logic→template card. [C03]

## QUEUED — prior (unchanged)
- C06 reorder to position #1 (coordinated: renumber cards, move `kind=` ids + reveal blocks + cross-refs).
- Whole-template starters for L08/L09/L10 + L03 C05/C06 (currently ref `finished`).
- Maker batch: starters-only bulk download · `?lesson=N` soft gate · C## folder labels · verify `?kind=` = starters not solutions.
- L01: VS Code multi-root workspace + "Pick a folder" step.

## BENCH ITEMS (need the robot — DJ)
- Q017 L09 green-tape six numbers · Q044 calibration-spin stopwatch · Q046 gyro-bias · L02 §5 green-LED check · Constrain RUN_MS duration.

## STILL PARKED (do not reopen unprompted)
- Challenge solution-disclosure (DJ rules after classroom use) · Monetization/ebook · "Know Your Zumo" reference page · AI Tutor rebuild (LAST — draws on the learner-mode walkthroughs) · Day-by-day grid + syllabus doc · TDP template v3 (A5 Lab Log).

## Repo hygiene (low priority)
- `README_S39_PUSH.md` — leftover, `git rm` when convenient.
- `ZUMO_L03_TEMPLATES.md` is staging — don't mistake it for a live payload source.

## AI-Tutor model note (from S47)
C05's structure worked ("learned stuff, but not frustrated"): isolate each new idea, let the wrong answer happen and correct in place, trace values by hand. Reuse for the tutor rebuild.
