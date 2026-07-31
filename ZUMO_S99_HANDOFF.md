# ZUMO — S99 HANDOFF (written at S98 close · paste at top of Session 99)

## Session open ritual (do this without being asked)
1. `git clone --depth 1 https://github.com/Weymuth/zumo.git`
2. Read `LIVE_ZUMO_TEXTBOOK.md` — verify date / status / versions.
3. `grep -m1 -oE "Bible version: v[0-9.]+" ZUMO_SUPER_BIBLE.md` — **`-m1` matters, the version
   line runs ~99,000 characters.** This is grep's ONE legal use per §24.10.
4. Run: `python3 book_gates.py` · `python3 gen_component.py --selftest` ·
   `python3 lesson_inventory.py` · `python3 lesson_inventory.py --anomalies` ·
   `python3 pill_sweep.py --audit lessons/Lesson_*.html` · `python3 build_family_map.py` ·
   `python3 fit_raster_svg.py --selftest` ·
   `python3 session_versions.py --selftest` then `python3 session_versions.py`
5. **`--anomalies` is now SILENT when clean** (S98). Anything it prints is a real lead.
6. **Do not hand-type a version.** `session_versions.py --live` and `--handoff` EMIT the blocks
   this file and LIVE.md use. Generated text cannot drift.
7. **Do not hand-grep an instrument's version either.** A plain grep of `book_gates.py` returned
   **v1.26.1** against a live v1.29 in S98 — a changelog line, three releases stale, and it read
   exactly like an answer. `grep_trap()` in `session_versions.py` now keeps every home above its
   changelog and CONTROL D proves it fires. **The Bible is the exception and is FINE:** it greps
   as v8.63 first by design, which is why the ritual's Bible grep is anchored to the label.
8. Entrypoints are traps: `lesson_inventory.build(path)` — there is no `inventory()`.
   `gen_component.load_standard()` — there is no `parse()`.
9. **A CLONE CAN COME BACK STALE.** Poll `git ls-remote` before concluding a push failed — a
   cached clone reads exactly like a lost one.
10. **AFTER A PUSH, DIFF THE WHOLE TREE, NOT JUST THE PUSH LIST.** S98: seven files were
    byte-matched and the suite ran green, while a 327 KB outlined-text graphic rode in on the
    same commit unnoticed. `git diff --stat <session-open-sha> origin/main` takes one second.

---

# STATE

Fresh-clone verified at **`0b8360d`**. Census **39,972**.
Bible **v8.84** · `BookComponentStandard` **v01.10.0** · Maker **v2.45.1** ·
`marks/` **41** · `icons/` **49** incl. LICENSE.

Instruments: `book_gates` **v1.31** · `lesson_inventory` **v1.1.2** ·
`gen_component` **v1.6.1** · `pill_sweep` **v1.0** · `gate_payload_match` **v1.6** ·
`build_family_map` **v1.1.3** · `build_mark_index` **v1.0.2** · `gen_bonus_banner` **v1.2.1** ·
`gen_part_banners` **v1.0** · `session_versions` **v1.4.1** · `fit_raster_svg` **v1.1** ·
`going_deeper` **v01.1.1**.

Lessons: L01 v03.15.0 · L02 v03.6.0 · L03 v03.20.0 · L04 v04.15.0 · L05 v04.15.0 · L06 v04.19.1 · L07 v04.15.0 · L08 v04.14.0 · L09 v05.12.0 · L10 v02.11.0 · L11 v02.12.0 · L12 v01.14.0 · L13 v02.12.0 · L14 v02.15.0 · L15 v02.11.1 · L16 v02.7.0.

**Gate suite is 38.** No lesson file was edited in S98.

---

# THE S98 FINDING — A GATE CAN BE WRONG IN THE OTHER DIRECTION

S97 wrote gate 37 as *no REFERENCED `.svg` carries an embedded raster*. **That rule was itself the
defect.** It would have gone red on the first legitimate photo-plus-labels composite the book
shipped, and DJ ruled plainly: *"Some of the images need to be raster wrapped svg. Otherwise they
look like crap."*

**A photograph cannot be redrawn.** Measured across the five staged files: every one carries
photographic content (top-50 colours cover 9–48% of pixels). And the one true-vector redraw DJ had
actually looked at — `zumo_32u4_oled_main_board_top_view_r02.svg`, 16,651 B, 194 vector elements,
zero raster — turned out to be **a cartoon of the board**: its 39 text runs are the *silkscreen*
("Pololu", "www.pololu.com", "Engage Your Brain", "F 093 / 330 / 6.3V"), not labels. Nothing in it
could be spliced onto the photo either; its board rect is 110,190 at 1228×816 against the photo's
258,210 at 930×771.

