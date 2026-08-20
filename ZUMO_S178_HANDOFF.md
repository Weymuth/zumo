# ZUMO — S178 HANDOFF (written at S177 close · paste at top of Session 178)

## READ THIS FIRST

**S177's work IS PUSHABLE and DJ verifies the push himself (standing ruling, S158).**
`git rm ZUMO_S177_HANDOFF.md` is part of that push. **If `__pycache__/` exists in your tree,
delete it LAST, immediately before pushing** — it REGENERATES on every gate run.

**78/78 gates** · `gate_payload_match` **PASS with the census armed** · `quiz_bank` 16 banks at
**1,246** questions · `build_css --check` current at 574 rules · `image_audit --check` current ·
`build_worklist --check` current **after regeneration** · `callout_id` **1127/0** ·
census **41,009** · `next_pointer` clean.

**`site_parity` HAS NOT RUN THIS SESSION AND COULD NOT.** The tree now differs from the published
site by design. **Run it at least twice AFTER this push, tree untouched between runs, and believe
the repeat (§16.42).** It was PARITY on two consecutive runs at S176 close.

**`byte_audit` DID NOT RUN AND DID NOT NEED TO.** No payload moved, no Maker change. The eight
standing controls are verified as of S175 — do not re-prove them unless the toolchain or a payload
has moved.

**S177 EDITED ONE LESSON, THREE BANKS, ONE INSTRUMENT AND TWO DOCUMENTS.**
`Lesson_01.html` → **v03.31.0** (moderate, both §5b homes) · `QUIZ_L01` **1.1.3** ·
`QUIZ_L02` **1.0.5** · `QUIZ_L16` **1.0.12** · `book_gates` **v1.72.8** (§27.11 digest only) ·
`ZUMO_SUPER_BIBLE.md` **v8.170** (§16.46 NEW, seated with a numbered body) ·
`GPT_WORKLIST.md` regenerated (stamp line only) · `css/book.css` regenerated.

---

# 1. LESSON 1's TEN FINDINGS ARE ALL APPLIED. NOTHING FROM THE L01 SET IS OPEN.

DJ's ruling (S176) was *"Get lesson one rewritten and zero errors and i'll bench test all of it."*
All ten confirmed-live findings shipped in one arc, plus one adjacent contradiction found while
reading. **Twenty-one edits, every one asserted `count == 1`.**

| ID | what shipped |
|---|---|
| `L01-01` | §6 *Break It On Purpose* now says **UNPLUG THE USB CABLE**; troubleshooting row, Quick Reference row and the closing sentence all re-aimed; a new paragraph teaches the corrected fact |
| `L01-03` | §4.2, KEY TERM 1.15, NOTE 1.18 and the glossary entry stop claiming PlatformIO downloads libraries *via Git*; the Mac Command Line Tools reason is named. **The step stays.** |
| `L01-07` | *touches exactly three things* → five named, three tabled (table NOT enlarged, S154); the *everything else … the motors* sentence corrected |
| `L01-08` | *B had no printf* → B had one, the tutorial used `putchar()`; image `alt` and caption *introduced* → **popularized** |
| `L01-09` | *the very first programmers in history* → a line back to Kernighan's 1972 tutorial |
| `L01-11` | *feedback separates a robot from an appliance* → a thermostat closes a loop too; steering by **how far** off sets up L08 |
| `L01-12` | the USB chime bullet is platform-neutral |
| `L01-04` | Challenge 9 → **prop it up**, not the floor; floor test cross-referenced |
| `L01-05` | Challenge 4's reveal corrected: **two `delay(350)` calls, you changed one** |
| `L01-06` | Challenge 11's solution prints to the SCREEN the scaffold promised, sets up the display first, and **defends 4500 against the hint's 4200** |
| *(extra)* | the "Still stuck?" checklist's *wheels in the air = broken* now says §7 does it on purpose |

**THE FLOOR TEST IS A NAMED RITUAL NOW, SEATED ONCE IN CHALLENGE 4** — upload tethered, unplug,
switch power ON, set down, hands clear — and Challenge 9 points at it. **It is prose, not a new
callout, deliberately:** a new callout moves `callout_id`, the family map and §5.1's geometry
baseline for a paragraph that needed none of them (rule 46).

## TWO HANDOFF CLAIMS DID NOT SURVIVE VERIFICATION

**`L03` WAS NOT EDITED AND OWED NOTHING.** S177's handoff named L03 Part 2's *Robot connected via
USB with power ON* as a fourth site of the L01-01 false premise. **It is not a site.** Part 2 drives
the robot across a floor, so power ON is required and the sentence is true. Checked before anything
moved (§24.6c). *(A different, real L03 issue is noted in §4 below.)*

