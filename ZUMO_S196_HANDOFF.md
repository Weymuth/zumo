# ZUMO — S196 HANDOFF (written at S195 close · paste at top of Session 196)

## READ THIS FIRST

**NOTHING FROM S195 IS PUSHED.** Six paths differ from HEAD (`e57904c`) — five modified, one
**deletion**, one new file, one handoff rename. **0 unbumped.**

**THE DELETION IS THE ONE THAT GETS MISSED, AND IT IS THE ONLY RED GATE.**
`images/L03_IMAGE_3-14_astar_board.jpg` is the S194 rename's delete side — the add side landed,
the delete side did not. It is a separate checkbox in GitHub Desktop. **Gate §10 stays red until
it goes, and it is the only gate failing.** Proved in a scratch copy: delete the file, leave
`IMAGE_WORKLIST.md` untouched, and `image_audit --check` reads current and `book_gates` returns
ALL GATES PASS. **The committed worklist is right and the file is the error** — do not regenerate
the worklist to match the tree.

**`site_parity` IS DISCHARGED FOR S194's PUSH AND IS OWED AFTER THIS ONE.** S194's work landed as
`e57904c` (Aug 29, 07:11 EDT) — **the S195 handoff's "NOTHING FROM S194 IS PUSHED" was stale by the
time it was read, the SECOND SESSION RUNNING.** Verified at S195 open: **PARITY twice, 11:25 and
11:27 UTC**, 13m15s and 15m26s past the 10m57s floor. This push moves no asset except a deletion,
so the asset arm should not move — run it twice past the floor anyway and believe the repeat.

**`byte_audit` OWES NOTHING. Zero payloads moved and zero bytes.** Every S195 edit is a syllabus
sentence, three instruments and one new instrument. The harness was never stood up. Standing
control **20,592**.

**81/82 gates** (§10, the orphan, above) · `gate_payload_match` **PASS**, advisory unmoved at **635** ·
`retired_claims` **CLEAN, 24 registered** · `quiz_bank --check` **16 banks valid** ·
`callout_id` **1135** · `census --selftest` ALL CONTROLS PASS ·
`session_versions --selftest` ALL EIGHT · `build_css`, `build_worklist`, `build_syllabus_html`,
`prose_canon` all `--check` clean.
**Tally unmoved: 103 closed / 96 fixed / 2 parked / 140 open of 245.**

---

# 1. WHAT S195 DID

## DJ'S RULING: L09 AND FORWARD ARE TABLED. THE SCOPE IS L01–L08 ACCURACY.
Every open worklist row is L09 or later — **L01–L08 has zero**, derived structurally from
`census.worklist()`, not read off a handoff. That is not a proof of correctness; it means GPT's
review pass is exhausted there and the work has to come from the other registries.

## THE QUIZ BANKS ARE IN CANVAS. A NEW INSTRUMENT SHIPPED TO PUT THEM THERE.
`quizzes/qti_export.py` **v1.2** converts the sixteen banks to Canvas QTI 1.2. Three packages were
built and imported successfully: **63 question banks** (choice/matching split per set) and
**16 practice quizzes** (459 items). DJ built and took the L01 gate quiz; the draw re-randomised.

**RULINGS MADE, ALL WRITTEN INTO THE SYLLABUS (v1.4 → v1.5):**
- **The gate quiz is GRADED; the Post-Build Checks are UNGRADED PRACTICE.** The gate is structural —
  the whole flipped model rests on it — and the milestone already measures learning better than
  eight multiple-choice items do. Grading the after set pays twice for one measurement, and the
  weaker one.
- **The gate is OPEN BOOK, OPEN NOTES, and the syllabus now says so.** It is taken at home,
  unproctored, with the textbook a tab away; silence there traps the conscientious student who
  assumes closed-book. The questions ask *why*, so an open page helps only someone who read.
