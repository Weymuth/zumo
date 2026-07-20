/*
=====================================================
LESSON 01 - Hello Robot — Challenge 8: The Pirouette
=====================================================
WHAT THIS PROGRAM DOES:
(update this as you build!)
AUTHOR: DJ Weymuth
DATE: 7/19/2026
=====================================================
*/

#include <Zumo32U4.h>

// ┌─────────────────────────────────────────────────────────┐
// │ CHALLENGE 8 — THE PIROUETTE                    [MEDIUM] │
// ├─────────────────────────────────────────────────────────┤
// │                                                         │
// │ GOAL: make the robot spin in place on its own center    │
// │ instead of driving forward.                             │
// │                                                         │
// │ HINT: what happens if one track goes forward while the  │
// │ other goes backward?                                    │
// │                                                         │
// │ Find  <<< CHALLENGE 8  below. The line reads:           │
// │                                                         │
// │     motors.setSpeeds(200, 200);                         │
// │                                                         │
// │ Those two numbers are the LEFT track and the RIGHT      │
// │ track, in that order. Right now they are the same, so   │
// │ both tracks push the same way and the robot goes        │
// │ straight.                                               │
// │                                                         │
// │ PREDICT FIRST:                                          │
// │   If the left track goes forward and the right goes     │
// │   backward, which way does the robot turn? ___________  │
// │                                                         │
// │ Now make the two numbers opposite and find out.         │
// │                                                         │
// │ TEST on the floor. Did it spin the way you predicted?   │
// │                                                         │
// │ ── WHY THIS IS THE WHOLE COURSE ──                      │
// │ This is called DIFFERENTIAL steering, and it is how     │
// │ your Zumo turns for the rest of the book. It has no     │
// │ steering wheel and no front axle -- every turn it ever  │
// │ makes comes from running the two tracks at different    │
// │ speeds.                                                 │
// │                                                         │
// │ Small difference = gentle curve.                        │
// │ Opposite numbers = spin in place.                       │
// │                                                         │
// │ ── NOW EXPERIMENT ──                                    │
// │ One change at a time. Write down what you get.          │
// │                                                         │
// │ 1) setSpeeds(200, 100) -- both forward, but one track   │
// │    slower. What shape does the robot drive?             │
// │                                                         │
// │    ___________________________________________________  │
// │                                                         │
// │ 2) setSpeeds(-200, 200) -- the opposite of your spin.   │
// │    Which way does it turn now, and why?                 │
// │                                                         │
// │    ___________________________________________________  │
// │                                                         │
// │ 3) A robot curves toward its SLOWER track. Check that   │
// │    against what you just saw. Does the rule hold?       │
// │                                                         │
// │    ___________________________________________________  │
// │                                                         │
// │ 4) setSpeeds(200, 0) -- one track driving, one stopped. │
// │    PREDICT before you upload:                           │
// │                                                         │
// │    I think it will: __________________________________  │
// │                                                         │
// │    It actually:     __________________________________  │
// │                                                         │
// │    Is this a spin in place, or something different?     │
// │    Where is the robot pivoting around?                  │
// │                                                         │
// │    ___________________________________________________  │
// │                                                         │
// │ 5) Your two tracks are not identical. Send them the     │
// │    SAME number -- setSpeeds(200, 200) -- and watch a    │
// │    long straight run closely. Does it drift?            │
// │                                                         │
// │    Which way? _____________________________________     │
// │                                                         │
// │    Hold on to that answer. In Lesson 3 you will get a   │
// │    number called TRIM whose entire job is fixing it.    │
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
    motors.setSpeeds(200, 200);   // <<< CHALLENGE 8: make these opposite
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
