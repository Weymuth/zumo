# ZUMO — S182 HANDOFF (written at S181 close · paste at top of Session 182)

## READ THIS FIRST

**S181's work IS PUSHABLE and DJ verifies the push himself (standing ruling, S158).**
`git rm ZUMO_S181_HANDOFF.md` is part of that push. If `__pycache__/` exists, delete it LAST.

**78/78 gates** · `gate_payload_match` **PASS** · `quiz_bank --selftest` ALL CONTROLS, 16 banks at
**1,246** · `build_css --check` current · `image_audit --check` current · `build_worklist --check`
current · `callout_id` **1132/0** · `next_pointer` clean · **`session_versions --currency` 0 unbumped**
· `byte_audit` **221 payloads, all 8 standing controls reproduced, --selftest/--check/--discards PASS**.

**29 CHANGED, 1 NEW (`ZUMO_S182_HANDOFF.md`), 1 DELETED (`ZUMO_S181_HANDOFF.md`) — 31 entries,
derived from `git status`, never typed (S163/S170: the number that is TYPED is the number that is
wrong).** 5 lessons · Maker **v2.65** · Bible **v8.175** · 13 quiz banks ·
`book_gates` **v1.72.16** · `gate_payload_match` **v1.9.1** · `session_versions` **v1.30.1** ·
`site_parity` **v1.2.1** · `ZUMO_BENCH_TESTS` **v1.3** · `ZUMO_GPT_REVIEW_WORKLIST` **v1.4** ·
`css/book.css` · `GPT_WORKLIST.md`.

**AFTER THE PUSH, `site_parity` WILL NOT TELL YOU THE LESSONS LANDED — see §3 below. md5 the
changed PAGES against a cache-busted fetch.**

---

# 1. THE LEDGER HAD TWO FAILURE MODES AND BOTH WERE STRUCTURAL

**S180 diagnosed *silence reads as closed* and then shipped five L02 rows without recording them.**
S181 found the same shape four more times, in the other direction: **rows that were DONE and never
written down** — `L13-08` (two of three sites already correct), `L13-09` (already dead), `L13-10`
(the hedge already there), `L13-12` (the labelled C6 pair already shipped).

**AND A SECOND MODE: A MISCATEGORISED ✅.** `L06-01` sat in Part 0 as *✅ MEASURED — confirmed in
Part 5b*. Part 5b's ✅ means **the bug was confirmed to EXIST**; its own verdict reads *the most
important code finding in the review, AGREE-EXPENSIVE*. **A ✅ meaning "confirmed present" was
filed under CLOSED ROWS.** `L08-13` is closed on identical wording and needs the same look.

**PART 0 IS REBUILT (v1.3 → v1.4) AROUND AN EXACTLY-ONCE RULE:** every one of the 245 rows resolves
to CLOSED, PARKED or OPEN, and **PART 4 IS NOT A DISPOSITION SECTION** — D-3/D-4/D-5 say *hold until
priced*, *price it first*, *unverified*. **The rule caught its own author four hours later**, when a
duplicate `L06-01` row was written.

**LEDGER NOW: 57 closed · 2 parked · 186 open. All 16 lessons reconcile, zero duplicates.**
**Only L01 and L02 are done.** L03 has 2 open; **L13 has 5**.

**THE HANDOFF'S *still-verbatim* SHORTLIST WAS NOT A REMAINDER.** Full-history search (964 commits,
handoffs + Bible, worklist excluded) found **12 of L12/L13's 39 rows ever named, and only four ever
ruled** — `L13-01/03/05/11` at S167/S168, recorded in **Bible §16.33/§16.34 and never in the ledger.**
That is the whole of *"L12 and L13 have had a pass."*

---

# 2. ELEVEN ROWS CLOSED, AND THE BIGGEST WAS A LIVE CODE DEFECT

`L13-02` `L13-04` `L13-06` `L13-07` `L13-08` `L13-09` `L13-10` `L13-13` `L13-14` `L13-20` `L06-01`,
plus `L13-17` REFUTED and `L13-12` found already-done.

## `L06-01` — REVERSE TRIM. THE ONE THAT MATTERED

