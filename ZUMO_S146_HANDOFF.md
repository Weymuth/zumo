# ZUMO — S146 HANDOFF (rewritten at S145 close · paste at top of Session 146)

## Session open ritual (do this without being asked)
1. **`git ls-remote https://github.com/Weymuth/zumo.git HEAD` FIRST.** A stale answer is
   timing, not caching — **retry a minute later before concluding a push failed** (§12.4).
   **S145 OPENED ON THE OTHER FAILURE MODE: the SHA matched and the CONTENT did not.**
2. Read `LIVE_ZUMO_TEXTBOOK.md` — verify date / status / versions.
3. **Do NOT grep the Bible version.** `session_versions.bible_consistency()` parses it.
4. Run the full suite and **READ THE EXIT CODE, NOT THE LAST LINE**. Plus
   **`callout_id.py --selftest` then `--audit`**, **`keyterm_prefix.py --audit`**,
   **`quizzes/quiz_bank.py --selftest` then `--check`**, and
   **`session_versions.py --selftest`** — **its CONTROL C is what reports an unfinished
   documentation pass, and at S145 open it was the ONLY thing in the tree that could see a
   push that had not landed.**
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
14. **THE AVR TOOLCHAIN IS ONE COMMAND AND IT NOW HAS A KNOWN CONTROL.**
    `apt-get install -y gcc-avr avr-libc`, clone the eight repos under `pololu/`
    (+ `arduino/ArduinoCore-avr`) into `/home/claude/harness`, checkout the Zumo library at
    tag **2.0.1**, then `bash pio_harness.sh --setup`. **TWO REPO NAMES ARE TRAPS: the
    harness wants `usb-pause-arduino` (NOT `usb-pause-interrupt-arduino`) and also needs
    `pololu-menu-arduino`.** **THE CONTROL: L11 `after_step_1` MUST compile to 20,516.**
    Verified twice in S145, from two different clones.
    **`shim.cpp` does not exist in the repo and is not needed — the harness guards for it.**

---

# THE ONE THING TO CARRY OUT OF S145

**A CONTROL THAT FIRES FOR THE WRONG REASON IS NOT A CONTROL.**

S145 fixed 18 stale byte figures in L12 and then ran a blinding control: revert one figure,
confirm something notices. **It fired. It was worthless.** The figure I happened to pick sat
inside a literal pinned by `build_family_map`'s content tier, so the gates were reporting an
unnameable callout — not a wrong number. Reverting a figure OUTSIDE every tier — B1's
Sabotage header — **passes all 70 gates and `gate_payload_match`.**

**NOTHING IN THIS TREE CAN SEE A WRONG BYTE FIGURE.** Only the AVR toolchain can, and nothing
in `book_gates.py` runs it. Same debt shape as *no gate holds a quiz bank* and *no gate holds
a nav pill* — logged the day it was created.

Rule 20 already said *a hold that is also satisfied by an accident is not a hold*. S145 is the
first session where the accident was **my own control**, and the only thing that exposed it was
picking a second target and asking the question again.

---

# SEPTEMBER 8 IS UNDER FOUR WEEKS OUT

**READING QUIZZES — status is DERIVED: `python3 quizzes/quiz_bank.py --status`.
`quizzes/QUIZ_SPEC.md` (v1.1.0) first. THE ORDER IS CANON: READ -> FIX -> QUIZ**, same session.

**L11 AND L12 ARE READ, FIXED AND BANKED. L13, L14, L15 AND L16 ARE UNREAD.**
**Course scope for Fall is L01–L12 (QUIZ_SPEC §9), so the remaining four banks may not be
needed for September at all — that is an open ruling, not an assumption.**

**THE IN-SCOPE FIGURES ALL NEED DJ AND THE ROBOT.** Stills **3.2 · 3.5 · 3.6 · 4.1 · 4.3 ·
12.1**, videos **3.1 · 4.1 · 6.1 · 8.1**. **VIDEO 3.1 carries L03's opening page.**
**`IMAGE 12.1` (the delrin sheet) is listed *still needed* in L12's figure table.**

---

# STATE

