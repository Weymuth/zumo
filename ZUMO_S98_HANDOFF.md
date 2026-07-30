# ZUMO — S98 HANDOFF (written at S97 close · paste at top of Session 98)

## Session open ritual (do this without being asked)
1. `git clone --depth 1 https://github.com/Weymuth/zumo.git`
2. Read `LIVE_ZUMO_TEXTBOOK.md` — verify date / status / versions.
3. `grep -m1 -oE "Bible version: v[0-9.]+" ZUMO_SUPER_BIBLE.md` — **`-m1` matters, the version
   line runs ~99,000 characters.** This is grep's ONE legal use per §24.10.
4. Run: `python3 book_gates.py` · `python3 gen_component.py --selftest` ·
   `python3 lesson_inventory.py` · `python3 lesson_inventory.py --anomalies` ·
   `python3 pill_sweep.py --audit lessons/Lesson_*.html` · `python3 build_family_map.py` ·
   `python3 session_versions.py --selftest` then `python3 session_versions.py`
5. **READ THE ANOMALIES LIST ITEM BY ITEM.** Clean apart from the Brain Check family-norm line.
6. **Do not hand-type a version.** `session_versions.py --live` and `--handoff` EMIT the blocks
   this file and LIVE.md use. Generated text cannot drift.
7. Entrypoints are traps: `lesson_inventory.build(path)` — there is no `inventory()`.
   `gen_component.load_standard()` — there is no `parse()`.
8. **A CLONE CAN COME BACK STALE.** Twice this session a fresh clone returned the previous
   commit with the pushed file absent, and `ls-remote` showed `main` had already moved. Poll
   `git ls-remote` before concluding a push failed — a cached clone reads exactly like a lost one.

---

# STATE

Fresh-clone verified at **`a0fd093`**. Census **39,972**.
Bible **v8.82** · `BookComponentStandard` **v01.10.0** · Maker **v2.45.1** ·
`marks/` **41** · `icons/` **49** incl. LICENSE.

Instruments: `book_gates` **v1.29** · `lesson_inventory` **v1.1.1** ·
`gen_component` **v1.6.1** · `pill_sweep` **v1.0** · `gate_payload_match` **v1.6** ·
`build_family_map` **v1.1.2** · `build_mark_index` **v1.0.2** · `gen_bonus_banner` **v1.2.1** ·
`gen_part_banners` **v1.0** · `session_versions` **v1.3** · `going_deeper` **v01.1.1**.

Lessons: L01 v03.15.0 · L02 v03.6.0 · L03 v03.20.0 · L04 v04.15.0 · L05 v04.15.0 · L06 v04.19.1 · L07 v04.15.0 · L08 v04.14.0 · L09 v05.12.0 · L10 v02.11.0 · L11 v02.12.0 · L12 v01.14.0 · L13 v02.12.0 · L14 v02.15.0 · L15 v02.11.1 · L16 v02.7.0.

**Gate suite is 37, not 35.** No lesson file was edited this session.

---

# THE S97 FINDING — A PASSING SUITE IS ONLY AS WIDE AS ITS GATES

**Four images were 404 on the published site and had been through a full 35/35 pass.**
Lesson 02 pointed at three `.svg` files and Lesson 05 at one that existed nowhere on `main`.
Three of the first five lessons a student opens. Every gate was green the whole time, because
**nothing in the suite had ever looked at an `<img src>`.**

They were not found by an instrument. They were found by chasing a stray branch —
`Weymuth-patch-1`, 302 commits behind, which turned out to be the only surviving copy of the
missing files. A dead branch nobody had opened was load-bearing.

**The correction is two gates, and the second exists because the first is not enough:**

- **Gate 36 `§21`** — every image reference resolves to a file on disk. Control-run four ways,
  including against the unfixed tree at `cd47f50` where it independently rediscovered exactly
  those four with line numbers.
- **Gate 37 `§21.1`** — no REFERENCED `.svg` carries an embedded raster. **A reference that
  resolves says nothing about what it resolves to.** Gate 36 stayed green while
  `L02_GRAPHIC_2-08_memory_ladder.svg` shipped at **4,879,809 B** — a PNG in an SVG envelope,
  zero drawing elements, the same image embedded twice.

**Gate 36 proved itself the same afternoon.** Three L05 photographs were deleted in a push; the
gate named all three with line numbers on its first run, minutes after the push. This morning an
identical defect survived unnoticed for an unknown number of sessions.

---

# WHAT SHIPPED IN S97

