# ZUMO — S132 HANDOFF (written at S131 close · paste at top of Session 132)

## Session open ritual (do this without being asked)
1. **`git ls-remote https://github.com/Weymuth/zumo.git HEAD` FIRST.** A stale answer is
   timing, not caching — **retry a minute later before concluding a push failed** (§12.4).
2. Read `LIVE_ZUMO_TEXTBOOK.md` — verify date / status / versions.
3. **Do NOT grep the Bible version.** `session_versions.bible_consistency()` parses it; the
   Bible has THREE homes and fails if any two disagree.
4. Run the full suite and **READ THE EXIT CODE, NOT THE LAST LINE**. Plus
   **`callout_id.py --selftest` then `--audit`**.
5. **`--anomalies` BELONGS TO `lesson_inventory`, NOT `session_versions`.** Correct:
   `python3 lesson_inventory.py --anomalies lessons/*.html`, which IS silent when clean.
6. If `flatten_alpha --selftest` prints `NOT FULLY TESTED`: `pip install cairosvg
   --break-system-packages`. **Needed every session.**
7. **NEVER run `build_css.py --help` or `session_versions.py --help`.** Read the docstring.
8. **Do not hand-type a version, and do not hand-type a COUNT.**
9. **`gate_payload_match.py` needs `newproject.html` FIRST, then the full lesson glob.**
10. **A CLONE IS NOT THE SITE.** Run `site_parity.py` after any push.
11. **VERIFY THE PUSH BY FRESH CLONE AND MD5 — AND DIFF THE STAGE AGAINST THE CLONE.**
12. **`css/semantic.css` AND `ZUMO_FAMILY_PINS.md` ARE HAND-AUTHORED PRESERVED LAYERS.**

---

# SEPTEMBER 8 IS ABOUT FOUR WEEKS OUT

**14 images outstanding of 141** — and that number was nearly lost this session. Photography
still parked.

---

# THE ONE THING TO CARRY OUT OF S131

**AN ARC'S PRICE IS PAID BY THE INSTRUMENTS NOBODY POINTED AT IT.**

S130's lesson was *run the blinding control against the consumer that CAN fail*. S131 found the
same shape one instrument later, and the reason is simpler and worse: **`image_audit` was never
in the marks arc's blast radius because nobody thought to put it there.** It had been silently
wrong since that push, reporting **8 outstanding against a true 14**, and the only signal was
`--check` printing DIFFERS — whose obvious reading is *re-run me*, which would have written the
wrong number into the shot list four weeks before the course.

**When an arc changes the markup, enumerate every instrument that READS that markup, not every
instrument the arc's ruling mentions.**

And the session's second finding, which cost more time than the first: **re-derive a
measurement, but READ THE RECORD for a design.** The per-lesson glossary dual was ruled at S128
and its drift hypothesis already tested and rejected; S131 re-derived it as a defect and priced
a ruling on it before DJ named the prior decision.

---

# STATE

<!-- VERSION BLOCK: emitted by session_versions.py --handoff. Never hand-typed. -->
Fresh-clone verified at **`96d41cd`**. Census **40,683**.
Bible **v8.123** · `BookComponentStandard` **v01.12.1** · Maker **v2.45.4** ·
`marks/` **41** · `icons/` **49** incl. LICENSE.
`ZUMO_Syllabus_WORKING.md` **v1.2**.

Instruments: `book_gates` **v1.58** · `lesson_inventory` **v1.3.4** ·
`gen_component` **v1.6.1** · `pill_sweep` **v1.1** · `gate_payload_match` **v1.7** ·
`build_family_map` **v1.4.0** · `callout_id` **v1.0** · `build_mark_index` **v1.1.0** · `gen_bonus_banner` **v1.4.1** ·
`gen_part_banners` **v1.2** · `session_versions` **v1.22.0** · `fit_raster_svg` **v1.2** ·
`flatten_alpha` **v1.2** · `svg_layout_audit` **v1.20** · `site_parity` **v1.1** ·
`build_css` **v1.3.0** ·
`image_audit` **v1.2** ·
`strip_inline` **v1.2** ·
`build_worklist` **v1.1** ·
`regex_audit` **v1.0** ·
`build_palette` **v1.1** ·
`class_sweep` **v1.0** ·
`color_index` **v1.0** ·
`entity_sweep` **v1.0** ·
`font_stack_sweep` **v1.3.0** ·
`next_pointer` **v1.2** ·
`family_tag` **v1.1** ·
`mark_wire` **v1.0.2** ·
`glyph_scan` **v1.1** ·
`title_feed` **v1.0** ·
`timer.html` **v1.3.2** ·
`going_deeper` **v01.6.1**.

Lessons: L01 v03.24.0 · L02 v03.17.0 · L03 v03.36.1 · L04 v04.24.0 · L05 v04.24.0 · L06 v04.28.0 · L07 v04.27.0 · L08 v04.26.0 · L09 v05.21.0 · L10 v02.22.0 · L11 v02.23.0 · L12 v01.26.0 · L13 v02.23.0 · L14 v02.28.0 · L15 v02.24.0 · L16 v02.17.0.

