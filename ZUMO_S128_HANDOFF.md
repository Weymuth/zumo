# ZUMO — S128 HANDOFF (written at S127 close · paste at top of Session 128)

## Session open ritual (do this without being asked)
1. **`git ls-remote https://github.com/Weymuth/zumo.git HEAD` FIRST.** If the clone's
   `git log -1` does not match, fetch the sha by name (§12.4, *caches lie*). A stale
   answer is timing, not caching — **retry a minute later before concluding a push
   failed.** Saying "the push didn't land" is a wrong answer, and a wrong answer costs 3×.
2. Read `LIVE_ZUMO_TEXTBOOK.md` — verify date / status / versions.
3. **Do NOT grep the Bible version.** `session_versions.bible_consistency()` parses it; the
   Bible has THREE homes — header line 17, the `Current:` clause, and the newest CHANGELOG
   entry — and it fails if any two disagree.
4. Run the full suite, and **READ THE EXIT CODE, NOT THE LAST LINE**:
   `book_gates.py` · `gen_component.py --selftest` · `lesson_inventory.py` ·
   `lesson_inventory.py --anomalies` · `pill_sweep.py --selftest` ·
   `pill_sweep.py --audit lessons/Lesson_*.html` · `build_family_map.py` ·
   `class_sweep.py --selftest` · `fit_raster_svg.py --selftest` · `flatten_alpha.py --selftest` ·
   `svg_layout_audit.py --selftest images/L01_GRAPHIC_1-13_zumo_rear_view.svg` ·
   `regex_audit.py --selftest` then `regex_audit.py` · `build_worklist.py --selftest` ·
   `font_stack_sweep.py --selftest` then `font_stack_sweep.py` ·
   `session_versions.py --selftest` then `--check` · `site_parity.py --selftest` then `site_parity.py` ·
   `build_css.py --selftest` then `--check` · `image_audit.py --selftest` then `--check` ·
   `strip_inline.py --selftest` then `strip_inline.py --verify` ·
   **`entity_sweep.py --selftest` then `entity_sweep.py`** (NEW S127 — a bare run must report
   0 conversions; anything else means a character re-entitised) ·
   `build_palette.py --selftest` then `--check` ·
   `color_index.py --selftest` then `--check` ·
   `gen_bonus_banner.py --selftest` · `gen_part_banners.py --selftest` ·
   `gate_payload_match.py newproject.html lessons/Lesson_*.html` ·
   `next_pointer.py --selftest` then `--check` ·
   `title_feed.py --selftest` then `--check`
5. If `flatten_alpha --selftest` prints `NOT FULLY TESTED`: `pip install cairosvg
   --break-system-packages`. **Needed every session.**
6. **NEVER run `build_css.py --help`.** It has no help branch — it BUILDS, against whatever
   tree is on disk. **`session_versions.py --help` has no help branch either.**
7. `--anomalies` is SILENT when clean. Anything it prints is a real lead.
8. **Do not hand-type a version, and do not hand-type a COUNT.** `session_versions.py
   --live` / `--handoff` EMIT the blocks.
9. **`gate_payload_match.py` needs the FULL lesson glob.**
10. Entrypoints are traps: `lesson_inventory.build(path)`, `gen_component.load_standard()`,
   `svg_layout_audit.audit(path)`, `flatten_alpha.flatten(path)`, `build_worklist.build(dir)`,
   `regex_audit.audit(paths)`, `session_versions.bible_consistency(path)`,
   `build_css.build(paths)`, `image_audit.audit(paths)`, `strip_inline.build(paths)`,
   `build_palette.build()`, `class_sweep.sweep(paths)`, `color_index.index(paths)`,
   `title_feed.build(root)`, **`entity_sweep.build(paths)`**.
11. **A CLONE IS NOT THE SITE.** Run `site_parity.py` after any push. It can FAIL on the first
   run in the minute after a push and pass on retry — Pages lag, not a defect (S112).
