# ZUMO — S148 HANDOFF (rewritten at S147 close · paste at top of Session 148)

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
6. `pip install cairosvg --break-system-packages` **and `pyyaml`. Needed every session.**
7. **NEVER run `build_css.py --help` or `session_versions.py --help`.** Read the docstring.
8. **Do not hand-type a version, and do not hand-type a COUNT.**
9. **`gate_payload_match.py` needs `newproject.html` FIRST, then the full lesson glob.**
10. **A CLONE IS NOT THE SITE.** Run `site_parity.py` after any push.
11. **VERIFY THE PUSH BY FRESH CLONE AND MD5 — AND DIFF THE STAGE AGAINST THE CLONE.**
12. **`css/semantic.css` AND `ZUMO_FAMILY_PINS.md` ARE HAND-AUTHORED PRESERVED LAYERS.**
13. **`rm -rf __pycache__` BEFORE `git status`. Also `find . -name pbuild -exec rm -rf {} +`**
    if the toolchain has been run — the harness leaves build dirs inside the project trees.

## 14. THE AVR TOOLCHAIN — S146's CORRECTED INSTRUCTIONS ARE RIGHT. S147 RAN THEM VERBATIM.

`apt-get install -y gcc-avr avr-libc` **(no `sudo` — `sudo` is not on this box and returns
exit 127 with a confusing error).** Then clone into `/home/claude/harness` **FLAT, not under a
`pololu/` subdirectory** — `pio_harness.sh` looks for `$H/<name>`.

**READ THE EIGHT LIBRARIES OUT OF `LIBDIRS` IN THE SCRIPT. DO NOT CARRY THEM FROM A HANDOFF —
INCLUDING THIS ONE.** S147 did exactly that (`grep -n "LIBDIRS" -A 20 pio_harness.sh`) and the
list matched; that is the procedure, not the list. `l3g-arduino` and `lsm303-arduino` are NOT
in it. Also clone `arduino/ArduinoCore-avr` to `$H/ArduinoCore-avr`. Checkout the Zumo library
at tag **2.0.1** (shallow-clone first, then re-clone full — `--depth 1` cannot check out a tag),
`cp pio_harness.sh` into `$H`, then `bash pio_harness.sh --setup`. **Expect *objects: 41*.**

**THE CONTROL: L11 `after_step_1` MUST COMPILE TO 20,516.** Now verified in S144, S145, S146
**and S147**, from four different clones. **`shim.cpp` does not exist and is not needed.**
Build with `python3 extract_project.py newproject.html <lesson> <kind> <dir>` then
`bash /home/claude/harness/pio_harness.sh <dir>`. **The anchor is `var PAYLOADS = `.**

---

# THE ONE THING TO CARRY OUT OF S147

**THE CITATIONS WERE NOT INDIVIDUALLY WRONG. THEY WERE A WHOLE EDITION BEHIND.**

L14 §4.1 cites `§4.2.7` for the handle and `§4.2.8` for the start button *and* the LoP
procedure. L14's own Engineer's Log cites `§4.3.7` for the same LoP requirement. It reads like
one of them is a typo. **It is not.** The RCJ 2025 changes list carries *Added "Terms and
Definitions"* — a new **§4.1** that pushed all of Section 4 down by one. `4.2.7 → 4.3.6`,
`4.2.8 → 4.3.7`. **Every §4.x citation in the book is a 2024 number.** The Engineer's Log was
right; §4.1 was wrong; and no amount of staring at the two numbers would have told you which,
because the answer is not in either lesson — it is in the rulebook's changelog.

**Confirmed twice over.** RCAP U19 v2026.0, a *different* ruleset derived from RCJ 2025,
numbers the handle **§4.3.6** and the switch-plus-LoP rule **§4.3.7** identically. Two
independent editions agree. **§4.3.7 is safe regardless of which ruleset governs.**

