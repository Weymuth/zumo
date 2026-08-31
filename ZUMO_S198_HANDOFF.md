# ZUMO — S198 HANDOFF (written at S197 close · paste at top of Session 198)

## READ THIS FIRST

**NOTHING FROM S197 IS PUSHED. 29 ENTRIES: 27 MODIFIED, 1 DELETED, 1 NEW.**
**THE DELETION IS `ZUMO_S197_HANDOFF.md` AND THE NEW FILE IS THIS ONE.** GitHub Desktop shows a
deletion as its own checkbox and it is the one most often missed — tick it. There are no new
directories this time; S196's two are already live.

**`site_parity` WILL REPORT EXACTLY ONE MISMATCH UNTIL THE PUSH LANDS** —
`images/L14_GRAPHIC_14-03_how_a_run_is_scored.svg`, site 7,388 B vs repo 7,379 B. That is the arm
working: S197 edited a published figure and the site still serves the old one. **After the push it
must return to PARITY on the second run past the 10m57s floor. If it does not, the image did not go
up** — and an image that silently fails to push is how a corrected figure keeps showing the old claim.

**`newproject.html` IS IN THE BATCH.** It is ~5.8 MB. It must go up as a file, never edited in the
GitHub web UI.

**DJ'S PLAN FOR S198: THE §16 DEBT.** 26 rules, untouched a **twelfth** session. Deferred from S197
by DJ, deliberately, not dropped.

**WORKLIST TALLY — derived by `census.worklist()`, unmoved: 103 closed / 96 fixed / 2 parked /
140 open of 245.** S197 touched no worklist row; it spent the S196 bench instead.

---

# 1. WHAT S197 DID

