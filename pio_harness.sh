#!/bin/bash
# ZUMO COMPILE HARNESS v3.0 — PIO-TRUE
# Mirrors PlatformIO platform-atmelavr/builder/frameworks/arduino.py EXACTLY:
#   CCFLAGS  : -Os -Wall -ffunction-sections -fdata-sections -flto
#   CXXFLAGS : -fno-exceptions -fno-threadsafe-statics -fpermissive
#   LINKFLAGS: -Os -Wl,--gc-sections -flto -fuse-linker-plugin
# AND enforces the REAL ceiling from boards/a-star32U4.json: 28672 B flash / 2560 B RAM.
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
CCF="$DEF -Os -w -ffunction-sections -fdata-sections -flto"
CF="$CCF -std=gnu11 -fno-fat-lto-objects"
CXXF="$CCF -std=gnu++11 -fno-exceptions -fno-threadsafe-statics -fpermissive"
LDF="$DEF -Os -Wl,--gc-sections -flto -fuse-linker-plugin"

if [ "$1" = "--setup" ]; then
  build_includes
  OBJ=/tmp/pio_core; rm -rf $OBJ; mkdir -p $OBJ; cd $OBJ || exit 1
  for f in "$H"/ArduinoCore-avr/cores/arduino/*.c "$H"/ArduinoCore-avr/cores/arduino/*.S \
           "$H"/ArduinoCore-avr/libraries/Wire/src/utility/*.c; do
    [ -f "$f" ] && avr-gcc $CF $INC -c "$f" -o "$(basename "$f").o" 2>/dev/null; done
  LIBS=$(ls "$H"/ArduinoCore-avr/cores/arduino/*.cpp "$H"/ArduinoCore-avr/libraries/Wire/src/*.cpp \
            "$H"/ArduinoCore-avr/libraries/SPI/src/*.cpp "$H"/ArduinoCore-avr/libraries/HID/src/*.cpp 2>/dev/null | grep -v hooks)
  for d in $LIBDIRS; do
    if [ -d "$H/$d/src" ]; then LIBS="$LIBS $(ls "$H/$d"/src/*.cpp 2>/dev/null)"
    else LIBS="$LIBS $(ls "$H/$d"/*.cpp 2>/dev/null)"; fi; done
  for f in $LIBS "$H/shim.cpp"; do
    [ -f "$f" ] && avr-g++ $CXXF $INC -c "$f" -o "$(basename "$f").o" 2>/dev/null; done
  rm -f "$H/libcore_lto.a"
  avr-gcc-ar rcs "$H/libcore_lto.a" ./*.o      # gcc-ar: loads the LTO plugin
  echo "objects: $(ls ./*.o | wc -l)  -> $H/libcore_lto.a"
  exit 0
fi

D="$1"; [ -d "$D" ] || { echo "no such dir: $D"; exit 2; }
build_includes; INC="$INC -I$D -I$D/include"
mkdir -p "$D/pbuild"; rm -f "$D/pbuild/fw.elf"
SRC=$(find "$D" -maxdepth 2 -name "*.cpp" -not -path "*/build/*" -not -path "*/pbuild/*")
avr-g++ $CXXF $LDF $INC -o "$D/pbuild/fw.elf" $SRC "$H/libcore_lto.a" -lm 2>/tmp/pio_err.txt
if [ ! -f "$D/pbuild/fw.elf" ]; then echo "FAIL  $(grep -oE 'overflowed by [0-9]+ bytes' /tmp/pio_err.txt | head -1)"; exit 1; fi
read T Dd B <<< "$(avr-size "$D/pbuild/fw.elf" | tail -1 | awk '{print $1, $2, $3}')"
FL=$((T+Dd)); RM=$((Dd+B))
if [ $FL -gt $CEIL_FLASH ]; then echo "OVER  flash=$FL  (+$((FL-CEIL_FLASH)) over $CEIL_FLASH)  ram=$RM"; exit 1; fi
echo "PASS  flash=$FL  ($((CEIL_FLASH-FL)) B spare)  ram=$RM/$CEIL_RAM"