**They must also EMBED.** An SVG loaded through `<img src>` runs in secure static mode and cannot
fetch an external file, so a single-file photo-plus-crisp-vector composite has no external-href
option. A gate forbidding base64 forbids the asset class.

**But 4.26 MB was never the price of one.** Two wastes, both free, neither visible on screen: the
payload stored **twice** in one `<image>` (`href` and `xlink:href`, identical bytes — the chassis
file has it too), over an alpha channel measured **100% opaque, zero transparent, zero partial**.

---

# WHAT SHIPPED IN S98

**1. `book_gates.py` v1.30 — gate 37 rewritten** to duplicated payload · 500,000 B ceiling ·
3-element vector floor. Control-run three ways, and **the one that matters is control B**: a
referenced 350,471 B composite with an embedded raster PASSES, whole suite green. Control A (fat
referenced file) and control C (raster-only envelope under the ceiling) both FAIL as intended.

**2. `fit_raster_svg.py` v1.1 — new.** `--write` normalises any raster-wrapped SVG:
dedupe · drop dead alpha · cap at 2× the on-screen box · re-encode at a **pinned q92**.
**Quality is the rule, size is the consequence.** v1.0 searched quality downward to hit a byte
budget and squeezed the two-photo file to q70 — degrading the picture, which is the exact complaint
that started the work. Six files: **11.89 MB → 1.67 MB**.

**3. Version homes normalised** across `book_gates`, `build_family_map`, `lesson_inventory`
(which carried TWO homes, agreeing by luck), plus `grep_trap()` + CONTROL D in `session_versions`.

**4. `lesson_inventory --anomalies` is silent when clean.**

**7. GATE 38 (`§21.2`) — drawn graphics keep their text and stay small.** Written because four
referenced graphics were replaced with outlined-text versions (**+1.13 MB, 50×**) and **passed 37/37
for a week**; one rode in on `09a33f8`, this suite's own commit. 60,000 B ceiling plus a
path-data-without-`<text>` flag. Control-run three ways including **the real historical defect
restored from `0b3f070`**. All four are now fixed at 6–11 KB with live text, and **zero
outlined-text files remain book-wide**. Bible **v8.84** adds **§17.3a, the two recipes** — Recipe 1
(drawn: live `<text>`, Arial/Courier New, viewBox 1100×850) proven on five files, Recipe 2
(photograph: keep the embed, add labels only, md5 unchanged) plus the note that **these files open
in Illustrator**, the embedded raster arriving as an ordinary image object.