**1. `ZUMO_Teacher_Daily_Grid_WORKING.md` v1.0** — 9,030 B, **23 periods + 3 buffers**, the
teacher-facing counterpart to the syllabus and the last planning doc outside the repo.
Five corrections are recorded inside the file:
- **The old Pd 20 taught the wrong lesson.** It read *"L12 (cont.) — Silver-strip detection; the
  calibrated-scale clamp."* Both are **Lesson 13**. L12 contains the word "silver" **zero times**;
  L13 holds `7B — The Silver Brake` and `8A.1 The Clamp, With Numbers`, the grid's phrase verbatim.
- **Fall now runs through L13 Step 3.** DJ ruling: *"Fall runs until they discover the silver
  line."* That is `silverDetected()`, L13 Step 2 — the Doorman. The old grid ended at L12 and
  **could not deliver its own last milestone.** No syllabus edit needed: M6 already reads *"stop
  at the rescue zone,"* which is the boundary, not the interior.
- **Two periods for L13, not four.** Steps 1–3 measure **191 lines** of §6 build; L11's entire
  build is **188** and already gets two periods. Same lesson shape — both open by copying the
  previous project.
- **The countdown column was recomputed** and its convention stated (every scheduled meeting,
  buffers included). The old one disagreed with its own demo rows.
- **The L13 reading splits at §5** — Fall assigns §1–§4; §5.1 `driveUntil()` and §5.2–5.3 the
  lawnmower sweep are Winter.

**2. Four recovered SVGs** — the live 404s, restored from the stranded branch.

**3. `book_gates.py` v1.27.1 → v1.29** — gates 36 and 37 (above).

**4. `L02_GRAPHIC_2-08_memory_ladder.svg` 4,879,809 B → 4,517 B.** True vector, produced by GPT
after being told to emit markup rather than an image. **Lesson 02's three diagrams now total
15,484 bytes.** At the worst point today they totalled 10.27 MB.

**5. The 16 spiral stars, flat.** DJ ruling: *"The RoboLore guidelines are no gradients. So, book
standard flat is the answer."* All 16 now `#7B6240` with `#F5F2E9` digits, **zero gradients**,
16,279 B for the set. Filenames and `<img>` references unchanged, so no lesson was touched.

**6. `gen_component.py` v1.5 → v1.6.1.** See the withdrawal below.

**7. 3.27 MB of unreferenced files deleted** — three L02 PNGs that **nothing had ever
referenced** (the lessons asked for `.svg` throughout) plus a `(1)` browser-download duplicate.

---

# THE WITHDRAWN GENERATOR — READ BEFORE RE-ATTEMPTING

