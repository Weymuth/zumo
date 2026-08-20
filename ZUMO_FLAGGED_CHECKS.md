# ZUMO — FLAGGED CHECKS FOR DJ
### The short list. Things DJ has said he will run himself, pulled out of the bench tracker so they are not buried.

**Flagged checks version: v1.0.0** — increment on every substantive edit
(moderate change → `v1.x`; minor → `v1.x.y`). The version lives ONLY in this line.

> **WHY THIS FILE EXISTS.** `ZUMO_BENCH_TESTS.md` is the complete tracker — 51 rows across 15
> lesson blocks — and it is the right home for everything that needs the robot. But a 51-row
> file is a file nobody works from at the bench. **This is the short list: the specific items
> DJ has said he will run, in the order they unblock work.** A row leaves this file the moment
> its Result is written; the full tracker keeps the record.
>
> **HOW TO USE IT.** Run it, write what happened in the **Result** column in your own words,
> and say so in the next session. A number measured here goes into the book; a number that has
> not been measured here does not.

---

## Lesson 1 — the whole open set

These three are all L01 owes. Everything else in Lesson 1 is done: fourteen of fifteen GPT
worklist rows are shipped or dead, `L01-03` (Git) is closed by DJ's S179 ruling and seated in
Bible §16.48, and §8's Common Pitfalls slash was fixed at S179.

| # | What to do | Where | Why it matters | Result |
|---|---|---|---|---|
| **F1** | **Unplug the USB cable FIRST, then click Upload.** Not a cable pulled mid-transfer — an upload with no port at all. **Write the error text down verbatim**, exactly as PlatformIO prints it. | §6 *Break It On Purpose* | The exercise's whole payoff is the student recognizing the error when it happens for real on a build day. The book currently describes the failure without quoting it. | |
| **F2** | **Challenge 4 on the floor.** Change the **FIRST** `delay(350)` to 700 and nothing else. Does the robot finish roughly one nudge **ahead** of where it started? | §9 Challenge 4 | S177 corrected the revealed solution from *twice as long in each direction* to *twice as far out as it comes back*. That correction is reasoned, not observed. If the robot ends up behind or level, the new reveal is wrong too. | |
| **F3** | **Challenge 11's solution exactly as printed.** `setLayout21x8()`, then the voltage, 1.5 s, then the `< 4500` branch. **Can you read the number on the OLED** before §6's setup reprints *Press A* over it? | §9 Challenge 11 | If the number is overwritten before it is readable, the printed solution does not do what the challenge asks, and the student will think their code is broken. | |

---

## What is NOT on this list, and why

- **`L01-B2` (cable in, power off, upload succeeds)** — **CLOSED by DJ's ruling, S179.** You do
  not have to switch the robot on to upload; the cable powers the chip, the switch feeds the
  motors. Bible §16.48.
- **`L01-B9` (Git on a fresh Mac)** — **CLOSED by DJ's ruling, S179.** Git is required because
  it triggers Apple's Command Line Tools installer, which is where the compiler lives. Bible
  §16.48. This also closes worklist row `L01-03`, open since S137.
- **Everything else** — still in `ZUMO_BENCH_TESTS.md`, which stays the complete tracker. The
  oldest open item there is `L09-B1`, carried since S41; the most consequential is `L10-B1`,
  §16.12's perpendicular arrival, unruled since S143 and carrying a falsifiable prediction.

---
*Flagged checks · short list only · the full tracker is `ZUMO_BENCH_TESTS.md`*