**`L01-12` WAS SMALLER THAN RECORDED.** TIP 1.45 sits immediately under the bullet and already
carries the Mac form *Allow accessory to connect?* Only the bullet needed rewording.

**THAT IS FOUR TIMES NOW THAT GPT WAS RIGHT ABOUT THE PLACE AND WRONG ABOUT THE DIAGNOSIS, PLUS
TWICE THAT THE HANDOFF'S OWN SUMMARY OVERSTATED A FINDING.** Verify before editing. Every time.

---

# 2. THE BANK WAS RIGHT AND THE LESSON WAS WRONG — READ THIS ONE

`L01_A06` has keyed Challenge 4's correct behaviour all along (*twice as far out as it comes back*)
and even carries a distractor whose `why` reads **"Only the first one changed."** The lesson's
revealed solution said *twice as long in each direction*, which is false. **The bank was authored
from the payload; the reveal was never corrected.**

**When a bank and its lesson disagree, neither is automatically the outlier — the PAYLOAD is the
artefact both derive from, and it decides.** Verified: the `c04` payload's `<<< CHALLENGE 4` marker
sits on the FORWARD `delay(350)` only.

**THREE BANK ANSWERS WERE KEYED TO CLAIMS THIS SESSION FALSIFIED** (the S165 shape, live):
`L01_B02` (printf) · `L01_B37` (Git) · `L01_A04` (whose STEM described an exercise the lesson no
longer contains). **`L01_A04`'s *check that the USB cable carries data* distractor was replaced
too** — the fix made it collide with the truth. **A correct edit can turn a fair distractor into an
unfair one; sweep the whole item, not just the keyed option.**

**THE PIN ARC CLOSED IN THE SAME SESSION (§37).** `QUIZ_L02` and `QUIZ_L16` also pin `lesson_01`;
their three L01-asserting questions (`L02_B54`, `L16_B08`, `L16_B10`) were read and are untouched by
any changed sentence, so both pins were **earned**, not bumped. `UNREAD_PINS` stays 0.

---

# 3. §27.8b's CYCLE WAS NOT OWED, AND A SCRATCH COPY IS WHAT SAID SO — REUSE THIS

`build_css --check` went RED after the edits, as it will after any edit that adds a styled element.
**The cycle (`--restore` → `build_css` → `--apply`) exists to stop a NAME disappearing or
repointing.** Whether that happened is CHECKABLE without touching the tree:

```
cp -r zumo scratch && cd scratch && python3 build_css.py     # regenerate in a COPY
# then diff name-by-name: names added / dropped / declarations changed
```

**Measured: 574 rules both ends, 2,033 declarations, ZERO names added, dropped or repointed.** The
whole diff was `.p-m-12px06px` 11→12 and `.p-m-8px00` 9→10 changing frequency and therefore
position. **A plain regeneration was sufficient and the cycle was not run** — which also kept
S168's held-LESSON-STRIP hazard (`--restore` expands held blocks that `--apply` will not restore)
out of the session entirely. `strip_inline --verify` 0 dead.

**Do this check before the cycle every time. It costs one copy and one diff.**

**S175's COUPLING FIRED A THIRD TIME, ON SCHEDULE.** `build_worklist --check` green at open, red
immediately after the Bible bump; **the entire diff is the stamp line**, S176 → S177, 38 files and
9 findings UNCHANGED. Keep the close-ritual item.

---

# 4. S178 OPENS HERE — THE GPT LIST IS STILL THE ASSIGNMENT

**DJ: *"I can't ship a book with errors in it."* Lesson 1 is done. Fourteen confirmed-verbatim rows
remain, and 161 rows have never been looked at.**

## THE 14 STILL-VERBATIM ROWS (verify each against the tree BEFORE editing)

`L02-01` `L02-08` `L03-03` `L05-01` `L06-03` `L08-05` `L09-07` `L09-13` `L10-06`
`L12-05` `L12-09` `L12-17` `L13-06` `L13-08` `L13-10`

**TWO ARE ALREADY CONFIRMED AND UNFIXED:**
- **`L02-08`** — §4 says *"Lesson 1 used one button, one light, and the screen."* L01 calls
  `playFrequency` **18** times, references `buzzer` **28** and calls `setSpeeds` **20**.
  **This is now L01-07's exact twin and should be fixed with the same wording**, since L01 §3 was
  corrected this session to say five things.
- **`L03-03`** — Part 2 still lists *"Your Zumo_Lesson_2 project folder (we'll copy it)"*, one
  occurrence, against a §5.1/§6 that use the Maker for a fresh project.

