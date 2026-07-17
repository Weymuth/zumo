# ZUMO — L03 Challenge Templates + Solutions (STAGING)

> **⚠️ STAGING — NOT YET MAKER-GATED.** These are learner-mode reconstructions from Session 47, built for teaching. They are **not** yet verified against the Maker's `mainCpp()` wrapper or run through `gate_payload_match.py`. Before they become live Maker payloads they need the payload-body treatment:
> - The wrapper AUTO-PREPENDS the banner + `#include <Zumo32U4.h>` + the MY PLAN block. So a stored **payload body starts at `// ===== HARDWARE OBJECTS =====`** and EXCLUDES the header shown here. (Bible §18.3.)
> - Gate-check each against its lesson source at save.
> - **Chat-display rule (Bible §18.3):** when SHOWING a starter to DJ, PREPEND the wrapper header so what DJ sees matches the generated file. The full-file versions below already include the header for that reason.
>
> **Term:** "challenge template" (Bible §18.3 canon as of S48; retires "scaffold" for this sense).
> **Canon followed:** whole-template starters (Bible §18.3) — full 5-section scaffold, the ONE hardware object the concept needs pre-placed, concept blank in a marked landing zone, MY PLAN blank. TRIM on the LEFT motor (`setSpeeds(speed + TRIM, speed)`).
>
> **Payload note (corrected S49):** an L03 `finished` payload DOES exist in the Maker, so C01/C02/C05/C06 (payloadRef `finished`) and C03/C04 (payloadRef `constrain`/`ramp`) all emit valid code — the earlier "no finished payload" claim was wrong against the live file. **DJ ruling S49: C01–C06 stay finished-preload.** So this file is a **teaching/reference record** of all 8 challenges + solutions, not a payload-staging file. The two genuinely broken cards are **C07 and C08**, whose `payloadRef` is literally `"CHALLENGES"` (group name leaked into the ref slot) — a real defect to fix in a later Maker pass; their templates are recorded below for that work.

---

## Header the wrapper prepends (shown in each full template, EXCLUDED from stored payload body)

```cpp
/*
=====================================================
LESSON 03 - Motors & Movement — <challenge title>
=====================================================
WHAT THIS PROGRAM DOES:
(update this as you build!)
AUTHOR: LastName
DATE: <auto>
=====================================================
*/

#include <Zumo32U4.h>

// ==================== MY PLAN ====================
// Pseudo-code first, real code second.
// In plain English: what should this program do,
// step by step?
//
//   1.
//   2.
//   3.
//   4.
//
// Update the plan when your plan changes.
// =================================================
```

---

## C01 — Add a Spin Test

### Challenge Template (payload body — object pre-placed: `motors`)
```cpp
// ===== HARDWARE OBJECTS =====
Zumo32U4Motors motors;

// ===== CONSTANTS =====

// ===== FUNCTION PROTOTYPES =====
// DECLARE your functions here (name only, with a semicolon)

// ==== SETUP ====
void setup() {
  // write your code here
}

// ==== LOOP ====
void loop() {
}

// ===== HELPER FUNCTIONS =====
// DEFINE your functions here
```

### Solution
```cpp
// ===== HARDWARE OBJECTS =====
Zumo32U4Motors motors;

// ===== FUNCTION PROTOTYPES =====
void runSpinTest();

void setup() {
  runSpinTest();
}

void loop() {
}

// ===== HELPER FUNCTIONS =====
void runSpinTest() {
  motors.setSpeeds(150, -150);  // start the spin (opposite signs = spin in place)
  delay(1000);                  // let it run 1 second
  motors.setSpeeds(0, 0);       // stop
}
```

---

## C02 — Battery Warning System

