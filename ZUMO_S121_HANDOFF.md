# ZUMO — S121 HANDOFF (written at S120 close · paste at top of Session 121)

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

**THE L14 → L15 → L16 FLOW ITEM IS CLOSED.** Queued by DJ at S115, unblocked when the conversion
arc finished at S119, ruled and applied at S120. Nothing in it remains open.

---

# THE ONE THING TO CARRY OUT OF S120

**A GATE CAN BE SATISFIED BY THE GEOMETRY OF A DEFECT RATHER THAN BY ITS ABSENCE — AND THE FIX
IS THE THING THAT REVEALS IT.**

§24's cross-lesson promise gate FAILED the L14 rewrite naming `L14 -> L16: promises ['PID']`.
The new bullets carried no terminal punctuation, so *full PID* in the Lesson 15 bullet ran on
into the Lesson 16 sentence.

**The ORIGINAL bullets had exactly the same run-on.** They passed only because the third bullet —
*"Different competitions: sumo wrestling, maze solving, soccer"* — pushed the distance to the next
period past the gate's 110-character window. Delete that bullet, as the ruling required, and the
latent defect becomes visible. The gate was never protecting L14; a piece of prose the ruling
happened to remove was.

This is §24.8 in a new place: the instrument could not distinguish *no promise* from *a promise
too far from a period*, and the passing report read identically either way. Closed by punctuating
each bullet as its own sentence — **not** by touching the gate.

---

# STATE

Fresh-clone verified at **`b3dd802`**. Census **40,979**.
Bible **v8.109** · `BookComponentStandard` **v01.12.1** · Maker **v2.45.2** ·
`marks/` **41** · `icons/` **49** incl. LICENSE.
`ZUMO_Syllabus_WORKING.md` **v1.2**.

Instruments: `book_gates` **v1.45** · `lesson_inventory` **v1.2.0** ·
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

Lessons: L01 v03.19.2 · L02 v03.11.2 · L03 v03.28.1 · L04 v04.19.2 · L05 v04.19.3 · L06 v04.23.3 · L07 v04.22.2 · L08 v04.19.3 · L09 v05.16.3 · L10 v02.17.1 · L11 v02.18.1 · L12 v01.20.1 · L13 v02.18.0 · L14 v02.23.0 · L15 v02.19.0 · L16 v02.12.1.

**49/49 gates.** `--anomalies` silent · family map **1069/1069** · `regex_audit` 0 leads ·
`build_css --check` current at **643 rules**, UNMOVED by this session's edits · 0 dead classes ·
`color_index --check` clean · `build_palette --check` matches the ruling · `image_audit --check`
current at 14 outstanding of 141 · both banner generators green · `gate_payload_match` PASS on the
full glob. **No stylesheet regeneration this session, so none of §27.8b's three steps ran and no
innocent lesson was rewritten** — only the two edited files differ.

---

# S120 WORK — THE FLOW RULING, AND THE ENDING THAT WAS NOT AUTHORED

**§3.1 IS NEW: THE BOOK ENDS AT LESSON 16, FOR EVERY READER.** The review measured the seam three
ways and they disagreed:

| Measured | Result |
|---|---|
| **Code chain** | continuous — L13 24,902 → L14 25,640 → L15 28,034 → L16 starts 28,034 |
| **Narrative** | L14 carries a course ending; L15 carries no forward pointer at all |
| **Exit blocks** | legacy / converted / legacy — the S115 exemption's visible cost |

**L14 was closing the course two lessons early.** Its *What's Next?* offered L15 and L16 as
post-competition ***options***, third bullet *"Different competitions: sumo wrestling, maze
solving, soccer"* — an after-the-book list in peer position with the capstone. **L16 §4.2 audits
*"where YOUR 28,034 bytes are"*, which IS L15's finished build**, so L16 hard-requires the lesson
L14 called optional. Prose and byte chain disagreed and the prose was wrong.

**A SECOND ENDING WAS OFFERED AND DJ RULED IT OUT.** The grid stops Fall at L13 Step 3, so the
obvious third fix was a Fall-terminal close in L13. DJ: *"I don't think we need to make the book
tell them they are done at 13… if this book is used by others, then 13 won't be the end. It would
be 16."* **Dropped, not parked.** The corollary is now canon: this Bible carries **no calendar
canon**. Measured **against the file as it stood before the S120 entry**, `trimester` / `Fall` /
`Winter` / `calendar` / `class period` each occurred **zero** times; they occur now, in that entry
and in §3.1. **The first draft asserted the zero in the present tense about a file it had just
falsified, and a full gate pass did not see it, because no gate counts words.** The term split stays in `ZUMO_Teacher_Daily_Grid_WORKING.md`, which already
rules its own mid-L13 break *"a calendar seam, not a book seam."*

