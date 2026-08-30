#!/usr/bin/env bash
# ZUMO §24.22 TRIPWIRE — install with:  bash tools/no_text_match.sh install
#
# WHY THIS EXISTS. §24.22 was ruled at S182, re-ruled at S186 with `census.py`
# behind it, and violated again at S196 — the fifth recurrence of the family.
# Every previous fix made the RIGHT call POSSIBLE. None made the WRONG call
# UNAVAILABLE, so the reflex kept winning.
#
# WHAT IT DOES. Shadows grep/egrep/fgrep/rg in /usr/local/bin, which precedes
# /usr/bin. A text match against REPO CONTENT stops with a nonzero exit and names
# the parser to use instead. A text match against anything else — /tmp, pip output,
# a build log, this script's own install check — passes straight through, because
# the ruling is about the BOOK, not about the shell.
#
# WHAT IT DOES NOT DO, STATED SO NOBODY MISTAKES IT FOR A GUARANTEE:
#   - It does not survive a container rebuild. It is a session-open step.
#   - It does not stop Python's `re` against raw bytes, which is the same defect
#     in a language the shim cannot see. §24.22 covers that; this does not.
#   - It is a TRIPWIRE, not a proof. It converts a silent reflex into a loud stop.

set -euo pipefail

REAL_GREP=/usr/bin/grep

if [ "${1:-}" = "install" ]; then
  for tool in grep egrep fgrep rg; do
    cat > "/usr/local/bin/$tool" <<'SHIM'
#!/usr/bin/env bash
# ZUMO §24.22 tripwire. Real binary: /usr/bin/grep
#
# DENY BY DEFAULT. The first version of this shim tested whether any ARGUMENT
# looked like repo content - an ALLOWLIST, firing only on shapes anticipated in
# advance, which is the exact defect §24.22 exists to name. It leaked two ways on
# the first adversarial pass: `grep -rn PAT .` (no repo-shaped operand) and
# `cat FILE | grep PAT` (no operand at all). Both read the book; both passed.
#
# The rule is now about WHERE YOU ARE STANDING, not what you typed: inside the
# repo, a text match is refused unless every operand is an existing path OUTSIDE
# it. Silence means every form has been refused or excused, not that one pattern
# happened to match.
[ -n "${ZUMO_ALLOW_TEXT_MATCH:-}" ] && exec /usr/bin/grep "$@"

# repo root = nearest ancestor holding the Bible
d="$PWD"; root=""
while [ "$d" != "/" ]; do
  if [ -f "$d/ZUMO_SUPER_BIBLE.md" ]; then root="$d"; break; fi
  d="$(dirname "$d")"
done
[ -z "$root" ] && exec /usr/bin/grep "$@"      # not in the repo at all

