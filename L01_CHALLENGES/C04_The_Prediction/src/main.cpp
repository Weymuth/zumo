/*
=====================================================
LESSON 01 - Hello Robot — Challenge 4: The Prediction
=====================================================
WHAT THIS PROGRAM DOES:
(update this as you build!)
AUTHOR: DJ Weymuth
DATE: 7/19/2026
=====================================================
*/

#include <Zumo32U4.h>

// ┌─────────────────────────────────────────────────────────┐
// │ CHALLENGE 4 — THE PREDICTION                     [EASY] │
// ├─────────────────────────────────────────────────────────┤
// │                                                         │
// │ This one is about thinking BEFORE you upload. That is   │
// │ the whole exercise -- the code change takes 4 seconds.  │
// │                                                         │
// │ ⚠️ WRITE YOUR PREDICTION FIRST. No peeking by uploading. │
// │                                                         │
// │ You are going to change the FIRST delay(350) in the     │
// │ drive section to delay(700).                            │
// │                                                         │
// │ WHAT DO YOU EXPECT? (write it before you touch the code)│
// │                                                         │
// │   The robot will: ____________________________________  │
// │                                                         │
// │   ____________________________________________________  │
// │                                                         │
// │   Will it end up where it started?  YES / NO            │
// │   Why? ______________________________________________   │
// │                                                         │
// │ NOW DO IT. Find  <<< CHALLENGE 4  below and change      │
// │ that 350 to 700.                                        │
// │                                                         │
// │ TEST on the floor, not in the air. Wheels in the air    │
// │ spin freely and tell you nothing about distance.        │
// │                                                         │
// │ WHAT ACTUALLY HAPPENED?                                 │
// │                                                         │
// │   ____________________________________________________  │
// │                                                         │
// │ Did your prediction match? If it did, that is           │
// │ engineering intuition forming. If it did not, you just  │
// │ learned something the easy way -- for free, with no     │
// │ broken robot.                                           │
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
    delay(350);                   // <<< CHALLENGE 4: change to 700
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
