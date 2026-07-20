/*
=====================================================
LESSON 01 - Hello Robot — Challenge 1: Hello, World!
=====================================================
WHAT THIS PROGRAM DOES:
(update this as you build!)
AUTHOR: DJ Weymuth
DATE: 7/19/2026
=====================================================
*/

#include <Zumo32U4.h>

// ┌─────────────────────────────────────────────────────────┐
// │ CHALLENGE 1 — HELLO, WORLD!                    [MEDIUM] │
// ├─────────────────────────────────────────────────────────┤
// │                                                         │
// │ Section 1 told you the story: in 1978, Kernighan and    │
// │ Ritchie put a program in a book that printed two words. │
// │ Every programmer since has started the same way.        │
// │                                                         │
// │ Your robot has not actually said it yet. Fix that.      │
// │ FIVE PARTS, in order. Test after each one.              │
// │                                                         │
// │ ── PART 1: put it on the SCREEN ──                      │
// │ Find  <<< CH1 PART 1  below. Add these two lines ABOVE  │
// │ the display.print("Press A"); line:                     │
// │                                                         │
// │     display.gotoXY(0, 0);                               │
// │     display.print("Hello, World!");                     │
// │                                                         │
// │ Then put this line just before the "Press A" print, so  │
// │ it lands on the second row:                             │
// │                                                         │
// │     display.gotoXY(0, 1);                               │
// │                                                         │
// │ TEST: the OLED shows TWO lines --                       │
// │         Hello, World!                                   │
// │         Press A                                         │
// │                                                         │
// │ gotoXY(column, row) parks the cursor before you print.  │
// │ Row 0 is the top. Leave it out and the second print     │
// │ lands on top of the first.                              │
// │                                                         │
// │ ── PART 2: say it in BOTH places ──                     │
// │ Find  <<< CH1 PART 2. The Serial Monitor says           │
// │ "Hello, Robot!". Change it to "Hello, World!" so the    │
// │ screen and the monitor agree.                           │
// │                                                         │
// │ ── PART 3: make it YOURS ──                             │
// │ Change the SCREEN greeting to your own name --          │
// │ "Hello, DJ!" -- and leave the Serial line saying        │
// │ "Hello, World!".                                        │
// │                                                         │
// │ ── PART 4: change the button ──                         │
// │ Find  <<< CH1 PART 4. Make the robot wait for Button B  │
// │ instead of Button A. TWO things must change:            │
// │                                                         │
// │     the TEXT:      display.print("Press B");            │
// │     the BEHAVIOR:  while (!buttonB.getSingle...         │
// │                                                         │
// │ TEST: press A. Nothing. Press B. The show runs.         │
// │                                                         │
// │ ⚠️ Change only the text and your screen tells a lie --   │
// │ it asks for B while the robot still waits for A. Change │
// │ only the behavior and it lies the other way. Code and   │
// │ label move together. That is true for the rest of this  │
// │ course, and the rest of engineering.                    │
// │                                                         │
// │ ── PART 5: find your robot's name ──                    │
// │ Your robot has a name in its permanent memory. It is    │
// │ NOT in this file -- scrolling will not find it. The     │
// │ only way to learn it is to ask the robot.               │
// │                                                         │
// │ Open the Serial Monitor, press Button A, and look at    │
// │ the line right after "Hello".                           │
// │                                                         │
// │     My robot's name is: ________________________        │
// │                                                         │
// │ Now find out WHY. Some of these names are ordinary      │
// │ words -- searching "Data" or "Bishop" gets you nowhere. │
// │ Give the search context. Ask it like this:              │
// │                                                         │
// │        why would my robot be named ______ ?             │
// │                                                         │
// │ Those two words -- MY ROBOT -- turn a common word into  │
// │ the right answer.                                       │
// │                                                         │
// │     Named after: ______________________________         │
// │                                                         │
// │     What did they do? (one line)                        │
// │                                                         │
// │     ___________________________________________         │
// │                                                         │
// │ Examples of the format:                                 │
// │   Marvin    -- The Hitchhiker's Guide to the Galaxy.    │
// │                A robot with a brain the size of a       │
// │                planet and nothing to do but sulk.       │
// │   Shakey    -- Stanford Research Institute, 1966. The   │
// │                first mobile robot that could reason     │
// │                about its own actions.                   │
// │   Sojourner -- NASA, 1997. First rover to drive on      │
// │                Mars. Named for Sojourner Truth.         │
// │                                                         │
// │ ⚠️ The AI answers your question, then keeps going --     │
// │ guessing about YOUR robot ("probably named this         │
// │ because it performs precise tasks..."). It has never    │
// │ seen your robot. Take the fact. Ignore the guess.       │
// │                                                         │
// │ Print a label for it. That robot is yours all term.     │
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
    display.print("Press A");        // <<< CH1 PART 1 and PART 4

    // ───── 1. WAIT FOR THE BUTTON ─────
    while (!buttonA.getSingleDebouncedPress()) {   // <<< CH1 PART 4
        delay(10);
    }

    // ───── 2. SAY HELLO ─────
    Serial.println("Hello, Robot!");  // <<< CH1 PART 2

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
