# Teacher Daily Planning Grid — Zumo, Fall Term 2026
### D block · 28 dated periods + the exam block · Mr. Weymuth
<!-- ZUMO_Teacher_Daily_Grid_F26.md v2.1 — S199, Aug 31 2026: model reset to flipped-reading-only (build is class work); L02 given a second period; no Fall Midterm -->

> **Pinned to the Fall 2026 block schedule.** D block meets **29 times**: 28 teaching periods
> (Sep 4 – Nov 13) plus the exam block Nov 17. Reconciled twice against the schedule's own footer —
> 26 × 65 min + 25 + 30 + 120 = **1,865 minutes**, and **D‑29 meetings**. Both match exactly.
>
> **Model: flipped reading, everything else in class** (ruled S199). The **reading** happens before
> class and a short **graded reading quiz** gates entry — it is drawn from the bank's `before` set,
> which is answerable from the text alone. **Building, uploading, practice and the challenges are
> class work**, and each unit closes with an **ungraded end-of-unit check** drawn from the bank's
> `after` set. **⭐** = the concept needs a live demo at the open (~15 min). **DEMO** = milestone
> check-off. **[B]** = deliberate buffer.
>
> **Roster is five.** Milestone demos cost roughly twenty minutes, not a period, which is why
> periods 6 and 21 carry a lesson as well as a demo.

