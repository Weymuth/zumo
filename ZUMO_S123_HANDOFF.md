# ZUMO — S123 HANDOFF (written at S122 close · paste at top of Session 123)

## Session open ritual (do this without being asked)
1. **`git ls-remote https://github.com/Weymuth/zumo.git HEAD` FIRST.** If the clone's
   `git log -1` does not match, fetch the sha by name (§12.4, *caches lie*).
2. Read `LIVE_ZUMO_TEXTBOOK.md` — verify date / status / versions.
3. **Do NOT grep the Bible version.** `session_versions.bible_consistency()` parses it, and the
   Bible has THREE homes now — header line 17, the `Current:` clause, and the newest CHANGELOG
   entry. **Control F fails if any two disagree**, and it caught exactly that at S122 when the
   first two were bumped and the changelog was not.
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
   `next_pointer.py --selftest` then `--check`
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
   `build_palette.build()`, `class_sweep.sweep(paths)`, `color_index.index(paths)`.
11. **A CLONE IS NOT THE SITE.** Run `site_parity.py` after any push. It can FAIL on the first
   run in the minute after a push and pass on retry — Pages lag, not a defect (S112).
12. **VERIFY THE PUSH BY FRESH CLONE AND MD5 — AND DIFF THE STAGE AGAINST THE CLONE.**
13. **The lesson files are `Lesson_NN.html`, no topic suffix, and they live in `lessons/`.**

---

# ⏰ SEPTEMBER 8 IS ABOUT FOUR WEEKS OUT

**14 images outstanding of 141.** Unchanged. Photography still parked.

---

# THE ONE THING TO CARRY OUT OF S122

**A SECTION QUESTION ASKED WITH A PAGE-WIDE INSTRUMENT RETURNS AN ANSWER, AND IT IS WRONG.**

It happened three times in one session, in three different disguises:

- The audit reported L05 as needing only an id. That MEANT its opener paragraph already
  existed — and a second, near-identical opener was added anyway, because the *result* was read
  instead of the file.
- A stray-`Next:`-paragraph check searched the whole page, so a paragraph correctly **moved
  into** the section still tripped it. The file was right; the instrument could not tell
  *inside* from *outside*.
- A read-back assert counted `<p>In <strong>Lesson` page-wide and caught L12's **backward**
  references — *"In Lesson 4 you calibrated…"* — and aborted a run that had worked.

**Gate 51 is section-scoped throughout, and it earned its place immediately** by catching L09's
opener buried mid-paragraph after a hand-rolled audit had passed it. **The gate found what the
sweep that motivated it could not.** When the question is about a construct, scope the
instrument to the construct — the page is not the unit.

---

# STATE

Fresh-clone verified at **`5ff1ab2`**. Census **41,128**.
Bible **v8.111** · `BookComponentStandard` **v01.12.1** · Maker **v2.45.2** ·
`marks/` **41** · `icons/` **49** incl. LICENSE.
`ZUMO_Syllabus_WORKING.md` **v1.2**.

Instruments: `book_gates` **v1.46.2** · `lesson_inventory` **v1.2.0** ·
`gen_component` **v1.6.1** · `pill_sweep` **v1.1** · `gate_payload_match` **v1.7** ·
`build_family_map` **v1.3.7** · `build_mark_index` **v1.0.2** · `gen_bonus_banner` **v1.4.1** ·
`gen_part_banners` **v1.2** · `session_versions` **v1.18.0** · `fit_raster_svg` **v1.2** ·
`flatten_alpha` **v1.2** · `svg_layout_audit` **v1.20** · `site_parity` **v1.1** ·
`build_css` **v1.2.1** ·
`image_audit` **v1.1** ·
`strip_inline` **v1.1** ·
`build_worklist` **v1.1** ·
`regex_audit` **v1.0** ·
`build_palette` **v1.1** ·
`class_sweep` **v1.0** ·
`color_index` **v1.0** ·
`font_stack_sweep` **v1.2.0** ·
`next_pointer` **v1.0.2** ·
`going_deeper` **v01.4.1**.

Lessons: L01 v03.21.0 · L02 v03.13.0 · L03 v03.30.0 · L04 v04.21.0 · L05 v04.20.1 · L06 v04.25.0 · L07 v04.24.0 · L08 v04.21.0 · L09 v05.18.0 · L10 v02.19.0 · L11 v02.20.0 · L12 v01.22.0 · L13 v02.20.0 · L14 v02.25.0 · L15 v02.21.0 · L16 v02.13.0.

