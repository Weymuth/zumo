# GPT_BRIEF_FORMAT.md — how to brief the drafting model

**Written S112.** The S111 four-task package came back with three good outputs and one
unusable one, and the split was not about quality of reasoning. It was about facts.

## The finding

Tasks 1, 2 and 4 handed GPT a file and asked it to write. The file was the whole world,
and the work was good — Task 4 returned 19/19 headings, 263/263 table pipes and 10/10
checklist items intact while cutting 499 bytes of prose.

Task 3 asked which two content categories should take the unnamed section colours. That
answer depends on facts spread across the repo: how many sections exist, whether the spine
is fixed, how the candidate content is distributed, and which colours are already reserved.
GPT had none of them. It reasoned soundly to an unusable recommendation, and — to its
credit — closed by saying the frequencies should be checked against the live inventory.

**A drafting model cannot count the book. Do not ask it questions whose answer is a count.**

## The rule

Every brief opens with a **MEASURED FACTS** block. Facts only, each naming the instrument
that produced it (§24.10 — a number with no named source is a lead, not a finding). If a
task's answer depends on a number that is not in that block, either add the number or do
not send the task.

```
## MEASURED FACTS — taken from the live repo at <sha>, do not re-derive

- The lesson spine is FIXED: 174 sections, 10-11 per lesson, zero variance
  across all 16 lessons. §4.4 makes all ten mandatory. [lesson_inventory.py]
- Six colour bands cover that spine. Two further band colours exist and are
  assigned to nothing. [ZUMO_S111_VISUAL_RULING.md, build_palette.py --check]
- WARNING carries a reserved colour that is never assigned to a band, 80
  blocks. [build_family_map.py]
- ENGINEER'S LOG: 16 blocks, all 16 inside §10. [lesson_inventory.py]
- Competition/rules terms: 88 hits, 63 of them in L14, 12 in L16, 0 in seven
  lessons. [regex over lesson source, control-run]
```

## Task shapes

**SEND** — the supplied file is the whole world:
prose tightening · learning objectives · student-facing sections · rewriting for
observability · candidate generation with tradeoffs named.

**DO NOT SEND** — the answer is a count, a distribution, or a canon lookup:
"which of these deserves X" · "how often does Y appear" · anything resolved by a
ruling already recorded in the Bible.

**SEND WITH FACTS ATTACHED** — judgement over measured ground:
"given these counts, which two categories" · "given this spine, where would a new
section go."

## Two things the S111 package did right — keep asking for both

1. **Structural recommendations were kept OUT of the diff file** and returned separately,
   so the diff stayed reviewable. Ask for this every time.
2. **It named its own inferences** and flagged the frequency gap rather than papering over
   it. That flag is what made the failure cheap to catch. Ask for an explicit
   *"what I assumed vs what I read"* section.

## And one thing to require

**Return the reference files unmodified alongside the outputs.** S111 did, and both came
back byte-identical to the repo — which is how the package was cleared in one command
instead of being read line by line.
