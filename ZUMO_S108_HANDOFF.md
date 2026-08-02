# ZUMO — S108 HANDOFF (written at S107 close · paste at top of Session 108)

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
   --break-system-packages` and re-run. **Needed every session — needed again at S107 open.**
6. `--anomalies` is SILENT when clean. Anything it prints is a real lead.
7. **Do not hand-type a version.** `session_versions.py --live` / `--handoff` EMIT the blocks.
8. Entrypoints are traps: `lesson_inventory.build(path)`, `gen_component.load_standard()`,
   `svg_layout_audit.audit(path)`, `flatten_alpha.flatten(path)`, `build_worklist.build(dir)`,
   `regex_audit.audit(paths)`, `session_versions.bible_consistency(path)`,
   `build_css.build(paths)`, `image_audit.audit(paths)`, `strip_inline.build(paths)`.
9. **A CLONE IS NOT THE SITE.** Run `site_parity.py` after any push.
10. **VERIFY THE PUSH BY FRESH CLONE AND MD5.**
11. **READ `ZUMO_S107_BANNER_RULINGS.md` BEFORE ANY BANNER WORK.** It is the authority
    for the entire typography/banner arc and none of it is applied yet.

---

# STATE

Fresh-clone verified at **`4d7695f`**. Census **39,993**.
Bible **v8.96** · `BookComponentStandard` **v01.12.1** · Maker **v2.45.1** ·
`marks/` **41** · `icons/` **49** incl. LICENSE.
`ZUMO_Syllabus_WORKING.md` **v1.0**.

Instruments: `book_gates` **v1.38.2** · `lesson_inventory` **v1.2.0** ·
`gen_component` **v1.6.1** · `pill_sweep` **v1.0** · `gate_payload_match` **v1.6** ·
`build_family_map` **v1.1.3** · `build_mark_index` **v1.0.2** · `gen_bonus_banner` **v1.2.1** ·
`gen_part_banners` **v1.0** · `session_versions` **v1.14.1** · `fit_raster_svg` **v1.2** ·
`flatten_alpha` **v1.2** · `svg_layout_audit` **v1.19** · `site_parity` **v1.1** ·
`build_css` **v1.2.1** · `image_audit` **v1.1** · `strip_inline` **v1.1** ·
`build_worklist` **v1.1** · `regex_audit` **v1.0** · `font_stack_sweep` **v1.0** ·
`going_deeper` **v01.1.1**.

Lessons: L01 v03.15.5 · L02 v03.7.4 · L03 v03.20.3 · L04 v04.15.3 · L05 v04.15.3 ·
L06 v04.19.4 · L07 v04.16.3 · L08 v04.14.3 · L09 v05.12.3 · L10 v02.11.3 · L11 v02.12.3 ·
L12 v01.14.3 · L13 v02.12.3 · L14 v02.16.3 · L15 v02.11.5 · L16 v02.7.3.

**45/45 gates.** **NO lesson or instrument version changed in S107.** The session produced
one root document and two deletions.

---

# THE ONE THING TO CARRY OUT OF S107

**CLAUDE REASONED FROM A DELIVERY MODEL THAT WAS RETIRED FOUR SESSIONS AGO — WHILE
READING THE FILE THAT SAYS SO.**

S107 opened with Claude telling DJ that students read the book through Canvas and that
the inline-style constraint was live. Both were retired at **S103, Bible §27, v8.90**
(*"There will be no pasting html text into canvas"*). Claude had quoted `build_css.py`
in the same reply — whose docstring opens *"Bible §27 retired the Canvas-paste delivery
model, so the book is a website"* — read past that sentence, and kept the stale premise.

**The Bible is clean here.** §27.6 already enumerates every passage resting on the retired
constraint and rules them annotated-not-rewritten per §26.7. The residue is deliberate.

**The session-open ritual cannot catch this.** It verifies VERSIONS — LIVE.md,
`session_versions --check`, 45 gates. Version agreement cannot detect a wrong premise, and
every downstream conclusion was correctly derived from a false one. Corrected in memory at
S107; recorded here because the ritual still has the hole.

---

# S107 WORK — a design session, not a code session

## The complete banner ruling set → `ZUMO_S107_BANNER_RULINGS.md`

**Read that file. It is 19 KB and it is the authority.** Summary only:

- **Type "E"** — Inter, headings 700, negative tracking, `#1d1d1f` body, generous spacing.
  KEEPS the 2px border, 8px radius and full table grid. A lighter treatment was built and
  DJ rejected it as *"too light"*; the reference is Apple, which is **heavy at the top of
  the hierarchy and quiet below it**.
- **Banner "F1"** — every cap becomes small eyebrow + large headline.
  Rule: *headline = the most descriptive string available; eyebrow = everything before it.*
