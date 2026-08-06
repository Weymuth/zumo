# ZUMO — S122 HANDOFF (written at S121 close · paste at top of Session 122)

## Session open ritual (do this without being asked)
1. **`git ls-remote https://github.com/Weymuth/zumo.git HEAD` FIRST.** If the clone's
   `git log -1` does not match, fetch the sha by name (§12.4, *caches lie*).
2. Read `LIVE_ZUMO_TEXTBOOK.md` — verify date / status / versions.
3. **Do NOT grep the Bible version.** `session_versions.bible_consistency()` parses it.
4. Run, and **READ THE EXIT CODE, NOT THE LAST LINE**:
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
9. **`gate_payload_match.py` needs the FULL lesson glob.** Run against one lesson it exits 1,
   because §11's inheritance rule puts lesson N−1's `finished` payload in N's corpus. That is
   not a defect and it cost a minute at S119.
10. Entrypoints are traps: `lesson_inventory.build(path)`, `gen_component.load_standard()`,
   `svg_layout_audit.audit(path)`, `flatten_alpha.flatten(path)`, `build_worklist.build(dir)`,
   `regex_audit.audit(paths)`, `session_versions.bible_consistency(path)`,
   `build_css.build(paths)`, `image_audit.audit(paths)`, `strip_inline.build(paths)`,
   `build_palette.build()`, `class_sweep.sweep(paths)`, `color_index.index(paths)`.
   **`lesson_inventory.build()` runs `expand_classes()` first**, so every `off` it reports is an
   offset into the EXPANDED source. Expand first, then slice.
11. **A CLONE IS NOT THE SITE.** Run `site_parity.py` after any push. It can FAIL on the first
   run in the minute after a push and pass on retry — Pages lag, not a defect (S112).
12. **VERIFY THE PUSH BY FRESH CLONE AND MD5 — AND DIFF THE STAGE AGAINST THE CLONE.**
13. **The lesson files are `Lesson_NN.html`, no topic suffix, and they live in `lessons/`.**

---

# ⏰ SEPTEMBER 8 IS ABOUT FOUR WEEKS OUT

**14 images outstanding of 141.** Unchanged. Photography still parked.

**THE FORWARD-POINTER ITEM IS CLOSED.** Opened as S121's first queue item, ruled by DJ in three
steps, applied and gated. Nothing in it remains open.

---

# THE ONE THING TO CARRY OUT OF S121

**VERSION CONTROL IS NOT A CONTROL HARNESS WHEN THE WORK UNDER TEST HAS NEVER BEEN COMMITTED.**

Gate 50 was control-run four ways. Each control injected a defect, ran the gates, then restored with
`git checkout -- <file>`. **All four printed FAIL and all four were worthless**, because none of the
session's work was committed: every *restore* reverted to the pushed tree and therefore DELETED the
block instead of putting it back. Controls two, three and four ran against a tree already failing for
a reason that had nothing to do with their injection.

**The untouched-tree control is what caught it** — the one control whose entire job is to have
nothing wrong with it, and it failed. Without that control the four FAILs would have been recorded as
evidence and the gate would have shipped unproven.

Redone from a pristine copy of the *working* tree, each control isolates cleanly: a deleted block
FAILS naming `07`, a wrong target FAILS naming *points at Lesson 9, expected 6*, a block on L16
FAILS, a block below the footer FAILS. §24.6b said *assert the injection landed*; it did not say
*assert the RESTORE landed*, and that is the half this session paid for.

---

# STATE

Fresh-clone verified at **`c2c8b97`**. Census **41,028**.
Bible **v8.110** · `BookComponentStandard` **v01.12.1** · Maker **v2.45.2** ·
`marks/` **41** · `icons/` **49** incl. LICENSE.
`ZUMO_Syllabus_WORKING.md` **v1.2**.

Instruments: `book_gates` **v1.46** · `lesson_inventory` **v1.2.0** ·
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
`next_pointer` **v1.0.1** ·
`going_deeper` **v01.4.1**.

