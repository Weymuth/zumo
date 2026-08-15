# ZUMO — S156 HANDOFF (rewritten at S155 close · paste at top of Session 156)

## Session open ritual (do this without being asked)
1. **`git ls-remote https://github.com/Weymuth/zumo.git HEAD` FIRST.** A stale answer is
   timing, not caching — **retry a minute later before concluding a push failed** (§12.4).
   **AND THE SHA IS NOT THE CHECK. `session_versions --check` IS** (rule 60, S145).
2. Read `LIVE_ZUMO_TEXTBOOK.md` — verify date / status / versions.
3. **Do NOT grep the Bible version.** `session_versions.bible_consistency()` parses it.
   The phrase `Bible version: v` occurs THREE times and two of them are grep COMMANDS quoted
   inside the Bible; a naive `grep -o` returns `v8.145.1`, `v`, `v`.
4. Run the full suite and **READ THE EXIT CODE, NOT THE LAST LINE**. **THE SUITE IS 73 GATES,
   NOT 72** (gate 73 new, S154). Plus **`callout_id.py --selftest` then `--audit`**,
   **`keyterm_prefix.py --audit`**, **`quizzes/quiz_bank.py --selftest` then `--check`**, and
   **`session_versions.py --selftest`** — **its CONTROL C is the unfinished-documentation-pass
   signal and nothing else in the tree can see one.**
5. **`--anomalies` BELONGS TO `lesson_inventory`, NOT `session_versions`.**
   **`svg_layout_audit.py` TAKES FILENAMES. A bare invocation prints usage and exits 1 —
   that is a usage error, not a finding.** **`pill_sweep.py` and `class_sweep.py` also take
   arguments; a bare run is a usage error, not a finding either.**
6. `pip install cairosvg --break-system-packages` **and `pyyaml`. Needed every session.**
7. **NEVER run `build_css.py --help` or `session_versions.py --help`.** Read the docstring.
8. **`book_gates.py` TAKES NO ARGUMENTS.**
9. **Do not hand-type a version, and do not hand-type a COUNT.**
10. **`gate_payload_match.py` needs `newproject.html` FIRST, then the full lesson glob.**
11. **A CLONE IS NOT THE SITE.** Run `site_parity.py` after any push.
12. **VERIFY THE PUSH BY FRESH CLONE AND MD5 — AND DIFF THE STAGE AGAINST THE CLONE.**
13. **`css/semantic.css` AND `ZUMO_FAMILY_PINS.md` ARE HAND-AUTHORED PRESERVED LAYERS.**
14. **`rm -rf __pycache__` BEFORE `git status`. Also `quizzes/__pycache__`.**
15. **THE FULL SUITE TAKES ~40 SECONDS.** Budget control harnesses accordingly.

## 16. THE AVR TOOLCHAIN — S146's INSTRUCTIONS STILL HOLD. NOT RUN IN S153, S154 OR S155.

`apt-get install -y gcc-avr avr-libc` **(no `sudo` — it is not on this box, exit 127).** Clone
into `/home/claude/harness` **FLAT, not under a `pololu/` subdirectory**.

**READ THE EIGHT LIBRARIES OUT OF `LIBDIRS` IN THE SCRIPT. DO NOT CARRY THEM FROM A HANDOFF —
INCLUDING THIS ONE.** Also clone `arduino/ArduinoCore-avr`. Zumo library at tag **2.0.1**
(plain clone then `git checkout 2.0.1`). `cp pio_harness.sh` into `$H`, then
`bash pio_harness.sh --setup`. **Expect *objects: 41*.**

**THE CONTROL: L11 `after_step_1` MUST COMPILE TO 20,516.** Held S144–S149, from five clones.

---

# THE ONE THING TO CARRY OUT OF S155

**A TRIPLE CHECK THAT VARIES THE MECHANISM AND NOT THE PREDICATE IS A SINGLE CHECK RUN THREE
TIMES.**

