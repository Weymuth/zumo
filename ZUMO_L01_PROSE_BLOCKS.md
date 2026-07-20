# ZUMO — L01 Prose Blocks (drafted & DJ-approved S54, Jul 19 2026)
### Status: **APPROVED, NOT YET INSERTED** — all four land in the single L01 v03.3.0 pass

These are the exact HTML blocks as approved in Session 54. Paste verbatim; do not
re-draft. Canvas-compatible (inline styles only, no `<style>` blocks, no `class=`).

**Placement summary**

| # | Block | Goes in | Sets up |
|---|-------|---------|---------|
| 1 | Jim Reekes / the Mac chime | **§5**, immediately after the "📖 LEARN — Sound Is Physics" callout | Challenge 2 |
| 2 | Williams & Spielberg / five notes | **§9**, in the section intro before the challenge cards | Challenge 10 |
| 3 | AI autocomplete hard callout | **§3.1**, at the PlatformIO extension-install step | course-wide |
| 4 | "How You Ask Is Part of the Answer" | **§1**, right after the "Welcome to the club" line | Challenge 1 Part 5 |

Both music stories were **web-verified this session** (Pololu docs, Wikipedia, CNBC
interview coverage, Classic FM, Shmoop). Do not re-litigate the facts without re-checking.

---

## 1. §5 — Jim Reekes (sets up Challenge 2)

Place directly **after** the `📖 LEARN — Sound Is Physics` callout, which ends on the line
about sound being electricity moving air on a schedule.

```html
<!-- CALLOUT: Coach's Tip (Green) -->
<div style="background-color: #f0f7f0; border-left: 4px solid #6b8e6b; padding: 15px; margin: 15px 0; border-radius: 4px;">
    <div style="font-weight: bold; margin-bottom: 8px; font-size: 1.05em;">💡 Coach's Tip: The Two-Second Sound Somebody Fought For</div>
    <p>You are about to type a number and make a sound. It is worth knowing that somebody, somewhere, agonized over a sound just like this one.</p>
    <p>In the early 1990s an Apple engineer named <strong>Jim Reekes</strong> could not stand the Macintosh startup chime. The problem was not that it sounded bad &mdash; it was that Macs crashed constantly, and the same family of tones played when they died. People had learned to associate the startup sound with failure. Turning your computer on made you flinch.</p>
    <p>So he went home and recorded a new one on a synthesizer in his living room: a single C major chord, played with both hands stretched as wide as they would reach. Calm. Resolved. The opposite of a crash.</p>
    <p><strong>He did not have permission to change it.</strong> He got it into the machines with help from the engineers who controlled the ROM chips. When Apple found out and told him to take it back out, he refused, and offered a reason why removing it now would be too risky &mdash; a reason he later admitted he made up.</p>
    <p>That chord shipped on Macs for years. Millions of people heard it every morning. One engineer decided two seconds of sound were worth the trouble, and was stubborn enough to win.</p>
    <p>In Section 9 you will change <code style="background:#e8e8e8; padding:2px 6px; border-radius:4px;">440</code> to a number you choose. It is a small thing. So was his.</p>
</div>
```

**Verified facts behind this block.** Reekes recorded it on a Korg Wavestation in his home
studio; it is a C major chord "played with both hands stretched out as wide as possible
(with 3rd at the top)." He wrote it because the older tri-tone chimes were too closely
associated with the death chimes and crashes. Apple did not give him permission; he snuck
it in with help from the engineers in charge of the ROM chips, and refused to remove it
when discovered. It debuted on the early-1990s Quadras.

⚠️ **Do not pin a specific year.** Sources disagree on which Quadra shipped it first
(Quadra 700–800 vs. 840AV). "The early 1990s" is the safe phrasing and is what the block
uses. An earlier draft said "since 1991" — that was wrong and was corrected.

---

## 2. §9 — Williams & Spielberg (sets up Challenge 10)

Place in the **§9 section intro**, before the challenge cards begin.

