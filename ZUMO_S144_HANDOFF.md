# ZUMO — S144 HANDOFF (rewritten at S143 close · paste at top of Session 144)

## Session open ritual (do this without being asked)
1. **`git ls-remote https://github.com/Weymuth/zumo.git HEAD` FIRST.** A stale answer is
   timing, not caching — **retry a minute later before concluding a push failed** (§12.4).
2. Read `LIVE_ZUMO_TEXTBOOK.md` — verify date / status / versions.
3. **Do NOT grep the Bible version.** `session_versions.bible_consistency()` parses it.
4. Run the full suite and **READ THE EXIT CODE, NOT THE LAST LINE**. Plus
   **`callout_id.py --selftest` then `--audit`**, **`keyterm_prefix.py --audit`**,
   **`quizzes/quiz_bank.py --selftest` then `--check`**, and
   **`session_versions.py --selftest`** — **its CONTROL C is what reports an unfinished
   documentation pass, and nothing else in the tree can see one.**
5. **`--anomalies` BELONGS TO `lesson_inventory`, NOT `session_versions`.**
6. `pip install cairosvg --break-system-packages` **and `pyyaml`. Needed every session.**
7. **NEVER run `build_css.py --help` or `session_versions.py --help`.** Read the docstring.
8. **Do not hand-type a version, and do not hand-type a COUNT.**
9. **`gate_payload_match.py` needs `newproject.html` FIRST, then the full lesson glob.**
10. **A CLONE IS NOT THE SITE.** Run `site_parity.py` after any push.
11. **VERIFY THE PUSH BY FRESH CLONE AND MD5 — AND DIFF THE STAGE AGAINST THE CLONE.**
12. **`css/semantic.css` AND `ZUMO_FAMILY_PINS.md` ARE HAND-AUTHORED PRESERVED LAYERS.**
13. **`rm -rf __pycache__` BEFORE `git status`.** S141, S142 and S143 all grew one.
14. **NEW: THE AVR TOOLCHAIN IS ONE COMMAND.** `apt-get install -y gcc-avr avr-libc`, then
    clone the eight repos under `pololu/` (+ `arduino/ArduinoCore-avr`) and symlink them
    beside `pio_harness.sh`. **Byte claims are now CHECKABLE. Check them.**

---

# THE ONE THING TO CARRY OUT OF S143

**A GATE THAT CERTIFIES AGREEMENT IS NOT CERTIFYING CORRECTNESS.**

L10's avoidance maneuver could never return to the line. It turned `+90`, drove, turned
`-90` — **net rotation ZERO** — so the robot finished on its approach heading, displaced
sideways, and `RETURNING_TO_LINE` ran PARALLEL to the line until the timeout. Every student
who ever built it would have watched it fail.

`gate_payload_match` passed for the maneuver's whole life **precisely because 202 payload
files copied the wrong code faithfully.** That is what a PASS looks like when the source is
wrong. The gate pins agreement between the book and the Maker; nothing in the tree pins the
book against physics.

**AND EVERYTHING EXCEPT THE CODE WAS RIGHT.** GRAPHIC 10.2's four arrows draw the correct
four-leg box. `PHASE_DRIVE_PAST`'s comment says *past the obstacle*. `PHASE_TURN_BACK`'s says
*toward the line*. §3.3 names *out · along · back · hunt* — four movements, where the code had
three. **The art and the names were the design document and the code was a leg short of it.**

**THE REASON IT SURVIVED IS THE WORST PART: §8.3 anticipated the exact symptom and gave a
plausible WRONG cause.** *"The turn-back is almost certainly wrong — go re-prove your 90°
turn."* A perfectly accurate ±90 pair is what GUARANTEES the failure. The first student to
report it would have been sent to tune the one thing that makes it worse.

---

# SEPTEMBER 8 IS UNDER FOUR WEEKS OUT

**READING QUIZZES — 9 of 16 WRITTEN, 695 questions.** Status is DERIVED:
`python3 quizzes/quiz_bank.py --status`. **`quizzes/QUIZ_SPEC.md` (v1.1.0) first. THE ORDER IS
CANON: READ -> FIX -> QUIZ**, same session.

