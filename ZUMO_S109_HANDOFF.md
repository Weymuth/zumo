# ZUMO — S109 HANDOFF (written at S108 close · paste at top of Session 109)

## Session open ritual (do this without being asked)
1. **`git ls-remote https://github.com/Weymuth/zumo.git HEAD` FIRST.** A shallow clone served a
   STALE head twice in S108 while the remote was already ahead (§12.4, *caches lie*). If the
   clone's `git log -1` does not match the remote sha, fetch the sha by name:
   `git init v && cd v && git remote add o <url> && git fetch --depth 1 o <sha> && git checkout FETCH_HEAD`
2. Read `LIVE_ZUMO_TEXTBOOK.md` — verify date / status / versions.
3. **Do NOT grep the Bible version.** `session_versions.bible_consistency()` parses it.
4. Run: `book_gates.py` · `gen_component.py --selftest` · `lesson_inventory.py` ·
   `lesson_inventory.py --anomalies` · `pill_sweep.py --audit lessons/Lesson_*.html` ·
   `build_family_map.py` · `fit_raster_svg.py --selftest` · `flatten_alpha.py --selftest` ·
   `svg_layout_audit.py --selftest images/L01_GRAPHIC_1-13_zumo_rear_view.svg` ·
   `regex_audit.py --selftest` then `regex_audit.py` · `build_worklist.py --selftest` ·
   `font_stack_sweep.py --selftest` then `font_stack_sweep.py` ·
   `session_versions.py --selftest` then `--check` · `site_parity.py --selftest` then `site_parity.py` ·
   `build_css.py --selftest` then `--check` · `image_audit.py --selftest` then `--check` ·
   `strip_inline.py --selftest` then `strip_inline.py --verify`.
5. If `flatten_alpha --selftest` prints `NOT FULLY TESTED`: `pip install cairosvg
   --break-system-packages`. **Needed every session.**
6. `--anomalies` is SILENT when clean. Anything it prints is a real lead.
7. **Do not hand-type a version.** `session_versions.py --live` / `--handoff` EMIT the blocks.
8. Entrypoints are traps: `lesson_inventory.build(path)`, `gen_component.load_standard()`,
   `svg_layout_audit.audit(path)`, `flatten_alpha.flatten(path)`, `build_worklist.build(dir)`,
   `regex_audit.audit(paths)`, `session_versions.bible_consistency(path)`,
   `build_css.build(paths)`, `image_audit.audit(paths)`, `strip_inline.build(paths)`.
9. **A CLONE IS NOT THE SITE.** Run `site_parity.py` after any push.
10. **VERIFY THE PUSH BY FRESH CLONE AND MD5** — and see §1 above about which clone.

---

# STATE

Fresh-clone verified at **`d9332d2`**. Census **40,025**.
Bible **v8.97** · `BookComponentStandard` **v01.12.1** · Maker **v2.45.1** ·
`marks/` **41** · `icons/` **49** incl. LICENSE.
`ZUMO_Syllabus_WORKING.md` **v1.0**.

Instruments: `book_gates` **v1.39.0** · `lesson_inventory` **v1.2.0** ·
`gen_component` **v1.6.1** · `pill_sweep` **v1.0** · `gate_payload_match` **v1.6** ·
`build_family_map` **v1.1.3** · `build_mark_index` **v1.0.2** · `gen_bonus_banner` **v1.3.0** ·
`gen_part_banners` **v1.0** · `session_versions` **v1.14.1** · `fit_raster_svg` **v1.2** ·
`flatten_alpha` **v1.2** · `svg_layout_audit` **v1.19** · `site_parity` **v1.1** ·
`build_css` **v1.2.1** ·
`image_audit` **v1.1** ·
`strip_inline` **v1.1** ·
`build_worklist` **v1.1** ·
`regex_audit` **v1.0** ·
`font_stack_sweep` **v1.1.0** ·
`going_deeper` **v01.2.0**.

Lessons: L01 v03.18.0 · L02 v03.10.1 · L03 v03.23.1 · L04 v04.18.1 · L05 v04.18.1 · L06 v04.22.1 · L07 v04.20.1 · L08 v04.18.1 · L09 v05.15.1 · L10 v02.15.0 · L11 v02.16.0 · L12 v01.18.0 · L13 v02.16.0 · L14 v02.20.0 · L15 v02.16.0 · L16 v02.11.0.
**45/45 gates.** Four pushes in S108, all verified clean.

---

# THE ONE THING TO CARRY OUT OF S108

**VERIFYING ON THE WORKING TREE IS NOT VERIFYING THE PUSH.**