**Applied, both MODERATE (pages render differently, so both §5b homes move):**
- **L14** — *What's Next?* rewritten: two lessons remain, L16 named the capstone, the sumo/maze/
  soccer line demoted out of the peer list to a closing italic. The *Final Word* and 🏆 box were
  read and **deliberately left alone** — a competition send-off at lesson 14 is legitimate; the
  menu was the defect.
- **L15** — gains the `Next:` pointer it had never carried, seated on **L13's live placement**
  (after the *One sentence to carry out of here* block, before Engineer's Log, same unclassed
  `<p><strong>Next:</strong>` markup). Its two figures were checked, not assumed: L15 finished is
  28,034, L16 §4.2 names that same number, the §16 ceiling is 28,672, so 638 bytes.

Census 40,978 → **40,979**. Bible reaches **v8.109** (from v8.108.1).

---

# S121 QUEUE

## Ruled at S120, needs a decision next
- **THE FORWARD POINTER IS NOT A NORM AND SHOULD BE RULED.** Parsed, not grepped:
  `<strong>Next:</strong>` exists in exactly **three** lessons — **13, 14, 15** — and a
  *What's Next* heading in **seven** — 01, 03, 05, 06, 07, 08, 14 — overlapping only in L14.
  **Seven carry neither: 02, 04, 09, 10, 11, 12 and 16**, and only L16 is entitled to.
  **The heading TEXT drifts three ways** — *What's Next* (L01, L08), *What's Next?* (L05, L06,
  L07, L14), *What's Next: Preview of Lesson 4* (L03) — and **only L03 carries a `whats-next`
  anchor id**, so this is §6.8a's shape: an observed practice with no canon behind it.
  **Three questions:** must every lesson 01–15 carry a pointer, which of the two constructs is
  canon, and does it take an anchor? Ruling it makes it gateable; unruled, §3.1's *"every lesson
  points forward"* holds only where someone happens to look (§24.2).
  **Instrument note, because it nearly cost a wrong number:** the S120 census was first taken by
  grep, then re-derived by an EXACT heading-text match which returned **six** and omitted L03 —
  the correct list came only from a third pass matching the heading text by PREFIX. Two of the
  three instruments disagreed and the grep was the one that happened to be right. §24.13 exactly:
  a re-derivation is only a check if the new instrument is the right one.

## Carried, unchanged
- **L01's BC02 does not carry L01's objectives.** Ruled legacy at S119, not fixed. Still the only
  remaining §25.5 violation in the book.
- **S116's past-tense question: RETIRE IT.** L15 carried no checklist so it never recurred.
  Carried six sessions now. Retire deliberately.
- **L10's `What You Built` is the only non-Brain-Check `<h4>` in a converted §10.** One look
  across all fourteen.
- **The syllabus/TDP consequence of the L13 stop, flagged S120 and NOT opened.** `ZUMO_Syllabus_
  WORKING.md` says the TDP is written *"by Lesson 16"*, and `ZUMO_TDP_Template_v3.md` feeds §7
  entirely from Log #14, §5's bench row from #15, and §4, §8 and the Abstract from #16. A student
  who stops at L13 Step 3 has no source for four sections and the Abstract. **This is a
  syllabus/TDP question, not a book question** — §3.1 rules that the book must not absorb it.

## Rulings outstanding — carried
- **Should `build_family_map` parse its total instead of holding a baseline?** The baseline did
  NOT move this session, the first time in seven — the conversion arc is over and the recurring
  cause is genuinely gone. Rule it or drop it.
- **Should `build_css` name rules by usage RANK at all?**
- **The `#666` footer colour** — 18 declarations, eight `.p-c-666*` families whose NAMES encode the hex.
- **16 uppercase-only colours** — 197 occurrences, no variance, unruled.
- **`font_stack_sweep` rule** — Consolas: 15 declarations, all with a fallback, zero bare.
- **Callout colours re-examined** — v8.87's Scope C.
- **`3.2` vs `3.5`** — before/after split, or one figure and a deleted row.
- **NOTE per-block pass** (133 blocks, four destinations).
- **Nav `<details>` carry no `data-reveal`** — §25.12 exists because one untyped `<details>` slipped.
- **Selftest-coverage gate** — offered, not built.
- **§25.10l's constant lives ONLY in `book_gates.py`** (gate 49), §21.1's shape.
- **The seven remaining figure tags** — S114's table.
- **⭐ heavy-lesson list needs a ruling** — the grid flags L13 as now a Fall lesson carrying a
  genuinely counter-intuitive idea, deliberately left unmarked pending DJ's call.

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
9. **Exactly ONE `ZUMO_SNN_HANDOFF.md` in the root (gate 28).** At S121 close, adding
   `ZUMO_S122_HANDOFF.md` means DELETING **this** file — a GitHub Desktop checkbox.
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
