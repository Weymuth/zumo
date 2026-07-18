# ZUMO — S50 HANDOFF (paste at top of next session)

## Session open ritual (clone-first — everything lives in the repo)
1. `git clone --depth 1 https://github.com/Weymuth/zumo.git` — do NOT wait for an upload.
2. Read `LIVE_ZUMO_TEXTBOOK.md` — verify date / status / currently-working-on.
3. `grep -oE "Bible version: v[0-9.]+" ZUMO_SUPER_BIBLE.md` — expect **v8.33**.
4. `grep -o "Lesson version: v[0-9.]*" lessons/Lesson_NN.html` per lesson as needed.
5. Report what's live, then proceed. **LIVE.md wins** over memory and any pasted version.

## ⚠️ FIRST THING — confirm S49 is fully live
Everything from S49 was pushed and verified by fresh clone. At open, confirm:
- Latest commit ≈ `a8e2130 "Pre S50"` (or later).
- L03 **v03.4.7** · L04 **v04.0.12** · Bible **v8.33** · Maker **v2.32** · LIVE.md Session 49.
- `L04_LEARNMODE_LOG.md` present in repo root.
If any of these are missing/lower, something regressed — grep first, don't redo blind.

## What's LIVE (S49 close — ALL PUSHED & VERIFIED)
- All 16 lessons: L01 v03.2.7 · L02 v02.2.4 · L03 **v03.4.7** · L04 **v04.0.12** · L05 v04.1.9 · L06 v04.5.9 · L07 v04.3.9 · L08 v04.1.7 · L09 v05.0.9 · L10 v02.1.12 · L11 v02.2.2 · L12 v01.2.3 · L13 v02.2.2 · L14 v02.4.2 · L15 v02.2.3 · L16 v02.2.2
- Bible **v8.33** · Maker **v2.32** · Gate v1.3 · Harness v3.0

## What S49 did (three commits)
**bb10c28 — L03 card fix + payloads:**
- L03 dark-block anomaly fixed: L03 was the ONLY lesson of 16 wrapping challenge **Goal prose** in a dark `#1e1e1e` block (styling prose like code). 8 goal-blocks unwrapped to the white-body norm — root cause of invisible code-chips + a washed-out amber callout. Reveal `<pre>` blocks stay dark (correct).
- Maker C07/C08 payloadRef `null` → `finished` (DJ ruling: C01–C06 stay finished-preload; an L03 `finished` payload DOES exist — the old "no finished payload" claim was wrong). Maker v2.32.
- `ZUMO_L03_TEMPLATES.md` completed: 6 → all 8 challenges, term "challenge template", reference record (NOT a payload source).

**05247d4 — book-wide image fix + L04 photos:**
- **raw→Pages image URLs, ALL 16 LESSONS (114 refs).** The "images not showing" problem was `raw.githubusercontent.com` **rate-limiting** (429 on random images per load), NOT missing files. Converted every `<img src>` to `https://weymuth.github.io/zumo/images/` (same-origin, unthrottled, Canvas-compatible). `ZUMO_Template.zip` links correctly LEFT on raw (rule scoped to `/images/`).
- **L04 jumper photos:** IMAGE 4.2 (factory jumper close-up) + new IMAGE 4.4 (5-sensor jumper position) wired in; EXIF/GPS stripped. IMAGE 4.1 = temporary L11-diagram stand-in until the real underside photo is shot.

**a8e2130 — S49 close batch:**
- L03 v03.4.7 prose: prototype explainer [C01] · 3 build Coach's Tips [C04: stale-build→Clean/Build · compiler judges file-on-disk not the editor tab · errors surface one at a time] · zero-index clause [C05 modulo callout] · global-vs-local scope note [C06].
- L04 v04.0.12: **API crutch** — each of the 5 challenge cards gains a "🔧 Functions you'll need" line with exact signatures at point-of-use. Pilots the S49 walkthrough headline (logic solid, API is the wall).
- Bible v8.33: §10 image-URL canon (Pages not raw) + strip-EXIF rule + temp-GRAPHIC-stand-in rule; §11 checklist "prose is not code — never dark-block Goal prose."
- LIVE.md regenerated; `L04_LEARNMODE_LOG.md` added.

## 🔴 IMAGE QUEUE — DJ still to shoot (has the robot)
- **L04 IMAGE 4.1** — underside of the Zumo, blade toward camera, five windows numbered 1–5 (a temp L11-diagram stand-in is live now; swap to real photo when shot).
- **L04 IMAGE 4.3** — finished test surface: white poster board, straight black tape line, wide white margins.
- The rest of the 22-photo `IMAGE_SHOT_LIST.md`.
- When shooting: strip EXIF/GPS before push (Bible §10). Name per shot list: `L04_IMAGE_4-0N_short.jpg`.

## LEARNER MODE (DJ writing challenge code himself, Socratic)
- Coach with leading questions; do NOT reveal the solution unless DJ explicitly asks. Tag `L##_C##_W##`.
- **DJ's pattern (confirmed L03 + L04 C01): LOGIC is solid; the wall is Zumo/OLED API recall.** Spend less time coaching logic, hand over API signatures faster when he hits a "what's it called" wall. (This is what the L04 API-crutch cards now do in the book.)
- **L04 C01 Line Light = DONE** (walked S49; logged in `L04_LEARNMODE_LOG.md`). Key concept taught: on/off state needs an `else` to clean up (unlike L02's one-way battery message).
- **NEXT: L04 C02–C05** — BUT DJ is doing the L04 discoveries + calibration FIRST (readCalibrated() needs calibration or the challenges silently fail). Resume C02 (Line Counter) after that.
- Still pending from before L04: **L03_C05 Variable Speed** (array + index + modulo; DJ has done L03 C01–C04, C06).
- Grep Claude's own code against canon (correct lib pin = `pololu/Zumo32U4@2.0.1`).

## QUEUED — book tasks
- **API-crutch rollout:** if the L04 "Functions you'll need" cards test well in class, roll the pattern out to the other lessons' challenge cards. (New this session — candidate book-wide standardization.)
- L03: C06 reorder to position #1 (coordinated: renumber cards, move `kind=` ids + reveal blocks + cross-refs).
- Whole-template starters for L08/L09/L10 (still ref `finished`).
- Maker batch: starters-only bulk download · `?lesson=N` soft gate · C## folder labels · verify `?kind=` = starters not solutions.
- L01: VS Code multi-root workspace + "Pick a folder" step.

## BENCH ITEMS (need the robot — DJ)
- Q017 L09 green-tape six numbers · Q044 calibration-spin stopwatch · Q046 gyro-bias · L02 §5 green-LED check · Constrain RUN_MS duration.

## STILL PARKED (do not reopen unprompted)
- Challenge solution-disclosure (DJ rules after classroom use) · Monetization/ebook · "Know Your Zumo" reference page · AI Tutor rebuild (LAST — draws on learner-mode walkthroughs incl. the new L04 log) · Day-by-day grid + syllabus doc · TDP template v3 (A5 Lab Log) · §9 difficulty grouping · L06 goal→logic→template card pattern.

## Repo hygiene (low priority)
- `README_S39_PUSH.md` — leftover, `git rm` when convenient.
- `ZUMO_L03_TEMPLATES.md` is a reference record (all 8 challenges), NOT a live payload source.
- `L04_LEARNMODE_LOG.md` is a teacher-side record per Bible §19 (companion to `ZUMO_LEARNMODE_L03.md`).

## Note
Session count is real: this was **Session 49** (opened from the S49 handoff). Next is S50.
