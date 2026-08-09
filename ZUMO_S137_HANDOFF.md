# ZUMO — S137 HANDOFF (written at S136 close · paste at top of Session 137)

## Session open ritual (do this without being asked)
1. **`git ls-remote https://github.com/Weymuth/zumo.git HEAD` FIRST.** A stale answer is
   timing, not caching — **retry a minute later before concluding a push failed** (§12.4).
2. Read `LIVE_ZUMO_TEXTBOOK.md` — verify date / status / versions.
3. **Do NOT grep the Bible version.** `session_versions.bible_consistency()` parses it.
4. Run the full suite and **READ THE EXIT CODE, NOT THE LAST LINE**. Plus
   **`callout_id.py --selftest` then `--audit`**, and **`keyterm_prefix.py --audit`**.
5. **`--anomalies` BELONGS TO `lesson_inventory`, NOT `session_versions`.**
6. `pip install cairosvg --break-system-packages`. **Needed every session.**
7. **NEVER run `build_css.py --help` or `session_versions.py --help`.** Read the docstring.
8. **Do not hand-type a version, and do not hand-type a COUNT.**
9. **`gate_payload_match.py` needs `newproject.html` FIRST, then the full lesson glob.**
10. **A CLONE IS NOT THE SITE.** Run `site_parity.py` after any push.
11. **VERIFY THE PUSH BY FRESH CLONE AND MD5 — AND DIFF THE STAGE AGAINST THE CLONE.**
12. **`css/semantic.css` AND `ZUMO_FAMILY_PINS.md` ARE HAND-AUTHORED PRESERVED LAYERS.**

---

# SEPTEMBER 8 IS ABOUT FOUR WEEKS OUT — AND THE QUEUE IS SORTED WRONG

**S136's most useful finding was not a defect. It was that the queue has been sorted by what
the instruments can see rather than by what has to exist on September 8**, and the instruments
have no way to report on what is missing entirely.

**THE READING QUIZZES DO NOT EXIST. TWELVE ARE NEEDED AND ZERO ARE WRITTEN.**
`ZUMO_Syllabus_WORKING.md` makes the pre-class quiz the **gate into build time** — *"If you
don't pass the reading quiz, you're not cleared to start building that day"* — and
`ZUMO_Teacher_Daily_Grid_WORKING.md` assumes the flip happened on every non-buffer row.
A grep of every `.md` in the repo for *reading quiz* returns only those two planning documents
and LIVE.md. **Nothing builds one.** This is the single largest unbuilt thing standing between
the book and the first day of class, and it is the one a session can actually do — the lessons
are the source text. Suggested start: L01–L04, which covers periods 1–5.

**THE 11 IN-SCOPE FIGURES ALL NEED DJ AND THE ROBOT.** Of 16 outstanding, eleven fall in
L01–L12: stills **3.2 · 3.5 · 3.6 · 4.1 · 4.3 · 4.5 · 12.1** and videos **3.1 · 4.1 · 6.1 ·
8.1**. No session can produce any of them. **`IMAGE 4.5` is blocked on two counts, not one:**
§14 forbids a drafting model estimating where a component sits in a photograph, so it needs
highlight-box coordinates; and the caption asks the windows be **numbered 1–5 left to right**,
which the whole two-act jumper story depends on, where the delivered draft labelled them
Left / Left-Center / Center / Right-Center / Right. **`GRAPHIC 15.4` was never produced** and a
full brief for it sits in the S135 chat. The five remaining outstanding figures are L13–L16 and
are **outside the fall scope entirely** — they can miss September without consequence.

**The daily grid is blocked until ~Aug 24** by its own header, pending the real schedule.

---

# THE ONE THING TO CARRY OUT OF S136

**A LABEL IS NOT THE THING IT NAMES, AND NO GATE TIES THE TWO TOGETHER.**

A section carries THREE independent spellings — the **banner cap**, the **HTML section fence**,
and the **nav pill** — and S136 found live disagreements in all three. Gate §6.8a ties the fence
to the banner and caught a half-rename within seconds. **Nothing at all ties the pill to either**,
and that is where the two real defects were: **L14's `8. Tune & Test` pointed at a Troubleshooting
section**, and **L16's `9. Tiers` sat over a banner reading Challenges.** A student clicking either
landed somewhere the label had not promised, and 69 gates had nothing to say about it.

**AND THE SECOND, WHICH IS BIGGER: NO INSTRUMENT READS PROSE.**
L01 §3.0 promised a **sumo match** the course never runs — contradicted in place by L03's
*"our non-sumo RoboCup bots"* and L14 listing sumo as *beyond these pages*. It survived 135
sessions and a 69-gate suite because **gates measure structure, and a false claim in prose is
perfectly well-formed.** §24.13's *re-derive, do not re-read* has no purchase on a sentence.
**A content read of L01 is done. L02–L16 are not** — and L02 (4,555 lines) and L03 (4,409) are
both the heaviest in the book and the two a first-week student lives inside.

