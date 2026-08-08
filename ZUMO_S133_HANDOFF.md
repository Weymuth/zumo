# ZUMO — S133 HANDOFF (written at S132 close · paste at top of Session 133)

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

**14 images outstanding of 141.** Photography still parked. Nothing this session touched it,
and `image_audit --check` stayed current across the whole glossary arc.

---

# THE ONE THING TO CARRY OUT OF S132

**THE HARVEST KEY WAS NEVER THE FAMILY.**

DJ asked for one thing and it was not a markup question: *"I want it to match and I want to be
able to pull a glossary down later."* The obvious reading is that the 151 entries need a family
a harvest can select on — and that reading is wrong by 33 blocks. `data-family="KEY TERM"`
returns **184**: the glossary entries AND the body callouts that teach the same terms, mixed,
with nothing to separate them. **The thing that separates them is WHERE THEY SIT**, and until
this session nothing in the tree could say where anything sat below the §-banner level.

So the ruling DJ actually needed was the one he was not asked about: `lesson_inventory` gains
`region`. The family question — KEY TERM or GLOSSARY — was the visible question and the cheap
one; **a family names CONTENT and a region names LOCATION, and the request was about location
all along.**

**When someone asks for a capability rather than a shape, find the field that answers it before
proposing the shape.** The five schemas had to go regardless. They were not what was blocking
the harvest.

---

# STATE

<!-- VERSION BLOCK: emitted by session_versions.py --handoff. Never hand-typed. -->
Fresh-clone verified at **`3c0566a`**. Census **40,440**.
Bible **v8.124** · `BookComponentStandard` **v01.13.0** · Maker **v2.45.4** ·
`marks/` **41** · `icons/` **49** incl. LICENSE.
`ZUMO_Syllabus_WORKING.md` **v1.2**.

Instruments: `book_gates` **v1.59** · `lesson_inventory` **v1.3.5** ·
`gen_component` **v1.6.1** · `pill_sweep` **v1.1** · `gate_payload_match` **v1.7** ·
`build_family_map` **v1.5.0** · `callout_id` **v1.0** · `build_mark_index` **v1.1.0** · `gen_bonus_banner` **v1.4.1** ·
`gen_part_banners` **v1.2** · `session_versions` **v1.23.0** · `fit_raster_svg` **v1.2** ·
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
`family_tag` **v1.2** ·
`glossary_convert` **v1.0** ·
`mark_wire` **v1.0.2** ·
`glyph_scan` **v1.1** ·
`title_feed` **v1.0** ·
`timer.html` **v1.3.2** ·
`going_deeper` **v01.6.1**.

Lessons: L01 v03.25.0 · L02 v03.18.0 · L03 v03.37.0 · L04 v04.25.0 · L05 v04.25.0 · L06 v04.29.0 · L07 v04.28.0 · L08 v04.27.0 · L09 v05.22.0 · L10 v02.23.0 · L11 v02.24.0 · L12 v01.27.0 · L13 v02.24.0 · L14 v02.29.0 · L15 v02.25.0 · L16 v02.18.0.

**64/64 gates.** `lesson_inventory --anomalies` silent · family map **1123/1123** ·
`family_tag` **1123 correct, 0 drifted, 0 unnamed** · `callout_id --audit` **1123, 0 problems** ·
census **40,440 == `wc -l`** · `regex_audit` **1 lead** (known `entity_sweep.py:70`) ·
`build_css --check` current at 598 rules · `color_index --check` clean ·
**`image_audit --check` current at 14 of 141** · `gate_payload_match` PASS ·
`strip_inline --verify` **0 dead class names** · the pin is **125 rows**.

---

# WHAT S132 DID

**THE GLOSSARY IS ONE COMPONENT.** All **151** entries in all sixteen lessons are the canon
term card (`BookComponentStandard` §7.4, new). Five schemas retired: 97 KEY TERM callouts in
four sub-shapes, 14 bare `div-9b59b6` (L04), 15 `<dl>/<dt>` (L13/L14), 25 table rows (L11/L15).
**54 of them had carried no `data-family` and no `data-callout`** — a third of the book's
vocabulary that no gate could fail on.

