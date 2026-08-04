# ZUMO — S116 HANDOFF (written at S115 close · paste at top of Session 116)

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
6. `--anomalies` is SILENT when clean. Anything it prints is a real lead.
7. **Do not hand-type a version.** `session_versions.py --live` / `--handoff` EMIT the blocks.
8. Entrypoints are traps: `lesson_inventory.build(path)`, `gen_component.load_standard()`,
   `svg_layout_audit.audit(path)`, `flatten_alpha.flatten(path)`, `build_worklist.build(dir)`,
   `regex_audit.audit(paths)`, `session_versions.bible_consistency(path)`,
   `build_css.build(paths)`, `image_audit.audit(paths)`, `strip_inline.build(paths)`,
   `build_palette.build()`, `class_sweep.sweep(paths)`, `color_index.index(paths)`.
9. **A CLONE IS NOT THE SITE.** Run `site_parity.py` after any push. It can FAIL on the first
   run in the minute after a push and pass on retry — that is Pages lag, not a defect (S112).
10. **VERIFY THE PUSH BY FRESH CLONE AND MD5.**
11. **The lesson files are `Lesson_NN.html`, no topic suffix.** A hand-typed
    `Lesson_10_Obstacles.html` fails; use the glob.

---

# ⏰ SEPTEMBER 8 IS UNDER FIVE WEEKS OUT

**14 images outstanding of 141.** Unchanged from S114 — no figure work this session.
DJ has parked photography. The seven rulings under S114's table are still the cheapest
board item and none of them needs a camera to DECIDE, only to execute.

**FOUR LESSONS LEFT TO CONVERT: L11, L12, L13, L15.** That is the standing arc now, and
it is the biggest authoring block between here and September.

---

# STATE

Fresh-clone verified at **`f03c93f`**. Census **40,206**.
Bible **v8.104.1** · `BookComponentStandard` **v01.12.1** · Maker **v2.45.2** ·
`marks/` **41** · `icons/` **49** incl. LICENSE.
`ZUMO_Syllabus_WORKING.md` **v1.2**.

Instruments: `book_gates` **v1.44.1** · `lesson_inventory` **v1.2.0** ·
`gen_component` **v1.6.1** · `pill_sweep` **v1.1** · `gate_payload_match` **v1.7** ·
`build_family_map` **v1.3.3** · `build_mark_index` **v1.0.2** · `gen_bonus_banner` **v1.4.1** ·
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

Lessons: L01 v03.19.2 · L02 v03.11.2 · L03 v03.28.1 · L04 v04.19.2 · L05 v04.19.2 · L06 v04.23.2 · L07 v04.22.1 · L08 v04.19.2 · L09 v05.16.2 · L10 v02.17.0 · L11 v02.17.1 · L12 v01.19.1 · L13 v02.17.1 · L14 v02.22.0 · L15 v02.17.1 · L16 v02.12.1.

Lessons: L01 v03.19.1 · L02 v03.11.1 · L03 v03.28.0 · L04 v04.19.1 · L05 v04.19.1 · L06 v04.23.1 · L07 v04.22.0 · L08 v04.19.1 · L09 v05.16.1 · L10 v02.17.0 · L11 v02.17.1 · L12 v01.19.1 · L13 v02.17.1 · L14 v02.22.0 · L15 v02.17.1 · L16 v02.12.1.

**48/48 gates.** `--anomalies` silent · family map **1053/1053** · `regex_audit` 0 leads ·
`build_css --check` current at **645 rules** · 0 dead classes · `color_index --check` clean ·
`build_palette --check` matches the ruling · `image_audit --check` current at 14 outstanding
of 141 · both banner generators green · `gate_payload_match` PASS.

Lessons: L01 v03.19.2 · L02 v03.11.2 · L03 v03.28.1 · L04 v04.19.2 · L05 v04.19.2 ·
L06 v04.23.2 · L07 v04.22.1 · L08 v04.19.2 · L09 v05.16.2 · **L10 v02.17.0** ·
L11 v02.17.1 · L12 v01.19.1 · L13 v02.17.1 · L14 v02.22.0 · L15 v02.17.1 · L16 v02.12.1.

---

# THE ONE THING TO CARRY OUT OF S115

**TWO PREDICATES FOR ONE CONCEPT, AND ONLY ONE OF THEM WAS COUNTED.**