§16.25 was written at S154 to stop the fleet-hardware question recurring, and it priced the fix at
*13 / 8 / 1 / ~1* A-Star occurrences. **All four were `grep -c` output, which counts matching
LINES.** Rule 50 committed inside the section that cites it.

**THE RE-DERIVATION THEN WENT WRONG A SECOND TIME, AND THAT IS THE PART TO KEEP.** Asked for a
triple check, the correction ran three genuinely independent mechanisms — `grep -o | wc -l`,
`re.finditer` over raw bytes, and `len(re.split()) - 1`. **All three agreed at 15 / 16 / 54. All
three were wrong**, because the widened pattern `a[-_ ]?star` matches the phrase *"a start line"*,
36 times in `newproject.html` alone. The agreement was real and meant nothing: the three shared
the predicate, and the predicate was the defect.

**§24.13's *re-derive, do not re-read* is satisfied only when the PREDICATE varies.** What settled
it was reading the hits — at which point the count stopped being the useful output and the
INVENTORY became it: six of L01's fifteen are the CORRECT build target, two are element ids, and
two of L03's ten are a photograph's filename. **A fix pass scoped by the total would have edited
things that are right.**

---

# THE ONE THING TO CARRY OUT OF S154

**AGREEMENT BETWEEN TWO INSTRUMENTS OF THE SAME KIND IS NOT CORROBORATION. IT IS ONE
INSTRUMENT REPORTING TWICE.**

An external model reviewed all sixteen lessons and produced **245 findings**. Reading them
back, roughly **200 drew agreement**. That ratio looked like a strong review and it is not
evidence of one: **the reviewer and the reader are the same kind of tool, reading the same
HTML, with no robot and no compiler between them.** Rule 79 was written about two gates sharing
a scope pin; it applies unchanged to two models sharing an architecture.

**WHAT MADE THE REVIEW USABLE WAS A CALIBRATION PASS, NOT THE AGREEMENT.** Seven findings
decidable from the repo alone were measured before anything was ruled: **six confirmed, one
refuted.** The refutation is worth more than the six. A claim that L02 §7's *"about 85–95 lines"*
was wrong against a payload *"closer to ~119 lines"* — measured, the payload is **95 total / 86
non-blank / 75 code**, and **the lesson was right.** A confident, specific, plausible number that
is simply wrong is §24.16's shape again, and it is what the remaining 238 unmeasured rows should
be assumed to contain.

**THE OPERATIONAL RULE: `AGREE` IN THE WORKLIST MEANS *the claim is coherent*, NOT *measured*.**
Every row still owes its own check before it becomes an edit.

---

# S155's RULINGS

**TRIPLE CHECK, THEN CORRECT, THEN REISSUE THE HANDOFF.** DJ's word on being shown the count
error. The triple check is what caught the second, worse error.

---

# S154's RULINGS

**THE FLEET IS ZUMO 32U4 WITH OLED (§16.25, v8.145).** Ruled so it stops recurring. And the
ruling settled the question **against DJ's own rebuttal**: the citation offered was to the *Zumo
Robot for Arduino*, a shield on a separately bought A-Star — a different product. The reviewer
then folded to that rebuttal without testing it. **Both parties were wrong in one exchange.**

**CONTINUE INTAKE, FIX L01/L03 IN ONE PASS AT THE END.** DJ's call after being shown that L01
would attract more findings and that opening it now guarantees opening it three times.

**BUILD THE INDEX-COMPLETENESS GATE NOW**, and DJ ruled it jumps the queue as an instrument
failure rather than content. It was built, and it turned out **not** to be an instrument failure
— see gate 73 below.

**"I WANT IT TO BE CORRECT"** — on the A-Star KEY TERM. The binary offered (rename vs. keep) was
the wrong question; correctness needs **three** terms, not a swap.

---

# S156 QUEUE

