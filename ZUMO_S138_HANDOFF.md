# ZUMO — S138 HANDOFF (rewritten at S137 close · paste at top of Session 138)

## Session open ritual (do this without being asked)
1. **`git ls-remote https://github.com/Weymuth/zumo.git HEAD` FIRST.** A stale answer is
   timing, not caching — **retry a minute later before concluding a push failed** (§12.4).
2. Read `LIVE_ZUMO_TEXTBOOK.md` — verify date / status / versions.
3. **Do NOT grep the Bible version.** `session_versions.bible_consistency()` parses it.
4. Run the full suite and **READ THE EXIT CODE, NOT THE LAST LINE**. Plus
   **`callout_id.py --selftest` then `--audit`**, **`keyterm_prefix.py --audit`**,
   **`quizzes/quiz_bank.py --selftest` then `--check`**, and
   **`session_versions.py --selftest`** — its Control F caught a missing Bible CHANGELOG
   entry at S137 close that nothing else in the tree could see.
5. **`--anomalies` BELONGS TO `lesson_inventory`, NOT `session_versions`.**
6. `pip install cairosvg --break-system-packages` **and `pyyaml`. Needed every session.**
7. **NEVER run `build_css.py --help` or `session_versions.py --help`.** Read the docstring.
8. **Do not hand-type a version, and do not hand-type a COUNT.**
9. **`gate_payload_match.py` needs `newproject.html` FIRST, then the full lesson glob.**
10. **A CLONE IS NOT THE SITE.** Run `site_parity.py` after any push.
11. **VERIFY THE PUSH BY FRESH CLONE AND MD5 — AND DIFF THE STAGE AGAINST THE CLONE.**
12. **`css/semantic.css` AND `ZUMO_FAMILY_PINS.md` ARE HAND-AUTHORED PRESERVED LAYERS.**

---

# THE ONE THING TO CARRY OUT OF S137

**A TEXT MATCH LOCATES; IT NEVER ANSWERS — AND NAMING THE TOOL LET ME ROUTE AROUND THE RULE.**

§24.10 has said *the parser is the default, a text match is the narrow exception* since **S91**,
off DJ's own words: *"Grep has caused most of the issues we have faced in the book."* **It was
violated twice in the session that amended it**, both times by an operator who believed he was
complying because he had not typed `grep`. A Python `if 'for loop' in line` walk over L03
returned two hits, and those two went to DJ as a **finding with two rulings attached** — a
population of unknown size reported as a measurement.

**THE RULE NOW PINS A PROPERTY, NOT A SPELLING (§24.10, v8.130.1).** A *text match* is `grep`,
`rg`, editor find, `str.find`, `in`, `re.search` over lines, or an `--audit` flag doing any of
those internally — **one instrument in different clothes.** Its output is a set of candidate
lines **whose population is unknown by construction**, because the one case it cannot return is
the one lacking the string. **A hit is READ IN FULL before it is reported, and an empty result
is never reported as absence.** Clause 3 now covers CLAIMS as well as COUNTS, and **a lead never
carries a ruling request** — attaching a decision to an unverified premise asks DJ to rule on
something that may not be true.

**AND NO INSTRUMENT THAT READS THE TREE CAN SEE A RULING.** The `for`-loop question the scan
"found" **had already been ruled in S57 and shipped** — L04 §8A.6 owns the tutorial, L05 §5.15 is
the spiral rung, and Bible §11 (v8.36.1) came out of it. Search the session record before
measuring the book.

**THE PRICE WAS PAID AGAIN, AND A CENSUS CAUGHT IT.** `IMAGE 3.16` vs `GRAPHIC 3.16` was reported
as a collision. The census across all sixteen lessons shows **eleven lessons reuse a number across
figure types** — L04 carries `4.1` as an IMAGE, a GRAPHIC *and* a VIDEO. **It is the book's
convention, not a defect.** DJ ruled it in one line: *they teach two different things.*

---

# SEPTEMBER 8 IS ABOUT FOUR WEEKS OUT

**READING QUIZZES — 1 of 12 WRITTEN.** Status is DERIVED: `python3 quizzes/quiz_bank.py --status`.
**Read `quizzes/QUIZ_SPEC.md` first; do not re-derive the rules.** **THE ORDER IS CANON:
READ → FIX → QUIZ.** S137 is the proof — **sixteen defects in L03 that no gate could see**, and
a bank written against the unread lesson would have keyed several of them correct.

