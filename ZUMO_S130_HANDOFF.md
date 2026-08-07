# ZUMO — S130 HANDOFF (written at S129 close · paste at top of Session 130)

## Session open ritual (do this without being asked)
1. **`git ls-remote https://github.com/Weymuth/zumo.git HEAD` FIRST.** A stale answer is
   timing, not caching — **retry a minute later before concluding a push failed** (§12.4).
2. Read `LIVE_ZUMO_TEXTBOOK.md` — verify date / status / versions.
3. **Do NOT grep the Bible version.** `session_versions.bible_consistency()` parses it; the
   Bible has THREE homes and fails if any two disagree.
4. Run the full suite and **READ THE EXIT CODE, NOT THE LAST LINE**. Same list as S129, plus
   **`glyph_scan.py --selftest` then bare** (NEW S129 — a bare run reports leads and exits 1
   when any is NEW; 3 NEW is the current, read state, see below).
5. If `flatten_alpha --selftest` prints `NOT FULLY TESTED`: `pip install cairosvg
   --break-system-packages`. **Needed every session.**
6. **NEVER run `build_css.py --help` or `session_versions.py --help`.** Neither has a help
   branch; `build_css` BUILDS against whatever tree is on disk.
7. `--anomalies` is SILENT when clean. Anything it prints is a real lead.
8. **Do not hand-type a version, and do not hand-type a COUNT.** `session_versions.py
   --live` / `--handoff` EMIT the blocks.
9. **`gate_payload_match.py` needs the FULL lesson glob.**
10. Entrypoints are traps — add **`glyph_scan.scan(paths)`** and `glyph_scan.scan_file(path)`.
11. **A CLONE IS NOT THE SITE.** Run `site_parity.py` after any push; it can FAIL on the
   first run in the minute after a push and pass on retry (S112).
12. **VERIFY THE PUSH BY FRESH CLONE AND MD5 — AND DIFF THE STAGE AGAINST THE CLONE.**
13. **`css/semantic.css` IS HAND-EDITED ON PURPOSE (§27.15).** `css/book.css` is not.
14. **`regex_audit.py` after any gate you write.**
15. **`session_versions --check` will report disagreements at session open naming
   `ZUMO_S130_HANDOFF.md`** — the INCOMING document, stale by definition once work starts.
   If a line names LIVE.md or the Bible, that IS drift.

---

# SEPTEMBER 8 IS ABOUT FOUR WEEKS OUT

**14 images outstanding of 141.** Unchanged. Photography still parked.

---

# THE ONE THING TO CARRY OUT OF S129

**A CONTROL THAT DEPENDS ON THE STATE OF WHAT IT AUDITS IS NOT A CONTROL.**

`glyph_scan` shipped with a Control A asserting that §5.1's two glyph pins were present in
the live `book_gates.py`. They were — that was the whole point of the session — and the
moment they were removed the control failed. It was pinned to a defect that was supposed to
go away, so it could only ever be right once. Rebuilt against a scratch fixture reproducing
the S128 shape verbatim, where it stays loud permanently.

Its Control F then fired **twice more, both on my own edits**, each time because an
acceptance named a site I had just rewritten. That is the same rule from the other side and
it is why the ACCEPTED table is keyed on a derived expression rather than a line number: a
hold for a site that no longer exists must expire loudly.

---

# STATE

<!-- VERSION BLOCK: emitted by session_versions.py --handoff. Never hand-typed. -->
Fresh-clone verified at **`4ab805a`**. Census **40,698**.
Bible **v8.121** · `BookComponentStandard` **v01.12.1** · Maker **v2.45.4** ·
`marks/` **41** · `icons/` **49** incl. LICENSE.
`ZUMO_Syllabus_WORKING.md` **v1.2**.

Instruments: `book_gates` **v1.55** · `lesson_inventory` **v1.3.2** ·
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
`mark_wire` **v1.0.2** ·
`glyph_scan` **v1.0** ·
`title_feed` **v1.0** ·
`timer.html` **v1.3.2** ·
`going_deeper` **v01.6.1**.

Lessons: L01 v03.23.2 · L02 v03.16.0 · L03 v03.35.0 · L04 v04.23.2 · L05 v04.23.0 · L06 v04.27.2 · L07 v04.26.2 · L08 v04.25.0 · L09 v05.20.2 · L10 v02.21.2 · L11 v02.22.2 · L12 v01.25.0 · L13 v02.22.2 · L14 v02.27.2 · L15 v02.23.2 · L16 v02.16.1.

