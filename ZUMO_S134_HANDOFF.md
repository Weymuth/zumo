# ZUMO — S134 HANDOFF (written at S133 close · paste at top of Session 134)

## Session open ritual (do this without being asked)
1. **`git ls-remote https://github.com/Weymuth/zumo.git HEAD` FIRST.** A stale answer is
   timing, not caching — **retry a minute later before concluding a push failed** (§12.4).
2. Read `LIVE_ZUMO_TEXTBOOK.md` — verify date / status / versions.
3. **Do NOT grep the Bible version.** `session_versions.bible_consistency()` parses it.
4. Run the full suite and **READ THE EXIT CODE, NOT THE LAST LINE**. Plus
   **`callout_id.py --selftest` then `--audit`**.
5. **`--anomalies` BELONGS TO `lesson_inventory`, NOT `session_versions`.**
6. `pip install cairosvg --break-system-packages`. **Needed every session.**
7. **NEVER run `build_css.py --help` or `session_versions.py --help`.** Read the docstring.
8. **Do not hand-type a version, and do not hand-type a COUNT.**
9. **`gate_payload_match.py` needs `newproject.html` FIRST, then the full lesson glob.**
10. **A CLONE IS NOT THE SITE.** Run `site_parity.py` after any push.
11. **VERIFY THE PUSH BY FRESH CLONE AND MD5 — AND DIFF THE STAGE AGAINST THE CLONE.**
12. **`css/semantic.css` AND `ZUMO_FAMILY_PINS.md` ARE HAND-AUTHORED PRESERVED LAYERS.**

---

# SEPTEMBER 8 IS ABOUT FOUR WEEKS OUT

**19 images outstanding of 146**, up from 14 of 141. The five new ones are §1 hook figures and
that rise is the point: they were always missing and nothing could say so.

---

# THE ONE THING TO CARRY OUT OF S133

**A GENERATED NAME IS NOT A HANDLE. DO NOT GRAB ONE.**

DJ asked for something three bytes wide — an objective list should not draw a bullet on top of
its checkbox. Assigning the existing class `ul-ls-none-3` to the four offending lists silently
re-resolved **twelve lessons nobody touched**: L03's lists went `padding-left: 0 → 5px`,
L06–L13 went `5px → 0`. Reverted, re-authored as **inline**, and it happened **again** —
because `.ul-ls-none` and `.ul-ls-none-3` are distinguished only by a rank-assigned `-N`
suffix, so adding uses to either **swaps them**. §27.15b, twice, in one hour.

**It was caught both times by comparing RESOLVED STYLING against a snapshot. No gate saw it,
and no gate can.** §27.13 asserts the sheet regenerates from the lessons; a swap regenerates
perfectly.

The fix DJ ruled is `css/semantic.css`, and it worked first time with **zero** collateral —
all 22,142 resolved declaration strings byte-identical. **The selector is an ATTRIBUTE, not a
class** (`ul[data-objectives]`), which is S128's lesson: a semantic class going INTO markup
runs the generator backwards, and `class="mark"` was re-emitted as `.img-fs-0` for exactly
that reason.

**The general rule: if a construct needs a name that means something, the name lives in the
preserved layer and the markup carries an attribute. Never reach for a name build_css emitted.**

**AND A SECOND, RECORDED NOT FIXED: `build_css` IS NOT IDEMPOTENT ON THIS TREE.** The same
sixteen lesson files produce two different stylesheets depending on which sheet you start
from — `.ul-ls-none-2` and `.ul-ls-none-3` alternate across runs. Settled on one fixed point.
§27.13 assumes there is only one. **There are two.**

---

# STATE

<!-- VERSION BLOCK: emitted by session_versions.py --handoff. Never hand-typed. -->
Fresh-clone verified at **`77531bb`**. Census **40,450**.
Bible **v8.126** · `BookComponentStandard` **v01.13.0** · Maker **v2.45.4** ·
`marks/` **41** · `icons/` **49** incl. LICENSE.
`ZUMO_Syllabus_WORKING.md` **v1.2**.