**NOT EVERY SPLIT IS DRIFT.** §4's banner carries seven different labels and they were measured
and **left alone**: read paired with their headlines each is accurate to its lesson. The test is
whether the variation carries meaning, not whether it is uniform.

---

# STATE

<!-- VERSION BLOCK: emitted by session_versions.py --handoff. Never hand-typed. -->
Fresh-clone verified at **`06023bd`**. Census **40,455**.
Bible **v8.129** · `BookComponentStandard` **v01.13.0** · Maker **v2.45.4** ·
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

Lessons: L01 v03.28.1 · L02 v03.21.1 · L03 v03.40.1 · L04 v04.28.1 · L05 v04.28.1 · L06 v04.31.1 · L07 v04.31.1 · L08 v04.30.1 · L09 v05.26.1 · L10 v02.27.1 · L11 v02.28.2 · L12 v01.31.2 · L13 v02.28.2 · L14 v02.33.1 · L15 v02.30.1 · L16 v02.22.1.

**69/69 gates.** `lesson_inventory --anomalies` silent · family map **1119/1119** ·
`callout_id --audit` **1119, 0 problems** · `keyterm_prefix --audit` **238 = 151 + 4 + 83 + 0** ·
`regex_audit` **1 lead** (known `entity_sweep.py:70`) · `build_css --check` current at 574 rules ·
**`image_audit --check` current at 16 of 146** · `gate_payload_match` PASS ·
`strip_inline --verify` **0 dead class names** · the pin is **55 rows** · `site_parity` PARITY.

---

# S137 QUEUE

## THE READING QUIZ BANK — NOT STARTED, AND IT IS THE SEPTEMBER BLOCKER
Twelve quizzes for L01–L12. Nothing exists. The lessons are the source text, so this is
authoring a session can actually complete. **Check the syllabus's own mechanics before writing:**
short, auto-graded, ONE attempt, opens before class and LOCKS at the period start, soft gate.
The Brain Check BC01 blocks are the nearest existing model — five items, answer-from-your-head,
each citing the § to re-read — and BC03 Knowledge Check is the nearer one for graded questions.
**Do not invent a new construct before reading how BC01 and BC03 are built.**

## OPENED S136, UNRULED
- **NO GATE HOLDS A PILL.** The vocabulary is now uniform across sixteen files and nothing
  guards it. **A ruling that creates a new invariant owes a gate in the same pass (§24.2,
  v8.116.1)** — and this one shipped without. The obvious shape ties pill 1–9 text to a
  constant and asserts the anchor resolves to a section whose banner exists. The harder and
  more valuable arm would tie a pill to its OWN banner, which is what would have caught L14
  and L16.
- **THE PILL VOCABULARY HAS NO SECTION BODY.** It lives only in the v8.129 changelog entry —
  the §3.1a / §24.14 / §21.1 shape, recorded as debt rather than fixed.
- **THE `for` LOOP HAS THREE HOMES AND NO OWNER.** Introduced in L01's INSIGHT (traced fully),
  dissected in L04 §8A.6 with GRAPHIC 4.6, and the objective *write a for loop and trace it*
  owned by L05 §5.15. **L04 §8A.6 opens *"nobody explained it"***, which is true only if L01's
  INSIGHT is skipped, and **L03 points a student at Lesson 5** for a loop they met in L01 and
  will dissect in L04. Two sentences fix it; which lesson owns the teaching is DJ's call.
- **L14's §10 IS THE ONLY §10 THAT IS NOT AN EXIT TICKET** — `10.1 Morning Routine` /
  `10.2 Pre-Match Routine` under a banner reading *Exit Ticket*. The pill exception was granted;
  whether the BANNER should move is unruled.
- **L15 and L16's §8 titles are near-duplicates** — *Symptoms and Stress Tests* and *Symptoms
  and the Hunt*. DJ ruled this acceptable; recorded so it is not re-opened as drift.

## Carried from S135, still open
- **THE SPIRAL ARC — RULED, ENUMERATED, DELIBERATELY NOT STARTED.** §18.1's "1–2 prior
  concepts" is a **FLOOR** (DJ: *"floor. No ceiling."*). **Do not start without finishing** —
  a half-starred book is worse than an unstarred one and is exactly what produced the *"spiral
  stops at Lesson 11"* misreading. It never started: 13 of 171 units, 8%.
  **Five approved first:** L04 4.4→L03 · L05 5.1→L04 · L06 6.7→L03,L04 · L12 12.2→L06 ·
  L15 15.2→L04. **Then 17 self-declaring cards:** 2.6→1 · 3.8→2 · 4.4→3 · 4.5→3 · 7.4→6 ·
  9.1→7 · 9.2→2 · 9.4→6 · 9.6→6,7 · 10.4→6 · 10.5→5,6,8,9 · 11.1→6 · 11.5→10 · 12.3→6,7,8 ·
  13.3→6,8,10,11,12 · 14.1→11 · 15.7→8. **THE SCAN IS STRUCTURALLY BLIND TO THE REST** — only
  one of the five read-found spirals appears in it. True population **21 minimum, top end
  unknown**; the enumeration is a READ of all 171 cards, not a query. Each star is a NEW
  CALLOUT (`data-family="BUILDS ON"`, `arrow-repeat` mark, `img-h-11em`) with an identity
  **minted by `callout_id.py --apply`, never hand-written** — it moves the family map off
  1,119 and the stylesheet with it. **`ZUMO_SPIRAL_MOVE_ASSESSMENT.md` IS ALREADY TAKEN** by an
  S67 study of which challenges could MOVE between lessons; do not overwrite it — pick a new name.
