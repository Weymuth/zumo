#!/bin/sh
# harness_setup.sh v1.0.0 — rebuild the AVR compile harness from pinned upstream SHAs.
#
# WHY THIS FILE EXISTS. The harness is NOT in this repo (see the RULING note at the
# bottom), so every session that needs a byte figure has to rebuild it. Until S166 the
# recipe lived only in the session handoff — a document that is deleted and rewritten
# every session, which is precisely the failure mode ZUMO_AFTER_LAUNCH.md was opened to
# stop (S162). A recipe whose only home is a file the next session overwrites is not a
# recipe. It also drifted: the S146 handoff named two libraries that were never cloned
# and omitted two that were, which is why Bible §16.36 says to read LIBDIRS out of
# pio_harness.sh rather than out of any handoff.
#
# WHY THE SHAs ARE PINNED. An unpinned clone makes the byte figures in this book a
# function of what upstream did this week. The eight standing byte controls only mean
# something against a fixed toolchain AND a fixed library set. If a pin below is moved,
# every control must be re-reproduced before any figure is trusted (rule 30).
#
#   ./harness_setup.sh          (the target dir is read out of pio_harness.sh)
#
# Correct setup prints "objects: 41". Then: python3 byte_audit.py --sizes, then --check.

set -e
HERE="$(cd "$(dirname "$0")" && pwd)"

# The target is DERIVED from pio_harness.sh, not accepted as an argument. An earlier
# draft of this script took a target directory, cloned into it, and then ran
# pio_harness.sh --setup -- which hardcodes its own H and therefore built the core
# somewhere else entirely, reporting "objects: 41" against a directory the caller had
# never named. A script whose argument silently does not reach the thing it configures
# is worse than one with no argument (§24.8). One home for the path, and it is there.
H=$(sed -n 's/^H=\(.*\)$/\1/p' "$HERE/pio_harness.sh")
[ -n "$H" ] || { echo "FAIL: could not read H out of pio_harness.sh"; exit 1; }
echo "harness dir (read from pio_harness.sh): $H"

# repo <TAB> pinned SHA.  Verified S166: this set builds and reproduces all eight
# standing controls, L11 after_step_1 = 20,592 first (rule 30).
REPOS="
zumo-32u4-arduino-library	f4dfe054e23176ba445748b4b91f463701e7eb76
pololu-buzzer-arduino	ad19e6e2aa37512ddc78b655d20e8ec2bcdbd0e3
pololu-oled-arduino	e6b83b6c181962ffb98f99a4a4c3fd7cbf7e6707
pololu-menu-arduino	8970b8db6e4e80b1c0e95172a87a35410bf593bf
pushbutton-arduino	79f501e6ea5399c02bd46c681585ae10f602f7b5
fastgpio-arduino	3d705ed8bf5fd1fd1179591cbbf80c6da44eaa7e
usb-pause-arduino	bc662383d3e9d66854b5c95890e7e83caeebb21b
pololu-hd44780-arduino	1fe2a6afc5b20a7897679e141348802d3d03435f
"
CORE_SHA=11b9130371e8447920edb65a75706a6c951e51fc

echo "== toolchain =="
if ! command -v avr-gcc >/dev/null 2>&1; then
  # There is no sudo on the container. apt-get sat on 'Reading package lists' for
  # ~5 minutes when backgrounded at S163 and finished in seconds in the foreground —
  # run this in the FOREGROUND.
  apt-get install -y gcc-avr avr-libc binutils-avr
fi
avr-gcc --version | head -1

echo "== libraries -> $H (FLAT; ArduinoCore-avr at the TOP LEVEL, not under arduino/) =="
mkdir -p "$H"
cd "$H"
echo "$REPOS" | while IFS='	' read -r repo sha; do
  [ -z "$repo" ] && continue
  if [ -d "$repo/.git" ]; then
    echo "  = $repo (present)"
  else
    git clone -q "https://github.com/pololu/$repo.git" "$repo"
    ( cd "$repo" && git checkout -q "$sha" )
    echo "  + $repo @ $(echo "$sha" | cut -c1-9)"
  fi
done
if [ -d ArduinoCore-avr/.git ]; then
  echo "  = ArduinoCore-avr (present)"
else
  git clone -q https://github.com/arduino/ArduinoCore-avr.git
  ( cd ArduinoCore-avr && git checkout -q "$CORE_SHA" )
  echo "  + ArduinoCore-avr @ $(echo "$CORE_SHA" | cut -c1-9)"
fi

echo "== the LIBDIRS the harness declares must all be present =="
# DERIVED from pio_harness.sh, never typed here (rule 19): if that script's library
# list changes, this check fails rather than silently building a different harness.
LIBDIRS=$(sed -n 's/^LIBDIRS="\(.*\)"$/\1/p' "$HERE/pio_harness.sh")
[ -n "$LIBDIRS" ] || { echo "FAIL: could not read LIBDIRS out of pio_harness.sh"; exit 1; }
miss=0
for d in $LIBDIRS ArduinoCore-avr; do
  [ -d "$H/$d" ] || { echo "  MISSING: $d"; miss=1; }
done
[ "$miss" = 0 ] || { echo "FAIL: pio_harness.sh declares a library this script does not clone."; exit 1; }
echo "  all $(echo $LIBDIRS | wc -w) declared LIBDIRS present, plus ArduinoCore-avr"

echo "== core build =="
cp "$HERE/pio_harness.sh" "$H/"
cd "$H"
bash pio_harness.sh --setup

cat <<'EOF'

Expected above: "objects: 41". Anything else means the library set is wrong.

Next, and in this order:
  python3 byte_audit.py --sizes        # compiles every payload the Maker defines
  python3 byte_audit.py --check        # six arms
  python3 byte_audit.py --selftest     # nine controls; run this before trusting --check

RULE 30: reproduce the standing control BEFORE trusting any other figure.
CONTROL A does exactly that and its constant is byte_audit.STANDING_CONTROL.

RULING, S166 — WHY THE HARNESS IS NOT VENDORED INTO THIS REPO.
Measured rather than assumed: a full vendoring is 746 files and 27 MB, of which
ArduinoCore-avr is 25 MB and roughly 24 MB of THAT is firmwares/, drivers/ and
bootloaders/ that this build never opens. The subset the harness actually includes is
about 2 MB. Two things stop the trim from being an easy win: deletions in this repo go
through GitHub Desktop by hand, so 746 files is expensive to undo (§24.17's
recoverability carve-out); and ArduinoCore-avr ships NO licence file at its root, so
vendoring a partial copy is a licensing question and not an engineering one. All eight
Pololu repos do carry LICENSE.txt. This script is the cheap half of the answer: the
recipe is now IN the repo, pinned, and testable, without any of that being decided.
EOF
