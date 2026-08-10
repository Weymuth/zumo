# ZUMO — S143 HANDOFF (rewritten at S142 close · paste at top of Session 143)

## Session open ritual (do this without being asked)
1. **`git ls-remote https://github.com/Weymuth/zumo.git HEAD` FIRST.** A stale answer is
   timing, not caching — **retry a minute later before concluding a push failed** (§12.4).
2. Read `LIVE_ZUMO_TEXTBOOK.md` — verify date / status / versions.
3. **Do NOT grep the Bible version.** `session_versions.bible_consistency()` parses it.
4. Run the full suite and **READ THE EXIT CODE, NOT THE LAST LINE**. Plus
   **`callout_id.py --selftest` then `--audit`**, **`keyterm_prefix.py --audit`**,
   **`quizzes/quiz_bank.py --selftest` then `--check`**, and
   **`session_versions.py --selftest`** — **its CONTROL C is what reports an unfinished
   documentation pass, and nothing else in the tree can see one.**
5. **`--anomalies` BELONGS TO `lesson_inventory`, NOT `session_versions`.**
6. `pip install cairosvg --break-system-packages` **and `pyyaml`. Needed every session.**
7. **NEVER run `build_css.py --help` or `session_versions.py --help`.** Read the docstring.
8. **Do not hand-type a version, and do not hand-type a COUNT.**
9. **`gate_payload_match.py` needs `newproject.html` FIRST, then the full lesson glob.**
10. **A CLONE IS NOT THE SITE.** Run `site_parity.py` after any push.
11. **VERIFY THE PUSH BY FRESH CLONE AND MD5 — AND DIFF THE STAGE AGAINST THE CLONE.**
12. **`css/semantic.css` AND `ZUMO_FAMILY_PINS.md` ARE HAND-AUTHORED PRESERVED LAYERS.**
13. **`rm -rf __pycache__` BEFORE `git status`.** S141 and S142 both grew one.

---

# THE ONE THING TO CARRY OUT OF S142

**A CONTROL THAT CANNOT FAIL IS NOT A CONTROL — AND THAT INCLUDES THE ONES YOU WRITE TO
CHECK YOUR OWN WORK.**

`gate_payload_match`'s line-wise fallback asked `l in corpus` — containment in the whole
corpus TEXT. So a payload line that had **LOST a leading qualifier the lesson carries**
matched trivially as a substring of the longer lesson line:

```
corpus : static unsigned int sensorValues[5];     // Array to store ...
payload:        unsigned int sensorValues[5];     // Array to store ...
```

Reverting exactly **one of 136 payloads** left the gate printing **PASS**. Additions it
always caught; a dropped `static`, `const` or `unsigned` it could not see **at all**.
**THE ENTIRE `static` PASS HAD BEEN ARGUED SAFE ON THAT GATE**, in writing, to DJ — and the
claim was false when it was made. Now line EQUALITY against a stripped corpus line set,
control-run **five shapes × two gate versions**, with the two already-caught shapes proving
nothing was lost. `gate_payload_match` **v1.8.0**.

**AND THE SECOND HALF IS WORSE, BECAUSE IT WAS SELF-INFLICTED.** The verifier written to
catch drifted quiz-header ids checked them against a mapping **typed into the script**
rather than parsed from the file. It validated intent, not the artefact — and printed
**ALL HOLD against a file that had not been written**, because the edit had thrown an
assertion first. Rewritten to parse the header's own claims, **at which point it failed**,
which is the only reason it is known to work.

**THE HEADER OF A THING IS NOT THE THING (S140 rule 44, twice more).** Both wrong claims in
the L08 bank header were created by the REBALANCE pass that followed the draft — ids shift,
the header keeps naming the old ones. Both named ids that EXIST.

---

# SEPTEMBER 8 IS ABOUT FOUR WEEKS OUT

**READING QUIZZES — 8 of 16 WRITTEN (L01–L08), 620 questions.** Status is DERIVED:
`python3 quizzes/quiz_bank.py --status`. **Read `quizzes/QUIZ_SPEC.md` first (v1.1.0). THE
ORDER IS CANON: READ -> FIX -> QUIZ**, and QUIZ_SPEC §0 requires the read to have happened
**in the same session** as the bank.