```html
<!-- CALLOUT: Learn (Blue) -->
<div style="background-color: #e3f2fd; border-left: 4px solid #2196f3; padding: 15px 20px; margin: 20px 0; border-radius: 4px;">
    <strong style="color: #0d47a1;">📖 LEARN — Five Notes That Said Hello</strong>
    <p>In 1977, Steven Spielberg had a problem. He needed humans and an alien ship to talk to each other with no shared language, nothing written, nothing spoken. He went to composer <strong>John Williams</strong> and asked for a musical phrase that could do the job.</p>
    <p>Williams wanted seven notes. Spielberg insisted on five &mdash; any longer, he said, and it stopped sounding like a greeting. What he wanted was <em>a doorbell</em>.</p>
    <p>So Williams asked a mathematician how many five-note sequences you could build from a twelve-note scale. The answer came back at roughly <strong>134,000</strong>. He wrote about 350 of them. Then he and Spielberg sat in a room and listened to them one at a time until they found the one you know.</p>
    <p>Here it is, the version played at Devil's Tower:</p>
    <table style="border-collapse: collapse; margin: 15px 0;">
        <tr>
            <th style="border: 1px solid #ccc; padding: 8px; background: #f8f9fa;">Note</th>
            <th style="border: 1px solid #ccc; padding: 8px; background: #f8f9fa;">G</th>
            <th style="border: 1px solid #ccc; padding: 8px; background: #f8f9fa;">A</th>
            <th style="border: 1px solid #ccc; padding: 8px; background: #f8f9fa;">F</th>
            <th style="border: 1px solid #ccc; padding: 8px; background: #f8f9fa;">F (low)</th>
            <th style="border: 1px solid #ccc; padding: 8px; background: #f8f9fa;">C</th>
        </tr>
        <tr>
            <td style="border: 1px solid #ccc; padding: 8px;"><strong>Hz</strong></td>
            <td style="border: 1px solid #ccc; padding: 8px;">392</td>
            <td style="border: 1px solid #ccc; padding: 8px;">440</td>
            <td style="border: 1px solid #ccc; padding: 8px;">349</td>
            <td style="border: 1px solid #ccc; padding: 8px;">175</td>
            <td style="border: 1px solid #ccc; padding: 8px;">262</td>
        </tr>
    </table>
    <p>Williams pointed out one thing about his own phrase that is easy to miss: <strong>it is left hanging on the fifth note.</strong> It does not resolve. It sounds like a question that expects an answer &mdash; which, in the film, is precisely what it is.</p>
    <p>Two things worth taking from that. A search space of 134,000 got narrowed to one by listening &mdash; the same way you will find your Kp value in Lesson 8 and your PID gains in Lesson 15. And five notes were enough to carry a meaning, because somebody chose them on purpose.</p>
    <p><strong>Challenge 10 asks you to write five of your own.</strong> Not a tune &mdash; a message.</p>
</div>
```

**Verified facts behind this block.** Williams pushed for seven notes; Spielberg insisted on
five, believing anything longer was too long for the simple greeting the phrase was meant to
imply. Williams asked a mathematician to calculate the number of five-note combinations
available from a 12-note scale; the answer was around 134,000. He had already written
roughly 350 candidate phrases, and he and Spielberg chose by ear, listening one at a time.
Spielberg described the motif as "a doorbell." Williams noted the phrase is left hanging on
the fifth note, as if waiting for a response. The Devil's Tower sequence is G, A, F, F an
octave lower, then C.

✅ **HARDWARE-VERIFIED S54.** DJ played all five notes on a real Zumo: *"Sounded exactly like
the movie."* All five audible at even volume, including the low F at 175 Hz (the library
floor is 40 Hz, so it is comfortably in range). **Ship the real sequence — no octave
substitution needed.** An earlier concern that 175 Hz would be too thin on the piezo was
tested and dismissed.

---

## 3. §3.1 — AI autocomplete, hard framing (course-wide)

Place at the **PlatformIO extension-install step in §3.1** — the moment VS Code actually
offers to install Copilot. Catching it at the decision beats explaining it afterward.

