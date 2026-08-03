# The complete callout family map

**All 1,048 callout blocks assigned. 30 families.** Every number parsed from the live lesson
files with HTML entities decoded.

**Reproducible.** `build_family_map.py` **v1.1.0** emits this table row-for-row from a clean
clone with no prior step: `assigned 1048 / 1048`, `families 30`, `UNASSIGNED: 0`. Between S94
and S96 the document and the generator disagreed — the document was right, and the generator
has been brought to it (S96). The table below is generated output, not hand-typed.

> **S112 ANNOTATION — the two claims above are now FALSE and are left in place per §26.7.**
> The generator is **v1.2**, not v1.1.0, and it reports **`assigned 1047 / 1048`,
> `UNASSIGNED: 1`**. The orphan is **L15 line 295**, a header-less emphasis block reading
> *"How long does one pass through your loop actually take?"*
>
> **Nothing was re-ruled and no block moved.** The S111 repaint changed that block's accent
> from `#3a7d5c` to `#433014`, and the block had only ever been assigned because a
> COLOUR-keyed fallback recognised the old hex. Control-run against the pre-repaint tree
> `185e086` with the identical generator version: **1048 / 1048**. So the repaint did not
> break the assignment — it revealed that the assignment was never earned. STILL GREEN is
> the byte-count-report family, and a rhetorical question is not a byte-count report.
>
> **S112 also shrank the surface this can happen on.** A glyph-first tier was added ahead of
> the colour table: thirteen glyphs each resolve to exactly one family across every block
> that reached the fallback, so **252 hex-dependent blocks became 39**. Controlled
> positionally across all 1,048 blocks — **0 changed family**, with a sabotage arm moving
> 159 to prove the control could fire.
>
> **The remaining 39 are the fragile surface and need rulings:** 🏆 splits INSIGHT (13) /
> REAL-WORLD CONNECTION (1), ✅ splits INSIGHT (6) / CHECKPOINT (5), and 14 glyph-less
> blocks split KEY TERM (10) / LEARN (4). Ruling those retires the colour table entirely.

> **S112 SECOND PASS — THE COLOUR TABLE IS DELETED.** DJ read all 39 survivors and ruled
> each by content. `build_family_map.py` **v1.3**.
>
> **Five blocks moved, and they were hidden by paint.** Thirteen L12 blocks wore one glyph
> and one green and were **three families**: eight conceptual payoffs (INSIGHT), **three
> byte-count build reports** — *"21,342 → 24,534 bytes. +3,192"* — and **two
> observed-behaviour blocks** — *"Button C on delrin: the square closes."* S94 had already
> ruled a byte-count report is STILL GREEN, and 16 elsewhere in the book are filed that way.
> These three read as INSIGHT purely because they shared paint with their neighbours. **The
> ruling was right; the colour overrode it.** Counts: INSIGHT 60 → **55**, STILL GREEN
> 16 → **19**, WHAT YOU SHOULD SEE 25 → **27**.
>
> Controlled positionally across all 1,048 blocks: **exactly 5 changed, and only those 5.**
> Every one of the 39 prefixes was verified to match exactly one block book-wide before
> being written.
>
> **Family now comes from CONTENT, so the mark and the colour are both OUTPUTS of the
> family.** That is the order that survives the emoji-to-mark conversion — 41 marks are
> generated and none are wired in, so a taxonomy resting on emoji was resting on something
> already scheduled for replacement. The remaining glyph tier is explicitly a stopgap.
>
> **STILL OPEN:** `assigned 1047 / 1048`. The orphan is L15:295, outside the 39 and
> unruled. Gate 47 cannot be written until it is — a gate written to 1047 would be written
> to the sweep instead of to the ruling.

*Written S94 · rulings completed and generator reconciled S96 · annotated S112 · colour table deleted S112.*

