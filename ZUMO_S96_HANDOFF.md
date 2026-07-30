# ZUMO — S96 HANDOFF (written at S95 close · paste at top of Session 96)

## Session open ritual (do this without being asked)
1. `git clone --depth 1 https://github.com/Weymuth/zumo.git`
2. Read `LIVE_ZUMO_TEXTBOOK.md` — verify date / status / versions.
3. `grep -m1 -oE "Bible version: v[0-9.]+" ZUMO_SUPER_BIBLE.md` — **`-m1` matters, the version
   line runs ~99,000 characters.** This is grep's ONE legal use per §24.10.
4. Run: `python3 book_gates.py` · `python3 gen_component.py --selftest` ·
   `python3 lesson_inventory.py` · `python3 lesson_inventory.py --anomalies` ·
   `python3 pill_sweep.py --audit lessons/Lesson_*.html` · `python3 build_family_map.py`
5. **READ THE ANOMALIES LIST ITEM BY ITEM.** Clean apart from the Brain Check family-norm line,
   so any new entry is a real lead.
6. **Every version below is a LEAD. Grep the files. The files win.**
7. Entrypoints are traps: `lesson_inventory.build(path)` — there is no `inventory()`.
   `gen_component.load_standard()` — there is no `parse()`.
8. **Both generators now run from a clean clone with no prior step.** `build_family_map.py` used
   to die on a missing `/tmp/inv.json`; `build_mark_index.py` used to write its output into repo
   root, which is what failed the gate at S95 open. Both fixed. Do not re-introduce either.

---

# STATE

Fresh-clone verified at **`9ba2630`**. **35/35 gates pass.** Census **39,972**.
Bible **v8.82** · `BookComponentStandard` **v01.10.0** · Maker **v2.45.1** ·
`marks/` **41** · `icons/` **48 + LICENSE**.

Instruments: `book_gates` **v1.26.3** (35 gates) · `lesson_inventory` **v1.1.1** ·
`gen_component` **v1.5** (ALL CHECKS PASS) · `pill_sweep` **v1.0** · `gate_payload_match` **v1.6** ·
`build_family_map` **v1.0.1** · `build_mark_index` **v1.0.1** · `gen_bonus_banner` **v1.2** ·
`gen_part_banners` **v1.0** · `going_deeper` **v01.1.1**.

Lessons: L01 **v03.15.0** · L02 **v03.6.0** · L03 **v03.20.0** · L04 **v04.15.0** ·
L05 **v04.15.0** · L06 **v04.19.0** · L07 **v04.15.0** · L08 **v04.14.0** · L09 **v05.12.0** ·
L10 **v02.11.0** · L11 v02.12.0 · L12 v01.14.0 · L13 v02.12.0 · L14 **v02.15.0** ·
L15 v02.11.0 · L16 v02.7.0. *(Eleven lessons moved in S95.)*

Callout schemes **51 → 46** · one-off schemes **12 → 6** · off-canon widths **115 → 114** ·
teal **31 blocks** · LEARN's blue **43**.

---

# THE S95 FINDING — THE INSTRUMENTS WERE WHERE THE DEFECTS WERE

Nothing a student opened was wrong at S95 open, and 35 gates said so. **Two of those gates were
making claims they could not back**, and both were found by chasing one logged anomaly.

**`§5.1 callout title uses the block form` could not see the one violation in the book.**
The idiom was:

```python
off = sum(len(l) + 1 for l in lines[:c['line'] - 1])
gt  = src.find('>', off)
```

It jumped to the start of the callout's line and took the **first `>`**. L14 line 159's
`THE ONE IDEA` shared its line with the `</div>` closing the block above it, so `find('>')`
landed on *that* tag, the check ran one element late, inspected the callout's own `<div` opener
instead of the title inside it, and a bare `<strong>` title passed unseen for sessions.
**The identical idiom was in gate 35 too** — an assert pinned the count at 2 before patching,
because fixing one would have left the other half-blind. Now anchors on `'<' + c['tag']`.

**The control-run took two attempts and the first was worthless.** Run from `/tmp`, the old gate
crashed on `import lesson_inventory` and printed no failure — which reads exactly like a pass.
**An absent FAIL is not a PASS (§24.8).** Re-run in-tree against the same re-seeded defect:
v1.26.2 → `PASS`, v1.26.3 → `FAIL 14 line 159`. That is the proof.

**Every finding shrank when measured.** Three for three this session, four counting S94's phantoms:
- The L14 anomaly was real but **1 block, not a class** of them.
- "Six callouts need normalising" was **one** — the other six were `<p>` and `<details>` callouts
  that start their own lines fine. My test asked "does this line start with `<div`?", which
  conflates *isn't a div* with *shares a line*.
- The "12 one-off schemes" were 12 real schemes but **only 5 were typo-shaped**; the rest each
  folded into a larger paint question.

**Standing lesson for S96: measure the finding before pricing the work, and control-run the
control.**

---

# WHAT SHIPPED IN S95 (nine pushes, every one fresh-clone verified)

