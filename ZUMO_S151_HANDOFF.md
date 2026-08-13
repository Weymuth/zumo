# ZUMO — S151 HANDOFF (rewritten at S150 close · paste at top of Session 151)

## Session open ritual (do this without being asked)
1. **`git ls-remote https://github.com/Weymuth/zumo.git HEAD` FIRST.** A stale answer is
   timing, not caching — **retry a minute later before concluding a push failed** (§12.4).
   **AND THE SHA IS NOT THE CHECK. `session_versions --check` IS** (rule 60, S145).
2. Read `LIVE_ZUMO_TEXTBOOK.md` — verify date / status / versions.
3. **Do NOT grep the Bible version.** `session_versions.bible_consistency()` parses it.
4. Run the full suite and **READ THE EXIT CODE, NOT THE LAST LINE**. **THE SUITE IS 71 GATES
   NOW, NOT 70.** Plus **`callout_id.py --selftest` then `--audit`**,
   **`keyterm_prefix.py --audit`**, **`quizzes/quiz_bank.py --selftest` then `--check`**, and
   **`session_versions.py --selftest`** — **its CONTROL C is the unfinished-documentation-pass
   signal and nothing else in the tree can see one.**
5. **`--anomalies` BELONGS TO `lesson_inventory`, NOT `session_versions`.**
   **`svg_layout_audit.py` TAKES FILENAMES. A bare invocation prints usage and exits 1 —
   that is a usage error, not a finding.** **`pill_sweep.py` and `class_sweep.py` also take
   arguments; a bare run is a usage error, not a finding either.**
6. `pip install cairosvg --break-system-packages` **and `pyyaml`. Needed every session.**
7. **NEVER run `build_css.py --help` or `session_versions.py --help`.** Read the docstring.
8. **`book_gates.py` TAKES NO ARGUMENTS. Passing it the lesson glob makes `build_family_map`
   resolve ROOT to a lesson FILE and the run dies at gate 60** (S150 lost a run to this).
9. **Do not hand-type a version, and do not hand-type a COUNT.**
10. **`gate_payload_match.py` needs `newproject.html` FIRST, then the full lesson glob.**
11. **A CLONE IS NOT THE SITE.** Run `site_parity.py` after any push.
12. **VERIFY THE PUSH BY FRESH CLONE AND MD5 — AND DIFF THE STAGE AGAINST THE CLONE.**
13. **`css/semantic.css` AND `ZUMO_FAMILY_PINS.md` ARE HAND-AUTHORED PRESERVED LAYERS.**
14. **`rm -rf __pycache__` BEFORE `git status`. Also `find . -name pbuild -exec rm -rf {} +`**
    if the toolchain has been run.

## 15. THE AVR TOOLCHAIN — S146's INSTRUCTIONS STILL HOLD. NOT RUN IN S150.

`apt-get install -y gcc-avr avr-libc` **(no `sudo` — it is not on this box, exit 127).** Clone
into `/home/claude/harness` **FLAT, not under a `pololu/` subdirectory**.

**READ THE EIGHT LIBRARIES OUT OF `LIBDIRS` IN THE SCRIPT. DO NOT CARRY THEM FROM A HANDOFF —
INCLUDING THIS ONE.** Also clone `arduino/ArduinoCore-avr`. Zumo library at tag **2.0.1**
(plain clone then `git checkout 2.0.1`; `--depth 1` cannot check out a tag). `cp pio_harness.sh`
into `$H`, then `bash pio_harness.sh --setup`. **Expect *objects: 41*.**

**THE CONTROL: L11 `after_step_1` MUST COMPILE TO 20,516.** Held S144–S149, from five clones.
**The harness prints `flash=` on success and `OVER flash=` on an overflow — parse both.**

---

# THE ONE THING TO CARRY OUT OF S150

**THE `<title>` TAG WAS THE ONLY TITLE SLOT WITH NO INSTRUMENT ON IT, AND THAT IS EXACTLY WHERE
THE BOOK DRIFTED.**