12. **VERIFY THE PUSH BY FRESH CLONE AND MD5 — AND DIFF THE STAGE AGAINST THE CLONE.**
13. **The lesson files are `Lesson_NN.html`, no topic suffix, and they live in `lessons/`.**
14. **`css/semantic.css` IS HAND-EDITED ON PURPOSE (§27.15).** It is the ONLY stylesheet file
   that is. `css/book.css` is still DO-NOT-HAND-EDIT — edit the source and regenerate.
15. **`regex_audit.py` after any gate you write.**
16. **`session_versions --check` will report ~24 disagreements at session open and they are
   EXPECTED** — every one names `ZUMO_S128_HANDOFF.md`, the INCOMING document, which
   describes the state at open and is stale by definition once work starts. Read WHICH
   artefact each line names. If a line names LIVE.md or the Bible, that IS drift.
17. **`session_versions --selftest` FAILS THE MOMENT THE BIBLE NAMES THE CURRENT SESSION**
   — Control C reports *the outgoing handoff is read by S(N+1)*. That is not a defect and
   not a push failure; it is the tool saying the session is not closed. It clears when the
   S(N+1) handoff replaces this one. **S127 hit this AFTER a verified-clean push** and the
   correct read was *finish the close*, not *something broke*.

---

# SEPTEMBER 8 IS ABOUT FOUR WEEKS OUT

**14 images outstanding of 141.** Unchanged. Photography still parked.

---

# THE ONE THING TO CARRY OUT OF S127

**A DISCREPANCY BETWEEN TWO COUNTS CAN MEAN BOTH INSTRUMENTS ARE WRONG — AND THE
DENOMINATOR THE WHOLE NEXT ARC WOULD HAVE BEEN PRICED ON WAS OFF BY 700.**

The handoff carried *95 distinct / 2,701* against S126's re-derived *3,258*, same distinct
count, and called it a scope difference to be settled. It was settled, and the answer was
not the one the question implied. **3,258 is reproducible at exactly one scope out of an
eight-way grid** — literal bytes of the sixteen lesson files, Unicode symbol categories —
which yields **95 / 3,273**, and the 15-occurrence gap **IS the almost-equal sign U+2248**,
the only character in the census with a count of 15.

**But that scope is the defect.** The book spelled the same character two ways: **5,935
non-ASCII characters literal, 4,827 as entities.** Decoded, the true figure is **110
distinct / 3,984**. **34 characters were written BOTH ways and 15 existed ONLY as
entities** — house 16, copyright 16, spy 8, star 3, graduation cap, and the three medals —
and **those fifteen appear in no census ever taken of this book.** Every glyph number in the
handoff was low: lightbulb 114 is **118**, key 158 is **174**, bullseye 113 is **125**.

**§24.8 arriving on a DENOMINATOR rather than on a gate:** the population you can enumerate
by spelling is not the population that renders. Had the glyph arc been priced on 3,258 it
would have retired characters it could not see.

**AND DJ'S PUSHBACK IS WHAT PRODUCED THE RULE.** Asked whether all-entity would be safer, the
honest answer is that it **fails on its own terms**: entity form is three spellings, not one,
and the book already carried **14 characters spelled two ways inside entity form alone**
(em dash named 2,129 / decimal 117; apostrophe decimal 27 / hex 44, never literal). Literal
is the only direction that collapses to exactly one spelling — and the only legible one,
since **103 of the book's 143 non-ASCII characters have no named entity.**

---

# STATE

<!-- VERSION BLOCK: emitted by session_versions.py --handoff. Never hand-typed. -->
Fresh-clone verified at **`d97b00f`**. Census **40,700**.
Bible **v8.119** · `BookComponentStandard` **v01.12.1** · Maker **v2.45.4** ·
`marks/` **41** · `icons/` **49** incl. LICENSE.
`ZUMO_Syllabus_WORKING.md` **v1.2**.

