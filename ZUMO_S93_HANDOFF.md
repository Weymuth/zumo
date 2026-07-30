# ZUMO — S93 HANDOFF (written at S92 close · paste at top of Session 93)

## Session open ritual (do this without being asked)
1. `git clone --depth 1 https://github.com/Weymuth/zumo.git`
2. Read `LIVE_ZUMO_TEXTBOOK.md` — verify date / status / versions.
3. `grep -m1 -oE "Bible version: v[0-9.]+" ZUMO_SUPER_BIBLE.md` — **`-m1` matters, the version
   line runs ~99,000 characters.**
4. `python3 book_gates.py` · `python3 gen_component.py --selftest` ·
   `python3 lesson_inventory.py` · `python3 lesson_inventory.py --schemes` ·
   `python3 pill_sweep.py --audit lessons/Lesson_*.html`
5. **Every version below is a LEAD. Grep the files. The files win.**
6. §24.10: the parser is the default instrument. `lesson_inventory.build(path)` is the
   entrypoint — **there is no `inventory()`**; calling it returns a false zero (S92 hit this).

---

# ⚠️ NOTHING IN S92 WAS PUSHED

Everything below is applied and verified **in a local clone only**. Head is still `9bffbee`.
The first job in S93 is to push, or to decide not to. **Do not treat S92's versions as live
until a fresh clone confirms them.**

---

# READ THIS FIRST — S92's own ruling was too strong, and the gate is what caught it

Mid-session I proposed and DJ approved: **"the scheme is the family of record."** I tested it
against 142 blocks where scheme and glyph agreed — **zero conflicts** — and read that as
confirmation.

It was not confirmation. **Those 142 could not disagree**, because I had selected the set BY
GLYPH. The blocks that could disagree were outside the set I was looking at.

Gate 35, written to the ruling rather than to my sweep, immediately found **24 blocks wearing
§6.6a paint while carrying another family's glyph**:

| glyph / label | blocks | what it actually is |
|---|---:|---|
`🔬 Curious how any of this actually works?` | 7 | the `going_deeper.html` hook |
`📝 DO THIS NOW` (on WARNING amber) | 7 | its own Icon Guide family |
`📋 WHAT YOU NEED BEFORE STARTING` (amber) | 2 | its own construct |
`🧠` `🔍` `💾` `📓` `🍽️` `🚨` `🎯` | 8 | one-offs, a read each |

Rewriting these to `📘 NOTE` / `⚠️ WARNING` would destroy seven families to satisfy a rule
about three. **The scheme is not the family — it is paint, and these 24 borrow it.**

Gate 35 was therefore **narrowed to the agreeing set (250)**, not the finding buried. Narrowing
the gate was the honest fix; deleting the failure was the tempting one.

**AN ASSERT THAT CANNOT FAIL IS NOT EVIDENCE.** Put in the Bible as the S92 lesson.

The one decision resting on the ruling was **L03 1285** (`Tip` title on a slate NOTE block,
📘 glyph). It survives on its own merits — two of three signals said Note — not on the ruling.

---

# WHAT SHIPPED (locally) IN S92

**1. The §6.6a `Coach's` audit — run for the first time, returns ZERO.**
0 violations across **279 family callouts and all 18 pages**. The four live `coach` strings are
one HTML comment in L02 and three prose sentences. **S91's 69-item list was entirely an artifact
of a rule read only as far as *"Labels are"***. Confirmed dead; do not revive it.

**2. OPTION C SWEPT — 250 blocks, 178 gained a line.**
Label element holds the family word ALONE; title beneath at 1.05em carrying the 8px gap.
- **Caps authored literally**, no `text-transform` — source string == rendered string.
- **72 bare blocks changed case only**: nothing to split, so nothing to demote.
- **3 blocks held out** (off-canon schemes, family not derivable): **L01 411, L02 2277, L06 731**.
  L06 731 is the interesting one — a bare `💡 Tip` whose LABEL is right and whose PAINT is wrong,
  the reverse of every other case.
- `sweep_option_c.py` is in the repo root. One-time tool; `--plan` is safe and re-runnable.

**3. Verification.** Applied to a CONTROL COPY first: all 16 files flatten identically outside
the label region, and the `<div>` delta equalled the titled count **178** — not merely balanced.
Census **39,792 → 39,970 = +178 exactly**; every other figure byte-identical incl. **constructs
at 171**, the count that caught S91's attribute-stripping bug.

