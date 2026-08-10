# ZUMO — S141 HANDOFF (rewritten at S140 close · paste at top of Session 141)

## Session open ritual (do this without being asked)
1. **`git ls-remote https://github.com/Weymuth/zumo.git HEAD` FIRST.** A stale answer is
   timing, not caching — **retry a minute later before concluding a push failed** (§12.4).
2. Read `LIVE_ZUMO_TEXTBOOK.md` — verify date / status / versions.
3. **Do NOT grep the Bible version.** `session_versions.bible_consistency()` parses it.
4. Run the full suite and **READ THE EXIT CODE, NOT THE LAST LINE**. Plus
   **`callout_id.py --selftest` then `--audit`**, **`keyterm_prefix.py --audit`**,
   **`quizzes/quiz_bank.py --selftest` then `--check`**, and
   **`session_versions.py --selftest`** — **its CONTROL C caught S138's missing Bible
   changelog entry at S139 open, and nothing else in the tree could see it.**
5. **`--anomalies` BELONGS TO `lesson_inventory`, NOT `session_versions`.**
6. `pip install cairosvg --break-system-packages` **and `pyyaml`. Needed every session.**
7. **NEVER run `build_css.py --help` or `session_versions.py --help`.** Read the docstring.
8. **Do not hand-type a version, and do not hand-type a COUNT.**
9. **`gate_payload_match.py` needs `newproject.html` FIRST, then the full lesson glob.**
10. **A CLONE IS NOT THE SITE.** Run `site_parity.py` after any push.
11. **VERIFY THE PUSH BY FRESH CLONE AND MD5 — AND DIFF THE STAGE AGAINST THE CLONE.**
12. **`css/semantic.css` AND `ZUMO_FAMILY_PINS.md` ARE HAND-AUTHORED PRESERVED LAYERS.**

---

# THE ONE THING TO CARRY OUT OF S140

**WHEN TWO SECTIONS DISAGREE, READ THE CITATIONS — THE OLDER ONE USUALLY PREDATES THE
NEWER, AND NO INSTRUMENT IN THE TREE CAN SEE EITHER.**

L05's Observation Experiment 3 placed a box at **45° off the flank** and its hint predicted
RIGHT would answer. §3.4a states that roughly **19°–72° off each side is a blind wedge with
nothing aimed into it** — 45° is 26° past FRONT's edge and 27° short of RIGHT's, almost
exactly the middle. **The tell was the citation:** the hint cites §3.4, not §3.4a. The
experiment was written first, §3.4a was inserted later, nobody went back. A student running
it would have read 0 and concluded the hardware had failed — the precise inference §3.4a
exists to prevent, four sections earlier.

**AND A KEYWORD CAN BE USED, GLOSSED AND NEVER TAUGHT.** `static` appears in L05 §5.11
(retained local, no prose), again in L06's `averageCounts()` (file scope, no prose), and is
explained only in L07. Two unrelated meanings of one word, met twice before either is
defined. **Both now teach their own sense and name the other.**

**AND THE HEADER OF A THING IS NOT THE THING.** Both new banks named question ids that had
shifted during drafting; one claim pointed at a question that does not exist. Caught only by
**re-deriving the ids from the file**, in a triple check, after everything else was green.

---

# SEPTEMBER 8 IS ABOUT FOUR WEEKS OUT

**READING QUIZZES — 4 of 12 WRITTEN (L02, L03, L04, L05).** Status is DERIVED:
`python3 quizzes/quiz_bank.py --status`. **Read `quizzes/QUIZ_SPEC.md` first (v1.1.0).**
**THE ORDER IS CANON: READ -> FIX -> QUIZ.** S140 is the proof twice over — five L05
questions would have been keyed BACKWARDS against the unfixed Experiment 3.

**L06 IS NEXT AND IT IS NOT YET READ.** L01 is also unwritten and IS read (S136).

**THE IN-SCOPE FIGURES ALL NEED DJ AND THE ROBOT.** Stills **3.2 · 3.5 · 3.6 · 4.1 · 4.3 ·
12.1**, videos **3.1 · 4.1 · 6.1 · 8.1**. `GRAPHIC 15.4` was never produced; its brief is in
the S135 chat. **VIDEO 3.1 carries L03's opening page** and is the highest-value shot.