**6. Bible §17.3 NEW — "PHOTOGRAPHS ARE NOT DRAWINGS."** The export canon, written because
§17 covered drawn graphics only and the gap is what produced a wrong gate. Records: IMAGE vs GRAPHIC
**by subject**; Photoshop → Illustrator as the route; **Embed never Link** (a linked photo is a blank
graphic on the published site — silent, production-only); **fonts** (live `<text>` renders with the
viewer's fonts, so use a common stack or convert to outlines); `fit_raster_svg.py --write` after
every export; and the `_##` / `_r##` suffixes.

**5. `Weymuth-patch-1` is no longer load-bearing** — see the queue below.

---

# WHAT TO TELL CHATGPT — THE TWO INSTRUCTIONS

**Never give it a byte budget.** S97 has the receipt: it reported the sensor arrays fixed and the
embedded PNG came back **byte-identical, same md5** — it had reworked the vector overlay and never
touched the photograph. Bytes are mechanical and are handled locally by `fit_raster_svg.py` with
gate 37 as the backstop. What GPT owes is the content decision, forked on one question.

**If the subject is a DRAWING** (memory ladder, flowchart, folder structure):
> Emit SVG markup, not an image. The file must contain no `<image>` tag and no
> `data:image/…;base64` string. Redraw the subject using `<rect>`, `<circle>`, `<path>`, `<text>`.

Acceptance test is one line: search the file for `base64`. Present means it ignored you.

**If the subject is a PHOTOGRAPH** (a populated board, the chassis, jumper positions):
> Do not redraw the photograph. Keep the embedded image exactly as it is, unmodified. Add only the
> label layer over it — `<text>`, leader lines, highlight boxes. Do not trace the board, and do not
> reproduce silkscreen text as vector.

**That last sentence is the load-bearing one.** Left alone GPT traces the board — `_r02` is exactly
that.

---

# STANDING QUEUE

**Images — decisions waiting on DJ (all five files are UNREFERENCED, nothing is broken today):**
- **The five raster-in-SVG files.** Claude's recommendation was DELETE, and the *container* half of
  that argument was wrong and is withdrawn. What stands: `5-08`/`5-09` wrap **the same photographs
  already live** as `5-05a`/`5-05b` (matched-scale diff **2.07**/**2.09**, different-subject control
  **8.17**), and their panel prose contradicts L05 — it says the sensors are *"installed"* and
  *"populated"* at 1/3/5 and promises *"right, front, and left coverage"*, where the lesson says
  *the jumpers do not move the sensors — they choose which ones are wired up*, and 1/3/5 are
  downward-facing reflectance sensors. **Lead, not verdict — read it before acting.**
  If any are kept: `python3 fit_raster_svg.py FILE --write`.
- **`5-10` is the only file over the ceiling at full quality** (697,330 B, two photographs). Split
  it into its two panels — "3-SENSOR CONFIGURATION" and "5-SENSOR CONFIGURATION" — or drop it.
- **Prose baked into pixels** is the deeper issue with all four panels: unselectable, unsearchable,
  no screen reader, no reflow, and a "Tip:" box painted into a photograph routes around all 30
  callout families and every gate that governs them.
- **`Weymuth-patch-1` can be deleted whenever DJ says.** The blocker is gone:
  `L03_IMAGE_3-14_astar_board.jpg` was removed from **main** deliberately (`9d5a85b`, *"remove
  redundant images"*) and recovers byte-identical from main's own history
  (`git show 9d5a85b^:images/L03_IMAGE_3-14_astar_board.jpg`, `205eabf1…`, 245,460 B). "astar"
  appears nowhere in the book; L03 has zero A\*, pathfinding or maze content. The branch is one
  commit ahead (`f97470b`, *Delete lessons/Lesson_13.html* — **do not merge**) and 316 behind.
- Carried: **26 orphan images** · `render_1-13_preview_3(1)_r01.svg` carries a `(1)` browser
  artifact · `images/Archived Images/` has a space in the folder name (URL-hostile).
- **Naming convention, still recorded nowhere:** trailing `_##` = spiral star (all 16, zero
  exceptions) · trailing `_r##` = a ChatGPT redo, staged not live · mid-name `N-NN` is the image
  number · **`IMAGE_` = photograph, `GRAPHIC_` = drawn.** That last one now has a gate behind it
  (the vector floor) and belongs in the Bible.

**SEPTEMBER 8 IS FIVE WEEKS AND FIVE DAYS OUT.**
- **Image shot list: 21 of 25 outstanding.** The long pole, and the one thing nobody else can do —
  camera work, not AI. The pipeline is now ready for them: each shot costs ~200 KB, not 1.7 MB.
- **Syllabus — four items, three of them one sentence from DJ:** TDP template Google Doc link,
  battery charging location and charge time, late-milestone penalty amount. Only **milestone due
  dates** are calendar-blocked. **DJ still owes `In the Lab` a read.**
- **SCHEDULE STILL BLOCKED UNTIL ~AUG 24** — DJ does not know which weekdays he teaches.
- **Grid, unresolved:** the ⭐ heavy-lesson list still reads L03, L06, L07, L08, L09, L12, and
  **L13 is now a Fall lesson and is deliberately unmarked** pending a ruling — it carries the most
  counter-intuitive idea in the back half, a sensor reading of 0 meaning *too bright* rather than
  *white*. Also open: whether Pd 23 needs a partner period for M6 re-demos.

**Canon debts, growing:**
- Bible §18.2 vs `BookComponentStandard` §9 on the spiral star (gradient vs flat, font text vs
  vector path) · §9 names no shape · §9 names no font-family.
- **§21.1's numeric thresholds are still only in `book_gates.py`.** §17.3 (S98) now names the three
  checks and deliberately does not restate the numbers a gate already owns — if that is the wrong
  call, the ceiling and floor belong in the Bible beside them.
- ~~The `_##` / `_r##` / `IMAGE_` vs `GRAPHIC_` conventions are recorded nowhere.~~ **PAID — §17.3, S98.**
- §25.6's header example reads `Version 02.7` for L11 · **§25.10e is misfiled**, line 1 of the Bible
  above its own title · **9 new roster rows still not activated in `BookComponentStandard.md`.**

**Paint, unchanged and still parked:** KEY TERM spans three purples (`#9b59b6` ×136 / `#9c27b0` ×33
/ `#9b6a9e` ×1, the third being MY PLAN's own colour) · the label convention for KEY TERM's 184
blocks · six one-off schemes · 46 distinct glyphs, 12 used once · **the mark library is still
entirely unwired**, zero references to `images/marks/` across all 21 pages. **The highest-value
paint work is still the diff nobody has done:** where the Bible and `BookComponentStandard` describe
the same thing they have never been compared. **§26 stays parked until DJ says RoboLore is
committed.**

**Stage Two (S95, still open):** two live blocks labelled `Learn/Insight` (L03:3636, L09:1342) each
need a side · Bible line 1033's Brain Check "Problem-Solving" item names the shared hex pair by hand
· Bible §18's data-type callout gives LEARN's blue a third job.

**`§12/§23` globs `**/*.html` only** — six non-HTML root strays are invisible to it; two are canon
(`favicon.ico`, `pio_harness.sh`), four unexplained (`L03_C05_starter_main.cpp`,
`ZUMO_NAME_WRITER_main.cpp`, `ZUMO_Template.zip`, `_archive_log.txt`). The syllabus, the grid and
the family map are root `.md` files governed by no gate at all.

Also carried: **difficulty-progression audit** (DJ's stated big goal; §6.12a is silent on whether
difficulty must ascend *within* a lesson) · challenge-card redesign Part B (~80–100 cards) · Maker
batch (bulk starters DL · `?lesson=N` gate · C## labels) · L01 VS Code multi-root step · BC03
weeding criterion · L16 outside the bonus family (DJ: *"Let's wait."*) · robot icons §21 still 2 of
5 · S87's six logged-not-fixed leads · S86's eight PART-seam readings · **`pill_sweep` and
`gen_part_banners` still have no selftest** · version-home shape normalisation for `lesson_inventory`
(done S98), `pill_sweep`, `gate_payload_match`, `gen_part_banners` (cosmetic, all read correctly).

**Bench (need the robot):** Q017 L09 six numbers · Q044 calibration-spin · Q046 gyro-bias ·
L02 §5 green-LED · Constrain RUN_MS.

---

# ON HOW S98 WENT

**Nothing a student sees changed.** No lesson file was touched, the census did not move, and the
work was entirely in the instruments — which is the right shape for a session six weeks out from a
course start, but worth naming honestly.

**The session's real lesson is that a green gate is not a correct gate.** S97's gate 37 passed 37/37
every run while encoding a rule that would have blocked the book's own asset class. It took DJ
looking at a rendered file and saying it looked like crap to find that; no instrument could have.

**Three things were caught by controls rather than by reading.** The `fit_raster_svg` selftest
enlarged a file on its first run. CONTROL D failed initially for a reason unrelated to what it
tested — its work tree omitted `images/`, so the probe crashed before reaching the check. And
control D's seed string was a version *literal* that would have stopped matching silently the next
time `book_gates` bumped, one command later. **An assert that cannot fail is not evidence, and that
applies to the controls themselves.**

**One measurement I reported was wrong and self-corrected within a minute:** the branch divergence
came back as ~50 unique commits from a `--depth 1` clone. Git does not error on ancestry it cannot
see; it answers confidently. Unshallowed, the true numbers are 1 and 316.

**Image viewing was broken for me all session** — a control PNG rendered blank — so every claim
about these files is from measurement, never inspection. **DJ should eyeball the fitted r03 against
r01 before q92 becomes the standard.**

---

# PUSH LIST

| Action | File | Note |
|---|---|---|
| upload | `fit_raster_svg.py` | **new file**, v1.1 |
| upload | `book_gates.py` | v1.30 — gate 37 rewritten |
| upload | `lesson_inventory.py` | v1.1.2 |
| upload | `build_family_map.py` | v1.1.3 — output asserted byte-identical |
| upload | `session_versions.py` | v1.4.1 |
| upload | `LIVE_ZUMO_TEXTBOOK.md` | regenerated at S98 close, versions EMITTED |
| upload | `ZUMO_S99_HANDOFF.md` | this file |
| **delete** | `ZUMO_S98_HANDOFF.md` | §12.2 — exactly one handoff in root, gate 28 enforces it |

**SECOND PUSH, same session (the Bible edit came after the first):**

| Action | File | Note |
|---|---|---|
| ~~upload~~ **DONE** | `ZUMO_SUPER_BIBLE.md` | §17.3 — pushed and verified at `a2f24bc` |
| upload | `LIVE_ZUMO_TEXTBOOK.md` | Versions line re-emitted |
| upload | `ZUMO_S99_HANDOFF.md` | this file, STATE re-emitted |

No deletion in the second push — the handoff filename is unchanged.

**THIRD PUSH, same session:**

| Action | File | Note |
|---|---|---|
| upload | `book_gates.py` | **v1.31** — gate 38 new, suite is now 38 |
| upload | `ZUMO_SUPER_BIBLE.md` | **v8.84** — §17.3a, the two recipes |
| upload | `LIVE_ZUMO_TEXTBOOK.md` | Versions line re-emitted |
| upload | `ZUMO_S99_HANDOFF.md` | this file, STATE re-emitted |

No deletion in the third push — the handoff filename is unchanged.


⚠️ **The deletion is a separate checkbox in GitHub Desktop, and four two-part pushes lost a half in
S97.** After pushing, verify by fresh clone and confirm `python3 book_gates.py` returns **37/37**.

**Optional, not in the push:** `zumo_32u4_oled_main_board_top_view_r03.svg` — the fitted 350,471 B
version of DJ's upload. Look at it first; it goes in `images/` only if it is going to be referenced.
