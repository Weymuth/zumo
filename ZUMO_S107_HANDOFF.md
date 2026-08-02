# ZUMO — S107 HANDOFF (written at S106 close · paste at top of Session 107)

## Session open ritual (do this without being asked)
1. `git clone --depth 1 https://github.com/Weymuth/zumo.git`
2. Read `LIVE_ZUMO_TEXTBOOK.md` — verify date / status / versions.
3. **Do NOT grep the Bible version.** `session_versions.bible_consistency()` parses it.
4. Run: `book_gates.py` · `gen_component.py --selftest` · `lesson_inventory.py` ·
   `lesson_inventory.py --anomalies` · `pill_sweep.py --audit lessons/Lesson_*.html` ·
   `build_family_map.py` · `fit_raster_svg.py --selftest` · `flatten_alpha.py --selftest` ·
   `svg_layout_audit.py --selftest images/L01_GRAPHIC_1-13_zumo_rear_view.svg` ·
   `regex_audit.py --selftest` then `regex_audit.py` · `build_worklist.py --selftest` ·
   `font_stack_sweep.py --selftest` then `font_stack_sweep.py` ·
   `session_versions.py --selftest` then `session_versions.py --check` ·
   `site_parity.py --selftest` then `site_parity.py` ·
   `build_css.py --selftest` then `--check` · `image_audit.py --selftest` then `--check` ·
   `strip_inline.py --selftest` then `strip_inline.py --verify`.
5. If `flatten_alpha --selftest` prints `NOT FULLY TESTED`: `pip install cairosvg
   --break-system-packages` and re-run. **Needed every session — it was needed at S106 open.**
6. `--anomalies` is SILENT when clean. Anything it prints is a real lead.
7. **Do not hand-type a version.** `session_versions.py --live` / `--handoff` EMIT the blocks.
8. Entrypoints are traps: `lesson_inventory.build(path)`, `gen_component.load_standard()`,
   `svg_layout_audit.audit(path)`, `flatten_alpha.flatten(path)`, `build_worklist.build(dir)`,
   `regex_audit.audit(paths)`, `session_versions.bible_consistency(path)`,
   `build_css.build(paths)`, `image_audit.audit(paths)`, `strip_inline.build(paths)`.
9. **A CLONE IS NOT THE SITE.** Run `site_parity.py` after any push.
10. **VERIFY THE PUSH BY FRESH CLONE AND MD5.**

---

# STATE

Fresh-clone verified at **`a15c277`**. Census **39,993**.
Bible **v8.96** · `BookComponentStandard` **v01.12.1** · Maker **v2.45.1** ·
`marks/` **41** · `icons/` **49** incl. LICENSE.
`ZUMO_Syllabus_WORKING.md` **v1.0**.

Instruments: `book_gates` **v1.38.2** · `lesson_inventory` **v1.2.0** ·
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

Lessons: L01 v03.15.5 · L02 v03.7.4 · L03 v03.20.3 · L04 v04.15.3 · L05 v04.15.3 · L06 v04.19.4 · L07 v04.16.3 · L08 v04.14.3 · L09 v05.12.3 · L10 v02.11.3 · L11 v02.12.3 · L12 v01.14.3 · L13 v02.12.3 · L14 v02.16.3 · L15 v02.11.5 · L16 v02.7.3.

**45/45 gates.** Two new: §27.12 and §27.13.

---

# THE ONE THING TO CARRY OUT OF S106

**THE INSTRUMENTS CHECKED THE FIRST FACE IN A FONT STACK AND NOTHING ELSE.**

`font_stack_sweep` reported 0 rewrites and `svg_layout_audit` reported CLEAN on a file
Illustrator refused to open. The offending name — `Consolas`, Windows-only — was sitting in
**position two** of `"Courier New", Consolas, monospace`, and both instruments read position
one and stopped. DJ found it by double-clicking; no gate in the repo could.

