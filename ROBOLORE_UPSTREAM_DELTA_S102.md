# RoboLore upstream delta — owed from the Zumo book, S101–S102

**From:** `Weymuth/zumo` · `ZUMO_SUPER_BIBLE.md` §26.8 and `BookComponentStandard.md` v01.12.0
**To:** RoboLore brand canon (`BRANDING/`)
**Date:** 2026-08-01

Four rulings were made downstream that upstream does not yet carry — one of them corrected after this document was first drafted, plus one instruction of ours
that upstream is still holding and should now release. Each is routed to the file the brand
record itself names as owning that subject.

**Precedence, now stated in `BookComponentStandard.md` §1.1:** RoboLore canon is upstream on every
brand value. The book applies it and may not redefine it. These four items are therefore
*requests*, not decisions — the book has recorded them as book-local and provisional, and an
upstream ruling supersedes.

---

## 1. RELEASE THE PARK — the palette conflict is resolved

**Target:** `BRANDING/ColorPalette.md` · also remove the hold from any handoff repeating it

The `Brand_Identity_Record` §3.11 records a graphics-production instruction dated `2026-07-31`:

> Do not apply a Heritage Blue palette from memory. Two canon documents define that palette with
> five different hex values for all five colours, the conflict is formally parked.

**That instruction was ours and it is now superseded.** DJ stated the five values himself, which
dissolved the problem the park was built on: the park existed because every claim cited an
uncommitted file, and a value stated by the owner cites the owner.

The record notes the alternative five hexes were *"NOT RECOVERED"*. They were
`BookComponentStandard` §5.0's, introduced by a single undocumented commit. **They are withdrawn.**

Three independent confirmations, recorded so this does not reopen:

- All ten published contrast ratios in `ColorPalette.md` recompute to **0.018 total absolute error**.
- Re-deriving navy's title contrast from these five gives **12.75** — the figure the downstream
  standard published *before* the undocumented swap.
- `BookComponentStandard` §5.0's own numbers were **not** arithmetically wrong. They reproduce
  exactly against their own tints. The case rested on provenance alone, and saying otherwise was a
  wrong finding, corrected in the same session.

**Approved five, unchanged:** `#0B1A2E` · `#3D5266` · `#7B6240` · `#C9A463` · `#F5F2E9`

---

## 2. FORGE RED `#D46554` — a FUNCTIONAL colour, replacing `#F44747`

**Target:** `BRANDING/Standards/InstructionalGraphicStandards.md` §7, functional token table
**Files that do NOT change:** `ColorPalette.md`, `ColorPaletteValidation.md`, `robolore-colors.css`,
`README.md`, `HERITAGE_BLUE_UPDATE_NOTES.md`, `Foundation/CODEX.md`, `VisualIdentity.md` — **all
seven remain correct. Heritage Blue stays five.**

The book needs a danger colour for terminal output. `#F44747` measures **89% saturation** against
the palette's own ceiling of 49% (Warm Brass) and reads as foreign beside it. `#D46554` is
saturation 60, holding **4.60:1 on the `#1E1E1E` editor background** against `#F44747`'s 4.64 — as
close to the palette as the contrast floor allows. Pulling into the 49 range drops to 3.60 and
breaks 4.5:1.

Warning `#CCA700` and danger `#D46554` stay **distinct states**, not merged.

**§7's existing prohibition needs no amendment.** It states that error red must not be presented as
a RoboLore brand colour, and under this filing it is not — it is a functional token, which is
precisely what §6 says functional colours are for.

**Correction to a claim made downstream.** An earlier version of this delta, and Bible §26.8(7),
recorded Forge Red as a **sixth brand colour** and stated that it obliged amending §7's prohibition
and rewriting eight files. That was wrong and is reversed in Bible **§26.9**. The hex, the name and
every contrast figure stand; only the placement changed. The obligation to rewrite eight upstream
files was the signal that the ruling was filed in the wrong document.

## 3. NO GRADIENTS — extend the scope from identity to everything

**Target:** `BRANDING/VisualIdentity.md` (product-wide) ·
`BRANDING/Standards/InstructionalGraphicStandards.md` (figures)

The record already rejects gradients in four places — §1.6 wordmark, §1.8 prohibitions, §2.6
symbol forms, §3.10 print. **Every one is scoped to identity artwork.**

The downstream ruling is broader and was stated without qualification: *no gradients whatsoever
— not on logos, not on pages, not on graphics, nothing.* That covers page chrome, nav, callout
headers and figure backgrounds, none of which the existing prohibitions reach.

Measured in the book at the time of ruling: **7 distinct gradient strings, 134 instances,
17 pages, plus 13 SVG figures.**

---

## 4. DEPICTED PHYSICAL COLOUR — new rule, no upstream equivalent

**Target:** `BRANDING/Standards/InstructionalGraphicStandards.md`
(*not* `ImageryAndDiagramStandards.md`, which the record marks as partially superseded)

Recorded downstream as `BookComponentStandard` §5.0.2 and flagged book-local pending an upstream
ruling.

**The rule:** a colour that exists on a real object is depicted in the palette; the real-world
colour is stated in prose where the student needs it.

**The problem it solves.** A competition field carries red goal tape, green intersection markers,
silver and black victims, red and green evacuation triangles. Each is a physical fact a student
must recognise on a table; none is in Heritage Blue. Reproducing every real hue imports an
unbounded set of saturated colours into a palette whose ceiling is 49% and whose rarest-colour
budget is 2–6%. Omitting the colour removes the only property the object is identified by.

**Applied:** the goal-tile strip is drawn `#D46554` and captioned *red tape*. Green markers, when
drawn, take `#6A9955` — §7's syntax green, already approved upstream — at **3.33:1 on white**,
which clears the 3:1 floor for a non-text graphical object but **not** 4.5:1, so it must never
carry label text.

---

## 5. NOTHING OWED — recorded because agreement is evidence

`Brand_Identity_Record` lines 1025–1027 already reject designer-font-first stacks inside Zumo-book
SVG figures, for the same reason the book has: figures load through `<img src>` and cannot fetch
webfonts.

**The book is in violation of this, upstream and downstream both.** 41 unsafe stacks across
26 files — `Inter` 13, `Consolas` 9, `Segoe UI` 7, `JetBrains Mono` 7, ArialMT variants 5. This is
a book backlog, not a canon disagreement. No upstream edit is needed.

---

## Filing hazard

The `RoboLore_Brand_Identity_Record` is a **chat export, not a committed file**. So is much of what
it cites. That is the precise condition that caused the five-session park: rulings citing documents
that cannot be read by the party asked to follow them.

**This delta should not be applied from the export.** It should be applied to the committed files
in the RoboLore repository, and the export should be reconciled against them afterward.