Instruments: `book_gates` **v1.62** · `lesson_inventory` **v1.3.5** ·
`gen_component` **v1.6.1** · `pill_sweep` **v1.1** · `gate_payload_match` **v1.7** ·
`build_family_map` **v1.6.0** · `callout_id` **v1.0** · `build_mark_index` **v1.1.0** · `gen_bonus_banner` **v1.4.1** ·
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
`family_tag` **v1.2.1** ·
`glossary_convert` **v1.0** ·
`mark_wire` **v1.0.2** ·
`glyph_scan` **v1.1** ·
`title_feed` **v1.0** ·
`timer.html` **v1.3.2** ·
`going_deeper` **v01.6.1**.

Lessons: L01 v03.27.0 · L02 v03.20.0 · L03 v03.39.0 · L04 v04.27.0 · L05 v04.27.0 · L06 v04.30.0 · L07 v04.30.0 · L08 v04.29.0 · L09 v05.25.0 · L10 v02.26.0 · L11 v02.28.0 · L12 v01.31.0 · L13 v02.28.0 · L14 v02.32.0 · L15 v02.29.0 · L16 v02.21.0.

**67/67 gates.** `lesson_inventory --anomalies` silent · family map **1119/1119** ·
`family_tag` **1119 correct, 0 drifted, 0 unnamed** · `callout_id --audit` **1119, 0 problems** ·
`regex_audit` **1 lead** (known `entity_sweep.py:70`) · `build_css --check` current at 574 rules ·
`color_index --check` clean · **`image_audit --check` current at 19 of 146** ·
`gate_payload_match` PASS · `strip_inline --verify` **0 dead class names** · the pin is **125 rows**.

---

# WHAT S133 DID

**THE EM DASH LEAVES THE BODY KEY TERMS — 24 blocks, not the 41 first reported.** S132 made all
151 glossary entries the canon term card, *no em dash*. The body half of the same family was
never touched. **The first count was wrong because it measured a PROXY** — blocks missing
`<strong>` — which conflated four different shapes. Measured against the separator itself:
**41 already correct, 24 em-dash, 10 carrying a literal `KEY TERM:` prefix, 9 plain, 3
outliers.** The 24 converted (L02×11, L03×7, L09×6), L03's seven `<span id="term-*">` becoming
`<strong id="term-*">` so the anchors survived. **The other 22 shapes are UNRULED and parked.**

**EVERY BACK-TO-TOP LINK IN THE BOOK IS ONE SPELLING.** 237 links, `<p class="p-ta-right">`,
where there had been five wrappers and **L15 and L16's 28 links rendered flush LEFT** — no
`text-align` at all, verified three ways: markup census, DOM ancestor walk, and OCR of a render
(x=890 on L14 against x=122 on L15). Three rules died carrying two declarations each and
**§27.15b did not fire, because all three were used by back-to-top links and nothing else** —
checked before deletion.

**§1 HAS A RULE AND A GATE (66).** Eight of sixteen lessons opened the hook with a real figure,
three had a placeholder and **five had nothing at all** — invisible to `image_audit`, correctly,
because nobody had ever declared a figure was wanted. Five placeholders authored; the gate
accepts a placeholder by design, because a gate demanding a landed asset is a to-do list wearing
a gate. **Its predicate is the authored name `L##_IMAGE_`/`L##_GRAPHIC_`, not the directory** —
the first draft keyed on the path, counted every decorative mark as a figure and reported a
false **16 of 16 with six lessons still empty**.

**§2 HAS A RULE AND A GATE (67).** Objectives exist, each is a box, and the list does not also
draw a bullet. L01 and L15 carried **13 objectives with no box at all**; v8.108 had recorded
that as an observation with no gate. The lead-in normalised to the ten-lesson majority
(15 of 16 now carry the comma; L16 keeps its own wording by ruling).

