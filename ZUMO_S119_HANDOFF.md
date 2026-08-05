# ZUMO — S119 HANDOFF (written at S118 close · paste at top of Session 119)

## Session open ritual (do this without being asked)
1. **`git ls-remote https://github.com/Weymuth/zumo.git HEAD` FIRST.** If the clone's
   `git log -1` does not match, fetch the sha by name (§12.4, *caches lie*).
2. Read `LIVE_ZUMO_TEXTBOOK.md` — verify date / status / versions.
3. **Do NOT grep the Bible version.** `session_versions.bible_consistency()` parses it.
4. Run, and **READ THE EXIT CODE, NOT THE LAST LINE**:
   `book_gates.py` · `gen_component.py --selftest` · `lesson_inventory.py` ·
   `lesson_inventory.py --anomalies` · `pill_sweep.py --selftest` ·
   `pill_sweep.py --audit lessons/Lesson_*.html` · `build_family_map.py` ·
   `class_sweep.py --selftest` · `fit_raster_svg.py --selftest` · `flatten_alpha.py --selftest` ·
   `svg_layout_audit.py --selftest images/L01_GRAPHIC_1-13_zumo_rear_view.svg` ·
   `regex_audit.py --selftest` then `regex_audit.py` · `build_worklist.py --selftest` ·
   `font_stack_sweep.py --selftest` then `font_stack_sweep.py` ·
   `session_versions.py --selftest` then `--check` · `site_parity.py --selftest` then `site_parity.py` ·
   `build_css.py --selftest` then `--check` · `image_audit.py --selftest` then `--check` ·
   `strip_inline.py --selftest` then `strip_inline.py --verify` ·
   `build_palette.py --selftest` then `--check` ·
   `color_index.py --selftest` then `--check` ·
   `gen_bonus_banner.py --selftest` · `gen_part_banners.py --selftest` ·
   `gate_payload_match.py newproject.html lessons/Lesson_*.html`
5. If `flatten_alpha --selftest` prints `NOT FULLY TESTED`: `pip install cairosvg
   --break-system-packages`. **Needed every session.**
6. **NEVER run `build_css.py --help`.** It has no help branch — it BUILDS, against whatever
   tree is on disk. §27.8b's order is not optional and the tool will let you skip it silently.
   **`session_versions.py --help` has no help branch either** — it prints the version table.
   Harmless, but it is not documentation.
7. `--anomalies` is SILENT when clean. Anything it prints is a real lead.
8. **Do not hand-type a version, and do not hand-type a COUNT.** `session_versions.py
   --live` / `--handoff` EMIT the blocks.
9. Entrypoints are traps: `lesson_inventory.build(path)`, `gen_component.load_standard()`,
   `svg_layout_audit.audit(path)`, `flatten_alpha.flatten(path)`, `build_worklist.build(dir)`,
   `regex_audit.audit(paths)`, `session_versions.bible_consistency(path)`,
   `build_css.build(paths)`, `image_audit.audit(paths)`, `strip_inline.build(paths)`,
   `build_palette.build()`, `class_sweep.sweep(paths)`, `color_index.index(paths)`.
   **`lesson_inventory.build()` runs `expand_classes()` first, so every `off` it reports is an
   offset into the EXPANDED source, not into the file on disk.** Slicing the raw file by those
   offsets silently returns the wrong region — or an empty one. Expand first, then slice.
10. **A CLONE IS NOT THE SITE.** Run `site_parity.py` after any push. It can FAIL on the first
   run in the minute after a push and pass on retry — that is Pages lag, not a defect (S112).
   Seen twice at S118, both transient, both on a different asset.
11. **VERIFY THE PUSH BY FRESH CLONE AND MD5 — AND DIFF THE STAGE AGAINST THE CLONE.**
12. **The lesson files are `Lesson_NN.html`, no topic suffix.** Use the glob.
   **And they live in `lessons/`.** S117's whole conversion was pushed to the repo ROOT and
   the site served the pre-conversion L12 until S118 caught it — see below.

---

# ⏰ SEPTEMBER 8 IS ABOUT FOUR AND A HALF WEEKS OUT

**14 images outstanding of 141.** Unchanged. DJ has parked photography. The seven rulings
under S114's table are still the cheapest board item and none needs a camera to DECIDE.

**ONE LESSON LEFT TO CONVERT: L15.** L13 closed at S118. L15 is the last, and S117 measured
it as all-authoring: **no checklist, no Knowledge Check, a narrative §10** (*What you built.*).
Expect BC01/BC03/BC04 authored from nothing, as on L13.