"Converted to the four exit blocks" was decided by §25.2 on the string `MENTAL KNOWLEDGE
CHECK` and by gate 29 on `id="brain-check-01"`. **Nothing asserted the two agreed.**

Measured, not argued: mistyping CHECK → CHEK in ONE lesson dropped it out of §25.2's
enforcement entirely — no four-block conformance, no retired-name ban, no checkbox/tag
parity — and **ALL 47 GATES PASSED**. Breaking the OTHER predicate failed three gates loudly.
**§24.8 exactly: if a lesson silently left §25.2's scope, that gate looked identical either
way.** It had been violating the S83 rule the whole time — import the definition, never write
a third regex.

Closed with one shared `is_converted()` requiring BOTH marks, which reports a HALF-conversion
as its own finding, because half a conversion must not buy exemption from the gates.

**AND GATE 29'S LITERAL IS GONE, WHICH IS THE HALF WORTH REMEMBERING.** `converted != 9`
could not say WHICH lesson moved, and the conversion arc would have required editing that
number five times — each edit indistinguishable from disarming the gate. It is now derived
from **named sets**:

```
BC_EXEMPT  = {'14', '16'}                 # DJ ruling S115
BC_PENDING = {'11', '12', '13', '15'}     # DJ ruling S115; L10 removed when it converted
```

**Converting a lesson is the deletion of its number from `BC_PENDING`, in the same edit.**
Control-run four ways: the CHECK→CHEK sabotage FAILS; the opposite half FAILS; a pending
lesson converting FAILS naming it; an exempt lesson converting FAILS naming it.

This is S114's lesson applied one layer up: S114 said a baseline that looks like a count will
be read as a count. S115 says **a baseline that cannot name its subject should not be a number
at all.**

---

# S115 SHIPPED IN TWO PUSHES — THE SECOND ONE IS THE LESSON

**PUSH 1 WAS INCOMPLETE AND EVERY MD5 MATCHED.** It carried `css/book.css` and L10 and omitted
**the nine lessons the regeneration had also rewritten.** The pushed clone came back **47/48**
with §27.13 failing, where the identical local tree passed 48/48.

**Cause: a class RENAME, which §27 already names as its own case.** L10's four Brain Check
blocks added ten `<details>`, flipping the usage ranking `build_css` sorts by, so
`.details-dee2e6` and `.details-dee2e6-2` **swapped names**. Proven a rename and not a restyle
by asserting declaration-set equality across the swap in both directions.

**The live site sat in a broken intermediate state** — nine lessons naming `-2` against a
stylesheet where `-2` now meant the other spacing, so every Brain Check reveal in L01–L09
rendered with the wrong margin and padding. Visible on the page; invisible to a push that
looked clean.

**THE RULE WAS ALREADY WRITTEN AND WAS NOT FOLLOWED.** Push item 6 says stage into a copy of
the PUSHED CLONE and run `book_gates` THERE before presenting md5s. The gates were run in the
staging tree, which passed, and nobody asked **which files the restore→regenerate→apply cycle
had modified** — the cycle rewrites all sixteen lessons and only the ones it actually changes
need pushing.

**THE MISSING STEP IS ONE LINE, AND IT IS NOW PUSH ITEM 10: diff the stage against the pushed
clone and push every file that DIFFERS, not every file you meant to change.**

---

# S115 WORK

## DJ's exemption ruling, and why L15 is not exempt

**L14 and L16 are EXEMPT.** L14's §10 is the competition-day Morning and Pre-Match routines;
L16's is Final Deliverables and Looking Forward. The four blocks would displace real content
rather than fill a gap.

**DJ, on L15: *"No, don't exempt 15. Revisit later about the flow from 14-15-16."*** L15's §10
is the longest in the book, which is what prompted the question — but length is not the test,
JOB is. L15's §10 does the same job as L12's and L13's (Exit Ticket → Engineer's Log → bonus
mysteries), so exempting it would give L12 and L13 the same claim and the ruling would eat
itself. **L15 is also the one lesson in the book with ZERO checkboxes** — an argument for
converting it, not exempting it.

**QUEUED BY THE SAME RULING: revisit the L14 → L15 → L16 flow** as its own question.

## A correction that changed the price before any writing started

The three L10 ancestors were first reported as **14 / 9 / 4 items**. A DOM sibling walk says
**5 / 5 / 4**. The first numbers came from a hand-rolled slicer that cut at the next `<h3>` —
but the ancestors are `<h4>`s inside ONE panel, so every slice swallowed the ones after it and
the counts came out cumulative. **§24.6c applies to the slicer that SCOPES the work exactly as
it applies to the gate that CHECKS it.** The estimate was inflated by four authored items.

