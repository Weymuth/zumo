# ZUMO — S137 HANDOFF (rewritten at S136 close · paste at top of Session 137)

## Session open ritual (do this without being asked)
1. **`git ls-remote https://github.com/Weymuth/zumo.git HEAD` FIRST.** A stale answer is
   timing, not caching — **retry a minute later before concluding a push failed** (§12.4).
2. Read `LIVE_ZUMO_TEXTBOOK.md` — verify date / status / versions.
3. **Do NOT grep the Bible version.** `session_versions.bible_consistency()` parses it.
4. Run the full suite and **READ THE EXIT CODE, NOT THE LAST LINE**. Plus
   **`callout_id.py --selftest` then `--audit`**, **`keyterm_prefix.py --audit`**, and
   **`quizzes/quiz_bank.py --selftest` then `--check`**.
5. **`--anomalies` BELONGS TO `lesson_inventory`, NOT `session_versions`.**
6. `pip install cairosvg --break-system-packages` **and `pyyaml`. Needed every session.**
7. **NEVER run `build_css.py --help` or `session_versions.py --help`.** Read the docstring.
8. **Do not hand-type a version, and do not hand-type a COUNT.**
9. **`gate_payload_match.py` needs `newproject.html` FIRST, then the full lesson glob.**
10. **A CLONE IS NOT THE SITE.** Run `site_parity.py` after any push.
11. **VERIFY THE PUSH BY FRESH CLONE AND MD5 — AND DIFF THE STAGE AGAINST THE CLONE.**
12. **`css/semantic.css` AND `ZUMO_FAMILY_PINS.md` ARE HAND-AUTHORED PRESERVED LAYERS.**

---

# THE ONE THING TO CARRY OUT OF S136

**NO INSTRUMENT READS PROSE — AND THE BOOK HAS BEEN GRADED BY INSTRUMENTS FOR 135 SESSIONS.**

A read of L01 and L02 end to end found **seven defects. Not one was visible to any of the
69 gates**, because a gate measures structure and **a false claim in prose is perfectly
well-formed structure.** §24.13's *re-derive, do not re-read* has no purchase on a sentence.

**THREE WERE CONTRADICTIONS BETWEEN LESSONS — INVISIBLE INSIDE EITHER ONE.** L01 promised a
**sumo match** the course never runs, while L03 says *"our non-sumo RoboCup bots"* and L14
lists sumo as *beyond these pages*. L01's troubleshooting table blamed garbled serial on a
**wrong baud rate** where L02 §8, L02 §6 Step 2 and L02's own Glossary all say the Zumo's
native-USB link **ignores** that number — and L01 is the lesson a student is in when it
happens. L02 pointed at **Lesson 7** for `float`, which teaches it nowhere; the first lesson
that makes a student TYPE one is **L06**.

**THE METHOD THAT FOUND THEM: grep the figure book-wide and READ EVERY SENTENCE IT APPEARS
IN.** A number is only checkable against the other fifteen lessons.

**AND TWO TECHNIQUES THAT BEAT READING.** *Compile it* — `g++ -fsyntax-only` against a stub
header put *The Broken Code*'s errors on lines 2/5/8 where the reveal said 3/7/11, **and
revealed that the third error is invisible on the first build**, which no reading would have
shown. *Let the book's own code testify* — L01's chime writes `delay(900)` after an 800 ms
note, which is only meaningful if `playFrequency()` returns immediately; that proved the
buzzer non-blocking with the library source unreachable.

**A FACT THAT LIVES ONLY IN AN SVG IS NOT IN THE BOOK.** The buzzer's background behaviour
was already taught — inside GRAPHIC 1.19 and nowhere else. Invisible to a skimmer,
unreachable by a screen reader, absent from both Quick References, and silently required by
a challenge. Now in prose.

**NOT EVERY HIT IS A DEFECT.** L01 carries a second `6000` that was checked and **left**: a
Challenge 11 prompt, *"try a threshold of 6000 — what happens, and why?"*, whose whole point
is that the threshold is unreachable. Read before you fix.

---

# SEPTEMBER 8 IS ABOUT FOUR WEEKS OUT

**THE QUEUE WAS SORTED BY WHAT THE INSTRUMENTS CAN SEE.** They cannot see a missing quiz
bank or a false sentence, so neither ever surfaced. Both now have a home.

