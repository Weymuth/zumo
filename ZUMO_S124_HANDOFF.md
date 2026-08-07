# ZUMO — S124 HANDOFF (written at S123 close · paste at top of Session 124)

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
   **`title_feed.py --selftest` then `--check`**  ← new S123
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

---

# ⏰ SEPTEMBER 8 IS ABOUT FOUR WEEKS OUT

**14 images outstanding of 141.** Unchanged. Photography still parked.

---

# THE ONE THING TO CARRY OUT OF S123

**THE LEAD NAMES A SYMPTOM. SCOPING THE INSTRUMENT TO THE LEAD'S OWN VOCABULARY GUARANTEES
YOU MEASURE ONLY WHAT YOU WERE ALREADY TOLD.**

The queue said *Consolas*, so the sweep was scoped to Consolas — and it could not see that the
book's dominant code type was `'Courier New', monospace` at **21 rules / 2,825 uses** against
Consolas's 14 / 459. **That error reached DJ as a priced ruling**: the A/B/C specimen was costed
on 459 uses when the population was 3,294, and option A was described as a downgrade when for
86% of the book it was already the status quo. Re-measured, re-priced, re-ruled B-full.

It happened **twice more in the same session, one level up each time**:

- **Gate 53** (one mono stack) was written from that corrected measurement — and immediately
  found what the whole Consolas frame had hidden.
- **Gate 53 then could not see the next layer and said so by PASSING.** 1,199 bare `<code>`
  elements are reached by NO author rule, and a gate that checks declarations cannot see an
  element that has none. §24.8, on a gate four hours old.
- **DJ cut through the third layer in one sentence** — *"I thought since we weren't using canvas
  we didn't need the inline code"* — which was the actual finding, and bigger than the font.

**The question was never *where is Consolas*. It was *how many mono stacks does this book have*,
and then *why can the stylesheet not say what a thing is*.**

---

# STATE

<!-- VERSION BLOCK: emitted by session_versions.py --handoff. Never hand-typed. -->
Fresh-clone verified at **`c4519b6`**. Census **41,128**.
Bible **v8.114** · `BookComponentStandard` **v01.12.1** · Maker **v2.45.3** ·
`marks/` **41** · `icons/` **49** incl. LICENSE.
`ZUMO_Syllabus_WORKING.md` **v1.2**.

Instruments: `book_gates` **v1.49** · `lesson_inventory` **v1.2.0** ·
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

Lessons: L01 v03.21.0 · L02 v03.13.1 · L03 v03.30.1 · L04 v04.21.1 · L05 v04.20.2 · L06 v04.25.1 · L07 v04.24.0 · L08 v04.21.0 · L09 v05.18.0 · L10 v02.19.2 · L11 v02.20.0 · L12 v01.22.0 · L13 v02.20.0 · L14 v02.25.1 · L15 v02.21.0 · L16 v02.13.1.

**54/54 gates.** `--anomalies` silent · family map **1069/1069** · `regex_audit` 0 leads ·
`build_css --check` current at **636 rules** · `color_index --check` clean ·
`image_audit --check` current at 14 outstanding of 141 · both banner generators green ·
`gate_payload_match` PASS on the full glob · `next_pointer --check` clean ·
`title_feed --check` clean · `font_stack_sweep` 0 rewrites across 212 files.

**§27.11's baseline is 636 / 2,332 and is now SCOPED TO THE GENERATED BLOCK.** It moved twice
this session for the font ruling, then held UNCHANGED across the §27.15 layer — which is the
proof that adding the semantic layer moved nothing generated.

---

# S123 WORK — SEE `LIVE_ZUMO_TEXTBOOK.md` FOR THE FULL ACCOUNT

**Three arcs, each one opening the next.**

**1. §3.1b extended — the title is FED, the opener is UNIQUE, the apostrophe is RULED.**
`title_feed.py` v1.0 rewrites the opener title from the §6.5a strip. Gate 52 holds a hole gate 51
cannot see: a section with the correct opener PLUS a stale duplicate satisfies gate 51's count,
and S122 committed exactly that defect to L05. DJ ruled the apostrophe straight (B); **three
owners moved in one commit** because one left behind re-creates the drift.