- **Matching items are OUT of the gate draw.** A four-pair item is several times the work of one
  multiple choice. **Measured before deciding:** the matching pools are tiny (median two, one set
  has none), so a separate random group was not available — a draw of one from one is not a draw.
  They live in the practice package instead, where unequal length costs nobody anything.

**TWO PACKAGE DEFECTS, BOTH FOUND BY A ROUND-TRIP ARM AND NEITHER BY THE FIRST CONTROLS:**
1. **`&nbsp;` is not valid XML** — five entities are predefined and that is not one. The package
   did not parse; Canvas would have refused it. **The control was ASSERTING THE DEFECT.**
2. **`<code>` was a real XML CHILD of `<mattext>`.** It parsed fine, which is why it was dangerous:
   Canvas takes the node's TEXT, so all 42 code spans would have vanished **with no error anywhere**.
   Canvas's own exports entity-encode the markup inside `mattext`. Confirmed fixed visually.

**GENERALISE: THE ARM THAT PASSES IS NOT THE ARM THAT WATCHES.** Both defects were invisible to a
selftest that only checked the emitter against itself.

## THE L01–L08 BANK AUDIT: FOUR SWEEPS, ALL CLEAN
854 questions. **identifiers** (every function/constant asserted exists in its lesson) — 3 hits,
all deliberate distractors, **0 real**. **section references** — **0**. **numeric claims** — 19 hits,
all in distractors, **0 real**. **section-count claims** — **0**.

**A RULING I MADE THIS MORNING WAS WRONG AND THE SWEEP OVERTURNED IT.** I judged `L01_A12`
unanswerable — it asks for a Lesson 4 function name in a Lesson 1 quiz. **Lesson 1 says it
outright**: *"by Lesson 4 it has a name, `waitForStart()`, and it is a safety rule, not a
convenience."* The stem asks for the name AND the status and the keyed option gives both. It is a
near-verbatim comprehension check. **A ruling made against a description of an artefact is a lead;
the artefact is the answer** — and the forward-pointer rule now stands at five of five, not four.

## `retired_claims` v1.1.2 → **v1.2.0** — S194's OPEN ITEM, TAKEN
`assert_true_text` now reads a `true_false` question's `why:` in **both** directions. It previously
read stem AND why only when `correct is True` and **NEITHER when False**, leaving **134 `why:`
fields across the sixteen banks (64 in L01–L08)** as prose in the book's voice that no instrument
read. **Fourth occurrence of the family** after S193's `L10_B21`. The STEM of a false true/false
stays excluded by structure — it is the declared-wrong trap.

S194 declined this on the grounds that a session changing the content should not also change what
watches the content. **That objection lapsed: S195 changed no bank content.**

**Controlled on the live tree, both directions.** A retired claim planted in `L01_B11`'s `why:`
**FIRES under v1.2.0 and is SILENT under v1.1.2 on the identical file** — blindness demonstrated,
not asserted. **The first plant injected nothing** (it matched a field order the YAML does not use)
and the assert caught it. Bank restored byte-exact. Existing `CONTROL E` was safe but
**under-specified** — its fixtures are stem-only, so it passes identically under both versions.
Added **E2/E3/E4**; grafting them onto HEAD's code proves they discriminate.

## `prose_canon` v1.1.0 → **v1.3.0** — TWO OF THREE OWED ARMS BUILT
**ARM 4 (section-count claims).** Unbuilt since S182 because the obvious predicate — prose number vs
payload banner count — **convicts L02 eight times and L06 once, all on correct prose.**
**The two numbers reconcile exactly:** L02 teaches NINE (Header · Includes · Objects · Constants ·
Global Variables · Prototypes · setup() · loop() · Helpers); a payload body ships SEVEN banners
starting at `HARDWARE OBJECTS`, and `mainCpp()` auto-prepends the header and the `#include` (S44).
**7 + 2 = 9.** So the discriminator is not the number but WHAT THE SENTENCE COUNTS: a canon claim
expects nine, a file claim expects that payload's banner count, and **anything unclassifiable is
REPORTED UNADJUDICATED, NEVER CONVICTED.** Live: 0 findings, 4 unadjudicated, all legitimate.

