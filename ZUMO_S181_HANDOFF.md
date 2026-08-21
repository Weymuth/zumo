# ZUMO — S181 HANDOFF (written at S180 close · paste at top of Session 181)

## READ THIS FIRST

**S180's work IS PUSHABLE and DJ verifies the push himself (standing ruling, S158).**
`git rm ZUMO_S180_HANDOFF.md` is part of that push. **If `__pycache__/` exists in your tree,
delete it LAST** — it regenerates on every gate run.

**78/78 gates** · `gate_payload_match` **PASS** · `quiz_bank` 16 banks at **1,246** questions ·
`build_css --check` current · `build_worklist --check` current · `image_audit --check` current ·
`callout_id` **1132/0** · `next_pointer` clean · census **41,465**.

**THE HARNESS IS UP AND `byte_audit` RAN FOR THE FIRST TIME SINCE S175.** All eight standing
controls reproduced (20,592 first, rule 30). **221 payloads now, not 216.** `--check` PASS on
eight arms. **ARM 9 is 15 discards over 7 of 110, 7 adjudicated, 0 unexplained.**

**`site_parity` HAS NOT RUN THIS SESSION** and is owed after this push. Run it at least twice,
tree untouched between runs — **and read §16.42's amendment below before you believe a repeat.**

**S180 TOUCHED SEVENTEEN FILES.** `Lesson_02.html` **v03.24.1** · `Lesson_12.html` **v01.35.2** ·
`Lesson_13.html` **v02.38.0** · `newproject.html` **v2.64** · `book_gates` **v1.72.15** ·
`build_family_map` **v1.6.6.2** · `gate_payload_match` (census +5) · `css/book.css` ·
`ZUMO_BENCH_TESTS.md` **v1.2** · eight quiz banks.

---

# 1. LESSON 2 WAS NOT DONE, AND THE LEDGER DID NOT SAY SO

**S179's Part 0 ledger accounted for 14 of L02's 19 GPT rows. FIVE WERE NEVER RESOLVED AND
NEVER RECORDED AS OPEN.** That is a defect in the ledger I built: **silence reads as closed
unless you cross-check against the full list.** A row never ruled looks identical to a row
never mentioned. **S181 SHOULD FIX THE LEDGER'S SHAPE** — an OPEN section, or a rule that every
row appears exactly once somewhere.

Three shipped, two struck:

- **`L02-15`** — Challenge 2's battery screen. Shipped the release-wait.
- **`L02-13`** — *two objects for the same motor would fight over it* was a **rule with a fabled
  mechanism**. Replaced by the real cost: SRAM, and two names for one piece of hardware, *which
  is how you end up staring at a line that is working perfectly while the one that is wrong sits
  somewhere else.*
- **`L02-17`** — the MY PLAN block ships in every L02 payload and the lesson never named it.
  Now a prose section in §6, pointing at L07 where the plan becomes the student's own.
- **`L02-12`** STRUCK — the stack model is the right simplification; GPT's technically-correct
  alternative teaches a Lesson 2 student nothing.
- **`L02-19`** STRUCK — **L02 §9 says spiral markers start in the NEXT lesson, deliberately**,
  and Warm-Up 4 is a warm-up, not a challenge card. GPT could not see that ruling.

## AND I SHIPPED A FALSE MECHANISM INTO L02, WHICH LIVED ABOUT AN HOUR

`L02-15`'s prose claimed all three screens draw *in a single trip through `loop()`*. **I cloned
`pololu/pushbutton-arduino`, transcribed `PushbuttonStateMachine` exactly, and ran it:**

```
pass 1: A single=0  B single=0  ->  BATTERY
pass 2: A single=1  B single=1  ->  CONTROLS
pass 3: A single=0  B single=0  ->  BATTERY
```

**Two passes, not one.** A debounced press needs ~15 ms of stable-true and **the state machine
only advances WHEN POLLED**. Corrected — and the true mechanism is the better lesson, because it
is also why the fix works: *while the program is parked in the `while`, nothing is calling
`getSingleDebouncedPress()` at all. A press that begins and ends between two calls is a press the
library never sees.*

**`L02-B2` IS NOW A FALSIFIABLE PREDICTION, NOT A QUESTION** (`ZUMO_BENCH_TESTS.md` v1.2): with
the wait removed you should see ONE flash of the Controls screen, then the battery screen settle.
**If the flash does not appear, §9 C2's *Why it takes two trips and not one* is wrong and the
paragraph comes out.**

---

# 2. THE SPIRAL: MEASURED, AND THE INSTRUMENT I PROPOSED WOULD HAVE BEEN WRONG

**DJ's standing concern: *keep a close eye on the Saxon spiral so students use their time well
and do not waste it on things that do not teach them more or deeper.***

