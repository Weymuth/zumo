# ZUMO — S90 HANDOFF (written at S89 close · paste at top of Session 90)

## Session open ritual (do this without being asked)
1. `git clone --depth 1 https://github.com/Weymuth/zumo.git`
2. Read `LIVE_ZUMO_TEXTBOOK.md` — verify date / status / versions.
3. `grep -oE "Bible version: v[0-9.]+" ZUMO_SUPER_BIBLE.md`
4. `python3 book_gates.py` · `python3 pill_sweep.py --audit lessons/Lesson_*.html` · `python3 lesson_inventory.py`
5. **Every version in this handoff is a LEAD. Grep the files. The files win.**

**Grepping the Bible: exclude line 17.** The version line is one ~93,000-character paragraph
containing the entire changelog. It matches almost any pattern and floods the output. Always
`| grep -v "^17:"`. This cost two wasted turns in S89.

---

## LIVE AT S89 CLOSE — four pushes, all verified by fresh clone

Bible **v8.77** · book_gates **v1.21 (32 gates, 32/32 PASS)** · **BookComponentStandard v01.0.1** ·
Maker v2.45.1 · pill_sweep v1.0 · lesson_inventory v1.0.5 · gen_bonus_banner v1.2 · Harness v3.0 ·
timer v1.3.0 · tutor v1.1.0 · index v1.3.0

L01 v03.10.5 · L02 v03.2.1 · L03 v03.16.1 · L04 v04.9.2 · L05 v04.11.2 · L06 v04.14.1 ·
L07 v04.10.1 · L08 v04.9.1 · L09 v05.7.1 · L10 v02.7.1 · L11 v02.9.1 · L12 v01.10.1 ·
L13 v02.9.1 · L14 v02.11.1 · L15 v02.8.1 · L16 v02.5.5 · going_deeper **v01.1.1**

`images/icons/` — 48 Bootstrap Icons + `LICENSE` (49 files).

Census: lines **39,792** (was 39,865; −73 = exactly the 17 deleted banners) · headings 1,025 ·
anchors 174 · fences 174 · part 64 · constructs 171 · mystery 56 · reveals 403 — every counter
except lines byte-identical to S87/S88. pill_sweep 16/16 SWEPT, 0 old pills.

---

# FIRST JOB — DELETE `ZUMO_S89_HANDOFF.md`

The root must carry exactly ONE `ZUMO_SNN_HANDOFF.md` (§12.2, gate 28). If S89's is still there
alongside this one, **gate 28 is failing right now.** Procedure is in `PUSH_WORKFLOW.md` §Deletions —
a file batch can only add and overwrite, never delete, and this step has been missed twice.

---

# WHAT SHIPPED IN S89

## 1. `BookComponentStandard.md` v01.0.1 — repo root, beside the Bible

The RoboLore Book Component Standard. Everything S88 approved-and-unwritten is now on disk:
identity + anti-circular stamp rule · one versioning scheme · scope · the collapse rule ·
**the three primitives** · the 8-role palette · Bootstrap Icons + the single LICENSE obligation ·
**24 families / 48 marks** · collisions + near-collisions · numbered marks · generation · gate
design · change procedure.

**The core of the document is §4 — mark / callout / legend entry.**

```
mark(family)              -> one glyph, one family, no wrapper
callout(family,title,body)-> box + border + mark + title + body
legend_entry(family)      -> mark + family name, no box
```

One mark table, one generator, three emitters. **The mark is identical in every wrapper** — this is
not a tolerance for two rendering contexts, there is one mark and the wrappers differ. Legend
entries are GENERATED, never hand-authored.

## 2. The S88 family table was wrong in four places — corrected before writing

| | S88 said | Live truth (S89, verified against files) |
|---|---|---|
| NOTE | phantom, "zero lessons carry 📘" | **113 occurrences**, live in L01 + L06 |
| 📖 ×3 members | LEARN / NOTE / EXPLANATION | **LEARN / GLOSSARY / EXPLANATION** (crosses slate→bronze) |
| Families | 22 | **24** (+ HOW THIS SECTION WORKS, + WRITE IT) |
| Marks | 45 | **48** (+ `pin-angle`, `keyboard`, and the 3 battery marks I first omitted) |

