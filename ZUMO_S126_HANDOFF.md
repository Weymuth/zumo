# ZUMO — S126 HANDOFF (written at S125 close · paste at top of Session 126)

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
   `title_feed.build(root)`.
11. **A CLONE IS NOT THE SITE.** Run `site_parity.py` after any push. It can FAIL on the first
   run in the minute after a push and pass on retry — Pages lag, not a defect (S112).
12. **VERIFY THE PUSH BY FRESH CLONE AND MD5 — AND DIFF THE STAGE AGAINST THE CLONE.**
13. **The lesson files are `Lesson_NN.html`, no topic suffix, and they live in `lessons/`.**
14. **`css/semantic.css` IS HAND-EDITED ON PURPOSE (§27.15).** It is the ONLY stylesheet file
   that is. `css/book.css` is still DO-NOT-HAND-EDIT — edit the source and regenerate.
15. **`regex_audit.py` after any gate you write.** Gate 55 shipped a match-and-discard
   alternation and the audit caught it on the first run.
16. **NEW S125 — `css/semantic.css` NOW HAS A DIRECT CONSUMER.** `going_deeper.html` links it
   (§27.15c). **Anything added to the semantic layer from now on lands on that page too**, and
   it defines its own `.callout`, `.body`, `pre` and `table`. Before graduating a construct,
   check what it does to going_deeper. Its `<style>` block sits BELOW the link, so the page wins
   any collision on a declaration it sets — and only on those.

---

# ⏰ SEPTEMBER 8 IS ABOUT FOUR WEEKS OUT

**14 images outstanding of 141.** Unchanged. Photography still parked.

---

# THE ONE THING TO CARRY OUT OF S125

**A MECHANISM INHERITED FROM A CHANGELOG IS A LEAD, NOT A FINDING — AND THE OPTIONS WERE PRESENTED
WITH THAT LEAD BAKED IN.**

Asked *"didn't we go with the pill by linking?"*, the honest answer required reading the tree, and the
tree says **nothing in the repo links `css/semantic.css` at all**. The lessons link `css/book.css`,
which carries the layer preserved verbatim at byte offset 973. S124 shipped the pill through a pipe
that already existed; *linking* was never the mechanism.

**That error had already reached the ruling.** Option C was written as *link `css/semantic.css`* and
described as though it followed S124's precedent. It does not — it CREATES the first direct link in
the repo. DJ's question is what surfaced it, one turn before the edit.

**The second half is the ruling principle, and it is worth keeping:** when two options both work, rule
on **which failure each leaves behind**. A second spelling of a ruled construct inside a page's own
`<style>` block is drift that gate 54 is structurally blind to — silent and unwatched. Inheriting a
future graduate uninvited is visible at the moment of the next graduation. **Silent-and-unwatched loses
to visible-and-scheduled**, and that is why the more-coupled option was the right one.

**AND THEN THE RULING SHIPPED UNGATED, WHICH IS THE SAME MISTAKE ONE LEVEL UP.** §27.15c created a
delivery path nothing held. The coupling cost was written into THIS handoff as a known risk and no gate
was written for it in the same pass. Measured afterwards: deleting the `<link>`, restating the dark rule
in the page's own `<style>`, breaking the `href`, or seating the link below the `<style>` block each left
**all 55 preceding gates green and exit 0** — and `site_parity` and `font_stack_sweep`, the two
instruments that look like they should have covered it, are both structurally blind (§24.8 twice).
**Gate 56 closes it.** The rule: **a ruling that creates a new delivery path creates a new unguarded
path, and the session that rules it owes the gate — in the same pass, not in the handoff.**

---

# STATE

<!-- VERSION BLOCK: emitted by session_versions.py --handoff. Never hand-typed. -->
Fresh-clone verified at **`907b26e`**. Census **41,128**.
Bible **v8.116.1** · `BookComponentStandard` **v01.12.1** · Maker **v2.45.3** ·
`marks/` **41** · `icons/` **49** incl. LICENSE.
`ZUMO_Syllabus_WORKING.md` **v1.2**.

