# ZUMO — S101 HANDOFF (written at S100 close · paste at top of Session 101)

## Session open ritual (do this without being asked)
1. `git clone --depth 1 https://github.com/Weymuth/zumo.git`
2. Read `LIVE_ZUMO_TEXTBOOK.md` — verify date / status / versions.
3. `grep -m1 -oE "Bible version: v[0-9.]+" ZUMO_SUPER_BIBLE.md` — **`-m1` matters**.
4. Run: `python3 book_gates.py` · `gen_component.py --selftest` · `lesson_inventory.py` ·
   `lesson_inventory.py --anomalies` · `pill_sweep.py --audit lessons/Lesson_*.html` ·
   `build_family_map.py` · `fit_raster_svg.py --selftest` · `flatten_alpha.py --selftest` ·
   `svg_layout_audit.py --selftest images/L01_GRAPHIC_1-13_zumo_rear_view.svg` ·
   `session_versions.py --selftest` then `session_versions.py` ·
   **`site_parity.py --selftest` then `site_parity.py`** ← NEW, and see below.
5. `--anomalies` is SILENT when clean. Anything it prints is a real lead.
6. **Do not hand-type a version.** `session_versions.py --live` / `--handoff` EMIT the blocks.
7. **Do not hand-grep an instrument's version either** — `grep_trap()` keeps every home above its
   changelog. The Bible is the exception and is FINE.
8. Entrypoints are traps: `lesson_inventory.build(path)`, `gen_component.load_standard()`,
   `svg_layout_audit.audit(path)`, `flatten_alpha.flatten(path)`.
9. **A CLONE CAN COME BACK STALE — and `git ls-remote` can too.** Poll, but believe the clone.
10. **AFTER A PUSH, DIFF THE WHOLE TREE**, then run `site_parity.py`.

---

# STATE

Fresh-clone verified at **`485bb34`**. Census **39,972** — no lesson file was touched in S100.
**40/40 gates. `site_parity` reports PARITY.**

Bible **v8.86** · `BookComponentStandard` **v01.10.0** · Maker **v2.45.1** ·
`marks/` **41** · `icons/` **49** incl. LICENSE.

Instruments: `book_gates` **v1.34** · `lesson_inventory` **v1.1.2** ·
`gen_component` **v1.6.1** · `pill_sweep` **v1.0** · `gate_payload_match` **v1.6** ·
`build_family_map` **v1.1.3** · `build_mark_index` **v1.0.2** · `gen_bonus_banner` **v1.2.1** ·
`gen_part_banners` **v1.0** · `session_versions` **v1.7** · `fit_raster_svg` **v1.2** ·
`flatten_alpha` **v1.1** · `svg_layout_audit` **v1.16** · `site_parity` **v1.0** ·
`going_deeper` **v01.1.1**.

Lessons unchanged: L01 v03.15.0 · L02 v03.6.0 · L03 v03.20.0 · L04 v04.15.0 · L05 v04.15.0 ·
L06 v04.19.1 · L07 v04.15.0 · L08 v04.14.0 · L09 v05.12.0 · L10 v02.11.0 · L11 v02.12.0 ·
L12 v01.14.0 · L13 v02.12.0 · L14 v02.15.0 · L15 v02.11.1 · L16 v02.7.0.

---

# THE S100 FINDING — A CLONE IS NOT THE SITE

**Lesson 3 was serving a TRIM diagram under the name `L03_GRAPHIC_3-16_three_turn_types.svg`.**
3,467,471 B, the raw unfitted trim file, uploaded under the wrong name. At the same time
`L03_IMAGE_3-01_motor_gearbox_in_frame.jpg` was returning a **live 404** — a `.png` had replaced
it and the lesson's reference was left behind.

**Every instrument was green throughout.** They all read the clone, and the clone was correct:
gate 21 passed because the reference resolved, to a file on disk that was the right picture. The
browser was happy; it rendered a perfectly good image of the wrong thing.

**I checked the repo, said "nothing was deleted, the file is intact", and was wrong about the
only thing that mattered — what a student's browser actually receives.** DJ found it by looking
at the page. He had also said "somehow it got deleted" one turn earlier, and I chased the wrong
file; the deletion he meant was the 3-01 jpg, and it took a full sweep to surface it.

**§24 corollary, recorded:** *a clone is not the site.* Alongside S99's *"a control that does not
ask WHICH is not a control"*, and S100's other two below.

