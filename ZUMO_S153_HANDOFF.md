# ZUMO — S153 HANDOFF (rewritten at S152 close · paste at top of Session 153)

## Session open ritual (do this without being asked)
1. **`git ls-remote https://github.com/Weymuth/zumo.git HEAD` FIRST.** A stale answer is
   timing, not caching — **retry a minute later before concluding a push failed** (§12.4).
   **AND THE SHA IS NOT THE CHECK. `session_versions --check` IS** (rule 60, S145).
2. Read `LIVE_ZUMO_TEXTBOOK.md` — verify date / status / versions.
3. **Do NOT grep the Bible version.** `session_versions.bible_consistency()` parses it.
4. Run the full suite and **READ THE EXIT CODE, NOT THE LAST LINE**. **THE SUITE IS 71 GATES,
   NOT 70.** Plus **`callout_id.py --selftest` then `--audit`**,
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

## 15. THE AVR TOOLCHAIN — S146's INSTRUCTIONS STILL HOLD. RUN AND VERIFIED IN S152.

`apt-get install -y gcc-avr avr-libc` **(no `sudo` — it is not on this box, exit 127).** Clone
into `/home/claude/harness` **FLAT, not under a `pololu/` subdirectory**.

**READ THE EIGHT LIBRARIES OUT OF `LIBDIRS` IN THE SCRIPT. DO NOT CARRY THEM FROM A HANDOFF —
INCLUDING THIS ONE.** Also clone `arduino/ArduinoCore-avr`. Zumo library at tag **2.0.1**
(plain clone then `git checkout 2.0.1`; `--depth 1` cannot check out a tag). `cp pio_harness.sh`
into `$H`, then `bash pio_harness.sh --setup`. **Expect *objects: 41*.**

**THE CONTROL: L11 `after_step_1` MUST COMPILE TO 20,516.** Held S144–S149, from five clones.
**The harness prints `flash=` on success and `OVER flash=` on an overflow — parse both.**

---

# THE ONE THING TO CARRY OUT OF S152

**A LABEL CAN AGREE WITH ITSELF AND BE WRONG ABOUT THE WORLD.**

Five L16 KINDS labels carried byte figures. All five were stale. `step_3` read
*"28,662 bytes — TEN to spare"* for a payload that is **152 OVER the ceiling**, in the step whose
entire subject is that it does not fit.

They survived because **each label's spare clause was arithmetically correct for its own stale
figure.** `28,672 − 28,662 = 10`. Nothing looked wrong because nothing internally *was* wrong.
Rule 51 in a new place: the label was certifying agreement with itself.

And nothing in the tree could see them. `gate_payload_match` asserts payload BYTES against lesson
`<pre>`. ARM 2 asserts the LESSON's figures. **No instrument read a label** — the one string the
student actually reads in the dropdown.

**`byte_audit` v1.2 ARM 4 now derives the expectation from the size table.** Reword a label and it
stays silent; move a figure or a clause and it is loud.

---

# S152's RULINGS

**AUTHOR THE PAYLOAD, DO NOT EXEMPT THE FIGURE.** DJ ruled after both options were priced. The
28,756 state was BUILT before the recommendation was made (rule 70) — twice, by independent
routes — and both landed on `+84 over`, the lesson's own wording. `step_5_serial_traded` ships
with a catch-up door seated between the failed first trade and the second, which is where a
stuck student actually is. **The missing payload was the defect the figure pointed at**: every
other step in L16 has a door and this one did not.

**DERIVE THE LABEL FIGURES.** DJ's word. ARM 4's predicate comes from the compile, never from a
typed number, so a sixth stale label cannot be authored the way the first five were.

**`data-midstep` DECLARES A NON-ENDPOINT DOOR.** Chosen after scoping: the population is TWO, and
**L10 Step 4 has carried two doors since it was written**, with the RED build declared by
`data-nobuild` on the link. The convention already existed and was merely ungeneralised, so the
new attribute matches its shape and `step_blocks()` learned ONE rule covering both. **L10 needed
no edit.**

---

# S153 QUEUE

## 0. THE GPT REVIEW — INCOMPLETE, AND THE MISSING PART IS THE VALUABLE PART
DJ ran a sixteen-lesson review in another model. **The paste carried only L15, L16 and an
overarching 26-item pass** — a select-all copies the rendered page, not the conversation, so
fourteen of sixteen replies were dropped while every one of DJ's own turns survived. A data
export was requested and **had not arrived at S152 close.**