A lesson has a BANNER name (`<h1>`, §5b footer) and a CATALOG name (the §6.5a strip's `title=`,
`index.html`, `<title>`, and both generated pointers). **They are not required to agree** — L01
runs *Sense, Decide, Act* over *Hello, Robot!* and five other lessons do the same. **The defect
was L15 and L16 putting their `h1` in the `<title>` tag.**

**EVERY GENERATED SLOT WAS RIGHT.** `next_pointer` and `title_feed` both derive from the strip,
so L14's footer pointer read *Advanced PID Control* while L15's own tab read *The Present Isn't
Enough*. **Rule 51 at its sharpest: unanimity among the generated artefacts certified nothing
about the slot nobody generated.** S70 found it; §25.9 carried it under *not built, not ruled*
for **eighty sessions**, because no instrument opened the tag.

**§6.5c NEW · GATE 71 NEW.** Predicate DERIVED from the strip, never pinned. **The blinding
control is the proof: rename Lesson 6 in all sixteen strips and gate 71 names L06 ALONE.**

**AND THE GATE FOUND A THIRD SPLIT ON ITS FIRST RUN — SEE THE QUEUE. DJ TO RULE.**

---

<!-- VERSION BLOCK: emitted by session_versions.py --handoff. Never hand-typed. -->
Fresh-clone verified at **`0a08cd1`**. Census **40,642**.
Bible **v8.141** · `BookComponentStandard` **v01.13.0** · Maker **v2.49.4** ·
`marks/` **41** · `icons/` **49** incl. LICENSE.
`ZUMO_Syllabus_WORKING.md` **v1.2**.

Instruments: `book_gates` **v1.66.0** · `lesson_inventory` **v1.3.5** ·
`gen_component` **v1.6.1** · `pill_sweep` **v1.1** · `gate_payload_match` **v1.8.0** ·
`build_family_map` **v1.6.4** · `callout_id` **v1.0** · `keyterm_prefix` **v1.0.1** · `build_mark_index` **v1.1.0** · `gen_bonus_banner` **v1.4.1** ·
`gen_part_banners` **v1.2** · `session_versions` **v1.25.0** · `fit_raster_svg` **v1.2** ·
`flatten_alpha` **v1.2** · `svg_layout_audit` **v1.20** · `site_parity` **v1.1** ·
`build_css` **v1.3.0** ·
`image_audit` **v1.2** ·
`strip_inline` **v1.2** ·
`build_worklist` **v1.1** ·
`regex_audit` **v1.0** ·
`byte_audit` **v1.1** ·
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

Lessons: L01 v03.28.3 · L02 v03.21.3 · L03 v03.41.0 · L04 v04.29.0 · L05 v04.29.0 · L06 v04.32.1 · L07 v04.31.4 · L08 v04.31.1 · L09 v05.27.0 · L10 v02.29.2 · L11 v02.30.0 · L12 v01.31.3 · L13 v02.29.0 · L14 v02.34.0 · L15 v02.31.1 · L16 v02.23.1.

**Derive the bank count, never read it out of a sentence:** `python3 quizzes/quiz_bank.py --status`

---

# S150's OPEN FINDINGS

- **THE `<title>` SEPARATOR IS SPLIT AND IS DJ'S TO RULE.** **L03 and L04 write
  `Lesson N: Name | Zumo 32U4 Robotics`; the other fourteen write an em dash.** Found by gate
  71 on its first run. **Gate 71 deliberately asserts the NAME and not the separator** — widening
  it certifies a split nobody ruled, narrowing it convicts two lessons on a ruling never made
  (rule 26). Two minor bumps if DJ rules the em dash; the gate then tightens in one line.
- **`byte_audit` STILL EXITS 1 ON EXACTLY ONE ROW.** L16 Step 5's first COMPILE CHECK promises
  **28,756** — the state after the Serial trade, before the Z–N trade. The number is right.
  **No Maker payload produces it**, so a student stuck at that intermediate has no catch-up and
  no instrument can verify the figure. **Author the payload or rule the figure exempt. DJ was
  shown both at S150 open and ruled neither — it is still open.**