**L09 IS NEXT AND IT IS NOT YET READ.** L01–L08 are all read, fixed and banked.

**THE IN-SCOPE FIGURES ALL NEED DJ AND THE ROBOT.** Stills **3.2 · 3.5 · 3.6 · 4.1 · 4.3 ·
12.1**, videos **3.1 · 4.1 · 6.1 · 8.1**. `GRAPHIC 15.4` was never produced; its brief is in
the S135 chat. **VIDEO 3.1 carries L03's opening page** and is the highest-value shot.

---

# STATE

<!-- VERSION BLOCK: emitted by session_versions.py --handoff. Never hand-typed. -->
Fresh-clone verified at **`8221d96`**. Census **40,531**.
Bible **v8.134** · `BookComponentStandard` **v01.13.0** · Maker **v2.46.0** ·
`marks/` **41** · `icons/` **49** incl. LICENSE.
`ZUMO_Syllabus_WORKING.md` **v1.2**.

Instruments: `book_gates` **v1.65.4** · `lesson_inventory` **v1.3.5** ·
`gen_component` **v1.6.1** · `pill_sweep` **v1.1** · `gate_payload_match` **v1.8.0** ·
`build_family_map` **v1.6.1** · `callout_id` **v1.0** · `keyterm_prefix` **v1.0.1** · `build_mark_index` **v1.1.0** · `gen_bonus_banner` **v1.4.1** ·
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

Lessons: L01 v03.28.3 · L02 v03.21.2 · L03 v03.41.0 · L04 v04.29.0 · L05 v04.29.0 · L06 v04.32.1 · L07 v04.31.3 · L08 v04.31.0 · L09 v05.26.1 · L10 v02.27.2 · L11 v02.28.2 · L12 v01.31.2 · L13 v02.28.2 · L14 v02.33.1 · L15 v02.30.1 · L16 v02.22.1.

---

# WHAT SHIPPED IN S142

**THE S141 TIDY, AND IT WAS BIGGER THAN ITS ESTIMATE.** `L07_IMAGE_7-11` renamed to
`error_no_such_file` — the set slugs its filenames from its own banner (`ERROR 1 — NOT
DECLARED` → `error_not_declared`), and 7-11 was the only one that did not. **FIVE index rows
were stale, not four** — 7.8 had the same defect and the handoff missed it — derived by
crossing every *still needed* row in all sixteen lessons against the GENERATED
`IMAGE_WORKLIST.md`. `[IMAGE 7.3]` also surfaced and was **correctly left alone**: it is the
parked landed-by-a-GRAPHIC case and its row is honest. **THE CLIPPED CAPTION BOX WAS FOUR
FILES, NOT TWO** — every `<rect>` measured against its own `viewBox` book-wide, and the
background rect had to grow with the viewBox or the caption would have sat on transparent.

**`IMAGE_SHOT_LIST.md` WAS A THIRD STALE RECORD AND IS NOW BRIEFS-ONLY.** 10 of its 24 rows
named figures already on disk; it listed three lessons as *fully illustrated* while the
generator had outstanding figures in all three; it still listed the retired IMAGE 7.13. Its
status claims are gone and it points at `IMAGE_WORKLIST.md`, which cannot go stale.

**L08 READ END TO END. L08 v04.30.1 -> v04.31.0, SIX FINDINGS.** Step 2's *complete file*
reveal had **deleted the TRIM block** while Step 8's `handleGap()` uses it — compiled, and
it fails with `'TRIM' was not declared in this scope`. The Maker was correct in all seven
payloads; **only the book was wrong**, and `gate_payload_match` could not see it because the
Maker's `RobotConfig.h` derives from **L07's** reveal. §8A.2 used raw `read()` against a
**calibrated** threshold — the exact thing Step 5 teaches against, in the same lesson.
§8A.4 claimed to be *the complete pattern you've implemented* while naming **three
identifiers that exist nowhere in the book** — `SETPOINT`, `MAX_CORRECTION`, a bare `Kp` —
and clamping the correction where the lesson clamps the speeds; it is now Step 7's own
function, **asserted line-for-line identical**. Step 8's hint cited *Lesson 6's timers* and
**L06 contains zero `millis()`**; repointed to L05's beep-interval trick, the same
non-blocking stamp-and-compare shape. Two variables called *module-private* had external
linkage. And the Kp range had two spellings.

