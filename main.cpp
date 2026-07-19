/*
=====================================================
ZUMO ROBOT NAME WRITER  —  TEACHER UTILITY
=====================================================
Flash this ONCE per robot, before the term starts.

WHAT IT DOES:
  Writes a permanent name into the robot's EEPROM at
  address 512. The name survives every reflash the
  student ever does -- uploading Lesson 4 code does
  NOT erase it. That is the whole point.

HOW TO USE:
  1. Set ROBOT_NAME below to the name for THIS robot.
  2. Upload to that robot.
  3. The OLED confirms what was written.
  4. Change ROBOT_NAME, upload to the next robot.
  5. When the fleet is done, put your normal lesson
     code back on them. The names stay.

ADDRESS MAP (do not change without checking L16):
  addr 0   .. 511  -> reserved: Lesson 16 tuning struct
  addr 512 .. 543  -> robot name (this file)
=====================================================
*/

#include <Zumo32U4.h>
#include <EEPROM.h>

// ===== SET THIS, THEN UPLOAD =====
const char ROBOT_NAME[] = "WOPR";
// =================================

// ===== THE FLEET ROSTER =====
// HAL 9000   WOPR        Johnny 5    R2-D2
// C-3PO      Bishop      T-800       Iron Giant
// Robot B9   KITT        Optimus     Wall-E
// EVE        Baymax      Ava         Data
// Bender     Rosie       Kamelion    Asimo
// Turing     Lovelace
// ============================

Zumo32U4OLED display;
Zumo32U4Buzzer buzzer;

const int  NAME_ADDR  = 512;   // stays clear of Lesson 16's struct at 0
const byte NAME_MAGIC = 0x5A;  // "a name lives here"
const int  NAME_MAX   = 20;    // 20 chars + terminator, fits 21x8 OLED row

void setup() {
    Serial.begin(115200);
    display.clear();
    display.setLayout21x8();

    // Write the magic byte, then the name, one byte at a time.
    // EEPROM.update() only writes when the value actually changes,
    // which spares the cell its limited write budget.
    EEPROM.update(NAME_ADDR, NAME_MAGIC);

    int i = 0;
    while (i < NAME_MAX && ROBOT_NAME[i] != '\0') {
        EEPROM.update(NAME_ADDR + 1 + i, ROBOT_NAME[i]);
        i++;
    }
    EEPROM.update(NAME_ADDR + 1 + i, '\0');   // terminator

    // Read it straight back so the confirmation is proof, not hope.
    char check[NAME_MAX + 1];
    for (int j = 0; j <= NAME_MAX; j++) {
        check[j] = EEPROM.read(NAME_ADDR + 1 + j);
        if (check[j] == '\0') { break; }
    }
    check[NAME_MAX] = '\0';

    display.gotoXY(0, 0);
    display.print("NAME WRITTEN:");
    display.gotoXY(0, 1);
    display.print(check);
    display.gotoXY(0, 3);
    display.print("Next robot ->");
    display.gotoXY(0, 4);
    display.print("edit ROBOT_NAME");

    Serial.print("Wrote robot name: ");
    Serial.println(check);

    buzzer.playFrequency(784, 150, 15);
    delay(180);
    buzzer.playFrequency(1047, 250, 15);
}

void loop() {
    // Nothing. The write already happened, once, in setup().
}
