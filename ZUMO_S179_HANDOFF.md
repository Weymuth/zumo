# ZUMO — S179 HANDOFF (written at S178 close · paste at top of Session 179)

## READ THIS FIRST

**S178's work IS PUSHABLE and DJ verifies the push himself (standing ruling, S158).**
`git rm ZUMO_S178_HANDOFF.md` is part of that push. **If `__pycache__/` exists in your tree,
delete it LAST, immediately before pushing** — it REGENERATES on every gate run.

**78/78 gates** · `quiz_bank` 16 banks at **1,246** questions · `build_css --check` current ·
`build_worklist --check` current **after regeneration** · `image_audit --check` current ·
`callout_id` **1127/0** · `next_pointer` clean · census **41,006**.

**`site_parity` RAN TWICE AT S178 OPEN AND WAS PARITY BOTH TIMES**, which closes S177's owed
item. The tree now differs from the published site by design again. **Run it at least twice
AFTER this push, tree untouched between runs, and believe the repeat (§16.42).**

**`byte_audit` DID NOT RUN AND DID NOT NEED TO.** No payload moved, no Maker change. The eight
standing controls are verified as of S175.

**S178 EDITED TWO LESSONS, FIVE BANKS, ONE INSTRUMENT AND ONE DOCUMENT.**
`Lesson_02.html` → **v03.22.0** (moderate, both §5b homes) · `Lesson_01.html` → **v03.31.2**
(minor, hidden home only) · `QUIZ_L01` **1.1.5** · `QUIZ_L02` **1.0.8** ·
`QUIZ_L03` **1.0.5** · `QUIZ_L04` **1.1.7** · `QUIZ_L16` **1.0.15** ·
`book_gates` **v1.72.9** (gate 78 predicate + §27.11 digest) ·
`ZUMO_SUPER_BIBLE.md` **v8.171** (§16.47 NEW, seated with a numbered body) ·
`GPT_WORKLIST.md` regenerated (stamp line only) · `css/book.css` regenerated.

**Census 41,009 → 41,006.** The −3 is DERIVED, not a loss: §8A.2's block went 6 printed lines
to 5 and §8A.3's went 10 to 8 when both were converted from Allman to K&R.

---

# 1. LESSON 2's ARC — TEN EDITS SHIPPED, TWO PARKED WITH REASONS, TWO ALREADY DEAD

## THE COMPILER SETTLED WHAT READING COULD NOT

`L02-01` said §3.1's *Three Builds That Fail* produce the wrong errors. **Installed `gcc-avr`
and compiled all three.**

| build | lesson claimed | measured |
|---|---|---|
| 1 | stops at `flashTwice();`, *not declared in this scope* | **CORRECT** — it is the FIRST error reported |
| 2 | compiles clean, linker says *undefined reference to 'beep()'* | **CORRECT, exactly** |
| 3 | *another undefined reference* (linker) | **FALSE** — `error: too many arguments to function 'void showCount()'` |

Build 3 never reaches the linker: the definition sits below `loop()`, so the only `showCount`
in scope at the call is the argument-less promise. **The section now teaches three cases
instead of two** — forgot to ANNOUNCE (B1, compiler) · announced it WRONGLY (B3, compiler) ·
announced it and never WROTE it (B2, linker).

**GPT WAS RIGHT ABOUT THE PLACE AND WRONG ABOUT THE DIAGNOSIS A FIFTH TIME.** Its Build 1
objection — a missing `#include`, so `ledYellow` is undeclared too — is the book's own fragment
convention; the INSIGHT four lines above prints `Serial` with no include either. No edit owed.

## §8A WAS WRITTEN IN A FOREIGN HOUSE STYLE, AND THE LESSON HAD ALREADY CONVICTED IT

The block introduced as *the `blinkLED()` function you read earlier* is not that function:
`ledRed` against the canonical `ledYellow`, **Allman braces thirty lines after §3 declares
*this book uses K&R everywhere***, and 4-space indent against the book's 2. Step 5's own
checkpoint says *Yellow is the only LED that's fully yours.* **§16.46's shape again.** Both
§8A blocks corrected. `ledRed` is 0 in L02's payloads, so the edit could not leak.

