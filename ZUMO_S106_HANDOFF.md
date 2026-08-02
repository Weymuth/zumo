# ZUMO — S106 HANDOFF (written at S105 close · paste at top of Session 106)

## Session open ritual (do this without being asked)
1. `git clone --depth 1 https://github.com/Weymuth/zumo.git`
2. Read `LIVE_ZUMO_TEXTBOOK.md` — verify date / status / versions.
3. **Do NOT grep the Bible version.** `session_versions.bible_consistency()` parses it and
   checks the header, the `Current:` field and the newest changelog entry against each other.
4. Run: `book_gates.py` · `gen_component.py --selftest` · `lesson_inventory.py` ·
   `lesson_inventory.py --anomalies` · `pill_sweep.py --audit lessons/Lesson_*.html` ·
   `build_family_map.py` · `fit_raster_svg.py --selftest` · `flatten_alpha.py --selftest` ·
   `svg_layout_audit.py --selftest images/L01_GRAPHIC_1-13_zumo_rear_view.svg` ·
   `regex_audit.py --selftest` then `regex_audit.py` · `build_worklist.py --selftest` ·
   `font_stack_sweep.py --selftest` then `font_stack_sweep.py` ·
   `session_versions.py --selftest` then `session_versions.py --check` ·
   `site_parity.py --selftest` then `site_parity.py` ·
   `build_css.py --selftest` then `--check` · `image_audit.py --selftest` then `--check` ·
   **NEW S105:** `strip_inline.py --selftest` then `strip_inline.py --verify`.
5. If `flatten_alpha --selftest` prints `NOT FULLY TESTED`: `pip install cairosvg
   --break-system-packages` and re-run.
6. `--anomalies` is SILENT when clean. Anything it prints is a real lead.
7. **Do not hand-type a version.** `session_versions.py --live` / `--handoff` EMIT the blocks.
8. Entrypoints are traps: `lesson_inventory.build(path)`, `gen_component.load_standard()`,
   `svg_layout_audit.audit(path)`, `flatten_alpha.flatten(path)`, `build_worklist.build(dir)`,
   `regex_audit.audit(paths)`, `session_versions.bible_consistency(path)`,
   `build_css.build(paths)`, `image_audit.audit(paths)`, `strip_inline.build(paths)`.
9. **A CLONE IS NOT THE SITE.** Run `site_parity.py` after any push.
10. **VERIFY THE PUSH BY FRESH CLONE AND MD5**, and run `session_versions.py --selftest`
    immediately after.

---

# STATE

Fresh-clone verified at **`c95ed32`**. Census **39,994**.
Bible **v8.94** · `BookComponentStandard` **v01.12.1** · Maker **v2.45.1** ·
`marks/` **41** · `icons/` **49** incl. LICENSE.
`ZUMO_Syllabus_WORKING.md` **v1.0**.

Instruments: `book_gates` **v1.35.2** · `lesson_inventory` **v1.2.0** ·
`gen_component` **v1.6.1** · `pill_sweep` **v1.0** · `gate_payload_match` **v1.6** ·
`build_family_map` **v1.1.3** · `build_mark_index` **v1.0.2** · `gen_bonus_banner` **v1.2.1** ·
`gen_part_banners` **v1.0** · `session_versions` **v1.14.1** · `fit_raster_svg` **v1.2** ·
`flatten_alpha` **v1.2** · `svg_layout_audit` **v1.19** · `site_parity` **v1.1** ·
`build_css` **v1.2.1** ·
`image_audit` **v1.1** ·
`strip_inline` **v1.1** ·
`build_worklist` **v1.1** ·
`regex_audit` **v1.0** ·
`font_stack_sweep` **v1.0** ·
`going_deeper` **v01.1.1**.

Lessons: L01 v03.15.5 · L02 v03.7.3 · L03 v03.20.3 · L04 v04.15.3 · L05 v04.15.3 · L06 v04.19.4 · L07 v04.16.3 · L08 v04.14.3 · L09 v05.12.3 · L10 v02.11.3 · L11 v02.12.3 · L12 v01.14.3 · L13 v02.12.3 · L14 v02.16.3 · L15 v02.11.5 · L16 v02.7.3.

**42/42 gates · seven controls · every lesson converted.** Census 39,979 → **39,994**
(+15, the fifteen `<link>` lines).

---

# THE ONE THING TO CARRY OUT OF S105

**When a whole class of gates fails at once, fix the generator — not the instances.**

