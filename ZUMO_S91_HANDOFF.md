# ZUMO — S91 HANDOFF (written at S90 close · paste at top of Session 91)

## Session open ritual (do this without being asked)
1. `git clone --depth 1 https://github.com/Weymuth/zumo.git`
2. Read `LIVE_ZUMO_TEXTBOOK.md` — verify date / status / versions.
3. `grep -m1 -oE "Bible version: v[0-9.]+" ZUMO_SUPER_BIBLE.md`
4. `python3 book_gates.py` · **`python3 gen_component.py --selftest`** ·
   `python3 pill_sweep.py --audit lessons/Lesson_*.html` · `python3 lesson_inventory.py`
5. **Every version in this handoff is a LEAD. Grep the files. The files win.**

**CORRECTION to S90's handoff — the Bible grep.** S90's handoff said *"always exclude line 17."*
**Line 17 IS the version line.** It opens `**Bible version: v8.77**` and then runs ~95,000
characters of changelog on the same line, which is why it floods a loose pattern — but excluding
it returns nothing at all. Use `grep -m1` as in step 3. This cost a turn at S90 open and had cost
two in S89 for the opposite reason. **§24.6c has now been paid five times, always against a
handoff — including this one.**

---

## LIVE AT S90 CLOSE — six pushes, all fresh-clone verified

`a289c58` marks · `c0371d4` S90 Fix · `9f18d77` + `e465b4b` bricks · `7c59a0d` Heritage Blue ·
`b97df52` band ramp

Bible **v8.77** (untouched) · **BookComponentStandard v01.5.0** · **gen_component v1.3 (22 checks)** ·
book_gates **v1.21 (32 gates, 32/32)** · Maker v2.45.1 · pill_sweep v1.0 · lesson_inventory v1.0.5 ·
gen_bonus_banner v1.2 · gen_part_banners v1.0 · gate_payload_match v1.6 · Harness v3.0 ·
timer v1.3.0 · tutor v1.1.0 · index v1.3.0

**NO LESSON FILE CHANGED IN S90.** L01 v03.10.5 · L02 v03.2.1 · L03 v03.16.1 · L04 v04.9.2 ·
L05 v04.11.2 · L06 v04.14.1 · L07 v04.10.1 · L08 v04.9.1 · L09 v05.7.1 · L10 v02.7.1 ·
L11 v02.9.1 · L12 v01.10.1 · L13 v02.9.1 · L14 v02.11.1 · L15 v02.8.1 · L16 v02.5.5 ·
going_deeper v01.1.1

`images/icons/` 49 marks + LICENSE (**generator INPUT, never written**) · `images/marks/` 41
generated marks · 8 marks deferred to the nav batch.

Census unchanged from S87/S88/S89: lines **39,792** · headings 1,025 · anchors 174 · fences 174 ·
part 64 · constructs 171 · mystery 56 · reveals 403. pill_sweep 16/16 SWEPT, 0 old pills.

---

# DJ'S STANDING DIRECTIVE — READ BEFORE TOUCHING ANY LESSON

Given verbatim at S90, and it governs everything downstream:

> Heritage Blue governs the book's structural identity: navigation, lesson and section headers,
> table framing, neutral instructional UI, and branded surfaces. It does not automatically
> replace semantic callout colors. NOTE, TIP, INSIGHT, WARNING, THE WALL, and similar roles may
> retain distinct functional colors when they support meaning, but they must sit coherently
> beneath the Heritage Blue system.
>
> **Do not perform a broad L11/L12-only repaint yet.** Correct the two objectively misfiled
> component types if desired, but **hold the palette rollout until the component generation table
> and semantic palette are approved.** Then repaint all affected lessons as one coordinated batch
> and bump only the lessons whose HTML changes.

**Two things gate the repaint and NEITHER has been approved:** the 26-family component table, and
the semantic palette (green / amber / red / purple). Do not start a repaint until DJ rules on both.

---

# WHAT SHIPPED IN S90

## 1. `gen_component.py` — the generator (v1.0 → v1.3)

