# ZUMO — S103 HANDOFF (written at S102 close · paste at top of Session 103)

## Session open ritual (do this without being asked)
1. `git clone --depth 1 https://github.com/Weymuth/zumo.git`
2. Read `LIVE_ZUMO_TEXTBOOK.md` — verify date / status / versions.
3. `grep -m1 -oE "Bible version: v[0-9.]+" ZUMO_SUPER_BIBLE.md` — **`-m1` matters**.
4. Run: `book_gates.py` · `gen_component.py --selftest` · `lesson_inventory.py` ·
   `lesson_inventory.py --anomalies` · `pill_sweep.py --audit lessons/Lesson_*.html` ·
   `build_family_map.py` · `fit_raster_svg.py --selftest` · `flatten_alpha.py --selftest` ·
   `svg_layout_audit.py --selftest images/L01_GRAPHIC_1-13_zumo_rear_view.svg` ·
   `regex_audit.py --selftest` then `regex_audit.py` ·
   `build_worklist.py --selftest` ·
   `session_versions.py --selftest` then `session_versions.py` ·
   `site_parity.py --selftest` then `site_parity.py`.
5. `flatten_alpha --selftest` no longer dies without `cairosvg` (v1.2) — it **SKIPS control 2 and
   says so**. If you see `NOT FULLY TESTED`, the gradient path was not exercised:
   `pip install cairosvg --break-system-packages` and re-run.
6. `--anomalies` is SILENT when clean. Anything it prints is a real lead.
7. **Do not hand-type a version.** `session_versions.py --live` / `--handoff` EMIT the blocks.
8. Entrypoints are traps: `lesson_inventory.build(path)`, `gen_component.load_standard()`,
   `svg_layout_audit.audit(path)`, `flatten_alpha.flatten(path)`, `build_worklist.build(dir)`,
   `regex_audit.audit(paths)`.
9. **A CLONE IS NOT THE SITE.** Run `site_parity.py` after any push.
10. **VERIFY THE PUSH.** Three pushes silently failed in S102 and one carried five files nobody
    intended. Fresh-clone and md5 every file before believing it landed.

---

# STATE

Fresh-clone verified at **`4aafdc8`**. Census **39,978**.
Bible **v8.88** · `BookComponentStandard` **v01.12.1** · Maker **v2.45.1** ·
`marks/` **41** · `icons/` **49** incl. LICENSE.

Instruments: `book_gates` **v1.34.5** · `lesson_inventory` **v1.1.2** ·
`gen_component` **v1.6.1** · `pill_sweep` **v1.0** · `gate_payload_match` **v1.6** ·
`build_family_map` **v1.1.3** · `build_mark_index` **v1.0.2** · `gen_bonus_banner` **v1.2.1** ·
`gen_part_banners` **v1.0** · `session_versions` **v1.9.1** · `fit_raster_svg` **v1.2** ·
`flatten_alpha` **v1.2** · `svg_layout_audit` **v1.19** · `site_parity` **v1.0** ·
`build_worklist` **v1.0** ·
`regex_audit` **v1.0** ·
`going_deeper` **v01.1.1**.

Lessons: L01 v03.15.0 · L02 **v03.7.0** · L03 v03.20.0 · L04 v04.15.0 · L05 v04.15.0 ·
L06 v04.19.1 · L07 v04.15.0 · L08 v04.14.0 · L09 v05.12.0 · L10 v02.11.0 · L11 v02.12.0 ·
L12 v01.14.0 · L13 v02.12.0 · L14 **v02.16.0** · L15 v02.11.1 · L16 v02.7.0.

**40/40 gates.** Two lesson files touched in S102 (L02, L14); census 39,972 → **39,978**.

---

# THE ONE THING TO CARRY OUT OF S102

**Eight defects were found. Reading code found none of them.**

Every one came from comparing an output against something external — a render, a fresh clone, a
regeneration, or a re-run with the input perturbed:

| Found by | Defect |
|---|---|
| render vs. estimator | `svg_layout_audit` was CSS-blind — 371 of 2,469 labels measured at the wrong size |
| DJ's corrected file | absolute `y` on a `<tspan>` was invisible; wrapped labels collapsed onto one baseline |
| render vs. estimator | `rotate()` matched by the transform regex and silently dropped — a 14-unit label reported 95 wide |
| regenerate + diff | set iteration made the work list non-reproducible across processes |
| wiring a graphic | L14's scoring table taught one side of a rules contradiction as fact |
| adding a row | L02's `2-05` SVG was missing a row **its own caption named** |
| repointing a link | a student-facing PDF download button had been 404ing |
| render vs. audit | four of five findings on one file were phantoms |

**The discipline that produced them:** after any tool reports, ask what independent artefact would
disagree if the report were wrong — then produce that artefact. Reading the code checks it against
your model of it; rendering checks it against reality.

**And the counter-lesson, twice:** two of my own controls reproduced the bug they were testing for.
An isolation render **stripped the `<style>` block**, so the text rendered at the wrong size — the
exact CSS blindness under test. A composite scan returned **the same number for three different
strings**, which is the tell (§24.8). Control the control.