**L10 IS READ AND FIXED BUT HAS NO BANK.** It is the only lesson in that state, and the read
is a perishable asset — **bank L10 first in S144, or the read has to be repeated.**
L11–L16 are unread.

**THE IN-SCOPE FIGURES ALL NEED DJ AND THE ROBOT.** Stills **3.2 · 3.5 · 3.6 · 4.1 · 4.3 ·
12.1**, videos **3.1 · 4.1 · 6.1 · 8.1**. **VIDEO 3.1 carries L03's opening page.**

---

# STATE

<!-- VERSION BLOCK: emitted by session_versions.py --handoff. Never hand-typed. -->
Fresh-clone verified at **`a8befe7`**. Census **40,608**.
Bible **v8.135** · `BookComponentStandard` **v01.13.0** · Maker **v2.49.0** ·
`marks/` **41** · `icons/` **49** incl. LICENSE.
`ZUMO_Syllabus_WORKING.md` **v1.2**.

Instruments: `book_gates` **v1.65.8** · `lesson_inventory` **v1.3.5** ·
`gen_component` **v1.6.1** · `pill_sweep` **v1.1** · `gate_payload_match` **v1.8.0** ·
`build_family_map` **v1.6.1** · `callout_id` **v1.0** · `keyterm_prefix` **v1.0.1** · `build_mark_index` **v1.1.0** · `gen_bonus_banner` **v1.4.1** ·
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

Lessons: L01 v03.28.3 · L02 v03.21.2 · L03 v03.41.0 · L04 v04.29.0 · L05 v04.29.0 · L06 v04.32.1 · L07 v04.31.3 · L08 v04.31.0 · L09 v05.27.0 · L10 v02.29.0 · L11 v02.28.2 · L12 v01.31.2 · L13 v02.28.2 · L14 v02.33.1 · L15 v02.30.1 · L16 v02.22.1.

---

# S144 QUEUE

## 1. BANK L10 FIRST — the read is already spent
Then continue the arc at **L11**, which is unread.

## OPENED S143, UNRULED

- **THE CATCH-UP CONVENTION IS SPLIT AND NOBODY HAS RULED IT.** Derived across all 64
  CATCH-UP rows: **L07–L10 use OFFSET (`step_N -> after_step_(N-1)`, the file you START the
  step from); L11–L16 use IDENTITY (`step_N -> after_step_N`, the file AFTER it).** The split
  is perfectly clean. It may be deliberate — L07–L10 all open with *copy your previous
  project*, so `after_step_1` is the previous lesson's finished build and every later row
  lags by one. **I MISREAD THIS AS A DEFECT MID-SESSION, REPOINTED L10's `step_8`, AND HAD TO
  REVERT.** Do not write a gate for this until it is ruled: a gate pinning either convention
  would certify 64 rows and fail 32.
- **STEP 9's ABSOLUTE BYTE TOTAL IS NOW 20,516 AND IT IS MINE, NOT PLATFORMIO's.** The
  toolchain reproduced the OLD 20,364 exactly, so the number is trustworthy — but a single
  PlatformIO build of L10 `finished` would confirm it independently. Thirty seconds on DJ's
  machine.
- **`AVOID_OUT_CM = 15.0` HAS NEVER TOUCHED A FLOOR.** 15 cm of step-out is derived to clear
  the line and the block, not measured against a real block. **Bench item.**
- **CHALLENGE 6's WEDGE NUMBERS ARE SIMULATED, NOT DRIVEN.** ~30 cm to close at 120°.

## Carried from S142, still unruled
- **THE RESOURCE SECTION AS A BOOK PAGE — PARKED UNTIL AFTER SEPTEMBER 8 (DJ ruling).**
  (a) companion page on the `going_deeper` model — named in **29 places in `book_gates.py`**
  plus six other instruments; (b) **THE NUMBERS MUST BE DERIVED OR GATED, NEVER RETYPED.**
