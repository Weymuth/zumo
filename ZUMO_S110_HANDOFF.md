# ZUMO — S110 HANDOFF (written at S109 close · paste at top of Session 110)

## Session open ritual (do this without being asked)
1. **`git ls-remote https://github.com/Weymuth/zumo.git HEAD` FIRST.** If the clone's `git log -1`
   does not match, fetch the sha by name (§12.4, *caches lie*).
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
10. **VERIFY THE PUSH BY FRESH CLONE AND MD5.**

---

# STATE

Fresh-clone verified at **`fedb9ef`**. Census **40,025**.
Bible **v8.98** · `BookComponentStandard` **v01.12.1** · Maker **v2.45.1** ·
`marks/` **41** · `icons/` **49** incl. LICENSE.
`ZUMO_Syllabus_WORKING.md` **v1.0**.

Instruments: `book_gates` **v1.39.2** · `lesson_inventory` **v1.2.0** ·
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

Lessons: L01 v03.18.0 · L02 v03.10.2 · L03 v03.23.2 · L04 v04.18.1 · L05 v04.18.1 · L06 v04.22.1 · L07 v04.20.2 · L08 v04.18.1 · L09 v05.15.1 · L10 v02.15.0 · L11 v02.16.0 · L12 v01.18.0 · L13 v02.16.0 · L14 v02.20.0 · L15 v02.16.0 · L16 v02.11.0.
**45/45 gates.** Three pushes in S109, all verified clean. `--anomalies` silent, family map
1048/1048, 0 dead classes, parity holding.

---

# ⚠️ FIRST THING IN S110 — DJ ASKED FOR THIS BY NAME

**More warm-earth-adjacent palette options.** DJ ruled warm earth (specimen A) and then asked to
see the range before committing: *"I like the muted feel, but i want to see what else is
possible."* Build several muted directions, same page content in each so only the palette varies,
every hex contrast-checked in code before he sees it.

**The muted quality comes from LOW SATURATION, not from any particular hue** — so the range is
wider than "earth tones" suggests. Suggested directions: deeper/moodier earth · muted-cool bands
with warmth kept in the tints · sun-faded lighter · and one pulling Heritage's bronze/parchment
into a warm frame, since **warm earth is currently the furthest of the three specimens from
RoboLore canon** and that one direction would reconcile book and brand.

---

# THE ONE THING TO CARRY OUT OF S109

**§24.13 IS NEW CANON AND I BROKE IT IN THE SAME SESSION I WROTE IT.**

*Re-derive, do not re-read — and a list presented in prose is not the list.*

A 17-family callout taxonomy was computed correctly in code, printed `CORE CONCEPT 60` with
`unaccounted: 0`, then **hand-typed into a chat message** as an 11-row table with INSIGHT's 60
blocks dropped in the retyping. The next build read **the chat message** rather than the verified
structure. Three passes over that table found nothing, because all three were re-readings — and a
list with a member missing looks complete from the inside (§24.8, failed). One line caught it:
`assert tot + rem == 1048`.

**DJ's words, which are the entry:** *"So when I say double check you don't double check?"*

The distinction to hold: **re-reading is not checking.** A second look at the same artefact is the
same instrument run twice. A check is a DIFFERENT METHOD or an ASSERT against a number the
artefact cannot supply. Do not use the word *verified* for anything else. And the rule proved
itself twice more the same session — bumping the Bible surfaced a **third** version home nobody
knew about (a changelog list at line 98, separate from the `Current:` field), caught by
`bible_consistency()` and invisible to re-reading; and an md5 comparison script reported a false
MISMATCH because `sed 's|.*/||'` ate the hash along with the path, caught only by printing both
sets before speaking.

---

# S109 WORK

**The Bible advanced one moderate step, adding §24.13.** Three version homes now agree, asserted by parser.

**Six INSIGHT blocks repainted.** All carried INSIGHT's canonical magnifier while wearing five
non-canon paints across L02/L03/L07 — and three were borrowing **other families' canon**: TIP's
`#f0f7f0`/`#6b8e6b`, What-You-Should-See's `#d1ecf1`/`#17a2b8`, Checkpoint's `#4caf50`. Canon
31 → 37, non-canon magnifier blocks 0, INSIGHT's paint spread 11 → 6. Three stylesheet rules died
and **all three had zero Bible mentions**; every canon paint touched survived because other
families still hold it. The remaining five INSIGHT paints are RULED and were left alone (L11's ✅
and L12's 🏆 are S94's success-green payoff blocks; L13/L14's 💭 are `THE ONE IDEA`, hard-coded in
`build_family_map` line 75). Verified in a staged copy of the pushed clone: 13 lessons byte-
identical through restore→regenerate→apply, all 30 family counts unchanged.