`speed` carries the sign of travel, so `speed + TRIM` hands the WEAK motor LESS duty in reverse.
**Measured at the register, not modelled:** `Zumo32U4Motors::setLeftSpeed` negates the sign into a
bool and writes `|speed|` to `OCR1B`, putting direction on one GPIO pin — so `setSpeeds(-135,-150)`
is a real 2× swing. **Bible v8.13's hardware-direction rule satisfied against Pololu's own source.**
L06 calls `driveDistance(-20)`; L07 calls `-15` and `-20`. It was live in three lessons.

**SCOPE WAS THE WORK.** 439 sites match `setSpeeds(<var> + TRIM, ...)`; **only 153 are the bug.**
`DRIVE_SPEED`/`BASE_SPEED`/`gapSpeed` are unsigned and correct. **`leftSpeed + TRIM` is L12's
DELIBERATELY PLANTED sabotage** — a blanket fix would have silently repaired a bonus mystery.
Excluded by name and asserted untouched after every write.

**FOUR WRONG MEASUREMENTS BEFORE THE RIGHT ONE, and this is the reusable half:**
1. Zero delta everywhere — could have been a transform that never fired.
2. Substitution counter + a `millis()` control (+26..+100) proved the harness sees deltas. Still 0.
3. Disassembled: `.text` byte-identical. **`RobotConfig.h` ships `const int TRIM = 0;`** — the
   student's blank — so both forms fold to `speed + 0`. **A constant that ships as zero hides every
   sign bug that uses it.**
4. Re-run at TRIM=15: STILL identical, because `avr-nm` shows **no `driveDistance` symbol** — it is
   inlined and its only calls are positive constants, so the negative branch is dead-code-eliminated.

**TRUE PRICE: only THREE payloads in the book call it with a negative literal** — `11/c1_backup`,
`13/challenge_9_1_keep_sweeping`, `13/challenge_9_3_row_zero`. **+10 bytes each, +8 in `6/finished`,
0 elsewhere, 0 as shipped.** `16/after_step_2` measured unchanged at **28,648 with 24 spare.**

**PROSE CARRIES THE REASON, NOT 153 PAYLOAD COMMENTS** (the anchor comment is 151/153 in the Maker).
L06 Step 13 explains it; **L03 §8's *that never changes, in this lesson or any lesson after it* is
scoped** — WHICH motor is fixed, the SIGN is not.

## `L03` BONUS 2 WAS THE SAME DEFECT WITH THE STUDENT AS WITNESS

Bonus 2 has the student negate both speeds, *keep the TRIM math*, watch the robot curve worse — and
then blamed **gearbox asymmetry**. It is the sign error, roughly a doubling. **A false mechanism the
student has already CONFIRMED with their own eyes is the worst kind.** Re-premised: the sign is the
headline, asymmetry is the fine print, and it now spirals into L06.

**`L03-B3b` FILED (bench):** with the sign fixed, a robot tuned forward should drive *nearly*
straight backward. **If the residual is as large as the original error, the premise is wrong and
Bonus 2's reveal must put asymmetry back as the headline.**

## `L13-06` — GPT WAS RIGHT AND UNDERSTATED IT

B4's reveal said *the door never triggers*. Traced against the payload: calibrated white floor is 0,
`SILVER_RAW_MAX` is tuned in the hundreds, so the guard never trips and **it returns TRUE.**
**And §6 checks silver BEFORE `isLineVisible()`, deliberately** — so `handleGap()` never runs and
`LINE_LOST` is impossible. **The reveal contradicted a code comment two screens away.** Symptom
corrected (fires at the first gap, sweeps mid-course) and a new closing beat added: **the real
doorway still works**, because silver clamps to 0 too — *the broken code passes the one test you
would have written.*

---

# 3. THREE INSTRUMENT FINDINGS, ALL FROM THE CLOSE-OUT TRIPLE CHECK

**1. `session_versions --currency` CAUGHT SEVEN UNBUMPED FILES.** Every lesson, the Maker and
`book_gates` had been edited and none bumped. **Without that arm this session ships unversioned.**

