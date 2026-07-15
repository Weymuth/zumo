# ZUMO SESSION 40 — HANDOFF

*Paste this at the top of the new chat. The repo is the source — clone it.*

---

## OPEN THE SESSION (do this first, before any work)

```bash
git clone --depth 1 https://github.com/Weymuth/zumo.git
grep -oE "Bible version: v[0-9.]+" zumo/ZUMO_SUPER_BIBLE.md     # expect v8.25 (BUMPED in S39)
grep -oE "Project Maker v2\.[0-9]+"  zumo/newproject.html        # expect v2.28 (unchanged)
```

Then verify LIVE.md date (**July 15, 2026 — Session 39 close**) and lesson versions against the clone.
**If LIVE.md and the Bible disagree, ASK DJ. Never decide unilaterally.**

### ⚠️ FIRST THING: S38 **AND** S39 ARE BOTH STAGED, NOT PUSHED

Two sessions of work are waiting. S38 (visual pass) was never pushed; S39 (L03 content pass + L01 cover + Bible) is also staged. **They push together.** Verify by clone which version landed — not just that a commit exists.

| Probe | Expect if S38 pushed | Expect if S39 pushed |
|---|---|---|
| `index.html` | `FRONT DOOR — v1.2.1`; Mercersburg mark | (same — S39 didn't touch index) |
| `lessons/Lesson_03.html` | S38 banner/merge present | `grep -c "Blue = 75:1"` = 1; three `L03_GRAPHIC_3-1[678]` refs; NO `L03_IMAGE_3-14_astar_board` ref |
| `images/L03_GRAPHIC_3-16_three_turn_types.svg` | — | present |
| `images/L03_GRAPHIC_3-18_gear_train.svg` | — | present |
| `images/L03_IMAGE_3-16_gearmotor_gear_train.png` | — | present |
| `images/L01_IMAGE_1-18_kr_c_programming_book.png` | (old K&R hardcover) | new paperback (square, ~573px) |
| `ZUMO_SUPER_BIBLE.md` | v8.24 | `grep -oE "Bible version: v[0-9.]+"` = v8.25; `## 16. HARDWARE` + `## 17. SVG` present |
| `images/L03_GRAPHIC_3-07_trim_flowchart.svg` | — | NO `textLength` (`grep -c textLength` = 0) |

**If probes show S37/S38-era content, nothing has been pushed — that's job #1.**

### 🗑️ DELETIONS — a zip cannot delete. Run at push time:

```bash
# S38's five (if not already run):
git rm images/L01_IMAGE_1-13_kr_c_programming_book.png \
       images/L07_GRAPHIC_7-16_six_file_architecture.svg \
       images/L08_GRAPHIC_8-03_project_file_tree.svg \
       images/L09_GRAPHIC_9-07_sensor_patterns.svg \
       images/L09_GRAPHIC_9-08_project_file_tree.svg
# S39's one:
git rm images/L03_IMAGE_3-14_astar_board.jpg
```

---

## STATE AT S39 CLOSE

L01 **v03.2.4** · L02 v02.1.1 · L03 **v03.2.0** · L04 v04.0.6 · L05 v04.1.6 · L06 v04.5.5 · L07 v04.3.6 · L08 v04.1.4 · L09 v05.0.5 · L10 v02.1.8 · L11 v02.2.1 · L12 v01.2.2 · L13 v02.2.1 · L14 v02.4.1 · L15 v02.2.1 · L16 v02.2.1
**index.html v1.2.1 · Bible v8.25 · Maker v2.28 · Gate v1.1 · Harness v3.0 · engine.py**

- 📗 **S39 = L03 content pass + L01 cover + Bible v8.25.** Display/prose/art only on L03 — no payload, byte, gate, or Maker changes.
- 🎨 L03: 3 new SVGs (3.16 turns, 3.17 number line, 3.18 gear train), gearmotor photo (3.16), A-Star board dropped, gear-ratio color code (Blue=75:1, verified 0J63 §1.1), GRAPHIC 3.7 textLength fixed.
- 📖 Bible v8.25: NEW §16 HARDWARE GROUND TRUTH + §17 SVG CANON (memory-only canon now in the durable doc, per DJ "err toward more in the Bible").
- 🖼️ L01 cover swapped (K&R hardcover → PH paperback), image-only, Lesson_01.html unchanged.
- ⚠️ **Payload gate + byte figures UNAFFECTED.**

---

## S40 QUEUE

1. 🔴 **PUSH S38 + S39 TOGETHER, FIRST.** Order (blocking): SVGs/PNGs → `images/` · `index.html` → Pages · lessons + root docs (Bible, LIVE) → repo · lessons → Canvas · then ALL the `git rm` (5 from S38 + 1 from S39). Verify by clone after.
2. **Q017 bench session (DJ, one robot, three riders):**
   a. **Green-tape numbers** — six calibration numbers (white/green/black under outer sensors). Decision table in S39 handoff / memory.
   b. **Calibration-spin stopwatch (Q044)** — time B-press → "Calibration done!".
   c. **Gyro-bias stopwatch (Q046 — DJ has not ruled)** — optional L12+ boot bias timing.
3. **Q037 ruling — L01 "Coming from Arduino?" callout** (4–5 bullets). Approve / modify / drop.
4. **L03 leftovers:** two placeholders (brushed/brushless §4.2 — DJ has a blurb + video; 3-Roombas Coach's Note §4.5 — DJ to supply story) + IMAGE 3.4 terminal-success screenshot.
5. **22-photo queue** (DJ — `IMAGE_SHOT_LIST.md`).
6. 🔴 **AI Tutor rebuild — LAST.** Standing ruling. (Needs updated lesson titles/taglines from S38.)

---

## PARKED — DO NOT RE-OPEN UNPROMPTED

- **textLength SVG audit** (NEW S39) — 30 SVGs use `textLength`; only over-stretched ones are defects (fit-to-box is fine). Per-file audit, NOT a blind find/replace. Scoped session.
- **Challenge solution-disclosure** (DJ rules after classroom use; options D/E/F in memory).
- **Byte re-audit** (L10/L12–L15 carry S25-harness figures) · **Maker-wiring for L11–L16** · **lib_deps version pin** (candidate syntaxes need bench-test) · "Know Your Zumo" board-map page · §9 difficulty grouping · L06 card pattern · gate filename regex.

---

## WHAT S39 LEARNED

- **A defect DJ can see may live inside an SVG, not the lesson HTML.** The "weird spacing" code box was `textLength="560"` baked into GRAPHIC 3.7 (lines 63–65), invisible to HTML greps. I wrongly called it a cache ghost twice before checking the SVG. When a rendered artifact looks wrong but the HTML is clean, grep the REFERENCED asset.
- **A true top-down view cannot show a height relationship.** The gear "ladder" is a stacked-height fact; looking straight down collapses it to concentric circles. It needed a side/cutaway view, traced from DJ's photo. Don't fake a view that can't carry the information.
- **Verify hardware color codes against the manufacturer, not memory.** Gear-ratio sticker (Green/Blue/Red = 50/75/100) came from Pololu 0J63 §1.1; the earlier lesson text ("the color is the gear ratio") was unverified and vague.
- **Package like §12 the FIRST time.** Delivered individual files before DJ reminded me it should be ONE zip in repo layout. Session close = one zip, full repo layout, git rm lines — every time.
- **Err toward MORE in the Bible.** DJ ruling: canon that lives only in memory has no backup. §16/§17 pulled hardware + SVG ground truth into the durable doc.
- **Prereq box goes ABOVE the PART bar (S38 canon) — do not "flip" it below.** S39 tried moving L03's PART-2 prereq box below the banner to close a top gap; that broke the banner→section merge (the bar must cap directly onto its first section). Reverted. If a prereq box seems to leave "free space," the fix is spacing/margins, not reordering the box below the bar.

---

## CONTAINER SETUP (rebuild each session)

```bash
pip install cairosvg pillow pillow-avif-plugin --break-system-packages
# AVR toolchain + 9 dep repos only if compiling — see pio_harness.sh v3.0
```

**Preview technique:** render SVGs to PNG with cairosvg and present for sign-off; the Visualizer's design system forbids the book's colors/Title-case, so build browser-HTML previews for skin work.
**Gate quirk:** copy lessons to `Lesson_NN_x.html` before running the gate.
**Delivery (Bible §12):** session open = clone · session close = ONE zip, repo layout, every changed file · removals = explicit `git rm` lines.
