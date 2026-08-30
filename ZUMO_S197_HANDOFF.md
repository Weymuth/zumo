# ZUMO — S197 HANDOFF (written at S196 close · paste at top of Session 197)

## READ THIS FIRST

**NOTHING FROM S196 IS PUSHED.** Two NEW UNTRACKED DIRECTORIES are in the batch and directories
are the thing GitHub Desktop hides inside a single collapsed row: **`fixtures/`** and **`tools/`**.
Neither is optional — `svg_layout_audit --selftest` and the §24.22 tripwire both fail without them.

**S196 WAS A BENCH SESSION AND IT DELETED PRINTED PROSE FOR THE FIRST TIME.** Full results are in
`ZUMO_FLAGGED_CHECKS.md` **v1.5**, recorded as observed. Two rows failed, one passed and validated
another row to 1%. **The prose deletions are NOT yet made** — that is keyboard work and it is S197's
job, not the bench's.

**DJ'S STATED PLAN FOR S197: THE MISSING IMAGES.** See §2.


**WORKLIST TALLY — derived by `census.worklist()`, unmoved this session: 103 closed / 96 fixed / 2 parked / 140 open of 245.** S196 touched no worklist row.
---

# 1. WHAT S196 DID

## THE BENCH (DJ at the robot, one sitting — all 18 rows are L01–L04)
- **F10 ❌ FAILED** — L02 §9 C2's three-screen prediction did not occur in EITHER build, and the
  wait-IN case contradicts the book outright: the battery screen VANISHED on release, which is the
  case the book calls stable. **A flash too fast to see cannot make a screen disappear and stay
  gone**, so that half stands on its own. **§9 C2's "Why it takes two trips and not one" comes out.**
- **F14 ❌ FAILED** — §9 Bonus 2 predicts ~2x baseline; measured **0.37x**. The naively-aimed TRIM
  left the robot STRAIGHTER than no TRIM at all. **Bonus 2's reveal must be rewritten.**
- **F13 ✅ PASSED** — ramp minus slam **+29.35 cm** vs **29.7 cm** predicted from F11's own rate.
  1% agreement across two programs; also demonstrates near-linear speed over 0–400.
- **F11 · F12 · F16-raw · F17 · F18 closed. F5 half.** **F17 had blocked F15/F16/F18 and the L04
  learner build since S51 — fifty-one sessions.**
- **F5 CONTRADICTS BATTERY CANON.** Fresh **5199** (canon says ~5400), and a hard session ended at
  **5092**, still ~292 mV above canon "working". **The three-band scheme does not describe the
  fleet**, and it appears in 34 figures across L01–L03. The genuinely-tired reading stays OPEN:
  twelve speed-400 runs moved the pack 2%, so the low band is not reachable at a bench on demand.

**BD1 / BD2 — NEW, OPEN, IN THE MAKER.** `L3/braking_test` launches at speed 400 with **no countdown
and no wait**; the press nudges the robot at the instant the run starts and the nudge lands inside
the measurement. L03's own TRIM Finder has a 3-second countdown. **THE SWEEP THAT FOUND THE SECOND
ONE RAN OVER THE PAYLOADS STRUCTURE, NOT LESSON PROSE** — a prose search returns zero, because the
code lives in the Maker and lessons only describe it. **`L2/speed_limit` has the identical defect and
was never hit at the bench.** Both open.

**CROSS-ROW, AND MORE USEFUL THAN ANY SINGLE ROW:**
- **Distance is repeatable to 1%; lateral drift is not** (2.2x run to run). **L03 asks students to
  judge TRIM from ONE run** — direction survives that, magnitude does not.
- **A settling trend appeared in THREE unrelated programs.** NOT claimed: battery was not logged per
  run. **Log battery with every run next bench session.**
- The robot tracks **straighter at 400 than at 200**, so TRIM tuned at 200 may not correct at 400.

## `prose_canon` v1.3.0 → **v1.4.0** — ARM 2 BUILT, ALL FOUR ARMS NOW EXIST
Live: 0 findings, 5 claims judged, twelve lessons blind (printed by the arm).
- **THE BOUNDARY IS ARM 1'S MIRROR.** Arm 1 reads listings so a code ELEMENT is its subject; arm 2
  reads sentences, and this book puts `setup()`, `loop()` and section names inside INLINE `<code>`
  spans WITHIN the prose. Copying arm 1's boundary collapsed the population **140 → 3**.