**A NEW, UNTAGGED L03 FINDING FROM THIS SESSION'S READ, RECORDED NOT FIXED:** Part 2's prerequisites
ask for *Robot connected via USB* **and** *Clear floor space (6+ feet)*. **You cannot drive six feet
tethered.** L01 now names the floor-test ritual; L03 is where it should first be USED. Cheap, and it
makes the two lessons agree.

**THE OTHER BUCKETS:** 48 rows whose quote is GONE with no surviving 4-word fragment (strong
evidence already fixed — a mechanical DEAD/LIVE pass would close them) · 45 ambiguous · 63 with no
checkable quote, needing a human read.

## SECOND JOB — SHIP THE GATE 78 FIX. **DJ RULED IT INTO S178.**

**FOUND BY THE S177 TRIPLE CHECK, AND IT IS S175's UNDER-REACH A SECOND TIME.** Gate 78's
predicate is `(\d+) discards? over (\d+)(?: of (\d+))? payloads?` and **the digits must sit
ADJACENT to the words**, so a bold-wrapped figure slips straight past it.

**CONTROLLED BOTH WAYS IN A SCRATCH TREE BEFORE ANYTHING WAS RULED — one mutation each:**

| plant into LIVE.md's current region | gate 78 |
|---|---|
| `12 discards over 7 of 105 payloads` | **FAILS alone** |
| `**12** discards over **7** of 105 payloads` | **SILENT — 78/78 green** |

**S175 ALREADY WIDENED THIS ARM ONCE** — off `**`-immediately-before-the-digit, onto
digits-outside-code — **and the adjacency requirement survived the widening.** That is the
lesson worth more than the fix: *a widening closes the case it was aimed at, not the property.*

**IT IS A LIVE RISK AND NOT A THEORETICAL ONE.** This project's house style bolds figures —
`**1,246** questions` appears in LIVE.md, the handoff AND the Bible. Today's documents happen to
bold the WHOLE phrase, so the digits come out bare and the gate sees them. **Correct by luck
rather than by assertion (rule 59).** The first session that writes `**15** discards` in the
ordinary house style gets a silent gate.

### THE DESIGN, ALREADY PRICED

**Blank `**` the way `_CODE78` already blanks backticks — at EQUAL LENGTH**, so the offsets a
failure message reports stay true to the source. `_CODE78` is the working precedent sitting four
lines above; this is the same move on a second marker, not a new idea.

**ORDER MATTERS AND IT IS THE ONE TRAP:** blank the backticks FIRST, then the asterisks. Reverse
that and a bolded figure *inside* inline code stops being excluded — the arm would start
convicting quoted spellings, which is exactly the noise S175 declared unusable.

### WHAT IT OWES BEFORE IT COUNTS (rule 59)

**A CONTROL PAIR, and the bold plant must FIRE where it is currently silent:**

1. `12 discards over 7 of 105 payloads` → still FAILS *(no regression)*
2. `**12** discards over **7** of 105 payloads` → **now FAILS** *(the whole point)*
3. `` `15 discards over 7 payloads` `` in backticks → still SILENT *(the exclusion survives)*
4. `**`15 discards over 7 payloads`**` — bold AROUND inline code → **must stay SILENT**
   *(this is the ordering trap, and it is the control that catches it)*
5. the clean tree → 78/78 green

**Plant into LIVE.md's CURRENT session region** — the gate reads lines 3–6 plus the newest
`## WHAT SHIPPED` block, and nothing else in that file.

**`book_gates` takes a MINOR bump** (`v1.72.8` → `v1.72.9`): predicate widened, no baseline moves,
no other gate touched. **A Bible §16 entry is owed** — this is the second under-reach in one arm
and the pattern is the finding.

**DO NOT LET THIS DISPLACE THE GPT LIST.** It is fifteen minutes. **Lesson 02 is the primary.**

---

## BENCH — `ZUMO_BENCH_TESTS.md` IS THE HOME NOW. NEW FILE, S177.

**Every bench item in the project is in `ZUMO_BENCH_TESTS.md`: 51 rows across 15 lesson blocks,
DERIVED from the file rather than typed (rule 44 — the S177 triple check caught this count wrong
at 40 in the first draft).**
They had been scattered across handoffs since S40 and re-reported as open by every reader since
(rule 72). **Do not carry bench items in a handoff again — put them in that file.**

**It also carries the floor-test ritual once**, so lessons point at it rather than restating it.

