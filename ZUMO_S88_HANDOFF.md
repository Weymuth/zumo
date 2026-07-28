# ZUMO — S88 HANDOFF (written at S87 close · paste at top of Session 88)

## Session open ritual (do this without being asked)
1. `git clone --depth 1 https://github.com/Weymuth/zumo.git`
2. Read `LIVE_ZUMO_TEXTBOOK.md` — verify date / status / versions.
3. `grep -oE "Bible version: v[0-9.]+" ZUMO_SUPER_BIBLE.md`
4. `python3 book_gates.py` · `python3 pill_sweep.py --audit lessons/Lesson_*.html` · `python3 lesson_inventory.py`
5. **Every version in this handoff is a LEAD.** Grep the files. The files win.

## LIVE AT S87 CLOSE
Bible **v8.76** · book_gates **v1.20 (32 gates, 32/32 PASS)** · gen_bonus_banner **v1.2** ·
lesson_inventory v1.0.5 · tutor v1.1.0 · Maker v2.45.1 · pill_sweep v1.0 · Harness v3.0

L01 v03.10.4 · L02 **v03.2.0** · L03 **v03.16.0** · L04 v04.9.1 · L05 v04.11.1 · L06 **v04.14.0** ·
L07 **v04.10.0** · L08 **v04.9.0** · L09 **v05.7.0** · L10 **v02.7.0** · L11 **v02.9.0** ·
L12 **v01.10.0** · L13 **v02.9.0** · L14 **v02.11.0** · L15 **v02.8.0** · L16 v02.5.4

Census: lines **39,865** (was 39,837) · headings 1,025 · anchors 174 · fences 174 · part 64 ·
constructs 171 · mystery 56 · reveals 403. **Only `lines` moved** — that identity is the evidence
the batch was additive prose, no structural change. `--anomalies` unchanged.

## FIRST JOB S88 — DJ IS UPLOADING ChatGPT NOTES TO ANALYSE
DJ has been drafting **book standards in ChatGPT in parallel** and will paste/upload the notes.
Analyse them against live canon the way S87 did the VISUALS folder proposal: **grep the repo before
agreeing or disagreeing.** The six corrections already sent back on the VISUALS proposal:
1. **IMAGE and GRAPHIC are SEPARATE number spaces** — their example ran `GRAPHIC_7-15 → IMAGE_7-16`
   as one sequence, and `L07_GRAPHIC_7-16_eight_file_architecture.svg` already exists (real clash).
2. **SOURCE/ and WORKING/ cannot live in this repo** — Pages serves the whole repo; verified
   `book_gates.py`, `ZUMO_SUPER_BIBLE.md`, `IMAGE_SHOT_LIST.md` all return **HTTP 200**.
3. **FINAL stays flat in `images/`** — 192 live `<img>` refs point at `/zumo/images/`.
4. **"Replace in place" needs a cache clause** — 0 of 192 srcs carry `?v=`.
5. **Say where the version lives** — image change = MINOR bump of the LESSON, in the hidden comment.
6. **Add a no-spaces-in-filenames rule** — two live offenders.

## WHAT SHIPPED IN S87
**Rendered-pages verification (the S86 debt), then two classes closed.**

- **Pages is reachable from the sandbox for the first time.** All **21 pages byte-identical**
  between GitHub Pages and repo HEAD. Images load (13/13 on L08, 0 broken).
- **All 14 bonus banners verified RENDERED** — OCR compared against `gen_bonus_banner.py`'s own
  table (imported, not retyped): **14/14 MATCH**. **14/14 nav pills** carry the family word, zero
  residual "Bonus" outside L16. Emoji resolve: **three pixel signatures, three families, zero
  within-family variance** (practice .153/11 bins · observation .167/12 · sabotage .180/13) —
  tofu would have collapsed all fourteen to one.
- **§4.5a NEW** — the cap and the FINISHED EARLY pointer, both generated from one constant and
  byte-gated. See Bible §4.5a. DJ ruled **B**.

## THE THING TO CARRY FORWARD
**A SUBSTRING TEST CANNOT DISTINGUISH FLAT FROM GRADIENT.** Gate 30's placement check was
`'#6c757d' not in capstyle`. L03's `linear-gradient(135deg, #6c757d, #4d5358)` **contains**
`#6c757d`, so it passed for its entire life. The independence test: same tree, **old gate PASSES,
new gate FAILS** — and it also passes a flat cap whose padding drifted 13px→12px, i.e. the hole was
never about gradients specifically. **When a gate checks a style, compare the bytes.**

## INSTRUMENT FINDINGS — READ BEFORE RENDERING ANYTHING (extends §24.7)
- Whole-page paint stops at **exactly 32,766 px = 2¹⁵−2**. That is the mechanism behind §24.7's
  black tail, which S86 could only describe as a percentage. L08 is 42,964 px, so 24% of it can
  never appear in a whole-page render.
- **`--crop-y` windows repaint past the ceiling and are byte-identical across runs (md5-verified).**
  A 14,000 px window paints fully → ~4–7 windows per lesson, ~50–95 s each.
- **In-page geometry is unusable**: bimodal (settled vs ~5× narrow-column), identical at 15 s and
  45 s, unchanged by `--width` 1000 vs 2400, `clientWidth` reads 0, and `--crop-h` under ~90 px
  perturbs layout. **The S87 sweep is coordinate-free for this reason** — it marches windows and
  detects the target by colour, then OCRs it.
