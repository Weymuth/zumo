# ZUMO — S131 HANDOFF (written at S130 close · paste at top of Session 131)

## Session open ritual (do this without being asked)
1. **`git ls-remote https://github.com/Weymuth/zumo.git HEAD` FIRST.** A stale answer is
   timing, not caching — **retry a minute later before concluding a push failed** (§12.4).
2. Read `LIVE_ZUMO_TEXTBOOK.md` — verify date / status / versions.
3. **Do NOT grep the Bible version.** `session_versions.bible_consistency()` parses it; the
   Bible has THREE homes and fails if any two disagree.
4. Run the full suite and **READ THE EXIT CODE, NOT THE LAST LINE**. Plus
   **`callout_id.py --selftest` then `--audit`** (NEW S130).
5. **`--anomalies` BELONGS TO `lesson_inventory`, NOT `session_versions`** — CORRECTED S130.
   The S130 handoff filed it under `session_versions`, which has no such flag, so an
   unrecognised arg fell through to the FULL VERSION REPORT. Run literally, the old ritual
   manufactured a lead every session. Correct: `python3 lesson_inventory.py --anomalies
   lessons/*.html`, which IS silent when clean. Bible §24 always had this right.
6. If `flatten_alpha --selftest` prints `NOT FULLY TESTED`: `pip install cairosvg
   --break-system-packages`. **Needed every session.**
7. **NEVER run `build_css.py --help` or `session_versions.py --help`.**
8. **Do not hand-type a version, and do not hand-type a COUNT.**
9. **`gate_payload_match.py` needs `newproject.html` FIRST, then the full lesson glob.**
10. **A CLONE IS NOT THE SITE.** Run `site_parity.py` after any push.
11. **VERIFY THE PUSH BY FRESH CLONE AND MD5 — AND DIFF THE STAGE AGAINST THE CLONE.**
12. **`css/semantic.css` AND `ZUMO_FAMILY_PINS.md` ARE HAND-AUTHORED PRESERVED LAYERS.**
13. **`.DS_Store` / `__pycache__` housekeeping is DONE** — a `.gitignore` covers both.
    RETIRED from this list at S130; stop re-checking it.

---

# SEPTEMBER 8 IS ABOUT FOUR WEEKS OUT

**14 images outstanding of 141.** Unchanged. Photography still parked.

---

# THE ONE THING TO CARRY OUT OF S130

**A STOPGAP THAT RESOLVES REAL BLOCKS IS NOT A STOPGAP, IT IS A DEPENDENCY.**

S112 deleted a COLOUR-keyed tier and replaced it with a GLYPH table. S130 deleted the GLYPH
table. Same failure, one decoration later — **and the second was caused by the fix for the
first.** The tier shipped calling itself temporary and was load-bearing for 212 blocks
eleven sessions on. §24.14c now forbids keying any tier on decoration at all.

**And the acceptance that certified it was measured on the wrong consumer.** `glyph_scan`'s
S129 entry read *"GLYPH={} still returns 1069/1069, so no family depends on it"* — true, and
false in its conclusion, because `build_family_map` reads `data-family` first and cannot fail
that test. The AUDITOR, `family_tag`, failed at 212. **Run a blinding control against the
consumer that CAN fail, not the one that reports.**

---

# STATE

<!-- VERSION BLOCK: emitted by session_versions.py --handoff. Never hand-typed. -->
Fresh-clone verified at **`fe1f2b5`**. Census **40,683**.
Bible **v8.122.1** · `BookComponentStandard` **v01.12.1** · Maker **v2.45.4** ·
`marks/` **41** · `icons/` **49** incl. LICENSE.
`ZUMO_Syllabus_WORKING.md` **v1.2**.