**FILE-SCOPE `static`, 139 SITES.** 136 Maker payloads (L08–L16) plus 3 lesson reveals (L08
Step 4, L08 Step 5, L10). The anchor was the **two-line pair**, and that mattered: a 137th
occurrence exists — **L05's `jumper_check`**, a single-file program where `sensorValues` is a
legitimate `main.cpp` global. Anchoring on one line would have made it `static` and taught
the wrong thing one lesson before the module architecture exists. Verified by re-deriving
all 136 from the parsed `PAYLOADS` object, plus a two-translation-unit compile.
Maker **v2.46.0**.

**BIBLE §16.10 AND §16.11 NEW — v8.134, filed in BOTH homes.** §16.10: **39 mm is the
diameter OVER THE TRACK**, sprocket alone 35 mm, spacing 85 mm, 12 CPR, 909.7 at 75.81:1,
with the pitch-line question recorded as a bench item that lands inside §7's own ±2 cm
tolerance either way. §16.11: **Kp 0.1–0.3, start 0.10, on the 75:1 fleet** — and the number
is DERIVED, not chosen: §3.1 states the correction range as *roughly −600 to +600*, and
**600 = 0.3 × 2000**, so that sentence can only have been written against a 0.3 ceiling.
§7.3 and the Quick Reference at 0.08–0.25 were the drift. Challenge 5's three adaptive gains
had been sitting on the OLD range's endpoints and moved with it.

**BANK L08 v1.0.0 — 50 before + 25 after = 75**, both sets at **72% MC / 20% TF / 8%
matching**, the spec's amended §3 target. Five of the six findings are load-bearing in it.
Four things are deliberately NOT asked and the header says why.

---

# S143 QUEUE

## 1. CONTINUE THE READ — L09 IS NEXT
**L01–L08 are READ, FIXED AND BANKED. L09–L16 ARE NOT READ.**

## OPENED S142, UNRULED
- **THE RESOURCE SECTION AS A BOOK PAGE — PARKED UNTIL AFTER SEPTEMBER 8 (DJ ruling).**
  Two constraints are recorded at the top of `ZUMO_Resource_Section_WORKING.md` and must
  travel with it: (a) it is a companion page on the `going_deeper` model — which is named in
  **29 places in `book_gates.py`** plus six other instruments, so budget the wiring; (b)
  **THE NUMBERS MUST BE DERIVED OR GATED, NEVER RETYPED.** Every headline fact already lives
  in 3–4 lessons; a page that restates them adds a fifth home to each, and S141 spent a
  session repairing the 39 mm wheel in five places for exactly that reason.
- **THE 100:1 Kp SUGGESTION IS UNVERIFIED AND THE DIRECTION IS CONTESTED.** Recorded in the
  resource doc, flagged, and explicitly NOT book content. More gear stages mean more backlash
  (argues lower Kp); but forward speed and turn rate scale down together so path curvature per
  unit error is unchanged while the ~50 Hz loop covers less ground per pass (argues higher).
  **Settle it with L08 Challenge 2's Wiggle Test if a red-sticker robot ever appears.**
- **NO GATE HOLDS A QUIZ BANK** and **NO GATE HOLDS A NAV PILL.** Unchanged from S142.

## Carried from S141, still unruled
- **THE BAUD BENCH TEST.** `monitor_speed = 9600`, leave `Serial.begin(115200)`, upload,
  open the monitor. Clean text means the number is ignored on this fleet; garbage means
  **L02 §6 Step 2 is wrong**. Put it back to 115200 after, and **keep 1200 out of the test**.
