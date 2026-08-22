# ZUMO — S183 HANDOFF (written at S182 close · paste at top of Session 183)

## READ THIS FIRST

**S182's work IS PUSHABLE and DJ verifies the push himself (standing ruling, S158).**
`git rm ZUMO_S182_HANDOFF.md` is part of that push. If `__pycache__/` exists, delete it LAST.

**78/78 gates** · `gate_payload_match` **PASS** (census re-pinned 221→221) · `quiz_bank --check`
**16 banks valid** · `byte_audit` **0 of 221 figures moved**, all eight standing controls exact,
`--selftest` ALL CONTROLS, `--check` and `--discards` PASS (15 over 7, all adjudicated) ·
`build_css`/`image_audit`/`build_worklist --check` current · `callout_id` **1133** ·
`build_family_map` **1133/1133** UNASSIGNED 0 · `strip_inline --verify` **0 dead** ·
`session_versions --currency` **0 unbumped**.

**AFTER THE PUSH, `site_parity` WILL NOT TELL YOU THE LESSONS LANDED (S181 §3). md5 the changed
PAGES against a cache-busted fetch.** Eight lessons changed this session.

---

# 1. THE NINE SECTIONS — DJ'S RULINGS, ALL FILED IN BIBLE §18.3a

| | Ruling |
|---|---|
| Order | header box · `INCLUDES` · `HARDWARE OBJECTS` · `CONSTANTS` · `GLOBAL VARIABLES` · `FUNCTION PROTOTYPES` · `SETUP` · `MAIN LOOP` · `HELPER FUNCTIONS` |
| Retired | `CONFIGURATION` → `CONSTANTS` · `STATE VARIABLES` → `GLOBAL VARIABLES` · bare `LOOP` → `MAIN LOOP` |
| Helpers | **below `loop()`**, so the prototype is load-bearing |
| Coverage | all eight banners in every full-program starter AND every bonus challenge |
| Exempt | **one payload**: L02 `broken_code`, already `data-nobuild` (§16.23) |
| MY PLAN | ships **L02–L09 only** |
| Header comment | keeps its `// ┌────` box, NOT a `// =====` banner |

**THE POPULATION WAS THE FINDING.** L02 and L06 shipped no `GLOBAL VARIABLES`, L03 no
`FUNCTION PROTOTYPES`, L04 the right set in the WRONG ORDER. **Only L04 obeyed §18.3, which had
declared the order canonical since S48.**

**TWO LIVE DEFECTS FELL OUT OF THE ABSENCE.** L06's odometer challenge told students to put
`totalDistance`, `prevLeft`, `prevRight` — all mutable — **in the CONFIGURATION section**, naming a
wrong home outright. And **all eleven L01 challenge files shipped `#include <EEPROM.h>` stranded
inside CONSTANTS**, the only misplaced include in the book, in the files students open first.

**ZERO BYTES, PROVED THREE TIMES.** Baseline compiled BEFORE the pass with `11/after_step_1` at
**20,592** reproduced first (rule 30); all 221 recompiled after: **0 figures moved**, eight controls
exact, `16/after_step_2` tightest at **28,648 / 24 spare**. The nine added prototypes cost nothing.

---

# 2. WHAT THE INSTRUMENTS CAUGHT THAT I DID NOT

**1. `session_versions --currency` WAS CRASHING AND SILENCING ITSELF.** It decoded `git show` as
UTF-8 and died with `UnicodeDecodeError` on the regenerated `.png` — **taking the check for all 22
other files with it.** First binary change since the arm shipped at S172, which is why it had never
fired. Reads bytes now; **v1.30.2**, blinding-controlled both ways.

**2. §27.8b's CYCLE WAS OWED FOR THE FIRST TIME IN FIVE SESSIONS.** My two new `<h4>` elements in
L02 §5 tipped the frequency ranking and **`.h4-c-433014` and `.h4-c-433014-2` TRADED their
`margin-top: 25px`**. The order-only proof is what caught it — it had printed *maps identical* three
times earlier the same session, which is exactly when you stop reading it. Cycle run in full with
`--include-held`; acceptance test was **22,963 elements, 0 resolved-styling changes**, and the blast
radius included **L01, L14 and L16 — three lessons I never edited.**