### Challenge Template (object pre-placed: `display`)
```cpp
// ===== HARDWARE OBJECTS =====
Zumo32U4OLED display;

// ===== CONSTANTS =====

// ===== FUNCTION PROTOTYPES =====
// DECLARE your functions here (name only, with a semicolon)

// ==== SETUP ====
void setup() {
}

// ==== LOOP ====
void loop() {
  // write your code here
}

// ===== HELPER FUNCTIONS =====
// DEFINE your functions here
```

### Solution
```cpp
// ===== HARDWARE OBJECTS =====
Zumo32U4OLED display;

void setup() {
}

void loop() {
  int mv = readBatteryMillivolts();
  if (mv < 4200) {
    display.clear();
    display.gotoXY(0, 0);
    display.print(F("LOW BATT"));
    return;
  }
  // normal display would continue here
}
```

---

## C03 — Clamp the Speed with constrain()

### Challenge Template (objects pre-placed: `buttonA` for the safety gate, `motors`)
```cpp
// ===== HARDWARE OBJECTS =====
Zumo32U4ButtonA buttonA;
Zumo32U4Motors  motors;

// ===== CONSTANTS =====
// <-- YOUR NUMBERS go here

// ===== FUNCTION PROTOTYPES =====
// DECLARE your functions here (name only, with a semicolon)

// ==== SETUP ====
void setup() {
  buttonA.waitForButton();   // safety: nothing moves until you press A
  // write your code here
}

// ==== LOOP ====
void loop() {
}

// ===== HELPER FUNCTIONS =====
// DEFINE your functions here
```

### Solution
```cpp
// ===== HARDWARE OBJECTS =====
Zumo32U4ButtonA buttonA;
Zumo32U4Motors  motors;

// ===== CONSTANTS =====
const int LEFT_SPEED  = 150;   // try 150, then 200, then 250
const int RIGHT_SPEED = 150;
const int MAX_SPEED   = 200;   // the cap
const int RUN_MS      = 1000;  // how long to run before stopping

void setup() {
  buttonA.waitForButton();
  motors.setSpeeds(
    constrain(LEFT_SPEED,  -MAX_SPEED, MAX_SPEED),
    constrain(RIGHT_SPEED, -MAX_SPEED, MAX_SPEED)
  );
  delay(RUN_MS);
  motors.setSpeeds(0, 0);   // stop before the edge
}

void loop() {
}
```

---

## C04 — Ramp Up to Speed  (Ramp Option C: hand-unrolled, NO for-loop)

### Challenge Template (objects pre-placed: `buttonA`, `motors`)
```cpp
// ===== HARDWARE OBJECTS =====
Zumo32U4ButtonA buttonA;
Zumo32U4Motors  motors;

// ===== CONSTANTS =====
// <-- YOUR NUMBERS go here

// ===== FUNCTION PROTOTYPES =====
// DECLARE your functions here (name only, with a semicolon)

// ==== SETUP ====
void setup() {
  buttonA.waitForButton();   // safety: nothing moves until you press A
  // write your code here
}

// ==== LOOP ====
void loop() {
}

// ===== HELPER FUNCTIONS =====
// DEFINE your functions here
```

### Solution
```cpp
// ===== HARDWARE OBJECTS =====
Zumo32U4ButtonA buttonA;
Zumo32U4Motors  motors;

// ===== CONSTANTS =====
const int MAX_SPEED = 200;   // the top of the climb
const int STEP_MS   = 200;   // how long each rung holds

void setup() {
  buttonA.waitForButton();
  // hand-written climb, one rung at a time (no for-loop until L05):
  motors.setSpeeds(50,  50);                delay(STEP_MS);
  motors.setSpeeds(100, 100);               delay(STEP_MS);
  motors.setSpeeds(150, 150);               delay(STEP_MS);
  motors.setSpeeds(MAX_SPEED, MAX_SPEED);   delay(STEP_MS);  // stop at the cap — don't go past
  motors.setSpeeds(0, 0);
}

void loop() {
}
```

---

## C05 — Variable Speed Test  (hardest rung: array + index + modulo)

