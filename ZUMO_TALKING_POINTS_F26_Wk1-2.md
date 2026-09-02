<!-- ZUMO_TALKING_POINTS_F26_Wk1-2.md v1.0 — S199, Aug 31 2026. Teacher-facing. Covers periods 1–4 only. -->

# Talking Points — Periods 1–4
### Sep 4 · Sep 9 · Sep 11 · Sep 14 · Robotics D Block · Mr. Weymuth

> **Teacher-facing. Do not hand this to students.** Companion to `ZUMO_Teacher_Daily_Grid_F26.md`
> v2.1 and `ZUMO_DAY1_F26_Sep4.md` v1.0. Where the two disagree, the grid is the schedule and the Day-1
> script is the minute-by-minute.
>
> **The model, in one line:** they read before class and a graded quiz gates the door; **everything
> else — building, uploading, practice, challenges — happens in this room**, and each unit closes
> with an ungraded check.
>
> Bracketed lines like *[if nobody answers]* are fallbacks, not script.

---

# PERIOD 1 — Friday, September 4 · 2:05–2:30 · 25 minutes

**The one job:** every student leaves with a robot and knows where the book is. Everything else is
optional today.

### 0–4 · Hand out the hardware

Print `ZUMO_DAY1_SIGNOUT_F26.md`. Four items each: robot, USB cable, four AA eneloop, jumpers.

Read the agreement line aloud once before they sign. It takes fifteen seconds:

> *"I have this robot, this cable, four batteries and my jumpers. I bring all of it to every class,
> charged. If something breaks, I tell Mr. Weymuth — I don't hide it and I don't try to fix it
> myself."*

**Why the last clause is the one that matters.** Say it plainly: *"A student who works around a dead
motor for three weeks loses a milestone. A student who tells me on the day loses nothing. I am not
going to be annoyed. I am going to be annoyed if I find out in October."*

**The cable warning, said once, out loud.** *"This is a data cable. A charge-only cable looks
exactly the same and will not work. Don't swap it with the one in your room."* This is the single
most common Week-1 failure and it costs a whole period to diagnose.

### 4–9 · How this class works

Four sentences, one minute each. Do **not** open the syllabus and do **not** explain the grade
breakdown — that dilutes the period and they can read it.

1. *"You read the lesson before class."*
2. *"A short quiz opens the door. It's on the reading — nothing else."*
3. *"Class time is building. I don't lecture; I circulate."*
4. *"Seven milestones. You show me the robot doing the thing."*

**If one student asks "what if I fail the quiz?"** — answer it honestly and briefly: *"You're not
locked out. You catch up on the reading and then you join the build. It's a door, not a wall."*
Don't elaborate. The soft-gate policy is in the syllabus.

**Expect the "is this hard?" question.** Best answer: *"It's hard the way learning an instrument is
hard. Nothing today is beyond you. The thing that sinks people is falling behind, not difficulty."*

### 9–13 · Where things live

Three things on the board, and leave them up:

- **Canvas** — quizzes and submissions
- **weymuth.github.io/zumo** — the book
- **the Project Maker** — starting code

### 13–15 · Everyone opens the book, right now

Phones are fine. *"Go to weymuth dot github dot io slash zumo. Click Lesson 1. Read me the first
heading."* The first heading is **"The True Story of 'Hello, World!'"** — if a student reads you
something else, they're on the wrong page.

**Watch all five screens.** This is two minutes that converts the period's one unverified assumption
into a verified one. A typo'd URL costs a student the entire weekend and you will not find out until
Wednesday.

### 15–20 · The assignment

Read it out. Say the due time out loud twice.

> **Due before 9:50 AM, Wednesday September 9:**
> 1. Read Lesson 1, **Sections 1 through 5**.
> 2. Install **Visual Studio Code, Git, and the PlatformIO extension** — Section 4 walks you through
>    all three.
> 3. Take the **Lesson 1 reading quiz** in Canvas.

