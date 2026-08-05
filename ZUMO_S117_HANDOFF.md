# ZUMO — S117 HANDOFF (written at S116 close · paste at top of Session 117)

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
   tree is on disk. S116 ran it to read the flags and it wrote a stylesheet from an
   unrestored tree (645 → 644, the S115 slide). §27.8b's order is not optional and the
   tool will let you skip it silently.
7. `--anomalies` is SILENT when clean. Anything it prints is a real lead.
8. **Do not hand-type a version, and do not hand-type a COUNT.** `session_versions.py
   --live` / `--handoff` EMIT the blocks. S116 hand-typed a census into two Bible homes
   and had to correct it from `lesson_inventory.py` afterwards — §24.10 exactly.
9. Entrypoints are traps: `lesson_inventory.build(path)`, `gen_component.load_standard()`,
   `svg_layout_audit.audit(path)`, `flatten_alpha.flatten(path)`, `build_worklist.build(dir)`,
   `regex_audit.audit(paths)`, `session_versions.bible_consistency(path)`,
   `build_css.build(paths)`, `image_audit.audit(paths)`, `strip_inline.build(paths)`,
   `build_palette.build()`, `class_sweep.sweep(paths)`, `color_index.index(paths)`.
10. **A CLONE IS NOT THE SITE.** Run `site_parity.py` after any push. It can FAIL on the first
   run in the minute after a push and pass on retry — that is Pages lag, not a defect (S112).
11. **VERIFY THE PUSH BY FRESH CLONE AND MD5 — AND DIFF THE STAGE AGAINST THE CLONE.**
12. **The lesson files are `Lesson_NN.html`, no topic suffix.** Use the glob.

---

# ⏰ SEPTEMBER 8 IS UNDER FIVE WEEKS OUT

**14 images outstanding of 141.** Unchanged. DJ has parked photography. The seven rulings
under S114's table are still the cheapest board item and none needs a camera to DECIDE.

**THREE LESSONS LEFT TO CONVERT: L12, L13, L15.** L11 closed at S116. These three are the
thin ones — an Exit Ticket and an Engineer's Log and little else — so they are **mostly
authoring, not migration**, and L11 priced that: 13 items authored against 11 migrated.

---

# STATE

Fresh-clone verified at **`d9b3191`**. Census **40,391**.
Bible **v8.105** · `BookComponentStandard` **v01.12.1** · Maker **v2.45.2** ·
`marks/` **41** · `icons/` **49** incl. LICENSE.
`ZUMO_Syllabus_WORKING.md` **v1.2**.

Instruments: `book_gates` **v1.44.2** · `lesson_inventory` **v1.2.0** ·
`gen_component` **v1.6.1** · `pill_sweep` **v1.1** · `gate_payload_match` **v1.7** ·
`build_family_map` **v1.3.4** · `build_mark_index` **v1.0.2** · `gen_bonus_banner` **v1.4.1** ·
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

Lessons: L01 v03.19.2 · L02 v03.11.2 · L03 v03.28.1 · L04 v04.19.2 · L05 v04.19.2 · L06 v04.23.2 · L07 v04.22.1 · L08 v04.19.2 · L09 v05.16.2 · L10 v02.17.0 · L11 v02.18.0 · L12 v01.19.1 · L13 v02.17.1 · L14 v02.22.0 · L15 v02.17.1 · L16 v02.12.1.

**48/48 gates.** `--anomalies` silent · family map **1057/1057** · `regex_audit` 0 leads ·
`build_css --check` current at **644 rules** · 0 dead classes · `color_index --check` clean ·
`build_palette --check` matches the ruling · `image_audit --check` current at 14 outstanding
of 141 · both banner generators green · `gate_payload_match` PASS.

---

# THE ONE THING TO CARRY OUT OF S116

**A HAND-PREDICTED COUNT IS A LEAD, AND ASSERTING IT IS HOW IT STAYS ONE.**

