# ZUMO — S136 HANDOFF (written at S135 close · paste at top of Session 136)

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

**16 images outstanding of 146** — down from 19. The three §1 hook GRAPHICs are live.
**`GRAPHIC 15.4` was never produced** and a full brief for it is in the S135 chat, ready to
send. **`IMAGE 4.5` is blocked on DJ**, and on two counts, not one: §14 forbids a drafting
model estimating where a component sits in a photograph, so it needs highlight-box
coordinates; and the lesson's caption asks the windows be **numbered 1–5 left to right**,
which the whole two-act jumper story depends on, where the delivered draft labelled them
Left / Left-Center / Center / Right-Center / Right.

---

# THE ONE THING TO CARRY OUT OF S135

**A FIGURE IS PLANNED BY ITS TAG, AND THE TAG DOES NOT LIVE WHERE THE FIGURE DOES.**

Landing three figures made `image_audit` report **planned 146 → 143 with LANDED UNMOVED at
127**. They had not moved from outstanding to landed — they had left the population. The
tag lives in the lesson's **FIGURES INDEX TABLE**; the body carries only the `<img>`.
**Nothing failed.** The one signal was `--check` printing DIFFERS, which reads as *re-run
me*, and `--write` would have accepted the smaller denominator and printed a smaller
`outstanding` **that looks exactly like progress**. Gate 69 now pins the PLANNED total.

**AND A SECOND, ABOUT MY OWN WORKING COPIES.** Mid-session I reported a gate 69 that did not
exist, quoted its comment block, and said it was already in the repo. It was not. Two
sandbox clones I had been running tools in had drifted — three copies of `book_gates.py`,
three different md5s — and I read the polluted ones instead of re-deriving from a clean
clone. **When two readings disagree, re-clone; do not reconcile.** The push itself was
fine and was re-verified from an untouched clone.

---

# STATE

<!-- VERSION BLOCK: emitted by session_versions.py --handoff. Never hand-typed. -->
Fresh-clone verified at **`b05357e`**. Census **40,455**.
Bible **v8.128** · `BookComponentStandard` **v01.13.0** · Maker **v2.45.4** ·
`marks/` **41** · `icons/` **49** incl. LICENSE.
`ZUMO_Syllabus_WORKING.md` **v1.2**.

Instruments: `book_gates` **v1.64** · `lesson_inventory` **v1.3.5** ·
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

Lessons: L01 v03.28.0 · L02 v03.21.0 · L03 v03.40.0 · L04 v04.28.0 · L05 v04.28.0 · L06 v04.31.0 · L07 v04.31.0 · L08 v04.30.0 · L09 v05.26.0 · L10 v02.27.0 · L11 v02.28.1 · L12 v01.31.1 · L13 v02.28.1 · L14 v02.33.0 · L15 v02.30.0 · L16 v02.22.0.

**69/69 gates.** `lesson_inventory --anomalies` silent · family map **1119/1119** ·
`callout_id --audit` **1119, 0 problems** · `keyterm_prefix --audit` **238 = 151 + 4 + 83 + 0** ·
`regex_audit` **1 lead** (known `entity_sweep.py:70`) · `build_css --check` current at 574 rules ·
**`image_audit --check` current at 16 of 146** · `gate_payload_match` PASS ·
`strip_inline --verify` **0 dead class names** · the pin is **55 rows**.

---

# S136 QUEUE

## THE SPIRAL ARC — RULED, ENUMERATED, DELIBERATELY NOT STARTED
**DJ ruled §18.1's "1–2 prior concepts" a FLOOR, not a ceiling** (*"floor. No ceiling."*),
on the §25.8 precedent. **Do not start this without finishing it** — under a floor ruling a
half-starred book is worse than an unstarred one, and a half-starred book is exactly what
produced DJ's *"the spiral stops at Lesson 11"* reading. It does not stop there: **L13 has
the highest coverage in the book and L11 is second. It never started** — 13 of 171 challenge
units, 8%.