**§24.14b NEW — THE STRUCTURE TIER.** A callout inside the glossary region is a KEY TERM,
**97 of 97, zero exceptions**. A section id is STRUCTURE, not decoration: colour died at S112
and the glyph at S130 because both were presentation that could be changed without the family
changing. A banner id cannot be repainted, and moving a block out of the glossary is a MOVE,
after which it SHOULD stop being a KEY TERM.

**THE PIN FELL 212 → 125 AND THE GATE RULED IT.** Taught the tier, gate 62's coverage arm
reported 87 holds EXPIRED without being told to. Retired by property, never by a list of ids.
Converting with no tier would have taken the pin to **266** — a 141-row swing.

**GATE 64 NEW**, written in the same pass. It asserts the PREDICATE, not the tier's output —
asking the tier whether it returns KEY TERM is circular — by BLINDING the tier and failing if
any other tier resolves a glossary-region block to something else. Arm 2 pins the banner roster.

**§6.9's glossary format and §8's 11-type callout table are now POINTERS** to
`BookComponentStandard` §7.4 and §7. §8's table named 11 of 30 families and its opening clause
(*"All callouts use inline `style=` only"*) had been retired by §27.

---

# S133 QUEUE

## Opened S132, unruled — the glossary arc's own remainder
- **25 body KEY TERM callouts have NO same-lesson glossary entry.** 56 of 81 do. Whether the 25
  get authored entries is unruled, and it is the last content question in this arc.
- **L11, L12 and L13 carry ZERO body KEY TERM callouts** — their glossaries exist and their
  bodies never mark a term. Ruling the 25 above without noticing this rules on the wrong shape.
- **THE LINK ITSELF IS NOT WIRED.** The direction is ruled (body term → glossary entry, S128
  and S131 agreeing) and all 151 entries now carry an `id` so a link HAS a target — but not one
  body callout links to one yet. **The ids are affordance, not use**, and `45 of 55` pre-existing
  `term-*` anchors were already targeted by nothing. §27.14 is structurally blind to this: it
  asserts links RESOLVE, never that ids are REACHED.
- **A BOOK-WIDE GLOSSARY IS NOW POSSIBLE AND IS NOT DESIGNED.** The harvest key is the region.
  S128's ruling governs the content: ADDITIVE, every definition stays in place, one entry per
  lesson-term pair disambiguated by topic (*Dead Reckoning (gyro)* vs *(encoders)*).
  **Six ids repeat across pages** — legal, since a link names the page — and those six are
  exactly the terms a book-wide glossary has to disambiguate. **READ S128 BEFORE DESIGNING IT.**

## Ruled but not done
- **§6.5's nav-pill rule still says 12–14 where the live range is 10 to 19.** Carried since
  S129 with *"rewrite before touching a lesson"* — sixteen lessons were touched this session and
  it is still unwritten. It does not block anything; it is simply false in the canon right now.
- **§21's coverage constant and `build_family_map`'s frozen total are ONE ruling** (DJ:
  *"probably"*). Both moved again this session, by hand, in two places.
- **L07 `[IMAGE 7.3]`** is landed by `L07_GRAPHIC_7-15_platformio_file_tree.svg` — a GRAPHIC
  standing in for an IMAGE across the two number spaces (§10), no prose declaring it, where
  L10's equivalent says so. Held by name in gate 63's `REUSE`, marked UNRULED.

## Carried, unchanged
- **Should `ZUMO_FAMILY_PINS.md` carry a version home?** Sharper now: the file CHANGED this
  session, and its only identity is a gate constant.
- **The 3 `glyph_scan` leads** — `book_gates:843` (☐, a BRAIN CHECK dependency to record),
  `engine.py:103` (dead code, verified S130), `lesson_inventory:688` (innocent).
- **`glyph_scan`'s U+2100 floor** — an ASCII pseudo-glyph is still invisible to it.
- **Quick-reference anchors exist in five lessons only** (L02-L06).
- **Timers appear in L02, L03, L04 only — S69 burned a session on a false finding here, READ
  before counting.**
- **Callout border-width probe returned zero shapes** — it looked for inline `border-left`,
  which §27 deleted; it has to read the stylesheet now.