**`book_gates` v1.39.0 → v1.39.2.** Gate §27.11's printed label was hard-coded and stale at
664/2,434 while its constants tested 660/2,418 — right test, wrong name — now DERIVED. And
**`BAND_END`** names the §10+ band, previously typed literally in **eleven** places (five inline
sites + six `GEOM_BASELINE` keys). Refactor asserted behaviour-neutral by byte-identical gate
output, then control-run by flipping it to Steel `#708BAF` — because byte-identical is also what a
DEAD constant produces (§24.8). **The flip fires FOUR gates: §25.10h, §4.5, §4.5a and §5.1.**
The S108 handoff said three and missed §5.1's `GEOM_BASELINE` keys, which would have fired
mid-ramp with no warning.

---

# THE VISUAL ARC — READ THE SPEC, IT IS THE SESSION'S REAL PRODUCT

**`ZUMO_S109_VISUAL_SPEC.md`** (repo root, new). Seven rulings with DJ's words attached, palette
hexes with measured contrast, nav mechanism, and **six open items**.

**The ruling that reframes everything, DJ S109:** *"I'm not expecting the kids to memorize that
burgandy is note, red is warning. I just want the book to be visually appealing and not boring."*

**COLOUR IS NOT A CODE.** Every callout's label already says `WARNING` or `KEY TERM` in words;
swapping colours between blocks loses nothing. Therefore families may SHARE colours, the palette
can be small, and **family count is an authoring question, never a palette question.** Half of
S109 was spent optimising against a constraint that did not exist — solving "N families need N
distinguishable colours," which is exactly what produced a 14-hue rainbow DJ rejected as *"truly
hurts my eyes."* Only WARNING red is exempt: cultural, not learned.

**Ruled:** warm earth · six groups (five expandable + Troubleshoot standalone, unnumbered) ·
vertical left rail · `<details>` with no JavaScript · **no section numbers in the nav, numbers stay
on the page** (nav is for finding, the page is for referring to) · bronze `#725637` headings.

**Bronze is a defect fix, not taste:** today's heading colours run 3.15–4.92 and **341 of 814
heading uses are below the 4.5 floor.**

**⚠️ THIS SUPERSEDES THE HERITAGE BLUE BAND RAMP.** §5.0.1's Frost/Mist/Fog/Harbor/Steel was built
for five blue bands the book will no longer have. **`BAND_END` survives as the mechanism** and the
bronze ruling survives; the five specific blues do not. §5.0.1 needs superseding the way §6.5's
icon rule was superseded in S108 — do not re-litigate the ramp, and do not delete `BAND_END`.

**Cost of the rail, measured:** `.nav` is ONE class with ONE rule, so it is **~4 rules in
`css/book.css` and ZERO lesson files** — the S103 migration paying off. A media query is
mandatory below ~700px.

---

# CALLOUT CONSOLIDATION — RULED-READY, NOT RULED

**`ZUMO_S109_CALLOUT_CONSOLIDATION.md`** (repo root, new). **30 families → 12**, asserted:
1,030 blocks in 12 moments + 18 leaving = 1,048.

Built by reading the **bodies** of 188 stratified blocks, not labels — labels misled twice and both
errors are recorded in §6 of that document. Roughly **1 in 10** sampled blocks sits in the wrong
family; NOTE is the largest share because it is the residue bucket (133 blocks, no defining job).

**Leaving the callout taxonomy entirely:** `(card header)` 9 (§7.2 mark, ruled S94) · MYSTERY 5 ·
ANSWER 4. **MYSTERY is an L10 authoring deviation** — L08/L09/L11–L15 mark mysteries as
`data-kind="bonus-sabotage"` CARDS, and **L10 carries both**, 5 cards *and* 5 callouts. Verified
two ways.

**Unresolved and blocking the final number:** the **NOTE split**. 133 blocks need per-block
disposition across at least four destinations (EXPLAIN · CORE CONCEPT · FAIL ON PURPOSE · HOW THIS
SECTION WORKS). Also open: whether DEFINE belongs in the callout system at all — 184 blocks, 165
distinct term-and-definition entries, which is a glossary rendered inline.

