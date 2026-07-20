/*
=====================================================
LESSON 01 - Hello Robot — Challenge 7: The Siren
=====================================================
WHAT THIS PROGRAM DOES:
(update this as you build!)
AUTHOR: DJ Weymuth
DATE: 7/19/2026
=====================================================
*/

#include <Zumo32U4.h>

// ┌─────────────────────────────────────────────────────────┐
// │ CHALLENGE 7 — THE SIREN                        [MEDIUM] │
// ├─────────────────────────────────────────────────────────┤
// │                                                         │
// │ GOAL: before the robot moves, make it alternate between │
// │ a LOW tone and a HIGH tone, twice -- like a siren.      │
// │                                                         │
// │ ── WHERE TO WRITE IT ──                                 │
// │ Find the landing zone marked                            │
// │     <<< CHALLENGE 7: YOUR SIREN GOES HERE               │
// │ down in setup(), just before the drive section. Your    │
// │ code replaces that comment line.                        │
// │                                                         │
// │ You could write four playFrequency lines in a row. But  │
// │ you already know a way to say "do this twice" without   │
// │ typing it twice -- you have one right above, blinking   │
// │ the LED.                                                │
// │                                                         │
// │ THE SHAPE:                                              │
// │                                                         │
// │     for (int i = 0; i < 2; i++) {                       │
// │       buzzer.playFrequency(392, 200, 15);   // low      │
// │       delay(250);                                       │
// │       buzzer.playFrequency(784, 200, 15);   // high     │
// │       delay(250);                                       │
// │     }                                                   │
// │                                                         │
// │ ⚠️ Each note needs a delay AFTER it. The buzzer starts   │
// │ the note and your program keeps running -- without the  │
// │ delay, the next note interrupts the one before it and   │
// │ you hear one short blip instead of four notes.          │
// │                                                         │
// │ NOTICE: 784 is exactly double 392. One octave apart --  │
// │ that gap is what makes a siren sound like a siren.      │
// │                                                         │
// │ ── NOW EXPERIMENT ──                                    │
// │ Change ONE thing at a time and write down what you get. │
// │                                                         │
// │ 1) Make the two notes CLOSE together -- try 392 and     │
// │    440 instead of 392 and 784. Does it still sound      │
// │    like an alarm, or like something else?               │
// │                                                         │
// │    ___________________________________________________  │
// │                                                         │
// │ 2) Change the loop count from 2 to 5. How does a longer │
// │    siren feel different from a short one?               │
// │                                                         │
// │    ___________________________________________________  │
// │                                                         │
// │ 3) Cut both delays from 250 to 60. What happens, and    │
// │    WHY? (Look at the note duration -- it is 200 ms.)    │
// │                                                         │
// │    ___________________________________________________  │
// │                                                         │
// │ 4) DELETE both delay lines entirely. Predict first:     │
// │                                                         │
// │    I think I will hear: ______________________________  │
// │                                                         │
// │    I actually heard:    ______________________________  │
// │                                                         │
// │ 5) Real sirens SLIDE between pitches instead of jumping.│
// │    With only the tools you have today, could you get    │
// │    closer to a slide? What would you need?              │
// │                                                         │
// │    ___________________________________________________  │
// │                                                         │
// │ ⚠️ Question 3 and question 4 are the same lesson from    │
// │ two directions. A delay SHORTER than the note cuts it   │
// │ off early. NO delay means the next note interrupts the  │
// │ one still playing -- and four notes collapse into one   │
// │ blip. See the playFrequency diagram in Section 5.       │
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

    // <<< CHALLENGE 7: YOUR SIREN GOES HERE

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