- **The colour ledger — 16 items, `#f8f9fa` the largest unreported surface**, plus L03's
  `div-c-922b21` title red. **Heritage Blue cannot be piloted on one lesson.**
- **`index.html` carries no version home** · **`BONUS_MARK`/`MARK` indexed nowhere** ·
  **L01's BC02 does not carry L01's objectives** (legacy, S119) · **S116's past-tense question:
  RETIRE IT** · **L14's score formula is `<code>` and is not code** ·
  **the two `book_gates` versions S115 shipped carry NO changelog line** ·
  **four `data-reveal="mechanism"` blocks are not on §20.1's whitelist** ·
  **The mark roster RECONCILES and is gated (61). Do not re-open.**

## Learner mode & book content (untouched for many sessions)
L03_C05 Variable Speed · L03 C01/C05/C06 reference a `finished` payload that does not exist for
L03 (staged in `ZUMO_L03_TEMPLATES.md`) · whole-template starters L08/L09/L10 · Maker batch
(bulk DL · `?lesson=N` gate · C## labels) · L01 VS Code multi-root step · TDP template v3 (A5
Lab Log) · challenge card Pass B (Goal→Logic→Template).

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
   DELETING `ZUMO_S132_HANDOFF.md` — a GitHub Desktop checkbox.
8. **THE NUMBER IN THE FILENAME IS THE SESSION THAT READS IT.**
9. **Never write a real version number as an arrow pair in prose.** `_versions_in()` takes the
   LAST match. Write *"reaches vNEW (from vOLD)"*.
10. **A document cannot name the commit that contains it.**
11. **AN EDIT TO A FILE WITH REPEATED LANDMARK LINES TARGETS AN INDEX AND ASSERTS IT** (§6.12c).
12. **AN EDIT THAT CHANGES LINE COUNT INVALIDATES EVERY LINE-KEYED TARGET BELOW IT.** Go
    DESCENDING per file.
13. **A SNAPSHOT TAKEN BEFORE THE WORK IS NOT A SNAPSHOT OF THE WORK.** Re-snapshot after every
    landed batch.
14. **A CONTROL THAT DEPENDS ON THE STATE OF WHAT IT AUDITS IS NOT A CONTROL.**
15. **A CONTROL RUN AGAINST AN UNTRACKED FILE HAS NO RESTORE PATH.**
16. **A LIBRARY MAY NOT EXIT.**
17. **RUN A BLINDING CONTROL AGAINST THE CONSUMER THAT CAN FAIL.**
18. **A DERIVED KEY IS NOT AN IDENTITY.**
19. **A GATE THAT PINS A SPELLING CERTIFIES WHATEVER IT WAS GIVEN. PIN THE PROPERTY.**
    **S132 hit this before the rule saved it:** the first region probe keyed on the `div-bg-*`
    wrapper, **which L04's glossary banner does not wear**, and returned ZERO regions for L04 —
    clean by omission, which is the worst kind of clean.
20. **A HOLD THAT IS ALSO SATISFIED BY AN ACCIDENT IS NOT A HOLD.**
21. **SNAPSHOT THE STATE YOU ARE IN, NOT THE STATE YOU ARE LEAVING.**
22. **A GENERATED ARTEFACT PRINTING `DIFFERS` IS A LEAD, NOT AN INSTRUCTION.**
23. **NEW, S132: A CONTROL THAT CANNOT TELL A LOST WORD FROM A LOST SPACE IS NOT A CONTROL.**
    The no-text-lost check fired on 8 of 16 glossary regions and every hit was whitespace at a
    tag boundary. Re-run comparing WORDS, it returned 0 of 16. **A control's own normalisation
    is part of the control**, and one that flags 8 false positives will be tuned away by the
    next reader instead of being fixed.
24. **NEW, S132: THE ACCEPTANCE TEST FOR A CSS REGENERATION IS THE RESOLVED STYLING, NOT THE
    RULE COUNT.** Six rules died and **12 SURVIVING spellings changed declarations** —
    `.th-17496a-2` and `-3` swapped grounds outright. The restore → regenerate → apply
    `--include-held` cycle makes that harmless, and the PROOF is that all **22,933** resolved
    declaration strings are byte-identical across the cycle in all sixteen lessons.