L11's *Skills Checklist* held seven rungs against six §2 objectives. Four restate an objective
in the **past tense** — *"I converted encoder counts…"* against *"Convert encoder counts…"* —
so L05's word-identical duplicate test does not fire on them, and reading them by eye returns
whatever the reader already expected.

I predicted 4/3, wrote the assert, and **the assert failed**: the normaliser stripped only the
*"I can"* / *"I have"* subjects, so *"I converted…"* and *"I measured…"* read as unique.

**The temptation at that moment is to tune the normaliser until it reproduces the prediction.
That is writing the gate to the sweep.** What was done instead: score all 7 × 6 pairs, print
the best match per rung, read the separation. It is clean — duplicates **0.55–0.73**, survivors
**0.31–0.38** — and the ruling is now a NAMED PAIRING with `min(dup) > max(keep)` asserted,
which a wrong pairing cannot satisfy where a bare count of four could be met by any four rungs.

Canonized as **§25.10i**.

---

# AND THE SECOND THING, WHICH IS WORSE

**A CONTROL THAT DIES BEFORE IT WRITES IS A CONTROL THAT NEVER RAN — WEARING A PASS.**

The family-map deletion control misfired **three times**. Each time the target string was
absent, the assert threw, the script exited before `open(...,'w')`, and `book_gates` then ran
against a **completely unmodified tree** and printed `PASS §24.14`.

That PASS was one keystroke from being recorded as *"the moved baseline still catches a
deletion."* It caught nothing. It never saw a deletion.

**§24.6b says assert the injection LANDED in the shape intended.** S84 wrote that after an
injection truncated at the wrong `</div>`. This is the cheaper and more embarrassing version:
the injection did not land at all, and the shell reported success because the *gate* exited 0.
**Read what the control DID, not what the gate said afterwards.** The real run, once it landed,
failed correctly at 1056/1057.

---

# S116 WORK — L11, THE ELEVENTH CONVERSION

| Block | Ancestor | Price |
|---|---|---|
| **BC01** | **none** — 0 pre-§6 reveals, 0 `check`, 0 TRY IT | 5 authored, §3.1→§3.2→§3.3→§3.4→§3.5, every citation read and verified to CONTAIN its answer |
| **BC02** | §2's six objectives (§25.5) + 3 checklist rungs as **I have…** (§25.10a) | 9 items, literal ☐ |
| **BC03** | *Reflection Questions*, 5, answerless | migrated VERBATIM (asserted); 5 answers + 5 citations authored |
| **BC04** | **none** | 3 prompts authored, no reveals |

**Authored 13, migrated 11.** The Engineer's Log survives as its own block after BC04 (S80).
`'11'` left `BC_PENDING` in the same edit — control-run with it left in, and the gate **names
L11**, where the pre-S115 count could only have said ten.

**Three baselines moved, each controlled in both directions:**

| Baseline | Move | Control |
|---|---|---|
| §27.11 rules/decls | 645/2,365 → **644/2,362** | one selector gone (`.div-bg-eafaf1`, 3 decls — the −3 IS that rule), **zero born, zero altered** |
| §21 image coverage | 230 → **235** | sole delta `BrainGear_Incomplete.png` 45 → 50 |
| family map | 1053 → **1057** | exactly ONE family moves, BRAIN CHECK 40 → 44; other 29 byte-identical |

**NO CLASS RENAME THIS TIME.** L11's ten new `<details>` did not flip the usage ranking the way
L10's did — `ALTERED = 0` across the whole stylesheet. That is S115's defect not recurring,
**not** a rule that stopped applying: diff by SELECTOR every time, and diff the stage against
the pushed clone every time.

---

# RULED THIS SESSION, AND THE ONE THING STILL OPEN FROM IT

**OPEN — DJ HAS NOT RULED:** the four past-tense rungs are **parked**, not deleted
(`ZUMO_PARKED_EXIT_ITEMS.md`, with the pairing table). The question is whether *"did you
actually do it"* is worth keeping alongside *"can you do it"*. If yes, all seven fold into BC02
and the student ticks the same claim twice under two labels. If no, they stay parked. **This
recurs on L12/L13/L15 if any of them carries a past-tense checklist — decide it once.**