**CHECK L15's §2 OBJECTIVE PHRASING BEFORE PLANNING BC02.** L15 shows **zero ☐ objectives** in
the §2 survey — the same reading L01 gives — so §25.5's "migrate the objectives" step may have
nothing to migrate. Measure it first; L13 proved this is where the surprise lives.

---

# THE FIRST THING S118 DID, AND IT WAS NOT ON THE QUEUE

**S117's L12 CONVERSION WAS PUSHED TO THE REPO ROOT INSTEAD OF `lessons/`.**

`Lesson_12.html` sat at the root at v01.20.0 — 133,996 B, linked by nothing, reachable at a
public 200 — while `lessons/Lesson_12.html` was still **v01.19.1**, the pre-conversion file, and
**that is what the site served**. `css/book.css` had gone up correctly, so the stylesheet was at
the S117 state and the lesson that consumes it was not.

**Seven gates failed and every one named the same cause**: §25.2 (*L12 left §25 scope silently*),
§12/§23 (*STRAY page*), §25.10h (11 of 12 scanned), §21 (235 refs, expected 240), §27 (`div-ddd-3`
used with no rule — the class S117 deleted, still live in the old file), §27.13, §24.14 (1057/1061).
`session_versions --check` named it in one line: `L13… written=v01.20.0 files=v01.19.1`.

**The fix was a file move, controlled both ways: 41/48 broken → 48/48 passing.** No version bump
and no LIVE.md edit were needed, because the content was already v01.20.0 and both docs already
claimed it — the file simply was not where they said it was.

**WHAT MAKES THIS WORTH CARRYING.** LIVE.md recorded *"Verified by fresh clone at `b307865`"* —
a commit that PREDATES the commit carrying the work. The verification named the wrong object.
**A push is verified against the tree you intended to push, not against the last sha you wrote
down**, and rule 11 above exists because matching md5s did not catch S115 either.

---

# STATE

Fresh-clone verified at **`UNKNOWN`**. Census **40,780**.
Bible **v8.107** · `BookComponentStandard` **v01.12.1** · Maker **v2.45.2** ·
`marks/` **41** · `icons/` **49** incl. LICENSE.
`ZUMO_Syllabus_WORKING.md` **v1.2**.

Instruments: `book_gates` **v1.44.4** · `lesson_inventory` **v1.2.0** ·
`gen_component` **v1.6.1** · `pill_sweep` **v1.1** · `gate_payload_match` **v1.7** ·
`build_family_map` **v1.3.6** · `build_mark_index` **v1.0.2** · `gen_bonus_banner` **v1.4.1** ·
`gen_part_banners` **v1.2** · `session_versions` **v1.17.0** · `fit_raster_svg` **v1.2** ·
`flatten_alpha` **v1.2** · `svg_layout_audit` **v1.20** · `site_parity` **v1.1** ·
`build_css` **v1.2.1** ·
`image_audit` **v1.1** ·
`strip_inline` **v1.1** ·
`build_worklist` **v1.1** ·
`regex_audit` **v1.0** ·
`build_palette` **v1.1** ·
`class_sweep` **v1.0** ·
`color_index` **v1.0** ·
`font_stack_sweep` **v1.2.0** ·
`going_deeper` **v01.4.1**.

Lessons: L01 v03.19.2 · L02 v03.11.2 · L03 v03.28.1 · L04 v04.19.2 · L05 v04.19.3 · L06 v04.23.3 · L07 v04.22.2 · L08 v04.19.3 · L09 v05.16.3 · L10 v02.17.1 · L11 v02.18.1 · L12 v01.20.1 · L13 v02.18.0 · L14 v02.22.1 · L15 v02.17.1 · L16 v02.12.1.

**48/48 gates.** `--anomalies` silent · family map **1065/1065** · `regex_audit` 0 leads ·
`build_css --check` current at **643 rules** · 0 dead classes · `color_index --check` clean ·
`build_palette --check` matches the ruling · `image_audit --check` current at 14 outstanding
of 141 · both banner generators green · `gate_payload_match` PASS.

---

# THE ONE THING TO CARRY OUT OF S118

**AN ASSERT THAT CANNOT SUCCEED IS THE MIRROR OF AN ASSERT THAT CANNOT FAIL — AND BOTH READ AS
EVIDENCE.**

S117 canonized the disk read-back. S118 added it to every control and **the control still
misfired twice, in two different ways the read-back cannot see.**