<!-- VERSION BLOCK: emitted by session_versions.py --handoff. Never hand-typed. -->
Fresh-clone verified at **`UNKNOWN`**. Census **40,605**.
Bible **v8.135.4** · `BookComponentStandard` **v01.13.0** · Maker **v2.49.2** ·
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

Lessons: L01 v03.28.3 · L02 v03.21.2 · L03 v03.41.0 · L04 v04.29.0 · L05 v04.29.0 · L06 v04.32.1 · L07 v04.31.4 · L08 v04.31.1 · L09 v05.27.0 · L10 v02.29.1 · L11 v02.30.0 · L12 v01.31.3 · L13 v02.28.3 · L14 v02.33.1 · L15 v02.30.1 · L16 v02.22.1.

**Quiz banks: 12 of 16, 920 questions. Derive it; never read this sentence as current.**

---

# S146 QUEUE

## 1. THE BYTE CASCADE — RULED AT S145, NOT STARTED. THIS IS THE BIG ONE.

**L16 carries a finished-size table for the whole book and six of its nine rows are wrong.**
Measured on the toolchain, control first:

| | L16 says | measured | |
|---|---|---|---|
| L07 | 14,380 | **14,380** | exact |
| L08 | 17,194 | **17,194** | exact |
| L09 | 18,158 | **18,158** | exact |
| L10 | 20,364 | **20,516** | +152 |
| L11 | 20,542 | **20,702** | +160 |
| L12 | 24,534 | **24,694** | +160 — **FIXED S145** |
| L13 | 24,902 | **25,072** | +170 |
| L14 | 25,640 | **25,816** | +176 |
| L15 | 28,034 | **28,214** | +180 |

**THE SEAM IS AT L10 — the lesson S143 rebuilt.** That correction and S144's L11 figure both
landed in their own lessons and **neither propagated**. L10 and L11 each carry exactly one
byte figure and both are already right; the damage is all downstream.

**THE CAPSTONE ARITHMETIC IS THE SHARP END AND IT IS NOT COSMETIC.** L16's whole premise is
*"Your Lesson 15 project is 28,034 of them. You have 638 bytes left — and this lesson is going
to spend them, run out, and hit the wall in front of you, on purpose."* **L15 finished measures
28,214, so the real headroom is 458.** The capstone budget is overstated by 180 bytes — **28%
more room than the chip has.** If L16's exercises are sized against 638 they overflow before
reaching the wall the lesson is built around. **Read L16's exercise budget before assuming the
fix is only numbers.**

**PRICE: ~80 byte figures across L13 (10), L14 (8), L15 (16) and L16 (47), each needing its own
compile.** L12's pass took 18 sites and cost one instrument bump.

**AND EXPECT RULE 56 AGAIN.** Correcting L12's figures broke `build_family_map`'s literal tier,
which pinned the exact sentence being corrected. **Grep the tier list for any figure you are
about to change, before you change it.**

## 2. THE READ ARC — L13 IS NEXT, AND ITS BYTE FIGURES ARE KNOWN STALE
L13 carries two `COMPILE CHECK 24,534` claims keyed to **L12's old figure**, plus 24,902 ×4,
24,714 ×2, 24,946 and 24,966. **Its read and its byte fix are the same job.** Measured L13
finished is **25,072**.

## 3. STILL OPEN, CARRIED
- **THE CATCH-UP CONVENTION IS SPLIT.** L07–L10 OFFSET (`step_N -> after_step_(N-1)`);
  L11–L16 IDENTITY. Clean across all 64 rows. **A gate pinning either would certify 64 and
  fail 32.** DJ to rule.
- **L10's ARRIVAL GEOMETRY (S144, unruled).** The rebuilt box turns `+90`, `−90`, `−90` — net
  `−90` — so it arrives PERPENDICULAR to the line with nothing to realign it, and **every
  artefact agrees with the code.** Bench prediction: watch the two seconds after `SEEKING`
  flips to `FOLLOWING`. **Challenge 6's wedge meets the line at 30°, which a P-controller can
  pull out of; the box meets it at 90°, which it cannot.**