The panel unification retired five stylesheet rules. That reordered `build_css`'s
frequency ranking and **re-spelled classes in L02–L09 — eight lessons nobody edited.**
My working tree was internally consistent and 45/45. The nine-file push I was about to
hand DJ would have shipped `div-3498db-3` into a lesson with no rule behind it.

It was caught ONLY because DJ said *"double check first"* and I rebuilt the tree he would
actually create — **pushed clone + staged files** — and ran the gates there. Five failed.

**The rule: after any change that regenerates `css/book.css`, stage into a copy of the
pushed clone and run `book_gates` THERE before presenting md5s.** The working tree cannot
see this class of defect by construction. This is `strip_inline`'s own S105 lesson
(46 names kept their spelling and changed their meaning) arriving from a new direction.

**Second, smaller:** a shallow clone served a stale HEAD twice while the remote was ahead.
`git ls-remote HEAD` before trusting any verification clone. Now step 1 of the ritual.

---

# S108 WORK — the banner arc, applied

**Bible now v8.97** (the prior state is recorded in its own changelog). §6.5's LOCKED icon rule SUPERSEDED · NEW §6.5b eyebrow/headline
canon incl. the fence rule · NEW §6.5a-T type treatment E · §4.5's mark superseded, word
retained · §6.9 `image-index` → `figures` ×3 · §6.5 Box confirmed and unified.

- **237 caps on F1**, zero glyphs. 189 carry an eyebrow; the other 48 are Glossary /
  Quick Reference / Figures × 16. Verified by DOM lookup, not regex.
- **Type E body treatment.** Inter served the way the front door already serves it; the
  Windows-only Segoe stack retired after eleven sessions of `font_stack_sweep` reporting
  0 rewrites because it never opened `css/book.css`. Census +32, exactly two lines × 16.
- **Panel ruling A.** 104 panels unified, five duplicate rules collapsed.
- **`going_deeper` v01.2.0** — six anchor ids at last, entry 5 → *Using Fixed Point*,
  four lesson pointers deep-linked. L02/L12/L16 correctly stay at the top: each names
  two or three entries.

## THE RAMP WAS PILOTED AND REVERTED — read before re-attempting

§5.0.1's Heritage Blue band ramp applied to L03 alone fired **seven gates**. The finding
is structural and will not change: **it cannot be piloted on one lesson.**

Five constructs are byte-compared across all sixteen and move together or not at all:
**lesson strip (§6.5a) · hero (§25.6) · PART dividers (§6.8) · bonus cap (§4.5) ·
FINISHED EARLY box (§4.5a)**. Three more gates hard-code `#6c757d` — §25.10h's Brain Check
panel test and both bonus gates. Rules went 660 → **694** as L03 diverged, re-creating the
duplicate-rule state Panel A had just collapsed.

**Sequence for the real attempt: instruments FIRST, then all sixteen in one pass.**

Also caught: a global dark-hex substitution over-reached into a callout and tripped §5.1's
off-canon border gate. Scope the sweep to the role, not the string.

**DJ rulings already banked for that arc:**
- Bands → the §5.0.1 ramp: Frost `#CBD3DE` §1–3 · Mist `#AFBCCE` §4–6 · Fog `#96A8C0`
  §7/8/8A · Harbor `#7E95B4` §9 · Steel `#708BAF` §10+
- Cap text white → Deep Navy `#162337`
- **h3 subheadings → BRONZE `#725637`** (DJ: *"I agree bronze"*) — the palette's warm axis,
  contrast 6.5 on white. Note the current h3 colours run 3.15–4.92, and blue `#3498db` at
  **3.15 is below the 4.5 floor** — this is a live contrast defect, not only aesthetics.
- Callout `border-left` accents **do not move** — semantic; the bands moving away is what
  resolves the 78-callout collision.
- Challenge-card gradient and in-text link colour: unruled, left alone.
- Table headers: unruled. Deep Navy on Parchment was proposed, never ruled.

---

# S109 QUEUE

## Ruled, not yet applied
- **L02's `#d1ecf1` callout** — provisional fix so it sits with today's `#3498db`. It is the
  only pale-blue block in the book, and it is the collision §5.0.1's 30° rule predicts.
- **§2 Learning Objectives contents vary** (DJ found this by eye, and he was right):
  checkboxes in 14 of 16 — **L01 and L15 have none**; seven lessons embed an extra coloured
  callout in four different colours; three different icons (🎯 L02 · 🔑 L05/L06 · 📘
  L07/09/10/14); item counts 6–11. This is authoring, not CSS.

## Parked with a price
- **§26, now correctly scoped as THREE LAYERS**, not "the repaint": page colour (Parchment,
  not rendered) · section bands (the ramp, not rendered) · callout semantics (rendered, 31
  accent colours for 30 families). Brand owns the top two; the book owns the third.
  **78 callouts currently wear a section colour**, which is the disease §5.0.1 exists to cure.