## 0. THE GPT REVIEW IS INTAKEN. NOTHING IS RULED. NOTHING IS FIXED.
**`ZUMO_GPT_REVIEW_WORKLIST.md` v1.1 is the artefact** — 18 documents, 68,123 words, **245
findings indexed**, 7 measured, 0 fixed. **IT IS STILL NOT IN THE REPO.** S155 confirmed this by
inspection: `GPT_WORKLIST.md` in the root is the unrelated S103 graphics list. The file exists
only as a working deliverable and was re-delivered at S155. **Ask for it; do not assume it is on
disk, and do not mistake `GPT_WORKLIST.md` for it.**

**THE FIRST DECISION IS THE SIX CANON STATEMENTS, NOT THE 245 ROWS.** Each collapses 15–40
findings, and fixing them lesson-by-lesson means fixing L08 three times:
- **C1 — TRIM: *"open loop needs TRIM, closed loop must not get it."*** Too absolute; feed-forward
  and feedback coexist. L06, L08, L10, L11, L12, L15. The narrow pedagogical rule is true and
  teachable; the universal one has to be untaught in L15.
- **C2 — SENSOR-AS-TRUTH LANGUAGE.** *"Encoders tell the truth" · "the gyro reports the truth" ·
  "proximity 3 = 3 cm" · "green reads 300–700" · "black absorbs IR."* L04–L13. **The strongest
  item in the review**, and it gives the book a spine it nearly has already.
- **C3 — BLOCKING AND THE KILL SWITCH.** L10 claims B is live *"in every state, at every
  moment"*; `driveDistance()`, `turnDegrees()` and `delay(600)` all block. **This is a safety
  claim, not a style claim.**
- **C4 — UNMEASURED PRECISION.** Covered by §24.15 — **STRUCK as a new item**, instances still
  need disposition.
- **C5 — ABSOLUTES.** Covered by §16.16 / rule 61 — **STRUCK as new**, instances still live.
- **C6 — COMPETITION RULE vs ROBOLORE POLICY**, unlabelled across L13–L16.

**FIVE OF THE REVIEW'S 26 CROSS-CUTTING ITEMS ARE ALREADY RULED** and were struck on intake:
the spiral audit · year-tied competition claims (rule 63) · the absolutes pass (§16.16) ·
measured-facts discipline (§24.15) · *"write a canon sheet first"* (that is the Bible). **Rule 39
and rule 72, working as designed.**

**THE LARGEST SINGLE CODE FINDING, NOT PREVIOUSLY IN ANY QUEUE — REVERSE TRIM.**
`driveDistance()` does `setSpeeds(speed + TRIM, speed)` where `speed` flips sign for reverse, so
a correction that strengthens the weak motor forward **weakens it backward.** Verified in the
live tree: L06's `driveDistance`, its finished build, and `driveDistanceSmooth`. Propagates to
L07 (Challenge 1 `driveBackward()`, C4, C7) and L13 Challenge 1's `driveDistance(-10.0)`.
**Moves bytes — needs the toolchain and a full lesson arc.**

**BOTH S154-QUEUE CODE FINDINGS WERE INDEPENDENTLY CONFIRMED** by the review, working only from
the HTML: L16's `saveBaseline()` inflating the lap, and L15's architecturally impossible
gap-windup. Two instruments, same defect.

**READ PART 4 BEFORE ACTING ON ANY CUT LIST.** `Lesson_02_GPT_Feedback.docx` ends with a ~30-item
challenge cut table written **before** the reviewer knew about the Saxon spiral; in the L04
document it learns the design and **reverses several of its own verdicts** (L01 C11, L02 Warm-Up
4, L03 C1, L04 Line Light all move from *cut* to *keep*). **Anyone working from the L02 file
alone will cut challenges the reviewer later argued to protect.**

**THE CHEAPEST NEXT MOVE NEEDS NO RULING: the rulebook verification pass.** Eight findings across
L14 and L16 are rulebook claims, and `RCJRescueLine2026-final.pdf` is in the repo root. One read
settles all eight. **The reviewer's rulebook claims carry no edition (rule 63) and must not reach
a lesson unchecked.**

