<!-- ZUMO_TALKING_POINTS_F26_Wk3-4.md v1.0 — S200, Sep 1 2026. Teacher-facing. Covers periods 5–8 only. -->

# Talking Points — Periods 5–8

### Sep 16 · Sep 18 · Sep 21 · Sep 23 · Robotics D Block · Mr. Weymuth

> **Teacher-facing. Do not hand this to students.** Continues `ZUMO_TALKING_POINTS_F26_Wk1-2.md` v1.0.
> Companion to `ZUMO_Teacher_Daily_Grid_F26.md` v2.1. Where the two disagree, the grid is the schedule.
>
> **The model, unchanged:** they read before class and a graded quiz gates the door; **everything else
> — building, uploading, practice, challenges — happens in this room**, and each unit closes with an
> ungraded check.
>
> **This block is two lessons, not one.** Periods 5–6 are **L03 Motors & TRIM**, ending in the **M1
> demo**. Periods 7–8 are **L04 Line Sensors**, ending in the exit ritual — and **M2 is demoed on
> Sep 28**, in the L05 period, on the L04 program.
>
> Bracketed lines like *[if nobody answers]* are fallbacks, not script.

---

# PERIOD 5 — Wednesday, September 16 · 9:50–10:55 · 65 minutes

**The one job:** every robot drives, curves, and gets a TRIM number that its owner measured.

**Flip due:** L03 §1–§5 + reading quiz. ⭐ **This period opens with a live demo.**

> **Load note:** L03's pre-class read is **about 8,800 words — the longest in the term**, and this is
> the period the term gets steep. You warned them Monday. Expect at least one student who skimmed.

### 0–5 · Bell-ringer from the quiz

Pull the item analysis at 9:40. Two questions, five minutes, no re-teaching the lesson.

| if they missed | say this |
|---|---|
| **Which way it curves** | *"A robot turns toward its **slower** side. The fast wheel travels further and swings the nose away from it."* This one sentence prevents most of the period's frustration. |
| **What TRIM a left-curving robot needs** | *"Positive. TRIM always adjusts the **left** motor — in this lesson and every lesson after it. Positive boosts the left, negative cuts it."* |
| **The speed range** | *"Minus four hundred to plus four hundred. The **sign** is direction, the **size** is speed. Those are two separate pieces of information living in one number."* |
| **What speed 200 physically is** | *"It's not 'half throttle.' The driver switches full power on and off twenty thousand times a second, and 200 means it's on about half the time."* |
| **Open loop** | *"Sending a command with no feedback about what happened. The book calls it dead reckoning. Lesson 6 is where we fix it — today we live with it."* |
| **The battery numbers** | *"Fresh is about 5,400 millivolts, the healthy middle is about 4,800, and below about 4,200 you recharge. A TRIM tuned on a fresh pack drifts on a tired one."* |

### 5–18 · ⭐ The live demo — the crooked robot

**Do this with one robot, at the front, before anyone touches their own.** The whole demo is thirteen
minutes and it is the reason the lesson exists.

1. **Run it wrong first.** Both motors commanded to the same speed. Put a tape line on the floor and
   drive along it. It curves. *"Nothing is broken. This is a working robot."*
2. **Ask before explaining:** *"Both motors got the same number. Why didn't it go straight?"* Let them
   guess. Someone will say a motor is bad. That's the guess worth correcting.
3. **The answer, said plainly:** *"No two motors are the same. About one percent different, from the
   same factory on the same day. One percent per second, for ten seconds, is a robot pointing
   somewhere else."*
4. **Then fix it in front of them.** Add TRIM, re-run, drive straight. *"That number isn't in the
   book. It belongs to that robot. Yours will be different, and finding it is today's work."*

**Why the demo and not the reading.** They can read what TRIM is. What reading does not give them is
seeing a *correctly built* robot fail, which is the thing that makes them stop looking for a broken
part.

*[If the demo robot happens to drive straight]* — say so, and use it: *"This one's TRIM is near zero.
That happens. It doesn't mean yours is."* Do not fake it.

### 18–50 · Build the TRIM Finder — §6, fourteen steps