---

# STATE

<!-- VERSION BLOCK: emitted by session_versions.py --handoff. Never hand-typed. -->
Fresh-clone verified at **`fc16c2b`**. Census **40,489**.
Bible **v8.132** · `BookComponentStandard` **v01.13.0** · Maker **v2.45.5** ·
`marks/` **41** · `icons/` **49** incl. LICENSE.
`ZUMO_Syllabus_WORKING.md` **v1.2**.

Instruments: `book_gates` **v1.64.5** · `lesson_inventory` **v1.3.5** ·
`gen_component` **v1.6.1** · `pill_sweep` **v1.1** · `gate_payload_match` **v1.7.1** ·
`build_family_map` **v1.6.0** · `callout_id` **v1.0** · `keyterm_prefix` **v1.0.1** · `build_mark_index` **v1.1.0** · `gen_bonus_banner` **v1.4.1** ·
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

Lessons: L01 v03.28.2 · L02 v03.21.2 · L03 v03.41.0 · L04 v04.29.0 · L05 v04.29.0 · L06 v04.32.0 · L07 v04.31.1 · L08 v04.30.1 · L09 v05.26.1 · L10 v02.27.1 · L11 v02.28.2 · L12 v01.31.2 · L13 v02.28.2 · L14 v02.33.1 · L15 v02.30.1 · L16 v02.22.1.

**69/69 gates.** `lesson_inventory --anomalies` silent · family map **1119/1119** ·
`callout_id --audit` **1119, 0 problems** · `keyterm_prefix --audit` **238 = 151 + 4 + 83 + 0** ·
`build_css --check` current at 574 rules · `image_audit --check` current ·
`gate_payload_match` PASS · `strip_inline --verify` **0 dead class names** · the pin is
**55 rows** · `quiz_bank --selftest` **9/9 controls loud** · `quiz_bank --check` **4 banks
valid, 319 questions**.

---

# WHAT SHIPPED IN S140

**L03's LAST TWO `[CONTENT PLACEHOLDER]` BLOCKS ARE GONE. L03 v03.40.2 -> v03.41.0.** The
brushed-vs-brushless explainer is written into §4.2 as **prose, not a callout** — seated
after the motor photo rather than tight against LEARN 3.36, so `GRAPHIC 3.18` stays with the
paragraph it illustrates. **The Roomba story was SKIPPED by DJ ruling**: §1 *The Crooked
Robot Problem* already states that thesis 1,150 lines above, and L03 is the second-heaviest
lesson at 4,418 lines. The word appears **zero times** in the tree outside L01's pre-existing
is-it-a-robot table.

**L05: FOUR FINDINGS, ALL FIXED. L05 v04.28.1 -> v04.29.0.** Experiment 3 rewritten to
DEMONSTRATE the dead spot, with a second move out toward **90°** so the card still proves the
side detector works — this is the last lesson in which the side receivers exist at all.
`static` taught in §5.11 with the file-scope sense named and forward-pointed; glossary entry
is now **Static Variable (retained local)**. BRAIN CHECK 03 Q4 asked about `delay()` and
answered about duplicated code — **both halves now address `delay()`**, and the blocking
point was already taught in L04's calibration helper, so the reveal names a connection rather
than introducing one. Challenge 4's `CLOSE_THRESHOLD` moved **4 -> 5**, because the comment
was right and the NUMBER was wrong: at 5 the three zones map exactly onto §3.2's three
distance bands, and it was a one-character fix where changing the comment would have taken
four edits.

**L06 v04.31.1 -> v04.32.0** — `averageCounts()`'s comment now says its `static` is the
file-scope sense and **not** L05's, and admits the word does nothing useful yet in a one-file
program. L07 collects the debt.

**ONE FINDING WAS REVERSED BY MEASUREMENT.** L05's BC02 shares **zero** character-exact lines
with its §2 objectives, which reads as a §25.5 violation — until all sixteen lessons are
measured: **only L06 satisfies §25.5, at 6/6.** Every other lesson is 0–4. Book-wide
condition, not an L05 defect. **Do not re-open this as a lesson-level bug.**

