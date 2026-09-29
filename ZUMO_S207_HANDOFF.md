# ZUMO — S207 HANDOFF (written at S206 close · paste at top of Session 207)

## READ THIS FIRST

**THIS SENTENCE CANNOT TELL YOU WHETHER S206 IS PUSHED — READ THE DIFF.** It was wrong five sessions
running (S198–S202) and at S203 open it was wrong again in the same direction: S202's batch **was**
already live. **The artefact is the answer** (S197). At the moment this was written S206's batch was
handed to DJ as files and was NOT pushed, which is exactly why this line is worthless.

**COUNT THE DIFF; DO NOT TRUST THIS LINE.** S206 touched **16 paths**, counted from
`git status --porcelain`: **14 modified** — `LIVE_ZUMO_TEXTBOOK.md`, `ZUMO_SUPER_BIBLE.md`,
`GPT_WORKLIST.md`, `css/semantic.css`, `css/book.css`, `lessons/Lesson_06.html`, and the eight banks
`ZUMO_QUIZ_L06/L07/L09/L10/L11/L12/L13/L15.yaml` — plus **one added** (this handoff) and **one
deleted** (`ZUMO_S203_HANDOFF.md`). No new directories, **no new `.html` anywhere**.
`GPT_WORKLIST.md` moved by exactly one line, its session stamp S202 → S206. If the count differs, a
later batch landed and is not described here.

**FIFTEEN LESSONS WERE NOT TOUCHED.** Only L06 changed. If any other lesson shows a diff, stop and look.

---

# 1. WHAT S206 DID

**LESSON 6 HAS A STANDARD/LITE READING SWITCH (§27.15g NEW).** DJ ruled it after the class reported
too much text. **The complaint was not length and the measurement says so:** L06 is 13,889 words and
is SHORTER than L01, L02, L03, L04 and L07. Density was the complaint, and DJ named the register —
*"Prob. theory/explanation prose"* — so the switch reaches **§3 and §5 only**. §3 **1,196 → 964**
words in Lite (19% lighter); §5 **2,166 → 1,383** (36%). **1,015 words across the two.** Every other
section is byte-identical in both registers.

**NOTHING IS DELETED.** 26 `data-verbose` blocks, 12 `data-lite` replacements. Browser-verified in
both registers: **79 images, 74 code blocks, 18 key terms, 12 challenges, 32 reveals** all render in
Lite exactly as in Standard. **17 browser controls pass**, including persistence across a reload.

**THE PREVIOUS ATTEMPT FAILED NINE GATES AND THE DIAGNOSIS WAS THE ENTIRE FIX.** It built the control
from inline `style=""` — which §27.12 forbids outright — and then needed a new callout family and two
hardcoded count bumps to carry it. **None of that was necessary.** §27.15's semantic layer is
hand-authored and preserved verbatim, and **§27.11's digest is SCOPED to the generated block**
precisely so a graduating rule costs no baseline. S123 wrote that scoping for this exact case.

**CONTROL-RUN BEFORE A WORD OF CONTENT WAS WRITTEN.** A throwaway comment appended to
`css/semantic.css`, then `build_css`: generated block **byte-identical at both ends — digest
`75cbd52391a95870`, 67,298 bytes** — 82/82 green. **THE SWITCH MOVED NO BASELINE AT ALL:** not the
digest, not `CSS_RULES`, not `CSS_DECLS`, not the callout count, not `NIMG_EXPECTED`.

**THE SELECTOR IS A DATA ATTRIBUTE, FOR THE THIRD TIME (§27.15b).** S128 put `class="mark"` into
markup and `build_css` re-emitted it as `.img-fs-0`; S133 hit the same wall twice with `.ul-ls-none`.
`data-verbose` / `data-lite` / `data-textmode` are invisible to the generator.