Lessons: L01 v03.20.0 · L02 v03.12.0 · L03 v03.29.0 · L04 v04.20.0 · L05 v04.20.0 · L06 v04.24.0 · L07 v04.23.0 · L08 v04.20.0 · L09 v05.17.0 · L10 v02.18.0 · L11 v02.19.0 · L12 v01.21.0 · L13 v02.19.0 · L14 v02.24.0 · L15 v02.20.0 · L16 v02.12.1.

**50/50 gates.** `--anomalies` silent · family map **1069/1069** · `regex_audit` 0 leads ·
`build_css --check` current at **643 rules** · 0 dead classes · `color_index --check` clean ·
`build_palette --check` matches the ruling · `image_audit --check` current at 14 outstanding of 141 ·
both banner generators green · `gate_payload_match` PASS on the full glob · `next_pointer --check`
clean. **The stylesheet was regenerated** (digest-only move, see below), but **no class was renamed
and no lesson was re-classed**, so none of §27.8b's three steps ran.

---

# S121 WORK — THE FORWARD POINTER, AND THE LINK THAT WAS NEVER THERE

**§3.1a IS NEW: EVERY LESSON 01–15 ENDS WITH A WORKING LINK TO THE NEXT LESSON.**

The construct census S120 recorded was right and led the wrong way. Counting **constructs**, seven
lessons carried neither a *What's Next* heading nor a `Next:` paragraph. Counting **content**,
thirteen of fifteen already named the next lesson in their final quarter — the pointer was nearly
universal and nearly invisible. **Only L11 and L12 had no forward reference at all**, and L11's only
tail mention pointed *backward* to L10. DJ: *"keep the 2 new ones like the other 13."*

**The real defect was elsewhere, and it was measurable:** zero of sixteen lessons contained a single
`<a href>` to a lesson file anywhere in their tail. *"In **Lesson 7: Code Organization**…"* is bolded
text shaped exactly like a link that does nothing.

**The seat is the ruling's other half.** The pointer prose sits at 84% of the page, *above*
Engineer's Log — which feeds the TDP, 25% of the syllabus grade — and above the bonus block and quick
reference. A link there routes students past the graded work: §3.1's failure one scale down. The
generated block therefore sits immediately above the §5b footer, the last element on the page and the
only seat present exactly once in all sixteen lessons.

**New tool `next_pointer.py` v1.0**, generating rather than repairing (§6.8a). Lesson titles are
DERIVED from the §6.5a strip after asserting it is byte-identical across all sixteen — no title is
typed anywhere in this session's work. L16 generates no block and gate 50 fails if it acquires one.

**The anchor is a teacher affordance and is labelled as one.** DJ ruled *"we need an anchor link in
all books"*; the block carries `id="next-lesson"` in all fifteen, giving a stable Canvas address.
It buys students nothing new: the strip lives in `<nav class="nav">` at `position: sticky; top: 0`,
so all sixteen links are already on screen at the bottom of every page. **L03's orphan
`id="whats-next"` is the proof** — the string occurs exactly once in the repo, in L03's own heading,
targeted by no link anywhere, and §27.14 cannot see it because it asserts every LINK resolves to an
id, never that every ID is reached.

**§27.11's digest moved, rules did not** — 643/2,357, zero born/died/altered, S113's shape a fourth
time. `build_css` orders rules by usage RANK, so fifteen new uses of `.link-c-2e86ab` (398→413) and
`.p-mt-22px` (29→44) relocated one rule and changed two comments. 20 changed lines, every one a
comment or that relocation. Re-controlled: a dropped `color: white;` still FAILS.

Census 40,979 → **41,028** — 45 lines for fifteen blocks plus 4 for the two authored pointers, which
is the arithmetic proving nothing else moved.

---

# S122 QUEUE

