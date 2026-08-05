# ZUMO — S120 HANDOFF (written at S119 close · paste at top of Session 120)

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
   tree is on disk. **`session_versions.py --help` has no help branch either.**
7. `--anomalies` is SILENT when clean. Anything it prints is a real lead.
8. **Do not hand-type a version, and do not hand-type a COUNT.** `session_versions.py
   --live` / `--handoff` EMIT the blocks.
9. **`gate_payload_match.py` needs the FULL lesson glob.** Run against one lesson it exits 1,
   because §11's inheritance rule puts lesson N−1's `finished` payload in N's corpus. That is
   not a defect and it cost a minute at S119.
10. Entrypoints are traps: `lesson_inventory.build(path)`, `gen_component.load_standard()`,
   `svg_layout_audit.audit(path)`, `flatten_alpha.flatten(path)`, `build_worklist.build(dir)`,
   `regex_audit.audit(paths)`, `session_versions.bible_consistency(path)`,
   `build_css.build(paths)`, `image_audit.audit(paths)`, `strip_inline.build(paths)`,
   `build_palette.build()`, `class_sweep.sweep(paths)`, `color_index.index(paths)`.
   **`lesson_inventory.build()` runs `expand_classes()` first**, so every `off` it reports is an
   offset into the EXPANDED source. Expand first, then slice.
11. **A CLONE IS NOT THE SITE.** Run `site_parity.py` after any push. It can FAIL on the first
   run in the minute after a push and pass on retry — Pages lag, not a defect (S112).
12. **VERIFY THE PUSH BY FRESH CLONE AND MD5 — AND DIFF THE STAGE AGAINST THE CLONE.**
13. **The lesson files are `Lesson_NN.html`, no topic suffix, and they live in `lessons/`.**

---

# ⏰ SEPTEMBER 8 IS ABOUT FOUR WEEKS OUT

**14 images outstanding of 141.** Unchanged. Photography still parked. The seven rulings under
S114's table remain the cheapest board item and none needs a camera to DECIDE.

**THE CONVERSION ARC IS FINISHED.** L15 closed at S119 and `BC_PENDING` is **empty**. Fourteen
lessons converted, L14 and L16 exempt by DJ ruling S115. The set is kept rather than deleted so a
future L17 has a home.

---

# THE ONE THING TO CARRY OUT OF S119

**AN INSTRUMENT WHOSE TRANSFORM ERASES THE DISTINCTION UNDER TEST WILL REPORT AGREEMENT NO MATTER
WHICH WAY THE ANSWER FALLS.**

§27.8b step 3 was run as `strip_inline --apply` **without `--include-held`** — the flag is
written in the S119 handoff in those exact words. That reverted the four byte-exact-across-lesson
constructs from `class=` to inline `style=` in **all fifteen** other lessons.

**And S118's own innocence proof passed on the broken tree.** Expanding a lesson through its
tree's stylesheet resolves every class back to its declarations — so a lesson left inline expands
**byte-identically** to one correctly classed. The proof establishes RENDERING equivalence and is
structurally incapable of seeing FILE-STATE divergence. Only the line diff saw it, at 570 changed
lines.

This is §24.8 aimed at a *proof* rather than at a gate, and it is not the same failure as S118's
two: the read-back was fine, the assert could fail. **The transform itself was the hole.** Before
trusting any equivalence proof, ask what its normalisation throws away — and whether the thing
you are hunting lives in the discarded part.

Redone correctly, exactly **one** lesson differs from the pushed clone plus the stylesheet, with
both instruments agreeing at zero.

---

# STATE

Fresh-clone verified at **`0fb3b940`** — confirmed AFTER the push: recursive stage-vs-clone diff
at zero differences, md5 on all eight files, 48/48 gates run inside that clone, `site_parity`
PASS. **Verify against the tree that carries the work, never against the sha the session opened
on (S118).** Census **40,978**.
Bible **v8.108** · `BookComponentStandard` **v01.12.1** · Maker **v2.45.2** ·
`marks/` **41** · `icons/` **49** incl. LICENSE.
`ZUMO_Syllabus_WORKING.md` **v1.2**.

Instruments: `book_gates` **v1.44.5** · `lesson_inventory` **v1.2.0** ·
`gen_component` **v1.6.1** · `pill_sweep` **v1.1** · `gate_payload_match` **v1.7** ·
`build_family_map` **v1.3.7** · `build_mark_index` **v1.0.2** · `gen_bonus_banner` **v1.4.1** ·
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

