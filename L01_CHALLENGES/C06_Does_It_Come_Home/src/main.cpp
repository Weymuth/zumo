/*
=====================================================
LESSON 01 - Hello Robot — Challenge 6: Does It Come Home?
=====================================================
WHAT THIS PROGRAM DOES:
(update this as you build!)
AUTHOR: DJ Weymuth
DATE: 7/19/2026
=====================================================
*/

#include <Zumo32U4.h>

// ┌─────────────────────────────────────────────────────────┐
// │ CHALLENGE 6 — DOES IT COME HOME?               [MEDIUM] │
// ├─────────────────────────────────────────────────────────┤
// │                                                         │
// │ ⚠️ THERE IS NO CODE TO CHANGE. That is the point.        │
// │                                                         │
// │ The drive section already sends the robot forward and   │
// │ then back by IDENTICAL numbers -- same speed, same      │
// │ delay, opposite signs. In theory it lands exactly       │
// │ where it started.                                       │
// │                                                         │
// │ WHAT TO DO:                                             │
// │   1. Put a strip of tape on the floor at the robot's    │
// │      FRONT EDGE.                                        │
// │   2. Press A. Let it drive out and back.                │
// │   3. Measure the gap between the tape and where the     │
// │      front edge actually ended up. In millimeters.      │
// │   4. Do it THREE times. Do not reposition between runs  │
// │      -- pick the robot up, put it back on the tape.     │
// │                                                         │
// │ MY MEASUREMENTS:                                        │
// │     Run 1 gap: ______ mm    (left / right / short / far)│
// │     Run 2 gap: ______ mm    (left / right / short / far)│
// │     Run 3 gap: ______ mm    (left / right / short / far)│
// │                                                         │
// │ Were the three runs the same? ______________________    │
// │                                                         │
// │ ── WHY IT DOES NOT COME HOME ──                         │
// │ Your two motors are not identical twins. The tracks     │
// │ grip differently. The battery sags a little as it       │
// │ works. "The same command" does not buy you "the same    │
// │ motion."                                                │
// │                                                         │
// │ Lesson 3 gives you a number called TRIM to correct the  │
// │ mismatched motors. Lesson 11 shows you why TIMED        │
// │ driving can never be fully trusted -- and what to count │
// │ instead.                                                │
// │                                                         │
// │ ⚠️ KEEP THESE NUMBERS. Put them in your engineering      │
// │ notebook. This is the first honest data your robot      │
// │ ever gave you, and you will want it in Lesson 3.        │
// └─────────────────────────────────────────────────────────┘
// ===== HARDWARE OBJECTS =====
Zumo32U4ButtonA buttonA;
Zumo32U4ButtonB buttonB;
Zumo32U4ButtonC buttonC;
Zumo32U4OLED display;
Zumo32U4Motors motors;
Zumo32U4Buzzer buzzer;

// ===== CONSTANTS =====
#include <EEPROM.h>
const int NAME_ADDR = 512;   // where your robot's name lives

// ===== GLOBAL VARIABLES =====
// (none needed for this challenge)

// ===== FUNCTION PROTOTYPES =====
// (none needed for this challenge)

void setup() {
    // ───── START SERIAL ─────
    Serial.begin(115200);

    // ───── SET UP THE DISPLAY ─────
    display.clear();
    display.setLayout21x8();
    display.print("Press A");

    // ───── 1. WAIT FOR THE BUTTON ─────
    while (!buttonA.getSingleDebouncedPress()) {
        delay(10);
    }

    // ───── 2. SAY HELLO ─────
    Serial.println("Hello, Robot!");

    // ───── WHO AM I? ─────
    Serial.print("Robot name: ");
    if (EEPROM.read(NAME_ADDR) == 0x5A) {
        for (int i = 0; i < 20; i++) {
            char c = EEPROM.read(NAME_ADDR + 1 + i);
            if (c == '\0') { break; }
            Serial.print(c);
        }
    } else {
        Serial.print("(unnamed -- see your teacher)");
    }
    Serial.println();

    // ───── 3. BEEP ─────
    buzzer.playFrequency(440, 800, 15);
    delay(900);

    // ───── 4. BLINK THE LED ─────
    for (int i = 0; i < 3; i++) {
        ledYellow(1);
        delay(200);
        ledYellow(0);
        delay(200);
    }

    // ───── 5. DRIVE: FORWARD, THEN BACK ─────
    display.clear();
    display.print("Moving!");
    motors.setSpeeds(200, 200);   // Forward
    delay(350);
    motors.setSpeeds(0, 0);       // Stop
    delay(200);
    motors.setSpeeds(-200, -200); // Backward
    delay(350);
    motors.setSpeeds(0, 0);       // Stop

    // ───── 6. VICTORY JINGLE ─────
    display.clear();
    display.print("Done!");
    buzzer.playFrequency(523, 100, 15);  // C5
    delay(150);
    buzzer.playFrequency(659, 100, 15);  // E5
    delay(150);
    buzzer.playFrequency(784, 300, 15);  // G5
}

void loop() {
    // Nothing here for Lesson 1
}

// ===== HELPER FUNCTIONS =====
// (none needed for this challenge)