**2. §6.5a-T extended — one mono stack, DJ ruling B-full.** All 38 mono declarations now carry
`ui-monospace, SFMono-Regular, Menlo, Consolas, 'Liberation Mono', 'Courier New', monospace`.
Gate 53 holds it; the tool pages joined `font_stack_sweep`'s scan; the web-served exemption is
DERIVED per file and the mono target is CONTEXT-dependent (an SVG cannot use `ui-monospace`).

**3. §27.15 NEW — the semantic layer.** `css/semantic.css`, preserved verbatim, hand-edited on
purpose. First graduate: `code, pre`. **Zero lesson edits, all 540 value-named classes still
work, generated block unchanged at 636/2,332.** Gate 54 holds it, and its independence is
measured: add a value-named class and regenerate, and `build_css --check` says *current* while
§27.13 stays green — gate 54 alone names it.

---

# S124 QUEUE

## Unblocked by §27.15 — this is the big one
- **THE COLOUR LEDGER IS NO LONGER BLOCKED.** `ZUMO_COLOR_LEDGER.md`'s first item was never a
  colour — it was *whether `build_css` emits custom properties*. **It now can**, in the semantic
  layer. The 16 items can be reopened, and the blocking fact (155 hexes inside 562 class names,
  so a repaint is a RENAME) is now a fact about the GENERATED block only: a colour that
  graduates into `semantic.css` becomes a custom property that can be changed in one place.
  **Three items are marked *re-measure before ruling* — they date from S94, before §27.**

## The pill — cheap now, and deliberately deferred
- **Inline code has TWO conventions split at the L09/L10 seam** — the same seam S108 found for
  the §6.5 Box. L01–L09 styled pill (2,136 uses), L10–L16 bare (1,199). **L01 is the outlier at
  49% and was ruled LEGACY at S119.** Reading a sample confirmed both do the same job:
  identifiers, function names and filenames in running prose.
  **The typography hole is closed** (both now get the ruled stack), so what remains is purely
  visual and costs ONE LINE in `css/semantic.css`. Options priced at S123: bare→styled (1,199
  elements gain a pill, back half of the book gains a lot of grey), styled→bare (2,136 lose it,
  front half is where they are densest — L02 358, L03 351, L07 324), or rule it in the layer and
  drop the classes as a graduation.
  **DJ has not seen the pill rendered in a real lesson page yet — do that before ruling.**

## Graduation candidates — the §27.15 pattern, one at a time
Each is: write the semantic rule, drop the value-named class, generated block shrinks.
**540 of 636 class names encode a value** (22,816 of 25,752 uses), so there is a lot of runway.
Suggested order — highest use count and clearest meaning first:
- `.code-inline-bg-e8e8e8` (2,097 uses) — becomes the pill rule, if the pill is ruled in.
- `.code-block-333` / `.code-block-bg-1e1e1e` (286 / 255) — §6.11's LOCKED single dark block,
  which is ALSO a Tier-2 census item: **16 distinct `<pre>` opening shapes** against a rule that
  says there is one. Graduating it and closing the census item are the same job.
- Callout families — but **do NOT start these before the colour ledger**, since their whole
  point is paint.

## The consistency census — Tier 1 done, Tier 2 partly measured, Tier 3 open
- **Code block opening tag: RE-MEASURED S123 at 31 shapes total**, which splits into ~16 `<pre>`
  block shapes and ~14 inline `<code>` shapes. The S122 figure of 17 was the block half.
  **Do not inherit either number — re-measure, the rules moved twice this session.**
- **Nav pill count ranges 10 to 19** — L09 has 19, nine lessons have 11. §6.5's "12–14" rule is
  obsolete under the six-pill rail; **rewrite the rule before touching a lesson.**
- **Quick-reference anchors exist in five lessons only** (L02–L06); eight carry none.
- **Tier 3 needs reading, not counting:** three lessons have cards with Goal and Logic but fewer
  Templates (L03 short one, L08 short three, L10 short two — may be legitimate, §6.12a allows
  prose); §7 ladder rungs 7A–7E appear in six lessons only (L10–L15) against §15.1's five-rung
  canon; L16's Engineer's Log wrapper does not match the other fifteen; **timers appear in L02,
  L03, L04 only — S69 already burned a session on a false finding here, READ before counting.**
