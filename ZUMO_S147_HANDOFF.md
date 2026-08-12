# ZUMO — S147 HANDOFF (rewritten at S146 close · paste at top of Session 147)

## Session open ritual (do this without being asked)
1. **`git ls-remote https://github.com/Weymuth/zumo.git HEAD` FIRST.** A stale answer is
   timing, not caching — **retry a minute later before concluding a push failed** (§12.4).
   **AND THE SHA IS NOT THE CHECK. `session_versions --check` IS** (rule 60, S145).
2. Read `LIVE_ZUMO_TEXTBOOK.md` — verify date / status / versions.
3. **Do NOT grep the Bible version.** `session_versions.bible_consistency()` parses it.
4. Run the full suite and **READ THE EXIT CODE, NOT THE LAST LINE**. Plus
   **`callout_id.py --selftest` then `--audit`**, **`keyterm_prefix.py --audit`**,
   **`quizzes/quiz_bank.py --selftest` then `--check`**, and
   **`session_versions.py --selftest`** — **its CONTROL C is the unfinished-documentation-pass
   signal and nothing else in the tree can see one.**
5. **`--anomalies` BELONGS TO `lesson_inventory`, NOT `session_versions`.**
6. `pip install cairosvg --break-system-packages` **and `pyyaml`. Needed every session.**
7. **NEVER run `build_css.py --help` or `session_versions.py --help`.** Read the docstring.
8. **Do not hand-type a version, and do not hand-type a COUNT.**
9. **`gate_payload_match.py` needs `newproject.html` FIRST, then the full lesson glob.**
10. **A CLONE IS NOT THE SITE.** Run `site_parity.py` after any push.
11. **VERIFY THE PUSH BY FRESH CLONE AND MD5 — AND DIFF THE STAGE AGAINST THE CLONE.**
12. **`css/semantic.css` AND `ZUMO_FAMILY_PINS.md` ARE HAND-AUTHORED PRESERVED LAYERS.**
13. **`rm -rf __pycache__` BEFORE `git status`. Also `find . -name pbuild -exec rm -rf {} +`**
    if the toolchain has been run — the harness leaves build dirs inside the project trees.

## 14. THE AVR TOOLCHAIN — CORRECTED S146. THE OLD INSTRUCTIONS NAMED THE WRONG REPOS.

`apt-get install -y gcc-avr avr-libc` **(no `sudo` — `sudo` is not on this box and returns
exit 127 with a confusing error).** Then clone into `/home/claude/harness` **FLAT, not under a
`pololu/` subdirectory** — `pio_harness.sh` looks for `$H/<name>`, and a `pololu/` layer makes
every include silently miss.

**THE EIGHT LIBRARIES ARE THE EIGHT IN `LIBDIRS`, AND S146 OPENED BY CLONING THE WRONG SET.**
Read the list out of the script, do not carry it from a handoff:

```
zumo-32u4-arduino-library  pololu-buzzer-arduino  pololu-oled-arduino  pololu-menu-arduino
pushbutton-arduino  fastgpio-arduino  usb-pause-arduino  pololu-hd44780-arduino
```

**`l3g-arduino` AND `lsm303-arduino` ARE NOT IN IT** — S146 cloned both and missed
`pololu-buzzer-arduino` and `pololu-oled-arduino`, which are. Also clone
`arduino/ArduinoCore-avr` to `$H/ArduinoCore-avr`. Checkout the Zumo library at tag **2.0.1**,
then `bash pio_harness.sh --setup` (expect *objects: 41*).

**THE CONTROL: L11 `after_step_1` MUST COMPILE TO 20,516.** Verified in S144, S145 and S146,
from three different clones. **`shim.cpp` does not exist and is not needed — the harness
guards for it.** Build any payload with
`python3 extract_project.py newproject.html <lesson> <kind> <dir>` then
`bash /home/claude/harness/pio_harness.sh <dir>`. **The anchor is `var PAYLOADS = `, not
`const PAYLOADS`.**

---

# THE ONE THING TO CARRY OUT OF S146

**L12's UNIFORM SHIFT WAS A PROPERTY OF L12, NOT OF BYTE FIXES.**

S145 closed with a corollary to rule 49: *when the deltas are already right, the swap is safe.*
All eighteen L12 figures had moved by exactly 160, so every delta the lesson taught with
survived and not one sentence needed rewriting. **It reads like a rule about re-baselining. It
is not.**

