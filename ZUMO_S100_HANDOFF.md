# ZUMO — S100 HANDOFF (written at S99 close · paste at top of Session 100)

## Session open ritual (do this without being asked)
1. `git clone --depth 1 https://github.com/Weymuth/zumo.git`
2. Read `LIVE_ZUMO_TEXTBOOK.md` — verify date / status / versions.
3. `grep -m1 -oE "Bible version: v[0-9.]+" ZUMO_SUPER_BIBLE.md` — **`-m1` matters**, the version
   line runs ~99,000 characters. This is grep's ONE legal use per §24.10.
4. Run: `python3 book_gates.py` · `gen_component.py --selftest` · `lesson_inventory.py` ·
   `lesson_inventory.py --anomalies` · `pill_sweep.py --audit lessons/Lesson_*.html` ·
   `build_family_map.py` · `fit_raster_svg.py --selftest` · **`flatten_alpha.py --selftest`** ·
   **`svg_layout_audit.py --selftest images/L01_GRAPHIC_1-13_zumo_rear_view.svg`** ·
   `session_versions.py --selftest` then `session_versions.py`
5. `--anomalies` is SILENT when clean. Anything it prints is a real lead.
6. **Do not hand-type a version.** `session_versions.py --live` / `--handoff` EMIT the blocks.
7. **Do not hand-grep an instrument's version either** — `grep_trap()` keeps every home above its
   changelog. The Bible is the exception and is FINE: it greps as v8.63 first by design.
8. Entrypoints are traps: `lesson_inventory.build(path)`, `gen_component.load_standard()`,
   `svg_layout_audit.audit(path)`, `flatten_alpha.flatten(path)`.
9. **A CLONE CAN COME BACK STALE — and `git ls-remote` can too.** S99: ls-remote returned a SHA
   one commit behind what the clone then produced. Poll, but believe the clone.
10. **AFTER A PUSH, DIFF THE WHOLE TREE.** `git diff --stat <session-open-sha> origin/main`.
    S99 had eight pushes where files rode in unannounced; two of them broke a live image.

---

# STATE

Fresh-clone verified at **`68cd396`**. Census **39,972**.
Bible **v8.86** · `BookComponentStandard` **v01.10.0** · Maker **v2.45.1** ·
`marks/` **41** · `icons/` **49** incl. LICENSE.

Instruments: `book_gates` **v1.32** · `lesson_inventory` **v1.1.2** ·
`gen_component` **v1.6.1** · `pill_sweep` **v1.0** · `gate_payload_match` **v1.6** ·
`build_family_map` **v1.1.3** · `build_mark_index` **v1.0.2** · `gen_bonus_banner` **v1.2.1** ·
`gen_part_banners` **v1.0** · `session_versions` **v1.5** · `fit_raster_svg` **v1.2** ·
`flatten_alpha` **v1.1** · `svg_layout_audit` **v1.16** ·
`going_deeper` **v01.1.1**.

Lessons: L01 v03.15.0 · L02 v03.6.0 · L03 v03.20.0 · L04 v04.15.0 · L05 v04.15.0 · L06 v04.19.1 · L07 v04.15.0 · L08 v04.14.0 · L09 v05.12.0 · L10 v02.11.0 · L11 v02.12.0 · L12 v01.14.0 · L13 v02.12.0 · L14 v02.15.0 · L15 v02.11.1 · L16 v02.7.0.

**Gate suite is 38.** Verified three ways at close — instruments, an independent lxml
re-derivation of gates 36 and 38, and **128 of 128 images fetched live from the published site**.

---

# THE S99 FINDING — EVERY COMPOSITE WAS UNOPENABLE IN ILLUSTRATOR

**Plain `href` on `<image>` is SVG 2. Illustrator parses SVG 1.1.** It cannot read the attribute,
reports the picture as a MISSING LINK, and names the folder the document sits in — which reads
like a stray file rather than a format problem.

**Browsers render both forms identically.** Every file looked perfect on the published site and
not one would open for editing, which is the entire purpose of a Recipe 2 composite. It took DJ
trying to edit one to find.

**The rule that caused it was half right.** S98 correctly found the chassis storing its payload
TWICE and made `fit_raster_svg` dedupe. Deduping was right. Keeping the wrong survivor was not —
and **its control asserted only that the duplicate was gone, never WHICH survived**, so it passed
green throughout. Control 1 now counts both attributes and is seeded with v1.1's own output.

Recorded as **Bible §17.3c**. Fixed in `fit_raster_svg` v1.2, `svg_layout_audit`, and the graphics
prompt — which had been instructing the exact defect.

**§24 corollary: a control that does not ask WHICH is not a control.**

---

# TWO NEW INSTRUMENTS

**`svg_layout_audit.py` v1.16** — pre-flight audit for an incoming graphic, run before a human
opens it. Ten checks: viewBox, raster payload and resolution, gate-37 ceiling, outlined text,
fonts, text-vs-panel overflow, same-baseline overlap, callout grouping and badge centring,
leader/box collisions, provenance. `--fixnote` emits a paste-ready correction block with the
measurements in it and the local-only items split out. Nine controls, both directions.

