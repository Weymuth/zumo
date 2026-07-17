# ZUMO — S46 HANDOFF (paste at top of next session)

## Session open ritual (clone-first — everything lives in the repo)
1. `git clone --depth 1 https://github.com/Weymuth/zumo.git` — do NOT wait for an upload of a file that's in the repo.
2. Read `LIVE_ZUMO_TEXTBOOK.md` from the clone — verify date / status / currently-working-on.
3. `grep -o "Bible version: v[0-9.]*" ZUMO_SUPER_BIBLE.md` — confirm internal version (expect **v8.31**).
   - Lesson full version now lives in a hidden comment: `grep -o "Lesson version: v[0-9.]*" lessons/Lesson_NN.html` (new §5b — see below).
4. Report what's live, then proceed.
- **LIVE.md wins** over memory and over any pasted version number. Grep the actual file, never trust a claim.

## What's LIVE (verified S45 close by fresh clone, md5 matches staged — do NOT re-push)
- **Content:** L02 §3.2b data-types callout + int/bool prose · L03 C02 USB-battery callout · L03 C03 constrain two-jobs callout.
- **Pill sweep:** 39 pills L01/L02/L04–L10 recolored to §6.12 canon (MEDIUM #ff9800→#2196f3 ×25, HARD #f44336→#ff9800 ×14) + C06 re-rated →EASY. Labels unchanged, diff-audited 0 non-pill lines.
- **Versions live:** L01 v03.2.6 · L02 v02.2.3 · L03 v03.4.3 · L04 v04.0.8 · L05 v04.1.8 · L06 v04.5.7 · L07 v04.3.8 · L08 v04.1.6 · L09 v05.0.7 · L10 v02.1.10 · **Bible v8.31** · **Maker v2.30** · **Gate v1.3** · Harness v3.0.
- **NEW §5b — VERSION IN TWO IN-FILE HOMES (Bible v8.31):** the version now lives inside every lesson so it's never trapped in LIVE.md again. (1) VISIBLE banner (header+footer) = **major.minor** `vXX.XX` — churns only on a moderate+ bump, left alone on a minor/cosmetic one. (2) HIDDEN HTML comment, line 1 = **full** `<!-- Lesson version: vXX.XX.XX -->` — updated every bump, greppable. Filename stays stable `Lesson_NN.html`. Applied to L01–L10; **L11–L16 get it when each is next opened** (version reconciled from the floor below). GATE at close: hidden comment = banner major.minor = LIVE.md, all three agree.
- **Bible v8.30:** §18.4 TYPE-EXPLAINER CALLOUT canon (blue #e3f2fd callout, reused for each type's deep dive) + §18.3 CHAT-DISPLAY RULE (prepend the wrapper header `#include <Zumo32U4.h>` + MY PLAN when showing a Maker starter in chat, so the display matches the generated file).

## ⚠️ L11–L16 VERSION FLAG (git-proven FLOOR, not exact — reconcile on next open)
LIVE.md's status line had **corrupted** L11–L16 versions (v02.2.1 / v01.2.2 / v02.4.1 …). A **deep clone** (full 415-commit history) recovered the true versioned filenames from the rename commits:
- **L11 v02.0.3 · L12 v01.0.3 · L13 v02.0.3 · L14 v02.1.1 · L15 v02.0.2 · L16 v02.0.1**

⚠️ **These are a FLOOR, not the exact current version.** After those renames, all six were edited in **Session 35 / Session 36 / "39 Lessons"** commits (200–365 lines changed each) — WITHOUT a re-versioned filename, and LIVE.md never recorded the resulting numbers. So the true current version is **≥ the floor above**, by one or more bumps that are not recoverable from the repo.
- The published filenames are stable `Lesson_NN.html` and the in-file header carries the **major digit only** (Bible §5b), so the repo cannot supply the minor version for these six.
- **Action:** when any of L11–L16 is next opened for a depth pass, correct its version forward from the floor. Until then, LIVE.md shows the floor. Do NOT invent an exact number — the floor is repo-proven; anything beyond it is a guess.
- (For the record: the earlier S45 "S33 reconstruction" was WRONG on 5 of 6 — the deep clone was necessary.)

## FIRST UP — LEARNER MODE: `L03_C05` Variable Speed (Socratic)
- Coach with leading questions; do NOT reveal the hidden solution or hand over finished code unless DJ explicitly asks.
- Tag exchanges `L##_C##_W##`. Grep Claude's own code against canon (correct lib pin = `pololu/Zumo32U4@2.0.1`).
- **This is the hardest rung:** arrays + cycling index + modulo. DJ paused it in S45 (overwhelmed) — go slow.
- **Starter file is staged:** `L03_C05_starter_main.cpp` (the finished L03 program WITH the wrapper header, per §18.3). DJ modifies this.
- **The 3 edits:** (1) array + index in CONFIG (`int TEST_SPEEDS[] = {…}; int speedIndex = 0;`), (2) `TEST_SPEEDS[speedIndex]` swap in runMotorTest, (3) `speedIndex = (speedIndex + 1) % NUM_SPEEDS;` in the B-button handler.
- ⚠️ **Modulo `%` is never taught anywhere L01–L03** but C05's reveal uses it — teach it in the walkthrough (it's a REMAINDER, not divide; wraps 0→1→2→3→0). See queued task #1b.

## QUEUED (own sessions / coordinated edits)
1. **C06 reorder to position #1** — it's the simplest challenge (one-line edit), belongs first. Coordinated edit: renumber cards, move Maker `kind=` ids + reveal-solution blocks + cross-refs with each card. Bumps L03.
2. **4 EXPERT pills** (L04, L06, L09, L10) — EXPERT is retired, but TOUGH sits BELOW HARD in the new scale while EXPERT sat ABOVE, so a blind rename demotes them a tier. Needs a per-card ADVANCED-vs-TOUGH ruling. Left untouched in the S45 sweep on purpose.
3. **Whole-template starters for L08/L09/L10 + L03 C05/C06** — their challenge starters still ref `finished` (the completed program), not the whole-template canon (Bible §18.3). Reversal debt.
4. **L03 book tasks** (from learner-mode finds): (1) add "1000 ms = 1 second" — delay() unit used but never taught; (1b) modulo `%` explainer where C05 introduces the cycling index; (3) Coach's Tip: upload/power-on sequence (setup() fires once at power-on); (4) Coach's Tip: AI-autocomplete injects wrong code, verify against the lesson.
5. **Maker work session (batch):** starters-only full-course bulk download · progressive disclosure by `?lesson=N` (soft gate) · challenge folder labels get C## prefix (rename output-string only, keep `kind=` ids, flat) · verify `?kind=` downloads are starters not solutions.
6. **L01** — VS Code multi-root workspace + "Pick a folder / point PlatformIO at your project" step.

## BENCH ITEMS (need the robot — DJ)
- Q017 — L09 green-tape six numbers.
- Q044 — calibration-spin stopwatch.
- Q046 — gyro-bias.
- L02 §5 green-LED bench check (is the flicker really "USB activity," or the display interface?).
- Constrain RUN_MS duration (C03).

## STILL PARKED (do not reopen unprompted)
- Challenge solution-disclosure (DJ rules after classroom use as a student).
- Monetization / ebook (after book is done).
- "Know Your Zumo" reference page (after book is done).
- AI Tutor rebuild (LAST; could draw on the learner-mode walkthroughs).
- Day-by-day period grid + syllabus doc (working drafts in DJ's folder, not repo).
- TDP template v3 (add A5 Lab Log).

## Repo hygiene note (low priority)
Stale handoffs sit in the repo root: S35, S36, S37, S38, S40, S42, S43. Purge with `git rm` when convenient (DJ's call — a zip can't delete).

## Memory
At **26/30** after S45 consolidation (4 slots free). No urgent trim needed.