**DJ's icon rulings:** NOTE = `sticky` (chosen over `info-circle` — the set already has four
circle-outline marks and PITFALLS `slash-circle` is its nearest neighbour) · HOW THIS SECTION
WORKS = `pin-angle` · WRITE IT = `keyboard`. DJ raised `pencil` for WRITE IT and chose **A** after
seeing the collision rendered: MY PLAN keeps `pencil-square`, WRITE IT takes `keyboard`, because the
two are adjacent items in the same list, share the brass role, and the book's own pedagogical point
is *plan in prose, then code at the keyboard* — two pencils erase it.

**Inferred, flagged not asked, one-line reversible:** WRITE IT role = **brass** · HOW THIS SECTION
WORKS role = **slate** (replacing its off-palette `#eceff1`/`#607d8b`) · family name **WRITE IT**
(must sit above both live wordings since the standard is book-agnostic).

## 3. Two legends exist and BOTH over-declare

- **HOW THIS SECTION WORKS** — 7 occurrences, L03–L09, always immediately after the `section-6`
  anchor. Names six steps; only four appear downstream. In L08's §6: THE GOAL 8× · MY PLAN 8× ·
  Compare 8× · Build green 10× — but **EXPLANATION and WRITE IT: zero.**
- **The 12-icon Icon Legend** — L01–L10 only, L11–L16 have none. Covers 8 of 24 families, declares
  4 that are not callouts, omits the rest.

Both are hand-authored. Generating them from the mark table fixes both by construction — that is
the payoff for the §4 primitive and it closes S88's parked "regenerate the legend" item as a side
effect rather than as separate work.

**WRITE IT's wording splits at the L06/L07 seam by design** — `Translate it` (L03–L06) →
`Build from YOUR plan` (L07–L09), where the lesson hands planning to the student. **Three seam
findings, three different causes: mono font L09/L10 = drift · FINISHED EARLY pointer L10 = absence ·
WRITE IT L06/L07 = intentional.** Do not flatten them into one "the book changes at lesson N" note.

## 4. Build banner deleted — 18 files, one atomic commit

Block gone from all 17 pages; `book_gates.py` v1.20 → **v1.21**. Old gates FAIL on new source
(2 gates), new gates PASS — proven, so the commit could not be split.

**A live defect was found and fixed:** `going_deeper.html` shipped a visible `Version 01.0` against
a hidden `v01.1.0`. **It survived because both §5b gates iterated `files` (16 lessons) while §25.6
iterated 17** — the one file that drifted was the one file the comparison never ran on. The gate's
logic was correct the whole time.

Also fixed: `L(f)` slices `f[15:17]` and returns `ml` for `going_deeper.html`, so the gate named the
wrong file while reporting the defect. New `P(f)` helper.

## 5. Bible v8.77 — §24.9 NEW

§5b loses home 1b · §9's superseded "BOTH VISIBLE HOMES" addendum kept as marked provenance with the
current one-visible-banner rule beneath it · §25.6 retitled.

**§24.9 A GATE'S COVERAGE SET IS PART OF THE GATE** — four rules:
- **Coverage is stated and asserted, never inherited.** A gate that passes because it never looked
  is indistinguishable in its output from one that passes because the condition holds.
- **A gate deliberately relied upon for a property it does not check is load-bearing on an
  accident.** v8.53 stated in the open that the two-homes gate *"needed no edit — it greps raw
  source, and raw source includes comments."* Seen, judged harmless, built upon — 19 sessions. This
  is NOT S87/S88's shape of an instrument silently failing.
- **A rule restated in two sections is two rules.**
- **A conformance stamp must name a document that exists.**

---

# S90 — WHERE TO START

**`gen_component.py`, at repo root** (matches `gen_bonus_banner.py` / `gen_part_banners.py`).
Built to the §4 primitives, generating from the standard's own table.

**Design question to settle first:** the 48 SVGs in `images/icons/` are **black**. Marks ship
pre-coloured per role because `currentColor` does not resolve through `<img>`. So either the
generator emits recoloured copies at build time, or the folder holds role-coloured variants and 48
becomes more. **The 48 are the generator's INPUT, not the shipped marks.**

