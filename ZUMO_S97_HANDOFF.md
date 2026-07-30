# ZUMO — S97 HANDOFF (written at S96 close · paste at top of Session 97)

## Session open ritual (do this without being asked)
1. `git clone --depth 1 https://github.com/Weymuth/zumo.git`
2. Read `LIVE_ZUMO_TEXTBOOK.md` — verify date / status / versions.
3. `grep -m1 -oE "Bible version: v[0-9.]+" ZUMO_SUPER_BIBLE.md` — **`-m1` matters, the version
   line runs ~99,000 characters.** This is grep's ONE legal use per §24.10.
4. Run: `python3 book_gates.py` · `python3 gen_component.py --selftest` ·
   `python3 lesson_inventory.py` · `python3 lesson_inventory.py --anomalies` ·
   `python3 pill_sweep.py --audit lessons/Lesson_*.html` · `python3 build_family_map.py` ·
   `python3 session_versions.py --selftest` then `python3 session_versions.py`
5. **READ THE ANOMALIES LIST ITEM BY ITEM.** Clean apart from the Brain Check family-norm line,
   so any new entry is a real lead.
6. **Do not hand-type a version.** `session_versions.py --live` and `--handoff` EMIT the blocks
   that LIVE.md and this file use, read from each file's one home. Generated text cannot drift.
7. Entrypoints are traps: `lesson_inventory.build(path)` — there is no `inventory()`.
   `gen_component.load_standard()` — there is no `parse()`.
8. **`build_family_map.py` now reproduces the map document exactly.** If it does not, something
   moved — and the way to tell is a per-family diff, NOT the assigned total. See below.

---

# STATE

Fresh-clone verified at **`298c508`**. Census **39,972**.
Bible **v8.82** · `BookComponentStandard` **v01.10.0** · Maker **v2.45.1** ·
`marks/` **41** · `icons/` **49** incl. LICENSE.

Instruments: `book_gates` **v1.27.1** · `lesson_inventory` **v1.1.1** ·
`gen_component` **v1.5** · `pill_sweep` **v1.0** · `gate_payload_match` **v1.6** ·
`build_family_map` **v1.1.2** · `build_mark_index` **v1.0.2** · `gen_bonus_banner` **v1.2.1** ·
`gen_part_banners` **v1.0** · `going_deeper` **v01.1.1**.

Lessons: L01 v03.15.0 · L02 v03.6.0 · L03 v03.20.0 · L04 v04.15.0 · L05 v04.15.0 · L06 v04.19.1 · L07 v04.15.0 · L08 v04.14.0 · L09 v05.12.0 · L10 v02.11.0 · L11 v02.12.0 · L12 v01.14.0 · L13 v02.12.0 · L14 v02.15.0 · L15 v02.11.1 · L16 v02.7.0.

Family map: **1,048 / 1,048 assigned · 0 unassigned · 30 families** — generator and document
agree row-for-row.

---

# THE S96 FINDING — A CLEAN TOTAL IS NOT A CLEAN RESULT

The 15 unassigned blocks were closed and the generator now reproduces `ZUMO_FAMILY_MAP.md`. The
part worth carrying is how it was checked.

After encoding the rulings, the script reported `assigned 1048 / 1048`, `unassigned 0`,
`families 30`. Every number a person would look at was correct. **Then one ruling was
deliberately misrouted** — `Did Your Robot Wiggle` sent to WARNING instead of CHECKPOINT — and
re-run:

```
assigned 1048 / 1048   families 30   UNASSIGNED: 0     <-- unchanged
CHECKPOINT   doc=112  gen=111
WARNING      doc=80   gen=81                            <-- only the per-family diff saw it
```

**A block moving between families does not change the sum.** The total is structurally blind to
the exact defect it looks like it would catch. Any future gate on this data must compare rows.
Had the check stopped at the total, S96 would have repeated S95's mistake — an instrument
reporting a pass it could not back.

**Three of the five verifications were the ones that did work:** that the edit landed, that every
family row matched the document, and that only the nine ruled families moved and by exactly the
ruled amounts. B (totals) proved nothing.

---

# WHAT SHIPPED IN S96 (five pushes, every one fresh-clone verified by md5)

