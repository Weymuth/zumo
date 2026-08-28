# ZUMO — S194 HANDOFF (written at S193 close · paste at top of Session 194)

## READ THIS FIRST

**NOTHING FROM S193 IS PUSHED.** 19 paths differ from HEAD (`d90399d`) — 17 modified, one deletion,
one new file. 0 unbumped.
`git rm ZUMO_S193_HANDOFF.md` is part of this push and **`ZUMO_S194_HANDOFF.md` IS A NEW FILE** —
both are checkboxes in GitHub Desktop, which is where the deletion and the new file get missed.
**`newproject.html` was NOT touched this session** — no Maker upload, no rename-on-disk dance.
If `__pycache__/` exists, delete it LAST; it regenerates on every gate run.

**`site_parity` IS DISCHARGED FOR S192's PUSH AND IS OWED AFTER THIS ONE.** S192's push
(`d90399d`, Aug 27 22:23 EDT) was verified at S193 open: **PARITY twice, 02:42 and 02:46 UTC**,
19 and 23 minutes past the 10m57s build floor. **Two lesson files changed in S193** (L08, L15) and
`css/book.css` was regenerated, so the asset arm CAN move — run it twice past the floor and believe
the repeat.

**`byte_audit` OWES NOTHING.** **Zero payloads moved this session and zero bytes.** All three S193
content fixes are lesson prose and bank text. The harness was never stood up. Standing control is
**20,592**.

**82/82 gates** — gate 82 is NEW · `gate_payload_match` **PASS**, advisory unmoved at **635** ·
`retired_claims` **CLEAN, 23 registered** (was 21) · `quiz_bank --check` **16 banks valid** ·
`callout_id` **1135** (was 1134) · `census --selftest` **19 controls** ·
`build_worklist --check` current (regenerated on the Bible bump, S175 coupling).

---

# 1. WHAT S193 DID

## `L08-15` CLOSED — AND **L01 THROUGH L08 ARE NOW DONE. L09 IS THE FRONTIER.**

**The C1 family INVERTED, and the smallest row in the file: 2 sites, 0 Maker payloads, 0 bytes.**
C1 called feed-forward a RIVAL of the loop; this called a feed-forward RULE a loop. L08 C6's GOAL
said *two proportional controllers running on the same error* — but `speed = BASE_SPEED − KS×|error|`
is proportional to the STEERING loop's error and **nothing measures the robot's actual speed**.

**`L08_A17` NEEDED RESTRUCTURING, NOT REWORDING** — its stem asserted the defect while its
`correct: true` option stated the truth. The `L08_B25` / `L11_B44` shape, third occurrence.

**GPT'S SECOND HALF DOES NOT REPRODUCE.** *"Challenge 5 Adaptive Kp is gain scheduling, not PID"* —
measured, **ZERO** sites call it PID; all 5 L08 `PID` hits are the nav bar, §1's Real-World
Connection and *Looking Ahead: The Full PID*. Recorded as measured-clean in the closure row rather
than dropped.

## THE TRIPLE CHECK: THREE ARMS AGREED AND WOULD HAVE SHIPPED A DEFECT
| arm | method | result |
|---|---|---|
| 1 | parse the shipped C6 solution | only sensor read is `readLinePosition()`; **zero encoder reads** |
| 2 | the book's own Closed Loop definition, applied mechanically | steering CLOSED, throttle **OPEN** |
| 3 | simulate a load disturbance | shipped rule leaves speed at **137.5** and never corrects |

Controls: arm 1's detector must SEE a measurement (its first form returned empty for *everything* —
**a broken slice caught before it became evidence**); arm 2 must SPLIT `driveDistance()` into
closed-on-distance and open-on-heading; arm 3's controls are a real speed loop restoring **200.0**
and the steering loop settling a line disturbance.

**THE FOURTH ARM IS THE ONE THAT MATTERED.** A completeness sweep of all **132** `controller` /
`closed loop` sites found **L15 §5.8 BUILDS THE REAL SPEED LOOP** — `measureSpeedCmPerSec()` off
`averageCounts()` and `COUNTS_PER_CM`, under the comment *You already own this instrument*.
**My forward pointer said *you already own the sensor* and POINTED NOWHERE.** Three agreeing arms
would have shipped a question with no address. It now names Lesson 15 and does not answer it, and
**L15 §5.8 carries the BUILDS ON back-pointer (DJ ruled both).**