**The overlap/deletion work DJ cared most about lives in the missing fourteen.** Overlap is a
cross-lesson claim (rule 34) and cannot be judged one lesson at a time.

**Triage rules established, apply them when it lands:**
- **STRIKE, already ruled:** the spiral audit (ruled, enumerated, 13 of 171, deliberately not
  started) · tie competition claims to a year (S148, rule 63) · the absolutes pass (§16.16,
  rule 61) · measured-facts discipline (§24.15) · "write a canon sheet first" (that is the Bible).
- **ONE RULING WEARING FOUR HATS:** the L15 theory notes (D-knows-the-future, P-always-weaves,
  I-never-belongs, I-is-the-only-term) are not four defects. They are one — **the book teaches
  conditional physics as absolutes** — and it is DJ's call, not a fix.
- **GPT CANNOT SEE A RULING (rule 39)** and will re-report settled items. Read its list against
  the Bible before reporting any of it (rule 72).
- **GPT'S OWN RULEBOOK CLAIMS CARRY NO EDITION** — TDP at 60% of rubrics, rubrics at 20% of the
  total, a required poster, video length deferred to league docs. **Rule 63, in the review that
  was auditing this book for unsourced numbers.** Settle them against
  `RCJRescueLine2026-final.pdf` in the root before any of them reaches a lesson.

## 1. TWO CONFIRMED CODE FINDINGS, DELIBERATELY NOT FIXED
Both verified against the tree at S152. Both move bytes, so both need the toolchain and a full
lesson arc — patching either alone compiles the chain twice.
- **L16's RUN IS NOT FROZEN WHEN IT ENDS.** `saveBaseline()` computes `millis() - runStart` at
  CALL time, and it is called from `RUN_REPORT` — after the run is over. Every second the student
  spends reading the report inflates the saved lap. **`showScore()` recomputes it the same way,
  so the displayed number is climbing while they read it.** GPT caught the save and missed the
  display.
- **L15's GAP-WINDUP DEMONSTRATION IS ARCHITECTURALLY IMPOSSIBLE.** `followLine()` is called only
  inside `if (isLineVisible())`, so `lineIntegral` cannot accumulate during a gap. Prose and code
  disagree **and the code is right.**

## 2. THE PHOTOGRAPHY — STILL THE ONLY THING BETWEEN THE BOOK AND SEPTEMBER
Stills **3.2 · 3.5 · 3.6 · 4.1 · 4.3 · 12.1 · 13.1 · 13.2**, videos **3.1 · 4.1 · 6.1 · 8.1**.
**VIDEO 3.1 carries L03's opening page.** Nothing in the tree can produce them.
*(`IMAGE 14.1` and `IMAGE 16.1` are also unshot; both lessons sit outside the September scope.)*

## 3. THE CATCH-UP CONVENTION — READ §16.22 BEFORE RE-RAISING
**§16.22 (v8.140) ruled the split LEGITIMATE** and ARM 3 measures rather than judges it. What is
open is only whether a gate should pin the measurement. **A gate pinning either convention would
certify 64 rows and fail 32.** Note ARM 3 reaches only TWO rows book-wide, because it needs a
stated byte figure and only L15 and L16 state them.

## 4. INVARIANTS WITH NO GATE
**NO GATE HOLDS A QUIZ BANK · A NAV PILL · A RULE CITATION.** The byte figure has `byte_audit`
v1.1+, and **the Maker label now has ARM 4** — that one is closed. **The quiz-bank gate is the
urgent one**: `quiz_bank --check` is loud but nothing calls it, so a broken bank can be pushed.

## 5. STILL OPEN, CARRIED
- **`GRAPHIC 16.1` OVERFLOWS ITS PANEL BY 31 UNITS** — recorded at S148, not fixed, pre-existing.
- **§4.2's AUDIT TABLE IS UNCONFIRMED AND MAY NOT BE CONFIRMABLE.** Left alone deliberately — the
  instrument, not the table, is what failed.
