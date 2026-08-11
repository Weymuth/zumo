# ZUMO — S145 HANDOFF (rewritten at S144 close · paste at top of Session 145)

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
13. **`rm -rf __pycache__` BEFORE `git status`.**
14. **THE AVR TOOLCHAIN IS ONE COMMAND AND IT NOW HAS A KNOWN CONTROL.**
    `apt-get install -y gcc-avr avr-libc`, clone the nine repos under `pololu/`
    (+ `arduino/ArduinoCore-avr`) and symlink them into `/home/claude/harness`, then
    `bash pio_harness.sh --setup`. **TWO REPO NAMES ARE TRAPS: the harness wants
    `usb-pause-arduino` (NOT `usb-pause-interrupt-arduino`) and also needs
    `pololu-menu-arduino`.** **THE CONTROL: L11 `after_step_1` MUST compile to 20,516 —
    that is S143's verified L10 `finished` figure, byte-for-byte. If it does not, stop;
    every number after it is worthless.**

---

# THE ONE THING TO CARRY OUT OF S144

**WHEN EVERY ARTEFACT AGREES, ASK WHETHER THE DESIGN IS RIGHT — NOT WHICH ONE IS THE DESIGN.**

S143 fired rule 51 once: `gate_payload_match` passed on 202 faithful copies of a maneuver
that could not work. S144 fired it twice more, in two different shapes, and the shapes are
the point.

**L10: every artefact agrees and the design is still short a step.** The rebuilt box turns
`+90`, `−90`, `−90` — net `−90` — so it arrives PERPENDICULAR to the line and nothing
realigns the robot. GRAPHIC 10.2 says *LINE FOUND — follow it again*; §3.3 says *ready to
cross it*; §7.7 claims *resumes as if nothing happened*; Sabotage B5 treats square-on as
correct. **There is no outlier to defer to.** In S143 the code was the outlier and the fix
was a reconciliation. Here the reconciliation is already done and the thing is still wrong.

**L11: the book contradicts itself across two lessons, and the OLDER one is right.** §3.5
rests on *no reflection reads exactly the same as the brightest possible white*. **L04's
troubleshooting table already says the opposite — *air counts as black* — and Pololu's own
QTRSensors header names the exact case, twice: larger values are lower reflectance, "a black
surface OR A VOID."** Two lessons, opposite answers, one physics question, invisible inside
either one.

**NEITHER WAS FINDABLE BY ANY INSTRUMENT IN THIS TREE, AND BOTH WERE SETTLED FROM OUTSIDE
IT** — one by arithmetic the tree cannot do, one by a library source the tree does not hold.

---

# SEPTEMBER 8 IS UNDER FOUR WEEKS OUT

**READING QUIZZES — status is DERIVED: `python3 quizzes/quiz_bank.py --status`.
`quizzes/QUIZ_SPEC.md` (v1.1.0) first. THE ORDER IS CANON: READ -> FIX -> QUIZ**, same session.

**L11 IS READ, FIXED AND UNBANKED — AND NO LONGER BLOCKED.** §3.5 was ruled and corrected at
S144 close, so the bank can be written against v02.30.0. **Six of its homes changed, so do
not reuse any question drafted before that.** L12–L16 are unread.

**THE IN-SCOPE FIGURES ALL NEED DJ AND THE ROBOT.** Stills **3.2 · 3.5 · 3.6 · 4.1 · 4.3 ·
12.1**, videos **3.1 · 4.1 · 6.1 · 8.1**. **VIDEO 3.1 carries L03's opening page.**

---

# STATE

<!-- VERSION BLOCK: emitted by session_versions.py --handoff. Never hand-typed. -->
Fresh-clone verified at **`6f5a276`**. Census **40,605**.
Bible **v8.135.3** · `BookComponentStandard` **v01.13.0** · Maker **v2.49.1** ·
`marks/` **41** · `icons/` **49** incl. LICENSE.
`ZUMO_Syllabus_WORKING.md` **v1.2**.

Instruments: `book_gates` **v1.65.10** · `lesson_inventory` **v1.3.5** ·
`gen_component` **v1.6.1** · `pill_sweep` **v1.1** · `gate_payload_match` **v1.8.0** ·
`build_family_map` **v1.6.3** · `callout_id` **v1.0** · `keyterm_prefix` **v1.0.1** · `build_mark_index` **v1.1.0** · `gen_bonus_banner` **v1.4.1** ·
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

