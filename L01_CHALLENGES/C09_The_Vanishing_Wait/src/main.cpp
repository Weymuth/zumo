/*
=====================================================
LESSON 01 - Hello Robot — Challenge 9: The Vanishing Wait
=====================================================
WHAT THIS PROGRAM DOES:
(update this as you build!)
AUTHOR: DJ Weymuth
DATE: 7/19/2026
=====================================================
*/

#include <Zumo32U4.h>

// ┌─────────────────────────────────────────────────────────┐
// │ CHALLENGE 9 — THE VANISHING WAIT               [MEDIUM] │
// ├─────────────────────────────────────────────────────────┤
// │                                                         │
// │ Think it through, THEN test.                            │
// │                                                         │
// │ What would happen if you deleted the entire button      │
// │ wait -- these three lines?                              │
// │                                                         │
// │     while (!buttonA.getSingleDebouncedPress()) {        │
// │         delay(10);                                      │
// │     }                                                   │
// │                                                         │
// │ ⚠️ WRITE YOUR ANSWER BEFORE YOU DELETE ANYTHING:         │
// │                                                         │
// │   I think the robot will: ____________________________  │
// │                                                         │
// │   ____________________________________________________  │
// │                                                         │
// │ NOW DELETE THEM. Find  <<< CHALLENGE 9  below and       │
// │ remove all three lines. Upload.                         │
// │                                                         │
// │ ⚠️ PUT THE ROBOT ON THE FLOOR FIRST. You are about to    │
// │ remove the only thing standing between "upload          │
// │ finished" and "the motors run." It will not wait for    │
// │ you to be ready.                                        │
// │                                                         │
// │ WHAT ACTUALLY HAPPENED?                                 │
// │                                                         │
// │   ____________________________________________________  │
// │                                                         │
// │ ── WHY THE WAIT EXISTS ──                               │
// │ The show now starts the instant the robot powers on or  │
// │ resets. No warning. That is exactly why the wait is     │
// │ there: it buys you time to put the robot down, get      │
// │ your hands clear, and open the Serial Monitor before    │
// │ anything moves.                                         │
// │                                                         │
// │ You just proved the while-loop trapdoor from Section 5  │
// │ by REMOVING the trapdoor. That is a legitimate way to   │
// │ understand a piece of code: take it out and watch what  │
// │ breaks.                                                 │
// │                                                         │
// │ ⚠️ PUT THE THREE LINES BACK when you are done. Every     │
// │ program you write from here on starts with a wait like  │
// │ this one -- by Lesson 4 it has a name, waitForStart(),  │
// │ and it is a safety rule, not a convenience.             │
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
    // <<< CHALLENGE 9: delete these three lines
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