## 1. THE A-STAR FIX — RULED, RE-MEASURED AT S155, NOT STARTED
§16.25 is canon (Bible **v8.145.1**). **The S154 figures were LINE counts from `grep -c` and are
corrected: 15 `Lesson_01.html` · 10 `Lesson_03.html` · 2 `newproject.html` · 2 pre-existing in
the Bible · ZERO quiz banks.** Three terms: `Zumo 32U4 Main Board` (hardware, inherits the
*brain* framing) · `ATmega32U4` (chip) · `a-star32U4` (build target only). **`board = a-star32u4`
is CORRECT and must survive the sweep.**

**USE THE INVENTORY, NOT THE TOTAL.** L01's 15 = **5 wrong-claim** (§3.3 *built around*, the KEY
TERM and its glossary twin both reading *the brain of your Zumo robot*, the Brain Check answer,
and the §3.3 checklist line) · **6 legitimate build-target** · **2 element ids** (`term-a-star`,
`term-a-star-gloss`) · **2 checklist/quiz**. L03's 10 = **8 wrong-claim** (four prose sentences
attributing motor control to the A-Star, the IMAGE 3.14 caption, the Figures-index row, the
battery-monitoring sentence, and the TDP header block) · **2 asset filename**.
`newproject.html`'s 2 are both correct build-target.

**TWO OPEN QUESTIONS THE COUNT WOULD HAVE HIDDEN — BOTH NEED A DJ RULING BEFORE THE PASS.**
- **THE CAPITALIZATION IS SPLIT AND THE BIBLE IS ON THE OTHER SIDE OF IT.** Lessons and Maker
  ship `a-star32u4` with a **LOWERCASE u** in six places; this Bible writes `a-star32U4` twelve
  times including §16.8's `boards/a-star32U4.json`, `pio_harness.sh` agrees with the Bible, and
  §16.25 declares uppercase canonical. **The book contradicts its own canon in six places.**
  PlatformIO evidently tolerates lowercase — the book has shipped that way — so **normalising is
  a RULING, not a defect fix.**
- **L03's PHOTOGRAPH IS NAMED FOR A BOARD THE ROBOT DOES NOT CONTAIN:**
  `L03_IMAGE_3-14_astar_board.jpg`, a top view of the Zumo 32U4 main board. Renaming is disk work
  plus `image_audit`. The pass may correct the caption and keep the filename — but **decide it,
  do not miss it.**

**AND §11 CARRIES ONE OF THE WRONG CLAIMS ITSELF:** *"A-Star32U4 capitalization for the
microcontroller"*, where the microcontroller is the ATmega32U4. §16.25 contradicts a line in its
own file.

Do this in the single L01 pass with the rest of L01's findings, not alone.

## 2. THE PHOTOGRAPHY — STILL THE ONLY THING BETWEEN THE BOOK AND SEPTEMBER
Stills **3.2 · 3.5 · 3.6 · 4.1 · 4.3 · 12.1 · 13.1 · 13.2**, videos **3.1 · 4.1 · 6.1 · 8.1**.
**VIDEO 3.1 carries L03's opening page.** Nothing in the tree can produce them.
*(`IMAGE 14.1`, `IMAGE 16.1` and `GRAPHIC 15.4` are also unshot; all three sit outside the
September scope.)* **September 8 is the launch date. This is the critical path and nothing else is.**

## 3. INVARIANTS WITH NO GATE — ONE MORE CLOSED
**The figure index is CLOSED (gate 73, S154).** The quiz bank closed at S152/S153; the Maker
label at S152. **Still open: A NAV PILL · A RULE CITATION.** Neither is urgent. Do not open one
without a ruling.

**AND GATE 73 CARRIES A STATED BLIND SPOT — DO NOT READ ITS SILENCE AS PROOF.** It compares tags
PRINTED against tags INDEXED. A figure landed with **no caption tag and no index row** is
invisible to it, because nothing in the tree says that figure was meant to exist. **Nine lessons
print fewer than half their indexed figures**, so for those it is much weaker than it looks.

