# ZUMO — S125 HANDOFF (written at S124 close · paste at top of Session 125)

## Session open ritual (do this without being asked)
1. **`git ls-remote https://github.com/Weymuth/zumo.git HEAD` FIRST.** If the clone's
   `git log -1` does not match, fetch the sha by name (§12.4, *caches lie*).
2. Read `LIVE_ZUMO_TEXTBOOK.md` — verify date / status / versions.
3. **Do NOT grep the Bible version.** `session_versions.bible_consistency()` parses it; the
   Bible has THREE homes — header line 17, the `Current:` clause, and the newest CHANGELOG
   entry — and Control F fails if any two disagree.
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
   **`title_feed.build(root)`**.
11. **A CLONE IS NOT THE SITE.** Run `site_parity.py` after any push. It can FAIL on the first
   run in the minute after a push and pass on retry — Pages lag, not a defect (S112).
12. **VERIFY THE PUSH BY FRESH CLONE AND MD5 — AND DIFF THE STAGE AGAINST THE CLONE.**
13. **The lesson files are `Lesson_NN.html`, no topic suffix, and they live in `lessons/`.**
14. **`css/semantic.css` IS HAND-EDITED ON PURPOSE (§27.15).** It is the ONLY stylesheet file
   that is. `css/book.css` is still DO-NOT-HAND-EDIT — edit the source and regenerate.

14. **`css/semantic.css` IS HAND-EDITED ON PURPOSE (§27.15).** It is the ONLY stylesheet file
   that is. `css/book.css` is still DO-NOT-HAND-EDIT — edit the source and regenerate.
15. **NEW S124 — `regex_audit.py` after any gate you write.** Gate 55 shipped a match-and-discard
   alternation and the audit caught it on the first run.

---

# ⏰ SEPTEMBER 8 IS ABOUT FOUR WEEKS OUT

**14 images outstanding of 141.** Unchanged. Photography still parked.

---

# THE ONE THING TO CARRY OUT OF S124

**AN ELEMENT RULE REACHES ELEMENTS NO AUTHOR EVER LISTED. THE POPULATION YOU CAN ENUMERATE IS NOT
THE POPULATION THE RULE REACHES.**

The pill was ruled in and the dark-context audit enumerated the `<code>` elements that still carried
a CLASS. It found two, and reported two. **Seven more sit inside dark table headers carrying no
class at all** — invisible to an instrument that was looking at classes while the rule under test
was an element selector. Every one of those containers declares `color: white`, so an opaque pill
would have made all eight unreadable, silently, in shipped lessons.

**DJ found it with one question** — *"why would I want to change from code to span?"* — aimed at a
proposal to retag L14's element. That proposal was only defensible on a sample of one. With eight
cases the markup was obviously innocent and the RULE was obviously unscoped.

**And the options were mispriced to him twice, both times away from the option he preferred.** The
wash was called the conservative choice when it repaints 3,336 elements against 1,233, then called
more work when it is a one-line value change. **A count of what CHANGES is not a count of what it
COSTS. State the two numbers separately.**

---

# STATE

<!-- VERSION BLOCK: emitted by session_versions.py --handoff. Never hand-typed. -->
Fresh-clone verified at **`695ec87`**. Census **41,128**.
Bible **v8.115** · `BookComponentStandard` **v01.12.1** · Maker **v2.45.3** ·
`marks/` **41** · `icons/` **49** incl. LICENSE.
`ZUMO_Syllabus_WORKING.md` **v1.2**.

Instruments: `book_gates` **v1.50** · `lesson_inventory` **v1.2.0** ·
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
`going_deeper` **v01.4.2**.

Lessons: L01 v03.22.0 · L02 v03.14.0 · L03 v03.31.0 · L04 v04.22.0 · L05 v04.21.0 · L06 v04.26.0 · L07 v04.25.0 · L08 v04.22.0 · L09 v05.19.0 · L10 v02.20.0 · L11 v02.21.0 · L12 v01.23.0 · L13 v02.21.0 · L14 v02.26.0 · L15 v02.22.0 · L16 v02.14.0.