**59/59 gates.** `--anomalies` silent · family map **1069/1069** · `regex_audit` **1 lead** ·
`build_css --check` current at **604 rules** · `strip_inline --verify` 0 dead class names ·
`color_index --check` clean · `image_audit --check` current at 14 outstanding of 141 ·
`gate_payload_match` PASS on the full glob · `next_pointer --check` and `title_feed --check`
clean · `entity_sweep` decoded text byte-identical in 21 files · `family_tag` **1069 correct,
0 to write** · `site_parity` **PARITY** · `glyph_scan` **3 NEW leads, all read** (below).

**§27.11 holds at 604 / 2,141** across two regenerations — zero born, zero died, zero
altered. `.div-fs-09em` moved 156 → 160 → 154 and the attribute count tracked it exactly.

---

# S129 WORK — SEE `LIVE_ZUMO_TEXTBOOK.md` FOR THE FULL ACCOUNT

**One Bible entry (v8.121). Six lessons, four instruments, one new tool, one deletion.**

**THE MARKS ARC'S THREE PREREQUISITES ARE ALL CLEAR.** S129 opened with them blocking
`mark_wire --apply`; none of them blocks it now.

1. **The AST scan is done and is an instrument, not a one-off.** `glyph_scan.py` v1.0.
   **§5.1 was the ONLY gate pinned on the glyph**, and a separate sweep found **zero
   glyph-pinned locators outside Python** — the blast radius was one gate.
2. **The detector is widened.** `lesson_inventory` v1.3.2 sees `</>`. It needed **three**
   fixes, not the one predicted — see below.
3. **§21's baseline is DERIVED at 1,134**, delta exactly **884**, reconciling against a
   per-lesson count. **Do not move the constant until the marks are actually applied.**

**§5.1 NOW READS `data-family`, NOT THE GLYPH**, in both places the glyph sat. Coverage 251
→ 255. The decisive proof is the S128 experiment re-run: 34 marks on L04, the exact input
that measured 251 → 240, leaves the gate at **255**.

**DJ RULED A** on rendered specimens (*"B looks stupid"*): canonical family glyph in the
label, old glyph dropped. Four blocks split — then reading BELOW the label found the class
rather than the instance: **8 of 183 two-div blocks opened their title with their own family
word**. All eight fixed. **Both residues have one cause:** `sweep_option_c.py` scoped on
`FAMILY_GLYPHS` and §5.1 scoped on `_FAMGLYPH`, so the sweep and the gate shared one blind
spot and the blocks it missed are exactly the blocks the gate could not see.

**`sweep_option_c.py` IS DELETED** (DJ ruling), its ruling verified recorded in the v8.79 changelog
entry and in `BookComponentStandard` §5.1 first. It is also out of `session_versions.UNVERSIONED` —
**those two edits are coupled and must ride the same push.**

**A BOOK DEFECT NO GATE COULD SEE:** two L16 WARNING blocks carried a **doubled variation
selector**. A lone selector renders as nothing, so it was invisible on the page, to every
gate, and to `entity_sweep`, which compares DECODED text. Found only because `mark_wire`'s
own read-back assert refused to finish the file. Censused at exactly two, both L16.

---

# S130 QUEUE

## THE MARKS ARC — NOTHING BLOCKS `--apply` NOW

`mark_wire` v1.0.2 reconciles at **884 SWAP + 13 NO_GLYPH + 56 HELD**. **It is still not
applied, and that is DJ's ruling to make, not an oversight.** When it runs:
- **§21's coverage constant moves 250 → 1,134.** Derived, not projected. Move it in the same
  pass and control it in the failing direction.
- **The 13 NO_GLYPH blocks get an INSERTION, not a swap** — `mark_wire` reports them and
  does not write them. L14's DO THIS NOW header is an `<h4>` one level deeper than the other
  twelve, **so that one needs its own locator.**
- **DJ RULED EACH L12 GLOSSARY TERM GETS THE MARK**, not just the first of the run.
- **BRAIN CHECK is HELD BY NAME** (§25.2a) and the hold is real and provable — but **if the
  §7.1 middot normalisation is ever removed, the hold silently stops working.**

## RULED THIS SESSION, NOT YET DONE
- **Bible §8's LOCKED 11-type callout table becomes a POINTER to `BookComponentStandard`
  §7.** Measured: BCS is parsed by SIX instruments and the Bible by ONE, 30 KB against
  694 KB, and §8 opens with *"All callouts use inline `style=` only"*, which §27 retired.