**2. AND THE ARM ITSELF HAD A HOLE.** `CURRENCY_HOMES` maps `.py` to `^VERSION = '...'`, so
**`gate_payload_match.py` (version in a header line), `ZUMO_BENCH_TESTS.md` and
`ZUMO_GPT_REVIEW_WORKLIST.md` reported *no version home* and were asserted by nothing** — all three
were edited this session and all three would have shipped unbumped. Three PATH predicates added,
each blinding-controlled (revert → named; restore md5-exact). `session_versions` **v1.30.1**.

**3. `site_parity` PRINTED *PARITY* WITH FIVE LESSONS AND THE MAKER REWRITTEN AND UNPUSHED.**
It compares **REFERENCED ASSETS**, never the pages. Measured: `Lesson_13.html` differed from the
live site by **3,613 bytes** while the arm said PARITY. The docstring was always honest; **the
VERDICT LINE overclaimed, and the session-open ritual reads the verdict.** Narrowed, **v1.2.1**.
**To confirm a push landed, md5 the changed PAGES against a cache-busted fetch.** Widening the arm
is a design change owing its own controls — not done.

---

# 4. THE PIN ARC — FIVE BANK ITEMS WERE FALSIFIED BY CORRECT EDITS

Bumping five lessons put **19 `source:` pins stale across 12 banks**, and reading them found the
S177/S178 shape again: **a bank authored faithfully from a wrong lesson.**

- **`L13_B43`'s CORRECT ANSWER WAS the retired DRV8838 claim.** Re-keyed to *there is no arm*, with
  the retired claim kept as the strongest distractor and a `why` explaining why it sounds right.
- **`L14_B30`'s CORRECT ANSWER carried it too.** Re-keyed.
- `L13_B42`, `L14_B04` — distractor rationales resting on the retired mechanism. (§16.30 again:
  **distractor rationales are where claims survive longest.**)
- **`L06_A04`'s CORRECT ANSWER quoted the OLD code string** `setSpeeds(speed + TRIM, speed)`.
- `L03_A19`'s `why` was the retired asymmetry mechanism; `L03_B48`'s scoped to WHICH motor.

**Every pin then bumped as EARNED, not swept.** Banks with no asserting question were read and left.
**AND THREE UNEARNED BUMPS WERE REVERTED** — `QUIZ_L01/L02/L05` had no pin change at all and their
only diff was a version I had just moved (rule 37).

**A VERSION REGRESSION WAS CAUGHT MID-FLIGHT:** a `\S+` capture ate the quotes and wrote
`bank_version: 1.0.11` over `"1.0.18"`. Corrected to `"1.0.19"` and **both homes synced** (§24.2).

---

# 5. DJ'S SCOPE RULING — BIBLE §24.21, FILED IN BOTH HOMES

**DJ, S181:** *these small bots will NOT be able to do anything in the rescue zone or on ramps —
stop worrying about meeting the RULES of RoboCup beyond basics*, and **second semester will focus on
their robot, which will / should be able to do the rescue zone.**

**MEASURED BEFORE FILING: 11 open rows rest on rulebook fidelity, 8 of them in L14/L16 — out of Fall
scope. In-scope the count is ZERO.** The ruling costs September 8 nothing.

