# ZUMO — S92 HANDOFF (written at S91 close · paste at top of Session 92)

## Session open ritual (do this without being asked)
1. `git clone --depth 1 https://github.com/Weymuth/zumo.git`
2. Read `LIVE_ZUMO_TEXTBOOK.md` — verify date / status / versions.
3. `grep -m1 -oE "Bible version: v[0-9.]+" ZUMO_SUPER_BIBLE.md` — **`-m1` matters, line 17 is
   the version line and runs ~96,000 characters.**
4. `python3 book_gates.py` · `python3 gen_component.py --selftest` ·
   `python3 lesson_inventory.py` · `python3 lesson_inventory.py --schemes` ·
   `python3 pill_sweep.py --audit lessons/Lesson_*.html`
5. **Every version below is a LEAD. Grep the files. The files win.**
6. **§24.10 is now canon: the parser is the default instrument.** Structural questions go to
   `lesson_inventory.py`; grep is legal only for reading ONE line of known format.

---

# READ THIS FIRST — S91's biggest error, and it governs S92's first job

**I spent most of S91 acting on a rule I had only read half of.** §6.6a's sentence was
truncated in every extraction I made of it, ending at *"Labels are"*. I filled in the rest
and built a 69-item violation list on top of it. The full text says:

> Labels are **bare** ("Tip" / "Note" / "Warning", never "Coach's Tip/Note") to match the
> Icon Guide; the coach's warmth lives in the prose, not the label.
> … ⚠️ **Warning** — *a real caution, usually safety*. **A titled warning keeps its
> descriptive title (e.g. "⚠️ Battery Safety").**

**"Bare" means no `Coach's` prefix. §6.6a EXPLICITLY PERMITS a descriptive title, and its own
worked example is `⚠️ Battery Safety` — the exact label I flattened to bare `⚠️ WARNING`.**

So: **there were never 69 violations.** A real §6.6a audit is a search for `Coach's`
prefixes, and **that audit has never been run.** Do it in S92 before anything else in this area.

**Four labels are currently flattened against the rule** and are a live inconsistency — 44
other titled labels kept theirs:

| L | line | was | is now |
|---|---:|---|---|
| 01 | 713 | `⚠️ Battery Safety` — §6.6a's own example | `⚠️ WARNING` |
| 06 | 1103 | `⚠️ SAFETY — first autonomous drive` | `⚠️ WARNING` |
| 07 | 1762 | `⚠️ SAFETY — tuning runs` | `⚠️ WARNING` |
| 04 | 125 | `📘 One promise before we start` | `📘 Note` |

DJ has not ruled on restoring them. **Option C (below) restores titles by construction**, so
the two decisions can be taken together.

---

# FIRST JOB — OPTION C, DJ's own design (DJ: *"Let's handoff and start C on the next session"*)

The callout label splits onto two lines: **bare family word, then the title, then prose.**

```
BEFORE   📘 Note: Comments Are for Future-You
         When you write code, you understand it perfectly…

OPTION C 📘 Note
         Comments are for future-you
         When you write code, you understand it perfectly…
```

**Why DJ chose it:** nothing is lost, and the label element ends up containing *exactly* the
family word — so `lesson_inventory` and `gen_component` can read the family by exact match
instead of parsing prose out of a label. That is precisely what made the amber scheme hard to
classify (S91 found ONE scheme doing SIX jobs).

**What it costs, recorded so it is not a surprise:**
- ~44 titled callouts gain a line; two stacked bold lines per block.
- **§5.1 defines ONE title element.** C makes two, so the standard needs amending and bumping.
- It is a third structural sweep across all 16 lessons after S91's 794 and 133.
- A standalone bold line arguably reads *more* like a heading than an inline suffix — the
  "more categories" worry DJ raised originally. He accepted this.

**Do it as a generate, not per-instance** — the §6.8a precedent, and it is the third sweep in
two sessions, so the pattern is established. **Write the gate in the same pass (§24.2).**

---

## LIVE AT S91 CLOSE — twelve pushes, every one fresh-clone verified

Head `03d1e85`.