---

# NEW INSTRUMENT — `site_parity.py` v1.0

Compares the **published site** against the repo for every referenced image — Content-Length
against byte count, `--deep` to hash the bytes. Catches wrong-file-under-right-name and live
404s, the two failures actually observed.

**Deliberately NOT a gate.** `book_gates.py` is offline by contract — it must run on a plane, and
a network dependency inside it turns "no wifi" into "the book is broken". Run it AFTER a push, in
the same breath as the fresh-clone verification `PUSH_WORKFLOW.md` already requires.

Four controls, both directions. Network failure reports as *unknown*, never as a finding.
**Registered in `session_versions` ARTEFACTS** — see below for why that sentence exists.

---

# TWO NEW GATES — 38 → 40

**Gate 39 · §17.3c** — plain `href` on `<image>` is SVG 2; Illustrator parses SVG 1.1, cannot
read it, and the composite renders perfectly while refusing to OPEN. Also catches `xlink:href`
used without `xmlns:xlink`. S99 found this by hand after every composite in the book was already
broken, then recorded it only in `svg_layout_audit` — **which the suite does not run. Advisory is
how it regressed.** Control-run five ways: seeded plain href, seeded dual attribute, stripped
namespace, coverage drop, and clean.
It immediately found **5 staged files** carrying the defect: `L02_IMAGE_2-07_ir_sensors_r02` and
`_r13`, `L05_GRAPHIC_5-08`, `5-09`, `5-10`. All unreferenced, so reported not fatal — but red the
moment one is wired in.

**Gate 40 · §21.1b — FRAGILE IF EDITED.** Advisory, never fatal. Names every referenced composite
that is fine today but would breach the ceiling if an Illustrator round-trip returned its payload
lossless. **Currently 11 files.** It flags `L01 1-10` at ~1,938,090 B — which is S99's actual
incident (439 KB up, 2.37 MB back) *predicted* instead of discovered.
PIL import is **guarded**: absent, the gate says so and stays green. A crash is worse than a false
positive, and worse than a missing advisory.

---

# THE ILLUSTRATOR ROUND-TRIP, MEASURED

DJ asked: does editing an SVG in Illustrator always grow it? **Measured on his own edit of 6-05:
+5,165 B, +1.4%.** So no — but the risk is real and format-dependent:

- **Markup bloat is trivial.** Illustrator rewrites structure (groups, CSS classes, tspans,
  `data-name`): +3,825 B on a 374 KB file. Ignorable.
- **Payload re-encoding is the danger.** The embedded photo is ~97% of a composite's bytes.
  Illustrator decodes on open and re-encodes on save. **JPEG re-saved as lossless PNG can
  quadruple** — that is what happened to `L01 1-10` in S99.

**DJ asked to convert the two JPEG payloads to PNG pre-emptively. Measurement said no** and it was
not done: lossless PNG is over the ceiling (5-05 → 833,592 B, 2-08 → 620,081 B) and palette PNG
that fits costs **4× the drift of JPEG q92** (1.708 vs 0.454 mean, max error 133 vs 42). *The fix
is the warning, not the conversion.* Gate 40 carries it.

**Also confirmed good:** Illustrator deduped 6-05's two identical small wheels into a shared
`<image>` in `<defs>` + two `<use>` — correct, and exactly the optimisation offered and declined
earlier.

---

# `session_versions` v1.7 — AND WHY

Two separate fixes.

**v1.6 — CONTROL C could not tell a wrong reader from a wrong book.** Its clean direction ran
`check()` against the LIVE tree, so a duplicate handoff in the repo printed as *"FAILED. --check
reports drift on a clean tree"* — a fault in the TOOL — and it `return 1`'d before CONTROL D ran.
**D never executed at session open and that was indistinguishable from D passing.** Now: a fixture
made clean by construction, both directions inside it, live tree read afterwards as a labelled
report that cannot mask what follows.
**§24 corollary: a control that depends on the state of what it audits is not a control.**

**v1.7 — `site_parity` was not registered in ARTEFACTS.** Its version would never have reached
LIVE.md or the handoff. **Third time in three sessions** (v1.4.1 `fit_raster_svg`, v1.5
`flatten_alpha` + `svg_layout_audit`, now this). Twice the fix was "be careful"; it did not work.
**CONTROL E** now compares ARTEFACTS against the root `.py` files and names any that declare a
`VERSION` but are not registered. Seeded an unregistered tool → fires by name; removed it →
silent. **ALL FIVE CONTROLS PASS.**

