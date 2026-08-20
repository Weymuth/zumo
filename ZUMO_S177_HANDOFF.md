# ZUMO — S177 HANDOFF (written at S176 close · paste at top of Session 177)

## READ THIS FIRST

**S176's work IS PUSHABLE and DJ verifies the push himself (standing ruling, S158).**
`git rm ZUMO_S176_HANDOFF.md` is part of that push. **If `__pycache__/` exists in your tree,
delete it LAST, immediately before pushing** — it REGENERATES on every gate run.

**78/78 gates** · `gate_payload_match` **PASS with the census armed** · `quiz_bank` 16 banks at
**1,246** questions · `build_css --check` current at 574 rules · `image_audit --check` current ·
`build_worklist --check` current · `callout_id` **1127/0** · census **40,993** ·
`next_pointer` clean.

**`site_parity` RAN TWICE THIS SESSION AND BOTH RUNS SAY PARITY.** That was S175's one open item;
it needed a published tree and now has one. Run it again after THIS push, at least twice,
and believe the repeat (§16.42).

**`byte_audit` DID NOT RUN AND DID NOT NEED TO.** No payload, no lesson and no bank moved.
The eight standing controls are verified as of S175 — do not re-prove them unless the
toolchain or a payload has moved.

**S176 TOUCHED NO LESSON, NO BANK AND NO PAYLOAD.** One instrument, one document, one
generated file: `gate_payload_match` → **v1.9.0**, `ZUMO_SUPER_BIBLE.md` → **v8.169**
(§16.45 NEW, seated with a numbered body), `GPT_WORKLIST.md` regenerated (stamp line only).

---

# 1. THE ONE-DIRECTIONALITY IS CLOSED, AND THE DEFECT WAS WORSE THAN THE HANDOFF SAID

S173 recorded it as *a ruling, then a design*, with a reproduction. The reproduction was run
first and it under-stated the case.

Deleting **one** executable line — the S172 kill-switch guard
`if (turnDegreesGyro(90.0 * sweepDir) == STOP_KILL) break;` — from
`13/challenge_9_1_keep_sweeping`, leaving `Lesson_13.html` untouched, left the gate printing
**PASS with the advisory count unmoved at 635.** Not one number changed. **The gate could not
see the removal of the thing S172 shipped.**

**RULED A DEFECT CLASS, NOT A STATED SCOPE LIMIT.** A stated limit is a shape a gate declines
to reach; this was a gate passing on a corruption of the artefact it exists to certify.

**THE SYMMETRIC PREDICATE WAS REJECTED, NOT OVERLOOKED (rule 20).** *Every lesson line appears
in some payload* convicts wrong-code examples, "before" versions and the Serial-cut demos —
noise on day one, and an arm that noisy is one somebody switches off.