Lessons: L01 v03.19.2 · L02 v03.11.2 · L03 v03.28.1 · L04 v04.19.2 · L05 v04.19.3 · L06 v04.23.3 · L07 v04.22.2 · L08 v04.19.3 · L09 v05.16.3 · L10 v02.17.1 · L11 v02.18.1 · L12 v01.20.1 · L13 v02.18.0 · L14 v02.22.1 · L15 v02.18.0 · L16 v02.12.1.

**48/48 gates.** `--anomalies` silent · family map **1069/1069** · `regex_audit` 0 leads ·
`build_css --check` current at **643 rules** · 0 dead classes · `color_index --check` clean ·
`build_palette --check` matches the ruling · `image_audit --check` current at 14 outstanding
of 141 · both banner generators green · `gate_payload_match` PASS on the full glob.

---

# S119 WORK — L15, THE FOURTEENTH AND LAST CONVERSION

| Block | Ancestor | Price |
|---|---|---|
| **BC01** | **none** — first reveal in the file is a §6 `catchup`; 0 `check`, 0 `quiz`, 0 TRY IT | 5 authored, §3.2 → §3.3 → §3.4 → §4.1 → §5.1 |
| **BC02** | §2's **seven** objectives — already verb-first, **no ☐ glyph at all** | 7 migrated, equality ASSERTED, literal ☐ supplied |
| **BC03** | **§10's *What you should be able to say out loud*** — five items, under a name no retired list carries | 5 migrated + **1 authored**, all six citing §3.2 · §4.2 · §3.4+§5.8 · §7B · §5.5 · §3.6 |
| **BC04** | none | 3 prompts authored, no reveals |

**§25.10l IS NEW AND IT CAME OUT OF A BAD QUESTION.** Claude asked *"objective 7 has no BC01
item — add one?"* and DJ ruled yes. **The premise was false:** four of seven objectives had no
BC01 item, because BC01 has never been an objective map — BC02 is. BC01 measured at **5 items in
13 of 13** converted lessons, a norm no gate holds. Three options were priced; **DJ ruled a
fourth on the teaching**: objective 7's verb is *Diagnose*, BC01 sits before §6 and asks what the
BUILD depends on, and diagnostic vocabulary is what a student reaches for at the BENCH in §7. So
objective 7 lands in **BC03**, BC01 holds at five and **14/14**, and BC03 goes to **six** —
legal without a ruling because §25.8 is a floor and L02 ships seven.

**L01 IS RULED LEGACY (DJ, S119).** L15 and L01 are the only lessons whose §2 carries no ☐, and
S118's survey read that as *zero objectives* — it was counting the **glyph**. L15 has seven,
verb-first, standard lead-in, so §25.10k's reword was unnecessary. L01's own BC02 carries ten
technical-skill items against §2's six, sourced from a list §2 never states; it is pre-§25.5, not
a competing precedent. **A separate cleanup item, not opened.**

**§25.10i RAN AND RETURNED NOTHING, WHICH IS ALSO A RESULT.** All 5 × 7 pairs scored; matrix max
**0.182** against L11's duplicates at 0.53–0.86 and its *keepers* at 0.36 on the same scorer.
Nothing folds. The scorer was control-run first against L11's four recorded pairings and
reproduced all four **rankings**, while its magnitudes differ from S116's — so the ranking was
trusted and **S117's absolute 0.78/0.42 threshold deliberately was not.** Recorded, not tuned
away: reading says say-2 restates Objective 3 and say-3 restates Objective 6; the scorer sees
0.154 and 0.111 because those sentences share one content token.

**Three baselines moved, each controlled in the failing direction:**

| Baseline | Move | Control |
|---|---|---|
| §21 image coverage | 245 → **250** | four block icons plus the column emblem |
| family map | 1065 → **1069** | identical generator version; ONE family moves, BRAIN CHECK 52 → 56, other 29 byte-identical |
| §27.11 digest | → `f852cf656a9bda51` | rules/decls **UNCHANGED** at 643/2,357, zero born, zero died, zero altered — S113's shape |

Plus `'15'` leaving `BC_PENDING`, which fails **naming L15** — what §25.2a's named sets buy.

---

# S120 QUEUE

## First, because the arc just closed
- **Revisit the L14 → L15 → L16 flow** (DJ ruling S115, queued deliberately, still untouched).
  Now unblocked — every lesson it touches is in its final structural shape.
- **L01's BC02 does not carry L01's objectives.** Ruled legacy at S119, not fixed. It is the one
  remaining §25.5 violation in the book and it is now the *only* one.
- **S116's past-tense question: RETIRE IT.** L15 carried no checklist, so it did not recur on
  L11's successors at all. It has been carried five sessions. Retire deliberately.