Bible **v8.78** · **BookComponentStandard v01.8.0** · **gen_component v1.5** ·
**book_gates v1.25 (34 gates, 34/34)** · **lesson_inventory v1.1.0** · Maker **v2.45.1** ·
pill_sweep v1.0 · gen_bonus_banner v1.2 · gen_part_banners v1.0 · gate_payload_match v1.6 ·
Harness v3.0 · timer v1.3.0 · tutor v1.1.0 · index v1.3.0 · going_deeper **v01.1.1**

**ALL 16 LESSONS CHANGED IN S91** (three times each — SAFETY/labels, then the 794 title
sweep, then the 133 shape sweep):
L01 **v03.13.0** · L02 **v03.4.0** · L03 **v03.18.0** · L04 **v04.12.0** · L05 **v04.13.0** ·
L06 **v04.17.0** · L07 **v04.13.0** · L08 **v04.12.0** · L09 **v05.10.0** · L10 **v02.9.0** ·
L11 **v02.11.0** · L12 **v01.12.0** · L13 **v02.11.0** · L14 **v02.13.0** · L15 **v02.10.0** ·
L16 **v02.7.0**

`images/icons/` **48 svg + LICENSE** (generator INPUT, never written) · `images/marks/` **40**

**Census unchanged from S87 through S91:** lines **39,792** · headings 1,025 · anchors 174 ·
fences 174 · part 64 · constructs 171 · mystery 56 · reveals 403. pill_sweep 0 old pills.

**Callout census:** 1,048 blocks · 105 (bg, border, glyph) triples · titles **991 canonical
block form · 0 inline · 22 sentence-lead `<b>` · 35 no title** · **115 off-canon geometry**
(frozen baseline, gate 33).

---

# DJ'S STANDING DIRECTIVE — STILL HOLDS THE REPAINT

> Heritage Blue governs the book's structural identity. It does not automatically replace
> semantic callout colors. **Hold the palette rollout until the component generation table and
> semantic palette are approved.** Then repaint all affected lessons as one coordinated batch.

**The component table was APPROVED at S91** and is recorded in §7 on disk. **The semantic
palette is still UNAPPROVED** — and it is now a semantic **THREE**, green/amber/purple, because
retiring SAFETY emptied the red role. §7 states in writing that the roster approval does NOT
cover the palette, so a later reader cannot mistake one for the other.

**DJ has palette studies he has not shown yet** — row C of the RoboLore study settled Heritage
Blue's values at S91 and he said there were others he liked. Ask for them when the palette
comes up.

---

# WHAT SHIPPED IN S91

1. **The 26-family table APPROVED** (DJ: *"I approve"*), recorded in §7 with a dated entry.
   THE WALL's name raised for rename and kept.
2. **Heritage Blue corrected to the study's row C** — `#162337` · `#43566B` · `#8C6A43` ·
   `#C3A36A` · `#F4EBDD`. All 8 tints, titles and contrast figures **re-derived**, floor
   landing at **5.11**, exactly where the book already was.
3. **Brass's published contrast fixed** — 5.44 was bronze's number, copied with bronze's title
   colour. Verified by reproducing 7 of 8 tints byte-exact from the 10% mix model.
4. **Steel Blue `#6985AB` → `#708BAF`** — row C's lighter navy dropped band text to 4.17.
5. **SAFETY retired** (DJ: *"get rid of safety and make them all warning"*). Red role emptied,
   `shield-exclamation` deleted from icons/ AND marks/, 25 families / 48 marks.
6. **Bible §24.10** — the parser is the default instrument, grep reads one known line.
7. **`gen_component` v1.5** — the marks-absence hole closed; two hardcoded counts derived.
8. **`lesson_inventory` v1.1.0** — callouts enumerated by (bg, border, glyph); `--callouts`
   and `--schemes`.
9. **`book_gates` v1.25, gates 33 + 34** — callout geometry against a frozen 115 baseline, and
   the title block-form gate.