**READING QUIZZES — 1 of 12 WRITTEN.** `quizzes/` now exists with the L02 bank (58 before +
18 after), the authoring spec, and a validator. **Do not re-derive the rules — read
`quizzes/QUIZ_SPEC.md` first, it is the whole recipe.** Status is DERIVED: run
`python3 quizzes/quiz_bank.py --status`. **THE ORDER IS CANON AND IT IS NOT NEGOTIABLE:
READ → FIX → QUIZ.** Four of S136's seven defects sat directly under questions the L02 bank
asks; a bank written against the unread lesson would have keyed **6000** correct and marked
the students who read carefully WRONG. **An auto-graded gate that punishes the attentive is
worse than no gate.**

**THE 11 IN-SCOPE FIGURES ALL NEED DJ AND THE ROBOT.** Of 16 outstanding, eleven are in
L01–L12: stills **3.2 · 3.5 · 3.6 · 4.1 · 4.3 · 4.5 · 12.1** and videos **3.1 · 4.1 · 6.1 ·
8.1**. No session can produce any. **`IMAGE 4.5` is blocked on two counts:** §14 forbids a
drafting model estimating where a component sits in a photograph, so it needs highlight-box
coordinates; and the caption asks the windows be **numbered 1–5 left to right**, where the
delivered draft labelled them Left / Left-Center / Center / Right-Center / Right.
**`GRAPHIC 15.4` was never produced**; a full brief sits in the S135 chat. The other five
outstanding figures are L13–L16 — **outside the fall scope**, and can miss September.

**The daily grid is blocked until ~Aug 24** by its own header.

---

# STATE

<!-- VERSION BLOCK: emitted by session_versions.py --handoff. Never hand-typed. -->
Fresh-clone verified at **`41a5f5c`**. Census **40,458**.
Bible **v8.130** · `BookComponentStandard` **v01.13.0** · Maker **v2.45.4** ·
`marks/` **41** · `icons/` **49** incl. LICENSE.
`ZUMO_Syllabus_WORKING.md` **v1.2**.

Instruments: `book_gates` **v1.64** · `lesson_inventory` **v1.3.5** ·
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

Lessons: L01 v03.28.2 · L02 v03.21.2 · L03 v03.40.1 · L04 v04.28.1 · L05 v04.28.1 · L06 v04.31.1 · L07 v04.31.1 · L08 v04.30.1 · L09 v05.26.1 · L10 v02.27.1 · L11 v02.28.2 · L12 v01.31.2 · L13 v02.28.2 · L14 v02.33.1 · L15 v02.30.1 · L16 v02.22.1.

**69/69 gates.** `lesson_inventory --anomalies` silent · family map **1119/1119** ·
`callout_id --audit` **1119, 0 problems** · `keyterm_prefix --audit` **238 = 151 + 4 + 83 + 0** ·
`regex_audit` **1 lead** (known `entity_sweep.py:70`) · `build_css --check` current at 574 rules ·
**`image_audit --check` current at 16 of 146** · `gate_payload_match` PASS ·
`strip_inline --verify` **0 dead class names** · the pin is **55 rows** ·
`quiz_bank --selftest` **9/9 controls loud** · `quiz_bank --check` **1 bank valid**.

---

# S137 QUEUE

## 1. CONTINUE THE CONTENT READ — L03 IS NEXT
**L01 and L02 are READ. L03–L16 ARE NOT.** L03 is 4,409 lines, the second-heaviest in the
book, and week-one material. **Read it end to end before writing its quiz.** Known leads
already sitting in L03:
- **L03 points a student at Lesson 5 for the `for` loop.** Measured: L01's INSIGHT traces it
  fully, **L04 §8A.6** dissects it with GRAPHIC 4.6, and the objective *write a for loop and
  trace it* is owned by **L05 §5.15** — whose own header reads *"Builds on: the for loop you
  took apart in Lesson 4."* **Three homes, no owner.** L04 §8A.6 opens *"nobody explained
  it,"* true only if L01's INSIGHT is skipped. Which lesson owns the teaching is DJ's call.
- L03 is where the `1000 ms = 1 second` queue item lives. **It IS taught** — in L01's
  GRAPHIC 1.19 and in L02's Warm-Up 1 reveal. **Both are places a student can miss** (a
  figure, and a hint behind *"click after time is up"*). Read before acting; S69 burned a
  session on a false finding of exactly this shape.

