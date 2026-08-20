# SHOT BRIEF — the week-one figures

**Shot brief version: v1.2** — increment on every substantive edit. The version lives ONLY in
this line. (v1.0 was the S110 original; v1.1 the S179 six-feet amendment below; v1.2 corrects the
filename claim, which was stricter than the matcher.)

**Six shots. Two need nothing but a laptop; three need one floor rig; one needs both.**
Everything a student sees in periods 2–4 depends on these. Written S110 against
`IMAGE_WORKLIST.md` and the live lesson prose, not from memory.

**Filenames are not optional — but only the PREFIX is load-bearing.** `image_audit.py` matches
`^L{NN}_{KIND}_{N}-0*{n}_`, so everything after that trailing underscore is a free slug.
**Tested against the matcher itself at S179**, not read: `L03_IMAGE_3-02_testing_setup_floor`
and `L03_IMAGE_3-02_recommended_motor_testing_setup_sh` BOTH match, which is why this brief
and `IMAGE_SHOT_LIST.md` can name different slugs for one shot without either being wrong.
What the matcher genuinely rejects: an unpadded lesson number (`L3_`), the wrong kind
(`GRAPHIC` for an `IMAGE` tag), and a name with **no slug at all** (`L03_IMAGE_3-02.jpg`),
because the trailing underscore is required. Save as written below and you cannot go wrong;
the older *any other name reads as no asset* overstated it.

All six names were run against the matcher itself, with four deliberately wrong names as a
control: an unpadded lesson number, the wrong kind, and a name with no slug were all
rejected. **The one thing the matcher does NOT enforce is zero-padding** — `3-6` passes as
readily as `3-06`, because the pattern allows zero or more zeros. Padding is convention held
by eye alone, so match the names below exactly rather than trusting the audit to catch it.

---

## Before you shoot: one row is not a shot

**`[IMAGE 3.14]` needs no photograph.** The tag appears exactly once in L03, inside the
figure table's own row, which reads *"removed from 'Inside the can' — replaced by GRAPHIC
3.18."* `L03_GRAPHIC_3-18_gear_train.svg` exists and the lesson prints `GRAPHIC 3.18` three
times. The audit counts it as planned because it cannot tell a retirement note from a plan.

**Ruling needed, one line:** either the row loses its bracketed tag, or `image_audit`
learns to skip a tag whose row is marked removed. Until then the outstanding count is
inflated by one and so is the deadline. *(Lead, not a finding: 3.14 was a board photo and
3.18 is a gear-train diagram — different subjects. The "replaced by" claim may itself be
loose wording. Worth a look when the row is ruled; it does not change that no photo is due.)*

---

## GROUP 1 — desk only, no robot, can be done tonight

### `[IMAGE 2.5]` → `L02_IMAGE_2-05_vscode_completed_lesson2.png`
**Where:** L02 Quick Reference. **Promised:** VS Code with the completed Lesson 2 code, full
program.

The figure sits directly above the **Code Anatomy (in order)** list — header comment,
`#include`, hardware objects, constants, `setup()`, `loop()`, helper functions. The reader is
meant to run their eye down that list and find each item in the screenshot.

- **The whole program must be in frame, closing brace included.** If it will not fit, drop the
  editor font size — do not crop. A cropped program silently breaks the list beneath it.
- Editor pane only. Collapse the sidebar and the terminal.
- Check the title bar and any open tabs for personal paths before you save.

### `[IMAGE 3.4]` → `L03_IMAGE_3-04_build_success_terminal.png`
**Where:** L03 Step 12, Build the Code. **Promised:** build and upload success messages in
the terminal.

The DO THIS NOW immediately above says *look for SUCCESS in the terminal output*, so SUCCESS
has to be legible in the frame — that is the whole job of the picture.

- Include the RAM / Flash usage lines. The book tracks byte counts elsewhere and a student
  comparing their numbers to yours is doing exactly what STILL GREEN asks.
- Build clean first. A cached "nothing to do" build does not show what the step describes.
- Terminal panel only, full width.

---

## GROUP 2 — one floor rig clears all three

**Rig once:** smooth floor, a clear stretch in the driving direction, no table legs, tape
starting line down, Post-its for landing marks, robot on fresh batteries, USB to the laptop.