- **§16.14 AND §16.18–§16.21 HAVE NO NUMBERED SECTION BODIES.** §16.12 and §16.13 sit BELOW §17.
- **ARM 2 OF `byte_audit` REACHES TWO LESSONS.** L11–L14 quote figures in tables and prose.
- **L10's ARRIVAL GEOMETRY (S144, unruled)** — only the floor can settle it.
- **§8A.4's 65 cm/s IS UNVERIFIED** · **L14 §8A.2's "five orders of magnitude"** · **`AVOID_OUT_CM
  = 15.0` HAS NEVER TOUCHED A FLOOR** · **CHALLENGE 6's WEDGE NUMBERS ARE SIMULATED** · **L11
  §7A's 999.0 RULER TRICK.**
- **L14's GLOSSARY says "95% ten times" where §3.1 teaches 90%** — deliberate, named in the bank.
- **THE RESOURCE SECTION AS A BOOK PAGE — PARKED UNTIL AFTER SEPTEMBER 8.**
- **L14 §10 IS THE ONLY §10 THAT IS NOT AN EXIT TICKET.** Unruled.
- **`shim.cpp` IS REFERENCED BY `pio_harness.sh` AND EXISTS NOWHERE IN THE REPO.** The `[ -f ]`
  guard makes it optional and *objects: 41* is unaffected. Recorded so nobody hunts for it.

## Carried from S141/S140, still unruled
**THE BAUD BENCH TEST** · **THE 1200-BAUD RESET HAS NO HOME** · **`IMAGE 7.9`–`7.12` INDEXED AS
*Photo / screenshot*** · **§3.2's *about 13½ milliseconds*** · **L05 §3.6 alkaline tension** ·
**the `static` split glossaries still disagree.**

## Carried from S137/S138/S139, still unruled
**§4.2's stall-current multiple** · **`IMAGE 4.1` IS A PHANTOM IN THE FIGURE COUNT** · **CONSTANTS
vs CONFIGURATION DRIFT** · **THE 3Pi+ NOTE COMES OUT OF L03** · **L03 C1's hint hands over the
numbers its own blanks ask for** · **§3.3's header-contents bullet in L07 still lists *Include
guards*** · **§7's BANNER is three spellings** · **whether the `after` quiz set is graded at all.**

## Carried from S135/S133/S134, still open
**THE SPIRAL ARC — RULED, ENUMERATED, DELIBERATELY NOT STARTED.** 13 of 171 units. · **THE FIGURE
BLOCK HAS FOUR SPELLINGS** · **`svg_layout_audit.py` HAS FOUR MEASURED DEFECTS, NONE FIXED** · KEY
TERM paint is five grounds across 238 blocks · L03 `3.44` carries `id="glossary-trim"` on a BODY
block · `BookComponentStandard` §7.4 says 184 where the measured figure is 238 · §6.5's nav-pill
rule says 12–14 where the live range is 10 to 19 · **THE AMBER LEAK: L02 §2.7 is the last of three.**

## AFTER SEPTEMBER 8 — PARKED ON PURPOSE, DO NOT START EARLY
**THE RESOURCE SECTION PAGE** · **REDO `GRAPHIC 4.7` IN THE BLUEPRINT COMPOSITION** (chips run
**5 4 3 2 1** left to right — do not re-derive) · Challenge card Pass B · monetization/ebook ·
DISCOVERIES tagging · TDP template v3 A5 Lab Log.

## Learner mode & book content
L03_C05 Variable Speed · L03 C01/C05/C06 reference a `finished` payload that does not exist for
L03 · whole-template starters L08/L09/L10 · Maker batch · L01 VS Code multi-root step.

## Bench (need the robot — parked with photography)
Q017 L09 six numbers · Q044 calibration-spin · Q046 gyro-bias · L02 §5 green-LED · Constrain
RUN_MS · **cm/s at a stated BASE_SPEED** · the floor rig for 3.2 / 3.5 / VIDEO 3.1 · a real TRIM
run for `IMAGE 3.6` · **run 7E on a lab tile** · **L04's wave test and Act Two row-1 overflow** ·
**L05 Experiment 3 at 45°** · **L06 Experiment 3 both drags** · **the baud test** · **commanded
30 cm vs measured across a few robots** · **DRIVE THE SEVEN-PHASE BOX** · **drive Challenge 6's
wedge** · **HOLD THE ROBOT OVER A TABLE EDGE AND READ THE FIVE CALIBRATED VALUES** · **L11's §7
ladder** · **L12's §7 ladder** · **L13's ENTIRE §7 LADDER** · **L14's §7 ladder** · **L15's WHOLE
§7 LADDER** · **L16's §7.1 baseline.**
**Every §7 measurement in L13, L14, L15 and L16 is named in those banks as deliberately unasked.**