The same blindness hides a second shape: `font-family: "Courier New, monospace", ...` inside a
`<style>` block is a request for a single font **literally named** `Courier New, monospace`.
Its first face is spelled with the right letters, so it passes. **14 declarations in 7 files
were in that state** and every one of them was live.

**And DJ was double-clicking a file no gate could see.** Two orphan SVGs sat in `lessons/` —
copies of `images/` files, referenced by nothing, therefore invisible to §21. The L02 one was
the PRE-FIX copy. The fix shipped three times and the error kept appearing because the file
being opened was not the file being fixed. Deleted at S106 close. `image_audit` was the only
instrument that ever saw them, and only because it compares bytes rather than following refs.

**A file that nothing references is not thereby harmless. It is a file no instrument checks.**

---

# S106 WORK

## Two new gates, both control-run in both directions

- **§27.12 / gate 44 — no converted page carries an inline `style=`.** Seeding one
  `<p style="color: #ff00aa">` into L05 left **all 43 preceding gates green**, and the element
  renders correctly while doing it. Scope keyed on the `<link>`, the §25.6a rule.
  **It caught a real mistake on its first day**: `strip_inline --apply` was run without
  `--include-held`, restoring 624 held attributes as inline and leaving them there. Not a
  seeded control — an actual error, caught before it shipped.
- **§27.13 / gate 45 — `css/book.css` regenerates byte-identically from the lessons.**
  The guard on §27.8a/b that a repaint cannot spend. Gate 43 catches a hand-edited stylesheet
  and is blind to a lesson-side desync; 45 is the reverse. **Neither subsumes the other.**
  `strip_inline --verify` was OFFERED and NOT added: it computes gate 41's assertion twice and
  never fired independently of it across four controls.

## L02 IMAGE 2.2 — built, wired, outstanding 20 → 19

DJ shot the figure; it arrived 2.4 MB with an alpha PNG payload, Arial-first-by-PostScript-name
fonts, and the L01 template's filename still baked into its own footer. `flatten_alpha` →
`fit_raster_svg` → `font_stack_sweep` took it to **433 KB** under the 500 KB ceiling.
Redesigned against GPT's proposal: badges carry **A B C** instead of 1 2 3, per-button
Position lines, a Position mapping box, an `In your code` panel and an `Asking a button`
panel. `Middle` → `Center` because L02 ships `// Center button`.

**Wiring it forced the full §27.8b cycle.** Adding one figure changed class usage, which
changed `build_css`'s frequency ranking, which desynced the stylesheet — gate 45 red.
**restore → regenerate → apply --include-held.** Blast radius when run correctly: **one
lesson.** `css/book.css` reordered two rules and dropped `.div-2196f3`, whose last use in the
book was that placeholder. §21 coverage 223→224, §27.11 digest moved; counts did not.

## The font sweep

- `Consolas` removed book-wide. **0 SVGs name it.**
- The 14 bogus quoted families killed in 7 files (`L02 2-04` · `2-09` · `L04 4-04` · `4-05` ·
  `L06 6-02` · `6-03` · `L16 16-03`).
- **§17.3c: five staged rasters carried a plain `href`** — Illustrator reports MISSING LINK and
  the file cannot be edited. Converted to `xlink:href` with `xmlns:xlink` declared
  (`L02 2-07 r02` · `r13` · `L05 5-08` · `5-09` · `5-10`). **This was the only real failure;
  everything else was a dismissable dialog.**
- All 13 SVG edits proved **pixel-identical** by render-diff.

## Three findings I nearly shipped wrong

1. **"84 files missing a viewBox"** — the test read the first `>` in the file, which is the XML
   declaration. Corrected: **0**.
2. **"65 files with a bogus font family"** — counted string matches, not declarations. In an
   *attribute*, `font-family="Courier New, monospace"` is valid (the quotes are XML). **57 of
   the 65 needed nothing.** Real number: 7.
