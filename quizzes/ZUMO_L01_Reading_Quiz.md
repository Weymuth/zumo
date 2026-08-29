# Lesson 1 Reading Quiz — Hello, Robot!
### Fall 2026 · D Block · closes when class starts **Wednesday September 9, 9:50 AM**
<!-- ZUMO_L01_Reading_Quiz.md v1.0 — S194. The eight selected questions, keyed. The importable
     QTI package is built from these same eight and is NOT committed (a binary zip in the repo
     drifts silently from the bank); regenerate it when the selection changes. -->

> **Fallback copy.** The importable package is `ZUMO_L01_Reading_Quiz_CANVAS_QTI.zip`. If Canvas
> refuses the import, build the quiz by hand from this page — the correct answer is marked **✅**.
> **One attempt, auto-graded, 8 points.** This is a gate, not an exam.

**Why these eight.** Two of them — Q7 and Q8 — cannot be answered by a student who read the lesson
but never opened PlatformIO or plugged the robot in. That is deliberate: Assignment 1 ends with a
program running on the robot, and the quiz has to be able to tell.

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

### 7. PlatformIO creates several folders. Which one holds the program you actually work in?
*Source: §6 Step 1 · bank id `L01_B43` · 1 point*

- **✅ src — main.cpp lives here**
- include — for your own header files, empty for now
- lib — for project-private libraries
- .pio — the compiler's private workspace

### 8. Upload fails with "could not open port … Resource busy." What is holding it?
*Source: §7.2 · bank id `L01_B48` · 1 point*

- **✅ The Serial Monitor — only one program can use the port at a time, so stop the monitor and upload again**
- The bootloader, which never released the port after the last upload
- The robot's own program, which must be stopped with the reset button
- A power-only USB cable

---

## Building it by hand in Canvas

1. **Quizzes → + Quiz → Classic Quizzes** (the QTI package imports as a Classic quiz).
2. **Settings:** 1 attempt · shuffle answers ON · show correct answers **after the due date**, not immediately.
3. **Available until Wed Sep 9, 9:50 AM** — the syllabus says the quiz closes when class starts, and that promise only holds if this field is set.
4. Add each question as **Multiple Choice**, 1 point, and paste the text above.

## If you want to swap a question

The full L01 bank is `quizzes/ZUMO_QUIZ_L01.yaml` — **79 questions, 60 of which cite §1–§7.**
Keep at least one from §6 or §7 so the quiz cannot be passed without having plugged in.

---
*Generated from the L01 bank · S194 · Fall Term 2026*
