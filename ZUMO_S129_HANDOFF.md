# ZUMO — S129 HANDOFF (written at S128 close · paste at top of Session 129)

## Session open ritual (do this without being asked)
1. **`git ls-remote https://github.com/Weymuth/zumo.git HEAD` FIRST.** A stale answer is
   timing, not caching — **retry a minute later before concluding a push failed** (§12.4).
   Saying "the push didn't land" is a wrong answer, and a wrong answer costs 3×.
2. Read `LIVE_ZUMO_TEXTBOOK.md` — verify date / status / versions.
3. **Do NOT grep the Bible version.** `session_versions.bible_consistency()` parses it; the
   Bible has THREE homes — header line 17, the `Current:` clause on that SAME line, and the
   newest CHANGELOG entry — and it fails if any two disagree.
4. Run the full suite and **READ THE EXIT CODE, NOT THE LAST LINE**:
   `book_gates.py` · `gen_component.py --selftest` · `lesson_inventory.py` ·
   `lesson_inventory.py --anomalies` · `pill_sweep.py --selftest` ·
   `pill_sweep.py --audit lessons/Lesson_*.html` · `build_family_map.py` ·
   `class_sweep.py --selftest` · `fit_raster_svg.py --selftest` · `flatten_alpha.py --selftest` ·
   `svg_layout_audit.py --selftest images/L01_GRAPHIC_1-13_zumo_rear_view.svg` ·
   `regex_audit.py --selftest` then `regex_audit.py` · `build_worklist.py --selftest` ·
   `font_stack_sweep.py --selftest` then bare · `session_versions.py --selftest` then `--check` ·
   `site_parity.py --selftest` then bare · `build_css.py --selftest` then `--check` ·
   `image_audit.py --selftest` then `--check` · `strip_inline.py --selftest` then `--verify` ·
   `entity_sweep.py --selftest` then bare · `build_palette.py --selftest` then `--check` ·
   `color_index.py --selftest` then `--check` · `gen_bonus_banner.py --selftest` ·
   `gen_part_banners.py --selftest` ·
   `gate_payload_match.py newproject.html lessons/Lesson_*.html` ·
   `next_pointer.py --check` · `title_feed.py --check` ·
   **`family_tag.py --selftest` then bare** (NEW S128 — a bare run must report
   *1069 already correct, 0 to write*; anything else means a callout's family drifted) ·
   **`mark_wire.py --selftest` then bare** (NEW S128 — a bare run must report
   *880 SWAP / 17 NO_GLYPH / 56 HELD*; it does NOT write without `--apply`).
5. If `flatten_alpha --selftest` prints `NOT FULLY TESTED`: `pip install cairosvg
   --break-system-packages`. **Needed every session.**
6. **NEVER run `build_css.py --help`.** It has no help branch — it BUILDS, against whatever
   tree is on disk. **`session_versions.py --help` has no help branch either.**
7. `--anomalies` is SILENT when clean. Anything it prints is a real lead.
8. **Do not hand-type a version, and do not hand-type a COUNT.** `session_versions.py
   --live` / `--handoff` EMIT the blocks.
9. **`gate_payload_match.py` needs the FULL lesson glob.**
10. Entrypoints are traps: `lesson_inventory.build(path)`, `gen_component.load_standard()`,
   `svg_layout_audit.audit(path)`, `flatten_alpha.flatten(path)`, `build_worklist.build(dir)`,
   `regex_audit.audit(paths)`, `session_versions.bible_consistency(path)`,
   `build_css.build(paths)`, `image_audit.audit(paths)`, `strip_inline.build(paths)`,
   `build_palette.build()`, `class_sweep.sweep(paths)`, `color_index.index(paths)`,
   `title_feed.build(root)`, `entity_sweep.build(paths)`,
   **`family_tag.build(paths, apply=False)`**, **`mark_wire.build(paths, apply=False)`**.
11. **A CLONE IS NOT THE SITE.** Run `site_parity.py` after any push. It can FAIL on the
   first run in the minute after a push and pass on retry — Pages lag, not a defect (S112).
12. **VERIFY THE PUSH BY FRESH CLONE AND MD5 — AND DIFF THE STAGE AGAINST THE CLONE.**
13. **The lesson files are `Lesson_NN.html`, no topic suffix, and they live in `lessons/`.**
14. **`css/semantic.css` IS HAND-EDITED ON PURPOSE (§27.15).** It is the ONLY stylesheet file
   that is. `css/book.css` is still DO-NOT-HAND-EDIT — edit the source and regenerate.
15. **`regex_audit.py` after any gate you write.**
16. **`session_versions --check` will report ~22 disagreements at session open and they are
   EXPECTED** — every one names `ZUMO_S129_HANDOFF.md`, the INCOMING document, stale by
   definition once work starts. Read WHICH artefact each line names. If a line names LIVE.md
   or the Bible, that IS drift.
17. **`session_versions --selftest` FAILS THE MOMENT THE BIBLE NAMES THE CURRENT SESSION.**
   Not a defect and not a push failure — it is the tool saying the session is not closed.

---

# SEPTEMBER 8 IS ABOUT FOUR WEEKS OUT

**14 images outstanding of 141.** Unchanged. Photography still parked.

---

# THE ONE THING TO CARRY OUT OF S128

**A NUMBER CAN BE REAL, USABLE-LOOKING, AND MEASURED AGAINST A DIFFERENT DOCUMENT.**

`lesson_inventory.build()` runs `expand_classes` before parsing, so **every node offset it
has ever reported indexes the EXPANDED source**, where each `class="…"` has become a much
longer `style="…"`. The offsets are internally correct. They are not file offsets, the drift
grows with position, and a writer using them lands mid-prose — **and lands PLAUSIBLY**.

Nothing in the tree had ever needed file offsets, so nothing had noticed. It surfaced only
because the marks arc needed to WRITE to an element the parser had FOUND. **§24.8 arriving on
an offset rather than on a gate.** Closed with `expand_classes_mapped()`; all 1,069 callout
offsets verified to bracket a clean opening tag.

**The general shape, and it is the reusable part: when a reading instrument grows a writing
consumer, every coordinate it reports has to be re-proved against the file on disk.** A
coordinate that was only ever compared with other coordinates from the same instrument was
never tested at all.

---

# STATE

<!-- VERSION BLOCK: emitted by session_versions.py --handoff. Never hand-typed. -->
Fresh-clone verified at **`bbcc9bb`**. Census **40,700**.
Bible **v8.120** · `BookComponentStandard` **v01.12.1** · Maker **v2.45.4** ·
`marks/` **41** · `icons/` **49** incl. LICENSE.
`ZUMO_Syllabus_WORKING.md` **v1.2**.

Instruments: `book_gates` **v1.55** · `lesson_inventory` **v1.3.1** ·
`gen_component` **v1.6.1** · `pill_sweep` **v1.1** · `gate_payload_match` **v1.7** ·
`build_family_map` **v1.3.8** · `build_mark_index` **v1.0.2** · `gen_bonus_banner` **v1.4.1** ·
`gen_part_banners` **v1.2** · `session_versions` **v1.21.0** · `fit_raster_svg` **v1.2** ·
`flatten_alpha` **v1.2** · `svg_layout_audit` **v1.20** · `site_parity` **v1.1** ·
`build_css` **v1.3.0** ·
`image_audit` **v1.1** ·
`strip_inline` **v1.2** ·
`build_worklist` **v1.1** ·
`regex_audit` **v1.0** ·
`build_palette` **v1.1** ·
`class_sweep` **v1.0** ·
`color_index` **v1.0** ·
`entity_sweep` **v1.0** ·
`font_stack_sweep` **v1.3.0** ·
`next_pointer` **v1.2** ·
`family_tag` **v1.0** ·
`mark_wire` **v1.0** ·
`title_feed` **v1.0** ·
`timer.html` **v1.3.2** ·
`going_deeper` **v01.6.1**.

Lessons: L01 v03.23.2 · L02 v03.15.2 · L03 v03.33.2 · L04 v04.23.2 · L05 v04.22.2 · L06 v04.27.2 · L07 v04.26.2 · L08 v04.23.2 · L09 v05.20.2 · L10 v02.21.2 · L11 v02.22.2 · L12 v01.24.2 · L13 v02.22.2 · L14 v02.27.2 · L15 v02.23.2 · L16 v02.15.2.

**59/59 gates.** `--anomalies` silent · family map **1069/1069** · `regex_audit` **1 lead** ·
`build_css --check` current at **604 rules** · `strip_inline --verify` 0 dead class names ·
`color_index --check` clean · `image_audit --check` current at 14 outstanding of 141 ·
`gate_payload_match` PASS on the full glob · `next_pointer --check` and `title_feed --check` clean ·
`entity_sweep` decoded text byte-identical in 21 files ·
`family_tag` **1069 correct, 0 to write** · `site_parity` **PARITY**.

**§27.11 is 604 / 2,141**, unchanged — no class attribute moved, so §27.8b's three-step
sequence never ran.

---

# S128 WORK — SEE `LIVE_ZUMO_TEXTBOOK.md` FOR THE FULL ACCOUNT

**One push (`bbcc9bb`), one Bible entry (v8.120), §24.14a and §24.14b NEW.** `data-family`
now sits on all **1,069** callouts. Nothing renders differently — every lesson change is an
inserted attribute, which is why all sixteen are MINOR and the visible §5b banners stay put.

**THE BLOCKER WAS NEVER THE MAPPING.** `build_family_map`'s GLYPH tier resolved **209 of the
953 mapped blocks by the decorative emoji alone** — KEY TERM 159 of 184, THE WALL 17 of 17,
GOING DEEPER 7 of 7. Replacing that emoji with a mark would have erased their only family
signal and failed gate 47. **S112 shipped that tier calling itself a stopgap and predicting
this exact moment in its own comment.**

**THE CORRECTNESS PROOF IS AGREEMENT, NOT INSPECTION.** The generator reading the attribute
reproduces its 30-family table **byte-identically**, and **blinding the GLYPH tier entirely
still returns 1069/1069**. The emoji is now decoration and nothing else.

**THE MAPPING WAS ALREADY RULED AND THE S128 HANDOFF MISSTATED IT.** DJ: *"I thought we had
the new marks all designated by callout names?"* Correct — `BookComponentStandard` §7 carries
the 26-family roster he approved at S91 and amended at S93. The join is **family→mark**, 20
families / 953 blocks, **89%**, EXTRACTED — against the handoff's INFERRED name-match at 58%.
**§7.2 covers 11 of the 14 marks reported role-less**; only `battery`, `battery-full` and
`battery-half` sit in no table, and **§7.2 names seven marks that are not on disk**.

**A NAME-MATCH MAPPING WAS MEASURED AND REJECTED, WITH A NUMBER ON IT.** The bullseye carries
**thirteen distinct labels across its 125 uses** while NOTE's 133 blocks wear thirteen
different emoji. Glyph→mark is not a function in either direction; matching the bullseye to
`bullseye.svg` by name would be right 100 times and **wrong 25**.

**GATE 59 NEW**, same pass as the ruling. It asserts the PROPERTY, not presence: it re-derives
the family from CONTENT through `family_tag` — which imports `build_family_map`'s own tiers,
never a second copy (§83) — and requires the attribute to AGREE, so a hand-typed attribute
contradicting its own content fails exactly like a missing one. Coverage arm included.
Control-run four ways with read-back and restore asserts, each firing gate 59 **ALONE** at 58
of 58 green, untouched tree passing at BOTH ends, file restored byte-identical.

**A SECOND DEFECT IN MY OWN TOOL:** a dry run reported **zero work to do** because the counter
only incremented inside the apply branch. **A report that cannot distinguish *nothing to do*
from *not looking* is not evidence.**

---

# S129 QUEUE

## THE MARKS ARC — BUILT, VERIFIED, AND DELIBERATELY NOT APPLIED

`mark_wire.py` v1.0 is in the repo and its dry run reconciles exactly:
**880 SWAP + 17 NO_GLYPH + 56 BRAIN CHECK = 953.**

**THREE THINGS COME FIRST, IN THIS ORDER. Do not run `--apply` before them.**

1. **THE AST SCAN FOR GLYPH-PINNED LOCATORS — S127's rule 19, and it is already live.**
   The L04 control proved it: with 34 marks in, **§5.1's coverage fell 251 → 240**, because
   that gate finds a callout's label THROUGH the glyph. Eleven labels went invisible in ONE
   lesson. S127's silent case — `strip_inline`'s locator dropping L01's held attributes 39 →
   32 — was found **only** by the AST scan and by no gate. Running 884 swaps first would be
   doing the exact thing the rule was written about.
2. **WIDEN `lesson_inventory`'s GLYPH DETECTOR.** It takes the first character above U+2100,
   so an **ASCII pseudo-glyph is invisible to it** — and **four LEARN blocks carry a literal
   `</>` marker** (L02 ×1, L04 ×3). Found by READING, not by the instrument. §24.8, the same
   shape as `_LAND` missing the literal left arrow at S127. Once widened, those four
   reclassify from NO_GLYPH to SWAP, so **the true population is 884 swaps and 13
   insertions**, not 880 and 17.
3. **MOVE §21's COVERAGE BASELINE BY A CONTROLLED PER-FILE DELTA.** One lesson's marks moved
   it 250 → 284. Book-wide it lands near 1,134. **Derive it; do not project it** — the total
   alone is not evidence (§24.14).

**RULINGS ALREADY MADE, DO NOT RE-OPEN:**
- **BRAIN CHECK is HELD BY NAME** (§25.2a). All 56 already carry the two-state BrainGear
  emblem, which is precisely the behaviour §7.1 specifies, so a mark would be their SECOND.
  Holding the family also disposes of **all 22** non-leading-glyph blocks, every one of which
  is a BRAIN CHECK. **`mark_wire`'s own Control E caught this hold being FAKE** — §7.1's keys
  read `BRAIN CHECK · open`, so the family was falling out of scope on a middot mismatch
  rather than on the hold. Normalised; the hold is now real and provable. **If that
  normalisation is ever removed, the hold silently stops working and nothing fails.**
- **DJ RULED THE 17 NO-GLYPH BLOCKS IN** — *"Do we know what the blocks are Named? If so,
  yes."* All 17 carry a named header. 10 KEY TERM (L12's glossary run), 4 LEARN (the `</>`
  four), 2 TIP, 1 DO THIS NOW. **L14's DO THIS NOW header is an `<h4>` one level deeper than
  the other twelve, so its insertion point differs** — that one needs its own locator.
