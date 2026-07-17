# ZUMO — S49 HANDOFF (paste at top of next session)

## Session open ritual (clone-first — everything lives in the repo)
1. `git clone --depth 1 https://github.com/Weymuth/zumo.git` — do NOT wait for an upload.
2. Read `LIVE_ZUMO_TEXTBOOK.md` — verify date / status / currently-working-on.
3. `grep -oE "Bible version: v[0-9.]+" ZUMO_SUPER_BIBLE.md` — expect **v8.32**.
4. `grep -o "Lesson version: v[0-9.]*" lessons/Lesson_NN.html` per lesson as needed.
5. Report what's live, then proceed. **LIVE.md wins** over memory and any pasted version.

## ⚠️ FIRST THING — did the S48 batch get pushed?
S48 staged three files but DJ hadn't pushed at close. At open, clone and check:
- `grep -oE "Bible version: v[0-9.]+"` → v8.32? (was v8.31)
- `grep -oE "Project Maker v[0-9.]+" newproject.html` → v2.31? (was v2.30)
- LIVE.md header says Session 48?

If still v8.31 / v2.30 / S46 → **the S48 push didn't land.** The three files are in DJ's Downloads (Bible v8.32, newproject.html v2.31, LIVE.md S48). Re-present from a rebuilt clone if needed. Do NOT redo the edits blind — grep first.

## What's LIVE (S48 close — STAGED, may or may not be pushed)
- All 16 lessons UNCHANGED: L01 v03.2.6 · L02 v02.2.3 · L03 **v03.4.4** · L04 v04.0.9 · L05 v04.1.8 · L06 v04.5.8 · L07 v04.3.8 · L08 v04.1.6 · L09 v05.0.8 · L10 v02.1.11 · L11 v02.2.1 · L12 v01.2.2 · L13 v02.2.1 · L14 v02.4.1 · L15 v02.2.2 · L16 v02.2.1
- Bible **v8.32** · Maker **v2.31** · Gate **v1.3** · Harness **v3.0**

## What S48 did (Bible-only + Maker label, NO lessons touched)
- **Bible §19 NEW** — per-lesson learning-mode file convention (`ZUMO_LEARNMODE_LNN.md`, repo root; teacher-side record + AI-Tutor source, NOT a payload source). L03's is live.
- **§18.3 term = "challenge template"** project-wide. "Starter" = OK generic synonym; "scaffold" retired for THIS sense only (§14 TDP + §5 theory senses untouched).
- **Maker v2.31** — two L03 dropdown labels `(starter)`→`(challenge template)` (Clamp the Speed, Ramp Up to Speed). Label text only; no `kind=`/payload/byte change.
- Lessons needed NO edit (their only starter/scaffold hits were the other senses).

## 🔴 FRONT TASK S49 — the L03 challenge-template STARTER FIX (the big coordinated one)
- **C01/C05/C06 (and L08/L09/L10) starters ref a `finished` payload that doesn't exist for L03** → Maker emits a blank scaffold while the card claims "preloaded with the finished lesson program." Card text AND payloads out of sync.
- **Fix:** lift the staged `ZUMO_L03_TEMPLATES.md` in as gate-verified WHOLE-TEMPLATE payloads (strip wrapper, start at `// ===== HARDWARE OBJECTS =====`, gate-check) + correct the card text + name "challenge template" in the L03 cards (they carry no `(starter)` suffix yet, so the term isn't visible there — add it).
- Coordinated Maker + card edit; **bumps L03 + Maker.**
- ⚠️ `ZUMO_L03_TEMPLATES.md` is STAGING, not a live payload source — it needs payload-body treatment first.

## QUEUED — L03 prose (used-but-never-taught, all found S47)
- Prototype explainer (why a call above its definition fails). [C01]
- Three Coach's Tips: stale build (Clean→Build) · compiler judges file-on-disk not editor tab · errors surface one at a time. [C04]
- Zero-index one-liner (arrays start at slot 0). [C05]
- Global-vs-local scope note. [C06]

## QUEUED — prior (unchanged)
- C06 reorder to position #1 (coordinated: renumber cards, move `kind=` ids + reveal blocks + cross-refs).
- Whole-template starters for L08/L09/L10 (currently ref `finished`).
- Maker batch: starters-only bulk download · `?lesson=N` soft gate · C## folder labels · verify `?kind=` = starters not solutions.
- L01: VS Code multi-root workspace + "Pick a folder" step.

## LEARNER MODE (DJ writing challenge code himself, Socratic)
- Coach with leading questions; do NOT reveal the hidden solution unless DJ explicitly asks.
- Tag exchanges `L##_C##_W##`. Grep Claude's own code against canon (correct pin = `pololu/Zumo32U4@2.0.1`).
- **NEXT UP: `L03_C05` Variable Speed** (array + index + modulo — the hardest rung; modulo explainer already in the card). DJ has done C01–C04, C06.

## BENCH ITEMS (need the robot — DJ)
- Q017 L09 green-tape six numbers · Q044 calibration-spin stopwatch · Q046 gyro-bias · L02 §5 green-LED check · Constrain RUN_MS duration.

## STILL PARKED (do not reopen unprompted)
- Challenge solution-disclosure (DJ rules after classroom use) · Monetization/ebook · "Know Your Zumo" reference page · AI Tutor rebuild (LAST — draws on learner-mode walkthroughs) · Day-by-day grid + syllabus doc · TDP template v3 (A5 Lab Log) · §9 difficulty grouping · L06 goal→logic→template card pattern.

## Repo hygiene (low priority)
- `README_S39_PUSH.md` — leftover, `git rm` when convenient.
- `ZUMO_L03_TEMPLATES.md` is staging — don't mistake it for a live payload source.

## Note
Memory at 21/30 after S48 consolidation (removed S19/S20/S22/S23/S27/S32/S33 logs — rules now durable in Bible). Room to spare.