Instruments: `book_gates` **v1.57** · `lesson_inventory` **v1.3.4** ·
`gen_component` **v1.6.1** · `pill_sweep` **v1.1** · `gate_payload_match` **v1.7** ·
`build_family_map` **v1.4.0** · `callout_id` **v1.0** · `build_mark_index` **v1.1.0** · `gen_bonus_banner` **v1.4.1** ·
`gen_part_banners` **v1.2** · `session_versions` **v1.22.0** · `fit_raster_svg` **v1.2** ·
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
`family_tag` **v1.1** ·
`mark_wire` **v1.0.2** ·
`glyph_scan` **v1.1** ·
`title_feed` **v1.0** ·
`timer.html` **v1.3.2** ·
`going_deeper` **v01.6.1**.

Lessons: L01 v03.24.0 · L02 v03.17.0 · L03 v03.36.1 · L04 v04.24.0 · L05 v04.24.0 · L06 v04.28.0 · L07 v04.27.0 · L08 v04.26.0 · L09 v05.21.0 · L10 v02.22.0 · L11 v02.23.0 · L12 v01.26.0 · L13 v02.23.0 · L14 v02.28.0 · L15 v02.24.0 · L16 v02.17.0.

**62/62 gates.** `lesson_inventory --anomalies` silent · family map **1069/1069** ·
`family_tag` **1069 correct, 0 drifted, 0 unnamed** · `callout_id --audit` **1069, 0 problems** ·
**census 40,683 == `wc -l`** (gate 62 — pre-S130 figures run high by the LESSON COUNT, see §12.6) ·
`regex_audit` **1 lead** (known `entity_sweep.py:70`) · `build_css --check` current at 604 rules ·
`color_index --check` clean · `image_audit --check` current at 14 of 141 ·
`gate_payload_match` PASS · `site_parity` **PARITY**.

---

# S130 WORK — SEE `LIVE_ZUMO_TEXTBOOK.md` FOR THE FULL ACCOUNT

**One Bible entry (v8.122). Sixteen lessons, five instruments, one new tool, one new gate,
one new preserved layer, one tier deleted.**

- **884 marks applied.** All verified to LEAD their own label. §21 coverage **250 → 1,134**.
- **`callout_id.py` v1.0** — `data-callout="L.n"` on all 1,069 callouts, §20.2's form.
  **Authored, never recomputed.** Stripping it back out returns all 16 files byte-identical.
- **`lesson_inventory` emits `callout_id`** — the stable identity the suite never had.
  (Version deliberately not restated here: a real version in prose is taken as the LAST match
  by `_versions_in()`, which is push rule 11. Read it from the version block above.)
- **`ZUMO_FAMILY_PINS.md`** — 212 blocks, generated ONCE from the verified state.
  **PRESERVED LAYER. Never regenerate it from `data-family`.**
- **The GLYPH tier is DELETED**, including for the rump of 4 whose families have no §7 row.
- **Gate 60** pins the table by **md5, not row count** — a regenerated pin has the same keys.

---

# S131 QUEUE

## Ruled but not done — carried from S129
- **Bible §8's LOCKED 11-type callout table becomes a POINTER to `BookComponentStandard` §7.**
- **§21's coverage constant and `build_family_map`'s frozen total are ONE ruling** (DJ: *"probably"*).
  §21's constant HAS now moved (250 → 1,134); the family-map total is still a hand-held literal.

## Opened S130, unruled
- **DONE S130:** `glyph_scan` **v1.1** — post-run line generalised; gate 60's own glyph read
  accepted by name after a behavioural proof (0 of 1,069 resolutions change when blanked).
- **Should `ZUMO_FAMILY_PINS.md` carry a version home?** Same shape as the carried
  `css/semantic.css` question, now with a gate depending on it.
- **The 3 NEW `glyph_scan` leads are unchanged and still read** — `book_gates:843` (☐, a BRAIN
  CHECK dependency to record), `engine.py:103` (**one character spelled two ways in one
  expression, and the `or` branch is unreachable — dead code, verified S130**),
  `lesson_inventory:688` (innocent; note its line number drifted 660 → 688).