**`Learning Objectives` COST A TAXONOMY FIX, AND THE FIX FOUND THREE COPIES OF ONE RULE.**
Renaming L02's `🎯 OBJECTIVES` re-familied it LEARN, because CANON matched a bare prefix and
`LEARNING` starts with `LEARN`. The prefix now must end on a **word boundary** — **measured
inert first: across all 1,119 live labels the result changes for ZERO of them.** The matcher
was written out **three times** (twice in `book_gates`, once in `family_tag`); all three now
import the exported `canon_of()`. The OBJECTIVES rule names the **noun**, not the string start.

---

# S134 QUEUE

## Ready to go — the art is briefed and in DJ's hands
- **Four §1 hook GRAPHICs** — `GRAPHIC 11.5` battery lies · `12.4` the turn that never happened ·
  `13.3` the line's three jobs · `15.4` only the present. Full briefs were delivered at S133 with
  house style, free numbers and a MEASURED FACTS block. **Numbering is by CREATION, not document
  order** (L11 runs 01,04,02,03 down the page), so these renumber nothing.
- **`IMAGE 4.5`** — the Zumo underside sensor row. **Photograph, not a drawing** (§17.3); joins
  the parked photography.
- Each needs its `[TAG]` swapped for the asset, `svg_layout_audit`, `fit_raster_svg`,
  `image_audit --write`, and `site_parity` after the push.

## Opened S133, unruled
- **The other 22 body KEY TERM shapes** — 10 carry a literal `KEY TERM:` prefix the mark already
  says; 9 are plain; **3 L15 outliers use `<b>` on a near-white `#f4f9fc` ground and their
  definitions contain real em dashes in the prose**, so a dash rule would eat punctuation.
- **KEY TERM paint is five grounds.** 238 blocks: 151 glossary uniform purple, but the 87 body
  callouts run purple ×49, pink ×33, near-white ×3, teal ×1, pale blue ×1 — and it is STRATA
  (purple lessons, pink lessons), not scatter. **DJ parked this deliberately at S133.**
  The question when it reopens: one paint for all 238, or two on purpose so a student can tell
  *taught here* from *looked up here*.
- **`BookComponentStandard` §7.4 carries a stale number** — it states the harvest problem as
  *"184 blocks where the glossary is 151"*. Measured now: **238**. The 184 was counted mid-S132
  before the last 54 entries gained `data-family`. A frozen count in canon; make it a derivation.
- **L16 keeps numbered `1.x` subsections under §1** — the only lesson that does. **DJ ruled it
  intentional.** Do not re-open.

## Ruled but not done
- **§6.5's nav-pill rule still says 12–14 where the live range is 10 to 19.** Carried since S129.
- **§21's coverage constant and `build_family_map`'s frozen total are ONE ruling.**
- **L07 `[IMAGE 7.3]`** landed by a GRAPHIC across the two number spaces (§10), UNRULED.
- **§24.14a and §24.14b have NO section body in the Bible** — both are enforced by live gates
  (59 and 64) whose only prose home is a changelog entry, and **`§24.14b` names TWO different
  rules** across the S128 and S132 entries. Next free letter is §24.14d.
- **The §1-figure and §2-objective rules are gates with no Bible section** — the same debt shape,
  created this session. Gates 66 and 67 print `§2.1` and `§2.2` against numbers the Bible has
  never carried.

## Carried, unchanged
- **Should `ZUMO_FAMILY_PINS.md` carry a version home?** · **`css/semantic.css` carries none
  either, and it grew a rule this session.**
- The 3 `glyph_scan` leads · `glyph_scan`'s U+2100 floor · quick-reference anchors in five
  lessons only (L02–L06) · **timers appear in L02/L03/L04 only — S69 burned a session on a false
  finding here, READ before counting** · the callout border-width probe · the colour ledger,
  16 items · `index.html` carries no version home · `BONUS_MARK`/`MARK` indexed nowhere ·
  **L01's BC02 does not carry L01's objectives (legacy, ruled S119)** · S116's past-tense
  question: RETIRE IT · L14's score formula is `<code>` and is not code · four
  `data-reveal="mechanism"` blocks are not on §20.1's whitelist · **the mark roster RECONCILES
  and is gated (61). Do not re-open.**

