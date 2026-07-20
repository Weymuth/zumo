# ZUMO — L04 Learner-Mode Log (Session 50)
### Socratic walkthrough of L04 challenges · friction points + refinement ideas

> Running record. Each entry: where DJ (proxy for a student) hit a snag, or a lesson gap / improvement idea surfaced during the walkthrough. Feeds classroom-issue predictions + book-task queue (same class as the S47 L03 finds). Tags: L04_C##_W##.
>
> **Annotated S57 (July 20, 2026).** Findings are preserved as originally observed; resolutions are appended and dated rather than written over, so the record still shows what a learner actually hit. One factual error was corrected in place and marked (the for-loop tutorial is L05 §5.15, not §5.13).

## 🔑 HEADLINE FINDING (S50, confirmed across L03 + L04 C01)
**The logic is not the wall — the Zumo/OLED API is.** DJ (and by extension students) reason through if/else, states, and both-branch cleanup correctly on the first try. Every stall is API RECALL: which function (`ledYellow` vs `display`), `gotoXY`, `F()`, array-slot indices, brace/paren placement. DJ, in his words: "the logic part works for me, it's the code intricacies that mess me up."
**Design implication:** put a cheap API crutch AT THE POINT OF USE in each challenge card (the exact function signatures that challenge needs), not a "see Quick Reference" pointer. This is the single highest-value refinement from the walkthroughs. Candidate: a small "🔧 Functions you'll need" line per challenge listing just the signatures (`ledYellow(1/0)`, `display.gotoXY(col,row)`, `display.print(F("..."))`, `lineSensorValues[i]`).

## Student-difficulty roll-up
| # | Challenge | Concept(s) | Predicted student snag | Severity |
|---|-----------|-----------|------------------------|----------|
| C01 | Line Light | if/else · array slot · LED vs OLED · erase-with-spaces · gotoXY both branches | API recall (ledYellow/gotoXY/F/spaces); else-cleanup vs one-way state; 3v5 center-slot | MEDIUM |
| C02 | The Line Counter | transition-vs-state · bool memory · hysteresis · `&&` · reset block | `=` vs `==` (both directions, silent) · `};` vs `;`+`}` · stray `if(...);` · increment spellings · threshold inversion · slot `[1]` | MEDIUM |
| C03 | The Position Pointer | `readLine()` 0–2000 · integer-division scaling · off-by-one (`/251`) · `for` loop · `if/else` in a loop | ~~`for` not taught until L05~~ — **RESOLVED S57:** L04 §8A.6/§8A.7 now teach the `for` loop and the loop-with-an-if. Remaining snag is ordinary API recall, as with C01/C02 | **HARD** (was "misscoped") |
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


---
## Session 53 (Jul 19, 2026) — C02 COMPLETE (hardware-verified) · C03 PAUSED at the `for` wall

DJ had robot + surface + tape. **Book NOT edited; L04 stays v04.0.12.** Walked C02 end to end; C03 stopped at DJ's request ("I need a break, I'm frustrated") after the concepts landed but the syntax wall held.

### L04_C02 — The Line Counter — ✅ DONE, runs on hardware
DJ derived the entire mechanism Socratically: current reading + remembered previous reading → the arrival is the *transition* (light→dark), not the state; the release (dark→light) resets the memory; hysteresis band 500 catch / 400 release. **The logic was never the problem.** Every single stall was C++ syntax.

**Syntax walls hit, in order (each one a book candidate — see below):**
- `=` vs `==` — hit in BOTH directions in one challenge: `onLine = true` written inside an `if` (would fire every pass), and `onLine == true;` written as a standalone statement (asks a question, discards the answer, changes nothing). **Neither errors. Neither warns.**
- `count(ii + 1)` — parentheses read as a function call; increment written as if it were one.
- Three increment spellings all written at once (`count = count+1;` `count++;` `count += 1;`) → counter jumped by 3. DJ: "We need to point out the three different ways to do a count +".
- `if (...);  {` — stray semicolon after the condition; the `if` then controls nothing and the block runs unconditionally. Compiles clean.
- `};` vs `;` then `}` — statement terminator and block close conflated repeatedly; cost several rounds and broke `loop()`'s brace balance (helpers ended up defined inside `loop()`).
- Threshold inversion — catch 400 / release 500 (backwards), which makes the dead band an overlap band. Self-corrected once the consequence was named.
- Bool values inverted in both blocks simultaneously (`== true` / `= false` in arrival) — recovered once `onLine` was restated as the single question "was it dark last pass?"
- Array name singular (`lineSensorValue`) recurring.

**⭐ Slot ambiguity recurrence (3rd instance).** DJ first wrote `lineSensorValues(1,3,5)` — the *physical window* numbering — then over-corrected to `[2]`. Center on the 3-sensor array is `[1]`. This has now bitten in C01 and twice in C02. **Strengthens the existing S52 candidate: state the array size and center slot at point-of-use in every card.**

**⭐ Display collision — DJ ruling: MAKE IT A TEACHING MOMENT.** The card's own solution prints the count to `gotoXY(0,0)` — the exact cell `showReadings()` rewrites every loop pass. A student following the card verbatim gets an invisible counter and a "my code doesn't work" that is not a logic bug at all. DJ hit it, diagnosed it from the symptom himself, and fixed it with a one-character change (`(0,0)` → `(0,1)`). **Ruling: do not silently fix the card — keep the collision and teach it** (two things owning one resource; ask "what else is writing there?"). Candidate placement: a hint or a post-challenge note, not a spoiler.

**C02 verdict:** logic mastered (transition-vs-state, bool memory, hysteresis, reset). All friction was syntax + API. Severity for students: **MEDIUM** — but higher than C01 because the silent-failure syntax traps give no compiler help. Time: ~20 exchanges.

