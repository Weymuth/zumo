# Robotics — Zumo Autonomous Robot
### How This Class Works · Fall Trimester · Mercersburg Academy · Mr. Weymuth
<!-- ZUMO_Syllabus_WORKING.md v1.0 — S96, Jul 30 2026 -->

> **This is a working draft.** Sections marked _[TBD]_ aren't finalized yet. Everything else reflects decisions made as of this planning session. This document will grow into the student-facing syllabus.

---

## What You're Going to Do

Over this trimester you will program a Pololu Zumo 32U4 robot to navigate a line-following course on its own — driving straight, following a line, making decisions at intersections, avoiding obstacles, crossing gaps, and finally finding the rescue zone and stopping at its edge. You'll do it in stages, and you'll document the whole thing as you go.

You work on **your own robot** — this is a solo build, not a team project.

---

## How Class Runs Each Day

This is a **flipped classroom**. That means the *reading* happens before class, so *class time* is for building, testing, and getting help — not for lectures.

**Before class (at home or in open lab):**
1. **Read** the assigned lesson section in Canvas.
2. **Take the reading quiz** in Canvas. It's short, auto-graded, one attempt, and it **locks when class starts** — so you have to do it *before* class.
3. **Pull your starting code** from the Project Maker.

**In class (65 minutes):**
- **First few minutes — Bell-ringer.** Mr. Weymuth reviews the 2–3 things the class struggled with on the reading quiz. This is your live teaching moment; it's short because you already did the reading.
- **Most of the period — Build time.** You work at your own pace on your current lesson. Mr. Weymuth circulates to help, checks that you brought your materials, and signs off milestones when you're ready.
- **Last few minutes — Exit ticket + notebook.** You complete the end-of-lesson checklist (what you should now be able to do) and add one line to your engineering notebook.

A few lessons have a tougher concept than reading alone can carry — encoders, the multi-file code structure, proportional control, the state machine. On those days, Mr. Weymuth will give a short live demo at the start. Everything else, you get from the reading.

---

## The Reading Quiz — Read Before You Build

**If you don't pass the reading quiz, you're not cleared to start building that day.**

You read the section, retake the quiz, *then* you join the build. This isn't a punishment — it's because trying to build a lesson you haven't read wastes your class time and everyone else's. The reading quiz is your ticket into the day's work.

This is a **soft gate**: you're never locked out of the course, just asked to catch up on the reading first. The open lab (M–Th evenings) and your free periods are there for exactly this. Come prepared and this never comes up.

*(Mechanically: the quiz opens before class and closes at the start of the period. One attempt, auto-graded in Canvas.)*

---

## Milestones — What You Prove, and When

The course is built around **7 milestones**. Each is a checkpoint where you show that your robot can do something new. You have flexibility in *how and when* you get there between checkpoints — but the checkpoint dates are fixed, so you always know what has to be done by when.

Each milestone has two parts:
- **Your code (60%)** — is the program correct, complete, and commented? Code without comments loses points even if it runs.
- **The task (40%)** — does the robot actually do the thing? You can **demo live** to Mr. Weymuth *or* **upload a video**.

| # | Milestone | You'll show that your robot can… | Approx. |
|---|---|---|---|
| M1 | Foundations | drive straight and a measured distance (TRIM works) | Week ~1.5 |
| M2 | Sensing the Floor | calibrate and report live sensor values | Week ~3 |
| M3a | Measuring the World | drive an accurate 30 cm and close a square | Week ~4.5 |
| M3b | Follows the Line | follow a line around a course | Week ~6 |
| M4 | Makes Decisions | handle a T, a turn, and a dead end | Week ~7 |
| M5 | Handles the Course | avoid an obstacle and cross a gap | Week ~8.5 |
| M6 | Finds the Zone | run the full course and stop at the rescue zone | Week ~9.5 |

_[Exact dates TBD once the class schedule is finalized.]_

> **Milestones build on each other.** A missed checkpoint makes the next one harder. Most milestones need some work outside of class — plan ahead, and use the open lab.

---

## Your Engineering Notebook (= Your TDP)

You keep one running engineering notebook for the whole trimester. It's not busywork — it's structured as a real **Technical Description Paper**, the kind teams submit at RoboCup competitions. You fill in a piece each lesson, and by the end it's a complete document.