1. **Three instrument carry-overs closed.** `build_mark_index.py` landed (v1.0.0 → **v1.0.1**:
   default output moved out of repo root — root was the reintroduction path for the very stray
   that failed the gate at S95 open; also `len(html)` was labelled "bytes" and is now
   `len(html.encode())`). `build_family_map.py` made self-contained (**v1.0.0**, then v1.0.1) —
   it read `/tmp/inv.json` and died on a fresh clone; it now calls `lesson_inventory.build()`
   itself, proven by diffing old-with-JSON against new-without to an empty diff. `.gitignore`
   gained `__pycache__/`, `*.pyc`, and `ZUMO_MARK_INDEX.html`.

2. **Six one-off schemes retired.** L03:1535 `#f0f7f0`→`#eef7f1` · L05:1339 `#e8f3ec`→`#e3f2ed` ·
   L01:1159 `#e0f2f4`→`#d1ecf1` · L08:124 `#fff3cd`→`#fff8e1` · L01:413 `#ffb300`→`#ffc107` ·
   L03:937 `#f8d7da`→`#fdecea`. All byte-neutral.

3. **L01:413 pulled a gate with it.** Snapping to `#ffc107` brought the block into gate 35's
   scope, so `seen` went 250→251 and the coverage assert fired — control-run before the bump.
   Its merged label was split into the canonical `⚠️ WARNING` label + separate title line
   (`Turn Off AI Autocomplete — Yes, Really`), copied from the L01:847/970 pattern.

4. **L03:937 exposed that the repaint and the width debt are coupled.** The geometry gate
   baselines off-canon widths per `(lesson, px, border, bg)`, so repainting any of the 115
   off-canon blocks moves it to a tuple with baseline 0 and reads as NEW debt. **DJ ruling: from
   S95 on, a repaint landing on an off-canon block normalises the width in the same edit.**
   That block went 5px → canon 4px, debt **115 → 114**, and its `GEOM_BASELINE` row was deleted
   because the gate's own shrinkage branch asked for it ("tighten the baseline"). Debt **paid,
   not moved**. The ruling is recorded in `book_gates.py`'s header so a session reads it from
   the file.

5. **TEAL — INSIGHT left the shared blue. DJ ruling.** 31 blocks across 10 lessons to
   `#e9f7f5`/`#2da99d`, hue 174. **18 of them also carried a deep-blue title `#0d47a1`**, moved
   to `#165a53` — a blue title on a teal panel would have undone the split. Bible **v8.81 →
   v8.82**: callout table type 7 split into **7 Learn** / **7a Insight**, and the *second*
   type-7 row (the title-colour table at line 1082, nearly missed) split the same way.
   `build_family_map` **v1.0.1** with the 🔍-on-blue key **replaced, not kept**.

6. **L14:159 fixed** — line split, `<strong>` title → canonical block form byte-copied from the
   L13 sibling. `book_gates` **v1.26.3**.

---

# THE CANON CONFLICT S95 FOUND — READ THIS BEFORE ANY PAINT WORK

**LEARN and INSIGHT were not colliding by accident. Canon put them together.**
`ZUMO_SUPER_BIBLE.md` declared *"Learn / Insight"* as **one type with two glyphs** on one scheme,
while `BookComponentStandard.md`'s roster listed them as **two families with different roles**
(LEARN slate, INSIGHT bronze). The two governing documents disagreed for sessions and nobody
noticed **because the roster renders on zero pixels.** The S94 family map followed the roster,
which is where "one must move" came from.

**Generalise this before the next paint decision:** where the Bible and
`BookComponentStandard` describe the same thing, they have not been diffed. The Bible's KEY TERM
row names `#f3e5f5`/`#9c27b0` (live on **33** blocks) while the dominant KEY TERM scheme is
`#e7d4ff`/`#9b59b6` (**136**). **`BookComponentStandard` records ZERO live callout hexes** — it
governs only the Heritage Blue role layer, which renders nowhere. A systematic diff of the two
documents is unglamorous and is probably the highest-value paint work left.

**§26 STAYS PARKED and needed no ruling.** Because the standard records no live hexes, teal was
not a §5.0 change and invented no Heritage Blue role. The derived-fill route sidesteps §26
entirely — INSIGHT's mark fill derives from `#2da99d` and clears **4.68:1** on its own panel.
Do not reopen §26 until DJ says RoboLore is committed.

---

# STAGE TWO — NOT DONE, NOT A PHANTOM (recorded in the Bible changelog, so it survives)

Three items need DJ meaning calls, not paint:
1. **Two live blocks are labelled `Learn/Insight`** — L03:3636 and L09:1342. They were following
   canon. Each now needs a side.
2. **Bible line 1033** — the Brain Check "Problem-Solving" item names the shared hex pair by hand.
   If Problem-Solving is INSIGHT it moves to teal; if LEARN it stays.
3. **Bible §18's data-type callout** gives LEARN's blue a third job, with a `</>` glyph.

---

# STANDING QUEUE