**55/55 gates.** `--anomalies` silent · family map **1069/1069** · `regex_audit` 0 leads ·
`build_css --check` current at **627 rules** · `color_index --check` clean ·
`image_audit --check` current at 14 outstanding of 141 · both banner generators green ·
`gate_payload_match` PASS on the full glob · `next_pointer --check` and `title_feed --check` clean ·
`font_stack_sweep` 0 rewrites · `strip_inline --verify` 0 dead class names.

**§27.11 is 627 / 2,297, digest `3f4c39d35c2d6b64`**, scoped to the generated block.

---

# S124 WORK — SEE `LIVE_ZUMO_TEXTBOOK.md` FOR THE FULL ACCOUNT

The pill graduated by DELETION: 2,132 class attributes stripped, ten rules dead, one born, net −9.
Ground ruled **B**, `rgba(0, 0, 0, 0.08)`. §27.15a, §27.15b and gate 55 are new.

**THE BUILD WAS RE-DERIVED FROM A CLEAN CLONE AND THAT IS WORTH KNOWING.** A first attempt sat in the
working tree whose authorship could not be accounted for. Nothing was pushed; everything was rebuilt
from `695ec87` with every edit scripted and asserted. **All sixteen lesson files and the entire
76,473-byte generated block came back byte-identical.** Two independent runs agreeing beats one run
verifying itself — and the rebuild also dropped a spliced comment block the first attempt carried
into the preserved layer, which gate 54 would have copied verbatim into `css/book.css`.

---

# S125 QUEUE

## The obvious next one
- **`going_deeper.html` CARRIES A THIRD INLINE-CODE TREATMENT AND IT IS NOT RULED.** A DARK pill —
  `#1e1e1e` ground, `#9cdcfe` text, a border, `.88em` — across **71 inline uses**. It does not link
  `css/book.css`; it carries its own `<style>`, and it reached the `pre code` reset independently.
  Whether it converts to the lesson pill, or is ruled a deliberately different context, is open.
  **Do not assume convert. Measure what those 71 elements ARE first** — the L02/L03 operator lesson.

## The colour ledger — still the big one, now with a second graduate behind it
- **`ZUMO_COLOR_LEDGER.md`'s 16 items can be reopened.** The blocking fact (155 hexes inside 562 class
  names, so a repaint is a RENAME) is a fact about the GENERATED block only. **Three items are marked
  *re-measure before ruling* — they date from S94, before §27.**
- **The wash is a precedent worth noticing here:** a value that inherits its context can retire a
  whole class of scope exceptions. Some ledger items may have the same shape.

## Graduation candidates — one at a time
**540 of 636 class names encoded a value at S123; the pill took nine of them out.** Suggested next:
- `.code-block-333` / `.code-block-bg-1e1e1e` — §6.11's LOCKED single dark block, which is ALSO a
  Tier-2 census item: **16 distinct `<pre>` opening shapes** against a rule saying there is one.
  Graduating it and closing the census item are the same job. **Re-measure — S123 put the total at 31
  shapes splitting ~16 block / ~14 inline, and the inline half just moved under this session's strip.**
- Callout families — but **NOT before the colour ledger**, since their whole point is paint.

## The consistency census — Tier 2 partly measured, Tier 3 open
- **Nav pill count ranges 10 to 19** — L09 has 19, nine lessons have 11. §6.5's "12–14" rule is
  obsolete under the six-pill rail; **rewrite the rule before touching a lesson.**
- **Quick-reference anchors exist in five lessons only** (L02–L06); eight carry none.
- **Tier 3 needs reading, not counting:** three lessons have cards with Goal and Logic but fewer
  Templates (L03 short one, L08 short three, L10 short two — may be legitimate, §6.12a allows prose);
  §7 ladder rungs 7A–7E appear in six lessons only (L10–L15) against §15.1's five-rung canon; L16's
  Engineer's Log wrapper does not match the other fifteen; **timers appear in L02, L03, L04 only —
  S69 already burned a session on a false finding here, READ before counting.**
- **Two instrument caveats:** glossary reported absent in all sixteen (the probe only read `h2`/`h3`
  text); callout border-width returned zero shapes (that probe looked for inline `border-left`, which
  §27 deleted — it has to read the stylesheet now).

## The glyph arc — DJ queued it explicitly
*"Leave the glyph and we can deal with them after this update. Then let's do the glyph."*
**2,701 glyphs across 95 distinct characters**, against **41 marks in `images/marks/` and not one
wired into a lesson.**