Your notebook **is** your competition TDP — they are the same document. You do not write a paper at the end; you fill in a piece each lesson, and by Lesson 16 it is written.

**Get it:** _[LINK TBD — the Google Doc copy of the TDP template]_

**Set it up, once, on day one:**
1. **File → Make a copy**
2. Rename it: `TDP — Your Name`
3. Keep it in your own Drive all term
4. Share it with Mr. Weymuth (comment access is enough)

**How it is built:**
- **Part A — Standing Logs.** You add to these all term, not once: the work you did, one improvement idea per lesson, a failure log, your measured data tables, and your lab-time log.
- **Part B — The TDP.** Eight sections. Each lesson's Engineer's Log entry drops into a section that is already marked for it.

**Two rules that matter:**
- **No source code.** Diagrams, tables, and prose only. Judges reward measured data over adjectives.
- **Date every entry, and do not go back and edit old ones.** Your Lesson 1 "before" paragraph and your Lesson 16 "after" are supposed to disagree — the gap between them *is* your abstract.

### How to Submit

You keep one document all term; you never submit a new file.

- **Weekly:** your notebook is checked in place. Nothing to upload — Mr. Weymuth opens your shared doc. Keep it current; an entry written three weeks late reads like one.
- **At each milestone:** the relevant log entry must already be in the doc when you demo.
- **At the end of term:** you submit the **link** in Canvas, one time. The document you have been filling in all term *is* the final submission.

---

## How Your Grade Works

| Category | Weight | What it is |
|---|---|---|
| **Milestones** | 35% | The 7 checkpoints — code (60%) + task performance (40%) |
| **Engineering Notebook / TDP** | 25% | Your running notebook, filled in as you go |
| **Reading Quizzes** | 20% | Short pre-class quizzes — read before class |
| **Exit Tickets / Checklists** | 10% | End-of-lesson "can you do this?" self-checks |
| **Materials** | 5% | Come ready: robot, case, charged batteries, programming cable |
| **Outside Work** | 5% | Logged lab/practice time outside of class |

---

## If You Fall Behind

Milestones build on each other. A missed one makes the next harder, and the course does not slow down to wait. So the plan is: **catch up fast, on a known path, without drama.**

**If you miss a reading quiz:** retake it before you build that day. You are not locked out of the course — you are asked to read first. Do it in open lab or a free period.

**If you miss a milestone date:** it is not a zero and it is not forgotten.
1. **See Mr. Weymuth within one class period.** Not next week.
2. **Name the blocker.** Be specific — unfinished reading, a build that won't compile, a robot problem, missing data, a behavior that still fails. "I'm stuck" is not a blocker; "my robot overshoots every left turn" is.
3. **Go back to the last thing that worked.** Get that behavior running again before you add the next one. Debugging two problems at once is debugging neither.
4. **Agree on a catch-up date** — normally the next open lab.
5. **Come with one named target,** not "work on the robot."
6. **Demo, and update your notebook the same day.** The catch-up is done when the robot, the code, and the notebook all agree.

Late milestones are graded on the same rubric, with a late penalty of _[AMOUNT TBD]_.

**If you are behind by more than one milestone:** stop trying to do both at once. We will pick the one that unblocks the most and get that working first — newer lesson work can wait until the thing underneath it is stable. Three **buffer periods** are built into the term for exactly this; they exist so that falling behind is recoverable, not fatal.

**The one thing that does not work** is going quiet. Every problem in this course is smaller the day it happens than the week after. A problem you report can be scheduled. A problem you hide becomes several problems.

---

## Coming Prepared (the Materials grade)

Every class, bring:
- Your robot
- Your marked carrying case, with **all four batteries charged**
- Your USB cable

Coming to class with uncharged batteries means your robot cannot work that period. That is a Materials grade.

---

## Batteries — Read This Once, Follow It All Term

Your Zumo runs **four rechargeable NiMH AA cells — Eneloop Pro by Panasonic.** Every battery number in this course is written for NiMH. Here is what your robot will tell you when you hold **A + B**:

| Reading | What it means |
|---|---|
| ~5,400 mV | Fresh off the charger |
| ~4,800 mV | The plateau — normal, healthy, most of the battery's life |
| ~4,200 mV | Nearly empty. **Stop and swap.** |
| ~6,300 mV | Somebody put alkalines in |