Let them work from the book. Circulate. Fourteen steps sounds like a lot; most are short.

**Three places the room will stall, and the one-line fix for each:**

1. **The deliberate red build at Step 12.** The book has them move `runMotorTest()` below `loop()` and
   rebuild on purpose. *"That error is the assignment. Read it, then put the prototype up top."* If a
   student skips the break, they will hit the same error by accident in Lesson 7 and not recognise it.
2. **The A+C reset branch has to come first.** It's checked with `isPressed()` while the three single
   buttons use `getSingleDebouncedPress()`. If a student's reset never fires, that ordering is why.
3. **Battery display looks like nonsense math.** `mv / 1000`, then a dot, then `(mv % 1000) / 100`.
   *"Integer division throws away the remainder. That's how you get 5.4 out of 5400 without a decimal
   type."*

**Say the floor space thing before anyone runs a motor.** They need about a metre of clear floor. At
`BASE_SPEED` 200 for two seconds, a measured run on our robots went **59 cm** — call it two feet of
travel plus room to stop.

**And the safety line, once, out loud:** *"Low speeds first. Know where your power switch is. A robot
that runs away is a robot nobody could reach the switch on."*

### 50–62 · Measure the TRIM — the actual lesson

**This is what the period is for. Protect these twelve minutes.**

Tape a starting line. Drive, watch, adjust, repeat.

**The one warning that saves the most time:** *"Judge left and right from the **robot's** point of
view, not yours. When it's driving away from you they agree. When it's driving toward you they don't,
and you will tune the wrong direction for twenty minutes."* This is the single most common way a TRIM
hunt goes backwards.

**Adjust in steps of 5 to 10, not 1 or 2.** *"A change of two is too small to see over a two-second
run. You'll burn a whole test learning nothing."*

**If a student needs more than about ±30** — that's the book's flag for a hardware problem, not a
tuning problem. Look at the robot yourself.

*[If two robots disagree wildly about how far speed 200 travels]* — before blaming code, check the
**coloured sticker inside the battery compartment**. It marks the gear ratio, and they are not
guaranteed identical across the fleet.

### 62–65 · Close and assign

Everyone writes their TRIM number in the notebook, in the L03 table, today. *"That number is data. It
goes in the paper. If you leave it on the screen it's gone when the robot powers off."*

> **Due Friday:** nothing new to read. **Come with your TRIM number and a working robot.**
> Friday is challenges and the **M1 demo**.

**Say the M1 line now, not Friday morning:** *"Friday you show me the robot driving straight and
driving a measured distance. Twenty minutes for five people. If your robot doesn't drive today, it
won't drive Friday."*

### What can go wrong today

| | |
|---|---|
| A student's robot never uploaded, from L01 or L02 | Fix it in the first ten minutes or they lose M1. This is the deadline that was set on Sep 14. |
| Someone tunes the wrong direction for the whole period | Stand behind them and re-run the robot driving **away**. Point of view is almost always the cause. |
| No clear floor | Move to the hallway rather than shortening the run. A 30 cm run hides the drift you're trying to see. |
| The build runs long | Cut the challenges from Friday, not the tuning from today. TRIM is the milestone. |

---

# PERIOD 6 — Friday, September 18 · 8:40–9:45 · 65 minutes

**The one job:** M1 signed off for all five, and nobody leaves without a recorded TRIM value.

**Flip due:** nothing new — L03's second period. No quiz, so no bell-ringer.

> **Timing note:** the demo window is real but short. Five students at roughly four minutes each is
> about twenty minutes, and that budget is what paid for L02's second period. If it overruns, the
> challenges are what gets cut.

### 0–3 · Open

One question to the room: *"Who does **not** have a TRIM number yet?"* Deal with those first, out
loud. Everyone else starts on challenges immediately.

### 3–22 · Finish TRIM tuning

Stragglers finish. Everyone else refines: *"Run it three times with the same number. Does it curve the
same way each time? If it doesn't, the number isn't the problem — the surface or the battery is."*