**63/63 gates.** `lesson_inventory --anomalies` silent · family map **1069/1069** ·
`family_tag` **1069 correct, 0 drifted, 0 unnamed** · `callout_id --audit` **1069, 0 problems** ·
census **40,683 == `wc -l`** · `regex_audit` **1 lead** (known `entity_sweep.py:70`) ·
`build_css --check` current at 604 rules · `color_index --check` clean ·
**`image_audit --check` current at 14 of 141** · `gate_payload_match` PASS · `site_parity` PARITY.

---

# S132 QUEUE

## THE ARC: THE GLOSSARY CLEANUP (DJ ruled A, S131)

**Measured, ruled, not started.** DJ: *"I feel like we need to clean up the lessons first."*

- **151 glossary entries in FIVE schemas.** KEY TERM card 97 (L01 02 03 05 06 07 08 09 10 12 16) ·
  bare `div-9b59b6` 14 (L04) · `<dl>/<dt>` 15 (L13 L14) · table 25 (L11 L15).
- **97 cards + 87 body KEY TERM = 184**, the family map's total, exactly.
- **The other 54 carry no `data-family` and no `data-callout`** — invisible to
  `build_family_map`, `family_tag`, `callout_id`, the pin and every gate reading through them.
  **This is what threatens S128's ruled additive glossary:** a harvest keyed on `data-family`
  misses a third of the terms and nothing fires.
- **L12's ten cards wear `callout-2e86ab-bg-fff` — blue on white, no key mark** — while still
  tagged KEY TERM. Four more cards use `-e7d4ff-2`, a one-declaration margin drift.
- **RULED: normalize all 151 to the canon term card. NO EM DASH.**
- **THE CANON MUST BE RESTATED FIRST.** Its inline `style=` is superseded by §27, its
  `<span>🔑</span>` by S130, its `<strong id="term-...">` by the live tree (the term sits in
  `div-fs-105em`; `<strong>` 60 of 97, `<b>` 10, the id 37).