**4. `book_gates` v1.25 → v1.26, gate 35.** Control-run against the pre-sweep tree, where it
fails with **230** — twenty short of the 250 edits, and those twenty are precisely the bare
labels already all-caps and therefore already conformant. Both numbers correct.

**5. `BookComponentStandard` v01.8.0 → v01.9.0.** §5.1 grew from one title element to two. Its
own `--selftest` caught a stale footer stamp at line 578 that the version bump missed — §1's
"every version stamp agrees" check earning its keep.

**6. Bible v8.78 → v8.79.** 15 lessons bumped MODERATE; **L16 unchanged at v02.7.0** (no §6.6a
family callouts).

---

# RULINGS TAKEN IN S92 (record, so they are not relitigated)

- Option C approved at 201→250 blocks after the scope was re-measured.
- **Case: CAPS everywhere.** DJ first ruled "no more all caps," then reversed to caps once
  counting showed the three §6.6a families are themselves Icon Guide entries and that normal
  text everywhere is **229 further labels** in families this sweep never opened.
- Unflatten the four S91-flattened labels — **NOT YET DONE, see open items.**
- Glyph follows family: **L03 1180 💡→📘 done.**
- **L03 1285** title `Tip`→`NOTE` done. **L05 1330** → Tip in TIP's green, **L08 1427** → NOTE:
  both **NOT DONE** (foreign glyphs put them outside the derived sweep).
- **CURIOUS → Going Deeper**, confirmed by measurement: all 7 blocks link to
  `going_deeper.html`, 7 for 7.
- **SEE stays its own family.** Tested and failed the same question: those blocks state expected
  output after an action already taken, which is verification, not enrichment. A student skipping
  every Going Deeper block should still read every SEE block.
- **1.0em PARKED, not declined.** 990 of 1,048 titles carry 1.05em → its own batch plus a §5.1
  amendment, and it would cut S91's three-property justification for the block form to two.

---

# OPEN — NOT RESOLVED