10. **Two structural sweeps:** 794 titles `<strong>` → block form + 119 redundant `<br>`;
    then 133 more (111 `<span>`-led, 22 `<b>` titles) + 111 retired em-dashes.

---

# OPEN — NOT RESOLVED

## The semantic three holds the repaint
Green `#3F6B52` · amber `#8A6420` · purple `#5B4B7A`. Unapproved. **Nothing of Heritage Blue
renders on the site** — zero of its values appear in any of the 18 pages, and the 40 marks are
referenced nowhere. **Five sessions of palette work have produced no visible change to the book.**
DJ knows; he asked directly at S91 and was told plainly.

## The amber scheme was doing SIX jobs — classification done, not applied
`ZUMO_AMBER_CLASSIFICATION_S91.md` (delivered, not in the repo) holds DJ's markup of all 76:
**Reminder 27 · Note 23 · Warning 19 · Rule 4 · Tip 2 · 1 unresolved.** Two of those are
families the table does not have — **REMINDER** and **RULE/POLICY**.

**DJ asked for a repurposing candidate and there are two clean ones:** **WRITE IT** and
**COMMON PITFALLS** have **ZERO live blocks each**, so the table can absorb both new families
at 25 with no new icons. Careful: HINT, ANSWER and GLOSSARY also read zero but are alive as
OTHER constructs (`<details>` reveals, a page section) — retiring those would break live things.

## Glyph / family mismatches — at least three, never fully audited
L03 1180 `💡 Note` · L03 1285 `📘 Tip` · L05 1330 `👀 Note`. Only two pairings were ever
tested. **A full glyph-vs-family audit has not been run.**

## 22 sentence-lead `<b>` blocks are deliberately not titles
A `<b>` not followed by `<br>` or a block element is a sentence SUBJECT — converting it splits
the sentence (*"The #1 project killer"* / *"is not a bug."*). **No assert verifies that
discriminator; it is judgement encoded as a rule.**

## Carried from S90, untouched
§9 numbered marks vs Bible §18.2 (LOCKED — do not reopen; DJ closed it). §9 also now names two
hexes that left the palette (`#7B6240`, `#F5F2E9`). The page still renders `#fafafa`/`#333`,
not Parchment/Deep Navy, so **every contrast figure in the standard is against the intended
page, not the live one.** §18.2's canonical tag mandates `raw.githubusercontent.com` while all
223 live image refs use `weymuth.github.io`. Two misfiled blocks in L12.

---

# STANDING QUEUE (carried)

**Difficulty-progression audit — measured at S91, and the news is good.** The two-axis pill is
the instrument. Doing-axis averages per lesson: 1.36 · 1.67 · 1.88 · 2.00 · 2.20 · 2.29 · 2.29 ·
2.50 · 2.50 · 2.60 · 2.00 · 2.67 · 3.00 · 2.67 · 3.29 · (L16 none). **Only 2 inversions in 14
transitions**, so this is not a rebuild — it is three specific problems:
- **L10→L11 is the real dip** (2.60 → 2.00) and L11's internal order is the jaggedest in the
  book: `1 · 2 · 4 · 2 · 1`, peaking mid-lesson and **ending on its easiest challenge**.
- **TOUGH is used 3 times in 87 challenges.** The five-tier scale behaves as four, with the gap
  exactly where a gradual ramp needs the most resolution.
- **The grasp axis is bumpier than the doing axis** (4 inversions vs 2) — the opposite of what a
  flipped classroom wants.
- L03 and L11 both end on their easiest challenge after a hard one. **§6.12a fixes sequential
  numbering but says nothing about ascending difficulty within a lesson — needs a DJ ruling.**