Instruments: `book_gates` **v1.54** · `lesson_inventory` **v1.3.0** ·
`gen_component` **v1.6.1** · `pill_sweep` **v1.1** · `gate_payload_match` **v1.7** ·
`build_family_map` **v1.3.7** · `build_mark_index` **v1.0.2** · `gen_bonus_banner` **v1.4.1** ·
`gen_part_banners` **v1.2** · `session_versions` **v1.20.0** · `fit_raster_svg` **v1.2** ·
`flatten_alpha` **v1.2** · `svg_layout_audit` **v1.20** · `site_parity` **v1.1** ·
`build_css` **v1.3.0** ·
`image_audit` **v1.1** ·
`strip_inline` **v1.2** ·
`build_worklist` **v1.1** ·
`regex_audit` **v1.0** ·
`build_palette` **v1.1** ·
`class_sweep` **v1.0** ·
`color_index` **v1.0** ·
`entity_sweep` **v1.0** ·
`font_stack_sweep` **v1.3.0** ·
`next_pointer` **v1.2** ·
`title_feed` **v1.0** ·
`timer.html` **v1.3.2** ·
`going_deeper` **v01.6.1**.

Lessons: L01 v03.23.1 · L02 v03.15.1 · L03 v03.33.1 · L04 v04.23.1 · L05 v04.22.1 · L06 v04.27.1 · L07 v04.26.1 · L08 v04.23.1 · L09 v05.20.1 · L10 v02.21.1 · L11 v02.22.1 · L12 v01.24.1 · L13 v02.22.1 · L14 v02.27.1 · L15 v02.23.1 · L16 v02.15.1.

**58/58 gates.** `--anomalies` silent · family map **1069/1069** · `regex_audit` 0 leads ·
`build_css --check` current at **604 rules** · `strip_inline --verify` 0 dead class names ·
`color_index --check` clean · `image_audit --check` current at 14 outstanding of 141 ·
`gate_payload_match` PASS on the full glob · `next_pointer --check` and `title_feed --check` clean ·
`entity_sweep` 0 conversions, 239 held, 357 protected ·
`site_parity` PARITY at **140** referenced assets.

**§27.11 is 604 / 2,141**, unchanged — the sweep touched no class attribute, so §27.8b's
three-step sequence never ran and `css/book.css` was not in the push.

---

# S127 WORK — SEE `LIVE_ZUMO_TEXTBOOK.md` FOR THE FULL ACCOUNT

**One push, one Bible entry (v8.119), §27.16 NEW.** 4,789 entity-spelled characters converted
to the literal character across 20 files; **239 held as entities** because their literal form
is invisible in source; **357 protected occurrences** left alone in `<script>`, `<style>` and
attribute interiors.

**THE PROOF IS RENDER-EQUIVALENCE, NOT THE DIFF.** The HTML-decoded text of all 21 files is
byte-identical before and after, asserted inside the tool and again independently against a
full-tree snapshot. Census unchanged at **40,700** — only bytes moved, not lines.

**THE COUPLING PREDICTED AS DANGEROUS WAS THE SAFE ONE.** 439 entities sit inside `<pre>` and
`gate_payload_match` byte-derives Maker payloads from those blocks — but `decode_pres()` calls
`H.unescape`, so it compares DECODED text and was always invariant. It passed untouched.
**Measured before acting, not assumed.**

**WHAT BROKE WAS S126's RULE 18, LIVE: FOUR PREDICATES PINNED A SPELLING.** §25.6, §25.2, §4.5
searched for the literal string `&mdash;`; `next_pointer` EMITTED it. **`book_gates.py:396`
already carried the correct dual form eleven lines from its broken twin at 701** — one
assertion, written both ways, in one file.

**THE DANGEROUS ONE WAS SILENT.** `strip_inline`'s hero and footer locators use the same pinned
strings, and blind they dropped **L01's held attributes from 39 to 32** — seven attributes
unprotected, the `--include-held` hazard reached by a different road. **Caught by the tool's
own Control H and by no gate.** Nothing was damaged because `--apply` never ran.