- **THE FIGURE BLOCK HAS FOUR SPELLINGS.** L11 `div-m-24px0`/`img-ddd`/`div-c-666-2`; L12
  semantic `<figure>`/`<figcaption>`; L13 `div-m-25px0`/`img-br-8px`; L15 `div-m-26px0`/
  `img-cdd9e1`. **L12's is the best** — semantic, and its class is unranked.
- **`svg_layout_audit.py` HAS FOUR MEASURED DEFECTS AND NONE IS FIXED.** (1) the resolution arm
  ignores `preserveAspectRatio="meet"`, so letterboxed images get a false *under the 2× floor* —
  **this already cost DJ a wrong answer about `IMAGE 4.5`**; (2) nested `callout-*` groups
  compare against their parent, giving false overlaps; (3) an `<image>` in `<defs>` used via
  `<use>` is measured at definition size, reporting 0.38× where the truth is 2.39×; (4) blind to
  text-versus-box collisions across baselines and to an element hidden BEHIND an opaque box.

## Carried from S133/S134, still unruled
- **KEY TERM paint is five grounds** across 238 blocks. DJ parked it deliberately.
- **The four held body blocks are a FAMILY question**, not a shape one.
- **The head colour `#6a1b9a` is 16 blocks in clean strata** (L04 5/5, L09 6/6, L10 5/5,
  0 of 59 elsewhere), cutting ACROSS the shape classes.
- **L03 `3.44` carries `id="glossary-trim"` on a BODY block** where every other is `term-*`.
- **`BookComponentStandard` §7.4 carries a stale number** — says 184 where the measured figure
  is 238. Make it a derivation.
- **§6.5's nav-pill rule still says 12–14** where the live range is 10 to 19. Since S129.
- **§24.14a and §24.14b still have NO section body**, and `§24.14b` names TWO different rules
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
5. **`lessons/` IS PART OF THE FILENAME. `css/` likewise.** Say the directory out loud.
6. **A push that bumps a version and omits LIVE.md is an INCOMPLETE push (§12.6).**
7. **Exactly ONE `ZUMO_SNN_HANDOFF.md` in the root (gate 28).**
8. **THE NUMBER IN THE FILENAME IS THE SESSION THAT READS IT.**
9. **Never write a real version number as an arrow pair in prose.**
10. **A document cannot name the commit that contains it.**
11. **AN EDIT TO A FILE WITH REPEATED LANDMARK LINES TARGETS AN INDEX AND ASSERTS IT** (§6.12c).
12. **AN EDIT THAT CHANGES LINE COUNT INVALIDATES EVERY LINE-KEYED TARGET BELOW IT.** Go DESCENDING.
13. **A SNAPSHOT TAKEN BEFORE THE WORK IS NOT A SNAPSHOT OF THE WORK.**
14. **A CONTROL THAT DEPENDS ON THE STATE OF WHAT IT AUDITS IS NOT A CONTROL.**
15. **A CONTROL RUN AGAINST AN UNTRACKED FILE HAS NO RESTORE PATH** — `git checkout --`
    reverts to HEAD, so on uncommitted work it DELETES rather than restores. Snapshot yourself.
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
26. **MEASURE THE PROPERTY THE RULING NAMES, NOT A PROXY FOR IT.** Read the specimens first.
27. **A COVERAGE COUNT MEASURES BLOCKS SCANNED, NOT BLOCKS ASSERTED.**
28. **A STRUCTURAL CHANGE THAT ENDS A SENTENCE EARLY OWES THE SENTENCE A LOOK.**
29. **PIN THE DENOMINATOR, NOT THE REMAINDER.** A count MEANT to fall cannot guard its population.
30. **A WORKING COPY YOU HAVE RUN TOOLS IN IS NOT THE REPO.** When two readings disagree, RE-CLONE.
31. **NEW, S136: A LABEL IS NOT THE THING IT NAMES.** Banner, fence and pill are three spellings
    of one section and they drift independently. Where a gate ties two together the drift is
    caught in seconds; where nothing ties them, it lives for a hundred sessions.
32. **NEW, S136: NOT EVERY SPLIT IS DRIFT.** §4's seven banner labels are accurate per lesson.
    Before normalising a variation, ask whether it CARRIES INFORMATION — uniformity that
    destroys meaning is a regression wearing a tidy shirt.
33. **NEW, S136: NO INSTRUMENT READS PROSE.** A suite grows to cover what it can see, and the
    uncovered region is invisible precisely because nothing reports on it. The sumo error
    survived 135 sessions at 69 green gates. **Read the book, not only the measurements.**