L13's chain moves **+160 at Step 1 and +170 at Step 6**. Two of its three deltas are different
numbers now: **+232 → +240**, **−44 → −42**, total **368 → 378**. Had I carried S145's
corollary forward as a rule and swapped only absolutes, the lesson would have shipped saying
*up 232* over a measured 240 — and it would have gated cleanly, because nothing in this tree
can see a byte figure.

**Compile every step. Derive every delta from the compiles. The absolutes are the easy half.**

---

# SEPTEMBER 8 IS UNDER FOUR WEEKS OUT

**FALL SCOPE IS L01–L13 — RULED BY DJ AT S146 OPEN.** `QUIZ_SPEC` §9 is restated, spec now
**v1.2.0**. **ALL THIRTEEN IN-SCOPE LESSONS ARE READ, FIXED AND BANKED.** L14, L15 and L16 are
unread, unbanked and **out of scope for September** — three lessons, not four.

**READING QUIZZES — status is DERIVED: `python3 quizzes/quiz_bank.py --status`.**
**THE ORDER IS CANON: READ -> FIX -> QUIZ**, same session.

**THE PHOTOGRAPHY IS NOW THE ONLY THING BETWEEN THE BOOK AND SEPTEMBER, AND THE SCOPE RULING
ADDED TWO.** Stills **3.2 · 3.5 · 3.6 · 4.1 · 4.3 · 12.1 · 13.1 · 13.2**, videos
**3.1 · 4.1 · 6.1 · 8.1**. **VIDEO 3.1 carries L03's opening page.** `IMAGE 13.1` is the
rescue space itself — walled zone, silver entrance strip, both victim balls — and `IMAGE 13.2`
is the gripper/competition-robot preview in §8A.3. **Neither has ever been shot, and both sit
in a lesson that is now required.**

---

# STATE

<!-- VERSION BLOCK: emitted by session_versions.py --handoff. Never hand-typed. -->
Fresh-clone verified at **`97106d0`**. Census **40,605**.
Bible **v8.136.2** · `BookComponentStandard` **v01.13.0** · Maker **v2.49.2** ·
`marks/` **41** · `icons/` **49** incl. LICENSE.
`ZUMO_Syllabus_WORKING.md` **v1.2**.

Instruments: `book_gates` **v1.65.10** · `lesson_inventory` **v1.3.5** ·
`gen_component` **v1.6.1** · `pill_sweep` **v1.1** · `gate_payload_match` **v1.8.0** ·
`build_family_map` **v1.6.4** · `callout_id` **v1.0** · `keyterm_prefix` **v1.0.1** · `build_mark_index` **v1.1.0** · `gen_bonus_banner` **v1.4.1** ·
`gen_part_banners` **v1.2** · `session_versions` **v1.24.1** · `fit_raster_svg` **v1.2** ·
`flatten_alpha` **v1.2** · `svg_layout_audit` **v1.20** · `site_parity` **v1.1** ·
`build_css` **v1.3.0** ·
`image_audit` **v1.2** ·
`strip_inline` **v1.2** ·
`build_worklist` **v1.1** ·
`regex_audit` **v1.0** ·
`build_palette` **v1.1** ·
`class_sweep` **v1.0** ·
`color_index` **v1.0** ·
`entity_sweep` **v1.0** ·
`font_stack_sweep` **v1.3.0** ·
`next_pointer` **v1.2** ·
`family_tag` **v1.2.1** ·
`glossary_convert` **v1.0** ·
`mark_wire` **v1.0.2** ·
`glyph_scan` **v1.1** ·
`title_feed` **v1.0** ·
`timer.html` **v1.3.2** ·
`going_deeper` **v01.6.1**.

Lessons: L01 v03.28.3 · L02 v03.21.2 · L03 v03.41.0 · L04 v04.29.0 · L05 v04.29.0 · L06 v04.32.1 · L07 v04.31.4 · L08 v04.31.1 · L09 v05.27.0 · L10 v02.29.1 · L11 v02.30.0 · L12 v01.31.3 · L13 v02.29.0 · L14 v02.33.1 · L15 v02.30.1 · L16 v02.22.1.

`quizzes/QUIZ_SPEC.md` **v1.2.0**.

**Quiz banks: derive it. Never read a count out of this sentence.**

---

# S147 QUEUE

## 1. THE PHOTOGRAPHY — NOW THE CRITICAL PATH, AND IT NEEDS DJ AND THE ROBOT

Everything else in scope is done. **Eight stills and four videos**, listed above. Nothing in
the tree can produce them and no amount of book work substitutes.

