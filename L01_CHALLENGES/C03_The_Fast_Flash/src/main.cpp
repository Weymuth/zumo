/*
=====================================================
LESSON 01 - Hello Robot — Challenge 3: The Fast Flash
=====================================================
WHAT THIS PROGRAM DOES:
(update this as you build!)
AUTHOR: DJ Weymuth
DATE: 7/19/2026
=====================================================
*/

#include <Zumo32U4.h>

// ┌─────────────────────────────────────────────────────────┐
// │ CHALLENGE 3 — THE FAST FLASH                     [EASY] │
// ├─────────────────────────────────────────────────────────┤
// │                                                         │
// │ GOAL: make the yellow LED blink exactly 10 times, at    │
// │ TWICE the speed of the original.                        │
// │                                                         │
// │ Find  <<< CHALLENGE 3  below. TWO numbers change.       │
// │                                                         │
// │ 1) THE COUNT. The loop currently reads:                 │
// │                                                         │
// │        for (int i = 0; i < 3; i++)                      │
// │                                                         │
// │    That 3 is how many times it repeats. Section 5       │
// │    walked through all three parts of that line -- go    │
// │    back and reread it if the pieces are fuzzy.          │
// │                                                         │
// │ 2) THE SPEED. Inside the loop are two delay(200) calls  │
// │    -- one with the light on, one with it off. Cut BOTH  │
// │    in half.                                             │
// │                                                         │
// │    Smaller delay = faster blink. Change only one and    │
// │    you get a limp: on-fast, off-slow.                   │
// │                                                         │
// │ PREDICT BEFORE YOU UPLOAD:                              │
// │     How long will the whole blink take now? ______ ms   │
// │     (Count it up: 10 blinks x how many ms each?)        │
// │                                                         │
// │ TEST: count the flashes. Exactly 10, twice as quick.    │
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
    for (int i = 0; i < 3; i++) {      // <<< CHALLENGE 3: the count
        ledYellow(1);
        delay(200);                    // <<< CHALLENGE 3: light-on time
        ledYellow(0);
        delay(200);                    // <<< CHALLENGE 3: light-off time
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