**THE POPULATION IS 172 PRACTICE UNITS, NOT 88.** My first count used `data-difficulty`, which
only graded challenge cards carry. Widened: 88 `challenge` + 35 `bonus-sabotage` + 21
`bonus-observation` + 12 `tryit` + 12 `bonus-practice` + 4 `warmup`. That reconciles the
worklist's *13 of 171 units*.

**THIRTEEN CARRY A SPIRAL MARKER. 7.6%.** L04, L05, L06, L12 and L15 have zero between them and
31 cards. §18.1 rules L01/L02 out by design; the rest is a stalled rollout.

## THE CODE CAN SEE WHAT THE MARKER CANNOT — AND IT SEES THE WRONG THING

Prototyped a symbol map: every unit's `<pre>` blocks name the functions it asks the student to
write, and the book knows where each was introduced. Three passes to get it clean (984 symbols
scanning whole lessons, including prose words like `floor(`; 344 restricted to `<pre>`; **261**
after filtering banner words and blanks).

**IT FLAGGED SEVEN CARDS AS *PRIOR-ONLY*. I READ FOUR OF THEM AND NOT ONE SHOULD BE CUT.**
`10.2` teaches a counter that survives loop passes plus a `case`-body brace gotcha; `10.6` builds
a second solution and argues for one; `14.2` uses `while(true)` as a design choice; `9.4` is
textbook retrieval that points at the student's own `RobotMotion.h`.

**"Uses no function introduced in its own lesson" is not "teaches nothing new."** New concepts
are frequently not function calls. **The map is a good RETRIEVAL detector and a bad REPETITION
detector**, and its real yield is the **35 unmarked cards that lean on two or more prior lessons**.

## DJ'S RULING UNDER §24.19: THE 35-CARD MARKER ROLLOUT IS NOT WHAT IS BEST FOR STUDENTS

**A marker naming its source lesson converts retrieval into lookup.** The two cards that do this
well use no banner at all — `9.4` points at the student's own file, `10.2` weaves it into the
reasoning. **35 banners across 88 cards would kill the salience of the 13.** And the marker
serves the AUTHOR, not the student; the map already gives DJ that as a report with no file
changed. **The spiral map stays author-side.**

---

# 3. L12 AND L13 WENT FROM 7 PRACTICE UNITS TO 10 — LEVEL WITH THE MIDDLE OF THE BOOK

They were the thinnest **in-scope** lessons and the ones students reach last before September 8.
(L16 has zero units of any kind, but L16 is out of scope for fall.)

**SIX NEW CHALLENGES, EACH WITH A MAKER BUILD.**

| card | kind | flash | vs base |
|---|---|---|---|
| 12.4 The Short Way Round | `c4_shortway` | 20,968 | +22 |
| 12.5 The Square That Closes | `c5_square` | 21,742 | +774 |
| 12.6 How Long Is Your Gyro Good For? | `c6_driftmeter` | 20,728 | — |
| 13.4 The Landmark That Was Not There | `c4_landmark` | **25,248** | **+0** |
| 13.5 Log the Strip Going Under | `c5_striplog` | 25,366 | +118 |
| 13.6 How Wide Does It Actually See? | `cal_7a` (existing) | — | no build needed |

**`c4_landmark` COSTS ZERO BYTES**, and the COMPILE CHECK says so: *the guard that stops the
robot announcing victims at bare walls is free.* Next to 12.5's +774 for a new capability, the
numbers teach the lesson themselves.

## 13.4 IS A REAL BUG, AND THE BOOK ALREADY KNEW

`SWEEPING_ZONE` runs `lastRowCm = lastLegCm;` unconditionally — but a row can end on
`MAX_ROW_CM` instead of the wall. True wall at 60, budget 90: a missed row writes 90, the next
row stops correctly at 60, and the victim test asks `60 < 90 - 15` → **true. A victim announced
at a bare wall.** §8's troubleshooting table lists that symptom and gives two causes, both about
wrong numbers. **This one is a good number written in the wrong place.**

**Step 6 STATES the hazard** (*the previous row actually reached a wall — if the prox missed,
`lastRowCm` is not a wall distance at all*) and **`L13_A17b` GRADES IT AS A DISTRACTOR.** The
lesson named it and walked past it. The card now says so: **an assumption you can test is a bug
you have chosen to keep.**

## 13.6 DOES NOT ADD PRACTICE — IT MAKES THREE EXISTING SENTENCES TRUE

