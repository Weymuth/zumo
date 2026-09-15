# ZUMO — S203 HANDOFF (written at S202 close · paste at top of Session 203)

## READ THIS FIRST

**THIS SENTENCE CANNOT TELL YOU WHETHER S202 IS PUSHED — READ THE DIFF.** It was wrong four sessions
running (S198–S201) and at S202 open it was wrong again in the same direction: S201's batch **was**
already live at `4b20953`. **The artefact is the answer** (S197). S202's own batch was handed to DJ as
a zip and was NOT pushed at the moment this was written, which is exactly why this line is worthless.

**COUNT THE DIFF; DO NOT TRUST THIS LINE.** S202 changed **39 files**, counted from
`git status --porcelain`. **No files added, none deleted except `ZUMO_S202_HANDOFF.md`.** No new
directories. If the count differs, a later batch landed and is not described here.

**FIFTEEN LESSONS CHANGED BY A HANDFUL OF LINES EACH AND ONE DID NOT.** All sixteen gained a TUTOR
pill; **L03 alone carries content edits** (§5.4). **If a lesson other than L03 shows a content change,
stop and look.** All 16 quiz banks moved because all 16 lessons bumped.

---

# 1. WHAT S202 DID

**THE §6.5a STRIP HAS A TUTOR PILL, IN ALL SIXTEEN LESSONS.** DJ ruled it. `TUTOR` sits between
`DEEPER` and the ⌂ home square, pointing at `../tutor/tutor.html`, on the v8.53 DEEPER precedent —
the strip already reached outside `lessons/`, so nothing structural was invented. `tutor.html` gains
a matching back-link to the book, styled from its own `<style>` block so it never touches `book.css`.

**REUSING AN EXISTING CLASS IS WHY THE STYLESHEET MOVE WAS SAFE.** The pill uses
`link-bc-rgba2552`, so no rule could be born. Proved before the baseline moved: **574 rules / 2,033
declarations at both ends, ZERO born, died or altered**, every declaration block byte-identical. The
whole 19-line diff is the header census 23,022 → 23,038 — **+16, exactly one link per lesson, the
number checking itself** — plus ONE rank swap as `.link-bc-rgba2552` rises ×288 → ×304 past
`.tok-4ec9b6` at ×302. §27.8b's cycle was **NOT** owed.

