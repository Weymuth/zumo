/*
=====================================================
LESSON 01 - Hello Robot — Challenge 11: Add a Battery Check
=====================================================
WHAT THIS PROGRAM DOES:
(update this as you build!)
AUTHOR: DJ Weymuth
DATE: 7/19/2026
=====================================================
*/

#include <Zumo32U4.h>

// ┌─────────────────────────────────────────────────────────┐
// │ CHALLENGE 11 — ADD A BATTERY CHECK               [HARD] │
// ├─────────────────────────────────────────────────────────┤
// │                                                         │
// │ GOAL: make your robot warn you if the batteries are     │
// │ low BEFORE it runs the test.                            │
// │                                                         │
// │ This challenge introduces SENSE -- your robot can       │
// │ check its own internal state, not just the world.       │
// │                                                         │
// │ THE FUNCTION: readBatteryMillivolts() returns the       │
// │ battery voltage in millivolts. No object in front of    │
// │ it -- just call it.                                     │
// │                                                         │
// │ WHAT THE NUMBERS MEAN (rechargeable NiMH, your fleet):  │
// │     ~5,400 mV   fresh off the charger                   │
// │     ~4,800 mV   healthy working range                   │
// │     ~4,200 mV   LOW -- recharge now. Draining past      │
// │                 this damages the cells permanently.     │
// │                                                         │
// │ Find  <<< CHALLENGE 11  below, right after              │
// │ Serial.begin(). Your code goes there.                   │
// │                                                         │
// │ THE SHAPE:                                              │
// │                                                         │
// │     int voltage = readBatteryMillivolts();              │
// │     Serial.print("Battery: ");                          │
// │     Serial.println(voltage);                            │
// │                                                         │
// │     if (voltage < 4500) {                               │
// │       display.clear();                                  │
// │       display.print("LOW BATT!");                       │
// │       buzzer.playFrequency(200, 1000, 15);              │
// │       delay(2000);                                      │
// │     }                                                   │
// │                                                         │
// │ ⚠️ ONE BIG CATCH -- READ THIS OR YOU WILL BE FOOLED.     │
// │ The reading is only honest when the robot is running    │
// │ on BATTERIES with the power switch ON. On USB power     │
// │ alone the number reads low and strange, and your        │
// │ warning fires on perfectly good batteries.              │
// │                                                         │
// │ TEST IT PROPERLY:                                       │
// │   1. Batteries in, power switch ON, USB unplugged       │
// │   2. Read the number off the OLED or Serial             │
// │                                                         │
// │   My voltage on good batteries: ______ mV               │
// │   My voltage on USB only:       ______ mV               │
// │                                                         │
// │ Those two numbers are why the catch matters.            │
// │                                                         │
// │ ── WHY 4500? ──                                         │
// │ It sits between "healthy" (4,800) and "damaged"         │
// │ (4,200) -- an early warning, not an emergency. You      │
// │ will meet these numbers again in Lesson 3 as named      │
// │ constants, and in Lesson 11 you will find out why a     │
// │ tired battery quietly ruins timed driving.              │
// │                                                         │
// │ ── NOW THINK IT THROUGH ──                              │
// │                                                         │
// │ 1) Set the threshold to 6000 and upload. What happens,  │
// │    and why is that useless?                             │
// │                                                         │
// │    ___________________________________________________  │
// │                                                         │
// │ 2) Set it to 3000 instead. Now the warning almost       │
// │    never fires. Which mistake is WORSE for a robot on   │
// │    a competition floor -- warning too early, or too     │
// │    late? Defend your answer.                            │
// │                                                         │
// │    ___________________________________________________  │
// │                                                         │
// │    ___________________________________________________  │
// │                                                         │
// │ 3) This code WARNS you and then runs anyway. It could   │
// │    have refused to run at all. Which is the better      │
// │    design, and who should decide -- the programmer or   │
// │    the driver?                                          │
// │                                                         │
// │    ___________________________________________________  │
// │                                                         │
// │ 4) The check runs ONCE, at startup. Your robot might    │
// │    drive for two minutes after that. What could this    │
// │    code miss?                                           │
// │                                                         │
// │    ___________________________________________________  │
// │                                                         │
// │ 5) Run the robot until the batteries are genuinely      │
// │    tired, then check the voltage again.                 │
// │                                                         │
// │    Fresh: ______ mV    After a long run: ______ mV      │
// │                                                         │
// │    Now put the SAME robot on fresh batteries and drive  │
// │    the Challenge 6 out-and-back. Does it travel the     │
// │    same distance as it did when tired?                  │
// │                                                         │
// │    ___________________________________________________  │
// │                                                         │
// │ ⚠️ That last one is not a trick question. Same code,     │
// │ same delay, different distance. Lesson 11 is built      │
// │ entirely around why that happens -- and what to count   │
// │ instead of milliseconds.                                │
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

    // <<< CHALLENGE 11: YOUR BATTERY CHECK GOES HERE

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