---

# THE WHITE BORDER — TWO WRONG DIAGNOSES BEFORE THE RIGHT ONE

DJ reported a border around the robot in three L05/L13 composites. It took three attempts:

1. **Wrong:** measured a halo, found the ring 1–2 levels *darker* than the background. Not it.
2. **Wrong:** found a real white matte fringe (knockout cut from a light studio background, so
   partial-alpha edge pixels carry white RGB), patched it 1400 → 77 px. Real, but not what DJ saw.
3. **Right:** the photo's **opaque square was punching a flat rectangle through the artwork** —
   erasing the cones in 5-01, the blind wedges in 5-07, the sweep line in 13-01.

**My "seamless" call in step 2 was a bad measurement**: I sampled one point per side, hit flat
cream on all four, and declared it clean. Sampling 164 points around the perimeter found the cuts
instantly (15, 31, 31). *Four samples where the answer varies around the edge is not evidence.*

Fixed by restoring alpha and cropping tight: artwork now shows through at 87.6 / 88.1 / 86.7%,
robot moved 0.00 units, residual is a ring within 6 px of the silhouette and **0.0% beyond 20 px**.

**§24 corollary from gate 40's sibling finding: a mean over an area cannot see a defect on a
perimeter.** `flatten_alpha` scored 0.408 drift on a visibly defective file — the rim was ~4,200
px of 935,000, so even total error moves the mean 0.55 against a 3.0 threshold.

---

# `svg_layout_audit` HAS A BAD TEXT-WIDTH ESTIMATOR — DO NOT ACT ON ITS OVERFLOW FINDINGS

Verified against rendered pixels under Liberation Sans (metric-compatible with Arial):

| File | Audit said | Measured | |
|---|---|---|---|
| `10-02` ×3 | 32 / 81 / 48 | 20 / 16 / 20 | real, magnitude 2–5× inflated |
| `6-04` | overflow 15 | **fits by 11.5** | verdict FLIPPED |
| `6-05` | overflow 43 | **fits by 30.5** | verdict FLIPPED |

Plus a **2× boundary bug** whose message demanded exactly what the file already had
(*"765x659 … needs a source at least 765 px wide"*).

**Consequence not yet acted on:** `GPT_WORKLIST_S99.md` is 30 files ordered worst-first **by this
estimator**. Its "worst: L07 7-04 at 105, L10 10-02 at 81" — the 10-02 entry measures 16 in
reality. **The worklist's ordering, and possibly its membership, is likely wrong, and the graphics
chat is working from it.** Re-deriving it by render is the highest-value instrument work open.

---

# GRAPHICS PROCESSED IN S100 — 20 FILES, ALL LIVE AND AT PARITY

| File | Before | After |
|---|---|---|
| `L05_GRAPHIC_5-01_robot_sees_obstacles` | 2,284,836 | 374,159 |
| `L05_GRAPHIC_5-07_the_dead_spot` | 2,287,160 | 208,011 |
| `L13_GRAPHIC_13-01_lawnmower_sweep` | 2,285,108 | 40,616 |
| `L05_GRAPHIC_5-05_proximity_sensor_layout` | 2,286,755 | 264,393 |
| `L10_GRAPHIC_10-02_avoidance_box_five_phases` | 2,286,437 | 71,477 |
| `L10_GRAPHIC_10-03_course_setup_clearance` | 2,286,504 | 58,778 |
| `L03_GRAPHIC_3-08_trim_before_after` | 3,467,471 | 165,755 |
| `L03_GRAPHIC_3-10_objects_hardware_map` | 1,937,865 | 41,354 |
| `L02_IMAGE_2-08_oled_status_screen` | 1,936,909 | 144,942 |
| `L02_IMAGE_2-06_oled_about_screen` | 1,936,454 | 156,707 |
| `L02_IMAGE_2-07_oled_controls_screen` | 1,936,128 | 156,381 |

**~25 MB of payload removed. No lesson file touched; census unchanged at 39,972.**