**THE STRIP GATE WAS CONTROL-RUN BOTH WAYS.** Hand-varying one lesson's `title=` fired **§6.5a AND
§3.1b** — a drifted strip means the next-pointer titles cannot be derived, which is a second gate
nobody would have predicted. Restored **from a byte copy taken before the injection, not
`git checkout`** (S201's lesson), verified byte-exact by SHA.

**`tutor/tutor.html` IS NOW A TRACKED ARTEFACT** at v1.1.1, and `tutor/` was removed from
`session_versions`' own selftest scratch-copy exclusions — an artefact you track cannot be one you
hide from your controls. **CONTROL G CAUGHT THE HALF-DONE JOB:** registering it without adding it to
BOTH emitted blocks left it tracked but invisible to `--live` and `--handoff`. The selftest said so
before anything shipped.

## THE ONE DJ'S ROOM FOUND THAT NO INSTRUMENT COULD

**L03 §5.4 COULD NOT BE FOLLOWED.** DJ reported the Section 5 pseudo-code as unclear. §5 contains **no
pseudo-code** — the defect was arithmetic. §5.4 opened *"you'll write **four** helper functions"*,
listed **four** table rows, then said **"all five"** twice and printed **five** prototypes.
`printInstructions()` appeared **exactly once in all of §5**, as a bare name inside the block that
calls itself *"the whole of it"*, where the other four appeared twice each. The finished program has
**five** helpers, so "four" was the wrong number and the table was the incomplete home. **AND THE
BLOCK'S ORDER WAS WRONG** — it led with `runMotorTest()` where the built file ends with it. Row added,
count corrected, order corrected and **asserted by extracting both lists and comparing, not by eye.**

**THE COUNT/ENUMERATION GATE WAS PROBED AND NOT BUILT — DJ RULED "add it later if we find more
examples."** Broad shape priced **226 claims, flagged 156**, and the three strongest hand-checked
**CLEAN**. Narrow shape is clean but has a population of **8 prototypes in one lesson**, and a gate
that scans almost nothing passes for the wrong reason. **THE TRIGGER IS MORE INSTANCES, NOT MORE
CLEVERNESS.** Probe script deliberately not committed.
**DO NOT "FIX" L07's *"Eight organized files"* OVER FIVE BULLETS — IT IS CORRECT.** Three bullets name
`.h`/`.cpp` pairs: 1+1+2+2+2 = 8. Any future check of this shape will flag it.

## MEASURED, NOT FIXED
**`site_parity` COMPARES BYTE COUNTS, NOT BYTES.** The regenerated `book.css` is **84,994 bytes at
both ends** — a rank swap moves a block and the census digits are equal-width — so parity printed
PARITY on a stylesheet whose content had changed. A second S181-class scope limit in the same
instrument. **Never use file size to decide whether `book.css` copied; use the §27.11 digest.**

---

# 2. S203 OPENS HERE

**FOUR RULINGS ARE OWED BY DJ AND ALL FOUR ARE ABOUT LESSON 3.** S202 measured them and did not
decide them:

1. **HOW MANY PERIODS L03 GETS.** It currently gets two (Pd 5–6) and Pd 6 loses ~20 min to M1 demos,
   so ~110 min for **8,589 words of reading and a 232-line program** — against L02's 130 clean
   minutes for 6,428 words and 97 lines. **Three is the honest floor unless something is cut.**
2. **WHETHER §5.5 AND §5.6 LEAVE THE READING SCOPE.** 1,677 words, 20% of the assigned reading, and
   both are **L02 material** — `if`, comparison, `=` vs `==`, three ways to add one. Added July 20;
   the only structural addition to L03's reading scope in its whole history.
3. **WHETHER THE M1 DEMO MOVES OFF PERIOD 6** to Pd 9 (Fri Sep 25, a 30-minute catch-up day with
   nothing assigned). That alone makes L03 a clean two periods.
4. **WHETHER §6's EIGHT PLANS GET RENUMBERED.** L02's four pseudo-code blocks carry **18 numbered
   items**; L03's eight carry **ONE**. The MY PLAN block every student downloads is pre-printed
   `1. 2. 3. 4.`, and §6 tells them to copy the plan into it — so L02's habit has nothing to practise
   on in L03. L03 also introduces `settings →` and `memory →`, which appear nowhere in L02 and are
   never taught. **Worst is Step 11 `loop()`** — Serial-connect check, held-button reset, three
   debounced branches and a redraw, as unnumbered compound clauses.

**L03's READING SCOPE GREW 76% AND WAS NEVER ONCE CUT** — 4,885 → 8,589 words over six sessions,
each adding ~300. **L02 is the only lesson in the book that ever got shorter** (−12%). L04 drops back
to 6,475, so L03 is a spike, not a trend. **No single session made it hard.**

**PERIOD 7 (Mon Sep 21) TALKING POINTS STILL SAY "Build the test surfaces."** That contradicts the
S201 tile ruling, which took surface-building out of L04 §4.3 and closed the poster-board purchase.
**UNFIXED — it will teach wrong on Sep 21.** S202 flagged it and did not touch it.

**BELL-RINGERS.** S202 built a twelve-question **L02** spoken set and a Period 4 page, both delivered
as files **outside the repo** (the page would trip §12/§23 as a stray). **L01's original twelve
questions are still lost** — `ZUMO_BELL_RINGERS.md` was never committed by S201 and the five rules it
held are unrecoverable. L03–L16 unbuilt.

**THE SHOOT LIST DID NOT CLOSE.** Derived, not read: **14 outstanding of 144 planned**, unchanged
from S201 close. `ZUMO_SHOOT_LIST_F26_Sep3.md` was dated Thursday Sep 3. **Filenames must be
`L##_IMAGE_#-0#_snake_name.jpg` or `image_audit` will not see them.**

**CANVAS, DJ's HANDS.** L03 QTI closes **Wed Sep 16, 9:50 AM**; L04 QTI closes **Mon Sep 21, 1:15 PM**.

## AND THESE ARE OWED, UNCHANGED FROM S202
- **THE FOUR L05 ORPHANS — NEEDS DJ (irreversible).** 31 unreferenced files total.
- **The `(none needed)` ruling (S183) is unbuilt** — 133 sites, every one L01–L07. **NEEDS DJ.**
- **The notebook Google Doc link** (`ZUMO_Syllabus_WORKING.md` line 103). **NEEDS DJ.**
- **`ZUMO_BENCH_TESTS.md` CARRIES NONE OF THE MEASURED NUMBERS.** Migrating S196's results is a real
  job. Until it is done, do not delete a closed row from the flagged-checks sheet.
- **NINE BENCH ROWS REMAIN, SIX NEED ONLY A DESK** — F1, F3, F4, F6, F7 (Windows), F8. F2 needs floor.
  **F15 needed tape and the tile ruling may have retired it — check before running it.**
- **`F9` HAS NEVER HAD A WHY COLUMN.** Carried since S41.
- **`Q017`/`L09-B1` — the oldest bench row in the project, open since S41** — now wants white, black,
  the competition marker and each comparison green, plus both gaps. **A null result is a finding.**
- **`going_deeper.html` AND `index.html` REPORT "no version home"** although both carry one in a
  comment. Registering them is a small job nobody has done. **The tutor was just registered; these
  two are the same shape and the method is now demonstrated.**
- **THE LESSON `<title>` TAGS STILL END `— Zumo 32U4 Robotics`.** Gate-71 territory, **DJ's call.**
- **`ROBOLORE_BRAND_CARD_S201.md` NAMES TWO STALE FILES AND NEITHER IS FIXED.** `BookComponentStandard`
  §5.0 still prints the five Heritage Blue hexes S102 withdrew; `ROBOLORE_GRAPHICS_CHAT_HANDOFF.md` §7
  still carries the released palette park. **Approved five: `#0B1A2E` · `#3D5266` · `#7B6240` ·
  `#C9A463` · `#F5F2E9`.** DJ was asked fix-or-cite-around and has not ruled.
- **TALKING POINTS EXIST FOR PERIODS 1–8.** Periods 9–12 are next: the Sep 25 buffer, L05 with the
  **M2 demo**, and L06 Encoders ⭐ where the course turns closed-loop.
- **WORKLIST TALLY — derived by `census.worklist()`, unmoved: 103 closed / 96 fixed / 2 parked /
  140 open of 245.** S202 touched no worklist row.

---

# 3. STANDING
- **INSTALL THE TRIPWIRE AT SESSION OPEN:** `bash tools/no_text_match.sh install` then `selftest`.
  It does NOT survive a container rebuild.
- **USE THE PARSER, NOT A TEXT MATCH** (§24.22). **A count comes with its population or it does not come.**
- **A NAME THAT RESOLVES TWICE IS TWO FILES (S200).** Search by path.
- **THE YEAR LAYER IS `_F26` (S199).** The book carries no calendar (Bible §3.1).
- **THE READING QUIZ DRAWS FROM §1–§5 ONLY (S200).** **L01 IS `--check` ONLY AND CANNOT BE REBUILT.**
- **THE BOOK IS *SENSE, DECIDE, ACT* (S201).** Imprint RoboLore, © DJ Weymuth, never `LLC` or `Inc`.
- **A FLAG OUTLIVES ITS RESOLUTION UNLESS THE RESOLUTION EDITS IT (S201).**
- **A `git checkout` IS NOT A RESTORE ON A TREE WITH UNCOMMITTED WORK (S201).** Take a byte copy first.
- **AN EDIT SCRIPT THAT DIES ON AN ASSERT WRITES NOTHING — AND THE GREEN RUN AFTER IT MEANS NOTHING
  (S201).** A control that fails to plant reads exactly like one that passed.
- **A RESIDUE CHECK FAILS WHEN THE NEW STRING CONTAINS THE OLD ONE (S201).**
- **BUMPING A LESSON REPINS ITS BANKS, AND A REPINNED BANK IS AN UNBUMPED EDIT (S201).** `--currency`
  catches every one. **A BANK VERSION HAS TWO HOMES** — the comment AND the `bank_version` field.
  **A SOURCE PIN IS READ BEFORE IT IS BUMPED** (rule 37) — S202 enforced this by assertion, not care.
- **NO FIGURE CAN BE WIRED ANYWHERE IN THE BOOK RIGHT NOW (S201).** `build_css` two-cycles. The
  documented remedy **breaks an untouched clone**. Reproduce before believing anything else about it.
  **S202 regenerated `book.css` twice with no trouble — plain `build_css.py` is not the hazard;
  `strip_inline --restore` is.**
- **A NEW `.html` ANYWHERE IN THE TREE IS A STRAY (S202).** §12/§23 enumerates every page it will
  accept, twenty-two of them. Adding one means declaring it in `EXPECTED` — a decision, not a chore.
- **`gate_payload_match` IS NOT ONE OF THE GATES** and **TAKES ARGUMENTS**.
- **`--update-census` PRINTS a replacement table; it does not write one.**
- **`pio_harness.sh` NEEDS `bash`, NOT `sh`.** It takes a **DIRECTORY**, not a file.
- **`--live` and `--handoff` PRINT, they do not WRITE** (§24.20). LIVE.md carries TWO
  `**Versions:**` lines — **line 6 is current**. Keep Status to ONE line.
- **LIVE.md's CURRENT-SESSION REGION MUST STATE THE WORKLIST TALLY (S202).** §24.24 fails with *"states
  no tally at all"* if it does not, and §16.44 and §24.24 both need a `## WHAT SHIPPED IN S###` block
  matching the header's session number before they can resolve their scope at all.
- **A BIBLE BUMP IS A REGENERATION OBLIGATION** (S175) and **HAS TWO HOMES** (S185) — plus a line in
  the running changelog at the top. **One session is one entry; extend it, do not bump twice.**
- **A PROJECT-FILE COPY IS NOT THE TREE** (rule 32). `/mnt/project` still carries `_v2` of the TDP
  template, an S41 handoff, and the pre-rename `_WORKING` grid and syllabus.
- **SESSION OPEN:** `git ls-remote` → fresh clone → verify the Bible's internal version **with the
  parser** → read LIVE.md → `book_gates` → `session_versions --check` and `--selftest` →
  `census --selftest` → `lesson_inventory --selftest` → `svg_layout_audit --selftest` →
  `gate_payload_match newproject.html lessons/Lesson_*.html` → `callout_id` → `retired_claims` →
  `quiz_bank --check` → `reading_quiz --check` and `--selftest` → `build_css --check` →
  `build_worklist --check` → `build_syllabus_html --check` → `prose_canon --check` and `--selftest`
  → `image_audit --check` → `site_parity` twice past the 10m57s floor.

# STANDING AUTHORITY — §24.17, §24.19, §24.21
**Decide and report; do not ask.** Carve-outs: facts about the ROOM · irreversible moves · RoboLore
brand and course scope. **§24.19 is the tiebreaker.**

---
<!-- VERSION BLOCK: emitted by session_versions.py --handoff. Never hand-typed. -->
Fresh-clone verified at **`4b20953`**. Census **41,870**.
Bible **v8.201** · `BookComponentStandard` **v01.13.0** · Maker **v2.72** ·
`marks/` **41** · `icons/` **49** incl. LICENSE.
`ZUMO_Syllabus_WORKING.md` **v1.6** · `ZUMO_Teacher_Daily_Grid_F26.md` **v2.1**.

Instruments: `book_gates` **v1.77.3** · `lesson_inventory` **v1.4.1** ·
`gen_component` **v1.6.1** · `pill_sweep` **v1.1** · `gate_payload_match` **v1.9.6** ·
`build_family_map` **v1.6.6.8** · `callout_id` **v1.0** · `keyterm_prefix` **v1.0.1** · `build_mark_index` **v1.1.0** · `gen_bonus_banner` **v1.4.1** ·
`gen_part_banners` **v1.2** · `session_versions` **v1.37.0** · `fit_raster_svg` **v1.2** ·
`flatten_alpha` **v1.2** · `svg_layout_audit` **v1.23** · `site_parity` **v1.2.1** ·
`build_css` **v1.4.0** · `build_syllabus_html` **1.1** ·
`image_audit` **v1.3** ·
`strip_inline` **v1.2** ·
`build_worklist` **v1.2** ·
`qti_export` **1.2** ·
`reading_quiz` **v1.0** ·
`prose_canon` **v1.4.0** ·
`retired_claims` **v1.3.1** ·
`census` **v1.3.0** ·
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
`tutor/tutor.html` **v1.1.1** ·
`harness_setup.sh` **v1.1** ·
`pio_harness.sh` **v3.1** ·
`going_deeper` **v01.7.0**.

Lessons: L01 v03.33.1 · L02 v03.27.1 · L03 v03.48.2 · L04 v04.31.1 · L05 v04.31.1 · L06 v04.38.1 · L07 v04.34.1 · L08 v04.35.1 · L09 v05.30.1 · L10 v02.31.1 · L11 v02.32.1 · L12 v01.36.1 · L13 v02.40.1 · L14 v02.37.1 · L15 v02.33.1 · L16 v02.29.1.