**The battery point lands naturally here.** A student whose robot behaved yesterday and wanders today
has a tired pack. Have them press **A and B together** to read the voltage. Below about 4,200 mV,
recharge — and note that the TRIM they measure on a dying pack is not the TRIM they'll demo with.

### 22–40 · Challenges

L03 has eight: **Spin Test · Battery Warning · Clamp the Speed · Ramp Up · Variable Speed ·
Save TRIM to Code · Drive a Square · Auto-TRIM Preview.** Nobody does all eight. Point each student at
one or two.

**How to pick.** Challenges 1–3 are the accessible ones. **Challenge 6 (Save TRIM to Code)** is the one
every student should do, because it's the one that survives into Lesson 6 — and it has a trap the
challenge names: saving the value but leaving the variable initialised to zero, so the robot still
starts at 0.

**Challenge 7 (Drive a Square)** is the honest preview of what's coming. *"If your square drifts badly
by the fourth corner, that's not bad tuning. That's open-loop control telling you it can't do this.
Lesson 6 is the answer."* Worth setting up out loud even for students who don't attempt it.

**Coaching, not fixing.** Same as Monday: *"What did you expect? Where's the line that does that?
What's the smallest change that tests your guess?"* Do not type in a student's file.

**If someone builds the LOW BATTERY warning and it fires on a full charge** — they're on USB. Say it
and move on; it's in the challenge.

### 40–58 · M1 demos

**Two parts, both required:** drives straight, and drives a **measured** distance.

Run them one at a time while the rest keep working. Video is allowed but with five students in the
room, live is faster.

**What you're actually checking on the code half (60% of the grade):** is it commented? *"Code without
comments loses points even if it runs"* was in the syllabus and this is the first time it's enforced.
Say it once here rather than writing it on five rubrics.

**What counts as a pass on the task half:** the robot goes where they said it would. A robot that
drifts two centimetres over 59 has passed. A robot that curves off the line has not.

### 58–65 · End-of-unit check and close

Draw eight from the L03 bank's `after` set. **Say "ungraded" before you hand it out and mean it.**
Then go over the two most-missed immediately, while they still care.

> **Due before 1:15 Monday:** read **Lesson 4, Sections 1–5** + reading quiz.

**Set up Lesson 4 honestly:** *"Monday your robot gets eyes. It still won't be smart — it just measures
brightness — but it's the first time it knows anything about the world instead of just doing what you
told it."*

### What to watch for by the end of this period

| signal | what it means |
|---|---|
| A student passed M1 with someone else's TRIM number | The number is per-robot. Re-run it in front of you. |
| Notebook still empty after three lessons | The TDP is 25% and cannot be reconstructed in November. Escalate now, not in October. |
| Struggled with Challenge 6 (the variable vs. the constant) | They will struggle with L04 §5.5's array indexing. Sit near them Monday. |

---

# PERIOD 7 — Monday, September 21 · 1:15–2:20 · 65 minutes

**The one job:** every robot calibrates and shows honest sensor numbers — first with three sensors,
then with five.

**Flip due:** L04 §1–§5 + reading quiz.

> **MATERIALS — check this Friday, not Monday.** Every student builds their own test surface in the
> first ten minutes and it needs **white poster board** and **3/4-inch black electrical tape**, at
> least two feet of it. Five of each. A marker line or printed line will not work — the sensors read
> infrared and only matte black tape absorbs it properly. **The whole period's data quality rests on
> this.** Position the surfaces away from windows.

### 0–5 · Bell-ringer from the quiz

| if they missed | say this |
|---|---|
| **Big number = dark or light?** | *"Big number means **dark**. The sensor is timing how long a tiny capacitor takes to drain, and more reflected infrared drains it faster. Dark surface, less light back, longer time, bigger number."* |
| **The sunlight question** | *"Sunlight is full of infrared. A sunbeam across your board floods the sensors and everything reads bright. It's why we're not by the window."* |
| **What calibration produces** | *"A per-sensor record of the brightest and darkest thing that sensor saw during the sweep. Not a setting — a memory."* |
| **Does calibration survive power-off?** | *"No. It lives in RAM. **Every session, every power-on, you sweep again.**"* This is the one they will forget on Wednesday and again in Lesson 8. |
| **Which sensors are always connected** | *"One, three and five. Those three have their own permanent wires. Two and four are the ones sharing, and the jumpers decide who gets them."* |
| **Whose left is sensor 1?** | *"The robot's. Sensor 1 is the robot's far-left eye, not yours."* |

