# ZUMO — S95 HANDOFF (written at S94 close · paste at top of Session 95)

## Session open ritual (do this without being asked)
1. `git clone --depth 1 https://github.com/Weymuth/zumo.git`
2. Read `LIVE_ZUMO_TEXTBOOK.md` — verify date / status / versions.
3. `grep -m1 -oE "Bible version: v[0-9.]+" ZUMO_SUPER_BIBLE.md` — **`-m1` matters, the version
   line runs ~99,000 characters.** This is grep's ONE legal use per §24.10.
4. Run: `python3 book_gates.py` · `python3 gen_component.py --selftest` ·
   `python3 lesson_inventory.py` · `python3 lesson_inventory.py --anomalies` ·
   `python3 pill_sweep.py --audit lessons/Lesson_*.html` · `python3 build_family_map.py`
5. **READ THE ANOMALIES LIST ITEM BY ITEM.** It is now clean apart from the Brain Check family-norm
   line, so **any new entry in it is a real lead.** That was not true before S94.
6. **Every version below is a LEAD. Grep the files. The files win.**
7. Entrypoints are traps: `lesson_inventory.build(path)` — there is no `inventory()`.
   `gen_component.load_standard()` — there is no `parse()`.

---

# ⚠️ FIRST JOB — ONE GATE IS FAILING

**`ZUMO_MARK_INDEX.html` sits in repo root and `§12/§23 site layout` FAILS on it:**
`STRAY page: ZUMO_MARK_INDEX.html (not a canonical location)`. The book is **34/35**, not 35/35.

It is a workshop reference sheet, not a book page, and in root it is also published at
`weymuth.github.io/zumo/ZUMO_MARK_INDEX.html` where a student can reach it.

**Fix: delete it from root.** `build_mark_index.py` regenerates it from `images/marks/` in seconds —
that is why it was written as a generator. If DJ wants it committed instead, it needs a
non-published home **and** a §12/§23 canon entry; that is a Bible change, not a file move.

**`build_mark_index.py` is not in the repo yet.** Land it in the same push.

---

# STATE

Fresh-clone verified at **`b2ee980`**. Bible **v8.81** · `BookComponentStandard` **v01.10.0** ·
Maker **v2.45.1** · census **39,970** · `marks/` **41** · `icons/` **48 + LICENSE**.

Instruments: `book_gates` **v1.26** (35 gates, **34 passing — see above**) ·
`lesson_inventory` **v1.1.1** · `gen_component` (selftest ALL CHECKS PASS) · `pill_sweep` **v1.0** ·
`gate_payload_match` **v1.6** · `gen_bonus_banner` **v1.2** · `gen_part_banners` **v1.0** ·
`build_family_map.py` (new, no version string yet — give it one).

Lessons unchanged this session: L01 v03.14.0 · L02 v03.5.0 · L03 v03.19.0 · L04 v04.14.0 ·
L05 v04.14.0 · L06 v04.18.0 · L07 v04.14.0 · L08 v04.13.0 · L09 v05.11.0 · L10 v02.10.0 ·
L11 v02.12.0 · L12 v01.14.0 · L13 v02.12.0 · L14 v02.14.0 · L15 v02.11.0 · L16 v02.7.0.

**No lesson file was touched in S94.** Everything shipped was an instrument, a document, or a ruling.

---

# WHAT SHIPPED IN S94

1. **`lesson_inventory.py` v1.1.0 → v1.1.1.** The visible-banner expectation was still the pre-S89
   value of **2**, so `--anomalies` printed a false lead for **all sixteen** lessons while §5b and the
   gate have required exactly **ONE** since S89. Corrected 2 → 1, **control-run first** by seeding a
   real second banner into a throwaway copy and confirming the check fired. The anomalies list now
   holds one informational line, which is what makes rule 5 above meaningful.

2. **`ZUMO_TDP_Template.md` v2 → v3 — A5 Lab Log added.** The syllabus grades **Outside Work at 5%**
   on a log the template gave students nowhere to record. A5 is date · in · out · what I worked on,
   eight seeded rows, running total, plus the assembly-checklist line. Four assert-guarded edits, all
   `count==1`; diff against v2 was **+24 / −3** lines, all three removals intentional.
   **`ZUMO_TDP_Template_v2.md` has been deleted** — the filename carries the version here, so v3 did
   not overwrite v2 and two student-facing templates briefly coexisted.

3. **`ZUMO_S94_FAMILY_MAP.md` — all 1,048 callout blocks assigned to 30 families.** Reproducible via
   `build_family_map.py`. Nine new rows required; four roster families that had **zero** blocks now
   have work (IF YOU'RE STUCK 0→9 · GOING DEEPER 0→7 · HOW THIS SECTION WORKS 0→2 ·
   COMMON PITFALLS 0→1). The card header stays a §7.2 supporting mark, not a family.

