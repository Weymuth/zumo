/*
=====================================================
LESSON 01 - Hello Robot — Challenge 5: Two Places at Once
=====================================================
WHAT THIS PROGRAM DOES:
(update this as you build!)
AUTHOR: Dj
DATE: 7/19/2026
=====================================================
*/

#include <Zumo32U4.h>

// ┌─────────────────────────────────────────────────────────┐
// │ CHALLENGE 5 — TWO PLACES AT ONCE               [MEDIUM] │
// ├─────────────────────────────────────────────────────────┤
// │                                                         │
// │ GOAL: make the robot report the SAME message twice --   │
// │ once to the OLED, once to the Serial Monitor, at the    │
// │ same moment. Print "Test starting" to both.             │
// │                                                         │
// │ Find  <<< CHALLENGE 5  below -- right after the button  │
// │ press is detected. Add THREE lines there:               │
// │                                                         │
// │     display.clear();                                    │
// │     display.print("Test starting");                     │
// │     Serial.println("Test starting");                    │
// │                                                         │
// │ TEST: watch both at once. Screen and monitor say the    │
// │ same thing at the same instant.                         │
// │                                                         │
// │ ── WHY THIS MATTERS LATER ──                            │
// │ Two audiences, two devices, one truth. The display      │
// │ talks to whoever is standing next to the robot. The     │
// │ Serial Monitor talks to your computer.                  │
// │                                                         │
// │ Every debugging session for the rest of this course is  │
// │ a choice between those two. From Lesson 11 on, your     │
// │ robot runs untethered on the floor, and the OLED is     │
// │ the only one of the two you can still read.             │
// │                                                         │
// │     Which one would you trust more? _________________   │
// │     Why? ____________________________________________   │
// │                                                         │
// │     Why might the Serial Monitor be a challenge         │
// │     at that point? __________________________________   │
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

    // <<< CHALLENGE 5: YOUR THREE LINES GO HERE

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