- **`glyph_scan`'s U+2100 floor is unchanged** — an ASCII pseudo-glyph is still invisible to it.

## Carried, unchanged
- **Nav pill count ranges 10 to 19**; §6.5's "12-14" rule is obsolete — **rewrite before touching a lesson.**
- **Quick-reference anchors exist in five lessons only** (L02-L06).
- **Timers appear in L02, L03, L04 only — S69 burned a session on a false finding here, READ
  before counting.**
- **Callout border-width probe returned zero shapes** — it looked for inline `border-left`, which
  §27 deleted; it has to read the stylesheet now.
- **The colour ledger — 16 items, `#f8f9fa` (641 instances) the largest unreported surface**, plus
  L03's `div-c-922b21` title red.
- The glossary arc — **106 distinct terms, 184 KEY TERM blocks, 55 anchored.** Note **159 of the
  184 are now PINNED**, so the glossary arc and the pin now overlap: anchoring a term does NOT
  give it a content-resolvable family.
- **`index.html` carries no version home** · **`BONUS_MARK`/`MARK` indexed nowhere** ·
  **L01's BC02 does not carry L01's objectives** (legacy, S119) · **S116's past-tense question:
  RETIRE IT** · **L14's score formula is `<code>` and is not code** ·
  **the two `book_gates` versions S115 shipped carry NO changelog line** ·
  **four `data-reveal="mechanism"` blocks are not on §20.1's whitelist** ·
  **The mark roster now RECONCILES and is gated (61).** The seven absent marks are §7.2's SYSTEMS group, which §7.2's own Grounds table already rules *"in scope: no"* — NOT a debt. Held by name; the hold expires if any one lands. **Do not re-open this.**

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
   DELETING `ZUMO_S130_HANDOFF.md` — a GitHub Desktop checkbox.
8. **THE NUMBER IN THE FILENAME IS THE SESSION THAT READS IT.**
9. **Never write a real version number as an arrow pair in prose.** `_versions_in()` takes the
   LAST match. Write *"reaches vNEW (from vOLD)"*.
10. **A document cannot name the commit that contains it.**
11. **AN EDIT TO A FILE WITH REPEATED LANDMARK LINES TARGETS AN INDEX AND ASSERTS IT** (§6.12c).
    The Bible's version anchor is on line 17 AND in the changelog.
12. **AN EDIT THAT CHANGES LINE COUNT INVALIDATES EVERY LINE-KEYED TARGET BELOW IT.** Go
    DESCENDING per file.
13. **A SNAPSHOT TAKEN BEFORE THE WORK IS NOT A SNAPSHOT OF THE WORK.** Re-snapshot after every
    landed batch.
14. **A CONTROL THAT DEPENDS ON THE STATE OF WHAT IT AUDITS IS NOT A CONTROL.**
15. **NEW, S130: A CONTROL RUN AGAINST AN UNTRACKED FILE HAS NO RESTORE PATH.** `git checkout`
    on an untracked file does nothing and says nothing. Snapshot it like any lesson.
16. **NEW, S130: A LIBRARY MAY NOT EXIT.** A module-level `SystemExit` in anything the gate suite
    imports kills the run MID-SUITE and can still exit 0. Report absent input through the GATE.
17. **NEW, S130: RUN A BLINDING CONTROL AGAINST THE CONSUMER THAT CAN FAIL.** A tier's death is
    measured on the AUDITOR, not on the generator that reads the attribute first.
18. **NEW, S130: A DERIVED KEY IS NOT AN IDENTITY.** Three failed at S130 (87/212, 199/212,
    14/193). If a record must survive an edit, the key is AUTHORED.
19. **A GATE THAT PINS A SPELLING CERTIFIES WHATEVER IT WAS GIVEN. PIN THE PROPERTY.**
20. **A HOLD THAT IS ALSO SATISFIED BY AN ACCIDENT IS NOT A HOLD.**