## Opened and not ruled
- **Should `css/semantic.css` carry a version home?** Carried from S123, and it now holds TWO ruled
  constructs rather than one, so the case is stronger. `session_versions` could register it in a line.
- **Is anything ELSE in the repo carrying a version that nothing tracks?** `timer.html` was the S123
  case; the sweep was never run.
- **L14's score formula is marked up as `<code>` and is not code.** Left alone this session because
  retagging it was the wrong answer to the dark-ground problem, but the markup question is real and
  separate: `FIELD SCORE = ( LINE TRACING SCORE + EXIT BONUS ) × EVACUATION ZONE MULTIPLIER`.
- **The two pink pills in L03 are spelled `#f5c6cb` and `#f5c6c0`** — one digit apart, both pink, on
  the same construct. That is a typo, not two colours. **A colour-ledger item, not a pill item.**

## Carried, unchanged
- **L01's BC02 does not carry L01's objectives.** Ruled legacy S119, still the only §25.5 violation.
- **S116's past-tense question: RETIRE IT.** Ten sessions now.
- **L10's `What You Built` is the only non-Brain-Check `<h4>` in a converted §10.**
- **The syllabus/TDP consequence of the L13 stop** — a syllabus question, not a book question.
- **L03's `id="whats-next"` is in all fifteen**; §27.14 still cannot see an unreached id.

## Rulings outstanding — carried
- Should `build_family_map` parse its total instead of holding a baseline? Baseline unmoved five
  sessions running.
- Should `build_css` name rules by usage RANK at all? **S124 sharpened this** — rank-naming is what
  renamed `.code-ff-uimonosp-2` out from under three surviving elements (§27.15b).
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

1. **`(1)` does not mean stale.** Verify by **md5**, never by suffix.
2. **Never present a test file, or a DIAGNOSTIC, in the same list as repo files.**
3. **Never produce PUSH_ME_*.md or MD5_*.txt.** Checksums and instructions go in the CHAT ONLY.
4. **`lessons/` IS PART OF THE FILENAME.** Check the destination path of every file.
   **`css/` likewise — `css/book.css` AND `css/semantic.css` are both in `css/`.** S124 proved the
   gates catch this: `semantic.css` pushed to the ROOT failed §27.15 and §27.13 in the clone.
5. **A push that bumps a version and omits LIVE.md is an INCOMPLETE push (§12.6).**
6. **§27.8b's third step is `strip_inline --apply --include-held`.** Without the flag, 624 held
   strings revert to inline and fifteen innocent lessons are rewritten.
7. **After any change that regenerates `css/book.css`, stage into a copy of the PUSHED CLONE
   and run `book_gates` THERE before presenting md5s.**
8. **AFTER ANY `css/book.css` REGENERATION, DIFF THE STAGE AGAINST THE PUSHED CLONE AND PUSH
   EVERY FILE THAT DIFFERS** — and diff by LINE, not only by expansion.
9. **Exactly ONE `ZUMO_SNN_HANDOFF.md` in the root (gate 28).** At S125 close, adding
   `ZUMO_S126_HANDOFF.md` means DELETING **this** file — a GitHub Desktop checkbox.
10. **THE NUMBER IN THE FILENAME IS THE SESSION THAT READS IT, NOT THE ONE THAT WROTE IT.**
11. **Never write a real version number as `vOLD → vNEW` in prose.** `_versions_in()` takes the
    LAST match in the file. Write *"reaches vNEW (from vOLD)"*. Backticks do not shield it.
12. **THE SAME TRAP APPLIES TO SHAs.** One sha per parsed line. Never name a second one in prose.
13. **A document cannot name the commit that contains it.** LIVE.md's verification line names the
    commit carrying the WORK; the follow-up push that fills it is necessarily one commit later.
    **S124 found this unpaid:** LIVE.md and the S124 handoff both named `c4519b6`, a commit that
    contains none of S123's work — the work shipped in `753c8cc` and was fixed in `695ec87`.
14. **AN EDIT TO A FILE WITH REPEATED LANDMARK LINES TARGETS AN INDEX AND ASSERTS IT** (§6.12c for
    markdown), never a prefix match. LIVE.md has TWO `**Versions:**` lines and the second is a
    historical per-session snapshot whose contents must not move.