## THE OTHER SEVEN

`L02-08` §4 continuity (L01 touched five things — now matches L01-07's wording; the *still
idle, exactly as in Lesson 1* sentence went with it) · `L02-10` Step 3 (`Zumo32U4ButtonC
buttonA;` is legal C++ — *a green build is evidence, not proof*) · `L02-11` + `L02-18` closed
by ONE sentence · `L02-14` Step 7 (only Button A ever had LED code) · `L02-16` *The Seven
Sections* reframed as the RoboLore standard rather than a C++ rule.

## TWO WERE ALREADY DEAD, FOUND BY READING RATHER THAN ASSUMED

`L02-04`'s straight-road paragraph already credits Lesson 1's `while` and `for`; `L02-05`
already names **Warm-Up 2**. Both fixed in some prior session and still carried on the list.

## TWO PARKED, EACH FOR A MEASURED REASON — S179 SHOULD RULE THE SECOND

- **`L02-09` (the baud comment) IS A MAKER EDIT, NOT A LESSON EDIT.** The string
  `115200 = the speed; the Serial Monitor must match it` appears **4× inside L02's own
  payload**. A lesson-only fix breaks `gate_payload_match`. Belongs in the Maker batch.
- **`L02-06` (globals have no home) IS REAL AND EXPENSIVE.** Measured: `GLOBAL VARIABLES`
  appears **0 times in `Lesson_02.html` and 0 times in L02's payloads** — lesson and payload
  agree — while Challenge 3 says *declare three counters up top* and "up top" is the only
  address the lesson gives. The fix moves `L02_GRAPHIC_2-05_sketch_anatomy.svg`, the §3.1
  color key, *The Seven Sections* → eight, §5's walkthrough, and probably Bible §18.3.
  **RULED AT S178 CLOSE UNDER §24.17: PARKED UNTIL AFTER SEPTEMBER 8, and filed in
  `ZUMO_AFTER_LAUNCH.md` rather than carried here (rule 72).** The reason is the SVG: the fix
  is not finished until `L02_GRAPHIC_2-05_sketch_anatomy.svg` gains an eighth band, which goes
  through the graphics chat and `GPT_WORKLIST.md`, and **a half-applied fix leaves the prose
  saying eight while the picture the lesson prints says seven** — S171's stale-wall shape, where
  the caption and the picture disagreed for three sessions and nothing in this repo reads inside
  an SVG. **The student-facing cost of leaving it is low and was measured:** Challenge 3's
  template prints the three declarations in position at the top of the file, so *up top* is
  imprecise rather than wrong, and the payload already carries the banner S51 added. `L02-09`
  is parked beside it for the same reason — one coupled Maker+SVG pass, after launch.

---

# 1a. LESSON 1 IS CLOSED. ALL FIFTEEN GPT ROWS ARE ACCOUNTED FOR.

**DJ's focus at S178 close was L01, so all fifteen rows were re-checked against the TREE rather
than against S177's summary.** Ten shipped at S177. Four were already dead and an INSTRUMENT is
what says so, not a memory:

| row | why it is closed |
|---|---|
| `L01-02` + `L01-10` | the *brain of your Zumo* claim is gone; six `A-Star` mentions survive and all six are the legitimate `board = a-star32U4` build target. **Gate 76 forbids the retired wording book-wide and passes.** |
| `L01-14` | **Gate 73** asserts every printed figure has an index row, all 16 lessons, and passes. |
| `L01-15` | **Gate 71** asserts the strip's catalog name, all 16, and passes. L01's one `Lesson 16 —` hit is Engineer's Log prose, not the nav strip. |

## `L01-13` WAS THE LAST ONE OPEN, AND IT IS NOW FIXED — `Lesson_01.html` **v03.31.2**

Three sites disagreed about where a project lives. **Step 1 was broken independent of which path
was right:** it told the student to copy the Lesson 1 project folder *while in*
`Documents/PlatformIO`, which the turn-in callout says is one level ABOVE where that folder sits.
**Read in order, the lesson disproved its own instruction — §16.46's shape a third time.**