**AND THE TRAP FIRED ANYWAY, ON THE ONE CLASS THAT WAS REUSED RATHER THAN BORN.** Three Lite
paragraphs were authored `<p data-lite class="p-mb-0">` — an **existing** class, not a new one — and
**gate 45 (§27.13) failed on the next check.** Adding uses to a ranked class re-ranks it and renames
rules in untouched lessons. Dropping the class from all three cleared it.
**A NEW ELEMENT AUTHORED INTO A LESSON CARRIES NO CLASS AT ALL — NOT EVEN AN EXISTING ONE.**

**DEFAULT IS STANDARD AND IT FAILS SAFE.** `[data-lite]{display:none}` is the FIRST of the four rules,
so a reader whose JavaScript never runs gets the whole lesson, and the failure mode of a toggle — both
registers printing at once — cannot occur even before the script runs. Mode persists in `localStorage`.

**THE ANALOGIES WERE RULED ONE AT A TIME, ON DJ'S INSTRUCTION.** He declined the sweep: *"sometimes a
connection to real life needs to be there."* **Turnstile** → Lite only; it restates the sentence above
it. **Blindfolded walk** → stays in BOTH; it is the lesson's hook and IMAGE 6.1 is a picture of it.
**Odometer / mice / 3D printers** → stays; Challenge 5 is named The Odometer.