- **§16.18 THROUGH §16.21 HAVE NO NUMBERED SECTION BODIES**, same as §16.14. §6.5c was seated
  properly this session to avoid making it worse.
- **ARM 2 OF `byte_audit` REACHES TWO LESSONS.** L11–L14 quote byte figures in tables and prose,
  not in step headings, so they are covered only by ARM 2b's leads.


# S151 QUEUE

**The read arc is finished. Every lesson is read, fixed and banked.** What is left is not
content.

## 1. THE PHOTOGRAPHY — THE ONLY THING BETWEEN THE BOOK AND SEPTEMBER
Stills **3.2 · 3.5 · 3.6 · 4.1 · 4.3 · 12.1 · 13.1 · 13.2**, videos **3.1 · 4.1 · 6.1 · 8.1**.
**VIDEO 3.1 carries L03's opening page.** Nothing in the tree can produce them.
*(`IMAGE 14.1` and `IMAGE 16.1` are also unshot but both lessons sit outside the September
scope.)*

## 2. FOUR INVARIANTS WITH NO GATE — AND THE CASE FOR CLOSING ONE IS NOW STRONGER
**NO GATE HOLDS A QUIZ BANK · A NAV PILL · A BYTE FIGURE · A RULE CITATION.**
**S148 makes the byte-figure gate look cheap and the quiz-bank gate look urgent.** The
compile-against-figure verifier written this session is ~40 lines: parse the figures out of a
lesson, compile the payload each one names, assert equality. **It would have caught L16's
unbuildable finished build months ago.** It cannot live in `book_gates.py` (no toolchain in a
normal session) but it could be a standalone `byte_audit.py` run whenever the harness is up.
**The citation one is also cheaper than it was**, because every L14 citation now names its
edition — a gate can assert the edition string is present without validating a section number
it cannot look up.

## 3. STILL OPEN, CARRIED
- **THE CATCH-UP CONVENTION IS SPLIT.** L07–L10 OFFSET, L11–L16 IDENTITY, clean across all 64
  rows. **A gate pinning either would certify 64 and fail 32.** DJ to rule.
- **L15's TITLE IS SPLIT BOOK-WIDE AND THE GENERATOR IS ON THE WRONG SIDE.** L15 names itself
  *The Present Isn't Enough*; the nav strip in all 16 lessons says *Advanced PID Control*, and
  `next_pointer.py` derives from the strip — so L14's footer pointer is **generated wrong, not
  typed wrong** (rule 51). **S147 and S148 both held it deliberately. With the read arc closed
  this is now the largest un-ruled item in the book.**
- **`GRAPHIC 16.1` OVERFLOWS ITS PANEL BY 31 UNITS** — *"the sensors rent ~960 B of it (heap)"*
  spans 410..690 inside 435..665. Found by `svg_layout_audit` at S148 close; that file was not
  touched this session, so it is pre-existing. **Recorded, not fixed.**
- **§4.2's AUDIT TABLE IS UNCONFIRMED AND MAY NOT BE CONFIRMABLE.** An `avr-nm` pass by symbol
  name under-counts it badly (buzzer 598 B where deletion proves 1,828). The table says
  "Approx. cost" and the one row measurable by deletion matches. **Left alone deliberately —
  the instrument, not the table, is what failed.**
- **L10's ARRIVAL GEOMETRY (S144, unruled)** — every artefact agrees with the code; only the
  floor can settle it.
- **§8A.4's 65 cm/s IS UNVERIFIED** (pololu.com unreachable). · **L14 §8A.2's "five orders of
  magnitude"** needs the kill-switch poll at ~6 µs. · **`AVOID_OUT_CM = 15.0` HAS NEVER TOUCHED
  A FLOOR** · **CHALLENGE 6's WEDGE NUMBERS ARE SIMULATED** · **L11 §7A's 999.0 RULER TRICK.**
