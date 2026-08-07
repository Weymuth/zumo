# ZUMO — S127 HANDOFF (written at S126 close · paste at top of Session 127)

## Session open ritual (do this without being asked)
1. **`git ls-remote https://github.com/Weymuth/zumo.git HEAD` FIRST.** If the clone's
   `git log -1` does not match, fetch the sha by name (§12.4, *caches lie*).
   **S126: a push was reported and `ls-remote` still showed the OLD sha. It was reported
   correctly and I checked too early. CHECK AGAIN BEFORE CONCLUDING A PUSH FAILED** —
   `ls-remote` reads the repo directly, so a stale answer is timing, not caching, and one
   retry a minute later settles it. Saying "the push didn't land" is a wrong answer, and a
   wrong answer costs 3× a blank one.
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
   `title_feed.build(root)`.
11. **A CLONE IS NOT THE SITE.** Run `site_parity.py` after any push. It can FAIL on the first
   run in the minute after a push and pass on retry — Pages lag, not a defect (S112).
12. **VERIFY THE PUSH BY FRESH CLONE AND MD5 — AND DIFF THE STAGE AGAINST THE CLONE.**
13. **The lesson files are `Lesson_NN.html`, no topic suffix, and they live in `lessons/`.**
14. **`css/semantic.css` IS HAND-EDITED ON PURPOSE (§27.15).** It is the ONLY stylesheet file
   that is. `css/book.css` is still DO-NOT-HAND-EDIT — edit the source and regenerate.
15. **`regex_audit.py` after any gate you write.**
16. **`session_versions --check` will report ~21 disagreements at session open and they are
   EXPECTED** — every one names `ZUMO_S127_HANDOFF.md`, the INCOMING document, which
   describes the state at open and is stale by definition once work starts. Read WHICH
   artefact each line names before treating any of it as drift. If a line names LIVE.md or
   the Bible, that IS drift.

---

# ⏰ SEPTEMBER 8 IS ABOUT FOUR WEEKS OUT

**14 images outstanding of 141.** Unchanged. Photography still parked.

---

# THE ONE THING TO CARRY OUT OF S126

**AN AGGREGATE CAN BE A TRUE NUMBER TELLING THE WRONG STORY — AND DJ'S EYE WAS THE INSTRUMENT
THAT CAUGHT IT.**

The dark code block's border was reported to DJ as a **57/42 split**: 398 blocks with
`1px solid #333`, 289 without. That number is correct and it framed the question as a
preference to be ruled. It is not one. Broken down per lesson it is **the L09/L10 SEAM** —
L02–L09 bordered 365 of 372, L10–L16 bordered 29 of 281 — the same seam S108 found for the
§6.5 Box and S123 for the mono stack, now three constructs deep. **There was never a majority
to defer to; there were two conventions.** DJ asked *"is this for the entire book, or just a
small section?"* and that question is what produced the breakdown.

**AND THE SPECIMENS WERE THE OTHER HALF.** Shown four rendered variants, DJ said *"they all
look the same to me."* He was right by measurement: `#333` on `#1e1e1e` is **1.32:1**, against
a 3:1 WCAG minimum for a non-text boundary. **398 blocks had been carrying a line nobody could
see.** A table would never have surfaced that. **Show the thing.**

**THE SAME ERROR CLASS THEN CAUGHT ME TWICE MORE, AND BOTH WERE CAUGHT BY MEASUREMENT RATHER
THAN MEMORY:**
- **`#686868` was hand-computed as "3:1" and is 2.992:1.** Gate 57 asserts the **RATIO**, not
  the spelling, so it failed before the push. **A gate checking for the literal hex would have
  certified an invisible border as the ruled one.** `#696969` is the lowest grey that clears.
- **A population was sampled at ONE and reported as two wrapper spellings. It was eight.**
  §24.8, again: the population you can enumerate is not the population an element rule reaches.

---

# STATE

<!-- VERSION BLOCK: emitted by session_versions.py --handoff. Never hand-typed. -->
Fresh-clone verified at **`4604ec7`**. Census **40,700**.
Bible **v8.118** · `BookComponentStandard` **v01.12.1** · Maker **v2.45.3** ·
`marks/` **41** · `icons/` **49** incl. LICENSE.
`ZUMO_Syllabus_WORKING.md` **v1.2**.

