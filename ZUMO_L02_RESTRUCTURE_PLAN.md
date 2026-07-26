# L02 RESTRUCTURE — MEASURED PLAN (written S72) — **EXECUTED S73, L02 v03.0.0**

> **DO NOT RE-CUT FROM THIS FILE.** It shipped S73 and is kept as the record of how the renumber was
> measured, not as an instruction. Two things below turned out wrong at execution and are corrected in
> LIVE.md: (1) §3 closes to **3.1–3.6**, not 3.1–3.5 — `3.2d` is its own `<h3>`, not nested inside `3.2c`;
> (2) the citation trap was worse than logged — BC01 item 3 cited §3.2 for the function prototype, which
> §3.2 never taught, so the pointer was already wrong before any renumber touched it.

**Authority:** Bible **§4.4** (v8.58, S72). DJ-ruled S72: ten-section skeleton mandatory · §4 is always
Hardware · lesson-unique material folds · §8A stays conditional · concepts before the code walkthrough ·
the seven-section **diagram** stays early even though its walkthrough moves.

**Target version: L02 v02.16.0 → v03.0.0** (major — the file's shape moves).

---

## THE MOVE, IN ONE LINE

`3.2 Understanding Each Section` lifts out of §3 and becomes §5 The Code. Everything else in §3 stays
where it is, in the order it is. Then §5 Build It → §6, and the two orphans (§4 Getting Ready, §6 Make
It Yours) fold into their real homes.

## MEASURED, S72 (verified against the live file)

| Current | Bytes | Destination |
|---|---|---|
| §3 · 3.1 The Seven Sections | 16,481 | **stays §3** — this IS the diagram + print tip + notebook card + the prototype INSIGHT. It is orientation, not walkthrough. |
| §3 · 3.2 Understanding Each Section | **29,833** | **→ §5 The Code** (the one contiguous lift) |
| §3 · 3.2b Data Types | 7,727 | stays §3 |
| §3 · 3.2c the `if` Statement (3.2d appears to nest inside this block — verify) | 14,465 | stays §3 |
| §3 · 3.3 The Two-Week Rule | 4,829 | stays §3 |
| §3 · 3.4 Common Pitfalls | 13,996 | stays §3 |
| §4 Getting Ready | 11,410 | **→ opening of the new §6 Build It** |
| §5 Build It | 70,892 | **→ §6** (renumber only) |
| §6 Make It Yours | 4,242 | **→ §9 Challenges** — it is ⭐-rated optional customization, i.e. challenge content wearing a section banner (Bible §4.4 Rule 2) |
| — | — | **NEW §4 Hardware** — author: no new parts this lesson + what today's code touches (Button A/B/C, yellow LED, OLED) |

§3 total today: 92,901 b — the largest section in the book's largest lesson. The split is worth doing on
size alone, independent of numbering.

**No reordering is required.** 3.2 lifts from the middle; the survivors keep their sequence. This was the
open pedagogy question at S72 and the measurement dissolved it — the concepts already sit after 3.1 and
before nothing that depends on them.

---

## THE TRAP — READ BEFORE CUTTING

**16 §-citations written into L02's Brain Check blocks during S72 point at sections this renumber moves.**

- BC01 Mental: `§3.1 · §3.2 · §3.1 · §3.2 · §3.2 · §3.3`
- BC03 Knowledge Check: `§3.1 · §5 Step 7 · §3.2 · §3.2 · §8A · §5 Step 2 · §5 Step 6 · §3.3 · §3.2 · §3.3`

After the move: every **§3.2** becomes **§5**, and every **"§5 Step N"** becomes **"§6 Step N"**. §3.1,
§3.3 and §8A are unaffected.

**The gate will not catch a wrong one.** book_gates §25.2 asserts that a Mental item *names* a § — not
that it names the right one. A mis-pointed citation ships green and only fails in a student's hands, in a
flipped course where the whole point of the citation is "this is where to re-read." Re-point these by
hand and eyeball every one against the moved content.

Also outstanding, same class: **3 × `Section 3.x`**, **12 × `&sect;3.x`**, **5 × `3.2b|c|d`** references
live in the file (S72 count, whole-file). Some overlap the 16 above. Re-grep at S73 open rather than
trusting these counts.

---

## EXECUTION ORDER

1. Fresh clone; confirm L02 reads **v02.16.0** and all 21 gates pass before touching anything.
2. Author the new §4 Hardware body (only genuinely new prose in the job).
3. Lift 3.2 → build the new §5 banner + panel around it.
4. Renumber: old §5 → §6; fold old §4 Getting Ready into §6's opening; fold old §6 Make It Yours into §9.
5. Renumber anchors `section-5`→`section-6`, retire `section-6`, add `section-4`/`section-5` in their new
   jobs. Update nav pill labels, back-to-top targets, and the PART banner subtitles (they name section
   ranges, e.g. "Sections 4–6: …").
6. **Move BC01** from the §4/§5 seam to the §5/§6 seam — it must still land at the last seam before
   hands-on work (§25.2), which after the renumber is before §6 Build It.
7. Re-point the 16 Brain Check citations + the other subsection refs. Eyeball, do not trust the gate.
8. Decide subsection renumbering inside §3: leaving `3.1, 3.2b, 3.2c, 3.3, 3.4` with a hole at 3.2 is ugly;
   renumbering to `3.1–3.5` is cleaner but multiplies the reference edits. **DJ ruling needed.**
9. Version → **v03.0.0**, both homes (§5b): hidden comment full three-digit, visible banners `Version 03.0`.
10. `book_gates.py` (expect 21 PASS) + `pill_sweep.py --audit` + injection controls on the §25.2 gate.
11. Regenerate LIVE.md **last**.

---

## OPEN RULINGS FOR S73

1. §3 subsection renumbering — close the 3.2 hole (`3.1–3.5`) or leave the lettered sequence intact?
2. "Make It Yours" landing in §9 — does it become challenge cards in the canonical three-panel format, or
   ship as a prose block (it is currently a 4-row option table with ⭐ ratings)?
3. Does the new §5 keep the name **The Code** (matches L01 and L03) or take L02's own voice?

---
*Written S72, July 25 2026. The renumber's real payoff is not tidiness: it makes Bible §15.2's existing
wording — "if Section 6 has N steps" — true across all sixteen lessons, instead of rewording canon to
accommodate the one lesson that never fit it.*
