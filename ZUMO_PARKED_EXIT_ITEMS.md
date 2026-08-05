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

### L09 — *Problem-Solving: Can you modify or extend…?*, 3 items (displaced S80, L09 v05.4.2 → v05.5.0)

DJ approved folding this block into BC02 as a labelled group per §25.10a, but §25.10c's achievability
rule overrides the fold: none of these is a baseline skill every student who did the lesson can claim,
so behind BC02's Mark-done lock they would make the button unreachable. The block's **fourth** item was
an explicit *Reflection:* duplicate of L09's live *Reflection: Draw Your State Diagram* and was retired
into it (S73 L03 duplicate-Reflection precedent). These three remain, verbatim:

1. Add a new `PAUSED` state that freezes the robot when button A is pressed and resumes on a second press.
2. Extend `checkForIntersection()` to recognize a cross (+) intersection where the center sensors stay black through the junction.
3. Combine debounced detection (Challenge 5) with encoder turns (Challenge 4) for a competition-ready navigator.

**Why they are not yet mysteries.** DJ ruled at S80 to reshape them into mysteries 6–8 per §25.10c.
Blocked on discovery, not on authoring: **every L09 construct links its own Maker payload kind** — all
six challenges and all five mysteries — so a new mystery needs a new sabotaged 8-file payload registered
in `newproject.html` (5.2 MB, edited by offset per §15) plus a payload byte-match gate run. And the
deeper mismatch: a mystery is a planted *defect* and these three are *extensions*. Item 1 has nothing to
sabotage. **Reshaping them as bonus challenges is the likelier correct target** — same payload cost, no
invented bug. Needs a ruling before authoring.

---

## GRAPHIC 11.2 — "BASE_SPEED 150" is not book canon  *(logged S100)*

A GPT redesign of `L11_GRAPHIC_11-02_cliff_arithmetic.svg` labels its speed row
**"Robot speed at BASE_SPEED 150: 25 cm/s."** Every other number in that graphic matches
Lesson 11 §8A.4 exactly — 4.5 cm warning, 180 ms, 10 cm gap, 400 ms, the 220 ms deficit, and
the "there is no such number" ruling, all verbatim. **`BASE_SPEED 150` appears nowhere in any
lesson.** L11 sources the figure differently: *"Section 8A.4 ran the cliff arithmetic on a demo
robot — 25 cm/s, 4.5 cm of warning, 10 cm gaps."* It is a measured speed on one demo robot, not
a value derived from a named constant.

**Why it matters, and why it is not urgent.** The cliff proof is *ratio-based* — going slower
shrinks both numbers and the ratio never changes, which is the whole §8A.6 point. So the
argument survives any speed. But a student who sets `BASE_SPEED` to 150, measures something
other than 25 cm/s, and concludes the proof is broken has been misled by a label, not by the
maths.

**Options when this is taken up:**
1. Drop the clause — "Robot speed: 25 cm/s" — cheapest, matches L11's own framing.
2. Say "demo robot" — "Robot speed (demo robot): 25 cm/s" — mirrors §8A.4 wording exactly.
3. Make it true — measure cm/s at a stated `BASE_SPEED` on the fleet and canonize the pair in
   L11 plus the Resource section. This is the only option that adds knowledge, and it is a
   BENCH item: it needs the robot, a tape measure and a stopwatch.

**Do not fix this in the graphic alone.** If option 3 is ever chosen, the number has to land in
the lesson prose first and the graphic second, or the two disagree the moment someone re-reads
§8A.4. Recorded so the reasoning is not re-derived.


---

## Open question this file exists to answer later