**Six one-off schemes remain**, and only L11:170 is off-canon (3px `#ccc`, no background — it is a
pull-quote and probably does not belong in the sweep at all). The other five each fold into a
larger question: L02:571 · L04:1827 (WHERE THIS GOES; its nearest neighbour is KEY TERM's
136-block purple, so snapping would paint the wrong family) · L06:1427 (the KEY TERM/MY PLAN
purple) · L07:1928 · L14:1746 (no background).

**Open paint questions unchanged from S94:** KEY TERM spans three purples, `#9b59b6` ×136 /
`#9c27b0` ×33 / `#9b6a9e` ×1, the third being MY PLAN's own colour · **the label convention for
KEY TERM's 184 blocks** (does the label carry the words, or does 🔑 alone identify it once marks
are wired?) — governs more blocks than everything else combined · 46 distinct glyphs, 12 used
once · **the mark library is still entirely unwired**, zero references to `images/marks/` across
all 21 pages.

**`build_family_map.py` does not reproduce `ZUMO_S94_FAMILY_MAP.md`** — generator: 1,033 assigned,
**15 unassigned**, 31 buckets (incl. `(card header)`, not a family), KEY TERM 182 / NOTE 128 /
CHECKPOINT 111. Document: 1,048 / 30 / 184 / 133 / 112. The committed script predates the last
rulings. Closing it means ruling on 15 blocks (L03:3376 🆕 modulo · L03:3434 🧠 scope ·
L07:440 📋 Best Practice · L07:1070 🔍 Header vs Implementation · L08:1584 🎉 Did Your Robot
Wiggle · ten more).

**`§12/§23` globs `**/*.html` only** — a non-HTML root stray is invisible to it, as `gitignore.txt`
demonstrated when it sat in root through a full 35/35 pass. Widen it or log it.

**SCHEDULE — BLOCKED UNTIL ~AUG 24.** DJ does not know which weekdays he teaches until then, and
the grid alternates three periods one week and two the next, so every date downstream waits.
**Course starts Tuesday September 8, 2026** — about five weeks out at S95 close.
**But the syllabus is NOT fully blocked:** seven of its eight open items need no calendar —
battery safety specifics, lab/classroom expectations, academic honesty and working-together
policy, the catch-up path, first-day setup checklist, notebook template link and submission
process. Only the milestone due dates need the schedule. **This is the most student-facing
unblocked work on the queue.** Both documents are working drafts outside the repo.

Also carried: **difficulty-progression audit** (DJ's stated big goal, needs a ruling — §6.12a is
silent on whether difficulty must ascend *within* a lesson; L10→L11 dips 2.60→2.00, L11 runs
`1·2·4·2·1`, TOUGH used in 3 of 87 challenges) · challenge-card redesign Part B (~80–100 cards) ·
Maker batch (bulk starters DL · `?lesson=N` gate · C## labels) · L01 VS Code multi-root step ·
**L03 Coach's Tips** (upload/power-on sequence; AI-autocomplete injects wrong code — small,
unblocked, student-facing) · BC03 weeding criterion · L16 outside the bonus family (DJ: *"Let's
wait."*) · robot icons §21 still 2 of 5 · S87's six logged-not-fixed leads · S86's eight PART-seam
readings · §25.6's header example reads `Version 02.7` for L11 · **§25.10e is misfiled**, line 1
of the Bible above its own title.

**Image shot list: 21 of 25 outstanding.** Most are DJ-and-a-camera and must not be AI-generated.
Four are legitimate GPT atmosphere work (L13-02, L14-01, L14-02, L16-01). L07 7-13 is a diagram,
so it is Claude's.

**Bench (need the robot):** Q017 L09 six numbers · Q044 calibration-spin · Q046 gyro-bias ·
L02 §5 green-LED · Constrain RUN_MS.

---

# ON HOW S95 WENT

DJ said mid-session it felt like little got done. The clock says otherwise — **first commit 08:00,
last 09:27, nine pushes, all clone-verified.** But he was right about the part that matters:
**nothing shipped tonight teaches a student anything new.** Teal renders, unlike S94's 89
unreferenced assets, but it fixes nothing a student would have noticed. The one genuinely
student-facing repair was L14's malformed title.

**Five weeks to September 8.** The two documents a classroom actually needs on day one — the
syllabus and the grid — are still drafts outside the repo. If S96 wants something a student will
read, the syllabus's seven calendar-independent items and the L03 Coach's Tips are the candidates
that need nothing from anyone else.

---

# PUSH LIST

| Action | File | Note |
|---|---|---|
| upload | `LIVE_ZUMO_TEXTBOOK.md` | regenerated at S95 close, versions grepped from the files |
| upload | `ZUMO_S96_HANDOFF.md` | this file |
| **delete** | `ZUMO_S95_HANDOFF.md` | §12.2 — exactly one handoff in root, gate 28 enforces it |

⚠️ **Deletions appear as checkboxes in GitHub Desktop's Changes list and are easy to miss.**
There is one here. Verify by fresh clone and confirm `book_gates.py` still returns **35/35**.