**Two families have no equivalent in standard publisher taxonomies and should be kept
deliberately:** FAIL ON PURPOSE (THE WALL, 17) and VERIFY's byte-count half (STILL GREEN, 17).

---

# S110 QUEUE

## Live thread
- **Warm-earth palette variants** (above — DJ asked by name, do this first)
- Rule the 12 families, then run the NOTE per-block pass so dispositions have fixed destinations
- Verify **`div-d-flex-2` scope** before any rail work — if used outside the nav, flipping it to
  column hits other blocks, the exact over-reach that killed the ramp pilot. Ten minutes.
- Nav `<details>` carry **no `data-reveal`** — the tutor queries `<details>` and §20.1 strips by
  type. **§25.12 exists because one untyped `<details>` slipped through before.** Needs a ruling.

## Ruled, not yet applied
- §2 Learning Objectives contents vary — checkboxes in 14 of 16 (**L01 and L15 have none**), seven
  lessons embed an extra coloured callout in four colours, three different icons, counts 6–11.
  Authoring, not CSS.
- Three of L12's 🏆 INSIGHT blocks are byte-count reports (*"21,342 → 24,534 bytes"*) and S94 sends
  byte-count blocks to STILL GREEN. Classified by glyph+paint, so the generator cannot see it.

## Instrument work
- Orphan gate re-scoped to byte-match against `images/`, not filename patterns
- `font_stack_sweep` reads only the first face; teach it every named face
- `pill_sweep` and `gen_part_banners` still have no selftest
- `_ctm` discards `rotate()`/`matrix()`; `regex_audit` reports 1 lead across 23 files

## Canon debts
§21.1's thresholds live only in `book_gates.py` · §25.6 header example · §25.10e misfiled ·
challenge-card redesign Part B · difficulty-progression audit · Maker batch · L01 VS Code
multi-root · Stage Two two blocks labelled `Learn/Insight` (L03, L09) ·
`ROBOLORE_UPSTREAM_DELTA_S102.md` written and unapplied · robolore.com hosting ·
§6.5's "nav button count is 12–14" becomes **obsolete** under the six-pill rail — retire, don't argue
· `css/book.css` has 172 colours and zero custom properties · gradients 134 instances, unruled ·
Consolas: 15 declarations, **all with a fallback, zero bare** — the standing note is CORRECT, do not
revisit.

## Bench (need the robot)
Q017 L09 six numbers · Q044 calibration-spin · Q046 gyro-bias · L02 §5 green-LED ·
Constrain RUN_MS · cm/s at a stated BASE_SPEED.

---

# ⏰ IMAGES — STILL THE ONLY DEADLINE, AND IT DID NOT MOVE IN S109

**SEPTEMBER 8 IS FIVE WEEKS OUT.** 19 outstanding of 145. Seven due in periods 2–4, week one:
`2.5` · `VIDEO 3.1` · `3.2` · `3.4` · `3.5` · `3.6` · `3.14`.

**Still offered, still not built:** a shot brief for those seven, so one bench session with the
robot clears all of them. Cheapest item is `[IMAGE 7.13]` — *"diagram showing final project
structure"*, a diagram tagged as a photo while L07 already ships two such graphics. **One ruling
may delete a row.** Do not draw it without DJ.

The visual arc is good work and is NOT on a clock. The images are.

---

# PUSHING — READ THIS

Named-file CLI for adds and modifies; **GitHub Desktop for deletions.** **Never `git add .`**

**After any change that regenerates `css/book.css`, stage into a copy of the PUSHED CLONE and run
`book_gates` THERE before presenting md5s.** The working tree cannot see class re-spelling by
construction (S108).

1. **`(1)` does not mean stale.** Verify by **md5**, never by suffix.
2. **Never present a test file in the same list as repo files.**
3. **Never produce PUSH_ME_*.md or MD5_*.txt.** Checksums and instructions go in the CHAT ONLY.
4. `going_deeper.html` belongs at the repo ROOT, not in `lessons/`.

---

# PUSH LIST FOR THIS SESSION'S CLOSE

| Action | File | Note |
|---|---|---|
| upload | `ZUMO_S110_HANDOFF.md` | this file |
| upload | `LIVE_ZUMO_TEXTBOOK.md` | **regenerate LAST**, versions EMITTED not typed |
| **delete** | `ZUMO_S109_HANDOFF.md` | §12.2 — gate 28 enforces exactly one |