- **§8A.4's *"Pololu rates the 75:1 gearmotors at roughly 65 cm/s flat out"* IS UNVERIFIED.**
  pololu.com is not reachable from the sandbox.
- **`AVOID_OUT_CM = 15.0` HAS NEVER TOUCHED A FLOOR.** · **CHALLENGE 6's WEDGE NUMBERS ARE
  SIMULATED.** · **L11 §7A's 999.0 RULER TRICK HAS NEVER TOUCHED A FLOOR.**
- **THE RESOURCE SECTION AS A BOOK PAGE — PARKED UNTIL AFTER SEPTEMBER 8.**
- **THE 100:1 Kp SUGGESTION IS UNVERIFIED AND THE DIRECTION IS CONTESTED.**
- **NO GATE HOLDS A QUIZ BANK** · **NO GATE HOLDS A NAV PILL** · **NEW: NO GATE HOLDS A BYTE
  FIGURE.**
- **§16.14 HAS NO NUMBERED SECTION BODY.** v8.135.3 announces *§16.14 NEW* and the Bible carries
  no `### 16.14` line — S144's cliff ruling lives only in a changelog entry. **§16.12 and
  §16.13 are also seated BELOW §17's heading**, and §16.15 was seated beside them rather than
  moving three sections in a pass nobody ruled.
- **L12 §3.2's *5.5 counts per degree* IS A ROUNDING ARTIFACT, NOT A DEFECT.** The real constant
  computes to **5.507**, so 90° is 495.7 counts and the lesson's **496 is right** — but 5.5 × 90
  is 495. Recorded as a lead. **Not asked in the L12 bank, for that reason.**

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
EDGE AND READ THE FIVE CALIBRATED VALUES** — expect ~1000 each · **L11's whole §7 ladder,
including the 999.0 ruler** · **NEW: L12's §7 ladder — 7A hand-turn, 7B uncalibrated drift,
7C encoder-vs-gyro on a slick surface, 7D, 7E's two squares. NONE of it has been driven, and
`IMAGE 12.1` (the delrin sheet) has never been shot.**

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
15. **A CONTROL RUN AGAINST AN UNTRACKED FILE HAS NO RESTORE PATH.** Restore by `cp` from an
    md5-verified snapshot, and check the md5 after.
16. **A LIBRARY MAY NOT EXIT.**
17. **RUN A BLINDING CONTROL AGAINST THE CONSUMER THAT CAN FAIL.**
18. **A DERIVED KEY IS NOT AN IDENTITY.**
19. **A GATE THAT PINS A SPELLING CERTIFIES WHATEVER IT WAS GIVEN. PIN THE PROPERTY.**
20. **A HOLD THAT IS ALSO SATISFIED BY AN ACCIDENT IS NOT A HOLD.** **S145 EXTENDS THIS TO THE
    CONTROL ITSELF — see rule 59.**
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
32. **NOT EVERY SPLIT IS DRIFT.** **S145 CLOSED THE TRIM CASE AND THE ANSWER WAS BOTH:** 194
    sites of drift beside 148 carrying a true fact, in one population reported as one number.
33. **NO INSTRUMENT READS PROSE. Read the book.**
34. **A NUMBER IS ONLY CHECKABLE AGAINST THE OTHER FIFTEEN LESSONS.** **S145: L16's byte table
    is exactly this, and six of its nine rows were wrong.**
35. **COMPILE THE SNIPPET; LET THE BOOK'S OWN CODE TESTIFY.**
36. **A FACT THAT LIVES ONLY IN AN SVG IS NOT IN THE BOOK.**
37. **READ -> FIX -> QUIZ, NEVER QUIZ FIRST** — same session.
38. **A TEXT MATCH LOCATES; IT NEVER ANSWERS.** **S145 PAID THIS TWICE ON ONE QUESTION:** *L03
    says both* and *L09 says Lesson 6* were both text matches read as answers, and both were
    false — L03's hits are forward pointers to encoders, L09's describes `turnDegrees()`.