**S196 MEASURED; S197 SPENT THE MEASUREMENTS.** Full narrative is in LIVE.md's `WHAT SHIPPED IN
S197`. The short version:

- **F10** — L02 §9 C2's three-screen prediction and its two-trips mechanism **DELETED**, registered
  as retired claim `F10` under **two spellings**. **The wait-OUT half is still uncited and still
  wants serial timestamps** — the replacement paragraph states only the wait-IN behaviour.
  **The 15 ms debounce interval is NOT retired** — it is a real library property.
- **F14** — L03 §9 Bonus 2's reveal **rewritten**. Sign arithmetic verbatim; `2x` gone.
  `L03_A19`'s `why:` carried the same claim in other words and was fixed in the same sweep (rule 72).
- **F11** — **59 cm** landed twice in L03 §4.4. §5 Step 3's *short test run* LEFT deliberately.
- **BD1 CLOSED** — `L3/braking_test` gains a five-blink `countdown()`. **Maker v2.72.**
- **BD2 OVERRULED** — `L2/speed_limit` is NOT the same defect. No measurement to corrupt,
  hold-to-run is a dead-man switch, and **the 400 is the defect the student is asked to fix.**
- **L05 NOTE 5.47** — the jumper pad geometry (`DN4 · 4 · RGT` / `DN2 · 20 · LFT`) now appears in
  visible prose. It had lived only in `IMAGE 5.4a`'s ALT TEXT.

## THE FINDING THAT ARRIVED AFTER THE CLOSE — READ THIS ONE
**A RETIRED CLAIM WAS LIVE IN A REFERENCED FIGURE FOR SIXTEEN SESSIONS.** `L13-13` was closed at S181
with the note **"`spoken for` is 0x book-wide."** True of seventeen pages and sixteen banks; **false of
`L14_GRAPHIC_14-03_how_a_run_is_scored.svg`**, which `Lesson_14` references and the site serves. The
graphic gave *both motor drivers are spoken for, one per tread* as the reason a gripper is impossible —
the reasoning S181 retired. **L13 §8A.3 and the L14 BANK were both fixed in that pass and have said
*there is no arm* ever since. Only the figure was missed, and no instrument could see it.**
**THE ZERO WAS REAL AND THE POPULATION WAS WRONG.** `retired_claims` **v1.3.0** now sweeps the text of
every REFERENCED `.svg` (scope 17 → 122 pages). Controlled both ways on the same file: restoring the
sentence makes v1.3.0 FIRE and leaves v1.2.1 SILENT.
**IT WAS FOUND BY INSPECTING LITTER.** The probe was aimed at `L05_GRAPHIC_5-04_for_anatomy.svg`, the
last uninspected L05 orphan — which turns out to carry `L05-01`'s retired push-up analogy. That one is
UNREFERENCED and is deliberately NOT convicted: litter no student can reach is a reason to delete, not
to fail a gate. **It is now a FOURTH orphan with a named reason to go.**
**AND TWO COVERAGE CHECKS ASSERTED EQUALITY WITH 17** — `CONTROL G4` and gate 80's page count. Both
would have failed on a CORRECT widening and taught the next session to edit the number instead of
asking why it moved. G4 now derives its floor; gate 80's is one-sided (`>=`). **A coverage control that
must be hand-edited when coverage improves is a trap.**

## THE TRIPLE CHECK (six arms, thirteen controls, every one fires)
**ARM 1 COMPILE** — harness rebuilt from pinned SHAs. Payload **PASS flash=4,772 ram=182 warn=0**.
Seeded typo **FAILS**; pre-fix payload from `HEAD` **PASSES at 4,714**, so the countdown costs a
**MEASURED +58 B** and 0 RAM. **ARM 2 LIVE-SITE DIFF** — independent HTMLParser, no suite
instruments: 13 untouched lessons diff to **ZERO** against the published site, L02/L03/L05 show only
intended lines; a planted sentence in `Lesson_09` **FIRES**, so ZERO is a verdict. **ARM 3
VERSION/PIN RE-DERIVATION** — 57 source pins, 16 banks × two homes, 19/20 changed files bumped;
four seeded defects all **FIRE**.

**ARM 4 SVG DIFF** — built because arm 2 diffs PAGE text and is blind to figures, which is the blind
spot that hid `L13-13`. 105 referenced svg, 104 identical, planted node FIRES. **ARM 5 CORPUS REALITY**
— an independent HTMLParser derives the reference set a second way (105, matching); 64,959 chars
actually swept; **nine entries are textless and all nine are spiral stars**, now declared by name so a
newcomer fires. **THE LIMIT IT NAMES IS REAL AND UNCLOSABLE BY PATTERN: text flattened to outlines is
invisible to this sweep.** **ARM 6 PACKAGING** — caught `retired_claims.py` presented at v1.3.0 while
the tree held v1.3.1, and prices the handoff's own entry count against `git status`. **Its control C
had to be rebuilt twice** (its own `.bak` files were the finding; then it fired on the wrong arm) —
**a control that fires for the wrong reason is not a control.**

---

# 2. S198 OPENS HERE — THE §16 DEBT

26 rules, twelfth session carried. DJ named it at S197 close. Nothing else was promised for S198.

## AND THESE ARE OWED, UNCHANGED
- **F5 BATTERY CANON — NEEDS DJ.** Fresh **5199** against a canon of ~5400; a hard session ended at
  **5092**, still ~292 mV above canon "working". **The three-band scheme does not describe the
  fleet**, and it appears in 34 figures across L01–L03. **This is a fleet fact, not a text fix.**
- **THE FOUR L05 ORPHANS — NEEDS DJ (irreversible). NOW ALL FOUR HAVE A NAMED REASON.**
  `5-04_for_anatomy.svg` was inspected at S197 close: a for-loop anatomy diagram in the book's own
  livery, carrying **`L05-01`'s retired push-up analogy** (retired S188). Unreferenced. `5-08`, `5-09`, `5-10`, and `5-04_for_anatomy`
  are tracked, committed, and **serving HTTP 200** at `weymuth.github.io/zumo/images/`. `5-08`/`5-09`
  are the book's own `IMAGE 5.5a`/`5.5b` under a vendor wrapper whose caption contradicts §7.3.
  Delete, or leave staged? 31 unreferenced files total. `5-04_for_anatomy.svg` (5.4 KB) was never
  inspected.
- **`ZUMO_GPT_REVIEW_WORKLIST.md` footer carries a second version token** disagreeing with the header
  home `session_versions` reads. Flagged **eight** sessions, not ruled.
- **The `(none needed)` ruling (S183) is unbuilt** — 133 sites, every one L01–L07. Priced as an ADD
  of ~148 × 4, not an edit. **Needs DJ.**
- **The notebook Google Doc link** (`ZUMO_Syllabus_WORKING.md` line 103). **Needs DJ.**
- **F14 proper** would need a fresh pack and six baseline runs before any backward run, and may not
  be resolvable on a robot this well-matched. **F15** waits on DJ's own L04 build BY DESIGN — do NOT
  hand him a calibration sketch; stock `LineFollower` contains `calibrateSensors()`, the exact
  identifier whose absence is his deliberate RED build at L04 Step 5.

---

# 3. STANDING
- **INSTALL THE TRIPWIRE AT SESSION OPEN:** `bash tools/no_text_match.sh install` then `selftest`.
  It does NOT survive a container rebuild, and it does NOT cover Python `re` on raw bytes.
- **USE THE PARSER, NOT A TEXT MATCH** (§24.22). `import census` / `import lesson_inventory` work
  plainly from the repo root. **A count comes with its population or it does not come.**
- **`gate_payload_match` IS NOT ONE OF THE GATES** and **TAKES ARGUMENTS**. **NEW, S197: ITS CENSUS
  WATCHES THE PAYLOAD, NOT THE LESSON `<pre>`.** Editing a lesson listing alone leaves it GREEN.
  Observed as a control, not theorised. A known limit, not a defect — but a lesson that gains lines
  its payload never gets ships a listing the student cannot download.
- **`--update-census` PRINTS a replacement table; it does not write one.** Move the one pin by hand.
  Pasting 216 lines to move one relicenses every other drift in the same keystroke.
- **`pio_harness.sh` NEEDS `bash`, NOT `sh`** — line 94 uses a `<<<` here-string. `harness_setup.sh`
  is correctly `sh`. The harness takes a **DIRECTORY**, not a file.
- **`--live` and `--handoff` PRINT, they do not WRITE** (§24.20). LIVE.md carries TWO `**Versions:**`
  lines — **line 6 is current**. Keep Status to ONE line.
- **A BIBLE BUMP IS A REGENERATION OBLIGATION** (S175) and **HAS TWO HOMES** (S185).
- **A BANK VERSION HAS TWO HOMES** — the comment AND the `bank_version` field; `--status` reads the
  FIELD. **A SOURCE PIN IS READ BEFORE IT IS BUMPED** (rule 37): ten banks in S197, five came back
  with nothing touching the changed claims and that is a result, not a formality.
- **`--currency` CATCHES WHAT THE GATES DO NOT.** Editing a source pin is still editing the bank.
- **A PROJECT-FILE COPY IS NOT THE TREE** (rule 32). `/mnt/project` still carries `_v2` of the TDP
  template and an S41 handoff; the live template is `ZUMO_TDP_Template_v3.md` at **v3.3.0**.
- **SESSION OPEN:** `git ls-remote` → fresh clone → verify the Bible's internal version **with the
  parser** → read LIVE.md → `book_gates` → `session_versions --check` and `--selftest` →
  `census --selftest` → `lesson_inventory --selftest` → `svg_layout_audit --selftest` →
  `gate_payload_match newproject.html lessons/Lesson_*.html` → `callout_id` → `retired_claims` →
  `quiz_bank --check` → `build_css --check` → `build_worklist --check` → `build_syllabus_html --check`
  → `prose_canon --check` and `--selftest` → `site_parity` twice past the 10m57s floor.

# STANDING AUTHORITY — §24.17, §24.19, §24.21
**Decide and report; do not ask.** Carve-outs: facts about the ROOM · irreversible moves · RoboLore
brand and course scope. **§24.19 is the tiebreaker.**
**FROM S196:** when the question is whether more measurement is worth it, the person holding the
robot is better placed than the instrument.
**FROM S197:** **a handoff instruction is a description of an artefact, and the artefact is the
answer.** S197 opened with two instructions from S196 — wire in the L05 graphic, and fix BD2 like
BD1. Reading the artefacts overturned both. Neither handoff line was careless; both were written
without the file in front of them.

---
<!-- VERSION BLOCK: emitted by session_versions.py --handoff. Never hand-typed. -->
Fresh-clone verified at **`075e6ce`**. Census **41,841**.
Bible **v8.195** · `BookComponentStandard` **v01.13.0** · Maker **v2.72** ·
`marks/` **41** · `icons/` **49** incl. LICENSE.
`ZUMO_Syllabus_WORKING.md` **v1.5**.

Instruments: `book_gates` **v1.76.6** · `lesson_inventory` **v1.4.1** ·
`gen_component` **v1.6.1** · `pill_sweep` **v1.1** · `gate_payload_match` **v1.9.6** ·
`build_family_map` **v1.6.6.7** · `callout_id` **v1.0** · `keyterm_prefix` **v1.0.1** · `build_mark_index` **v1.1.0** · `gen_bonus_banner` **v1.4.1** ·
`gen_part_banners` **v1.2** · `session_versions` **v1.33.0** · `fit_raster_svg` **v1.2** ·
`flatten_alpha` **v1.2** · `svg_layout_audit` **v1.23** · `site_parity` **v1.2.1** ·
`build_css` **v1.4.0** · `build_syllabus_html` **1.1** ·
`image_audit` **v1.3** ·
`strip_inline` **v1.2** ·
`build_worklist` **v1.2** ·
`qti_export` **1.2** ·
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
`harness_setup.sh` **v1.1** ·
`pio_harness.sh` **v3.1** ·
`going_deeper` **v01.6.1**.

Lessons: L01 v03.32.2 · L02 v03.26.2 · L03 v03.47.3 · L04 v04.29.6 · L05 v04.30.2 · L06 v04.37.3 · L07 v04.33.1 · L08 v04.34.4 · L09 v05.28.0 · L10 v02.30.7 · L11 v02.31.4 · L12 v01.35.4 · L13 v02.39.0 · L14 v02.36.3 · L15 v02.32.2 · L16 v02.28.1.
