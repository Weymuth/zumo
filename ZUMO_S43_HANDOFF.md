# ZUMO — S43 HANDOFF (paste at top of next session)

## Session open ritual
1. Clone the repo (everything lives at github.com/Weymuth/zumo — §12 canon).
2. `grep -oE "Bible version: v[0-9.]+" ZUMO_SUPER_BIBLE.md` — should read **v8.27**.
3. Verify LIVE.md date/status/currently-working-on against the tree; live tree wins on conflict.

## What LANDED in S42 (in the tree; commit/push if not yet pushed)
Two files changed: `ZUMO_SUPER_BIBLE.md` and `lessons/Lesson_03.html`. LIVE.md regenerated.
- **L03 §3.7 milliseconds callout** — green tip "1000 ms = 1 second" at the TOP of §3.7. **L03 is HELD, UNPRESENTED, still v03.2.0.** The single moderate bump to **v03.3.0** happens when the surgery below lands — NOT before, NOT separately. (Ghost rule: do not present a v03.2.1.)
- **Bible v8.27 — §6.12 rating scale → UP-TO-5 tiers** (a lesson uses as many as it needs, in order; no minimum per tier):
  EASY green `#4caf50` · MEDIUM blue `#2196f3` · TOUGH purple `#9c27b0` · HARD orange `#ff9800` · ADVANCED red `#f44336`.
  Replaces old EASY/MEDIUM/HARD/EXPERT/COMPETITION.
- **Bible v8.27 — §18.2 marker header** renamed "🔁 Spiraled skills:" → "🔁 Builds on:". "Spiral" stays the teacher-side method name. ⭐ stars unchanged.

## THIS SESSION = FINISH THE L03 CHALLENGE-REDESIGN SURGERY
Steps 1–2 (ms callout + Bible canon) done in S42. Do the rest, in order:

3. **L02 — add the "Builds on:" explainer callout.** Introduce the ⭐ + "Builds on:" mark ONCE, before its first use in L03 (L03 Battery Warning is the first marked card). Student-facing: when you see this mark, the challenge reuses a skill from an earlier lesson; the number tells you which. Placed at/before §9. Bumps L02.

4. **L03 surgery — reorder 6→8 cards** (ladder table below). Move each card's `kind=` link AND its reveal-solution block WITH the card (§15 gate: ordered Section-9 letters/kinds must still match). **Re-rate every pill to the 5-tier scale.** Add "Builds on:" markers: Battery ⭐L02 (OLED display), Constrain ⭐L02 (constants). **DELETE NOTHING.** Then bump L03 v03.2.0 → **v03.3.0** (moderate, single).

5. **Maker — starter payloads for the 2 new challenges** (`constrain`, `ramp`), §18.3 minimal skeletons (includes + motors object pre-placed + empty section headers + blank MY PLAN + "// write your code here"; do NOT re-explain setup()/loop()). Verify `?kind=` downloads are STARTERS not solutions. Two NEW kinds. Bumps Maker.

6. **THEN** learner-mode the cards in the new order (Socratic; coach, don't hand over the solution). Grep Claude's own code vs canon — lib pin `pololu/Zumo32U4@2.0.1`.

## L03 LADDER — 8 CARDS (locked S41; tiers now on the new 5-tier scale)
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

*(TOUGH tier unused in L03 — fine, tiers are optional. Bonus set untouched: creep_mode, backwards_trim, backwards_robot, braking_test, figure_eight, speedometer.)*

## CONSTRAIN CARD — LOCKED SPEC (unchanged from S42 handoff)
- Two motor-speed constants: `const int LEFT_SPEED = 150;` / `const int RIGHT_SPEED = 150;` — student EDITS these 150 → 200 → 250 across three uploads (Method A, NOT button-cycle — buttons not taught yet).
- Cap: `const int MAX_SPEED = 200;`
- `setSpeeds( constrain(LEFT_SPEED, -MAX_SPEED, MAX_SPEED), constrain(RIGHT_SPEED, -MAX_SPEED, MAX_SPEED) );`
- `delay(...)` then `setSpeeds(0, 0);` to STOP (so it doesn't drive off the table). Time is only a stop-timer.
- **The "aha":** 150 runs slower; 200 and 250 come out IDENTICAL (both clamp to 200). Try LEFT≠RIGHT to see the clamp act per-argument (robot curves — fine).
- Constrain is on SPEED, not time. TRIM stays OUT of the code — only named in the "Builds on:" line as another constant they've met.
- **Builds on:** constants from L02 (⭐ `spiral_star_02.svg`). EASY *because* it's the third left/right reinforcement in L03 (Spin signs → TRIM offset → Constrain clamp).
- **BENCH ITEM:** does a ~1 s run show the 150-vs-clamped-200 difference clearly? `RUN_MS` ships as a tunable with the guess in the comment (§11 blank convention).

## RAMP CARD — SPEC (refine at build)
Soft-start: ramp LEFT/RIGHT from 0 up to MAX_SPEED in a loop (not a jump). Spirals back to Constrain (ramp up to the clamped cap). MEDIUM, rung 4.

## QUEUED DEBT (NOT applied — own scoped session)
- **Book-wide pill sweep** — ~47 pills across L01–L10 to the new 5-tier scale:
  MEDIUM orange→blue ×27 · HARD red→orange ×15 · EXPERT→TOUGH purple ×5.
  New hex map (from §6.12 v8.27) is the authority. Bumps every touched lesson — its own session, do not fold into the L03 surgery.

## BENCH ITEMS (need the robot)
- Q017 L09 green-tape six numbers · Q044 calibration-spin stopwatch · Q046 gyro-bias · L02 §5 green-LED check · **Constrain RUN_MS duration.**

## STILL PARKED (do not reopen unprompted)
- Challenge solution-disclosure (DJ rules after classroom use)
- Monetization / ebook (after book is done)
- "Know Your Zumo" reference page (after book is done)
- AI Tutor rebuild (LAST; could draw on the learner-mode walkthroughs)

## Note
Memory near full. If S43 generates many new decisions, consolidate the older SVG-session log entries next.
