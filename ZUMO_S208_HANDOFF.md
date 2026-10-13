# ZUMO — S208 HANDOFF (written at S207 close · paste at top of Session 208)

## READ THIS FIRST

**THIS SENTENCE CANNOT TELL YOU WHETHER S207 IS PUSHED — READ THE DIFF.** The artefact is the answer (S197).

**COUNT THE DIFF; DO NOT TRUST THIS LINE.** S207 touched **6 paths**: **4 modified** — `LIVE_ZUMO_TEXTBOOK.md`,
`ZUMO_SUPER_BIBLE.md`, `tutor/worker.js`, `GPT_WORKLIST.md` (session stamp S206 → S207 only) — plus **one added** (this handoff) and **one deleted**
(`ZUMO_S207_HANDOFF.md`). **No lesson, bank, CSS, grid or syllabus file. No new `.html`.** If the count differs,
a later batch landed and is not described here.

---

# 1. WHAT S207 DID

**THE BOOK DID NOT MOVE — THAT WAS THE RULING.** The class asked to fold in Robotics I planning and building.
DJ: read and code for a stretch, **stop and build, return to the book**, breaks probably after milestones,
**book finished by end of Trimester 2**. *"You aren't adjusting anything"* — grid and syllabus untouched until DJ
rules a schedule. Bible **v8.203**.

**THE BUILD IS THE NEWMO** (new + Zumo), a custom robot. **Nothing about its hardware is locked.**

**THE TUTOR'S "CREDIT TOO LOW" WAS A KEY FROM OUTSIDE DJ'S ORG.** DJ's Org held $24.76. New key
`zumosupport-tutor` (DJ's Org, Default workspace) fixed it, verified live. **`tutor/worker.js` → v3.1**, which also
serves the Bot Builder via `mode:"builder"`; the tutor path is byte-identical to v3 (proved against a stub).
Deployed on Cloudflare and verified at S207 close: one tutor call, one builder call.

**BOT BUILDER BUILT** — 12 stages from DJ's *Vortex Build Process — Extracted v1.0*, notebook per stage saved on
the student's computer, "Done when" gate, coach chat. Own repo **`Weymuth/BotBuilder`**, served at
**`weymuth.github.io/BotBuilder/`** (capital B's — the lowercase URL 404s).

**MADE OUTSIDE THE REPO (v1.0, RoboLore styled, PDFs delivered):** *Rescue Line Robot Specs*, *Ramps, Bumps and
Traction*, *Zumo Baseline Tests*.

**THE KEY TRAP, SO IT IS NOT RELIVED.** The Console now mints identity-backed `sk-ant-usr-` keys; three pasted
into a fresh `botbuilder` worker were all rejected, under both `x-api-key` and `Bearer`. The fix was to stop
minting keys and route the Bot Builder through the working worker. **A new tool rides `zumosupport` first.**

---

# 2. S208 OPENS HERE

**FIRST — THE BOT BUILDER PAGE IS STILL v1.0 IN ITS REPO.** At S207 close `Weymuth/BotBuilder` held v1.0, which
calls the dead `botbuilder` worker, so "Ask the coach" fails for students. **Upload `index.html` v1.1** (points at
`zumosupport`, sends `mode:"builder"`) via github.com → Add file → Upload files. Verify by one builder call from
the live page. **DO NOT GUESS whether DJ has done it — check the repo.**

**OPEN — NEEDS DJ, DO NOT GUESS:**
- **Lite mode (§27.15g):** has the class seen L06's switch, and do they want it in L07–L16?
- **Build-break schedule:** which milestones, how long. Grid untouched until ruled.
- **Newmo hardware:** gear ratio (DJ thinks the class Zumos are 75:1 — unconfirmed), motor (20D vs 25D),
  driver (MAX14870 if 20D; a bigger one if 25D HP), battery (3S for 12 V motors), OLED needs a level shifter.
- **Rescue Line Robot Specs:** two rows read "check PDF" (no-mains, no-drones section numbers).
- **Zumo Baseline Tests:** whether the free idler end sits level with wheels on; whether the 75:1 gearbox
  back-drives in the tilt test.
- **File-naming CODE / Type** for the three handouts under DJ's naming rule.

**CLEAN-UP, DJ'S HANDS:** delete the `botbuilder` Cloudflare worker and any `sk-ant-usr-` botbuilder keys in the
Console. **DJ deleted the old legacy key `ANTHROPIC_API_KEY` (`sk-ant-api03-ZYV…`) at S207** — the tutor never
used it, but it had $0.21 of use; **if `capstone-planner` or `zumoauth` break, that is why.** Auto-reload is off
and the spend limit is $1,000 — DJ was advised to change both.

## AND THESE ARE STILL OWED (carried from S207's handoff, unchanged)
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

**Today's task:** ______________________________________________

---
<!-- VERSION BLOCK: emitted by session_versions.py --handoff. Never hand-typed. -->
Fresh-clone verified at **`15be698`**. Census **41,938**.
Bible **v8.203** · `BookComponentStandard` **v01.13.0** · Maker **v2.72** ·
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