4. **`ZUMO_S94_FAMILY_RULINGS.md`** — every ruling with who made it and why.

---

# THE ENTITY LESSON, AGAIN — THIS TIME AGAINST MY OWN ANALYSIS

**`ENGINEER'S LOG` was reported as ZERO blocks. It has 17.** The labels carry `&rsquo;`, not a
straight apostrophe, so the matcher missed every one. This is **§24.11 verbatim — an entity is not
the character it encodes** — and it was committed by the analysis, not the book, eleven sessions
after the same mistake shipped a live L12 regression.

**Any future label matching MUST `html.unescape()` twice and normalise `\u2019` → `'` before
comparing.** `build_family_map.py` does this; anything new must too.

Three further corrections against S94's own earlier numbers, all logged in the map:
- **"5 collisions / 121 repaints" is VOID** — computed pre-entity-fix. Must be recomputed.
- **`WHAT YOU NEED` was reported as 6 blocks. It has 13**, across four schemes and two glyphs.
- **"104 blocks remaining" understated the job.** 420 blocks lacked a family label; the 104 were
  only those on schemes where *nothing at all* matched.

---

# THREE PHANTOM QUEUE ITEMS CLOSED

All three had been carried for many sessions on premises that were simply false:

1. **L03/L08/L09/L10 `finished`-payload debt.** All four lessons **have** a `finished` payload, every
   challenge row resolves, labels honestly read *"(finished preload)"*, and the Maker changelog
   records **DJ's own S49 ruling that C01–C06 stay finished-preload.** Not a defect. What remains is
   a design question — should challenge downloads be whole-template starters per §18.3? — and
   answering "yes" means **authoring ~24 new payloads.**
2. **L03 "1000 ms = 1 second" explainer.** Already written and live: *"Every timing number in this
   lesson is in milliseconds (ms) — thousandths of a second. So 1000 ms = 1 second."*
3. **L03 modulo explainer.** Already written and live: *"New operator: % (modulo) — the % operator
   gives you the remainder of a division, not the divide itself. 7 % 3 is 1."*

**Before doing any queue item, verify it still exists.** Three of them did not.

---

# PAINT — NOTHING DECIDED, AND THAT WAS DELIBERATE

Naming is complete. Colour is not. **These were not invented at hour thirteen of a session where
two prior sweeps each shipped a regression.**

1. **LEARN and INSIGHT both sit dominant on `#e3f2fd`/`#2196f3`.** One must move. Near-identical
   cost either way (37 vs 38 blocks), so it is a meaning call, not arithmetic.
2. **KEY TERM spans three purples** — `#9b59b6` ×136, `#9c27b0` ×33, `#9b6a9e` ×1 — and the third is
   **MY PLAN's own colour**, so a KEY TERM block and a MY PLAN block already share paint.
3. **12 of the 51 schemes are one-offs**, several one hex from a neighbour: `#ffb300` vs `#ffc107`,
   `#fff9e6` vs `#fef9e7`, `#e8f3ec` vs `#e3f2ed`. Those look like typos, and they are the safest
   possible first repaint batch — 12 blocks, proves the method before touching anything with 136.
4. **46 distinct glyphs book-wide, 12 used exactly once**: 🔎 🍽 📐 🔋 📚 🔢 📏 🆕 ≈ 🍳 🎉 🔌.
5. **THE BIG ONE — the label convention for KEY TERM's 184 blocks.** Does the label carry the words
   "KEY TERM", or does the 🔑 mark alone identify the family once marks are wired? **Governs more
   blocks than every other open question combined.**

## The measured facts the paint decisions rest on

- **51 distinct bg/border schemes · 32 distinct border colours · for 30 families.** Top 10 schemes
  cover 72% of blocks; 12 are used exactly once.
- **The mark library is still entirely unwired** — parsed every attribute of every element across
  all 21 pages: **zero** references to `images/marks/` or `images/icons/`, against a control of 196
  other `images/` references. 89 SVGs, none used. Every live block runs on emoji.
- **Every generated mark's baked fill disagrees with its family's live paint.** Worst: INSIGHT's
  bronze `#725637` mark against a blue `#2196f3` callout. The marks were coloured for Heritage Blue
  role colours that **render nowhere in the book.**
- **The route that needs no §26 ruling:** derive each mark's fill from that family's own border hue,
  darkened until it clears 4.5:1 against its own panel. All 14 tested families clear it, no new hue
  is invented, and marks can then ship as plain `<img src>` with no inline-SVG byte cost. A rendered
  14-family preview was approved by DJ in S94.