§4.5 and §4.5a failed on the first conversion attempt, and the obvious move was to add the
bonus banner to the hold list. That would have worked, and it would have been wrong: the
handoff named four held block types, the bonus banner was a fifth, and nothing said there
wasn't a sixth. The actual cause was one line — `canon()` sorts declarations for grouping,
which is correct, and the emitter was reusing that sorted form for OUTPUT, which is not.
`build_css.preferred()` emits authored order instead. One rule replaced an open-ended hold
list, and 23,364 of 23,886 attributes now round-trip byte-exact through the expander.

**Holding blocks until the gates go green is §24.8 wearing a hard hat.**

**And three controls in two sessions have now expired on success.** S104 found two in
`build_css`. S105 found `session_versions`'s CONTROL A seeding its corruption with the
literal string `Lesson version: v03.20.0` — the moment L03 bumped, the seed matched nothing,
nothing was corrupted, and nothing surfaced. It **failed loudly rather than passing silently**,
which is the right direction for the wrong reason. Seeds are patterns now, with an assert that
something was actually seeded.

---

# S105 WORK

## The migration — all sixteen lessons

- **24,412** inline attributes converted · **624 held** (39 per lesson, every lesson) ·
  24,412 + 624 = **25,036**, the §27 census exactly · **0 unmapped, 0 dead classes**.
- **Render identity proved twice.** By construction (every class carries declarations
  canonically equal to the string it replaced), then **independently**: 25,036 styled
  elements compared in document order against the pre-conversion tree — declaration sets
  identical, visible text identical apart from one `<link>` line per lesson.
- Lesson bytes **3,534,934 → 2,638,947**, 25% smaller; 23% counting the 81,806 B stylesheet.
- `css/book.css`: **167 → 664 rules**.

## The three hazards, all measured, all now canon (§27.8a–c)

- **(a) Widening `SOURCES` renames rules.** 57 of L01's 167 names changed meaning and
  **46 kept their spelling** — `.link-c-2e86ab` and its `-2` sibling swapped bold for
  non-bold. Only the 11 that vanished were visible to gate 41. **Every converted lesson must
  be re-stripped whenever `SOURCES` changes.**
- **(b) The order is forced.** `expand_classes` reads the stylesheet from disk and leaves an
  unresolvable class in place rather than failing, so regenerating before restoring strands
  74 L01 elements permanently. **restore → regenerate → apply.** Proved the hard way in a
  sandbox that had to be thrown away.
- **(c) `canon()` sorts; the gates assert authored order.** See above.

## Instruments

`strip_inline` **v1.0 NEW** — `--plan` / `--apply` / `--restore` / `--verify` / `--selftest`,
eight controls. Never invents a class: no rule means the attribute is left alone and
**reported**, and a non-zero unmapped count is exit 1. Held blocks located **by marker, never
by offset**. **CONTROL H** is the load-bearing one: marker-derived locators independently
reproduce S104's hand-picked 39 held attributes in L01 — two unrelated processes, same number.
**CONTROL G** encodes hazard (b).

`build_css` **v1.2** — `SOURCES` widened to all 16, `preferred()` added, all three hazards
documented in the file header.
`session_versions` **v1.14.1** — pattern seeding, `strip_inline` registered.

---

# THE MIGRATION — WHAT REMAINS

1. ~~The held blocks~~ — **DONE S105.** Zero inline styles remain book-wide.
2. **§26's repaint**, which is what all of this was for. `#f8f9fa` 641 · `#fffbe6` 87 ·
   `#4ec9b6` 294 → `#4EC9B0` · `#f14c4c` 14 → `#D46554` · 9 roster rows · 41 marks unwired ·
   LEARN/INSIGHT still sharing `#e3f2fd`/`#2196f3` · KEY TERM's purple colliding with MY PLAN.
   **Now a stylesheet edit, not a 25,000-attribute sweep.**
3. ~~473 absolute links~~ — **DONE S105.** 496 converted; the book is domain-agnostic.
4. **Class names are provisional.** The semantic set (27 accents / 30 families) is not
   designed. Renaming costs one line in the generator plus a re-emit — but see hazard (a):
   a re-emit means a re-strip.

---

# IMAGES — THE DEADLINE PATH

**SEPTEMBER 8 IS FIVE WEEKS OUT.** `IMAGE_WORKLIST.md` is generated and authoritative;
`IMAGE_SHOT_LIST.md` is stale and should be retired or regenerated.

