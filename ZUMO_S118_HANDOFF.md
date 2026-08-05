# ZUMO — S118 HANDOFF (written at S117 close · paste at top of Session 118)

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
7. `--anomalies` is SILENT when clean. Anything it prints is a real lead.
8. **Do not hand-type a version, and do not hand-type a COUNT.** `session_versions.py
   --live` / `--handoff` EMIT the blocks.
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

**TWO LESSONS LEFT TO CONVERT: L13 and L15.** L12 closed at S117. Both are thinner than L12 —
**neither carries a checklist at all**, and both §10s are narrative (L13 an *Inventory* plus a
forward pointer, L15 a *What you built* list). Measured at S117 by reading all three §10s.
So expect **BC01–BC04 all four authored from nothing** on each, worse than L12's ratio.

---

# STATE

Fresh-clone verified at **`b307865`**. Census **40,579**.
Bible **v8.106** · `BookComponentStandard` **v01.12.1** · Maker **v2.45.2** ·
`marks/` **41** · `icons/` **49** incl. LICENSE.
`ZUMO_Syllabus_WORKING.md` **v1.2**.

Instruments: `book_gates` **v1.44.3** · `lesson_inventory` **v1.2.0** ·
`gen_component` **v1.6.1** · `pill_sweep` **v1.1** · `gate_payload_match` **v1.7** ·
`build_family_map` **v1.3.5** · `build_mark_index` **v1.0.2** · `gen_bonus_banner` **v1.4.1** ·
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

Lessons: L01 v03.19.2 · L02 v03.11.2 · L03 v03.28.1 · L04 v04.19.2 · L05 v04.19.2 · L06 v04.23.2 · L07 v04.22.1 · L08 v04.19.2 · L09 v05.16.2 · L10 v02.17.0 · L11 v02.18.0 · L12 v01.20.0 · L13 v02.17.1 · L14 v02.22.0 · L15 v02.17.1 · L16 v02.12.1.

**48/48 gates.** `--anomalies` silent · family map **1061/1061** · `regex_audit` 0 leads ·
`build_css --check` current at **643 rules** · 0 dead classes · `color_index --check` clean ·
`build_palette --check` matches the ruling · `image_audit --check` current at 14 outstanding
of 141 · both banner generators green · `gate_payload_match` PASS.

---

# THE ONE THING TO CARRY OUT OF S117

**A CONTROL THAT DIES BEFORE IT WRITES IS A CONTROL THAT NEVER RAN — AND KNOWING THAT DOES NOT
STOP IT HAPPENING.** S116 canonized exactly this. S117 did it **three more times** in one
sitting, on the same gate.

The §24.14 deletion control needed one real callout block removed. Attempt 1 used a regex that
matched nothing. Attempt 2 named a class that does not exist in L04. Attempt 3 deleted a block
the family map does not count as a callout at all — so it landed, and §24.14 **PASSED**, which
looked like the gate failing when it was the injection missing.

On two of the three the script raised, the shell moved on, and `book_gates` printed **`exit=0`
against a completely untouched tree**. That zero is indistinguishable from a real pass.

**What actually fixed it was not remembering the rule. It was a line of code:** read the file
back off disk and assert the count moved, *before* the gate is allowed to run. Attempt 4 did
that and fired correctly at 1060/1061.

Add the read-back to every control. A rule you have to recall at the moment of temptation is
not working — that is §24.10's own argument, applied to §24.6b.

---

# AND THE SECOND ONE, WHICH DESTROYED A FILE

**AN ENCODE ERROR INSIDE `open(p,'w')` TRUNCATES THE FILE TO ZERO.**

The first attempt at the S117 Bible entry built the text with a Python `\ud83c\udfc6` escape — an
unpaired surrogate. `open(P,'w')` truncated the Bible, *then* `.write()` raised
`UnicodeEncodeError`, and `ZUMO_SUPER_BIBLE.md` was **0 bytes**.

Recovered in one command from the clone, because the clone is always on disk. **That is the only
reason this was a footnote and not a session.**