**WHAT SHIPPED: `PAYLOAD_CENSUS`, 216 pins, `[count, md5]` over stripped executable lines**,
DERIVED with `--update-census` and never typed. Count AND hash, because a count alone lets a
loss in one file cancel against a gain in a sibling file of the same payload (rule 79's shape).
It reads the WHOLE registry, not the lessons passed in.

---

# 2. TEN CONTROLS, AND CONTROL 4 CORRECTED THE AUTHOR

**TWO controls are the arm's whole reason to exist, because derivation PASSES on both:**
a **DELETED** executable line, and **two executable lines REORDERED** — the second found only
because a control was written for it, at zero other failures.

| shape | derivation | census |
|---|---|---|
| delete a line | **PASS** | **FIRES** |
| reorder two lines | **PASS** | **FIRES** |
| add a line | FAIL | FIRES |
| change a value | FAIL | FIRES |
| reword a trailing comment | FAIL | FIRES |
| reindent | PASS | **SILENT** |

**CONTROL 4 DISAGREED WITH THE PREDICTION AND THE PREDICTION WAS WRONG.** It was written
expecting SILENCE on a comment reword, from a probe that counted LINES only. A **trailing**
comment is part of the stripped executable line and is not excluded by the comment rule, so the
md5 sees it. **The prediction had already been published in the code comment; the comment was
corrected to match the artefact rather than the control re-aimed to match the comment.**

Three controls hold the pin itself: an **EMPTIED** table fires rather than passing on no truth ·
an **ORPHAN** pin fires (S138's shape) · a pin whose **COUNT is corrupted while its md5 stays
correct** fires, proving both fields are asserted and not just one.

**STATED SCOPE LIMIT (rule 78): a pin asserts content has not MOVED since a human blessed it,
never that it is CORRECT.** A payload that shipped wrong and was pinned wrong stays wrong,
silently. `BOXED_FP` carries the identical limit. Declared, not hidden.

**MAINTENANCE COST, MEASURED NOT FEARED:** every edit that moves executable content already
requires a paired lesson edit to keep derivation green, so the census adds **no new obligation
except on deletion and reordering** — the two events it exists to catch. Reindentation, the one
genuinely free edit today, stays free.

---

# 3. S175's COUPLING FIRED AGAIN, ON SCHEDULE

`build_worklist --check` was GREEN at session open and RED immediately after the Bible bump,
exactly as S175 predicted. **Measured rather than feared: the entire diff is the stamp line**,
S175 → S176, with 38 files needing a human and 9 local-fix findings across 5 files UNCHANGED.

**The close-ritual item works. Keep it: after any Bible session bump, regenerate
`GPT_WORKLIST.md`.**

---

# 3b. S177's ONLY JOB: THE GPT LIST. DJ RULED IT.

**DJ: *"I can't ship a book with errors in it"* and *"I want the book so it has no known errors."***
**Do not open instrument work. The list is the assignment.**

**THE 245-ROW REVIEW HAD NEVER BEEN WORKED AS A LIST.** 167 rows are in Fall scope (L01-L13);
**only 6 are named by ID anywhere in the Bible or LIVE.md**, and 19 more were closed wholesale
when S159/S160/S161-162 shipped the C6/C2/C1 classes. **~15% closed. 161 never looked at.**
The file records CLOSED/DONE/FIXED/SHIPPED **zero** times — it is stale as well as unadjudicated.

**A MECHANICAL FIRST CUT SPLIT THEM, AND IT IS CONTROLLED.** Each row is matched on its own
quoted string against the live lesson text (tags stripped, entities decoded, quotes normalised).
**CONTROL: L06-02 and L11-03, both fixed at S161 and S160, both correctly read DEAD.**

| bucket | n | meaning |
|---|---|---|
| quote GONE, no 4-word fragment survives | **48** | strong evidence already fixed |
| quote gone BUT fragments survive | 45 | ambiguous — paraphrase or partial edit |
| **quote STILL VERBATIM in the live lesson** | **17** | **work these first** |
| no checkable quote | 63 | needs a human read |

**THE 17:** `L01-01` `L01-12` `L02-01` `L02-08` `L03-03` `L05-01` `L06-03` `L08-05` `L09-07`
`L09-13` `L10-06` `L12-05` `L12-09` `L12-17` `L13-06` `L13-08` `L13-10`

**THREE ARE VERIFIED AND NONE IS FIXED. NO LESSON WAS EDITED AT S176.**

**L01-01 — P0, DAY ONE, AND IT IS A HARDWARE FACT WITH A PRIMARY SOURCE.** L01 §6 *Break It On
Purpose* tells the student to switch robot power OFF, click Upload, and watch it fail.
**It will SUCCEED.** Pololu 0J63 §3.8: *when the Zumo 32U4 is connected via USB it receives 5 V
logic power even when the power switch is off ... useful if you want to upload or test a program
without drawing power from the batteries and without operating the motors.* The first
prove-it-yourself exercise in the book disproves the book. Two troubleshooting rows carry the same
premise (*Make sure robot power is ON*; *Upload fails -> robot not connected / powered*), and L03's
Part 2 prerequisite repeats it.

**THE REPLACEMENT IS RULED AND IT IS NOT GPT'S.** GPT proposed an invalid `board =` id. **Rejected
on two grounds:** it fails at BUILD, not upload, so the section stops being about its own subject;
and it has the student edit `platformio.ini` and restore it — **twelve students editing a config
file on day one, and the ones who restore it wrong are a support burden all term.**
**RULED: UNPLUG THE USB CABLE.** A genuine upload failure, no file edit, no persistent state,
and it is the error the book's own troubleshooting table lists first.
**BENCH ITEM, AND IT CANNOT BE CLOSED IN THE CONTAINER: PlatformIO IS NOT INSTALLED** —
`pio_harness.sh` is a misnomer and runs raw `avr-gcc`/`avr-g++`. **Someone with a robot must read
the actual error text once** before either version ships.

**L02-08 — CONFIRMED.** §4 says *"Lesson 1 used one button, one light, and the screen."* L01 calls
`playFrequency` **18** times, references `buzzer` **28** times and calls `setSpeeds` **20** times.
The continuity sentence is false.

**L03-03 — CONFIRMED PRESENT.** Part 2 still lists *"Your Zumo_Lesson_2 project folder (we'll copy
it)"*, one occurrence, against a §5.1/§6 that use the Maker for a fresh project.

**METHOD FOR S177:** verify the remaining 14 against the tree before touching anything (GPT is a
good LOCATOR and an unreliable DIAGNOSTICIAN — of ~11 findings ever checked, roughly 3 in 4 held,
and the misses were *right place, wrong diagnosis*). Then apply every confirmed fix in ONE arc with
a single gate run at the close. **Do not fix a lesson before its finding is verified.**

---

# 3c. LESSON 1 IS FULLY TRIAGED — 5 DEAD, 7 CONFIRMED LIVE, 3 CARDS LEFT

**DJ RULED THE ARC (S176): *"Get lesson one rewritten and zero errors and i'll bench test all of
it."*** All fifteen L01 findings were worked. **Nothing was edited — no lesson file changed at
S176.** Open into the edit pass.

## DEAD — verified by ABSENCE in the live file, not by assumption

| ID | evidence |
|---|---|
| `L01-02` | *"brain of your Zumo"* and `term-a-star` ids — **0 hits**. Fixed S162/S163. |
| `L01-10` | *"controller board"* — **0 hits**. Fixed S163. |
| `L01-13` | `PlatformIO/Projects` — **0 hits**; both path sites agree at `Documents/PlatformIO`. |
| `L01-14` | 19 figure tags in the body, all indexed; **gate 73 passes**. Closed by §10. |
| `L01-15` | stale strip titles — **0 hits**. Fixed S150 by gate 71. |

## CONFIRMED LIVE — quoted text present verbatim. Seven fixes, and two need care.

**`L01-01` — P0, DAY ONE. THE REPLACEMENT IS RULED AND IT IS NOT GPT'S.** §6 *Break It On Purpose*
says switch power OFF, Upload, watch it fail. **It SUCCEEDS.** Pololu 0J63 §3.8: USB supplies 5 V
logic power *even when the power switch is off ... useful if you want to upload or test a program
without drawing power from the batteries and without operating the motors.* **RULED: UNPLUG THE
USB CABLE** — a real UPLOAD failure (GPT's bad `board =` id fails at BUILD, so the section stops
being about its own subject), no file edit, **no persistent state** (GPT's version has twelve
students editing `platformio.ini` on day one and the bad restores are a term-long support load).
**Two troubleshooting rows carry the same false premise** (*Make sure robot power is ON*;
*Upload fails -> robot not connected / powered*) and **L03 Part 2's prerequisite repeats it**
(*Robot connected via USB with power ON*) — fix all four sites or the lesson still contradicts
itself. **BENCH, CANNOT BE CLOSED IN THE CONTAINER: PlatformIO IS NOT INSTALLED**, and
`pio_harness.sh` is a misnomer running raw `avr-gcc`/`avr-g++`. DJ reads the real error text once.

**`L01-03` — INSTRUCTION CORRECT, REASON FALSE. DJ SETTLED THE MECHANISM (S176).** §4.2 says
*"Git is a tool that PlatformIO uses behind the scenes to download robot libraries."* **False** —
`lib_deps = pololu/Zumo32U4@2.0.1` is a PlatformIO **Registry** package over HTTPS, not a git
clone. **But the STEP MUST STAY:** on macOS `git` ships inside Apple's **Xcode Command Line
Tools**, and running `git` on a fresh Mac triggers the *Install Command Line Developer Tools*
dialog; that package supplies `clang`/`make` and is what PlatformIO actually needs. DJ: *"It
fails ... it's not github that makes it work, but something that github installs."* **GPT's
implied fix — drop the Git step — would have broken every Mac in the room.** Rewrite the SENTENCE
to name the Command Line Tools. **Third occurrence this session of GPT being right about the
place and wrong about the diagnosis.**

**`L01-07`** — *"Today your program touches exactly three things"* (Button A, OLED, yellow LED).
The Lesson 1 program also drives the motors and plays a jingle: `setSpeeds` **20**, `buzzer` **28**,
`playFrequency` **18**. At least five. **Reword; do not enlarge the table** (S154).

**`L01-08`** — *"B had no `printf`"*. False; B's documentation contains `printf`. The early
example used `putchar()` because of B's character constants. Figure caption also says K&R
*introduced* Hello World while the prose credits the earlier B tutorial -> **"popularized"**.

**`L01-09`** — *"you are exactly copying the very first programmers in history"*. Programming
predates 1972 by decades.

**`L01-11`** — *"That feedback loop is what separates a robot from an appliance"*. A thermostat is
closed-loop. Related: the toaster row's *"can't really decide"*. GPT's replacement sets up
P-control better than the original.

**`L01-12`** — *"You should hear a USB connection sound"* is Windows-only. Add the Mac form
(*Allow accessory to connect?*). **Pairs with L01-03: §4 is platform-blind in BOTH directions.**

## STILL OPEN — three challenge cards, no external facts needed

`L01-04` Challenge 9 removes the startup wait and puts a **tethered** robot on the floor with no
unplug instruction (GPT's floor-test ritual is worth making a reusable convention) ·
`L01-05` Challenge 4's solution says BOTH directions become 700 where the prompt changes only the
FIRST `delay(350)` — actual behaviour is 2x forward, 1/2 back · `L01-06` Challenge 11 hint says low
~ 4200 mV while the solution tests `< 4500`, and the scaffold promises a screen print. **Read each
card against its own reveal before writing anything.**

## THE EDIT PASS

Read the three cards, then apply all ten fixes in **ONE arc**: L01 moderate bump (both §5b homes —
§6's exercise is structure), the §27.8b CSS restore->regenerate->apply cycle, one full 78-gate run,
`gate_payload_match`, and `quiz_bank` — **`ZUMO_QUIZ_L01` pins `lesson_01` and grades §5.0 and the
A-Star distinction, so check it against every changed sentence before closing** (the S165 shape: a
bank grading a figure its lesson stopped printing). **L03 moves too** for the power-ON prerequisite.

---

# 4. S177 OPENS HERE

- **A GATE FOR `GPT_WORKLIST.md` IS STILL OWED AND STILL PRICED, NOT SHIPPED** (S174). `--check`
  closes what a session ritual can reach; a gate costs an `svg_layout_audit` pass over every SVG
  on **every** `book_gates` run, and **an arm that made the routine slower is one somebody
  eventually skips**. If it ships, it likely belongs behind the same door ARM 9 uses.
- **`gate_payload_match` IS STILL NOT ONE OF THE 78** — nothing in `book_gates` runs it, which is
  the S137 defect that once let it go PASS → FAIL inside a push while the handoff claimed PASS.
  The new census arm inherits that exposure. **Priced, not shipped:** it needs the Maker parsed on
  every suite run. Recorded here so it is not rediscovered.
- **EIGHT INSTRUMENTS DIE ON AN UNRECOGNIZED ARGUMENT WITH A RAW TRACEBACK** —
  `build_mark_index`, `gate_payload_match`, `pill_sweep`, `extract_project`, `fit_raster_svg`,
  `flatten_alpha`, `gen_component`, `glyph_scan`. **Ugly and SAFE: none of them writes.**
  Cosmetic, not owed. (`gate_payload_match` takes ARGUMENTS:
  `python3 gate_payload_match.py newproject.html lessons/Lesson_*.html`; it also now takes
  `--update-census`.)
- **S167's DEBT IS CLOSED AND MUST NOT BE RE-OPENED** (Bible §16.43).
- **ARM 7's two remaining false skips** are stated blind spots, not bugs.
- **`byte_audit` ARM 2 STILL CANNOT SEE A FIGURE IN PROSE**, and nothing here reads a sentence.
- **L16 STILL NEVER STATES ITS MATCH-MODE FIGURE** (S166).
- **`strip_inline --restore` DOES NOT RESPECT THE HELD LESSON STRIP** (S168). SCRATCH-COPY works.
- **GATE 77 DOES NOT EXCLUDE `<pre>`** (S165). When it first fires, the answer is a ruling.
- **§16.32–§16.44 STILL HAVE NO NUMBERED BODIES** — the debt v8.153 recorded. §16.45 was seated
  rather than added to that queue; the other thirteen remain changelog-only.
- **THE REMAINING GPT WORKLIST** — 245 findings, most unadjudicated. Two of its SVG entries
  became newly visible at S174's regeneration.
- **L13/L14 bank pin arcs — LIKELY ALREADY CLOSED, STRUCK AT S176.** `UNREAD_PINS` is 0 and
  gate §24.18 passes, so no bank carries a stale pin; S172 recorded those figures as living in
  `#` header comments, which §16.37 rules is history. It was carried forward unchecked from the
  prior handoff — rule 72's own shape. Verify once, then delete.
- L12 BONUS B4's bench measurement · L15 Challenge 3's
  `turnDegreesGyroSafe()` · L03 queued content · `ZUMO_L03_TEMPLATES.md` staging ·
  Bible §14 TDP-canon entry · day-by-day grid + syllabus.
- **The poster is a GRADED deliverable** (DJ, S159). **Photography is OFF the critical path**
  (S156).
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

**STANDING CONTROLS, ALL REPRODUCED S175, UNTOUCHED BY S176:**
`11/after_step_1` **20,592** · `11/finished` **20,778** · `12/finished` **24,790** ·
`12/c2_slipalarm` **21,334** · `13/finished` **25,248** · `14/finished` **26,002** ·
`15/finished` **28,406** · `16/finished` **28,626**.

**216 payloads, FOUR declared overflows** — `16/after_step_3` **29,008** · `16/after_step_4`
**29,644** · `16/step_5_serial_traded` **28,944** · `16/step_5_zn_traded` **28,788**.

**THE TIGHTEST PASSING BUILD IS `16/after_step_2` AT 28,648, WITH 24 BYTES SPARE.**

**ARM 9: 15 discards over 7 of 105 payloads, 7 adjudicated, 0 unexplained.**

---

# STANDING AUTHORITY — §24.17 AND §24.19

**Decide and report; do not ask.** Three carve-outs: facts about the ROOM no instrument can see;
moves that are irreversible or expensive to undo; and RoboLore brand and course scope.
**Delegation removes the question, never the disclosure.**

**§24.19 IS THE TIEBREAKER** — what is best for student learning, when nothing else discriminates.

---
<!-- VERSION BLOCK: emitted by session_versions.py --handoff. Never hand-typed. -->
Fresh-clone verified at **`ad72a35`**. Census **40,993**.
Bible **v8.169** · `BookComponentStandard` **v01.13.0** · Maker **v2.62** ·
`marks/` **41** · `icons/` **49** incl. LICENSE.
`ZUMO_Syllabus_WORKING.md` **v1.3**.

Instruments: `book_gates` **v1.72.7** · `lesson_inventory` **v1.3.5** ·
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

Lessons: L01 v03.30.1 · L02 v03.21.5 · L03 v03.43.2 · L04 v04.29.2 · L05 v04.29.1 · L06 v04.32.4 · L07 v04.31.5 · L08 v04.32.1 · L09 v05.27.4 · L10 v02.30.3 · L11 v02.31.1 · L12 v01.33.1 · L13 v02.35.0 · L14 v02.36.0 · L15 v02.32.0 · L16 v02.28.0.
