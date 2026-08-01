# ZUMO — S105 HANDOFF (written at S104 close · paste at top of Session 105)

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
   **NEW S104:** `build_css.py --selftest` then `--check` · `image_audit.py --selftest` then
   `--check`.
5. If `flatten_alpha --selftest` prints `NOT FULLY TESTED`: `pip install cairosvg
   --break-system-packages` and re-run.
6. `--anomalies` is SILENT when clean. Anything it prints is a real lead.
7. **Do not hand-type a version.** `session_versions.py --live` / `--handoff` EMIT the blocks.
8. Entrypoints are traps: `lesson_inventory.build(path)`, `gen_component.load_standard()`,
   `svg_layout_audit.audit(path)`, `flatten_alpha.flatten(path)`, `build_worklist.build(dir)`,
   `regex_audit.audit(paths)`, `session_versions.bible_consistency(path)`,
   `build_css.build(paths)`, `image_audit.audit(paths)`.
9. **A CLONE IS NOT THE SITE.** Run `site_parity.py` after any push.
10. **VERIFY THE PUSH BY FRESH CLONE AND MD5**, and run `session_versions.py --selftest`
    immediately after — S104 lost three pushes and CONTROL E caught the stray in seconds.

---

# STATE

Fresh-clone verified at **`95e1203`**. Census **39,979**.
Bible **v8.91** · `BookComponentStandard` **v01.12.1** · Maker **v2.45.1** ·
`marks/` **41** · `icons/` **49** incl. LICENSE.
`ZUMO_Syllabus_WORKING.md` **v1.0**.

Instruments: `book_gates` **v1.35.1** · `lesson_inventory` **v1.2.0** ·
`gen_component` **v1.6.1** · `pill_sweep` **v1.0** · `gate_payload_match` **v1.6** ·
`build_family_map` **v1.1.3** · `build_mark_index` **v1.0.2** · `gen_bonus_banner` **v1.2.1** ·
`gen_part_banners` **v1.0** · `session_versions` **v1.14** · `fit_raster_svg` **v1.2** ·
`flatten_alpha` **v1.2** · `svg_layout_audit` **v1.19** · `site_parity` **v1.1** ·
`build_css` **v1.1** ·
`image_audit` **v1.1** ·
`build_worklist` **v1.1** ·
`regex_audit` **v1.0** ·
`font_stack_sweep` **v1.0** ·
`going_deeper` **v01.1.1**.

Lessons: L01 v03.15.2 · L02 v03.7.0 · L03 v03.20.0 · L04 v04.15.0 · L05 v04.15.0 · L06 v04.19.1 · L07 v04.16.0 · L08 v04.14.0 · L09 v05.12.0 · L10 v02.11.0 · L11 v02.12.0 · L12 v01.14.0 · L13 v02.12.0 · L14 v02.16.0 · L15 v02.11.2 · L16 v02.7.0.