**ARM 1 (printed banner sequences).** **THERE IS NO SINGLE CANON ORDER.** Derived from all 367
payload bodies with 2+ banners: eight orderings resolving to **THREE SPINES** — `main.cpp`,
`RobotConfig.h`, and the in-`setup()` sub-banners. **A flat canon would have convicted 292 of 367.**
The test is **SUBSEQUENCE, not equality** (§18.3: an omitted section is not a mistake). Boundaries
are `<pre>`/`<code>` ELEMENTS — a first draft segmented on banner names and reported 22 findings,
every one an artefact of gluing two listings together. Measured: **203 of 203 banner occurrences
sit inside a code block**, so the element boundary is total coverage of the phenomenon.

**STATED COVERAGE LIMIT, PRINTED BY THE ARM ITSELF:** a block needs 2+ distinct banners to have an
order, so it judges **23 blocks** and **SEVEN LESSONS HAVE NONE (L06, L10–L15).** Clean there does
not mean they were checked. 21 of the 23 are in L01–L08, so coverage sits where the scope is.

**THE CONTROL THAT TAUGHT THIS FAILED FIRST, FOR THE WRONG REASON.** The initial plant went into an
L03 block holding ONE banner — a block the arm correctly declines to judge — so the arm was silent
and the control read as an arm failure. **A control must plant where the arm LOOKS.** Twelve
controls now pass, including C1/C2 (a `RobotConfig.h` order is legal on its own spine and fires
reversed — the control that would have caught a flat predicate) and F3 (the blind lessons are
asserted, so the limit cannot drift unnoticed).

**ARM 2 (placement claims) is the last one owed.**

## `build_syllabus_html` HAD NO ARGUMENT HANDLING AT ALL — v1.0 → **v1.1**
The write branch was the fall-through, so **`--help` regenerated the file** and a typo of any flag
would have too. Same defect `image_audit.py` was fixed for at **S174**; this one never got the
guard. Now: unknown argument exits 2, `--help` writes nothing, and a real `--check` exists.
**Found by running `--help` and watching it write.**

**AND IT BIT AGAIN DURING THE TRIPLE CHECK.** Running HEAD's copy with `--help` to demonstrate the
old behaviour **rewrote `syllabus.html` with the v1.0 header**, contaminating the tree mid-check.
Caught by the byte comparison, repaired, re-verified. **Demonstrating a write-defect executes it.**

## `session_versions` — CONTROL G EARNED ITS KEEP
Registering `qti_export` in `ARTEFACTS` was not enough: **Control G failed, naming it missing from
BOTH emitted blocks** — registered but never visible. Added to `--live` and `--handoff`. All eight
controls pass. `session_versions` **v1.33.0** (table edit, no version bump — the roster is data).

## BIBLE **v8.191 → v8.192** (S195, moderate)
One entry, landed at the TOP after asserting nothing preceded the anchor (the S194 defect), both
version homes moved, and **the S175 regeneration obligation FIRED** — `build_worklist --check` went
red on the bump and `GPT_WORKLIST.md` was regenerated. The coupling works.

---

# 2. S196 OPENS HERE

