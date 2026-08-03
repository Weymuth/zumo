# Callout consolidation — 30 families to 12

**Session 109. Nothing applied. This document exists to be ruled on.**

Every number below was produced by the parser (`build_family_map` + `lesson_inventory`), never
by grep, per §24.10. Every disposition below was reached by reading the **body** of the block,
not its label — because labels misled twice in this session and both errors are recorded in
§6 of this document.

Glyphs are deliberately absent. DJ ruled S109 that the current glyphs are not being kept, so
assigning them would be work against a retired constraint.

---

## 1. The finding

The 30 families are named for **topic**. The book actually operates on **pedagogical moment** —
what the reader is being asked to *do* at that instant. Re-cut that way, 30 families become 12,
every one of the 1,048 blocks lands somewhere, and no residue category is required.

That last clause is the test. `NOTE` currently fails it: 133 blocks with no defining job, holding
explanation, analogy, deliberate-failure demonstrations, section meta-commentary and vocabulary
asides. Anything that was not clearly something else became a NOTE.

## 2. The twelve moments

| moment | blocks | absorbs |
|---|---:|---|
| **EXPLAIN** | 186 | NOTE (133), LEARN (47), YOU MIGHT WONDER (4), HOW THIS SECTION WORKS (2) |
| **DEFINE** | 184 | KEY TERM (184) |
| **CAUTION** | 175 | TIP (85), WARNING (80), IF YOU'RE STUCK (9), COMMON PITFALLS (1) |
| **VERIFY** | 154 | CHECKPOINT (112), WHAT YOU SHOULD SEE (25), STILL GREEN (17) |
| **DO** | 108 | DO THIS NOW (58), THE GOAL (30), MY PLAN (20) |
| **CORE CONCEPT** | 60 | INSIGHT (60) |
| **REFLECT** | 53 | BRAIN CHECK (36), ENGINEER'S LOG (17) |
| **CONNECT** | 50 | BUILDS ON (22), WHERE THIS GOES (14), GOING DEEPER (7), REAL-WORLD CONNECTION (7) |
| **PRACTISE** | 22 | TRY THIS (22) |
| **FAIL ON PURPOSE** | 17 | THE WALL (17) |
| **PREPARE** | 14 | WHAT YOU NEED (13), OBJECTIVES (1) |
| **PREDICT** | 7 | THINK ABOUT IT (7) |

**1,030 blocks in 12 moments + 18 leaving the taxonomy = 1,048.** Asserted, not hand-added.

## 3. Three constructs leave the callout taxonomy

These are not callouts and should not be given callout colours.

| construct | blocks | why |
|---|---:|---|
| `(card header)` | 9 | `Work in: / Where to look:` — a §7.2 supporting mark. Already ruled S94. |
| MYSTERY | 5 | **All five are in L10 only.** See §5. |
| ANSWER | 4 | All four in L11, answering L11's sabotage *cards*. |

They belong to the **challenge-card system**, which has its own difficulty pills and its own
redesign arc already queued.

## 4. Where the current assignment is wrong

Reached by reading bodies. Roughly **1 in 10** of a 188-block stratified sample sits in the
wrong family, and NOTE accounts for the largest share.

| block | currently | should be | why |
|---|---|---|---|
| L02 §6 *"IT BREAKS — ON PURPOSE"* | NOTE | FAIL ON PURPOSE | demonstrates a deliberate compile error |
| L02 §6 *"EXPECTED ERROR! This is intentional"* | NOTE | FAIL ON PURPOSE | same device |
| L15 §8A *"An instrument is not good or bad…"* | NOTE | CORE CONCEPT | the lesson's central takeaway |
| L16 §5 *"Design pattern worth stealing"* | NOTE | CORE CONCEPT | takeaway, not aside |
| L15 §5 *"The general rule, worth more than this lesson"* | NOTE | CORE CONCEPT | says so in its own text |
| L12 §6 / L08 §6 *"How this section works"* | NOTE | (own family) | literally titled it |
| L14 §1 *"The Reality Check — at every RoboCup competition…"* | WHAT YOU SHOULD SEE | CONNECT | not expected output |
| L10 §7 *"Where are the numbers? There is no TURN_MS"* | WHAT YOU SHOULD SEE | CORE CONCEPT | a payoff, not an output |
| L09 §6 *"THE GREEN SURVEY — add this TEMPORARY block"* | TRY THIS | DO | an instruction |
| L14 §6 *"Why these numbers and not round ones"* | IF YOU'RE STUCK | EXPLAIN | the only one of nine that is not a Maker rescue |

**REAL-WORLD CONNECTION → CONNECT, not PREDICT.** An earlier draft of this analysis merged it
into THINK ABOUT IT. Reading the bodies disproved that: *"Encoders are everywhere: car odometers,
computer mice, 3D printers"* is an application, not a prompt to reflect.

## 5. The MYSTERY finding

MYSTERY looked undercounted at 5 blocks against 35 `bonus-sabotage` constructs book-wide. It is
not undercounted — it is an **L10 authoring deviation**.

Verified two independent ways:

- L08, L09, L11–L15 mark each mystery as `<h3 data-challenge data-kind="bonus-sabotage">` — a
  **card**, which sits outside the callout population entirely.
- **L10 carries both**: 5 sabotage cards *and* 5 MYSTERY callouts. Its mysteries are cards that
  additionally wear callout paint.

So L10 should be brought to the card form used by the other seven lessons. That is an authoring
fix, not a palette question, and it is **not** proposed here.

## 6. Two errors made and corrected in this session

Recorded per §24.6c, because both came from trusting a fast instrument over reading.

1. **A keyword classifier on NOTE resolved 13 of 133 blocks** and left 120 unclassified. Its
   numbers were discarded rather than presented. A classifier that cannot answer is not evidence.
2. **`ANSWER → MYSTERY` was asserted from labels and was wrong on the evidence given.** The five
   MYSTERY blocks are in L10; the four ANSWER blocks are in L11. Reading L11 showed it has its own
   mysteries authored as cards, so the pairing survives — but the reasoning offered for it did not.
3. **INSIGHT's 60 blocks were dropped from the first model build.** Caught only because the block
   count was asserted against 1,048 rather than eyeballed. An arithmetic check found what review
   did not.

## 7. What this does not settle

- **The NOTE split.** 133 blocks need a per-block disposition. This document establishes that at
  least four destinations exist (EXPLAIN, CORE CONCEPT, FAIL ON PURPOSE, HOW THIS SECTION WORKS)
  but does not assign them.
- **OBJECTIVES (1 block, L02 §2).** Left where it is. It is a §2 Learning Objectives construct,
  and the §2 objectives variance is already an open S109 queue item; merging it into REFLECT would
  move a §2 block into a §10 family.
- **Whether DEFINE belongs in the callout system at all.** 184 blocks, 165 distinct term-and-
  definition entries, several holding multiple terms in one block. That is a glossary rendered
  inline, structurally unlike every other family.
- **Colour.** Deliberately out of scope. Families first, then paint.

## 8. Two families with no equivalent in standard publisher taxonomies

Worth keeping deliberately rather than losing in a consolidation:

- **FAIL ON PURPOSE** (THE WALL, 17) — the moment an approach is shown to be structurally
  impossible, not merely hard. *"There is no threshold that works. Not a badly chosen one."*
- **VERIFY's byte-count half** (STILL GREEN, 17) — *"COMPILE CHECK 24,534 bytes — byte-identical."*
  Teaching that a correct change can cost zero bytes is specific to this book.

---

*Session 109 · produced by parser, dispositions by reading 188 block bodies · nothing applied*