Instruments: `book_gates` **v1.51** · `lesson_inventory` **v1.2.0** ·
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
`going_deeper` **v01.5.0**.

Lessons: L01 v03.22.0 · L02 v03.14.0 · L03 v03.31.0 · L04 v04.22.0 · L05 v04.21.0 · L06 v04.26.0 · L07 v04.25.0 · L08 v04.22.0 · L09 v05.19.0 · L10 v02.20.0 · L11 v02.21.0 · L12 v01.23.0 · L13 v02.21.0 · L14 v02.26.0 · L15 v02.22.0 · L16 v02.14.0.

**56/56 gates.** `--anomalies` silent · family map **1069/1069** · `regex_audit` 0 leads ·
`build_css --check` current at **627 rules** · `color_index --check` clean ·
`image_audit --check` current at 14 outstanding of 141 · both banner generators green ·
`gate_payload_match` PASS on the full glob · `next_pointer --check` and `title_feed --check` clean ·
`font_stack_sweep` 0 rewrites (and BLIND to gate 56's population — an absent stack is not non-compliant) · `strip_inline --verify` 0 dead class names ·
`site_parity` PARITY at **140** referenced assets (was 139 — the new `css/semantic.css` reference).

**§27.11 is 627 / 2,297, digest `3f4c39d35c2d6b64`**, scoped to the generated block. Unmoved by S125:
`going_deeper.html` is not a `build_css` source, so nothing regenerated.

---

# S125 WORK — SEE `LIVE_ZUMO_TEXTBOOK.md` FOR THE FULL ACCOUNT

DJ ruled **C**: *"I want the book to be the same throughout."* `going_deeper.html` is the **first
direct consumer of `css/semantic.css`**. Four declarations left the page, nothing was added, six lines
changed. **§27.15c NEW.** Bible **v8.116**, `going_deeper` **v01.5.0**.

**Gate 56 NEW (`book_gates` v1.51), shipped in a second push** after the ruling was found ungated —
control-run six ways, each defect firing it ALONE, `regex_audit` 0 leads. Bible **v8.116.1** carries the entry.

**Two things recorded and NOT ruled, both live for S126:**
- **§27.12 still cannot reach `going_deeper.html`.** Gate 44 keys on `css/book.css` appearing in the
  file, so the page's **seven inline `style` attributes** stay outside it while the page is now PARTLY
  converted. The gate's own scope comment names those seven deliberately — so this is a scope question,
  not an oversight. **Is a page that consumes the semantic layer "converted"?**
- **`going_deeper.html` loads the Inter webfont and never uses it.** Preconnect plus stylesheet link on
  lines 9–10; its only `font-family` declarations were Arial for `body` and the ruled mono stack, and
  the mono ones are now gone. Every lesson body is Inter. So the page is off-family in body text AND
  pays for a font it discards. **Two possible rulings and they point opposite ways:** adopt Inter (the
  book's body face, and the request is already being made), or drop the two `<link>` lines (the page is
  deliberately its own thing). Measure what else differs before ruling — this is a page-identity
  question, not a font question.

---

# S126 QUEUE

## The colour ledger — still the big one
- **`ZUMO_COLOR_LEDGER.md`'s 16 items can be reopened.** The blocking fact (155 hexes inside 562 class
  names, so a repaint is a RENAME) is a fact about the GENERATED block only. **Three items are marked
  *re-measure before ruling* — they date from S94, before §27.**
- **The wash remains the precedent to notice:** a value that inherits its context can retire a whole
  class of scope exceptions.
- **The two pink pills in L03 are spelled `#f5c6cb` and `#f5c6c0`** — one digit apart, both pink, on the
  same construct. That is a typo, not two colours. A colour-ledger item.

