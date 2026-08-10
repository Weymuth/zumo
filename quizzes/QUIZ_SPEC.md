# ZUMO READING QUIZ — AUTHORING SPEC

**Spec version: v1.1.0** · Ruled S136 · Amended S139 · Applies to all sixteen lessons.

**v1.1.0 (S139) — §3 FORMAT MIX.** The three ratios could not all hold at once: at both
ceilings the multiple-choice floor was 76%, so "~70% MC" was unreachable and L02 met it
only by running true/false 2 points over its cap. The matching allowance moved to ~10%
rather than the true/false cap, because matching carries `extra_answers` and true/false
is 50% guessable. L04 was authored to the amended mix; **L02 still reads TF 22% before /
83% MC after and has not been rebalanced.**

**Read this before writing a single question.** Everything below was decided once, with
reasons. None of it needs re-deriving, re-debating, or re-discovering. If a ruling here
turns out to be wrong, change it *here* and bump the spec version — do not quietly do
something different in one lesson's bank.

**Status is never written down.** Run `python3 quizzes/quiz_bank.py --status`. It reads
the tree and reports what exists. There is no progress list to keep in sync, because a
list that must be updated by hand is wrong the moment somebody forgets — silently. Same
reasoning as Bible §24.13.

---

## 0. THE ONE RULE THAT OUTRANKS THE REST

**NEVER WRITE A QUIZ AGAINST A LESSON YOU HAVE NOT READ END TO END IN THIS SESSION.**

This is not a style preference. In S136 a full read of L02 found six defects, and **four
of them sat directly under questions this bank now asks** — the battery figure was 6000
where the fleet reads 5400, the Broken Code reveal named three wrong line numbers, the
`float` pointer aimed at a lesson that never teaches it, and L01's troubleshooting table
blamed a baud rate that this hardware ignores.

A quiz written against the unread version of L02 would have keyed **6000** as the correct
answer and marked the students who read carefully as wrong. An auto-graded gate that
punishes the attentive is worse than no gate.

So the order is fixed, per lesson: **READ → FIX → QUIZ.** Never quiz first.

---

## 1. WORKFLOW FOR EACH LESSON

1. **Read the lesson end to end.** Not scan. The defects that matter are false claims in
   prose, and no instrument in this repo can see one — `book_gates.py` measures structure,
   and a wrong sentence is perfectly well-formed structure.
2. **Cross-check every number against the other lessons** before trusting it. The method
   that works: grep the figure book-wide and read every sentence it appears in. Three of
   S136's findings were *contradictions between lessons*, not errors visible inside one.
3. **Fix what you find, gate it** (`python3 book_gates.py`, read the exit code), and bump
   the lesson's version.
4. **Write the bank** against the fixed files.
5. **Pin the source versions** in the bank's `source:` block. This is what lets a future
   session know whether the answer keys are still trustworthy.
6. **Validate:** `python3 quizzes/quiz_bank.py --check` must exit 0.

### Verifying a code-behaviour answer
Do not reason it out and hope. Two techniques both paid off in S136:

- **Compile it.** A stub header plus `g++ -fsyntax-only` settles what the compiler
  actually says. This is how the Broken Code line numbers were nailed down — and it also
  surfaced that the third error is *invisible on the first build*, which no amount of
  reading would have revealed.
- **Let the book's own code testify.** L01's chime writes `playFrequency(440, 800, 15);`
  followed by `delay(900);` — a delay longer than the note, repeated for every note in the
  jingle. Those delays are only meaningful if the call returns immediately, which proves
  the buzzer is non-blocking without needing the library source.

---

## 2. TWO SETS PER LESSON

| | **before** | **after** |
|---|---|---|
| Purpose | The pre-class gate | Post-build check |
| Answerable by | Reading the text alone | Having actually built it |
| Must NOT require | The robot, a compiler, a built program | — |
| Typical sources | §1–§5, §8, §8A, Quick Reference, Glossary | §6 steps, §9 challenges, Extra Practice |
| Canvas draw | 10 | 8 |