- **A 17th section — Prerequisites** (DJ, S108, *"just a thought, don't have to deal with it
  now"*). ⚠️ **"17th" does not match a count I can find** — the spine is §1–§10 plus §8A
  (eleven core) and 15 caps per lesson. Pin what is meant before anyone builds it.
  **Cost note: at the FRONT it renumbers the whole spine** — fences, gate 27's core tuple,
  §6.9's ID order, nav pills, F1 eyebrows. At the back it is nearly free.
- `css/book.css` has 172 distinct colours and zero custom properties, while `index.html` and
  `going_deeper.html` each carry a 12-token `:root`.
- Gradients: 134 instances, 7 strings, 17 pages, 18 SVGs. Unruled.
- **Consolas in `css/book.css`: 15 declarations, ALL of them with a fallback** — six
  `Consolas, monospace`, four `'Consolas', monospace`, three `'Consolas','Monaco','Courier
  New',monospace`, and one each of two Monaco variants. **Zero bare.** The standing note that
  parks these as harmless browser CSS is CORRECT and needs no revisiting.
  ⚠️ **§24.6c — I asserted the opposite at S108 and DJ's last-check request caught it.**
  `font_stack_sweep` prints `8 x Consolas -> Courier New, monospace`, and I read the label as
  *"8 declarations that are bare Consolas."* It is not: the sweep groups by FIRST FACE, so
  those 8 are every declaration whose first face is Consolas, fallbacks included. **A tool's
  grouping label is not a finding.** The real spelling variance (five ways to write one stack)
  is a tidiness item, not a substitution risk.

## Instrument work
- **Orphan gate, re-scoped** — byte-match against `images/`, not filename patterns.
- `font_stack_sweep` reads only the first face; teach it every named face, and to reject a
  quoted family containing a comma.
- `pill_sweep` and `gen_part_banners` still have no selftest.
- `_ctm` still discards `rotate()`/`matrix()`; `regex_audit` reports 1 lead across 23 files.

## Canon debts
§21.1's thresholds live only in `book_gates.py` · §25.6 header example · §25.10e misfiled ·
challenge-card redesign Part B · difficulty-progression audit · Maker batch · L01 VS Code
multi-root step · Stage Two two blocks labelled `Learn/Insight` (L03, L09) ·
`ROBOLORE_UPSTREAM_DELTA_S102.md` written and unapplied · robolore.com hosting ·
`PUSH_WORKFLOW.md`: a repeat download of the same repo filename makes `(1)` the NEW file.

## Bench (need the robot)
Q017 L09 six numbers · Q044 calibration-spin · Q046 gyro-bias · L02 §5 green-LED ·
Constrain RUN_MS · cm/s at a stated BASE_SPEED.

---

# ⏰ IMAGES — STILL THE ONLY DEADLINE

**SEPTEMBER 8 IS FIVE WEEKS OUT.** 19 outstanding of 145. Seven are due in periods 2–4,
week one: `2.5` · `VIDEO 3.1` · `3.2` · `3.4` · `3.5` · `3.6` · `3.14`.
**Still offered, still not built:** a shot brief for those seven, so one bench session with
the robot clears all of them. Cheapest item on the list is `[IMAGE 7.13]` — *"diagram showing
final project structure"*, a diagram tagged as a photo, while L07 already ships two such
graphics. **One ruling may delete a row.** Do not draw it without DJ.

**After Sept 8:** "What the F()" (going_deeper entry 2, DJ's own park) · L02 §1 whodunit
restructure · IMAGE + GRAPHIC → one FIGURE space.

---

# PUSHING — READ THIS

Named-file CLI for adds and modifies; **GitHub Desktop for deletions.** **Never `git add .`**

**Stage into a copy of the PUSHED CLONE and run the gates there before presenting md5s.**

1. **`(1)` does not mean stale.** Verify by **md5**, never by suffix.
2. **Never present a test file in the same list as repo files.**
3. **`going_deeper.html` landed in `lessons/` once in S108** — the §25.6a defect, caught by
   gate 22. It belongs at the repo ROOT.

---

# PUSH LIST FOR THIS SESSION'S CLOSE

| Action | File | Note |
|---|---|---|
| upload | `ZUMO_SUPER_BIBLE.md` | **v8.97** |
| upload | `ZUMO_S109_HANDOFF.md` | this file |
| upload | `LIVE_ZUMO_TEXTBOOK.md` | **regenerate LAST**, versions EMITTED not typed |
| **delete** | `ZUMO_S108_HANDOFF.md` | §12.2 — gate 28 enforces exactly one |
