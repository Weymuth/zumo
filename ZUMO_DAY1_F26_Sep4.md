# Day 1 — Friday, September 4, 2026 · 2:05–2:30 PM · D Block
### Robotics · Zumo 32U4 · Mercersburg Academy · 25 minutes

> **Verified against the Fall 2026 block schedule.** D block meets 29 times; this is meeting #1 and it
> is a 25-minute opening-week period. The next D block is **Wednesday, September 9, 9:50–10:55** — a
> full 65 minutes. There is no D block on September 8.

---

## The 25 minutes

| min | what | why it's here |
|---|---|---|
| **0–4** | **Hand out the hardware.** Robot, USB cord, jumpers, batteries. Sign-out sheet — `ZUMO_DAY1_SIGNOUT_F26.md`, printed — this robot is theirs all term and comes to every class. | They cannot do the homework without it, and this is the only thing today that physically cannot be done later. |
| **4–9** | **How this class works, in one minute each:** you read before class · a short quiz opens the door · you build during class · seven milestones you demo. | Sets the expectation that reading is not optional. Do not explain the grade breakdown — that's the syllabus's job. |
| **9–13** | **Where things live.** Canvas (quizzes, submissions), **weymuth.github.io/zumo** (the book), the Project Maker (starting code). Put all three on the board. | If they can't find the book tonight, the homework doesn't happen. |
| **13–15** | **Everyone open the book, right now.** Phone or laptop, whatever is in their hand: go to **weymuth.github.io/zumo**, click Lesson 1, and read the first heading out loud. Watch all five screens. Nobody leaves until the page is up. | Turns the period's one unverified assumption into a verified one. A typo'd URL or a blocked page costs a student the whole weekend, and it costs two minutes to find out here. |
| **15–20** | **The assignment.** Read it out. Say the due time out loud: **before 9:50 AM Wednesday.** | The single most important five minutes of the period. |
| **20–25** | **Questions**, and the one warning: *if your laptop isn't ready Wednesday, you'll spend Wednesday fixing it instead of driving your robot.* | Turns a soft deadline into a concrete cost they can picture. |

*Timed for a five-student roster (ruled S199). Handing out five robots is about four minutes, not
eight; the recovered time went to the book check and to questions. If somebody has no device on
them at minute 13, pair them with a neighbour's screen — the point is that every student has seen
the page load once, not that each did it alone.*

**Not today, and on purpose:**
- **No PlatformIO check in class.** Not because there isn't time — because **there is nothing to
  check.** The install IS Assignment 1; on Friday afternoon no student has done it yet. The
  toolchain check belongs in Wednesday's first five minutes, where the plan already puts it.
- **No TDP notebook copy.** It's a two-minute Google Doc action that would dilute the one job. It belongs on Wednesday.
- **No syllabus walkthrough.** Post it; don't read it. They'll read it when the first milestone is due.

---

## Assignment 1 — due before class Wednesday, September 9

> **Read Lesson 1, Sections 1 through 5, and get your laptop working.**
>
> **1. Read** — weymuth.github.io/zumo → Lesson 1, Sections 1–5. About 6,000 words.
> **2. Install** — §4 walks you through Visual Studio Code, Git, and the PlatformIO extension. All three.
> **3. Take the Lesson 1 reading quiz in Canvas.** It closes when class starts Wednesday.
>
> Bring the robot, the cord, the jumpers and charged batteries.

**Why the assignment stops at §5 and not the whole lesson.** L01 is about **14,300** words. Sections 1–5 are
**5,618** — the concepts, the install, and a read-through of the program they'll build. Sections 6–7
are the build-and-upload steps, which is exactly what Wednesday's 65 minutes are for. Section 9 is
the challenges, which is another **3,927** words and is not reading, it's work.

*Measured at S199 on `Lesson_01.html` v03.32.2, rendered text between the `section-N` anchors, by
a block-aware tokenizer — a separator at block boundaries only, so `<strong>TRIM</strong>ming` stays
one word and two list items stay two. **Word count is method-dependent to about 2%; treat these as
"about," not as exact.** The figures printed here before S199 (14,714 / 5,993 / 5,686) were not method
noise — §9's was 41% high. No instrument in the tree derives a word count, which is why they went
unguarded. Re-measure rather than copy them forward, and say which tokenizer you used.*

**Why the install is the assignment and not a class activity.** It's the one task that needs no robot,
fails in a dozen laptop-specific ways, and can eat a whole period. Five days and an open lab absorb
that; a 65-minute Wednesday does not. If the toolchain is up Wednesday morning, M1 stays on schedule.

**Building the Canvas quiz: the quiz is over the READING, not the build or the challenges** (ruled
by DJ, S199). §6, §7 and §9 are class work and nothing is drawn from them. **Eight questions are
built and importable** — `ZUMO_L01_Reading_Quiz_CANVAS_QTI.zip`, with `ZUMO_L01_Reading_Quiz.md` as
the by-hand fallback. Five to eight questions is a gate, not an exam.

Of the bank's 79 questions, 43 name a §1–§5 heading — 18 in §1–§4 and 25 in §5 — but **40 cite
§1–§5 and nothing else**, and 40 is the pool. The other three reach outside the assigned reading
(§8 once, the Quick Reference twice).

---

## Wednesday, September 9 · 9:50–10:55 · what Day 1 makes possible

Toolchain check in the first five minutes, then build and upload the first program, run the test
sequence, and make the TDP notebook copy. That period only works if Assignment 1 actually happened —
which is why today's last three minutes are the warning, not the syllabus.
