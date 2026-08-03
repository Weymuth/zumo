# ZUMO — S112 HANDOFF (written at S111 close · paste at top of Session 112)

## Session open ritual (do this without being asked)
1. **`git ls-remote https://github.com/Weymuth/zumo.git HEAD` FIRST.** If the clone's `git log -1`
   does not match, fetch the sha by name (§12.4, *caches lie*).
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
   `gen_bonus_banner.py --selftest` · `gen_part_banners.py --selftest` ·
   `gate_payload_match.py newproject.html lessons/Lesson_*.html`
5. If `flatten_alpha --selftest` prints `NOT FULLY TESTED`: `pip install cairosvg
   --break-system-packages`. **Needed every session.**
6. `--anomalies` is SILENT when clean. Anything it prints is a real lead.
7. **Do not hand-type a version.** `session_versions.py --live` / `--handoff` EMIT the blocks.
8. Entrypoints are traps: `lesson_inventory.build(path)`, `gen_component.load_standard()`,
   `svg_layout_audit.audit(path)`, `flatten_alpha.flatten(path)`, `build_worklist.build(dir)`,
   `regex_audit.audit(paths)`, `session_versions.bible_consistency(path)`,
   `build_css.build(paths)`, `image_audit.audit(paths)`, `strip_inline.build(paths)`,
   `build_palette.build()`, `class_sweep.sweep(paths)`.
9. **A CLONE IS NOT THE SITE.** Run `site_parity.py` after any push.
10. **VERIFY THE PUSH BY FRESH CLONE AND MD5.**

---

# STATE

Fresh-clone verified at **`8ae3857`**. Census **40,013**.
Bible **v8.100** · `BookComponentStandard` **v01.12.1** · Maker **v2.45.2** ·
`marks/` **41** · `icons/` **49** incl. LICENSE.
`ZUMO_Syllabus_WORKING.md` **v1.0**.

Instruments: `book_gates` **v1.42.1** · `lesson_inventory` **v1.2.0** ·
`gen_component` **v1.6.1** · `pill_sweep` **v1.1** · `gate_payload_match` **v1.7** ·
`build_family_map` **v1.3.1** · `build_mark_index` **v1.0.2** · `gen_bonus_banner` **v1.4.1** ·
`gen_part_banners` **v1.2** · `session_versions` **v1.15.1** · `fit_raster_svg` **v1.2** ·
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
`going_deeper` **v01.4.1**.

Lessons: L01 v03.19.1 · L02 v03.11.1 · L03 v03.24.1 · L04 v04.19.1 · L05 v04.19.1 · L06 v04.23.1 · L07 v04.21.1 · L08 v04.19.1 · L09 v05.16.1 · L10 v02.16.1 · L11 v02.17.1 · L12 v01.19.1 · L13 v02.17.1 · L14 v02.21.1 · L15 v02.17.1 · L16 v02.12.1.

**47/47 gates.** `--anomalies` silent · family map 1048/1048 · `regex_audit` 0 leads ·
`build_css --check` current at 650 rules · 0 dead classes · `build_palette --check` matches
the ruling · both banner generators green.

---

# THE ONE THING TO CARRY OUT OF S111

**THE REPAINT IS APPLIED, AND THE THING THAT NEARLY BROKE IT WAS SCOPE, NOT COLOUR.**

2,460 elements across sixteen lessons plus `going_deeper.html`. All **134 gradients flattened**
(v8.87's ban is absolute — the S111 handoff had listed them as *unruled*, which was an
inherited claim nobody had grepped). The 87 challenge-card headers took the §9 band.

**Callouts were protected BY DECLARATION STRING, never by hex.** Four of the five old group
colours — `#3498db`, `#3a7d5c`, `#9b6a9e`, `#6c757d` — are ALSO used by **nine callout rules**,
63 elements. A hex-level substitution would have repainted them, breaking v8.87's Scope C, and
**no gate would have said anything**: gate 41 only asks whether a class resolves. The repaint
therefore matched whole declaration blocks and skipped the 80 known callout declaration
strings, leaving **933 callout attributes untouched**.

**The general rule: a repaint is scoped by CONSTRUCT, and a colour is not a construct.**

**Seven gates fired and sorted into three kinds** — worth knowing because S108 predicted the
number and not the shape:
- **four generators hard-coded the old band colours** — `BAND_END`, `gen_part_banners`,
  `gen_bonus_banner`, and §25.10h's panel. All four cleared once the constants moved.
- **one real gap** — `going_deeper.html` is page 17, is NOT in `lessons/`, and does not link
  `css/book.css`. §25.6 caught it as *sixteen heroes agree, one does not*.
- **two baselines that move by design** — §27.11 and §5.1's `GEOM_BASELINE`.