- An **unreadable render file** is the reliable end-of-page signal.
- Working invocation:
  `wkhtmltoimage --width 1400 --disable-smart-width --crop-y Y --crop-h H --enable-javascript --javascript-delay 8000 --load-error-handling ignore <url> out.png`
- **`tesseract` is installed** — OCR the banner and compare against the generator's table.
- **S86's eight PART-seam readings used this instrument before the bimodality was known.
  Re-derive them, do not inherit them.** The S87 sweep would do it cheaply.

## OPEN — IN PRIORITY ORDER

**1. The mono font splits mid-book.** `<pre>`/`<code>` are **Courier-first in L02–L09** and
**Consolas-first in L01, L10–L16** — the same construct disagreeing with itself (`<pre>` 536 vs 282,
`<code>` 1,779 vs 112). A student moving from L09 to L10 watches the code typeface change. Two
sharpeners: **§22 ties the code styling to the student's REAL editor, and VS Code's default is
Consolas/Menlo, not Courier New** — so the ~2,315-use majority is the variant that does not match
the thing it imitates; and the break sits at **exactly the L09/L10 seam where the FINISHED EARLY
pointer also stopped**, consistent with L12–L16 landing in one commit (`94acc10`, S35). Needs a DJ
ruling, and it is *not* brand-decidable — see below.

**2. RoboLore branding guide is coming — protect the carve-out BEFORE it is written.**
§22 records that the real terminal green is ~`#23d18b`, that `#6a9955` is off it, and that DJ ruled
to keep `#6a9955` anyway — ***"do not 'correct' it."*** A branding guide arriving without that will
correct it, and the same argument covers the code FONT. **The code palette and code font must be
marked out of scope where the guide's author will see it.** Rebrand surface, measured S87:
230 distinct colours · 80 governed (18,979 uses) · **150 in no rule (1,615 uses)** · 20,594 colour
literals total, of which ~10,000 are the VS Code theme and must not move. Also 17 font-family
declarations for two roles, 47 font-sizes, 15 border-radii — all ungoverned.
**Canvas strips `<style>` and `class=`, so inline colour is forced: generation from a table is the
only mechanism that scales.** §4.5a is the worked example.

**3. §21 Robot Icon Family already disagrees with itself on the record** — spec is 64px inset, all
five ship at **10–18px**, DJ ruled "leave them for now". A RoboLore guide must ratify or repair it.

**4. Weeding criterion for BC03 still needs a DJ ruling** — candidates L02 (7 items), L07 (6),
L08 (6). Blocks the §25.8 weeding pass. Carried from S84.

**5. L16 remains outside the family** — 2 cards against 4, still reads `Bonus:`, still the only pill
saying "Bonus", and now the only lesson with no FINISHED EARLY pointer. Gate 31 fails the moment it
reaches four cards. DJ: *"Let's wait."*

**6. LEADS LOGGED IN S87, NOT FIXED** (read before acting — §24.6c):
- **The back-to-top construct is drifted three ways** (`↑` literal · `&uarr;` · `&#8593;`, differing
  inline styles) and **L10 has none at all before its bonus block** — it wraps the link in a `<div>`
  rather than a `<p>`. Same §6.8a shape.
- **Bonus card titles are drifted four ways**: L10 bare titles · L11 `Mystery N:` · L12–L14
  `Mystery BN —` · L15 `BN —`. Crosses the tagged line, no rule governs it.
- Carried from S86, all still open: **L12's bonus block holds ZERO `<details>`** · **L15's four
  Sabotage reveals are `hint`-only** · four `data-reveal="mechanism"` blocks reach the tutor ·
  card title level is three strata (h3 / h4 / `#6c757d` div in L12 alone) · a `__pycache__/*.pyc`
  is committed, same class as the standing `.DS_Store`.

**7. Sabotage family's internal order may be inverted against the difficulty goal** — hidden-culprit
hunts FIRST (L08–L10), shown-line mechanism LATER (L11–L16). **Look at this during the difficulty
audit, not before.**

## STANDING QUEUE (carried)
Difficulty-progression audit (L01–L03 easy → consistently harder book-wide, DJ's stated big goal) ·
challenge-card full redesign Part B (~80–100 cards to the L06 Goal→Logic→Template pattern) ·
Maker batch (bulk starters DL · `?lesson=N` gate · C## labels) · L01 VS Code multi-root step ·
TDP template v3 (A5 Lab Log) · day-by-day grid + syllabus · L03 open items (1000 ms explainer,
modulo explainer, two Coach's Tips, C01/C05/C06 starter `finished`-payload debt shared with
L08/L09/L10).

## LESSONS FROM S87 (the ones that cost time)
- **`git checkout` reverts to HEAD, and during an unpushed session HEAD is the DEFECT.** Two
  controls silently tested the wrong tree. Caught only by asserting the injection landed. §24.6b,
  fourth session running.
- **Locate the cap from the banner match's START, never from the `id=` offset** — searching back
  from `id="bonus-challenges"` lands on the banner's own `<div>`. Gate 30 does this right; two
  ad-hoc audits in S87 did not, and one printed all-`?` output that was the tell.
- **A colour tolerance can erase the distinction you are testing** — `tol=6` conflated the callout's
  `#f8f9fa` with the page's `#fafafa`. Exact match, or the instrument cannot see the thing.
- **`rows[0]` and `rows[-1]` are min and max of a SPARSE list**, not a contiguous run. Compute runs.
- **A constant is not unique just because it is canonical** — `CAP` appears 5× in L10 (§10 panel
  headers share it). Anchor on the unique id, not on the style string.
