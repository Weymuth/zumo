# ZUMO — S154 HANDOFF (rewritten at S153 close · paste at top of Session 154)

## Session open ritual (do this without being asked)
1. **`git ls-remote https://github.com/Weymuth/zumo.git HEAD` FIRST.** A stale answer is
   timing, not caching — **retry a minute later before concluding a push failed** (§12.4).
   **AND THE SHA IS NOT THE CHECK. `session_versions --check` IS** (rule 60, S145).
2. Read `LIVE_ZUMO_TEXTBOOK.md` — verify date / status / versions.
3. **Do NOT grep the Bible version.** `session_versions.bible_consistency()` parses it.
   **S153 measured why: the phrase `Bible version: v` occurs THREE times, and two of them are
   grep COMMANDS quoted inside the Bible.** A naive `grep -o` returns `v8.144`, `v`, `v`.
4. Run the full suite and **READ THE EXIT CODE, NOT THE LAST LINE**. **THE SUITE IS 72 GATES,
   NOT 71** (gate 72 new, S153). Plus **`callout_id.py --selftest` then `--audit`**,
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
14. **`rm -rf __pycache__` BEFORE `git status`. Also `quizzes/__pycache__` — S153's gate 72
    imports `quiz_bank` as a library, so the suite now CREATES that directory every run.**
    Also `find . -name pbuild -exec rm -rf {} +` if the toolchain has been run.
15. **THE FULL SUITE TAKES ~40 SECONDS.** Budget control harnesses accordingly; S153 lost a
    run to a harness that fired eight suite invocations inside one command timeout.

## 16. THE AVR TOOLCHAIN — S146's INSTRUCTIONS STILL HOLD. NOT RUN IN S153.

`apt-get install -y gcc-avr avr-libc` **(no `sudo` — it is not on this box, exit 127).** Clone
into `/home/claude/harness` **FLAT, not under a `pololu/` subdirectory**.

**READ THE EIGHT LIBRARIES OUT OF `LIBDIRS` IN THE SCRIPT. DO NOT CARRY THEM FROM A HANDOFF —
INCLUDING THIS ONE.** Also clone `arduino/ArduinoCore-avr`. Zumo library at tag **2.0.1**
(plain clone then `git checkout 2.0.1`; `--depth 1` cannot check out a tag). `cp pio_harness.sh`
into `$H`, then `bash pio_harness.sh --setup`. **Expect *objects: 41*.**

**THE CONTROL: L11 `after_step_1` MUST COMPILE TO 20,516.** Held S144–S149, from five clones.
**The harness prints `flash=` on success and `OVER flash=` on an overflow — parse both.**

---

# THE ONE THING TO CARRY OUT OF S153

**TWO MECHANISMS PINNED TO THE SAME SCOPE ARE NOT REDUNDANCY. THEY ARE ONE BLIND SPOT
COUNTED TWICE.**

`quizzes/quiz_bank.py` declared a `VERSION` and was registered in nothing for seventeen
sessions. Two separate instruments should have caught it — `roster_coverage()`, which runs on
every `--check`, and CONTROL E, which runs on `--selftest`. **Both spelled their scope as
`glob('*.py')`: the repo root.** Having two of them felt like defence in depth and bought
exactly nothing, because they shared the assumption, not the coverage.

**The corollary is how to audit for this.** When two controls cover one property, do not ask
whether both exist — ask what they would each say if the property were violated **in a place
neither was written for**. If the answer is the same silence, there is one control.

And the session's own correction belongs here: **CONTROL E's single-quote pin was reported to
DJ as a live exposure and was not one.** `roster_coverage()` covered root regardless of
quoting. **A failing control is what found the second mechanism** — the claim had survived a
triple check, because the triple check read CONTROL E and never asked what else was watching.

---

# S153's RULINGS

**DO THE QUIZ-BANK GATE FIRST.** DJ's word at open. It was the urgent one of the four ungated
invariants because `quiz_bank --check` was loud and nothing called it.

**FIX `check()`'s EMPTY SCAN.** DJ ruled after the gate was written and the hole was measured:
the gate protects the book, and nothing protected a person running `--check` by hand and
reading exit 0 as a result.

**REGISTER `quiz_bank` AND WIDEN BOTH MECHANISMS.** DJ asked for a recommendation, then for a
triple check, then ruled. The triple check confirmed the plan and **corrected one claim inside
it**, which is the strongest argument for the ritual that exists so far.

---

# S154 QUEUE