## `L10-12` LEFT RESIDUE, AND FOUR SPELLINGS SHARED ONE BLIND SPOT
`L10_B21`'s stem and correct option were fixed at S192. **The `why:` on its third DISTRACTOR still
asserted the retired mechanism** — *the stated mechanism is two controllers correcting the same
thing at once* — describing something the book no longer says anywhere.
`retired_claims` read **CLEAN** over it: the structural exemption covers a declared-wrong OPTION (a
taught trap), but **a `why:` asserts what the BOOK says.** All four S192 spellings missed it because
**all four were keyed on the PROSE that sweep had just finished reading — four readings of one
corpus, not four readings of the claim (rules 83/84).**
DJ ruled: fix it, note it on the closed row, **no new row; the total stays 245.**

## GATE 82 — AND THE CONTROL THAT DECIDED WHETHER TO KEEP IT
**The S192 session that BUILT gate 81 left the per-lesson table five closures stale** — 95 / 89 / 148
against a truth of 100 / 94 / 143 — and **81/81 passed over it for a full session.**

**MEASURED, NOT ARGUED. Against the exact worklist file at HEAD: gate 81 PASSES, gate 82 FAILS**
naming L08, L10, L11, L12, L15 — the S192 closure set exactly. That is why it is kept.

Gate 81 prices a digit BESIDE A STATUS WORD; a table cell is a bare digit between pipes whose status
word lives in the header row, up to sixteen lines away. **Different populations, different
predicates.** Widening 81 would price every number in every table — gate 78's mistake, third time.
Six controls, all firing: a wrong cell · **a row that still SUMS but disagrees with truth** ·
a TOTAL disagreeing with its own columns · a deleted row · a deleted TOTAL · a non-integer cell.
The row-sum arm is INDEPENDENT of the truth arm on purpose.
**§24.24b is seated with a numbered body.**

---

# 2. S194 OPENS HERE