---

# §26 — STILL PARKED. DO NOT REOPEN.

**RoboLore has not changed since DJ handed over the zip. It is uncommitted, and it is private, so a
session cannot check the remote.** A §26 ruling would be made against a document that cannot be
cited. Do not reopen the colour questions until DJ says RoboLore is committed.

The **derived-fill route above sidesteps §26 entirely**, which is why it is the recommended path.

---

# STANDING QUEUE (carried, minus the three phantoms)

**Difficulty-progression audit** — DJ's stated big goal, and **it needs a ruling before it can
proceed**: §6.12a says nothing about whether difficulty must ascend *within* a lesson. Findings
already computed: **L10→L11 dips 2.60→2.00** · L11's internal order runs `1·2·4·2·1` · **TOUGH used
in only 3 of 87 challenges** · the grasp axis is bumpier than the doing axis (4 vs 2) · L03 and L11
both end easiest-after-hardest.

**Syllabus + day-by-day grid** — the only presentation-facing documents still unbuilt, and both are
working drafts **outside the repo**. The grid is still in relative time. **Course starts Tuesday
September 8, 2026** (day after Labor Day). **BLOCKED: DJ does not yet know which weekdays he
teaches** — the grid alternates three periods one week, two the next, and every date downstream
depends on that pattern.

Also carried: challenge-card redesign Part B (~80–100 cards to L06's Goal→Logic→Template pattern) ·
Maker batch (bulk starters DL · `?lesson=N` gate · C## labels) · L01 VS Code multi-root step ·
L03 Coach's Tips (upload/power-on sequence; AI-autocomplete injects wrong code) · BC03 weeding
criterion · L16 outside the bonus family (DJ: *"Let's wait."*) · **robot icons §21 still 2 of 5**
(Romi, Balboa, Zircon absent; five regeneration prompts already written) · S87's six
logged-not-fixed leads · S86's eight PART-seam readings · §25.6's header example reads
`Version 02.7` for L11 · **§25.10e is misfiled** — line 1 of the Bible, above its own title, while
§25.10a–d and §25.10f are in place and §25.10f opens by discussing it (wants a ruling, see §26.6).

**Image shot list: 21 of 25 outstanding.** Most are DJ-and-a-camera and **must not be AI-generated**.
Four are legitimate GPT atmosphere work (L13-02, L14-01, L14-02, L16-01). L07 7-13 is misfiled — it
is a diagram, so it is Claude's.

**Bench (need the robot):** Q017 L09 six numbers · Q044 calibration-spin · Q046 gyro-bias ·
L02 §5 green-LED · Constrain RUN_MS.

**One real anomaly logged, not chased:** **L14 line 159's `THE ONE IDEA` block extracted empty**
while its L13 sibling read fine. Either the block is malformed or the extractor lost it — worth a
look either way.

---

# ON HOW S94 WENT — WORTH READING BEFORE PLANNING S95

DJ worked 12+ hours and said, correctly, that he was seeing little progress. The diagnosis: the
palette-and-icon work generates its own next task and **none of it reaches a student.** 89 generated
assets referenced nowhere; a 26-family roster the book agreed with 58% of the time; a palette
rendering on zero pixels. Meanwhile **nothing a student opens is wrong** — 35 gates were passing,
zero malformed tags, zero broken images, payloads byte-matched.

DJ ruled explicitly that the colour and icon work continues and is not to be deferred. That ruling
stands. But **the naming phase is now finished**, and the remaining paint work is bounded and
measured rather than open-ended — which it was not at S94 open.

**If DJ asks what to do next and wants something a student will see**, the candidates are the
difficulty audit (needs his ruling), the syllabus and grid (needs his teaching days), and the L03
Coach's Tips. The repaint is the biggest visible change and the safest first batch is the 12 one-off
typo schemes.

---

# PUSH LIST

| Action | File | Note |
|---|---|---|
| **delete** | `ZUMO_MARK_INDEX.html` | **root stray — this is what is failing the gate** |
| upload | `build_mark_index.py` | regenerates the index; not in the repo yet |
| upload | `LIVE_ZUMO_TEXTBOOK.md` | regenerated at S94 close, versions grepped from the files |
| upload | `ZUMO_S95_HANDOFF.md` | this file |
| **delete** | `ZUMO_S94_HANDOFF.md` | §12.2 — exactly one handoff in root |

⚠️ **Deletions appear as checkboxes in GitHub Desktop's Changes list and are easy to miss.** There
are two here. Verify by fresh clone, and confirm `book_gates.py` returns **35/35** afterwards — that
is the check that the stray is really gone.