**APPROVED BY DJ, BUILD THESE FIVE FIRST** (they close the five lessons at zero):
- **L04 4.4 Edge Guard → L03** — first time line sensors drive wheels; the card says
  *"motors change everything."*
- **L05 5.1 Detection Counter → L04** — the arrived/left boolean-memory trick, same
  technique as L04's Line Counter, new sensor.
- **L06 6.7 Smooth Acceleration → L03 and L04** — L03's Ramp done properly, now that the
  `for` loop exists (L04 §8A.6). Two sources; legal under the floor.
- **L12 12.2 The Slip Alarm → L06** — the student writes the encoder-vs-gyro comparison.
- **L15 15.2 Filter the Derivative → L04** — *"sensor noise is a rate too."* Chosen over the
  obvious 15.1 → L08 because **L15 §1 already carries a Builds-on pointing at L08**.

**THEN THE 17 SELF-DECLARING CARDS** (their own text names a prior lesson, all unstarred):
2.6→1 · 3.8→2 · 4.4→3 · 4.5→3 · 7.4→6 · 9.1→7 · 9.2→2 · 9.4→6 · 9.6→6,7 · 10.4→6 ·
10.5→5,6,8,9 · 11.1→6 · 11.5→10 · 12.3→6,7,8 · 13.3→6,8,10,11,12 · 14.1→11 · 15.7→8.

**THE SCAN THAT FOUND THOSE 17 IS STRUCTURALLY BLIND TO THE REST.** Only ONE of the five
read-found spirals (4.4) appears in it. **The remaining enumeration is a READ of all 171
cards, not a query.** True population **21 minimum, top end unknown**.

**COST PER STAR:** each is a NEW CALLOUT — `data-family="BUILDS ON"`, `arrow-repeat` mark,
star `img-h-11em`, and an identity **minted by `callout_id.py --apply`, never hand-written**
(a second minter is the third-copy defect, S83). ~21 of them move the family map off 1,119,
move §21's coverage off 1,201, and move the stylesheet. Consider banking the enumeration in
`ZUMO_SPIRAL_MOVE_ASSESSMENT.md` so S137 applies a derived list (§24.13).

## Opened S135, unruled
- **THE FIGURE BLOCK HAS FOUR SPELLINGS.** L11 `div-m-24px0`/`img-ddd`/`div-c-666-2`; L12
  semantic `<figure>`/`<figcaption>`; L13 `div-m-25px0`/`img-br-8px`; L15 `div-m-26px0`/
  `img-cdd9e1` with a bracketed caption. Each lesson's own was matched rather than one
  imposed. **L12's is the best of the four** — `<figure>`/`<figcaption>` is semantic and its
  class is unranked. Whether the book converges on it is a ruling.
- **`svg_layout_audit.py` HAS FOUR MEASURED DEFECTS AND NONE IS FIXED.** (1) the resolution
  arm ignores `preserveAspectRatio="meet"`, so every letterboxed image gets a false *under
  the 2× floor* — **this one already cost DJ a wrong answer about `IMAGE 4.5`**; (2) nested
  `callout-*` groups are compared against their parent, giving false overlaps; (3) an
  `<image>` in `<defs>` used via `<use>` is measured at its definition size, not its
  placement, reporting 0.38× where the truth is 2.39×; (4) it is blind to text-versus-box
  collisions across different baselines, and to an element hidden BEHIND an opaque box —
  which is the one that would have caught a defect I authored.

## Carried from S133/S134, still unruled
- **KEY TERM paint is five grounds** across 238 blocks. DJ parked it deliberately.
- **The four held body blocks are a FAMILY question**, not a shape one; two wear another
  family's canon ground.
- **The head text colour `#6a1b9a` is 16 blocks in clean strata** (L04 5/5, L09 6/6,
  L10 5/5, 0 of 59 elsewhere), cutting ACROSS the shape classes.