§12 has required atomic temp-file + `os.replace` for a long time. The missing half is *why the
order matters inside the write itself*: **encode the whole blob first, then open.** A truncating
`open()` must never be reachable from a call that can raise. And prose with emoji goes in a
heredoc file, never in a Python string literal.

---

# S117 WORK — L12, THE TWELFTH CONVERSION

| Block | Ancestor | Price |
|---|---|---|
| **BC01** | **none** — 0 pre-§6 `check`, 0 `quiz`, 0 TRY IT (all 13 pre-§9 reveals are `catchup`) | 5 authored, §3.1→§3.2→§3.3→§3.4→§3.5, every citation read and verified to CONTAIN its answer |
| **BC02** | §2's six objectives (§25.5) + 5 rungs folded as **I have…** (§25.10a) | 11 items, literal ☐ |
| **BC03** | **four Exit-Ticket rungs, reshaped into questions** (§25.10j, DJ ruling) | 4 stems migrated, 4 answers + citations authored |
| **BC04** | **none** | 3 prompts authored, no reveals |

The 🏆 *one sentence to walk out with* and the *Next lesson* prose stay OUTSIDE the family and
reseat after BC04 — L10's arrangement. Engineer's Log survives as its own block (S80).

**Three baselines moved, each controlled in both directions:**

| Baseline | Move | Control |
|---|---|---|
| §27.11 rules/decls | 644/2,362 → **643/2,357** | one selector gone (`.div-ddd-3`, 5 decls — the −5 IS that rule), **zero born, zero altered** |
| §21 image coverage | 235 → **240** | sole delta `BrainGear_Incomplete.png` 55 → 60 |
| family map | 1057 → **1061** | exactly ONE family moves, BRAIN CHECK 44 → 48; other 29 byte-identical |

**NO CLASS RENAME.** S116's shape, not S115's — but diff by SELECTOR every time anyway.
**Only two files differ from the pushed clone:** `Lesson_12.html` and `css/book.css`. The other
fifteen lessons returned byte-identical through restore → regenerate → apply. Measured, not
assumed.

---

# RULED THIS SESSION, AND THE TWO THINGS STILL OPEN FROM IT

**RULED — §25.10j.** A checklist rung that claims to *understand why* is a Knowledge Check item
wearing a checkbox. The test is the **verb, not the tense**: capability → BC02 *I can…*;
observation → BC02 *I have…*; *understand why* → BC03 as a question. First move *into* BC03;
L07 and L09 both went the other way.

**ANSWERED — THE LOCK IS FINE, AND A BIGGER THING FELL OUT OF THE ANSWER.** DJ: *"We don't use
delrin sheets. It's melamine (I think) and we have tons of tiles sitting in the lab."* Access is
not rationed, so BC02's folded 7E rung is earnable and **nothing comes out of the locked list**.

**BUT THE BOOK NAMES A MATERIAL THE LAB DOES NOT STOCK — AND THAT IS THE SMALL HALF.**
`delrin`/`acetal` appears **17 times in L12**, twice more inside `newproject.html`'s 7D and 7E
payloads (byte-compared by `gate_payload_match`, so lesson and Maker must move together), and
6 times across `IMAGE_SHOT_LIST.md`, `ZUMO_SHELVED_CARDS.md` and `ZUMO_FAMILY_MAP.md`.

**DJ STOPPED THE RENAME, AND HE WAS RIGHT TO:** *"Wait on changing. I think originally I said we
could use delrin to get a slick surface, but it's prob not much slicker than the melamine."*
Delrin was chosen **because it is slick**. If the lab tile is not meaningfully slicker than the
floor, renaming the material **writes the wrong physics down more accurately.**