39. **NO INSTRUMENT THAT READS THE TREE CAN SEE A RULING.** Search the session record first.
40. **PULL THE PAYLOAD, NOT THE CARD.**
41. **AN ENTRY FILED IN ONE HOME IS NOT FILED.**
42. **A SPEC'S OWN NUMBERS CAN BE ARITHMETICALLY IMPOSSIBLE.**
43. **WHEN TWO SECTIONS DISAGREE, READ THE CITATIONS.** The rule is *read the citations*, not
    *prefer the newer* — S144 inverted it on L04 vs L11.
44. **THE HEADER OF A THING IS NOT THE THING.**
45. **A SNAPSHOT YOU HAVE RUN TOOLS IN HIDES ITS OWN DEBRIS.**
46. **A CALLOUT IS NEVER A FREE EDIT.** A seventh INSIGHT in L11 failed SIX gates at once.
47. **A STEP PAYLOAD IS THE FILE AS IT STANDS AT THAT STEP.**
48. **A VERIFIER THAT READS YOUR INTENT INSTEAD OF THE ARTEFACT VALIDATES NOTHING.**
49. **A NUMBER THAT A SENTENCE DERIVES FROM CANNOT BE SWAPPED WITHOUT REWRITING THE SENTENCE.**
    **S145's COROLLARY: WHEN THE DELTAS ARE ALREADY RIGHT, THE SWAP IS SAFE.** All eighteen
    L12 figures moved and not one sentence needed rewriting, because +800, +0, +3,192 and −204
    were correct against the new absolutes as well as the old.
50. **A COUNT INSIDE A SENTENCE IS A CLAIM. DERIVE IT OR DELETE IT.**
51. **A GATE THAT CERTIFIES AGREEMENT IS NOT CERTIFYING CORRECTNESS.** Something outside the
    tree has to check the physics — **and now, the arithmetic.**
52. **WHEN THE ART AND THE CODE DISAGREE, ASK WHICH ONE IS THE DESIGN.**
53. **WHEN EVERY ARTEFACT AGREES, ASK WHETHER THE DESIGN IS RIGHT.** Unanimity is not evidence;
    it is the absence of a second opinion.
54. **A DIRECTIONAL CLAIM WITH NO NUMBER IS STILL A CLAIM.** *Smaller*, *fewer* and *faster*
    are as checkable as *five*.
55. **"NOTHING READS IT" IS NOT "NOTHING MENTIONS IT."**
56. **A CONTENT TIER THAT PINS A SPELLING OWES AN EDIT WHEN THE SPELLING IS THE DEFECT.**
    **THIRD FIRING, S145:** `build_family_map` pinned *Build it. 21,342 → 24,534 bytes*, the
    exact sentence being corrected. **Repoint it in the same pass; grep the tier list BEFORE
    editing any sentence that carries a number.**
57. **AN EDIT THAT CHANGES LENGTH INVALIDATES OFFSETS COMPUTED BEFORE IT.** Slice first, or
    re-find after every replace.
58. **A CONTROL RUN ON THE PRE-EDIT FILE IS HOW YOU KNOW A FINDING IS YOURS.**
59. **NEW, S145: A CONTROL THAT FIRES FOR THE WRONG REASON IS NOT A CONTROL.** I reverted one
    of eighteen corrected byte figures to prove something could see it. Two gates failed and I
    nearly recorded that as evidence — **they were failing because the figure sat inside a
    pinned literal, not because anything checks byte counts.** A second target, outside every
    tier, **passes all 70 gates.** Rule 20 is about the artefact being held by an accident;
    this is about the CONTROL being satisfied by one. **Ask what your control would report if
    the property you are testing did not exist at all** — and if the answer is *the same
    thing*, you have not tested it.
60. **NEW, S145: A SHA THAT MATCHES DOES NOT MEAN THE CONTENT LANDED.** S145 opened with the
    handoff naming `6f5a276` and claiming L11 v02.30.0, Bible v8.135.3 and `book_gates`
    v1.65.10 — **at that exact SHA the tree held v02.29.0, v8.135.2 and v1.65.9.** §12.4's
    retry-for-timing does not reach this case: the remote was correct and current, and the
    close-out work had simply never been committed. **The version block is the check, not the
    SHA** — `session_versions --check` named seven disagreements and `--selftest` CONTROL C
    named the cause.