**FLAGGED, NOT RESOLVED — an achievability edge the fold created.** BC02's folded rung *"Run 7E
and watched the stopwatch version fail on a tired battery"* now sits **behind the Mark-done
lock** and needs a TIRED BATTERY to earn. §7E mandates the run so the lesson plants the rep, but
this is §25.10c's shape exactly: an item not every student can earn makes the lock unreachable.
It was a plain checkbox for eleven sessions; **the lock is new exposure even though the item
is old.**

---

# S117 QUEUE

## The conversion arc — the standing work
- **L12, L13, L15** to convert. Remove each number from `BC_PENDING` in the same edit.
  All three are thin: expect L11's ratio or worse, i.e. mostly authoring.
- **Revisit the L14 → L15 → L16 flow** (DJ ruling S115, queued deliberately, still untouched).
- **L10's `What You Built` is the only non-Brain-Check `<h4>` in a converted §10.** L11 had no
  equivalent. Worth one look across the other nine for consistency.

## Rulings outstanding — carried, and one got cheaper
- **Should `build_family_map` parse its total instead of holding a baseline?** **Third hand
  edit of that literal in three sessions** (1049 → 1053 → 1057). Three conversions left means
  three more. The cost of parsing is that gate 47 stops noticing an added or deleted callout.
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
**the two `book_gates` versions S115 shipped carry NO changelog line** — the version moved in
the constant only, both times. Recorded at S116, deliberately not backfilled: this file is not
the place to reconstruct a session from memory. (Their numbers are deliberately not written
here — a version literal in prose is the LAST match `_versions_in()` finds, and it silently
overrides the emitted STATE block. `session_versions --check` caught exactly that at S116 close.)

## Bench (need the robot — photography parked, so these are parked with it)
Q017 L09 six numbers · Q044 calibration-spin · Q046 gyro-bias · L02 §5 green-LED ·
Constrain RUN_MS · cm/s at a stated BASE_SPEED · the floor rig for 3.2 / 3.5 / VIDEO 3.1 ·
**a real TRIM run for `IMAGE 3.6`**.

---

# PUSHING — READ THIS

Named-file CLI for adds and modifies; **GitHub Desktop for deletions.** **Never `git add .`**

1. **`(1)` does not mean stale.** Verify by **md5**, never by suffix.
2. **Never present a test file, or a DIAGNOSTIC, in the same list as repo files.**
3. **Never produce PUSH_ME_*.md or MD5_*.txt.** Checksums and instructions go in the CHAT ONLY.
4. `going_deeper.html` belongs at the repo ROOT, not in `lessons/`. `book.css` belongs in `css/`.
5. **A push that bumps a version and omits LIVE.md is an INCOMPLETE push (§12.6).**
6. **After any change that regenerates `css/book.css`, stage into a copy of the PUSHED CLONE
   and run `book_gates` THERE before presenting md5s.**
7. **Exactly ONE `ZUMO_SNN_HANDOFF.md` in the root (gate 28).** At S117 close, adding
   `ZUMO_S118_HANDOFF.md` means DELETING **this** file — a GitHub Desktop checkbox.
8. **THE NUMBER IN THE FILENAME IS THE SESSION THAT READS IT, NOT THE ONE THAT WROTE IT.**
9. **AFTER ANY `css/book.css` REGENERATION, DIFF THE STAGE AGAINST THE PUSHED CLONE AND PUSH
   EVERY FILE THAT DIFFERS.** S116's cycle rewrote all sixteen lessons and only **three** of
   them actually differ — but which three is a measurement, not a guess. **Then re-run
   `book_gates` in a FRESH CLONE — matching md5s do not prove a complete push.**
10. **Never write a real version number as `vOLD → vNEW` in prose.** `_versions_in()` takes the
   LAST match in the file, so a prose arrow silently overrides the emitted STATE block. Write
   *"reaches vNEW (from vOLD)"*. Backticks do not shield it.