**51/51 gates.** `--anomalies` silent · family map **1069/1069** · `regex_audit` 0 leads ·
`build_css --check` current at **641 rules** · `color_index --check` clean ·
`image_audit --check` current at 14 outstanding of 141 · both banner generators green ·
`gate_payload_match` PASS on the full glob · `next_pointer --check` clean.

**§27.11's baseline is 641 / 2,350** — it moved TWICE in S122 and the second move **died two
rules**, which had not happened before in this arc.

---

# S122 WORK — SEE `LIVE_ZUMO_TEXTBOOK.md` FOR THE FULL ACCOUNT

**§3.1b is new canon: every lesson 01–15 carries the canonical `What's Next?` section.** The
book ended four different ways; it now ends one way. **The shape is a FLOOR, not a ceiling** —
nothing was deleted to reach conformance, and lessons carrying more kept it. **§3.1a finally has
a numbered section body**, and the standing claim that §3.1 lacked one was measured FALSE.

**Titles are DERIVED from the §6.5a strip**, which caught L07 and L08 whose prose disagreed with
their own generated link block ninety lines below on the same page.

**Tier-1 normalizations:** one spelling of `🧠 THE LOGIC (Pseudocode)` (17 blocks) · one
back-to-top markup (89 of 237 rewritten) · the literal ☐ everywhere (98 entities).

---

# S123 QUEUE

## Top of the list — DJ asked for this by name
- **FEED THE TITLE, DON'T TYPE IT.** A generator that rewrites the
  `<strong>Lesson N: Title</strong>` span in every §3.1b opener from the §6.5a strip, so a title
  change propagates instead of drifting. **The target is measured and unique**:
  `<p>In <strong>Lesson N: Title</strong>,` occurs exactly once per lesson (a page-wide search
  does NOT — it matches backward references; see the S122 lesson above). Ship a gate with it.
  **Known lossy step to design around, not discover:** `next_pointer.py`'s `esc()` rewrites an
  apostrophe to `&rsquo;`, which today affects only a link label. Feeding titles into PROSE makes
  it visible in body text, which raises the priority of the fix deferred at S121 — L11's title
  *Time Lies, Distance Doesn't* is the affected one.

## The consistency census — Tier 1 done, Tiers 2 and 3 open
DJ: *"I feel like we should have every lesson checked like we did on this first one."* The method
is: parse one construct across all sixteen, group by shape, count the distinct shapes. **Counting
produces CANDIDATES; reading produces FINDINGS** (§24.6c), and a wrong finding costs 3× a blank one.

**Tier 2 — real spread, needs a ruling BEFORE any edit:**
- **Code block opening tag: 17 distinct shapes**, six-plus classes against §6.11's LOCKED single
  dark block.
- **Nav pill count ranges 10 to 19** — L09 has 19, nine lessons have 11. §6.5's "12–14" rule is
  already obsolete under the six-pill rail; **rewrite the rule before touching a lesson.**
- **Quick-reference anchors exist in five lessons only** (L02–L06); eight carry none.

**Tier 3 — needs reading, not counting:**
- **Three lessons have cards with Goal and Logic but fewer Templates**: L03 short one, L08 short
  three, L10 short two. May be legitimate — §6.12a allows prose for guided-edit and debug cards.
- **§7 ladder rungs 7A–7E appear in six lessons only** (L10–L15), against §15.1's five-rung canon.
- **L16's Engineer's Log is structured unlike the other fifteen** — the entry exists, the wrapper
  does not match.
- **Timers appear in L02, L03, L04 only.** S69 already burned a session on a false finding here.
  **Read this one before counting it.**

**Two instrument caveats, recorded so neither becomes a false finding:**
- **Glossary reported absent in all sixteen** — the probe only read `h2`/`h3` text, and §3.1a's
  own seat reasoning names a glossary. The absence is probably in the instrument.
- **Callout border-width returned zero shapes** — that probe looked for inline `border-left`,
  which the §27 migration deleted. It has to read the stylesheet now.

## Colour — see `ZUMO_COLOR_LEDGER.md`, do not re-derive it here
**16 items, opened S122, named by Bible §26.10.** The blocking fact: **155 hexes appear inside
562 class names**, so a repaint is a RENAME, not a substitution, and **the first item is not a
colour** — it is whether `build_css` emits custom properties. Three items are marked *re-measure
before ruling* because they date from S94, before the §27 migration.