**THE CASE TRAP, and it cost the most time.** `build_palette` emits **UPPERCASE** hexes; every
value parsed out of the book is **lowercase**. §5.1 compares the raw string, so the mismatch
made five constructs read as NEW off-canon blocks — and then *passed* §5.1 while failing four
other gates once half-fixed, which sent the first diagnosis in the wrong direction entirely.
The whole repaint is now lowercase, 1,809 occurrences normalised through the cycle.

**`strip_inline` HAS NO DEFECT — I reported one and was wrong.** `--restore` then `--apply`
leaves 39 inline attributes per lesson because the four held blocks are held on the apply side.
**`--apply --include-held` is the flag, it already existed, and it round-trips BYTE-IDENTICALLY
across all sixteen** (controlled: 0 files changed, css untouched). The documented cycle is
**restore → edit → `build_css` → `apply --include-held`**, and skipping the restore step first
destroys information: regenerating before restoring left 3 classes unrestorable.

---

# S111 WORK

## The palette was re-ruled from rendered specimens — `ZUMO_S111_VISUAL_RULING.md`

Eight bands. `build_palette.py` **v1.0 → v1.1**, and it reproduces the approved specimen under
assert — which caught a real bug: reading the hue-override chroma straight from the constant
instead of round-tripping through a real sRGB colour moved Testing `#00474B` → `#00494D`, a
palette DJ never saw.

- **+18° Wrap Up rotation DROPPED** — re-derived, it bought ΔE76 **0.33**.
- **Heritage Slate Blue LEFT the band set.** DJ found Theory and Testing by eye before any
  number said so. Leave-one-out over nine candidates: dropping Slate Blue → 18.9, Theory →
  17.5, any other band → 9.4, **Hardware → 5.3, worse**. Only removing a navy helps.
- **Testing takes teal 200°; rose 337° and hunter green 148° join. Amber REJECTED** — 20.4°
  from WARNING and ΔE76 11.6 from Challenges.
- **Chroma damping 0.62 → 0.90**, a deliberate step back from S110's sun-faded look. It also
  *improved* separation 15.4 → 22.2.
- **Chroma is per band**: rose and green stay 0.62, Challenges 1.20 — the gamut ceiling, since
  real Warm Brass is L* 69 and white on it is 2.34, so **a band with white cap text cannot be
  brass**.
- **Challenge-card headers take the §9 band**, superseding v8.87's Antique Bronze.
- **Nav and hero take Theory's band** `#1f2a3d` — chosen because the alternatives needed four
  white-on-dark rules re-treated inside the nav.

**Rose and green still have NO JOB.** They cannot appear on a page until something names them.

## Other S111 work

- **`[IMAGE 2.5]` RETIRED.** L02's completed program is a live code block, not a screenshot —
  `image_audit` can ask whether a tag HAS an asset and never whether the tag SHOULD EXIST.
  Planned 145 → 144, outstanding 19 → **18**. `[IMAGE 3.4]` and `[IMAGE 3.6]` are the same
  shape (§22 terminal blocks, of which the book already carries 13) and are QUEUED.
- **THE ICON LEGEND IS GONE**, 10 lessons — **L11–L16 never had one**. Nothing linked to it.
  §6.6 annotated in place: the icon TABLE still governs, only the legend block is retired.
  Recorded there: §6.6 specified THIRTEEN icons and every live block carried TWELVE — 📘 NOTE
  was added to canon at v8.40 and never to the blocks.
- **A link/id audit of all 20 pages: 1,237 links, 705 ids, 0 duplicates, 0 broken.** Control-run
  with three planted defects, all named. **No gate covers this** — offered as gate 46, not built.
- **41 marks are generated in `images/marks/` and NOT ONE is wired into a lesson**, against
  **2,016 emoji glyphs** in the sixteen lessons. The icon arc is fully built on the supply side
  and has not started on the demand side. DJ: *"All the icons will be updated at some point."*

---

# S112 SO FAR — GATE 46 IS IN

**§27.14: every link and every id resolves.** 1,237 links, 705 ids, 20 pages, and nothing had
ever checked any of them. Parser-based (§24.10). Control-run on four shapes — dead in-page
anchor, duplicate id, missing file, dead cross-page fragment — with a RESOLVING cross-page
fragment planted beside the dead one so the branch runs both ways.

**Two things recorded in the gate itself:**
- Its first version reported **223 broken links**, all of them Maker URLs like
  `../newproject.html?lesson=1&kind=c01` — the query string read as part of the filename.
- **WHERE A GATE SITS IN THE FILE IS PART OF THE GATE.** Appended below the summary and its
  `sys.exit(1)`, it printed PASS *after* `ALL GATES PASS` on a clean tree and **never ran at
  all** on a failing one. A gate that executes only when everything else passes cannot catch
  anything in a failing suite. Caught by the control run, not by reading.

`book_gates` **v1.41.0, 46 gates** · Bible **v8.100** No lesson file changed.

## Going Deeper is on the book's settings

