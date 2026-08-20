# ZUMO — S180 HANDOFF (written at S179 close · paste at top of Session 180)

## READ THIS FIRST

**S179's work IS PUSHABLE and DJ verifies the push himself (standing ruling, S158).**
`git rm ZUMO_S179_HANDOFF.md` is part of that push, and **`ZUMO_FLAGGED_CHECKS.md` is a NEW
file** — a new file is a separate checkbox in GitHub Desktop and is frequently missed.
**`ZUMO_S110_SHOT_BRIEF_WEEK1.md` is in this push too** — a photography document, easy to
skip past. **If `__pycache__/` exists in your tree, delete it LAST** — it regenerates on every gate run.

**78/78 gates** · `gate_payload_match` **PASS** · `quiz_bank` 16 banks at **1,246** questions ·
`build_css --check` current · `build_worklist --check` current **after regeneration** ·
`image_audit --check` current · `callout_id` **1127/0** · `next_pointer` clean ·
census **41,010**.

**`site_parity` RAN TWICE AT S179 OPEN AND WAS PARITY BOTH TIMES**, which closes S178's owed
item. The tree now differs from the published site by design again. **Run it at least twice
AFTER this push, tree untouched between runs, and believe the repeat (§16.42).**

**`byte_audit` DID NOT RUN AND DID NOT NEED TO.** No payload moved. The Maker changed by ONE
STRING in a display hint — not a payload — so no compiled figure can have moved. The eight
standing controls are verified as of S175.

**§27.8b's CYCLE WAS NOT OWED, AND THE SCRATCH-COPY CONTROL SAYS SO RATHER THAN A GUESS.**
Regenerated in a COPY of the tree and compared name by name: **574 rules both ends, ZERO names
added, dropped or repointed, and the two files are md5-IDENTICAL.** Third session running that
this check costs one copy and one diff and answers the question the cycle exists to guard.

**SEVEN LESSONS, TWENTY-ONE BANK BUMPS, THE MAKER, ONE SVG, TWO NEW BIBLE SECTIONS AND A NEW
DOCUMENT.** Census 41,006 → 41,010: the +4 is L03's added Step 3 paragraph and checklist item.

---

# 1. DJ RULED THREE ROOM FACTS AND ALL THREE ARE NOW CANON, NOT QUEUE ITEMS

**This is the session's most durable output. Each of these had been re-asked across three or
more sessions because it lived in a bench tracker or a worklist row instead of in the Bible.**

## §16.48 — GIT ON A MAC, AND POWER AT UPLOAD (Bible v8.172)

**1. Git is required on a Mac because it installs Apple's XCODE COMMAND LINE TOOLS — the
software most students are missing (DJ, S179).** Typing `git --version` triggers the *Install
Command Line Developer Tools* dialog, and that package carries the compiler. **The Git step is
the Xcode-toolchain step wearing Git's name**, and the book now says so, because the failure
from skipping it arrives later as a build error in a lesson about something else.

**The reason is load-bearing and the section records why.** GPT was RIGHT that
`lib_deps = pololu/Zumo32U4@2.0.1` is a Registry package over HTTPS and not a git fetch — and
its implied fix, *drop the step*, **would have broken every Mac in the room.** That is why S177
rekeyed `L01_B37` instead of deleting the step. **A true observation about a stated reason is
not a licence to delete the step the reason was attached to.**

**Closes `L01-03`, open since S137, and bench row `L01-B9`.**

**2. You do not have to switch the robot on to upload.** The cable powers the chip and display;
the switch feeds the motors. Pololu 0J63 §3.8 and L01's own WARNING 1.46. **Closes `L01-B2`.**

## §16.49 — `Documents/PlatformIO/Projects/<FolderName>` (Bible v8.173)

**DJ ruled the path. S178 had fixed L01 only, and the ruling is book-wide.** L02 said
`ZUMO_Template` lived in `Documents/PlatformIO` while L01 said `Documents/PlatformIO/Projects`
— **two lessons naming different homes for one folder, in week 1.**

**THE POPULATION WAS MEASURED TWICE AND THE FIRST MEASUREMENT WAS SHORT.** Scoped to the
lessons it returned ELEVEN; scoped to the whole tree it is **FOURTEEN** — ten lesson prose
sites, the Maker's unzip hint, **two present-tense canon lines in §11 of the Bible itself**, and
the root label inside an SVG. §24.6c: a predicate built from where you already found the defect
measures only where you already looked. Provenance left alone (rule 37).

### THE SVG WAS PRICED AS EXPENSIVE AND IT WAS NOT — READ §16.49

S179 opened expecting a graphics-chat pass, because `L02-06` was parked at S178 close for
exactly that shape. **Read, `L02_GRAPHIC_2-09_folder_structure.svg` is live text, 6 KB, and the
path is a SINGLE `<text>` node.** The only real cost was layout: 29 Courier characters at 33 px
run x=174→748 against a panel edge at 726, so `mono-root` drops to 30 px.