Built to §4's three primitives. `mark()` is one glyph with no wrapper; `callout()` and
`legend_entry()` wrap it; the mark is byte-identical in both, asserted. **Everything is PARSED
from `BookComponentStandard.md`** — §5.0 Heritage Blue, §5.0.1 band ramp, §5 palette, §5.1
geometry, §6.1 shipping form, §7 families, §7.1 states, §7.2 groups and grounds, §7.3 counts.
No colour, glyph, role or geometry literal is restated in the generator.

**A family now goes in as a table row and the generator picks it up with no code change.** That
happened twice in S90 and is the whole payoff.

## 2. `images/marks/` — 41 generated marks, `images/icons/` pristine

25 family marks take their role's **title** colour; 14 supporting marks on the page tint take
body text `#0B1A2E`; the **8 Systems marks sit on filled band headers and are deferred to the nav
batch by parsing the §7.2 Grounds table**, not by judgement. Regeneration is byte-stable.

## 3. Two new families — the table went 24 → 26

**ENGINEER'S LOG · `journal-text` · brass.** Found while surveying: a live, book-wide callout in
all 16 lessons that the family table did not have. `journal-text` was already in the set as the
Systems *notebook* mark, so the family cost **no new icon** — it was promoted, and the Systems
entry removed. §7.2 now records the rule: a promoted mark leaves the supporting list, because two
entries would put one glyph on two grounds in two colours, which §4.1 forbids.

**THE WALL · `bricks` · purple.** The red `#fdecea`/`#e74c3c` block in L11/L12 — 18 of its 20
book-wide occurrences are in those two lessons. It is not WARNING (the student did nothing wrong),
not SAFETY (no hazard), not INSIGHT (a wall, not a door). It states or demonstrates a limit that
cannot be tuned away: *"There is no threshold that works. Not a badly chosen one — there is no
such number."* · *"A spin cannot calibrate a gyro."* · *"The encoder is not broken."* Named by DJ,
who noted he does not love the name — **a rename is now a table edit and a re-run, so it is cheap
to revisit.**

## 4. Heritage Blue defined — §5.0

It existed only in a chat window. Now on disk and gated. **All five values were already the spine
of §5:** Deep Navy `#0B1A2E` (navy border + title + body text) · Slate Blue `#3D5266` (slate
border) · Antique Bronze `#7B6240` (bronze border) · Warm Brass `#C9A463` (brass border) ·
Parchment `#F5F2E9` (page). So §5 never had to move.

Four roles are structural (slate, bronze, brass, navy) and four are semantic (green, amber, red,
purple), exactly as the directive describes.

**Recorded so nobody "fixes" it later:** titles are contrast-corrected derivations, not palette
hexes. Slate Blue at title weight fails the contrast floor, so slate's title is `#364A5E`. *A
title pulled back to its palette hex has been broken, not corrected.*

## 5. Section band ramp — §5.0.1, DJ-approved

**Hue carries meaning. Lightness carries location. One axis each, never both.**

| Band | Hex | Name |
|---|---|---|
| learn §1–3 | `#CBD3DE` | Frost Blue |
| build §4–6 | `#AFBCCE` | Mist Blue |
| verify §7–8 | `#96A8C0` | Fog Blue |
| extend §9 | `#7E95B4` | Harbor Blue |
| close §10+ | `#6985AB` | Steel Blue |

Runs **light to dark** — DJ's call, and it matches his stated goal that the book start easy and
get consistently harder. Deep Navy text on every band and Deep Navy for the bar; **one text colour
throughout.** No gradients. **No accent marks** — brass and bronze measure under 1.4:1 against the
lighter steps and occupy the same lightness region the ramp passes through, so no shade of them
separates across the whole scale. DJ scrapped the brass edge on §9 for this reason.

## 6. Six defects fixed from DJ's triple-check request

The standard carried **three version homes**, two stale — including the §1 conformance stamp,
which embedded a full version so every patch bump silently invalidated every stamp. **The stamp
now carries MAJOR.MINOR only**, mirroring the book's own §5b two-homes rule, and a gate holds every
stamp to the version line. Also: ENGINEER'S LOG was appended after the navy block instead of beside
the brass ones; the promotion paragraph split the five contiguous group blocks; a `§4.3` should
have been `§4.4`; `gen_component v1.0` had shipped three times with three different contents; and
the count gates used a hardcoded integer→word map that would have **failed a correct document** the
moment the count left the map.