- **THE 1200-BAUD RESET HAS NO HOME IN THE BOOK.** Candidate *Going Deeper* entry.
- **`IMAGE 7.9`, `7.10`, `7.11`, `7.12` ARE INDEXED AS *Photo / screenshot*** in
  `IMAGE_SHOT_LIST.md`'s briefs — harmless now the file carries no status, but the briefs
  still describe screenshots where four live drawn SVGs exist.

## Carried from S140, still unruled
- **§3.2's *about 13½ milliseconds*** for the six-round proximity read — unverified.
- **L05 §3.6 alkaline tension**: prose derives 6.0 V from 1.5 V/cell; the table reads 6,300 mV.
- **The `static` split is taught in L05, L06 and now L08, but the GLOSSARIES still disagree** —
  no lesson glossary defines the file-scope sense. **L08 now teaches it in Step 4, which
  strengthens the case for a glossary entry.**

## Carried from S137/S138/S139, still unruled
- **§4.2's stall-current multiple**: *~1.5 A … roughly 5× its free-running draw*, where
  Pololu's no-load figure is ~0.10 A, i.e. ~15×. **Still not fixed, still not quizzed.**
- **`IMAGE 4.1` IS A PHANTOM IN THE FIGURE COUNT** — planned reads 146, true population 145.
- **THE CONSTANTS vs CONFIGURATION VOCABULARY DRIFT.** Derive the canonical set first.
- **THE 3Pi+ NOTE COMES OUT OF L03** — needs a new root file as the 3Pi+ book seed.
- **`class period` APPEARS IN L10.** Read it before removing.
- **L03 C1's hint hands over the exact two numbers its own template blanks ask for** —
  **L07 Challenge 4 is a second instance, and L08 Challenge 4 is a THIRD**: its hint says
  map *turns 0–4000 into a 21-column screen position*, handing over the `4000` blank.
- **§3.3's header-contents bullet in L07 still lists *Include guards*** three sections before
  §3.6 files them under *The Old Way*.
- **§7's BANNER is still three spellings** — 9 lessons `· Test It`, 6 bare, L12 `· Calibrate`.
- **L14's §10 is the only §10 that is not an exit ticket.**
- **Whether the `after` quiz set is graded at all.** Eight lessons now have one.

## Carried from S135, still open
- **THE SPIRAL ARC — RULED, ENUMERATED, DELIBERATELY NOT STARTED.** All-or-nothing. 13 of 171
  units. **Five approved first:** L04 4.4→L03 · L05 5.1→L04 · L06 6.7→L03,L04 · L12 12.2→L06 ·
  L15 15.2→L04. **THE SCAN IS BLIND TO THE REST.**
- **THE FIGURE BLOCK HAS FOUR SPELLINGS.** L12's is the best.
- **`svg_layout_audit.py` HAS FOUR MEASURED DEFECTS, NONE FIXED.**

## Carried from S133/S134, still unruled
KEY TERM paint is five grounds across 238 blocks · the four held body blocks are a FAMILY
question · head colour `#6a1b9a` is 16 blocks in clean strata · L03 `3.44` carries
`id="glossary-trim"` on a BODY block · `BookComponentStandard` §7.4 says 184 where the
measured figure is 238 · §6.5's nav-pill rule still says 12–14 where the live range is 10 to
19 · **§24.14a and §24.14b still have NO section body** · **L07 `[IMAGE 7.3]`** is landed by
a GRAPHIC across the two number spaces.

## Carried, unchanged
Should `ZUMO_FAMILY_PINS.md` carry a version home? · `css/semantic.css` carries none either ·
the 3 `glyph_scan` leads · quick-reference anchors in L02–L06 only · **timers appear in
L02/L03/L04 only — S69 burned a session on a false finding here, READ before counting** ·
the colour ledger, 16 items · `index.html` carries no version home · **L01's BC02 does not
carry L01's objectives (legacy, ruled S119)** · L14's score formula is `<code>` and is not
code · **the mark roster RECONCILES and is gated (61). Do not re-open.**