**And the same pass killed three specs that never existed.** L14 §4.1's *"25cm × 25cm
footprint"*, *"no height limit"* and *"no weight limit"* appear in **no edition** — RCJ 2025
§4.5 Inspection has no size, height or weight row, and neither does RCAP §4.5. The 25 cm is
**bridge geometry** (RCJ §3.2.3: pillars make each tile entrance 25 cm and floor-to-ceiling
25 cm), split into two wrong bullets. *"Must fit under obstacles"* is wrong twice: obstacles
are **≥ 15 cm high** and the robot is expected to go **around** them (§3.5.4, §3.5.6). You fit
under a **bridge**. **RCAP drops the bridge clause entirely, so there is no edition in which
that sentence is defensible.**

---

# S147 SHIPPED NOTHING TO THE TREE. THAT IS THE HONEST HEADLINE.

L14 was READ end to end and fully measured — **twelve compiles** — and the whole fix is
specified below to the byte. **Not one character was written.** The session went into the read
and then into three uploaded rulebooks. **The tree is unchanged at `0e62713`.** No version
moved, no bank was written, nothing was pushed.

**S148 opens on the L14 FIX with every number already measured.** Do not re-derive the chain;
**do re-run the control** (rule 30 — a working copy is not the repo, and these figures came
from a clone that no longer exists).

---

# STATE

<!-- VERSION BLOCK: emitted by session_versions.py --handoff. Never hand-typed. -->
Fresh-clone verified at **`0e62713`**. Census **40,605**.
Bible **v8.137** · `BookComponentStandard` **v01.13.0** · Maker **v2.49.2** ·
`marks/` **41** · `icons/` **49** incl. LICENSE.
`ZUMO_Syllabus_WORKING.md` **v1.2**.

Instruments: `book_gates` **v1.65.10** · `lesson_inventory` **v1.3.5** ·
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

Lessons: L01 v03.28.3 · L02 v03.21.2 · L03 v03.41.0 · L04 v04.29.0 · L05 v04.29.0 · L06 v04.32.1 · L07 v04.31.4 · L08 v04.31.1 · L09 v05.27.0 · L10 v02.29.1 · L11 v02.30.0 · L12 v01.31.3 · L13 v02.29.0 · L14 v02.33.1 · L15 v02.30.1 · L16 v02.22.1.

`quizzes/QUIZ_SPEC.md` **v1.2.0**.

**Quiz banks: derive it. Never read a count out of this sentence.**

**DJ RULED AT S147 OPEN: the L14–L16 arc proceeds even though it is outside the September
scope — *"so we keep the pattern the same until the end. No risk of drift."*** Fall scope is
still L01–L13 for teaching purposes; the arc ruling is about the book's internal consistency.

---

# S148 QUEUE

## 1. THE L14 FIX — FULLY MEASURED, NOT STARTED

### 1a. The byte chain — the shift is NOT uniform

Twelve compiles, S147, control-first. **+170 at the top of the chain, +176 at the bottom**, so
**two of the three deltas change.** This is L13's trap again, not L12's.

| site | book says | MEASURED | |
|---|---|---|---|
| §6 lead-in (L13 finished) | 24,902 | **25,072** | orphan, keyed to L13's old figure |
| Step 1 | 24,902 | **25,072** | |
| Step 2 | 24,902 | **25,072** | |
| Step 3 | 25,640 · up 738 | **25,816** · **up 744** | **delta changes** |
| Step 4 / finished | 25,640 | **25,816** | |
| 7C match mode | 25,604 · 36 fewer | **25,780** · **36 fewer** | **delta survives** |
| Sabotage header | 25,640 | **25,816** | |
| B1 | 24,906 · 734 smaller | **25,076** · **740 smaller** | **delta changes** |
| B2 / B3 / B4 | byte-identical | **all 25,816** | claim holds |
| B4 in match mode | 8 bytes smaller | **25,780 → 25,772** | **holds exactly** |
| Quick Ref "36 bytes of theater" | 36 | **36** | holds |

Challenge solutions also compiled (not cited in prose, recorded for completeness):
C1 wheel test **26,178** · C2 strict mode **25,794** · C3 LoP counter **25,940**.

**Three orphaned `24,902` sites are lines 699, 732, 861** — the ones S146 deliberately left.
**Fix L14 whole or not at all** still applies, and S148 is the whole.