**Then the repaint** — biggest diff, touches every callout in 16 lessons, gets a settled gate suite
and a proven generator underneath it. Note that the repaint and the build-banner commit each bump
all 17 files, so lessons take two bumps across the two batches. That was accepted deliberately:
isolating a gate change from a full-book repaint is worth more than a saved bump.

**A gate worth writing with it:** `images/icons/` must hold exactly the marks named in the standard's
table, in both directions. §7.3 exists to make that checkable — it was written for this.

**Nav colours are a SEPARATE SECOND BATCH** (§10+end group scheme, L03: `#3498db` `#3a7d5c`
`#c45d76` `#9b6a9e` `#6c757d`). Callouts and nav will look mismatched until both land. Do not fold
nav into the component pass.

---

# STANDING QUEUE (carried)

Difficulty-progression audit (L01–L03 easy → consistently harder — **DJ's stated big goal**) ·
challenge-card redesign Part B (~80–100 cards to the L06 Goal→Logic→Template pattern) ·
Maker batch (bulk starters DL · `?lesson=N` gate · C## labels) · L01 VS Code multi-root step ·
TDP template v3 (A5 Lab Log) · day-by-day grid + syllabus · L03 open items (1000 ms explainer,
modulo explainer, two Coach's Tips, C01/C05/C06 starter `finished`-payload debt shared with
L08/L09/L10) · BC03 weeding criterion (L02 7 items, L07 6, L08 6) · L16 outside the bonus family
(DJ: *"Let's wait."*) · robot icons §21 recolour against Heritage Blue · S87's six logged-not-fixed
leads (back-to-top drifted three ways with L10 missing it · bonus card titles drifted four ways ·
L12 zero `<details>` · L15 hint-only reveals · four `data-reveal="mechanism"` blocks reach the tutor ·
committed `.pyc`) · S86's eight PART-seam readings still need re-deriving, not inheriting ·
§25.6's header example reads `Version 02.7` for L11 (now v02.9) — stale before S89, left deliberately;
fixing Bible examples wants its own pass.

---

# LESSONS FROM S89

- **A GREP PROVES ONLY THAT A STRING YOU THOUGHT OF IS ABSENT.** DJ asked for a triple-check on the
  Bible before pushing and it found **three defects a passing grep had certified clean** — a summary
  line placed before the item it summarised, two orphaned bullets, and a stale `hidden banners`
  reference my `BUILD BANNER` search missed on casing alone. **Every one was a correct string in the
  wrong place.** What found them: reading each changed region in document order, plus a
  case-insensitive sweep. §24.8's test applies to greps — if the file had been perfect, that grep
  would have printed the same thing.
- **`book_gates.py` DOES NOT CHECK THE BIBLE.** It walks lesson HTML. Reporting "32/32 PASS" after a
  Bible edit is reporting on a file you did not touch. I did this repeatedly before catching it.
- **AN EMPTY RESULT ACROSS EVERY FILE IS AN INSTRUMENT FAILURE UNTIL PROVEN OTHERWISE.** A per-file
  grep for 📘 returned 0 for all 17 because `$'\U0001F4D8'` does not expand under `/bin/sh`. The
  Python census found 113. **A clean row of zeros is a tell, not a finding.** Control the instrument
  against a case you know is present.
- **A CONTAINER IS NOT ITS CONTENTS — AGAIN.** I asserted the §5b gate "counts without comparing"
  after reading its NAME. Its body compares on line 47. The real cause was coverage.
- **BOUNDED-EDIT ASSERTS EARN THEIR KEEP.** A `count==4` guard fired on my miscounted 6 and the
  write never happened.
- **§24.6c PAID FOUR TIMES, ALL AGAINST THE HANDOFF.** S89's handoff was wrong that §5b demands two
  visible banners (§5b superseded that at v8.53; the stale text was in §9), wrong that §5b's format
  string contradicts its examples (the `vXX.XX` is only in the v8.31 CHANGELOG, which is history and
  is not retro-edited), wrong that three gates must change together (only two would have broken),
  and wrong that zero lessons carry 📘. **A handoff is a lead, including this one.**