**3. THE MAKER BADGE READ v2.64 AGAINST A FILE READING v2.65** — the S160 defect recurring, the one
string in the Maker a student reads. **v2.65 has NO changelog entry**; deliberately NOT back-filled
(S159). Now v2.66 in all three homes.

**4. TWO BANK DEFECTS, BOTH AUTHORED FAITHFULLY FROM A LESSON SINCE CORRECTED.**
`L02_B02` asked *which row is unnumbered* — a question with no answer now. **`L03_B36` keyed
*"defines its helper functions above `setup()`"*, the exact sentence the ruling reversed** — a
student reading the live L03 would be marked wrong (v8.130). Both re-keyed, retired claims kept as
the strongest distractors.

**5. AND `QUIZ_L02`'s HEADER HAD ALREADY CHECKED B02 AND RULED IT SAFE.** *"B02's seven numbered
sections and one unnumbered row still holds."* **That note is why it survived** — the next reader
trusts the record instead of the artefact (§16.30). Left standing as provenance with the overturn
recorded beneath it.

---

# 3. PARSER TRAPS — REUSABLE, ALL CAUGHT BY CONTROLS

- **`// ==================== MY PLAN ====================` MATCHED THE BANNER REGEX** and was
  mangled into a section name. Tightened to require a real name — then **all 63 already-applied
  payloads were re-derived under the tightened parser and 0 disagreed**, because output from a
  parser you have since changed is not verified.
- **A LINE-WISE PREDICATE CANNOT SEE A WRAPPED DECLARATION.** `const float COUNTS_PER_DEGREE = (…) *`
  wraps; the first arm read the continuation alone and reported 5 false mismatches — meaning it was
  **SILENT on a wrapped mutable declaration.** Rebuilt continuation-aware, wrapped plant added.
- **A SPECIMEN CAUGHT WHAT THE INVARIANT COULD NOT.** The first rebuild put `Zumo32U4Buzzer buzzer;`
  ABOVE the HARDWARE OBJECTS banner while that banner read *(none needed)*. Now filed by WHAT A LINE
  IS, never where it sits. **Generate one real file and look at it.**
- **`grep -c` COUNTS LINES, NOT OCCURRENCES** (rule 84). It reported 3 stale references in L02 where
  there were 6.
- **I INVENTED A CSS CLASS** (`pre-bg-1e1e1e`) that follows the book's naming scheme perfectly and
  does not exist. §27 named it immediately.

---

# 4. S183 OPENS HERE

**THE GPT LIST IS STILL THE ASSIGNMENT. DJ: *"I can't ship a book with errors in it."***
**DJ's S182 scope ruling: NO further work on L13–L16 until L01–L08 are done.**

**L03 §5.1 WAS A DELIBERATE TEACHING CHOICE, NOT DRIFT** — it documented helpers-above-`setup()`
with a stated reason. The ruling overrode it and the rewrite keeps *both layouts are common,
recognize either* while explaining why this book picks one. If that reads wrong in class, that is
the sentence to revisit.

**NOT DONE, AND KNOWN:**
- **L02 §5's walkthrough is complete at nine**, but no other lesson's walkthrough was audited for
  the same gap.
- **`svg_layout_audit` reports one finding on the anatomy SVG — it is INHERITED**, identical on the
  original at 7 markers. Not mine, not fixed.
- The notebook card is now **landscape (1800×1280)** where it was near-square, because it is the
  diagram at 2× rather than a second layout. DJ has seen it; flag if the shape matters.

## §24.22 IS NEW CANON AND `prose_canon.py` IS S183's FIRST INSTRUMENT JOB

**§24.22 (Bible v8.177): a claim-type sweep is not done until the POPULATION is enumerated and every
member adjudicated. A grep that finds zero has not found zero — it has found nothing.**

**It is earned by four consecutive failures in S182**, each pass reported clean and each recheck
finding a NEW class: banner names → section counts → printed banner SEQUENCES → placement claims.
The fourth found **six defects in L03, the lesson already twice declared fixed**, one of which had
broken Step 12's deliberate red-build.