**THE 11 IN-SCOPE FIGURES ALL NEED DJ AND THE ROBOT.** Stills **3.2 · 3.5 · 3.6 · 4.1 · 4.3 ·
4.5 · 12.1**, videos **3.1 · 4.1 · 6.1 · 8.1**. `IMAGE 4.5` is blocked on two counts: §14 forbids
a drafting model estimating where a component sits in a photograph, so it needs highlight-box
coordinates; and the caption asks the windows be **numbered 1–5 left to right** where the
delivered draft labelled them Left / Left-Center / Center / Right-Center / Right. `GRAPHIC 15.4`
was never produced; its brief is in the S135 chat. **VIDEO 3.1 carries L03's opening page** and is
the highest-value shot in the set.

---

# STATE

<!-- VERSION BLOCK: emitted by session_versions.py --handoff. Never hand-typed. -->
Fresh-clone verified at **`e27d50b`**. Census **40,467**.
Bible **v8.130.1** · `BookComponentStandard` **v01.13.0** · Maker **v2.45.5** ·
`marks/` **41** · `icons/` **49** incl. LICENSE.
`ZUMO_Syllabus_WORKING.md` **v1.2**.

Instruments: `book_gates` **v1.64.1** · `lesson_inventory` **v1.3.5** ·
`gen_component` **v1.6.1** · `pill_sweep` **v1.1** · `gate_payload_match` **v1.7** ·
`build_family_map` **v1.6.0** · `callout_id` **v1.0** · `keyterm_prefix` **v1.0.1** · `build_mark_index` **v1.1.0** · `gen_bonus_banner` **v1.4.1** ·
`gen_part_banners` **v1.2** · `session_versions` **v1.24.0** · `fit_raster_svg` **v1.2** ·
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

Lessons: L01 v03.28.2 · L02 v03.21.2 · L03 v03.40.2 · L04 v04.28.2 · L05 v04.28.1 · L06 v04.31.1 · L07 v04.31.1 · L08 v04.30.1 · L09 v05.26.1 · L10 v02.27.1 · L11 v02.28.2 · L12 v01.31.2 · L13 v02.28.2 · L14 v02.33.1 · L15 v02.30.1 · L16 v02.22.1.

**69/69 gates.** `lesson_inventory --anomalies` silent · family map **1119/1119** ·
`callout_id --audit` **1119, 0 problems** · `keyterm_prefix --audit` **238 = 151 + 4 + 83 + 0** ·
`build_css --check` current at 574 rules · **`image_audit --check` current at 16 of 146** ·
`gate_payload_match` PASS · `strip_inline --verify` **0 dead class names** · the pin is
**55 rows** · `quiz_bank --selftest` **9/9 controls loud** · `quiz_bank --check` **1 bank valid**.

---

# WHAT SHIPPED IN S137

**L03 WAS READ END TO END — 4,409 LINES — AND CARRIES SIXTEEN FIXES.** Not one was visible to any
of the 69 gates.

**The three that would have reached a student at the bench.** Challenge 2's reveal printed
**`Replace batteries`** in a book whose §3.6 says *recharge — draining NiMH below 4200 mV damages
the cells*; it now reads `Recharge batteries`. Challenge 3's reveal told students to place code
*"after `waitForButtonA()`"* — **a function that is not in the library, an object that is not in
their file, and a gate that did not exist.** And §1's Physics Corner explained the curve with
**F=ma and "1% less acceleration"** where §3.11 explains the same phenomenon as a **speed**
difference; open-loop motors settle to a steady speed in well under a second, so the mechanism is
a small steady speed gap the robot integrates for the whole run. §1 and §3.11 now agree.

**THE SAFETY ONE, AND IT WAS FOUND BY PULLING THE PAYLOAD RATHER THAN READING THE CARD.** Both
L03 challenge-template starters — `constrain` and `ramp` — carried **no button object and no
gate**: the robot drove the instant the upload finished. The `ramp` starter also **never told the
student to stop the motors**, in a lesson whose §3.8 warning is *"the robot drives off the
table."* Both now open with an empty `setup()` and run inside
`if (buttonB.getSingleDebouncedPress())` — **L03's own pattern, 12 uses in the lesson, written by
the student in Step 11.** `waitForButton()` was rejected on measurement: **it does not appear
anywhere before L04.**

