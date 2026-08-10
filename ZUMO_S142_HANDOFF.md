# ZUMO — S142 HANDOFF (rewritten at S141 close · paste at top of Session 142)

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

---

# THE ONE THING TO CARRY OUT OF S141

**A PAYLOAD NAMED FOR A STEP MUST BE THE FILE AS IT STANDS *AT* THAT STEP — AND A GATE THAT
CHECKS FOR A WORD IS CHECKING FOR A WORD.**

L06's `after_step_7` through `after_step_11` shipped **Step 13's FIXED** `driveDistance()`
and `turnDegrees()`. Five DISCOVERIES entries — Step 8, Discovery 6.7, Step 10, Discovery
6.8, Step 12 — handed a catching-up student a file with **both of the bugs Step 13 exists to
find already repaired**, so Step 13 quoted two lines that were not in their file and promised
a square would fail when it would have closed. Cause is in the Maker's own changelog: v2.14's
TRIM pass regenerated `PAYLOADS[6..9]` **wholesale** instead of only the post-repair states.
**Nothing saw it for 117 sessions**, because `gate_payload_match` asserts a payload derives
from **SOME** lesson `<pre>` and never from the `<pre>` belonging to the step it is NAMED for.

**GATE 70's FIRST DRAFT WAS BLIND ON ITS FAR SIDE AND A BLINDING CONTROL CAUGHT IT.** It
asserted only that `finished` did NOT hold the broken body and that the words `TRIM` and
`averageCounts` appeared somewhere. Deleting `+ TRIM` from `finished` left it **SILENT** —
the block matched neither shape and both words survived elsewhere in the file. It now
compares CODE LINES against an expectation derived from the lesson's own reveals.

