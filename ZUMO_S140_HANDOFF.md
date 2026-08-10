# ZUMO — S140 HANDOFF (rewritten at S139 close · paste at top of Session 140)

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

# THE ONE THING TO CARRY OUT OF S139

**AN ENTRY FILED IN ONE HOME IS NOT FILED — AND THIS TIME THE READER WAS RIGHT AND THE
BOOK WAS WRONG.**

S138 bumped the Bible version home to v8.130.2 and wrote its entry into line 17's
`Current:` chain, but **never inserted the line-start changelog entry.** The diff proves the
convention: S136 and S137 each show `@@ -17 +17 @@` *and* `@@ -97,0 +98,2 @@`; S138 shows
only the first. `bible_consistency()` reads the line-start list, so it believed S137 had
just run and reported LIVE.md and the handoff as wrong — **when both were right.** That is
the reverse of the usual case and the reason to read the disagreement rather than obey it.
Note the two homes have **never been byte-identical** (S137: 2,607 chars filed against 2,816
in the chain, differently worded and tailed), so **filing is authoring, not copying.**

**AND THE CLOSE PUSH IS WHERE THINGS BREAK, BECAUSE NOTHING RUNS AFTER IT.**
`session_versions --check` was **exit 0** at `442f68d` and exit 1 at `2f33655`. That is the
second session running — `gate_payload_match` went PASS -> FAIL inside the S137 close push
the same way. **Re-run the full instrument set AFTER the final push, not before it.**

---

# CARRIED FROM S138

**AN ASSET IS NOT A DELIVERY UNTIL SOMETHING REFERENCES IT.** A file nothing points at lands
in `image_audit`'s unreferenced bucket and moves three counters. The instruments watch the
DIRECTORY as well as the prose, so a half push is louder than no push.

**A TEXT MATCH LOCATES; IT NEVER ANSWERS (§24.10, v8.130.1).** `grep`, `rg`, `str.find`,
`in`, `re.search`, or an `--audit` flag doing any of those internally — one instrument in
different clothes. **A hit is READ IN FULL before it is reported, and an empty result is
never reported as absence.** A lead never carries a ruling request.

**NO INSTRUMENT THAT READS THE TREE CAN SEE A RULING.** Search the session record before
measuring the book.

---

# SEPTEMBER 8 IS ABOUT FOUR WEEKS OUT

**READING QUIZZES — 2 of 12 WRITTEN (L02, L04).** Status is DERIVED:
`python3 quizzes/quiz_bank.py --status`. **Read `quizzes/QUIZ_SPEC.md` first — it is now
v1.1.0 and the format mix CHANGED.** **THE ORDER IS CANON: READ -> FIX -> QUIZ.** L04 is
the proof: five of its questions would have been keyed wrong against v04.28.3.

**L03 IS NEXT AND IT IS UNBLOCKED** — read at S137, fixed at S137, bank not yet written.

**THE IN-SCOPE FIGURES ALL NEED DJ AND THE ROBOT.** Stills **3.2 · 3.5 · 3.6 · 4.1 · 4.3 ·
12.1**, videos **3.1 · 4.1 · 6.1 · 8.1**. `GRAPHIC 15.4` was never produced; its brief is in
the S135 chat. **VIDEO 3.1 carries L03's opening page** and is the highest-value shot.

---

# STATE

<!-- VERSION BLOCK: emitted by session_versions.py --handoff. Never hand-typed. -->
Fresh-clone verified at **`2f33655`**. Census **40,479**.
Bible **v8.131** · `BookComponentStandard` **v01.13.0** · Maker **v2.45.5** ·
`marks/` **41** · `icons/` **49** incl. LICENSE.
`ZUMO_Syllabus_WORKING.md` **v1.2**.

Instruments: `book_gates` **v1.64.3** · `lesson_inventory` **v1.3.5** ·
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

Lessons: L01 v03.28.2 · L02 v03.21.2 · L03 v03.40.2 · L04 v04.29.0 · L05 v04.28.1 · L06 v04.31.1 · L07 v04.31.1 · L08 v04.30.1 · L09 v05.26.1 · L10 v02.27.1 · L11 v02.28.2 · L12 v01.31.2 · L13 v02.28.2 · L14 v02.33.1 · L15 v02.30.1 · L16 v02.22.1.