**Three rules:**

1. **Do not run below 4,200 mV.** Draining NiMH past ~1.05 V per cell damages the cells permanently. The robot will still move — that is the trap. Check before you run, not after your robot starts acting strange.
2. **Do not stall the motors.** Holding the wheels by hand, or letting the robot push against a wall, drives current toward stall and can cause **thermal damage to the windings in seconds.** If your robot is pushing and not moving, cut power.
3. **Never mix chemistries and never mix charge levels** in one robot. Four cells from the same pack, charged together.

**About alkalines:** they are allowed, and they are honestly worse for this course. Alkaline is 6.0 V nominal, so a fresh set is slightly faster — but alkaline voltage **slides downhill the whole time you use it,** while NiMH holds a flat plateau and then drops. *The robot you tuned in first period is not the robot you get in seventh.* You will meet this exact physics again in Lesson 11, "Time Lies, Distance Doesn't."

**Charging:** you charge your own batteries, on your own time, with the BQ-CC17 charger issued in your case. A charge takes _[HOW LONG TBD]_ — plan backwards from that. Charged batteries are part of your Materials grade. Coming to class with a dead robot is coming to class without your robot.

---

## Outside Class

Class time alone won't get you through your milestones — plan on some outside work. The lab is open **Monday–Thursday, 7:00–9:30 PM**, plus your free periods. Log your outside sessions in your notebook (date, time in/out, what you worked on) — that log is your Outside Work grade.

---

## In the Lab

**Your robot is yours.** It is numbered and assigned to you. You do not borrow someone else's robot, and you do not lend yours. If a robot is damaged, tell Mr. Weymuth the same day — a damaged robot reported is a repair; a damaged robot discovered is a problem.

**Your case is yours too.** You are issued one clearly marked Zumo carrying case holding:

- One USB-C–to–Micro-USB cable — this is your **programming** cable
- One Panasonic **BQ-CC17** charger, which plugs into the wall
- Four **Eneloop Pro by Panasonic** — NiMH AA cells

**The cable and the charger do different jobs, and this catches people out.** **The Zumo does not charge over USB.** There is no charging circuit on the board — the USB cable carries your program to the robot and powers the electronics while it is plugged in, and that is all it does. It never puts anything back into the cells. To charge, the batteries come **out** of the robot and go into the BQ-CC17. Leave a Zumo plugged into your laptop overnight and you get four flat cells in the morning, not a charged robot.

Everything issued to you lives in that case. Do not borrow from someone else's case or lend out of yours — a charger that walks off is two students who cannot run next period. Missing and dead equipment gets reported the same day, same rule as the robot.

**You charge your own batteries, on your own time.** Bring all four charged. Class and open lab are for building and testing, not for waiting on a charger.

**Shared tools go back.** Screwdrivers, tape, chargers, and course tape live in one place and return there before you leave. The last five minutes of every period are cleanup — not one more test run.

**The floor is the test surface.** Robots run on the course, on the floor, or on a bench with a barrier. **Never on an open table edge.** A Zumo at speed cannot stop before a drop — there is no software fix for this, only a physical barrier. This is not a suggestion. **Stop the robot before you reach for it**, move it, or put your hands near the wheels.

**Food and drink stay away from robots, batteries, chargers, and laptops.**

**Open lab is a work session, not a hangout.** Sign in, log your time in your notebook, clean up, sign out.

**Before you leave, every time:**
- ☐ Robot stopped and powered down
- ☐ Shared tools and course pieces returned
- ☐ Cable, charger, and all four batteries back in your case
- ☐ Case marking checked — it is yours
- ☐ Work area and course clear — chairs in, laptops closed
- ☐ Robot back on the shelf
- ☐ Case goes home with you, so the batteries are charged for next class

---

## Whose Code Is It? — Academic Honesty

This is a **solo build.** Every robot on the shelf runs code its owner wrote. That is the whole point — the milestone demo proves *you* can do the thing. It is not silent work, though: engineers ask questions and compare results, and you are expected to do that here.

**Encouraged:**
- Talking through a problem with another student at the whiteboard
- Comparing behavior: *"my robot wobbles on left turns, does yours?"*
- Helping someone read an error message, or decide what to test next
- Telling someone **where** to look: *"check your TRIM sign"*