## 2. THE BYTE CASCADE — L14, L15, L16 REMAIN. OUT OF SCOPE, NOT WRONG TO DO.

| | L16 says | measured | |
|---|---|---|---|
| L07 | 14,380 | **14,380** | exact |
| L08 | 17,194 | **17,194** | exact |
| L09 | 18,158 | **18,158** | exact |
| L10 | 20,364 | **20,516** | +152 |
| L11 | 20,542 | **20,702** | +160 |
| L12 | 24,534 | **24,694** | +160 — **FIXED S145** |
| L13 | 24,902 | **25,072** | +170 — **FIXED S146** |
| L14 | 25,640 | **25,816** | +176 |
| L15 | 28,034 | **28,214** | +180 |

**L16's table itself is still wrong in six rows, including the two now fixed in their own
lessons.** L10 and L11 each carry one figure and both are already right; the damage is in L16's
summary table and in L13–L16's own prose.

**L14 CARRIES THREE ORPHANED `24,902` SITES** — lines 699, 732, 861, keyed to L13's old finished
figure. **Deliberately not fixed in S146.** L14 holds eight byte figures; correcting three would
leave a lesson where some are compiled and some are stale with nothing marking which. **Fix L14
whole or not at all.**

**THE CAPSTONE ARITHMETIC IS THE SHARP END AND IT IS NOT COSMETIC.** L16 tells the student
*"Your Lesson 15 project is 28,034 of them. You have 638 bytes left."* **L15 finished measures
28,214, so the real headroom is 458** — the budget is overstated by 180, **28% more room than
the chip has.** **Read L16's exercise budget before assuming the fix is only numbers.**

**PRICE: ~70 byte figures across L14 (8), L15 (16) and L16 (47), each needing its own compile.**
L13's pass took nine compiles for twelve edits. **AND EXPECT RULE 56** — grep
`build_family_map`'s tier list for any figure before changing it. It pinned an L12 sentence at
S145; it pinned no L13 sentence, which is luck, not design.

## 3. THE READ ARC — L14, L15, L16, ALL UNREAD AND ALL OUT OF SCOPE
Each one's read and its byte fix are the same job. L14 first if it is started at all.

## 4. STILL OPEN, CARRIED
- **THE CATCH-UP CONVENTION IS SPLIT.** L07–L10 OFFSET (`step_N -> after_step_(N-1)`);
  L11–L16 IDENTITY. Clean across all 64 rows. **A gate pinning either would certify 64 and
  fail 32.** DJ to rule. **Now half in scope and half out.**
- **L10's ARRIVAL GEOMETRY (S144, unruled).** The rebuilt box turns `+90`, `−90`, `−90` — net
  `−90` — so it arrives PERPENDICULAR to the line with nothing to realign it, and **every
  artefact agrees with the code.** Bench: watch the two seconds after `SEEKING` flips to
  `FOLLOWING`. **Challenge 6's wedge meets the line at 30°, which a P-controller can pull out
  of; the box meets it at 90°, which it cannot.**
- **§8A.4's *"Pololu rates the 75:1 gearmotors at roughly 65 cm/s flat out"* IS UNVERIFIED.**
  pololu.com is not reachable from the sandbox.
- **`AVOID_OUT_CM = 15.0` HAS NEVER TOUCHED A FLOOR.** · **CHALLENGE 6's WEDGE NUMBERS ARE
  SIMULATED.** · **L11 §7A's 999.0 RULER TRICK HAS NEVER TOUCHED A FLOOR.**
- **THE RESOURCE SECTION AS A BOOK PAGE — PARKED UNTIL AFTER SEPTEMBER 8.**
- **THE 100:1 Kp SUGGESTION IS UNVERIFIED AND THE DIRECTION IS CONTESTED.**
- **NO GATE HOLDS A QUIZ BANK** · **NO GATE HOLDS A NAV PILL** · **NO GATE HOLDS A BYTE
  FIGURE.** Three invariants, no gates. **S146 added nothing to this list and closed nothing
  on it.**
- **§16.14 HAS NO NUMBERED SECTION BODY.** v8.135.3 announces *§16.14 NEW* and the Bible carries
  no `### 16.14` line. **§16.12 and §16.13 are also seated BELOW §17's heading**, and §16.15
  was seated beside them.
- **L12 §3.2's *5.5 counts per degree* IS A ROUNDING ARTIFACT, NOT A DEFECT.** The constant
  computes to **5.507**, so 90° is 495.7 counts and the lesson's **496 is right**. Not asked in
  the L12 bank, for that reason.