3. **"Naming Helvetica triggers the dialog"** — falsified by probe. `FONT_PROBE_A`
   (`Arial, Helvetica, sans-serif`) and `FONT_PROBE_B` (`Arial, sans-serif`) BOTH opened
   silently. **A 99-file sweep avoided by two throwaway files.** Cost: the probes were staged
   in the same download list as real deliverables and got pushed into `images/`; gate 21.2
   caught them (181 vs 179) and they were deleted next push. **Test files must never be
   presented alongside repo files.**

---

# OPEN — THE HELVETICA DIALOG

Unresolved and **parked by recommendation**. It is a warning, not a failure: click OK and the
file opens. Two hypotheses remain untested — `FONT_PROBE_C_weight500` / `D_weight700` were
built and never run.

**The leading candidate: 22 files request font-weight 500, 600 or 800**, and macOS Helvetica
has faces only for 400 and 700, which matches the dialog's wording ("in a different format
than originally specified"):
`L01 1-11` · `L02 2-04` · `2-07 ir_sensors` · `2-08` · `2-09` · `2-07 r13` · `L04 4-04` ·
`4-05` · `L05 5-01` · `5-07` · `5-08` · `5-09` · `5-10` · `L06 6-02` · `6-03` · `6-04` ·
`6-05` · `L12 12-02` · `12-03` · `L13 13-01` · `13-02` · `L16 16-03`.

Second: **33 SVGs contain glyphs Helvetica lacks** (`→ ⚡ ✅ ✓ ✗ 👁 ▲ ▼ •`). Browsers render
these from the system emoji font, so students are fine; Illustrator shows them missing.

**Do not chase this before September 8.**

---

# IMAGES — THE DEADLINE PATH

**SEPTEMBER 8 IS FIVE WEEKS OUT.** `IMAGE_WORKLIST.md` is generated and authoritative.

**19 outstanding of 145 — 15 images + 4 videos, all DJ's.** Cross-referenced against
`ZUMO_Teacher_Daily_Grid_WORKING.md`, they are NOT evenly urgent:

| Due | Items | Count |
|---|---|---|
| **Periods 2–4 (week 1)** | 2.5 · VIDEO 3.1 · 3.2 · 3.4 · 3.5 · 3.6 · 3.14 | **7** |
| Period 5 (week 2) | 4.1 · VIDEO 4.1 · 4.3 | 3 |
| Periods 7–11 (wks 3–4) | VIDEO 6.1 · 7.13 · VIDEO 8.1 | 3 |
| Period 19 (week 7) | 12.1 | 1 |
| **Winter trimester** | 13.1 · 13.2 · 14.1 · 14.2 · 16.1 | **5** |

**Seven figures are the September 8 deadline.** The winter five are not Sept-8 work at all.

Cheapest item on the list: **`[IMAGE 7.13]`** reads *"Diagram showing final project structure"*
— a diagram tagged as a photo — while L07 already ships `GRAPHIC 7-15 platformio_file_tree` and
`GRAPHIC 7-16 eight_file_architecture`. **One ruling may delete a row rather than draw a third
file tree.** Do not draw it without DJ.

**Offered at S106 and not built:** a shot brief for the seven week-one figures — each tag's
surrounding prose, what the lesson claims the reader is looking at, framing and props — so one
bench session with the robot clears all seven.

---

# STANDING QUEUE

## Instrument work — the S106 lesson made these concrete

- **`font_stack_sweep` reads only the first face.** Teach it to check EVERY named face and to
  reject a quoted family containing a comma. Right now nothing in the repo can see either
  defect. **Offered, not ruled.**
- **A gate asserting `build_css --check` and `strip_inline --verify` are clean** — superseded
  by gates 44/45. Closed.
- **A gate failing on any root file matching `PUSH_ME*` / `MD5*` / `* (1)*`** — still offered,
  still unruled, and S106 pushed two `FONT_PROBE` files by exactly this mechanism.
- `pill_sweep` and `gen_part_banners` still have no selftest.
- `_ctm` still discards `rotate()`/`matrix()`; `regex_audit` reports 1 lead across 23 files.
- **A gate on orphan copies in `lessons/`** — new. `image_audit` sees them; nothing fails.

