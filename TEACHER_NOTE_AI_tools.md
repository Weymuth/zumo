# Teacher Note — AI Coding Tools, 2026 Comparison
### For `ZUMO_Resource_Section_WORKING.md` · teacher-side, NOT student-facing

---

## The test

The same coding challenge was given to four AI assistants and evaluated against
**this** codebase — Zumo 32U4, Pololu library, the book's own conventions.

**Result (DJ, 2026):**

| Rank | Tool | Note |
|---|---|---|
| 1 | **Claude** | The only one that reliably produced code that worked on this robot |
| 2 | Grok | Second best; used for per-lesson read-through reviews (Bible §—, external review) |
| 3 | Gemini | |
| 4 | ChatGPT | |
| — | GitHub Copilot | Not ranked in this test — see below |

**Copilot is a separate category.** It is GitHub's (Microsoft-owned) product and
is not a single fixed model — the engine behind it has changed over time and now
offers a choice of models. More importantly, its failure mode is different in
kind from the four above: it is **inline autocomplete**, so it inserts code into
the file without being asked and without reasoning. See the incidents below.

---

## Why this is recorded here and not in the student book

The ranking is **real evidence** — same challenge, same codebase, four tools —
but it is a **snapshot**. These tools change monthly, and a published ranking
would be wrong at some point during the book's life. A student who finds the
book wrong about something checkable discounts it on things they cannot check.

**What the student book says instead** (L01 §3.1): use the course tutor, because
a general chatbot does not know this robot has 75:1 gearmotors, a 21×8 OLED, or
that pins 20 and 4 are shared. That claim is durable and gives a *mechanism*
rather than an authority ranking. The Claude choice is stated with an explicit
2026 date stamp so it reads as history, not as a permanent verdict.

---

## The documented autocomplete incidents (S40)

These are the concrete cases behind the L01 §3.1 hard warning:

- **`setMotorPower()`** — invented. Does not exist in the Zumo32U4 library.
- **`set motorSpeed()`** — invented, and with a space in the identifier.
- **`pololu/Zumo32U4@^1.3.0`** — wrong library version pin injected into
  `platformio.ini`. Correct pin is `pololu/Zumo32U4@2.0.1`. Breaks the build in
  a way that reads as student error.

The real function is **`setSpeeds()`**.

**DJ's fix at the time:** VS Code Command Palette → **"Disable AI Features
(Workspace)"** — switches autocomplete off for the Zumo folder only.

⚠️ **Claude's own output is subject to the same rule.** In S40 Claude supplied
the wrong lib pin (`1.3.0`) from memory. Book canon: grep generated code against
the live library source before trusting it, regardless of which tool produced it.

---

## The distinction the book teaches

**Chat AI** — you ask, you get an answer with reasoning, you judge it before
using it. Allowed and encouraged.

**Inline autocomplete** — inserts into your file, in grey text, looking exactly
like something you typed. Never asks. Turned off for this course.

Students are learning what the robot's commands *are*. A tool that types them —
sometimes correctly, sometimes not — removes the thing they came to learn and
hands them a debugging problem they do not yet have the tools to solve.

---
*Teacher note · recorded S54, July 2026 · source: S40 session findings*