**Say what is NOT assigned, or they will worry about it.** *"Sections 6 and 7 are building and
uploading. Don't. We do that together Wednesday. If your tools are installed, you're done."*

**The reassurance, because they will assume the worst.** *"You have five days and a weekend. The
reading is about twenty minutes. The install is the part that takes time, and it's mostly waiting on
downloads."*

**Say the Git thing.** Students skip it because they don't know what it's for and nothing appears to
break. *"Install Git even though nothing visible happens. PlatformIO needs it underneath. There's a
quiz question on why."*

### 20–25 · Questions, and the one warning

> *"If your laptop isn't ready Wednesday, you'll spend Wednesday fixing it instead of driving your
> robot."*

That's the whole warning. Concrete cost, not a scolding.

**If time remains** — and with five students it might — let them look at the robot. Don't start a
lesson. Don't hand out the syllabus in the last four minutes; it will be lost.

### What can go wrong today

| | |
|---|---|
| A student has no device at minute 13 | Pair them with a neighbour's screen. The point is that every student has watched the page load once. |
| Somebody's robot is visibly damaged | Swap it now from the spares. Note it on the sheet's condition column. |
| The handout runs long | Cut the "how this class works" block to two sentences. Never cut minutes 13–15 or the assignment. |

---

# PERIOD 2 — Wednesday, September 9 · 9:50–10:55 · 65 minutes

**The one job:** every robot beeps, blinks, moves and plays the victory jingle before they leave.

**Flip due:** L01 §1–§5 + install + reading quiz.

### Open: read the quiz before class, not after

The quiz is your bell-ringer. Pull the item analysis at 9:40 and pick the two questions the class
did worst on. Likely candidates and the fix for each:

| if they missed | say this |
|---|---|
| **Q1, the robot cycle** | *"Sense, think, act. Every single thing we build this term is those three words in a loop."* Draw it on the board once; you'll point at it all term. |
| **Q2, open vs closed loop** | *"Open loop is driving with your eyes shut and hoping. Closed loop is looking. Today's robot is open loop — it's blind, and that's the whole reason Lesson 4 exists."* |
| **Q3, why Git** | *"PlatformIO uses it underneath to fetch libraries. You'll never type a Git command in this course."* |
| **Q5, the `@2.0.1` pin** | *"That number freezes the library version. Without it your robot works today and breaks in November when Pololu ships an update."* |
| **Q7, the include** | *"`#include` opens the library that `lib_deps` downloaded and pours every Zumo command into your program."* |
| **Q8, the for loop** | Trace it on the board. `i` starts at 0, runs while `i < 3`, so 0, 1, 2 — three passes. This one predicts who will struggle in Lesson 3. |

Keep this to five minutes. **Do not re-teach the whole lesson.**

### 5–10 · Toolchain check

Walk the room. You are looking for exactly two things: **VS Code opens**, and **the PlatformIO icon
(the alien head) is in the left sidebar.** Nothing else.