## Graduation candidates — one at a time, and now with a second consumer to check
**540 of 636 class names encoded a value at S123; the pill took nine of them out.** Suggested next:
- `.code-block-333` / `.code-block-bg-1e1e1e` — §6.11's LOCKED single dark block, which is ALSO a
  Tier-2 census item: **16 distinct `<pre>` opening shapes** against a rule saying there is one.
  Graduating it and closing the census item are the same job. **NOTE: going_deeper sets its own `pre`
  background `#1e1e1e` and `color #e8e8e8`, below the link, so it would win the collision — but check,
  do not assume.** Re-measure: S123 put the total at 31 shapes splitting ~16 block / ~14 inline, and the
  inline half moved under S124's strip.
- Callout families — but **NOT before the colour ledger**, since their whole point is paint. **And
  going_deeper defines its own `.callout`.**

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
- **Should `css/semantic.css` carry a version home?** Carried from S123. **The case is stronger again
  at S125** — it now holds two ruled constructs, has an external consumer that can break if it changes,
  and TWO gates (54 and 56) depend on its contents. `session_versions` could register it in a line.
- **Is anything ELSE in the repo carrying a version that nothing tracks?** `timer.html` was the S123
  case; the sweep was never run.
- **L14's score formula is marked up as `<code>` and is not code.** The markup question is real and
  separate: `FIELD SCORE = ( LINE TRACING SCORE + EXIT BONUS ) × EVACUATION ZONE MULTIPLIER`.
- **`sweep_option_c.py` sits in the repo root** — the S92 one-shot callout sweep. `session_versions.py`
  references it so it is not orphaned, but it is not in any handoff's instrument list. Housekeeping.

## Carried, unchanged
- **L01's BC02 does not carry L01's objectives.** Ruled legacy S119, still the only §25.5 violation.
- **S116's past-tense question: RETIRE IT.** Eleven sessions now.
- **L10's `What You Built` is the only non-Brain-Check `<h4>` in a converted §10.**
- **The syllabus/TDP consequence of the L13 stop** — a syllabus question, not a book question.
- **L03's `id="whats-next"` is in all fifteen**; §27.14 still cannot see an unreached id.

## Rulings outstanding — carried
- Should `build_family_map` parse its total instead of holding a baseline? Baseline unmoved six
  sessions running.
- Should `build_css` name rules by usage RANK at all? Rank-naming is what renamed
  `.code-ff-uimonosp-2` out from under three surviving elements (§27.15b).
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
9. **Exactly ONE `ZUMO_SNN_HANDOFF.md` in the root (gate 28).** At S126 close, adding
   `ZUMO_S127_HANDOFF.md` means DELETING **this** file — a GitHub Desktop checkbox.
10. **THE NUMBER IN THE FILENAME IS THE SESSION THAT READS IT, NOT THE ONE THAT WROTE IT.**
11. **Never write a real version number as `vOLD → vNEW` in prose.** `_versions_in()` takes the
    LAST match in the file. Write *"reaches vNEW (from vOLD)"*. Backticks do not shield it.
12. **THE SAME TRAP APPLIES TO SHAs.** One sha per parsed line. Never name a second one in prose.
13. **A document cannot name the commit that contains it.** LIVE.md's verification line names the
    commit carrying the PREVIOUS state; the push that fills it is necessarily one commit later.
    `session_versions --check` prints this as an expected note, not drift — read the note.
14. **AN EDIT TO A FILE WITH REPEATED LANDMARK LINES TARGETS AN INDEX AND ASSERTS IT** (§6.12c for
    markdown), never a prefix match. LIVE.md has TWO `**Versions:**` lines and the second is a
    historical per-session snapshot whose contents must not move.
16. **WRITE THE GATE IN THE SAME PASS AS THE RULING.** S125 ruled §27.15c, shipped it, and wrote the
    coupling risk into this handoff without a gate — four separate defects then passed 55 of 55.
    A ruling that creates a new delivery path owes a gate on that path before the push, not after.
15. **A VERSION HOME FOUND BY GREPPING FOR A SPELLING IS A HOME YOU HAVE NOT ENUMERATED.** S125
    grepped `version:` and `Version 1` and missed `Version 01.4`. Gate 1 caught it. `session_versions`
    holds the regex for every registered artefact — read ARTEFACTS, do not invent a search.