## 4. STILL OPEN, CARRIED
- **24 STALE `source:` PINS ACROSS 13 OF 16 QUIZ BANKS.** S154 re-derived this by parsing the
  YAML: the S154 handoff carried *three pins across two banks* and the real figure is **24 across
  13**. **Do NOT rewrite them** — the pin records what was actually read, and updating it without
  the read destroys the only signal it carries (rules 37 and 51). **Recommended when there is
  time: a `--pins` REPORT arm on `quiz_bank` that derives the stale list every run and exits 0.**
  A gate would fail 13 of 16 banks and needs a ruling first.
- **`GRAPHIC 16.1` OVERFLOWS ITS PANEL BY 31 UNITS** — recorded S148, pre-existing.
- **§4.2's AUDIT TABLE IS UNCONFIRMED AND MAY NOT BE CONFIRMABLE.** The review raised it again
  (Git required for PlatformIO on Mac); DJ asserted it is required, the reviewer folded without
  testing. **Still unsettled, still needs a Mac.**
- **§16.14, §16.18–§16.21 AND §24.11–§24.16 HAVE NO NUMBERED SECTION BODIES.** §16.12 and §16.13
  sit BELOW §17. **S154 seated §16.25 correctly rather than adding a sixth to the pile** — the
  disposition v8.144 flagged and did not take. The six are still owed.
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
Fresh-clone verified at **`208cc94`**. Census **40,668**.
Bible **v8.145.1** · `BookComponentStandard` **v01.13.0** · Maker **v2.50** ·
`marks/` **41** · `icons/` **49** incl. LICENSE.
`ZUMO_Syllabus_WORKING.md` **v1.2**.

Instruments: `book_gates` **v1.68.1** · `lesson_inventory` **v1.3.5** ·
`gen_component` **v1.6.1** · `pill_sweep` **v1.1** · `gate_payload_match` **v1.8.0** ·
`build_family_map` **v1.6.4** · `callout_id` **v1.0** · `keyterm_prefix` **v1.0.1** · `build_mark_index` **v1.1.0** · `gen_bonus_banner` **v1.4.1** ·
`gen_part_banners` **v1.2** · `session_versions` **v1.26.0** · `fit_raster_svg` **v1.2** ·
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
`quiz_bank` **v1.0.1** ·
`timer.html` **v1.3.2** ·
`going_deeper` **v01.6.1**.

Lessons: L01 v03.28.4 · L02 v03.21.3 · L03 v03.41.1 · L04 v04.29.1 · L05 v04.29.0 · L06 v04.32.1 · L07 v04.31.4 · L08 v04.31.1 · L09 v05.27.0 · L10 v02.29.2 · L11 v02.30.0 · L12 v01.31.3 · L13 v02.29.0 · L14 v02.34.0 · L15 v02.31.2 · L16 v02.24.0.

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
20. **A HOLD THAT IS ALSO SATISFIED BY AN ACCIDENT IS NOT A HOLD.** **S154: L15's unshot
    `GRAPHIC 15.4` was the obvious exemption for gate 73, and L03's and L12's equally unshot
    figures ARE indexed — the exemption would have certified the defect's second instance.**
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
33. **NO INSTRUMENT READS PROSE — AND NONE COMPILES EITHER.**
34. **A NUMBER IS ONLY CHECKABLE AGAINST THE OTHER FIFTEEN LESSONS.**
35. **COMPILE THE SNIPPET; LET THE BOOK'S OWN CODE TESTIFY.**
36. **A FACT THAT LIVES ONLY IN AN SVG IS NOT IN THE BOOK** — and a WRONG one is still wrong.
37. **READ -> FIX -> QUIZ, NEVER QUIZ FIRST — AND THE READ DOES NOT TRANSFER BETWEEN SESSIONS.**
38. **A TEXT MATCH LOCATES; IT NEVER ANSWERS.** **S154: committed AGAIN, on the stale-pin count —
    a regex reading `lesson_NN: vX` returned TWO because the pins are double-QUOTED, where a YAML
    parse returned TWENTY-FOUR. S155: committed a THIRD time, on §16.25's own scope figures, which
    were `grep -c` LINE counts reported as occurrences. THE HITS MUST BE READ: L03's photograph
    filename and L01's two element ids are hits that are not defects, and six of L01's fifteen are
    the CORRECT build target.**