## 2. THE QUIZ BANKS — 11 MORE FOR THE FALL SCOPE
L01, L03–L12. **`quizzes/QUIZ_SPEC.md` is the recipe; do not reinvent it.** L13–L16 may
never be needed — course scope is L01–L12.

## OPENED S136, UNRULED
- **NO GATE HOLDS A QUIZ BANK.** `quiz_bank.py --check` is loud, but `book_gates.py` never
  calls it, so a broken bank can be pushed. **A ruling that creates an invariant owes a gate
  in the same pass (§24.2)** — this shipped without one, deliberately and recorded.
- **NO GATE HOLDS A NAV PILL** either (v8.129). Pills 1–9 are now byte-identical across
  sixteen files and nothing guards them. The valuable arm ties a pill to its OWN banner —
  that is what would have caught L14's `8. Tune & Test` and L16's `9. Tiers`.
- **THE PILL VOCABULARY HAS NO SECTION BODY.** Lives only in the v8.129 changelog entry.
- **§7's BANNER is still three spellings** — 9 lessons `· Test It`, 6 bare, L12 `· Calibrate`.
  Only the PILLS were ruled. With pill 7 now `Verify`, whether the banner follows is open.
- **L14's §10 is the only §10 that is not an exit ticket** — `10.1 Morning Routine` /
  `10.2 Pre-Match Routine` under a banner reading *Exit Ticket*. The pill exception was
  granted (`10. Match Day`); whether the BANNER moves is unruled.
- **L15 and L16's §8 titles are near-duplicates.** DJ ruled it acceptable — do not re-open.
- **Whether the `after` quiz set is graded at all.** The syllabus split (Quizzes 20 / Exit
  Tickets 10) has no third slot, and BRAIN CHECK 03 already does that job in-page.
- **`digitalWrite(LED_BUILTIN, …)` in L02 Challenge 1** is the only place the book uses it
  instead of `ledYellow()`. Cosmetic; noted, not fixed.

## Carried from S135, still open
- **THE SPIRAL ARC — RULED, ENUMERATED, DELIBERATELY NOT STARTED.** §18.1's "1–2 prior
  concepts" is a **FLOOR** (DJ: *"floor. No ceiling."*). **Do not start without finishing** —
  a half-starred book is worse than an unstarred one. It never started: 13 of 171 units, 8%.
  **Five approved first:** L04 4.4→L03 · L05 5.1→L04 · L06 6.7→L03,L04 · L12 12.2→L06 ·
  L15 15.2→L04. **Then 17 self-declaring cards:** 2.6→1 · 3.8→2 · 4.4→3 · 4.5→3 · 7.4→6 ·
  9.1→7 · 9.2→2 · 9.4→6 · 9.6→6,7 · 10.4→6 · 10.5→5,6,8,9 · 11.1→6 · 11.5→10 · 12.3→6,7,8 ·
  13.3→6,8,10,11,12 · 14.1→11 · 15.7→8. **THE SCAN IS BLIND TO THE REST** — only one of the
  five read-found spirals appears in it. True population **21 minimum, top end unknown**.
  Each star is a NEW CALLOUT with an identity **minted by `callout_id.py --apply`, never
  hand-written**. **`ZUMO_SPIRAL_MOVE_ASSESSMENT.md` IS ALREADY TAKEN** by an S67 study of
  which challenges could MOVE between lessons — do not overwrite it; pick a new name.
- **THE FIGURE BLOCK HAS FOUR SPELLINGS.** L11 `div-m-24px0`/`img-ddd`; L12 semantic
  `<figure>`/`<figcaption>`; L13 `div-m-25px0`; L15 `div-m-26px0`. **L12's is the best.**
- **`svg_layout_audit.py` HAS FOUR MEASURED DEFECTS, NONE FIXED.** (1) ignores
  `preserveAspectRatio="meet"`, so letterboxed images get a false *under the 2× floor* —
  **this already cost DJ a wrong answer about `IMAGE 4.5`**; (2) nested `callout-*` groups
  compare against their parent; (3) an `<image>` in `<defs>` used via `<use>` is measured at
  definition size; (4) blind to text-vs-box collisions and to elements hidden BEHIND a box.