### Challenge Template (objects pre-placed: `buttonB`, `display`, `motors`; includes a GLOBAL VARIABLES section)
```cpp
// ===== HARDWARE OBJECTS =====
Zumo32U4ButtonB buttonB;
Zumo32U4OLED    display;
Zumo32U4Motors  motors;

// ===== CONSTANTS =====
// <-- YOUR ARRAY and count go here

// ===== GLOBAL VARIABLES =====
// <-- YOUR index variable goes here

// ===== FUNCTION PROTOTYPES =====
// DECLARE your functions here (name only, with a semicolon)

// ==== SETUP ====
void setup() {
}

// ==== LOOP ====
void loop() {
  // wait for a B press, then run the test at the current speed
  // write your code here
}

// ===== HELPER FUNCTIONS =====
// DEFINE your functions here
```

### Solution
```cpp
// ===== HARDWARE OBJECTS =====
Zumo32U4ButtonB buttonB;
Zumo32U4OLED    display;
Zumo32U4Motors  motors;

// ===== CONSTANTS =====
const int TEST_SPEEDS[] = {150, 200, 250, 300};
const int NUM_SPEEDS = 4;

// ===== GLOBAL VARIABLES =====
int speedIndex = 0;   // which slot we're on (slots are 0..3)

void setup() {
}

void loop() {
  if (buttonB.getSingleDebouncedPress()) {
    int currentSpeed = TEST_SPEEDS[speedIndex];   // read the array at the current slot
    display.clear();
    display.print(currentSpeed);
    motors.setSpeeds(currentSpeed, currentSpeed);
    delay(1000);
    motors.setSpeeds(0, 0);
    speedIndex = (speedIndex + 1) % NUM_SPEEDS;   // advance, wrap 3 -> 0
  }
}
```

---

## C06 — Save TRIM to Code

### Challenge Template (object pre-placed: `motors`; TRIM-finder skeleton present so there's a `trimValue` to save)
```cpp
// ===== HARDWARE OBJECTS =====
Zumo32U4Motors motors;

// ===== CONSTANTS =====
// <-- YOUR saved TRIM value goes here

// ===== GLOBAL VARIABLES =====
int trimValue = 0;   // <-- change this so it STARTS from your saved value

// ===== FUNCTION PROTOTYPES =====
// DECLARE your functions here (name only, with a semicolon)

// ==== SETUP ====
void setup() {
  // drive straight using trimValue (the TRIM goes on the LEFT motor)
  motors.setSpeeds(200 + trimValue, 200);
  delay(2000);
  motors.setSpeeds(0, 0);
}

// ==== LOOP ====
void loop() {
}

// ===== HELPER FUNCTIONS =====
// DEFINE your functions here
```

### Solution
```cpp
// ===== HARDWARE OBJECTS =====
Zumo32U4Motors motors;

// ===== CONSTANTS =====
const int MY_TRIM = 15;   // your bench-found value

// ===== GLOBAL VARIABLES =====
int trimValue = MY_TRIM;   // boot with the saved value already set

void setup() {
  motors.setSpeeds(200 + trimValue, 200);
  delay(2000);
  motors.setSpeeds(0, 0);
}

void loop() {
}
```

## C07 — Drive a Square

### Challenge Template (object pre-placed: `motors`; uses the LEFT-motor TRIM convention on the straights)
```cpp
// ===== HARDWARE OBJECTS =====
Zumo32U4Motors motors;

// ===== CONSTANTS =====
const int DRIVE_SPEED = 200;
const int TURN_SPEED  = 150;
const int DRIVE_TIME  = 1000;   // ms per side  <-- YOUR NUMBER
const int TURN_TIME   = 350;    // ms per 90° turn  <-- YOUR NUMBER (adjust!)

// ===== GLOBAL VARIABLES =====
int trimValue = 0;   // <-- your bench-found TRIM

// ===== FUNCTION PROTOTYPES =====
// DECLARE driveSquare() here (name only, with a semicolon)

// ==== SETUP ====
void setup() {
  // write your code here: call driveSquare() once
}

// ==== LOOP ====
void loop() {
}

// ===== HELPER FUNCTIONS =====
// DEFINE driveSquare() here:
//   repeat 4 times { drive forward one side, stop, turn right 90°, stop }
//   TRIM goes on the LEFT motor for the straight; the turn opposes the wheels.
```

