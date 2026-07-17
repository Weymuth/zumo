# ZUMO — S47 HANDOFF (paste at top of next session)

## Session open ritual (clone-first — everything lives in the repo)
1. `git clone --depth 1 https://github.com/Weymuth/zumo.git` — do NOT wait for an upload of a file that's in the repo.
2. Read `LIVE_ZUMO_TEXTBOOK.md` from the clone — verify date / status / currently-working-on.
3. `grep -o "Bible version: v[0-9.]*" ZUMO_SUPER_BIBLE.md` — confirm internal version (expect **v8.31**).
4. Lesson versions now live in a hidden comment in EVERY lesson: `grep -o "Lesson version: v[0-9.]*" lessons/Lesson_NN.html`.
5. Report what's live, then proceed.
- **LIVE.md wins** over memory and over any pasted version number. Grep the actual file, never trust a claim.

## What's LIVE (verified S46 close by fresh clone — do NOT re-push)
All 16 lessons are now §5b-compliant (hidden comment + `NN.N` visible banner). EXPERT tier is retired book-wide.

**Versions live (all grep-verified against the repo, S46 close):**
- L01 v03.2.6 · L02 v02.2.3 · L03 **v03.4.4** · L04 **v04.0.9** · L05 v04.1.8 · L06 **v04.5.8** · L07 v04.3.8 · L08 v04.1.6 · L09 **v05.0.8** · L10 **v02.1.11**
- L11 **v02.2.1** · L12 **v01.2.2** · L13 **v02.2.1** · L14 **v02.4.1** · L15 **v02.2.2** · L16 **v02.2.1**
- Bible **v8.31** · Maker **v2.30** · Gate **v1.3** · Harness **v3.0**

## ⭐ L11–L16 VERSIONS — NOW PROVEN (the floor-guess is RETIRED — do NOT re-litigate)
Prior handoffs treated L11–L16 as a git-rename FLOOR (v02.0.3 etc.) because S35/S36/S38 edited them without re-versioning and the S45 LIVE.md had CORRUPTED them to that floor. **S46 recovered the true numbers.** Four independent sources agree, and DJ's uploaded lessons were byte-identical to the live repo:
1. S38 LIVE.md snapshot · 2. S39-push-zip LIVE.md · 3. S43 LIVE.md · 4. git history (NO commit touched L11–L16 after the "39 Lessons" / S38 commit).
The true current versions are the S38-recorded numbers: **L11 v02.2.1 · L12 v01.2.2 · L13 v02.2.1 · L14 v02.4.1 · L15 v02.2.1 (→ v02.2.2 after S46's EXPERT→ADVANCED edit) · L16 v02.2.1.**
These are now stamped INTO each file (§5b hidden comment), so the LIVE.md single-point-of-failure that lost them is closed. Do not reconstruct from a floor again — the number is in the file.

## SESSION 46 — WHAT LANDED (all PUSHED & VERIFIED, fresh clone)
1. **L03 book tasks (v03.4.3 → v03.4.4):** modulo `%` explainer (blue `#e3f2fd` callout) in the C05 Variable Speed card, before the reveal (teaches remainder + wrap-to-0 for the cycling index); two Coach's Tips at Step 13 — upload→power-on (setup() runs once; put the robot down before upload completes) and don't-trust-AI-autocomplete. Task (a) "1000 ms = 1 second" was ALREADY present (line 766) — no change.
2. **EXPERT tier retired book-wide:** all 5 instances → ADVANCED `#f44336` (red, the §6.12 top tier — no demotion). 4 card pills (L04 C5 · L06 C8 · L09 C6 · L10 C5) + 1 inline heading tag (L15 §9.7). Card-header gradients `#7d5283→#9b6a9e` left intact; L16 line-192 prose "Version 2 — If I Built the Next One" protected from the banner sweep. EXPERT now appears NOWHERE.
3. **§5b applied to ALL 16 lessons:** L11–L16 previously had bare `Version N` banners and NO hidden comment — now fixed. Every lesson: hidden `<!-- Lesson version: vXX.XX.XX -->` first line + `Version NN.N` visible banner.
4. **LIVE.md regenerated** — correct roster, S46 block, floor caveat removed.

## FIRST UP — pick one (all queued, none blocking)
- **LEARNER MODE: `L03_C05` Variable Speed** (Socratic) — the hardest rung: arrays + cycling index + modulo. Starter staged in repo: `L03_C05_starter_main.cpp`. Modulo explainer is NOW in the card to support it. The 3 edits: (1) array+index in CONFIG, (2) `TEST_SPEEDS[speedIndex]` swap in runMotorTest, (3) `speedIndex=(speedIndex+1)%NUM_SPEEDS` in the B handler. Coach with leading questions; don't hand over the solution unless DJ asks. Grep Claude's own code against canon (lib pin = `pololu/Zumo32U4@2.0.1`).

## QUEUED (own sessions / coordinated edits)
1. **C06 reorder to position #1** — it's the simplest challenge (one-line edit), belongs first. Coordinated L03 edit: renumber cards, move Maker `kind=` ids + reveal-solution blocks + cross-refs with each card. Bumps L03.
2. **Whole-template starters for L08/L09/L10 + L03 C05/C06** — their challenge starters still ref `finished`, not the whole-template canon (Bible §18.3). Reversal debt.
3. **Maker work session (batch):** starters-only full-course bulk download · progressive disclosure by `?lesson=N` (soft gate) · challenge folder labels get C## prefix (rename output-string only, keep `kind=` ids, flat) · verify `?kind=` downloads are starters not solutions.
4. **L01** — VS Code multi-root workspace + "Pick a folder / point PlatformIO at your project" step.

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

## Repo hygiene note (low priority — DJ's hands, a push can't delete)
- `README_S39_PUSH.md` — leftover S39 push note, safe to `git rm` when convenient.
- The old S35–S43 handoffs were already purged (verified S46). Only this handoff + the S39 push note remain.

## §5b — the durable win from S46 (remember this)
Stable published filename (`Lesson_NN.html`) + a major-only banner meant the exact MINOR version lived ONLY in LIVE.md. One LIVE.md corruption (S45) lost L11–L16's minor and forced a multi-source reconstruction (S46). §5b's hidden comment ends that: the full version is now durable INSIDE every file, greppable, invisible to students. Never revert to major-only banners. GATE at close: hidden comment's major.minor == visible banner == LIVE.md roster, all three agree.