- **L10's `What You Built` is the only non-Brain-Check `<h4>` in a converted §10.** L15's
  equivalent is unheaded prose. One look across all fourteen.

## Rulings outstanding — carried
- **Should `build_family_map` parse its total instead of holding a baseline?** **Sixth hand edit
  in six sessions** (1049 → 1053 → 1057 → 1061 → 1065 → 1069). **The conversion arc is over, so
  the recurring cause is gone** — this is the session to rule it or drop it.
- **Should `build_css` name rules by usage RANK at all?** S118's swap did not recur at S119
  (zero names changed meaning), which is evidence about frequency, not about safety.
- **The `#666` footer colour** — 18 declarations, eight `.p-c-666*` families whose NAMES encode the hex.
- **16 uppercase-only colours** — 197 occurrences, no variance, unruled.
- **`font_stack_sweep` rule** — Consolas: 15 declarations, all with a fallback, zero bare.
- **Callout colours re-examined** — v8.87's Scope C.
- **`3.2` vs `3.5`** — before/after split, or one figure and a deleted row.
- **NOTE per-block pass** (133 blocks, four destinations).
- **Nav `<details>` carry no `data-reveal`** — §25.12 exists because one untyped `<details>` slipped.
- **Selftest-coverage gate** — offered, not built.
- **The seven remaining figure tags** — S114's table.

## Ruled, not yet done
- **`[IMAGE 3.6]` → §22 terminal block, ONCE THERE ARE REAL NUMBERS.**
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
**the two `book_gates` versions S115 shipped carry NO changelog line** — recorded S116,
deliberately not backfilled · **four `data-reveal="mechanism"` blocks book-wide** are not on
§20.1's strip whitelist.

## Bench (need the robot — parked with photography)
Q017 L09 six numbers · Q044 calibration-spin · Q046 gyro-bias · L02 §5 green-LED ·
Constrain RUN_MS · cm/s at a stated BASE_SPEED · the floor rig for 3.2 / 3.5 / VIDEO 3.1 ·
**a real TRIM run for `IMAGE 3.6`** · **THE SURFACE TEST: run 7E on a lab tile and see whether
the encoder square actually collapses.**

---

# PUSHING — READ THIS

Named-file CLI for adds and modifies; **GitHub Desktop for deletions.** **Never `git add .`**

1. **`(1)` does not mean stale.** Verify by **md5**, never by suffix.
2. **Never present a test file, or a DIAGNOSTIC, in the same list as repo files.**
3. **Never produce PUSH_ME_*.md or MD5_*.txt.** Checksums and instructions go in the CHAT ONLY.
4. **`lessons/` IS PART OF THE FILENAME.** Check the destination path of every file, not just
   its name (S117 put a converted lesson at the repo root and it passed unnoticed).
5. **A push that bumps a version and omits LIVE.md is an INCOMPLETE push (§12.6).**
6. **§27.8b's third step is `strip_inline --apply --include-held`.** Without the flag, 624 held
   strings revert to inline and fifteen innocent lessons are rewritten. **S119 did exactly this.**
7. **After any change that regenerates `css/book.css`, stage into a copy of the PUSHED CLONE
   and run `book_gates` THERE before presenting md5s.**
8. **AFTER ANY `css/book.css` REGENERATION, DIFF THE STAGE AGAINST THE PUSHED CLONE AND PUSH
   EVERY FILE THAT DIFFERS** — and diff by LINE, not only by expansion (see the S119 finding).
9. **Exactly ONE `ZUMO_SNN_HANDOFF.md` in the root (gate 28).** At S120 close, adding
   `ZUMO_S121_HANDOFF.md` means DELETING **this** file — a GitHub Desktop checkbox.
10. **THE NUMBER IN THE FILENAME IS THE SESSION THAT READS IT, NOT THE ONE THAT WROTE IT.**
11. **Never write a real version number as `vOLD → vNEW` in prose.** `_versions_in()` takes the
   LAST match in the file. Write *"reaches vNEW (from vOLD)"*. Backticks do not shield it.
12. **THE SAME TRAP APPLIES TO SHAs, AND IT IS NEW AT S119.** `session_versions` parses a sha
   out of LIVE.md's verification line. Writing a second sha in that sentence — even to say
   *"the session opened on X, which is NOT the verification"* — makes the tool read **X**.
   It reported the wrong commit and looked completely normal doing it. **One sha per parsed
   line. Never name a second one in prose, however clearly you disclaim it.**
13. **A document cannot name the commit that contains it.** `session_versions --check` says so
   itself. LIVE.md's verification line names the commit carrying the WORK; the follow-up push
   that fills the line is necessarily one commit later. That is expected, not drift.