`gen_component.py` **v1.6 shipped a numbered-mark generator and it was wrong.** v1.6.1 removes it.
The §9 spec is still PARSED (document conformance, including the assert that *"Gradients are
prohibited"* remains in the standard) but **no emitter ships**.

**Two independent failures, both mine:**

1. **§9 names two radii and NO SHAPE.** "It is a star" was an inference reported as fact. §9's
   6.2/9.6 gives inner/outer **0.646**; the book's own mark is **0.421** — 53% blunter, visibly a
   different mark.
2. **`dominant-baseline="central"` is unreliable through `<img>`**, which is how §18.2 renders
   these. Measured: when ignored, the digits sit **16% of the star's height too high** and
   overhang the body. **Bible §18.2 had already ruled the digits must be VECTOR PATHS —
   "renderer-proof" — and I overrode it, having flagged the contradiction myself.**

The live stars are therefore **recoloured S40 assets**, not generated: §9's flat fill applied over
§18.2's proven geometry, with the polygon points and glyph transforms asserted byte-identical.
Ten digit glyphs were harvested from the S40 files, so the letterforms are the approved ones.

**A generator that silently overwrites 16 good files is a landmine.** Do not re-add an emitter
until §9 names a shape. The rationale is recorded at the parse site in `gen_component.py`.

**§18.2 and §9 still contradict on canon** — §18.2 records the gold gradient as DJ-approved and
nothing says §9 supersedes it. **Bible correction not yet written.**

---

# THE PATTERN THAT COST THE MOST TIME — TWO-PART PUSHES LOSE A HALF

Not one of these was a defect in the book. All four are the same shape:

| What happened | The missing half |
|---|---|
| `book_gates.py` landed in `images/` | the root file was never updated |
| four residue files reported deleted | the commit had not gone up |
| `gen_component.py` deleted | its replacement was never added |
| three L05 photos deleted | the lesson was never repointed |

**A rename in the same commit went through cleanly** (`R100`), so the mechanism works. It is
**add-plus-delete** that loses a half, because the deletion is a separate checkbox in GitHub
Desktop. `PUSH_WORKFLOW.md` already says this; it kept happening anyway.

**Standing rule for S98: after any push, run `book_gates.py`.** 37/37 means the images are whole.
It caught the L05 deletion in seconds.

---

# IMAGE PIPELINE — WHAT IS TRUE NOW

**199 SVGs. 194 are true vector. 5 carry embedded raster, 7.27 MB, and every one is
unreferenced** — no student loads any of them, and gate 37 blocks each the instant it is wired in.

```
zumo_chassis_with_dual_tracks_r01.svg        2,564,003 B
L05_GRAPHIC_5-08_three_sensor_array.svg      1,692,300 B   <- promoted to canonical name
L05_GRAPHIC_5-09_five_sensor_array.svg       1,681,892 B   <- promoted to canonical name
L05_GRAPHIC_5-10_jumper_positions.svg        1,095,810 B   <- promoted to canonical name
L02_GRAPHIC_2-07_ir_sensors_r02.svg            593,050 B
```

**The three L05 files sit at canonical names, which makes them look ready. They are not.**
Dropping `_r02` changed the name, not the contents.

**GPT reported the sensor arrays fixed and they were not — but it did do work.** Measured
r01 → r02: the embedded PNG is **byte-identical, same md5**, while the vector overlay went 54 → 28
and 66 → 28 elements. It reworked the layer that was already fine and never touched the
photograph. *"Fix the SVG"* is satisfiable by editing anything inside the file.

**The instruction that works** (it produced every good output today): the file must contain **no
`<image>` tag and no `data:image/…;base64` string**; redraw the subject as `<rect>`, `<circle>`,
`<path>`, `<text>`; target under 20 KB. **The acceptance test is one line — search the file for
`base64`.** Real vector files today ran 4–10 KB.

**Naming conventions, confirmed against all 155 files and unambiguous:**
- trailing **`_##`** → spiral stars. All 16, zero exceptions.
- trailing **`_r##`** → a ChatGPT redo. Staged, not live.
- mid-name `N-NN` (hyphen) is the image number and cannot collide.
- **`_##` alone would have collided** — DJ first described the convention as `_##`, which matches
  every spiral star.
- **Neither is recorded in the Bible or `BookComponentStandard`.**

**Gate 37 is scoped to REFERENCED files on purpose.** Raw exports are staged in `images/` before
being wired up, and a gate that reddens on work-in-progress is a gate people learn to ignore.
Measured before choosing: strict would have failed on 7 staged files the same day. Unreferenced
offenders are counted and printed, never fatal. **Protect the book, not the staging area.**

---

# STANDING QUEUE

**Images:** the five raster-in-SVG files above · **26 orphan images** (`orphans.py` pattern:
compare every file in `images/` against every reference; spiral stars 01 and 11–16 are STAGED, not
waste — sources cited so far are all L02–L10) · `render_1-13_preview_3(1)_r01.svg` carries a `(1)`
browser artifact needing a rename before it goes live · `images/Archived Images/` holds one file
and its folder name contains a space (URL-hostile).

**`Weymuth-patch-1` must not be merged** — 302 commits behind, and its one unique commit deletes a
lesson file. But **do not delete it yet**: it is the only copy of
`L03_IMAGE_3-14_astar_board.jpg`. L03 references 3-13 then jumps to 3-15; "astar" appears nowhere
in the repo. Not a broken link, a numbering gap. Retrieve before deleting the branch.

**Canon debts opened this session:** Bible §18.2 vs `BookComponentStandard` §9 on the spiral star
(gradient vs flat, font text vs vector path) · §9 names no shape · §9 names no font-family · the
`_##`/`_r##` convention is recorded nowhere.

**Grid, unresolved and named in the file:** the **⭐ heavy-lesson list** still reads L03, L06, L07,
L08, L09, L12, carried forward unchanged. **L13 is now a Fall lesson and is deliberately
unmarked** pending a ruling — it carries the most counter-intuitive idea in the back half, a
sensor reading of 0 that means *too bright* rather than *white*, which is the profile of every
other starred lesson. Also open: whether Pd 23 needs a partner period for M6 re-demos.

**SCHEDULE — STILL BLOCKED UNTIL ~AUG 24.** DJ does not know which weekdays he teaches.
**Course starts Tuesday September 8, 2026 — about five and a half weeks out at S97 close.**

**Syllabus — four items left**, three of them one sentence from DJ: milestone due dates (the only
calendar-blocked one), the TDP template Google Doc link, battery charging location and charge
time, late-milestone penalty amount. **DJ still owes `In the Lab` a read.**

**Version-home normalisation, carried from S96:** `lesson_inventory` · `pill_sweep` ·
`gate_payload_match` · `gen_part_banners` still carry their version in a bespoke shape.
`session_versions.py` reads all four correctly, so this is cosmetic. **`pill_sweep` and
`gen_part_banners` have no selftest** — verify by running and diffing output.

**Paint, unchanged:** KEY TERM spans three purples (`#9b59b6` ×136 / `#9c27b0` ×33 / `#9b6a9e` ×1,
the third being MY PLAN's own colour) · the label convention for KEY TERM's 184 blocks · six
one-off schemes · 46 distinct glyphs, 12 used once · **the mark library is still entirely
unwired**, zero references to `images/marks/` across all 21 pages.

**The highest-value paint work is still the diff nobody has done:** where the Bible and
`BookComponentStandard` describe the same thing they have never been compared. §26 STAYS PARKED
until DJ says RoboLore is committed.

**Stage Two (S95, still open):** two live blocks labelled `Learn/Insight` (L03:3636, L09:1342)
each need a side · Bible line 1033's Brain Check "Problem-Solving" item names the shared hex pair
by hand · Bible §18's data-type callout gives LEARN's blue a third job.

**`§12/§23` globs `**/*.html` only** — a non-HTML root stray is invisible to it. Six such files
sit in root today; two are canon (`favicon.ico`, `pio_harness.sh`), four are unexplained
(`L03_C05_starter_main.cpp`, `ZUMO_NAME_WRITER_main.cpp`, `ZUMO_Template.zip`, `_archive_log.txt`).
The syllabus, the grid and the family map are root `.md` files governed by no gate at all.

Also carried: **difficulty-progression audit** (DJ's stated big goal; §6.12a is silent on whether
difficulty must ascend *within* a lesson) · challenge-card redesign Part B (~80–100 cards) ·
Maker batch (bulk starters DL · `?lesson=N` gate · C## labels) · L01 VS Code multi-root step ·
BC03 weeding criterion · L16 outside the bonus family (DJ: *"Let's wait."*) · robot icons §21
still 2 of 5 · S87's six logged-not-fixed leads · S86's eight PART-seam readings · §25.6's header
example reads `Version 02.7` for L11 · **§25.10e is misfiled**, line 1 of the Bible above its own
title · **9 new roster rows still not activated in `BookComponentStandard.md`.**

**Image shot list: 21 of 25 outstanding.** Most are DJ-and-a-camera and must not be AI-generated.

**Bench (need the robot):** Q017 L09 six numbers · Q044 calibration-spin · Q046 gyro-bias ·
L02 §5 green-LED · Constrain RUN_MS.

---

# ON HOW S97 WENT

**Two things a student sees got fixed.** Four broken images in Lessons 02 and 05 are gone, and
Lesson 02's diagram payload fell from 10.27 MB to 15,484 bytes. Both were live on the published
site while every gate read green.

**The teacher grid is in the repo**, which was the open half of S96's syllabus work — and reading
it against the lessons found a real error: two periods of Lesson 13 content labelled Lesson 12,
and a Fall trimester that could not deliver its own final milestone.

**Note what the instruments cost and returned.** Gate 36 was written because of a defect nobody
would have found on purpose, and it caught a second one within the hour. But **I shipped two
wrong things this session** — a numbered-mark generator built on an inference I reported as fact,
and a first attempt at removing it that would have deleted 428 lines instead of 84 because
`.index()` matched a comment that appears twice. Both were caught by checking the result rather
than trusting the edit. **Neither would have been caught by reading the code.**

**Five and a half weeks to September 8.** The syllabus and the grid are both in the repo. What
neither has is dates.

---

# PUSH LIST

| Action | File | Note |
|---|---|---|
| upload | `LIVE_ZUMO_TEXTBOOK.md` | regenerated at S97 close, versions EMITTED by `session_versions.py` |
| upload | `ZUMO_S98_HANDOFF.md` | this file |
| **delete** | `ZUMO_S97_HANDOFF.md` | §12.2 — exactly one handoff in root, gate 28 enforces it |

⚠️ **The deletion is a separate checkbox in GitHub Desktop and four two-part pushes lost a half
this session.** Verify by fresh clone and confirm `book_gates.py` returns **37/37**.