### Solution
```cpp
// ===== HARDWARE OBJECTS =====
Zumo32U4Motors motors;

int trimValue = 0;

void driveSquare() {
  const int DRIVE_SPEED = 200;
  const int TURN_SPEED  = 150;
  const int DRIVE_TIME  = 1000;
  const int TURN_TIME   = 350;   // Adjust for 90°!
  for (int side = 0; side < 4; side++) {
    // Drive forward with TRIM (LEFT motor)
    motors.setSpeeds(DRIVE_SPEED + trimValue, DRIVE_SPEED);
    delay(DRIVE_TIME);
    motors.setSpeeds(0, 0);
    delay(200);
    // Turn right: left forward, right backward
    motors.setSpeeds(TURN_SPEED, -TURN_SPEED);
    delay(TURN_TIME);
    motors.setSpeeds(0, 0);
    delay(200);
  }
}

void setup() {
  driveSquare();
}

void loop() {
}
```
> Motor convention confirmed: `setSpeeds(TURN_SPEED, -TURN_SPEED)` = left forward + right backward = turn right. Calibrate ONE 90° turn first, then build up to the full square. Timing-based turns compound error (5°×4 = 20° drift) — Lesson 6 fixes this with encoders.

---

## C08 — Auto-TRIM Preview  (research/pseudocode — no runnable concept, comments only)

### Challenge Template (object pre-placed: `motors`; deliverable is a commented algorithm, not new behavior)
```cpp
// ===== HARDWARE OBJECTS =====
Zumo32U4Motors motors;

// ===== CONSTANTS =====
// (none needed for this challenge)

// ===== GLOBAL VARIABLES =====
int trimValue = 0;

// ===== FUNCTION PROTOTYPES =====
// (none needed — the deliverable is a comment block, no new function is called)

// ==== SETUP ====
void setup() {
  // your working TRIM Finder can stay here
}

// ==== LOOP ====
void loop() {
}

// ===== HELPER FUNCTIONS =====
// write your AUTO-TRIM ALGORITHM here as a /* ... */ comment block.
// Describe the steps — do NOT implement it (encoders come in Lesson 6).
```

### Solution
```cpp
// ===== HARDWARE OBJECTS =====
Zumo32U4Motors motors;

int trimValue = 0;

/*
AUTO-TRIM ALGORITHM (Preview of Lesson 6)
-------------------------------------------
1. Reset both encoder counts to 0
2. Run both motors at same speed for 2 seconds
3. Read encoder counts: leftCount, rightCount
4. If leftCount > rightCount:
   - Left wheel turned more = robot curved right
   - Need to slow left OR speed up right
   - difference = leftCount - rightCount
   - TRIM = -1 * (difference / totalCount) * BASE_SPEED
5. If rightCount > leftCount:
   - Right wheel turned more = robot curved left
   - Need to slow right OR speed up left
   - TRIM = +1 * (difference / totalCount) * BASE_SPEED
6. Apply TRIM and test again
7. Repeat until leftCount ≈ rightCount

This is CLOSED-LOOP control — we implement it in Lesson 6.
*/

void setup() {
}

void loop() {
}
```
> Where it goes: paste the comment block right after `runMotorTest()`, above `setup()` — helpers defined above `setup` need no prototype. The deliverable is the well-commented algorithm, not running code.

---

---
*L03 Challenge Templates + solutions · all 8 challenges (C07/C08 added S49) · reference record, not Maker-gated · see ZUMO_LEARNMODE_L03.md for the teaching detail*