**THE CONTRADICTION CONVICTED IT; THE DIRECTION OF THE FIX NEEDED THE ROOM.** PlatformIO is NOT
installed in the container and `pio_harness.sh` is a misnomer running raw `avr-gcc`, so nothing
here can observe where the New Project wizard drops a folder. **DJ confirmed it against a live
PlatformIO: `Documents/PlatformIO/Projects/<name>`.** §24.17 carve-out 1, used exactly as
intended — the internal evidence named the defect, the room settled the fix.

Both wrong sites now match the turn-in callout, and step 1 says *the same folder your Lesson 1
project landed in* so the three sites cross-reference rather than merely agree.

**PIN ARC CLOSED IN THE SAME SESSION.** `QUIZ_L01`, `QUIZ_L02` and `QUIZ_L16` pin `lesson_01`.
**No question in any bank asserts a filesystem path** — `L01_A15` asserts the template RULE
(*never work inside it again*), which did not move. All three pins **earned**.

**L01 NOW OWES ONLY A BENCH PASS.** See `ZUMO_BENCH_TESTS.md` — Challenge 4 on the floor,
Challenge 11's solution as printed, and the unplugged-upload error string.

---

# 2. THE BANK INHERITED THE LESSON'S ERROR — S177's INVERSION, REVERSED

`L02_B05` keyed *C++ treats them as two different functions, and the promised one is never
written*, with a distractor `why` reading **"the failure arrives later, from the linker."**
Both were authored faithfully from a lesson that was wrong.

**S177: the bank was right and the lesson wrong. S178: the bank inherited the lesson's error.
The payload decides in one direction and the COMPILER decides in the other — and a correct
edit can falsify a bank that was authored faithfully.**

**THE PIN ARC CLOSED IN THE SAME SESSION (§37).** `QUIZ_L03`, `QUIZ_L04` and `QUIZ_L16` also
pin `lesson_02`; their four L02-asserting questions were read and are untouched by any changed
sentence, so all three pins were **earned**. `UNREAD_PINS` stays 0.

**AND §24.2's TWO-HOMES COMPARATOR FIRED ON MY OWN EDIT** — I bumped `bank_version:` without
the `# Bank version:` comment on all four banks. The arm working exactly as S161 built it.

---

# 3. GATE 78's FIX SHIPPED — AND THE PRICED DESIGN DID NOT WORK ON ITS FIRST BUILD

**READ §16.47. THIS IS THE SESSION'S BEST FINDING AND IT IS NOT THE ONE THAT WAS PRICED.**

S177 priced: *blank `**` at EQUAL LENGTH, the way `_CODE78` blanks backticks, so the offsets a
failure message reports stay true to the source.* Built exactly as specified, **control 2 — the
bold plant, the whole point of the fix — stayed SILENT.**

Equal-length blanking turns `**12** discards` into `  12   discards`. **Three spaces where the
predicate demanded one.** The rationale for the mechanism caused the failure of the mechanism.
Widened to `\s+`, which also reaches a figure broken across a LINE WRAP.

**AND THE ORDERING TRAP THE DESIGN WARNED ABOUT DOES NOT EXIST.** Measured on six shapes, both
orders behave identically — `**` and a backtick are disjoint characters, so equal-length
blanking preserves the other marker's delimiters either way. Backticks stay first because it
costs nothing; the comment now records the measurement, not the prediction. **A hazard reasoned
out and written into a design is a lead and not a finding (§24.6c) — including when this book
wrote the lead.**

### SEVEN CONTROLS, ONE PER INVOCATION, ALL PLANTED INTO LIVE.md's CURRENT SESSION REGION

1. `12 discards over 7 of 105 payloads` → **FAILS** *(no regression)*
2. `**12** discards over **7** of 105 payloads` → **FAILS** *(the whole point; SILENT on build 1)*
3. `` `15 discards over 7 payloads` `` → **SILENT** *(exclusion survives)*
4. ``**`15 discards over 7 payloads`**`` → **SILENT** *(the recorded trap, proven absent)*
5. clean tree → **78/78**
6. `12 discards over 7 of 105\npayloads` → **FAILS** *(new reach: line wrap)*
7. `**15** discards over **7** of 105 payloads` → **SILENT** *(no false positive)*