- **THE 100:1 Kp SUGGESTION IS UNVERIFIED AND THE DIRECTION IS CONTESTED.** Settle it with
  L08 Challenge 2's Wiggle Test if a red-sticker robot ever appears.
- **NO GATE HOLDS A QUIZ BANK** and **NO GATE HOLDS A NAV PILL.**

## Carried from S141, still unruled
- **THE BAUD BENCH TEST.** `monitor_speed = 9600`, leave `Serial.begin(115200)`, upload, open
  the monitor. Garbage means **L02 §6 Step 2 is wrong**. **Keep 1200 out of the test.**
- **THE 1200-BAUD RESET HAS NO HOME IN THE BOOK.** Candidate *Going Deeper* entry.
- **`IMAGE 7.9`–`7.12` ARE INDEXED AS *Photo / screenshot*** where four live drawn SVGs exist.

## Carried from S140, still unruled
- **§3.2's *about 13½ milliseconds*** for the six-round proximity read — unverified.
- **L05 §3.6 alkaline tension**: prose derives 6.0 V from 1.5 V/cell; the table reads 6,300 mV.
- **The `static` split is taught in L05, L06 and L08, but the GLOSSARIES still disagree.**

## Carried from S137/S138/S139, still unruled
- **§4.2's stall-current multiple**: *~1.5 A … roughly 5× its free-running draw*, where
  Pololu's no-load figure is ~0.10 A, i.e. ~15×.
- **`IMAGE 4.1` IS A PHANTOM IN THE FIGURE COUNT** — planned reads 146, true population 145.
- **THE CONSTANTS vs CONFIGURATION VOCABULARY DRIFT.** Derive the canonical set first.
- **THE 3Pi+ NOTE COMES OUT OF L03** — needs a new root file as the 3Pi+ book seed.
- **`class period` IN L10 — READ AND CLOSED (S143).** It is §4.2 warning that another class may
  have moved the jumpers back. Legitimate. **Keep. Do not reopen.**
- **L03 C1's hint hands over the exact two numbers its own template blanks ask for** — L07
  Challenge 4 and L08 Challenge 4 are the second and third instances.
- **§3.3's header-contents bullet in L07 still lists *Include guards***.
- **§7's BANNER is still three spellings** — 9 lessons `· Test It`, 6 bare, L12 `· Calibrate`.
- **L14's §10 is the only §10 that is not an exit ticket.**
- **Whether the `after` quiz set is graded at all.** Nine lessons now have one.

## Carried from S135, still open
- **THE SPIRAL ARC — RULED, ENUMERATED, DELIBERATELY NOT STARTED.** 13 of 171 units. Five
  approved first: L04 4.4→L03 · L05 5.1→L04 · L06 6.7→L03,L04 · L12 12.2→L06 · L15 15.2→L04.
- **THE FIGURE BLOCK HAS FOUR SPELLINGS.** L12's is the best.
- **`svg_layout_audit.py` HAS FOUR MEASURED DEFECTS, NONE FIXED.**

## Carried from S133/S134, still unruled
KEY TERM paint is five grounds across 238 blocks · the four held body blocks are a FAMILY
question · head colour `#6a1b9a` is 16 blocks · L03 `3.44` carries `id="glossary-trim"` on a
BODY block · `BookComponentStandard` §7.4 says 184 where the measured figure is 238 · §6.5's
nav-pill rule still says 12–14 where the live range is 10 to 19 · **§24.14a and §24.14b still
have NO section body** · **L07 `[IMAGE 7.3]`** is landed by a GRAPHIC.
**THE AMBER LEAK, S143:** `#856404` is the WARNING family's colour and it has leaked onto
TIP/NOTE in **L02 §2.7 and L10 10.5**. L09's six were normalised; these two were deferred to
their own lessons' reads. **L10 is now read — its stray is still there.**