**THE REST.** C4's reveal pointed at **Lesson 5** for the `for` loop, which S57 gave to
**L04 §8A.6** — and the `ramp` payload carried a second copy of the same stale pointer, invisible
from the book side. C5's stated goal said the cycle starts at 150 when its own `speedIndex = 1`
starts it at 200. §3.1 carried a dead `<p>Differential drive diagram:</p>` with nothing under it.
Step 4 said *"under **your** banner"* when Step 2 had just had them delete it. §8A.4's inline
challenge added a 300 ms settle before a **3-second** countdown, for a stated reason that was not
true; it now removes three hard-coded `delay(1000)` calls instead. Bonus 4 hands over a
descending, stepped, counter-as-value loop and named none of it. **And L04 §8A.6's opener said
"nobody explained it"** — L01 had. Plus the *robot's* left/right rule at §3.7 and §8, and one
sentence at §3.5 on **why TRIM always hits the left motor** (one sign convention, every robot,
all year).

**WHAT WAS CHECKED AND DELIBERATELY LEFT ALONE.** Gear-ratio sticker colours, TRIM polarity, the
`constrain()` rationale and the NiMH voltage bands all match Bible §16.1–16.3 exactly. **§8A does
cover what §9 requires** — C5 needs arrays and `%`, both taught at §8A.5–8A.6, and the card says
so. **`1000 ms = 1 second` is TAUGHT, in §3.7, in prose** — retire that queue item; it has been
open since S40 and S69 already burned a session on a false finding of the same shape.

**§24.10 AMENDED (Bible v8.130.1).** Five clauses; see THE ONE THING above. Ungated by design —
§24.2 owes no gate because there is nothing in the book to assert against.

---

# S138 QUEUE

## 1. CONTINUE THE READ — L04 IS NEXT
**L01, L02 and L03 are READ. L04–L16 ARE NOT.** L04 is the lesson S57 gave the `for` tutorial to,
and the one whose §8A.6 opener just changed — read it against L01 and L05 as a set.

## 2. THE QUIZ BANKS — 11 MORE FOR THE FALL SCOPE
L01, L03–L12. **L03 is now read and fixed, so its bank is unblocked.**
`quizzes/QUIZ_SPEC.md` is the recipe; do not reinvent it.

## OPENED S137, UNRULED
- **NO GATE TIES A CHALLENGE CARD TO ITS STARTER PAYLOAD.** **Measured, not argued:** reverting
  `buttonB` out of the `constrain` payload while leaving the card gated **passes all 69 gates,
  exit 0.** That hole is how `RUN_MS` came to sit in the payload and not in the card. The
  valuable arm asserts every constant named in a payload appears in its card's TEMPLATE block.
- **THE 3Pi+ NOTE COMES OUT OF L03** — DJ: *"Yes, but that will eventually be a separate book."*
  One self-contained NOTE, `data-callout="3.33"`, lines 1021–1026, **not** held in the family pin.
  **PRICED: it moves three baselines from 1119 to 1118** — the literal at
  `build_family_map.py:338`, gate 47's count at `book_gates.py:3146`, and `callout_id --audit`.
  **Neither park file will take it:** `ZUMO_PARKED_EXIT_ITEMS.md` is §25 exit-region only and its
  header forbids merging contracts; `ZUMO_SHELVED_CARDS.md` holds proposals that were never live.
  **It needs a new root file as the 3Pi+ book seed — pick the name deliberately**
  (`ZUMO_SPIRAL_MOVE_ASSESSMENT.md` is the standing warning: already taken by an S67 study).
- **`class period` APPEARS IN L10.** §3.1 (v8.109) forbids calendar facts inside a lesson so an
  adopter can run a different length. **Read it before removing** — it may be innocent prose.
- **L03 §5.1 says "the seven-section `main.cpp` you know from Lesson 2."** L02's own code blocks
  carry **four** distinct banners; the Maker emits 29 across the book; and L03 uses
  `CONFIGURATION` / `STATE VARIABLES` where L02 uses `CONSTANTS`, so it is not "L02's set minus
  prototypes" either. **Derive the canonical section set before touching the sentence.**
- **§4.2: "stall current ~1.5 A … roughly 5× its free-running draw."** Pololu's no-load figure is
  ~0.10 A, which is 15×. 5× only holds if *free-running* means the max-efficiency point (0.34 A).