*[If a student's install failed]* — sit them next to a working student, have them start the install
now, and let them watch the neighbour build. Do not spend the period on one laptop. They can finish
tonight; the material is not lost.

### 10–45 · Build and upload — L01 §6, six steps

Let them work from the book. Circulate. The six steps are: create project → configure
`platformio.ini` → add the code → connect the robot → build → upload.

**Three places the room will stall, and the one-line fix for each:**

1. **They pick the wrong board.** The PlatformIO board profile is `a-star32U4` with a capital U.
   *"That's a tooling name, not a part inside your robot. Your robot is a Zumo 32U4."* Say this or a
   student will spend Lesson 3 looking for an A-Star on the board.
2. **The upload can't find the port.** Nine times out of ten the Serial Monitor is still open. *"Only
   one program can hold the port. Close the monitor, upload again."*
3. **Nothing happens and no error appears.** The power switch is off. It's the first thing to check
   and the last thing anyone checks.

**Say the port thing before they plug in, not after:** *"Use the same USB port every time. Switching
ports changes the COM number and produces upload errors that look like broken code."*

### 45–58 · Test it — §7, and make them predict first

**This is the highest-value ten minutes of the period. Don't skip the prediction.**

> **"Prop the robot on a cup or a box so the tracks spin free. It is tethered by a short cable and
> it will drag itself off the desk."**

Then, before anyone presses anything:

> *"Write one sentence: exactly what do you expect it to do, and in what order? You wrote this code.
> You should be able to call the shot."*

What should happen when they press A: display shows "Press A" → beep at 440 Hz → yellow LED blinks
three times → "Moving!" → nudge forward, then backward → "Done!" → victory jingle, C-E-G.

**Then the checkpoint, which is the actual lesson:** *"Did it match your sentence? If anything
surprised you — wrong order, wrong count, a sound you didn't expect — open the code and find the
exact line responsible."* A student who traces one surprise back to one line has learned more today
than one whose robot worked first try.

*[Reset button is near the USB port — they'll want to run it again.]*

### 58–65 · TDP notebook copy

Everyone makes **one copy** of the template and puts it in their own Drive. Name and date on every
entry. *"This is not busywork and it is not a report you write at the end. It's a real competition
document and you fill in a piece each lesson."*

**Engineer's Log #01 is the "before" paragraph** — what board, what processor, what it can do today.
Say why: *"In Lesson 16 you write the 'after.' The gap between them is your abstract. You cannot
fake this one later, which is why it's due first."*

### Assign, before they leave

> **Due before 8:40 AM Friday:** read **Lesson 2, Sections 1–5**. That's it — no building.

**Say this about Lesson 2 §1:** *"Section 1 is four short mystery programs with no instructions. Read
it, but don't solve them at home — we do those together Friday and it doesn't work if you've already
seen the answer."*

---

# PERIOD 3 — Friday, September 11 · 8:40–9:45 · 65 minutes

**The one job:** the warm-up gauntlet and the debrief. This is the period that teaches them to read
code instead of guessing at it.

**Flip due:** L02 §1–§5 + reading quiz.

> **Load note:** L02's pre-class read is **about 8,300 words — the heaviest in the term**, and §3 alone is more than half of it. It's why L02 now has two periods instead of one. Don't try to cover §3 and the
> warm-ups on the same day.

### 0–5 · Bell-ringer from the quiz

Likely weak spots, in order: **the two-week rule** (§3.5), **`&&` vs `||`** (§3.4), and **data
types** (§3.2).

- **The two-week rule:** *"Write comments for the person who reads this in two weeks. That person is
  you, and they will have forgotten everything."*
- **`&&` vs `||`:** *"AND means both. OR means either. The bug you will actually write is using OR
  when you meant AND, and the robot will do something almost right."*

### 5–30 · The warm-ups — four mysteries, no instructions

Setup, said once: *"Copy your ZUMO_Template and name it LastName_L02_Mystery. One sandbox, not four
— you'll paste each challenge into the same folder. The clock is running."*

**The rules, and hold them:** work independently, no asking for help, limited time on each.

**This is deliberately uncomfortable and you should say so afterward, not before.** The point is that
they experience needing structure before they're taught structure. If you rescue them, the debrief
has nothing to work with.

The four: **Blink Speed · Wrong Button · Find Your Name · Spin Direction.**

*[If a student finishes all four early]* — have them write down, for each one, the exact line that
told them the answer. That's the debrief currency.

*[If a student is stuck and frustrated]* — *"You're supposed to be stuck. That's the point of the
next twenty minutes."* Don't give the answer.

### 30–45 · The debrief — the real lesson

Run it as discussion, not lecture. The questions that do the work:

1. *"What did you look for first?"*
2. *"What made one of these easier than another?"*
3. *"Which one wasted your time, and why?"*

Land it here: *"You were reading someone else's code with no map. Section 3 is the map — nine
sections, always in the same order. From now on every program you open has the same shape, and you'll
know where to look."*

The sheet-music comparison from §1 is worth repeating out loud: structure is what lets musicians play
each other's songs, and it's what lets programmers read each other's code.

### 45–62 · L02 §6 — build the Status Screen

Straightforward after L01. Two reminders:

- **Same USB port as last time.** Switching ports changes the COM number.
- **The Maker's DISCOVERIES menu exists.** *"Wrecked your file? Missed a day? Pick the Discovery for
  the thing you're building and it opens a project already caught up. No shame, no retyping."* Say
  this now, before anyone needs it, so nobody spends twenty minutes retyping in silence.

### 62–65 · Close

> **Due Monday:** nothing new to read. *"Come ready to work — Monday is challenges."*

Monday is L02's second period and there's no new flip, so this is the one night in the first two
weeks with no reading. Say that; they'll notice and it buys goodwill.

---

# PERIOD 4 — Monday, September 14 · 1:15–2:20 · 65 minutes

**The one job:** the six bonus challenges, and finish anyone still trailing from L01.

**Flip due:** nothing new — L02's second period.

### 0–5 · Open

No bell-ringer; there's no new quiz. Instead, one question to the room: *"Who still has a robot that
hasn't uploaded successfully?"* Deal with that first, in front of everyone, in five minutes or less.
Anyone still broken on Wednesday is in real trouble, because L03 is where the term gets steep.

### 5–50 · Challenges

Six of them: **Blink Count · Backwards LED · Buzzer Pitch · Line Order · Endless Beep · Speed Limit.**

**How to coach these, which is different from how you taught the build.** They write the code. Your
job is questions, not answers:

- *"What did you expect it to do?"*
- *"Where's the line that does that?"*
- *"What's the smallest change that would test your guess?"*

**Do not fix a student's code by typing in it.** A student who watches you fix it has learned that
you fix it.

**The AI autocomplete warning, and say it here rather than later.** *"Turn autocomplete off. It will
confidently invent functions that don't exist and library versions that aren't ours. It looks right
and it wastes an hour."*

**Speed Limit is the one that predicts Lesson 3.** A student who handles it cleanly will be fine with
TRIM. One who doesn't needs watching on Wednesday.

### 50–60 · End-of-unit check — ungraded

Draw eight from the L02 bank's `after` set. **Say "ungraded" before you hand it out and mean it.**
*"This is so you and I both find out what didn't land. It's not in the gradebook."*

Then go over the two most-missed answers immediately, while they still care.

### 60–65 · Close, and set up Wednesday

**Lesson 3 is the first genuinely hard one.** Set it up honestly:

> *"Wednesday your robot drives. You'll find out that no two motors are the same — yours will curve,
> and you'll fix it with a number you measure yourself. That number is called TRIM and it's the first
> real engineering you do in here."*

> **Due before 9:50 Wednesday:** L03 §1–§5 + reading quiz. **Heads up: it's a long one — start it
> Monday night, not Tuesday night.**

L03's pre-class read is about 8,800 words, the longest in the term. Warning them is free and it works.

### What to watch for by the end of this period

| signal | what it means |
|---|---|
| A robot still hasn't uploaded | Fix before Wednesday or that student loses M1. |
| Struggled with Speed Limit | Sit near them during L03 TRIM tuning. |
| Notebook still empty | The TDP is 25% of the grade and it cannot be reconstructed in November. |

---

## Standing — all four periods

- **Exit ticket and one notebook line close every build period.** Not a separate agenda item; it's
  the last two minutes.
- **Circulate. Don't sit.** With five students you can reach everyone twice a period.
- **Never fix a robot by typing.** Ask what they expected, then where the line is.
- **Reading is checked at the door; everything else happens here.** If you find yourself lecturing
  for more than ten minutes, the flip has failed and the fix is the quiz, not the lecture.

---
*Periods 1–4 · Fall 2026 · companion to the daily grid v2.1 · v1.0*
