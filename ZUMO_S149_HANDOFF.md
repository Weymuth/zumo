# ZUMO — S149 HANDOFF (rewritten at S148 close · paste at top of Session 149)

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

# THE ONE THING TO CARRY OUT OF S148

**LESSON 16 DID NOT FIT ON THE CHIP, AND NOTHING IN THE TREE COULD SEE IT.**

L15's finished build grew 180 bytes, so L16's whole chain started higher. Measured: **Step 3
overflowed by 152, and the FINISHED build — the one both sabotages and the entire capstone
derive from — was 84 bytes over the ceiling.** The trade the lesson teaches (Serial out,
EEPROM in) no longer paid the bill.

**Seventy gates passed the whole time.** `gate_payload_match` passed. A lesson whose central
build cannot be flashed is, to every instrument in this repo, a perfectly well-formed lesson.
**Rule 33 in its most expensive form yet: no instrument reads prose, and no instrument
compiles anything either — only the toolchain does, and only when you point it at every kind.**

**The fix was a design ruling, not a number.** Six candidate cuts were priced by deletion
against the finished build:

| cut | frees | lands |
|---|---|---|
| **Ziegler–Nichols hint (CHOSEN)** | **156** | 28,600 · 72 spare |
| buzzer, all 12 `playNote()` calls | 1,828 | 26,928 · 1,744 spare |
| `checkBattery()` A+B report | 114 | 28,642 · 30 spare |
| the 3-2-1 countdown | 104 | 28,652 · 20 spare |
| the WEAVE row | 60 | still over by 24 |
| `showStatus()` prox readout | 8 | still over by 76 |

**The buzzer was rejected even though it is by far the biggest.** §7.4 hands it to the STUDENT
as their reserve and writes their TDP sentence for them; spending it in the book would leave
1,744 bytes of runway, so no student would ever have to trade anything — in a lesson called
*Nothing Left to Take Away*. **`checkBattery()` was rejected because §7.1 requires the A+B
report for benchmark battery honesty.** Only Z–N both closes the gap and breaks nothing.

**And it made the lesson better.** Step 5 now makes TWO trades: the easy one (Serial, −704,
**still 84 over**) and the hard one (Z–N, −156, green at 28,600). The book previously modelled
only the kind of cut everyone agrees with. **The sentence it can now write is *the obvious cut
was not enough*.**

---

# STATE

<!-- VERSION BLOCK: emitted by session_versions.py --handoff. Never hand-typed. -->
Fresh-clone verified at **`8179899`**. Census **40,642**.
Bible **v8.139** · `BookComponentStandard` **v01.13.0** · Maker **v2.49.4** ·
`marks/` **41** · `icons/` **49** incl. LICENSE.
`ZUMO_Syllabus_WORKING.md` **v1.2**.

Instruments: `book_gates` **v1.65.12** · `lesson_inventory` **v1.3.5** ·
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

Lessons: L01 v03.28.3 · L02 v03.21.2 · L03 v03.41.0 · L04 v04.29.0 · L05 v04.29.0 · L06 v04.32.1 · L07 v04.31.4 · L08 v04.31.1 · L09 v05.27.0 · L10 v02.29.1 · L11 v02.30.0 · L12 v01.31.3 · L13 v02.29.0 · L14 v02.34.0 · L15 v02.31.0 · L16 v02.23.0.

`quizzes/QUIZ_SPEC.md` **v1.2.0** · banks L14, L15, L16 **v1.0.0** NEW ·
`ZUMO_TDP_Template_v3.md` **v3.1.1** · `RCJRescueLine2026-final.pdf` NEW (repo root, 9.8 MB).

**ALL SIXTEEN LESSONS ARE READ, FIXED AND BANKED. Derive the count, never read it out of this
sentence:** `python3 quizzes/quiz_bank.py --status`

---

# WHAT S148 SHIPPED

Three full READ → FIX → QUIZ arcs — **L14, L15 and L16** — plus the rules pass. Sixteen of
sixteen banks now exist.

## 1. THE RULES PASS — S147's CITATION FINDING WAS BACKWARDS