- **THE RELATION WORD'S OPERANDS ARE NOT THE ANCHORS BESIDE IT.** The first predicate convicted
  **three correct sentences out of five judged**. Fixed by binding the relation to an adjacency
  window. Control G plants that exact sentence and **fires under the unbound predicate, silent under
  the bound one**.
- **A TRIPLE CHECK FOUND TWO MORE DEFECTS AFTER I CALLED IT DONE.** An independent AST/HTMLParser
  reimplementation showed arm 2 judged only the FIRST subject of a multi-subject claim; the fix then
  regressed judged 4 → 1 because `_ANCHOR` is case-sensitive while the outer matcher compiles with
  `re.I`. **A SUB-PATTERN REUSED UNDER DIFFERENT FLAGS IS NOT THE SAME PATTERN.**
- Arms 1, 2 and 4 now run their controls from **one entry point**; arm 2's were previously reachable
  only by importing the module, so `--selftest` could print ALL CONTROLS PASS with an arm untested.

## THE SEVEN S184 RESIDUE PINS — CLOSED (ninth session carried)
L05 5.3 → **Constants**, L06 Steps 5/9 → **Distance / Turn Constants**, plus four Maker labels; a
step title and the label that opens it are ONE fix. **Names came from the files** (every other L05
heading mirrors its banner; L06's prose says "Four constants"/"Three more constants"). **The sweep
also DECLINED three sites and that matters as much** — L07's heading is already ruled legitimate by
arm 3's CONTROL J, and the Maker/Bible occurrences are changelog prose recording what the retired
label USED to read. All recorded in the now-empty `RESIDUE` table.

## `svg_layout_audit` v1.21.2 → **v1.23** — L07_GRAPHIC_7-15 HAD NO OVERFLOW AT ALL
**All five findings were phantom, and so was the "14.5 units" the handoff carried for eight
sessions.** Panels were read RAW while text was measured through the CTM; the finding string said so
out loud — `spans 220..392 inside 18..378`, and 392.5 − 378 = 14.5. **This is v1.14's own lesson
recurring** (it taught the raster checks to honour transforms; rects were the neighbour that never
got it). **My own first fix then introduced FOUR new false positives** by selecting the container on
the span's left edge instead of the anchor point, which made `text-anchor="middle"` transition labels
graze the box on their left. Final delta: exactly one file, 5 → 0. Worklist **37 → 36 files**.

## §24.22 — THE FIFTH RECURRENCE, AND THE FIRST FIX THAT REMOVES THE CAPABILITY
DJ objected for the FOURTH time. Root cause found: **`census` was built at S186 for exactly this and
had a hole** — `rendered()` resolved ENTITIES but not SMART PUNCTUATION, so a straight-quoted pattern
missed curly-quoted prose. A search for "Engineer's Log" read **ZERO across fifteen lessons** whose
true count is sixteen.
- `census` **v1.3.0** — `normalise()` folds curly quotes/dashes/nbsp/ellipsis, applied to **BOTH the
  pattern and the corpus** (folding only the corpus mirrors the defect). `literal_punct=True` opts out.
- `lesson_inventory` **v1.4.1** — `prose()` and `count_across()`, both calling `census.normalise()`
  so the mapping has ONE home.
- **`tools/no_text_match.sh`** — shadows grep/egrep/fgrep/rg in `/usr/local/bin`. **DENY BY DEFAULT,
  keyed on WHERE YOU ARE STANDING, not on argument shape.** The first version was an ALLOWLIST and
  leaked two ways on the first adversarial pass (`grep -rn PAT .` and `cat FILE | grep PAT`).
  Eleven controls; the two leaks are the first two.
- **AND I HAD TO UN-WRITE MY OWN CONTROL** — an earlier one asserted "a straight-quote pattern IS
  blind", locking the defect in as expected behaviour.
- **The friction was self-inflicted**: `import census` works plainly from the repo root. The wrong
  path was one word and the right path LOOKED like three lines of importlib ceremony.

## `ZUMO_FLAGGED_CHECKS.md` v1.2 → **v1.5**
F10 and F14 rewritten at S196 because **neither procedure could test the claim it named** — F10 said
"one flash" where §9 C2 prints a three-screen SEQUENCE; F14 asked for two runs where the claim is a
RATIO needing a baseline. **Both were found by reading the lesson instead of the row.** Then BD1/BD2
appended, then the bench results.

---

# 2. S197 OPENS HERE — DJ'S STATED PLAN: THE MISSING IMAGES

`IMAGE_WORKLIST.md` (generated; never hand-edit): **15 outstanding of 145 planned tags.**
Four are VIDEO (L03 3.1, L04 4.1, L06 6.1, L08 8.1). Eleven are stills:
L03 IMAGE 3.2 / 3.5 / 3.6 · L04 IMAGE 4.1 / 4.3 · L12 12.1 · L13 13.1 / 13.2 · L14 14.1 ·
L15 GRAPHIC 15.4 · L16 16.1. **Ten of the eleven are L12–L16, which DJ TABLED at S195** — so the
in-scope stills are **L03 and L04 only, five of them**. Briefs live in `IMAGE_SHOT_LIST.md`
(PHOTOS = DJ, SVGs = Claude).

## START HERE, AND IT CAME OUT OF THE BENCH
**`images/L05_GRAPHIC_5-10_jumper_positions.svg` EXISTS ON DISK, 1.05 MB, TITLED "3-SENSOR
CONFIGURATION / 5-SENSOR CONFIGURATION" — AND NO PAGE POINTS AT IT.** At the bench DJ had to ask
which pads to bridge; the book tells students to move the jumpers to DN2/DN4 but never shows the
three-pad geometry (`DN4 — 4 — RGT`, shunt bridges the middle pin to one side) or says which pad the
shunt connects. **It is a permanent, one-way hardware change with no undo, and the graphic that
explains it is sitting unreferenced.** `L05_GRAPHIC_5-08_three_sensor_array.svg` and
`5-09_five_sensor_array.svg` are unreferenced too. **Wire these in before drawing anything new.**
31 unreferenced files total — "not a defect by itself, but every one is either future work or litter."

## THEN, THE PROSE THE BENCH DELETED (do not let this slip — it is why the bench ran)
1. **L02 §9 C2** — remove "Why it takes two trips and not one". **Before citing the wait-OUT half,
   confirm with SERIAL TIMESTAMPS, not an eyeball**: add `Serial.println` markers in each screen
   function so the ORDER is read off the monitor. The wait-IN half needs no such support.
2. **L03 §9 Bonus 2** — rewrite the reveal. Measured 0.37x, not 2x; no evidence of direction
   asymmetry on this robot.
3. **BD1 `L3/braking_test` and BD2 `L2/speed_limit`** — countdown before any `setSpeeds` ≥300.
   Bench version used 5 s with a per-second LED blink. **Also check whether L02 should be running
   at 400 at all.**
4. **L03 "short" run** — F11 says **59.4 cm**. Give the number; "short" undersells the floor needed.
5. **Battery canon** — F5 contradicts 5400/4800/4200 across 34 figures in L01–L03. **Needs DJ**: this
   is a fleet fact, not a text fix.

## STILL OWED, UNCHANGED
- **Seat the §16 debt.** 26 rules, untouched an **eleventh** session.
- **`ZUMO_GPT_REVIEW_WORKLIST.md` footer carries a second version token** disagreeing with the header
  home `session_versions` reads. Flagged seven sessions, not ruled.
- **The `(none needed)` ruling (S183) is unbuilt** — 133 sites, every one L01–L07. S184 priced it as
  an ADD of ~148 × 4, not an edit. **Needs DJ.**
- **F14 proper** would need a fresh pack, six baseline runs before any backward run, and may not be
  resolvable on a robot this well-matched. **F15** waits on DJ's own L04 build by design (learner
  mode — do NOT hand him a calibration sketch; stock `LineFollower` contains `calibrateSensors()`,
  the exact identifier whose absence is his deliberate RED build at L04 Step 5).

