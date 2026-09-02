# Lesson 1 Reading Quiz — Hello, Robot!
### Fall 2026 · D Block · closes when class starts **Wednesday September 9, 9:50 AM**

> **Fallback copy.** The importable package is `ZUMO_L01_Reading_Quiz_CANVAS_QTI.zip`. If Canvas
> refuses the import, build the quiz by hand from this page — the correct answer is marked **✅**.
> **One attempt, auto-graded, 8 points.** This is a gate, not an exam.

**Why these eight.** Every one of them is answerable from the assigned reading, §1–§5, and none of
them needs the robot. **Ruled S199: this quiz is over the reading, not the build.** Building,
uploading and the challenges are class work — §6, §7 and §9 are Wednesday's 65 minutes, so nothing
here draws on them. Q8 is the can't-skim question: it asks the student to trace a loop rather than
recognise a sentence.

---

### 1. What are the three steps of the robot cycle, in order?
*Source: §3 · bank id `L01_B04` · 1 point*

- **✅ SENSE, DECIDE, ACT**
- DECIDE, SENSE, ACT
- SENSE, ACT, DECIDE
- ACT, SENSE, DECIDE

### 2. What makes a line-following Zumo closed-loop rather than open-loop?
*Source: §3 · bank id `L01_B10` · 1 point*

- **✅ It acts, senses the result, and adjusts — it notices when it has drifted off center and steers back**
- It runs its instructions in a loop() function rather than once
- It follows a longer list of instructions than an open-loop machine
- It has more sensors than an open-loop machine

### 3. Why does this course have you install Git?
*Source: §4.2 · bank id `L01_B37` · 1 point*

- **✅ PlatformIO expects it to be installed — and on a Mac, installing it is what brings in Apple's Command Line Tools, where the compiler lives**
- PlatformIO uses it to download the robot libraries
- You will use it to submit your work to Canvas
- It is the editor you write your code in

### 4. The lesson tells you to turn AI autocomplete OFF — not "use it carefully." What is the stated reason?
*Source: §4.3 · bank id `L01_B38` · 1 point*

- **✅ It invents functions that do not exist, routinely — it has produced setMotorPower() and set motorSpeed() for Zumo motor code, when the real one is setSpeeds()**
- It slows the editor down too much on school computers
- It costs money to use
- It is against school policy to use any AI in this course

### 5. `lib_deps = pololu/Zumo32U4@2.0.1` — what is the `@2.0.1` doing, and why does the lesson insist on it?
*Source: §5.0 · bank id `L01_B15` · 1 point*

- **✅ It is a version pin: without it the project quietly takes whatever was published most recently, and the robot you build in June stops matching the one you built in September**
- It tells PlatformIO how many times to retry the download
- It is the Zumo library's product number in Pololu's catalog
- It sets the minimum version, so anything newer is used automatically

### 6. How many times does each of the two functions run?
*Source: §5.3, §5.4 · bank id `L01_B21` · 1 point*

- **✅ setup() runs exactly once at power-on or reset; loop() runs forever afterward**
- setup() runs forever; loop() runs once
- Both run once, setup() first
- Both run forever, alternating

### 7. What does `#include <Zumo32U4.h>` actually do for your program?
*Source: §5.1 · bank id `L01_B17` · 1 point*

- **✅ It opens the Pololu library that lib_deps downloaded, pouring every Zumo command into your program**
- It downloads the Zumo library from the internet
- It connects your computer to the robot over USB
- It creates the motors, display and buzzer objects

### 8. Trace `for (int i = 0; i < 3; i++)`. How many times does the body run, and what ends it?
*Source: §5.5 · bank id `L01_B32` · 1 point*

- **✅ Three times; the loop ends when the counter reaches 3 and 3 < 3 is false**
- Four times, because the counter starts at 0
- Two times, because the counter stops one short
- Three times; the loop ends when the counter is reset to 0

---

## Building it by hand in Canvas

1. **Quizzes → + Quiz → Classic Quizzes** (the QTI package imports as a Classic quiz).
2. **Settings:** 1 attempt · shuffle answers ON · show correct answers **after the due date**, not immediately.
3. **Available until Wed Sep 9, 9:50 AM** — the syllabus says the quiz closes when class starts, and that promise only holds if this field is set.
4. Add each question as **Multiple Choice**, 1 point, and paste the text above.

## If you want to swap a question

The full L01 bank is `quizzes/ZUMO_QUIZ_L01.yaml` — 79 questions, of which **40 cite §1–§5 and
nothing else.** That is the pool. **Do not draw from §6, §7 or §9** — those are class work, not the
assigned reading, and a question from them tests something the assignment never asked for.

Three further questions mention a §1–§5 heading *and* something outside it (§8 once, the Quick
Reference twice). They are not in the 40 and should not be swapped in without reading them first.

---
*Generated from the L01 bank · S194, rescoped to §1–§5 at S199 · Fall Term 2026*