**`flatten_alpha.py` v1.1** — drops a transparent photo onto the backdrop it actually sits on.
Four controls. **Three real backdrop cases, all met in S99:** a flat page colour, an inner panel
(and a first attempt picked a 3px brass rule that would have haloed the robot gold — the rule is
the SMALLEST rect that fully covers the image box), and a gradient, which needs the page rendered
without the photo and composited onto the real pixels. Control 4 seeds the wrong backdrop and
catches it at 13.58 drift against a 3.0 threshold.

**THE STANDARD RECIPE IS NOW: `flatten_alpha --write` then `fit_raster_svg --write`.** DJ's PSD
sources carry knocked-out backgrounds; a real alpha channel cannot become JPEG, so composites
arrive at 1.0–4.1 MB against a 500,000 B ceiling. Measured: 2,732,428 B → 322,548 B on one file,
4,102,914 → 191,374 B on another. Then the fit caps both photos at 2× their boxes.

---

# THE HARDER LESSON — EVERY ONE OF MY OWN TOOLS CRIED WOLF

`svg_layout_audit` went 1.0 → 1.16 in one session. **Nine of those bumps were false positives or
crashes found by pointing it at real work**, and three of them sent DJ to fix something that was
not broken:

- **tspan** — a correctly wrapped two-line label measured as one 522-unit line. DJ was sent to
  have a non-defect corrected and GPT re-balanced a wrap that was already fine.
- **spiral stars** — 16 stars + 2 wordmarks flagged as "labels outlined". They are text-free BY
  RULING (§18.2). Gate 38 already had the guard; the audit did not.
- **badge anchors** — Illustrator rewrites `text-anchor="middle"` as a left-edge transform.
  The audit called that a defect; **acting on it double-corrected four badges by 5.6 units.**
  The tool caused the defect it warned about.
- **transforms** — Illustrator positions text via `transform="translate()"`. Every label
  collapsed to (0,0): 69 findings on a good file. Then the same bug in the raster check reported
  1.00× against a true 2.13×.
- **crash** — a `<text>` with no `x` killed the whole audit, reporting nothing.
- **imgs[0]** — `flatten_alpha` v1.0 skipped a whole file because its FIRST image had no alpha,
  while a 2.7 MB transparent PNG sat beside it.

**A crash is worse than a false positive; a false positive is worse than a missing check.** The
rule that keeps earning its keep: point a new instrument at real work early, and read the file
before believing its first finding.

---

# WORKING WITH THE GRAPHICS CHAT

`ROBOLORE_GRAPHICS_CHAT_HANDOFF.md` (repo root) is the standing prompt. It works — the last three
files arrived with `xlink:href`, correct fonts, per-callout grouping and the Pololu credit
unprompted. Rules added in S99: **the payload attribute**, **`<tspan>` wrapping**, **corrections
EDIT rather than paint over** (twice a "fix" was a white rect over the defect plus a new element
on top — element count is the test), **never render the `_r##` suffix as visible text**, and
**flatten transparency at embed time**.

**Never give it a byte budget. Never let it touch a photograph** — asked to embed one it will
resample it; a 1200×503 source came back at 300×300, letterboxed into a square box.

**THE WORKFLOW RULE, agreed with DJ:** *the last file Claude hands over is the one that gets
pushed.* If DJ edits it in Illustrator afterwards, **it comes back here before the push.** This
cost `L01 1-10` two full rounds of identical work — a fixed 439 KB version went up, was
overwritten by a 2.37 MB export, and DJ then edited that one.

`GPT_WORKLIST_S99.md` — **30 files**, worst-first by text overflow. Mechanical defects are not on
it. Worst: `L07 7-04` at 105 units, `L10 10-02` at 81, `L10 10-07` at 79.

---

# RULINGS MADE IN S99

- **All graphic banners are flat `#0B1A2E`.** 15 converted from six gradient variants and one
  parchment. 44 navy banners, zero exceptions. `L07 7-02` needed its title recoloured to white —
  navy-on-navy was a 1.00:1 contrast ratio, invisible.
- **`L01 1-13` and `L01 1-10`** are now photo composites replacing drawn diagrams. Both keep
  `GRAPHIC_` names while embedding photographs — six files now contradict §17.3's convention.
  Not ruled on.
- **Page weight is NOT gated, deliberately.** 12 referenced bare PNG/JPG files exceed 500,000 B;
  gate 37 covers only raster-wrapped SVG. **Lesson 5 loads 7.29 MB**; **7,133,980 B recoverable
  book-wide** by storing photographs as JPEG. DJ: boarding school, campus wifi, not worth gating.
  Recorded so it is not re-derived.

---

# STANDING QUEUE