- **L14's GLOSSARY says "95% ten times" where §3.1 teaches 90%** — confirmed live, deliberately
  not fixed (both are true of the same principle), and named in the bank as unasked.
- **THE RESOURCE SECTION AS A BOOK PAGE — PARKED UNTIL AFTER SEPTEMBER 8.**
- **§16.14 HAS NO NUMBERED SECTION BODY.** §16.12 and §16.13 sit BELOW §17's heading.
- **L14 §10 IS THE ONLY §10 THAT IS NOT AN EXIT TICKET** — the Competition Day Playbook. Unruled.

## Carried from S141/S140, still unruled
- **THE BAUD BENCH TEST** · **THE 1200-BAUD RESET HAS NO HOME** · **`IMAGE 7.9`–`7.12` INDEXED
  AS *Photo / screenshot*** where four drawn SVGs exist · **§3.2's *about 13½ milliseconds***
  · **L05 §3.6 alkaline tension** · **the `static` split glossaries still disagree.**

## Carried from S137/S138/S139, still unruled
- **§4.2's stall-current multiple** · **`IMAGE 4.1` IS A PHANTOM IN THE FIGURE COUNT** ·
  **CONSTANTS vs CONFIGURATION DRIFT** · **THE 3Pi+ NOTE COMES OUT OF L03** · **L03 C1's hint
  hands over the numbers its own blanks ask for** (L07 C4, L08 C4 are instances two and three)
  · **§3.3's header-contents bullet in L07 still lists *Include guards*** · **§7's BANNER is
  three spellings** · **whether the `after` quiz set is graded at all.**

