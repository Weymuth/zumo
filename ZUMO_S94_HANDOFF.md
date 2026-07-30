# ZUMO — S94 HANDOFF (rewritten at S93 close, after the triple-check · paste at top of Session 94)

## Session open ritual (do this without being asked)
1. `git clone --depth 1 https://github.com/Weymuth/zumo.git`
2. Read `LIVE_ZUMO_TEXTBOOK.md` — verify date / status / versions.
3. `grep -m1 -oE "Bible version: v[0-9.]+" ZUMO_SUPER_BIBLE.md` — **`-m1` matters, the version
   line runs ~99,000 characters.** This is grep's ONE legal use per §24.10.
4. `python3 book_gates.py` · `python3 gen_component.py --selftest` ·
   `python3 lesson_inventory.py` · `python3 lesson_inventory.py --schemes` ·
   `python3 lesson_inventory.py --anomalies` · `python3 pill_sweep.py --audit lessons/Lesson_*.html`
5. **READ THE ANOMALIES LIST ITEM BY ITEM.** Do not scan it for the word FAIL. It printed two real
   live defects for two sessions and nobody read them — see §24.11 and the section below.
6. **Every version below is a LEAD. Grep the files. The files win.**
7. §24.10: the parser is the default instrument. `lesson_inventory.build(path)` is the entrypoint —
   **there is no `inventory()`**. `gen_component`'s entrypoint is **`load_standard()`** — there is no
   `parse()`; S93 guessed and got a `NoneType` before asserting the instrument had landed.

---

# STATE — batch 1 pushed and verified, batch 2 in DJ's hands

**Batch 1 is live at `b0489a0`**, fresh-clone verified: all five files byte-identical, `ZUMO_S93_HANDOFF.md`
deleted, §12.2 satisfied, 35/35 gates.

**Batch 2 (the two regression fixes) is NOT pushed as of writing.** Push list at the bottom.

---

# READ THIS FIRST — the anomalies list was right for two sessions and nobody read it

The S93 triple-check found **two real defects live on the site**, both of which **all 35 gates passed
over**, and both of which `lesson_inventory --anomalies` had been printing the whole time as
`unclosed <wire.h>` and `unclosed <strong>`.

**1. L12 lines 594 and 774 — `<Wire.h>` unescaped.** The browser tokenises it as an unknown element,
so the sentence rendered **"The #include  goes at the TOP of the file."** with the filename gone.
Escaped at S87, S89, S91 and `03d1e85`; **raw from `514588e`, the S92 Option C push.** That makes it
**v8.67's defect, same lesson, same sentence, eleven sessions later** — caused by the sweep's own
approved principle of *authoring the string literally*. **An entity is not the character it encodes.**

**2. L04 line 1363 — crossed tags, from a different sweep.** The block-form title conversion at
`53a44b6` (S91) closed the **inner** `</strong>` with `</div>`, so the deadband subtitle rendered
outside its own title element and unbolded.

**Both fixed. Class-swept by PARSE, not grep** — every start-tag that is not a real HTML element,
across all 21 pages: **2 before, 0 after.** Canonized as **§24.11**.

## And the stale expectation that gave them cover

The same anomalies list prints **`1 visible banner(s), expected 2` for all sixteen lessons**, because
`lesson_inventory` still carries the pre-S89 two-banner rule while §5b and the gate have required
exactly **ONE** visible banner since the build banner was deleted at S89. Sixteen identical false
leads trained the eye to skip the block that also held the two real ones.

**A uniform anomaly across every file is a lead about the INSTRUMENT, not the book (§24.8) — and a
false lead is not free: it buys cover for the true ones sitting beside it.**

**S94 JOB, SMALL AND WORTH DOING FIRST: correct `lesson_inventory`'s banner expectation from 2 to 1.**
Deliberately not done at S93 — changing an instrument mid-verification invalidates the verification.
After that the anomalies list should hold only the Brain Check norm line, and any future entry in it
is a real lead.

---

# WHAT SHIPPED IN S93

**Batch 1 — `BookComponentStandard` v01.9.0 → v01.10.0. GOING DEEPER is the 26th family, bronze.**
A **promotion out of §7.2 Systems at zero new icon cost** — the second instance of the ENGINEER'S LOG
move, on the same test: the nav affordance and the callout name one destination. `marks/` **40 → 41**;
the count gate **control-ran FAILING** at *1 would change* before regeneration. New mark carries
**`#725637`**, byte-identical to `stars.svg`, its bronze sibling.

**Batch 1 — Bible v8.79.1 → v8.80, new §26**: the palette conflict, parked. Plus §26.7.