## 0. THE GPT REVIEW — STILL INCOMPLETE, AND THE SHARE LINK DOES NOT WORK
DJ supplied `https://chatgpt.com/share/6a7dd392-c0d0-83ea-995e-4ace30278903` in S153.
**It cannot be read from here.** The page renders client-side, so both extraction methods
return the page TITLE and zero turns, and `chatgpt.com` is not on this box's allowed-domain
list either. The title is **"Zumo Asset Audit L01-16"**, which is **not obviously the same
conversation** the S152 handoff describes — do not assume it is.

**ASK FOR THE DATA EXPORT, NOT A PASTE.** ChatGPT → Settings → Data controls → Export data
produces a zip containing `conversations.json` with every turn intact. **A select-all copies
the rendered page, not the conversation** (rule 75) — that is what lost fourteen of sixteen
replies the first time. **Count sixteen replies before working from whatever arrives.**

**Triage rules from S152 still stand, apply them when it lands:**
- **STRIKE, already ruled:** the spiral audit · tie competition claims to a year (rule 63) ·
  the absolutes pass (§16.16, rule 61) · measured-facts discipline (§24.15) · "write a canon
  sheet first" (that is the Bible).
- **ONE RULING WEARING FOUR HATS:** the L15 theory notes are one item — the book teaches
  conditional physics as absolutes — and it is DJ's call, not a fix.
- **GPT CANNOT SEE A RULING (rule 39)** and will re-report settled items. Read its list
  against the Bible before reporting any of it (rule 72).
- **GPT'S OWN RULEBOOK CLAIMS CARRY NO EDITION.** Settle them against
  `RCJRescueLine2026-final.pdf` in the root before any of them reaches a lesson.

## 1. TWO CONFIRMED CODE FINDINGS, STILL DELIBERATELY NOT FIXED
Both verified against the tree at S152, untouched in S153. Both move bytes, so both need the
toolchain and a full lesson arc — patching either alone compiles the chain twice.
- **L16's RUN IS NOT FROZEN WHEN IT ENDS.** `saveBaseline()` computes `millis() - runStart` at
  CALL time from `RUN_REPORT`, so the saved lap inflates while the student reads the report.
  **`showScore()` recomputes it the same way, so the displayed number is climbing on screen.**
- **L15's GAP-WINDUP DEMONSTRATION IS ARCHITECTURALLY IMPOSSIBLE.** `followLine()` is called
  only inside `if (isLineVisible())`, so `lineIntegral` cannot accumulate during a gap. Prose
  and code disagree **and the code is right.**

## 2. THE PHOTOGRAPHY — STILL THE ONLY THING BETWEEN THE BOOK AND SEPTEMBER
Stills **3.2 · 3.5 · 3.6 · 4.1 · 4.3 · 12.1 · 13.1 · 13.2**, videos **3.1 · 4.1 · 6.1 · 8.1**.
**VIDEO 3.1 carries L03's opening page.** Nothing in the tree can produce them.
*(`IMAGE 14.1` and `IMAGE 16.1` are also unshot; both lessons sit outside the September scope.)*
**September 8 is the launch date. This is the critical path and nothing else is.**

## 3. INVARIANTS WITH NO GATE — ONE CLOSED, TWO LEFT
**The quiz bank is CLOSED (gate 72, S153).** The Maker label closed at S152 (ARM 4).
**Still open: A NAV PILL · A RULE CITATION.** Neither is urgent; neither has a measured
defect outstanding. Do not open one without a ruling.

## 4. THE CATCH-UP CONVENTION — READ §16.22 BEFORE RE-RAISING
**§16.22 (v8.140) ruled the split LEGITIMATE** and ARM 3 measures rather than judges it. What
is open is only whether a gate should pin the measurement. **A gate pinning either convention
would certify 64 rows and fail 32.** ARM 3 reaches only TWO rows book-wide.

## 5. STILL OPEN, CARRIED
- **`GRAPHIC 16.1` OVERFLOWS ITS PANEL BY 31 UNITS** — recorded S148, not fixed, pre-existing.
- **§4.2's AUDIT TABLE IS UNCONFIRMED AND MAY NOT BE CONFIRMABLE.**
- **§16.14, §16.18–§16.21 AND §24.11–§24.16 HAVE NO NUMBERED SECTION BODIES.** §16.12 and
  §16.13 sit BELOW §17. **S153 added §24.17's ruling to the changelog-only pile rather than
  seating one section beside six that need the same treatment** — that is a pass of its own.
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
- **THREE BANKS ARE PINNED TO SUPERSEDED LESSON VERSIONS** (S153 lead, not a finding): L15's
  bank names `lesson_15=v02.31.0` against a live `.1`, L16's names `lesson_16=v02.23.0` against
  `.24.0` and `lesson_02=v03.21.2` against `.3`. All three bumps were title-separator and
  Maker-label work, so the odds a question is now wrong are low — **but it is unverified, and
  rule 37 says the read does not transfer.** Do not rewrite the pins without doing the read.

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
Fresh-clone verified at **`c9be73a`**. Census **40,648**.
Bible **v8.144** · `BookComponentStandard` **v01.13.0** · Maker **v2.50** ·
`marks/` **41** · `icons/` **49** incl. LICENSE.
`ZUMO_Syllabus_WORKING.md` **v1.2**.