**The `before` set is the one that matters for September.** The syllabus makes it the gate
into build time — *"If you don't pass the reading quiz, you're not cleared to start
building that day"* — so it is the blocker. Write it first for every lesson.

**The `after` set overlaps BRAIN CHECK 03 by design.** BC03 already asks ~7 applied
questions in-page. Do not duplicate BC03 items; write the things BC03 misses. If BC03
stays the graded exit instrument, the `after` set becomes the retake/review bank instead.

**Grade-split caution:** the syllabus has Reading Quizzes 20% and Exit Tickets/Checklists
10%. There is no third slot. Adding `after` as a *graded* instrument needs DJ's ruling on
where it lives.

---

## 3. FORMATS

### Allowed
- `multiple_choice` — the workhorse. **~70% of a set.**
- `true_false` — the cheap end. **Cap at ~20%.**
- `matching` — vocabulary and grouped facts. **Up to ~10% of a set** (3–6 items in a
  50-question bank). **One or two is fine for a small set; do not exceed ~10%.**

**THESE THREE NUMBERS WERE ARITHMETICALLY IMPOSSIBLE UNTIL v1.1.0, AND THE FIRST BANK
BROKE A CAP TO SATISFY THEM.** The original spec said MC ~70%, TF cap ~20%, matching
"one or two per set, no more." Run the arithmetic: a 50-question set at both ceilings is
TF 10 plus matching 2, which leaves an **MC floor of 76%** — so ~70% MC was unreachable
by construction. L02 landed at MC 74% only by running true/false at **22%, over its own
cap**, and nobody noticed because no instrument checks a mix. Measured in S139 while
comparing L04 against L02.

**THE MATCHING ALLOWANCE MOVED, NOT THE TF CAP, AND THE REASON IS SIGNAL.** Reaching
~70% MC needs ~30% non-MC. Getting there by raising the true/false cap would have bought
the percentage with the *weakest* instrument in the set — true/false is 50% guessable, so
more of it actively lowers the signal the gate exists to produce. Matching with mandatory
`extra_answers` absorbs the guess instead, so the signal holds. When a ratio has to give,
give it to the instrument that measures better, not the one that is easiest to write.

**A MIX IS A TARGET, NOT A GATE.** Nothing validates these ratios — `quiz_bank.py` checks
structure, not proportions. Land close and move on; do not spend a session chasing a
percentage. But do not drift far enough that a bank becomes a true/false quiz wearing a
multiple-choice hat.

### Banned
- **`fill_in_blank` — ruled out S136.** Canvas string-matches it, so
  `getSingleDebouncedPress` fails on a capital G or a missing paren, and a student loses
  their entry to build time over spelling. The validator rejects it.
- `essay` / `short_answer` — cannot auto-grade, and the gate closes at period start.

### Rules per format

**multiple_choice**
- Exactly **one** correct option. Enforced by the validator.
- Three minimum, four preferred.
- Give a wrong option a `why` when the mistake is instructive — Canvas can show it as
  feedback rather than just a red mark.
- **Short code snippets make the best stems.** A skimmer cannot fake
  *"which line does the compiler name?"*

**true_false**
- 50% guessable, so it inflates scores exactly where you want a real signal. Keep it low.
- **The false ones must be false on a *specific* wrong fact**, not an obvious absurdity.
  Good: *"the number in `Serial.begin()` must match the Serial Monitor."*
  Useless: *"comments make your program slower."*

**matching**
- **`extra_answers` is mandatory.** With five prompts and five answers, a student who
  knows four gets the fifth free. Two spare answers absorb the guess. Validator enforces.
- No duplicate right-hand answers — two prompts would both be correct.
- One matching item is really *n* judgments, so it is a heavy pull in a 10-question draw.
  Price it accordingly. **The cap is §3's ~10% of a set — this line said "one or two, no
  more" until v1.1.0, which is the restatement that made the mix impossible.** A rule
  restated in two sections is two rules; when one is superseded, fix the other.