Is §25.8's cap of 5 a **ceiling**, a **floor**, or **advisory**? As of S77 the Bible says ceiling
(§25.8) and scaling (§25.2's *"# (scales with the lesson)"*) in two different places, and two live
lessons sit above the ceiling by DJ ruling. **No gate counts BC03 at all**, so the conflict is
currently invisible to `book_gates.py`. A count gate cannot be written until this is settled — written
against §25.8 as it stands, it would fail L02 and L07 on its first run.

---
*Opened S77 · Zumo 32U4 · Mercersburg Academy · evaluate, then prune*

---

## PARKED S104 — collapse IMAGE + GRAPHIC into one FIGURE number space

**DJ, S104: "Let's revisit Figure # after the 8th."** Recorded with its price so the decision is
not re-derived from scratch.

**The proposal.** Retire the two-space scheme (§10, v8.20) and number every figure once as
`FIGURE N.M`.

**The case for it.** The split is not a file-format distinction — `L02_IMAGE_2-06_oled_about_
screen.svg` is an SVG. It appears to encode *photographed/screenshotted* vs *drawn*, which is a
production fact, not a reader-facing one. A student reading "Figure 7.9" does not care how it was
made. Two number spaces are maintained to record something only the asset's author needs.

**The price, measured S104:**

| | Count |
|---|---|
| IMAGE tag instances / GRAPHIC tag instances | 104 / 127 |
| IMAGE files / GRAPHIC files | 38 / 88 |
| **Numbers used by BOTH spaces (each needs a renumber)** | **18** |
| Of those, colliding at file level | 12 — L05 ×4, L02 ×3 |

A renumber moves the tag, the filename, the `src`, the index row and every cross-lesson reference
together. L04's own prose states *"[IMAGE 4.1] and [GRAPHIC 4.1] are two different figures, by
design"* and would need rewriting.

**Why parked rather than declined.** It is right and the timing is wrong: it competes directly
with 20 outstanding figures five weeks before the course starts. Post-Sept-8 it is a clean
generated arc — the renumbers can be emitted and gated like every other sweep.

---

## L11 Skills Checklist — four rungs displaced by the S116 conversion

**Provenance.** `lessons/Lesson_11.html` §10, *Skills Checklist*, seven `☐` rungs, live from S64
through S115 and consumed when L11 converted to the four Brain Check blocks at S116.

**What happened to the other three.** Rungs 4, 5 and 6 are bench observations no objective covers
and became BC02's **I have…** group, tense-shifted per §25.10b. These four did not, because each
restates an objective that BC02 already carries under **I can…**.

| 1 | I can explain why a timer is the wrong instrument for measuring a gap. | Objective 1 — *Explain why a timer is the wrong instrument for measuring a gap, and an encoder is the right one.* |
| 2 | I converted encoder counts to centimeters using COUNTS_PER_CM, not a magic number. | Objective 2 — *Convert encoder counts to centimeters using COUNTS_PER_CM — and never hardcode a raw count again.* |
| 3 | I measured my gap in 7A instead of guessing GAP_MAX_CM. | Objective 5 — *Measure a real gap with your own robot instead of guessing a threshold.* |
| 7 | I can explain, with numbers, why this robot cannot detect a table edge. | Objective 6 — *Explain, with numbers, why this robot cannot be programmed to avoid falling off a table — and what you would have to change to make it possible.* |

**How the pairing was decided.** A scored pairwise diff of all 7 × 6 combinations, printed in the
builder and asserted rather than eyeballed: the four above score **0.55–0.73** against their
partner objective, the three kept rungs score **0.31–0.38** against their nearest. The builder
asserts `min(dup) > max(keep)`, so a wrong pairing cannot pass. §25.10c's L05 precedent — a
word-identical duplicate really is redundant — but the tense difference means these are *not*
word-identical, which is why they are parked rather than simply dropped.

**The open question for a later weeding pass.** The past-tense form asks something the objective
does not: *did you actually do it*, versus *can you do it*. If that distinction is worth keeping,
the right home is BC02's **I have…** group and all seven rungs fold — at the cost of the student
ticking the same claim twice under two labels. DJ has not ruled.

---

## L12 Exit Ticket — one rung displaced, four reshaped, two reworded (S117 conversion)

**Provenance.** `lessons/Lesson_12.html` §10, *Exit Ticket*, ten `☐` rungs under the heading
*"Tick every box. If you cannot tick one, go back — the section is named."* Consumed when L12
converted to the four Brain Check blocks at S117, L12 v01.19.1 → v01.20.0.

### Displaced — one rung, a duplicate of a §2 objective

| # | Exit-Ticket rung (verbatim) | Duplicates |
|---|---|---|
| 1 | ☐ I can explain why an encoder **structurally cannot** detect wheel slip. *(§3.2)* | Objective 1 — *Explain **why an encoder cannot detect wheel slip** — and why that is a structural limit, not a bug.* |

**How the pairing was decided.** A scored pairwise diff of all **10 × 6** combinations
(§25.10i), printed in the builder and read off the separation rather than eyeballed. Rung 1
scores **0.78** against Objective 1; the next-best pair in the whole matrix scores **0.42**.
`min(dup) 0.78 > max(keep) 0.42` on a single named pair, so a wrong pairing cannot satisfy it.

**Unlike L11, none of L12's past-tense rungs is a duplicate.** Rungs 2, 3, 4, 6 and 10 are bench
observations and outcome claims that no objective covers, and they folded into BC02's **I have…**
group per §25.10a/b without needing S116's open ruling. That ruling therefore stays open, and
still recurs on L13/L15 only if either carries a past-tense checklist.

### Instrument-vs-reading disagreement, recorded and NOT resolved

The scorer ranks **rung 2 → Objective 6 at 0.42**, the highest of the keepers, on the shared
words *robot / hands / turn / gyro*. Reading says rung 2 is a §7A bench observation (turn it by
hand, motors off) and that Objective 6's actual content — *prove the encoder turn and the gyro
turn disagree, and say which one is right* — lands on rungs **4 and 5** instead, which score
0.27 and 0.21. **The normaliser was deliberately not tuned to produce that pairing**; doing so
would be writing the gate to the sweep (§25.10i). Only the one pair above the separation was
acted on. If a later pass wants Objective 6 split into its two halves, this is the note that says
the instrument could not see it and why.

### Reshaped into BC03 — four rungs, per DJ ruling S117

DJ ruled these become **questions with answers** rather than staying tick-boxes: *"A = the
student ticks a box claiming they know. B = the student is asked, and finds out whether they
actually do."* — **B**. Each already carried its own §-citation, and L12's BC03 had **no
ancestor at all**, so these four are seeds rather than authoring from nothing.

| Rung (verbatim) | Became BC03 item |
|---|---|
| ☐ I can say, out loud, **which of those two numbers was wrong — and why neither sensor was broken.** | *You ran 7C and the OLED read `Encoder: 90` and `Gyro: 31`…* (§8A.2, §3.2) |
| ☐ I know why `gyroSetup()` must run **before** the line-sensor calibration. *(§3.6)* | *Your `setup()` calibrates two different things — why must the gyro go first?* (§3.6) |
| ☐ I know why `turnDegreesGyro()` has **no TRIM** in it. *(§5.2)* | *Every open-loop straight line in this book carries TRIM. `turnDegreesGyro()` has none…* (§5.2) |
| ☐ I understand why Bonus B4 compiles to **exactly the same number of bytes** as the correct build. | *Bonus B4 adds TRIM to the turn, and the build comes out at 24,534 bytes…* (§5.2, Bonus B4) |

**Why this is a ruling and not a mechanical fold.** §25.5 makes BC02's **I can…** group §2's
objectives character-exact, so an extra claim cannot join that list without breaking the
"asked back" contract, and a third labelled group would have been a new construct. Reshaping
across Brain Check blocks has precedent (L07 and L09 both moved an item from BC03 into BC04);
this is the first time the move runs the other way, from a checkbox into a question.

### Reworded — two rungs, both for §25.10c achievability

Behind the Mark-done lock, every BC02 item has to be earnable by every student who did the
lesson. §7's opening TIP already supplies the fallback for a student with no delrin sheet:
*"No delrin? Hold the robot. Grip the chassis firmly and let the wheels fight you. Guaranteed
slip, zero materials, works every time."* That covers 7A, 7B and 7C, which are motors-off or
turn-in-place. **It cannot cover 7E**, which drives four 30 cm sides and four corners — you
cannot hold the chassis while the robot drives a square.

| Was | Now | Why |
|---|---|---|
| ☐ I ran **§7C on a slick surface** and saw the encoder say 90 while the gyro said less. | ☐ Run 7C **on a slick surface** and seen the encoder say 90 while the gyro said far less. *(§7C)* | Tense-shifted for the **I have…** group; §-citation added, which the rung lacked. |
| ☐ I ran the Lesson 6 square **on the delrin** with **both** buttons and watched only one come home. *(§7E)* | ☐ Run the Lesson 6 square **on a slick floor** with **both** buttons and watched only one come home. *(§7E)* | The rung named a specific material the lesson only says *your teacher has*. Generalised to the property that actually matters. **The dependency is not removed** — 7E still needs a slick floor. |

**Still open for DJ.** L12's §7E genuinely requires a slick surface, and the rung is now behind
the Mark-done lock. This is S116's flagged §25.10c edge recurring with a *shared classroom
resource* in place of a tired battery: if every student gets floor time on the delrin, the lock
is earnable and nothing needs to change. If floor access is rationed, the honest move is to lift
this one rung out of the locked list. **Nobody has measured which is true, and it is a fact about
the room, not about the book.**

---

## PARKED S117 — the slick surface: the noun is not the problem, the coefficient is

**DJ, S117:** *"We don't use delrin sheets. It's melamine (I think) and we have tons of tiles
sitting in the lab with tons of options."* Then, on being offered three renames:
*"Wait on changing. I think originally I said we could use delrin to get a slick surface, but
it's prob not much slicker than the melamine."*

**NOTHING WAS CHANGED.** L12 still says delrin in all 17 places. This file records why the
obvious fix was not taken.

### What the finding actually is

The first read of this was a **vocabulary** defect — the book names a material the lab does not
stock — and it was priced as 17 edits in L12, 2 payload edits in `newproject.html` (the 7D and
7E code comments are byte-compared by `gate_payload_match`), and 6 more across
`IMAGE_SHOT_LIST.md`, `ZUMO_SHELVED_CARDS.md` and `ZUMO_FAMILY_MAP.md`.

**DJ's second message re-scoped it, and the second reading is the real one.** Delrin was chosen
*because it is slick*. If the lab's melamine is not meaningfully slicker than the classroom
floor, then renaming the material does not fix anything — **it writes the wrong physics down
more accurately.**

### What depends on the surface actually slipping

| Rung | Needs slip? | Covered by §7's hands fallback? |
|---|---|---|
| 7A — gyro with motors off | no | n/a |
| 7B — delete the calibration | no | n/a |
| 7C — the lie caught in the act (`Encoder: 90` / `Gyro: 31`) | **yes** | **yes** — grip the chassis, wheels fight you |
| 7D — the honest turn, same surface | **yes** | **yes** — same grip |
| **7E — the Lesson 6 square, A vs C** | **yes** | **NO** | 

**7E is the exposure.** It drives four 30 cm sides and four corners, so nobody can hold the
chassis through it. Its whole payoff — *Button A collapses into a pentagon that gave up, Button C
comes home* — reproduces only on a surface slick enough that the wheels genuinely spin without
carrying the robot. GRAPHIC 12.3 draws that outcome. §8A.1 cites it. The BC02 rung asks the
student to claim they saw it, and it sits behind the Mark-done lock.

**If the melamine does not slip, 7E does not fail loudly — it fails quietly**, with both squares
coming home roughly the same and the lesson's climax reading as a claim the robot did not
demonstrate. That is worse than a wrong noun.

### This is a BENCH item, not a decision

Put a lab tile on the floor, load 7E, press A, and see whether the encoder square collapses.
One robot, one tile, five minutes, and it answers the whole thing:

- **It collapses** → the surface is fine, and the only work left is the vocabulary rename
  (option C from S117: property in the prose, the lab's actual material named once in §7's TIP).
- **It does not collapse** → the lesson needs a slicker surface sourced, or 7E needs re-staging
  around something that does slip. That is a content change to the lesson's payoff section and it
  wants its own session.

**Do not rename anything until that test is run.** A rename performed first would have to be
performed again.

### Recorded so it is not re-derived

The pedagogy does **not** depend on the material — §3.2's structural-limit argument and §8A.2's
two-instruments argument stand on any surface. It is only the **demonstration** that needs the
coefficient. §7's own prose already knows this and says so: *"The delrin is the demonstration —
but your hands are the proof."*