### 1b. Seven defects a baseline shift would never have touched

1. **Step 3 states the same cost twice, differently** — *"up 738 … The report card costs 830
   bytes."* **830 appears in exactly one sentence in the entire tree** and nothing measures it:
   `selfTest()` has **no standalone symbol** in the Step 3 binary, LTO inlined it into
   `setup()`. **S147's ruling: replace with the measured 744**, not delete — unlike L13's
   120/26, an honest number exists and the sentence's rhetoric (cost vs. cost of a dead
   battery mid-match) survives intact.
2. **B1 contradicts itself across the reveal** — the question says *734 bytes SMALLER*, the
   reveal says *"The 820 missing bytes."* Measured: **740**. Same ruling: replace both.
   **Note the pattern — 830 vs 738 and 820 vs 734. Two paragraphs, same defect shape, gaps of
   92 and 86.** Worth asking where that pair came from before assuming it is coincidence.
3. **Step 2's *"260 lines of code, zero bytes of flash"*** — derived: the `selfTest()` body is
   **87 lines**; Step 1→2 adds **96** to `RobotHelpers.cpp` and **12** to `RobotHelpers.h`,
   **108** total. Nothing measures 260. (The *"zero selfTest symbols"* claim beside it **is**
   true — verified with `avr-nm` on `after_step_2`.)
4. **§8.5 points at *"Sections 3.3 and 6.3."*** **There is no 6.3** — Section 6 is Steps 1–4
   with no numbered subsections. Every other cross-ref in the lesson resolves; this is the only
   dangling one. Content match is **8.3 Environmental Variation Testing**.
5. **§4.3: *"To check battery voltage, add this to your code:"*** — **no code follows.** The
   callout underneath says *zero new code*. The colon promises what the lesson deliberately
   withholds. §8.2's *"Tuning Helper Code"* heading has the same shape, milder.
6. **§7E carries a draft self-correction in shipped prose** — *"have a teammate secretly
   flatten a tire… no — have them cover one line sensor with a finger of tape."*
7. **The Figures table calls it *"the twelve-item Competition Day Kit list."*** Derived from
   the `<li>` elements: **11**.

### 1c. The rules-citation fix — UNBLOCKED, both editions agree

- L14 §4.1: `§4.2.7` → **`§4.3.6`** (handle) · `§4.2.8` → **`§4.3.7`** (start button, and the
  LoP procedure — one rule covers both, which is why one citation serves).
- L14 §4.1: `§4.1` → **`§4.2.1`** (autonomous) · `§4.1.3` → **`§4.2.3`** (pre-mapped dead
  reckoning). **`§5.2.5` is correct and does not move.**
- **DELETE** the Size / Height / Weight inspection bullets — no edition carries them — and with
  them *"must fit under obstacles."*
- **`ZUMO_TDP_Template_v3.md` already says §4.3.7 and is CORRECT.** Do not "fix" it.
- **`ROBOCUP_RESCUE_LINE_2026.md` CARRIES THE STALE §4.2.7/§4.2.8 AND IS THE SOURCE OF L14's
  ERROR.** It needs the same correction. **It is also misnamed: its content is the 2025
  edition throughout** (*Last updated 2025-02-15*). Rename or add an internal edition line —
  **DJ has not ruled which.**
- **S147's recommendation, unruled: cite with the edition named inline** — *"§4.3.7 (RCJ
  Rescue Line 2025)"* — so a citation carries its own expiry date. This is the defect class
  that rotted silently for two editions.

## 2. BLOCKED ON DJ — WHICH RULESET GOVERNS. **ASK BEFORE TOUCHING L14 §3.2 OR L13.**

DJ uploaded **RCAP Junior Rescue Line U19 v2026.0** (RoboCup **Asia-Pacific**, derived from
RCJ 2025). **Mercersburg is in Pennsylvania**, so on its face this does not govern — but DJ
did not answer, and the question was still open at close.

**RCAP is not a reprint. It removes things the book teaches:**

