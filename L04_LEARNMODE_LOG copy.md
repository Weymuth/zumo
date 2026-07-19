# ZUMO — L04 Learner-Mode Log (Session 50)
### Socratic walkthrough of L04 challenges · friction points + refinement ideas

> Running record. Each entry: where DJ (proxy for a student) hit a snag, or a lesson gap / improvement idea surfaced during the walkthrough. Feeds classroom-issue predictions + book-task queue (same class as the S47 L03 finds). Tags: L04_C##_W##.

## 🔑 HEADLINE FINDING (S50, confirmed across L03 + L04 C01)
**The logic is not the wall — the Zumo/OLED API is.** DJ (and by extension students) reason through if/else, states, and both-branch cleanup correctly on the first try. Every stall is API RECALL: which function (`ledYellow` vs `display`), `gotoXY`, `F()`, array-slot indices, brace/paren placement. DJ, in his words: "the logic part works for me, it's the code intricacies that mess me up."
**Design implication:** put a cheap API crutch AT THE POINT OF USE in each challenge card (the exact function signatures that challenge needs), not a "see Quick Reference" pointer. This is the single highest-value refinement from the walkthroughs. Candidate: a small "🔧 Functions you'll need" line per challenge listing just the signatures (`ledYellow(1/0)`, `display.gotoXY(col,row)`, `display.print(F("..."))`, `lineSensorValues[i]`).

## Student-difficulty roll-up
| # | Challenge | Concept(s) | Predicted student snag | Severity |
|---|-----------|-----------|------------------------|----------|
| C01 | Line Light | if/else · array slot · LED vs OLED · erase-with-spaces · gotoXY both branches | API recall (ledYellow/gotoXY/F/spaces); else-cleanup vs one-way state; 3v5 center-slot | MEDIUM |
| C02 | The Line Counter | | | |
| C03 | The Position Pointer | | | |
| C04 | Edge Guard | | | |
| C05 | The Centering Game | | | |

## Coach's-Tip candidates (used-but-never-taught / gotchas)
- **C01 opens the FULL finished three-sensor program, not a blank template** — DJ's first reaction: "looks like a full version not the discovery template." This is BY DESIGN (all 5 L04 challenges payloadRef=`act_one`, the working program you modify), but it reads as "did I grab the wrong file / is this the answer?" Candidate Coach's Tip or card-text tweak: say plainly "this opens the WORKING program — you'll ADD to it, the challenge is not done for you." Same confusion class as the L03 finished-preload cards.

## Lesson refinement ideas
- (pending)

## Per-challenge detail
### L04_C01 — Line Light
- **DJ jumped straight to the challenge without doing the discovery/calibration first** — asked "should I do the discovery stuff before the challenge?" This is a real ordering trap: readCalibrated() returns meaningless values if calibration never ran, so the challenge threshold silently fails and the student blames their code. Candidate: a one-line gate at the top of every challenge card — "Do the discoveries + calibrate first; readCalibrated() needs it." (Ties to the flipped-classroom flow — reading quiz should enforce the discovery order.)
- **DJ asked why C01 needs an `else` when L02 battery-warning did not** — excellent conceptual question, will recur. The distinction: L02 low-battery is a ONE-WAY state (turns on, never needs to turn off — a dead battery stays dead). C01 line-detect is a REPEATING on/off state (you cross on AND off the line every loop), so the "no" branch must ERASE the message or "LINE!" sticks forever. Candidate Coach's Tip / prose: "If a state can turn back OFF, you need the else to clean up — one-shot messages (L02) don't; repeating ones (this) do." Strong spiral-back-to-L02 moment.
- **Slot confusion:** DJ said center = slot 2 (it is slot 1; 0/1/2 → 1 is the middle). Predictable off-by-one for students reading "three sensors." Card hint already says lineSensorValues[1]=center, but the numbering (why middle=1 not 2) isn't spelled out. Candidate: tiny "0,1,2 → 1 is the middle one" note.
- **return in loop():** DJ used `return` to end the on-line branch. Works, but with an if/else `return` is unnecessary and can mask the missing else. Watch whether this becomes a habit — candidate Coach's Tip on if/else vs early-return.
- **3-sensor vs 5-sensor "which slot is center" ambiguity (IMPORTANT — DJ hit this cleanly)** — DJ assumed 5-sensor (center=slot 2), but C01 is the 3-sensor track (center=slot 1). He reasoned CORRECTLY for 5-sensor; the card just doesn't make the array size salient at the point of use. L04 is dual-track, so "center sensor" is genuinely ambiguous without stating the array. Candidate fix: C01 card should say "(3-sensor array → center = slot 1; if you are on the 5-sensor build, center = slot 2)" right at the hint. High-value, students WILL trip on this given the dual track.
- **OLED vs LED confusion (log this — DJ said "I was using OLED")** — student conflates the OLED SCREEN (display.print) with the yellow LED (ledYellow). C01 needs BOTH and the card doesn't flag that they are different hardware. Candidate: one line — "the OLED is the screen; the yellow LED is a separate light — this challenge uses both."
- **erase-with-spaces not obvious:** DJ tried `clearDisplay` then `"_______"` (underscores). The "print 5 spaces at the same gotoXY" idiom is non-obvious; WHY (not wiping the whole screen / not visible chars) needs stating. Card hint says "clear by printing spaces" but not "same spot, same length, blanks not underscores."
- **gotoXY needed in BOTH branches — never surfaced in DJ's drafts.** He never wrote gotoXY at all; the cursor-positioning step is invisible to a student thinking only "print LINE / erase LINE." High-value: the card hint "display work goes in both branches" should explicitly include "and you must gotoXY(0,1) in both, or it prints in the wrong place."
- **F() macro** never appeared in DJ's drafts — students will omit it. Already taught earlier but not reinforced at point of use.
- DJ asked for the answer at this rung (LED name + space count). Stopping point: structure was correct; the gaps were all HARDWARE-API recall (ledYellow, gotoXY, F, spaces), not logic. **Pattern: DJ's LOGIC is solid; the wall is Zumo/OLED API syntax** — consistent with the L03 finding. Reinforces: challenges need an API-recall crutch at point of use, not just "see Quick Reference."