**Every incoming file needed renaming.** Not one arrived under the name its lesson references —
`_r0#` suffixes throughout, and in four cases a different descriptive name entirely
(`10-02_the_avoidance_box` → `10-02_avoidance_box_five_phases`, `trim_before_and_after_r01` →
`L03_GRAPHIC_3-08_trim_before_after`, and both L06 files). **Uploaded as sent they would all have
been orphans** and the redo would never have appeared on the page. Check the reference before
anything else.

**Also done:** 6-04 and 6-05 got parchment backgrounds and the real Zumo track wheel replacing
four drawn spoked wheels (the Zumo has tracks and sprockets, not spoked road wheels); 6-04's three
grey gearbox circles became brass gears with colours sampled from DJ's Pololu photo (median
`#CB9855`, near-identical to the book's existing gold `#C9A463`); a bare N20 micro motor was drawn
into 6-04's motor box, and all three drivetrain stages were aligned to a common 200–360 band.

**Banner ruling being applied by the graphics chat unprompted:** `9-3`, `3-17`, `3-18` and `3-09`
all arrived as single-change gradient → flat `#0B1A2E` fixes. **Six files still have a gradient
banner:** `L09_GRAPHIC_9-2_green_sensor_values` (`url(#scale)`), `9-5_test_course`, `9-6_fsm_uml`,
`9-7_sensor_patterns`, `9-8_project_file_tree` (all `url(#band)`), and
**`L03_GRAPHIC_3-16_three_turn_types`** (`url(#titleGrad)`, renders `#1D597D`).

---

# HELD BACK — `L06_GRAPHIC_6-05_wheel_circumference`

**DJ's Illustrator edit came back with two arrows destroyed.** The marker definitions were dropped
and both arrow paths collapsed to zero-length movetos:

| | Before | After the round-trip |
|---|---|---|
| Blue | `<line x1="167" y1="322" x2="421" y2="322">` + `arrowBlue` | `<path d="M586.4,322">` |
| Green | `<line x1="666" y1="300" x2="982" y2="300">` + `arrowGreen` | `<path d="M1147.4,300">` |
| `<marker>` defs | both present | **zero** |

Both `url(#arrowBlue)` and `url(#arrowGreen)` dangle. cairosvg crashes on it; a browser silently
draws nothing. Those arrows are the "roll one full turn → 122.5 mm" indicator and the
circumference span — the graphic's entire point.

**The live 6-05 is the ORIGINAL 12,868 B version** — the parchment + wheel work never landed.
DJ also changed the viewBox (1100×850 → 1431×915) and text count (24 → 45), so **ask what those
edits were meant to do before rebuilding**; do not simply restore from the pre-edit copy.

---

# STANDING QUEUE

**Highest value, instrument work:**
- **Re-derive `GPT_WORKLIST_S99.md` by render**, not by the bad estimator. The graphics chat is
  working from it.
- Fix `svg_layout_audit`'s text-width estimator and its 2× boundary test (v1.16 → v1.17).
- Fold the **under-the-box guard** into `flatten_alpha` as a refusal — it silently erases artwork
  when a photo does not sit on a flat backdrop. Used by hand all session; not yet in the tool.
- `pill_sweep` and `gen_part_banners` still have no selftest.

**Images:**
- **Six gradient banners** listed above, incl. 3-16 which is a one-attribute change.
- 3-16 and 24 other live files lead their font stack with a non-common font (Inter 13,
  Segoe UI 10, Consolas 7, JetBrains Mono 7). **§17.3b vs house style — unruled.** 1-19 is not an
  outlier; fixing it alone would make it inconsistent.
- 5 staged files carry plain `href` (gate 39 lists them). One-attribute fix each.
- `L03_IMAGE_3-01_motor_gearbox_in_frame.png` (1,433,599 B) is now **unreferenced** — the studio
  chassis shot. The live `.jpg` is a *different photograph*, 492×470 in a 900 px slot = **0.55×**,
  well under the 2× floor. Upgrade candidate for the shot list.
- `L05_GRAPHIC_5-06` and several others: numbered markers without `callout-*` groups.
- Carried: 26 orphan images · `images/Archived Images/` has a space in the folder name ·
  `L02_IMAGE_2-07_ir_sensors_r02`/`_r13` staged and over ceiling · the five S98 raster-in-SVG
  files whose prose contradicts L05.

