# ZUMO — S135 HANDOFF (written at S134 close · paste at top of Session 135)

## Session open ritual (do this without being asked)
1. **`git ls-remote https://github.com/Weymuth/zumo.git HEAD` FIRST.** A stale answer is
   timing, not caching — **retry a minute later before concluding a push failed** (§12.4).
2. Read `LIVE_ZUMO_TEXTBOOK.md` — verify date / status / versions.
3. **Do NOT grep the Bible version.** `session_versions.bible_consistency()` parses it.
4. Run the full suite and **READ THE EXIT CODE, NOT THE LAST LINE**. Plus
   **`callout_id.py --selftest` then `--audit`**, and **`keyterm_prefix.py --audit`**.
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

**19 images outstanding of 146.** Unmoved this session — S134 was markup, not art. The four
briefed §1 hook GRAPHICs and `IMAGE 4.5` are still in DJ's hands and are the only thing
between the book and 14 of 146.

---

# THE ONE THING TO CARRY OUT OF S134

**THE SHAPE THAT LOOKS LIKE DRIFT MAY BE THE SHAPE THAT IS RIGHT, AND ONLY THE WHOLE
POPULATION CAN SAY WHICH.**

S133 handed this session 22 body KEY TERM blocks in three unruled shapes, and the obvious
reading — the one this session opened with and put to DJ — was that a literal `KEY TERM:`
prefix is redundant with the `key` mark. **The measurement said the exact opposite.** Across
all 1,119 live callouts: NOTE 113/133, CHECKPOINT 102/112, TIP 79/85, DO THIS NOW 55/58,
WARNING 67/80, LEARN 38/47, four families at 100%. **KEY TERM stood at 13 of 238 — and those
13 were precisely the blocks about to be stripped.** One pass from making the only
self-unnaming family in the book unanimous in the wrong direction.

**DJ reversed it on the specimens, not on the argument**, and the second half of his ruling
is the part a count could not have produced: the prefix goes in the BODY and stays out of the
GLOSSARY, because a section banner already saying *Glossary* plus 151 repetitions pushes the
term — the thing a reader scans a glossary FOR — off the left edge of every line.

**AND A SECOND, FROM MY OWN GATE: A COVERAGE COUNT MEASURES BLOCKS SCANNED, NOT BLOCKS
ASSERTED.** Gate 68's first draft passed its own control run: adding a fifth id to `HELD`
excepted a real conformant block and every arm stayed green, because the coverage arm counts
what it looked at. **A gate that carries exceptions owes a HOLD ARM** — the set pinned by
NAME, and each held block asserted to still genuinely need holding, so a hold that has quietly
become unnecessary expires loudly instead of sitting there certified. That is rule 20 arriving
inside the gate written to enforce the ruling.

---

# STATE

<!-- VERSION BLOCK: emitted by session_versions.py --handoff. Never hand-typed. -->
Fresh-clone verified at **`ab8a6ad`**. Census **40,450**.
Bible **v8.127.1** · `BookComponentStandard` **v01.13.0** · Maker **v2.45.4** ·
`marks/` **41** · `icons/` **49** incl. LICENSE.
`ZUMO_Syllabus_WORKING.md` **v1.2**.

Instruments: `book_gates` **v1.63** · `lesson_inventory` **v1.3.5** ·
`gen_component` **v1.6.1** · `pill_sweep` **v1.1** · `gate_payload_match` **v1.7** ·
`build_family_map` **v1.6.0** · `callout_id` **v1.0** · `keyterm_prefix` **v1.0.1** · `build_mark_index` **v1.1.0** · `gen_bonus_banner` **v1.4.1** ·
`gen_part_banners` **v1.2** · `session_versions` **v1.24.0** · `fit_raster_svg` **v1.2** ·
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

Lessons: L01 v03.28.0 · L02 v03.21.0 · L03 v03.40.0 · L04 v04.28.0 · L05 v04.28.0 · L06 v04.31.0 · L07 v04.31.0 · L08 v04.30.0 · L09 v05.26.0 · L10 v02.27.0 · L11 v02.28.0 · L12 v01.31.0 · L13 v02.28.0 · L14 v02.33.0 · L15 v02.30.0 · L16 v02.22.0.

**68/68 gates.** `lesson_inventory --anomalies` silent · family map **1119/1119** ·
`family_tag` **1119 correct, 0 drifted, 0 unnamed** · `callout_id --audit` **1119, 0 problems** ·
`keyterm_prefix --audit` **238 = 151 glossary + 4 held + 83 canonical + 0 to convert** ·
`regex_audit` **1 lead** (known `entity_sweep.py:70`) · `build_css --check` current at 574 rules ·
`color_index --check` clean · **`image_audit --check` current at 19 of 146** ·
`gate_payload_match` PASS · `strip_inline --verify` **0 dead class names** ·
**the pin is 55 rows** (was 125).

---

# WHAT S134 DID