- **DJ RULED EACH L12 GLOSSARY TERM GETS THE MARK**, not just the first of the run.

**§24.14b THE MARK RULE IS ALREADY LIVE AND HAS NO USERS YET**, which §27.15 explicitly
permits (*stoppable at any point*). `css/semantic.css` carries `img[data-mark]`, and **the
selector is an ATTRIBUTE because §27.15b fired again in a NEW direction**: the first attempt
used `class="mark"` and `build_css` promptly re-emitted it into the generated block as
`.img-fs-0`, which would have killed `.mark` on the next strip. **The graduation model assumes
a class LEAVES the markup when a rule arrives; a new semantic class going INTO markup runs the
generator backwards.** `build_css --check` holds at 604 rules with marks applied.

## THE GLOSSARY ARC — NEWLY REACHABLE, AND DJ HAS RULED ITS SHAPE
`data-family` made this harvestable, and it is the mark's most useful side effect. **The mark
does NOT do this — the attribute does.**
- **184 KEY TERM blocks harvest in one pass**, 172 with an extractable term name, **55
  already carrying an `id="term-*"` anchor**, yielding **106 distinct terms**.
- **DJ RULING: KEEP EVERY DEFINITION WHERE IT IS.** Nothing is de-duplicated. The glossary is
  ADDITIVE and every mention links to it, so it can be built, read and thrown away without
  touching a lesson.