- **THE TARGET IS DERIVED:** wrapper `.callout-9b59b6-bg-e7d4ff` (83 of 97, and byte-identical
  to the Bible's five declarations), head `div-fs-105em` (88 of 97), mark `key` (87 of 97).
- **DO THE PIN QUESTION FIRST — it is a 141-pin swing.** Every callout inside a glossary region
  is a KEY TERM, **97 of 97**, so a structural tier resolves all 151 with **zero new pins**;
  convert first and it is +54, taking the pin to 266. **A section id is STRUCTURE, not
  decoration** — that distinction is the whole argument and belongs in the ruling, because
  colour and glyph both died for being decoration. **Prove it against `family_tag`, the auditor
  that CAN fail, never against `build_family_map`, which reads the attribute first.**
- **SEPARATE RULING, NOT FOLDED IN:** 87 of the pin's 159 KEY TERM rows are glossary-side and
  would become redundant. Deleting from a preserved layer deserves its own decision.
- **PRICE:** family map 1069 → 1123 · 54 new AUTHORED `data-callout` ids · §21 coverage
  1,134 → 1,188 · dead classes (`div-9b59b6`, the `dl/dt/dd` rules, two table classes) so
  **§27.15b's rename trap applies — strip → regenerate → rename survivors → regenerate.**
- **THE LINK DIRECTION IS RULED** (DJ, S131 and S128 agreeing): body key term → the glossary,
  additive, not arbitrary-mention → vocab. **Measured: 56 of 81 body terms have a same-lesson
  glossary entry; 25 do not, and L11 / L12 / L13 have ZERO body KEY TERM callouts.** Whether the
  25 get authored entries is unruled.
- **READ S128's RULING BEFORE DESIGNING ANY OF THE GLOSSARY** — keep every definition in place,
  the glossary is ADDITIVE, one entry per lesson-term pair disambiguated by topic
  (*Dead Reckoning (gyro)* vs *Dead Reckoning (encoders)*). **The dual is DESIGN, not drift.**

## Opened S131, unruled
- **L07 `[IMAGE 7.3]`** is landed by `L07_GRAPHIC_7-15_platformio_file_tree.svg` — a GRAPHIC
  standing in for an IMAGE across the two number spaces (§10), no prose declaring it, where
  L10's equivalent says so in the lesson. **Held by name in gate 63's `REUSE`, marked UNRULED.**
  Ruling it wrong in either direction either loses a real shot or sends DJ to re-shoot.

## Ruled but not done — carried from S129
- **Bible §8's LOCKED 11-type callout table becomes a POINTER to `BookComponentStandard` §7.**
- **§21's coverage constant and `build_family_map`'s frozen total are ONE ruling** (DJ: *"probably"*).

## Carried, unchanged
- **Should `ZUMO_FAMILY_PINS.md` carry a version home?** Same shape as the `css/semantic.css`
  question, now with a gate depending on it.
- **The 3 `glyph_scan` leads** — `book_gates:843` (☐, a BRAIN CHECK dependency to record),
  `engine.py:103` (dead code, verified S130), `lesson_inventory:688` (innocent).
- **`glyph_scan`'s U+2100 floor** — an ASCII pseudo-glyph is still invisible to it.
- **Nav pill count ranges 10 to 19**; §6.5's "12-14" rule is obsolete — **rewrite before touching a lesson.**
- **Quick-reference anchors exist in five lessons only** (L02-L06).
- **Timers appear in L02, L03, L04 only — S69 burned a session on a false finding here, READ before counting.**
- **Callout border-width probe returned zero shapes** — it looked for inline `border-left`, which
  §27 deleted; it has to read the stylesheet now.
- **The colour ledger — 16 items, `#f8f9fa` (641 instances) the largest unreported surface**, plus
  L03's `div-c-922b21` title red.
- **45 of the book's 55 `id="term-*"` anchors are targeted by no link on any page** — S121's orphan
  `id="whats-next"` at scale, and §27.14 is structurally blind to it (it asserts links resolve,
  never that ids are reached).
- **`index.html` carries no version home** · **`BONUS_MARK`/`MARK` indexed nowhere** ·
  **L01's BC02 does not carry L01's objectives** (legacy, S119) · **S116's past-tense question:
  RETIRE IT** · **L14's score formula is `<code>` and is not code** ·
  **the two `book_gates` versions S115 shipped carry NO changelog line** ·
  **four `data-reveal="mechanism"` blocks are not on §20.1's whitelist** ·
  **The mark roster RECONCILES and is gated (61). Do not re-open.**

## Bench (need the robot — parked with photography)
Q017 L09 six numbers · Q044 calibration-spin · Q046 gyro-bias · L02 §5 green-LED ·
Constrain RUN_MS · cm/s at a stated BASE_SPEED · the floor rig for 3.2 / 3.5 / VIDEO 3.1 ·
a real TRIM run for `IMAGE 3.6` · **THE SURFACE TEST: run 7E on a lab tile.**

---

# PUSHING — READ THIS

Named-file CLI for adds and modifies; **GitHub Desktop for deletions.** **Never `git add .`**

1. **DELIVER THE FILES** via `present_files`; instructions and md5s in the CHAT ONLY.
2. **`(1)` does not mean stale.** Verify by **md5**, never by suffix.
3. **Never present a test file or a DIAGNOSTIC beside repo files.**
4. **Never produce PUSH_ME_*.md or MD5_*.txt.**
5. **`lessons/` IS PART OF THE FILENAME. `css/` likewise.** Say the directory out loud.
6. **A push that bumps a version and omits LIVE.md is an INCOMPLETE push (§12.6).**
7. **Exactly ONE `ZUMO_SNN_HANDOFF.md` in the root (gate 28).** Adding this file means
   DELETING `ZUMO_S131_HANDOFF.md` — a GitHub Desktop checkbox.
8. **THE NUMBER IN THE FILENAME IS THE SESSION THAT READS IT.**
9. **Never write a real version number as an arrow pair in prose.** `_versions_in()` takes the
   LAST match. Write *"reaches vNEW (from vOLD)"*.
10. **A document cannot name the commit that contains it.**
11. **AN EDIT TO A FILE WITH REPEATED LANDMARK LINES TARGETS AN INDEX AND ASSERTS IT** (§6.12c).
    **S131 hit this live:** the Bible's version anchor sits on line 17 AND in the changelog, and
    a `count == 1` assert caught it before anything was written. Anchor each home uniquely.
12. **AN EDIT THAT CHANGES LINE COUNT INVALIDATES EVERY LINE-KEYED TARGET BELOW IT.** Go
    DESCENDING per file.
13. **A SNAPSHOT TAKEN BEFORE THE WORK IS NOT A SNAPSHOT OF THE WORK.** Re-snapshot after every
    landed batch.
14. **A CONTROL THAT DEPENDS ON THE STATE OF WHAT IT AUDITS IS NOT A CONTROL.**
15. **A CONTROL RUN AGAINST AN UNTRACKED FILE HAS NO RESTORE PATH.**
16. **A LIBRARY MAY NOT EXIT.** A module-level `SystemExit` in anything the suite imports kills
    the run MID-SUITE and can still exit 0.
17. **RUN A BLINDING CONTROL AGAINST THE CONSUMER THAT CAN FAIL.**
18. **A DERIVED KEY IS NOT AN IDENTITY.** If a record must survive an edit, the key is AUTHORED.
19. **A GATE THAT PINS A SPELLING CERTIFIES WHATEVER IT WAS GIVEN. PIN THE PROPERTY.**
20. **A HOLD THAT IS ALSO SATISFIED BY AN ACCIDENT IS NOT A HOLD.**
21. **NEW, S131: SNAPSHOT THE STATE YOU ARE IN, NOT THE STATE YOU ARE LEAVING.** A control run
    that restores the BEFORE snapshot destroys the fix under test and looks like a clean restore.
    Snapshot the FIXED tree before the first injection.
22. **NEW, S131: A GENERATED ARTEFACT PRINTING `DIFFERS` IS A LEAD, NOT AN INSTRUCTION.** Read
    the diff before regenerating. Re-running `image_audit` would have written 8 over 14 and
    silently retired six real photographs from the shot list.