**AND THE HEADER OF A THING IS STILL NOT THE THING (S140's rule 44, five more times).** Three
quiz-bank headers were written alongside their questions and named ids that had shifted during
drafting — L01 twice, L06 three times, L07 once. **Every one of them named an id that EXISTS**,
so a spot-check passes; only re-deriving what each id ASKS caught them. One cite also pointed
at a §3.9 that L07 does not have.

---

# SEPTEMBER 8 IS ABOUT FOUR WEEKS OUT

**READING QUIZZES — 7 of 16 WRITTEN (L01, L02, L03, L04, L05, L06, L07), 545 questions.**
Status is DERIVED: `python3 quizzes/quiz_bank.py --status`. **Read `quizzes/QUIZ_SPEC.md`
first (v1.1.0). THE ORDER IS CANON: READ -> FIX -> QUIZ**, and QUIZ_SPEC §0 requires the read
to have happened **in the same session** as the bank.

**L08 IS NEXT AND IT IS NOT YET READ.** L01–L07 are all read, fixed and banked.

**THE IN-SCOPE FIGURES ALL NEED DJ AND THE ROBOT.** Stills **3.2 · 3.5 · 3.6 · 4.1 · 4.3 ·
12.1**, videos **3.1 · 4.1 · 6.1 · 8.1**. `GRAPHIC 15.4` was never produced; its brief is in
the S135 chat. **VIDEO 3.1 carries L03's opening page** and is the highest-value shot.

---

# STATE

<!-- VERSION BLOCK: emitted by session_versions.py --handoff. Never hand-typed. -->
Fresh-clone verified at **`8b71826`**. Census **40,516**.
Bible **v8.133** · `BookComponentStandard` **v01.13.0** · Maker **v2.45.6** ·
`marks/` **41** · `icons/` **49** incl. LICENSE.
`ZUMO_Syllabus_WORKING.md` **v1.2**.

Instruments: `book_gates` **v1.65.2** · `lesson_inventory` **v1.3.5** ·
`gen_component` **v1.6.1** · `pill_sweep` **v1.1** · `gate_payload_match` **v1.7.1** ·
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

Lessons: L01 v03.28.3 · L02 v03.21.2 · L03 v03.41.0 · L04 v04.29.0 · L05 v04.29.0 · L06 v04.32.1 · L07 v04.31.2 · L08 v04.30.1 · L09 v05.26.1 · L10 v02.27.1 · L11 v02.28.2 · L12 v01.31.2 · L13 v02.28.2 · L14 v02.33.1 · L15 v02.30.1 · L16 v02.22.1.

**70/70 gates.** `lesson_inventory --anomalies` silent · family map **1120/1120** ·
`callout_id --audit` **1120, 0 problems** · `keyterm_prefix --audit` **238 = 151 + 4 + 83 + 0** ·
`build_css --check` current at 574 rules · `image_audit --check` current ·
`gate_payload_match` PASS · `strip_inline --verify` **0 dead class names** · the pin is
**55 rows** · `quiz_bank --selftest` **9/9 controls loud** · `quiz_bank --check` **7 banks
valid, 545 questions**.

---

# WHAT SHIPPED IN S141

**THE L06 CATCH-UP PAYLOADS ARE REVERTED TO THEIR OWN STEP. Maker v2.45.5 -> v2.45.6.** Five
payloads, five changed lines, `finished` untouched and byte-verified. The reversal targets were
EXTRACTED from L06's own Step 7 and Step 10 reveals, never retyped. **GATE 70 NEW**,
`book_gates` **v1.64.5 -> v1.65.2** — three controls, each firing gate 70 alone, including one
that rewords a comment in the lesson and proves the predicate really is derived. Bible **v8.133**,
§15.6 new, filed in BOTH version homes.

**L06 READ END TO END (it was edited in S140 but never read). L06 v04.32.0 -> v04.32.1.**
§5.4's without-`abs()` comment said *already true* where the paragraph beneath it and BRAIN
CHECK 01 Q5 both say **false** — and it contradicted itself, since a true condition runs.
Challenge 6's *Where to look* promised two while-loops where its own pseudocode and template
use one `while` with an `if`. **Observation Experiment 3 predicted an overshoot that cannot
happen** — the gate reads the left encoder, so retarding the RIGHT side turns the robot and
puts the left wheel on the OUTSIDE of the arc; it falls short. Rewritten so the two drags
produce two different KINDS of error, which is Step 13's own WARNING and plants L12 early.

**THE 39 mm WHEEL IS THE DIAMETER OVER THE TRACK, AND THE BOOK NOW SAYS SO IN FIVE PLACES.**
DJ confirmed the fleet ratio with Pololu, whose pages also give sprocket **35 mm**, diameter
with track **39 mm**, sprockets **85 mm** apart — so the wheel base is sourced too, and the
Zumo 32U4 User's Guide confirms 12 CPR x 75.81 = 909.7. §3.4 now names both numbers and says
why 39 is the one the maths uses; §4.1, the Quick Reference, Step 5's pseudo-code and
**GRAPHIC 6.5** all follow. The graphic was the worst of the five: it warned *measure the
diameter incorrectly and every driven distance is wrong* while labelling the measurement
ambiguously. **TIP 6.68 NEW** — calipers not a ruler, zero them, outside jaws through the
axle, gentle on silicone, three readings rotating between. DJ: tread is ~0.1 mm, which is
below the noise floor of the measurement, so it is deliberately not mentioned.

**L07 READ END TO END. L07 v04.31.1 -> v04.31.2, SEVEN FINDINGS.** Three callouts said Lesson
8 CREATES `RobotSensors` when Steps 3-4 create it today — contradicted by the lesson's own
Challenges 3 and 5 (*"your EXISTING RobotSensors files"*) and by L08's Step 3. **Step 4's GOAL
contradicted Step 4's own MY PLAN three lines apart**, seven objects against three, and the
Maker settles it at three. §8A.3's scope table put a **non-const global in RobotConfig.h**,
the exact shape §8's Error 2 names as multiple definition, in the file §8 calls *nothing but
const lines*. BRAIN CHECK 03 announced seven questions and asked six. Common Pitfall 3 said
*File A includes File B, which includes File B*. **`IMAGE 7.11` WAS REBUILT ENTIRELY** — its
banner read ERROR 3 over Error 4's message, for a function `driveStraight()` that exists
nowhere in this project, illustrating a scenario §3.8's own NOTE says produces no error at
all. It is now a terminal reproduction matching its siblings 7.9 and 7.10, and §8's Error 3
bullet moved with it.

**§8's SERIAL FIX WAS REORDERED RATHER THAN RE-CLAIMED.** The callout diagnosed the cause in
its own first sentence and then sent the student to check `monitor_speed` first — a value that
already matches by construction in every file they are handed. The real cause (timing) is now
Fix 1. **Nothing asserts the baud number is ignored**, because that claim rests on the book
alone: Pololu's USB-interface section never mentions baud rate in either direction. **L01 §5.0's
bullet was a different case and IS fixed** — §8 of the same lesson has said since S136 that the
number is ignored, so §5.0 was contradicting its own lesson, not an unsourced claim.

**THREE BANKS: L01 v1.0.0 (79), L06 v1.0.0 (78), L07 v1.0.0 (69).** All three written in the
session that read the lesson, per QUIZ_SPEC §0.

**ONE CALLOUT MOVED FOUR PINNED NUMBERS.** TIP 6.68 took labels 255 -> 256, image references
1,202 -> 1,203 (the lightbulb mark), the family map 1,119 -> 1,120, and the §27.11 digest.
`build_family_map` **v1.6.1**. The CSS cycle ran §27.8b in order: **class set byte-identical,
zero born, zero died, all 574 declaration blocks byte-identical**, rules and declarations
unchanged at 574/2,033 — usage RANK only, the S140 shape for the fifth time. **A callout is
never a free edit.**

---

# S142 QUEUE

## 1. CONTINUE THE READ — L08 IS NEXT
**L01–L07 are READ, FIXED AND BANKED. L08–L16 ARE NOT READ.**

## OPENED S141, UNRULED
- **THE BAUD BENCH TEST.** Set `monitor_speed = 9600`, leave `Serial.begin(115200)`, upload,
  open the monitor. Clean text means the number is ignored on this fleet and L02 §6 Step 2 can
  be quizzed; garbage means **L02 §6 Step 2 is wrong**, which is a much larger finding. Put
  `monitor_speed` back to 115200 after, and **keep 1200 out of the test** — Pololu's own revival
  procedure confirms 1200 baud triggers the bootloader reset on this chip.
- **THE 1200-BAUD RESET HAS NO HOME IN THE BOOK.** Real, sourced, and the mechanism behind every
  upload the students do. Candidate *Going Deeper* entry. Not askable from the text today.
- **IS 39 mm THE RIGHT EFFECTIVE DIAMETER FOR A TRACKED DRIVE?** The number is sourced as the
  outer diameter; whether travel per sprocket revolution follows the outer surface or the track's
  pitch line (somewhere between 35 and 39) is not settled. If nearer 37, true counts/cm is ~78
  rather than 74.3 and a commanded 30 cm lands ~1.6 cm short — **inside §7's own ±2 cm
  tolerance**, and §8's calibration step already absorbs it. Bench, not a correction.
- **`L07_IMAGE_7-11_header_in_wrong_folder.svg` IS NOW MISNAMED.** Under the rebuilt figure the
  wrong folder is the second cause, not the first. A rename is a deletion; deliberately not done
  unasked. Two-minute tidy: `L07_IMAGE_7-11_error_file_not_found.svg` plus the `<img src>`.
- **`IMAGE 7.9`, `7.10`, `7.11`, `7.12` ARE INDEXED AS *Photo / screenshot — still needed*** while
  all four are live drawn SVGs. Part of the parked IMAGE-tag-landed-by-a-GRAPHIC class.
- **THE CAPTION BOX IN `7.9` AND `7.10` IS CLIPPED** — `y=422, height=54` inside a `viewBox` of
  470, so the bottom 6px of its border is cut. Pre-existing across the set; a template fix.

## Carried from S140, still unruled
- **§3.2's *about 13½ milliseconds*** for the six-round proximity read — unverified, not wrong.
- **L05 §3.6 alkaline tension**: prose derives 6.0 V from 1.5 V/cell; the table reads 6,300 mV.
- **The `static` split is taught in L05 and L06 but the GLOSSARIES still disagree** — no lesson
  glossary defines the file-scope sense.

## Carried from S137/S138/S139, still unruled
- **§4.2's stall-current multiple**: *~1.5 A … roughly 5× its free-running draw*, where Pololu's
  no-load figure is ~0.10 A, i.e. ~15×. **Still not fixed, still not quizzed.**
- **`IMAGE 4.1` IS A PHANTOM IN THE FIGURE COUNT** — planned reads 146, true population 145.
- **THE CONSTANTS vs CONFIGURATION VOCABULARY DRIFT.** Derive the canonical set first.
- **NO GATE HOLDS A QUIZ BANK** and **NO GATE HOLDS A NAV PILL.** (Gate 70 closed the
  challenge-card/starter-payload half of this debt for L06 only — the general case is open.)
- **THE 3Pi+ NOTE COMES OUT OF L03** — needs a new root file as the 3Pi+ book seed.
- **`class period` APPEARS IN L10.** Read it before removing.
- **L03 C1's hint hands over the exact two numbers its own template blanks ask for** —
  **L07's Challenge 4 is a second instance**, LOGIC block gives 100 and 250, template blanks ask
  for both.
- **§3.3's header-contents bullet in L07 still lists *Include guards*** three sections before
  §3.6 files them under *The Old Way*. Same class as the S77 parked Self-Assessment note.
- **§7's BANNER is still three spellings** — 9 lessons `· Test It`, 6 bare, L12 `· Calibrate`.
- **L14's §10 is the only §10 that is not an exit ticket.**
- **Whether the `after` quiz set is graded at all.** Seven lessons now have one.

## Carried from S135, still open
- **THE SPIRAL ARC — RULED, ENUMERATED, DELIBERATELY NOT STARTED.** All-or-nothing. 13 of 171
  units. **Five approved first:** L04 4.4→L03 · L05 5.1→L04 · L06 6.7→L03,L04 · L12 12.2→L06 ·
  L15 15.2→L04. **THE SCAN IS BLIND TO THE REST.**
- **THE FIGURE BLOCK HAS FOUR SPELLINGS.** L12's is the best.
- **`svg_layout_audit.py` HAS FOUR MEASURED DEFECTS, NONE FIXED.**

## Carried from S133/S134, still unruled
KEY TERM paint is five grounds across 238 blocks · the four held body blocks are a FAMILY
question · head colour `#6a1b9a` is 16 blocks in clean strata · L03 `3.44` carries
`id="glossary-trim"` on a BODY block · `BookComponentStandard` §7.4 says 184 where the
measured figure is 238 · §6.5's nav-pill rule still says 12–14 where the live range is 10 to
19 · **§24.14a and §24.14b still have NO section body** · **L07 `[IMAGE 7.3]`** is landed by
a GRAPHIC across the two number spaces.

## Carried, unchanged
Should `ZUMO_FAMILY_PINS.md` carry a version home? · `css/semantic.css` carries none either ·
the 3 `glyph_scan` leads · quick-reference anchors in L02–L06 only · **timers appear in
L02/L03/L04 only — S69 burned a session on a false finding here, READ before counting** ·
the colour ledger, 16 items · `index.html` carries no version home · **L01's BC02 does not
carry L01's objectives (legacy, ruled S119)** · L14's score formula is `<code>` and is not
code · **the mark roster RECONCILES and is gated (61). Do not re-open.**

## AFTER SEPTEMBER 8 — PARKED ON PURPOSE, DO NOT START EARLY
- **REDO `GRAPHIC 4.7` IN THE BLUEPRINT COMPOSITION.** Do not re-derive the orientation —
  chips run **5 4 3 2 1** left to right.
- Challenge card Pass B · monetization/ebook · DISCOVERIES tagging.

## Learner mode & book content
L03_C05 Variable Speed · L03 C01/C05/C06 reference a `finished` payload that does not exist
for L03 · whole-template starters L08/L09/L10 · Maker batch · L01 VS Code multi-root step.

## Bench (need the robot — parked with photography)
Q017 L09 six numbers · Q044 calibration-spin · Q046 gyro-bias · L02 §5 green-LED ·
Constrain RUN_MS · cm/s at a stated BASE_SPEED · the floor rig for 3.2 / 3.5 / VIDEO 3.1 ·
a real TRIM run for `IMAGE 3.6` · **THE SURFACE TEST: run 7E on a lab tile.** ·
**L04's wave test and Act Two row-1 overflow.** · **L05 Experiment 3 at 45°.** ·
**NEW: L06 Experiment 3 both drags — the rewrite is right either way, but the bench sharpens
the wording.** · **NEW: the baud test above.** · **NEW: commanded 30 cm vs measured, across a
few robots, for the effective-diameter question.**

---

# PUSHING — READ THIS

Named-file CLI for adds and modifies; **GitHub Desktop for deletions.** **Never `git add .`**

1. **DELIVER THE FILES** via `present_files`; instructions and md5s in the CHAT ONLY.
2. **`(1)` does not mean stale.** Verify by **md5**, never by suffix.
3. **Never present a test file or a DIAGNOSTIC beside repo files.**
4. **Never produce PUSH_ME_*.md or MD5_*.txt.**
5. **`lessons/` IS PART OF THE FILENAME. `css/` and `quizzes/` likewise.**
6. **A push that bumps a version and omits LIVE.md is an INCOMPLETE push (§12.6).**
7. **Exactly ONE `ZUMO_SNN_HANDOFF.md` in the root (gate 28).**
8. **THE NUMBER IN THE FILENAME IS THE SESSION THAT READS IT.**
9. **Never write a real version number as an arrow pair in prose.**
10. **A document cannot name the commit that contains it.**
11. **AN EDIT TO A FILE WITH REPEATED LANDMARK LINES TARGETS AN INDEX AND ASSERTS IT** (§6.12c).
12. **AN EDIT THAT CHANGES LINE COUNT INVALIDATES EVERY LINE-KEYED TARGET BELOW IT.** Go DESCENDING.
13. **A SNAPSHOT TAKEN BEFORE THE WORK IS NOT A SNAPSHOT OF THE WORK.**
14. **A CONTROL THAT DEPENDS ON THE STATE OF WHAT IT AUDITS IS NOT A CONTROL.**
15. **A CONTROL RUN AGAINST AN UNTRACKED FILE HAS NO RESTORE PATH** — snapshot yourself.
16. **A LIBRARY MAY NOT EXIT.**
17. **RUN A BLINDING CONTROL AGAINST THE CONSUMER THAT CAN FAIL.** **S141 paid this again:**
    gate 70's far-side arm was checking for the WORDS `TRIM` and `averageCounts` and stayed
    silent on a real partial regression. **A gate that checks for a word is checking for a word.**
18. **A DERIVED KEY IS NOT AN IDENTITY.**
19. **A GATE THAT PINS A SPELLING CERTIFIES WHATEVER IT WAS GIVEN. PIN THE PROPERTY.**
20. **A HOLD THAT IS ALSO SATISFIED BY AN ACCIDENT IS NOT A HOLD.**
21. **SNAPSHOT THE STATE YOU ARE IN, NOT THE STATE YOU ARE LEAVING.**
22. **A GENERATED ARTEFACT PRINTING `DIFFERS` IS A LEAD, NOT AN INSTRUCTION.**
23. **A CONTROL THAT CANNOT TELL A LOST WORD FROM A LOST SPACE IS NOT A CONTROL.**
24. **THE ACCEPTANCE TEST FOR A CSS REGENERATION IS THE RESOLVED STYLING, NOT THE RULE COUNT.**
25. **A GENERATED CLASS NAME IS NOT A HANDLE.** Its `-N` suffix is assigned by usage RANK.
26. **MEASURE THE PROPERTY THE RULING NAMES, NOT A PROXY FOR IT.**
27. **A COVERAGE COUNT MEASURES BLOCKS SCANNED, NOT BLOCKS ASSERTED.**
28. **A STRUCTURAL CHANGE THAT ENDS A SENTENCE EARLY OWES THE SENTENCE A LOOK.**
29. **PIN THE DENOMINATOR, NOT THE REMAINDER.**
30. **A WORKING COPY YOU HAVE RUN TOOLS IN IS NOT THE REPO.** When two readings disagree, RE-CLONE.
31. **A LABEL IS NOT THE THING IT NAMES.**
32. **NOT EVERY SPLIT IS DRIFT.** Ask whether a variation CARRIES INFORMATION before normalising it.
33. **NO INSTRUMENT READS PROSE. Read the book.**
34. **A NUMBER IS ONLY CHECKABLE AGAINST THE OTHER FIFTEEN LESSONS.**
35. **COMPILE THE SNIPPET; LET THE BOOK'S OWN CODE TESTIFY.**
36. **A FACT THAT LIVES ONLY IN AN SVG IS NOT IN THE BOOK.** **S141's inverse:** a WRONG fact
    that lives only in an SVG is also not fixable in prose — `IMAGE 7.11` had to be rebuilt.
37. **READ -> FIX -> QUIZ, NEVER QUIZ FIRST** — and QUIZ_SPEC §0 requires the read to be in
    the SAME SESSION as the bank. The read is a perishable asset.
38. **A TEXT MATCH LOCATES; IT NEVER ANSWERS.** **S141 paid this in the good direction:** a sweep
    for the removed phrase *sails straight past* hit L15, where it correctly describes P-control
    overshoot. Read every hit in full before acting.
39. **NO INSTRUMENT THAT READS THE TREE CAN SEE A RULING.** Search the session record first.
40. **PULL THE PAYLOAD, NOT THE CARD.**
41. **AN ENTRY FILED IN ONE HOME IS NOT FILED.**
43. **WHEN TWO SECTIONS DISAGREE, READ THE CITATIONS.** The older text is usually the wrong one.
44. **THE HEADER OF A THING IS NOT THE THING.** **S141 paid this FIVE more times**, across three
    quiz-bank headers. Every wrong claim named an id that EXISTS, so existence is not the check —
    **re-derive what each id ASKS.**
45. **A SNAPSHOT YOU HAVE RUN TOOLS IN HIDES ITS OWN DEBRIS.** **S141 paid this again:** a root
    `__pycache__` was invisible against the working tree and showed instantly against a fresh clone.
42. **A SPEC'S OWN NUMBERS CAN BE ARITHMETICALLY IMPOSSIBLE.**
46. **NEW, S141: A CALLOUT IS NEVER A FREE EDIT.** One TIP moved four pinned numbers — a label
    count, an image-reference count, the family map's denominator and the CSS digest — because
    it carries a mark, a label and CSS usage rank. Budget the §27.8b cycle before adding one.
47. **NEW, S141: A STEP PAYLOAD IS THE FILE AS IT STANDS AT THAT STEP.** Where a lesson builds a
    defect ON PURPOSE, every payload before the repair still carries it. `after_step_N` is a
    snapshot of a build in progress, never an abbreviation of `finished`.