## AFTER SEPTEMBER 8 — PARKED ON PURPOSE, DO NOT START EARLY
- **THE RESOURCE SECTION PAGE** (see OPENED S142 above — the constraints matter more than the
  timing).
- **REDO `GRAPHIC 4.7` IN THE BLUEPRINT COMPOSITION.** Do not re-derive the orientation —
  chips run **5 4 3 2 1** left to right.
- Challenge card Pass B · monetization/ebook · DISCOVERIES tagging.

## Learner mode & book content
L03_C05 Variable Speed · L03 C01/C05/C06 reference a `finished` payload that does not exist
for L03 · whole-template starters L08/L09/L10 · Maker batch · L01 VS Code multi-root step.

## Bench (need the robot — parked with photography)
Q017 L09 six numbers · Q044 calibration-spin · Q046 gyro-bias · L02 §5 green-LED ·
Constrain RUN_MS · **cm/s at a stated BASE_SPEED — L08 Challenge 3 states ~15 cm/s and §7.2 /
Step 8's ~8 cm figures are consistent with it, but nothing has measured it** · the floor rig
for 3.2 / 3.5 / VIDEO 3.1 · a real TRIM run for `IMAGE 3.6` · **THE SURFACE TEST: run 7E on a
lab tile.** · **L04's wave test and Act Two row-1 overflow.** · **L05 Experiment 3 at 45°.** ·
**L06 Experiment 3 both drags.** · **the baud test above.** · **commanded 30 cm vs measured,
across a few robots, for the effective-diameter question.**

---

# PUSHING — READ THIS

Named-file CLI for adds and modifies; **GitHub Desktop for deletions.** **Never `git add .`**

1. **DELIVER THE FILES** via `present_files`; instructions and md5s in the CHAT ONLY.
2. **`(1)` does not mean stale.** Verify by **md5**, never by suffix.
3. **Never present a test file or a DIAGNOSTIC beside repo files.**
4. **Never produce PUSH_ME_*.md or MD5_*.txt.**
5. **`lessons/` IS PART OF THE FILENAME. `css/` and `quizzes/` likewise.**
6. **A push that bumps a version and omits LIVE.md is an INCOMPLETE push (§12.6).**
7. **Exactly ONE `ZUMO_SNN_HANDOFF.md` in the root (gate 28).**
8. **THE NUMBER IN THE FILENAME IS THE SESSION THAT READS IT.**
9. **Never write a real version number as an arrow pair in prose.**
10. **A document cannot name the commit that contains it.**
11. **AN EDIT TO A FILE WITH REPEATED LANDMARK LINES TARGETS AN INDEX AND ASSERTS IT** (§6.12c).
12. **AN EDIT THAT CHANGES LINE COUNT INVALIDATES EVERY LINE-KEYED TARGET BELOW IT.** Go DESCENDING.
13. **A SNAPSHOT TAKEN BEFORE THE WORK IS NOT A SNAPSHOT OF THE WORK.**
14. **A CONTROL THAT DEPENDS ON THE STATE OF WHAT IT AUDITS IS NOT A CONTROL.**
15. **A CONTROL RUN AGAINST AN UNTRACKED FILE HAS NO RESTORE PATH** — snapshot yourself.
16. **A LIBRARY MAY NOT EXIT.**
17. **RUN A BLINDING CONTROL AGAINST THE CONSUMER THAT CAN FAIL.** **S142 paid this hardest:**
    `gate_payload_match` was blind to a DROPPED qualifier for its whole life, and the `static`
    pass had been argued safe on it in writing before the control was run.
