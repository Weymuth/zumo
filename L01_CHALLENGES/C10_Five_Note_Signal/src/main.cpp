/*
=====================================================
LESSON 01 - Hello Robot — Challenge 10: Your Five-Note Signal
=====================================================
WHAT THIS PROGRAM DOES:
(update this as you build!)
AUTHOR: DJ Weymuth
DATE: 7/19/2026
=====================================================
*/

#include <Zumo32U4.h>

// ┌─────────────────────────────────────────────────────────┐
// │ CHALLENGE 10 — YOUR FIVE-NOTE SIGNAL             [HARD] │
// ├─────────────────────────────────────────────────────────┤
// │                                                         │
// │ Section 9 told you how John Williams and Steven         │
// │ Spielberg found five notes out of 134,000 -- and that   │
// │ the phrase is left hanging on the fifth note, like a    │
// │ question waiting for an answer.                         │
// │                                                         │
// │ Now write yours.                                        │
// │                                                         │
// │ ── YOUR TURN ──                                         │
// │ Five notes. Not a tune -- a MESSAGE. Pick one and make  │
// │ the notes fit it:                                       │
// │                                                         │
// │     "I am awake"          "I am done"                   │
// │     "Something is wrong"  "I found it"                  │
// │     "Are you there?"                                    │
// │                                                         │
// │ MY MESSAGE IS: _______________________________          │
// │                                                         │
// │ Sketch it BEFORE you type it:                           │
// │     note 1: ____ Hz     note 4: ____ Hz                 │
// │     note 2: ____ Hz     note 5: ____ Hz                 │
// │     note 3: ____ Hz                                     │
// │                                                         │
// │ Frequencies to choose from:                             │
// │     C4 262   D4 294   E4 330   F4 349                   │
// │     G4 392   A4 440   B4 494                            │
// │     C5 523   D5 587   E5 659   F5 698                   │
// │     G5 784   A5 880   B5 988   C6 1047                  │
// │                                                         │
// │ (Full chart, plus how to use note NAMES instead of      │
// │ numbers, is in the Quick Reference at the end of        │
// │ Lesson 1.)                                              │
// │                                                         │
// │ ── WHERE TO WRITE IT ──                                 │
// │ Find  <<< CHALLENGE 10  below. Replace the three        │
// │ victory-jingle notes with your five.                    │
// │                                                         │
// │ Each note needs TWO lines -- play it, then wait:        │
// │                                                         │
// │     buzzer.playFrequency(392, 200, 15);                 │
// │     delay(250);                                         │
// │                                                         │
// │ Without the delay, all five fire at once and you hear   │
// │ one noise. The silence between notes is part of the     │
// │ music.                                                  │
// │                                                         │
// │ ── WANT TO HEAR THE REAL ONE? ──                        │
// │ The Devil's Tower sequence, in order:                   │
// │                                                         │
// │     G4 392   A4 440   F4 349   F3 175   C4 262          │
// │                                                         │
// │ Type it in and listen before you write your own. Yes,   │
// │ your robot can play it -- all five notes are in range.  │
// │                                                         │
// │ TEST: play yours for somebody WITHOUT telling them the  │
// │ message. Ask what they think the robot is saying.       │
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
    // <<< CHALLENGE 10: YOUR FIVE-NOTE SIGNAL GOES HERE
    // Replace these three notes with your five.
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
