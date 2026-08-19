#!/bin/bash
# ZUMO COMPILE HARNESS v3.1 — PIO-TRUE
# Mirrors PlatformIO platform-atmelavr/builder/frameworks/arduino.py EXACTLY:
#   CCFLAGS  : -Os -Wall -ffunction-sections -fdata-sections -flto
#   CXXFLAGS : -fno-exceptions -fno-threadsafe-statics -fpermissive
#   LINKFLAGS: -Os -Wl,--gc-sections -flto -fuse-linker-plugin
# AND enforces the REAL ceiling from boards/a-star32U4.json: 28672 B flash / 2560 B RAM.
#
# v3.1 — THE COMPILER CAN SPEAK. For its whole life this script's header claimed
# -Wall while the code below carried -w, and every warning the student's own
# PlatformIO prints was discarded here. S167 named the debt; this pays the cheap
# half of it. Three things were MEASURED before the flag moved (rule 34):
#   1. -w vs -Wall is BYTE-IDENTICAL. The .elf is NOT reproducible build-to-build
#      (three identical -w builds gave three md5s — LTO embeds build state), so
#      the elf is the wrong instrument. `avr-objcopy -O binary` — the flash image
#      itself — is stable, and is the SAME under both flags. Warnings cannot move
#      a byte figure in this book, and that is why this change is affordable.
#   2. THE VENDOR CORE IS SILENT. ArduinoCore-avr plus all eight Pololu libraries
#      compile under -Wall with ZERO warnings, so -w was never protecting anyone
#      from third-party noise. It was only muting our own code.
#   3. POPULATION: 113 warnings across 70 of the 216 payloads, in TWO classes and
#      14 distinct sites — -Wswitch (110) and -Wunused-variable (3). 106 of the
#      110 are the build-up model working as designed: a state enters RobotState
#      in the lesson that declares it and gets its `case` a step or two later, so
#      the intermediate payload legitimately does not handle it. That is signal a
#      student SHOULD see, not noise. Four are not — see byte_audit's WARNINGS arm.
#
# THEREFORE THIS SCRIPT REPORTS AND DOES NOT FAIL ON A WARNING. A harness that
# failed here would fail 70 correct builds. The count rides on the PASS/OVER line
# and the text is left on disk beside the build for whoever wants to read it.
H=/home/claude/harness
CEIL_FLASH=28672
CEIL_RAM=2560
LIBDIRS="zumo-32u4-arduino-library pololu-buzzer-arduino pololu-oled-arduino pololu-menu-arduino pushbutton-arduino fastgpio-arduino usb-pause-arduino pololu-hd44780-arduino"
build_includes() {
  INC=""
  for d in $LIBDIRS; do [ -d "$H/$d/src" ] && INC="$INC -I$H/$d/src" || INC="$INC -I$H/$d"; done
  INC="$INC -I$H/ArduinoCore-avr/cores/arduino -I$H/ArduinoCore-avr/variants/leonardo"
  INC="$INC -I$H/ArduinoCore-avr/libraries/Wire/src -I$H/ArduinoCore-avr/libraries/Wire/src/utility"
  INC="$INC -I$H/ArduinoCore-avr/libraries/SPI/src -I$H/ArduinoCore-avr/libraries/EEPROM/src"
  INC="$INC -I$H/ArduinoCore-avr/libraries/HID/src"
}
DEF="-mmcu=atmega32u4 -DF_CPU=16000000L -DARDUINO=10819 -DARDUINO_AVR_A_STAR_32U4 -DARDUINO_ARCH_AVR -DUSB_VID=0x1ffb -DUSB_PID=0x2300"
CCF="$DEF -Os -Wall -ffunction-sections -fdata-sections -flto"
CF="$CCF -std=gnu11 -fno-fat-lto-objects"
CXXF="$CCF -std=gnu++11 -fno-exceptions -fno-threadsafe-statics -fpermissive"
LDF="$DEF -Os -Wl,--gc-sections -flto -fuse-linker-plugin"