It was the only page in the book with a **dark** design system — and the S111 repaint made that
worse before it made it better: dropping Theory's `#1f2a3d` on its hero gave **contrast 1.31
against `--bg` and 1.17 against `--surface`**, so the hero stopped being a distinguishable
element at all. Its own `--accent #4f8ff7` and `--accent-dim #3a6bc5` sit at hue 282° and 285°,
both in Deep Navy's family, so the page was blue on blue on blue.

**The conversion was small because the page is well built** — 35 `var()` references reading from
12 custom properties. All eleven live ones remapped, every value clearing 4.5: `--accent` to the
§1–3 band 12.88, `--green` to hunter green 4.90, `--yellow` to the §9 brass 5.76, `--orange` to
Forge Red 8.15, `--text-dim` 5.37. **`--purple` DELETED — it styled nothing.** Four rules
hard-coded a dark panel outside `:root` and each got a deliberate destination: `code` and `pre`
to `#1e1e1e` per §22, `th` to the accent with white text (the lessons' table-header pattern),
`.callout` to Green's tint. Zero dark values remain. **going_deeper v01.3.0 → v01.4.0.**

**NOT DONE, DELIBERATELY:** the page still does NOT link `css/book.css` and keeps its own 47
rules. Making it share the stylesheet means widening `build_css.SOURCES`, and `strip_inline`'s
header records what that cost at S105 — **46 of L01's 167 class names kept their spelling and
changed their meaning**, invisible to gate 41. One page is not worth that. It now carries the
same VALUES without sharing the FILE.

---

# S112 QUEUE

## Ruled, not yet done
- **Callout colours get re-examined** (DJ: *"we will need to look at the callout colors again"*).
  This is the 1,048-block arc v8.87's Scope C deliberately deferred.
- **`[IMAGE 3.4]` and `[IMAGE 3.6]` → §22 terminal blocks.** 3.6 still needs REAL numbers from a
  real TRIM run; a fabricated log is the same defect as a fabricated screenshot.
- **Name rose and green.** A ChatGPT brief was written for this (task 3).

## Rulings outstanding
- **`font_stack_sweep` rule** — it still wants to rewrite all 15 Consolas stacks and the
  standing note says they are correct. A genuine rule disagreement.
- **`IMAGE 3.14` row** — drop the bracketed tag, or teach `image_audit` to skip a removed row.
- **`3.2` vs `3.5`** — before/after split, or one figure and a deleted row.
- **Rule the 12 callout families**, then the NOTE per-block pass (133 blocks, four destinations).
- **Nav `<details>` carry no `data-reveal`** — §25.12 exists because one untyped `<details>` slipped.
- **Selftest-coverage gate** — offered, not built. (Gate 46 SHIPPED, see above.)

## Canon debts
§21.1's thresholds live only in `book_gates.py` · §25.6 header example · §25.10e misfiled ·
challenge-card redesign Part B · difficulty-progression audit · Maker batch · L01 VS Code
multi-root · Stage Two two blocks labelled `Learn/Insight` (L03, L09) ·
`ROBOLORE_UPSTREAM_DELTA_S102.md` written and unapplied · robolore.com hosting ·
§6.5's "nav button count is 12–14" becomes **obsolete** under the six-pill rail — retire, don't argue ·
`css/book.css` has zero custom properties (`build_palette --css` emits them ready) ·
**Consolas: 15 declarations, all with a fallback, zero bare — the note is CORRECT.** ·
**26 gradient definitions across 18 SVG files** remain (5 referenced by nothing) — v8.87's ban
covers graphics too and the SVGs were NOT touched this session.

## Bench (need the robot)
Q017 L09 six numbers · Q044 calibration-spin · Q046 gyro-bias · L02 §5 green-LED ·
Constrain RUN_MS · cm/s at a stated BASE_SPEED.

---

# ⏰ IMAGES — SEPTEMBER 8 IS FIVE WEEKS OUT

**18 outstanding of 144.** Two of those retire into terminal blocks the moment that queue item
is done, taking it to 16. `L02_IMAGE_2-05` is retired outright. `3.2`, `3.5` and `VIDEO 3.1`
need one floor rig; `3.4` and `3.6` have good captures already if the block route is declined.

---

# PUSHING — READ THIS

Named-file CLI for adds and modifies; **GitHub Desktop for deletions.** **Never `git add .`**

1. **`(1)` does not mean stale.** Verify by **md5**, never by suffix.
2. **Never present a test file in the same list as repo files.** The `PREVIEW_*.html` files from
   S111 are NOT repo files.
3. **Never produce PUSH_ME_*.md or MD5_*.txt.** Checksums and instructions go in the CHAT ONLY.
4. `going_deeper.html` belongs at the repo ROOT, not in `lessons/`.
5. **A push that bumps a version and omits LIVE.md is an INCOMPLETE push (§12.6).**
6. **After any change that regenerates `css/book.css`, stage into a copy of the PUSHED CLONE and
   run `book_gates` THERE before presenting md5s.**
