/*
=====================================================
LESSON 01 - Hello Robot — Challenge 2: Change the Beep
=====================================================
WHAT THIS PROGRAM DOES:
(update this as you build!)
AUTHOR: DJ Weymuth
DATE: 7/19/2026
=====================================================
*/

#include <Zumo32U4.h>

// ┌─────────────────────────────────────────────────────────┐
// │ CHALLENGE 2 — CHANGE THE BEEP                    [EASY] │
// ├─────────────────────────────────────────────────────────┤
// │                                                         │
// │ Section 5 told you about Jim Reekes, who risked his job │
// │ over two seconds of sound. Your turn.                   │
// │                                                         │
// │ Find  <<< CHALLENGE 2  below and change 440 to a note   │
// │ you pick. The first number is the FREQUENCY in Hertz.   │
// │ Bigger number, higher note. Double it, and you go up    │
// │ exactly one octave.                                     │
// │                                                         │
// │     262 = C4    (an octave below the original)          │
// │     440 = A4    (the original -- orchestras tune to it) │
// │     880 = A5    (exactly double 440 -- one octave up)   │
// │                                                         │
// │ More notes are in the Quick Reference at the end of     │
// │ Lesson 1 -- two full octaves, C4 up to C6.              │
// │                                                         │
// │ WRITE DOWN WHAT YOU PICKED:                             │
// │     My frequency: ______ Hz                             │
// │     Higher or lower than 440? ______                    │
// │                                                         │
// │ TEST: upload, press A. The beep changes pitch.          │
// │                                                         │
// │ NOTE: this file holds the beep for 800 ms -- the main    │
// │ Lesson 1 program uses 200 ms, which is so short it gets  │
// │ lost under the LED blinking that follows. You need to    │
// │ HEAR your change, so here it rings longer.               │
// │                                                         │
// │ The second number is the DURATION, in milliseconds.      │
// │ See the playFrequency diagram in Section 5.              │
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
    buzzer.playFrequency(440, 800, 15);   // <<< CHALLENGE 2: change 440
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