**THE EXPOSURE IS 7E AND ONLY 7E.** §7's hands fallback covers 7C and 7D — grip the chassis and
the wheels fight you — but nobody can hold a robot through four 30 cm sides and four corners.
7E's payoff (*Button A collapses, Button C comes home*), GRAPHIC 12.3, §8A.1's citation and the
BC02 rung behind the lock all rest on the surface genuinely slipping. **If it does not, 7E fails
QUIETLY** — both squares come home and the lesson's climax reads as a claim the robot did not
demonstrate. Worse than a wrong noun.

**IT IS A BENCH ITEM, NOT A DECISION.** One tile, one robot, load 7E, press A, five minutes.
Collapses → vocabulary rename only (property in the prose, the lab's material named once in §7's
TIP). Does not collapse → source a slicker surface or re-stage 7E, which is its own session.
**Do not rename anything before that test** — a rename done first has to be done again.
Full reasoning in `ZUMO_PARKED_EXIT_ITEMS.md`.

**STILL OPEN FROM S116 — the past-tense question did NOT recur on L12** (none of its past-tense
rungs is a duplicate), so it is undecided and now depends entirely on L13/L15. **Both have no
checklist at all**, which means it may never recur — decide it or retire it deliberately.

**RECORDED, NOT RESOLVED — an instrument-vs-reading disagreement.** L12's scorer ranks rung 2
against Objective 6 highest of the keepers (0.42) on shared words; reading says Objective 6's
content lands on rungs 4 and 5 (0.27, 0.21). The normaliser was **not** tuned to produce that
pairing. Full note in `ZUMO_PARKED_EXIT_ITEMS.md`.

---

# S118 QUEUE

## The conversion arc — the standing work
- **L13 and L15** to convert. Remove each number from `BC_PENDING` in the same edit.
  Both are **all-authoring**: no checklist ancestor, no Knowledge Check, narrative §10s.
- **Revisit the L14 → L15 → L16 flow** (DJ ruling S115, queued deliberately, still untouched).
- **L10's `What You Built` is the only non-Brain-Check `<h4>` in a converted §10.** L11 had no
  equivalent; L12 has the 🏆 block and the *Next lesson* paragraph in the same role. Worth one
  look across the other ten for consistency.

## Rulings outstanding — carried
- **Should `build_family_map` parse its total instead of holding a baseline?** **Fourth hand
  edit of that literal in four sessions** (1049 → 1053 → 1057 → 1061). Two conversions left
  means two more. The cost of parsing is that gate 47 stops noticing an added or deleted callout.
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
deliberately not backfilled. (Their numbers are deliberately not written here — a version
literal in prose is the LAST match `_versions_in()` finds and silently overrides the emitted
STATE block.)

## Bench (need the robot — photography parked, so these are parked with it)
Q017 L09 six numbers · Q044 calibration-spin · Q046 gyro-bias · L02 §5 green-LED ·
Constrain RUN_MS · cm/s at a stated BASE_SPEED · the floor rig for 3.2 / 3.5 / VIDEO 3.1 ·
**a real TRIM run for `IMAGE 3.6`** · **THE SURFACE TEST: run 7E on a lab tile and see whether
the encoder square actually collapses** — this one gates the L12 rename and possibly 7E itself.

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
7. **Exactly ONE `ZUMO_SNN_HANDOFF.md` in the root (gate 28).** At S118 close, adding
   `ZUMO_S119_HANDOFF.md` means DELETING **this** file — a GitHub Desktop checkbox.
8. **THE NUMBER IN THE FILENAME IS THE SESSION THAT READS IT, NOT THE ONE THAT WROTE IT.**
9. **AFTER ANY `css/book.css` REGENERATION, DIFF THE STAGE AGAINST THE PUSHED CLONE AND PUSH
   EVERY FILE THAT DIFFERS.** S117's cycle rewrote all sixteen lessons and only **one** of them
   actually differs — but which one is a measurement, not a guess. **Then re-run `book_gates`
   in a FRESH CLONE — matching md5s do not prove a complete push.**
10. **Never write a real version number as `vOLD → vNEW` in prose.** `_versions_in()` takes the
   LAST match in the file. Write *"reaches vNEW (from vOLD)"*. Backticks do not shield it.
