# ZUMO — S157 HANDOFF (written at S156 close · paste at top of Session 157)

## READ THIS FIRST — THERE IS UNPUSHED WORK AND IT MAY NOT EXIST ANY MORE

S156 edited `newproject.html` and `lessons/Lesson_10.html` in a container working copy.
**Nothing was pushed. HEAD is still `edd3d46`.** If DJ did not save the two delivered files,
that work is gone and must be rebuilt from the method recorded below. **Ask DJ before assuming
either state.** The files were delivered at S156 close with an explicit DO-NOT-PUSH.

md5 at close — `newproject.html` **91628ed50fba29636c209f7b7f91e69b** ·
`lessons/Lesson_10.html` **d209bd99cb6bab8cb9ca4270c14bb4ec**

**THEY ARE NOT PUSHABLE. 4 GATES RED + `gate_payload_match` RED.** L10 is half-converted:
payloads done, prose sentences done, printed code blocks NOT done.

---

# THE ONE THING TO CARRY OUT OF S156

**A COMPILE THAT DOES NOT MOVE IS NOT A FIX THAT DOES NOT COST — IT MAY BE A FIX THAT IS NOT THERE.**

The reverse-TRIM correction was priced at **delta = 0** on three lessons, and the ELF md5s
**differed**, which read as proof the change was live and free. Both readings were wrong.
Disassembly with addresses stripped showed **4 differing lines: the filename and one compiler
temp symbol** (`ccBKTYNV` → `ccFwfZed`). The md5 difference was a randomly-named temp, pure noise.

**The real cause: every shipped payload has `const int TRIM = 0;`** — it is the student's number
to fill in. So `speed + TRIM` and `speed + (-TRIM)` fold to the same constant and the compiler
emits identical code. Rebuilt with `TRIM = 8` injected, the fix separates cleanly at **+50 B**
(L06 single-file: +42). **Verified value-independent: +5, +8, +15, −5, −15 all give base 20,518
and fixed 20,568. Only TRIM = 0 collapses it.**

**A third near-miss in the same measurement:** a `unified_diff` count of "6 changed lines vs 4"
read as the fix being live where the reverse path is reachable. That was a counting artefact —
`unified_diff` emits `---`/`+++` headers that the filter counted as changes. Plain diff showed the
same 2 noise lines. **Instruction-level, nothing had changed anywhere.**

**RULE 85, NEW: A BINARY DIFFERENCE IS NOT A CODE DIFFERENCE.** Compare disassembly with
addresses stripped AND compiler temp symbols filtered, or you are reading noise.
**RULE 86, NEW: A CONSTANT THAT SHIPS AS ZERO HIDES EVERY SIGN BUG THAT USES IT.**

---

# S156's RULINGS