**AN AST SCAN THEN ENUMERATED THE REST** instead of waiting for the next failure, and found
**`_LAND` listing `&larr;` and `&#8592;` but not the literal left arrow** — **already blind to
33 of the book's 36 left-arrows BEFORE this session.** Widened; the book is clean behind it.

**GATE 58 NEW**, written in the same pass as the ruling. It asserts the PROPERTY, re-running
the sweep over every page, and **guards its own definition** — adding a fourth character to
`HOLD` fails it. Control-run **seven ways** from a full-tree snapshot with read-back asserts:
four defect shapes each fire gate 58 **ALONE** at 57 of 57 green; a `HOLD` drift fires alone;
an entity injected into a `<script>` body leaves it **correctly silent**; untouched tree at
58 of 58 at BOTH ends with a full-tree diff proving the restore real.

---

# S128 QUEUE

## The glyph and marks arc — the denominator is now trustworthy, so this is genuinely next
DJ queued it at S126 and S127 cleared its blocker. **The census discrepancy is CLOSED.**
- **The population is 3,984 occurrences / 110 distinct**, not 3,273 and not 3,258. Use
  `entity_sweep.census()` or decode before counting — a byte scan is now correct only because
  the sweep ran, and it will stay correct only while gate 58 holds.
- **THE RETIREMENT DENOMINATOR IS SMALLER THAN 3,984 AND THAT IS THE NEXT MEASUREMENT.**
  Roughly a thousand of those are typographic or structural, not decorative glyphs: degree 137,
  multiplication 81, minus 44, plus-minus 32, division 31, almost-equal 18, box-drawing 170,
  **ballot box 364** (almost certainly checklist STRUCTURE, not decoration), up arrow 237 and
  left arrow 36. **Pricing a glyph retirement against 3,984 would repeat the S126 aggregate
  error exactly.** Classifying each character decorative / typographic / structural is a
  RULING, not a measurement.
- **41 marks and not one wired into a lesson.** `build_mark_index.py` emits an index to /tmp.
- An obvious name-match mapping covers **31 distinct / 2,326 occurrences**, about 58 percent;
  79 distinct / 1,658 uncovered. **That mapping is INFERRED from name correspondence only**
  (lightbulb glyph to `lightbulb.svg`), not from role — `build_mark_index`'s FAMILY table maps
  mark to role, and **no glyph-to-mark table exists anywhere in the repo.** Building it is the
  arc's real work.
- **LIVE LEAD, found S127:** `BONUS_MARK` in `book_gates.py` and `MARK` in `gen_bonus_banner.py`
  are defined and **indexed nowhere**, and two stray-checks cannot fire — the bonus banner
  carries no mark at all, having lost it to S108's no-icons ruling. **Proved pre-existing
  against the snapshot: zero marks in any banner before the sweep.** The banner is exactly
  where a mark would go. **DJ ASKED AND IT IS UNRULED: delete the vestigial code, or hold it
  as the arc's entry point?**

## Opened S127 and not ruled
- **The 38 entities inside ATTRIBUTE values are excluded as a SCOPE, not an exception.**
  Sweeping them needs quote-context tracking (`&quot;` inside a double-quoted value is
  mandatory; only 5 of 579 ASCII entities were genuinely constrained). **DJ asked and it is
  unruled: sweep them too, or is "text nodes only" the ruled scope?**
- **`index.html` changed in this push** (23 conversions) and carries **no version home** — it is
  in no roster and `session_versions` does not track it. Same shape as `timer.html` at S123.
  **Is anything ELSE carrying content that nothing versions?** The sweep was never run.

## The colour ledger — unchanged from S127 open
- **16 items; three marked *re-measure before ruling*** — they date from S94, before §27.
- **`#f8f9fa` (641 instances) remains the largest unreported surface**, and 30 of them are the
  only classed `<pre>` left in the book. **Are the light code blocks a deliberate second
  construct or early drift?** They live in L02-L06 ONLY — the same confinement as the wrapper
  divs that turned out to be drift. Unruled.