- **L03 C1's hint hands over the exact two numbers its own template blanks ask for.**
- **Two `[CONTENT PLACEHOLDER]` blocks are still live in L03** — brushed-vs-brushless, and the
  three-Roombas story — both marked *DJ to supply*, in week-one material.
- **DECLINED at S137, recorded so they are not re-proposed:** a *"designed for two or three class
  periods"* note at the top of L03 — **§3.1 forbids it**, and pacing lives in
  `ZUMO_Teacher_Daily_Grid_WORKING.md`, which already spreads L03 over periods 3–4. An OLED curve
  hint and a quick-test countdown mode are changes to the **shipped build**, so they are payload
  work rather than prose and want their own session.

## Carried from S136, still unruled
- **NO GATE HOLDS A QUIZ BANK** and **NO GATE HOLDS A NAV PILL.** **THE PILL VOCABULARY HAS NO
  SECTION BODY** — it lives only in the v8.129 changelog entry.
- **§7's BANNER is still three spellings** — 9 lessons `· Test It`, 6 bare, L12 `· Calibrate`.
  Only the PILLS were ruled; whether the banner follows is open.
- **L14's §10 is the only §10 that is not an exit ticket.** The pill exception was granted
  (`10. Match Day`); whether the BANNER moves is unruled.
- **Whether the `after` quiz set is graded at all.** The syllabus split (Quizzes 20 / Exit Tickets
  10) has no third slot, and BRAIN CHECK 03 already does that job in-page.
- **`digitalWrite(LED_BUILTIN, …)` in L02 Challenge 1** — the only place the book uses it instead
  of `ledYellow()`. Cosmetic; noted, not fixed.
- **L15 and L16's §8 titles are near-duplicates. DJ ruled it acceptable — do not re-open.**

## Carried from S135, still open
- **THE SPIRAL ARC — RULED, ENUMERATED, DELIBERATELY NOT STARTED.** §18.1's "1–2 prior concepts"
  is a **FLOOR** (DJ: *"floor. No ceiling."*). **Do not start without finishing** — a half-starred
  book is worse than an unstarred one. It never started: 13 of 171 units, 8%.
  **Five approved first:** L04 4.4→L03 · L05 5.1→L04 · L06 6.7→L03,L04 · L12 12.2→L06 ·
  L15 15.2→L04. **Then 17 self-declaring cards:** 2.6→1 · 3.8→2 · 4.4→3 · 4.5→3 · 7.4→6 · 9.1→7 ·
  9.2→2 · 9.4→6 · 9.6→6,7 · 10.4→6 · 10.5→5,6,8,9 · 11.1→6 · 11.5→10 · 12.3→6,7,8 ·
  13.3→6,8,10,11,12 · 14.1→11 · 15.7→8. **THE SCAN IS BLIND TO THE REST** — only one of the five
  read-found spirals appears in it. True population **21 minimum, top end unknown**. Each star is
  a NEW CALLOUT with an identity **minted by `callout_id.py --apply`, never hand-written**, and it
  moves the family map off 1119.
- **THE FIGURE BLOCK HAS FOUR SPELLINGS.** L11 `div-m-24px0`/`img-ddd`; L12 semantic
  `<figure>`/`<figcaption>`; L13 `div-m-25px0`; L15 `div-m-26px0`. **L12's is the best.**
- **`svg_layout_audit.py` HAS FOUR MEASURED DEFECTS, NONE FIXED.** (1) ignores
  `preserveAspectRatio="meet"`, so letterboxed images get a false *under the 2× floor* — **this
  already cost DJ a wrong answer about `IMAGE 4.5`**; (2) nested `callout-*` groups compare
  against their parent; (3) an `<image>` in `<defs>` used via `<use>` is measured at definition
  size; (4) blind to text-vs-box collisions and to elements hidden BEHIND a box.

## Carried from S133/S134, still unruled
KEY TERM paint is five grounds across 238 blocks (DJ parked it deliberately) · the four held body
blocks are a FAMILY question, not a shape one · head colour `#6a1b9a` is 16 blocks in clean strata
(L04 5/5, L09 6/6, L10 5/5) · L03 `3.44` carries `id="glossary-trim"` on a BODY block where every
other is `term-*` · `BookComponentStandard` §7.4 says 184 where the measured figure is 238 — make
it a derivation · §6.5's nav-pill rule still says 12–14 where the live range is 10 to 19, since
S129 · **§24.14a and §24.14b still have NO section body**; `§24.14b` names TWO different rules
across the S128 and S132 entries, and the next free letter is §24.14e · **L07 `[IMAGE 7.3]`** is
landed by a GRAPHIC across the two number spaces (§10), unruled.