## Found after the S121 push, fixed, and worth a rule
- **A LOOP WITH NO `break` DESTROYED A HISTORICAL LINE IN LIVE.md, AND NO GATE COULD SEE IT.**
  The S121 regeneration replaced every line matching `**Versions:**`, not the first — so the
  per-session snapshot at line 1968 (an L01 from the v03.15 era) was overwritten with the S121 line
  and pushed. **The landmark COUNT was 2 before and 2 after**, so any count-based check is satisfied
  BY the defect — §24.6's shape exactly, one file over. Caught only by diffing LIVE.md against the
  pre-push clone, which is not part of any ritual. Restored byte-exact from that clone; LIVE.md now
  differs from its pre-push state in exactly ONE region, asserted. **The rule to adopt: an edit to a
  file with repeated landmark lines targets an INDEX and asserts it (§6.12c for markdown), never a
  prefix match — and a regeneration is verified by DIFFING against the pre-push copy, never by
  re-counting landmarks.** Offered and not built: a gate asserting LIVE.md's historical per-session
  blocks are append-only.
- **`next_pointer.py` reaches v1.0.1** — the lossy-derivation note DJ asked for is now in the
  docstring: `esc()` rewrites an apostrophe to `&rsquo;`, so the emitted title is not a byte-faithful
  copy of the strip's. One title is affected (L11's), nothing is broken, and L10's own callout
  already spells it that way. **Fix deferred by DJ ruling** — dropping the apostrophe branch changes
  one character in `Lesson_10.html` and needs a version bump.
- **BODY DEPTH IS ALREADY UNIFORM — THE VARIANCE I REPORTED DID NOT EXIST.** DJ ruled that all body
  depths should be identical across the book; measured three ways, they already are. The footer and
  the next-lesson block are direct children of `<body>` in all sixteen, ONE distinct ancestor chain
  each, confirmed by an independent library (bs4) after two hand-rolled parsers disagreed. **The
  2-vs-3 spread I reported was an instrument defect:** the parser pushed every start tag onto its
  stack including void elements (`<br>`, `<img>`, `<hr>`), which never emit an end tag, so measured
  depth grew with the number of unrelated voids in the ancestry. Control-run: 0/1/3 preceding `<br>`
  gives depth 2/3/5 on the buggy parser and 2/2/2 on the void-aware one. **No work is required, and
  a wrong finding cost a ruling.**

## Opened by S121, needs a decision
- **`next_pointer.py` IS NOT REGISTERED IN `session_versions.py`.** Its version is therefore
  unwatched — it appears in no emitted block and no `--check`. Registering it is not free: the
  selftest asserts every registered artefact appears in BOTH blocks, so the emitters move together.
  Rule it or accept the debt knowingly.
- **L03's orphan `id="whats-next"` was NOT removed.** Left live pending DJ's call, since he may want
  it as a link target. If it stays, the three-way heading-text drift below stays with it.
- **THE HEADING TEXT STILL DRIFTS THREE WAYS** and was deliberately not fixed: *What's Next* (L01,
  L08), *What's Next?* (L05, L06, L07, L14), *What's Next: Preview of Lesson 4* (L03). Priced and
  declined: heading text renders, so §5b makes each a MODERATE bump — three MODERATE bumps for a
  question mark, four weeks out. Revisit after September 8.
- **THE TWO POINTER CONSTRUCTS NOW COEXIST BY PRACTICE AND NOT BY RULING.** §3.1a governs the LINK,
  not the prose above it. The h3 section (7 lessons) and the `Next:` paragraph (now 11–15) do
  different-sized jobs and L14 stacks both. Recommended and not ruled: leave them, canonize neither.

## Carried, unchanged
- **L01's BC02 does not carry L01's objectives.** Ruled legacy S119, still the only §25.5 violation.
- **S116's past-tense question: RETIRE IT.** Seven sessions now. Retire deliberately.
- **L10's `What You Built` is the only non-Brain-Check `<h4>` in a converted §10.**
- **The syllabus/TDP consequence of the L13 stop** — a syllabus question, not a book question (§3.1).

## Rulings outstanding — carried
- **Should `build_family_map` parse its total instead of holding a baseline?** Baseline unmoved two
  sessions running now. Rule it or drop it.
- **Should `build_css` name rules by usage RANK at all?** — S121 makes this concrete: the ranking is
  the sole reason the digest moved for a change that added no rule and altered none.