---

# S102 WORK, BY LAYER

## Instruments

- **`svg_layout_audit` v1.16 → v1.19.** CSS cascade resolution (inline `style` > `<style>` class >
  presentation attribute, then inherited); mono/serif/italic metrics; letter-spacing; absolute
  `tspan y`; rotation **refused and reported** rather than mis-measured; proportional error floor
  (`max(2.0, 1.5%)`, set from five render-verified files); deterministic output; small containers
  (a label on a 126×38 pill is bounded by the pill); phantom badges (a badge number must be short,
  alphanumeric, and land inside its circle).
- **`build_worklist` v1.0 — NEW.** `GPT_WORKLIST_S99.md` was hand-assembled, which is why nobody
  could re-derive it when S101 doubted it. It is a generate now, with a control that tests
  **ordering**, since ordering is the product.
- **`regex_audit` v1.0 — NEW.** Finds match-and-discard: a regex enumerating cases the code only
  partly handles. Corpus is clean but for `_ctm` itself.
- **`book_gates` v1.34 → v1.34.5.** Coverage constants moved with the work; §21 now also walks
  **any** file referenced out of `images/`, not only image extensions.
- **`flatten_alpha` v1.1 → v1.2**, **`session_versions` v1.7 → v1.9.1**.

## Canon

- **Bible v8.88, §26.9 — FORGE RED IS FUNCTIONAL, NOT A SIXTH BRAND COLOUR.** §26.8(7) reversed on
  placement; hex, name and every contrast figure stand. `InstructionalGraphicStandards` §6 says
  brand colours identify RoboLore and functional colours communicate meaning — **danger is
  meaning**. S101 filed a danger colour into the brand palette using a split whose founding rule
  forbids it. Cost of the reversal: **8 upstream files → 1**, palette stays five, §7's prohibition
  needs no amendment. §26.8(7) carries a supersede pointer and is **not** rewritten (§26.7).
- **`BookComponentStandard` v01.10.0 → v01.12.1.** New **§1.1 Precedence** (RoboLore upstream on
  brand values; this standard applies and may not redefine; unruled space may be ruled book-locally
  and marked provisional). New **§5.0.2 Depicted physical colour** (DJ ruling: a colour on a real
  object is drawn in the palette, the real colour stated in prose).
- **`ROBOCUP_RESCUE_LINE_2026.md` §2.1a — the ramp contradiction, recorded not ruled.** §5.6.1 says
  10 points per ramp; §3.7.4 says per ramp tile. A three-tile ramp is 10 or 30 points depending on
  which line the referee reads. Unresolved upstream across at least two editions. The doc had
  stated one side as settled fact.

## Book

- **L14 v02.16.0** — `L14_GRAPHIC_14-05_tile_patterns.svg` (new, 9 tiles, original artwork) wired
  into §3.3, plus the scoring table's ramp row corrected to name the contradiction.
- **L02 v03.7.0** — `2-05` gained the **FUNCTION PROTOTYPES** row its caption already named;
  download button repointed from the missing PDF to the corrected SVG.
- **`10-02`** overflow fixed (GPT) · **`10-01`** correct at 201,315 B · **`11-02`** 1,724,271 →
  **263,221 B** via `fit_raster_svg --write` then `flatten_alpha --write`, and its
  *"Widest LEGAL gap"* label corrected to *"Gap on the demo course"* (the rules allow 20 cm; L11's
  prose already called 10 cm the demo value).

---

# STANDING QUEUE

## Mechanical, measured, nobody has done it

**41 unsafe font stacks across 26 files** — `Inter` 13, `Consolas` 9, `Segoe UI` 7,
`JetBrains Mono` 7, ArialMT variants 5. **Both canons already forbid these**
(`Brand_Identity_Record` lines 1025–1027 reject designer-font-first stacks inside Zumo-book SVGs,
for our exact reason: figures load through `<img src>` and cannot fetch webfonts). Reordering is
visually neutral for every reader — the browser already falls back. **The single biggest dent
available: 41 of 106 open findings.**

Other mechanical: 6 plain `href` · 4 dead alpha channels · 5 photo resolution/aspect ·
5 staged files over the gate-37 ceiling (unreferenced, not fatal).

## The paint arc — untouched, every figure re-measured at S102 close

1. **Design the semantic set.** 27 distinct 4px accents for 30 families; §8 documents 11. Unruled,
   not forbidden. **Not started.**
2. Re-derive `BookComponentStandard` §5.0 from the five — **derive, never hand-patch** (that is S91).
3. Gradient generate: **134 instances, 7 distinct strings, 17 pages, 18 SVG files**.
   DJ has **not** ruled flatten-now vs. flatten-with-repaint. **Ask before sweeping.**
4. **`#f8f9fa` — 641 instances.** Cool grey on what will be a warm page. Still the largest unruled
   surface in the book, and still nobody has looked at it. `#fffbe6` — 87.
