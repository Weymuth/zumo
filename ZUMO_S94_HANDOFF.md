# ZUMO — S94 HANDOFF (written at S93 close · paste at top of Session 94)

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
   entrypoint — **there is no `inventory()`**.

---

# S93 IS NOT PUSHED AS OF WRITING — live HEAD was `3664bf8`

Everything below is applied and verified **in a local clone**. Confirm by fresh clone before
treating these versions as live. **Push list and the one DELETION are at the bottom.**

---

# READ THIS FIRST — a push deleted a canon entry, and the mechanism is worth keeping

Commit **`3664bf8` "udate"** did two things. The first was right: it deleted the stray
`ZUMO_SUPER_BIBLE (1).md` that S92 had logged as housekeeping. The second was not: the same
commit **overwrote the live `ZUMO_SUPER_BIBLE.md` with that stray's header**, regressing the
version line **v8.79.1 → v8.78** and deleting the entire **v8.79 (S92 Option C)** changelog
entry — the whole record of last session's 250-block sweep.

It was invisible because the two files' bodies were identical; only the header differed. A
`diff` reported one changed line region and nothing else, which reads like a trivial edit.

Recovered byte-exact from `ae31126` before v8.80 was written, so the S92 record is intact.

**A DUPLICATE OF A CANON FILE IS NOT INERT — deleting it and overwriting from it are one hand
movement apart.** Recorded in Bible §26 and in the v8.80 entry.

---

# WHAT SHIPPED IN S93 (locally)

**1. `BookComponentStandard` v01.9.0 → v01.10.0 — GOING DEEPER is the 26th family, bronze.**
A **promotion out of §7.2 Systems at zero new icon cost** — the second instance of the
ENGINEER'S LOG move, on the same test: the nav affordance and the callout name one destination.
Seven edits, diff-audited against a control with nothing else moved. `marks/` **40 → 41**; the
count gate **control-ran FAILING** at *1 would change* before regeneration. New mark carries
**`#725637`**, byte-identical to `stars.svg`, its bronze sibling.

**2. Bible v8.79.1 → v8.80, new §26** — the palette conflict, parked. Plus §26.7, the session's
own lesson.

**3. Census byte-identical at 39,970.** No lesson file was touched. §11 step 5 does not apply.
The seven 🔬 blocks still render slate emoji until the wiring pass.

---

# THE TWO ROWS THAT WERE ASKED FOR AND COULD NOT BE WRITTEN

DJ approved "write the three missing rows (SEE / 🛑 / 🔬)." Only 🔬 was row-shaped. Measured with
`lesson_inventory.build()`, 1,048 callouts across all 18 pages:

**🛑 is not a missing family — it is THE WALL, already row 23.** 19 blocks, two jobs, two reds:

| | blocks | paint | what they say |
|---|---:|---|---|
| L11 ×5 + L12 ×13 | **18** | `#fdecea`/`#e74c3c` | *"a structural limit, not a tuning problem"* · *"A SPIN CANNOT CALIBRATE A GYRO"* |
| L03 937 | **1** | `#f8d7da`/`#c0392b` | *"ALWAYS STOP YOUR MOTORS"* — a real hazard |

The 18 are exactly what S90 created THE WALL for (`bricks`, purple, *"the L11/L12 limit block"*).
They were never repainted because purple is unapproved. **Writing a 🛑 row would put one construct
in the table twice, which §4.1 forbids.**

**SEE cannot name a scheme.** `#d1ecf1`/`#17a2b8` is worn by **51 blocks doing ~20 jobs** — SEE is
22 of them; the other 29 are LEARN ×4, INFO ×3, Real-World Connection ×3, 🏆 ×2, 🧠 ×2, OBJECTIVES,
INSIGHT, 🔮, unit/math notes ×4 and more. Naming it SEE's paint repeats S92's borrowed-paint error
at double the scale.

Two corrections to the S93 handoff's own claims:
- **"zero label edits" is wrong by one** — L07 2669 is title-case `What You Should See`, and it sits
  outside every gate because SEE is not canon yet.
- **`eye` already exists** as the §7.2 prose marker *see*, and §8 records it as deliberately *"freed
  for the see marker."* A new Bootstrap glyph would put two glyphs on one job.

---

# THE RED 21, FULLY RESOLVED INTO TWO GROUPS

- **18 = THE WALL** awaiting approved purple.
- **3 = the retired SAFETY family's orphans**, all on `#c0392b`: L03 937 🛑, L06 624 🚨, L14 1464 ⚠.
  §5.0 records that S91's reassignment covered *"seven SAFETY callouts in L01, L06, L07, L08 and
  L09"* — **L03 and L14 were never in scope.** So *"SAFETY was red's only member"* is false, and
  the fix is two fixes.

---

# §26 — THE PALETTE CONFLICT (PARKED; DO NOT RULE ON IT YET)

`BookComponentStandard` §5.0 and RoboLore `ColorPalette.md` v01.00.00 both define **Heritage Blue**,
disagreeing on **all five hexes**. Four tests favour RoboLore: ten stated contrast ratios reproduce
to **0.02** total error vs the standard's **6.00**; RoboLore's values appear **10–15× across four
upstream documents** and the standard's appear **nowhere** upstream; the standard's own **LOCKED §9**
uses RoboLore's bronze and parchment; and the S91 swap (`c4a90de`) recorded **no rationale** while
every contrast ratio **FELL**. **Gate gap: `gen_component.py` never parses §9.**

**DJ's instinct is that the standard supersedes. NOT SETTLED — his call.** Making it correct requires
writing the rationale plus bumping `ColorPalette.md` and `robolore-colors.css`.