1. **`ZUMO_Syllabus_WORKING.md` — the seven calendar-independent sections** (`7436d17`).
   6,758 → 14,825 bytes, 130 → 266 lines, `Still To Add` 8 items → 4. Zero original sections
   lost — asserted by heading-set diff, not assumed. Battery safety from Bible §13 + the motor
   card; academic-honesty AI section from `TEACHER_NOTE_AI_tools.md`'s documented injections
   (`setMotorPower()`, `set motorSpeed()`, `@^1.3.0`) and L01 §3.1; day-one checklist from the
   grid's Pd 1 and L01's own preflight; notebook/submission from `ZUMO_TDP_Template_v3.md`.
   **DJ has not read `In the Lab` yet** — it is the one section with zero repo backing, written
   from course structure and shop practice. Everything else traces to canon.
   The file also carries the project's first `.md` version line (`v1.0`, two homes: HTML comment
   line 3 + footer). That is a NEW convention for a root `.md` and nothing governs it.

2. **`build_family_map.py` v1.0.1 → v1.1.1** (`1b86d2c`, then `80721d7`).
   **v1.0.2 — the apostrophe root cause.** `norm()` folds `\u2019` on the INPUT side, and CANON
   is written straight, but the glyph+scheme fallback map hardcoded its OUTPUT values curly
   (`'ENGINEER\u2019S LOG'` at two places). Map values never pass back through `norm()`, so the
   one header-less block resolving by scheme landed in a bucket of its own: 16 + 1 instead of 17,
   31 families instead of 30. Control-run: only the two ENGINEER rows and the family count moved.
   That block turned out to be L07:3645.
   **v1.1.0 — the 15 rulings encoded.** Matched on label PREFIX, never line number, so an edit
   above a block cannot silently break its ruling.
   **v1.1.1 — reference renamed.**

3. **`ZUMO_S94_FAMILY_MAP.md` → `ZUMO_FAMILY_MAP.md`** (`4693c2f`, `80721d7`). Regenerated: the
   table is emitted from the generator's own run, not retyped, then re-parsed from disk and
   re-compared. Now records all 15 rulings block-by-block with their basis, how the LEARN/INSIGHT
   trio was settled, the struck-through paint items, and the instrument corrections. Renamed
   undated because it is maintained, not a session artifact. **The rename's deletion landed** —
   verified by fresh clone, old filename absent.

---

# HOW THE 15 WERE CLOSED — THE METHOD IS REUSABLE

Nobody had to read 15 blocks and argue 15 times. **The per-family shortfalls between the
generator and the document summed to exactly 15**, which recovered the target histogram before a
single block was examined. That turned "rule 15 blocks" into "find the assignment consistent with
a known histogram," and most rows fell out:

- **Two were forced by arithmetic** — HOW THIS SECTION WORKS and the second KEY TERM slot each
  had exactly one plausible block.
- **Three were settled by glyph canon.** The Bible's post-S95 split assigns **📖 LEARN** and
  **🔍 INSIGHT** (type 7 / 7a). Of the three blocks competing for those two slots, two matched
  their glyph exactly and the third (🧠) carried a glyph belonging to neither — so the third was
  the one that had to leave the pair. DJ ruled it NOTE.
- **The histogram out-predicted Claude twice.** It correctly refused `Why Today's Work Matters →
  WHERE THIS GOES` (that family had no slot), and the block it forced into NOTE turned out to be
  the very block exposing the apostrophe bug.

**Weakest link, flagged in the document itself:** `L03:3434` 🧠 Watch your scope → NOTE. It fits,
but it landed there partly as the block left standing.

---

# PHANTOMS — NOW SIX IN THREE SESSIONS, AND IT IS A PATTERN

**L03 Coach's Tips closed with zero edits.** Both already live:
- *setup() fires once at power-on* — live as a 💡 TIP in L03 (upload, then power-on; loop() takes
  over; a program with motor commands in setup() drives immediately).
- *AI autocomplete injects wrong code* — live as a ⚠️ WARNING in L03, with the Command Palette
  "Disable AI Features (Workspace)" fix in L01.

**And the queue item named a component that no longer exists.** "Coach" appears 4 times
book-wide, none a callout family — an L03 prose line, an L05 analogy, an L14 metaphor, and in
L02 an **HTML comment recording that an INSIGHT callout replaced an old "Coach's Note."** The
family was retired and the queue kept carrying work addressed to it.