Lessons: L01 v03.28.3 · L02 v03.21.2 · L03 v03.41.0 · L04 v04.29.0 · L05 v04.29.0 · L06 v04.32.1 · L07 v04.31.3 · L08 v04.31.0 · L09 v05.27.0 · L10 v02.29.1 · L11 v02.30.0 · L12 v01.31.2 · L13 v02.28.2 · L14 v02.33.1 · L15 v02.30.1 · L16 v02.22.1.

**Quiz banks: 10 of 16, 770 questions. Derive it; never read this sentence as current.**

---

# S145 QUEUE

## 1. ONE RULING IS STILL OPEN (the cliff was ruled and closed at S144 close)

- **THE CLIFF IS RULED AND CORRECTED (S144). DO NOT REOPEN IT.** §3.5, GRAPHIC 11.2, §8A.4,
  BRAIN CHECK 01 Q5, BRAIN CHECK 03 × 2, Challenge 5 and §2 objective 6 all now say the same
  thing: **a void reads BLACK, not white.** Over a cliff all five sensors read ~1000,
  `isLineVisible()` returns TRUE, the position lands dead centre, and the robot drives off
  the edge at full speed believing it found a perfect line — **the gap machinery never engages
  at all.** The fix is **sensor TYPE, not POSITION**: reflectance cannot separate tape from a
  void at any mounting position, so the boom argument is gone. **The conclusion is unchanged
  (*use a barrier*), so L13 §4.1 and L14 were untouched.** §8A.4 is now a one-minute EXPERIMENT
  — read white mat, black tape and open air, compare rows two and three — not arithmetic.
  **STILL WORTH DOING ON THE BENCH, as confirmation rather than as a blocker:** hold the robot
  over a table edge and read the five calibrated values. Expect ~1000 each.