**The semantic three is no longer undefined.** `InstructionalGraphicStandards.md` **v01.00.00
Approved** §7 locks warning gold `#CCA700`, error red `#F44747`, syntax green `#6A9955` — **no
purple** — and its §6 says teaching cards must not be filled or headed with Heritage Blue.

**THE ONE OPEN QUESTION: are the book's callouts "instructional cards" under §6?** If yes, §5's
seven-role Heritage Blue callout scheme is off-canon. Everything else waits on that.

**BLOCKED ON FILING, NOT ON DESIGN.** The approved v01.00.00 sits at `Standards/`; the superseded
v00.90.00 **draft** occupies the canonical path that `CODEX.md` and `VisualIdentity.md` point at. All
of RoboLore is uncommitted, and it is a private repo so a session cannot check the remote.
**S94 first ask: has RoboLore been committed?** If not, do not reopen the colour questions.

---

# OPEN — CARRIED

- **`SEE` / `YOUR TURN` renames** — ruled at S92, still blocked: the standard has no SEE row, and SEE
  has no derivable scheme (above). `✋` remains unused book-wide (0 occurrences).
- **The whole mark library is unwired** — **zero references to `images/icons/` or `images/marks/` in
  any page.** 89 files, none referenced; every live block runs on emoji. This is the single largest
  unstarted item and it is what most "missing construct" findings actually are.
- **📝 does eight jobs across 82 blocks**; `MY PLAN` (20) is OUT of scope — it is the pseudocode step
  with two ends, and the Maker stamps a matching comment block into every generated `main.cpp`
  (L01 excepted). Renaming it breaks book/generator agreement.
- **`WHAT YOU NEED BEFORE STARTING` exists on two glyphs** — 2 on 📝, 2 on 📋.
- **1.0em PARKED** (990 of 1,048 titles at 1.05em).
- **§25.10e is misfiled in the Bible** — it sits at **line 1, above the Bible's own title**, while
  §25.10a–d and §25.10f are in place; §25.10f opens by discussing it. Logged S93, **not moved** —
  relocating canon prose wants a ruling. See §26.6.
- Semantic three unapproved · Heritage Blue renders nowhere · `ZUMO_AMBER_CLASSIFICATION_S91.md`
  (note DJ's S92 definition of Note absorbs REMINDER) · WRITE IT and COMMON PITFALLS are the two
  zero-block repurposing candidates · §9 numbered marks LOCKED · §18.2 mandates
  `raw.githubusercontent.com` while all 223 live image refs use `weymuth.github.io` · two misfiled
  blocks in L12 · 22 sentence-lead `<b>` blocks deliberately not titles.

---

# STANDING QUEUE (carried)

**Difficulty-progression audit** — 2 inversions in 14 transitions, so three specific problems:
**L10→L11 is the real dip** (2.60→2.00) and L11's internal order is `1·2·4·2·1` · **TOUGH used 3
times in 87 challenges** · the **grasp axis is bumpier than the doing axis** (4 vs 2) · L03 and L11
both end easiest-after-hardest. **§6.12a says nothing about ascending difficulty within a lesson —
needs a DJ ruling.**

Challenge-card redesign Part B (~80–100 cards to L06's Goal→Logic→Template pattern) · Maker batch
(bulk starters DL · `?lesson=N` gate · C## labels) · L01 VS Code multi-root step · TDP template v3
(A5 Lab Log) · day-by-day grid + syllabus · L03 open items (1000 ms explainer, modulo explainer, two
Coach's Tips, C01/C05/C06 starter `finished`-payload debt shared with L08/L09/L10) · BC03 weeding
criterion · L16 outside the bonus family (DJ: *"Let's wait."*) · **robot icons §21 still 2 of 5** —
Romi, Balboa, Zircon absent, five regeneration prompts already written · S87's six logged-not-fixed
leads · S86's eight PART-seam readings · §25.6's header example reads `Version 02.7` for L11.

**Image shot list: 21 of 25 outstanding.** Most are DJ-and-a-camera and **must not be AI-generated**.
Four are legitimate GPT atmosphere work (L13-02, L14-01, L14-02, L16-01). L07 7-13 is misfiled — it
is a diagram, so it is Claude's.

**Housekeeping:** `__pycache__/lesson_inventory.cpython-312.pyc` is **cleared** — no longer tracked.
`ZUMO_SUPER_BIBLE (1).md` is **cleared** (that is what `3664bf8` did right). Still in root and
unreferenced by any page: **`ChatGPT Image Jul 29, 2026, 10_20_32 AM.png`** (1.5 MB, 1122×1402, from
S91 `c4a90de`) — needs a DJ ruling to delete. Note §12/§23's "no strays" gate passes with it present,
so its stray check does not reach root non-HTML files.

---

# PUSH LIST — 4 uploads + 1 DELETION

| Action | File | Replaces |
|---|---|---|
| upload | `BookComponentStandard.md` | v01.9.0 → **v01.10.0** |
| upload | `images/marks/file-earmark-plus.svg` | **NEW** (marks/ 40 → 41) |
| upload | `ZUMO_SUPER_BIBLE.md` | v8.78-on-live → **v8.80** (also restores the deleted v8.79 entry) |
| upload | `LIVE_ZUMO_TEXTBOOK.md` | S92 header → S93 |
| **DELETE** | **`ZUMO_S93_HANDOFF.md`** | replaced by `ZUMO_S94_HANDOFF.md` |

**The deletion is the item that gets missed** — it has no file to drag, so nothing prompts it, and
it has now been missed at `fb70426`, at S84, and at S92's first push. §12.2 fails with two handoffs
in root. Push order does not matter here: no lesson references any of these.