**69/69 gates.** `lesson_inventory --anomalies` silent · family map **1119/1119** ·
`callout_id --audit` **1119, 0 problems** · `keyterm_prefix --audit` **238 = 151 + 4 + 83 + 0** ·
`build_css --check` current at 574 rules · `image_audit --check` current ·
`gate_payload_match` PASS · `strip_inline --verify` **0 dead class names** · the pin is
**55 rows** · `quiz_bank --selftest` **9/9 controls loud** · `quiz_bank --check` **2 banks valid**.

---

# WHAT SHIPPED IN S139

**THE BIBLE'S MISSING S138 ENTRY WAS FILED**, using S138's own chain-copy text verbatim:
2 added, 0 deleted, the same hunk shape as S136 and S137.

**`session_versions` v1.24.0 -> v1.24.1 — THE HANDOFF READ IS NOW SCOPED.** `check()` read
the WHOLE handoff into `_versions_in`, which builds its dict with `re.findall`, so the LAST
occurrence of a key won: the handoff states `Bible **v8.130.2**` in its STATE block and
eighty lines later refers in prose to `(Bible v8.130.1)`. **The prose won.** LIVE.md never
had this — its read is already scoped to line 6, asserted to start with `**Versions:**` — so
the handoff took the same discipline: **a WINDOW anchored on the VERSION BLOCK marker.**
`_versions_in` is untouched, because it runs on generated text too and a rule about prose is
meaningless there. **THE MARKER IS NOW EMITTED** — its own sentence claimed it was, since
S138, while nothing produced it. **No whole-file fallback** (a fallback reinstates the defect
on exactly the file that most needs checking), and **a generated key absent from the window
is reported, not skipped.** **CONTROL H, three directions, plus a blinding run. ALL EIGHT PASS.**

**L04 — 11 OF 13 READ FINDINGS APPLIED. L04 v04.28.3 -> v04.29.0, MODERATE.**
Challenge 4's template did not compile (`LINE_SEEN` used, never declared) — now three blanks,
which is right because §8A.2 says choosing thresholds from real data IS the skill and
Challenge 1 already blanks one. `LEARN 4.38` cited a section L02 does not have. §8A.8's
*hundreds per crossing* contradicted its own arithmetic (10 Hz × half a second = FIVE); now
*every loop, not every crossing*, true at any tape speed. §5.5 presented arrays as new when
L03 §8A.5 taught them. Step 2's reveal contradicted its own pseudo-code and the shipped file
order. C4's function list named two sensors where everything else loops three.

**THRESHOLD CANON: 600 BOOK-WIDE IN L04, WITH THE MARGIN STATED (DJ ruling).** The census
split cleanly — six 500s all TEACHING, six 600s all PRACTICE — so a student applying the rule
just taught wrote 500 and met 600 in every reveal. **Eight sites swapped; TWO were REWRITTEN**
— substituting 600 into *"500 is the natural darker-than-halfway line"* manufactures a false
sentence, the S137 F=ma failure exactly. 500 stays the midpoint; 600 is a stated margin.

**THE *SEVEN-SECTION* FINDING WAS REVERSED BY MEASUREMENT.** L02 §3.1's Color Key lists eight
rows with Prototypes marked unnumbered — seven numbered — so the sentence is true. The banner
census counted `// ===== =====` banners, which Header and Include never carry, giving a
ceiling of 6. **The instrument could not return the answer the claim asserted.** This retires
the L03 §5.1 queue item.

**`waitForStart()` / `checkBattery()` moved into a new *Startup & safety* Quick Reference
group** (`#qr-startup`) — none of the ten existing groups fitted.