**THE SPIELBERG PASSAGE IS NOT IN LESSON 6.** DJ named it from the room; it is **L01's** LEARN box on
the five-note signal, and **Challenge 10 reads back into it** (*"You just read how Williams and
Spielberg narrowed 134,000 possibilities to one"*). Cutting it orphans a challenge. **Left alone —
DJ's call if it ever moves.**

**PIN-ONLY BUMPS, PROVED AND NOT ASSERTED (rule 37 / S167).** L06 **v04.38.1 → v04.39.0** (moderate,
both §5b homes). Seven downstream banks name `lesson_06` — **L07, L09, L10, L11, L12, L13, L15** — and
a repinned bank is an unbumped edit (S201), so each moved its own version in **both homes**. The
pin-only claim was earned by a **CLOSED DIFF**: the Standard register rendered and diffed against HEAD
with the switch chrome and version line normalised, **residue ZERO**. Not one lesson sentence was
altered — only wrapped.

---

# 2. S207 OPENS HERE

**THE EXPERIMENT IS OUTSTANDING AND IT IS THE POINT.** DJ: *"Once they do lesson 6 they can tell me if
they want the rest like it."* **Do not roll §27.15g into L07–L16 until the class has answered.** A
lesson without the switch is not in breach of it.

**IF THE ANSWER IS YES, THE COST IS KNOWN.** The CSS is done and reaches every lesson already — only
markup is needed per lesson. Budget the condensing, not the plumbing.

**THE SESSION NUMBER IS AN INFERENCE, NOT A READING.** DJ ran two sessions after S203 that pushed
nothing and left no handoff; the repo went 13 days with HEAD unmoved at `ddd35ed`. **S204 and S205 are
assumed to be those two, making this S206.** If DJ says otherwise it is a find-and-replace across
LIVE.md, the Bible entry, `css/semantic.css`, `Lesson_06.html` and eight bank notes.

**THE S203 PERIOD 7 FIX WAS NEVER PUSHED AND SEP 21 HAS PASSED.** `ZUMO_TALKING_POINTS_F26_Wk3-4.md`
is still **v1.0** in the repo with *"Build the test surfaces"* and the poster-board materials block,
both retired by the S201 tile ruling. The corrected **v1.0.1** was delivered to DJ on Sep 15 and never
landed. **It is now history, not a hazard** — but the file still teaches wrong if anyone reads it.

**THE CALENDAR HAS MOVED PAST THE GRID'S LAST CHECKED ROW.** Today is **Mon Sep 28 → Period 10**
(L05 Proximity, **M2 DEMO**). Periods 7, 8 and 9 went by with no session recording them.

## AND THESE ARE OWED, UNCHANGED FROM S203
- **THE FOUR L03 RULINGS ARE STILL OPEN** — periods, whether §5.5/§5.6 leave the reading scope, the M1
  demo move, and whether §6's eight plans get renumbered. **S203 re-measured two of them and the
  brief was wrong:** L02's reading scope is **7,716** prose words, not the 6,428 the S203 handoff
  claimed, so L03 is **~12% longer than L02, not ~34%**. The spike argument is weaker than written.
  **The real L03 defect S203 found is chunk size:** L02 §6 feeds **39 code blocks, largest 13 lines**;
  L03 §6 hands over **18 blocks, largest 61, then 53, then 46**. And L03's eight plans carry **ZERO**
  numbered items against L02's 18 — the S203 handoff said one; the count is none.
- **THE FOUR L05 ORPHANS — NEEDS DJ (irreversible).** Unreferenced files now **32**, not 31:
  `images/README.md` is in the count.
- **The `(none needed)` ruling (S183) is unbuilt** — 133 sites, every one L01–L07. **NEEDS DJ.**
- **The notebook Google Doc link** (`ZUMO_Syllabus_WORKING.md` line 103). **NEEDS DJ.**
- **`ZUMO_BENCH_TESTS.md` CARRIES NONE OF THE MEASURED NUMBERS.** Until S196's results are migrated, do
  not delete a closed row from the flagged-checks sheet.
- **NINE BENCH ROWS REMAIN, SIX NEED ONLY A DESK** — F1, F3, F4, F6, F7 (Windows), F8. F2 needs floor.
  **F15 needed tape and the tile ruling may have retired it — check before running it.**
- **`F9` HAS NEVER HAD A WHY COLUMN.** Carried since S41.
- **`Q017`/`L09-B1` — the oldest bench row in the project, open since S41.** A null result is a finding.
- **`going_deeper.html` AND `index.html` REPORT "no version home".** The tutor was registered at S202
  and these two are the same shape; the method is demonstrated.
- **THE LESSON `<title>` TAGS STILL END `— Zumo 32U4 Robotics`.** Gate-71 territory, **DJ's call.**
- **`ROBOLORE_BRAND_CARD_S201.md` NAMES TWO STALE FILES AND NEITHER IS FIXED.** Approved five:
  `#0B1A2E` · `#3D5266` · `#7B6240` · `#C9A463` · `#F5F2E9`. DJ was asked fix-or-cite-around; no ruling.
- **BELL-RINGERS ARE DEPRIORITISED.** DJ, S203: *"Bell ringers are just reviews."* For the record so it
  is not rediscovered as a crisis: **`ZUMO_BELL_RINGERS.md` IS in the repo** with L01's twelve
  questions and all five rules intact — the S203 handoff's claim that they were lost is **false**. All
  sixteen source pins read `.0` against `.1` lessons and nothing derives from the file, so the staleness
  costs nothing while it stays a review aid. S202's L02 set was delivered outside the repo and is gone.
- **THE SHOOT LIST DID NOT CLOSE.** Derived: **14 outstanding of 144 planned**, unchanged since S201.
  **Filenames must be `L##_IMAGE_#-0#_snake_name.jpg` or `image_audit` will not see them.**
- **`site_parity` HAS NOT RUN SINCE S202.** Two passes past a 10m57s floor; skipped at S203 and S206.
- **WORKLIST TALLY — derived by `census.worklist()`, unmoved: 103 closed / 96 fixed / 2 parked /
  140 open of 245.** S206 touched no worklist row.

---

# 3. STANDING
- **INSTALL THE TRIPWIRE AT SESSION OPEN:** `bash tools/no_text_match.sh install` then `selftest`.
  It does NOT survive a container rebuild.
- **USE THE PARSER, NOT A TEXT MATCH** (§24.22). **A count comes with its population or it does not come.**
  **AND A CASE-SENSITIVE ZERO IS NOT A ZERO (S206)** — `census.rendered` takes `flags=re.I`; a literal
  pattern with single spaces also misses `cast list  →  x`, which is padded. Widen before concluding.
- **A NEW ELEMENT IN A LESSON CARRIES NO CLASS AT ALL (S206).** Not even an existing one — adding uses
  re-ranks it and renames rules in untouched lessons. Gate 45 catches it; nothing else will.
- **THE SEMANTIC LAYER IS FREE AND THE GENERATED BLOCK IS NOT (S206).** `css/semantic.css` is
  hand-authored, preserved verbatim, and outside §27.11's digest scope. Attribute selectors there cost
  no baseline. That is the route for anything new.
- **`strip_inline --restore` IS THE LANDMINE, NOT `build_css` (S202).** Plain `build_css.py` regenerated
  cleanly four times across S202 and S206.
- **A NEW `.html` ANYWHERE IN THE TREE IS A STRAY (S202).** §12/§23 enumerates twenty-two pages.
  **S206 needed none** — the switch lives inside `Lesson_06.html`.
- **A NAME THAT RESOLVES TWICE IS TWO FILES (S200).** Search by path.
- **THE YEAR LAYER IS `_F26` (S199).** The book carries no calendar (Bible §3.1).
- **THE READING QUIZ DRAWS FROM §1–§5 ONLY (S200).** **L01 IS `--check` ONLY AND CANNOT BE REBUILT.**
- **THE BOOK IS *SENSE, DECIDE, ACT* (S201).** Imprint RoboLore, © DJ Weymuth, never `LLC` or `Inc`.
- **A FLAG OUTLIVES ITS RESOLUTION UNLESS THE RESOLUTION EDITS IT (S201).**
- **A `git checkout` IS NOT A RESTORE ON A TREE WITH UNCOMMITTED WORK (S201).** Take a byte copy first.
- **AN EDIT SCRIPT THAT DIES ON AN ASSERT WRITES NOTHING (S201)** — and that is the feature. S206's
  stage C died twice on anchor asserts and left the file untouched both times.
- **BUMPING A LESSON REPINS ITS BANKS (S201).** `--currency` catches every one. **A BANK VERSION HAS TWO
  HOMES.** **A SOURCE PIN IS READ BEFORE IT IS BUMPED** (rule 37) — enforce by assertion, not care.
  **AND A PIN-ONLY CLAIM IS EARNED BY A CLOSED DIFF, NEVER BY CONFIDENCE (S206).**
- **`gate_payload_match` IS NOT ONE OF THE GATES** and **TAKES ARGUMENTS**.
- **`--update-census` PRINTS a replacement table; it does not write one.**
- **`pio_harness.sh` NEEDS `bash`, NOT `sh`.** It takes a **DIRECTORY**, not a file.
- **`--live` and `--handoff` PRINT, they do not WRITE** (§24.20). LIVE.md carries TWO
  `**Versions:**` lines — **line 6 is current**. Keep Status to ONE line.
- **LIVE.md's CURRENT-SESSION REGION MUST STATE THE WORKLIST TALLY (S202)**, and §16.44 and §24.24 both
  need a `## WHAT SHIPPED IN S###` block matching the header's session number.
- **A BIBLE BUMP IS A REGENERATION OBLIGATION** (S175) and **HAS TWO HOMES** (S185) — plus a line in
  the running changelog at the top. **One session is one entry; extend it, do not bump twice.**
- **A PROJECT-FILE COPY IS NOT THE TREE** (rule 32). `/mnt/project` still carries `_v2` of the TDP
  template, an S41 handoff, and the pre-rename `_WORKING` grid and syllabus.
- **THE PUSH IS DJ'S.** The proxy refuses `Weymuth/zumo` (403, not in the session's authorized set), so
  every deliverable is handed over as files and DJ pushes via GitHub Desktop (S34 workflow).
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
Fresh-clone verified at **`ddd35ed`**. Census **41,938**.
Bible **v8.202** · `BookComponentStandard` **v01.13.0** · Maker **v2.72** ·
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

Lessons: L01 v03.33.1 · L02 v03.27.1 · L03 v03.48.2 · L04 v04.31.1 · L05 v04.31.1 · L06 v04.39.0 · L07 v04.34.1 · L08 v04.35.1 · L09 v05.30.1 · L10 v02.31.1 · L11 v02.32.1 · L12 v01.36.1 · L13 v02.40.1 · L14 v02.37.1 · L15 v02.33.1 · L16 v02.29.1.