## L10 — the tenth conversion

Scoped by READING §10 per §25.10e, not by grepping it: the retired-name sweep found **one**
ancestor, reading found **three**.

| Ancestor | Destination |
|---|---|
| *What You Built* (5) | **stays OUTSIDE the family** — it recaps, it does not check (L08 *Record Your Calibration* precedent) |
| *Check Your Understanding* (5, answerless) | **BC03**, migrated verbatim, five answers authored |
| *Rate Yourself* (4 rungs) | folds into **BC04** as a labelled group (§25.10a) |

**BC01 had no ancestor at all** — zero pre-§6 reveals, zero `check` reveals, zero TRY IT. Five
items authored, §-ordered §3.1 → §3.2 → §3.4 → §3.5 → §3.6, **each citation verified to CONTAIN
its answer** (v8.58.1) and each deliberately non-overlapping with BC03: the TRIM question moved
off BC01 onto `RETURN_TIMEOUT` for exactly that reason.

**BC02 is L10's own nine §2 objectives migrated character-exact** (§25.5), asserted equal.

**Three traps this conversion hit, and the next four will hit them too:**

1. **The box glyph must be the LITERAL `☐`.** The gate counts the literal; §2's objectives
   ship as `&#9744;`. Re-prefixing with the entity reports as *0 checkbox items but 9
   data-bc-skill tags*. This is S114's L07/L14 spelling trap in a new place.
2. **BC01 seats ABOVE the §6 SECTION FENCE**, not between the fence and its banner. §25.10h
   does not state this; §6.8a fails if you get it wrong.
3. **The column copy must start at its `<!-- ===== BRAIN CHECK COLUMN START` comment**, which
   is the string the gate looks for. Copying from the `<div id="brain-check-col">` misses it.
   The block carries ZERO lesson-specific tokens, so it is a byte copy.

Achievability confirmed BEFORE BC02 landed (§25.10): §6 Step 3's *"Type it wrong first"*
already plants the `error: redefinition` rep, so objective 4 is earnable by every student.

## Four baselines moved, each controlled in both directions

| Baseline | Move | Control |
|---|---|---|
| §21 image coverage | 225 → 230 | sole delta `BrainGear_Incomplete.png` 45 → 50 |
| §27.11 rules/decls | to 645 / 2,365 | one selector gone (`.h4-c-4d535f-5`, 2 decls), zero born, zero survivors altered |
| §27.11 digest | recomputed | deleting one `color: white;` still FAILS |
| family map | 1049 → 1053 | **exactly ONE family moves, BRAIN CHECK 36 → 40; other 27 byte-identical** |

**Diff the stylesheet by SELECTOR, never by the comment header.** The header carries usage
counts, so a rule whose count moved looks changed — the first diff reported ~20 rules
added and removed when the real delta was one.

**§27.8b is restore → regenerate → apply, and skipping *restore* makes the count slide.**
Running `build_css` against an already-stripped tree produced 645, then 644, then a dead class,
before the cycle was run properly from the top.

## THREE SELF-INFLICTED ERRORS — READ THESE

1. **A blind first-occurrence replace put the new family baseline into a CHANGELOG line**,
   rewriting S113's history as *"baseline 1048 -> 1053"*. Caught on read-back and reverted.
   **Editing history to record a present fact is a defect even when the present fact is right.**
   Every subsequent edit went through a `count==1` assert.
2. **The Bible was tangled across three successive edits** — an entry inserted mid-header-line,
   then a lift that cut the wrong span, truncating the `Prior:` chain from ~14,000 chars to
   3,989. **Fixed by RESTORING the file from the clean clone and redoing both edits with
   asserts**, not by repairing forward. The restore should have happened after the FIRST bad
   edit, not the third.
3. **`session_numbers()` parses the CHANGELOG SECTION, not the header line.** Its regex is
   `^v[\d.]+,\s*S(\d+),\s*(major|moderate|minor)` at a LINE START. An entry written only into
   the `**Bible version:**` header satisfies nothing. Both homes need the entry.

---

# S116 QUEUE

## The conversion arc — the standing work
- **L11, L12, L13, L15** to convert. Remove each number from `BC_PENDING` in the same edit.
  L11 has two ancestors (*Reflection Questions*, *Skills Checklist*); L12/L13/L15 have an Exit
  Ticket and an Engineer's Log and little else, so they are mostly authoring.