## Carried from S141/S140, still unruled
- **THE BAUD BENCH TEST.** `monitor_speed = 9600`, leave `Serial.begin(115200)`. Garbage
  means **L02 §6 Step 2 is wrong**. **Keep 1200 out of the test.**
- **THE 1200-BAUD RESET HAS NO HOME IN THE BOOK.** · **`IMAGE 7.9`–`7.12` ARE INDEXED AS
  *Photo / screenshot*** where four live drawn SVGs exist.
- **§3.2's *about 13½ milliseconds*** for the six-round proximity read — unverified.
- **L05 §3.6 alkaline tension**: prose derives 6.0 V from 1.5 V/cell; the table reads 6,300 mV.
- **The `static` split is taught in L05, L06 and L08, but the GLOSSARIES still disagree.**

## Carried from S137/S138/S139, still unruled
- **§4.2's stall-current multiple**: *~1.5 A … roughly 5×*, where Pololu's no-load is ~0.10 A.
- **`IMAGE 4.1` IS A PHANTOM IN THE FIGURE COUNT** — planned 146, true population 145.
- **THE CONSTANTS vs CONFIGURATION VOCABULARY DRIFT.** Derive the canonical set first.
- **THE 3Pi+ NOTE COMES OUT OF L03** — needs a new root file as the 3Pi+ book seed.
- **L03 C1's hint hands over the exact two numbers its own template blanks ask for** — L07 C4
  and L08 C4 are the second and third instances.
- **§3.3's header-contents bullet in L07 still lists *Include guards***.
- **§7's BANNER is still three spellings** · **L14's §10 is the only §10 that is not an exit
  ticket** · **whether the `after` quiz set is graded at all.**

## Carried from S135/S133/S134, still open
- **THE SPIRAL ARC — RULED, ENUMERATED, DELIBERATELY NOT STARTED.** 13 of 171 units.
- **THE FIGURE BLOCK HAS FOUR SPELLINGS.** L12's is the best.
- **`svg_layout_audit.py` HAS FOUR MEASURED DEFECTS, NONE FIXED.**
- KEY TERM paint is five grounds across 238 blocks · L03 `3.44` carries `id="glossary-trim"`
  on a BODY block · `BookComponentStandard` §7.4 says 184 where the measured figure is 238 ·
  §6.5's nav-pill rule says 12–14 where the live range is 10 to 19.
- **THE AMBER LEAK: two of three closed. L02 §2.7 is the last one** — deferred to its own read.

## AFTER SEPTEMBER 8 — PARKED ON PURPOSE, DO NOT START EARLY
- **THE RESOURCE SECTION PAGE** · **REDO `GRAPHIC 4.7` IN THE BLUEPRINT COMPOSITION** (chips
  run **5 4 3 2 1** left to right — do not re-derive) · Challenge card Pass B ·
  monetization/ebook · DISCOVERIES tagging · TDP template v3 (A5 Lab Log).

## Learner mode & book content
L03_C05 Variable Speed · L03 C01/C05/C06 reference a `finished` payload that does not exist
for L03 · whole-template starters L08/L09/L10 · Maker batch · L01 VS Code multi-root step.

## Bench (need the robot — parked with photography)
Q017 L09 six numbers · Q044 calibration-spin · Q046 gyro-bias · L02 §5 green-LED ·
Constrain RUN_MS · **cm/s at a stated BASE_SPEED** · the floor rig for 3.2 / 3.5 / VIDEO 3.1 ·
a real TRIM run for `IMAGE 3.6` · **THE SURFACE TEST: run 7E on a lab tile.** · **L04's wave
test and Act Two row-1 overflow.** · **L05 Experiment 3 at 45°.** · **L06 Experiment 3 both
drags.** · **the baud test above.** · **commanded 30 cm vs measured, across a few robots** ·
**DRIVE THE SEVEN-PHASE BOX** · **drive Challenge 6's wedge** · **HOLD THE ROBOT OVER A TABLE
EDGE AND READ THE FIVE CALIBRATED VALUES** — expect ~1000 each · **L11's whole §7 ladder** ·
**L12's §7 ladder — 7A hand-turn, 7B uncalibrated drift, 7C encoder-vs-gyro on a slick
surface, 7D, 7E's two squares.** · **NEW, AND NOW IN SCOPE: L13's ENTIRE §7 LADDER.** 7A's
surface-meter table is the one that matters — **four raw readings and nine prox counts, and
every one of L13's four tunables is blank until it is filled.** No student can complete Lesson
13 without it, and no value in it has ever been measured on this fleet. **7E's fan has never
been driven either.**