| Family | blocks | share | status |
|---|---:|---:|---|
| KEY TERM | 184 | 17.6% | existing roster family |
| NOTE | 133 | 12.7% | existing roster family |
| CHECKPOINT | 112 | 10.7% | existing roster family |
| TIP | 85 | 8.1% | existing roster family |
| WARNING | 80 | 7.6% | existing roster family |
| INSIGHT | 60 | 5.7% | existing roster family |
| DO THIS NOW | 58 | 5.5% | existing roster family |
| LEARN | 47 | 4.5% | existing roster family |
| BRAIN CHECK | 36 | 3.4% | existing roster family |
| THE GOAL | 30 | 2.9% | existing roster family |
| WHAT YOU SHOULD SEE | 25 | 2.4% | **NEW row required** |
| TRY THIS | 22 | 2.1% | **NEW row required** |
| BUILDS ON | 22 | 2.1% | existing roster family |
| MY PLAN | 20 | 1.9% | existing roster family |
| ENGINEER'S LOG | 17 | 1.6% | existing roster family |
| THE WALL | 17 | 1.6% | existing roster family |
| STILL GREEN | 17 | 1.6% | **NEW row required** |
| WHERE THIS GOES | 14 | 1.3% | existing roster family |
| WHAT YOU NEED | 13 | 1.2% | **NEW row required** |
| IF YOU'RE STUCK | 9 | 0.9% | **roster family, was 0** |
| (card header) | 9 | 0.9% | not a family — challenge-card header, §7.2 supporting marks |
| GOING DEEPER | 7 | 0.7% | **roster family, was 0** |
| THINK ABOUT IT | 7 | 0.7% | **NEW row required** |
| REAL-WORLD CONNECTION | 7 | 0.7% | **NEW row required** |
| MYSTERY | 5 | 0.5% | **NEW row required** |
| YOU MIGHT WONDER | 4 | 0.4% | **NEW row required** |
| ANSWER | 4 | 0.4% | existing roster family |
| HOW THIS SECTION WORKS | 2 | 0.2% | **roster family, was 0** |
| COMMON PITFALLS | 1 | 0.1% | **roster family, was 0** |
| OBJECTIVES | 1 | 0.1% | **NEW row required** |

## The 15 blocks ruled in S96

At S94 close, 30 families and 1,048 blocks were recorded here, but `build_family_map.py`
could only reach **1,033**. The gap was never a taxonomy disagreement: this document already
counted these 15, and the per-family shortfalls summed to exactly 15, which is how the target
was recovered before a single block was read. DJ ruled them in S96.

| Block | glyph | Label | Family | Basis |
|---|---|---|---|---|
| L02:3251 | 🔁 | A new kind of label: "Builds on:" | HOW THIS SECTION WORKS | forced — only block explaining a *book convention* rather than robot content, and the family had exactly one open slot |
| L03:734 | 📐 | Unit Conversion: Millivolts to Volts | NOTE | DJ |
| L03:772 | 🔋 | Which cells — and why the code says 4800 and 4200 | NOTE | DJ |
| L03:983 | 📚 | Where Does constrain() Come From? | KEY TERM | DJ |
| L03:1096 | 🔢 | Working Backward (TRIM imbalance %) | THINK ABOUT IT | hands the reader a formula to run on their own number rather than stating a fact |
| L03:1249 | 📏 | Accuracy Note (readBatteryMillivolts ±10%) | TIP | DJ |
| L03:3071 | 🧩 | About PROTOTYPE (declared-in-scope) | YOU MIGHT WONDER | answers an anticipated question before the reader hits it |
| L03:3376 | 🆕 | New operator: % (modulo) | KEY TERM | forced — only term-introduction left, one open slot |
| L03:3434 | 🧠 | Watch your scope | NOTE | residual — fits NOTE, but landed there partly as the block left standing |
| L07:440 | 📋 | Best Practice: Naming Conventions | TIP | DJ |
| L07:1070 | 🔍 | Header vs Implementation | INSIGHT | DJ, and 🔍 is INSIGHT's canonical glyph (Bible §, type 7a) |
| L07:3645 | 🎯 | Why Today's Work Matters | NOTE | DJ — overrides the S94 forward-pointer ruling, which WHERE THIS GOES had no slot for |
| L08:529 | 📖 | Why Signed Errors Matter | LEARN | 📖 is LEARN's canonical glyph (Bible §, type 7) |
| L08:1315 | 🧠 | Why TRIM here — and NOT in followLine() | NOTE | DJ, after INSIGHT's single slot was spent |
| L08:1584 | 🎉 | Did Your Robot Wiggle? | CHECKPOINT | already on CHECKPOINT's exact scheme `#d4edda`/`#28a745`, so zero repaint; the S94 success-green→INSIGHT precedent is moot post-teal |