**QUIZ_SPEC v1.0.0 -> v1.1.0 — THE FORMAT MIX WAS ARITHMETICALLY IMPOSSIBLE.** MC ~70%,
TF cap ~20%, matching *one or two, no more*: at both ceilings a 50-question set has an **MC
floor of 76%.** L02 met ~70% only by running TF at **22%, over its own cap**, unnoticed
because **nothing validates a mix.** **The matching allowance moved to ~10%, NOT the TF cap,
and the reason is signal** — true/false is 50% guessable, while matching's mandatory
`extra_answers` absorbs the guess. The superseded cap was **also restated in the per-format
rules** and fixed there in the same pass. **L02 IS NOT REBALANCED** and the spec says so.

**L04 QUIZ BANK v1.1.0 — 73 QUESTIONS.** before 51 (MC 69% / TF 20% / matching 12%), after 22
(MC 68% / TF 23% / matching 9%). Every question cited. Pins `lesson_04: v04.29.0`.

**CSS regenerated THREE times; digest `ce43da62` -> `d7702428` -> `3ce57062` -> `2cd8cd62`.**
Rules and declarations UNCHANGED at 574/2,033 every time, class set byte-identical, and **the
acceptance test was the RESOLVED STYLING (rule 24): all 574 declaration blocks byte-identical.**

---

# S140 QUEUE

## 1. L03'S QUIZ BANK — READ AND FIXED AT S137, UNBLOCKED
`quizzes/QUIZ_SPEC.md` **v1.1.0** is the recipe; the format mix changed, do not use L02 as
the template. **L02 is off-spec** (TF 22% before, MC 83% after) and is deliberately not fixed.

## 2. L04'S TWO REMAINING FINDINGS
- **#12, the Figures-table zebra breaks** — IMAGE 4.4 and GRAPHIC 4.1 are both shaded. Cosmetic.
- **#8 and #9 are BENCH.** The wave test (§6 Step 4 says readings *jump*; §8 says a robot in
  the air already reads maximum, so a hand makes them FALL — and §8 says *a few millimetres*
  against Step 4's *a couple of centimetres*), and Act Two's row 1: `P:` + 4 digits + a
  3-space wipe = **9 characters on an 8-character row**. **Neither is asked in the L04 bank.**

## 3. CONTINUE THE READ — L05 IS NEXT
**L01, L02, L03 and L04 are READ. L05–L16 ARE NOT.**

## OPENED S139, UNRULED
- **`IMAGE 4.1` IS A PHANTOM IN THE FIGURE COUNT.** S138 retired it — table row and body
  placeholder both gone — but **L04's Figures PREAMBLE still prints the tag**, in the sentence
  explaining that IMAGE and GRAPHIC are separate series. It is **the only such sentence in the
  book**, and `image_audit` cannot tell an example from a plan. So planned reads 146 where the
  true population is **145**, and **gate 69's pin is one high.** DJ ruled *not now* at S139.
  The 146 still reconciles honestly — `[IMAGE 4.5]` left and `[GRAPHIC 4.7]` arrived, net zero
  — **which is exactly why nobody had to touch the pin.** Rule 20 shape.
- **THE CONSTANTS vs CONFIGURATION VOCABULARY DRIFT** survives the seven-section reversal.
  L03 uses `CONFIGURATION` / `STATE VARIABLES` where L02 uses `CONSTANTS`; the Maker emits 28
  distinct banner names. **Derive the canonical set before touching any sentence about it.**
- **Challenge 4's reveal keys `LINE_SEEN = 600` while the template blank invites the student's
  own number** from the Step 4 table. Consistent with the new canon, but the reveal does not
  say a different well-chosen number is fine.

## Carried from S137/S138, still unruled
- **NO GATE TIES A CHALLENGE CARD TO ITS STARTER PAYLOAD.** Measured: reverting `buttonB` out
  of the `constrain` payload while leaving the card gated **passes all 69 gates, exit 0.**
- **THE 3Pi+ NOTE COMES OUT OF L03** — DJ: *"that will eventually be a separate book."*
  `data-callout="3.33"`. **PRICED: it moves three baselines from 1119 to 1118.** Neither park
  file will take it; **it needs a new root file as the 3Pi+ book seed.**
- **`class period` APPEARS IN L10.** §3.1 forbids calendar facts inside a lesson. **Read it
  before removing** — it may be innocent prose.