**41/41 gates · seven controls · PARITY.** Census 39,978 → **39,979** (+1, L01's `<link>`).

---

# THE ONE THING TO CARRY OUT OF S104

**Write controls for the world the change creates, not the world it leaves behind.**

Two of `build_css`'s controls died the moment run 2 landed — one counted raw `style="` in a source
that no longer has any, one asserted "zero class attributes exist," true during run 1 and false
forever after. **An assertion that expires on success is worse than none: it fails when you win.**

**And §24.8 twice more, both mine, both in controls written to prevent exactly this:**

- `image_audit`'s CONTROL E "proved" determinism by auditing twice **in one process**, where
  `PYTHONHASHSEED` is fixed and set order cannot vary. It passed on a generator that was not
  deterministic at all: `[IMAGE 4.1]` and `[VIDEO 4.1]` share the sort key `(4, 1, '')`, so their
  order fell out of set iteration and the written file disagreed with the next `--check` at
  random. E now runs three seeds in subprocesses.
- The first tag/filename sweep synthesised `src="{url}"` strings and fed them to the old regex.
  That tests the regex, not the hole. Two of three came back INCONCLUSIVE — the control refusing
  to claim a pass is the only reason it did not ship wrong.

**A plausible count is the dangerous kind.** The image audit's first pass reported **ten "type
mismatches"** — tag says IMAGE, a GRAPHIC file with that number exists — which looked exactly like
the L15 defect and would have justified a ten-lesson sweep. Reading all ten killed every one: §10
makes the spaces separate, and **L04 says so in its own prose**. §24.6c is not about sloppy greps;
it is about well-formed answers that are wrong.

---

# S104 WORK, BY LAYER

## The migration — Lesson 01 converted, end to end

- **Run 1 (infrastructure):** `css/book.css` + a `<link>` in L01. A no-op **by construction** —
  all 16 lessons carry 0 `class=` and 0 `<style>`, so class-scoped rules match nothing. Proved
  `css/` publishes, Pages serves `text/css`, `site_parity` covers it.
- **Run 2 (content):** 1,111 of 1,150 attributes → classes. **39 held** — the §6.5a strip (20),
  §25.6 hero (6) and footer (1), and the four §6.8 PART dividers (3 each) are compared byte-exact
  ACROSS lessons and must convert book-wide in one pass.
- **Render identity by construction**, not inspection: 1,150 elements in document order carry
  canonically equal declarations; visible text byte-identical. **204,356 → 154,731 B, −24%.**
- **One stylesheet, not sixteen** — 689 distinct strings, 92.5% of instances shared across
  lessons. `css/` not `images/` — the latter is seven instruments' declared scope.
- **`lesson_inventory.expand_classes()`** — six CSS-reading gates keep working in any conversion
  state; ONE function, not six edits (the S83 rule).
- **GATE 41 (§27)** — every class in use resolves to a rule. A typo'd class dropped L01's callout
  census 83→82 with all 40 gates green.

## Book / graphics

- **L15 v02.11.2** — `[IMAGE 15.x]` → `[GRAPHIC 15.x]` ×9, Image Index → Graphic Index,
  `id="image-index"` deliberately kept (gate keys on it). Reverse-substitution reproduces the
  pre-edit file byte-for-byte. A book-wide sweep then proved **L15 was the entire class**.
- **L07 v04.16.0 — CLEARED.** Five figures built, every diagnostic reproduced with g++ in the
  sandbox. Gate baselines moved deliberately: §21 218→223, §21.2 174→179.
- **`svg_layout_audit` cannot see a pointer aimed at the wrong thing** — 7-11's arrow landed on
  `RobotConfig.h` instead of the misplaced `RobotMotion.h` and the audit called it clean twice.
  Found by rendering and reading (§24.6a).

## Instruments

`build_css` **v1.1** (reads through the expander, so it regenerates from a converted lesson) ·
`image_audit` **v1.1** NEW · `book_gates` **v1.35.1** · `lesson_inventory` **v1.2.0** ·
`session_versions` **v1.14** · `site_parity` **v1.1** (three pre-existing scope holes closed:
tutor never scanned, no-slash refs, href-borne refs; the scope fix alone took the reference
count 128→131, and L07's five new figures took it to **137**. PARITY throughout).

---

# THE MIGRATION — 15 lessons to go

**Per-lesson cost, now measured rather than guessed.** L01: 168 distinct strings, **136 of them
used in other lessons too**. The ruleset is largely written; later lessons mostly reuse it.

**The order that remains:**

1. Convert L02–L16 the same way — `build_css.py` with `SOURCES` extended, then the strip.
2. **The held blocks, book-wide, in one generated pass** — strip / hero / footer / PART dividers.
   Cheapest conversion in the book: one block × 16 files, from generators that already exist.
3. Then §26's repaint, which is what this was all for. `#f8f9fa` 641 · `#fffbe6` 87 ·
   `#4ec9b6` 294 → `#4EC9B0` · `#f14c4c` 14 → `#D46554` · 9 roster rows · 41 marks still unwired.
4. **473 absolute links → relative**, after which the book is domain-agnostic.

---

# IMAGES — THE DEADLINE PATH

**SEPTEMBER 8 IS FIVE WEEKS OUT.** `IMAGE_WORKLIST.md` is generated and authoritative;
`IMAGE_SHOT_LIST.md` is stale and should be retired or regenerated.

**20 outstanding of 145 planned — 16 images + 4 videos.** All 16 are DJ's:
L02 2.2 · 2.5 · L03 3.2 · 3.4 · 3.5 · 3.6 · 3.14 · L04 4.1 · 4.3 · L12 12.1 · L13 13.1 · 13.2 ·
L14 14.1 · 14.2 · L16 16.1. Videos: 3.1 · 4.1 · 6.1 · 8.1.

**Flagged, needs a ruling:** `[IMAGE 7.13]` reads *"Diagram showing final project structure"* — a
diagram tagged as a photo — but L07 already ships `GRAPHIC 7-15 platformio_file_tree` and
`GRAPHIC 7-16 eight_file_architecture`. It may be redundant rather than mistyped. Do not draw a
third file tree without DJ.

**From GPT's S104 asset audit — three real finds, one false P0.** Real: a **divergent duplicate**
`lessons/L01_GRAPHIC_1-10_zumo_hardware_labeled.svg`, different bytes from the `images/` copy, seen
by no gate (§12/§23 governs .html only, `site_parity` only walks referenced assets); the **2.07
three-way collision** (`L02_IMAGE_2-07_oled_controls_screen.svg` live while r02, r13 and a GRAPHIC
2-07 sit unreferenced claiming the same number); and **30 unreferenced files** in `images/`
including five `ChatGPT Image …png` and a stray `README.md`. **False:** its P0 "restore every
Lesson 8–16 file" — all present, all references resolve, PARITY holds. Its 147-row branding arc
(44 branding-only, 30 photo-with-vector-labels, 3 true-vector rebuilds) is post-Sept-8 work.

---

# STANDING QUEUE

## Parked with a price (do not re-derive)

- **IMAGE + GRAPHIC → one FIGURE space** — DJ: *"revisit after the 8th."* 18 numbers used by both
  spaces, 12 colliding at file level, 126 files. Full entry in `ZUMO_PARKED_EXIT_ITEMS.md`.
- Gradients: 134 instances, 7 strings, 17 pages, 18 SVGs. **DJ has not ruled flatten-now vs
  flatten-with-repaint.**
- The 422 Consolas-first code stacks — one line in a stylesheet. **Do not sweep what the
  migration deletes.**

## Mechanical, measured

6 plain `href` · 4 dead alpha · 5 photo resolution/aspect · 5 staged files over the gate-37
ceiling · the divergent `lessons/` duplicate · the 2.07 collision · 30 unreferenced files.

## Instrument work

- `pill_sweep` and `gen_part_banners` still have no selftest.
- `_ctm` still discards `rotate()`/`matrix()`; 6 `<text>` across 4 files unchecked.
- **Offered and not yet ruled:** a gate failing on any root file matching `PUSH_ME*` / `MD5*` —
  and now also `* (1)*`, after S104 committed `lesson_inventory (1).py`.

## Canon debts

§21.1's thresholds live only in `book_gates.py` · §25.6 header example · §25.10e misfiled ·
challenge-card redesign Part B · difficulty-progression audit · Maker batch · L01 VS Code
multi-root step · Stage Two two blocks labelled `Learn/Insight` (L03:3636, L09:1342) ·
`ROBOLORE_UPSTREAM_DELTA_S102.md` written and unapplied · robolore.com hosting.

## Bench (need the robot)

Q017 L09 six numbers · Q044 calibration-spin · Q046 gyro-bias · L02 §5 green-LED ·
Constrain RUN_MS · cm/s at a stated BASE_SPEED.

---

# PUSHING — READ THIS

Named-file CLI for adds and modifies; **GitHub Desktop for deletions.** **Never `git add .`**

**md5 every staged file against the list in chat before committing.** S104 lost three pushes to
stale browser downloads, and one landed as `lesson_inventory (1).py`. A `(1)` in a filename is the
tell. **Matched pairs must ship together** — see `PUSH_WORKFLOW.md`.

---

# PUSH LIST FOR THIS SESSION'S CLOSE

| Action | File | Note |
|---|---|---|
| upload | `ZUMO_SUPER_BIBLE.md` | **v8.91** — §27.7 |
| upload | `PUSH_WORKFLOW.md` | matched pairs + verify-the-downloads |
| upload | `ZUMO_PARKED_EXIT_ITEMS.md` | the FIGURE entry |
| upload | `ZUMO_S105_HANDOFF.md` | this file |
| upload | `LIVE_ZUMO_TEXTBOOK.md` | **regenerate LAST**, versions EMITTED not typed |
| **delete** | `ZUMO_S104_HANDOFF.md` | §12.2 — gate 28 enforces exactly one |