## Parked with a price (do not re-derive)

- **§26's repaint.** `#f8f9fa` 641 · `#fffbe6` 87 · `#4ec9b6` 294 → `#4EC9B0` · `#f14c4c` 14 →
  `#D46554` · 9 roster rows · 41 marks unwired · LEARN/INSIGHT sharing `#e3f2fd`/`#2196f3` ·
  KEY TERM's purple colliding with MY PLAN. **Now a stylesheet edit.** Note: it moves gate 43's
  baseline, and the moment it does, gate 45 is the only guard left on hazard (a).
- **IMAGE + GRAPHIC → one FIGURE space** — DJ: *"revisit after the 8th."*
- Gradients: 134 instances, 7 strings, 17 pages, 18 SVGs. **Unruled.**
- **Consolas in `css/book.css`: 15 declarations.** Browser CSS, harmless — a browser falls back
  silently. One stylesheet edit at repaint. **Not the Illustrator problem.**
- Class names are provisional; the semantic set (27 accents / 30 families) is not designed.
  A re-emit means a re-strip (§27.8a).

## Mechanical, measured

6 plain `href` in lessons · 4 dead alpha · 5 photo resolution/aspect · **5 staged files over
the gate-37 ceiling** (the same five just xlink-fixed: 0.6–2.9 MB, fatal the moment a lesson
wires one in) · the 2.07 three-way collision · 30 unreferenced files in `images/` including
five `ChatGPT Image ….png` and a stray `README.md`.

## Canon debts

§21.1's thresholds live only in `book_gates.py` · §25.6 header example · §25.10e misfiled ·
challenge-card redesign Part B · difficulty-progression audit · Maker batch · L01 VS Code
multi-root step · Stage Two two blocks labelled `Learn/Insight` (L03, L09) ·
`ROBOLORE_UPSTREAM_DELTA_S102.md` written and unapplied · robolore.com hosting ·
**`PUSH_WORKFLOW.md`: a repeat download of the same repo filename makes `(1)` the NEW file,
not the stale one** — offered at S106, not written.

## Bench (need the robot)

Q017 L09 six numbers · Q044 calibration-spin · Q046 gyro-bias · L02 §5 green-LED ·
Constrain RUN_MS · cm/s at a stated BASE_SPEED.
**CLOSED S106:** badge order on IMAGE 2.2 — DJ confirmed **1=A · 2=B · 3=C**.

---

# PUSHING — READ THIS

Named-file CLI for adds and modifies; **GitHub Desktop for deletions.** **Never `git add .`**

**md5 every staged file against the list in chat before committing.**

**S106 cost four pushes to download-folder ambiguity. Two rules came out of it:**
1. **`(1)` does not mean stale.** Downloading the same repo filename twice in one session makes
   the `(1)` copy the NEW one. Verify by **md5**, never by suffix. S106 lost a push to deleting
   the `(1)` and shipping the leftover.
2. **Never present a test file in the same list as repo files.** Two `FONT_PROBE` SVGs were
   marked *do not push* in prose and got dragged in anyway. Gate 21.2 caught them. If a file
   must not reach the repo, it must not sit next to files that must.

---

# PUSH LIST FOR THIS SESSION'S CLOSE

| Action | File | Note |
|---|---|---|
| **delete** | `lessons/L01_GRAPHIC_1-10_zumo_hardware_labeled.svg` | orphan copy, referenced by nothing |
| **delete** | `lessons/L02_IMAGE_2-02_zumo_buttons_labeled.svg` | orphan copy — the PRE-FIX Consolas file DJ kept opening |
| upload | `IMAGE_WORKLIST.md` | regenerated; the `lessons/` duplicate section is gone |
| upload | `ZUMO_S107_HANDOFF.md` | this file |
| upload | `LIVE_ZUMO_TEXTBOOK.md` | **regenerate LAST**, versions EMITTED not typed |
| **delete** | `ZUMO_S106_HANDOFF.md` | §12.2 — gate 28 enforces exactly one |