**Standing rule for S97: before scheduling a queue item that names a component, verify the
component is live.** Three phantoms fell in S94, three findings shrank in S95, two more fell here.

---

# STANDING QUEUE

**Syllabus — four items left**, and three are one sentence from DJ: milestone due dates (the only
calendar-blocked one), the TDP template Google Doc link, battery charging location and charge
time, late-milestone penalty amount. **DJ still owes `In the Lab` a read.**

**The teacher grid is still a draft outside the repo** — the syllabus is now in; the grid is not.

**SCHEDULE — BLOCKED UNTIL ~AUG 24.** DJ does not know which weekdays he teaches; the grid
alternates three periods one week and two the next. **Course starts Tuesday September 8, 2026 —
about five and a half weeks out at S96 close.**

**Paint, unchanged:** KEY TERM spans three purples (`#9b59b6` ×136 / `#9c27b0` ×33 / `#9b6a9e` ×1,
the third being MY PLAN's own colour) · **the label convention for KEY TERM's 184 blocks** —
does the label carry the words, or does 🔑 alone identify it once marks are wired? governs more
blocks than everything else combined · six one-off schemes remain, only L11:170 off-canon (a
pull-quote that probably does not belong in the sweep) · 46 distinct glyphs, 12 used once ·
**the mark library is still entirely unwired**, zero references to `images/marks/` across all 21
pages.

**The highest-value paint work is still the diff nobody has done:** where the Bible and
`BookComponentStandard` describe the same thing they have never been compared.
`BookComponentStandard` records **zero** live callout hexes — it governs only the Heritage Blue
role layer, which renders nowhere. §26 STAYS PARKED until DJ says RoboLore is committed.

**Stage Two (from S95, still open, still not a phantom):** two live blocks labelled
`Learn/Insight` (L03:3636, L09:1342) each need a side · Bible line 1033's Brain Check
"Problem-Solving" item names the shared hex pair by hand · Bible §18's data-type callout gives
LEARN's blue a third job.

**`§12/§23` globs `**/*.html` only** — a non-HTML root stray is invisible to it. This bit twice
now: `gitignore.txt` sat in root through a full 35/35 pass, and **nothing would have caught the
rename leaving both filenames in place.** Widen it or log it. Note the syllabus and the family
map are both root `.md` files governed by no gate at all.

**`ZUMO_S96_HANDOFF.md` is deleted with this push** — its line 170 claimed the generator does not
reproduce the map, which S96 resolved.

Also carried: **difficulty-progression audit** (DJ's stated big goal, needs a ruling — §6.12a is
silent on whether difficulty must ascend *within* a lesson; L10→L11 dips 2.60→2.00, L11 runs
`1·2·4·2·1`, TOUGH used in 3 of 87 challenges) · challenge-card redesign Part B (~80–100 cards) ·
Maker batch (bulk starters DL · `?lesson=N` gate · C## labels) · L01 VS Code multi-root step ·
BC03 weeding criterion · L16 outside the bonus family (DJ: *"Let's wait."*) · robot icons §21
still 2 of 5 · S87's six logged-not-fixed leads · S86's eight PART-seam readings · §25.6's header
example reads `Version 02.7` for L11 · **§25.10e is misfiled**, line 1 of the Bible above its own
title · **9 new roster rows still not activated in `BookComponentStandard.md`.**

**Image shot list: 21 of 25 outstanding.** Most are DJ-and-a-camera and must not be AI-generated.
Four are legitimate GPT atmosphere work (L13-02, L14-01, L14-02, L16-01). L07 7-13 is a diagram,
so it is Claude's.

**Bench (need the robot):** Q017 L09 six numbers · Q044 calibration-spin · Q046 gyro-bias ·
L02 §5 green-LED · Constrain RUN_MS.

---

# ON HOW S96 WENT

**Something a student reads shipped.** That was the explicit ask coming out of S95, and the
syllabus went from eight open items to four with six of seven new sections traceable to repo
canon rather than invented. That is the difference from S95, where the honest verdict was that
nothing shipped taught a student anything.

The instrument work was real too, but note what it cost: **two of the four items worked this
session turned out to need no edit at all.** The L03 Coach's Tips were already written, and the
"31 buckets vs 30" was one hardcoded apostrophe. The pattern across three sessions is
unmistakable — **findings shrink when measured, and queue items decay.** The queue is now the
least reliable document in the project.

**Five and a half weeks to September 8.** The syllabus is in the repo. The grid is not.

---


# S96 LATE WORK — `session_versions.py`, AND WHY IT EXISTS

**Three false alarms in one close-out, all the same shape:** an unanchored search over a whole
file whose hit count was then treated as a fact. A Bible regex matched historical per-session
blocks; a scan for `**Versions:**` found a second, legitimate, pre-existing line in an S64 block;
a substring test missed a name written in backticks. **None was a defect in the book.** All were
grep; none was a read-through. The one check that never misfired was anchored to a position
(`lines[5]`) rather than searching for text.

**`session_versions.py` v1.2** reads all 14 artefacts + 16 lessons, each from ONE home in a
bounded header window, and asserts the pattern matches **exactly once** — zero or two is a hard
error naming the file, never a silent value. It then EMITS the LIVE.md Versions line and this
STATE block, so the two cannot disagree. Version drift stops being detected and becomes
impossible.

**It also enforces §5b for the first time.** Every lesson's hidden comment and visible banner are
read and required to agree; a disagreement is a hard error. That rule existed on paper and
nothing checked it.

**`--check` is the only comparison anyone should write.** It compares LIVE.md and the
handoff against the files and **normalises the commit sha away — the sha is not a version, and
LIVE.md can never name the commit that contains LIVE.md.** A naive hand-comparison always differs
by that one field and reads as a defect; that happened once, immediately, on this close-out. Every
ad-hoc comparison written in a shell during S96 produced a false alarm. This one is written once
and control-run.

**`--selftest` controls in BOTH directions.** §24.8 is normally asked one way — *would this look
different if the answer were the opposite?* — which catches a false PASS. The mirror, *if there
were no defect, would this say so?*, catches a false FAIL and is what all three S96 alarms needed.
All three controls pass. Building it hit both failure modes: a latent unbounded recursion (the control
spawned itself), and a control that **read the clean tree instead of the corrupted copy** because
`ROOT` derives from `__file__`, not `cwd` — the same shape as S95's worthless first control run.
**Verify the instrument is pointed where you think it is.**

## Version homes — four normalised, five to go (S97)

Nine scripts carried their version in six different shapes. Four now use the canonical home,
the one `gen_component.py` already documented as *"the only version home in this file"*:

```python
VERSION = 'v1.27.1'   # the only version home in this file
```

Done: `book_gates` **v1.27.1** · `build_family_map` **v1.1.2** · `build_mark_index` **v1.0.2** ·
`gen_bonus_banner` **v1.2.1**. Their four bespoke regexes in `session_versions.py` collapsed to
one rule. Behaviour-neutral: 35/35 gates, `build_mark_index` still emits 41 marks at 34,617 bytes.

**Remaining for S97:** `lesson_inventory` · `pill_sweep` · `gate_payload_match` ·
`gen_part_banners`. Each is the same edit: add the constant, strip the version from the header
line, bump, collapse its regex. **`pill_sweep` and `gen_part_banners` have no selftest of their
own**, so verify them by running and diffing output, not by assuming.

Leave the `.md`/`.html` homes alone — `<!-- Name version: vX -->` is §5b's own convention and the
gate reads it.

**Honest note on value:** normalising was load-bearing before `session_versions.py` existed and is
cosmetic after it. The residual benefit is that the reader's bespoke-regex table shrinks, and a
tenth script cannot invent a seventh shape.

---

# PUSH LIST

| Action | File | Note |
|---|---|---|
| upload | `LIVE_ZUMO_TEXTBOOK.md` | regenerated at S96 close, versions grepped from the files |
| upload | `ZUMO_S97_HANDOFF.md` | this file |
| **delete** | `ZUMO_S96_HANDOFF.md` | §12.2 — exactly one handoff in root, gate 28 enforces it |

⚠️ **Deletions appear as checkboxes in GitHub Desktop's Changes list and are easy to miss.**
There is one here. Verify by fresh clone and confirm `book_gates.py` still returns **35/35**.
