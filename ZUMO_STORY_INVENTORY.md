# ZUMO — STORY INVENTORY
### Every narrative passage in the book today · plus every story ChatGPT proposed adding

**Story inventory version: v1.0.0** — increment on every substantive edit
(moderate → `v1.x`; minor → `v1.x.y`). The version lives ONLY in this line.

> **WHAT COUNTS AS A STORY HERE.** A passage about **people and events** — somebody made a
> decision, something happened, and the lesson is better for knowing it. That is a narrower set
> than it feels like. `LEARN —` blocks are explanation, not story. Checklists, analogies
> (*"a pilot's aircraft is inspected before every flight"*), etymologies (*"bang-bang"*) and
> context tables (*Pentium 66 MHz*) are all excluded. **By that test the book currently has seven,
> and four of them are in Lesson 1.**
>
> **THE SOURCING RULE, AND WHY IT IS AT THE TOP.** GPT's own warning about its story list was
> *every story needs sourcing before drafting.* **S177 is the proof.** The Hello World story
> shipped two false claims — *B had no `printf`* and *you are exactly copying the very first
> programmers in history* — for the whole life of the book, because nobody sourced it. **Nothing
> in this repo reads a sentence**, so 78 green gates certified both. A story is the highest-risk
> prose in the book: it is the part a student remembers, and the part no instrument can check.
>
> **SOURCING LEGEND:** `SOLID` primary or uncontested public record · `NEEDS CITE` believed true,
> nothing pinned · `RISK` contains a specific claim or number I cannot verify.

---

# PART 1 — WHAT IS IN THE BOOK TODAY

## Lesson 01 — four of the book's seven stories live here

### S-01 · The True Story of "Hello, World!"
**Where:** §1, the lesson's opening section — the story IS the section.
**Sourcing:** `NEEDS CITE` (two false claims already removed at S177)

Kernighan at Bell Labs, 1972, writing the first tutorial for **B**; the phrase is born there and
goes world-famous six years later when he reprints it in the 1978 K&R *The C Programming Language*.
The 1972 example used `putchar()` and spelled the message out a few characters at a time.

**History:** shipped two false claims until S177 — *B had no `printf`* (it had one; the tutorial
reached for `putchar()` anyway) and *you are exactly copying the very first programmers in history*
(programming predates 1972 by decades). The figure caption also said K&R **introduced** Hello World
where the prose credits the earlier B tutorial; now **popularized**.
**Still unpinned:** *Bell Labs — the same place that invented the transistor and Unix* (both true
and uncontested, but nothing in the repo cites them).

---

### S-02 · Jim Reekes and the Macintosh startup chime
**Where:** §5, immediately before the student changes `440` to a frequency of their own.
**Sourcing:** `NEEDS CITE`

Early 1990s. An Apple engineer hates the startup chime — not because it sounds bad, but because
Macs crashed constantly and the same family of tones played when they died, so people had learned
to associate it with failure. He writes a new chord, **has no permission to ship it**, gets it into
the machines with help from the engineers who controlled the ROMs, and when told to remove it he
refuses and gives a reason he later admitted he invented. It shipped for years.

**Why it earns its place:** it is the only story in the book about somebody caring about a
two-second detail, and it lands one paragraph before the student is asked to care about one.
**"So was his"** is the best closing line of any story in the book.
**Risk:** the specific beats — no permission, the ROM engineers, the made-up reason — come from
Reekes's own retellings. **Nothing in the repo cites one.** They should be pinned to a named
interview before this ships to twelve students.

---

### S-03 · Five Notes That Said Hello — *Close Encounters*
**Where:** §9, the `LEARN` block opening the Challenges section; sets up Challenge 10.
**Sourcing:** ⚠️ **`RISK` — carries an unverified figure**

1977. Spielberg needs humans and an alien ship to communicate with no shared language. Williams
wants seven notes; Spielberg insists on five, because any longer stops sounding like a greeting —
*what he wanted was a doorbell.* Williams asks a mathematician how many five-note combinations
exist; **the answer comes back at roughly 134,000**; he writes about 350 of them, and the two of
them sit in a room listening until they find the one everybody knows.

**⚠️ THE 134,000 DOES NOT OBVIOUSLY DERIVE.** Five notes from a twelve-tone scale with repetition
is 12⁵ = **248,832**; without repetition it is 12·11·10·9·8 = **95,040**. Neither is 134,000, and
the book does not say what was being counted. **Rule 50 gives a number two fates: derive it or
delete it.** Either find what the figure counts and say so, or cut the number and keep the shape
of the story — *he asked how many were possible, the answer was a big number, he wrote 350 of them.*
The story survives the cut intact. **This is the single highest-risk sentence in the book's stories.**