**BANKS L03 v1.0.0 (83 questions) and L05 v1.0.0 (87).** L04's bank re-pinned to L03
v03.41.0 (**v1.1.1, pin only**) after re-reading its single Lesson-3 dependency — B25's A+C
distractor, untouched by the edit. Its comment header still read `v1.0.0` while the YAML key
read `1.1.0`: **two version homes, one updated.** Both now agree.

**THE §27.11 DIGEST MOVED FOUR TIMES, ALL USAGE RANK.** Rules and declarations unchanged at
574/2,033 every time; all 574 declaration blocks byte-identical each cycle. `.div-2196f3`
9->7, `.link-c-1f2a3d` 21->25, `.tok-6a9955` 839->845. **`build_css` was run four times in a
row and produced four identical md5s** — the `.ul-ls-none-2`/`-3` alternation did not fire on
this tree today, but check it again before trusting a pinned digest.

---

# S141 QUEUE

## 1. CONTINUE THE READ — L06 IS NEXT
**L01–L05 are READ. L06–L16 ARE NOT.** L06 was edited in S140 but **not read end to end**.

## 2. L01'S BANK IS THE ONLY READ-AND-UNWRITTEN ONE
L01 was read at S136 and fixed there. Cheapest bank available.

## OPENED S140, UNRULED
- **§3.2's *about 13½ milliseconds*** for the six-round proximity read could not be checked —
  `pololu.com` is not reachable from the container. **Unverified, not wrong.** Not quizzed.
- **L05 §3.6 alkaline tension**: prose derives 6.0 V from 1.5 V/cell; the table row reads
  **6,300 mV**. Both defensible (nominal vs fresh), but a question keyed to either fails a
  careful reader of the other. **Not quizzed. Needs a ruling or a sentence.**
- **The `static` split is now taught in L05 and L06 but the GLOSSARIES still disagree** —
  L05 defines the retained-local sense; no lesson glossary defines the file-scope sense.

## Carried from S137/S138/S139, still unruled
- **§4.2's stall-current multiple**: *~1.5 A … roughly 5× its free-running draw*, where
  Pololu's no-load figure is ~0.10 A, i.e. ~15×. **Still not fixed, still not quizzed.**
- **`IMAGE 4.1` IS A PHANTOM IN THE FIGURE COUNT** — planned reads 146 where the true
  population is 145, and gate 69's pin is one high. DJ ruled *not now* at S139.
- **THE CONSTANTS vs CONFIGURATION VOCABULARY DRIFT.** Derive the canonical set first.
- **NO GATE TIES A CHALLENGE CARD TO ITS STARTER PAYLOAD**, **NO GATE HOLDS A QUIZ BANK**,
  **NO GATE HOLDS A NAV PILL.**
- **THE 3Pi+ NOTE COMES OUT OF L03** — needs a new root file as the 3Pi+ book seed.
- **`class period` APPEARS IN L10.** Read it before removing.
- **L03 C1's hint hands over the exact two numbers its own template blanks ask for.**
- **§7's BANNER is still three spellings** — 9 lessons `· Test It`, 6 bare, L12 `· Calibrate`.
- **L14's §10 is the only §10 that is not an exit ticket.**
- **Whether the `after` quiz set is graded at all.** Four lessons now have one.

## Carried from S135, still open
- **THE SPIRAL ARC — RULED, ENUMERATED, DELIBERATELY NOT STARTED.** All-or-nothing.
  13 of 171 units. **Five approved first:** L04 4.4→L03 · L05 5.1→L04 · L06 6.7→L03,L04 ·
  L12 12.2→L06 · L15 15.2→L04. **THE SCAN IS BLIND TO THE REST.**
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
- **REDO `GRAPHIC 4.7` IN THE BLUEPRINT COMPOSITION.** Do not re-derive the orientation —
  chips run **5 4 3 2 1** left to right.
- Challenge card Pass B · monetization/ebook · DISCOVERIES tagging.