**Batch 1 — the Bible was recovered.** Commit `3664bf8` correctly deleted the stray
`ZUMO_SUPER_BIBLE (1).md` but **overwrote the live Bible with that stray's header**, regressing the
version line to v8.78 and deleting the whole **v8.79 (S92)** entry. Recovered byte-exact from
`ae31126`. **A duplicate of a canon file is not inert — deleting it and overwriting from it are one
hand movement apart.**

**Batch 2 — Bible v8.80 → v8.81, new §24.11**, plus L04 **v04.14.0** and L12 **v01.14.0**, both
MODERATE. Census **unchanged at 39,970** across both batches — the fixes add characters, not lines,
which is itself the check that they were surgical.

---

# THE TWO ROWS THAT COULD NOT BE WRITTEN (S93's other finding)

DJ approved "write the three missing rows (SEE / 🛑 / 🔬)." Only 🔬 was row-shaped.

**🛑 is not a missing family — it is THE WALL, already row 23.** 19 blocks, two jobs, two reds:
**L11 ×5 + L12 ×13 = 18** on `#fdecea`/`#e74c3c`, which is exactly what S90 created THE WALL for
(`bricks`, purple, *"the L11/L12 limit block"*), never repainted because purple is unapproved; plus
**L03 937** on `#f8d7da`/`#c0392b`, *"ALWAYS STOP YOUR MOTORS"*, a real hazard. **Writing a 🛑 row
would put one construct in the table twice, which §4.1 forbids.**

**SEE cannot name a scheme.** `#d1ecf1`/`#17a2b8` is worn by **51 blocks doing ~20 jobs** — SEE is 22;
the other 29 are LEARN ×4, INFO ×3, Real-World Connection ×3, 🏆 ×2, 🧠 ×2, OBJECTIVES, INSIGHT, 🔮,
unit/math notes ×4 and more. Naming it SEE's paint repeats S92's borrowed-paint error at double scale.

Two corrections to the S93 handoff's own claims:
- **"zero label edits" is wrong by one** — L07 2669 is title-case `What You Should See`, outside every
  gate because SEE is not canon yet.
- **`eye` already exists** as the §7.2 prose marker *see*, and §8 records it as deliberately *"freed
  for the see marker."* A new Bootstrap glyph would put two glyphs on one job.

**The red 21 resolves into 18 THE WALL + 3 SAFETY orphans** (L03 937 🛑, L06 624 🚨, L14 1464 ⚠, all
`#c0392b`). §5.0 records S91's reassignment as covering *"L01, L06, L07, L08 and L09"* — **L03 and L14
were never in scope**, so *"SAFETY was red's only member"* is false and the fix is two fixes.

---

# §26 — THE PALETTE CONFLICT (PARKED; DO NOT RULE ON IT YET)

`BookComponentStandard` §5.0 and RoboLore `ColorPalette.md` v01.00.00 both define **Heritage Blue**,
disagreeing on **all five hexes**. Four tests favour RoboLore: ten stated contrast ratios reproduce to
**0.02** total error vs the standard's **6.00**; RoboLore's values appear **10–15× across four upstream
documents** and the standard's appear **nowhere** upstream; the standard's own **LOCKED §9** uses
RoboLore's bronze and parchment; and the S91 swap (`c4a90de`) recorded **no rationale** while every
contrast ratio **FELL**. **Gate gap: `gen_component.py` never parses §9.**

**DJ's instinct is that the standard supersedes. NOT SETTLED — his call.** Making it correct requires
writing the rationale plus bumping `ColorPalette.md` and `robolore-colors.css`.

**The semantic three is no longer undefined.** `InstructionalGraphicStandards.md` **v01.00.00 Approved**
§7 locks warning gold `#CCA700`, error red `#F44747`, syntax green `#6A9955` — **no purple** — and its
§6 says teaching cards must not be filled or headed with Heritage Blue.

**THE ONE OPEN QUESTION: are the book's callouts "instructional cards" under §6?** If yes, §5's
seven-role Heritage Blue callout scheme is off-canon. Everything else waits on that.

**BLOCKED ON FILING, NOT DESIGN.** The approved v01.00.00 sits at `Standards/`; the superseded
v00.90.00 **draft** occupies the canonical path `CODEX.md` and `VisualIdentity.md` point at. All of
RoboLore is uncommitted, and it is private so a session cannot check the remote.
**S94 first ask: has RoboLore been committed?** If not, do not reopen the colour questions.

---

# OPEN — CARRIED

- **`lesson_inventory` banner expectation 2 → 1** (above). Small, first.
- **`SEE` / `YOUR TURN` renames** — ruled at S92, still blocked: no SEE row, no derivable scheme.
  `✋` remains unused book-wide (0 occurrences).