## L09 IS THE FRONTIER — 13 ROWS, ALL UNREAD
`L09-01` through `L09-13`. **None has been checked against the live tree.** This is a full session's
work, not a tail-end one. Read the row before measuring (S192's `L15-08` lesson).

## THE TALLY IS NOW GATED IN **FOUR** HOMES, NOT THREE
**101 closed / 95 fixed / 2 parked / 142 open of 245.** Close a row and `census` moves; **gates 81
AND 82 then fail until LIVE.md, the handoff AND the per-lesson table are all updated.** Absence also
fails — do not "simplify" the tally out of a home, and **do not quote a status glyph inside a row**
(it corrupts the derivation; S192 found that the hard way).

## STILL OWED, UNCHANGED
- **The 7 pinned `prose_canon` residue sites** — three L05/L06 lesson headings and four Maker labels,
  **ONE fix, not two**. Untouched a seventh session.
- **`prose_canon` arms 1, 2 and 4** — unbuilt. No arm without a control per direction.
- **Seat the §16 debt.** Still 26 rules, untouched an eighth session.
- **`L07_GRAPHIC_7-15`'s one real overflow** — `RobotSensors.h`, 14.5 units.
- **`ZUMO_BENCH_TESTS.md` ranks itself.** Run **1 `L10-B1` · 2 `L02-B2` · 7 `L10-B2`** in one sitting.
- **Syllabus dates still `[TBD]`; the day-by-day period grid is unbuilt. LAUNCH IS SEPTEMBER 8 —
  ELEVEN DAYS.**
- **`ZUMO_GPT_REVIEW_WORKLIST.md` footer carries a second version token** (`Worklist v1.2`) that
  disagrees with the header home `session_versions` reads (v1.12). Flagged four sessions, not ruled.

## THE NEXT INSTRUMENT ARGUMENT, IF THERE IS ONE
Gates 81 and 82 now cover the worklist tally in prose AND in its table. **Callout, bank, mark, icon
and payload figures written in ordinary prose are still unwatched** — `session_versions` owns the
emitted version block, gate 78 owns the discard figure, and between them is open ground.
**Priority is DJ's, and the launch is 11 days out.**

## STANDING, UNCHANGED
- **`gate_payload_match` IS NOT ONE OF THE GATES** (S137) and **TAKES ARGUMENTS** — pass
  `newproject.html lessons/Lesson_*.html`, or it reports a COVERAGE failure on a subset.
- **`--live` and `--handoff` PRINT, they do not WRITE** (§24.20). **LIVE.md carries TWO `**Versions:**`
  lines** — line 6 is current. **Keep the Status line to ONE line.**
- **The visible §5b banner is spelled `Version 04.31` — BARE.** A `v`-prefixed grep cannot see it.
- **`quiz_bank.py` LIVES IN `quizzes/`, NOT THE REPO ROOT.**
- **A BIBLE SESSION BUMP IS A REGENERATION OBLIGATION** (S175) — fired, `GPT_WORKLIST.md` regenerated.
- **A BIBLE BUMP HAS TWO HOMES** (S185): the version line AND the standalone changelog entry
  `current_session()` reads. **The changelog is one entry per PARAGRAPH, newest first** — S193
  inserted with a `) Prior: **v8.188** (` tail and swallowed the previous entry into its own
  paragraph before catching it. Anchor on the LINE-START version form; the line-17 home also carries
  a mid-line `Current: **v8.187**`.
- **A STALE NOTE IN LIVE.md's CURRENT REGION IS READ BY GATE 81, NOT JUST BY PEOPLE.** An S190
  paragraph — *THE WORKLIST COUNTS ARE DELIBERATELY NOT UPDATED*, naming eighty-seven closed and
  one hundred fifty-six open — sat in the current region for three sessions after S191 reconciled it
  and S192 derived it. **Gate 81 found it the moment the region resolved**, reading that paragraph's
  digits rather than the Status line's. Struck, not deleted. Rule 72, and the current region is where
  it costs most. **AND GATE 81 THEN FIRED ON THIS BULLET**, because a retired tally QUOTED in digits
  is indistinguishable from one asserted — so the figures above are spelled in WORDS on purpose, the
  same device S192 used for a projected tally. **You cannot cite a wrong tally in a gated home.**
- **A CALLOUT COSTS THREE PINS.** L15's one BUILDS ON callout moved image references (1,210 → 1,212),
  the gate 47/59 callout census (1,134 → 1,135, **in BOTH its homes — the comparison AND the failure
  message**) and the §27.11 digest. Prove count AND RANK before moving the digest: a SET comparison
  called this order-only and was wrong.

# HARNESS — NOT IN THE REPO. RUN THE SCRIPT.

```
apt-get install -y gcc-avr avr-libc
sh harness_setup.sh                     # objects: 41  AND  core stderr: clean
python3 byte_audit.py --sizes           # ~4 min at 221 payloads
python3 byte_audit.py --selftest ; --check ; --discards
```
**`--selftest` CANNOT RUN BEFORE `--sizes`** — CONTROL K dies with a `KeyError`.
**Run `harness_setup.sh` in the FOREGROUND and read `objects: 41` before trusting anything
downstream** — backgrounded, it has died silently at `== core build ==` with 0 objects.

# STANDING AUTHORITY — §24.17, §24.19, §24.21
**Decide and report; do not ask.** Carve-outs: facts about the ROOM · irreversible moves ·
RoboLore brand and course scope. **§24.19 is the tiebreaker** — what is best for student learning.

---
<!-- VERSION BLOCK: emitted by session_versions.py --handoff. Never hand-typed. -->
Fresh-clone verified at **`d90399d`**. Census **41,812**.
Bible **v8.189** · `BookComponentStandard` **v01.13.0** · Maker **v2.70** ·
`marks/` **41** · `icons/` **49** incl. LICENSE.
`ZUMO_Syllabus_WORKING.md` **v1.3**.

Instruments: `book_gates` **v1.76.1** · `lesson_inventory` **v1.3.5** ·
`gen_component` **v1.6.1** · `pill_sweep` **v1.1** · `gate_payload_match` **v1.9.5** ·
`build_family_map` **v1.6.6.6** · `callout_id` **v1.0** · `keyterm_prefix` **v1.0.1** · `build_mark_index` **v1.1.0** · `gen_bonus_banner` **v1.4.1** ·
`gen_part_banners` **v1.2** · `session_versions` **v1.32.2** · `fit_raster_svg` **v1.2** ·
`flatten_alpha` **v1.2** · `svg_layout_audit` **v1.21.2** · `site_parity` **v1.2.1** ·
`build_css` **v1.4.0** ·
`image_audit` **v1.3** ·
`strip_inline` **v1.2** ·
`build_worklist` **v1.2** ·
`prose_canon` **v1.1.0** ·
`retired_claims` **v1.1.1** ·
`census` **v1.2.0** ·
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

Lessons: L01 v03.32.1 · L02 v03.26.1 · L03 v03.47.0 · L04 v04.29.6 · L05 v04.30.0 · L06 v04.37.2 · L07 v04.33.1 · L08 v04.34.4 · L09 v05.27.6 · L10 v02.30.7 · L11 v02.31.4 · L12 v01.35.4 · L13 v02.39.0 · L14 v02.36.2 · L15 v02.32.2 · L16 v02.28.1.