## Carried, unchanged
Should `ZUMO_FAMILY_PINS.md` carry a version home? · `css/semantic.css` carries none either ·
the 3 `glyph_scan` leads · quick-reference anchors in L02–L06 only · **timers appear in
L02/L03/L04 only — S69 burned a session on a false finding here, READ before counting** ·
the colour ledger, 16 items · `index.html` carries no version home · **L01's BC02 does not
carry L01's objectives (legacy, ruled S119)** · L14's score formula is `<code>` and is not
code · **the mark roster RECONCILES and is gated (61). Do not re-open.**

## AFTER SEPTEMBER 8 — PARKED ON PURPOSE, DO NOT START EARLY
- **THE RESOURCE SECTION PAGE** · **REDO `GRAPHIC 4.7` IN THE BLUEPRINT COMPOSITION** (chips
  run **5 4 3 2 1** left to right — do not re-derive) · Challenge card Pass B ·
  monetization/ebook · DISCOVERIES tagging.

## Learner mode & book content
L03_C05 Variable Speed · L03 C01/C05/C06 reference a `finished` payload that does not exist
for L03 · whole-template starters L08/L09/L10 · Maker batch · L01 VS Code multi-root step.

## Bench (need the robot — parked with photography)
Q017 L09 six numbers · Q044 calibration-spin · Q046 gyro-bias · L02 §5 green-LED ·
Constrain RUN_MS · **cm/s at a stated BASE_SPEED** · the floor rig for 3.2 / 3.5 / VIDEO 3.1 ·
a real TRIM run for `IMAGE 3.6` · **THE SURFACE TEST: run 7E on a lab tile.** · **L04's wave
test and Act Two row-1 overflow.** · **L05 Experiment 3 at 45°.** · **L06 Experiment 3 both
drags.** · **the baud test above.** · **commanded 30 cm vs measured, across a few robots** ·
**NEW: DRIVE THE SEVEN-PHASE BOX. `AVOID_OUT_CM = 15.0` is derived, never measured against a
real block, and the whole maneuver has never touched a floor.** · **NEW: drive Challenge 6's
wedge and compare the two shapes for real.**

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
15. **A CONTROL RUN AGAINST AN UNTRACKED FILE HAS NO RESTORE PATH** — snapshot yourself.
    **S143 REFINEMENT: A TRACKED FILE HAS A RESTORE PATH, BUT `git checkout` RESTORES THE
    COMMITTED STATE, NOT THE STATE YOU WERE STANDING IN.** It silently reverted a regenerated
    `css/book.css`; only an md5 check caught it.
16. **A LIBRARY MAY NOT EXIT.**
17. **RUN A BLINDING CONTROL AGAINST THE CONSUMER THAT CAN FAIL.**
18. **A DERIVED KEY IS NOT AN IDENTITY.**
19. **A GATE THAT PINS A SPELLING CERTIFIES WHATEVER IT WAS GIVEN. PIN THE PROPERTY.**
    **S143 paid this in advance:** a CATCH-UP gate written on one hand-found "defect" would
    have certified 64 rows and failed 32, because nobody had ruled which convention is canon.
20. **A HOLD THAT IS ALSO SATISFIED BY AN ACCIDENT IS NOT A HOLD.**
21. **SNAPSHOT THE STATE YOU ARE IN, NOT THE STATE YOU ARE LEAVING.**
22. **A GENERATED ARTEFACT PRINTING `DIFFERS` IS A LEAD, NOT AN INSTRUCTION.**
23. **A CONTROL THAT CANNOT TELL A LOST WORD FROM A LOST SPACE IS NOT A CONTROL.**
    **S143: my own simulator printed a DIVERGING path as PARALLEL.** Two different failures;
    a control that calls one the other is not a control.
24. **THE ACCEPTANCE TEST FOR A CSS REGENERATION IS THE RESOLVED STYLING, NOT THE RULE COUNT.**
    **S143 has a PROOF now, not an inspection: no element in the sixteen lessons carries two
    classes, so a frequency reshuffle cannot decide a cascade.** Four digest moves this
    session, all rank-only, 574/2,033 every time.