- **NO ICONS ON ANY CAP** — all 237, bonus block included. **Supersedes §6.5 (marked
  LOCKED) and §4.5's family mark.** All 237 currently carry a leading emoji; zero are bare.
- **Every title and tail for all 237 caps is ruled**, lesson by lesson.
- **"Image Index" → "Figures"**, `id="image-index"` → `id="figures"`.
- **L04 `id="quick-reference"` → `quick-ref"`.**
- **going_deeper**: entry 5 retitled *Using Fixed Point*; the rest kept.

**NOTHING IS APPLIED.** The repo is unchanged apart from two deletions and one new file.

## Two deletions

Two root SVGs byte-identical to their `images/` copies, dragged in by the S106 close push.
**All 45 gates passed with them present.** §21 follows references and nothing referenced
them. The orphan gate offered at S106 keys on filename patterns (`PUSH_ME*` / `MD5*` /
`* (1)*`) and **would not have caught these** — the filenames were legitimate.
**Re-scope it: any file outside `images/` whose bytes match a file inside `images/`.**
`image_audit` already computes the hashes.

## Method correction, §24.6c

**`<h3>` COUNT IS NOT A PROXY FOR WHETHER A SECTION HAS CONTENT.** Claude used it as one
and reported L08 §4, L11 §4 and L13 §3 as empty. **All three have content** — 523, 867 and
3,371 characters, structured as tables and sustained prose. L13 §3 is one of the strongest
sections in the book: it quotes four lines of Pololu library source and walks the
`if (x < 0) x = 0;` clamp to prove silver tape is invisible to calibrated sensors.

**Also retracted:** L03's adjacent 8px/4px callout radii were called a defect. **§6.5a rules
exactly this** — inline callouts 4px, purple glossary/term cards 8px. Both were correct.

## Defects found by the ruling pass, none gate-visible

- Six banners render their icon twice (`📚 📚 Glossary` ×2, `🖼️ 🖼️ Image Index` ×2,
  `⚡ ⚡ Quick Reference` ×2)
- **L14 and L15 shipped byte-identical §8A titles**
- **L13, L14, L15 shipped byte-identical §5 tails** ("The Architecture")
- L15 titles its index "Graphic Index" — **accurate** (its index lists 0 IMAGEs, 3 GRAPHICs;
  so do L08, L09, L11). Being normalised anyway.
- `going_deeper.html` has **no anchor ids** on its six entries — no lesson can deep-link
- Four §1s carried authoring labels in student-facing text ("Opening Hook —",
  "Introduction —" ×3)

---

# S108 FIRST JOB — apply the rulings to L03 ALONE

**The S104 pattern.** One lesson, then the other fifteen. Gates 26, 27, 41, 43, 44, 45 and
§5b all move together, so a book-wide first attempt has no known-good baseline.

Per-lesson cost: banner markup → eyebrow + headline · emoji removed · title and tail
rewritten · **MODERATE bump** (visible banner moves, §5b two homes).

Book-wide, alongside: `_fence_title()` in `book_gates.py` must find the section name in
**both** shapes (it currently splits on the em dash, which F1 removes) · line 411's
`image-index` · `gen_bonus_banner.py` drops the family mark · full §27.8b
**restore → regenerate → apply `--include-held`** · Bible supersessions for §6.5 and §4.5
plus a new eyebrow/headline entry · three Bible passages for the Figures id ·
`BookComponentStandard` note that caps carry no marks.

---

# ⏰ AFTER SEPT 8 — REMIND DJ

- **"What the F()"** — DJ's title for going_deeper entry 2, parked by his own ruling.
  Memorable and names the macro; open question is register in a teacher-authored textbook
  for 15-year-olds. Alternatives: *What F() Buys You* · *The F() Wrapper*.
  Full note in `ZUMO_S107_BANNER_RULINGS.md` §7.
- **L02 §1 whodunit restructure** — three people's code, rank by error count. Matches
  §4.5's Observation family exactly (*"nothing is broken; predict, test, explain"*).
- **IMAGE + GRAPHIC → one FIGURE space.** The Figures rename makes this easier, not harder.

---

# IMAGES — STILL THE ONLY DEADLINE