- **§4.2: *stall current ~1.5 A … roughly 5× its free-running draw.*** Pololu's no-load figure
  is ~0.10 A, which is 15×.
- **L03 C1's hint hands over the exact two numbers its own template blanks ask for.**
- **Two `[CONTENT PLACEHOLDER]` blocks are still live in L03** — brushed-vs-brushless and the
  three-Roombas story, both *DJ to supply*, in week-one material.
- **NO GATE HOLDS A QUIZ BANK** and **NO GATE HOLDS A NAV PILL.**
- **§7's BANNER is still three spellings** — 9 lessons `· Test It`, 6 bare, L12 `· Calibrate`.
- **L14's §10 is the only §10 that is not an exit ticket.**
- **Whether the `after` quiz set is graded at all.** The syllabus split (Quizzes 20 / Exit
  Tickets 10) has no third slot, and BRAIN CHECK 03 already does that job in-page.
  **L02 and L04 both now have `after` sets, so this needs a ruling.**

## Carried from S135, still open
- **THE SPIRAL ARC — RULED, ENUMERATED, DELIBERATELY NOT STARTED.** §18.1's "1–2 prior
  concepts" is a **FLOOR** (DJ: *"floor. No ceiling."*). **Do not start without finishing.**
  13 of 171 units, 8%. **Five approved first:** L04 4.4→L03 · L05 5.1→L04 · L06 6.7→L03,L04 ·
  L12 12.2→L06 · L15 15.2→L04. Then 17 self-declaring cards. **THE SCAN IS BLIND TO THE REST**
  — true population **21 minimum, top end unknown.** Each star is a NEW CALLOUT minted by
  `callout_id.py --apply`, never hand-written, and it moves the family map off 1119.
  **NOTE: S139 added the L03→L04 array credit in §5.5 as PROSE, with no star** — deliberately,
  so the arc stays all-or-nothing.
- **THE FIGURE BLOCK HAS FOUR SPELLINGS.** L11 · L12 semantic `<figure>` · L13 · L15.
  **L12's is the best.**
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
code · **the mark roster RECONCILES and is gated (61). Do not re-open.** · **`build_css` is
NOT idempotent on this tree** — `.ul-ls-none-2`/`-3` alternate across runs.

## AFTER SEPTEMBER 8 — PARKED ON PURPOSE, DO NOT START EARLY
- **REDO `GRAPHIC 4.7` IN THE BLUEPRINT COMPOSITION.** Declined at S138 on evidence, not
  taste — its silkscreen read `OJ8696` where the board reads `0J8696`, and one provable wrong
  glyph means all fifteen labels are model output rather than measurement (§14). **Do not
  re-derive the orientation** — Pololu 0J63 §3.5 gives the convention, DJ confirmed on a real
  board, chips run **5 4 3 2 1** left to right.
- Challenge card Pass B · monetization/ebook · DISCOVERIES tagging.

## Learner mode & book content
L03_C05 Variable Speed · L03 C01/C05/C06 reference a `finished` payload that does not exist
for L03 · whole-template starters L08/L09/L10 · Maker batch · L01 VS Code multi-root step.

## Bench (need the robot — parked with photography)
Q017 L09 six numbers · Q044 calibration-spin · Q046 gyro-bias · L02 §5 green-LED ·
Constrain RUN_MS · cm/s at a stated BASE_SPEED · the floor rig for 3.2 / 3.5 / VIDEO 3.1 ·
a real TRIM run for `IMAGE 3.6` · **THE SURFACE TEST: run 7E on a lab tile.** ·
**L04's wave test and Act Two row-1 overflow.**

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
42. **NEW, S139: A SPEC'S OWN NUMBERS CAN BE ARITHMETICALLY IMPOSSIBLE.** QUIZ_SPEC asked for
    ~70% MC under caps whose floor was 76%. **Nothing validated the mix, so the first bank
    quietly broke a cap to satisfy it.** When a ratio must give, give it to the instrument
    that MEASURES BETTER, not the one that is easiest to write.