**Not allowed:**
- Copying code from another student's screen, file, message, or repo — in either direction
- Handing your file to someone "just to look at"
- Typing the fix on someone else's keyboard
- Submitting a milestone demo of a robot running code you did not write

**The line:** you may explain *how* something works. You may not supply the *what to type.* Help someone find the answer; do not hand them the answer. After the conversation, both of you should be able to walk back to your own machine and write it yourselves.

**The test:** if you can explain your own code line by line when asked, you are fine. If you cannot, you are not — regardless of who typed it.

### AI Tools

**Use the course tutor.** It knows this robot. A general chatbot does not know your Zumo has 75:1 gearmotors, a 21×8 OLED, or that pins 20 and 4 are shared — so it invents plausible code that does not exist.

**Turn off inline autocomplete for this project.** Command Palette → **"Disable AI Features (Workspace)."** This switches it off for your Zumo folder only; everything else on your machine is unaffected.

Autocomplete is a different problem from a chatbot: it **inserts code without being asked.** Real things it has injected into this exact project:

- `setMotorPower()` — does not exist. The real function is `setSpeeds()`.
- `set motorSpeed()` — invented, with a space in the name.
- `pololu/Zumo32U4@^1.3.0` in `platformio.ini` — wrong version. The correct pin is `pololu/Zumo32U4@2.0.1`. It breaks the build in a way that looks like *your* mistake.

**AI is a tool, not an author.** Use it to explain a concept, translate an error, or help you design a test — not to produce a finished milestone you paste in. You own every line in your project, including the ones something else suggested. Before you keep a suggestion, you must be able to:

- Say what it does
- Say why it belongs where you put it
- Test whether it actually works on your robot
- Repair it or rip it out when it fails

**If AI helped you, say so in your notebook** — one line: what you asked, what you kept, what you threw out. Documenting a tool you used is engineering. Hiding it is not.

---

## Day One — What You Leave With

By the end of the first period you should have all of these. Check them off:

**Hardware — your robot and your case**
- ☐ Zumo 32U4 robot, numbered and assigned to you
- ☐ Marked Zumo carrying case, assigned to you
- ☐ One USB-C–to–Micro-USB cable (programming)
- ☐ One Panasonic BQ-CC17 charger (wall)
- ☐ Four Eneloop Pro by Panasonic NiMH AA cells
- ☐ Every issued item accounted for and stored in your own case

**Software**
- ☐ VS Code installed
- ☐ Git installed
- ☐ PlatformIO extension installed
- ☐ **AI autocomplete disabled for this workspace** (Command Palette → "Disable AI Features (Workspace)")
- ☐ Test upload completed — a program compiled and sent to the robot

**Accounts & documents**
- ☐ Canvas course opened; you can find the readings and the quizzes
- ☐ Textbook bookmarked: **weymuth.github.io/zumo**
- ☐ Project Maker bookmarked
- ☐ **Your own copy of the TDP notebook made** (File → Make a copy), named with your name, saved in your Drive
- ☐ That copy shared with Mr. Weymuth

**Preflight — the four things to check every time your robot misbehaves**
- ☐ Power switch is ON
- ☐ All four batteries installed and charged
- ☐ USB cable is fully seated at both ends
- ☐ You uploaded the program you think you uploaded

Do not start a build with a setup item missing and hope it sorts itself out. Fix the setup first — then the behavior you are looking at belongs to the lesson, not to a flat battery or a half-finished install.

---

## Where to Find Things

- **Canvas** — readings, quizzes, milestone descriptions, submissions
- **The Textbook** — weymuth.github.io/zumo
- **The Project Maker** — starting code for each lesson _[link TBD]_
- **Mr. Weymuth** — in the lab or by email. Ask early, not the night before a milestone.

---

## Still To Add _[working notes — not student-facing yet]_
- Exact milestone due dates (pin to real calendar — blocked until ~Aug 24)
- Notebook template Google Doc link
- Battery charge time on the BQ-CC17 (location resolved: students charge at home)
- Late-milestone penalty amount

---
*Robotics · Zumo 32U4 · Mercersburg Academy · Fall Trimester · working draft v1.1*