## THE BENCH IS THE FRONTIER AND IT IS THE ONLY THING A KEYBOARD CANNOT DO
`ZUMO_FLAGGED_CHECKS.md` holds **eighteen rows, F1–F18, every one L01–L04** — claims the book makes
to students that have never been checked against a robot. Two are falsifiable and **delete printed
prose if they fail**: **F10** (L02 C2's *why it takes two trips* paragraph comes out) and **F14**
(L03 Bonus 2's reveal must put gearbox asymmetry back as the headline). **F5** covers three battery
numbers appearing in **34 figures across L01–L03**, never read off a real pack.

**F17 IS THE BLOCKER UNDER F15, F16 AND F18** and has been since **S51 — fifty-one sessions.** It
needs a white surface and **matte black electrical tape** (IR-absorbing; a marker line is
unreliable for reflectance). DJ said he could do it the afternoon of Aug 29. **Ask first, before
proposing any keyboard work** — fixing prose that a bench result deletes is wasted work.

## THEN, IN ORDER
1. **`prose_canon` arm 2** (placement claims — "above `setup()`"). The last owed arm, and the parser
   and spines it needs are now in the file.
2. **The seven pinned residue sites** — three L05/L06 headings and four Maker labels, **ONE fix, not
   two** (a step title and the Maker label that opens it move together). **Untouched a NINTH
   session.** The Fix Tracker names this exact sweep as its closer.
3. **`L07_GRAPHIC_7-15`'s one real overflow** — `RobotSensors.h`, 14.5 units.
4. **Canvas remainder (DJ's hands):** build the other 15 graded quizzes, drawing **10** from each
   `before_choice` bank (**8** for a post-build bank), 1 pt each.

---

# 3. STILL OWED, UNCHANGED
- **Seat the §16 debt.** Still 26 rules, untouched a **tenth** session.
- **`ZUMO_BENCH_TESTS.md` ranks itself.** Run **1 `L10-B1` · 2 `L02-B2` · 7 `L10-B2`** in one sitting.
- **`ZUMO_GPT_REVIEW_WORKLIST.md` footer carries a second version token** (`Worklist v1.2`)
  disagreeing with the header home `session_versions` reads (v1.12). Flagged six sessions, not ruled.
- **The `(none needed)` ruling (S183) is unbuilt** — 133 sites, **every one L01–L07**, dead centre of
  the current scope. S184 priced it: the ruling does not fit the tree as worded, because in L08–L16
  those banners are absent entirely, so it is an ADD of ~148 × 4, not an edit. **Needs DJ.**

# 4. STANDING, UNCHANGED
- **`gate_payload_match` IS NOT ONE OF THE GATES** (S137) and **TAKES ARGUMENTS** — pass
  `newproject.html lessons/Lesson_*.html`, or it reports a COVERAGE failure on a subset.
- **`--live` and `--handoff` PRINT, they do not WRITE** (§24.20). **LIVE.md carries TWO `**Versions:**`
  lines** — line 6 is current. **Keep the Status line to ONE line.**
- **The visible §5b banner is spelled `Version 04.31` — BARE.** A `v`-prefixed grep cannot see it.
- **`quiz_bank.py` AND `qti_export.py` LIVE IN `quizzes/`, NOT THE REPO ROOT.**
- **A BIBLE SESSION BUMP IS A REGENERATION OBLIGATION** (S175). **A BIBLE BUMP HAS TWO HOMES** (S185) —
  the version line AND the changelog entry `current_session()` reads, newest first, one per
  PARAGRAPH. **Anchor on the LINE-START version form AND confirm nothing precedes it** (S194).
- **A CALLOUT COSTS THREE PINS** — image references, the gate 47/59 census in BOTH homes, and the
  §27.11 digest. Prove count AND RANK before moving the digest.
- **YOU CANNOT CITE A WRONG TALLY IN A GATED HOME.** Gate §24.24 cannot tell a tally figure from any
  other digit beside a status word. **Spell retired or incidental figures in WORDS.** Describe the
  shape; never quote the string.
- **THE SYLLABUS IS GENERATED.** `syllabus.html` from `ZUMO_Syllabus_WORKING.md` via
  `build_syllabus_html.py`. **EDIT THE MARKDOWN, NEVER THE HTML.** Inline styles by DJ's ruling — he
  pastes it into Canvas, which strips `<style>` and `class=`.
- **A PROJECT-FILE COPY IS NOT THE TREE** (rule 32, S194). `/mnt/project`'s syllabus is stale.
  **Diff before you replace.**
- **A PREDICATE AT ZERO PROVES THE OLD STRING IS GONE, NEVER THAT WHAT REPLACED IT READS CORRECTLY**
  (S192 standing rule).
- **`grep` LOCATES CANDIDATES AND NEVER ANSWERS** (§24.22). Fired three times in S195 alone: the
  L05 seven-sections claim, the §8A.4 reference, and the eight-vs-seven banner count. **Every one
  was resolved only by the parser, and every one would have been filed as a defect on the grep.**

# HARNESS — NOT IN THE REPO. RUN THE SCRIPT.

```
apt-get install -y gcc-avr avr-libc
sh harness_setup.sh                     # objects: 41  AND  core stderr: clean
python3 byte_audit.py --sizes           # ~4 min at 221 payloads
python3 byte_audit.py --selftest ; --check ; --discards
```
**`--selftest` CANNOT RUN BEFORE `--sizes`** — CONTROL K dies with a `KeyError`.
**Run `harness_setup.sh` in the FOREGROUND and read `objects: 41`** — backgrounded, it has died
silently at `== core build ==` with 0 objects.

# SESSION OPEN, COMPLETE
`git ls-remote` → fresh clone → verify the Bible's internal version → read `LIVE_ZUMO_TEXTBOOK.md` →
`book_gates.py` → `session_versions --check` **and `--selftest`** → `census --selftest` →
`gate_payload_match newproject.html lessons/Lesson_*.html` → `callout_id` → `retired_claims` →
`quiz_bank --check` → `build_css --check` → `build_worklist --check` → `build_syllabus_html --check` →
`prose_canon --check` → `byte_audit --check` → `site_parity` twice.

# STANDING AUTHORITY — §24.17, §24.19, §24.21
**Decide and report; do not ask.** Carve-outs: facts about the ROOM · irreversible moves ·
RoboLore brand and course scope. **§24.19 is the tiebreaker** — what is best for student learning.

---
<!-- VERSION BLOCK: emitted by session_versions.py --handoff. Never hand-typed. -->
Fresh-clone verified at **`e57904c`**. Census **41,814**.
Bible **v8.192** · `BookComponentStandard` **v01.13.0** · Maker **v2.70** ·
`marks/` **41** · `icons/` **49** incl. LICENSE.
`ZUMO_Syllabus_WORKING.md` **v1.5**.

Instruments: `book_gates` **v1.76.4** · `lesson_inventory` **v1.3.5** ·
`gen_component` **v1.6.1** · `pill_sweep` **v1.1** · `gate_payload_match` **v1.9.5** ·
`build_family_map` **v1.6.6.6** · `callout_id` **v1.0** · `keyterm_prefix` **v1.0.1** · `build_mark_index` **v1.1.0** · `gen_bonus_banner` **v1.4.1** ·
`gen_part_banners` **v1.2** · `session_versions` **v1.33.0** · `fit_raster_svg` **v1.2** ·
`flatten_alpha` **v1.2** · `svg_layout_audit` **v1.21.2** · `site_parity` **v1.2.1** ·
`build_css` **v1.4.0** · `build_syllabus_html` **1.1** ·
`image_audit` **v1.3** ·
`strip_inline` **v1.2** ·
`build_worklist` **v1.2** ·
`qti_export` **1.2** ·
`prose_canon` **v1.3.0** ·
`retired_claims` **v1.2.0** ·
`census` **v1.2.0** ·
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

Lessons: L01 v03.32.2 · L02 v03.26.1 · L03 v03.47.1 · L04 v04.29.6 · L05 v04.30.0 · L06 v04.37.2 · L07 v04.33.1 · L08 v04.34.4 · L09 v05.28.0 · L10 v02.30.7 · L11 v02.31.4 · L12 v01.35.4 · L13 v02.39.0 · L14 v02.36.2 · L15 v02.32.2 · L16 v02.28.1.
