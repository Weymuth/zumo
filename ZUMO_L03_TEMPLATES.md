# ZUMO — L03 Code Templates + Solutions (STAGING)

> **⚠️ STAGING — NOT YET MAKER-GATED.** These are learner-mode reconstructions from Session 47, built for teaching. They are **not** yet verified against the Maker's `mainCpp()` wrapper or run through `gate_payload_match.py`. Before they become live Maker payloads they need the payload-body treatment:
> - The wrapper AUTO-PREPENDS the banner + `#include <Zumo32U4.h>` + the MY PLAN block. So a stored **payload body starts at `// ===== HARDWARE OBJECTS =====`** and EXCLUDES the header shown here. (Bible §18.3.)
> - Gate-check each against its lesson source at save.
> - **Chat-display rule (Bible §18.3):** when SHOWING a starter to DJ, PREPEND the wrapper header so what DJ sees matches the generated file. The full-file versions below already include the header for that reason.
>
> **Term:** "Code Template" (DJ's preferred term; retires "scaffold").
> **Canon followed:** whole-template starters (Bible §18.3) — full 5-section scaffold, the ONE hardware object the concept needs pre-placed, concept blank in a marked landing zone, MY PLAN blank. TRIM on the LEFT motor (`setSpeeds(speed + TRIM, speed)`).
>
> **Reversal-debt note:** the LIVE cards for C01/C05/C06 link to `?lesson=3&kind=...` with `payloadRef=finished`, but **no L03 `finished` payload exists**, so the Maker currently emits a blank scaffold and the card text ("preloaded with the finished lesson program") is wrong. These templates are the intended replacement.

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

### Code Template (payload body — object pre-placed: `motors`)
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

### Code Template (object pre-placed: `display`)
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

### Code Template (objects pre-placed: `buttonA` for the safety gate, `motors`)
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

### Code Template (objects pre-placed: `buttonA`, `motors`)
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

### Code Template (objects pre-placed: `buttonB`, `display`, `motors`; includes a GLOBAL VARIABLES section)
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

### Code Template (object pre-placed: `motors`; TRIM-finder skeleton present so there's a `trimValue` to save)
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

---
*L03 Code Templates + solutions · Session 47 · STAGING, not Maker-gated · see ZUMO_LEARNMODE_L03.md for the teaching detail*