Instruments: `book_gates` **v1.67.0** · `lesson_inventory` **v1.3.5** ·
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
33. **NO INSTRUMENT READS PROSE — AND NONE COMPILES EITHER.** Point the toolchain at every kind.
34. **A NUMBER IS ONLY CHECKABLE AGAINST THE OTHER FIFTEEN LESSONS.**
35. **COMPILE THE SNIPPET; LET THE BOOK'S OWN CODE TESTIFY.**
36. **A FACT THAT LIVES ONLY IN AN SVG IS NOT IN THE BOOK** — and a WRONG one is still wrong.
37. **READ -> FIX -> QUIZ, NEVER QUIZ FIRST — AND THE READ DOES NOT TRANSFER BETWEEN SESSIONS.**
38. **A TEXT MATCH LOCATES; IT NEVER ANSWERS.** **S153: committed again, inside a TRIPLE CHECK.
    A regex too narrow to see `% (VERSION, QUIZ_DIR)` returned TWO where `ast` returned THREE.**
39. **NO INSTRUMENT THAT READS THE TREE CAN SEE A RULING.**
40. **PULL THE PAYLOAD, NOT THE CARD.**
41. **AN ENTRY FILED IN ONE HOME IS NOT FILED.** **S153's second face: a DEFECT fixed in one of
    two homes is not fixed. CONTROL E and `roster_coverage()` shared a scope pin, and mending
    only the one that failed would have left the every-session check identically blind.**
42. **A SPEC'S OWN NUMBERS CAN BE ARITHMETICALLY IMPOSSIBLE.**
43. **WHEN TWO SECTIONS DISAGREE, READ THE CITATIONS — AND WHEN THE CITATIONS DISAGREE, READ
    THE RULEBOOK'S CHANGELOG. If you do not HAVE the rulebook, say so and stop.**
44. **THE HEADER OF A THING IS NOT THE THING.** **S153: CONTROL E's label said *a root .py*
    and its code carried a SECOND pin the label never mentioned. Read the predicate.**
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
59. **A CONTROL THAT FIRES FOR THE WRONG REASON IS NOT A CONTROL.** **S153: and a control that
    PASSES for the wrong reason is not one either — a harness read an ABSENT section as a
    silent one, committed inside a harness written to enforce this rule.**
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
    **S153's variant: a control reporting the section ABSENT — on the CLEAN copy as well as
    the seeded ones — is reporting a broken harness. Read the failure DETAIL, not the verdict.**
72. **A QUEUE IS NOT CANON.** Check the queue against the Bible before reporting it.
73. **A LABEL CAN AGREE WITH ITSELF AND BE WRONG ABOUT THE WORLD.**
74. **THE STRING THE USER READS IS AN ARTEFACT, AND IT NEEDS A GATE LIKE ANY OTHER.**
75. **A SELECT-ALL COPIES THE PAGE, NOT THE CONVERSATION.** **S153: and a SHARE LINK carries
    neither — the page renders client-side, so a fetch returns the title and zero turns.
    Ask for the data export.**
76. **SCOPE A DEFECT BEFORE BUILDING A CONVENTION FOR IT.**
77. **A CHECKSUM YOU DID NOT COMPUTE IS WORSE THAN NO CHECKSUM.** Paste the OUTPUT of
    `md5sum`, or publish none. Nothing in the tree can see a chat message.
78. **NEW, S153: A SCAN THAT FOUND NOTHING IS NOT A SCAN THAT FOUND NOTHING WRONG.**
    `quiz_bank.check()` returned an empty problem list on an empty glob, so `--check` exited 0
    with **every bank deleted**. Zero asserted is not zero problems (rule 27's other face), and
    any checker that can return clean from an empty population owes a coverage arm.
79. **NEW, S153: TWO MECHANISMS PINNED TO THE SAME SCOPE ARE ONE MECHANISM.** Ask what each
    would say if the property were violated where NEITHER was written to look.
80. **NEW, S153: A SECOND HOME IS ONLY WORTH WATCHING IF SOMETHING READS IT THAT CANNOT READ
    THE FIRST.** `quiz_bank` carried its version in a docstring and a constant. The fix was to
    DELETE one, not to register a watcher — §5b's visible banner earns its second home because
    a student reads it; a docstring duplicating what `main()` already prints does not.