**Misfire 1 — the injection landed and the gate stayed silent.** Deleting a
`<details data-reveal="quiz">` from L13 dropped the reveal count by one, the read-back confirmed
it, and §24.14 said nothing — because **a reveal is not a callout the family map counts.** This
is S117's third attempt repeating verbatim. The read-back proves *something moved*; it cannot
prove the thing that moved is the thing the gate measures. **Ask the generator what it counts.**
`build_family_map` iterates `inv['callouts']` from `lesson_inventory` — so the control target is
whatever that list holds, and the correct injection was a Brain Check container div, verified by
a parsed callout count of 22 → 21.

**Misfire 2 is new and it is the nastier one.** The landed-assert was
`assert 'brain-check-04' not in back` — which is **ALWAYS FALSE**, because the Brain Check column
carries nav links to that anchor. A perfectly correct injection would have been reported as a
failed one, and the natural next move is to "fix" the injection until the assert passes, which
means editing the control until it agrees with a wrong belief. The right assert scoped the string
to what it actually meant: `id="brain-check-04"`.

**§24.8 applied to the assert itself: if the injection had landed perfectly, would this assert
look different?** For misfire 2 the answer was no. That is the test, and it is not the same test
as the read-back.

---

# S118 WORK — L13, THE THIRTEENTH CONVERSION

| Block | Ancestor | Price |
|---|---|---|
| **BC01** | **none** — 0 pre-§6 reveals of ANY type (the first is a §6 `catchup`), 0 `check`, 0 `quiz`, 0 TRY IT | 5 authored, §3 → §4.1 → §4.2 → §4.3 → §5.1, every citation read and verified to CONTAIN its answer |
| **BC02** | §2's six objectives — **reworded verb-first first**, see §25.10k | 6 migrated, equality ASSERTED, literal ☐ |
| **BC03** | **none** — no Knowledge Check, no Reflection Questions | 5 authored, citing §5.2 · §8A.2 · §3 · §5.3 · §8A.3 |
| **BC04** | **none** | 3 prompts authored, no reveals |