- **§21's coverage constant and `build_family_map`'s frozen total are ONE ruling, not two**
  (DJ: *"probably"*). Both are hand-moved literals, both about to move for the same arc.

## `glyph_scan`'s 3 NEW leads — READ, not defects
- `book_gates:843` — `blk2.count('\u2610')`. Safe, **but by the BRAIN CHECK hold**: all 14
  ☐-led callouts are BRAIN CHECK, so §25.10's checkbox/skill-tag count is an unrecorded
  dependent of that hold. **Record the dependency.**
- `engine.py:103` — `'\u2192' in plain or '→' in plain`. Innocent for the arc (it separates
  pseudo-code `<pre>` from C++), but it is **one character spelled two ways in one
  expression**, §27.16's shape, in a file no instrument list names.
- `lesson_inventory:660` — compares against a label the parser generates itself. Innocent.

## `glyph_scan`'s own known limit — RECORDED HONESTLY
Its D2 floor is **U+2100, the same floor `lesson_inventory` had**. An ASCII pseudo-glyph pin
is invisible to the scanner exactly as `</>` was invisible to the detector. The detector was
widened at S129; **the scanner was not.** Same §24.8 shape, in the tool written to find it.

## Opened S127 and still not ruled
- **The 38 entities inside ATTRIBUTE values are excluded as a SCOPE, not an exception.**
- **`index.html` carries no version home.** Same shape as `timer.html` at S123.
- **`BONUS_MARK` in `book_gates.py` and `MARK` in `gen_bonus_banner.py` are indexed nowhere**
  and two stray-checks cannot fire. **Still unruled: delete, or hold as the banner's entry
  point in the marks arc?** The banner is exactly where a mark would go.

## The glossary arc — reachable, shape already ruled
`data-family` made it harvestable; **the mark does NOT do this, the attribute does.** 184
KEY TERM blocks, 172 with an extractable term, 55 already anchored, **106 distinct terms**.
DJ ruled: **keep every definition where it is** (additive, throwaway) and **one entry per
lesson-term pair, disambiguated by topic**. The "drift" hypothesis was tested and does not
hold — 39 of 49 repeats are within a SINGLE lesson, zero pairs above 0.90 similarity.
**The Tier-3 census item *"glossary reported absent in all sixteen"* is FALSE** — correct it
rather than acting on it. §7 already reserves `journal-bookmark` and nothing uses it.

## The colour ledger — unchanged
16 items; three marked *re-measure before ruling*. **`#f8f9fa` (641 instances) remains the
largest unreported surface.** **NEW: L03's `div-c-922b21` title red** — a colour class no
other §6.6a block uses, left alone by ruling at S129, belongs in the ledger.

## Graduation candidates
`code` (S123), the pill (S124), the dark block (S126), the mark (S128). Next: **callout
families — but NOT before the colour ledger.** `going_deeper.html` defines its own
`.callout` and consumes the semantic layer; check what a graduation does to that page first.

## The consistency census — Tier 3
- **Nav pill count ranges 10 to 19**; §6.5's "12-14" rule is obsolete — **rewrite the rule
  before touching a lesson.**
- **Quick-reference anchors exist in five lessons only** (L02-L06).
- **Tier 3 needs reading, not counting:** §7 ladder rungs 7A-7E appear in six lessons only;
  L16's Engineer's Log wrapper does not match the other fifteen; **timers appear in L02,
  L03, L04 only — S69 already burned a session on a false finding here, READ before
  counting.**
- **Callout border-width probe returned zero shapes** — it looked for inline `border-left`,
  which §27 deleted; it has to read the stylesheet now.

## Carried, unchanged
- **Should `css/semantic.css` carry a version home?** Carried since S123. FOUR gates depend
  on its contents and it has an external consumer.
- **L01's BC02 does not carry L01's objectives.** Ruled legacy S119.
- **S116's past-tense question: RETIRE IT.** Fifteen sessions now.
- **L10's `What You Built` is the only non-Brain-Check `<h4>` in a converted §10.**
- **L14's score formula is marked up as `<code>` and is not code.**
- **L03's `id="whats-next"` is in all fifteen**; §27.14 cannot see an unreached id.
- **`index.html` is §27.12's only NAMED exception**, held by name.
- **`regex_audit` reports 1 lead, `entity_sweep.py:70`** — a match-and-discard false
  positive. **Suppress it or record it, but stop re-discovering it every session.**
- **`.DS_Store` and a `__pycache__` `.pyc` are committed.** Housekeeping, not urgent.