Challenge-card redesign Part B (~80–100 cards to L06's Goal→Logic→Template pattern) ·
Maker batch (bulk starters DL · `?lesson=N` gate · C## labels) · L01 VS Code multi-root step ·
TDP template v3 (A5 Lab Log) · day-by-day grid + syllabus · L03 open items (1000 ms explainer,
modulo explainer, two Coach's Tips, C01/C05/C06 starter `finished`-payload debt shared with
L08/L09/L10) · BC03 weeding criterion · L16 outside the bonus family (DJ: *"Let's wait."*) ·
**robot icons §21 still 2 of 5** — Romi, Balboa, Zircon absent, S61 blocker never cleared, five
regeneration prompts already written · S87's six logged-not-fixed leads · S86's eight PART-seam
readings · §25.6's header example reads `Version 02.7` for L11 (now v02.11).

**Image shot list: 21 of 25 outstanding.** Most are DJ-and-a-camera and **must not be
AI-generated**. Four are legitimate GPT atmosphere work (L13-02, L14-01, L14-02, L16-01).
L07 7-13 is misfiled — it is a diagram, so it is Claude's.

**Housekeeping:** `__pycache__/lesson_inventory.cpython-312.pyc` is committed (logged S86,
never cleared). Same class as the old `.DS_Store`. `git rm` it.

---

# LESSONS FROM S91

- **A RULE READ IN PART IS A RULE NOT READ.** §6.6a's sentence ended at *"Labels are"* in every
  extraction I made, and I supplied the rest from inference. The missing half **permitted the
  exact thing I spent the session calling a violation**, and named as its example the one label
  I had already flattened. This happened in the session that canonized §24.10. **Print the whole
  rule before acting on it, and if a quote ends mid-clause, that is the finding.**
- **THREE ASSERTS, EACH EARNED BY A CONTROL THAT DEFEATED THE LAST.** Rendered-text-identical
  was beaten by a transform that ate a `<p>` (flat() strips tags either way). Tag-multiset-by-
  exact-delta was beaten by one that dropped every non-style attribute — **that one shipped into
  the tree and the CONSTRUCT CENSUS caught it at 171→169**, tags balancing perfectly while
  `data-challenge` markers vanished. Then a data-* multiset assert. **An assert you have not
  tried to defeat is a hope.**
- **A GATE'S BOUNDING CAN BE CORRECT BY ACCIDENT.** §25.2 bounded the Brain Check with
  `rfind('<div')` and worked only because the title happened to be a `<strong>`. Once titles
  became divs it read **0 items in all nine lessons** while every lesson was intact. The Bible
  already recorded this defect for §20.1(5) at S83, one gate over. **Old bounding produces 9
  false failures on the tree the fixed gate passes.**
- **A COUNT HAS NO BUSINESS INSIDE A PARSING ANCHOR.** Retiring one role broke
  `gen_component` twice: the §5 boundary was the literal `'Eight roles.'` and a
  `len(palette) == 8` assert sat beside it. Both now derive from the document. **This is S90's
  hardcoded-count lesson recurring inside the tool written to avoid it.**
- **A GATE WRITTEN TO THE SHAPE IN FRONT OF YOU COVERS ONE SHAPE.** Gate 34 rejected a bare
  `<strong>`, so 120 `<span>`-led and 44 `<b>` titles walked straight through the gate shipped
  two hours earlier. **Census the construct's shapes before writing its gate.**
- **A RULING APPLIED TO THE BOOK IS NOT A RULING APPLIED TO THE CANON.** SAFETY was retired in
  six lessons, in LIVE.md and in the Bible changelog, and `BookComponentStandard` was left
  saying 26 families on eight roles. `--selftest` passed 22/22 throughout, because the standard
  was internally consistent **with itself** — the instrument cannot see that a ruling never
  arrived (§24.8). **Found only because DJ asked for a triple-check.**
- **§24.4 TWICE IN ONE SESSION.** "4 fixed, 68 remain" and a hardcoded before-count of 123,
  both arrived at by subtracting from memory instead of re-running the parser. Both wrong, both
  caught by measuring afterwards.
- **VERIFY THE CONTROL LANDED (§24.6b).** A control reported zero failures because running it
  from `/tmp` put `/tmp` on `sys.path` and `lesson_inventory` never imported. Three "passing"
  results were that error.
- **A LINE-DERIVED OFFSET CANNOT SEPARATE TWO CALLOUTS ON ONE LINE.** L16 carries 9 such pairs,
  which is why gate 34 reports 142 where the sweep converted 133. Both are right.