**THE FLOOR SURVIVES: the book must not teach a student something FALSE about the rules.** Two rows
parked but FLAGGED — `L14-03` (LoP as a skip button) and `L14-15` (the *15-Minute Rule* that isn't).

**C6 IS NEARLY FREE.** Its blocker was *the three labels need a new callout family (rule 46)*. They
do not — **bolded prose, already shipped in L13 ×1 pair, L14 ×3, L16 ×1.**

**SEMESTER TWO reclassifies L14/L16 rulebook rows, victim transport, grippers and L16's enhancement
socket from PARKED to DEFERRED WITH A DESTINATION.** L13 §8A.3's corrected gripper passage is now a
**preview** — do not weaken it.

**Bible bump fired the S175 coupling as documented:** `GPT_WORKLIST.md` went stale on the stamp line
alone (38 files / 9 findings unchanged). Regenerated.

---

# 6. S182 OPENS HERE

**THE GPT LIST IS STILL THE ASSIGNMENT. DJ: *"I can't ship a book with errors in it."***

**L13 has FIVE open:** `L13-15` `L13-16` `L13-18` `L13-19` `L13-21`.

**Under §24.21 the two that matter most are `L13-16` and `L13-21`** — `ROW_STEP_CM` justified by
geometry rather than a measured envelope, and 7A taking one reading per target. **Those are about
whether the robot actually finds the ball, which is the part these bots CAN do.**
`L13-18` (5-of-5 vs 4-of-5) is DJ'S CALL / BENCH.

**`L13-15` and `L13-21` returned ZERO on my needles and are NOT cleared.** Three times this session
a zero was wrong — `L03-07`, `L13-04` and `L13-08` all read DEAD and were live. **Read the section.**

## STANDING, UNCHANGED

- **`gate_payload_match` IS STILL NOT ONE OF THE 78** (S137).
- **`byte_audit` ARM 2 CANNOT SEE A FIGURE IN PROSE**; S180's five COMPILE CHECK figures remain
  correct and unpoliced.
- **A GATE FOR `GPT_WORKLIST.md`** (S174). **§16.32–§16.44 STILL HAVE NO NUMBERED BODIES.**
- Poster is GRADED (S159). Photography OFF the critical path (S156).
- **Fall launch Sept 8. L13 is the last in-scope lesson.**

# HARNESS — NOT IN THE REPO. RUN THE SCRIPT.

```
apt-get install -y gcc-avr avr-libc
sh harness_setup.sh                     # objects: 41  AND  core stderr: clean
python3 byte_audit.py --sizes           # ~4 min at 221 payloads
python3 byte_audit.py --selftest ; --check ; --discards
```

**STANDING CONTROLS, ALL REPRODUCED S181:** `11/after_step_1` **20,592** · `11/finished` **20,778** ·
`12/finished` **24,790** · `12/c2_slipalarm` **21,334** · `13/finished` **25,248** ·
`14/finished` **26,002** · `15/finished` **28,406** · `16/finished` **28,626**.
**221 payloads, four declared L16 overflows. Tightest passing `16/after_step_2` at 28,648, 24 spare.**

# STANDING AUTHORITY — §24.17, §24.19 AND NOW §24.21

**Decide and report; do not ask.** Carve-outs: facts about the ROOM · irreversible moves · RoboLore
brand and course scope. **§24.19 is the tiebreaker** — what is best for student learning.

---
<!-- VERSION BLOCK: emitted by session_versions.py --handoff. Never hand-typed. -->
Fresh-clone verified at **`6ec9adb`**. Census **41,482**.
Bible **v8.175** · `BookComponentStandard` **v01.13.0** · Maker **v2.65** ·
`marks/` **41** · `icons/` **49** incl. LICENSE.
`ZUMO_Syllabus_WORKING.md` **v1.3**.

Instruments: `book_gates` **v1.72.16** · `lesson_inventory` **v1.3.5** ·
`gen_component` **v1.6.1** · `pill_sweep` **v1.1** · `gate_payload_match` **v1.9.1** ·
`build_family_map` **v1.6.6.1** · `callout_id` **v1.0** · `keyterm_prefix` **v1.0.1** · `build_mark_index` **v1.1.0** · `gen_bonus_banner` **v1.4.1** ·
`gen_part_banners` **v1.2** · `session_versions` **v1.30.1** · `fit_raster_svg` **v1.2** ·
`flatten_alpha` **v1.2** · `svg_layout_audit` **v1.20** · `site_parity` **v1.2.1** ·
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

Lessons: L01 v03.31.3 · L02 v03.24.1 · L03 v03.45.0 · L04 v04.29.3 · L05 v04.29.2 · L06 v04.33.0 · L07 v04.31.7 · L08 v04.32.1 · L09 v05.27.4 · L10 v02.30.3 · L11 v02.31.1 · L12 v01.35.2 · L13 v02.39.0 · L14 v02.36.1 · L15 v02.32.0 · L16 v02.28.0.