| | RCJ 2025 | RCAP U19 2026 |
|---|---|---|
| Victims | two silver + **one black** | *"There is one types of victims"* — **two live only** |
| Evacuation points | one green, one red | **green only** |
| Ramps | 10 pts, ≤ 25° | **§3.7.1 Not Applicable** |
| Max multiplier | 1.4³ ≈ **2.74** | 1.4² = **1.96** |
| Zone walls | *colored white* | **any colour except red, green, black** |
| Bridged tiles | 25 cm clearance | clause absent |

**THE BLACK VICTIM IS LOAD-BEARING IN L13, WHICH IS IN SCOPE, READ, FIXED AND BANKED.** It is
a stated learning objective **twice** (lines 115, 1149), **Reflection Question 5** (line 1185),
part of **`IMAGE 13.1`'s caption** — an unshot photo on the September critical path — and **a
banked question in `ZUMO_QUIZ_L13.yaml` (line 413).** L14 carries it in the §1 capability list
and the §3.2 scoring table. Under RCAP that entire honest-limitation thread describes a victim
that is not on the field.

**If RCJ governs: proceed with the L14 fix as specified and leave L13 alone.** RCAP becomes a
comparison note, nothing more. **Only §3.2's scoring table is blocked; 1a, 1b and 1c are not.**

**A THIRD PDF WAS UPLOADED AND IS A DIFFERENT COMPETITION ENTIRELY** — *RoboCup Rescue Robot
League 2026D*, the major/research league: 80 kg robots, teleoperation, tethers, stepfields,
GeoTIFF map submissions, no line and no evacuation zone. **Nothing in it applies.** It is
recorded here only so nobody mines it again.

## 3. AFTER THE FIX — L14's BANK, THEN L15 AND L16
READ -> FIX -> QUIZ, same session. L14's read is **done and recorded above**, so S148 can run
FIX -> QUIZ in one sitting. L15 (16 byte figures) and L16 (47) remain unread.

**THE CAPSTONE ARITHMETIC IS STILL THE SHARP END.** L16 tells the student *"Your Lesson 15
project is 28,034 bytes. You have 638 bytes left."* **L15 finished measures 28,214, so the real
headroom is 458** — overstated by 180, **28% more room than the chip has.** Read L16's exercise
budget before assuming the fix is only numbers.

Remaining cascade: **L14 +176 · L15 +180 · L16's summary table wrong in six rows.**

## 4. THE PHOTOGRAPHY — STILL THE ONLY THING BETWEEN THE BOOK AND SEPTEMBER
Stills **3.2 · 3.5 · 3.6 · 4.1 · 4.3 · 12.1 · 13.1 · 13.2**, videos **3.1 · 4.1 · 6.1 · 8.1**.
**VIDEO 3.1 carries L03's opening page.** Nothing in the tree can produce them.
*(`IMAGE 14.1` is also unshot but L14 is out of the September scope — it is not a ninth still.)*

## 5. STILL OPEN, CARRIED
- **THE CATCH-UP CONVENTION IS SPLIT.** L07–L10 OFFSET (`step_N -> after_step_(N-1)`);
  L11–L16 IDENTITY. Clean across all 64 rows. **A gate pinning either would certify 64 and
  fail 32.** DJ to rule.
- **L15's TITLE IS SPLIT BOOK-WIDE, AND THE GENERATOR IS ON THE WRONG SIDE.** L15 names itself
  *The Present Isn't Enough* three times (title, H1, footer). **The nav strip in all 16 lessons
  says *Advanced PID Control***, and `next_pointer.py` derives titles from the strip — so
  L14's footer pointer is **generated wrong, not typed wrong**. L14 uses both titles twelve
  lines apart (lines 2022, 2030, 2180); L08 line 345 carries the stale one too. **`next_pointer`
  passes clean because it certifies the block matches the strip, not that the strip is right —
  rule 51.** 16 files, two of them unread. **S147 held it deliberately.**