- **The whole mark library is unwired** — **zero references to `images/icons/` or `images/marks/` in
  any page**, re-verified at S93 by parsing every attribute of every element across all 21 pages,
  with a control proving the parser sees references at all (196 `<img src>` found). 89 files, none
  referenced; every live block runs on emoji. **Largest unstarted item, and it is what most "missing
  construct" findings actually are.**
- **📝 does eight jobs across 82 blocks**; `MY PLAN` (20) is OUT — the Maker stamps a matching comment
  block into every generated `main.cpp` (L01 excepted), so renaming breaks book/generator agreement.
- **`WHAT YOU NEED BEFORE STARTING` exists on two glyphs** — 2 on 📝, 2 on 📋.
- **1.0em PARKED** (990 of 1,048 titles at 1.05em).
- **§25.10e is misfiled** — line 1 of the Bible, above its own title, while §25.10a–d and §25.10f are
  in place and §25.10f opens by discussing it. Logged, **not moved** — wants a ruling. See §26.6.
- Semantic three unapproved · Heritage Blue renders nowhere · `ZUMO_AMBER_CLASSIFICATION_S91.md` (DJ's
  S92 definition of Note absorbs REMINDER) · WRITE IT and COMMON PITFALLS are the zero-block
  repurposing candidates · §9 numbered marks LOCKED · §18.2 mandates `raw.githubusercontent.com` while
  live refs use `weymuth.github.io` (**parser counts 192 of 196 `<img src>` on Pages, 2 bare `images`,
  2 `../images` — the carried "223" figure is unverified**) · two misfiled blocks in L12 · 22
  sentence-lead `<b>` blocks deliberately not titles.

---

# STANDING QUEUE (carried)

**Difficulty-progression audit** — 2 inversions in 14 transitions, so three specific problems:
**L10→L11 is the real dip** (2.60→2.00) and L11's internal order is `1·2·4·2·1` · **TOUGH used 3 times
in 87 challenges** · the **grasp axis is bumpier than the doing axis** (4 vs 2) · L03 and L11 both end
easiest-after-hardest. **§6.12a says nothing about ascending difficulty within a lesson — needs a DJ
ruling.**

Challenge-card redesign Part B (~80–100 cards to L06's Goal→Logic→Template pattern) · Maker batch
(bulk starters DL · `?lesson=N` gate · C## labels) · L01 VS Code multi-root step · TDP template v3
(A5 Lab Log) · day-by-day grid + syllabus · L03 open items (1000 ms explainer, modulo explainer, two
Coach's Tips, C01/C05/C06 starter `finished`-payload debt shared with L08/L09/L10) · BC03 weeding
criterion · L16 outside the bonus family (DJ: *"Let's wait."*) · **robot icons §21 still 2 of 5** —
Romi, Balboa, Zircon absent, five regeneration prompts already written · S87's six logged-not-fixed
leads · S86's eight PART-seam readings · §25.6's header example reads `Version 02.7` for L11.

**Image shot list: 21 of 25 outstanding.** Most are DJ-and-a-camera and **must not be AI-generated**.
Four are legitimate GPT atmosphere work (L13-02, L14-01, L14-02, L16-01). L07 7-13 is misfiled — it is
a diagram, so it is Claude's.

**Housekeeping:** `__pycache__` .pyc **cleared**. `ZUMO_SUPER_BIBLE (1).md` **cleared**. Still in root
and unreferenced by any page: **`ChatGPT Image Jul 29, 2026, 10_20_32 AM.png`** (1.5 MB, 1122×1402,
from S91 `c4a90de`) — needs a DJ ruling to delete. §12/§23's "no strays" gate passes with it present,
so its stray check does not reach root non-HTML files.

---

# PUSH LIST — BATCH 2 — 5 uploads, no deletions

| Action | File | Replaces |
|---|---|---|
| upload | `lessons/Lesson_04.html` | v04.13.0 → **v04.14.0** (crossed tags at 1363) |
| upload | `lessons/Lesson_12.html` | v01.13.0 → **v01.14.0** (`<Wire.h>` escaped, 594 + 774) |
| upload | `ZUMO_SUPER_BIBLE.md` | v8.80 → **v8.81** (§24.11) |
| upload | `LIVE_ZUMO_TEXTBOOK.md` | replaces the copy pushed in batch 1 |
| upload | `ZUMO_S94_HANDOFF.md` | **replaces the batch-1 copy** — same filename, newer contents |

**No deletion this time** — `ZUMO_S93_HANDOFF.md` is already gone and §12.2 passes.

⚠️ **`ZUMO_S94_HANDOFF.md` and `LIVE_ZUMO_TEXTBOOK.md` are being delivered a second time with
different contents.** The batch-1 copies are already live and are now superseded; overwrite both.