**OPTION C — `driveDistance()` AND `turnDegrees()` RETURN A `StopReason`.** Ruled, then talked
down to option A on September-8 pressure, then **DJ removed the date** (*"don't rush this book
because of a date"*) and **C was restored on merit.** The deciding argument: option A is correct
only *by accident* — `avoidPhase` still advances spuriously on a kill and is masked by
`avoidPhase = PHASE_TURN_AWAY` rewinding on entry to `OBSTACLE_DETECTED`. **Rule 20: a hold that
is also satisfied by an accident is not a hold.** And C is the same principle as C2 — a primitive
reports why it stopped and the caller must ask — so choosing A would teach one thing in prose and
the opposite in the students' own code.

**PHOTOGRAPHY IS DROPPED FROM THE CRITICAL PATH.** DJ: *"I am not worried about photography. So
drop it."* It is no longer tracked as a blocker.

**THE ENUM SPLITS ACROSS TWO LESSONS, TWO VALUES AT L10.** `STOP_DISTANCE` + `STOP_KILL` at L10;
`STOP_PROX` stays at L13. A one-value enum was scoped first and **is wrong** — the function must
return something on the common path where the leg simply finishes. Nothing was deleted; the enum
keeps all three values.

**`StopReason` IS BORN AT L10 STEP 6, NOT "AT L10".** The seam is the step where
`killSwitchPressed()` is born. Payloads before it keep `void` — **rule 47, a step payload is the
file as it stands at that step.** DJ ruled the early ones stay untouched and the change is
*taught* at Step 6 rather than flagged as a hazard.

**THE PRINTED MANEUVER SHOWS THE GUARDED FORM FROM ITS FIRST PRINTING** (Claude's call, DJ
deferred). The Step 6 INSIGHT teaches `StopReason` first; the lesson already spends one full beat
on type-it-wrong-then-fix (timed → encoder) and a second dilutes it; and the payloads are already
built and compiled guarded.

**FINISH L10 END-TO-END BEFORE STARTING L11** (Claude's call, DJ deferred). L10 invents the
pattern; six lessons built on a shape that later moves is the failure to avoid. L10 green is also
the only checkpoint the rollout currently lacks.

**THE TWO `delay(600)` ANNOUNCEMENTS STAY UNINTERRUPTIBLE AND ARE DESCRIBED HONESTLY.** Making
them interruptible would teach students to chase every blocking call on principle; leaving them
teaches the engineering question — *can this block hurt anyone?* Verified: `FOLLOWING_LINE` does
`motors.setSpeeds(0, 0);   // Stop FIRST - then think` before both, so the wheels are stopped.

---

# WHAT WAS MEASURED (all instrument-derived, none carried)

**THE TOOLCHAIN IS LIVE AND CALIBRATED AGAINST THE BOOK.** `objects: 41`. **Control: L11
`after_step_1` = 20,516, reproduced from a sixth clone.** Baseline compiled for **161 payloads**.

**EVERY BYTE FIGURE L10–L16 PRINTS REPRODUCES EXACTLY.** L10 `20,516` `+194` `+660` · L11
`20,702` · L12 `24,042` `24,690` `24,694` `24,718` `+800` · L13 `24,694` `24,874` `25,072`
`25,114` `+378` · L15 `28,214` · L16's entire ladder including **both deliberate overflows**
(28,824 = +152 over; 29,460 = +788 over; finished 28,600 with 72 spare).

**L16'S OVERFLOWS ARE NOT A DEFECT — THEY ARE THE LESSON.** Built S32, re-plotted S148.
`GRAPHIC 16.2` is captioned "the wall." The quiz bank's correct answers ARE these numbers, with
distractors naming the pre-S148 figures. **S156 flagged them as findings before reading the
lesson — rule 38 committed again.**

**C3 IS CONFIRMED AND WORSE THAN THE REVIEWER STATED.** Step 8's encoder "fix" changed the
accuracy axis and **nothing** on responsiveness. Derived structurally: `step_8_timed` = 7 phases,
1 kill check, 5 `delay()`, 0 blocking primitives; `finished` = 7 phases, 1 kill check, 0
`delay()`, **5 blocking primitives**. Five blocking legs became five blocking legs.
**`driveDistance()` had no timeout and no poll — a jam meant an unbounded block with B dead.**
`turnDegreesGyro()`: **71 of 71 bodies carry no `delay()` and no poll.**
**The book named the defect itself** — L13's `driveUntil` comment: *"`driveDistance()` is BLIND:
once it starts, nothing can interrupt a leg… A blind primitive, made watchful."*

**C1 IS CONFIRMED BUT THE REVIEWER AIMED IT WRONG.** L15 §3.5 already untaught it with
arithmetic: *"error = 8 / 0.1 = 80 units out of a ±2000 half-scale. That is 4%."* L15 also ships
`speedTrim` as `BASE_SPEED + speedTrim`. **The rule is not the defect; the justification is.**
L08's BC03 (*"a constant to spend the day undoing"*) and L10's glossary (*"make the controller
fight itself"*) are both backwards. L08 ships the absolute as a graded objective, **2 occurrences**.
**Recommended: keep the practice, rewrite the reason as pedagogical.** Rule 62.

**L07 CHALLENGE 1 IS "ADD REVERSE DRIVING" AND IT IS THE REVERSE-TRIM SITE.** Absent from
payloads because the student writes it; **9 mentions, L07 only.** Its own test claims
*"driveBackward(30); // Back 30cm - should return to start!"* — the exact claim the bug breaks.
**C4 and C7 are NOT reverse sites** (Speed Modes; Trapezoidal Profile) — that part of the S156
handoff was stale. **Only 3 payloads ever call `driveDistance()` with a negative:**
`L11/c1_backup`, `L13/challenge_9_1_keep_sweeping`, `L13/challenge_9_3_row_zero`.

---

# THE L10 CONVERSION — EXACT STATE

## DONE AND VERIFIED
**10 payloads converted** (`after_step_6/7/8`, `step_8_timed`, `finished`, `bonus_b1`–`b5`).
All compile. **Collateral: ZERO** — the other 105 payloads across all 16 lessons byte-identical.

| payload | before | after | Δ |
|---|---|---|---|
| after_step_6 | 19,562 | 19,606 | +44 |
| after_step_7 | 19,756 | 19,782 | +26 |
| after_step_8 | 20,416 | 20,492 | +76 |
| step_8_timed | 20,358 | 20,384 | +26 |
| **finished** | **20,516** | **20,592** | **+76** |
| bonus_b1 | 20,470 | 20,546 | +76 |
| bonus_b2 | 20,502 | 20,578 | +76 |
| bonus_b3 | 20,516 | 20,592 | +76 |
| bonus_b4 | 20,458 | 20,484 | +26 |
| bonus_b5 | 20,516 | 20,592 | +76 |

**THE BYTE-IDENTICAL SABOTAGE DESIGN SURVIVED:** finished / b3 / b5 were all 20,516 and are all
20,592. That property is load-bearing.

**`bonus_b5`'s PHASE_TURN_BACK IS A DELIBERATE SABOTAGE** — `turnDegrees(AVOID_TURN_DEGREES)`,
sign flipped positive, comment still reading *"Negative = left."* **A blind replace would have
silently repaired the bug students are meant to find.** An assert refused and the file was never
written. `bonus_b4` and `step_8_timed` are the TIMED variants — `delay()` legs, no primitive
calls, correctly no phase guards, hence +26.

**5 prose edits + 1 new callout** written to `Lesson_10.html`. Diff is 6 hunks, nothing
incidental. New **INSIGHT callout `data-callout="10.113"`** at the end of Step 6 teaching
`StopReason`. `callout_id --audit`: **1,121 callouts, 0 problems.**

Claims narrowed: *"in every state, at every moment"* → **"the whole time the wheels are
turning"**; *"without ever going deaf"* → **"while staying awake inside each one"**; §8.3's wrong
troubleshooting cause replaced (it sent students to a line already in their file — the S143 shape).

**VERIFIED: NO DEAF-WHILE-MOVING WINDOWS REMAIN.** Only four blocking constructs exist in the
finished build — `waitForStart` (before motion), `checkBattery` (STOPPED only, polls anyway), and
the two primitives, both now polling.

**ONE DEFECT OF CLAUDE'S, FOUND AND FIXED:** a literal U+202F in "600 ms" — §27.16 requires the
entity `&#8239;` for invisible characters.

## NOT DONE — THIS IS WHERE S157 STARTS
1. **L10's PRINTED §6 CODE BLOCKS.** The lesson prints the seven-phase `AVOIDING_OBSTACLE`
   switch and it now disagrees with the payloads. **Claude wrongly concluded earlier that L10
   prints no motion code — it prints no `void driveDistance(` DEFINITIONS but it does print the
   CALL SITES.** Findings cluster: `StopReason` 88 · `STOP_KILL` 52 · `STOP_DISTANCE` 30 ·
   `RobotConfig.h` 29 · turn wrappers 26.
2. **L10's PRINTED BYTE FIGURES** — `20,516` → `20,592`, and the Step 6 checkpoint's `+2 bytes`
   has moved. **Re-derive from the harness; never hand-type.**
3. **`build_css.py` restore → regenerate → apply** (§27.8b). §27.13 is red.
4. **THREE DENOMINATOR PINS**, red because one callout was legitimately added — §24.14 and
   §24.14a (1,121 vs pinned 1,120) and §21 (1,204 image refs vs pinned 1,203, from the
   `stars.svg` mark inside the new callout). **Rule 29: pin the denominator. DERIVE, never
   hand-type.**

## `gate_payload_match` CANNOT BE SCOPED — AND SHOULD NOT BE
It carries a coverage guard: *"a gate that checks a subset and reports PASS is not a gate."*
**Read its FINDINGS instead of its verdict.** L01–L09 passed in alone returns FAIL(1) where the
single finding IS the coverage complaint — i.e. **zero real mismatches in the untouched lessons.**
**Do not compare its counts across different argument sets:** L10-alone reported 300 and the full
book reports 606; those are different measurements, not a subset relation.

---

# THE REST OF THE ROLLOUT

**102 payloads get C, not 115.** Scoped to those carrying `killSwitchPressed`:
L10 **10 of 21** · L11 17/17 · L12 21/21 · L13 **17 of 19** (`ladder_7a_surface_meter` and
`ladder_7c_leg_and_turn` have no kill switch) · L14 12/12 · L15 16/16 · L16 9/9.

**MEASURED COST, PER LESSON — DO NOT EXTRAPOLATE ONE LESSON'S FIGURE TO ANOTHER.** S156 quoted
+76 book-wide from L10 alone and was wrong twice over: it extrapolated from one lesson, and
extrapolated a composite (primitives ≈ +40 plus callers ≈ +36) as if it were a unit cost.
Primitives-only: **L10 +40 · L13/L14/L15/L16 +64.**

**L16 IS THE CONSTRAINT AND IT NEEDS A TRADE.** `finished` ships with **72 bytes spare**.
Primitives-only puts it at 28,664 — fits with **8 bytes**. Reverse-TRIM's +50 erases that.
**L16 MUST BE LAST**: its Step 1 IS L15's finished build, so it cannot be re-plotted until L15's
number is final. Do not touch L16 prose before then. Precedent for the re-plot is S148.

**THE MAKER CANNOT BE ROUND-TRIPPED THROUGH `json.dumps`.** No indent setting is byte-identical —
closest is off by **6,070 characters**. Re-serializing would bury ~100 real changes in formatting
churn (rule 69). **The method: locate each payload's key inside its lesson span, brace-match its
byte range, replace only within it, DESCENDING by position.** Lessons are **not** stored in
numeric order — file order is 1, 15, 14, 13, 12, 11, 8, 9, 7, 6, 4, 3, 5, 2, 10, 16.
**`#include "RobotMotion.h"` appears TWICE per payload** (main.cpp and RobotMotion.cpp); the
unique landmark is `#include "RobotMotion.h"\n\n// ===== FUNCTION IMPLEMENTATIONS =====`.

---

# STILL OPEN, CARRIED FROM S156

- **C2 — SENSOR-AS-TRUTH LANGUAGE. RULED: ADOPT.** Phrase it *a sensor answers its own question,
  not yours.* L04–L13 prose plus the quiz re-keying it forces. **The strongest item in the review.**
- **C6 — COMPETITION RULE vs ROBOLORE POLICY.** Blocked on the rulebook pass. **Still the cheapest
  move in the queue and it needs no ruling** — 8 findings, one read of `RCJRescueLine2026-final.pdf`
  which is in the repo root. Reviewer's rulebook claims carry no edition (rule 63).
- **C4 and C5 remain STRUCK as new items**; instances still need disposition per-lesson.
- **§16.25's BODY IS STALE BY ONE SESSION.** Bible line 2662, inside the numbered section body,
  still says in the present tense that lessons and Maker ship `a-star32u4` lowercase "in six
  places" and that normalising is *"a ruling, not a defect fix."* **S155 made that ruling and
  applied it** — all six sites are uppercase, verified S156. **DJ ruled: RECORD IT.** Minor Bible
  bump, doc-only. The two other lowercase hits (lines 17, 98) are changelog narration and are
  correct as past-tense — leave them.
- **L03's PHOTOGRAPH `L03_IMAGE_3-14_astar_board.jpg`** still names a board the robot does not
  contain. Unruled.
- Everything else in the S156 handoff's §3, §4, and the carried-from lists stands unchanged.

---

<!-- VERSION BLOCK -->
Repo unchanged at **`edd3d46`**. Census **40,668**. Bible **v8.145.1** · Maker **v2.51**
(working copy modified, unversioned — **the version bump is owed when L10 lands**) ·
L10 **v02.29.2** (working copy modified, unversioned).
All other artefact versions as recorded in the S156 handoff's version block.

**NO VERSION WAS BUMPED IN S156 BECAUSE NOTHING SHIPPED.** When L10 lands: Maker and L10 both
bump, and **LIVE.md is regenerated LAST** (§12.6 — a push that bumps a version and omits LIVE.md
is an incomplete push).