---

# PUSHING — READ THIS

Named-file CLI for adds and modifies; **GitHub Desktop for deletions.** **Never `git add .`**

1. **DELIVER THE FILES** via `present_files`; instructions and md5s in the CHAT ONLY.
2. **`(1)` does not mean stale.** Verify by **md5**, never by suffix.
3. **Never present a test file or a DIAGNOSTIC beside repo files.**
4. **Never produce PUSH_ME_*.md or MD5_*.txt.**
5. **`lessons/` IS PART OF THE FILENAME. `css/`, `quizzes/` and `images/` likewise.**
6. **A push that bumps a version and omits LIVE.md is an INCOMPLETE push (§12.6).**
7. **Exactly ONE `ZUMO_SNN_HANDOFF.md` in the root (gate 28).**
8. **THE NUMBER IN THE FILENAME IS THE SESSION THAT READS IT.**
9. **Never write a real version number as an arrow pair in prose.**
10. **A document cannot name the commit that contains it.**
11. **AN EDIT TO A FILE WITH REPEATED LANDMARK LINES TARGETS AN INDEX AND ASSERTS IT** (§6.12c).
12. **AN EDIT THAT CHANGES LINE COUNT INVALIDATES EVERY LINE-KEYED TARGET BELOW IT.** DESCENDING.
13. **A SNAPSHOT TAKEN BEFORE THE WORK IS NOT A SNAPSHOT OF THE WORK.**
14. **A CONTROL THAT DEPENDS ON THE STATE OF WHAT IT AUDITS IS NOT A CONTROL.**
15. **A CONTROL RUN AGAINST AN UNTRACKED FILE HAS NO RESTORE PATH.**
16. **A LIBRARY MAY NOT EXIT.**
17. **RUN A BLINDING CONTROL AGAINST THE CONSUMER THAT CAN FAIL** — **and if no consumer can
    fail, say so and run a different control instead of a theatrical one (S146).**
18. **A DERIVED KEY IS NOT AN IDENTITY.**
19. **A GATE THAT PINS A SPELLING CERTIFIES WHATEVER IT WAS GIVEN. PIN THE PROPERTY.**
20. **A HOLD THAT IS ALSO SATISFIED BY AN ACCIDENT IS NOT A HOLD.**
21. **SNAPSHOT THE STATE YOU ARE IN, NOT THE STATE YOU ARE LEAVING.**
22. **A GENERATED ARTEFACT PRINTING `DIFFERS` IS A LEAD, NOT AN INSTRUCTION.**
23. **A CONTROL THAT CANNOT TELL A LOST WORD FROM A LOST SPACE IS NOT A CONTROL.**
24. **THE ACCEPTANCE TEST FOR A CSS REGENERATION IS THE RESOLVED STYLING, NOT THE RULE COUNT.**
25. **A GENERATED CLASS NAME IS NOT A HANDLE.**
26. **MEASURE THE PROPERTY THE RULING NAMES, NOT A PROXY FOR IT.**
27. **A COVERAGE COUNT MEASURES BLOCKS SCANNED, NOT BLOCKS ASSERTED.**
28. **A STRUCTURAL CHANGE THAT ENDS A SENTENCE EARLY OWES THE SENTENCE A LOOK.**
29. **PIN THE DENOMINATOR, NOT THE REMAINDER.**
30. **A WORKING COPY YOU HAVE RUN TOOLS IN IS NOT THE REPO.** When two readings disagree, RE-CLONE.
31. **A LABEL IS NOT THE THING IT NAMES.**
32. **NOT EVERY SPLIT IS DRIFT.**
33. **NO INSTRUMENT READS PROSE. Read the book.** **S146: seventy gates certified *the first
    lesson that adds zero hardware*, which L09 and L12 both falsify.**
34. **A NUMBER IS ONLY CHECKABLE AGAINST THE OTHER FIFTEEN LESSONS.**
35. **COMPILE THE SNIPPET; LET THE BOOK'S OWN CODE TESTIFY.**
36. **A FACT THAT LIVES ONLY IN AN SVG IS NOT IN THE BOOK.** **S146: GRAPHIC 13.2's plotted
    250 / 400 / 1200 / 2400 are askable ONLY because §8A.1 restates them in prose.**