| # | date | time | min | flip (due before class) | in class | milestone |
|---|---|---|---|---|---|---|
| 1 | **Fri Sep 4** | 2:05 | **25** | — | **Intro + hand out robots.** Assign L01 **§1–§5 + install** (VS Code, Git, PlatformIO). No build — there is no toolchain yet | |
| 2 | Wed Sep 9 | 9:50 | 65 | **L01 §1–§5** + reading quiz | Toolchain check (5 min), then **build and upload the first program**; test sequence; TDP notebook copy | |
| 3 | Fri Sep 11 | 8:40 | 65 | **L02 Read Code Like a Pro — §2–§5 only** (§1's four warm-ups are done in class) | The warm-up gauntlet + debrief; then L02 §6 practice: build and run it; finish L01 stragglers | |
| 4 | Mon Sep 14 | 1:15 | 65 | L02 (rest) | L02 challenges + end-of-unit check | |
| 5 | Wed Sep 16 | 9:50 | 65 | **L03 Motors & TRIM** ⭐ | TRIM: drive straight, then a measured distance | |
| 6 | Fri Sep 18 | 8:40 | 65 | L03 (rest) | Finish TRIM tuning; L03 challenges — **then M1 demos (~20 min for five)** | **M1 DEMO** — drives straight + measured distance |
| 7 | Mon Sep 21 | 1:15 | 65 | **L04 Line Sensors** | Calibrate; live sensor readout | |
| 8 | Wed Sep 23 | 9:50 | 65 | L04 (rest) | L04 challenges | |
| 9 | **Fri Sep 25** | 1:15 | **30** | — | **[B] Short period — Family & Alumni Weekend.** Catch-up + materials check | |
| 10 | Mon Sep 28 | 1:15 | 65 | **L05 Proximity Sensors** | Proximity + the five-sensor jumper move | **M2 DEMO** — calibrate + report live values |
| 11 | Wed Sep 30 | 9:50 | 65 | **L06 Encoders** ⭐ | counts/cm derivation; drive an accurate 30 cm | |
| 12 | Fri Oct 2 | 8:40 | 65 | L06 (rest) | Close a square; verify wheel-base | |
| 13 | Mon Oct 5 | 1:15 | 65 | — | Milestone work + demos | **M3a DEMO** — accurate 30 cm + closed square |
| 14 | Wed Oct 7 | 9:50 | 65 | **L07 Code Organization** ⭐ | Split the project into the file architecture | |
| 15 | Fri Oct 9 | 8:40 | 65 | L07 (rest) | Wire the files together; project compiles clean; L07 challenges | |
| 16 | Mon Oct 12 | 1:15 | 65 | **L08 Line Following (P-Control)** ⭐ | P-control; robot follows a line | |
| 17 | Wed Oct 14 | 9:50 | 65 | L08 (rest) | Tune Kp; follow a full course | |
| 18 | Fri Oct 16 | 8:40 | 65 | — | Milestone work + demos | **M3b DEMO** — follows a line around a course |
| — | *Mon Oct 19* | — | — | *LONG FALL WEEKEND — no class* | | |
| 19 | Wed Oct 21 | 9:50 | 65 | **L09 Intersections & Dead Ends** ⭐ | State machine; handle a T and a turn | |
| 20 | Fri Oct 23 | 8:40 | 65 | L09 (rest) | Dead ends + kill switch; **the Green Survey** | |
| 21 | Mon Oct 26 | 1:15 | 65 | — | Milestone work + demos | **M4 DEMO** — T, turn, dead end |
| 22 | Wed Oct 28 | 9:50 | 65 | **L10 Obstacles** | Front-prox avoidance; priority arbitration | |
| 23 | Fri Oct 30 | 8:40 | 65 | L10 (rest) | Integrate avoidance into the full run | |
| — | *Mon Nov 2* | — | — | *CIVICS CONFERENCE — no class* | | |
| 24 | Wed Nov 4 | 9:50 | 65 | **L11 Time Lies, Distance Doesn't** | Encoder-based gap crossing (the odometer) | |
| 25 | Fri Nov 6 | 8:40 | 65 | L11 (rest) | Full course: line + intersection + obstacle + gap | **M5 DEMO** — obstacle + gap |
| 26 | Mon Nov 9 | 1:15 | 65 | **L12 Wheels Lie (Gyro)** ⭐ | Gyro heading; accurate turns | |
| 27 | Wed Nov 11 | 9:50 | 65 | **L13 Rescue Zone** | Silver-strip detection; stop at the zone edge | |
| 28 | **Fri Nov 13** | 8:40 | 65 | — | **LAST CLASS.** Full run; TDP assembly push | **M6 DEMO** — full course, stops at the zone |
| — | **Tue Nov 17** | **1:30** | **120** | — | **EXAM BLOCK.** Final run / re-demos / TDP due | |

---

## Milestone dates — pinned

| # | milestone | demo date | period |
|---|---|---|---|
| **M1** | Foundations — drives straight and a measured distance | **Fri Sep 18** | 6 |
| **M2** | Sensing the Floor — calibrate + report live values | **Mon Sep 28** | 10 |
| **M3a** | Measuring the World — accurate 30 cm, closed square | **Mon Oct 5** | 13 |
| **M3b** | Follows the Line — follows a course | **Fri Oct 16** | 18 |
| **M4** | Makes Decisions — T, turn, dead end | **Mon Oct 26** | 21 |
| **M5** | Handles the Course — obstacle + gap | **Fri Nov 6** | 25 |
| **M6** | Finds the Zone — full run, stops at the zone | **Fri Nov 13** | 28 |

**Late/re-demo window:** the exam block, **Tue Nov 17, 1:30–3:30**.

---

## How this differs from the relative-time draft, and why

**Demo periods are shared now, because the roster is five.** Periods 13 and 18 carry no new flip.
Periods 6 and 21 carry a lesson *and* a demo: five students demonstrating "drives straight and a
measured distance" is about twenty minutes, not sixty-five, and the recovered time is what pays for
L02's second period.

**L02 gets two periods (ruled S199).** Its pre-class read is **about 8,300 words, §1–§5** — the heaviest in
the term — and it previously had one period on a two-day turnaround. It now has Sep 11 and Sep 14.
L03 slid to Sep 16 and Sep 18 to pay for it, with the M1 demos at the end of Sep 18.

**L02 §1 is assigned to the room, not to the night.** Its four warm-ups are timed mystery programs
run under "work independently, no asking for help," closing in a debrief discussion — they do not
survive being read at home, because a student who has already seen the answers has nothing to be
stuck about. So the Sep 11 flip is **§2–§5**, and the reading quiz that day draws nothing from §1.
**This is a scheduling fact and it is fixed here rather than in the lesson:** Bible §3.1 keeps
calendar canon out of the book so an adopter can run a different length, and "we do these together
in class" is calendar canon. The book is right as written; the assignment was wrong.

**The cost of that slide, named:** L03 no longer has a period of cushion before M1. It is taught and
demonstrated inside the same fortnight, with the demo on the back half of its second period. **If
TRIM tuning drags on Sep 18, M1 is what slips.** Watch it; the fallback is to demo the stragglers on
Sep 21 rather than to move the pinned date.

**The two short periods are used, not fought.** Sep 4 (25 min) is intro only; it cannot carry a
lesson. Sep 25 (30 min, Family & Alumni Weekend) is a declared buffer — a half period is exactly
enough for catch-up and a materials check, and not enough to start anything.

**Oct 9 is a normal class (ruled S199 — no Fall Midterm, no tests).** It was previously held soft on
the assumption of a distracted room. It is now a full period, which is the only extra teaching time
the L07/L08 stretch gets.

**L13 is real, but it is thin.** It gets period 27, one period, immediately before the last class.
That is the cost of a 13-lesson Fall scope in 28 periods, and it is the first thing to watch in the
first run. If L12 or L13 slips, M6 slips into the exam block — which is why the exam block is named
as the re-demo window rather than held in reserve.

**The tight stretch is periods 14–18 (Oct 7–16): L07 and L08 back to back**, the two heaviest lessons
in the course, with Long Fall Weekend immediately after. Watch this fortnight. If anything is going
to break, it breaks here.

---
*Dated against the Fall 2026 block schedule, last updated 8/4/2026 · D block · verified 29 meetings / 1,865 minutes*

---
*Dated against the Fall 2026 block schedule (last updated 8/4/2026) · D block · 29 meetings / 1,865 minutes, reconciled twice · v2.1*