---

### S-04 · Marvin, Shakey, Sojourner — the naming aside
**Where:** §1's NOTE on how to ask a search engine a good question.
**Sourcing:** `SOLID`

Three real references carried inside a lesson about search skill rather than about robots: Marvin
from *The Hitchhiker's Guide to the Galaxy*; **Shakey**, the 1966 Stanford Research Institute
machine that was the first to reason about its own actions; and **Sojourner**, NASA's first Mars
rover, named for Sojourner Truth.

**Not a full story — an aside with three real hooks in it.** Shakey in particular is one sentence
away from being a proper story about the origin of sense–decide–act, which is §3's own subject
two screens later. **Candidate for promotion rather than addition.**

---

## Lesson 02

### S-05 · The one-liner that cost Apple a year
**Where:** §3, the `LEARN` block on brace style.
**Sourcing:** `NEEDS CITE`

Two statements where the compiler saw one — the same mistake the lesson has just shown — caused a
real security hole in Apple's software in **2014** that went unnoticed for over a year. The book's
rule follows immediately: **braces are the default.**

**This is the book's best-integrated story and the model for the rest**: three sentences, no
sidebar, the rule falls straight out of it. It is also the only current story that is about a
**failure**, which is the register the rest of the book argues in.
**Unnamed in the text.** It is the *goto fail* bug (CVE-2014-1266). Naming it would let a student
look it up; not naming it keeps the paragraph tight. **DJ's call.**

---

## Lesson 15

### S-06 · Ziegler–Nichols
**Where:** §8A and the Glossary — the `TRY Kd` number printed on the robot's own score screen.
**Sourcing:** `NEEDS CITE`

*A recipe from the 1940s that has been landing engineers in the right ZIP code for eighty years.*
The table of P / PI / PID gains follows, then the honest caveat: **a starting point, not an answer**,
famously aggressive because it was designed for industrial processes that care more about
responding fast than about overshoot.

**Half a story and it works as one**, because the robot computes the number itself from the
student's own WEAVE reading. **GPT proposed adding a Ziegler–Nichols story to L15. It is
already there** — worth noting before anyone acts on the list.

---

## Lesson 16

### S-07 · Saint-Exupéry
**Where:** the lesson's opening epigraph; the lesson is named after it.
**Sourcing:** `SOLID`

*"Perfection is attained not when there is nothing more to add, but when there is nothing left to
take away."* — attributed in the book to **Antoine de Saint-Exupéry, aircraft engineer**, and the
job title is the point: it is the trade the student is about to make when the capstone will not fit.

**Not a narrative — an epigraph doing a story's work.** §6's third trade calls back to it directly
(*"this is the moment the lesson is named after"*). **GPT proposed adding Saint-Exupéry to L16. It
is already there.**

---

## Lessons with NO story today

**L03 · L04 · L05 · L06 · L07 · L08 · L09 · L10 · L11 · L12 · L13 · L14.**

Twelve of sixteen. Closest misses, none of which qualifies:
- **L08** — *"bang-bang," named after the jarring way the robot bangs back and forth.* Etymology.
- **L14** — *"your robot earns trust the same way a pilot's aircraft does."* A sustained analogy
  with no people or events in it. **GPT's proposed checklist-culture story would give it a source**
  and is the strongest single addition on its list.
- **L03** — *"every wheeled robot on Earth has it, from your Zumo to Mars rovers to Amazon
  warehouse robots."* A one-line aside.
- **L01 §5** — *How Fast Is Your Robot's Brain?* (Pentium 66 MHz · P4 ~3,000 MHz). Context table.

---

# PART 2 — WHAT ChatGPT PROPOSED ADDING

**Source:** `ZUMO_GPT_REVIEW_WORKLIST.md`, Part 5, *Structural suggestions*. **Nothing here has
been ruled and nothing has been drafted.** GPT supplied topics, not text.