- **TRIM'S HOME IS SPLIT BOOK-WIDE AND NOBODY HAS RULED IT.** Derived from lesson prose:
  **L01, L02, L04, L06 and L11 say Lesson 3; L07, L08 and L13 say Lesson 6; L03 says both.**
  **L06 ITSELF CREDITS LESSON 3, THREE TIMES** — the encoder lesson points back rather than
  claiming it, which is the strongest single signal. Lesson 3 is *titled* "Motor TRIM"
  (250 mentions against L06's 39). S144 fixed L11's seven and the two Maker payloads
  `gate_payload_match` flagged, and **STOPPED: 342 Maker payload comments still say
  Lesson 6 and were deliberately NOT swept.** A 342-site sweep on my own judgment is a
  ruling, not a fix. **Do not write a gate for this until it is ruled.**

## 2. BANK L11 FIRST — the read is already spent
Against **v02.30.0**. Then continue the arc at **L12**, which is unread.

## OPENED S144, UNRULED
- **L10's ARRIVAL GEOMETRY (above).** Bench prediction to falsify: set a block, run it, and
  **watch the two seconds after `SEEKING` flips to `FOLLOWING`.** If it crosses the tape and
  keeps going into open floor, the finding holds. **Challenge 6's wedge meets the line at
  30°, which a P-controller can pull out of; the box meets it at 90°, which it cannot —
  the CHALLENGE is the geometrically sound shape and the main build is not.**
- **§8A.4's *"Pololu rates the 75:1 gearmotors at roughly 65 cm/s flat out"* IS UNVERIFIED.**
  pololu.com is not reachable from the sandbox. Bench or DJ.
- **L11 §7A's 999.0 RULER TRICK HAS NEVER TOUCHED A FLOOR**, like every other L11 number.

## Carried from S143, still unruled
- **THE CATCH-UP CONVENTION IS SPLIT.** L07–L10 OFFSET (`step_N -> after_step_(N-1)`);
  L11–L16 IDENTITY. Clean across all 64 rows. **A gate pinning either would certify 64 and
  fail 32.** DJ to rule.
- **`AVOID_OUT_CM = 15.0` HAS NEVER TOUCHED A FLOOR.** · **CHALLENGE 6's WEDGE NUMBERS ARE
  SIMULATED, NOT DRIVEN.**
- **THE RESOURCE SECTION AS A BOOK PAGE — PARKED UNTIL AFTER SEPTEMBER 8 (DJ ruling).**
- **THE 100:1 Kp SUGGESTION IS UNVERIFIED AND THE DIRECTION IS CONTESTED.**
- **NO GATE HOLDS A QUIZ BANK** and **NO GATE HOLDS A NAV PILL.**

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
  §6.5's nav-pill rule says 12–14 where the live range is 10 to 19 · **§24.14a and §24.14b
  still have NO section body.**
- **THE AMBER LEAK: two of three closed.** L09's six were normalised (S143), **L10 10.5 was
  normalised (S144)**, and **L02 §2.7 is the last one** — deferred to its own read.

## Carried, unchanged
Should `ZUMO_FAMILY_PINS.md` carry a version home? · `css/semantic.css` carries none either ·
the 3 `glyph_scan` leads · quick-reference anchors in L02–L06 only · **timers appear in
L02/L03/L04 only — S69 burned a session on a false finding here, READ before counting** ·
the colour ledger, 16 items · `index.html` carries no version home · **L01's BC02 does not
carry L01's objectives (legacy, ruled S119)** · **the mark roster RECONCILES and is gated
(61). Do not re-open.**

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
**DRIVE THE SEVEN-PHASE BOX — the whole maneuver has never touched a floor** · **drive
Challenge 6's wedge and compare the two shapes for real** · **NEW: HOLD THE ROBOT OVER A
TABLE EDGE AND READ THE FIVE CALIBRATED VALUES.** Expect ~1000 each — the settling evidence
for §3.5 · **NEW: L11's whole §7 ladder, including the 999.0 ruler.**

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
15. **A CONTROL RUN AGAINST AN UNTRACKED FILE HAS NO RESTORE PATH.** **A TRACKED FILE HAS ONE,
    BUT `git checkout` RESTORES THE COMMITTED STATE, NOT THE STATE YOU WERE STANDING IN.**
    **S144: restore by `cp` from an md5-verified snapshot, and check the md5 after.**
16. **A LIBRARY MAY NOT EXIT.**
17. **RUN A BLINDING CONTROL AGAINST THE CONSUMER THAT CAN FAIL.**
18. **A DERIVED KEY IS NOT AN IDENTITY.**
19. **A GATE THAT PINS A SPELLING CERTIFIES WHATEVER IT WAS GIVEN. PIN THE PROPERTY.**
20. **A HOLD THAT IS ALSO SATISFIED BY AN ACCIDENT IS NOT A HOLD.**
21. **SNAPSHOT THE STATE YOU ARE IN, NOT THE STATE YOU ARE LEAVING.**
22. **A GENERATED ARTEFACT PRINTING `DIFFERS` IS A LEAD, NOT AN INSTRUCTION.**
23. **A CONTROL THAT CANNOT TELL A LOST WORD FROM A LOST SPACE IS NOT A CONTROL.**
24. **THE ACCEPTANCE TEST FOR A CSS REGENERATION IS THE RESOLVED STYLING, NOT THE RULE COUNT.**
    **S144 RE-DERIVED THE PROOF RATHER THAN CARRYING IT:** zero elements in the sixteen
    lessons carry two classes — the only 7 multi-class attributes in the tree are hand-authored
    pairs in `index.html` and `going_deeper.html`, outside the generated digest.
25. **A GENERATED CLASS NAME IS NOT A HANDLE.**
26. **MEASURE THE PROPERTY THE RULING NAMES, NOT A PROXY FOR IT.**
27. **A COVERAGE COUNT MEASURES BLOCKS SCANNED, NOT BLOCKS ASSERTED.**
28. **A STRUCTURAL CHANGE THAT ENDS A SENTENCE EARLY OWES THE SENTENCE A LOOK.**
29. **PIN THE DENOMINATOR, NOT THE REMAINDER.**
30. **A WORKING COPY YOU HAVE RUN TOOLS IN IS NOT THE REPO.** When two readings disagree, RE-CLONE.
31. **A LABEL IS NOT THE THING IT NAMES.**
32. **NOT EVERY SPLIT IS DRIFT.** **S144 PAID THIS TWICE:** the catch-up convention still
    carries information, and **TRIM's Lesson 3 / Lesson 6 split spans 342 payload comments —
    I fixed L11 and STOPPED.** Ask what a variation CARRIES before normalising it.
33. **NO INSTRUMENT READS PROSE. Read the book.**
34. **A NUMBER IS ONLY CHECKABLE AGAINST THE OTHER FIFTEEN LESSONS.**
35. **COMPILE THE SNIPPET; LET THE BOOK'S OWN CODE TESTIFY.**
36. **A FACT THAT LIVES ONLY IN AN SVG IS NOT IN THE BOOK** — and read the art's own
    coordinates before assuming the art is what is wrong.
37. **READ -> FIX -> QUIZ, NEVER QUIZ FIRST** — same session.
38. **A TEXT MATCH LOCATES; IT NEVER ANSWERS.**
39. **NO INSTRUMENT THAT READS THE TREE CAN SEE A RULING.** Search the session record first.
40. **PULL THE PAYLOAD, NOT THE CARD.**
41. **AN ENTRY FILED IN ONE HOME IS NOT FILED.**
42. **A SPEC'S OWN NUMBERS CAN BE ARITHMETICALLY IMPOSSIBLE.**
43. **WHEN TWO SECTIONS DISAGREE, READ THE CITATIONS.** The older text is usually wrong.
    **S144 INVERTS THIS: L04 vs L11 on what a void reads as, and the OLDER lesson is RIGHT.**
    The rule is *read the citations*, not *prefer the newer*.
44. **THE HEADER OF A THING IS NOT THE THING.**
45. **A SNAPSHOT YOU HAVE RUN TOOLS IN HIDES ITS OWN DEBRIS.**
46. **A CALLOUT IS NEVER A FREE EDIT — AND S144 PUT A NUMBER ON IT.** A seventh INSIGHT block
    in L11 failed **SIX** gates at once: §5.1 geometry, §21 image-reference coverage, §27.13,
    §24.14, §24.14a and §24.14c — every one a baseline pinned at six. **The fact became prose
    and all six cleared. Price the callout before you write it.**
47. **A STEP PAYLOAD IS THE FILE AS IT STANDS AT THAT STEP.**
48. **A VERIFIER THAT READS YOUR INTENT INSTEAD OF THE ARTEFACT VALIDATES NOTHING.**
49. **A NUMBER THAT A SENTENCE DERIVES FROM CANNOT BE SWAPPED WITHOUT REWRITING THE SENTENCE.**
50. **A COUNT INSIDE A SENTENCE IS A CLAIM. DERIVE IT OR DELETE IT.**
51. **A GATE THAT CERTIFIES AGREEMENT IS NOT CERTIFYING CORRECTNESS.** Faithfulness is not
    truth. **Something outside the tree has to check the physics.**
52. **WHEN THE ART AND THE CODE DISAGREE, ASK WHICH ONE IS THE DESIGN.**
53. **NEW, S144: WHEN EVERY ARTEFACT AGREES, ASK WHETHER THE DESIGN IS RIGHT.** Rule 52 has a
    ceiling. L10's box has GRAPHIC 10.2, §3.3, §7.7, Sabotage B5 and the code all agreeing —
    and it still arrives perpendicular to the line with nothing to realign it. **Unanimity is
    not evidence; it is the absence of a second opinion.**
54. **NEW, S144: A DIRECTIONAL CLAIM WITH NO NUMBER IS STILL A CLAIM.** Step 6 said the
    finished build was *smaller*. It is **186 bytes bigger** — measured against a control that
    reproduced 20,516 exactly. **No number is not the same as nothing to check**, and rule 50
    reaches *smaller*, *fewer* and *faster* as surely as it reaches *five*.
55. **NEW, S144: "NOTHING READS IT" IS NOT "NOTHING MENTIONS IT."** L11 Step 6 retired
    `gapStartTime` on a true statement — nothing read it — while **two lines still WROTE it**,
    and C++ needs the declaration either way. §6 promised every step compiles; §8 carried the
    resulting error and blamed the student, **repeating the same wrong word**. Before deleting
    a symbol, search the file and count every mention, whichever way the data flowed.
56. **NEW, S144: A CONTENT TIER THAT PINS A SPELLING OWES AN EDIT WHEN THE SPELLING IS THE
    DEFECT.** `build_family_map`'s INSIGHT tier matched the literal headline *"The stopwatch
    has no readers left"* — the very sentence that was false — so correcting the prose made
    the block unnameable and failed two gates. That coupling is the cost of a last-resort
    literal tier and is not a reason to avoid the fix: repoint the tier in the same pass.

57. **NEW, S144: AN EDIT THAT CHANGES LENGTH INVALIDATES OFFSETS COMPUTED BEFORE IT — INCLUDING
    OFFSETS IN THE SAME FUNCTION.** Rule 12 says this about line-keyed targets below an edit.
    S144 broke it a shorter way: I computed `i` and `j` with `.find()`, then ran three
    length-changing `.replace()` calls, then sliced `s[:i]+body+s[j:]`. It ate a `<div` opening
    tag and duplicated a `</details>`. **Slice first, or re-find after every replace. Tag
    balance caught it; nothing else would have.**
58. **NEW, S144: A CONTROL RUN ON THE PRE-EDIT FILE IS HOW YOU KNOW A FINDING IS YOURS.**
    `svg_layout_audit` reported an overflow on GRAPHIC 11.2 after my label edits, and that
    instrument carries four known measured defects — so the report alone proved nothing.
    **Running it on the untouched original returned CLEAN**, which is what made the overflow
    mine. When an instrument with known defects reports on a file you just changed, run it on
    the version you started from before you believe it either way.