**THE BODY KEY TERM NAMES ITS FAMILY; THE GLOSSARY ENTRY DOES NOT (§24.14d, gate 68).**
83 blocks across 13 lessons take `KEY TERM: <strong>Term</strong>` with the definition on the
next line: 65 canon gained the prefix, L04's five `Key Term:` took the caps spelling, L14/L16's
five gained the `<strong>`, L10's five plain terms gained both, and L15's three inline `<b>`
heads became the head div every other block already had. The glossary's 151 are **untouched** —
they were already exactly the word and the definition.

**THE PREFIX SITS OUTSIDE THE `<strong>`, AND IT IS STRUCTURAL.** 19 body head anchors sit there — 18 spelled
`id="term-*"` and one, L03 `3.44`, spelled `id="glossary-trim"` — as the targets of the ruled body→glossary link direction §27.14 enforces,
and that span is what the end-of-book glossary harvest extracts as the term.

**THE PIN FELL 125 → 55 AND THE GATE RULED IT, NOT THE SESSION.** Writing the family into the
markup means `canon_of` names 70 previously-unnameable blocks from CONTENT, and gate 62's
coverage arm reported the holds expired without being told to — S132's behaviour, rule 20 for
the second time. Retired **by the property**, the gate's own `_need` derivation, never a hand
list. Reconciles: 83 converted, less 13 already self-naming and therefore never pinned, = 70.
**The coupling is real and recorded:** those 70 now depend on the prefix staying, so removing
one fires §24.14a, §24.14c and §24.14d together — three gates agreeing, not three failing.

**THE LOCATOR IS THE AUTHORED ATTRIBUTE, NEVER A CLASS NAME.** The converter's first draft
matched the head by its style declarations, which exist only in the EXPANDED source — the file
carries `class="div-fs-105em"`. Keying on that class would have been worse than a bug: S133's
rule 25 means the `-N` name could be handed to another rule by an unrelated edit and the tool
would go silently blind. It walks out from `data-mark` instead, which reads the same for a
`<div>` head and for L15's inline `<b>`.

**AN INLINE HEAD BECOMING ITS OWN LINE TOOK THE PROSE WITH IT.** L15's three definitions were
lowercase because they were grammatically continuing `<b>KEY TERM — Term:</b>`. The converter's
span extends past the head to capitalise, asserting both that a letter follows and that it was
lower case. **This is the only prose S134 touched.**

**§27.11 MOVED BY DIGEST ONLY.** Rules and declarations UNCHANGED at 574/2,033 — zero born,
died or altered, diffed by selector. The entire sheet delta is FOUR lines: the header count and
`.div-fs-105em` ×792 → ×795, which is L15's three new heads. **Acceptance test was the RESOLVED
STYLING, not the rule count: all 22,142 pre-existing resolved declaration strings byte-identical
across the restore/regenerate/apply cycle in all sixteen lessons.** §27.15b could not fire —
nothing left a class, so no survivor could be renamed.

---

# S135 QUEUE

## Opened S134, unruled
- **L03 `3.44` CARRIES `id="glossary-trim"` ON A BODY BLOCK.** Every other term anchor in
  the book is spelled `term-*`; this one is glossary-prefixed and sits in the BODY. 169 term
  anchors book-wide, 18 body `term-*` plus this one. Found by the S134 triple-check, which is
  also where a wrong count in the v8.127 entry surfaced. Rename or rule.
- **THE FOUR HELD BODY BLOCKS ARE A FAMILY QUESTION, NOT A SHAPE QUESTION.** `3.31` is a
  provenance question, `3.101` an operator announcement, `6.24` a formula box, `14.28` a
  procedural list. None is a term followed by a definition. **Two wear another family's canon
  ground** — `3.31` on `#d1ecf1`, WHAT YOU SHOULD SEE's; `3.101` on `#e3f2fd`/`#2196f3`,
  §18.4's type-explainer. DJ held constrain explicitly at S134. The question is whether these
  belong in KEY TERM at all.
- **THE HEAD TEXT COLOUR IS 16 BLOCKS IN CLEAN STRATA.** `color: #6a1b9a` on L04 5/5, L09 6/6,
  L10 5/5, and **0 of 59 elsewhere**. It cuts ACROSS the shape classes — 6 of the 16 were
  already canon — so it is its own question, adjacent to the parked KEY TERM ground question
  below and NOT resolved by §24.14d.

## Carried from S133, still unruled
- **KEY TERM paint is five grounds.** 238 blocks: 151 glossary uniform purple; the 87 body
  callouts run purple ×49, pink ×33, near-white ×3, teal ×1, pale blue ×1 — STRATA, not scatter.
  **DJ parked this deliberately.** The question when it reopens: one paint for all 238, or two
  on purpose. **Note S134 changed the answer's shape** — the *taught here / looked up here*
  distinction now lives in the prefix, so paint no longer has to carry it alone.
- **`BookComponentStandard` §7.4 carries a stale number** — states the harvest problem as
  *"184 blocks where the glossary is 151"*. Measured now: **238**. Make it a derivation.
- **L16 keeps numbered `1.x` subsections under §1.** DJ ruled it intentional. Do not re-open.