Instruments: `book_gates` **v1.53** · `lesson_inventory` **v1.3.0** ·
`gen_component` **v1.6.1** · `pill_sweep` **v1.1** · `gate_payload_match` **v1.7** ·
`build_family_map` **v1.3.7** · `build_mark_index` **v1.0.2** · `gen_bonus_banner` **v1.4.1** ·
`gen_part_banners` **v1.2** · `session_versions` **v1.19.0** · `fit_raster_svg` **v1.2** ·
`flatten_alpha` **v1.2** · `svg_layout_audit` **v1.20** · `site_parity` **v1.1** ·
`build_css` **v1.3.0** ·
`image_audit` **v1.1** ·
`strip_inline` **v1.1** ·
`build_worklist` **v1.1** ·
`regex_audit` **v1.0** ·
`build_palette` **v1.1** ·
`class_sweep` **v1.0** ·
`color_index` **v1.0** ·
`font_stack_sweep` **v1.3.0** ·
`next_pointer` **v1.1** ·
`title_feed` **v1.0** ·
`timer.html` **v1.3.1** ·
`going_deeper` **v01.6.0**.

Lessons: L01 v03.23.0 · L02 v03.15.0 · L03 v03.33.0 · L04 v04.23.0 · L05 v04.22.0 · L06 v04.27.0 · L07 v04.26.0 · L08 v04.23.0 · L09 v05.20.0 · L10 v02.21.0 · L11 v02.22.0 · L12 v01.24.0 · L13 v02.22.0 · L14 v02.27.0 · L15 v02.23.0 · L16 v02.15.0.

**57/57 gates.** `--anomalies` silent · family map **1069/1069** · `regex_audit` 0 leads ·
`build_css --check` current at **604 rules** · `strip_inline --verify` 0 dead class names ·
`color_index --check` clean · `image_audit --check` current at 14 outstanding of 141 ·
`gate_payload_match` PASS on the full glob · `next_pointer --check` and `title_feed --check` clean ·
`site_parity` PARITY at **140** referenced assets.

**§27.11 is 604 / 2,141, digest `5c22a884d4031cd2`**, scoped to the generated block.

---

# S126 WORK — SEE `LIVE_ZUMO_TEXTBOOK.md` FOR THE FULL ACCOUNT

**Two pushes, one Bible entry each; the second reaches the version named in STATE above.**

**PUSH 1 — §27.12 EXTENDED + §27.15d NEW.** DJ: *"Fix the typo, all should be consistent in the
entire book."* The two pinks one digit apart were the last two of **FIVE** classed inline
`<code>` in the book, all in L03 — invisible to S124's strip because it enumerated the class
names it knew. §27.15a says no exception list, so all five went. **§27.15d: `expand_classes`
knew exactly ONE stylesheet**, so a page styling itself from its own `<style>` block was opaque
to every gate reading through it — which is why **`going_deeper.html`'s hero satisfied §25.6
ONLY BECAUSE IT WAS INLINE.** The seven attributes S125 filed as a scope question were not
leftovers; six were load-bearing for a gate. going_deeper converted and on **Inter**;
`index.html`'s one inline style out and the page **held by NAME** in §27.12 (§25.2a).
**THREE SCOPE DEFECTS, EACH FOUND BY THE NEXT:** a COMMENT mentioning `css/book.css` pulled
going_deeper into §27's scope (bare substring test); the specific predicate that replaced it
demanded `href="css/book.css"` and matched **ZERO lessons**, which link `../css/book.css`
(§27.10); and **that was caught ONLY because gate 44 had a coverage arm and §27 did not.**

**PUSH 2 — §27.15e NEW, the dark code block.** 802 `<pre>`, fourteen class names, one rule,
**no opt-out and no exception list.** Border `1px solid #696969` (3.037:1), radius 6px. The 30
light `#f8f9fa` blocks need no help — their class beats the element rule on every property it
sets. **The 109 blocks inside a dark wrapper `<div>` in L02/L03 were UNWRAPPED rather than
excepted**, all verified single-child across all eight spellings. **§27.15b FIRED FOR REAL:**
176 `<pre>` joined `.p-m-0`'s 120 users, `<pre>` became dominant, the rule renamed to
`.pre-m-0`, and **119 `<p>` plus one `<ul>` went dead** — caught by `strip_inline --verify`,
invisible to every gate. Tree **REVERTED and re-derived**, not patched forward.

---

# S127 QUEUE