**CONTROLLED RATHER THAN ASSERTED:** at 33 px `svg_layout_audit` reports the overflow and names
**748 against 726**; at 30 px it is clean. The instrument that blesses the shipped file
demonstrably fires on the failure mode (rule 59).

**THE REUSABLE HALF: *coupled to an SVG* IS NOT A COST, IT IS A CATEGORY.** `L02-06` needs an
eighth BAND drawn and stays parked. This needed a longer word. **Price the artefact, not the
category it belongs to (rule 70).**

**Zero stale path sites remain anywhere in the tree.**

---

# 2. LESSON 1 IS DONE EXCEPT FOR THREE THINGS ON A FLOOR

**All fifteen GPT rows are shipped, dead, or ruled.** The last content defect was found at S179
by READING, past a green gate.

## §8's COMMON PITFALLS EQUATED THE BUILD TARGET WITH THE BOARD, AND GATE 76 IS BLIND TO IT

It read *verify you're targeting the **A-Star 32U4 / Zumo 32U4***. **That slash is the exact
conflation §16.25 retired.** Gate 76 passes because it forbids the retired SLOGAN, not the
slash-equation — so S178's handoff claim that all six surviving `A-Star` mentions are the
legitimate build target was **true of five** (§24.8). Rewritten to name `board = a-star32U4` and
say plainly it is not a second name for the board.

**AND THE BANK WAS RIGHT WHILE THE LESSON CONTRADICTED IT — THIRD TIME IN THREE SESSIONS.**
`L01_B14` cites *§5.0 and §8*, keys the build-profile answer, and carries *"it names the exact
board you are holding"* as its declared trap with a `why` reading *this is the trap*. **The old
§8 line corroborated the trap** — a student who read §8 found evidence for the wrong answer.

## DJ ANSWERED THE `platformio.ini` QUESTION DIRECTLY: THE INI IS CORRECT AND STAYS

There is no `zumo32U4` board in PlatformIO. `a-star32U4` is the profile matching this
ATmega32U4 and bootloader. **The defect was never the ini. It was one sentence.**

## `ZUMO_FLAGGED_CHECKS.md` IS NEW, AND IT IS ALL L01 OWES

DJ asked for a short list he will run himself, separate from the 51-row tracker. Three rows:
**F1** the unplugged-upload error string verbatim · **F2** Challenge 4 on the floor · **F3**
Challenge 11's solution as printed, is the number readable before setup overwrites it.

**`ZUMO_BENCH_TESTS.md` stays the complete tracker** and now shows `L01-B1/B3/B4` as ROUTED and
`L01-B2`/`L01-B9` as **CLOSED — DJ ruled S179**, each carrying the ruling itself rather than a
pointer to it.

---

# 3. LESSON 3's ARC — ELEVEN EDITS, AND ONE OF THEM CORRECTED THIS SESSION'S OWN VERDICT

`Lesson_03.html` **v03.43.2 → v03.44.3**.

## THE FIRST BATCH — THE THREE ITEMS S179 INHERITED