39. **NO INSTRUMENT THAT READS THE TREE CAN SEE A RULING.**
40. **PULL THE PAYLOAD, NOT THE CARD.**
41. **AN ENTRY FILED IN ONE HOME IS NOT FILED.**
42. **A SPEC'S OWN NUMBERS CAN BE ARITHMETICALLY IMPOSSIBLE.**
43. **WHEN TWO SECTIONS DISAGREE, READ THE CITATIONS — AND WHEN THE CITATIONS DISAGREE, READ
    THE RULEBOOK'S CHANGELOG. If you do not HAVE the rulebook, say so and stop.**
44. **THE HEADER OF A THING IS NOT THE THING.** **S154: gate 69 is titled *the planned figure
    population is whole* and its predicate is the DENOMINATOR alone. The title read broader than
    the code for the life of the book, which is why gate 73's invariant went unheld.**
45. **A SNAPSHOT YOU HAVE RUN TOOLS IN HIDES ITS OWN DEBRIS.**
46. **A CALLOUT IS NEVER A FREE EDIT.**
47. **A STEP PAYLOAD IS THE FILE AS IT STANDS AT THAT STEP.**
48. **A VERIFIER THAT READS YOUR INTENT INSTEAD OF THE ARTEFACT VALIDATES NOTHING.**
49. **A NUMBER THAT A SENTENCE DERIVES FROM CANNOT BE SWAPPED WITHOUT REWRITING THE SENTENCE.**
50. **A COUNT INSIDE A SENTENCE IS A CLAIM. DERIVE IT OR DELETE IT.**
51. **A GATE THAT CERTIFIES AGREEMENT IS NOT CERTIFYING CORRECTNESS.**
52. **WHEN THE ART AND THE CODE DISAGREE, ASK WHICH ONE IS THE DESIGN.**
53. **WHEN EVERY ARTEFACT AGREES, ASK WHETHER THE DESIGN IS RIGHT.**
54. **A DIRECTIONAL CLAIM WITH NO NUMBER IS STILL A CLAIM.**
55. **"NOTHING READS IT" IS NOT "NOTHING MENTIONS IT."**
56. **A CONTENT TIER THAT PINS A SPELLING OWES AN EDIT WHEN THE SPELLING IS THE DEFECT.**
57. **AN EDIT THAT CHANGES LENGTH INVALIDATES OFFSETS COMPUTED BEFORE IT.**
58. **A CONTROL RUN ON THE PRE-EDIT FILE IS HOW YOU KNOW A FINDING IS YOURS.**
59. **A CONTROL THAT FIRES FOR THE WRONG REASON IS NOT A CONTROL.** **S154: the §27.11 blinding
    control did not fire because it deleted a declaration from the HAND-AUTHORED semantic layer,
    which sits outside the GENERATED block the gate hashes. The control was wrong, not the gate —
    read the failure DETAIL, not the verdict.**