## Learner mode & book content
L03_C05 Variable Speed · L03 C01/C05/C06 reference a `finished` payload that does not exist
for L03 · whole-template starters L08/L09/L10 · Maker batch · L01 VS Code multi-root step.

## Bench (need the robot — parked with photography)
Q017 L09 six numbers · Q044 calibration-spin · Q046 gyro-bias · L02 §5 green-LED ·
Constrain RUN_MS · cm/s at a stated BASE_SPEED · the floor rig for 3.2 / 3.5 / VIDEO 3.1 ·
a real TRIM run for `IMAGE 3.6` · **THE SURFACE TEST: run 7E on a lab tile.** ·
**L04's wave test and Act Two row-1 overflow.** · **NEW: L05 Experiment 3 at 45° — the
rewrite is right either way, but the bench would sharpen its wording.**

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
17. **RUN A BLINDING CONTROL AGAINST THE CONSUMER THAT CAN FAIL.**
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
28. **A STRUCTURAL CHANGE THAT ENDS A SENTENCE EARLY OWES THE SENTENCE A LOOK.** **S139 paid
    this again:** substituting 600 into *"500 is the natural darker-than-halfway line"* would
    have manufactured a false sentence. Two of the ten threshold sites were REWRITTEN, not
    swapped. Print the rendered paragraph back.
29. **PIN THE DENOMINATOR, NOT THE REMAINDER.**
30. **A WORKING COPY YOU HAVE RUN TOOLS IN IS NOT THE REPO.** When two readings disagree, RE-CLONE.
31. **A LABEL IS NOT THE THING IT NAMES.**
32. **NOT EVERY SPLIT IS DRIFT.** Ask whether a variation CARRIES INFORMATION before normalising it.
33. **NO INSTRUMENT READS PROSE. Read the book.**
34. **A NUMBER IS ONLY CHECKABLE AGAINST THE OTHER FIFTEEN LESSONS.** **S139 paid this:** the
    *seven-section* finding was a single-lesson read of a book-wide convention, and the census
    reversed it.
35. **COMPILE THE SNIPPET; LET THE BOOK'S OWN CODE TESTIFY.**
36. **A FACT THAT LIVES ONLY IN AN SVG IS NOT IN THE BOOK.**
37. **READ -> FIX -> QUIZ, NEVER QUIZ FIRST.** **S139 is the proof:** five L04 questions would
    have been keyed wrong against the unfixed lesson.
38. **A TEXT MATCH LOCATES; IT NEVER ANSWERS.** Read every hit in full; never report an empty
    result as absence. A lead never carries a ruling request.
39. **NO INSTRUMENT THAT READS THE TREE CAN SEE A RULING.** Search the session record first.
40. **PULL THE PAYLOAD, NOT THE CARD.**
41. **NEW, S139: AN ENTRY FILED IN ONE HOME IS NOT FILED.** Two homes drift independently and
    the gate cannot see the one it does not read. **And when a reader disagrees with a
    document, read the disagreement — the reader may be right.**
43. **NEW, S140: WHEN TWO SECTIONS DISAGREE, READ THE CITATIONS.** L05's Experiment 3 cited
    §3.4, not §3.4a — so the experiment predated the section that contradicted it and nobody
    revisited it. **The older text is usually the wrong one, and no instrument can see either.**
44. **NEW, S140: THE HEADER OF A THING IS NOT THE THING.** Both new quiz banks named question
    ids that had SHIFTED during drafting — one claim pointed at a question that does not exist.
    **Re-derive ids from the file before believing a header that names them.**
45. **NEW, S140: A SNAPSHOT YOU HAVE RUN TOOLS IN HIDES ITS OWN DEBRIS.** A root `__pycache__`
    was invisible against the working snapshot (both had it) and showed up instantly against a
    FRESH CLONE. Rule 30, one step earlier than usual.
42. **NEW, S139: A SPEC'S OWN NUMBERS CAN BE ARITHMETICALLY IMPOSSIBLE.** QUIZ_SPEC asked for
    ~70% MC under caps whose floor was 76%. **Nothing validated the mix, so the first bank
    quietly broke a cap to satisfy it.** When a ratio must give, give it to the instrument
    that MEASURES BETTER, not the one that is easiest to write.