- **Revisit the L14 → L15 → L16 flow** (DJ ruling S115, queued deliberately).
- **L10's `What You Built` is now the only non-Brain-Check `<h4>` in a converted §10.** Worth
  one look across the other nine to see whether the pattern is consistent.

## Rulings outstanding — carried from S114
- **Should `build_family_map` parse its total instead of holding a baseline?** Parsing makes the
  label honest; the cost is that gate 47 stops noticing an added or deleted callout. **This got
  more expensive this session, not less** — four callouts were added and the literal moved by
  hand, exactly as predicted. Four more conversions means four more hand edits.
- **The `#666` footer colour** — 18 declarations, eight `.p-c-666*` families whose NAMES encode
  the hex.
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
- **`[IMAGE 3.6]` → §22 terminal block, ONCE THERE ARE REAL NUMBERS.** Do not write it from
  imagination.
- **Apply GPT Task 2 and Task 4** — *if DJ still has the S112 outputs.* Not in the repo.

## Canon debts
§21.1's thresholds live only in `book_gates.py` · §25.6 header example · §25.10e misfiled ·
challenge-card redesign Part B · difficulty-progression audit · Maker batch · L01 VS Code
multi-root · Stage Two two blocks labelled `Learn/Insight` (L03, L09) ·
`ROBOLORE_UPSTREAM_DELTA_S102.md` written and unapplied · robolore.com hosting ·
§6.5's "nav button count is 12–14" is **obsolete** under the six-pill rail — retire, don't argue ·
`css/book.css` has zero custom properties (`build_palette --css` emits them ready) ·
**26 gradient definitions across 18 SVG files** remain (5 referenced by nothing) ·
**41 marks generated in `images/marks/`, not one wired into a lesson**, against 2,016 emoji
glyphs. The icon arc is fully built on the supply side and has not started on the demand side.

## Bench (need the robot — photography parked, so these are parked with it)
Q017 L09 six numbers · Q044 calibration-spin · Q046 gyro-bias · L02 §5 green-LED ·
Constrain RUN_MS · cm/s at a stated BASE_SPEED · the floor rig for 3.2 / 3.5 / VIDEO 3.1 ·
**a real TRIM run for `IMAGE 3.6`**.

---

# PUSHING — READ THIS

Named-file CLI for adds and modifies; **GitHub Desktop for deletions.** **Never `git add .`**

1. **`(1)` does not mean stale.** Verify by **md5**, never by suffix.
2. **Never present a test file in the same list as repo files.**
3. **Never produce PUSH_ME_*.md or MD5_*.txt.** Checksums and instructions go in the CHAT ONLY.
4. `going_deeper.html` belongs at the repo ROOT, not in `lessons/`. `book.css` belongs in `css/`.
5. **A push that bumps a version and omits LIVE.md is an INCOMPLETE push (§12.6).**
6. **After any change that regenerates `css/book.css`, stage into a copy of the PUSHED CLONE
   and run `book_gates` THERE before presenting md5s.**
7. **Exactly ONE `ZUMO_SNN_HANDOFF.md` in the root (gate 28).** At S116 close, adding
   `ZUMO_S117_HANDOFF.md` means DELETING **this** file — a GitHub Desktop checkbox.
8. **THE NUMBER IN THE FILENAME IS THE SESSION THAT READS IT, NOT THE ONE THAT WROTE IT.**
   This file is `ZUMO_S116_HANDOFF.md` and is titled S116 because **S116 reads it.**
   `session_versions.session_numbers()` now asserts this against the Bible and LIVE.md.
9. **AFTER ANY `css/book.css` REGENERATION, DIFF THE STAGE AGAINST THE PUSHED CLONE AND PUSH
   EVERY FILE THAT DIFFERS.** The restore→regenerate→apply cycle rewrites all sixteen lessons;
   a class RENAME changes whichever of them used the renamed class, and those files are not
   the ones you set out to edit. S115 shipped in two pushes for exactly this. **Then re-run
   `book_gates` in a FRESH CLONE — matching md5s do not prove a complete push.**
10. **Never write a real version number as `vOLD → vNEW` in prose.** `_versions_in()` takes the
   LAST match in the file, so a prose arrow silently overrides the emitted STATE block. Write
   *"reaches vNEW (from vOLD)"*. Backticks do not shield it.