DJ supplied the official **RCJ Rescue Line 2026** PDF and ruled *"Go with the newest post."*
**The 2026 changes list opens with *Deleted "Terms and Definitions"*** — the §4.1 the 2025
edition inserted — so Section 4 shifts **back** by one and **L14 §4.1's citations were right
all along**; the Engineer's Log's `§4.3.7` was the 2025 number. Verified three ways in the PDF
(contents page, §4.2's item numbering, footnote **[1]** on §4.1). **The number moved twice in
three editions and landed where it started: 2024 §4.2.8 → 2025 §4.3.7 → 2026 §4.2.8** — so a
bare section number can be *coincidentally* right. Every citation now names its edition inline.

**`ROBOCUP_RESCUE_LINE_2026.md` was convicted on an inference and is innocent** — it is
genuinely the 2026 edition, carrying the wall-colour, white-LED and fake-victim clauses that
exist in no earlier one. S147 doubted it because **there was nothing in the tree to compare it
to**, which is why the PDF is now in the root. **RCJ governs, so L13 is untouched.**

**The ramp is resolved:** §3.7.4 awards per inclined tile, the 2026 changes list DELETES the
sentence the contradiction rested on (footnote [2]), so a three-tile ramp is **30**.

## 2. THE BYTE CASCADE, RE-COMPILED AT EVERY LEVEL

Not carried from any handoff. Control first, then every payload of three lessons.

**L14** — every S147 figure reproduced exactly: 25,072 · 25,816 (+744) · 25,780 (36 fewer) ·
25,076 (740 smaller) · B2/B3/B4 identical at 25,816 · **B4-in-match-mode 25,772, composed by
putting B4's `main.cpp` on the match-mode config after diffing to prove the composition
unambiguous.**

**L15** — +176 at the top, +180 at the bottom, **four of five deltas moved**: 25,816 · 25,980
(+164) · 27,286 (+1,306) · 27,334 (+48) · 28,214 (+880) · 7A 26,292 · 7D 27,400 · B2 28,230 ·
B3 28,164 (−50, delta changed).

**L16** — 28,214 · 28,464 (+250) · 28,824 **over by 152** · 29,460 **over by 788** · 28,756
**still over by 84** · **28,600 after the second trade**, 72 spare. Six of nine rows in the
Section 1 ladder were stale and were re-derived by compiling each lesson's own `finished`.

## 3. TEN DEFECTS NO BASELINE SHIFT WOULD HAVE TOUCHED

**L14, and the eighth is the one that matters:** `QUIZ_SPEC` §0 requires an end-to-end read *in
the session that writes the bank*, and **S147's read does not transfer.** The re-read found
**§4.3 claiming 4,800 mV "is the number `selfTest()` judges you against"** where the code reads
`battOK = (mv >= BATTERY_LOW)` — **4200** — which **Sabotage B3's own reveal already stated**
(*"420 is not 4200"*). A bank written on S147's read would have keyed 4,800 and marked every
student who read the code as wrong. Also: `830` rewritten rather than swapped (`selfTest()` has
**no function symbol** in the Step 3 binary — LTO inlined it into `setup()`; the only
`selfTest` symbols are **16 string constants totalling 149 bytes**); *260 lines* → **87**;
*Sections 3.3 and 6.3* → **8.3** (no §6.3 exists); §4.3's empty colon promise; §8.2's *Tuning
Helper Code* heading; §7E's shipped draft self-correction; *twelve-item* kit → **11**.

**L15: the doorway cost was stated three times, three different ways, and none was right.**
Step 6's header said +58, its own prose said *"Sixty-eight bytes"*, §8A.3 said *"costs 68"*.
Measured **48**. Also: **the capstone headroom was overstated by 180** (*"638 bytes left"* →
**458**), and **two Maker payloads shipped a comment attached to the wrong variable** — the 7D
and Challenge 2 builds had `lineIntegral` and `dFiltered` each carrying *"How long THIS pass
took"*, a sentence describing `dtSec`, while `dtSec` had none. Repaired on both sides together
and verified byte-neutral.

**L16:** the ladder, the linker error (626 → **788**), §4.2's heading, every step figure, both
sabotage sizes, §7.4's reserve, the Quick Reference. *"638 bytes … about a fifth of one
percent"* was **also wrong by a factor of ten** independently of the re-baselining.

## 4. GRAPHIC 16.2 WAS REDRAWN FROM ITS OWN GEOMETRY

The wall chart carried the whole stale ladder plus the Step 3/4 figures. **The scale was
DERIVED from the file — 0.016006 px/byte, bars grounded at y=660 — not eyeballed.** Eleven bars
recomputed; Step 3 turned red because it now crosses the ceiling; every bar read back and
checked against its true value. **The first render caught a collision** the numbers alone would
not have shown: Step 3's label ran straight through the ceiling caption. Caption moved left,
Step 3's label matched to Step 4's `+N` form. Its subtitle said *"the step that finally hits
it"*; two do now.

## 5. THE BANKS — AND THE DOUBLE CHECK THAT FOUND WHAT THE FIRST PASS DID NOT

L14 **v1.0.0** (75) · L15 **v1.0.0** (75) · L16 **v1.0.0** (75). **16 of 16 banks.**

**DJ ASKED FOR A DOUBLE CHECK AND §24.13 MEANS A DIFFERENT METHOD.** Three assertion arms were
run over the artefacts rather than re-reading them:

1. **A superseded-figure sweep** over three lessons, three banks and the SVG — 41 hits, every
   one read. **Zero in any lesson and zero in the graphic.**
2. **Every byte figure a bank keys as correct, compiled** — 22 builds, **0 mismatches**.
3. **Every `cite:` resolved against the lesson's real section ids** — 142 distinct citations,
   **0 unresolved**.

**ARM 1 FOUND S146's DEFECT REPEATING IN ALL THREE BANKS.** Ten distractors offered a
pre-correction figure and explained it with *"a figure from an earlier baseline"* or *"the old
baseline's figures"* — **which is an appeal to the book's edit history, and a student has never
seen those numbers and cannot reach that history.** QUIZ_SPEC §4's whole contract is that
`cite:` tells the student **where to re-read**. All ten rewritten so the wrong answer is wrong
for a reason findable in the lesson: Step 3's own overflow, Mystery B1's figure, the ceiling
itself, Step 2's delta. **Three of the thirteen hits were false positives** — `"before the"`
matching *"the pit check comes before the robot is allowed to move"* — read, not acted on
(rule 38).

**The first pass could not have found this.** `quiz_bank --check` validates structure and was
green on all sixteen banks the whole time. **No gate holds a quiz bank, and no gate can hold
this.**

## 6. TWO PROCESS FAILURES, BOTH MINE, BOTH CAUGHT

**A blinding control fired for the wrong reason** (rule 59). §27.13 failed on the *restored*
tree too, because the L15 comment repair added two syntax-highlight spans. Re-run clean
afterwards: the seeded mid-chain defect passes all 70 gates **and** `gate_payload_match`, and
is loud only to the compile-against-figure verifier. The endpoint-only form stays blind, as
S146 measured.

**Then I ran step 3 of the CSS cycle without `--include-held`** — **S119's documented failure,
verbatim** — reverting the lesson strip from `class=` to inline `style=` in all sixteen
lessons. Re-running with the flag returned the fourteen untouched lessons byte-identical to
HEAD. The flag is in the docstring and in S119's changelog entry; knowing the rule conferred
no immunity.

**A third near-miss worth recording:** the first Maker edit re-serialised the whole PAYLOADS
object with `json.dumps` — **2,726 changed lines and +58 KB for a four-payload change.**
Restored and redone as targeted encoded-string splices: **2 changed lines, same result.**
**A diff you cannot read is not a reviewable edit.**

## 7. RULE 46 PAID TWICE, AND THE SECOND TIME IT WON

Step 3's compile-check callout was `data-family="STILL GREEN"` and Step 3 is no longer green.
I gave it **`THE WALL`** — a family that already exists in L11–L13, is semantically exact, and
that Lesson 16, *the lesson named after hitting it*, carried none of. **Five gates fired at
once.** The sharpest was **§5.1: `THE WALL`'s 5px border is frozen debt, baseline zero for L16,
and the gate exists to stop it spreading.** So Step 3's overflow became **prose** — *"there is
no compile-check box for this step, because there is nothing green to put in one"* — and the
new compile check took the callout slot. **Net zero callouts, zero family moves, zero new
marks; four of the five cleared without touching a baseline.** S144's precedent arriving live.

Baselines that did move, each derived and blinding-controlled: **§27.11 twice** (rules and
declarations UNCHANGED at 574/2,033 both times, class set byte-identical, every declaration
block byte-identical — usage rank only), `book_gates` **v1.65.10 → v1.65.12**.

---

# S149 QUEUE

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