**`prose_canon.py` IS OWED AND DELIBERATELY NOT BUILT.** Four arms exist as throwaway scripts from
S182 and all four found real defects: printed banner sequences vs canon · placement claims ·
retired names · section-count claims. **Do not ship it without a control per arm** — plant a stale
claim and confirm it fires, plant a legitimate one and confirm it is SILENT (§16.50: S181's
`session_versions` arm had a hole precisely because it was added under time pressure). The residue
needs a pin table with a one-line reason each: L15's own `THE SPEED LOOP` sections, *"AN OPEN
HEADING LOOP"*, *"CLOSED-LOOP control"*, and L03's deliberate *"you will meet code written that
way"* framing.

**THE GAP IT CLOSES: ALL 78 GATES RUN PAYLOAD → LESSON.** `gate_payload_match` is a SUBSET test
(§16.45), so a lesson can carry any number of lines no payload has and stale prose is invisible to
the whole suite. **Every S182 defect travelled lesson → canon.** This would be the first arm
running that direction.

## STANDING, UNCHANGED
- **`gate_payload_match` IS STILL NOT ONE OF THE 78** (S137).
- **`byte_audit` ARM 2 CANNOT SEE A FIGURE IN PROSE.**
- **A GATE FOR `GPT_WORKLIST.md`** (S174). **§16.32–§16.44 STILL HAVE NO NUMBERED BODIES.**
- **Fall launch Sept 8.**

# HARNESS — NOT IN THE REPO. RUN THE SCRIPT.

```
apt-get install -y gcc-avr avr-libc
sh harness_setup.sh                     # objects: 41  AND  core stderr: clean
python3 byte_audit.py --sizes           # ~4 min at 221 payloads
python3 byte_audit.py --selftest ; --check ; --discards
```
**`--selftest` CANNOT RUN BEFORE `--sizes`** — CONTROL K reaches for `16/finished` in the size table
and dies with a `KeyError`. The setup script's closing text implies otherwise. It does not.

**STANDING CONTROLS, ALL REPRODUCED S182:** `11/after_step_1` **20,592** · `11/finished` **20,778** ·
`12/finished` **24,790** · `12/c2_slipalarm` **21,334** · `13/finished` **25,248** ·
`14/finished` **26,002** · `15/finished` **28,406** · `16/finished` **28,626**.

# STANDING AUTHORITY — §24.17, §24.19, §24.21
**Decide and report; do not ask.** Carve-outs: facts about the ROOM · irreversible moves · RoboLore
brand and course scope. **§24.19 is the tiebreaker** — what is best for student learning.

---
<!-- VERSION BLOCK: emitted by session_versions.py --handoff. Never hand-typed. -->
Fresh-clone verified at **`99b567f`**. Census **41,743**.
Bible **v8.177** · `BookComponentStandard` **v01.13.0** · Maker **v2.66** ·
`marks/` **41** · `icons/` **49** incl. LICENSE.
`ZUMO_Syllabus_WORKING.md` **v1.3**.

Instruments: `book_gates` **v1.72.19** · `lesson_inventory` **v1.3.5** ·
`gen_component` **v1.6.1** · `pill_sweep` **v1.1** · `gate_payload_match` **v1.9.2** ·
`build_family_map` **v1.6.6.3** · `callout_id` **v1.0** · `keyterm_prefix` **v1.0.1** · `build_mark_index` **v1.1.0** · `gen_bonus_banner` **v1.4.1** ·
`gen_part_banners` **v1.2** · `session_versions` **v1.30.2** · `fit_raster_svg` **v1.2** ·
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

Lessons: L01 v03.31.4 · L02 v03.25.0 · L03 v03.46.1 · L04 v04.29.5 · L05 v04.29.3 · L06 v04.34.0 · L07 v04.31.8 · L08 v04.32.1 · L09 v05.27.4 · L10 v02.30.3 · L11 v02.31.1 · L12 v01.35.2 · L13 v02.39.0 · L14 v02.36.2 · L15 v02.32.0 · L16 v02.28.1.