**How the split blocks were settled.** Three blocks competed for one LEARN slot and one INSIGHT
slot: L07:1070 🔍, L08:529 📖, L08:1315 🧠. The Bible's post-S95 split already assigns the
glyphs — **📖 LEARN, 🔍 INSIGHT** — so two resolved on extracted evidence and the third, carrying
a glyph belonging to neither, was the one that had to leave the pair.

## Six new rows required

WHAT YOU SHOULD SEE 25 · TRY THIS 22 · STILL GREEN 17 · WHAT YOU NEED 13 ·
REAL-WORLD CONNECTION 7 · THINK ABOUT IT 7 · MYSTERY 5 · YOU MIGHT WONDER 4 · OBJECTIVES 1

## Four roster families that had ZERO blocks and now have work

IF YOU'RE STUCK 0→9 · GOING DEEPER 0→7 · HOW THIS SECTION WORKS 0→2 · COMMON PITFALLS 0→1

## What is NOT decided

Naming is complete. **Paint is not.**

1. ~~LEARN and INSIGHT both sit dominant on `#e3f2fd`/`#2196f3`.~~ **RESOLVED S95** — INSIGHT
   moved to teal `#e9f7f5`/`#2da99d`, 31 blocks across 10 lessons, 18 of which also carried a
   deep-blue title moved to `#165a53`. The collision was **canon, not drift**: the Bible declared
   "Learn / Insight" as one type while `BookComponentStandard`'s roster listed two families.
2. **KEY TERM spans three purples** — `#9b59b6` ×136, `#9c27b0` ×33, `#9b6a9e` ×1 — and the
   third is MY PLAN's own colour, so a KEY TERM block and a MY PLAN block already share paint.
3. ~~12 one-off schemes.~~ **Six retired in S95**; six remain, and only L11:170 is off-canon.
   The other five each fold into a larger paint question rather than being typo-shaped.
4. **46 distinct glyphs, 12 used exactly once.**
5. **The label convention for KEY TERM's 184 blocks** — does the label carry the words
   "KEY TERM", or does the 🔑 mark alone identify it? Governs more blocks than anything else.
6. **The Bible and `BookComponentStandard` have never been diffed** where they describe the same
   thing. `BookComponentStandard` records **zero** live callout hexes; the Bible's KEY TERM row
   names a pair live on 33 blocks while the dominant scheme carries 136.

## Queue items found to be phantoms

1. **L03/L08/L09/L10 `finished`-payload debt** (S94) — all four have a `finished` payload.
2. **L03 "1000 ms = 1 second" explainer** (S94) — already written.
3. **L03 modulo explainer** (S94) — already written; it is L03:3376 above.
4. **L03 Coach's Tip, setup() fires at power-on** (S96) — already live as a 💡 TIP.
5. **L03 Coach's Tip, AI autocomplete injects wrong code** (S96) — already live as a
   ⚠️ WARNING, with the Command Palette fix in L01.
6. **"Coach's Tip" is not a live family at all** (S96) — the only structural trace is an L02
   HTML comment recording that an INSIGHT callout *replaced* an old "Coach's Note." The queue
   carried work addressed to a component that had been retired.

## Corrections logged against my own earlier numbers

- **ENGINEER'S LOG was reported as 0 blocks. It has 17.** The label carries `&rsquo;`, so the
  matcher missed every one — §24.11's lesson applied to my own analysis. Decode entities first.
- **The generator split ENGINEER'S LOG across two buckets** and read 31 families instead of 30
  (S96). `norm()` folds the curly apostrophe on the **input** side, but the glyph+scheme fallback
  map hardcoded its **output** values curly, and map values never pass back through `norm()`.
  The one header-less block resolving by scheme therefore landed in a bucket of its own. Fixed
  in v1.0.2; the block was L07:3645.
- **A clean total is not a clean result** (S96). Control-running one deliberately misrouted
  ruling left `assigned 1048/1048` completely untouched — a block moving between families does
  not change the sum. Only the per-family diff caught it. Any future gate on this data must
  compare rows, not the total.
- **The "5 collisions / 121 repaints" figures are void**, computed pre-entity-fix.
- **WHAT YOU NEED was reported as 6 blocks. It has 13**, across four schemes and two glyphs.
- **"104 blocks remaining" understated the job.** 420 blocks lacked a family label.

*Rulings by DJ, placements by Claude where delegated. Table generated by `build_family_map.py`
v1.1.0; prose maintained by hand.*