---

# 4. S179 OPENS HERE — THE GPT LIST IS STILL THE ASSIGNMENT

**DJ: *"I can't ship a book with errors in it."* L01 and L02 are done.**

## THE 12 STILL-VERBATIM ROWS (verify each against the tree BEFORE editing)

`L03-03` `L05-01` `L06-03` `L08-05` `L09-07` `L09-13` `L10-06`
`L12-05` `L12-09` `L12-17` `L13-06` `L13-08` `L13-10`

**L03 IS THE OBVIOUS NEXT LESSON AND IT ALREADY HAS THREE ITEMS WAITING:**
- **`L03-03`** — Part 2 still lists *"Your Zumo_Lesson_2 project folder (we'll copy it)"*, one
  occurrence, against a §5.1/§6 that use the Maker for a fresh project. **CONFIRMED, UNFIXED.**
- **`L03-04`** — §4.1 *"this lesson introduces motor control."* L01 already drove the robot;
  **L02's Warm-Up 4 spins it, verified this session.** This is L01-07 and L02-08's third twin
  and should be fixed with the same wording.
- **THE UNTAGGED S177 FINDING:** Part 2's prerequisites ask for *Robot connected via USB* AND
  *Clear floor space (6+ feet)*. **You cannot drive six feet tethered.** L01 names the
  floor-test ritual; L03 is where it should first be USED.

**THE OTHER BUCKETS:** 48 rows whose quote is GONE with no surviving 4-word fragment (strong
evidence already fixed — a mechanical DEAD/LIVE pass would close them) · 45 ambiguous · 63 with
no checkable quote, needing a human read.

**AND TWO ROWS DIED WITHOUT ANYONE NOTICING (L02-04, L02-05).** That is evidence the 48-row
DEAD bucket is real and worth a mechanical pass — it would be cheap and it would shrink the
list by a third.

---

## BENCH — `ZUMO_BENCH_TESTS.md` IS THE HOME. DO NOT CARRY BENCH ITEMS IN A HANDOFF.

51 rows across 15 lesson blocks, DERIVED from the file. It also carries the floor-test ritual
once. **THE OLDEST OPEN ITEM IS `L09-B1`, carried since S41. THE MOST CONSEQUENTIAL IS
`L10-B1`** — §16.12's perpendicular arrival, unruled since S143, with a falsifiable prediction.

**L01 is still owed a bench pass** — DJ said he would test it. Nothing bench-dependent shipped.

---

## STANDING, UNCHANGED

- **A GATE FOR `GPT_WORKLIST.md` IS OWED AND PRICED, NOT SHIPPED** (S174). An arm that made the
  routine slower is one somebody eventually skips.
- **`gate_payload_match` IS STILL NOT ONE OF THE 78** — the S137 exposure.
- **EIGHT INSTRUMENTS DIE ON AN UNRECOGNIZED ARGUMENT WITH A RAW TRACEBACK.** Ugly and SAFE.
- **S167's DEBT IS CLOSED AND MUST NOT BE RE-OPENED** (Bible §16.43).
- **`byte_audit` ARM 2 STILL CANNOT SEE A FIGURE IN PROSE.** **Ten more prose defects shipped
  this session past 78 green gates** — §16.18 from the content side, second session running.
- **L16 STILL NEVER STATES ITS MATCH-MODE FIGURE** (S166).
- **GATE 77 DOES NOT EXCLUDE `<pre>`** (S165). When it first fires, the answer is a ruling.
- **§16.32–§16.44 STILL HAVE NO NUMBERED BODIES** — thirteen remain changelog-only. §16.45,
  §16.46 and §16.47 were all seated rather than added to that queue.
- L03 queued content · `ZUMO_L03_TEMPLATES.md` staging · Bible §14 TDP-canon entry ·
  day-by-day grid + syllabus.