```html
<!-- CALLOUT: Warning (Amber) -->
<div style="background-color: #fff8e1; border-left: 4px solid #ffb300; padding: 15px; margin: 15px 0; border-radius: 4px;">
    <div style="font-weight: bold; margin-bottom: 8px; font-size: 1.05em; color: #856404;">⚠️ Turn Off AI Autocomplete — Yes, Really</div>
    <p>VS Code will offer to install <strong>GitHub Copilot</strong> or a similar AI autocomplete. For this course, <strong>turn it off.</strong> Not "use it carefully" &mdash; off.</p>
    <p>Here is what it does. You start typing <code style="background:#e8e8e8; padding:2px 6px; border-radius:4px;">motors.</code> and grey text appears finishing the line for you. Press Tab and it is in your file. It looks exactly like code you wrote.</p>
    <p><strong>It invents functions that do not exist.</strong> Not rarely &mdash; routinely. Asked for Zumo motor code, autocomplete has produced <code style="background:#e8e8e8; padding:2px 6px; border-radius:4px;">setMotorPower()</code> and <code style="background:#e8e8e8; padding:2px 6px; border-radius:4px;">set motorSpeed()</code>. Neither is real. The real one is <code style="background:#e8e8e8; padding:2px 6px; border-radius:4px;">setSpeeds()</code>. It has also supplied the wrong library version number, which breaks the build in a way that looks like your fault.</p>
    <p>You are here to learn what the robot's commands actually are. A tool that types them for you &mdash; sometimes correctly, sometimes not &mdash; takes that away and hands you a debugging problem you do not yet have the tools to solve.</p>
    <p><strong>How to turn it off:</strong> open the Command Palette and run <strong>"Disable AI Features (Workspace)"</strong>. That switches it off for your Zumo folder only. Everything else on your computer is untouched.</p>
    <p><strong>Asking an AI a question is fine</strong> &mdash; that is a conversation, and you judge the answer before you use it. Autocomplete never asks. It just types. Those are not the same thing, and only one of them belongs in your editor this term.</p>
    <p><strong>Which AI should you ask?</strong> Use the course tutor your teacher set up. At the time this book was written, it was built on <strong>Claude</strong> &mdash; chosen after the same coding challenge was given to several AI tools and Claude was the one that reliably produced code that worked on <em>this</em> robot. That was a judgment about this course, this library, and this hardware, and it was made in 2026; the tools change fast, so treat it as what it is &mdash; the best choice available when this was written, not a permanent verdict.</p>
    <p>The reason it matters is not brand loyalty. A general chatbot does not know that your robot has 75:1 gearmotors, a 21&times;8 display, or that pins 20 and 4 are shared between two sensor systems. It will answer confidently anyway. The course tutor knows this book.</p>
</div>
```

**Design notes.** The `setMotorPower` / `set motorSpeed` / `@^1.3.0` examples are the REAL
S40 incidents, which is what makes this concrete rather than abstract. The four-way AI
ranking (Claude > Grok > Gemini > ChatGPT) stays **teacher-side** in
`TEACHER_NOTE_AI_tools.md` — a published ranking would go stale within the book's life, and
a student who finds the book wrong about something checkable discounts it on things they
cannot check. The date stamp turns a perishable claim into history. The final paragraph
carries the durable, mechanism-based reason.

---

## 4. §1 — "How You Ask Is Part of the Answer" (sets up C01 Part 5)

Place **right after the "Welcome to the club. Now let's make your robot say hello!" line**
at the end of §1, where the Hello-World origin story ends.

```html
<!-- CALLOUT: Coach's Tip (Green) -->
<div style="background-color: #f0f7f0; border-left: 4px solid #6b8e6b; padding: 15px; margin: 15px 0; border-radius: 4px;">
    <div style="font-weight: bold; margin-bottom: 8px; font-size: 1.05em;">💡 Coach's Tip: How You Ask Is Part of the Answer</div>
    <p>Your robot has a name, and in Section 9 you are going to go find out what it means. Some of those names are ordinary words &mdash; searching one on its own gets you nowhere useful.</p>
    <p>Watch what a little context does. Search <strong>Marvin</strong> and you get a thousand people. Search <strong>"why would my robot be named Marvin?"</strong> and you land on the depressed robot from <em>The Hitchhiker's Guide to the Galaxy</em>. Same with <strong>Shakey</strong> &mdash; a strange adjective on its own, but ask it as a robot name and you meet the 1966 machine at Stanford Research Institute that was the first to reason about its own actions. Or <strong>Sojourner</strong>, which sounds like a word until you ask, and find NASA's first Mars rover, named for Sojourner Truth.</p>
    <p>The words <em>my robot</em> are doing the work. You gave the search the context it was missing. That is a real skill, and you will use it every time you hit an error message in this course.</p>
    <p><strong>One warning.</strong> When an AI answers, it usually gets the fact right and then keeps going &mdash; guessing about <em>your</em> robot specifically. "Your robot is probably named this because it performs precise tasks&hellip;" It has never seen your robot. It is filling space.</p>
    <p><strong>Take the part that answers your question. Ignore the part that guesses about your situation.</strong> That habit matters more than any single command in this book &mdash; and it comes back in Lesson 3, when an autocomplete tool confidently offers you code for a function that does not exist.</p>
</div>
```

