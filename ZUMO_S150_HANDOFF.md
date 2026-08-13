# ZUMO — S150 HANDOFF (rewritten at S149 close · paste at top of Session 150)

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
   **`svg_layout_audit.py` TAKES FILENAMES. A bare invocation prints usage and exits 1 —
   that is a usage error, not a finding (S148 nearly recorded it as one).**
6. `pip install cairosvg --break-system-packages` **and `pyyaml`. Needed every session.**
7. **NEVER run `build_css.py --help` or `session_versions.py --help`.** Read the docstring.
8. **Do not hand-type a version, and do not hand-type a COUNT.**
9. **`gate_payload_match.py` needs `newproject.html` FIRST, then the full lesson glob.**
10. **A CLONE IS NOT THE SITE.** Run `site_parity.py` after any push.
11. **VERIFY THE PUSH BY FRESH CLONE AND MD5 — AND DIFF THE STAGE AGAINST THE CLONE.**
12. **`css/semantic.css` AND `ZUMO_FAMILY_PINS.md` ARE HAND-AUTHORED PRESERVED LAYERS.**
13. **`rm -rf __pycache__` BEFORE `git status`. Also `find . -name pbuild -exec rm -rf {} +`**
    if the toolchain has been run — the harness leaves build dirs inside the project trees.

## 14. THE AVR TOOLCHAIN — S146's INSTRUCTIONS STILL HOLD. S148 RAN THEM AGAIN.

`apt-get install -y gcc-avr avr-libc` **(no `sudo` — it is not on this box, exit 127).** Clone
into `/home/claude/harness` **FLAT, not under a `pololu/` subdirectory**.

**READ THE EIGHT LIBRARIES OUT OF `LIBDIRS` IN THE SCRIPT. DO NOT CARRY THEM FROM A HANDOFF —
INCLUDING THIS ONE.** Also clone `arduino/ArduinoCore-avr`. Zumo library at tag **2.0.1**
(plain clone then `git checkout 2.0.1`; `--depth 1` cannot check out a tag). `cp pio_harness.sh`
into `$H`, then `bash pio_harness.sh --setup`. **Expect *objects: 41*.**

**THE CONTROL: L11 `after_step_1` MUST COMPILE TO 20,516.** Held in S144–S148, from five
clones. **The harness prints `flash=` on success and `OVER flash=` on an overflow — parse
both, or an over-ceiling build reads as a crash** (S148 lost a run to this).

---

# THE ONE THING TO CARRY OUT OF S149

**I CLASSIFIED TEN PAYLOADS BY COMPILED SIZE AND TWO OF THEM WERE DIFFERENT SOURCE.**

Ruling the catch-up split needed a measurement. I made it by compiling `after_step_1` for L07–L16
and comparing each figure to the previous lesson's `finished`. All ten matched, so I reported that
all ten `step_1` rows are coincidental — both conventions agree there because Step 1 is a copy.

**That is S27 verbatim, and DJ's "double check your work first" is the only reason it was caught.**
Re-run as md5 over the materialised files, **L13 and L14 differ.** Their `after_step_1` already
carries the lesson's own Step 1 work — L13's five new states plus `SILVER_RAW_MAX`,
`WALL_STOP_COUNT`, `ROW_STEP_CM`, `VICTIM_SHORT_CM` and the `StopReason` enum; L14's
`COMPETITION_MODE` and three self-test limits. **Both cost ZERO BYTES, because a `const` or an
`enum` that nothing references yet emits no code.** The lessons confirm it: L12 Step 1 is *Copy
Your Lesson 11 Project*, L13's is *The Numbers, the Names, the Reasons*, L14's is *One Switch,
Three Limits*.

**The corrected tally is 27 genuine identity against 28 offset — near even — not 35 against 28.**

**AND IT IS A STANDING LIMIT ON `byte_audit`, NOT A ONE-OFF:** a payload can ship an entirely wrong
configuration block and ARM 1 will never see it, because unreferenced declarations are free.
**The compiler is an instrument for what the program DOES, never for what the source SAYS.**

---

<!-- VERSION BLOCK: emitted by session_versions.py --handoff. Never hand-typed. -->
Fresh-clone verified at **`4f806ee`**. Census **40,642**.
Bible **v8.140** · `BookComponentStandard` **v01.13.0** · Maker **v2.49.4** ·
`marks/` **41** · `icons/` **49** incl. LICENSE.
`ZUMO_Syllabus_WORKING.md` **v1.2**.

Instruments: `book_gates` **v1.65.12** · `lesson_inventory` **v1.3.5** ·
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

Lessons: L01 v03.28.3 · L02 v03.21.3 · L03 v03.41.0 · L04 v04.29.0 · L05 v04.29.0 · L06 v04.32.1 · L07 v04.31.4 · L08 v04.31.1 · L09 v05.27.0 · L10 v02.29.2 · L11 v02.30.0 · L12 v01.31.3 · L13 v02.29.0 · L14 v02.34.0 · L15 v02.31.0 · L16 v02.23.0.