**C01 verdict:** logic mastered (if/else, both-branches, on/off state vs one-way state). All friction was API recall. Severity for students: MEDIUM — the else-cleanup insight is the real teach; the rest is syntax lookup.

---
## Session close (S50)
- **Walked:** C01 Line Light only (logic mastered; all friction was API recall).
- **Stopped because:** DJ is going back to do the L04 discoveries + calibration first (correct order — readCalibrated() needs calibration to run before any challenge works).
- **C02–C05 not yet walked.**
- **Next learner-mode session:** either resume L04 at C02 (Line Counter) after discoveries, or the still-pending L03_C05 Variable Speed.
- **Nothing in the book was edited this session** — this log is a teaching-record / book-task-candidate file only, not yet Bible-canon or a lesson change.

---
## Session 52 (Jul 19, 2026) — L04 BUILD COMPLETED end-to-end (Discoveries → Act One → Act Two → §7 → restore)

DJ had robot + white surface + matte black electrical tape (the S51 blocker cleared). Whole L04 learner-mode build done and hardware-verified. **Book NOT edited; L04 stays v04.0.12.** Full session record + data tables in project doc `ZUMO_S52_LEARNMODE_L04_LOG.md`.

### Recorded data (DJ's robot)
Raw — white: S1 52 / S3 32 / S5 52 · tape: S1 1112 / S3 680 / S5 1280. Calibrated: white ~0 (agree); tape ~1000 outers, center caps ~800 (weakest eye; clears the 500 threshold fine).
5-sensor gap map: hides in outer gaps **1↔2 & 4↔5**; NOT in inner 2↔3 & 3↔4.

### Friction points (S52)
- **Missed multi-part edit, green build hid it (headline S52).** Step 5: prototype + both functions added, but `loop()` not switched to `readCalibrated`/`showReadings()`. Build went GREEN (same signature; an unused function is legal C++), so raw values + a blank OLED were the only symptom. **A green build confirms syntax, not that every edit landed — verify the file before upload on multi-part edits.**
- **Calibration sweep technique = biggest time sink.** DJ didn't know to slide DURING the countdown; a still/narrow sweep collapsed calibrated values to ~0 (left/right 0, center maxed at 7). Wide flat slide → full 1000. Timer is fine (5 s); the miss was the cue.
- `println`↔`print` recurred; prototype typos `intPosition` / `unit8_t` (pure-syntax walls, handed fast per profile).
- **POS** — DJ unsure what the position number is/does (math is in §3.5 but the purpose didn't land build-first); caught that POS is in the ROBOT's frame (turning the robot moves "4000" to the other side).
- **Test B misconception** — guessed "fewer sensors = smoother" (backwards; more eyes = finer resolution = smoother).
- **Forgot to reseat the sensor array** ("code isn't working" = array physically unplugged) — validates the reseat-caution callout below.

### 📋 BOOK-TASK CANDIDATES (S52 — for a book-work session; NOT applied here)
1. **Sweep clarity (Steps 5–6, §3.4):** OLED `"Sweep!"` → imperative `"SLIDE ←→"`; add a "Start Slide" cue; prose "slide DURING the countdown"; new SVG of the hand-slide. **Terminology LOCKED (DJ ruling S52): sweep = concept, slide = hand, spin = motor.** Keep `CAL_TIME_MS=5000` (lengthening rejected — data: a proper 5-sec slide hits 1000).
2. **Step 8 safety callouts (promote to prominent warnings):** POWER OFF **and UNPLUG**; gentle jumper seating (no twist/force, bent pins); **reseat sensor array carefully** (double-confirmed — DJ forgot it).
3. **POS at point of use (Step 8):** explain what POS is + its steering PURPOSE (not just the §3.5 back-ref); state it's in the robot's frame (0=robot-left, 4000=robot-right) and address "if I turn it around."
4. **⭐ BIG FINDING — §7 Test A / §3.6 "nowhere to hide" OVERCLAIMS.** Five sensors close the inner gaps (2↔3, 3↔4) but the wider OUTER gaps (1↔2, 4↔5) still hide a narrow line (verified, symmetric). Cause: sensors 2/4 sit nearer center than outers, so the outer gaps are widest. Reframe Test A as "map all 4 gaps, find the outer two still hide" — resolution is finite AND non-uniform. Bonus hook: pos=0 (left gap) / 4000 (right gap) IDs which gap swallowed the line. Add caveat: outer blind spots matter less in real following (line kept near center).
5. **§7 Test B — pre-empt the misconception:** "you might guess fewer sensors track more smoothly — measure it, you'll find the opposite."

### Next learner-mode session
L04 challenges **C02–C05** (C01 done S50), OR a book-work pass to apply candidates 1–5, OR L03_C05 Variable Speed.