## Carried from S135/S133/S134, still open
- **THE SPIRAL ARC — RULED, ENUMERATED, DELIBERATELY NOT STARTED.** 13 of 171 units.
- **THE FIGURE BLOCK HAS FOUR SPELLINGS** (L12's is best) · **`svg_layout_audit.py` HAS FOUR
  MEASURED DEFECTS, NONE FIXED** · KEY TERM paint is five grounds across 238 blocks · L03
  `3.44` carries `id="glossary-trim"` on a BODY block · `BookComponentStandard` §7.4 says 184
  where the measured figure is 238 · §6.5's nav-pill rule says 12–14 where the live range is
  10 to 19 · **THE AMBER LEAK: L02 §2.7 is the last of three.**

## AFTER SEPTEMBER 8 — PARKED ON PURPOSE, DO NOT START EARLY
**THE RESOURCE SECTION PAGE** · **REDO `GRAPHIC 4.7` IN THE BLUEPRINT COMPOSITION** (chips run
**5 4 3 2 1** left to right — do not re-derive) · Challenge card Pass B · monetization/ebook ·
DISCOVERIES tagging · TDP template v3 A5 Lab Log.

## Learner mode & book content
L03_C05 Variable Speed · L03 C01/C05/C06 reference a `finished` payload that does not exist for
L03 · whole-template starters L08/L09/L10 · Maker batch · L01 VS Code multi-root step.

## Bench (need the robot — parked with photography)
Q017 L09 six numbers · Q044 calibration-spin · Q046 gyro-bias · L02 §5 green-LED · Constrain
RUN_MS · **cm/s at a stated BASE_SPEED** · the floor rig for 3.2 / 3.5 / VIDEO 3.1 · a real
TRIM run for `IMAGE 3.6` · **run 7E on a lab tile** · **L04's wave test and Act Two row-1
overflow** · **L05 Experiment 3 at 45°** · **L06 Experiment 3 both drags** · **the baud test**
· **commanded 30 cm vs measured across a few robots** · **DRIVE THE SEVEN-PHASE BOX** · **drive
Challenge 6's wedge** · **HOLD THE ROBOT OVER A TABLE EDGE AND READ THE FIVE CALIBRATED
VALUES** (expect ~1000 each) · **L11's §7 ladder** · **L12's §7 ladder** · **L13's ENTIRE §7
LADDER** — 7A's surface-meter table gates all four of L13's tunables and no student can finish
Lesson 13 without it · **L14's §7 ladder** · **NEW: L15's WHOLE §7 LADDER — nobody has read a
real dt off the strip chart, found a real K<sub>u</sub>, or measured a real T<sub>u</sub> on
this fleet** · **NEW: L16's §7.1 baseline — no course has ever been benchmarked.**
**Every §7 measurement in L13, L14, L15 and L16 is named in those banks as deliberately unasked
for exactly this reason.**

---

# PUSHING — READ THIS

Named-file CLI for adds and modifies; **GitHub Desktop for deletions.** **Never `git add .`**

1. **DELIVER THE FILES** via `present_files`; instructions and md5s in the CHAT ONLY.
2. **`(1)` does not mean stale.** Verify by **md5**, never by suffix.
3. **Never present a test file or a DIAGNOSTIC beside repo files.**
4. **Never produce PUSH_ME_*.md or MD5_*.txt.**
5. **`lessons/`, `css/`, `quizzes/` and `images/` ARE PART OF THE FILENAME.**
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
17. **RUN A BLINDING CONTROL AGAINST THE CONSUMER THAT CAN FAIL.**
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
33. **NO INSTRUMENT READS PROSE — AND NONE COMPILES EITHER.** **S148's completion: seventy
    gates and `gate_payload_match` all passed on a Lesson 16 whose finished build could not be
    flashed. Structure was perfect. The program did not fit. Point the toolchain at every kind.**
34. **A NUMBER IS ONLY CHECKABLE AGAINST THE OTHER FIFTEEN LESSONS.**
35. **COMPILE THE SNIPPET; LET THE BOOK'S OWN CODE TESTIFY.**
36. **A FACT THAT LIVES ONLY IN AN SVG IS NOT IN THE BOOK.** **S148's corollary: and a WRONG
    fact in an SVG is still wrong. `GRAPHIC 16.2` carried nine stale ladder values and two
    stale step figures that no prose check would ever have reached. Derive the chart's scale
    from its own geometry and recompute, rather than swapping labels over bars that then lie.**
37. **READ -> FIX -> QUIZ, NEVER QUIZ FIRST — AND THE READ DOES NOT TRANSFER BETWEEN SESSIONS.**
38. **A TEXT MATCH LOCATES; IT NEVER ANSWERS.** **S148: three of thirteen sweep hits were
    `"before the"` inside legitimate prose. Read every hit.**
39. **NO INSTRUMENT THAT READS THE TREE CAN SEE A RULING.**
40. **PULL THE PAYLOAD, NOT THE CARD.**
41. **AN ENTRY FILED IN ONE HOME IS NOT FILED.**
42. **A SPEC'S OWN NUMBERS CAN BE ARITHMETICALLY IMPOSSIBLE.**
43. **WHEN TWO SECTIONS DISAGREE, READ THE CITATIONS — AND WHEN THE CITATIONS DISAGREE, READ
    THE RULEBOOK'S CHANGELOG. If you do not HAVE the rulebook, say so and stop.**
44. **THE HEADER OF A THING IS NOT THE THING.** **S148 paid it three times — every bank's own
    description line was wrong about the bank until it was re-derived from the file.**
45. **A SNAPSHOT YOU HAVE RUN TOOLS IN HIDES ITS OWN DEBRIS.**
46. **A CALLOUT IS NEVER A FREE EDIT.** **S148: one family change fired FIVE gates. Prose cost
    nothing and cleared four of them.**
47. **A STEP PAYLOAD IS THE FILE AS IT STANDS AT THAT STEP.**
48. **A VERIFIER THAT READS YOUR INTENT INSTEAD OF THE ARTEFACT VALIDATES NOTHING.**
49. **A NUMBER THAT A SENTENCE DERIVES FROM CANNOT BE SWAPPED WITHOUT REWRITING THE SENTENCE.**
    The S145 corollary stays REVOKED. **Four consecutive sessions now.**
50. **A COUNT INSIDE A SENTENCE IS A CLAIM. DERIVE IT OR DELETE IT.**
51. **A GATE THAT CERTIFIES AGREEMENT IS NOT CERTIFYING CORRECTNESS.**
52. **WHEN THE ART AND THE CODE DISAGREE, ASK WHICH ONE IS THE DESIGN.**
53. **WHEN EVERY ARTEFACT AGREES, ASK WHETHER THE DESIGN IS RIGHT.**
54. **A DIRECTIONAL CLAIM WITH NO NUMBER IS STILL A CLAIM.**
55. **"NOTHING READS IT" IS NOT "NOTHING MENTIONS IT."**
56. **A CONTENT TIER THAT PINS A SPELLING OWES AN EDIT WHEN THE SPELLING IS THE DEFECT.**
57. **AN EDIT THAT CHANGES LENGTH INVALIDATES OFFSETS COMPUTED BEFORE IT.**
58. **A CONTROL RUN ON THE PRE-EDIT FILE IS HOW YOU KNOW A FINDING IS YOURS.**
59. **A CONTROL THAT FIRES FOR THE WRONG REASON IS NOT A CONTROL.**
60. **A SHA THAT MATCHES DOES NOT MEAN THE CONTENT LANDED. The version block is the check.**
61. **A SUPERLATIVE IS A CROSS-LESSON CLAIM, AND IT IS ALWAYS CHECKABLE.**
62. **AN EXPLANATION CAN BE WRONG WITHOUT ANY NUMBER BEING WRONG.**
63. **A CITATION IS A CLAIM ABOUT AN EDITION, NOT ABOUT A NUMBER.**
64. **A FILE NAMED FOR A YEAR IS NOT EVIDENCE OF THAT YEAR — BUT VERIFY BEFORE CONVICTING.**
    **The fix is to put the primary source in the tree, not to distrust the extract.**
65. **CHECK THE LEAGUE BEFORE THE EDITION.**
66. **A REGIONAL VARIANT IS A DIFFERENT GAME, NOT A REPRINT — AND NOT A WITNESS.**
67. **A SCHEMA ERROR AND A CONTENT ERROR CAN ARRIVE IN THE SAME VALIDATOR MESSAGE, AND FIXING
    THE SCHEMA WILL HIDE THE CONTENT ONE.** When a mechanical fix silences a diagnostic, re-run
    it and ask whether any of the silenced messages were telling the truth.
68. **NEW, S148: A DISTRACTOR MUST BE WRONG FOR A REASON THE STUDENT CAN FIND IN THE BOOK.**
    Ten items across three banks offered a pre-correction byte figure and explained it with
    *"a figure from an earlier baseline."* **A student has never seen those numbers and has no
    access to the book's edit history.** `cite:`'s entire contract (QUIZ_SPEC §4) is to tell
    them where to re-read, and *"we changed it"* is not a place. **This is S146's finding
    recurring in the very session that quoted S146 — writing the rule down did not prevent
    committing it. The detector did.**
69. **NEW, S148: A DIFF YOU CANNOT READ IS NOT A REVIEWABLE EDIT.** Re-serialising the Maker's
    PAYLOADS object to change four payloads produced **2,726 changed lines and +58 KB**. The
    same change as targeted encoded-string splices produced **2**. When an edit's diff is
    orders of magnitude larger than the edit, the method is wrong even when the output is right.
70. **NEW, S148: PRICE EVERY CANDIDATE BEFORE RULING, AND PRICE IT BY DELETION.** L16 needed 84
    bytes. Six cuts were measured by actually removing them and compiling — 156, 1,828, 114,
    104, 60, 8 — and **the largest was the wrong answer**, because §7.4 hands the buzzer to the
    student and §7.1 depends on the A+B report. **A menu with numbers on it turns a preference
    into a ruling.**