37. **READ -> FIX -> QUIZ, NEVER QUIZ FIRST** — same session.
38. **A TEXT MATCH LOCATES; IT NEVER ANSWERS.**
39. **NO INSTRUMENT THAT READS THE TREE CAN SEE A RULING.** Search the session record first.
40. **PULL THE PAYLOAD, NOT THE CARD.**
41. **AN ENTRY FILED IN ONE HOME IS NOT FILED.**
42. **A SPEC'S OWN NUMBERS CAN BE ARITHMETICALLY IMPOSSIBLE.**
43. **WHEN TWO SECTIONS DISAGREE, READ THE CITATIONS.**
44. **THE HEADER OF A THING IS NOT THE THING.**
45. **A SNAPSHOT YOU HAVE RUN TOOLS IN HIDES ITS OWN DEBRIS.**
46. **A CALLOUT IS NEVER A FREE EDIT.**
47. **A STEP PAYLOAD IS THE FILE AS IT STANDS AT THAT STEP.**
48. **A VERIFIER THAT READS YOUR INTENT INSTEAD OF THE ARTEFACT VALIDATES NOTHING.**
49. **A NUMBER THAT A SENTENCE DERIVES FROM CANNOT BE SWAPPED WITHOUT REWRITING THE SENTENCE.**
    **S145's COROLLARY — *when the deltas are already right, the swap is safe* — IS ABOUT L12,
    NOT ABOUT BYTE FIXES. S146 REVOKES IT AS A GENERAL RULE:** L13's chain moved +160 at the
    top and +170 at the bottom, and two of its three deltas changed. **Recompute the deltas
    from the compiles every time.**
50. **A COUNT INSIDE A SENTENCE IS A CLAIM. DERIVE IT OR DELETE IT.** **S146: Step 6's
    *120 tighter / cost 26* nets −94 against a measured −42, and no honest pair closes on 42
    without teaching linker padding. DELETED, not replaced with a number that nearly works.**
51. **A GATE THAT CERTIFIES AGREEMENT IS NOT CERTIFYING CORRECTNESS.**
52. **WHEN THE ART AND THE CODE DISAGREE, ASK WHICH ONE IS THE DESIGN.**
53. **WHEN EVERY ARTEFACT AGREES, ASK WHETHER THE DESIGN IS RIGHT.**
54. **A DIRECTIONAL CLAIM WITH NO NUMBER IS STILL A CLAIM.**
55. **"NOTHING READS IT" IS NOT "NOTHING MENTIONS IT."**
56. **A CONTENT TIER THAT PINS A SPELLING OWES AN EDIT WHEN THE SPELLING IS THE DEFECT.**
57. **AN EDIT THAT CHANGES LENGTH INVALIDATES OFFSETS COMPUTED BEFORE IT.**
58. **A CONTROL RUN ON THE PRE-EDIT FILE IS HOW YOU KNOW A FINDING IS YOURS.**
59. **A CONTROL THAT FIRES FOR THE WRONG REASON IS NOT A CONTROL.** Ask what your control would
    report if the property you are testing did not exist at all. **S146's application: I ran NO
    blinding control on L13's byte figures, because S145 proved nothing in the tree can see one.
    The control I ran instead re-derives the chain OUT of the edited HTML and asserts EVERY STEP
    against the compiles. **The endpoint form is blind — proved by seeding it:** revert Step 5's
    figure alone and 25,072 − 24,694 = 378 still holds and all 70 gates still pass.**
60. **A SHA THAT MATCHES DOES NOT MEAN THE CONTENT LANDED. The version block is the check.**
61. **NEW, S146: A SUPERLATIVE IS A CROSS-LESSON CLAIM, AND IT IS ALWAYS CHECKABLE.** *First*,
    *only*, *never*, *the last time* — each one asserts something about the other fifteen
    lessons and each one costs exactly one grep to test. L13 carried *the first lesson that adds
    zero hardware* in two places and L09 and L12 both got there first. **When a sentence claims
    a rank, go and read the lessons it ranks against.**
62. **NEW, S146: AN EXPLANATION CAN BE WRONG WITHOUT ANY NUMBER BEING WRONG.** §7E said two
    builds differ by 64 bytes — *the price of keeping both turn functions alive in the binary*.
    Both functions are alive in **both** builds, so the explanation named no difference at all,
    and the builds are in fact identical. **Had the 64 been right, the sentence would still have
    been false.** Read the reason, not just the figure.