**Images:**
- `L06_IMAGE_6-11_encoder_hardware.svg` is live and good, but its `callout-1` leader passes
  **1.4 units** from `callout-3`'s anchor dot. Cosmetic.
- `L02_IMAGE_2-07_ir_sensors_r02` (2.9 MB) and `_r13` (593 KB) are staged, unreferenced, over the
  ceiling. `_r13` is byte-size-identical to the old branded file — probably a rename.
- The five raster-in-SVG files from S98 — `5-08`/`5-09` wrap **the same photographs already live**
  as `5-05a`/`5-05b`, and their baked-in prose contradicts L05 on what the jumpers do.
  **Lead, not verdict — read it before acting.**
- Carried: 26 orphan images · `images/Archived Images/` has a space in the folder name.
- **Naming: `IMAGE_` = photograph, `GRAPHIC_` = drawn** — now recorded in §17.3, contradicted by
  six live files.

**SEPTEMBER 8 IS FIVE WEEKS AND ONE DAY OUT.**
- **Image shot list: 21 of 22 outstanding.** The long pole, and camera work nobody else can do.
- **Pololu email SENT** — asking whether the credit line is acceptable and whether higher-resolution
  originals exist. **1200 px is their published maximum**, which caps any photo box at 600 CSS px
  at the 2× floor. Watch for a reply.
- **Syllabus — four items**, three of them one sentence from DJ. Milestone dates calendar-blocked.
- **SCHEDULE STILL BLOCKED UNTIL ~AUG 24** — DJ does not know which weekdays he teaches.
- **Grid:** ⭐ list still reads L03, L06, L07, L08, L09, L12; **L13 deliberately unmarked** pending
  a ruling.

**Canon debts:**
- Bible §18.2 vs `BookComponentStandard` §9 on the spiral star · §9 names no shape, no font-family.
- §21.1's numeric thresholds live only in `book_gates.py`.
- §25.6's header example reads `Version 02.7` for L11 · **§25.10e is misfiled** · **9 new roster
  rows still not activated in `BookComponentStandard.md`.**
- Version-home shape: `pill_sweep`, `gate_payload_match`, `gen_part_banners` declare theirs in a
  docstring rather than a `VERSION =` line. Cosmetic, all read correctly.

**Paint, unchanged and still parked:** KEY TERM spans three purples · 184 KEY TERM blocks need a
label convention · six one-off schemes · 46 distinct glyphs, 12 used once · **the mark library is
still entirely unwired**, zero references to `images/marks/` across all 21 pages. **The
highest-value paint work is still the diff nobody has done:** where the Bible and
`BookComponentStandard` describe the same thing they have never been compared. **§26 stays parked
until DJ says RoboLore is committed.**

**Stage Two (S95, still open):** two live blocks labelled `Learn/Insight` (L03:3636, L09:1342) ·
Bible line 1033's Brain Check names the shared hex pair by hand · §18's data-type callout gives
LEARN's blue a third job.

Also carried: difficulty-progression audit (DJ's stated big goal) · challenge-card redesign Part B
· Maker batch (bulk starters DL · `?lesson=N` gate · C## labels) · L01 VS Code multi-root step ·
BC03 weeding criterion · L16 outside the bonus family · robot icons §21 still 2 of 5 · S87's six
logged-not-fixed leads · S86's eight PART-seam readings · **`pill_sweep` and `gen_part_banners`
still have no selftest**.

**Bench (need the robot):** Q017 L09 six numbers · Q044 calibration-spin · Q046 gyro-bias ·
L02 §5 green-LED · Constrain RUN_MS.

---

# ON HOW S99 WENT

**Twelve pushes, all verified by fresh clone.** Two introduced live 404s — an `_r0#` file uploaded
while the live file was deleted, leaving the lesson's reference behind. Both caught by gate 36
within a minute of landing. It is the single most common failure in this repo and the cause is
always the same: **the deletion is a separate checkbox.**

**Nothing a student sees got worse and a good deal got better.** Nine graphics rebuilt or repaired,
15 banners unified, two live 404s closed, one lesson reference corrected, and every composite in
the book now opens in Illustrator.

**The session's real lesson is about my own instruments.** Two new tools, sixteen version bumps
between them, and most of those bumps were fixing noise the tools themselves generated. The audit
was worth building — it caught real defects in six files before DJ opened them — but it was only
trustworthy after being pointed at real work and being wrong in public a dozen times.

**A wrong finding costs 3× a blank one, and I spent that currency freely today.** The discipline
that held: measure before asserting, control both directions, and when a tool reports something
surprising, read the file before believing it.

---

# PUSH LIST

| Action | File | Note |
|---|---|---|
| upload | `ZUMO_S100_HANDOFF.md` | this file |
| **delete** | `ZUMO_S99_HANDOFF.md` | §12.2 — exactly one handoff in root, gate 28 enforces it |

⚠️ **The deletion is a separate checkbox in GitHub Desktop.** After pushing, verify by fresh clone
and confirm `python3 book_gates.py` returns **38/38**.