---

# OPEN — NOT RESOLVED

## §9 numbered marks vs Bible §18.2 (LOCKED)

**Do not reopen with DJ unprompted. He closed it. Know it is there.**

Bible §18.2 (LOCKED, DJ ruling S43) fixes the inline spiral star as the real `spiral_star_NN.svg`
asset: gold gradient `#FFD34D → #F5A623`, `#1a5276` **vector-path** number (explicitly *not* font
text — renderer-proof), 200×200, `height: 1.1em`. 16 assets, built S40, DJ-approved, **26 live
references across 14 lessons.**

Standard §9 describes a numbered mark doing the same job at the same rendered size and
contradicting it on every visual property — flat `#7B6240`, `#F5F2E9` font-text number, 20-unit
grid, **gradients prohibited** — and never says the word *spiral*.

**DJ's S90 ruling: the stars are DONE. §18.2 stands. §9 left as written, NOT built.**
If ever reopened: §9's font-text number loses §18.2's renderer-proofing, and filenames would not
have to change (emitting `spiral_star_NN.svg` keeps all 26 tags working). Measured, independent of
any of that: the current gold star reads **1.28:1** against the page — nearly invisible as a shape,
carried entirely by its blue number. Flat `#7B6240` measures 5.12:1.

## The page itself is not on Heritage Blue

Lessons render on `background-color: #fafafa` with `color: #333`. §5 assumes Parchment `#F5F2E9`
and Deep Navy `#0B1A2E`. **Every contrast figure in the standard is against the intended page, not
the live one.** The band ramp assumes the page will move. Nothing gates this yet.

## §18.2's canonical tag is stale against the book it governs

It mandates `raw.githubusercontent.com`. All **223 live image references, including all 26 stars**,
use `weymuth.github.io`. `gen_component.py`'s `URL_BASE` follows the live book, not the Bible. One
of the two is wrong and nothing checks it. Cheap gate, not written.

## Two misfiled blocks in L12

Of the 18 red blocks, ~16 are THE WALL. Two are riding the styling for something else: the
*"binary did not change. AT ALL… Did the edit not save?"* mystery hook, and the B4
lesson-of-the-bug, which is closer to INSIGHT. **DJ explicitly allowed correcting these
independently of the palette hold** — it is a content fix, bumps L12 only.

---

# THE L11/L12 SURVEY — the repaint's real scope

**1,048 callout blocks book-wide**, not 923. Four spellings live:

```
border-left: 4px solid    923   canonical §5.1
border-left: 5px solid    108   off-geometry
border-left:4px solid      10   off-geometry, no space
border-left: 3px solid      3   off-geometry
```

**125 are off-canon and nothing gates the geometry.** 92 of those 125 are in L11 and L12, which
were authored **entirely in a second design system** — only 6 of 24 and 3 of 73 blocks use
canonical geometry.

| Alt style | Glyph | Count | Maps to |
|---|---|---|---|
| `#eceff1` / `#607d8b` | 📘 | book-wide, 126 | **NOTE** (slate) — clean |
| `#f0f7f0` / `#6b8e6b` | 💡 | book-wide, 83 | **TIP** (green) — clean |
| `#eafaf1` / `#27ae60` | ✅ in L11, 🏆 in L12 | 19, L11–L12 only | **INSIGHT** (proposed, unapproved) |
| `#fdecea` / `#e74c3c` | 🛑 | 18, L11–L12 only | **THE WALL** |

The green block **carries a different glyph in each lesson** — if it is one component its glyph
already disagrees with itself across the seam. Per S89's rule, do not flatten the L11/L12 seam
findings into one cause.

**A live collision the band ramp exists to fix:** today's §4–6 green band `#3a7d5c` sits **5°**
from the green TIP callout `#3F6B52`, and §7–8 pink `#c45d76` sits **22°** from red SAFETY. A green
TIP inside a green band means green twice for unrelated reasons. `--selftest` control-runs this
exact case.

---

# STANDING QUEUE (carried)

