# DEPTH AUDIT — S65 findings map
### Systematic pass over all 16 lessons: used-vs-taught, substance profile, thin sections
### Companion to the human read. Machine findings verified per §11 before listing; candidates marked.

---

## FINDING 1 — THE TEACHING APPARATUS DISAPPEARS AT L11 (verified, structural)

The book's explainer machinery collapses in the back six lessons:

| | L01 | L02 | L03 | L04 | L05 | L06 | L07 | L08 | L09 | L10 | L11 | L12 | L13 | L14 | L15 | L16 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 📖 LEARN boxes | 9 | 12 | 1 | 2 | 1 | 1 | 3 | 2 | 2 | 6 | **0** | **0** | **0** | **0** | **0** | **0** |
| 🔑 KEY terms | 16 | 28 | 17 | 7 | 10 | 20 | 27 | 14 | 16 | 15 | **0** | **0** | **0** | 4 | **0** | **0** |

L11–L16 teach the book's hardest material (gyro fixed-point, PID, competition strategy) with **zero LEARN
boxes and near-zero KEY terms**. Their prose is often good — L11 and L15 read well — but the *apparatus*
students have been trained on for ten lessons (the blue box that says "this is the concept," the 🔑 that says
"this term matters") vanishes exactly when the concepts get hardest. This is the structural sibling of S64's
challenge-count collapse (L11–L14 carry 3 challenges each).

**Not a rewrite.** Most of the fix is *marking* — promoting existing strong paragraphs into LEARN boxes and
tagging the terms that are already defined inline. L12 §8A.3 (fixed point) is LEARN-box-quality prose wearing
no box.

## FINDING 2 — TERNARY `?:` BEFORE ITS LESSON (candidate — verify per §11)

`?:` is taught properly in **L06 §5.4** ("an if that hands back a value" — good section, verified). The
construct-scan shows hits in **L03 (6) and L05 (4)** — *before* the teaching. The L03 pointer scan on the
same lessons was 100% pseudocode false positives, so these need line-level verification before acting.
If real: same class as L03 C05's arrays/modulo (the oldest open gap).

## FINDING 3 — L14 IS THE THINNEST LESSON IN THE BOOK (verified profile; needs the human read)

L14 (Competition Prep) profiles worst on every axis: fewest code blocks (22), a run of near-empty sections —
"8A.1 The Code Freeze" (**8 words**), "8.3 Environmental Variation Testing" (10), "4.1 Robot Inspection
Requirements" (13), "10.1 Morning Routine" (0), "10.2 Pre-Match Routine" (0), "4.4 What to Bring" (0).
Some of those are legitimately checklists. But a section *named* "The Code Freeze" that contains eight words
is a heading making a promise the body doesn't keep — the exact L02 pattern DJ named. **Recommend L14 first
in the human read.**

## FINDING 4 — CURATED THIN-SECTION CANDIDATES (for the human read; word counts are prose-only)

False positives already removed (sections whose content is legitimately the code block below them, checklists,
and sections whose theory lives upstream — e.g. L08 §5.2 is thin but §3 carries P-control at full depth).

| Priority | Section | Words | Why it matters |
|---|---|---|---|
| HIGH | L14 §8A.1 The Code Freeze | 8 | Named concept, no content |
| HIGH | L14 §8.3/8.4 (variation / intermittent failures) | 10/18 | Debugging methodology named, not taught |
| HIGH | L15 §5.3 "the state the controller has to carry" | 34 | PID state (integral/prevError) is the lesson's hard idea |
| MED | L09 §3.5 Using Enums | 47 | Enums carry the whole state machine; §8A.1 adds 68 more — combined still light for a first meeting |
| MED | L07 §8A.2 extern | 56 | Load-bearing for the 8-file split; compact but works — DJ judgment call |
| MED | L05 §3.3 Threshold Constants | 32 | The 200/600 thresholds appear with little justification |
| MED | L03 §3.2 Motor Speed Values | 30 | −400..400 range stated, not explored |
| LOW | L01 §5.1 Include (67) · L06 §3.4 (43) · L11 §8A.4 (42) | | Brief but each has a neighbor carrying depth |

## FINDING 5 — WHAT CAME BACK CLEAN (so the read can skip re-proving it)

- Cross-lesson promises: every "Lesson N" forward-ref lands in its target (gate, book-wide)
- Arithmetic claims in prose: verify (gate)
- Hardware constants vs §16 canon: clean (gate); the one "9600" is a deliberate mismatch example
- Bitwise/pointer "uses": 100% false positives (progress bars, `<<<` markers, pseudocode arrows)
- L06 §5.4 abs()+ternary and L07 §8A.1 decl-vs-def: compact but genuinely teach

---

## HOW THE HUMAN READ SHOULD USE THIS

Suggested order: **L14 → L15 → L11–L13, L16 (apparatus pass) → the MED candidates → everything else.**
For each lesson, the questions the machines cannot answer: does each section's heading keep its promise; is
each new idea given a *reason* before a rule; could a student who reads only this lesson do its challenges.
Log findings per lesson; fixes ship as normal versioned depth passes.

*S65 · generated alongside book_gates.py v1.1 · verified findings vs candidates marked per §11.*