# Every non-flag operand that EXISTS and resolves OUTSIDE the repo is fine.
# A pattern is an operand too, so "exists" is the test, never "looks like".
outside_only=1; sawfile=0; prev=""
for a in "$@"; do
  case "$prev" in -e|-f|--regexp|--file) prev=""; continue ;; esac
  prev="$a"
  case "$a" in -*) continue ;; esac
  if [ -e "$a" ]; then
    sawfile=1
    rp="$(cd "$(dirname "$a")" 2>/dev/null && pwd -P)/$(basename "$a")"
    case "$rp" in "$root"/*|"$root") outside_only=0 ;; esac
  fi
done
# No file operand at all means STDIN - and stdin inside the repo is almost always
# the book arriving through a pipe, which is how leak B worked.
[ "$sawfile" = "1" ] && [ "$outside_only" = "1" ] && exec /usr/bin/grep "$@"

cat >&2 <<'MSG'
=============================================================================
 §24.22 STOP — text match on repo content is ruled against.
 Ruled S182. Re-ruled S186 with census.py. Violated again S196. Five times.

 A text match LOCATES CANDIDATES AND NEVER ANSWERS, and a ZERO from one is
 not evidence of absence — the book uses curly apostrophes, and `.` matches
 one of their three UTF-8 bytes.

 USE INSTEAD (import works plainly from the repo root):
   import census;            census.rendered(pat, 'lessons/Lesson_*.html')
   census.occurrences(pat, paths) / census.lines(pat, paths)
   census.questions(pat)     # question IDs, not lines
   census.payloads(token)    # payload entries
   import lesson_inventory;  lesson_inventory.count_across(pat)

 Deliberate, justified exception:  ZUMO_ALLOW_TEXT_MATCH=1 grep ...
 Non-repo file: pass its path; operands outside the repo are always allowed.
=============================================================================
MSG
# census is importable from the REPO ROOT only, and this shim fires from
# subdirectories too - so name the root instead of leaving a dead instruction.
echo " Run the parser from:  cd $root" >&2
echo "=============================================================================" >&2
exit 3
SHIM
    chmod +x "/usr/local/bin/$tool"
  done
  echo "installed: /usr/local/bin/{grep,egrep,fgrep,rg}"
  exit 0
fi

if [ "${1:-}" = "uninstall" ]; then
  rm -f /usr/local/bin/grep /usr/local/bin/egrep /usr/local/bin/fgrep /usr/local/bin/rg
  echo "removed"
  exit 0
fi

if [ "${1:-}" = "selftest" ]; then
  # errexit OFF for the duration: these controls EXPECT non-zero exits, and with
  # `set -e` the suite killed itself after the first passing control.
  set +e
  ok=1
  refused(){ "$@" >/dev/null 2>&1; [ $? -eq 3 ]; }
  must_refuse(){ d="$1"; shift; if refused "$@"; then echo "   PASS  $d"; else echo "   FAIL  $d - ALLOWED"; ok=0; fi; }
  must_allow(){ d="$1"; shift; if refused "$@"; then echo "   FAIL  $d - REFUSED"; ok=0; else echo "   PASS  $d"; fi; }

  # THE TWO THAT LEAKED. The first shim tested ARGUMENT SHAPE - an allowlist - and
  # both of these read the book while matching none of its patterns. They are the
  # first two controls precisely because they were not anticipated.
  must_refuse "A recursive bare dot (leaked in v1)"  grep -rn Engineer .
  echo "hi" > /tmp/_tw.txt
  cat lessons/Lesson_06.html | grep -c Engineer >/dev/null 2>&1
  if [ $? -eq 3 ]; then echo "   PASS  B stdin pipe (leaked in v1)"
  else echo "   FAIL  B stdin pipe - ALLOWED"; ok=0; fi
  ( cd lessons && grep -c Engineer Lesson_06.html >/dev/null 2>&1 )
  if [ $? -eq 3 ]; then echo "   PASS  C from a repo subdirectory"
  else echo "   FAIL  C from a repo subdirectory - ALLOWED"; ok=0; fi
  must_refuse "D direct repo path"    grep -c Engineer lessons/Lesson_06.html
  must_refuse "E glob operand"        grep -c Engineer lessons/Lesson_0*.html
  must_refuse "F absolute repo path"  grep -c Engineer "$PWD/lessons/Lesson_06.html"
  must_refuse "G markdown register"   grep -c Bible ZUMO_SUPER_BIBLE.md
  must_refuse "H egrep alias"         egrep -c Engineer lessons/Lesson_06.html

  # A TRIPWIRE THAT BLOCKS EVERYTHING GETS UNINSTALLED, AND THEN IT GUARDS NOTHING.
  must_allow "I non-repo operand"     grep -c hi /tmp/_tw.txt
  if ZUMO_ALLOW_TEXT_MATCH=1 grep -c Engineer lessons/Lesson_06.html >/dev/null 2>&1
    then echo "   PASS  J documented escape hatch works"
    else echo "   FAIL  J escape hatch blocked"; ok=0; fi

  # THE CONTROL MUST BE ABLE TO FAIL: the real binary must still read the repo, or
  # every refusal above proves only that the path is broken.
  if /usr/bin/grep -q html lessons/Lesson_01.html
    then echo "   PASS  K /usr/bin/grep still reads the repo (refusals are the shim)"
    else echo "   FAIL  K real binary cannot read the repo"; ok=0; fi

  [ "$ok" = "1" ] && echo "  TRIPWIRE CONTROLS PASS" || echo "  CONTROL FAILURE"
  [ "$ok" = "1" ] || exit 1
  exit 0
fi

echo "usage: bash tools/no_text_match.sh {install|selftest|uninstall}"
exit 2