## Graduation candidates
`code` (S123), the pill (S124), the dark block (S126). Next:
- **Callout families** — but **NOT before the colour ledger**, since their whole point is paint.
  **And `going_deeper.html` defines its own `.callout`** and consumes the semantic layer, so
  check what a graduation does to that page BEFORE shipping it (§27.15c's coupling cost).

## The consistency census — Tier 3 still open
- **Nav pill count ranges 10 to 19** — L09 has 19, nine lessons have 11. §6.5's "12-14" rule is
  obsolete under the six-pill rail; **rewrite the rule before touching a lesson.**
- **Quick-reference anchors exist in five lessons only** (L02-L06); eight carry none.
- **Tier 3 needs reading, not counting:** three lessons have cards with Goal and Logic but fewer
  Templates (L03 short one, L08 short three, L10 short two — may be legitimate, §6.12a allows
  prose); §7 ladder rungs 7A-7E appear in six lessons only (L10-L15) against §15.1's five-rung
  canon; L16's Engineer's Log wrapper does not match the other fifteen; **timers appear in L02,
  L03, L04 only — S69 already burned a session on a false finding here, READ before counting.**
- **Two instrument caveats:** glossary reported absent in all sixteen (the probe only read
  `h2`/`h3` text); callout border-width returned zero shapes (that probe looked for inline
  `border-left`, which §27 deleted — it has to read the stylesheet now).

## Carried, unchanged
- **Should `css/semantic.css` carry a version home?** Carried since S123. It holds THREE ruled
  constructs, has an external consumer that breaks if it changes, and **THREE gates (54, 55, 57)
  depend on its contents.** `session_versions` could register it in a line.
- **L01's BC02 does not carry L01's objectives.** Ruled legacy S119, still the only §25.5 violation.
- **S116's past-tense question: RETIRE IT.** Thirteen sessions now.
- **L10's `What You Built` is the only non-Brain-Check `<h4>` in a converted §10.**
- **L14's score formula is marked up as `<code>` and is not code.**
- **L03's `id="whats-next"` is in all fifteen**; §27.14 still cannot see an unreached id.
- **`sweep_option_c.py` sits in the repo root** — the S92 one-shot, in no instrument list.
- **`index.html` is §27.12's only NAMED exception**, held by name — correct, but must be remembered.

## Rulings outstanding — carried
- Should `build_family_map` parse its total instead of holding a baseline? Baseline unmoved eight
  sessions running.
- Should `build_css` name rules by usage RANK at all? **Fired at S126** — `.p-m-0` became
  `.pre-m-0` and killed 120 elements. Twice now (§27.15b). Strongest case yet.
- **NOTE per-block pass** (133 blocks, four destinations).
- Nav `<details>` carry no `data-reveal` — §25.12 exists because one untyped `<details>` slipped.
- Selftest-coverage gate — offered, not built.
- §25.10l's constant lives ONLY in `book_gates.py` (gate 49), §21.1's shape.
- The seven remaining figure tags — S114's table.
- **Heavy-lesson star list needs a ruling** — L13 as a now-Fall lesson, deliberately unmarked.
- The two pointer CONSTRUCTS above the link — §3.1b rules the section, not the prose pattern.

## Canon debts
§21.1's thresholds live only in `book_gates.py` · §25.6 header example · §25.10e misfiled ·
challenge-card redesign Part B · difficulty-progression audit · Maker batch · L01 VS Code
multi-root · Stage Two two blocks labelled `Learn/Insight` (L03, L09) ·
`ROBOLORE_UPSTREAM_DELTA_S102.md` written and unapplied · robolore.com hosting ·
§6.5's "nav button count is 12-14" is **obsolete** under the six-pill rail — retire, don't argue ·
**26 gradient definitions across 18 SVG files** remain (5 referenced by nothing) ·
**the two `book_gates` versions S115 shipped carry NO changelog line** ·
**four `data-reveal="mechanism"` blocks book-wide** are not on §20.1's strip whitelist.

## Bench (need the robot — parked with photography)
Q017 L09 six numbers · Q044 calibration-spin · Q046 gyro-bias · L02 §5 green-LED ·
Constrain RUN_MS · cm/s at a stated BASE_SPEED · the floor rig for 3.2 / 3.5 / VIDEO 3.1 ·
**a real TRIM run for `IMAGE 3.6`** · **THE SURFACE TEST: run 7E on a lab tile and see whether
the encoder square actually collapses.**

---

# PUSHING — READ THIS

Named-file CLI for adds and modifies; **GitHub Desktop for deletions.** **Never `git add .`**

1. **DELIVER THE FILES.** Every artefact destined for the repo goes through `present_files`;
   instructions and md5s go in the CHAT ONLY. Checksums are not a deliverable.
2. **`(1)` does not mean stale.** Verify by **md5**, never by suffix.
3. **Never present a test file, or a DIAGNOSTIC, in the same list as repo files.**
4. **Never produce PUSH_ME_*.md or MD5_*.txt.**
5. **`lessons/` IS PART OF THE FILENAME. `css/` likewise.**
6. **A push that bumps a version and omits LIVE.md is an INCOMPLETE push (§12.6).**
7. **§27.8b's third step is `strip_inline --apply --include-held`.** Without the flag, held
   strings revert to inline and innocent lessons are rewritten.
8. **After any `css/book.css` regeneration, stage into a copy of the PUSHED CLONE and run
   `book_gates` THERE before presenting md5s. Diff by LINE, not only by expansion.**
9. **Exactly ONE `ZUMO_SNN_HANDOFF.md` in the root (gate 28).** At S128 close, adding
   `ZUMO_S129_HANDOFF.md` means DELETING **this** file — a GitHub Desktop checkbox.
10. **THE NUMBER IN THE FILENAME IS THE SESSION THAT READS IT, NOT THE ONE THAT WROTE IT.**
11. **Never write a real version number as an arrow pair in prose.** `_versions_in()` takes the
    LAST match. Write *"reaches vNEW (from vOLD)"*. Backticks do not shield it.
12. **THE SAME TRAP APPLIES TO SHAs.** One sha per parsed line.
13. **A document cannot name the commit that contains it.** LIVE.md's verification line names
    the commit carrying the PREVIOUS state.
14. **AN EDIT TO A FILE WITH REPEATED LANDMARK LINES TARGETS AN INDEX AND ASSERTS IT** (§6.12c).
    LIVE.md has TWO `**Versions:**` lines and the second must not move.
15. **A VERSION HOME FOUND BY GREPPING FOR A SPELLING IS A HOME YOU HAVE NOT ENUMERATED.**
    `session_versions` holds the regex for every registered artefact — read ARTEFACTS.
16. **WRITE THE GATE IN THE SAME PASS AS THE RULING.** Held at S126 and S127.
17. **A CONTROL HARNESS MUST SNAPSHOT EVERY FILE IT CAN TOUCH — AND `git checkout --` IS NOT A
    RESTORE FOR UNCOMMITTED WORK.** Keep the untouched-tree control at BOTH ends of the run.
    **S127 vindicated it again:** a control batch timed out mid-injection and left a lesson
    dirty; the snapshot restored it byte-identical and nothing was lost.
18. **A GATE THAT PINS A SPELLING CERTIFIES WHATEVER IT WAS GIVEN. PIN THE PROPERTY.** Gate 57
    asserts a contrast RATIO; gate 58 asserts a spelling PROPERTY and derives its own HOLD set.
19. **WHEN A SPELLING IS RULED, SCAN EVERY INSTRUMENT BY AST FOR THE OLD ONE.** S127's four
    loud breakages were found by running the suite; **the silent one — `strip_inline`'s
    locator, 39 held attributes falling to 32 — and `_LAND`'s missing left arrow were found
    ONLY by the AST scan.** Waiting for the next failure finds only the loud ones.