if [ "$1" = "--setup" ]; then
  build_includes
  # The core build used to send BOTH compile loops to /dev/null. Measured: the
  # vendor tree is silent under -Wall, so nothing was being hidden TODAY — but a
  # library that failed to compile was also silent, and the only thing standing
  # between that and a wrong byte figure was a human reading "objects: 41". The
  # stream is kept now, and a non-empty one is announced. It is still not fatal:
  # deciding that a vendor warning stops the build is a ruling, not a default.
  CORE_ERR="$H/core_build.err"; : > "$CORE_ERR"
  OBJ=/tmp/pio_core; rm -rf $OBJ; mkdir -p $OBJ; cd $OBJ || exit 1
  for f in "$H"/ArduinoCore-avr/cores/arduino/*.c "$H"/ArduinoCore-avr/cores/arduino/*.S \
           "$H"/ArduinoCore-avr/libraries/Wire/src/utility/*.c; do
    [ -f "$f" ] && avr-gcc $CF $INC -c "$f" -o "$(basename "$f").o" 2>>"$CORE_ERR"; done
  LIBS=$(ls "$H"/ArduinoCore-avr/cores/arduino/*.cpp "$H"/ArduinoCore-avr/libraries/Wire/src/*.cpp \
            "$H"/ArduinoCore-avr/libraries/SPI/src/*.cpp "$H"/ArduinoCore-avr/libraries/HID/src/*.cpp 2>/dev/null | grep -v hooks)
  for d in $LIBDIRS; do
    if [ -d "$H/$d/src" ]; then LIBS="$LIBS $(ls "$H/$d"/src/*.cpp 2>/dev/null)"
    else LIBS="$LIBS $(ls "$H/$d"/*.cpp 2>/dev/null)"; fi; done
  for f in $LIBS "$H/shim.cpp"; do
    [ -f "$f" ] && avr-g++ $CXXF $INC -c "$f" -o "$(basename "$f").o" 2>>"$CORE_ERR"; done
  rm -f "$H/libcore_lto.a"
  avr-gcc-ar rcs "$H/libcore_lto.a" ./*.o      # gcc-ar: loads the LTO plugin
  echo "objects: $(ls ./*.o | wc -l)  -> $H/libcore_lto.a"
  if [ -s "$CORE_ERR" ]; then
    echo "core stderr: $(grep -c ': warning:' "$CORE_ERR") warning(s), $(grep -c ': error:' "$CORE_ERR") error(s)  -> $CORE_ERR"
  else
    echo "core stderr: clean"
  fi
  exit 0
fi

D="$1"; [ -d "$D" ] || { echo "no such dir: $D"; exit 2; }
build_includes; INC="$INC -I$D -I$D/include"
mkdir -p "$D/pbuild"; rm -f "$D/pbuild/fw.elf"
SRC=$(find "$D" -maxdepth 2 -name "*.cpp" -not -path "*/build/*" -not -path "*/pbuild/*")
# The error file used to be the FIXED path /tmp/pio_err.txt — one global name
# shared by every build on the box. byte_audit goes to the trouble of a fresh
# mkdtemp per payload precisely so no two builds can see each other's state, and
# this line handed that back. It lives beside its own build now. /tmp/pio_err.txt
# is still written as a compatibility copy for anyone with it in their fingers.
ERR="$D/pbuild/err.txt"
avr-g++ $CXXF $LDF $INC -o "$D/pbuild/fw.elf" $SRC "$H/libcore_lto.a" -lm 2>"$ERR"
cp "$ERR" /tmp/pio_err.txt 2>/dev/null
WARN=$(grep -c ': warning:' "$ERR")
if [ ! -f "$D/pbuild/fw.elf" ]; then echo "FAIL  $(grep -oE 'overflowed by [0-9]+ bytes' "$ERR" | head -1)"; exit 1; fi
read T Dd B <<< "$(avr-size "$D/pbuild/fw.elf" | tail -1 | awk '{print $1, $2, $3}')"
FL=$((T+Dd)); RM=$((Dd+B))
# warn= is APPENDED, never inserted. byte_audit reads this line with
# out.startswith("PASS") and a flash=(\d+) search; both survive a new trailing
# field and neither would survive a reordering. Keep it last.
if [ $FL -gt $CEIL_FLASH ]; then echo "OVER  flash=$FL  (+$((FL-CEIL_FLASH)) over $CEIL_FLASH)  ram=$RM  warn=$WARN"; exit 1; fi
echo "PASS  flash=$FL  ($((CEIL_FLASH-FL)) B spare)  ram=$RM/$CEIL_RAM  warn=$WARN"