## Ruled but not done
- **§6.5's nav-pill rule still says 12–14 where the live range is 10 to 19.** Carried since S129.
- **§21's coverage constant and `build_family_map`'s frozen total are ONE ruling.**
- **L07 `[IMAGE 7.3]`** landed by a GRAPHIC across the two number spaces (§10), UNRULED.
- **§24.14a and §24.14b still have NO section body** — enforced by gates 59 and 64 whose only
  prose home is a changelog entry, and **`§24.14b` names TWO different rules** across the S128
  and S132 entries. **§24.14d now HAS a body (S134); a and b remain the debt.** Next free
  letter is §24.14e.
- **The §1-figure and §2-objective rules got real sections at v8.126** — that debt is closed.

## Ready to go — the art is briefed and in DJ's hands
- **Four §1 hook GRAPHICs** — `GRAPHIC 11.5` battery lies · `12.4` the turn that never happened ·
  `13.3` the line's three jobs · `15.4` only the present. **Numbering is by CREATION, not
  document order**, so these renumber nothing.
- **`IMAGE 4.5`** — the Zumo underside sensor row. **Photograph, not a drawing** (§17.3).
- Each needs its `[TAG]` swapped, `svg_layout_audit`, `fit_raster_svg`, `image_audit --write`,
  and `site_parity` after the push.

## Carried, unchanged
- Should `ZUMO_FAMILY_PINS.md` carry a version home? · **`css/semantic.css` carries none either.**
- The 3 `glyph_scan` leads · `glyph_scan`'s U+2100 floor · quick-reference anchors in five
  lessons only (L02–L06) · **timers appear in L02/L03/L04 only — S69 burned a session on a
  false finding here, READ before counting** · the callout border-width probe · the colour
  ledger, 16 items · `index.html` carries no version home · `BONUS_MARK`/`MARK` indexed nowhere ·
  **L01's BC02 does not carry L01's objectives (legacy, ruled S119)** · S116's past-tense
  question: RETIRE IT · L14's score formula is `<code>` and is not code · four
  `data-reveal="mechanism"` blocks are not on §20.1's whitelist · **the mark roster RECONCILES
  and is gated (61). Do not re-open.** · **`build_css` is NOT idempotent on this tree** —
  `.ul-ls-none-2`/`-3` alternate across runs; §27.13 assumes one fixed point, there are two.

## Learner mode & book content (untouched for many sessions)
L03_C05 Variable Speed · L03 C01/C05/C06 reference a `finished` payload that does not exist for
L03 (staged in `ZUMO_L03_TEMPLATES.md`) · whole-template starters L08/L09/L10 · Maker batch
(bulk DL · `?lesson=N` gate · C## labels) · L01 VS Code multi-root step · challenge card Pass B ·
**note `ZUMO_TDP_Template_v3.md` v3.1 IS live with A5 Lab Log.**

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
15. **A CONTROL RUN AGAINST AN UNTRACKED FILE HAS NO RESTORE PATH** — and `git checkout --`
    reverts to HEAD, so on uncommitted work it DELETES rather than restores. Snapshot yourself.
16. **A LIBRARY MAY NOT EXIT.**
17. **RUN A BLINDING CONTROL AGAINST THE CONSUMER THAT CAN FAIL.**
18. **A DERIVED KEY IS NOT AN IDENTITY.**
19. **A GATE THAT PINS A SPELLING CERTIFIES WHATEVER IT WAS GIVEN. PIN THE PROPERTY.**
20. **A HOLD THAT IS ALSO SATISFIED BY AN ACCIDENT IS NOT A HOLD.**
21. **SNAPSHOT THE STATE YOU ARE IN, NOT THE STATE YOU ARE LEAVING.**
22. **A GENERATED ARTEFACT PRINTING `DIFFERS` IS A LEAD, NOT AN INSTRUCTION.**
23. **A CONTROL THAT CANNOT TELL A LOST WORD FROM A LOST SPACE IS NOT A CONTROL.**
24. **THE ACCEPTANCE TEST FOR A CSS REGENERATION IS THE RESOLVED STYLING, NOT THE RULE COUNT.**
25. **A GENERATED CLASS NAME IS NOT A HANDLE.** Its `-N` suffix is assigned by usage RANK, so
    adding uses to one of a pair **swaps them**. A construct needing a stable name gets an
    **attribute** and a rule in `css/semantic.css`. **S134 corollary: this applies to READING
    too** — a tool that LOCATES an element by a generated class name goes silently blind the
    day that name is reassigned. Locate by an authored attribute.
26. **MEASURE THE PROPERTY THE RULING NAMES, NOT A PROXY FOR IT.** Read the specimens before
    any count leaves the sandbox.
27. **NEW, S134: A COVERAGE COUNT MEASURES BLOCKS SCANNED, NOT BLOCKS ASSERTED.** A gate that
    carries exceptions owes a HOLD ARM: pin the exception set by NAME, and assert each held
    item still genuinely needs holding. Otherwise adding an exception silently un-gates a real
    block while every arm stays green — which gate 68's own first draft did.
28. **NEW, S134: A STRUCTURAL CHANGE THAT ENDS A SENTENCE EARLY OWES THE SENTENCE A LOOK.**
    Lifting an inline head onto its own line left three definitions opening in lower case.
    No gate can see that; only reading the rendered specimen can.