### 5–12 · Build the test surfaces

Poster board flat, tape the corners if it curls, one straight strip of black tape down the middle at
least two feet long, pressed down hard at the edges. Generous white margins — at least a robot's width
of clean white on each side.

*"A lifted tape edge casts a shadow and reads inconsistently. A bump under the board tilts the robot
and changes every sensor's height. Five minutes here saves the period."*

### 12–20 · Find the windows and the jumpers

Hands on hardware, no code. §4.1 and §4.2.

Five sensor windows underneath, numbered from the robot's point of view. Then the two configuration
jumpers. **Have them look at the current position and say it out loud** — the jumpers start in the
factory proximity position, and they need to know what "home" looks like before they move anything,
because they're putting it back on Wednesday.

*[VIDEO 4.1, the close-up jumper procedure, is not shot yet — demonstrate it on one robot at the front
instead.]*

### 20–48 · Act One — three sensors, §6 Steps 1–6

Raw readings first, then calibration.

**Step 4 is the honest moment: raw numbers with no calibration.** *"Look at the three columns on plain
white. They don't match each other. Same surface, three different numbers. That's not a defect —
that's why calibration exists."*

**Step 5 is a deliberate red build.** They add `calibrateSensors()` to `setup()` and earn
`'calibrateSensors' was not declared in this scope`. *"That's a rep, not a detour. You saw this exact
error in Lesson 3 and you'll see it in Lesson 7. The fix is a prototype above `setup()`."*

**Step 6, after the sweep:** ask before they run it — *"What will the three numbers do on plain white
now?"* Then run it. They converge. That's the payoff and it's worth naming.

**The blind gap.** Slide the line from sensor 1 toward sensor 3 slowly. There is a position where the
dashboard reads all-white **with the tape still under the robot**. *"Find it. That gap is the reason
the next twelve minutes exist."*

### 48–60 · Act Two — software first, then jumpers

**Step 7 changes the code to five sensors and leaves the jumpers alone, on purpose.** Digits 2 and 4
report garbage. *"It compiled. It ran. Nothing warned you. Remember that — a sensor bug doesn't crash,
it lies."*

**Then Step 8 moves the jumpers to DN2 / DN4.** Power **off**, USB unplugged, robot posed over the
table, both jumpers straight up and straight down, fully seated.

**And the thing they will all skip:** *"You just changed the hardware. Calibrate again. The old sweep
knows nothing about sensors 2 and 4."*

### 60–65 · Close and assign

> **Due before 9:50 Wednesday:** nothing new to read. Come with a working five-sensor robot.

**Say this out loud:** *"Leave the jumpers on DN2/DN4 tonight. Wednesday we compare three against five
and then we put them back — you're borrowing those pins for exactly one lesson."*

### What can go wrong today

| | |
|---|---|
| No poster board or no black tape | The period does not work. This is a Friday problem, not a Monday one. |
| A surface near a window | Move it. Sunlight quietly poisons every reading and the symptom looks like broken code. |
| A student calls `initFiveSensors()` with factory jumpers and doesn't notice | That IS Step 7 and it's deliberate. Make sure they know it was deliberate, or they'll think they broke it. |
| Someone moves jumpers with power on | Stop them. Power off, USB unplugged, every time. |

---

# PERIOD 8 — Wednesday, September 23 · 9:50–10:55 · 65 minutes

**The one job:** the three-versus-five comparison, and **every robot leaves restored**.

**Flip due:** nothing new — L04's second period. No quiz.

> **The exit ritual is not optional and it is not homework.** Lesson 5 on Sep 28 needs the side
> proximity receivers, which live on the pins the jumpers are currently borrowing. A robot that leaves
> today on DN2/DN4 cannot do Lesson 5.