L13's §3 is **FLAT — no subsections at all**, unlike L11's and L12's five §3.x, so BC01's
§-ordering runs across §3, §4 and §5 rather than down one section. The *Inventory* prose and the
*Next:* pointer stay OUTSIDE the family and reseat after BC04 (L10's arrangement); Engineer's Log
survives as its own block.

**Three baselines moved, each controlled in both directions:**

| Baseline | Move | Control |
|---|---|---|
| §21 image coverage | 240 → **245** | sole delta `BrainGear_Incomplete.png` 60 → 65 |
| family map | 1061 → **1065** | exactly ONE family moves, BRAIN CHECK 48 → 52; other 29 byte-identical |
| §27.11 digest | → `ee0c8ac2039bc90e` | rules/decls **UNCHANGED** at 643/2,357, zero born, zero died |

**THIS ONE IS A CLASS RENAME — S115's SHAPE.** `.ul-ls-none-2` and `.ul-ls-none-3` **swapped
declaration sets** (same spelling, different meaning) because `build_css` ranks by usage count and
BC02's list moved the counts. **TEN lessons differ from the pushed clone, not one.** L05–L12 and
L14 changed by NAME ONLY — proved two ways, a line diff showing all 44 changed lines touch only
those two class names, and an expansion through each tree's own stylesheet returning
byte-identical for all nine. Nine minor bumps, every visible banner asserted unmoved.

---

# S119 QUEUE

## The conversion arc — one left
- **L15**, the last. All-authoring. **Measure its §2 first** (see above).
- **Revisit the L14 → L15 → L16 flow** (DJ ruling S115, queued deliberately, still untouched).
- **L10's `What You Built` is the only non-Brain-Check `<h4>` in a converted §10.** L13's
  equivalent is unheaded prose; L15's is *What you built.* Worth one look across all thirteen.
- **S116's past-tense question is now decidable or retirable.** It did not recur on L12 or L13,
  and L13 had no checklist at all. L15 is the last chance for it to recur; if it does not,
  **retire it deliberately rather than carrying it a fifth session.**

## Rulings outstanding — carried
- **Should `build_family_map` parse its total instead of holding a baseline?** **Fifth hand edit
  of that literal in five sessions** (1049 → 1053 → 1057 → 1061 → 1065). One conversion left
  means one more. The cost of parsing is that gate 47 stops noticing an added or deleted callout.
- **Should `build_css` name rules by usage RANK at all?** New at S118 and the same shape as the
  above. Ranking is why two class names swapped meanings and nine innocent lessons were rewritten.
  A content-derived name would make a rename impossible; the cost is churn on every existing name.
- **The `#666` footer colour** — 18 declarations, eight `.p-c-666*` families whose NAMES encode the hex.
- **16 uppercase-only colours** — 197 occurrences, no variance, unruled.
- **`font_stack_sweep` rule** — Consolas: 15 declarations, all with a fallback, zero bare. The
  standing note is CORRECT and the tool disagrees. A genuine rule disagreement.
- **Callout colours re-examined** — v8.87's Scope C. Safe now: family no longer depends on colour.
- **`3.2` vs `3.5`** — before/after split, or one figure and a deleted row.
- **NOTE per-block pass** (133 blocks, four destinations).
- **Nav `<details>` carry no `data-reveal`** — §25.12 exists because one untyped `<details>` slipped.
- **Selftest-coverage gate** — offered, not built.
- **The seven remaining figure tags** — S114's table. Seven rulings, no camera needed to rule.

## Ruled, not yet done
- **`[IMAGE 3.6]` → §22 terminal block, ONCE THERE ARE REAL NUMBERS.** Do not write it from imagination.
- **Apply GPT Task 2 and Task 4** — *if DJ still has the S112 outputs.* Not in the repo.

## Canon debts
§21.1's thresholds live only in `book_gates.py` · §25.6 header example · §25.10e misfiled ·
challenge-card redesign Part B · difficulty-progression audit · Maker batch · L01 VS Code
multi-root · Stage Two two blocks labelled `Learn/Insight` (L03, L09) ·
`ROBOLORE_UPSTREAM_DELTA_S102.md` written and unapplied · robolore.com hosting ·
§6.5's "nav button count is 12–14" is **obsolete** under the six-pill rail — retire, don't argue ·
`css/book.css` has zero custom properties (`build_palette --css` emits them ready) ·
**26 gradient definitions across 18 SVG files** remain (5 referenced by nothing) ·
**41 marks generated in `images/marks/`, not one wired into a lesson**, against 2,016 emoji glyphs ·
**the two `book_gates` versions S115 shipped carry NO changelog line** — recorded at S116,
deliberately not backfilled · **L13 carries one `data-reveal="mechanism"` block**, one of the four
book-wide that are not on §20.1's strip whitelist.

## Bench (need the robot — photography parked, so these are parked with it)
Q017 L09 six numbers · Q044 calibration-spin · Q046 gyro-bias · L02 §5 green-LED ·
Constrain RUN_MS · cm/s at a stated BASE_SPEED · the floor rig for 3.2 / 3.5 / VIDEO 3.1 ·
**a real TRIM run for `IMAGE 3.6`** · **THE SURFACE TEST: run 7E on a lab tile and see whether
the encoder square actually collapses** — this one gates the L12 delrin rename and possibly 7E itself.

---

# PUSHING — READ THIS

Named-file CLI for adds and modifies; **GitHub Desktop for deletions.** **Never `git add .`**

1. **`(1)` does not mean stale.** Verify by **md5**, never by suffix.
2. **Never present a test file, or a DIAGNOSTIC, in the same list as repo files.**
3. **Never produce PUSH_ME_*.md or MD5_*.txt.** Checksums and instructions go in the CHAT ONLY.
4. **`lessons/` IS PART OF THE FILENAME.** `going_deeper.html` belongs at the repo ROOT and
   `book.css` in `css/` — but the sixteen lessons belong in `lessons/`, and S117 put one at the
   root where it passed unnoticed until the next session opened. **Check the destination path of
   every file, not just its name.**
5. **A push that bumps a version and omits LIVE.md is an INCOMPLETE push (§12.6).**
6. **After any change that regenerates `css/book.css`, stage into a copy of the PUSHED CLONE
   and run `book_gates` THERE before presenting md5s.**
7. **Exactly ONE `ZUMO_SNN_HANDOFF.md` in the root (gate 28).** At S119 close, adding
   `ZUMO_S120_HANDOFF.md` means DELETING **this** file — a GitHub Desktop checkbox.
8. **THE NUMBER IN THE FILENAME IS THE SESSION THAT READS IT, NOT THE ONE THAT WROTE IT.**
9. **AFTER ANY `css/book.css` REGENERATION, DIFF THE STAGE AGAINST THE PUSHED CLONE AND PUSH
   EVERY FILE THAT DIFFERS.** S118's cycle changed **ten** lessons and only one of them is the
   lesson that was edited — the other nine carry a class rename. Which files differ is a
   MEASUREMENT, not a guess. **Then re-run `book_gates` in a FRESH CLONE.**
10. **Never write a real version number as `vOLD → vNEW` in prose.** `_versions_in()` takes the
   LAST match in the file. Write *"reaches vNEW (from vOLD)"*. Backticks do not shield it.