- **L10's ARRIVAL GEOMETRY (S144, unruled).** Rebuilt box turns `+90`, `−90`, `−90` — net
  `−90` — arriving PERPENDICULAR to the line with nothing to realign it, and **every artefact
  agrees with the code.** Challenge 6's wedge meets the line at 30°, which a P-controller can
  pull out of; the box meets it at 90°, which it cannot.
- **§8A.4's *"Pololu rates the 75:1 gearmotors at roughly 65 cm/s flat out"* IS UNVERIFIED.**
  pololu.com is not reachable from the sandbox.
- **L14 §8A.2's *"five orders of magnitude"*** — 600 ms of demo pause against a kill-switch
  poll of *"microseconds"* needs the poll at ~6 µs to be literally true. Plausible, unmeasured,
  low priority. **A directional claim with a number is still a claim (rule 54).**
- **`AVOID_OUT_CM = 15.0` HAS NEVER TOUCHED A FLOOR.** · **CHALLENGE 6's WEDGE NUMBERS ARE
  SIMULATED.** · **L11 §7A's 999.0 RULER TRICK HAS NEVER TOUCHED A FLOOR.**
- **THE RESOURCE SECTION AS A BOOK PAGE — PARKED UNTIL AFTER SEPTEMBER 8.**
- **THE 100:1 Kp SUGGESTION IS UNVERIFIED AND THE DIRECTION IS CONTESTED.**
- **NO GATE HOLDS A QUIZ BANK** · **NO GATE HOLDS A NAV PILL** · **NO GATE HOLDS A BYTE
  FIGURE** · **NO GATE HOLDS A RULE CITATION.** Four invariants, no gates. **S147 added the
  fourth and closed none.**
- **§16.14 HAS NO NUMBERED SECTION BODY.** v8.135.3 announces *§16.14 NEW* and the Bible carries
  no `### 16.14` line. **§16.12 and §16.13 are also seated BELOW §17's heading.**
- **L12 §3.2's *5.5 counts per degree* IS A ROUNDING ARTIFACT, NOT A DEFECT.** Computes to
  **5.507**, so 90° is 495.7 counts and the lesson's **496 is right.**
- **L14 §10 IS THE ONLY §10 THAT IS NOT AN EXIT TICKET.** Confirmed by S147's read — it is the
  Competition Day Playbook (10.1–10.6). Still unruled.
- **L14's GLOSSARY says *"the reason 95% ten times is not 95%"* where §3.1 teaches 90%.**
  Minor, but the glossary cites the section it disagrees with.

## Carried from S141/S140, still unruled
- **THE BAUD BENCH TEST.** `monitor_speed = 9600`, leave `Serial.begin(115200)`. Garbage
  means **L02 §6 Step 2 is wrong**. **Keep 1200 out of the test.**
- **THE 1200-BAUD RESET HAS NO HOME IN THE BOOK.** · **`IMAGE 7.9`–`7.12` ARE INDEXED AS
  *Photo / screenshot*** where four live drawn SVGs exist.
- **§3.2's *about 13½ milliseconds*** for the six-round proximity read — unverified.
- **L05 §3.6 alkaline tension**: prose derives 6.0 V from 1.5 V/cell; the table reads 6,300 mV.
- **The `static` split is taught in L05, L06 and L08, but the GLOSSARIES still disagree.**

## Carried from S137/S138/S139, still unruled
- **§4.2's stall-current multiple**: *~1.5 A … roughly 5×*, where Pololu's no-load is ~0.10 A.
- **`IMAGE 4.1` IS A PHANTOM IN THE FIGURE COUNT** — planned 146, true population 145.
- **THE CONSTANTS vs CONFIGURATION VOCABULARY DRIFT.** Derive the canonical set first.
- **THE 3Pi+ NOTE COMES OUT OF L03** — needs a new root file as the 3Pi+ book seed.
- **L03 C1's hint hands over the exact two numbers its own template blanks ask for** — L07 C4
  and L08 C4 are the second and third instances.
- **§3.3's header-contents bullet in L07 still lists *Include guards***.
- **§7's BANNER is still three spellings** · **whether the `after` quiz set is graded at all.**