## Carried from S133/S134, still unruled
- **KEY TERM paint is five grounds** across 238 blocks. DJ parked it deliberately.
- **The four held body blocks are a FAMILY question**, not a shape one.
- **The head colour `#6a1b9a` is 16 blocks in clean strata** (L04 5/5, L09 6/6, L10 5/5).
- **L03 `3.44` carries `id="glossary-trim"` on a BODY block** where every other is `term-*`.
- **`BookComponentStandard` §7.4 says 184 where the measured figure is 238.** Make it a
  derivation.
- **§6.5's nav-pill rule still says 12–14** where the live range is 10 to 19. Since S129.
- **§24.14a and §24.14b still have NO section body**; `§24.14b` names TWO different rules
  across the S128 and S132 entries. Next free letter is §24.14e.
- **L07 `[IMAGE 7.3]`** is landed by a GRAPHIC across the two number spaces (§10), unruled.

## Carried, unchanged
Should `ZUMO_FAMILY_PINS.md` carry a version home? · `css/semantic.css` carries none either ·
the 3 `glyph_scan` leads · `glyph_scan`'s U+2100 floor · quick-reference anchors in L02–L06
only · **timers appear in L02/L03/L04 only — S69 burned a session on a false finding here,
READ before counting** · the callout border-width probe · the colour ledger, 16 items ·
`index.html` carries no version home · `BONUS_MARK`/`MARK` indexed nowhere · **L01's BC02
does not carry L01's objectives (legacy, ruled S119)** · S116's past-tense question: RETIRE
IT · L14's score formula is `<code>` and is not code · four `data-reveal="mechanism"` blocks
are not on §20.1's whitelist · **the mark roster RECONCILES and is gated (61). Do not
re-open.** · **`build_css` is NOT idempotent on this tree** — `.ul-ls-none-2`/`-3` alternate
across runs; §27.13 assumes one fixed point, there are two.

## Learner mode & book content (untouched for many sessions)
L03_C05 Variable Speed · L03 C01/C05/C06 reference a `finished` payload that does not exist
for L03 (staged in `ZUMO_L03_TEMPLATES.md`) · whole-template starters L08/L09/L10 · Maker
batch (bulk DL · `?lesson=N` gate · C## labels) · L01 VS Code multi-root step · challenge
card Pass B.

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
5. **`lessons/` IS PART OF THE FILENAME. `css/` and now `quizzes/` likewise.**
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
28. **A STRUCTURAL CHANGE THAT ENDS A SENTENCE EARLY OWES THE SENTENCE A LOOK.**
29. **PIN THE DENOMINATOR, NOT THE REMAINDER.**
30. **A WORKING COPY YOU HAVE RUN TOOLS IN IS NOT THE REPO.** When two readings disagree, RE-CLONE.
31. **A LABEL IS NOT THE THING IT NAMES.** Banner, fence and pill are three spellings of one
    section and they drift independently. Where a gate ties two together the drift dies in
    seconds; where nothing ties them, it lives for a hundred sessions.
32. **NOT EVERY SPLIT IS DRIFT.** §4's seven banner labels are accurate per lesson. Ask
    whether a variation CARRIES INFORMATION before normalising it — uniformity that destroys
    meaning is a regression wearing a tidy shirt.
33. **NO INSTRUMENT READS PROSE.** A suite grows to cover what it can see, and the uncovered
    region is invisible precisely because nothing reports on it. **Read the book.**
34. **NEW, S136: A NUMBER IS ONLY CHECKABLE AGAINST THE OTHER FIFTEEN LESSONS.** Three of
    S136's findings were contradictions BETWEEN lessons and were invisible inside either one.
    Grep the figure book-wide and read every sentence it appears in.
35. **NEW, S136: COMPILE THE SNIPPET; LET THE BOOK'S OWN CODE TESTIFY.** `g++ -fsyntax-only`
    against a stub header beat reading on the line numbers AND found a masked error. When a
    library's behaviour is unreachable, the book's existing code is evidence.
36. **NEW, S136: A FACT THAT LIVES ONLY IN AN SVG IS NOT IN THE BOOK.** Unreachable by a
    screen reader, unfindable by grep, invisible to a skimmer. If a challenge depends on it,
    the prose owes it.
37. **NEW, S136: READ → FIX → QUIZ, NEVER QUIZ FIRST.** Four of seven defects sat under
    questions the bank asks. **An auto-graded gate that punishes the attentive is worse than
    no gate.**