- **Two instrument caveats, so neither becomes a false finding:** glossary reported absent in all
  sixteen (the probe only read `h2`/`h3` text); callout border-width returned zero shapes (that
  probe looked for inline `border-left`, which §27 deleted — it has to read the stylesheet now).

## The glyph arc — DJ queued it explicitly
*"Leave the glyph and we can deal with them after this update. Then let's do the glyph."*
**2,701 glyphs across 95 distinct characters**, against **41 marks in `images/marks/` and not one
wired into a lesson.**

## Opened at S123, not ruled
- **Should `css/semantic.css` carry a version home?** It is canon and nothing versions it, unlike
  `BookComponentStandard.md`. `session_versions` could register it in one line.
- **`timer.html` was registered NOWHERE until S123** — it carried a version home that only ever
  could have been hand-typed, the §12.6 shape. Now registered. **Worth one sweep: is anything
  ELSE in the repo carrying a version that nothing tracks?**

## Carried, unchanged
- **L01's BC02 does not carry L01's objectives.** Ruled legacy S119, still the only §25.5 violation.
- **S116's past-tense question: RETIRE IT.** Nine sessions now.
- **L10's `What You Built` is the only non-Brain-Check `<h4>` in a converted §10.**
- **The syllabus/TDP consequence of the L13 stop** — a syllabus question, not a book question.
- **L03's `id="whats-next"` is now in all fifteen** rather than removed; §27.14 still cannot see
  an unreached id.

## Rulings outstanding — carried
- Should `build_family_map` parse its total instead of holding a baseline? Baseline unmoved four
  sessions running.
- Should `build_css` name rules by usage RANK at all? **§27.15 makes this less urgent** — a rule
  that graduates stops being rank-named.
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
   **`css/` likewise — `css/book.css` AND `css/semantic.css` are both in `css/`.**
5. **A push that bumps a version and omits LIVE.md is an INCOMPLETE push (§12.6).**
6. **§27.8b's third step is `strip_inline --apply --include-held`.** Without the flag, 624 held
   strings revert to inline and fifteen innocent lessons are rewritten.
7. **After any change that regenerates `css/book.css`, stage into a copy of the PUSHED CLONE
   and run `book_gates` THERE before presenting md5s.**
8. **AFTER ANY `css/book.css` REGENERATION, DIFF THE STAGE AGAINST THE PUSHED CLONE AND PUSH
   EVERY FILE THAT DIFFERS** — and diff by LINE, not only by expansion.
9. **Exactly ONE `ZUMO_SNN_HANDOFF.md` in the root (gate 28).** At S124 close, adding
   `ZUMO_S125_HANDOFF.md` means DELETING **this** file — a GitHub Desktop checkbox.
10. **THE NUMBER IN THE FILENAME IS THE SESSION THAT READS IT, NOT THE ONE THAT WROTE IT.**
11. **Never write a real version number as `vOLD → vNEW` in prose.** `_versions_in()` takes the
    LAST match in the file. Write *"reaches vNEW (from vOLD)"*. Backticks do not shield it.
12. **THE SAME TRAP APPLIES TO SHAs.** One sha per parsed line. Never name a second one in prose.
13. **A document cannot name the commit that contains it.** LIVE.md's verification line names the
    commit carrying the WORK; the follow-up push that fills it is necessarily one commit later.
14. **AN EDIT TO A FILE WITH REPEATED LANDMARK LINES TARGETS AN INDEX AND ASSERTS IT** (§6.12c for
    markdown), never a prefix match. LIVE.md has TWO `**Versions:**` lines and the second is a
    historical per-session snapshot whose contents must not move.
15. **`css/semantic.css` IS A NEW FILE — it has never been pushed.** A push that ships the
    regenerated `css/book.css` without it leaves the site serving a stylesheet whose source is
    absent, and gate 54 fails in the pushed clone.