5. Code-palette drifts: `#4ec9b6` **294** (should be `#4EC9B0`), `#f14c4c` **14** (retires to
   `#D46554`). *S101 published 295 and 136; the live tree measures 294 and 150 for `#9b59b6` — two
   S101 counts do not reproduce.*
6. **9 roster rows still not activated** — carried since S94.
7. **The mark library is still entirely unwired** — 41 marks, **0** references across 21 pages.

## Instrument work

- `pill_sweep` and `gen_part_banners` still have no selftest.
- `_ctm` still discards `rotate()`/`matrix()` — v1.19 refuses to measure rotated text rather than
  fixing the transform. **6 `<text>` across 4 files (5-07, 6-11, 8-1, 10-07) are unchecked.**
  Full rotated-AABB support is the real fix.
- Re-run `regex_audit` after any parser edit.

## Images — the deadline path

**SEPTEMBER 8 IS FIVE WEEks OUT.**

The S33 `IMAGE_SHOT_LIST.md` is **stale**; each lesson's Image Index Status column is the better
record: **15 images + 3 videos** outstanding, not 21. Several rows are satisfied by graphics under
different names and were never re-statused (2.2 by `1-10`, 7.3 by `7-15`, 7.13 likely by `7-16`).

- **Cheapest real progress:** 5 L07 assets I can build — tab bar, Go-to-Definition menu, wrong-folder
  tree, and two error states using **authentic GCC diagnostics** (verified: compiling broken code
  in the sandbox reproduces the exact wording, caret and gutter). That clears L07 entirely.
- **Genuinely DJ's:** 2.5, 3.2, 3.4, 3.5, 3.6, 4.1, 4.3 + 3 videos — robot, bench, terminal, venue.
- **4.3 re-specified:** not poster board. **Two or three 30 cm white hardboard tiles butted
  together** with one black electrical-tape line, shot square-on so the seam shows. The seam is the
  point — it teaches modularity and the ≤3 mm step. DJ will shoot this.
- **No start-tile marking exists in the rules.** The goal tile is the only marked one (25 mm ×
  300 mm red strip). Worth a sentence in L14.
- `Line_Rescue_Field_Ariel.jpeg` (599×333 — **0.54× against §17.3b's 2× floor**, needs a larger
  source) and `Sample_Robo_Tile.png` are keepers per DJ but both are **RCJ committee artwork with
  unresolved provenance**, and both are orphans. `9-3` credits Pololu; the pattern exists.

## Canon debts

§21.1's thresholds live only in `book_gates.py` · §25.6 header example · §25.10e misfiled ·
challenge-card redesign Part B · difficulty-progression audit (DJ's stated big goal) · Maker batch ·
L01 VS Code multi-root step · Stage Two (S95) two blocks labelled `Learn/Insight`
(L03:3636, L09:1342) · `PUSH_WORKFLOW.md` — **unanswered: is the CLI-for-adds/modifies,
Desktop-for-deletions split Zumo-only or global?** · TDP template v3 re-commit ·
**`ROBOLORE_UPSTREAM_DELTA_S102.md` is written and unapplied** — one upstream edit now, not eight.

## Bench (need the robot)

Q017 L09 six numbers · Q044 calibration-spin · Q046 gyro-bias · L02 §5 green-LED ·
Constrain RUN_MS · **cm/s at a stated BASE_SPEED** — note 11-02 publishes 25 cm/s, while L11's own
formula (`speed ÷ 400 × 65`) gives **24.38** at BASE_SPEED 150. The graphic's conclusion is
ratio-based and survives either way; the two ms figures do not.

---

# PUSHING — READ THIS

**Three pushes silently failed in S102**, and one carried five unintended files plus a deletion
nobody decided on. Named-file CLI for adds and modifies; **GitHub Desktop for deletions**, where
seeing the checkbox is the point:

```
cd /path/to/zumo
git add <named files>
git commit -m "..."
git push
```

Never `git add .` — that is how `ZUMO_S101_HANDOFF.md` came back from the dead, how two
unprovenanced images arrived, and how `L02_GRAPHIC_2-05_sketch_anatomy.pdf` disappeared.

**Verify every push by fresh clone and md5. Then run `site_parity.py`.**

---

# PUSH LIST FOR THIS SESSION'S CLOSE

| Action | File | Note |
|---|---|---|
| upload | `book_gates.py` | **v1.34.5** — §21 now walks non-image references too |
| upload | `flatten_alpha.py` | **v1.2** — control 2 skips loudly instead of aborting |
| upload | `session_versions.py` | **v1.9.1** — two emit lines printed literal `\n` |
| upload | `ZUMO_S103_HANDOFF.md` | this file |
| upload | `LIVE_ZUMO_TEXTBOOK.md` | **regenerate LAST**, versions EMITTED not typed |
| **delete** | `ZUMO_S102_HANDOFF.md` | §12.2 — exactly one handoff in root, gate 28 enforces it |

⚠️ The deletion is a separate checkbox in GitHub Desktop. After pushing: fresh clone,
`python3 book_gates.py` → **40/40**, and `python3 site_parity.py` → **PARITY**.