⚠️ **Marvin, Shakey and Sojourner are all OFF the 22-name fleet roster — deliberately.** No
student can find their own answer pre-written in the lesson. They were chosen to cover three
different flavours of the problem: a common first name, an odd adjective, an archaic noun.
Sojourner and Shakey also do double duty by showing a real machine and a historical one, so
students holding **Turing** or **Asimo** do not assume the answer must be a movie.

**DJ verified the search prompt on Google** during this session — `why would my robot be
named ______?` correctly disambiguated Bishop → *Aliens*, Data → *Star Trek*, and Turing →
Alan Turing. The prompt does the work; the earlier plan for "research difficulty tiers" was
**scrapped as unnecessary**.

The closing line forward-references L03's queued autocomplete Coach's Tip, so it sets that
up rather than duplicating it.

---

# 📌 THE C10 REVISION DECISION (recorded)

**The Williams/Spielberg story was MOVED OUT of the Challenge 10 header and into §9 prose
(block 2 above). Same for Reekes: out of the C02 header, into §5 prose (block 1).**

**Why.** Both stories were originally drafted as ~18-line comment blocks inside the
challenge files. In a file a student is trying to work in, that is a wall of comments to
scroll past. In the lesson they are prose — which is what they are.

**It also uses the flip properly.** Students read the story the night before, arrive already
knowing why five notes matter, and the challenge file just says *do it*.

**What replaced them.** The challenge headers collapsed to a two-line pointer:

```
// │ Section 5 told you about Jim Reekes and two seconds of  │
// │ sound. Your turn -- change 440 to a note you pick.      │
```

```
// │ Section 9 told you how John Williams and Steven         │
// │ Spielberg found five notes out of 134,000 -- and that   │
// │ the phrase is left hanging on the fifth note, like a    │
// │ question waiting for an answer.                         │
// │                                                         │
// │ Now write yours.                                        │
```

**Placement ruling (DJ):** the two stories go in **two separate sections** — Reekes in §5
(next to the buzzer physics), Williams in §9 (next to the challenge it sets up) — *not*
combined into one new subsection. §5 was already the longest section in L01, and splitting
them keeps each next to the thing it motivates.

**C10 was NOT given extra experiment questions**, unlike C07, C08 and C11. It is approved
as-is. Candidates exist if wanted later: did anyone guess your message · does yours resolve
or hang like Williams' · reverse your five notes · try seven like Williams originally wanted
· change only the durations to isolate rhythm from pitch.

---

# ⚠️ INSERTION CHECKLIST (S55)

- [ ] All four blocks pasted verbatim — do **not** re-draft
- [ ] Inline styles only (Canvas strips `<style>` blocks and `class=`)
- [ ] Block 2's table uses the canon `<td>`/`<th>` styling already in L01
- [ ] Diff-audit after insertion: every changed line reconciles with an intended edit
- [ ] These land in the **same pass** as the §9 card rewrite, GRAPHIC 1-19 wiring, and the
      Quick Reference note chart → **one** bump, L01 v03.2.7 → **v03.3.0**
- [ ] Re-run the payload gate: L01 must go FAIL(148) → PASS
- [ ] §5b version-in-two-homes: update the visible banner (major.minor) **and** the hidden
      `<!-- Lesson version: v03.3.0 -->` comment

---
*Drafted and approved Session 54, July 19 2026. Nothing inserted yet.*