## SEE has two names and Option C makes the rename FORCED
Icon Guide says `SEE`; the 20 live blocks say `WHAT YOU SHOULD SEE`. Under Option C the label
must hold exactly one string, so this family **cannot ship until one name wins.** DJ finds "SEE"
lame. Candidates surviving both collisions: **`WHAT YOU SHOULD SEE`** (zero label edits — retire
the guide's short form), `EXPECTED`, `CONFIRM`. **"Check for yourself" was rejected** — reads as
an instruction, and collides with `✅ CHECKPOINT` (63 blocks, biggest family).
**DJ also raised `✋ YOUR TURN` to replace `📝 DO THIS NOW`** (34 labels + 10 legends) — warmer,
same imperative job. **UNRULED.** It does NOT fit SEE.

## Three live constructs are absent from BookComponentStandard
**SEE** (20 blocks) · **🛑** (18 blocks, L11/L12) · **the 🔬 hook** (7). SEE and 🛑 have zero
mentions in the standard. SEE is also getting a **new Bootstrap glyph** per DJ — `images/icons/`
is Bootstrap Icons (`shield-exclamation`, deleted at S91, is a Bootstrap name).

## The standard contradicts the book on red
The standard states in writing that **"Red was retired at S91, with the SAFETY family that was
its only member."** **21 blocks still render red** — L03 931, L06 618, L11 ×5, L12 ×12, L14 1459
— in **four different border hexes** (`#c0392b`, `#e74c3c`), and the 🛑 glyph carrying 18 of them
is not in the standard at all. Either "only member" is false or 21 blocks are off-canon paint.
**VERIFIED contradiction, DJ's call, not Claude's.**

## Carried, untouched
Semantic three (green `#3F6B52` / amber `#8A6420` / purple `#5B4B7A`) **unapproved — still holds
the repaint**; nothing of Heritage Blue renders on the site. DJ has palette studies not yet
shown — **ask for them.** `ZUMO_AMBER_CLASSIFICATION_S91.md` (Reminder 27 · Note 23 · Warning 19
· Rule 4 · Tip 2 · 1 unresolved) — **note that DJ's S92 definition of Note, *"don't forget or
here is some useful info,"* absorbs REMINDER**, so that family may not need to exist. WRITE IT
and COMMON PITFALLS remain the two zero-block repurposing candidates. §9 numbered marks LOCKED.
§18.2 mandates `raw.githubusercontent.com` while all 223 live image refs use `weymuth.github.io`.
Two misfiled blocks in L12. 22 sentence-lead `<b>` blocks are deliberately not titles, verified
by no assert. Glyph-vs-family audit now RUN: 4 real mismatches found, 1 was a false positive of
my own regex (L12 1210 `🛑 Note what it does NOT do` — "Note" is an imperative VERB).

---

# STANDING QUEUE (carried)

**Difficulty-progression audit** — measured at S91, only 2 inversions in 14 transitions, so it is
three specific problems, not a rebuild: **L10→L11 is the real dip** (2.60→2.00) and L11's internal
order is `1·2·4·2·1`, ending on its easiest challenge · **TOUGH used 3 times in 87 challenges**, so
the five-tier scale behaves as four · the **grasp axis is bumpier than the doing axis** (4 vs 2),
the opposite of what a flipped classroom wants · L03 and L11 both end easiest-after-hardest.
**§6.12a fixes sequential numbering but says nothing about ascending difficulty within a lesson —
needs a DJ ruling.**

Challenge-card redesign Part B (~80–100 cards to L06's Goal→Logic→Template pattern) · Maker batch
(bulk starters DL · `?lesson=N` gate · C## labels) · L01 VS Code multi-root step · TDP template v3
(A5 Lab Log) · day-by-day grid + syllabus · L03 open items (1000 ms explainer, modulo explainer,
two Coach's Tips, C01/C05/C06 starter `finished`-payload debt shared with L08/L09/L10) · BC03
weeding criterion · L16 outside the bonus family (DJ: *"Let's wait."*) · **robot icons §21 still
2 of 5** — Romi, Balboa, Zircon absent, S61 blocker never cleared, five regeneration prompts
already written · S87's six logged-not-fixed leads · S86's eight PART-seam readings · §25.6's
header example reads `Version 02.7` for L11.

**Image shot list: 21 of 25 outstanding.** Most are DJ-and-a-camera and **must not be
AI-generated**. Four are legitimate GPT atmosphere work (L13-02, L14-01, L14-02, L16-01).
L07 7-13 is misfiled — it is a diagram, so it is Claude's.

**Housekeeping:** `__pycache__/lesson_inventory.cpython-312.pyc` is committed (logged S86, S91,
still not cleared). `git rm` it. Also `ZUMO_SUPER_BIBLE (1).md` is a stray duplicate in the root.

---

# LESSONS FROM S92

- **AN ASSERT THAT CANNOT FAIL IS NOT EVIDENCE.** "Scheme is the family of record" was validated
  against 142 blocks selected by glyph, which is to say against 142 blocks that could not
  contradict it. Ask what the control WOULD look like if the claim were false; if you cannot
  describe that case, you have not tested anything.
- **WRITE THE GATE TO THE RULING, NOT TO YOUR SWEEP.** Gate 35 was written to the ruling and
  immediately failed on 24 blocks the sweep had never selected. Had it been written to match the
  sweep it would have passed on day one and encoded a false rule permanently. **A gate that
  agrees with the code that produced it tests nothing.**
- **A RULE READ IN PART IS A RULE NOT READ — CONFIRMED AT SCALE.** S91's 69 violations were zero.
  Printing §6.6a whole, to the next section boundary, took one command and dissolved a session's
  worth of work. Do that first, every time.
- **THE PARSER'S OWN WARNINGS APPLY TO YOU.** `lesson_inventory` carries a comment saying glyphs
  are numeric entities in some lessons. My splitter matched `&#` anyway and reported **7 false
  glyph errors where there was 1.** Read the instrument's comments before writing a second one.
- **ASSERTS DO NOT SEE FORMATTING.** The second title element shipped unindented through a
  body-text assert, a data-* assert, an id assert and a div-delta assert. Found by READING the
  output. Also: gate 35 first printed below the suite's closing separator.
- **A FALSE ZERO LOOKS EXACTLY LIKE A CLEAN RESULT.** Calling `LI.inventory()` (which does not
  exist) returned 0 callouts and 0 violations, and the report read like good news. §24.6b again:
  assert the instrument LANDED before believing what it says.
- **A FIELD NAMED `label` NEED NOT CONTAIN A LABEL.** `lesson_inventory`'s `label` over-captures
  body prose, so title-shape questions cannot be answered with it. Two of my early censuses were
  wrong for this reason before I read the extractor.
- **MY OWN REGEX MANUFACTURED A VIOLATION.** L12 1210 `🛑 Note what it does NOT do` was reported
  as a glyph mismatch; "Note" is an imperative verb. The same sentence-subject trap S91 recorded
  for its 22 `<b>` blocks, reproduced one session later in a fresh matcher.