**20 outstanding of 145 planned — 16 images + 4 videos. All 16 are DJ's:**
L02 2.2 · 2.5 · L03 3.2 · 3.4 · 3.5 · 3.6 · 3.14 · L04 4.1 · 4.3 · L12 12.1 · L13 13.1 · 13.2 ·
L14 14.1 · 14.2 · L16 16.1. Videos: 3.1 · 4.1 · 6.1 · 8.1.

**Flagged, needs a ruling:** `[IMAGE 7.13]` reads *"Diagram showing final project structure"* —
a diagram tagged as a photo — but L07 already ships `GRAPHIC 7-15 platformio_file_tree` and
`GRAPHIC 7-16 eight_file_architecture`. May be redundant rather than mistyped. **Do not draw a
third file tree without DJ.**

**From GPT's S104 asset audit, still open:** the divergent duplicate
`lessons/L01_GRAPHIC_1-10_zumo_hardware_labeled.svg` (different bytes from the `images/` copy,
seen by no gate); the **2.07 three-way collision**; **30 unreferenced files** in `images/`
including five `ChatGPT Image ….png` and a stray `README.md`. Its 147-row branding arc is
post-Sept-8 work.

---

# STANDING QUEUE

## Parked with a price (do not re-derive)

- **IMAGE + GRAPHIC → one FIGURE space** — DJ: *"revisit after the 8th."* Full entry in
  `ZUMO_PARKED_EXIT_ITEMS.md`.
- Gradients: 134 instances, 7 strings, 17 pages, 18 SVGs. **DJ has not ruled flatten-now vs
  flatten-with-repaint.**
- The Consolas-first code stacks: **400 in lessons, 2 in `book.css`, 16 Segoe UI-first.** The
  migration has now collapsed L01's share into shared rules. **One stylesheet edit at repaint.**

## Mechanical, measured

6 plain `href` · 4 dead alpha · 5 photo resolution/aspect · 5 staged files over the gate-37
ceiling · the divergent `lessons/` duplicate · the 2.07 collision · 30 unreferenced files.

## Instrument work

- `pill_sweep` and `gen_part_banners` still have no selftest.
- `_ctm` still discards `rotate()`/`matrix()`; `regex_audit` reports 1 lead across 23 files
  (23 not 22 only because `strip_inline.py` entered scope).
- **Offered and not yet ruled:** a gate failing on any root file matching `PUSH_ME*` / `MD5*` /
  `* (1)*`.
- **New, worth considering:** a gate asserting `build_css --check` and `strip_inline --verify`
  are clean, so a stylesheet regenerated without a re-strip cannot ship (hazard a).

## Canon debts

§21.1's thresholds live only in `book_gates.py` · §25.6 header example · §25.10e misfiled ·
challenge-card redesign Part B · difficulty-progression audit · Maker batch · L01 VS Code
multi-root step · Stage Two two blocks labelled `Learn/Insight` (L03, L09) ·
`ROBOLORE_UPSTREAM_DELTA_S102.md` written and unapplied · robolore.com hosting.

## Bench (need the robot)

Q017 L09 six numbers · Q044 calibration-spin · Q046 gyro-bias · L02 §5 green-LED ·
Constrain RUN_MS · cm/s at a stated BASE_SPEED.

---

# PUSHING — READ THIS

Named-file CLI for adds and modifies; **GitHub Desktop for deletions.** **Never `git add .`**

**md5 every staged file against the list in chat before committing.** A `(1)` in a filename is
the tell of a stale browser download. **Matched pairs must ship together** — see
`PUSH_WORKFLOW.md`. Here the matched set is unusually wide: **`css/book.css` and all 16 lessons
are one atomic unit.** Shipping the stylesheet without the lessons, or any subset of the
lessons, leaves classes pointing at rules that changed meaning — and gate 41 will not see it.

---

# PUSH LIST FOR THIS SESSION'S CLOSE

| Action | File | Note |
|---|---|---|

| upload | `lessons/Lesson_01.html` … `Lesson_16.html` | all 16, converted, minor-bumped |
| upload | `book_gates.py` | **v1.36** — 42 gates; NEW gate 42 (§27.10) |

| upload | `session_versions.py` | **v1.14.1** |
| upload | `ZUMO_SUPER_BIBLE.md` | **v8.94** — §27.8, §27.9, §27.10 |
| upload | `ZUMO_S106_HANDOFF.md` | this file |
| upload | `LIVE_ZUMO_TEXTBOOK.md` | **regenerate LAST**, versions EMITTED not typed |
| **delete** | `ZUMO_S105_HANDOFF.md` | §12.2 — gate 28 enforces exactly one |