- **DJ RULING: ONE ENTRY PER LESSON-TERM PAIR, DISAMBIGUATED BY TOPIC** — *Dead Reckoning
  (gyro)* and *Dead Reckoning (encoders)*. This is what makes the link target unambiguous
  everywhere and means no winner has to be picked.
- **THE "DRIFT" HYPOTHESIS WAS TESTED AND DOES NOT HOLD.** 49 terms are defined more than
  once, and **39 of the 49 are within a SINGLE lesson** — §3 where the term is taught, §10
  where the lesson's own glossary restates it. Section split: **54 repeats in §10, 35 in §3,
  9 in §5**. **Zero pairs score above 0.90 similarity**; copy-paste drift would cluster near
  1.00. The **10 cross-lesson** pairs are the LEAST similar of all (dead reckoning L06/L12 at
  0.01, scope L02/L07 at 0.03) — different content at different depth, which is the Saxon
  spiral working. *Caveat: similarity is computed on the first 200 chars of extracted body
  text and is a LEAD; the 39/10 split and the section counts are structural and reliable.*
- **THE TIER-3 CENSUS ITEM *"glossary reported absent in all sixteen"* IS FALSE.** The
  glossaries exist and are built from this same family; the probe read only `h2`/`h3` text.
  **Correct that item rather than acting on it.**