## Carried from S135/S133/S134, still open
- **THE SPIRAL ARC — RULED, ENUMERATED, DELIBERATELY NOT STARTED.** 13 of 171 units.
- **THE FIGURE BLOCK HAS FOUR SPELLINGS.** L12's is the best.
- **`svg_layout_audit.py` HAS FOUR MEASURED DEFECTS, NONE FIXED.**
- KEY TERM paint is five grounds across 238 blocks · L03 `3.44` carries `id="glossary-trim"`
  on a BODY block · `BookComponentStandard` §7.4 says 184 where the measured figure is 238 ·
  §6.5's nav-pill rule says 12–14 where the live range is 10 to 19.
- **THE AMBER LEAK: two of three closed. L02 §2.7 is the last one** — deferred to its own read.

## AFTER SEPTEMBER 8 — PARKED ON PURPOSE, DO NOT START EARLY
- **THE RESOURCE SECTION PAGE** · **REDO `GRAPHIC 4.7` IN THE BLUEPRINT COMPOSITION** (chips
  run **5 4 3 2 1** left to right — do not re-derive) · Challenge card Pass B ·
  monetization/ebook · DISCOVERIES tagging · TDP template v3 (A5 Lab Log).

## Learner mode & book content
L03_C05 Variable Speed · L03 C01/C05/C06 reference a `finished` payload that does not exist
for L03 · whole-template starters L08/L09/L10 · Maker batch · L01 VS Code multi-root step.

## Bench (need the robot — parked with photography)
Q017 L09 six numbers · Q044 calibration-spin · Q046 gyro-bias · L02 §5 green-LED ·
Constrain RUN_MS · **cm/s at a stated BASE_SPEED** · the floor rig for 3.2 / 3.5 / VIDEO 3.1 ·
a real TRIM run for `IMAGE 3.6` · **THE SURFACE TEST: run 7E on a lab tile.** · **L04's wave
test and Act Two row-1 overflow.** · **L05 Experiment 3 at 45°.** · **L06 Experiment 3 both
drags.** · **the baud test above.** · **commanded 30 cm vs measured, across a few robots** ·
**DRIVE THE SEVEN-PHASE BOX** · **drive Challenge 6's wedge** · **HOLD THE ROBOT OVER A TABLE
EDGE AND READ THE FIVE CALIBRATED VALUES** — expect ~1000 each · **L11's whole §7 ladder** ·
**L12's §7 ladder.** · **L13's ENTIRE §7 LADDER** — 7A's surface-meter table is the one that
matters: **four raw readings and nine prox counts, and every one of L13's four tunables is
blank until it is filled.** No student can complete Lesson 13 without it. **7E's fan has never
been driven either.** · **NEW: L14's §7 ladder — 7A healthy pass, 7B's four deliberate
failures, 7D's ten consecutive runs, 7E's five-minute pit cycle.** None has been run.

---

# PUSHING — READ THIS

Named-file CLI for adds and modifies; **GitHub Desktop for deletions.** **Never `git add .`**

1. **DELIVER THE FILES** via `present_files`; instructions and md5s in the CHAT ONLY.
2. **`(1)` does not mean stale.** Verify by **md5**, never by suffix.
3. **Never present a test file or a DIAGNOSTIC beside repo files.**
4. **Never produce PUSH_ME_*.md or MD5_*.txt.**
5. **`lessons/` IS PART OF THE FILENAME. `css/`, `quizzes/` and `images/` likewise.**
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
17. **RUN A BLINDING CONTROL AGAINST THE CONSUMER THAT CAN FAIL** — **and if no consumer can
    fail, say so and run a different control instead of a theatrical one (S146).**
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
33. **NO INSTRUMENT READS PROSE. Read the book.**
34. **A NUMBER IS ONLY CHECKABLE AGAINST THE OTHER FIFTEEN LESSONS.**
35. **COMPILE THE SNIPPET; LET THE BOOK'S OWN CODE TESTIFY.**
36. **A FACT THAT LIVES ONLY IN AN SVG IS NOT IN THE BOOK.**
37. **READ -> FIX -> QUIZ, NEVER QUIZ FIRST** — same session.
38. **A TEXT MATCH LOCATES; IT NEVER ANSWERS.**
39. **NO INSTRUMENT THAT READS THE TREE CAN SEE A RULING.** Search the session record first.
40. **PULL THE PAYLOAD, NOT THE CARD.**
41. **AN ENTRY FILED IN ONE HOME IS NOT FILED.**
42. **A SPEC'S OWN NUMBERS CAN BE ARITHMETICALLY IMPOSSIBLE.**
43. **WHEN TWO SECTIONS DISAGREE, READ THE CITATIONS.** **S147's completion: and when the
    citations disagree, READ THE RULEBOOK'S CHANGELOG. Neither section was lying; one was
    two editions old.**