## Learner mode & book content (untouched for many sessions)
L03_C05 Variable Speed · L03 C01/C05/C06 reference a `finished` payload that does not exist for
L03 (staged in `ZUMO_L03_TEMPLATES.md`) · whole-template starters L08/L09/L10 · Maker batch
(bulk DL · `?lesson=N` gate · C## labels) · L01 VS Code multi-root step · TDP template v3 —
**note `ZUMO_TDP_Template_v3.md` v3.1 IS live with A5 Lab Log; the Bible's §14.1 names
`ZUMO_TDP_Template.md`, a file that does not exist** · challenge card Pass B.

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
7. **Exactly ONE `ZUMO_SNN_HANDOFF.md` in the root (gate 28).**
8. **THE NUMBER IN THE FILENAME IS THE SESSION THAT READS IT.**
9. **Never write a real version number as an arrow pair in prose.** Write *"reaches vNEW (from vOLD)"*.
10. **A document cannot name the commit that contains it.**
11. **AN EDIT TO A FILE WITH REPEATED LANDMARK LINES TARGETS AN INDEX AND ASSERTS IT** (§6.12c).
12. **AN EDIT THAT CHANGES LINE COUNT INVALIDATES EVERY LINE-KEYED TARGET BELOW IT.** Go DESCENDING.
13. **A SNAPSHOT TAKEN BEFORE THE WORK IS NOT A SNAPSHOT OF THE WORK.**
14. **A CONTROL THAT DEPENDS ON THE STATE OF WHAT IT AUDITS IS NOT A CONTROL.**
15. **A CONTROL RUN AGAINST AN UNTRACKED FILE HAS NO RESTORE PATH.**
16. **A LIBRARY MAY NOT EXIT.**
17. **RUN A BLINDING CONTROL AGAINST THE CONSUMER THAT CAN FAIL.**
18. **A DERIVED KEY IS NOT AN IDENTITY.**
19. **A GATE THAT PINS A SPELLING CERTIFIES WHATEVER IT WAS GIVEN. PIN THE PROPERTY.**
20. **A HOLD THAT IS ALSO SATISFIED BY AN ACCIDENT IS NOT A HOLD.**
21. **SNAPSHOT THE STATE YOU ARE IN, NOT THE STATE YOU ARE LEAVING.**
22. **A GENERATED ARTEFACT PRINTING `DIFFERS` IS A LEAD, NOT AN INSTRUCTION.**
23. **A CONTROL THAT CANNOT TELL A LOST WORD FROM A LOST SPACE IS NOT A CONTROL.**
24. **THE ACCEPTANCE TEST FOR A CSS REGENERATION IS THE RESOLVED STYLING, NOT THE RULE COUNT.**
25. **NEW, S133: A GENERATED CLASS NAME IS NOT A HANDLE.** Its `-N` suffix is assigned by usage
    RANK, so adding uses to one of a pair **swaps them** and silently re-resolves every other
    user in the book. This fires whether the edit is authored as a class **or as inline**.
    A construct that needs a stable name gets an **attribute** and a rule in `css/semantic.css`.
26. **NEW, S133: MEASURE THE PROPERTY THE RULING NAMES, NOT A PROXY FOR IT.** Five wrong counts
    reached DJ this session and every one came from measuring something adjacent — `<strong>`
    presence for *"has a readable term"* (41, truly 24), a path substring for *"is a figure"*
    (a false 16 of 16), a 400-byte window for *"what follows the glossary"*, a regex requiring a
    period for *"has a lead-in"*, `start`+`bytes` for a block whose length is measured in the
    EXPANDED source. **Read the specimens before any count leaves the sandbox.**