`L03-03` (Part 2 still said to copy the Lesson 2 project folder, against a §5.1/§6 that use the
Maker) · `L03-04` (§4.1's *this lesson introduces motor control* — L01 drove it, L02's Warm-Up 4
spun it; `L01-07` and `L02-08`'s third twin) · the untagged S177 finding (Part 2 asked for the
robot TETHERED **and** 6+ feet of floor at once; now L01's floor test, in order).

## STEPS 2–4 WERE ONE COUPLED DEFECT, NOT TWO

- **Step 2's checkpoint claimed the file held *nothing else***, when the Maker's blank starter
  also ships `#include <Zumo32U4.h>` and the MY PLAN block — **and Step 4 DEPENDS on that
  include** (*"right after the include"*). Read from `mainCpp()`, not assumed.
- **Step 3 told the student to paste a SECOND header** into a file the Maker had already headed,
  and to replace `[Your Name]`/`[Today's Date]` placeholders **the Maker fills with real
  values**. Reframed: the printed block is the TARGET SHAPE, they expand the Maker's blank
  `WHAT THIS PROGRAM DOES:` line into it, and a new checkbox reads *exactly one header block in
  the file — not two*.
- **Step 4's checkpoint denied the `setup()`/`loop()` Step 2 had just told them to keep** — one
  callout above a CHECKPOINT that builds green.

## `L03-06`, `L03-08`, `L03-09` — AND THE LESSON CONVICTED THE LAST ONE ITSELF

§4.5's drift test claimed an unpowered push *predicts which motor is stronger*; it measures
rolling resistance, and is now a hypothesis §7 settles. The **30-second full-speed cooldown
rule** had no pedigree and is replaced by the current-under-load mechanism. The **±10% figure on
`readBatteryMillivolts()`** is gone — **§3.6's own 5400/4800/4200 bands would be unusable if it
were true.**

**`L03_B35` WAS FALSIFIED BY A CORRECT EDIT.** Its keyed answer WAS the ±10% figure, authored
faithfully from a lesson that was wrong. §16.47's session found the same shape in `L02_B05`.
Rekeyed, with the load-sag point moved into a distractor rationale.

## DJ RULED THE SIX FEET OUT — AND THE FOURTH SITE WAS A DIFFERENT DEFECT

**DJ, S179: the curve test stays ON THE FLOOR; students just do not need 6+ feet.** Four sites
DELETED rather than corrected (rule 50): both prerequisite lists, §4.4's *at least 6 feet in
driving direction*, and **§4.5's *a 6-foot test run makes drift very obvious*** — which does not
describe the ROOM, it describes the RUN, and the run is `TEST_DURATION` 2000 ms at `BASE_SPEED`
200. **A two-second run at half speed is nothing like six feet; the lesson was overstating its
own test.**

**CORROBORATION THAT THE FIGURE WAS THE OUTLIER:** L06 asks for *~1 meter*, L07 for *a meter*,
L10 for *30 cm*. **The lesson demanding the most floor had the shortest run in it.**

Final wording is DJ's: *Find some clear space on the floor to test on.*

## THE RISER IS ALREADY WHERE DJ SAID IT SHOULD BE — CONFIRMED, NOT RE-ADDED

DJ: *the riser is for when they run it and it starts on its own.* **L01 Challenge 9, *The
Vanishing Wait*, already carries it in full** — *prop the robot up first, chassis on a box or an
overturned cup, tracks free in the air… there is no button press in between. It will not wait
for you to be ready.* Shipped at S177 as `L01-04`. L03 §4.4's riser Coach's Tip is scoped the
same way. **Nothing was owed.**


## THE SHOT BRIEF WAS STILL STAGING SIX FEET, AND IT IS OUTSIDE EVERY GATE

**`ZUMO_S110_SHOT_BRIEF_WEEK1.md` v1.0 → v1.2.** The whole-tree sweep at S179 close found the
deleted figure alive in a live instruction: *Rig once: smooth floor, **6+ feet clear**…* and
*Show the **full 6 feet***, staging `IMAGE 3.2` — L03 §4.4's still-unshot *recommended motor
testing setup*. **A photo taken to that brief would have put the deleted figure back into the
book as a picture, and nothing in this repo reads inside an image** (S171's stale wall, arriving
before the wall is built rather than after). Amended, with the reason stated in place so nobody
restores it, and the figure's caption question changed from *how much floor do I need to clear?*
to *what does a clear test lane look like?*

**IT WAS OUTSIDE EVERY GATE AND EVERY EARLIER SCOPE.** The S179 path and figure sweeps covered
lessons, banks, the Maker and the Bible; the photography documents are in none of those. **A
document that instructs a human is as capable of carrying a retired figure as one that instructs
a compiler**, and this repo gates the second kind only.

**A FREE FINDING THE EDIT PRODUCED:** the brief claimed *a figure saved under any other name
reads as no asset*. **Tested against `image_audit.expected()` rather than read: only the PREFIX
is load-bearing** — `L03_IMAGE_3-02_testing_setup_floor` and
`L03_IMAGE_3-02_recommended_motor_testing_setup_sh` BOTH match, which is why this brief and
`IMAGE_SHOT_LIST.md` can name different slugs for one shot without either being wrong. What the
matcher really rejects is an unpadded lesson number, the wrong kind, and a name with no slug at
all. The old sentence was stricter than the instrument. Corrected in v1.2.

---

# 4. A DEAD/LIVE PROBE MANUFACTURED A FALSE DEAD, AND THE RECOMMENDATION WAS WITHDRAWN IN THE SAME SESSION

**READ THIS BEFORE RUNNING ANY MECHANICAL PASS OVER THE 48-ROW DEAD BUCKET.**

`L03-01` was reported DEAD on a grep for `no setup()/loop() exists`. The file writes
`no <code>setup()</code>/<code>loop()</code> exists`, which strips to **spaces around the
slash**. The verdict came from the probe's spacing, not from the tree.

**A false DEAD is invisible, because nobody re-checks a retired row.** The proposal to run a
mechanical exact-quote pass over the 48 rows was made and withdrawn inside one session. **Any
such pass needs a probe that normalises inline-code markup first and fails loud rather than
quiet.**

`L03-05` stays dead because an INSTRUMENT says so: gate §16.31 forbids the retired C1 wording
book-wide and passes. **That is the difference between a dead row and a row a grep missed.**

---

# 5. `ZUMO_GPT_REVIEW_WORKLIST.md` v1.3 — PART 0, CLOSED ROWS

**DJ ruled: mark closed rows, do not delete them.** Rows below Part 0 stay verbatim as GPT wrote
them, so a row's presence in this file means nothing on its own — **Part 0 is what says whether
it is still live.** The header now leads with *read Part 0 first*.

**36 rows closed, 2 parked with reasons.** Each carries HOW it closed, not just that it did — so
`L03-01` records that it was first reported DEAD in error, and `L03-05` records that a gate says
so rather than a grep. **`L02-04` and `L02-05` are in there marked ALREADY DEAD with the note
that they are why Part 0 exists.**

The parked table gives `L02-06` and `L02-09` their reasons in full, **including the band-vs-label
distinction §16.49 established**, so nobody re-opens them looking for a one-string fix.

---

# 6. S180 OPENS HERE

## THE GPT LIST IS STILL THE ASSIGNMENT. DJ: *"I can't ship a book with errors in it."*

**L01, L02 and L03 are done.** The still-verbatim rows are:

`L05-01` `L06-03` `L08-05` `L09-07` `L09-13` `L10-06` `L12-05` `L12-09` `L12-17`
`L13-06` `L13-08` `L13-10`

**Verify each against the tree BEFORE editing — and normalise inline-code markup in the probe.**

**THE OTHER BUCKETS:** 48 rows whose quote is GONE (a mechanical pass would close them cheaply
IF the probe is fixed first — see §4 above) · 45 ambiguous · 63 with no checkable quote.

## BENCH — TWO FILES NOW, AND THEY ARE NOT INTERCHANGEABLE

`ZUMO_FLAGGED_CHECKS.md` is DJ's short list (F1–F3, all L01). `ZUMO_BENCH_TESTS.md` is the
complete tracker. **A row leaves the flagged file when its Result is written; the tracker keeps
the record.** Oldest open item is `L09-B1`, carried since S41. Most consequential is `L10-B1` —
§16.12's perpendicular arrival, unruled since S143, with a falsifiable prediction.

**`L03-B3` is NEW:** Bonus Challenge 4 asks for *about 3 meters of clear floor and a catcher*,
and that figure has no pedigree either. Unlike the TRIM run this one really is full speed for
1.5 s each way, so it was RAISED rather than swept. The card already offers `delay(800)` as the
short-floor escape, so nothing is blocked.

---

## STANDING, UNCHANGED

- **A GATE FOR `GPT_WORKLIST.md` IS OWED AND PRICED, NOT SHIPPED** (S174).
- **`gate_payload_match` IS STILL NOT ONE OF THE 78** — the S137 exposure. It requires the
  `Lesson_NN_Topic_` filename pattern; use topic-suffixed symlinks to run it.
- **EIGHT INSTRUMENTS DIE ON AN UNRECOGNIZED ARGUMENT WITH A RAW TRACEBACK.** Ugly and SAFE.
- **S167's DEBT IS CLOSED AND MUST NOT BE RE-OPENED** (Bible §16.43).
- **`byte_audit` ARM 2 STILL CANNOT SEE A FIGURE IN PROSE.** **Eleven more prose defects shipped
  this session past 78 green gates** — §16.18 from the content side, THIRD session running.
- **L16 STILL NEVER STATES ITS MATCH-MODE FIGURE** (S166).
- **GATE 77 DOES NOT EXCLUDE `<pre>`** (S165). When it first fires, the answer is a ruling.
- **§16.32–§16.44 STILL HAVE NO NUMBERED BODIES** — thirteen remain changelog-only. §16.45
  through §16.49 were all seated rather than added to that queue.
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

**STANDING CONTROLS, ALL REPRODUCED S175, UNTOUCHED BY S176–S179:**
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

**S179 used carve-out 1 four times and every one paid** — the Mac toolchain, the power switch,
the project path, and the six feet. **All four are now canon rather than queue items, which is
the point of §16.48's closing rule: a ruled room fact belongs in the Bible, not in a tracker.**

**§24.19 IS THE TIEBREAKER** — what is best for student learning, when nothing else discriminates.

---
<!-- VERSION BLOCK: emitted by session_versions.py --handoff. Never hand-typed. -->
Fresh-clone verified at **`b1986ac`**. Census **41,010**.
Bible **v8.173** · `BookComponentStandard` **v01.13.0** · Maker **v2.63** ·
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

Lessons: L01 v03.31.3 · L02 v03.22.1 · L03 v03.44.3 · L04 v04.29.3 · L05 v04.29.2 · L06 v04.32.5 · L07 v04.31.6 · L08 v04.32.1 · L09 v05.27.4 · L10 v02.30.3 · L11 v02.31.1 · L12 v01.33.1 · L13 v02.35.0 · L14 v02.36.0 · L15 v02.32.0 · L16 v02.28.0.