---

# 3. STANDING
- **INSTALL THE TRIPWIRE AT SESSION OPEN:** `bash tools/no_text_match.sh install` then `selftest`.
  It does NOT survive a container rebuild. It does NOT cover Python `re` on raw bytes — that hole is
  open and unclosable by mechanism (696 `re.*` uses across 39 files, `census` itself among them).
- **USE THE PARSER, NOT A TEXT MATCH** (§24.22). `import census` / `import lesson_inventory` work
  plainly from the repo root. **A count comes with its population or it does not come.**
- **`gate_payload_match` IS NOT ONE OF THE GATES** and **TAKES ARGUMENTS**.
- **`--live` and `--handoff` PRINT, they do not WRITE** (§24.20). LIVE.md carries TWO `**Versions:**`
  lines — **line 6 is current**. Keep Status to ONE line.
- **A BIBLE BUMP IS A REGENERATION OBLIGATION** (S175) and **HAS TWO HOMES** (S185). Both fired
  correctly this session.
- **A BANK VERSION ALSO HAS TWO HOMES** — the comment AND the `bank_version` field, and `--status`
  reads the FIELD. **The gate named ONE bank; checking all ten showed ALL TEN disagreed.**
- **`--currency` CATCHES WHAT THE GATES DO NOT.** Ten banks were changed-but-unbumped with all 82
  gates green. Editing a source pin is still editing the bank.