**Do not rule a single colour because an unrelated arc surfaced it.** The Engineer's Log stripe
(`#0e1a2c` L01–L11, `#6f7582` L12–L16) is parked as C10 for exactly that reason.

## The glyph arc — DJ queued it explicitly
*"Leave the glyph and we can deal with them after this update. Then let's do the glyph."*
**2,701 glyphs across 95 distinct characters** in the sixteen lessons, against **41 marks
generated in `images/marks/` and not one wired into a lesson.**

## Carried, unchanged
- **L01's BC02 does not carry L01's objectives.** Ruled legacy S119, still the only §25.5 violation.
- **S116's past-tense question: RETIRE IT.** Eight sessions now.
- **L10's `What You Built` is the only non-Brain-Check `<h4>` in a converted §10.**
- **The syllabus/TDP consequence of the L13 stop** — a syllabus question, not a book question.
- **The three-way heading drift is GONE** (closed by §3.1b), but **L03's `id="whats-next"` is now
  in all fifteen** rather than removed — it has a purpose and §27.14 still cannot see an unreached id.

## Rulings outstanding — carried
- **Should `build_family_map` parse its total instead of holding a baseline?** Baseline unmoved
  three sessions running.
- **Should `build_css` name rules by usage RANK at all?** S122 makes this concrete for the third
  time: the digest moved twice, once for a change that added no rule.
- **NOTE per-block pass** (133 blocks, four destinations).
- **Nav `<details>` carry no `data-reveal`** — §25.12 exists because one untyped `<details>` slipped.
- **Selftest-coverage gate** — offered, not built.
- **§25.10l's constant lives ONLY in `book_gates.py`** (gate 49), §21.1's shape.
- **The seven remaining figure tags** — S114's table.
- **⭐ heavy-lesson list needs a ruling** — L13 as a now-Fall lesson, deliberately unmarked.
- **The two pointer CONSTRUCTS above the link** — §3.1b now rules the section; whether the prose
  inside it should follow one further pattern is not ruled.

## Ruled, not yet done
- **`[IMAGE 3.6]` → §22 terminal block, ONCE THERE ARE REAL NUMBERS.**
- **Apply GPT Task 2 and Task 4** — *if DJ still has the S112 outputs.* Not in the repo.

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
5. **A push that bumps a version and omits LIVE.md is an INCOMPLETE push (§12.6).**
6. **§27.8b's third step is `strip_inline --apply --include-held`.** Without the flag, 624 held
   strings revert to inline and fifteen innocent lessons are rewritten.
7. **After any change that regenerates `css/book.css`, stage into a copy of the PUSHED CLONE
   and run `book_gates` THERE before presenting md5s.**
8. **AFTER ANY `css/book.css` REGENERATION, DIFF THE STAGE AGAINST THE PUSHED CLONE AND PUSH
   EVERY FILE THAT DIFFERS** — and diff by LINE, not only by expansion.
9. **Exactly ONE `ZUMO_SNN_HANDOFF.md` in the root (gate 28).** At S123 close, adding
   `ZUMO_S124_HANDOFF.md` means DELETING **this** file — a GitHub Desktop checkbox.
10. **THE NUMBER IN THE FILENAME IS THE SESSION THAT READS IT, NOT THE ONE THAT WROTE IT.**
11. **Never write a real version number as `vOLD → vNEW` in prose.** `_versions_in()` takes the
    LAST match in the file. Write *"reaches vNEW (from vOLD)"*. Backticks do not shield it.
12. **THE SAME TRAP APPLIES TO SHAs.** One sha per parsed line. Never name a second one in prose.
13. **A document cannot name the commit that contains it.** LIVE.md's verification line names the
    commit carrying the WORK; the follow-up push that fills it is necessarily one commit later.
14. **AN EDIT TO A FILE WITH REPEATED LANDMARK LINES TARGETS AN INDEX AND ASSERTS IT** (§6.12c for
    markdown), never a prefix match — and a regeneration is verified by DIFFING against the
    pre-push copy, never by re-counting landmarks. LIVE.md has TWO `**Versions:**` lines and the
    second is a historical per-session snapshot from an earlier era, whose contents must not
    move (naming its versions here would trip rule 11). S122 replaced index 6 only and
    asserted line 2073 byte-identical.