## The glyph and marks arc — DJ queued it explicitly and it is next
*"Leave the glyph and we can deal with them after this update. Then let's do the glyph."*
DJ, S126: *"before we get rid of glyphs the 41 marks are most important — am I right?"*
**He is right, with one correction: they are ONE arc, not two.** The 41 SVGs in `images/marks/`
are the replacement inventory FOR the glyphs — `lightbulb.svg` for 💡 (114 uses), `key.svg` for
🔑 (158), `unlock.svg` for 🔓 (163), `bullseye.svg` for 🎯 (113), `exclamation-triangle.svg` for
⚠ (93). You cannot retire a glyph with nothing to put in its place. Order: **census → map glyph
to mark → find the gaps → wire.**
- **RESOLVE THE CENSUS DISCREPANCY FIRST.** Re-derived at S126: **95 distinct characters** (the
  handoff's figure exactly) but **3,258 occurrences, not 2,701**. Same distinct count, 557 more
  hits. That is a SCOPE difference in what each count included, not necessarily an error in
  either — settle it before pricing anything off the denominator.
- **41 marks and not one wired into a lesson.** `build_mark_index.py` emits an index to /tmp.

## The colour ledger — now more tractable than it was
- **16 items; three marked *re-measure before ruling*** — they date from S94, before §27.
- **THE PINK TYPO IS CLOSED** (S126) and so is the dark-block normalisation. **Three colour
  rulings landed from MEASUREMENT rather than taste**, including one derived purely by contrast
  arithmetic — that is the precedent the ledger was waiting for.
- **`#f8f9fa` (641 instances) remains the largest unreported surface**, and 30 of them are now
  the only classed `<pre>` left in the book. **Are the light code blocks a deliberate second
  construct or early drift?** They live in L02–L06 ONLY, none after — the same confinement as
  the wrapper divs that turned out to be drift. Unruled.
- The wash remains the precedent: a value that inherits its context retires a class of scope
  exceptions.

## Graduation candidates — two now shipped, and the pattern is established
`code` (S123), the pill (S124), the dark block (S126). Next:
- **Callout families** — but **NOT before the colour ledger**, since their whole point is paint.
  **And `going_deeper.html` defines its own `.callout`** and now consumes the semantic layer, so
  check what a graduation does to that page BEFORE shipping it (§27.15c's coupling cost, and it
  is real — S126 already had to check it twice).

## The consistency census — Tier 2 partly measured, Tier 3 open
- **§6.11's "16 distinct `<pre>` shapes against a rule saying one" IS NOW CLOSED** by §27.15e.
- **Nav pill count ranges 10 to 19** — L09 has 19, nine lessons have 11. §6.5's "12–14" rule is
  obsolete under the six-pill rail; **rewrite the rule before touching a lesson.**
- **Quick-reference anchors exist in five lessons only** (L02–L06); eight carry none.
- **Tier 3 needs reading, not counting:** three lessons have cards with Goal and Logic but fewer
  Templates (L03 short one, L08 short three, L10 short two — may be legitimate, §6.12a allows
  prose); §7 ladder rungs 7A–7E appear in six lessons only (L10–L15) against §15.1's five-rung
  canon; L16's Engineer's Log wrapper does not match the other fifteen; **timers appear in L02,
  L03, L04 only — S69 already burned a session on a false finding here, READ before counting.**
- **Two instrument caveats:** glossary reported absent in all sixteen (the probe only read
  `h2`/`h3` text); callout border-width returned zero shapes (that probe looked for inline
  `border-left`, which §27 deleted — it has to read the stylesheet now).

## Opened and not ruled
- **Should `css/semantic.css` carry a version home?** Carried since S123 and **the case is
  stronger again**: it now holds THREE ruled constructs, has an external consumer that breaks if
  it changes, and **THREE gates (54, 55, 57) depend on its contents**. It changed twice this
  session and nothing tracked it. `session_versions` could register it in a line.
- **Is anything ELSE carrying a version that nothing tracks?** `timer.html` was the S123 case;
  the sweep was never run.
- **`index.html` is §27.12's only NAMED exception.** It links no stylesheet and is held by name
  — correct today, but it is the one entry in that gate that has to be remembered.
- **L14's score formula is marked up as `<code>` and is not code:**
  `FIELD SCORE = ( LINE TRACING SCORE + EXIT BONUS ) × EVACUATION ZONE MULTIPLIER`.
- **`sweep_option_c.py` sits in the repo root** — the S92 one-shot. Referenced by
  `session_versions.py` so not orphaned, but in no instrument list. Housekeeping.

## Carried, unchanged
- **L01's BC02 does not carry L01's objectives.** Ruled legacy S119, still the only §25.5 violation.
- **S116's past-tense question: RETIRE IT.** Twelve sessions now.
- **L10's `What You Built` is the only non-Brain-Check `<h4>` in a converted §10.**
- **The syllabus/TDP consequence of the L13 stop** — a syllabus question, not a book question.
- **L03's `id="whats-next"` is in all fifteen**; §27.14 still cannot see an unreached id.

## Rulings outstanding — carried
- Should `build_family_map` parse its total instead of holding a baseline? Baseline unmoved seven
  sessions running.
- Should `build_css` name rules by usage RANK at all? **Rank-naming fired AGAIN at S126** —
  `.p-m-0` → `.pre-m-0` killed 120 elements. Twice now (§27.15b). This is the strongest case yet.
- **NOTE per-block pass** (133 blocks, four destinations).
- Nav `<details>` carry no `data-reveal` — §25.12 exists because one untyped `<details>` slipped.
- Selftest-coverage gate — offered, not built.
- §25.10l's constant lives ONLY in `book_gates.py` (gate 49), §21.1's shape.
- The seven remaining figure tags — S114's table.
- **⭐ heavy-lesson list needs a ruling** — L13 as a now-Fall lesson, deliberately unmarked.
- The two pointer CONSTRUCTS above the link — §3.1b rules the section, not the prose pattern.

## Canon debts
§21.1's thresholds live only in `book_gates.py` · §25.6 header example · §25.10e misfiled ·
challenge-card redesign Part B · difficulty-progression audit · Maker batch · L01 VS Code
multi-root · Stage Two two blocks labelled `Learn/Insight` (L03, L09) ·
`ROBOLORE_UPSTREAM_DELTA_S102.md` written and unapplied · robolore.com hosting ·
§6.5's "nav button count is 12–14" is **obsolete** under the six-pill rail — retire, don't argue ·
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

1. **DELIVER THE FILES.** S126 gave checksums and a `git add` line and **presented no files at
   all** until DJ said *"You haven't given me any files to push this session."* Checksums are
   not a deliverable. **Every artefact destined for the repo goes through `present_files`,**
   and instructions and md5s go in the CHAT ONLY.
2. **`(1)` does not mean stale.** Verify by **md5**, never by suffix.
3. **Never present a test file, or a DIAGNOSTIC, in the same list as repo files.**
4. **Never produce PUSH_ME_*.md or MD5_*.txt.**
5. **`lessons/` IS PART OF THE FILENAME. `css/` likewise** — `css/book.css` AND
   `css/semantic.css` are both in `css/`.
6. **A push that bumps a version and omits LIVE.md is an INCOMPLETE push (§12.6).**
7. **§27.8b's third step is `strip_inline --apply --include-held`.** Without the flag, held
   strings revert to inline and innocent lessons are rewritten.
8. **After any `css/book.css` regeneration, stage into a copy of the PUSHED CLONE and run
   `book_gates` THERE before presenting md5s. Diff by LINE, not only by expansion.**
9. **Exactly ONE `ZUMO_SNN_HANDOFF.md` in the root (gate 28).** At S127 close, adding
   `ZUMO_S128_HANDOFF.md` means DELETING **this** file — a GitHub Desktop checkbox.
10. **THE NUMBER IN THE FILENAME IS THE SESSION THAT READS IT, NOT THE ONE THAT WROTE IT.**
11. **Never write a real version number as `vOLD → vNEW` in prose.** `_versions_in()` takes the
    LAST match. Write *"reaches vNEW (from vOLD)"*. Backticks do not shield it.
12. **THE SAME TRAP APPLIES TO SHAs.** One sha per parsed line.
13. **A document cannot name the commit that contains it.** LIVE.md's verification line names
    the commit carrying the PREVIOUS state.
14. **AN EDIT TO A FILE WITH REPEATED LANDMARK LINES TARGETS AN INDEX AND ASSERTS IT** (§6.12c).
    LIVE.md has TWO `**Versions:**` lines and the second must not move.
15. **A VERSION HOME FOUND BY GREPPING FOR A SPELLING IS A HOME YOU HAVE NOT ENUMERATED.**
    `session_versions` holds the regex for every registered artefact — read ARTEFACTS.
16. **WRITE THE GATE IN THE SAME PASS AS THE RULING.** Held at S126: gates 44-extended, 56 and
    57 all shipped with their rulings.
17. **A CONTROL HARNESS MUST SNAPSHOT EVERY FILE IT CAN TOUCH — AND `git checkout --` IS NOT A
    RESTORE FOR UNCOMMITTED WORK.** S126 snapshotted the stylesheets, injected a defect into
    `Lesson_05.html`, then ran `git checkout --` on it — which reverts to **HEAD** and silently
    destroyed that lesson's share of the build. **S121's exact error in a new place.** The
    untouched-tree control is what exposed it, by failing. Keep that control, always, at BOTH
    ends of the run.
18. **A GATE THAT PINS A SPELLING CERTIFIES WHATEVER IT WAS GIVEN. PIN THE PROPERTY.** Gate 57
    asserts the border's CONTRAST RATIO against its ground, and caught a ruled value that was
    hand-computed wrong. A gate asserting `#686868` would have blessed an invisible border.