### L04_C03 — The Position Pointer — ⏸️ PAUSED (concepts landed, syntax wall)
**Landed:** division as the range-squashing operation; the off-by-one at `2000/250 = 8` (no column 8) and why the card divides by **251**; `c < 8` for exactly 8 passes (derived the `< count`, not `<= last index` rule).
**Wall:** writing a `for` loop and an `if/else` inside it. DJ: "I have no clue where to start." Also misfired reaching for `printLine("...")` (not a function), `position(c)` (parens = function call), `if c = ` (no parens, `=` for `==`), and "then" as a keyword.

**⭐⭐ BIG FINDING — C03 HAS A MISSING PREREQUISITE.** C03 requires writing a `for` loop. **`for` is not taught until L05 §5.15.** *(Section number corrected S57 — this log originally said §5.13, which is L05's `loop()` walkthrough, not the for-loop tutorial.)* A student reaching C03 has seen a `for` loop only as unexplained code inside their own `showReadings()` helper. This is the same class as the L03 modulo find, but worse: modulo was one operator in a reveal; this is the entire structure the challenge is built on. Options: (a) move C03 to L05 or later, (b) add a short `for` primer to the card, (c) restructure C03 without a loop (8 hand-written prints — the L03 Ramp "Option C" precedent), (d) leave it and accept it as a stretch challenge with the solution as the teach.

> **✅ RESOLVED — S57 (July 20, 2026). DJ ruling: none of a–d. Option (e): teach it in L04, where the lesson's own design already said tutorials go.**
>
> The audit that followed this finding changed its shape. `for` was **not** absent from L04 — the lesson **uses it 8 times in its own taught code and 5 times in its Maker payloads**, and Step 4 has students type one. §5.8 even narrates it in a single sentence. What L04 lacked was the *tutorial*: §8A taught `if` and stopped, while its own intro states the rule — *"the challenges in Section 9 use it immediately; this section makes sure you own it first."*
>
> That killed option (c) outright: unrolling C03's loop would have stripped `for` from two challenges while it stayed in eight places elsewhere in the same lesson, including a passage that explains it. Options (a), (b) and (d) all treated a teaching gap as a scoping problem.
>
> **What shipped (L04 v04.1.0, L05 v04.2.0):**
> - **§8A.6** — the `for` loop, opening with the loop the student already typed in Step 4, a lap-by-lap trace table, and the argument only L04 can make: Act One reads 3 sensors, Act Two reads 5, and the loop is why that switch cost one character. New figure `L04_GRAPHIC_4-06_for_anatomy.svg`.
> - **§8A.7** — a loop with a decision inside, taught from `showReadings()`'s own `if (i < NUM_SENSORS - 1)` line. This is precisely C03's and C04's shape, taught without giving either answer away.
> - **L05 §5.15** demoted from first contact to the §18.1 spiral second rung (🔁 Builds on: ⭐4), and it gained the **descending loop** (`i >= 1; i--`) that L05's own challenge solutions had been using while pointing back at a section that never taught it.
> - **Bible v8.36.1 §11** — *§8A must cover what §9 requires.* Using a construct inside the lesson's given code is not teaching it.
>
> **For the AI Tutor rebuild:** this find is the cleanest example in the book of a gap that reads like a difficulty problem. DJ's "I have no clue where to start" was not a hard challenge and not a weak student — it was a tool the book had handed over without ever opening. Check that distinction before re-rating anything.

### 📋 BOOK-TASK CANDIDATES (S53 — none applied)
6. **`=` vs `==`** — assignment vs comparison, **both failure directions**, each shown with its silent symptom. Highest-value item from this session; hit repeatedly and never errors. Placement TBD (L02 data-types callout neighborhood, or L03 where `if` is introduced).
7. **Three spellings of increment** — `x = x + 1` / `x++` / `x += 1`, all equivalent, pick one. Used across the book, taught nowhere. (DJ raised this twice, unprompted.)
8. **The stray-semicolon killer** — `if (...);` silently disables the `if`. Coach's Tip class: "compiles clean, does the wrong thing."
9. **`;` vs `}`** — every statement ends `;`, every block closes `}` on its own line; they never combine as `};` inside a function body.
10. **C02 display collision → keep and teach** (DJ ruling, above).
11. ~~**C03 `for`-loop prerequisite** — needs a DJ ruling among options a–d.~~ **✅ DONE S57** — ruled option (e): `for` is now taught in L04 §8A.6/§8A.7; L05 §5.15 became the spiral second rung. See the resolution block under C03.
12. **Slot ambiguity, 3rd recurrence** — reinforces S52 candidate #3-adjacent: name the array size + center slot at point of use.

### ⏱️ Time-cost note (DJ raised it)
DJ's worry: "how much time will students spend on this if it's taking me this long?" Reading: DJ's run **overstates** student time — he was doing two jobs at once (solving + auditing the book), and he is colder on C++ syntax than students fresh out of L01–L03 will be. It **understates** in one way: DJ diagnosed the display collision from the symptom in seconds; a student may stare at a blank row for ten minutes. Estimate for C02 with the card in hand: **~25–35 min**, acceptable for a MEDIUM §9 challenge (challenges are extensions, not milestones). C03 is the genuine outlier and the cause is the missing `for` prerequisite, not student effort. *(S57: the prerequisite now exists — §8A.6/§8A.7. Re-time C03 on the next pass before trusting the outlier label; the wall it measured has been removed.)*

### Next learner-mode session
L04 **C03** — **unblocked S57**, resume against the new §8A.6/§8A.7 (do the walkthrough with the tutorial in hand and see whether the wall was the loop or the API) · then C04 Edge Guard / C05 · L03_C05 Variable Speed still pending.