`ROW_STEP_CM` is handed to the student as *Try 15 and work from there*, while **three summary
sentences claimed it came from the 7A table**: §7A's intro (*the blanks... come from this table
and nowhere else*), the Quick Reference (*all four filled from the 7A table*), and B3's reveal
(*sized in 7A so that adjacent rows' prox coverage overlaps*). **The 7A table measures prox
counts at 30/20/10 cm — forward distance. Nothing in the lesson measures lateral coverage.**
All three corrected; 13.6 takes the missing measurement.

**The lesson was careful AT the number and careless in the sentences ABOUT it — S166's finding
in a new place.**

## 13.5 WAS WEAK AND DJ CAUGHT IT

First draft was hand-rolling the robot over three surfaces reading two columns — **7A's activity
with one extra column.** Rewritten motors-ON: drive the line at speed, log both channels to
Serial, read the log after. **The Serial Monitor becomes a data logger because the OLED cannot
hold a stream at speed** — a genuinely new reason to reach for a tool used since Lesson 2.

---

# 4. FOUR DEFECTS IN THE MAKER WORK, EACH CAUGHT BY A DIFFERENT INSTRUMENT

**THIS IS THE SECTION TO READ BEFORE TOUCHING PAYLOADS AGAIN.**

**1. WRONG LESSON.** My extractor took the first `"finished"` payload containing `SWEEPING_ZONE`
and got **LESSON 15's build**. `gate_payload_match` failed with 321 unmatched lines naming L15's
PID constants. **NO BUILD-UP MARKER CAN IDENTIFY A LESSON IN THIS FILE** — measured: `silverDetected`
is in L13/14/15/16, `gyroSetup` in L12–L16, `blindDistanceCm` in L11–L16. **Only the key span
can**, and the Maker's lesson blocks are NOT in lesson order (L15 at 171,887; L13 at 1,738,935).
Each base is now controlled both ways: own marker present, next lesson's marker absent.

**2. CALL BEFORE DEFINITION.** `c5_square` defined `squareByHeading` above the `turnToHeading` it
calls — *not declared in this scope*. **That is L02 §3.1's Build 1, written into a payload four
hours after that section was corrected.** My static check said the ordering was fine and was
**worthless**: its prototype regex used `[^;]*`, which spans newlines, so every DEFINITION matched
as a prototype.

**3. THE FIX COMPILED AND WAS STILL WRONG.** `c5_square` came out **20,968 — byte-identical to
`c4_shortway`** — because `squareByHeading` was defined once and called ZERO times, and
`--gc-sections` stripped it. **The download would have run and never driven a square. No gate
would have spoken; only two equal figures did.**

**4. ARM 9 CAUGHT THE SQUARE DISCARDING A `StopReason`.** `driveDistance(SIDE_CM)` threw away its
return, so the square drove four sides with the kill switch dead. Guarded in template, reveal and
payload. **Then gate §24 caught the sentence I wrote about the guard**, which promised Lesson 13
closes `turnToHeading()`'s missing return value — **and Lesson 13 has no `turnToHeading` at all.**
Withdrawn.

**THE PATTERN, FIVE TIMES IN TWO SESSIONS: every probe defect was a predicate built to confirm
rather than to falsify, and every one was caught by an instrument or by a number being absurd —
never by re-reading.**

---

# 5. S181 OPENS HERE

## THE GPT LIST IS STILL THE ASSIGNMENT. DJ: *"I can't ship a book with errors in it."*

**L01, L02, L03, L12 and L13 have had a pass.** Still-verbatim rows:

`L05-01` `L06-03` `L08-05` `L09-07` `L09-13` `L10-06` `L12-05` `L12-09` `L12-17`
`L13-06` `L13-08` `L13-10`

**Verify each against the tree BEFORE editing, and normalise inline-code markup in the probe** —
S179's `L03-01` was reported DEAD by a grep that could not see
`no <code>setup()</code>/<code>loop()</code> exists`.

## OWED AND PRICED, NOT SHIPPED

- **`gate_payload_match` IS STILL NOT ONE OF THE 78** (S137). **This session is the strongest case
  yet:** `book_gates` passed 78/78 the entire time a wrong-lesson payload sat in the Maker.
  An arm that must be remembered is one somebody eventually skips.
- **`site_parity` NEEDS CACHE-BUSTING (S179).** §16.42 says *believe the repeat* — and at S179 the
  repeat was **wrong four times running** on a CDN-cached SVG. Only a cache-busted fetch settled
  it. **§16.42's stopping condition is wrong for a cache with a TTL**, and the Bible still tells
  the next reader to believe exactly what was wrong.
- **A GATE FOR `GPT_WORKLIST.md`** (S174).
- **`ZUMO_GPT_REVIEW_WORKLIST.md`'s Part 0 needs an OPEN section** — see §1 above.

## BENCH — TWO FILES, NOT INTERCHANGEABLE

`ZUMO_FLAGGED_CHECKS.md` is DJ's short list (F1–F3, all L01). `ZUMO_BENCH_TESTS.md` **v1.2** is
the complete tracker. Oldest open item `L09-B1` (S41); most consequential `L10-B1` (§16.12,
unruled since S143). **`L02-B2` and `L03-B1`/`L03-B3` are new or re-aimed this session.**

## STANDING, UNCHANGED

- **EIGHT INSTRUMENTS DIE ON AN UNRECOGNIZED ARGUMENT WITH A RAW TRACEBACK.** Ugly and SAFE.
- **S167's DEBT IS CLOSED AND MUST NOT BE RE-OPENED** (Bible §16.43).
- **`byte_audit` ARM 2 STILL CANNOT SEE A FIGURE IN PROSE — AND S180 ADDED FIVE MORE IT CANNOT
  SEE.** Blinding-controlled at S180 close: a COMPILE CHECK figure was moved 25,248 → 25,240 and
  **book_gates stayed 78/78 and `byte_audit --check` stayed PASS.** ARM 2 reads figures inside a
  declared band; a bolded number in a callout paragraph is prose. **All five new figures are
  correct today** — each derived against the compiled table at close — **but nothing will catch
  them if they drift.** That is the real cost of the COMPILE CHECK boxes and it was paid knowingly.
- **L16 STILL NEVER STATES ITS MATCH-MODE FIGURE** (S166) **and has ZERO practice units** — out of
  scope for fall, but it is the capstone.
- **GATE 77 DOES NOT EXCLUDE `<pre>`** (S165).
- **§16.32–§16.44 STILL HAVE NO NUMBERED BODIES** — thirteen changelog-only.
- **The poster is a GRADED deliverable** (DJ, S159). **Photography is OFF the critical path** (S156).
- **Fall launch Sept 8. L13 is the last in-scope lesson and it is whole.**

---

# HARNESS — IT IS NOT IN THE REPO. RUN THE SCRIPT.

```
apt-get install -y gcc-avr avr-libc     # foreground; the box has no toolchain
sh harness_setup.sh                     # prints objects: 41  AND  core stderr: clean
python3 byte_audit.py --sizes           # ~4 min at 221 payloads
python3 byte_audit.py --selftest
python3 byte_audit.py --check           # EIGHT arms
python3 byte_audit.py --discards        # ARM 9, NOT in --check's path
```

**TO COMPILE ONE PAYLOAD BY HAND, READ `pio_harness.sh` FOR THE INCLUDE SET.** It builds from an
eight-library list plus five Arduino core paths. S180 lost four attempts reconstructing it before
reading it.

**STANDING CONTROLS, ALL REPRODUCED S180:**
`11/after_step_1` **20,592** · `11/finished` **20,778** · `12/finished` **24,790** ·
`12/c2_slipalarm` **21,334** · `13/finished` **25,248** · `14/finished` **26,002** ·
`15/finished` **28,406** · `16/finished` **28,626**.

**221 payloads, FOUR declared overflows** — all four in L16, unchanged.
**THE TIGHTEST PASSING BUILD IS `16/after_step_2` AT 28,648, WITH 24 BYTES SPARE.**

---

# STANDING AUTHORITY — §24.17 AND §24.19

**Decide and report; do not ask.** Three carve-outs: facts about the ROOM no instrument can see;
moves that are irreversible or expensive to undo; and RoboLore brand and course scope.

**§24.19 IS THE TIEBREAKER** — what is best for student learning. **S180 used it to REFUSE work**:
the 35-card marker rollout was measured, priced, and declined because it would convert retrieval
into lookup. *Not every measured gap is a gap worth closing.*

---
<!-- VERSION BLOCK: emitted by session_versions.py --handoff. Never hand-typed. -->
Fresh-clone verified at **`93b50e9`**. Census **41,465**.
Bible **v8.174** · `BookComponentStandard` **v01.13.0** · Maker **v2.64** ·
`marks/` **41** · `icons/` **49** incl. LICENSE.
`ZUMO_Syllabus_WORKING.md` **v1.3**.

Instruments: `book_gates` **v1.72.15** · `lesson_inventory` **v1.3.5** ·
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

Lessons: L01 v03.31.3 · L02 v03.24.1 · L03 v03.44.3 · L04 v04.29.3 · L05 v04.29.2 · L06 v04.32.5 · L07 v04.31.6 · L08 v04.32.1 · L09 v05.27.4 · L10 v02.30.3 · L11 v02.31.1 · L12 v01.35.2 · L13 v02.38.0 · L14 v02.36.0 · L15 v02.32.0 · L16 v02.28.0.