**SEPTEMBER 8 IS FIVE WEEKS AND ONE DAY OUT** (Aug 1 → Sep 8 = 38 days).
- **Image shot list: 21 of 22 outstanding.** The long pole, and camera work nobody else can do.
  Two of them are now specified: side and top views for GRAPHIC 11.2.
- Pololu email sent — watch for a reply. 1200 px is their published maximum.
- Syllabus — four items, three of them one sentence from DJ. **Schedule blocked until ~Aug 24.**
- Grid: ⭐ list still reads L03, L06, L07, L08, L09, L12; **L13 deliberately unmarked** pending a
  ruling.

**New this session:** `GPT_SPEC_L11_11-02_cliff_arithmetic.md` — spec for rebuilding
`L11_GRAPHIC_11-02_cliff_arithmetic.svg` as SVG. A GPT PNG mockup arrived with **every number
matching L11 §8A.4 verbatim** (4.5 cm, 180 ms, 10 cm, 400 ms, 220 ms deficit, "no such number")
but one invented label — "BASE_SPEED 150", which appears nowhere in the book. Parked with three
costed options in `ZUMO_PARKED_EXIT_ITEMS.md`; option 3 is a BENCH item.

**Canon debts (unchanged):** Bible §18.2 vs `BookComponentStandard` §9 on the spiral star ·
§21.1's thresholds live only in `book_gates.py` · §25.6 header example · §25.10e misfiled ·
**9 new roster rows still not activated**.

**Paint, unchanged and still parked:** KEY TERM spans three purples · 184 KEY TERM blocks need a
label convention · six one-off schemes · 46 distinct glyphs, 12 used once · **the mark library is
still entirely unwired**, zero references to `images/marks/` across all 21 pages. **The
highest-value paint work is still the diff nobody has done:** where the Bible and
`BookComponentStandard` describe the same thing they have never been compared. **§26 stays parked
until DJ says RoboLore is committed.**

Also carried: difficulty-progression audit (DJ's stated big goal) · challenge-card redesign Part B ·
Maker batch (bulk starters DL · `?lesson=N` gate · C## labels) · L01 VS Code multi-root step ·
BC03 weeding criterion · L16 outside the bonus family · robot icons §21 still 2 of 5 · S87's six
logged-not-fixed leads · S86's eight PART-seam readings · **Stage Two (S95)** two live blocks
labelled `Learn/Insight` (L03:3636, L09:1342).

**Bench (need the robot):** Q017 L09 six numbers · Q044 calibration-spin · Q046 gyro-bias ·
L02 §5 green-LED · Constrain RUN_MS · **cm/s at a stated BASE_SPEED** (new).

---

# ON HOW S100 WENT

**Nothing a student sees got worse and a great deal got better.** Twenty graphics rebuilt or
refitted, ~25 MB removed, a trim diagram removed from Lesson 3's turn-types slot, a live 404 on
Lesson 3 closed, two new gates, one new instrument, and the published site verified at parity for
all 127 referenced images for the first time ever.

**The session's real lesson is the same as S99's, one level out.** S99 learned that a tool's first
finding must be read before it is believed. S100 learned that *the thing every tool reads* — the
clone — is not the artefact students receive. Every instrument in this repo was green while
Lesson 3 showed the wrong picture.

**My own error rate was high and the pattern was consistent: bad reference points in my own
controls.** Four times a control returned a confident number that was meaningless — a "BRASS"
check that passed on navy gears because it compared a percentage against a raw count; a centroid
control that gave identical answers for two different files because it was measuring the banner;
a clearance check that reported 8,623 px of collision against the wrong background; a
transparency check that read 26% because the mask was a brightness guess instead of the alpha
channel. **Every one of those files turned out fine.** The discipline that held: when a tool
reports something surprising, read the file before believing it — and control the control.

**A wrong finding costs 3× a blank one.** Spent freely again today.

---

# PUSH LIST

| Action | File | Note |
|---|---|---|
| upload | `ZUMO_S101_HANDOFF.md` | this file |
| upload | `LIVE_ZUMO_TEXTBOOK.md` | regenerate LAST, versions EMITTED not typed |
| **delete** | `ZUMO_S100_HANDOFF.md` | §12.2 — exactly one handoff in root, gate 28 enforces it |

⚠️ **The deletion is a separate checkbox in GitHub Desktop.** After pushing, verify by fresh clone,
confirm `python3 book_gates.py` returns **40/40**, and run **`python3 site_parity.py`** — it should
report PARITY.
