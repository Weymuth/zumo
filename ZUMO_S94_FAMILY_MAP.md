# S94 — the complete callout family map

**All 1,048 callout blocks assigned. 30 families.** Every number parsed from the live lesson
files with HTML entities decoded. Nothing pushed; nothing in the repo modified.

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
| THE WALL | 17 | 1.6% | existing roster family |
| STILL GREEN | 17 | 1.6% | **NEW row required** |
| ENGINEER'S LOG | 17 | 1.6% | existing roster family |
| WHERE THIS GOES | 14 | 1.3% | existing roster family |
| WHAT YOU NEED | 13 | 1.2% | **NEW row required** |
| IF YOU'RE STUCK | 9 | 0.9% | **roster family, was 0** |
| (card header) | 9 | 0.9% | not a family — challenge-card header, §7.2 supporting marks |
| GOING DEEPER | 7 | 0.7% | **roster family, was 0** |
| REAL-WORLD CONNECTION | 7 | 0.7% | **NEW row required** |
| THINK ABOUT IT | 7 | 0.7% | **NEW row required** |
| MYSTERY | 5 | 0.5% | **NEW row required** |
| ANSWER | 4 | 0.4% | existing roster family |
| YOU MIGHT WONDER | 4 | 0.4% | **NEW row required** |
| HOW THIS SECTION WORKS | 2 | 0.2% | **roster family, was 0** |
| COMMON PITFALLS | 1 | 0.1% | **roster family, was 0** |
| OBJECTIVES | 1 | 0.1% | **NEW row required** |

## Six new rows required

WHAT YOU SHOULD SEE 25 · TRY THIS 22 · STILL GREEN 17 · WHAT YOU NEED 13 ·
REAL-WORLD CONNECTION 7 · THINK ABOUT IT 7 · MYSTERY 5 · YOU MIGHT WONDER 4 · OBJECTIVES 1

## Four roster families that had ZERO blocks and now have work

IF YOU'RE STUCK 0→9 · GOING DEEPER 0→7 · HOW THIS SECTION WORKS 0→2 · COMMON PITFALLS 0→1

## What is NOT decided

Naming is complete. **Paint is not.** Outstanding paint questions:

1. **LEARN and INSIGHT both sit dominant on `#e3f2fd`/`#2196f3`.** One must move. This is a
   paint decision, deliberately not invented at the end of a long session.
2. **KEY TERM spans three purples** — `#9b59b6` ×136, `#9c27b0` ×33, `#9b6a9e` ×1 — and the
   third is MY PLAN's own colour, so a KEY TERM block and a MY PLAN block already share paint.
3. **12 of the 51 schemes are one-offs**, several one hex from a neighbour (`#ffb300` vs
   `#ffc107`, `#fff9e6` vs `#fef9e7`, `#e8f3ec` vs `#e3f2ed`). Those look like typos.
4. **46 distinct glyphs, 12 used exactly once** — 🔎 🍽 📐 🔋 📚 🔢 📏 🆕 ≈ 🍳 🎉 🔌.
5. **The label convention for KEY TERM's 184 blocks** — does the label carry the words
   "KEY TERM", or does the 🔑 mark alone identify it? Governs more blocks than anything else.

## Queue items found to be phantoms this session

1. **L03/L08/L09/L10 `finished`-payload debt** — all four lessons have a `finished` payload,
   every challenge row resolves, and S49 already ruled C01–C06 stay finished-preload.
2. **L03 "1000 ms = 1 second" explainer** — already written: *"Every timing number in this
   lesson is in milliseconds (ms) — thousandths of a second. So 1000 ms = 1 second."*
3. **L03 modulo explainer** — already written: *"New operator: % (modulo) — the % operator
   gives you the remainder of a division, not the divide itself. 7 % 3 is 1."*

## Corrections logged against my own earlier numbers

- **ENGINEER'S LOG was reported as 0 blocks. It has 17.** The label carries `&rsquo;`, so the
  matcher missed every one — §24.11's lesson applied to my own analysis. Decode entities first.
- **The "5 collisions / 121 repaints" figures are void**, computed pre-entity-fix.
- **WHAT YOU NEED was reported as 6 blocks. It has 13**, across four schemes and two glyphs.
- **"104 blocks remaining" understated the job.** 420 blocks lacked a family label; the 104
  were only those on schemes where nothing at all matched.

*S94 · rulings by DJ, placements by Claude where delegated · nothing pushed.*