| Lesson | GPT's proposed story | My read |
|---|---|---|
| **L02** | **Apollo / Margaret Hamilton** | Strong, and the register is right — Hamilton's priority-scheduling code is the reason Apollo 11 landed through the 1202 alarms. But **L02 already has the Apple 2014 story** and it is better integrated. Two stories in one lesson is a sidebar habit forming. **Hold, or move to another lesson.** |
| **L03** | **Manufacturing tolerances** | **The best fit on the whole list.** L03's thesis is literally *no two motors are the same*, and the lesson currently asserts it with no evidence beyond the student's own TRIM number. A real tolerance figure would turn an assertion into a fact. **Needs a Pololu or gearmotor-datasheet source** — which the repo already has in the resource draft. |
| **L04** | **Early guided vehicles** (line-following AGVs) | Good fit, low risk, easy to source. L04 is where line-following stops being a toy idea. |
| **L05** | **TV remote modulation** | **Strong and unusually useful** — it explains *why* IR proximity works the way it does, which the lesson currently states without a reason. The 38 kHz carrier story is the mechanism, not decoration. |
| **L06** | **Dead reckoning** (marine navigation) | Good. L06 is where the robot starts measuring instead of hoping, and dead reckoning is the same idea with the same failure mode — which L11 and L12 then spend two lessons demolishing. **Spirals well.** |
| **L07** | **Modular software** (the origin of separate compilation) | Fits L07's *messy room* thesis. Risk: this is the easiest one to write badly as a history-of-computing sidebar with no consequence attached. |
| **L08** | **Watt's governor** | **Excellent.** It is the canonical closed-loop story, it is mechanical so a student can picture it, and it lands in the lesson that introduces proportional control. **Top three.** |
| **L09** | **Machine modes / state machines** | Vaguest item on the list. GPT gave a topic, not an anchor. **Needs a specific machine before it can be drafted.** |
| **L10** | **Subsumption architecture, Rodney Brooks** | Genuinely apt — L10's subject is priority arbitration between behaviours, which is Brooks's actual contribution. **But L10 has an open unruled defect (§16.12, the perpendicular arrival).** Do not add prose to a lesson whose behaviour is not settled. |
| **L11 / L12** | **Navigation** | Overlaps L06's dead reckoning. **Pick one home, not three.** L12's *the gyro invented a hundred degrees of rotation that never happened* is already doing the work a story would do. |
| **L14** | **Checklist culture** | **The strongest addition on the list.** L14 already runs the pilot analogy for a whole lesson with nothing behind it. Gawande's *Checklist Manifesto* and the B-17 preflight-checklist origin would source it in three sentences. **Top three.** |
| **L15** | **Ziegler–Nichols** | ✅ **ALREADY IN THE BOOK** (S-06). GPT could not see it. |
| **L16** | **Saint-Exupéry** | ✅ **ALREADY IN THE BOOK** (S-07). GPT could not see it. |

## GPT's two warnings, which matter more than its list

1. **Do not put a 400-word historical sidebar in all sixteen lessons.** A story per lesson stops
   being a story and becomes a section students learn to skip.
2. **Every story needs sourcing before drafting.** Verbatim from the review — and S177 proved it
   the hard way inside the book's own oldest story.

## GPT's adjacent proposal, filed here because it is story-shaped

**A recurring "Engineering Habits" sidebar**, introduced progressively across the book and
collected in L16. Distinct from the story list: a habit is a rule with a name, not an event.
**Unruled.** Its attraction is that it gives L16's assembly section something to collect; its risk
is that it is the sixteen-sidebar pattern under a different name.

---

# PART 3 — WHAT I ACTUALLY THINK, IF IT HELPS

**Three additions, not thirteen: L08 Watt's governor · L14 checklist culture · L03 manufacturing
tolerances.** All three are cases where the history **IS** the engineering point rather than
decoration, all three sit in lessons that currently assert something without evidence, and all
three are cheap to source. That takes the book from seven stories to ten, spread across six
lessons instead of four.

**Two rules I would want ruled before any drafting:**

1. **A story earns its place by carrying the lesson's own claim** — not by being interesting.
   Every current story that works does this: Reekes lands one paragraph before the student changes
   `440`; the Apple bug lands one paragraph before *braces are the default*. S-03 is the weakest
   because it is adjacent to Challenge 10 rather than load-bearing for it.
2. **No story ships with a number nobody can derive.** The 134,000 is the live instance.

**And one cheap win that is not on GPT's list: promote Shakey.** It is already in L01 as a naming
aside, it is genuinely the origin of the sense–decide–act loop that §3 teaches two screens later,
and it costs one sentence and no new sourcing.

---

# OPEN QUESTIONS FOR DJ

1. **The 134,000 in S-03** — derive it, or cut the number and keep the story?
2. **Name the *goto fail* bug in S-05**, or keep the paragraph tight and unnamed?
3. **Ruling on volume:** three additions (my recommendation), GPT's thirteen, or none until after
   the Fall launch?
4. **Promote Shakey** in L01 from naming aside to a proper sense–decide–act origin?

---
*Story inventory · created S177 · seven current, thirteen proposed, two of the thirteen already shipped*