## Rulings outstanding — carried
- Should `build_family_map` parse its total instead of holding a baseline? **Now coupled to
  §21's constant by DJ's S129 ruling — answer them together.**
- Should `build_css` name rules by usage RANK at all? Fired at S126 and again at S128.
  **S129 saw it move `.div-fs-09em` twice without harm, which is the other side of the case.**
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
**§7.2 names seven marks that are not on disk** and three on disk are in no table.

## Bench (need the robot — parked with photography)
Q017 L09 six numbers · Q044 calibration-spin · Q046 gyro-bias · L02 §5 green-LED ·
Constrain RUN_MS · cm/s at a stated BASE_SPEED · the floor rig for 3.2 / 3.5 / VIDEO 3.1 ·
**a real TRIM run for `IMAGE 3.6`** · **THE SURFACE TEST: run 7E on a lab tile and see
whether the encoder square actually collapses.**

---

# PUSHING — READ THIS

Named-file CLI for adds and modifies; **GitHub Desktop for deletions.** **Never `git add .`**

1. **DELIVER THE FILES.** Every artefact destined for the repo goes through `present_files`;
   instructions and md5s go in the CHAT ONLY. Checksums are not a deliverable.
2. **`(1)` does not mean stale.** Verify by **md5**, never by suffix.
3. **Never present a test file, or a DIAGNOSTIC, in the same list as repo files.**
4. **Never produce PUSH_ME_*.md or MD5_*.txt.**
5. **`lessons/` IS PART OF THE FILENAME. `css/` likewise.** `present_files` flattens both —
   **say the directory out loud in the push message every time.**
6. **A push that bumps a version and omits LIVE.md is an INCOMPLETE push (§12.6).**
7. **§27.8b's third step is `strip_inline --apply --include-held`.**
8. **After any `css/book.css` regeneration, stage into a copy of the PUSHED CLONE and run
   `book_gates` THERE before presenting md5s. Diff by LINE, not only by expansion.**
9. **Exactly ONE `ZUMO_SNN_HANDOFF.md` in the root (gate 28).** At S130 close, adding
   `ZUMO_S131_HANDOFF.md` means DELETING **this** file — a GitHub Desktop checkbox.
10. **THE NUMBER IN THE FILENAME IS THE SESSION THAT READS IT, NOT THE ONE THAT WROTE IT.**
11. **Never write a real version number as an arrow pair in prose.** `_versions_in()` takes
    the LAST match. Write *"reaches vNEW (from vOLD)"*. Backticks do not shield it.
12. **THE SAME TRAP APPLIES TO SHAs.** One sha per parsed line.
13. **A document cannot name the commit that contains it.**
14. **AN EDIT TO A FILE WITH REPEATED LANDMARK LINES TARGETS AN INDEX AND ASSERTS IT**
    (§6.12c). The Bible's version anchor occurs on line 17 AND in the changelog.
15. **NEW, S129: AN EDIT THAT CHANGES LINE COUNT INVALIDATES EVERY LINE-KEYED TARGET BELOW
    IT IN THE SAME FILE.** Go **DESCENDING per file**. S129 walked into this on L03 and the
    callout lookup's `count == 1` assert is the only reason it cost nothing.
16. **NEW, S129: A SNAPSHOT TAKEN BEFORE THE WORK IS NOT A SNAPSHOT OF THE WORK.** S126's
    rule 17 reached by a new road: a restore from the SESSION-OPEN snapshot silently reverted
    L02's fixes and its version bump. Re-snapshot after every landed batch.
17. **NEW, S129: A CONTROL THAT DEPENDS ON THE STATE OF WHAT IT AUDITS IS NOT A CONTROL.**
    Reproduce the defect as a fixture; never assert that the live defect still exists.
18. **A GATE THAT PINS A SPELLING CERTIFIES WHATEVER IT WAS GIVEN. PIN THE PROPERTY.**
19. **WHEN A SPELLING IS RULED, SCAN EVERY INSTRUMENT BY AST FOR THE OLD ONE.** This is now
    `glyph_scan.py` — but **mind its U+2100 floor**, which is the very blindness it exists
    to find.
20. **A HOLD THAT IS ALSO SATISFIED BY AN ACCIDENT IS NOT A HOLD.**
21. **WHEN A READING INSTRUMENT GROWS A WRITING CONSUMER, RE-PROVE EVERY COORDINATE IT
    REPORTS AGAINST THE FILE ON DISK.**