18. **A DERIVED KEY IS NOT AN IDENTITY.**
19. **A GATE THAT PINS A SPELLING CERTIFIES WHATEVER IT WAS GIVEN. PIN THE PROPERTY.**
20. **A HOLD THAT IS ALSO SATISFIED BY AN ACCIDENT IS NOT A HOLD.**
21. **SNAPSHOT THE STATE YOU ARE IN, NOT THE STATE YOU ARE LEAVING.**
22. **A GENERATED ARTEFACT PRINTING `DIFFERS` IS A LEAD, NOT AN INSTRUCTION.**
23. **A CONTROL THAT CANNOT TELL A LOST WORD FROM A LOST SPACE IS NOT A CONTROL.**
24. **THE ACCEPTANCE TEST FOR A CSS REGENERATION IS THE RESOLVED STYLING, NOT THE RULE COUNT.**
25. **A GENERATED CLASS NAME IS NOT A HANDLE.** Its `-N` suffix is assigned by usage RANK.
26. **MEASURE THE PROPERTY THE RULING NAMES, NOT A PROXY FOR IT.**
27. **A COVERAGE COUNT MEASURES BLOCKS SCANNED, NOT BLOCKS ASSERTED.**
28. **A STRUCTURAL CHANGE THAT ENDS A SENTENCE EARLY OWES THE SENTENCE A LOOK.**
29. **PIN THE DENOMINATOR, NOT THE REMAINDER.**
30. **A WORKING COPY YOU HAVE RUN TOOLS IN IS NOT THE REPO.** When two readings disagree, RE-CLONE.
31. **A LABEL IS NOT THE THING IT NAMES.**
32. **NOT EVERY SPLIT IS DRIFT.** Ask whether a variation CARRIES INFORMATION before normalising it.
33. **NO INSTRUMENT READS PROSE. Read the book.**
34. **A NUMBER IS ONLY CHECKABLE AGAINST THE OTHER FIFTEEN LESSONS.**
35. **COMPILE THE SNIPPET; LET THE BOOK'S OWN CODE TESTIFY.** **S142: this is what turned the
    TRIM finding from a suspicion into a fact in one command.**
36. **A FACT THAT LIVES ONLY IN AN SVG IS NOT IN THE BOOK.**
37. **READ -> FIX -> QUIZ, NEVER QUIZ FIRST** — same session. The read is a perishable asset.
38. **A TEXT MATCH LOCATES; IT NEVER ANSWERS.**
39. **NO INSTRUMENT THAT READS THE TREE CAN SEE A RULING.** Search the session record first.
40. **PULL THE PAYLOAD, NOT THE CARD.**
41. **AN ENTRY FILED IN ONE HOME IS NOT FILED.**
42. **A SPEC'S OWN NUMBERS CAN BE ARITHMETICALLY IMPOSSIBLE.**
43. **WHEN TWO SECTIONS DISAGREE, READ THE CITATIONS.** The older text is usually the wrong one.
44. **THE HEADER OF A THING IS NOT THE THING.** **S142 paid this twice more, and BOTH were
    created by the REBALANCE pass that followed the draft** — ids shift, the header keeps the
    old ones, and every wrong claim named an id that EXISTS. Re-derive what each id ASKS.
45. **A SNAPSHOT YOU HAVE RUN TOOLS IN HIDES ITS OWN DEBRIS.** A root `__pycache__` again.
46. **A CALLOUT IS NEVER A FREE EDIT.** **S142 paid this on its own edit:** two NOTE callouts
    added to §8A took the suite from 70 to 64 — §5.1, §21, §24.14, §24.14a, §24.14c and §27.13
    all fired. Converted to prose; the content was the point, not the box.
47. **A STEP PAYLOAD IS THE FILE AS IT STANDS AT THAT STEP.**
48. **NEW, S142: A VERIFIER THAT READS YOUR INTENT INSTEAD OF THE ARTEFACT VALIDATES NOTHING.**
    The first quiz-header checker compared ids against a mapping typed into the script and
    printed ALL HOLD against a file that had not been written. **Parse the claim out of the
    file, then make the checker fail once on purpose before believing it.**
49. **NEW, S142: A NUMBER THAT A SENTENCE DERIVES FROM CANNOT BE SWAPPED WITHOUT REWRITING THE
    SENTENCE.** §3.1's *roughly −600 to +600* IS `0.3 × 2000`. Substituting 0.25 would have
    manufactured a false sentence — the S137 F=ma shape, and the tell that §3.1 was the
    original and §7.3 was the drift.