- **A PROJECT-FILE COPY IS NOT THE TREE** (rule 32). `/mnt/project`'s TDP template is `_v2`; the live
  one is `ZUMO_TDP_Template_v3.md` at **v3.3.0**, A5 Lab Log present, TRACK_WIDTH_MM 98.0 corrected.
  **The parked item "TDP template v3" is DONE.**
- **THE NOTEBOOK CHAIN IS COMPLETE**: all 16 Engineer's Log prompts exist, every log has a home in
  the template and every template slot has a lesson feeding it — **zero orphans both directions**.
  The ONE gap is the Google Doc link (`ZUMO_Syllabus_WORKING.md` line 103). **Needs DJ.**
- **SESSION OPEN:** `git ls-remote` → fresh clone → verify the Bible's internal version **with the
  parser** → read LIVE.md → `book_gates` → `session_versions --check` and `--selftest` →
  `census --selftest` → **`lesson_inventory --selftest`** → **`svg_layout_audit --selftest`** →
  `gate_payload_match newproject.html lessons/Lesson_*.html` → `callout_id` → `retired_claims` →
  `quiz_bank --check` → `build_css --check` → `build_worklist --check` → `build_syllabus_html --check`
  → `prose_canon --check` and `--selftest` → `site_parity` twice past the 10m57s floor.

# STANDING AUTHORITY — §24.17, §24.19, §24.21
**Decide and report; do not ask.** Carve-outs: facts about the ROOM · irreversible moves · RoboLore
brand and course scope. **§24.19 is the tiebreaker.**
**AND A NEW ONE FROM S196:** I advised DJ to SKIP the extra baseline runs that made F14 answerable.
He ran them anyway and the verdict exists because of it. **When the question is whether more
measurement is worth it, the person holding the robot is better placed than the instrument.**

---
<!-- VERSION BLOCK: emitted by session_versions.py --handoff. Never hand-typed. -->
Fresh-clone verified at **`dbd606f`**. Census **41,814**.
Bible **v8.193** · `BookComponentStandard` **v01.13.0** · Maker **v2.71** ·
`marks/` **41** · `icons/` **49** incl. LICENSE.
`ZUMO_Syllabus_WORKING.md` **v1.5**.

Instruments: `book_gates` **v1.76.4** · `lesson_inventory` **v1.4.1** ·
`gen_component` **v1.6.1** · `pill_sweep` **v1.1** · `gate_payload_match` **v1.9.5** ·
`build_family_map` **v1.6.6.6** · `callout_id` **v1.0** · `keyterm_prefix` **v1.0.1** · `build_mark_index` **v1.1.0** · `gen_bonus_banner` **v1.4.1** ·
`gen_part_banners` **v1.2** · `session_versions` **v1.33.0** · `fit_raster_svg` **v1.2** ·
`flatten_alpha` **v1.2** · `svg_layout_audit` **v1.23** · `site_parity` **v1.2.1** ·
`build_css` **v1.4.0** · `build_syllabus_html` **1.1** ·
`image_audit` **v1.3** ·
`strip_inline` **v1.2** ·
`build_worklist` **v1.2** ·
`qti_export` **1.2** ·
`prose_canon` **v1.4.0** ·
`retired_claims` **v1.2.0** ·
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

Lessons: L01 v03.32.2 · L02 v03.26.1 · L03 v03.47.1 · L04 v04.29.6 · L05 v04.30.1 · L06 v04.37.3 · L07 v04.33.1 · L08 v04.34.4 · L09 v05.28.0 · L10 v02.30.7 · L11 v02.31.4 · L12 v01.35.4 · L13 v02.39.0 · L14 v02.36.2 · L15 v02.32.2 · L16 v02.28.1.
