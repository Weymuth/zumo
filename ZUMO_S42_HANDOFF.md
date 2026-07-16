# ZUMO — S42 HANDOFF (paste at top of next session)

## Session open ritual
1. Clone the repo (everything lives at github.com/Weymuth/zumo — §12 canon).
2. `grep -oE "Bible version: v[0-9.]+" ZUMO_SUPER_BIBLE.md` — should read **v8.26**.
3. Verify LIVE.md date/status/currently-working-on against the tree; live tree wins on conflict.

## What's LIVE (verified by clone this session — do NOT re-push)
- Bible **v8.26** (§14.1 TDP-is-notebook + §18 challenge-design canon) — commit landed S41.
- All 16 **spiral stars** in `images/` (`spiral_star_01..16.svg`, commit `b3467a6`).
- S38+S39+S40 content, 5 image deletions, `ZUMO_TDP_Template.md` (root), `favicon.ico` (root).

## THIS SESSION = THE L03 CHALLENGE-REDESIGN GATED BUILD
Everything was DESIGNED in S41; nothing was injected into any lesson. This is the surgery. **Dependency order matters** — do them top to bottom:

1. **L03 body — teach "1000 ms = 1 second."** The `delay()` unit is used but never taught in L03. Prerequisite for the Constrain/Ramp cards (they use `delay()` to stop the robot). Likely home: near §3.8 / first `delay()` use. Bumps L03.

2. **Bible canon edits (bump internal version, note in change block):**
   - **§6.12 / rating canon** — rating scale is now **5 tiers: EASY · MEDIUM · TOUGH · HARD · ADVANCED** (was EASY/MEDIUM/HARD). No minimum cards per tier; order carries difficulty, labels assist.
   - **§18.2** — rename the student-facing marker header **"🔁 Spiraled skills:" → "🔁 Builds on:"**. Keep "spiral" as the teacher-side METHOD name in the prose. The ⭐ numbered-star convention is unchanged.

3. **L02 — add the "Builds on:" explainer callout.** Introduce the ⭐ + "Builds on:" mark ONCE, before its first use in L03 (L03 Battery Warning is the first marked card). Student-facing: "when you see this mark, this challenge reuses a skill from an earlier lesson; the number tells you which one." Placed at/before §9. Bumps L02.

4. **L03 surgery — reorder 6→8 cards** (see table below). Move each card's `kind=` link AND its reveal-solution block WITH the card (§15 gate: the ordered Section-9 letters/kinds must still match). Re-rate every pill to the 5-tier scale. Add "Builds on:" markers to Battery (⭐ L02 display) and Constrain (⭐ L02 constants). **DELETE NOTHING.** Bumps L03 (moderate).

5. **Maker — starter payloads for the 2 new challenges** (`constrain`, `ramp`), §18.3 minimal skeletons (includes + motors object pre-placed + empty section headers + blank MY PLAN + "// write your code here"; do NOT re-explain setup()/loop()). Verify `?kind=` downloads are STARTERS not solutions. Two NEW kinds needed.

6. **THEN** learner-mode the cards in the new order (Socratic; coach, don't hand over the solution). Grep Claude's own code vs canon — correct lib pin `pololu/Zumo32U4@2.0.1`.

## L03 LADDER — 8 CARDS (locked S41)
| # | Card | Tier | New concept | Builds on | kind |
|---|------|------|-------------|-----------|------|
| 1 | Spin Test | EASY | direction / signs | — | spin_test |
| 2 | Battery Warning | EASY | `if` comparison | ⭐ L02 OLED display | battery_warning |
| 3 | **Constrain** *(NEW)* | EASY | clamp a value | ⭐ L02 constants | **constrain** |
| 4 | **Ramp** *(NEW)* | MEDIUM | change a value over time | Constrain (rung 3) | **ramp** |
| 5 | Variable Speed | MEDIUM | arrays + cycling index | — | variable_speed |
| 6 | Save TRIM | MEDIUM | persist a tuned value | — | save_trim |
| 7 | Drive a Square | HARD | author a function + sequence | — | drive_a_square |
| 8 | Auto-TRIM | ADVANCED | open-ended research (no code) | — | auto_trim |

*(TOUGH tier unused in L03 — fine. Bonus set untouched: creep_mode, backwards_trim, backwards_robot, braking_test, figure_eight, speedometer.)*

## CONSTRAIN CARD — LOCKED SPEC
- Two motor-speed constants: `const int LEFT_SPEED = 150;` / `const int RIGHT_SPEED = 150;` — student EDITS these to 150 → 200 → 250 across three uploads (Method A, NOT button-cycle — buttons not taught yet).
- The cap: `const int MAX_SPEED = 200;`
- `setSpeeds( constrain(LEFT_SPEED, -MAX_SPEED, MAX_SPEED), constrain(RIGHT_SPEED, -MAX_SPEED, MAX_SPEED) );`
- Run `delay(...)` then `setSpeeds(0, 0);` to STOP (so it doesn't drive off the table). Time is only a stop-timer — unrelated to the constrain.
- **The demo / "aha":** 150 runs slower; 200 and 250 come out IDENTICAL because both clamp to 200. Also try LEFT≠RIGHT to see the clamp act per-argument (robot curves — that's fine).
- **Constrain is on SPEED, not time.** TRIM stays OUT of the code (that's Save TRIM's job at rung 6) — only referenced in the "Builds on:" line as another constant they've met.
- **Builds on:** constants from L02 (⭐ `spiral_star_02.svg`). EASY *because* it's the third left/right reinforcement in L03 (Spin signs → TRIM offset → Constrain clamp).
- **BENCH ITEM:** does a ~1 s run show the 150-vs-clamped-200 difference clearly? `RUN_MS` ships as a tunable with the guess in the comment (§11 blank convention).

## RAMP CARD — SPEC (refine at build)
Soft-start: ramp LEFT/RIGHT speed gradually from 0 up to MAX_SPEED in a loop (not a jump to full speed). Spirals back to Constrain (ramp up to the clamped cap). MEDIUM, rung 4.

## BENCH ITEMS (need the robot)
- Q017 L09 green-tape six numbers · Q044 calibration-spin stopwatch · Q046 gyro-bias · L02 §5 green-LED check · **Constrain RUN_MS duration.**

## STILL PARKED (do not reopen unprompted)
- Challenge solution-disclosure (DJ rules after classroom use)
- Monetization / ebook (after book is done)
- "Know Your Zumo" reference page (after book is done)
- AI Tutor rebuild (LAST; could draw on the learner-mode walkthroughs)

## Note
Memory near full. If S42 generates many new decisions, consolidate the older SVG-session log entries next.