`quizzes/QUIZ_SPEC.md` **v1.2.0** · banks L02/L07/L08/L09/L10 **v1.0.1** ·
`ZUMO_TDP_Template_v3.md` **v3.1.1**.

**Derive the bank count, never read it out of a sentence:** `python3 quizzes/quiz_bank.py --status`

---

# WHAT S149 SHIPPED

## 1. `byte_audit.py` v1.1 — THE ONLY INSTRUMENT HERE THAT COMPILES

Rule 33 said no instrument reads prose and none compiles either. This closes the second half.
It cannot live in `book_gates.py` — no toolchain in a normal session — so run it whenever the
harness is up.

- **ARM 1 CEILING** — compiles **every** payload the Maker defines. No parsing, no mapping, no
  inference. **This is the arm that would have caught S148's unflashable L16.** 213 payloads,
  0 undeclared overflows.
- **ARM 2 FIGURES** — every step figure must equal a compiled payload of its lesson.
- **ARM 2b LEADS** — every figure in the compiled band, book-wide. A lead, never a verdict.
- **ARM 3 CONVENTION** — written, and **it can only see L15 and L16**, because no other lesson
  states per-step byte figures. Do not read its verdict as book-wide (rule 27).

**SEVEN CONTROLS, AND THREE OF MY OWN BUGS WERE CAUGHT BY THEM RATHER THAN BY KNOWING THE RULES:**

1. The overflow control's pad was **collected by `--gc-sections`** and reported PASS — a control
   that never fired (rule 59). Moved to PROGMEM and read at runtime; now 31,054.
2. The wrapper test asked whether the body contained `#include`. **L01's challenge comment boxes
   mention it** (rule 55). Changed to a directive test — which **L01 c01's own `<EEPROM.h>`
   tripped.** `mainCpp()` prepends its head **unconditionally**; the fix was to do what the Maker
   does. Control: **0 of 197 previously-passing sizes moved.**
3. The step parser knew only `Step 3 — Title`. **L11 and L12 write `📁 Step 2b: Title`** and were
   read as having no steps at all.

## 2. §16.22 — THE CATCH-UP SPLIT IS RULED LEGITIMATE

DJ ruled it. **L07–L10 OFFSET, L11–L16 IDENTITY, both correct.** L07–L10 are the lessons where the
*doing* is the content, so a finished step deletes the lesson; L11–L16 are integration lessons
where one step behind blocks the chain. Rule 32.

**A gate may assert this per range only, and must exclude the eight coincidental `step_1` rows** —
they satisfy either convention, so counting them certifies nothing. **That gate is not written.**

## 3. §16.23 — A DELIBERATELY UNBUILDABLE PAYLOAD DECLARES ITSELF

`L02 broken_code` and `L10 step_4_RED` are correct by design and were declared **in prose only**,
which no instrument reads. `data-nobuild` on the catch-up link now **names the reason**; a bare
boolean was rejected because a label is not the thing (rule 31). Control G is loud on a missing
attribute **and on an empty one**.

## 4. THE STALE BANK KEYINGS — AND THE METHOD THAT FOUND WHAT A GREP DID NOT

Six keyings across five banks named lesson versions that had moved. **`Authored against:` was left
exactly as written** — it records when the bank was read, and rewriting it asserts a read that
never happened (rule 37). A **`Verified against:`** line was added instead.

**The first method was a keyword grep and it returned zero, which is a weak way to prove a
negative** (rule 38). Redone by resolving each changed diff hunk to its enclosing section, with a
blinding control that fires on a seeded cite: **11 bank questions across L08/L09/L10 cite §5.4 —
the section L08 changed.** All eleven were read. None touches the changed comment. Conclusion
unchanged; evidence real.

---

# S149's OPEN FINDINGS

- **`byte_audit` CURRENTLY EXITS 1 ON EXACTLY ONE ROW, AND IT IS A REAL GAP.** L16 Step 5's first
  COMPILE CHECK promises **28,756** — the state after the Serial trade, before the Z–N trade. The
  number is right. **No Maker payload produces it**, so a student stuck at that intermediate has no
  catch-up and no instrument can ever verify the figure. Either author the payload or rule the
  figure exempt. **DJ to rule.**
- **§16.18 THROUGH §16.21 HAVE NO NUMBERED SECTION BODIES**, same as §16.14. Four rules now live
  only in changelog entries. §16.22 and §16.23 were seated properly to avoid making it six.
- **THE `IMAGE 7.9`–`7.12` QUEUE ITEM IS ALREADY FIXED** and should be struck: L07 v04.31.4 reads
  `Diagram (SVG)` / `✅ in the lesson` on all five rows.
- **ARM 2 REACHES TWO LESSONS.** L11–L14 quote byte figures in tables and prose, not in step
  headings, so they are covered only by ARM 2b's leads. Widening ARM 2 is real work.

---

# S150 QUEUE

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
