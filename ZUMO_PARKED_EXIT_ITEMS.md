# ZUMO — Parked Exit-Region Items

**Status:** items that were **live in the book** and were displaced by a §25 Brain Check conversion,
or that are live and over a §25.8 cap. **Nothing here was deleted.** Every item below is recorded
verbatim with its provenance, so a later evaluation is a comparison and not a re-derivation.

**Contrast with `ZUMO_SHELVED_CARDS.md`,** which holds the opposite case: proposals that were never
authored and never live. Do not merge the two files — their contracts are inverses.

**Opened:** S77, Jul 26 2026, per DJ ruling — *"Don't retire them, put them somewhere for us to
evaluate later."*

---

## Class A — displaced ancestors

Blocks that were live in a lesson's §10 exit region and were replaced when that lesson converted to
the Brain Check family.

### L07 — *Self-Assessment*, 6 items (displaced S77, L07 v04.7.2 → v04.8.0)

Displaced because **BC02 migrates §2's nine objectives character-exact** per §25.5, which makes
Technical Skills and Objectives agree by construction. The six items below were the older, vaguer
list. Five of the six restate an objective already present in §2; one contradicts the lesson.

| # | Self-Assessment item (verbatim) | Maps to §2 objective | Note |
|---|---|---|---|
| 1 | ☐ Explain the difference between .h and .cpp files | **1** — *Explain the difference between a header file (.h) and an implementation file (.cpp)* | §2's is the same skill, stated with the file extensions spelled out. |
| 2 | ☐ Write include guards for a header file | **4** — *Use `#pragma once` and say what problem it does — and does not — solve* | **CONTRADICTS THE LESSON.** See below. |
| 3 | ☐ Use #include with quotes vs. angle brackets correctly | **3** — *Use `#include` to connect files, and say when to use `<angle brackets>` and when to use `"quotes"`* | §2's names the two cases instead of saying "correctly". |
| 4 | ☐ Organize code into logical, reusable files | **6** — *Split your Lesson 6 program into the eight-file architecture and keep it building green at each step* | §2's is the observable version of the same skill. |
| 5 | ☐ Navigate a multi-file project in VS Code | **9** — *Navigate a multi-file project in PlatformIO (tabs, Go to Definition, Peek)* | Tool-name drift: VS Code vs PlatformIO. §2's names the three moves. |
| 6 | ☐ Debug common multi-file errors | **7** — *Read a linker error and tell it apart from a compiler error* | §2's names which error distinction. |

**Not covered by the Self-Assessment at all** — §2 objectives **2** (declaration vs definition),
**5** (`extern` across eight files), **8** (tune the robot from two numbers in `RobotConfig.h`).
Migrating §2 is therefore a net gain of three skills, not a trade.

**Item 2 is the one to actually decide about.** L07 teaches `#pragma once` as the modern standard and
files include guards under a 📘 **"The Old Way"** note in §3.6 — *"If you see include guards in
someone else's code, now you know what they do."* The Glossary agrees: *"An older technique
(`#ifndef`/`#define`/`#endif`)… Modern code uses `#pragma once`."* So the checklist asked students to
self-certify writing a construct the lesson tells them **not** to write, and under §25.10 that item
was never achievable as stated. **It is not carried into BC02.** If a later pass wants the skill back,
the honest form is recognition, not production — *"Recognise an `#ifndef`/`#define`/`#endif` guard in
someone else's header and say what it does"* — and it would need §3.6 to stay as its landing target.

---

## Class B — over-cap items held pending the weeding pass

Items that are **live right now** and exceed a §25.8 cap, kept deliberately per DJ ruling S77 —
*"keep more than 5 and we can weed them out later."*

### BC03 counts against §25.8's cap of 5

| Lesson | BC03 items | Over cap by |
|---|---|---|
| L02 | 7 | +2 |
| L07 | 6 | +1 |

L01 (4), L03 (5), L04 (5), L05 (4) and L06 (5) are at or under the cap and are not listed.
L07 arrived with **seven**; item 7 left BC03 by reshape (below), so the live count is six.

**Nothing is proposed for cutting yet.** One item already left BC03, and it left by reshape, not by cut:

- **L07 item 7** *(the team/partner scenario)* — moved to **BC04 Reflection** in S77. It has no single
  correct answer and cites no section, so it was never a Knowledge Check item; it is a Reflection prompt
  that had been filed under the wrong construct. Its text is live in BC04 item 1. *Recorded here so the
  reshape is not re-litigated as a deletion.*

The remaining six all carry verified §-citations, so there is no obvious weakest item. **The weeding pass
needs a criterion, and none exists yet** — that is the open question below.

---

## Open question this file exists to answer later

Is §25.8's cap of 5 a **ceiling**, a **floor**, or **advisory**? As of S77 the Bible says ceiling
(§25.8) and scaling (§25.2's *"# (scales with the lesson)"*) in two different places, and two live
lessons sit above the ceiling by DJ ruling. **No gate counts BC03 at all**, so the conflict is
currently invisible to `book_gates.py`. A count gate cannot be written until this is settled — written
against §25.8 as it stands, it would fail L02 and L07 on its first run.

---
*Opened S77 · Zumo 32U4 · Mercersburg Academy · evaluate, then prune*