44. **THE HEADER OF A THING IS NOT THE THING.**
45. **A SNAPSHOT YOU HAVE RUN TOOLS IN HIDES ITS OWN DEBRIS.**
46. **A CALLOUT IS NEVER A FREE EDIT.**
47. **A STEP PAYLOAD IS THE FILE AS IT STANDS AT THAT STEP.**
48. **A VERIFIER THAT READS YOUR INTENT INSTEAD OF THE ARTEFACT VALIDATES NOTHING.**
49. **A NUMBER THAT A SENTENCE DERIVES FROM CANNOT BE SWAPPED WITHOUT REWRITING THE SENTENCE.**
    **S145's corollary is REVOKED as a general rule (S146). Recompute the deltas from the
    compiles every time. S147 CONFIRMS IT AGAIN: L14 moved +170 at the top and +176 at the
    bottom, and two of its three deltas changed.**
50. **A COUNT INSIDE A SENTENCE IS A CLAIM. DERIVE IT OR DELETE IT.** **S147: L14 carries three
    — *260 lines*, *twelve-item*, and *830 bytes*. Measured 108, 11, and unmeasurable.**
51. **A GATE THAT CERTIFIES AGREEMENT IS NOT CERTIFYING CORRECTNESS.** **S147: `next_pointer`
    passes green while emitting a title L15 abandoned, because it certifies the block against
    the strip and nothing certifies the strip.**
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
62. **AN EXPLANATION CAN BE WRONG WITHOUT ANY NUMBER BEING WRONG.** **S147's second instance:
    L14 Step 3 names a cost of 830 beside a measured 744 — but even at 744 the sentence would
    need checking, because the thing it claims to price has no symbol in the binary at all.**
63. **NEW, S147: A CITATION IS A CLAIM ABOUT AN EDITION, NOT ABOUT A NUMBER.** Two citations
    of the same rule that disagree are not a typo — they are two editions in one document.
    **Do not pick the more common one. Go to the rulebook's changes list and find out what got
    inserted.** RCJ 2025 added *§4.1 Terms and Definitions* and pushed all of Section 4 down
    by one; every §4.x number in the book is a 2024 number. **Cite the edition inline so the
    next reader can date the claim without re-deriving it.**
64. **NEW, S147: A FILE NAMED FOR A YEAR IS NOT EVIDENCE OF THAT YEAR.**
    `ROBOCUP_RESCUE_LINE_2026.md` is the **2025** ruleset in full, and it is the file the book
    checks itself against. **Every claim it certified inherited its edition.**
65. **NEW, S147: CHECK THE LEAGUE BEFORE THE EDITION.** A document can be the newest, be
    genuinely from this summer's championship, and still be **a different competition**. The
    *RoboCup Rescue Robot League 2026D* upload is the major league — 80 kg teleoperated robots
    on stepfields. Mining it for Junior rules would have put research-league specs in a
    student textbook. **Read the league name and the scenario before the section numbers.**
66. **NEW, S147: A REGIONAL VARIANT IS A DIFFERENT GAME, NOT A REPRINT.** RCAP U19 is
    *"based on the RoboCup Junior Rescue Line Rules 2025"* and still deletes the black victim,
    the red evacuation point, and ramps entirely. **A derived ruleset agreeing on one section's
    numbering is not evidence it agrees on the field. Diff it before trusting any part of it.**