---

## 4. EVERY QUESTION OWES A CITATION

`cite:` is mandatory and the validator fails without it. A wrong answer has to tell the
student **where to re-read** — that is the entire contract of a soft gate, and it is the
same contract the in-page Brain Checks already use (*"If your answer and the reveal
disagree, the section number tells you where to re-read"*).

Cite the section as the lesson labels it: `"§3.1"`, `"§6 Step 7"`, `"Quick Reference"`,
`"Lesson 1 §5"` when the question draws on an earlier lesson.

---

## 5. WHAT MAKES A QUESTION GOOD HERE

The bar is **"did you actually read,"** not "can you rank in the class." Missable by a
skimmer, gettable by a reader.

**Write:**
- Questions whose answer is a specific fact the lesson states once.
- Code snippets asking what happens, what the compiler says, what you hear.
- Distinctions the lesson draws explicitly — *not declared* vs *undefined reference*,
  parameter vs argument, SRAM vs stack, interior vs exterior angle.
- Traps the lesson warns about — the stray semicolon after `if`, the one-liner brace,
  short-circuit evaluation, `int` chopping a decimal.

**Do not write:**
- Anything answerable by general programming knowledge without reading *this* lesson.
- Anything requiring the robot, in the `before` set.
- Trick questions. The gate is not adversarial.
- Anything depending on a figure's contents unless the prose also states it — several
  facts in this book live only inside SVGs, which a screen reader cannot reach.

---

## 6. FILE FORMAT

One file per lesson: `quizzes/ZUMO_QUIZ_L##.yaml`

Required top-level keys: `lesson`, `title`, `bank_version`, `source`, `sets`.

```yaml
lesson: "L02"
title: "Mastering the Code — Reading Code You Didn't Write"
bank_version: "1.0.0"
source:
  lesson_02: "v03.21.1"     # pin EVERY lesson the answers depend on
  lesson_01: "v03.28.1"
sets:
  before:
    description: "Pre-class reading gate. Answerable from the text alone."
    suggested_draw: 10
    questions:
      - id: L02_B01           # L##_B## for before, L##_A## for after
        type: multiple_choice
        cite: "§3.1"
        points: 1
        stem: "..."
        options:
          - text: "..."
            correct: true
          - text: "..."
            correct: false
            why: "shown as feedback"
```

`bank_version` follows the project scheme: major `v#`, moderate `v#.#`, minor `v#.#.#`.
No letter suffixes.

**Why `source:` is pinned:** it is the only way a later session can tell whether an answer
key is stale. If a lesson is edited, re-check the questions citing the edited section
before reusing the bank.

---

## 7. QTI CONVERSION

Not built yet — deliberately. The YAML carries every field QTI needs (type, correct
answer, points, feedback, citation), so the converter is a script written **once** and run
across all sixteen banks. Writing prose question lists instead would have meant hand-keying
every item into XML, which is where mis-scored answers come from.

When the converter is written it belongs at `quizzes/to_qti.py` with its own `--selftest`.

---

## 8. TOOLS

```
python3 quizzes/quiz_bank.py --selftest   nine controls; run BEFORE trusting --check
python3 quizzes/quiz_bank.py --check      validate every bank; exit 1 on any problem
python3 quizzes/quiz_bank.py --status     derived progress across all sixteen lessons
```

`--selftest` builds broken banks in memory and confirms the checker is loud about each —
it never touches the real files, because a control that depends on the state of what it
audits is not a control.

---

## 9. OPEN, NOT YET RULED

- Where the `after` set lives in the grade split, if it is graded at all.
- Whether the L13–L16 banks are needed for Fall 2026 at all — the course scope is
  **L01–L12**, so four of the sixteen may never be required.
- `to_qti.py` — unwritten.
- **No gate holds the quiz banks.** `quiz_bank.py --check` exists and is loud, but nothing
  in `book_gates.py` calls it, so a broken bank can be pushed. Same debt shape as the nav
  pills (S136): an invariant with no gate.