25. **A GENERATED CLASS NAME IS NOT A HANDLE.**
26. **MEASURE THE PROPERTY THE RULING NAMES, NOT A PROXY FOR IT.**
27. **A COVERAGE COUNT MEASURES BLOCKS SCANNED, NOT BLOCKS ASSERTED.**
28. **A STRUCTURAL CHANGE THAT ENDS A SENTENCE EARLY OWES THE SENTENCE A LOOK.**
29. **PIN THE DENOMINATOR, NOT THE REMAINDER.**
30. **A WORKING COPY YOU HAVE RUN TOOLS IN IS NOT THE REPO.** When two readings disagree, RE-CLONE.
31. **A LABEL IS NOT THE THING IT NAMES.**
32. **NOT EVERY SPLIT IS DRIFT.** **S143 twice:** the catch-up convention split carries
    information, and two of L10's surviving *five*s were correct (five sensors, five ladder
    programs). Ask what a variation CARRIES before normalising it.
33. **NO INSTRUMENT READS PROSE. Read the book.**
34. **A NUMBER IS ONLY CHECKABLE AGAINST THE OTHER FIFTEEN LESSONS.**
35. **COMPILE THE SNIPPET; LET THE BOOK'S OWN CODE TESTIFY.**
36. **A FACT THAT LIVES ONLY IN AN SVG IS NOT IN THE BOOK.** **S143 INVERTS THIS ONCE: the SVG
    was RIGHT and the code was wrong.** Read the art's own coordinates before assuming.
37. **READ -> FIX -> QUIZ, NEVER QUIZ FIRST** — same session. **L10 is read and unbanked.**
38. **A TEXT MATCH LOCATES; IT NEVER ANSWERS.**
39. **NO INSTRUMENT THAT READS THE TREE CAN SEE A RULING.** Search the session record first.
40. **PULL THE PAYLOAD, NOT THE CARD.**
41. **AN ENTRY FILED IN ONE HOME IS NOT FILED.**
42. **A SPEC'S OWN NUMBERS CAN BE ARITHMETICALLY IMPOSSIBLE.**
43. **WHEN TWO SECTIONS DISAGREE, READ THE CITATIONS.** The older text is usually wrong.
44. **THE HEADER OF A THING IS NOT THE THING.**
45. **A SNAPSHOT YOU HAVE RUN TOOLS IN HIDES ITS OWN DEBRIS.** A root `__pycache__` again.
46. **A CALLOUT IS NEVER A FREE EDIT** — and **S143 adds: NEITHER IS A CHALLENGE CARD.**
    Challenge 6 moved the CSS digest on its own.
47. **A STEP PAYLOAD IS THE FILE AS IT STANDS AT THAT STEP.** **S143 built `after_step_8` to
    this rule:** `after_step_7` plus ONLY Step 8's cases, with Step 9's edits deliberately absent.
48. **A VERIFIER THAT READS YOUR INTENT INSTEAD OF THE ARTEFACT VALIDATES NOTHING.**
49. **A NUMBER THAT A SENTENCE DERIVES FROM CANNOT BE SWAPPED WITHOUT REWRITING THE SENTENCE.**
50. **NEW, S143: A COUNT INSIDE A SENTENCE IS A CLAIM. DERIVE IT OR DELETE IT.** §3.6's
    timed-turn sentence was wrong TWICE — *once*, then *twice*, when the true answer spans
    three lessons. It shipped with **no count at all**. The same session put *five* into eight
    other L10 sentences that all had to move to *seven*.
51. **NEW, S143: A GATE THAT CERTIFIES AGREEMENT IS NOT CERTIFYING CORRECTNESS.**
    `gate_payload_match` passed on 202 faithful copies of a maneuver that could not work.
    **Faithfulness is not truth. Something outside the tree has to check the physics.**
52. **NEW, S143: WHEN THE ART AND THE CODE DISAGREE, ASK WHICH ONE IS THE DESIGN.** GRAPHIC
    10.2, the phase comments and §3.3's four-word summary all described the correct maneuver.
    The code was the outlier. **I nearly rewrote three correct artefacts to match one wrong one.**