- §7 already reserves `journal-bookmark` for a GLOSSARY family and nothing uses it.

## Opened S127 and still not ruled
- **The 38 entities inside ATTRIBUTE values are excluded as a SCOPE, not an exception.**
  Sweeping them needs quote-context tracking. **Unruled: sweep them too, or is "text nodes
  only" the ruled scope?**
- **`index.html` carries no version home** — in no roster, `session_versions` does not track
  it. Same shape as `timer.html` at S123. **Is anything ELSE carrying content nothing versions?**
- **`BONUS_MARK` in `book_gates.py` and `MARK` in `gen_bonus_banner.py` are indexed nowhere**
  and two stray-checks cannot fire; the bonus banner lost its mark to S108's no-icons ruling.
  **DJ ASKED AND IT IS STILL UNRULED: delete the vestigial code, or hold it as the banner's
  entry point in the marks arc?** The banner is exactly where a mark would go.

## The colour ledger — unchanged
- **16 items; three marked *re-measure before ruling*** — they date from S94, before §27.
- **`#f8f9fa` (641 instances) remains the largest unreported surface**, and 30 of them are the
  only classed `<pre>` left in the book, confined to L02–L06. Unruled.

## Graduation candidates
`code` (S123), the pill (S124), the dark block (S126), the mark (S128). Next:
- **Callout families** — but **NOT before the colour ledger**, since their whole point is
  paint. **`going_deeper.html` defines its own `.callout`** and consumes the semantic layer,
  so check what a graduation does to that page BEFORE shipping (§27.15c's coupling cost).

## The consistency census — Tier 3
- **Nav pill count ranges 10 to 19**; §6.5's "12-14" rule is obsolete under the six-pill rail —
  **rewrite the rule before touching a lesson.**
- **Quick-reference anchors exist in five lessons only** (L02-L06); eight carry none.
- **Tier 3 needs reading, not counting:** three lessons have cards with Goal and Logic but
  fewer Templates (L03 short one, L08 short three, L10 short two — §6.12a allows prose);
  §7 ladder rungs 7A-7E appear in six lessons only (L10-L15) against §15.1's five-rung canon;
  L16's Engineer's Log wrapper does not match the other fifteen; **timers appear in L02, L03,
  L04 only — S69 already burned a session on a false finding here, READ before counting.**
- **Callout border-width probe returned zero shapes** — it looked for inline `border-left`,
  which §27 deleted; it has to read the stylesheet now.

## Carried, unchanged
- **Should `css/semantic.css` carry a version home?** Carried since S123. It now holds FOUR
  ruled constructs, has an external consumer that breaks if it changes, and **FOUR gates
  (54, 55, 57, and the §24.14b rule) depend on its contents.**
- **L01's BC02 does not carry L01's objectives.** Ruled legacy S119, still the only §25.5
  violation.
- **S116's past-tense question: RETIRE IT.** Fourteen sessions now.
- **L10's `What You Built` is the only non-Brain-Check `<h4>` in a converted §10.**
- **L14's score formula is marked up as `<code>` and is not code.**
- **L03's `id="whats-next"` is in all fifteen**; §27.14 still cannot see an unreached id.
- **`sweep_option_c.py` sits in the repo root** — the S92 one-shot, in no instrument list.
- **`index.html` is §27.12's only NAMED exception**, held by name — correct, must be remembered.
- **`regex_audit` reports 1 lead, `entity_sweep.py:70`** — a match-and-discard false positive
  (the group feeds a `\1` backreference and its value is never consumed). **The S127
  handoff's claim of 0 leads does not reproduce and both files are byte-unchanged since that
  push.** Suppress it or record it, but stop re-discovering it every session.

## Rulings outstanding — carried
- Should `build_family_map` parse its total instead of holding a baseline? Baseline unmoved
  nine sessions running — and **S128 did not move it either**, which is the point.
- Should `build_css` name rules by usage RANK at all? **Fired at S126** (`.p-m-0` → `.pre-m-0`,
  120 elements killed) **and again at S128** in a new direction (`class="mark"` → `.img-fs-0`).
  **Twice more since the last time this was asked. Strongest case yet.**
- **NOTE per-block pass** (133 blocks, four destinations).
- Nav `<details>` carry no `data-reveal` — §25.12 exists because one untyped `<details>` slipped.
- Selftest-coverage gate — offered, not built.
- §25.10l's constant lives ONLY in `book_gates.py` (gate 49), §21.1's shape.
- The seven remaining figure tags — S114's table.
- **Heavy-lesson star list needs a ruling** — L13 as a now-Fall lesson, deliberately unmarked.
- The two pointer CONSTRUCTS above the link — §3.1b rules the section, not the prose pattern.

## Canon debts
§21.1's thresholds live only in `book_gates.py` · §25.6 header example · §25.10e misfiled ·
challenge-card redesign Part B · difficulty-progression audit · Maker batch · L01 VS Code
multi-root · Stage Two two blocks labelled `Learn/Insight` (L03, L09) ·
`ROBOLORE_UPSTREAM_DELTA_S102.md` written and unapplied · robolore.com hosting ·
§6.5's "nav button count is 12-14" is **obsolete** — retire, don't argue ·
**26 gradient definitions across 18 SVG files** remain (5 referenced by nothing) ·
**the two `book_gates` versions S115 shipped carry NO changelog line** ·
**four `data-reveal="mechanism"` blocks book-wide** are not on §20.1's strip whitelist ·
**§7.2 names seven marks that are not on disk** (`ticket-perforated`, `stopwatch`,
`chat-dots`, `box-seam`, `images`, `table`, `trophy`) and three on disk are in no table
(`battery`, `battery-full`, `battery-half`).

## Bench (need the robot — parked with photography)
Q017 L09 six numbers · Q044 calibration-spin · Q046 gyro-bias · L02 §5 green-LED ·
Constrain RUN_MS · cm/s at a stated BASE_SPEED · the floor rig for 3.2 / 3.5 / VIDEO 3.1 ·
**a real TRIM run for `IMAGE 3.6`** · **THE SURFACE TEST: run 7E on a lab tile and see whether
the encoder square actually collapses.**

---

# PUSHING — READ THIS

Named-file CLI for adds and modifies; **GitHub Desktop for deletions.** **Never `git add .`**

1. **DELIVER THE FILES.** Every artefact destined for the repo goes through `present_files`;
   instructions and md5s go in the CHAT ONLY. Checksums are not a deliverable.
2. **`(1)` does not mean stale.** Verify by **md5**, never by suffix.
3. **Never present a test file, or a DIAGNOSTIC, in the same list as repo files.**
4. **Never produce PUSH_ME_*.md or MD5_*.txt.**
5. **`lessons/` IS PART OF THE FILENAME. `css/` likewise.** `present_files` flattens both —
   the download shows `book.css`, not `css/book.css`. **S128 shipped ten such files; say the
   directory out loud in the push message every time.**
6. **A push that bumps a version and omits LIVE.md is an INCOMPLETE push (§12.6).**
7. **§27.8b's third step is `strip_inline --apply --include-held`.** Without the flag, held
   strings revert to inline and innocent lessons are rewritten.
8. **After any `css/book.css` regeneration, stage into a copy of the PUSHED CLONE and run
   `book_gates` THERE before presenting md5s. Diff by LINE, not only by expansion.**
9. **Exactly ONE `ZUMO_SNN_HANDOFF.md` in the root (gate 28).** At S129 close, adding
   `ZUMO_S130_HANDOFF.md` means DELETING **this** file — a GitHub Desktop checkbox.
10. **THE NUMBER IN THE FILENAME IS THE SESSION THAT READS IT, NOT THE ONE THAT WROTE IT.**
11. **Never write a real version number as an arrow pair in prose.** `_versions_in()` takes the
    LAST match. Write *"reaches vNEW (from vOLD)"*. Backticks do not shield it.
12. **THE SAME TRAP APPLIES TO SHAs.** One sha per parsed line.
13. **A document cannot name the commit that contains it.** LIVE.md's verification line names
    the commit carrying the PREVIOUS state.
14. **AN EDIT TO A FILE WITH REPEATED LANDMARK LINES TARGETS AN INDEX AND ASSERTS IT** (§6.12c).
    **S128 WALKED INTO THIS AND THE ASSERT IS WHY IT COST NOTHING:** the Bible's
    `v8.119, S127` anchor occurs on the header line AND on the changelog line, and a
    first-occurrence insert put the whole new entry INSIDE line 17. Caught by
    `bible_consistency()`, reverted from snapshot, redone against an asserted line index.
    LIVE.md likewise has TWO `**Versions:**` lines and the second must not move.
15. **A VERSION HOME FOUND BY GREPPING FOR A SPELLING IS A HOME YOU HAVE NOT ENUMERATED.**
    `session_versions` holds the regex for every registered artefact — read ARTEFACTS.
16. **WRITE THE GATE IN THE SAME PASS AS THE RULING.** Held at S126, S127 and S128.
17. **A CONTROL HARNESS MUST SNAPSHOT EVERY FILE IT CAN TOUCH — AND `git checkout --` IS NOT A
    RESTORE FOR UNCOMMITTED WORK.** Keep the untouched-tree control at BOTH ends of the run.
    **S128 used a full-tree md5 snapshot taken at session open and reverted from it twice.**
18. **A GATE THAT PINS A SPELLING CERTIFIES WHATEVER IT WAS GIVEN. PIN THE PROPERTY.**
    Gate 57 asserts a contrast RATIO; gate 58 a spelling PROPERTY; **gate 59 re-derives the
    family from CONTENT and requires the attribute to agree, so it cannot certify a
    hand-typed value.**
19. **WHEN A SPELLING IS RULED, SCAN EVERY INSTRUMENT BY AST FOR THE OLD ONE.** **This is
    S129's FIRST JOB and it is not optional** — §5.1 already lost 11 labels on one lesson's
    worth of marks, and the emoji has not even been removed yet.
20. **NEW, S128: A HOLD THAT IS ALSO SATISFIED BY AN ACCIDENT IS NOT A HOLD.** `mark_wire`'s
    Control E caught BRAIN CHECK falling out of scope on a middot mismatch rather than on its
    named hold — delete the hold and behaviour was identical. **Every named exception needs a
    control proving the exception is what excludes it.**
21. **NEW, S128: WHEN A READING INSTRUMENT GROWS A WRITING CONSUMER, RE-PROVE EVERY COORDINATE
    IT REPORTS AGAINST THE FILE ON DISK.** A coordinate only ever compared with other
    coordinates from the same instrument has never been tested.