**THE OLDEST OPEN ITEM IS `L09-B1`, the green-tape six numbers, carried since S41.**
**THE MOST CONSEQUENTIAL IS `L10-B1`** — §16.12's perpendicular arrival, unruled since S143, with
a falsifiable prediction attached.

## L01 REFINEMENTS APPLIED AT S177 CLOSE (DJ questions 1 and 2)

**v03.31.0 → v03.31.1 (minor; both banks and `QUIZ_L16` re-pinned).** DJ asked whether unplugging
would simply abort the upload, and approved a raised platform. Both are now explicit:

- §6's first step says unplug **before** clicking anything and **never pull the cable while an
  upload is running** — the exercise is an upload with NO PORT, not an interrupted transfer.
- Challenge 4's floor test now matches GPT's ritual in full: **upload with the robot on a stand**,
  wait for SUCCESS, **close the Serial Monitor**, unplug, power ON, set down, stand clear.
  Closing the monitor matters because `L01_B48` teaches *Resource busy*.

## BENCH — DJ SAID HE WOULD TEST L01

- **The unplugged-upload error text.** §6 says *read the error message*; it quotes nothing, so
  **nothing bench-dependent shipped**. If you want the real string pinned into the lesson, DJ reads
  it once. **PlatformIO IS NOT INSTALLED in the container and `pio_harness.sh` is a misnomer running
  raw `avr-gcc`/`avr-g++`** — this cannot be closed here.
- **Challenge 4 on the floor**, unplugged: does it finish one nudge ahead of its start?
- **Challenge 11's solution** as printed — `display.setLayout21x8()` then the voltage, 1.5 s, then
  the `< 4500` branch — reads on the OLED before §6's setup reprints *Press A*.
- Standing: Q017 L09 six numbers · Q044 calibration-spin · Q046 gyro-bias · L02 §5 green-LED ·
  L12 BONUS B4 · L15 Challenge 3's `turnDegreesGyroSafe()`.

## STANDING, UNCHANGED FROM S177

- **A GATE FOR `GPT_WORKLIST.md` IS OWED AND PRICED, NOT SHIPPED** (S174). `--check` closes what a
  ritual can reach; a gate costs an `svg_layout_audit` pass on every `book_gates` run, and **an arm
  that made the routine slower is one somebody eventually skips.**
- **`gate_payload_match` IS STILL NOT ONE OF THE 78** — the S137 exposure. The census arm inherits
  it. Priced, not shipped: it needs the Maker parsed on every suite run.
- **EIGHT INSTRUMENTS DIE ON AN UNRECOGNIZED ARGUMENT WITH A RAW TRACEBACK.** Ugly and SAFE — none
  of them writes. Cosmetic, not owed.
- **S167's DEBT IS CLOSED AND MUST NOT BE RE-OPENED** (Bible §16.43).
- **ARM 7's two remaining false skips** are stated blind spots, not bugs.
- **`byte_audit` ARM 2 STILL CANNOT SEE A FIGURE IN PROSE**, and nothing here reads a sentence.
  **Ten prose defects shipped this session past 78 green gates** — §16.18 from the content side.
- **L16 STILL NEVER STATES ITS MATCH-MODE FIGURE** (S166).
- **GATE 77 DOES NOT EXCLUDE `<pre>`** (S165). When it first fires, the answer is a ruling.
- **§16.32–§16.44 STILL HAVE NO NUMBERED BODIES** — the debt v8.153 recorded. §16.45 and §16.46
  were both seated rather than added to that queue; thirteen remain changelog-only.
- **L13/L14 bank pin arcs — STRUCK AT S176, re-verified here.** `UNREAD_PINS` is 0 and §24.18
  passes. Delete the item.
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

**STANDING CONTROLS, ALL REPRODUCED S175, UNTOUCHED BY S176 AND S177:**
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
Fresh-clone verified at **`6225790`**. Census **41,009**.
Bible **v8.170** · `BookComponentStandard` **v01.13.0** · Maker **v2.62** ·
`marks/` **41** · `icons/` **49** incl. LICENSE.
`ZUMO_Syllabus_WORKING.md` **v1.3**.

Instruments: `book_gates` **v1.72.8** · `lesson_inventory` **v1.3.5** ·
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

Lessons: L01 v03.31.1 · L02 v03.21.5 · L03 v03.43.2 · L04 v04.29.2 · L05 v04.29.1 · L06 v04.32.4 · L07 v04.31.5 · L08 v04.32.1 · L09 v05.27.4 · L10 v02.30.3 · L11 v02.31.1 · L12 v01.33.1 · L13 v02.35.0 · L14 v02.36.0 · L15 v02.32.0 · L16 v02.28.0.
