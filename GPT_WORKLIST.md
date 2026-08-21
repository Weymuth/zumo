# GPT graphics work list (generated)

Work list session: S180 · `build_worklist.py v1.2` · `svg_layout_audit v1.20`

**38 files** needing a human, from an audit of all SVGs in `images/`.
Worst-first by how far text runs outside its panel.

**Do not hand-edit — regenerate.** Any list built against an audit below v1.18 was
ordered by font sizes the tool could not read and should be discarded.

Mechanical defects are NOT here — plain `href`, dead alpha, designer font stacks and
files over the gate 37 ceiling are fixed locally by `svg_layout_audit`, `flatten_alpha`
and `fit_raster_svg`. They are listed at the end so the backlog stays visible.

Send one file at a time. Attach the SVG, paste its block, bring the result back before
moving on.

13 of these 38 have text outside a panel; the rest are structural.

## L07_GRAPHIC_7-15_platformio_file_tree.svg
*worst overflow: 128 units*

- text overflows its panel by 3 units: "RobotSensors.h" spans 220..375 inside 18..378
- text overflows its panel by 107 units: "Put your header files (.h) here" spans 560..880 inside 1..779
- text overflows its panel by 128 units: "Put your source files (.cpp) here" spans 560..901 inside 1..779

## L07_GRAPHIC_7-04_how_files_connect.svg
*worst overflow: 105 units*

- text overflows its panel by 16 units: "void driveDistance(float);" spans 468..702 inside 434..692
- text overflows its panel by 105 units: "“What may I call?”" spans 328..433 inside 76..334
- text overlaps text at y=344: "void driveDistance(float);" ends 702, "“Here is how.”" starts 696

## L14_GRAPHIC_14-04_competition_mode.svg
*worst overflow: 70 units*

- text overflows its panel by 70 units: "match. The compiler deletes the delays outri" spans 400..1084 inside 80..1020

## L09_GRAPHIC_9-6_fsm_uml.svg
*worst overflow: 61 units*

- text overflows its panel by 61 units: "The filled dot is the initial state: the rob" spans 120..1065 inside 90..1010

## L05_GRAPHIC_5-02_emit_reflect_detect.svg
*worst overflow: 48 units*

- text overflows its panel by 48 units: "Like picking a friend out of a crowd because" spans 586..1082 inside 560..1040
- text overflows its panel by 9 units: "That is Bonus Mystery 5. It is a bug you can" spans 586..1043 inside 560..1040
- 4 numbered markers but no callout-* groups - they are grouped by object type, so moving one marker means hunting its parts across the layer

## L16_GRAPHIC_16-01_three_memories.svg
*worst overflow: 31 units*

- text overflows its panel by 31 units: "the sensors rent ~960 B of it (heap)" spans 410..690 inside 435..665

## L14_GRAPHIC_14-03_how_a_run_is_scored.svg
*worst overflow: 27 units*

- text overflows its panel by 27 units: "It can FIND a silver victim (Lesson 13). It " spans 115..1031 inside 90..1010

## L11_GRAPHIC_11-03_line_sensor_array.svg
*worst overflow: 26 units*

- text overflows its panel by 26 units: "Line sensors" spans 982..1078 inside 42..1058

## L09_GRAPHIC_9-1_robocup_course.svg
*worst overflow: 24 units*

- text overflows its panel by 6 units: "GO_LEFT — take the left branch" spans 780..1050 inside 720..1050
- text overflows its panel by 24 units: "GO_RIGHT — take the right branch" spans 780..1068 inside 720..1050
- 6 numbered markers but no callout-* groups - they are grouped by object type, so moving one marker means hunting its parts across the layer

## L12_GRAPHIC_12-02_measuring_the_lie.svg
*worst overflow: 13 units*

- text overflows its panel by 13 units: "-19" spans 1032..1057 inside 50..1050

## L06_GRAPHIC_6-10_function_anatomy.svg
*worst overflow: 12 units*

- text overflows its panel by 12 units: "How you call the function from anywhere in t" spans 596..1046 inside 570..1040
- 8 numbered markers but no callout-* groups - they are grouped by object type, so moving one marker means hunting its parts across the layer

## L09_GRAPHIC_9-2_green_sensor_values.svg
*worst overflow: 3 units*

- text overflows its panel by 3 units: "BLACK — near 1000" spans 869..1043 inside 54..1046

## L12_GRAPHIC_12-03_the_square_that_closes.svg
*worst overflow: 3 units*

- text overflows its panel by 3 units: "END — nowhere near" spans 48..176 inside 45..525

## L11_GRAPHIC_11-05_battery_strength_changes_the_outcome.svg

- leader of callout-3 crosses the box of callout-1
- leader of callout-3 crosses the box of callout-1
- leader of callout-3 crosses the box of callout-1
- highlight box of callout-1 overlaps that of callout-3
- highlight box of callout-1 overlaps that of callout-3
- highlight box of callout-1 overlaps that of callout-3

## L03_GRAPHIC_3-11_command_anatomy.svg

- text overlaps text at y=160: "motors" ends 322, "." starts 315
- text overlaps text at y=160: "." ends 330, "setSpeeds" starts 328
- text overlaps text at y=160: "setSpeeds" ends 458, "(leftSpeed, rightSpeed);" starts 447
- 8 numbered markers but no callout-* groups - they are grouped by object type, so moving one marker means hunting its parts across the layer

## L01_GRAPHIC_1-19_playfrequency_anatomy.svg

- text overlaps text at y=163: "buzzer" ends 228, "." starts 222
- text overlaps text at y=163: "playFrequency" ends 474, "(" starts 470