- **The poster is a GRADED deliverable** (DJ, S159). **Photography is OFF the critical path** (S156).
- **Fall launch Sept 8. L13 is the last in-scope lesson and it is whole.**

---

# HARNESS — IT IS NOT IN THE REPO. RUN THE SCRIPT.

```
apt-get install -y gcc-avr avr-libc     # foreground; the box has no toolchain
sh harness_setup.sh                     # prints objects: 41  AND  core stderr: clean
python3 byte_audit.py --sizes           # ~3 min
python3 byte_audit.py --selftest        # before trusting --check
python3 byte_audit.py --check           # EIGHT arms
python3 byte_audit.py --discards        # ARM 9, ~3 min, NOT in --check's path
```

**STANDING CONTROLS, ALL REPRODUCED S175, UNTOUCHED BY S176, S177 AND S178:**
`11/after_step_1` **20,592** · `11/finished` **20,778** · `12/finished` **24,790** ·
`12/c2_slipalarm` **21,334** · `13/finished` **25,248** · `14/finished` **26,002** ·
`15/finished` **28,406** · `16/finished` **28,626**.

**216 payloads, FOUR declared overflows** — `16/after_step_3` **29,008** · `16/after_step_4`
**29,644** · `16/step_5_serial_traded` **28,944** · `16/step_5_zn_traded` **28,788**.

**THE TIGHTEST PASSING BUILD IS `16/after_step_2` AT 28,648, WITH 24 BYTES SPARE.**

**ARM 9: 15 discards over 7 of 105 payloads, 7 adjudicated, 0 unexplained.**
*(Gate 78 now reaches that figure however this project's house style bolds it.)*

---

# STANDING AUTHORITY — §24.17 AND §24.19

**Decide and report; do not ask.** Three carve-outs: facts about the ROOM no instrument can see;
moves that are irreversible or expensive to undo; and RoboLore brand and course scope.
**Delegation removes the question, never the disclosure.**

**§24.19 IS THE TIEBREAKER** — what is best for student learning, when nothing else discriminates.

---
<!-- VERSION BLOCK: emitted by session_versions.py --handoff. Never hand-typed. -->
Fresh-clone verified at **`7bf5bef`**. Census **41,006**.
Bible **v8.171** · `BookComponentStandard` **v01.13.0** · Maker **v2.62** ·
`marks/` **41** · `icons/` **49** incl. LICENSE.
`ZUMO_Syllabus_WORKING.md` **v1.3**.

Instruments: `book_gates` **v1.72.9** · `lesson_inventory` **v1.3.5** ·
`gen_component` **v1.6.1** · `pill_sweep` **v1.1** · `gate_payload_match` **v1.9.0** ·
`build_family_map` **v1.6.6.1** · `callout_id` **v1.0** · `keyterm_prefix` **v1.0.1** · `build_mark_index` **v1.1.0** · `gen_bonus_banner` **v1.4.1** ·
`gen_part_banners` **v1.2** · `session_versions` **v1.30.0** · `fit_raster_svg` **v1.2** ·
`flatten_alpha` **v1.2** · `svg_layout_audit` **v1.20** · `site_parity` **v1.2** ·
`build_css` **v1.4.0** ·
`image_audit` **v1.3** ·
`strip_inline` **v1.2** ·
`build_worklist` **v1.2** ·
`regex_audit` **v1.0** ·
`byte_audit` **v1.9.1** ·
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
`quiz_bank` **v1.6.1** ·
`timer.html` **v1.3.2** ·
`harness_setup.sh` **v1.1** ·
`pio_harness.sh` **v3.1** ·
`going_deeper` **v01.6.1**.

Lessons: L01 v03.31.2 · L02 v03.22.0 · L03 v03.43.2 · L04 v04.29.2 · L05 v04.29.1 · L06 v04.32.4 · L07 v04.31.5 · L08 v04.32.1 · L09 v05.27.4 · L10 v02.30.3 · L11 v02.31.1 · L12 v01.33.1 · L13 v02.35.0 · L14 v02.36.0 · L15 v02.32.0 · L16 v02.28.0.