---

<!-- VERSION BLOCK: emitted by session_versions.py --handoff. Never hand-typed. -->
Fresh-clone verified at **`f3a5ce4`**. Census **40,648**.
Bible **v8.143** · `BookComponentStandard` **v01.13.0** · Maker **v2.50** ·
`marks/` **41** · `icons/` **49** incl. LICENSE.
`ZUMO_Syllabus_WORKING.md` **v1.2**.

Instruments: `book_gates` **v1.66.2** · `lesson_inventory` **v1.3.5** ·
`gen_component` **v1.6.1** · `pill_sweep` **v1.1** · `gate_payload_match` **v1.8.0** ·
`build_family_map` **v1.6.4** · `callout_id` **v1.0** · `keyterm_prefix` **v1.0.1** · `build_mark_index` **v1.1.0** · `gen_bonus_banner` **v1.4.1** ·
`gen_part_banners` **v1.2** · `session_versions` **v1.25.0** · `fit_raster_svg` **v1.2** ·
`flatten_alpha` **v1.2** · `svg_layout_audit` **v1.20** · `site_parity` **v1.1** ·
`build_css` **v1.3.0** ·
`image_audit` **v1.2** ·
`strip_inline` **v1.2** ·
`build_worklist` **v1.1** ·
`regex_audit` **v1.0** ·
`byte_audit` **v1.2** ·
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

Lessons: L01 v03.28.3 · L02 v03.21.3 · L03 v03.41.1 · L04 v04.29.1 · L05 v04.29.0 · L06 v04.32.1 · L07 v04.31.4 · L08 v04.31.1 · L09 v05.27.0 · L10 v02.29.2 · L11 v02.30.0 · L12 v01.31.3 · L13 v02.29.0 · L14 v02.34.0 · L15 v02.31.1 · L16 v02.24.0.

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
71. **NEW, S151: A CONTROL THAT NAMES A FILE IT NEVER TOUCHED IS REPORTING CONTAMINATION, NOT
    A FINDING.** Six controls printed FAIL at 70 of 71 green — the exact shape of a clean run —
    because the snapshot predated the edit and the first restore reverted the session's own
    work. **Read the failure DETAIL, not the verdict.** Rule 21's tell.
72. **S151: A QUEUE IS NOT CANON.** An item that survives the session that rules it will be
    re-reported as open by the next reader. **Check the queue against the Bible before
    reporting it.** S151 opened by telling DJ that L15's title split was the largest un-ruled
    item in the book; v8.141 had ruled it the session before.
73. **NEW, S152: A LABEL CAN AGREE WITH ITSELF AND BE WRONG ABOUT THE WORLD.** Five L16 KINDS
    labels carried stale byte figures whose spare clauses were arithmetically correct FOR THE
    STALE FIGURE. `28,672 - 28,662 = 10`, so *"TEN to spare"* read fine for a payload 152 OVER.
    **Internal consistency is not correctness (rule 51).** Check a derived number against the
    thing it is derived FROM, never against its own neighbours.
74. **NEW, S152: THE STRING THE USER READS IS AN ARTEFACT, AND IT NEEDS A GATE LIKE ANY OTHER.**
    `gate_payload_match` guarded payload bytes; ARM 2 guarded lesson figures. The Maker's dropdown
    label — the one string a stuck student actually reads — was guarded by nothing, and every
    instance of it was wrong. **Ask what the reader sees, not only what the tree contains.**
75. **NEW, S152: A SELECT-ALL COPIES THE PAGE, NOT THE CONVERSATION.** Fourteen of sixteen
    replies were dropped from a pasted review while every one of the user's own turns survived.
    **The tell was positional, not length-based.** When a paste's structure is lopsided, count
    what should be there before working from it.
76. **NEW, S152: SCOPE A DEFECT BEFORE BUILDING A CONVENTION FOR IT.** The mid-step door looked
    like a population of one. It is two, and **L10 had already solved it** with `data-nobuild` on
    the link. Scoping turned a new convention into a one-line generalisation of an existing one,
    and saved an edit to a lesson that did not need one.