- **The `#666` footer colour** — 18 declarations, eight `.p-c-666*` families whose NAMES encode the hex.
- **16 uppercase-only colours** — 197 occurrences, no variance, unruled.
- **`font_stack_sweep` rule** — Consolas: 15 declarations, all with a fallback, zero bare.
- **Callout colours re-examined** — v8.87's Scope C.
- **`3.2` vs `3.5`** — before/after split, or one figure and a deleted row.
- **NOTE per-block pass** (133 blocks, four destinations).
- **Nav `<details>` carry no `data-reveal`** — §25.12 exists because one untyped `<details>` slipped.
- **Selftest-coverage gate** — offered, not built.
- **§25.10l's constant lives ONLY in `book_gates.py`** (gate 49), §21.1's shape.
- **The seven remaining figure tags** — S114's table.
- **⭐ heavy-lesson list needs a ruling** — L13 as a now-Fall lesson, deliberately unmarked.

## Ruled, not yet done
- **`[IMAGE 3.6]` → §22 terminal block, ONCE THERE ARE REAL NUMBERS.**
- **Apply GPT Task 2 and Task 4** — *if DJ still has the S112 outputs.* Not in the repo.

## Canon debts
**§3.1 AND §3.1a HAVE NO NUMBERED SECTION BODY** — both exist only in the version line and the
CHANGELOG, which is exactly the shape v8.103 closed for §24.14 and v8.101 logged for §21.1: a rule
whose home is a changelog entry holds only where someone happens to look. **This is the cheapest
canon debt on the list and the one most likely to bite.** ·
§21.1's thresholds live only in `book_gates.py` · §25.6 header example · §25.10e misfiled ·
challenge-card redesign Part B · difficulty-progression audit · Maker batch · L01 VS Code
multi-root · Stage Two two blocks labelled `Learn/Insight` (L03, L09) ·
`ROBOLORE_UPSTREAM_DELTA_S102.md` written and unapplied · robolore.com hosting ·
§6.5's "nav button count is 12–14" is **obsolete** under the six-pill rail — retire, don't argue ·
`css/book.css` has zero custom properties (`build_palette --css` emits them ready) ·
**26 gradient definitions across 18 SVG files** remain (5 referenced by nothing) ·
**41 marks generated in `images/marks/`, not one wired into a lesson**, against 2,016 emoji glyphs ·
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
4. **`lessons/` IS PART OF THE FILENAME.** Check the destination path of every file, not just its name.
5. **A push that bumps a version and omits LIVE.md is an INCOMPLETE push (§12.6).**
6. **§27.8b's third step is `strip_inline --apply --include-held`.** Without the flag, 624 held
   strings revert to inline and fifteen innocent lessons are rewritten.
7. **After any change that regenerates `css/book.css`, stage into a copy of the PUSHED CLONE
   and run `book_gates` THERE before presenting md5s.**
8. **AFTER ANY `css/book.css` REGENERATION, DIFF THE STAGE AGAINST THE PUSHED CLONE AND PUSH
   EVERY FILE THAT DIFFERS** — and diff by LINE, not only by expansion.
9. **Exactly ONE `ZUMO_SNN_HANDOFF.md` in the root (gate 28).** At S122 close, adding
   `ZUMO_S123_HANDOFF.md` means DELETING **this** file — a GitHub Desktop checkbox.
10. **THE NUMBER IN THE FILENAME IS THE SESSION THAT READS IT, NOT THE ONE THAT WROTE IT.**
11. **Never write a real version number as `vOLD → vNEW` in prose.** `_versions_in()` takes the
    LAST match in the file. Write *"reaches vNEW (from vOLD)"*. Backticks do not shield it.
12. **THE SAME TRAP APPLIES TO SHAs.** `session_versions` parses a sha out of LIVE.md's verification
    line. **One sha per parsed line. Never name a second one in prose, however clearly you disclaim it.**
13. **A document cannot name the commit that contains it.** LIVE.md's verification line names the
    commit carrying the WORK; the follow-up push that fills it is necessarily one commit later.