**SEPTEMBER 8 IS FIVE WEEKS OUT.** DJ deprioritised these at S107 open (*"I am not worried
about 7 images. I am worried about a book that looks awesome"*) — recorded, not disputed,
but they remain the only items on `IMAGE_WORKLIST.md` with a date attached.

**19 outstanding of 145.** Seven are due in periods 2–4, week one:
`2.5` · `VIDEO 3.1` · `3.2` · `3.4` · `3.5` · `3.6` · `3.14`.
The winter five (13.1 · 13.2 · 14.1 · 14.2 · 16.1) are not Sept-8 work.

**Still offered, still not built:** a shot brief for those seven — surrounding prose, what
the lesson claims the reader is looking at, framing and props — so one bench session with
the robot clears all seven.

**Cheapest item on the list: `[IMAGE 7.13]`** reads *"Diagram showing final project
structure"* — a diagram tagged as a photo — while L07 already ships `GRAPHIC 7-15
platformio_file_tree` and `GRAPHIC 7-16 eight_file_architecture`. **One ruling may delete a
row.** Do not draw it without DJ.

---

# STANDING QUEUE

## Instrument work
- **Orphan gate, re-scoped** — byte-match against `images/`, not filename patterns (above)
- **`font_stack_sweep` reads only the first face.** Teach it every named face, and to reject
  a quoted family containing a comma. Nothing in the repo sees either defect.
- **`font_stack_sweep` does not scan `css/book.css`** — which is where the Segoe-UI-first
  body stack lived undetected. The S106 lesson recurring in a file the sweep never opens.
- `pill_sweep` and `gen_part_banners` still have no selftest
- `_ctm` still discards `rotate()`/`matrix()`; `regex_audit` reports 1 lead across 23 files

## Parked with a price (do not re-derive)
- **§26's repaint.** `#f8f9fa` 641 · `#fffbe6` 87 · `#4ec9b6` 294 → `#4EC9B0` · `#f14c4c` 14
  → `#D46554` · 9 roster rows · **41 marks unwired** · LEARN/INSIGHT sharing
  `#e3f2fd`/`#2196f3` · KEY TERM's purple colliding with MY PLAN.
  **CORRECTION TO S107's HANDOFF:** it called this *"now a stylesheet edit"*. It is not.
  `build_css.py`'s docstring: *"§24.12: THIS IS A GENERATED ARTEFACT. css/book.css is never
  hand-edited"* — and it has **no value-substitution layer**. A class RENAME is one line in
  `NAMES` plus a re-emit. A REPAINT changes the lessons, then restore → regenerate → apply.
- **`css/book.css` has 172 distinct colours and ZERO custom properties**, while `index.html`
  and `going_deeper.html` each carry a 12-token `:root`. Two files have a design language;
  sixteen do not. This is the real shape of §26.
- Gradients: 134 instances, 7 strings, 17 pages, 18 SVGs. Unruled.
- Consolas in `css/book.css`: 15 declarations. Browser CSS, harmless.
- Class names are provisional; the semantic set (27 accents / 30 families) is not designed.

## The Helvetica dialog — parked, do not chase before Sept 8
Warning, not failure. Leading candidate: 22 files request font-weight 500/600/800 and macOS
Helvetica has only 400 and 700. Second: 33 SVGs contain glyphs Helvetica lacks. Probes
`FONT_PROBE_C_weight500` / `D_weight700` were built and never run.

## Mechanical, measured
6 plain `href` in lessons · 4 dead alpha · 5 photo resolution/aspect · **5 staged files over
the gate-37 ceiling** (0.6–2.9 MB, fatal the moment a lesson wires one in) · the 2.07
three-way collision · 30 unreferenced files in `images/` including five `ChatGPT Image ….png`
and a stray `README.md`.

## Canon debts
§21.1's thresholds live only in `book_gates.py` · §25.6 header example · §25.10e misfiled ·
challenge-card redesign Part B · difficulty-progression audit · Maker batch · L01 VS Code
multi-root step · Stage Two two blocks labelled `Learn/Insight` (L03, L09) ·
`ROBOLORE_UPSTREAM_DELTA_S102.md` written and unapplied · robolore.com hosting ·
**`PUSH_WORKFLOW.md`: a repeat download of the same repo filename makes `(1)` the NEW file**
— offered S106 and S107, still not written.

## Bench (need the robot)
Q017 L09 six numbers · Q044 calibration-spin · Q046 gyro-bias · L02 §5 green-LED ·
Constrain RUN_MS · cm/s at a stated BASE_SPEED.

---

# PUSHING — READ THIS

Named-file CLI for adds and modifies; **GitHub Desktop for deletions.** **Never `git add .`**

**md5 every staged file against the list in chat before committing.**

1. **`(1)` does not mean stale.** Downloading the same repo filename twice in one session
   makes the `(1)` copy the NEW one. Verify by **md5**, never by suffix.
2. **Never present a test file in the same list as repo files.**
3. **S107's single-file push was clean** — verified `4d7695f`, md5 byte-identical, no
   drag-ins, 45/45. First clean push since S106 cost four.

---

# PUSH LIST FOR THIS SESSION'S CLOSE

| Action | File | Note |
|---|---|---|
| upload | `ZUMO_S108_HANDOFF.md` | this file |
| upload | `LIVE_ZUMO_TEXTBOOK.md` | **regenerate LAST**, versions EMITTED not typed |
| **delete** | `ZUMO_S107_HANDOFF.md` | §12.2 — gate 28 enforces exactly one |

*`ZUMO_S107_BANNER_RULINGS.md` is already live at `4d7695f` — do not re-push.*
