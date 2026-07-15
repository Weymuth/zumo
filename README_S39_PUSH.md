# ZUMO S39 PUSH — L03 content pass + L01 book cover

Repo layout. Copy files to matching paths in the working tree, run the git rm lines, then push in the blocking order below.

## FILES IN THIS ZIP (what replaces what)

### images/  → github.com/Weymuth/zumo/images/
- L03_GRAPHIC_3-07_trim_flowchart.svg      FIXED (removed textLength that stretched the code line)
- L03_GRAPHIC_3-16_three_turn_types.svg    NEW (spin/pivot/swing)
- L03_GRAPHIC_3-17_number_line.svg         NEW (math number line)
- L03_GRAPHIC_3-18_gear_train.svg          NEW (side view + laddered cutaway)
- L03_IMAGE_3-16_gearmotor_gear_train.png  NEW (Pololu gearmotor, Feel the gearbox)
- L01_IMAGE_1-18_kr_c_programming_book.png OVERWRITES existing (paperback cover)

### lessons/ → Canvas
- Lesson_03.html   replaces live L03 (v03.1.2 -> v03.2.0, moderate bump)

## DELETIONS — a zip cannot delete. Run at push time:
```bash
git rm images/L03_IMAGE_3-14_astar_board.jpg
```
(Orphaned: removed from "Inside the can," replaced by GRAPHIC 3.18. Nothing else references it.)

## PUSH ORDER (blocking)
1. images/*  ->  images/     (SVGs + PNGs land FIRST — L03 references them)
2. lessons/Lesson_03.html -> Canvas
3. git rm the astar_board.jpg, commit, push
Reversing 1 and 2 = broken images for students.

## VERSION TRACKING (for LIVE.md, not filenames)
- L03: v03.1.2 -> v03.2.0   (in-file "Version 3" header unchanged — major digit only)
- L01: v03.2.3 -> v03.2.4   (image-only swap; Lesson_01.html NOT changed — the file already
  referenced L01_IMAGE_1-18; only the image bytes changed. No Lesson_01.html in this zip.)

## VERIFY AFTER PUSH (fresh clone)
```bash
git clone --depth 1 https://github.com/Weymuth/zumo.git
ls images/L03_GRAPHIC_3-16* images/L03_GRAPHIC_3-17* images/L03_GRAPHIC_3-18* images/L03_IMAGE_3-16*
test ! -e images/L03_IMAGE_3-14_astar_board.jpg && echo "board image removed OK"
grep -c "Blue = 75:1" lessons/Lesson_03.html   # expect 1
```

## L03 CHANGE MANIFEST (23 edits)
Graphics/photos: three-turns SVG after turns preview; number-line SVG at "Think of a Number
Line" tip; gearmotor photo in "Feel the gearbox"; A-Star board -> gear-train SVG in "Inside
the can" (board image dropped).
Corrections: gear-ratio color code Green 50:1 / Blue 75:1 / Red 100:1 (verified vs Pololu
User's Guide 0J63 sec 1.1); "Test Length" -> "test duration".
Prose: notebook adds (predict-bias, dead-reckoning, motor-test doc); TRIM-on-tape + notebook
(tape stays); floor tape -> Post-it (TRIM stays tape); "why 5/10 not smaller" explainer;
constrain nuance (library hard-caps at 400 like VEX; constrain protects YOUR math, not the
motor); elevated "ALWAYS STOP YOUR MOTORS" callout; coast/brake/hold explainer at motor-stop;
expanded stall-current tip (hold-the-wheels AND too-heavy-to-move are the same event);
first-open server-pulldown build note; riser coach tip.
Placeholders left for DJ: brushed/brushless explainer (sec 4.2); 3-Roombas Coach's Note (sec 4.5).
Inventory table updated: 3.14 marked removed; rows added for 3.16 photo, 3.16/3.17/3.18 graphics.

## NON-ISSUES CONFIRMED (no action)
- IMAGE 3.4  = dashed placeholder, still-needed screenshot (not broken).
- IMAGE 3.14 = was live; now intentionally removed (see git rm).
- "Where TRIM goes in your code" black block w/ stretched spacing = REAL DEFECT, now FIXED.
  It lives INSIDE GRAPHIC 3.7 (not the lesson HTML), lines 63-65. Cause: textLength="560" on
  the code line forced the monospace text to stretch, padding every character gap. Removed it;
  text now renders at natural width. (Earlier "cache ghost" call was wrong.)


## FLAGGED FOR A FUTURE SESSION (not fixed here)
`textLength` appears in 30 repo SVGs. It is only a DEFECT when the value exceeds the text's
natural width (forces character-gap stretching, as GRAPHIC 3.7 did). When it constrains text
to fit a box (value <= natural width), it is intentional and fine. Needs a per-file audit to
tell which are over-stretched vs. fit-to-width — a scoped session, not a blind find/replace.
Only GRAPHIC 3.7 (the one DJ spotted) is fixed in this push.


## ROOT DOCS IN THIS ZIP (repo root)
- ZUMO_SUPER_BIBLE.md      v8.24 -> v8.25 (NEW sec16 Hardware Ground Truth + sec17 SVG Canon)
- LIVE_ZUMO_TEXTBOOK.md    regenerated for S39 close (versions grepped from artifacts)
- ZUMO_S40_HANDOFF.md      paste at top of the S40 chat