- **L03 `3.44` carries `id="glossary-trim"` on a BODY block** where every other is `term-*`.
- **`BookComponentStandard` §7.4 carries a stale number** — says 184 where the measured
  figure is 238. Make it a derivation.
- **§6.5's nav-pill rule still says 12–14** where the live range is 10 to 19. Since S129.
- **§24.14a and §24.14b still have NO section body**, and `§24.14b` names TWO different
  rules across the S128 and S132 entries. Next free letter is §24.14e.
- **L07 `[IMAGE 7.3]`** is landed by a GRAPHIC across the two number spaces (§10), unruled.

## Carried, unchanged
Should `ZUMO_FAMILY_PINS.md` carry a version home? · `css/semantic.css` carries none either ·
the 3 `glyph_scan` leads · `glyph_scan`'s U+2100 floor · quick-reference anchors in L02–L06
only · **timers appear in L02/L03/L04 only — S69 burned a session on a false finding here,
READ before counting** · the callout border-width probe · the colour ledger, 16 items ·
`index.html` carries no version home · `BONUS_MARK`/`MARK` indexed nowhere · **L01's BC02
does not carry L01's objectives (legacy, ruled S119)** · S116's past-tense question: RETIRE
IT · L14's score formula is `<code>` and is not code · four `data-reveal="mechanism"` blocks
are not on §20.1's whitelist · **the mark roster RECONCILES and is gated (61). Do not
re-open.** · **`build_css` is NOT idempotent on this tree** — `.ul-ls-none-2`/`-3` alternate
across runs; §27.13 assumes one fixed point, there are two.

## Learner mode & book content (untouched for many sessions)
L03_C05 Variable Speed · L03 C01/C05/C06 reference a `finished` payload that does not exist
for L03 (staged in `ZUMO_L03_TEMPLATES.md`) · whole-template starters L08/L09/L10 · Maker
batch (bulk DL · `?lesson=N` gate · C## labels) · L01 VS Code multi-root step · challenge
card Pass B.

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
9. **Never write a real version number as an arrow pair in prose.**
10. **A document cannot name the commit that contains it.**
11. **AN EDIT TO A FILE WITH REPEATED LANDMARK LINES TARGETS AN INDEX AND ASSERTS IT** (§6.12c).
12. **AN EDIT THAT CHANGES LINE COUNT INVALIDATES EVERY LINE-KEYED TARGET BELOW IT.** Go DESCENDING.
13. **A SNAPSHOT TAKEN BEFORE THE WORK IS NOT A SNAPSHOT OF THE WORK.**
14. **A CONTROL THAT DEPENDS ON THE STATE OF WHAT IT AUDITS IS NOT A CONTROL.**
15. **A CONTROL RUN AGAINST AN UNTRACKED FILE HAS NO RESTORE PATH** — `git checkout --`
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
25. **A GENERATED CLASS NAME IS NOT A HANDLE.** Its `-N` suffix is assigned by usage RANK.
    Check the rank MARGIN before adding uses; locate by an authored attribute, never a class.
26. **MEASURE THE PROPERTY THE RULING NAMES, NOT A PROXY FOR IT.** Read the specimens first.
27. **A COVERAGE COUNT MEASURES BLOCKS SCANNED, NOT BLOCKS ASSERTED.** A gate carrying
    exceptions owes a HOLD ARM.
28. **A STRUCTURAL CHANGE THAT ENDS A SENTENCE EARLY OWES THE SENTENCE A LOOK.**
29. **NEW, S135: PIN THE DENOMINATOR, NOT THE REMAINDER.** A count that is MEANT to fall
    cannot guard the population it is drawn from. `outstanding` falling looks like progress
    whether art landed or a tag was deleted; only `planned` can tell those apart.
30. **NEW, S135: A WORKING COPY YOU HAVE RUN TOOLS IN IS NOT THE REPO.** When two readings
    of the same file disagree, RE-CLONE. Do not reconcile them, and never quote a working
    copy as evidence of what is live.