### 0–3 · Open

*"Who does not have five working sensors?"* Fix those first. Everyone else starts Test A.

### 3–20 · §7 — Test A and Test B

**Test A, Hide the Line.** Same board, same tape, same robot — only the configuration changes. That's
what makes it a fair test and it's worth saying: *"One variable. Everything else held still. That's an
experiment; anything less is an anecdote."*

In three-sensor mode the line can hide in two separate places. In five-sensor mode it can't. **Have
them find both hiding spots in three-sensor mode before switching** — the contrast is the lesson.

**Test B, the Slow Slide.** Print the position from the three-sensor program and slide the surface
underneath. *"Watch what the number does when the line falls into a gap. It doesn't go blank — it
jumps. A lying sensor is worse than a dead one."*

**Everything measured goes in the notebook now,** not later. The A4 calibration table wants minimum,
maximum, and the room's lighting. *"These numbers change in a different room. Write down which room."*

### 20–30 · §7.3 — the exit ritual

**Run this as a class, together, and check all five yourself.**

1. Power **off**, USB unplugged.
2. Section 4 pose, over the table. Both jumpers back — one to **LFT**, one to **RGT**. Straight up,
   straight down, fully seated.
3. **Verify with software.** Flash the Act One three-sensor program, sweep, press A, confirm sensors
   1, 3 and 5 all respond to the tape.

*"Never trust a hardware change without a test. Three honest sensors is what restoration looks like —
not two jumpers that look right."*

**Say what happens next, because it sounds contradictory otherwise:** *"At the end of Lesson 5 these
go back to DN2/DN4 permanently. Today you're handing the side receivers back for exactly one lesson."*

### 30–52 · Challenges

L04 has five: **Line Light · The Line Counter · The Position Pointer · Edge Guard · The Centering
Game.** Challenges 4 and 5 move the robot — clear floor, same rules as Lesson 3.

**Line Light is the one everybody should do.** It's their first `if`/`else` that acts on a real
measurement, and it has a trap worth watching for: the display work has to appear in **both** branches
or the screen keeps the last thing it drew.

**If someone finishes early**, point them at the observation experiments in §8 — covering a sensor
window and recalibrating is thirty seconds and it teaches more about calibration than another
challenge would.

### 52–62 · End-of-unit check — ungraded

Draw eight from the L04 bank's `after` set. Say ungraded, mean it, go over the two most-missed.

### 62–65 · Close and assign

> **Due before 1:15 Monday Sep 28:** read **Lesson 5, Sections 1–5** + reading quiz.

**And say the M2 line, because it is Monday:** *"Monday you also demo M2 — calibrate and report live
values. It's the program you already have. Don't delete it, and remember it needs a fresh sweep every
time you power on."*

Friday Sep 25 is the short 30-minute Family Weekend period — catch-up and materials check, no new
content. Anyone behind should be told out loud today that Friday is their window.

### What to watch for by the end of this period

| signal | what it means |
|---|---|
| A robot leaves with jumpers on DN2/DN4 | It cannot do Lesson 5. Catch it today; Friday's 30 minutes is the only buffer. |
| Empty calibration table in the notebook | M2 is demoed Monday and the TDP wants the numbers with the room's lighting. |
| A student who never found the blind gap | They missed the argument for five sensors entirely. Two minutes at their desk fixes it. |
| Still shaky on `if`/`else` in Line Light | Lesson 8's P-control is built on it. Flag them now. |

---

## Standing — all four periods

- **Exit ticket and one notebook line close every build period.** Last two minutes, every time.
- **Circulate. Don't sit.** Five students, twice a period each.
- **Never fix a robot by typing.** Ask what they expected, then where the line is.
- **Calibration does not survive power-off.** You will say this in Lesson 4, Lesson 8, and every
  competition run. Start now.
- **Autocomplete stays off.** It invents functions and wrong library versions and it looks right.
- **Every measured number goes in the notebook the day it is measured.** A number read off the OLED
  and not written down is gone.

---

*Periods 5–8 · Fall 2026 · companion to the daily grid v2.1 · v1.0*