**AMENDED S179 — DO NOT STAGE SIX FEET.** DJ ruled that students do not need 6+ feet of clear
floor, and the figure was DELETED from L03 in four places rather than corrected (Bible rule 50).
The motor test is `TEST_DURATION` **2000 ms at `BASE_SPEED` 200** — a two-second run at half
speed. **A photo staged to the old brief would put the deleted figure back into the book as a
picture, and nothing in this repo reads inside an image.** Stage what the run actually needs.

**The surface is not a preference.** The WARNING sitting directly above `[IMAGE 3.5]` tells
students to test on tile, hardwood or linoleum and warns that carpet skews TRIM. A photo of
a robot on carpet would contradict the warning printed on the same screen.

### `[IMAGE 3.2]` → `L03_IMAGE_3-02_testing_setup_floor.jpg`
**Where:** L03 §4.4, Physical Setup for Motor Testing. **Promised:** the recommended setup,
clear floor space with a tape starting line.

This one is **the space, not the run.** Robot not yet placed, or set aside at the edge. It
answers *"what does a clear test lane look like?"* — **not** *"how many feet do I need?"*, which
is the question the deleted figure used to answer. Shoot from behind and low enough that the
depth reads, and frame a lane that is plainly clear rather than plainly long. Include the
Post-it landing markers the NOTE describes.

**The caption this must match is L03 §4.4's live text:** *Some clear space to drive in — the
test run is short.* If the photograph reads as a corridor, it disagrees with the prose it sits
beside.

### `[IMAGE 3.5]` → `L03_IMAGE_3-05_robot_at_start_line.jpg`
**Where:** L03 §7, Test It. **Promised:** robot on the floor, tape starting line, clear path
ahead.

Same rig, **robot now placed and powered** — nose on the tape, OLED lit, path open in front.
It answers *"am I set up right?"* immediately before the verification checklist.

> **3.2 and 3.5 are close enough to question.** Two tags need two files under §10, and the
> before/after split above is a real difference — but if you would rather carry one figure,
> that is a ruling that deletes a row, the same shape as the `[IMAGE 7.13]` question still
> open in the queue. Shoot both while the rig is up; ruling later costs nothing, re-rigging does.

### `[VIDEO 3.1]` → `L03_VIDEO_3-01_crooked_vs_straight.mp4`
**Where:** L03 §1, The Crooked Robot Problem — the first thing in the lesson. **Promised:** a
robot curving without TRIM, then driving straight with TRIM applied.

The prose right after it describes a slow sad curve to the left at speed 200 with both motors
commanded equally. The video has to make that curve unmistakable.

- **Two runs, same start line, same speed**, TRIM 0 then TRIM applied. One continuous take if
  you can manage it; the cut is what students will distrust.
- Camera fixed and elevated, looking **down the length of the run** so lateral drift reads
  against the tape. A side-on shot hides the very thing being demonstrated.
- 10–15 seconds is plenty.

---

## GROUP 3 — robot and laptop together, straight after Group 2

### `[IMAGE 3.6]` → `L03_IMAGE_3-06_serial_trim_log.png`
**Where:** L03 §7, after the Motor Behavior checklist. **Promised:** a Serial Monitor log of
several test runs with TRIM adjustments, 0 → 15.

Directly beneath it is the trial table students fill in — Trial # / Speed / TRIM tried /
Observed / New TRIM. **The log in the screenshot should look like the table beneath it:** at
least three or four Button B trials with TRIM actually changing between them.

- Capture this from the real runs you just did on the floor. A fabricated log will not match
  the convergence story the table teaches.
- Serial Monitor panel only, enough scrollback that the trials read as a sequence.

---

## Order of work

1. **Tonight, no robot:** `2.5`, `3.4`.
2. **Bench session, rig up once:** `3.2` (space), `3.5` (robot placed), `VIDEO 3.1` (two runs).
3. **Same session, laptop still attached:** `3.6` from those runs.
4. **Not a shot:** `3.14` — rule the row instead.

After the files land, `python3 image_audit.py --check` regenerates `IMAGE_WORKLIST.md`;
outstanding should fall from 18 to 12. If a file does not clear, the filename is wrong before
anything else is.
