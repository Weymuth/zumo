<!-- ZUMO_BELL_RINGERS.md v1.0 — S201. Spoken review questions, one set per lesson, for the first
     few minutes of the period. DJ asked for all sixteen; L01 is built and L02–L16 are S202's job.

     NO YEAR LAYER ON PURPOSE. This file keys to LESSONS, not to the calendar — no dates, no period
     numbers, no roster size — so it is not an `_F26` file and is not rewritten every August. It is
     the lesson versions it goes stale against, which is why every set carries a SOURCE PIN, the
     same way a quiz bank does.

     NOT REGISTERED with session_versions yet. Until it is, a pin going stale is invisible to every
     instrument. See the S202 job list at the foot of this file. -->

# Bell-Ringer Questions
### Spoken review, one set per lesson · read the pin before you trust a set

---

## How these are built

**These are for saying out loud, not for printing.** The bell-ringer is the first few minutes of the
period and it is driven by what the reading quiz says the class missed — so this is a bank to pull
from, not a script to run.

Five rules the sets follow:

1. **Ask *why*, not *what was on line four*.** A question whose answer is a remembered noun tells you
   nothing. A question whose answer is a reason tells you everything.
2. **Every question carries what to LISTEN FOR**, and where there is one, the **wrong answer worth
   catching** — because the value of asking out loud is hearing the misconception, not scoring.
3. **Nothing is reused verbatim from a quiz bank.** The banks ship items in rehearsal/variant pairs;
   speaking one aloud burns both. Same concepts, different questions.
4. **At least one question per set is about the thing they will get wrong in the next hour**, not
   the thing that is most interesting. Put it last so it lands right before build time.
5. **A set is pinned to the lesson version it was written against.** Lesson prose moves; a question
   built on prose that moved is a question with a wrong answer, which is worse than no question.

**Reading a pin.** If the lesson's `<!-- Lesson version: -->` is ahead of the pin below, the set
has not been re-read since that lesson changed. It is probably still fine. It is not verified.

---

# Lesson 1 — Hello, Robot!

**Source pin: `lesson_01: v03.33.0`** · built S201 · 12 questions

## The concept

**1. "Is a remote-control car a robot? Why not?"**
*Listen for:* a human makes the decisions; the car just obeys.
*Follow-up if they answer fast:* "What about your phone?" — it computes, but it does not physically
act on the world on its own.

**2. "Where in your program does the SENSE → DECIDE → ACT loop actually live?"**
*Listen for:* `loop()`.
*Wrong answer worth catching:* `setup()`. Lesson 1 is the exception, not the rule, and a student who
generalises from it will fight Lesson 3.

## The three names

**3. "Name the board. Name the chip. Now tell me what `a-star32U4` is."**
*Listen for:* board = **Zumo 32U4 OLED Main Board** · chip = **ATmega32U4** · `a-star32U4` = the
**build target**, not hardware.
*Wrong answer worth catching:* any student who thinks they own an A-Star board. §3.3 says outright
that the robot does not contain one.

**4. "Then why does a board name for hardware you do not own work at all?"**
*Listen for:* same chip, same bootloader, so the profile fits.

## The recipe card

**5. "`lib_deps` downloads the library. So what is `#include <Zumo32U4.h>` for — isn't that the same
job twice?"**
*Listen for:* two different jobs — one fetches it to the computer, the other pours it into *this*
program.
*Why it matters:* a student who cannot separate those cannot read their first failed build.

**6. "`monitor_speed = 115200`. If I delete that line, does the Serial Monitor break on this robot?"**
*Listen for:* no — the Zumo talks over native USB and sets its own speed. It is a formality here and
a real requirement on an Uno.
*Good bell-ringer* precisely because the honest answer is *it does not matter here, and it would
somewhere else.*

**7. "Why is the library pinned to `@2.0.1` instead of just taking the newest?"**
*Listen for:* anything about everyone building the same thing, or a version changing underneath you.

## The skeleton

**8. "What does `void` mean — and what would be there instead if it weren't `void`?"**
*Listen for:* returns nothing; a type, for a function that answers a question.
*The second half is the whole question.* It separates memorised from understood.

**9. "`setup()` runs once and `loop()` runs forever. So why did we put the entire show in `setup()`?"**
*Listen for:* we only want it once.

## Build, upload, and tomorrow

**10. "You unplug the robot tonight. Tomorrow you switch it on with no laptop anywhere. What happens?"**
*Listen for:* it runs the same program — flash keeps its contents with the power off.
*Follow-up:* "How many programs does the chip hold?" — exactly one; every upload overwrites the last.

**11. "What is the difference between clicking the checkmark and clicking the arrow?"**
*Listen for:* Build makes a binary on your computer; Upload copies it down the cable into flash.
Engineers call it flashing.

**12. "You opened the Serial Monitor and saw nothing. What did you do wrong?"**
*Listen for:* pressed A before the monitor connected. The robot says hello *the moment* A is pressed.
**This is rule 4's question — ask it even if they answer everything else cold, because it is the one
they will actually hit.**

---

# Lessons 2–16 — NOT BUILT

**S202's job.** Nothing below this line exists yet. Do not improvise a set in the room from this
file — there is nothing here to improvise from.

| Lesson | Pin to build against | Status |
|---|---|---|
| L02 Read Code | `v03.27.0` | not built |
| L03 Motors & TRIM | `v03.48.0` | not built |
| L04 Line Sensors | `v04.31.0` | not built |
| L05 Proximity | `v04.31.0` | not built |
| L06 Encoders | `v04.38.0` | not built |
| L07 Code Organization | `v04.34.0` | not built |
| L08 Line Following | `v04.35.0` | not built |
| L09 Intersections | `v05.30.0` | not built |
| L10 Obstacles | `v02.31.0` | not built |
| L11 Time Lies | `v02.32.0` | not built |
| L12 Wheels Lie | `v01.36.0` | not built |
| L13 Rescue Zone | `v02.40.0` | not built |
| L14 Competition | `v02.37.0` | not built |
| L15 PID | `v02.33.0` | not built |
| L16 Showcase | `v02.29.0` | not built |

**Pins above are the versions live at S201 close.** Re-grep before building a set — do not build
against a number copied out of this table.

---

## S202 job list for this file

1. **Build L02 and L03 first.** L03 is the next lesson with a bell-ringer that has to carry weight,
   and L02 is short.
2. **Register the file with `session_versions.py`** so the pins are visible to `--check`. Right now a
   stale pin is invisible to every instrument in the repo, which makes rule 5 a promise nobody keeps.
   `going_deeper.html` and `index.html` have the same gap.
3. **Decide whether the pins want a gate.** `quiz_bank` already asserts that a bank's `lesson_NN:`
   pin matches the live lesson. The same arm over this file would be cheap and would make rule 5 real.
4. **Cross-check against the banks once L02+ exist** — rule 3 is currently kept by hand.

---
*Bell-ringer bank · lesson-keyed, no calendar · ZUMO · Sense, Decide, Act*