60. **A SHA THAT MATCHES DOES NOT MEAN THE CONTENT LANDED. The version block is the check.**
61. **A SUPERLATIVE IS A CROSS-LESSON CLAIM, AND IT IS ALWAYS CHECKABLE.**
62. **AN EXPLANATION CAN BE WRONG WITHOUT ANY NUMBER BEING WRONG.**
63. **A CITATION IS A CLAIM ABOUT AN EDITION, NOT ABOUT A NUMBER.**
64. **A FILE NAMED FOR A YEAR IS NOT EVIDENCE OF THAT YEAR — BUT VERIFY BEFORE CONVICTING.**
65. **CHECK THE LEAGUE BEFORE THE EDITION.**
66. **A REGIONAL VARIANT IS A DIFFERENT GAME, NOT A REPRINT — AND NOT A WITNESS.**
67. **A SCHEMA ERROR AND A CONTENT ERROR CAN ARRIVE IN THE SAME VALIDATOR MESSAGE.**
68. **A DISTRACTOR MUST BE WRONG FOR A REASON THE STUDENT CAN FIND IN THE BOOK.**
69. **A DIFF YOU CANNOT READ IS NOT A REVIEWABLE EDIT.**
70. **PRICE EVERY CANDIDATE BEFORE RULING, AND PRICE IT BY DELETION.**
71. **A CONTROL THAT NAMES A FILE IT NEVER TOUCHED IS REPORTING CONTAMINATION, NOT A FINDING.**
72. **A QUEUE IS NOT CANON.** Check the queue against the Bible before reporting it.
73. **A LABEL CAN AGREE WITH ITSELF AND BE WRONG ABOUT THE WORLD.**
74. **THE STRING THE USER READS IS AN ARTEFACT, AND IT NEEDS A GATE LIKE ANY OTHER.**
75. **A SELECT-ALL COPIES THE PAGE, NOT THE CONVERSATION.** **S154's addition: a piecemeal paste
    loses the FRONT of a reply, not the tail — an L02 review arrived looking complete and was
    missing nineteen findings above the fold. THE DATA EXPORT, OR PER-LESSON DOCUMENTS.**
76. **SCOPE A DEFECT BEFORE BUILDING A CONVENTION FOR IT.**
77. **A CHECKSUM YOU DID NOT COMPUTE IS WORSE THAN NO CHECKSUM.**
78. **A SCAN THAT FOUND NOTHING IS NOT A SCAN THAT FOUND NOTHING WRONG.** **S154: gate 73 states
    its own blind spot in its comment, because nine lessons print fewer than half their indexed
    figures and its silence on those is not evidence.**
79. **TWO MECHANISMS PINNED TO THE SAME SCOPE ARE ONE MECHANISM.** **S154 extends it beyond
    instruments: two MODELS of the same kind, reading the same artefact with no robot and no
    compiler, are one reviewer. Agreement between them is not corroboration.**
80. **A SECOND HOME IS ONLY WORTH WATCHING IF SOMETHING READS IT THAT CANNOT READ THE FIRST.**
81. **NEW, S154: A FOLD IS NOT A CONCESSION.** Twice in one exchange a correct claim was
    abandoned because the other party sounded certain — the reviewer folding to DJ on §3.3 and on
    §4.2 Git, and DJ's own later ruling settling §3.3 against the rebuttal he had made. **An
    agreement reached by one side folding is the weakest evidence in the room, not the strongest.**
    When a correction is withdrawn without being tested, the question is still open.
82. **NEW, S154: AN AGREEMENT RATE IS A PROPERTY OF THE INSTRUMENTS, NOT OF THE CLAIM.** 200 of
    245 findings drew agreement and the calibration pass still refuted one of the first seven
    measured. **Measure a sample you can decide before weighting the ones you cannot.**
83. **NEW, S155: THREE METHODS THAT SHARE A PREDICATE ARE ONE METHOD.** §24.13 says re-derive
    rather than re-read, and a triple check ran `grep -o | wc -l`, `re.finditer` over raw bytes,
    and `len(re.split()) - 1` over the same widened pattern. **All three agreed and all three were
    wrong**, because the pattern `a[-_ ]?star` matches the phrase *"a start line"* — 36 times in
    one file. **Vary the PREDICATE, not merely the mechanism**, and read the hits before reporting
    the count. Rule 79 applied to a regex instead of to a gate.
84. **NEW, S155: `grep -c` COUNTS LINES.** Four figures in a hardware ruling were line counts
    reported as occurrence counts, in a section whose subject is *measure it, do not re-litigate
    it*. **If a number will be used to scope a fix, it must be the number the fix will encounter.**