## Carried, unchanged
Should `ZUMO_FAMILY_PINS.md` carry a version home? · `css/semantic.css` carries none either ·
the 3 `glyph_scan` leads · `glyph_scan`'s U+2100 floor · quick-reference anchors in L02–L06 only ·
**timers appear in L02/L03/L04 only — S69 burned a session on a false finding here, READ before
counting** · the callout border-width probe · the colour ledger, 16 items · `index.html` carries
no version home · `BONUS_MARK`/`MARK` indexed nowhere · **L01's BC02 does not carry L01's
objectives (legacy, ruled S119)** · S116's past-tense question: RETIRE IT · L14's score formula is
`<code>` and is not code · four `data-reveal="mechanism"` blocks are not on §20.1's whitelist ·
**the mark roster RECONCILES and is gated (61). Do not re-open.** · **`build_css` is NOT
idempotent on this tree** — `.ul-ls-none-2`/`-3` alternate across runs; §27.13 assumes one fixed
point, there are two.

## Learner mode & book content
L03_C05 Variable Speed · L03 C01/C05/C06 reference a `finished` payload that does not exist for
L03 (staged in `ZUMO_L03_TEMPLATES.md`) · whole-template starters L08/L09/L10 · Maker batch
(bulk DL · `?lesson=N` gate · C## labels) · L01 VS Code multi-root step · challenge card Pass B.

## Bench (need the robot — parked with photography)
Q017 L09 six numbers · Q044 calibration-spin · Q046 gyro-bias · L02 §5 green-LED ·
Constrain RUN_MS · cm/s at a stated BASE_SPEED · the floor rig for 3.2 / 3.5 / VIDEO 3.1 ·
a real TRIM run for `IMAGE 3.6` · **THE SURFACE TEST: run 7E on a lab tile.**

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
28. **A STRUCTURAL CHANGE THAT ENDS A SENTENCE EARLY OWES THE SENTENCE A LOOK.** **S137 paid this
    live:** replacing the front of the F=ma sentence left its tail reading *"1% faster means 1%
    less acceleration"* — a NEW contradiction manufactured by the fix itself, and **the edit
    assert was no protection because it was true.** Print the rendered paragraph back.
29. **PIN THE DENOMINATOR, NOT THE REMAINDER.**
30. **A WORKING COPY YOU HAVE RUN TOOLS IN IS NOT THE REPO.** When two readings disagree, RE-CLONE.
31. **A LABEL IS NOT THE THING IT NAMES.** Banner, fence and pill are three spellings of one
    section and they drift independently.
32. **NOT EVERY SPLIT IS DRIFT.** Ask whether a variation CARRIES INFORMATION before normalising
    it — uniformity that destroys meaning is a regression wearing a tidy shirt.
33. **NO INSTRUMENT READS PROSE.** The uncovered region is invisible precisely because nothing
    reports on it. **Read the book.**
34. **A NUMBER IS ONLY CHECKABLE AGAINST THE OTHER FIFTEEN LESSONS.** **S137 paid this twice** —
    the `for`-loop finding and the `3.16` "collision" were both single-lesson reads of a
    book-wide pattern, and the census reversed both.
35. **COMPILE THE SNIPPET; LET THE BOOK'S OWN CODE TESTIFY.** Used again at S137 close: both
    gated starters and both reveals built clean under `g++ -fsyntax-only` against a stub header.
36. **A FACT THAT LIVES ONLY IN AN SVG IS NOT IN THE BOOK.**
37. **READ → FIX → QUIZ, NEVER QUIZ FIRST.** An auto-graded gate that punishes the attentive is
    worse than no gate.
38. **NEW, S137: A TEXT MATCH LOCATES; IT NEVER ANSWERS.** The one case it cannot return is the
    one lacking the string. **Read every hit in full before reporting it, and never report an
    empty result as absence.** A lead never carries a ruling request.
39. **NEW, S137: NO INSTRUMENT THAT READS THE TREE CAN SEE A RULING.** Search the session record
    before measuring the book — S137 re-opened a question DJ had settled in S57 and shipped.
40. **NEW, S137: PULL THE PAYLOAD, NOT THE CARD.** The card describes the starter; the starter is
    what the student actually runs. Both L03 safety defects were invisible from the book side.