Difficulty-progression audit (L01–L03 easy → consistently harder — **DJ's stated big goal**) ·
challenge-card redesign Part B (~80–100 cards to the L06 Goal→Logic→Template pattern) ·
Maker batch (bulk starters DL · `?lesson=N` gate · C## labels) · L01 VS Code multi-root step ·
TDP template v3 (A5 Lab Log) · day-by-day grid + syllabus · L03 open items (1000 ms explainer,
modulo explainer, two Coach's Tips, C01/C05/C06 starter `finished`-payload debt shared with
L08/L09/L10) · BC03 weeding criterion · L16 outside the bonus family (DJ: *"Let's wait."*) ·
robot icons §21 — **still 2 of 5; Romi, Balboa and Zircon absent, S61 blocker never cleared, five
regeneration prompts already written** · S87's six logged-not-fixed leads · S86's eight PART-seam
readings still need re-deriving · §25.6's header example reads `Version 02.7` for L11 (now v02.9).

**Image shot list: 21 of 25 still outstanding** (only 4 landed since S33 — all three L05 SVGs plus
one L04 photo). Most are DJ-and-a-camera or DJ-and-a-screenshot and **must not be AI-generated** —
fabricated hardware photos and fake error screenshots contradict what the book teaches. Four are
legitimate GPT atmosphere work (L13-02, L14-01, L14-02, L16-01), with a caption caveat on L14-01.
**L07 7-13 is misfiled** — it is a diagram, so it is Claude's, not a photo.

**Parked:** the `icons/` ↔ §7.3 gate stays in `gen_component.py --selftest`, not `book_gates.py`
(DJ: *"No, let's do book later."*). `book_gates.py` walks lesson HTML; widening its coverage set is
exactly how S89's coverage defect happened.

---

# LESSONS FROM S90

- **A STANDARD'S PROSE IS NOT EVIDENCE ABOUT THE BOOK.** §9 reads like a plan to replace 16
  hand-drawn numbered files with one function, and matched the spiral stars on rendered size and
  outer radius. I built a line of reasoning on that and brought DJ a point-count question about a
  component he had finished in S40 and locked in S43. **One grep of §18.2 would have closed it
  before it was asked.** The standard describes what should be; only the files describe what is.
- **AN EXCEPTION CAN BE PROTECTING NOTHING.** I defended BRAIN CHECK's `#3D5266` as a deliberate
  exception because §5.2 demands two signals for a state change — without checking whether colour
  was one of them. It measures **1.91:1**. Measure the signal before defending the exception that
  carries it.
- **THE HANDOFF'S OWN FIX INSTRUCTIONS CAN BE THE DEFECT.** "Exclude line 17" was written to solve
  a real S89 problem and broke the grep it was meant to protect.
- **A NUMBER WITH TWO HOMES AND NO COMPARISON DRIFTS — AND SO DOES A VERSION.** §7 said
  `Forty-seven` while §7.3 said 48; the standard carried three version homes with two stale. Both
  now gated, both control-run.
- **A GATE THAT CRIES WOLF GETS IGNORED.** The count gates would have failed a *correct* document
  once the count left a hardcoded lookup. An unreadable input now reports as a gate limit, not a
  document defect — §24.9's rule applied to the gate itself.
- **RENDER IT BEFORE BELIEVING IT.** The band ramp looked settled as swatch rows. Drawn into the
  real nav, the §1–3 pills turned out to be Deep Navy on a Deep Navy bar. Three further rounds of
  measurement followed, and each one killed an idea that had read fine in the abstract — the
  graded bronze outline (edges collapse to 1.15:1 where the ramps cross), the Parchment bar (sits
  on a Parchment page), and the brass §9 edge (1.31:1).
- **I DREW A THING I HAD JUST PROVED WOULD NOT WORK.** Having measured that brass fails on light
  pills, I rendered a brass edge anyway, and used Parchment text at 3.38:1 in the same mock. Both
  were caught only by re-measuring the render afterwards. **Measure the artifact, not the
  intention.**
- **BOUNDED-EDIT ASSERTS PAID THREE TIMES** — two hardcoded family counts and a section boundary
  that started swallowing a new table, each caught before a write.
