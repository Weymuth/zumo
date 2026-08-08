# The family pin — blocks whose family CONTENT cannot re-derive

**212 of 1,069 callout blocks.** Generated ONCE, at S130, from the verified state.
This file is a PRESERVED LAYER: it is read-only input to `build_family_map.py` and
must never be regenerated from `data-family`. A pin rebuilt from the value it exists
to check would agree with any drift by construction.

## Why these blocks need a pin

Their family was only ever recoverable from a decorative emoji — `build_family_map`'s
GLYPH tier, which S112 shipped calling itself a stopgap. The marks arc replaced that
emoji with an `<img>`, so that signal is gone. The family itself is NOT lost: it sits in
`data-family`, and at S130 all 212 were verified against the pre-swap glyph with
**zero mismatches**. What the pin restores is the ability to catch a FUTURE change.

The key is `data-callout`, the authored identity added at S130. It is authored, never
derived, so it survives the edits that invalidate a file offset.

The retired glyph is recorded for provenance only. **Nothing may read it back to recover
a family** — §24.14 forbids closing that loop, and doing so would rebuild the very
decoration-keyed tier this file replaces.

## The pinned blocks

| `data-callout` | Family | Retired glyph | Label (first 58 chars) |
|---|---|---|---|
| `1.4` | KEY TERM | 🔑 | PlatformIO A professional development environment for prog |
| `1.7` | KEY TERM | 🔑 | Library Pre-written code that provides ready-to-use functi |
| `1.9` | KEY TERM | 🔑 | A-Star32U4 The brain of your Zumo robot. A small circuit b |
| `1.10` | KEY TERM | 🔑 | Microcontroller A small, self-contained computer on a sing |
| `1.15` | KEY TERM | 🔑 | Git A version control tool. PlatformIO uses it to download |
| `1.23` | KEY TERM | 🔑 | Object A named variable that represents a piece of hardwar |
| `1.59` | KEY TERM | 🔑 | Serial Monitor A window that displays text messages sent f |
| `1.75` | KEY TERM | 🔑 | A-Star32U4 The brain of your Zumo robot. A small circuit b |
| `1.76` | KEY TERM | 🔑 | Git A version control tool that PlatformIO uses to downloa |
| `1.77` | KEY TERM | 🔑 | Library Pre-written code that provides ready-to-use functi |
| `1.78` | KEY TERM | 🔑 | Microcontroller A small, self-contained computer on a sing |
| `1.79` | KEY TERM | 🔑 | Object A named variable that represents and controls a pie |
| `1.80` | KEY TERM | 🔑 | PlatformIO A professional development environment for prog |
| `1.81` | KEY TERM | 🔑 | Sense-Decide-Act Loop The fundamental pattern all robots f |
| `1.82` | KEY TERM | 🔑 | Serial Monitor A tool that displays text messages sent fro |
| `1.83` | GOING DEEPER | 🔬 | Curious how any of this actually works? The Going Deeper p |
| `2.5` | KEY TERM | 🔑 | Comment - Text in your code that the compiler ignores comp |
| `2.11` | ENGINEER'S LOG | 📓 | For your engineering notebook The PNG is sized to drop str |
| `2.14` | KEY TERM | 🔑 | Curly Braces { } - Define the start and end of a code bloc |
| `2.31` | KEY TERM | 🔑 | Header Comment - A block of text at the very top of your f |
| `2.34` | KEY TERM | 🔑 | include - Tells the computer to load a library (a collecti |
| `2.35` | KEY TERM | 🔑 | Object - A variable that represents a piece of hardware. Y |
| `2.37` | KEY TERM | 🔑 | Constant - A value that doesn't change while the program r |
| `2.40` | KEY TERM | 🔑 | setup() - Code inside this function runs exactly ONE time  |
| `2.41` | KEY TERM | 🔑 | loop() - Code inside this function runs FOREVER, repeating |
| `2.44` | KEY TERM | 🔑 | Function - A reusable chunk of code with a name. Instead o |
| `2.54` | KEY TERM | 🔑 | Serial Monitor - A window in VS Code that shows messages f |
| `2.77` | KEY TERM | 🔑 | Function Prototype - A one-line preview of a function: its |
| `2.96` | TRY THIS | 🎯 | CHALLENGE: Write a function beep(int count) that buzzes th |
| `2.107` | KEY TERM | 🔑 | Baud Rate - A speed setting for serial links, in bits per  |
| `2.108` | KEY TERM | 🔑 | Code Block - A group of statements enclosed in curly brace |
| `2.109` | KEY TERM | 🔑 | Comment - Text in your code that the computer ignores. Wri |
| `2.110` | KEY TERM | 🔑 | Constant - A value that doesn't change while the program r |
| `2.111` | KEY TERM | 🔑 | Curly Braces { } - Symbols that mark the start and end of  |
| `2.112` | KEY TERM | 🔑 | Execution - The process of the computer running your code, |
| `2.113` | KEY TERM | 🔑 | F() Macro - Wraps string literals to store them in flash m |
| `2.114` | KEY TERM | 🔑 | Function - A reusable chunk of code with a name. You "call |
| `2.115` | KEY TERM | 🔑 | Hardware Object - A variable that represents a piece of ha |
| `2.116` | KEY TERM | 🔑 | include - Loads a library of pre-written code so you can u |
| `2.117` | KEY TERM | 🔑 | loop() - Function that runs over and over forever after se |
| `2.118` | KEY TERM | 🔑 | Program Flow - The order in which lines of code are execut |
| `2.119` | KEY TERM | 🔑 | Scope - Where a variable can be used. Variables declared a |
| `2.120` | KEY TERM | 🔑 | Serial Monitor - A window that shows text messages from yo |
| `2.121` | KEY TERM | 🔑 | setup() - Function that runs exactly once when the robot p |
| `2.122` | GOING DEEPER | 🔬 | Curious how any of this actually works? The Going Deeper p |
| `3.2` | KEY TERM | 🔑 | Motor Imbalance - When two motors don't spin at exactly th |
| `3.4` | KEY TERM | 🔑 | TRIM - A small correction value you add to one motor to co |
| `3.6` | KEY TERM | 🔑 | Differential Drive - A two-motor system where steering is  |
| `3.11` | KEY TERM | 🔑 | Negative Speed Values - In everyday speech, you'd say "go  |
| `3.16` | KEY TERM | 🔑 | Open-Loop Control - Send a command and hope for the best.  |
| `3.17` | KEY TERM | 🔑 | Closed-Loop Control - Send a command, measure the result,  |
| `3.30` | KEY TERM | 🔑 | constrain(value, min, max) - Returns: min if value < min,  |
| `3.44` | KEY TERM | 🔑 | TRIM A single adjustable value added to one motor's speed  |
| `3.45` | INSIGHT | 🔍 | Why four small functions instead of one big loop() ? Each  |
| `3.91` | TRY THIS | 🎯 | CHALLENGE: Add a calibration constant SETTLE_TIME (try 300 |
| `3.96` | NOTE | 📘 | Testing on USB? The reading lies. readBatteryMillivolts()  |
| `3.98` | NOTE | 📘 | const and constrain() are two different jobs. They start w |
| `3.114` | KEY TERM | 🔑 | Closed-Loop Control - Send a command, measure the result,  |
| `3.115` | KEY TERM | 🔑 | constrain(value, min, max) - A function (from Arduino.h) t |
| `3.116` | KEY TERM | 🔑 | Differential Drive - A two-motor system where steering is  |
| `3.117` | KEY TERM | 🔑 | Motor Imbalance - When two motors don't spin at exactly th |
| `3.118` | KEY TERM | 🔑 | Negative Speed Values - In motor commands, the minus sign  |
| `3.119` | KEY TERM | 🔑 | Open-Loop Control - Send a command and hope for the best.  |
| `3.120` | KEY TERM | 🔑 | TRIM - A small correction value added to one motor to comp |
| `5.4` | KEY TERM | 🔑 | Proximity Sensor A sensor that detects how close an object |
| `5.7` | KEY TERM | 🔑 | Brightness Level A measure (0-6) of how many IR LED pulses |
| `5.8` | KEY TERM | 🔑 | Threshold A boundary value used to make decisions. Values  |
| `5.14` | KEY TERM | 🔑 | For Loop A control structure that repeats code a specific  |
| `5.43` | KEY TERM | 🔑 | Brightness Level A measure (0-6) of how many IR LED pulses |
| `5.44` | KEY TERM | 🔑 | Infrared (IR) Light with wavelengths longer than visible r |
| `5.45` | KEY TERM | 🔑 | Static Variable A local variable that retains its value be |
| `5.46` | KEY TERM | 🔑 | Threshold A boundary value used to make decisions. Values  |
| `6.2` | KEY TERM | 🔑 | Encoder A sensor that converts rotational motion into elec |
| `6.4` | KEY TERM | 🔑 | Behind the Scenes The Zumo32U4 library uses interrupts to  |
| `6.5` | KEY TERM | 🔑 | Quadrature Encoding A method using two offset sensors to d |
| `6.6` | KEY TERM | 🔑 | Signed Counts Encoder counts are signed integers . Forward |
| `6.8` | KEY TERM | 🔑 | The Math Counts per wheel rotation = 12 × 75.81 = 909.7 co |
| `6.12` | KEY TERM | 🔑 | The Formula Counts per degree = (wheel_base × π × counts_p |
| `6.13` | KEY TERM | 🔑 | Closed-Loop Control A control system that uses sensor feed |
| `6.24` | KEY TERM | 🔑 | The Formula Turn at each corner = 360 ÷ number of sides |
| `6.54` | KEY TERM | 🔑 | Function A reusable block of code that performs a specific |
| `6.60` | KEY TERM | 🔑 | Closed-Loop Control A control system that uses sensor feed |
| `6.61` | KEY TERM | 🔑 | Encoder A sensor that converts rotational motion into elec |
| `6.62` | KEY TERM | 🔑 | Function A reusable block of code with a name, optional pa |
| `6.63` | KEY TERM | 🔑 | Hall Effect Sensor A sensor that detects changes in magnet |
| `6.64` | KEY TERM | 🔑 | Interrupt A hardware signal that pauses normal code execut |
| `6.65` | KEY TERM | 🔑 | Quadrature Encoding A method using two offset sensors to d |
| `6.66` | KEY TERM | 🔑 | Dead Reckoning Tracking a robot's position by accumulating |
| `6.67` | KEY TERM | 🔑 | Wheel Base The distance between the centers of the left an |
| `7.9` | KEY TERM | 🔑 | Header Files (.h) Declarations: "What exists." Like a rest |
| `7.10` | KEY TERM | 🔑 | Implementation Files (.cpp) Definitions: "How it works." L |
| `7.12` | KEY TERM | 🔑 | include A directive that literally copies and pastes the e |
| `7.13` | KEY TERM | 🔑 | pragma once A compiler directive that says: "Only include  |
| `7.15` | KEY TERM | 🔑 | Scope Determines where in your code a variable can be acce |
| `7.21` | KEY TERM | 🔑 | Header file (.h) A file that declares what exists (functio |
| `7.22` | KEY TERM | 🔑 | Implementation file (.cpp) A file that contains the actual |
| `7.23` | KEY TERM | 🔑 | Include guard An older technique (#ifndef/#define/#endif)  |
| `7.24` | KEY TERM | 🔑 | Declaration Telling the compiler "this function exists" -  |
| `7.25` | KEY TERM | 🔑 | Definition The actual code that makes a function work - ha |
| `7.26` | KEY TERM | 🔑 | Refactoring Reorganizing existing code without changing wh |
| `7.27` | KEY TERM | 🔑 | Scope Determines where in your code a variable can be acce |
| `7.73` | KEY TERM | 🔑 | Declaration Tells the compiler "this function exists, here |
| `7.74` | KEY TERM | 🔑 | Definition Provides the actual code that makes the functio |
| `7.76` | KEY TERM | 🔑 | extern A keyword meaning "this variable/object exists in a |
| `7.78` | KEY TERM | 🔑 | Scope The region where a variable is accessible. Use it ou |
| `7.93` | KEY TERM | 🔑 | Declaration Telling the compiler "this function exists" -  |
| `7.94` | KEY TERM | 🔑 | Definition The actual code that makes a function work - ha |
| `7.95` | KEY TERM | 🔑 | Header File (.h) A file that declares what exists (functio |
| `7.96` | KEY TERM | 🔑 | Implementation File (.cpp) A file that contains the actual |
| `7.97` | KEY TERM | 🔑 | Include Guard An older technique (#ifndef/#define/#endif)  |
| `7.98` | KEY TERM | 🔑 | pragma once A compiler directive placed at the top of ever |
| `7.99` | KEY TERM | 🔑 | include Directive A command that copies the contents of an |
| `7.100` | KEY TERM | 🔑 | Linker The program that connects all your compiled files t |
| `7.101` | KEY TERM | 🔑 | Refactoring Reorganizing existing code without changing wh |
| `7.102` | KEY TERM | 🔑 | Battery Check A startup routine that reads readBatteryMill |
| `7.103` | GOING DEEPER | 🔬 | Curious how any of this actually works? The Going Deeper p |
| `8.8` | KEY TERM | 🔑 | Setpoint The target value you want to maintain. For line f |
| `8.9` | KEY TERM | 🔑 | Error The difference between where you are and where you w |
| `8.10` | KEY TERM | 🔑 | Kp (Proportional Gain) A tuning constant that scales error |
| `8.13` | KEY TERM | 🔑 | Error = Current Position − Setpoint Example: If position = |
| `8.55` | KEY TERM | 🔑 | Function Parameter A value you pass INTO a function that t |
| `8.63` | KEY TERM | 🔑 | Bang-Bang Control A control method that switches between d |
| `8.64` | KEY TERM | 🔑 | Error The difference between current position and target p |
| `8.65` | KEY TERM | 🔑 | extern A keyword meaning "this variable exists in another  |
| `8.66` | KEY TERM | 🔑 | Kp (Proportional Gain) A tuning constant that scales error |
| `8.67` | KEY TERM | 🔑 | Oscillation Back-and-forth motion caused by overcorrection |
| `8.68` | KEY TERM | 🔑 | Proportional Control A control method where correction is  |
| `8.69` | KEY TERM | 🔑 | Setpoint The target value (2000 for centered line). |
| `8.70` | GOING DEEPER | 🔬 | Curious how any of this actually works? The Going Deeper p |
| `9.1` | LEARN | 📖 | A Different Kind of Thinking This lesson marks a fundament |
| `9.2` | LEARN | 📖 | RoboCup Junior Connection In RoboCup Junior Line Rescue co |
| `9.4` | KEY TERM | 🔑 | Intersection - A point where the line branches, crosses, o |
| `9.6` | LEARN | 📖 | Why Green Works Green surfaces absorb some IR light but re |
| `9.7` | KEY TERM | 🔑 | Threshold - A boundary value used to categorize sensor rea |
| `9.12` | KEY TERM | 🔑 | Dead End - An intersection marked with green on both sides |
| `9.14` | KEY TERM | 🔑 | State Machine - A programming pattern where a system can o |
| `9.16` | KEY TERM | 🔑 | Enum (enumeration) - A data type that defines a set of nam |
| `9.17` | KEY TERM | 🔑 | Tank Turn - A turning method where opposite wheels spin in |
| `9.23` | LEARN | 📖 | Avoiding False Positives: Debouncing Sensor noise can caus |
| `9.70` | KEY TERM | 🔑 | Dead End An intersection marked with green on both sides,  |
| `9.71` | KEY TERM | 🔑 | Debouncing A technique requiring multiple consistent readi |
| `9.72` | KEY TERM | 🔑 | Enum (enumeration) A data type that defines a set of named |
| `9.73` | KEY TERM | 🔑 | Intersection A point where the line branches, crosses, or  |
| `9.74` | KEY TERM | 🔑 | Right-Hand Rule A maze-solving algorithm: prefer right, th |
| `9.75` | KEY TERM | 🔑 | State Machine A programming pattern where a system can onl |
| `9.76` | KEY TERM | 🔑 | Tank Turn A turning method where opposite wheels spin in o |
| `9.77` | KEY TERM | 🔑 | Threshold A boundary value used to categorize sensor readi |
| `10.2` | KEY TERM | 🔑 | Obstacle Anything physically blocking the robot's path tha |
| `10.11` | KEY TERM | 🔑 | Avoidance Maneuver A pre‑planned sequence of movements tha |
| `10.13` | KEY TERM | 🔑 | Behavior Arbitration Deciding, in advance and in writing , |
| `10.36` | KEY TERM | 🔑 | extern A promise that a variable or object exists somewher |
| `10.88` | KEY TERM | 🔑 | Phase Variable A variable that survives between passes of  |
| `10.102` | KEY TERM | 🔑 | Obstacle Anything physically blocking the robot's path tha |
| `10.103` | KEY TERM | 🔑 | Proximity Sensor An infrared emitter and receiver pair. It |
| `10.104` | KEY TERM | 🔑 | Behavior Arbitration Deciding, in advance and in writing , |
| `10.105` | KEY TERM | 🔑 | Avoidance Maneuver A pre‑planned sequence of moves that ta |
| `10.106` | KEY TERM | 🔑 | Phase Variable A variable that survives between passes of  |
| `10.107` | KEY TERM | 🔑 | Open Loop Motion where nothing is watching the result . Yo |
| `10.108` | KEY TERM | 🔑 | Closed Loop Motion where a sensor continuously corrects th |
| `10.109` | KEY TERM | 🔑 | extern A promise that a variable or object exists somewher |
| `10.110` | KEY TERM | 🔑 | Pin Sharing Two peripherals wired to the same microcontrol |
| `10.111` | KEY TERM | 🔑 | Accumulated Error A small error, repeated, becoming a larg |
| `11.2` | THE WALL | 🛑 | It depends on the battery. And that is fatal. A fresh batt |
| `11.5` | THE WALL | 🛑 | The alarm is not allowed to go off until the robot has alr |
| `11.9` | THE WALL | 🛑 | Read the last line. That TRIM is not decoration. Inside a  |
| `11.16` | THE WALL | 🛑 | This is the moment TRIM stops being homework. For three le |
| `11.22` | THE WALL | 🛑 | There is no threshold that works. Not a badly chosen one - |
| `12.1` | THE WALL | 🛑 | The encoder is not broken. It is doing its job perfectly.  |
| `12.4` | THE WALL | 🛑 | This is a structural limit, not a tuning problem. You cann |
| `12.6` | THE WALL | 🛑 | Do the arithmetic on that. A bias of 20°/sec, accumulated  |
| `12.9` | THE WALL | 🛑 | And therefore: A SPIN CANNOT CALIBRATE A GYRO. If the robo |
| `12.16` | THE WALL | 🛑 | Notice what is NOT in there: TRIM. There is no TRIM in tur |
| `12.28` | THE WALL | 🛑 | Build it. The binary did not change. AT ALL. Step 5 grew t |
| `12.31` | THE WALL | 🛑 | This block MUST come before waitForStart(). Here is why. T |
| `12.38` | THE WALL | 🛑 | The number climbs anyway. The robot is motionless . The an |
| `12.41` | THE WALL | 🛑 | Now put it on the delrin. Press B. Encoder: 90 Gyro: |
| `12.45` | THE WALL | 🛑 | Button A on delrin: the square collapses. Each corner slip |
| `12.51` | THE WALL | 🛑 | Notice what you did NOT do in this lesson. You did not rep |
| `12.60` | THE WALL | 🛑 | What B4 should teach you for the rest of your life Three o |
| `12.77` | GOING DEEPER | 🔬 | Curious how any of this actually works? The Going Deeper p |
| `14.1` | WHAT YOU SHOULD SEE | 👀 | The Reality Check At every RoboCup Junior competition, the |
| `14.6` | NOTE | 📘 | Read that formula again, because it overturns the obvious  |
| `14.12` | WHAT YOU SHOULD SEE | 👀 | Healthy Battery Readings ~5,400 mV: Fresh off the charger. |
| `14.13` | IF YOU'RE STUCK | 🔌 | Why these numbers and not round ones. Your fleet runs enel |
| `14.28` | KEY TERM | 🔑 | When to Call LoP Call Lack of Progress when: Robot is clea |
| `15.2` | WARNING | ⚠ | The honest warning up front. Most PID chapters end with a  |
| `15.5` | NOTE | 📘 | D is often called the damper , and that is exactly right.  |
| `15.7` | WARNING | ⚠ | And I is the most dangerous term in the equation. If the e |
| `15.10` | NOTE | 📘 | The general rule, and it is worth more than this lesson: i |
| `15.15` | WARNING | ⚠ | That last row is the whole reason this lesson uses micros( |
| `15.16` | WARNING | ⚠ | Ziegler–Nichols is a starting point, not an answer. It is  |
| `15.17` | WARNING | ⚠ | This rung is designed to fail. Build it anyway. Section 3. |
| `15.18` | NOTE | 📘 | An instrument is not “good” or “bad.” It is matched or mis |
| `15.19` | WARNING | ⚠ | Nothing is free. The filter also delays the derivative - y |
| `15.25` | GOING DEEPER | 🔬 | Curious how any of this actually works? The Going Deeper p |
| `16.6` | WARNING | ⚠ | The classic TDP mistakes: “it works because it works” (exp |
| `16.7` | WARNING | ⚠ | Two rules the hardware enforces. First: an EEPROM write ta |
| `16.8` | NOTE | 📘 | Design pattern worth stealing: the mode does not change wh |
| `16.12` | WARNING | ⚠ | Do not “fix” this by deleting the EEPROM code you just typ |
| `16.14` | TIP | 💡 | Write this trade down in your journal tonight. It is the s |
| `16.16` | WARNING | ⚠ | The #1 project killer is not a bug. It is the working robo |
| `16.19` | KEY TERM | 🔑 | Bootloader The 4,096-byte resident program that answers th |
| `16.20` | KEY TERM | 🔑 | Linker - The last tool in the build chain; places every fu |
| `16.21` | KEY TERM | 🔑 | EEPROM - 1,024 bytes of non-volatile memory on the 32U4. F |
| `16.22` | KEY TERM | 🔑 | Non-volatile - Memory that keeps its contents with the pow |
| `16.23` | KEY TERM | 🔑 | Magic byte - A chosen fingerprint written at the front of  |
| `16.24` | KEY TERM | 🔑 | Baseline - The inherited robot's scored run on your course |
| `16.25` | KEY TERM | 🔑 | A/B test - Two builds differing in exactly one variable -  |
| `16.26` | KEY TERM | 🔑 | MVP - Minimum Viable Product: the smallest version of the  |
| `16.27` | KEY TERM | 🔑 | TDP - Technical Description Paper - the RoboCupJunior subm |
| `16.28` | KEY TERM | 🔑 | Flash budget - The habit of pricing features in bytes and  |
| `16.29` | GOING DEEPER | 🔬 | Curious how any of this actually works? The Going Deeper p |

## Count by family

| Family | Blocks |
|---|---|
| KEY TERM | 159 |
| THE WALL | 17 |
| WARNING | 10 |
| GOING DEEPER | 7 |
| NOTE | 7 |
| LEARN | 4 |
| TRY THIS | 2 |
| WHAT YOU SHOULD SEE | 2 |
| ENGINEER'S LOG | 1 |
| INSIGHT | 1 |
| IF YOU'RE STUCK | 1 |
| TIP | 1 |

---
*Generated once at S130 from the verified state. Preserved layer — do not regenerate.*