## L05_GRAPHIC_5-03_two_led_system.svg

- text overlaps text at y=211: "(one of the LEFT pair)" ends 463, "the only ear — there is ju" starts 457
- text overlaps text at y=211: "the only ear — there is ju" ends 643, "(one of the RIGHT pair)" starts 632

## L05_GRAPHIC_5-07_the_dead_spot.svg

- 2 rotated/skewed <text> NOT checked for overflow or collision - this tool measures horizontal extent only. Eyeball them.
- 3 numbered markers but no callout-* groups - they are grouped by object type, so moving one marker means hunting its parts across the layer

## L05_GRAPHIC_5-10_jumper_positions.svg

- box aspect 2.627 vs photo aspect 3.606 - the picture is letterboxed or distorted inside its box; resize the box to match
- box aspect 2.627 vs photo aspect 3.195 - the picture is letterboxed or distorted inside its box; resize the box to match

## L01_GRAPHIC_1-11_sense_decide_act.svg

- 6 numbered markers but no callout-* groups - they are grouped by object type, so moving one marker means hunting its parts across the layer

## L02_GRAPHIC_2-05_sketch_anatomy.svg

- 7 numbered markers but no callout-* groups - they are grouped by object type, so moving one marker means hunting its parts across the layer

## L02_GRAPHIC_2-07_ir_sensors.svg

- photograph is 1750x190 but its box renders about 964 CSS px wide (box 1752 of a 2000 viewBox at a 1100 px column) = 1.82x - under the 2x floor. Needs a source at least 1927 px wide.

## L02_IMAGE_2-07_ir_sensors_r02.svg

- photograph is 1833x858 but its box renders about 1100 CSS px wide (box 916 of a 916 viewBox at a 1100 px column) = 1.67x - under the 2x floor. Needs a source at least 2200 px wide.

## L02_IMAGE_2-07_ir_sensors_r13.svg

- photograph is 1750x190 but its box renders about 964 CSS px wide (box 1752 of a 2000 viewBox at a 1100 px column) = 1.82x - under the 2x floor. Needs a source at least 1927 px wide.

## L04_GRAPHIC_4-06_for_anatomy.svg

- 3 numbered markers but no callout-* groups - they are grouped by object type, so moving one marker means hunting its parts across the layer

## L05_GRAPHIC_5-04_for_anatomy.svg

- 6 numbered markers but no callout-* groups - they are grouped by object type, so moving one marker means hunting its parts across the layer

## L05_GRAPHIC_5-06_jumper_move_procedure.svg

- 5 numbered markers but no callout-* groups - they are grouped by object type, so moving one marker means hunting its parts across the layer

## L06_GRAPHIC_6-09_five_move_demo.svg

- 10 numbered markers but no callout-* groups - they are grouped by object type, so moving one marker means hunting its parts across the layer

## L06_GRAPHIC_6-11_trapezoid_motion_profile.svg

- 2 rotated/skewed <text> NOT checked for overflow or collision - this tool measures horizontal extent only. Eyeball them.

## L06_GRAPHIC_6-12_measured_course.svg

- 4 numbered markers but no callout-* groups - they are grouped by object type, so moving one marker means hunting its parts across the layer

## L06_IMAGE_6-11_encoder_hardware.svg

- leader of callout-1 passes 1.4 units from the anchor dot of callout-3 (radius 7) - it runs across it

## L08_GRAPHIC_8-1_bang_bang_oscillation.svg

- 1 rotated/skewed <text> NOT checked for overflow or collision - this tool measures horizontal extent only. Eyeball them.

## L08_GRAPHIC_8-3_project_file_tree.svg

- 3 numbered markers but no callout-* groups - they are grouped by object type, so moving one marker means hunting its parts across the layer

## L09_GRAPHIC_9-5_test_course.svg

- 6 numbered markers but no callout-* groups - they are grouped by object type, so moving one marker means hunting its parts across the layer

## L10_GRAPHIC_10-02_avoidance_box_five_phases.svg

- 2 numbered markers but no callout-* groups - they are grouped by object type, so moving one marker means hunting its parts across the layer

## L10_GRAPHIC_10-03_course_setup_clearance.svg

- 4 numbered markers but no callout-* groups - they are grouped by object type, so moving one marker means hunting its parts across the layer

## L10_GRAPHIC_10-07_extended_state_machine.svg

- 1 rotated/skewed <text> NOT checked for overflow or collision - this tool measures horizontal extent only. Eyeball them.

## L13_GRAPHIC_13-03_the_line_was_doing_three_jobs.svg

- photograph is 360x342 but its box renders about 943 CSS px wide (box 1200 of a 1400 viewBox at a 1100 px column) = 0.38x - under the 2x floor. Needs a source at least 1885 px wide.

---

## Local-fix backlog (no redraw needed)

9 findings across 5 files.

- **L02_IMAGE_2-07_ir_sensors_r02.svg** — photo carries a fully-opaque alpha channel doing nothing; 2,914,487 B
- **L02_IMAGE_2-07_ir_sensors_r13.svg** — photo carries a fully-opaque alpha channel doing nothing; 593,201 B
- **L05_GRAPHIC_5-08_three_sensor_array.svg** — photo carries a fully-opaque alpha channel doing nothing; 1,692,415 B
- **L05_GRAPHIC_5-09_five_sensor_array.svg** — photo carries a fully-opaque alpha channel doing nothing; 1,682,007 B
- **L05_GRAPHIC_5-10_jumper_positions.svg** — 1,095,931 B

