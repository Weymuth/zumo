# ZUMO — S107 BANNER RULINGS

**Written at S107, 2 Aug 2026. Every ruling below is DJ's, made this session.
NOTHING HERE IS IN A FILE YET.** The repo is unchanged except for the two root
orphan SVGs DJ deleted at session open (`891127a`, 45/45 gates pass).

This document is the authority for the banner/typography arc until it is applied
and the Bible is amended.

---

## 0. SCOPE — what a "cap" is

237 caps across 16 lessons. Enumerated and reconciled, no orphans:

| id | count |
|---|---|
| `section-1` … `section-10` | 16 each = 160 |
| `image-index` | 16 |
| `glossary` | 16 |
| `quick-ref` | 15 |
| `quick-reference` (L04 only) | 1 |
| `bonus-challenges` | 15 |
| `section-8a` | 14 |
| **TOTAL** | **237** |

`going_deeper.html` carries **zero** caps and is governed separately (§6 below).

---

## 1. TYPE TREATMENT — "E"

Chosen over a lighter alternative that DJ rejected as "too light".
Reference: Apple. Heavy at the top of the hierarchy, quiet below it.

- **Inter**, served the way `index.html` already serves it
- Headings **700**, not `bold`-as-600
- Section banner **1.28em**, h3 **1.42em**
- Negative tracking `-0.021em` on headings, `-0.022em` on h3
- Body `#1d1d1f` (Apple's text black — DARKER than the current `#333`)
- line-height 1.65
- Padding 18px → 26px; callout margins 20px → 26px; table cells 12px → 14px

**UNCHANGED from today's book, deliberately:** 2px section border, 8px radius,
full `1px solid #ddd` table grid. These were tested lighter and DJ rejected it.

**Retired:** `.page { font-family: 'Segoe UI', Tahoma, Geneva, Verdana }` —
Segoe UI is Windows-only, so every non-Windows reader currently gets Tahoma or
Geneva, fonts nobody chose.

**NOT ruled:** the 172 distinct colours in `css/book.css`, the six mono-stack
spellings, the 15 Consolas declarations. §26's repaint remains parked.

---

## 2. BANNER STRUCTURE — "F1"

Every cap becomes **two lines**:

```
EYEBROW    small, uppercase, letter-spacing .1em, opacity .8
HEADLINE   1.28em, weight 700, negative tracking
```

**The derivation rule:**

> **Headline = the most descriptive string available.
> Eyebrow = everything before it.**

- Tailed: eyebrow `Section 3 · Background Theory` / headline `How Motors Make Robots Move`
- Untailed: eyebrow `Section 6` / headline `Build It`

The section NAME therefore sits in the eyebrow when a tail exists and in the
headline when it does not. Visually uniform; structurally two shapes.

**KNOWN FAILURE MODE OF THE MECHANICAL RULE.** Where the tail is the *less*
interesting half, the split promotes the dry part. Found once (L04 §8A,
"Deciding and Repeating — If Statements and For Loops"), fixed by dropping the
tail. Watch for it anywhere else a dash appears.

---

## 3. ICONS — NONE, ON ANY CAP

**DJ ruling: no icons on any of the 237 caps, bonus block included.**

All 237 currently carry a leading emoji; **zero** are bare.

### This supersedes two rules

- **§6.5 (marked LOCKED)** — *"Cap KEEPS the leading icon (📖 🔨 ▶️ ⚠️ 🔑 🏆 📋
  etc.); only the title-block h1 has no icon."*
- **§4.5 (DJ-ruled, S85, v8.72)** — the bonus banner's mark is derived from the
  family (🔨 Practice / 🔍 Observation / 🕵️ Sabotage). `gen_bonus_banner.py`
  generates it byte-exact and must change.
  *The three families survive in the WORD (Extra Practice / Observation /
  Sabotage), which remains on the banner. §4.5's harm argument — that collapsing
  Observation into Sabotage sends a student hunting a defect that isn't there —
  is preserved by the word, not the glyph.*

### What this closes

- The white-mark problem: §7 of `BookComponentStandard` ships marks pre-coloured
  per role, and no role emits white for a colour band. **No longer needed.**
- `bullseye` (THE GOAL) / `book` (LEARN) collisions at §2 / §3
- A third checkmark glyph alongside `check-circle` and `bookmark-check-fill`
- Six doubled-emoji defects (`📚 📚 Glossary` ×2, `🖼️ 🖼️ Image Index` ×2,
  `⚡ ⚡ Quick Reference` ×2) — they vanish with the emoji
- §8's 🔧/⚠️ split, Glossary's 📖/📚 split — resolved automatically

### Released back to the library, unused

`tools` · `code` · `hammer` · `play` · `bug` · `puzzle` · `trophy` ·
`ticket-perforated` · `images` · `stopwatch`. **No download needed** for
`backpack3` or `gift`.

**The 41 generated marks in `images/marks/` remain UNWIRED.** They are the
callout-family vocabulary (26 roster rows documenting 30 live families — the 9
missing rows are the standing S94 queue item). Wiring them is separate work and
is where those released glyphs may still earn a place.

---

## 4. TITLES AND TAILS — ALL 237

### §1 — lesson-specific headline, no eyebrow name

| L | Headline |
|---|---|
| 01 | The True Story of "Hello, World!" |
| 02 | **Reading Someone Else's Code** *(new — was "Mystery Code Challenges")* |
| 03 | **The Crooked Robot Problem** *(dropped "Opening Hook —")* |
| 04 | The Robot That Learned to See |
| 05 | Can Your Robot See? |
| 06 | Can Your Robot Measure Distance? |
| 07 | The Messy Room Problem |
| 08 | The Drunk Robot Problem |
| 09 | The Decision Point |
| 10 | The Thing That Is Not on the Map |
| 11 | The Bug You Have Not Met Yet |
| 12 | The Turn That Never Happened |
| 13 | The Line Has Been Carrying You |
| 14 | **The Robot That Has To Work THIS Time** *(dropped "Introduction —")* |
| 15 | **The Robot That Knows Where It Is and Nothing Else** *(dropped "Introduction —")* |
| 16 | **Sixteen Lessons of Addition** *(dropped "Introduction —")* |

*"Opening Hook" and "Introduction" are authoring labels that leaked into
student-facing text.*

### §2 — `Section 2` / **Learning Objectives** — BARE, all 16

No tail. Same job every lesson; a tail would restate the lesson title.

### §3 — eyebrow `Theory`, written headline

| L | Eyebrow | Headline |
|---|---|---|
| 01 | Theory | **What Makes a Robot a Robot** |
| 02 | **Code Anatomy** | **The Seven Sections of a Program** |
| 03 | Theory | How Motors Make Robots Move |
| 04 | Theory | How Robots See Lines |
| 05 | Theory | **Two Flashlights, Three Ears** |
| 06 | Theory | **From Counts to Centimetres** |
| 07 | Theory | **Why One File Becomes Eight** |
| 08 | Theory | **The Proportional Solution** |
| 09 | Theory | How Intersection Detection Works |
| 10 | Theory | How Obstacle Avoidance Works |
| 11 | Theory | How Gap Crossing Works |
| 12 | Theory | Why the Wheels Cannot Catch Themselves |
| 13 | Theory | Silver Is Invisible to Calibrated Eyes |
| 14 | Theory | The Science of Winning |
| 15 | Theory | Three Tenses |
| 16 | Theory | The Engineer Who Ships |

*L02 takes `Code Anatomy` for accuracy over uniformity — its §3 is the seven
program sections, data types and `if`, which is not theory in the sense the
other fifteen use it. Same reasoning as §4's lesson-specific eyebrow.*

### §4 — lesson-specific EYEBROW (six values) + headline

§4 is not about hardware in six lessons: L01 installs tooling, L09/L10/L13 set
up the course, L15 is `millis()` and `dt`, L16 is the flash budget.

| L | Eyebrow | Headline |
|---|---|---|
| 01 | Setup | Meet Your Robot, Install Your Tools |
| 02 | Hardware | Meet Your Buttons |
| 03 | Hardware | **No Two Motors Are the Same** |
| 04 | Hardware | Meet Your Sensors |
| 05 | Hardware | **The Two-LED System** |
| 06 | Hardware | **Meet Your Encoders** |
| 07 | Planning | **Before You Split the File** |
| 08 | Hardware | **Everything You Already Own** |
| 09 | The Course | **Building Your Testing Environment** |
| 10 | The Course | **Obstacles That Actually Work** |
| 11 | Hardware | **Nothing New to Install** |
| 12 | Hardware | The Sensor That Costs Nothing |
| 13 | The Course | The Rescue Space |
| 14 | Prep | **Passing Inspection** |
| 15 | Timing | The Clock You Have Been Using Cannot Do This |
| 16 | Budget | The Chip Is Full |

Eyebrow values: `Hardware` · `Setup` · `Planning` · `The Course` · `Prep` ·
`Timing` · `Budget`. **"Hardware and Concept Introduction" is RETIRED** — it was
one lesson's variant and made every eyebrow long.

### §5 — eyebrow `Code Walkthrough`, written headline

Name changed from `The Code` (×6) / `Code` (×4) / 5 other variants.

| L | Headline |
|---|---|
| 01 | **The Shape of Every Program** |
| 02 | **Reading a Program Top to Bottom** |
| 03 | **How TRIM Works** |
| 04 | How Today's Program Thinks |
| 05 | **The Order-Proof Trick** |
| 06 | **Waiting Until Something Happens** |
| 07 | **The Eight-File Architecture** |
| 08 | **The Error Signal** |
| 09 | **The State Machine Pattern** |
| 10 | **Four States Become Seven** |
| 11 | **The Function That Changed Its Mind** *(was "The Code, Explained")* |
| 12 | Four Functions and Three Words |
| 13 | **Four Blanks, Four Measurements** |
| 14 | **Why the Limits Are Not Blanks** |
| 15 | **Four Gains, Three Buttons** |
| 16 | The Instrument and the Socket |

*FIXED HERE: L13, L14 and L15 all shipped the byte-identical tail
"The Architecture".*

### §6 — eyebrow `Build It`, written headline

Name normalised from `Build It` ×11 / `Build It: Step-by-Step` ×4 / `Build It!` ×1.

| L | Headline |
|---|---|
| 01 | **Your First Upload** |
| 02 | **The Status Screen** |
| 03 | The TRIM Finder Program |
| 04 | **From Three Sensors to Five** |
| 05 | **The Proximity Display** |
| 06 | **The Distance Dashboard** |
| 07 | **Splitting One File Into Eight** |
| 08 | **The Line Follower** |
| 09 | **The Intersection Handler** |
| 10 | **The Obstacle Detector** |
| 11 | **The Odometer** |
| 12 | **The Honest Turn** |
| 13 | **The Rescue Zone Detector** |
| 14 | **The Competition Build** |
| 15 | **From P to PD** |
| 16 | **The Trade** |

*Six existing tails were step-counts ("Eight Steps", "Six Steps, Each One
Green") — process, not product. Under F1 those would have been the large
headline. Replaced. L03 was the only one already doing it right and is the model.*

*ACCEPTED LOSS: L15/L16's byte-count discipline ("Each One Compiles", "One of
Them Red") is dropped. DJ approved.*

### §7 — Test It for L01–L09, lesson-specific for L10–L16

| L | Eyebrow | Headline |
|---|---|---|
| 01 | Test It | **Watch It Run** |
| 02 | Test It | **The Final Checklist** |
| 03 | Test It | Verification Steps |
| 04 | Test It | The Resolution Experiment |
| 05 | Test It | **The Last Jumper Move** |
| 06 | Test It | **Measuring for Accuracy** |
| 07 | Test It | **The Payoff of One Config File** |
| 08 | Test It | **Finding Your Kp** |
| 09 | Test It | **The Green Survey** |
| 10 | Section 7 | Test & Calibrate |
| 11 | Section 7 | Calibrate |
| 12 | Section 7 · Calibrate | Catch the Encoder Lying |
| 13 | Section 7 | Ladder: Calibration |
| 14 | Section 7 | Ladder: Proof |
| 15 | Section 7 | Ladder: Tuning |
| 16 | Section 7 | Prove It |

*L15 is **Tuning**, not "Turning" — DJ confirmed the typo.*
*L16's tail "The Benchmark Protocol" is dropped.*

### §8 — eyebrow `Troubleshooting`, bare for L01–L13

| L | Headline |
|---|---|
| 01–13 | *(bare — eyebrow `Section 8` / headline `Troubleshooting`)* |
| 14 | **Hunting Intermittent Failures** |
| 15 | **Symptoms and Stress Tests** |
| 16 | Symptoms and the Hunt |

*L04's "Troubleshoot" and L03/L04's "— Systematic Debugging" are dropped.
L14/L15/L16 were three near-duplicate variants of "Symptoms/Stress Tests/the
Hunt"; now three distinct titles.*

### §8A — lesson-specific, ALL noun or gerund phrases

| L | Title |
|---|---|
| 02 | Writing Reusable Functions |
| 03 | Tuning with Calibration Constants |
| 04 | **Deciding and Repeating** *(tail dropped — see §2 failure mode)* |
| 05 | Reading the Proximity Sensor Pair |
| 06 | **Passing Values Into Functions** |
| 07 | **The Multi-File Contract** |
| 08 | Proportional Control Patterns |
| 09 | State Machines & Enums |
| 10 | One State, Many Steps |
| 11 | **Closing the Loop** |
| 12 | **Two Instruments, One Measurement** |
| 13 | **Checking the Claims** |
| 14 | **The Code Freeze** |
| 15 | **Persistent Errors** |

*FIXED: L14 and L15 shipped byte-identical titles. L02/L06/L07 all read as
"functions" and now read as three distinct rungs: write them (L02), feed them
values (L06), share them across files (L07).*

*DJ's proposals "Fine Tuning" (L06), "Get IN SHAPE" (L12) and "Hunt for
intermittent failures" (L14) were checked against section content and did not
match; the intermittent-failure content is in **§8**, not §8A — DJ's instinct was
right, the location was one section off.*

### §9 — `Section 9` / **Challenges** — BARE, all 16
### §10 — `Section 10` / **Exit Ticket** — BARE, all 16
### Glossary — `Glossary` — BARE
### Quick Reference — `Quick Reference` — BARE (L03's ": Lesson 3 Commands" dropped)
### Figures — see §5 below
### Bonus block — §4.5 word retained, mark removed

---

## 5. THE FIGURES RENAME

**"Image Index" → "Figures", and `id="image-index"` → `id="figures"`.**

Blast radius: 16 titles, 16 ids, `book_gates.py:411`, and three Bible passages
(§6.9 ID order at line 280, line 888, the §11 checklist at line 1282).

**DOES NOT TOUCH:** `[IMAGE 3.9]` / `[GRAPHIC 3.9]` captions, filenames,
`IMAGE_WORKLIST.md`, `image_audit.py`, or the two number spaces. The
IMAGE+GRAPHIC → FIGURE merge stays parked until after Sept 8; this makes it
easier, not harder.

*Note L08, L09, L11 and L15 indexes list zero IMAGEs and only GRAPHICs. L15 was
the only one titled accurately ("Graphic Index") and is being renamed for
uniformity. It was right, not sloppy.*

**L04: `id="quick-reference"` → `id="quick-ref"`** plus its one `href`.
L04 is internally consistent today so nothing is broken on the page — but it is
a trap for any future cross-book grep for `#quick-ref`.

---

## 6. going_deeper.html

Six `<details>` entries, dark theme, its own `:root` (12 tokens), Inter already
loaded — the same design system as `index.html`, NOT the lessons.
**Zero caps, zero `id=`, zero `<h2>`.** Nothing in §1–§5 above applies to it.

| # | Title | Anchors |
|---|---|---|
| 1 | How a letter becomes electricity | L02 |
| 2 | What F() is really doing — **PARKED, see below** | L02, L12, L16 |
| 3 | What actually happens when you press Build | L01, L12, L16 |
| 4 | Why eight files instead of one | L07 |
| 5 | **Using Fixed Point** *(was "Fixed point, applied to your own code")* | L08, L12, L15 |
| 6 | What an object is, one level down | L02 |

**HIGHEST-VALUE UNRULED CHANGE: the six entries have no `id` attributes**, so no
lesson can deep-link to one. Every pointer sends a student to the top of a 27 KB
page to hunt.

---

## 7. ⏰ REMIND DJ AFTER SEPT 8 — "What the F()"

**DJ's proposed title for going_deeper entry 2, parked by his own ruling
("let's leave what the F() for now") — RAISE THIS AGAIN AFTER SEPT 8.**

It is memorable and names the actual macro. The open question is register: it
reads as a profanity gag in a teacher-authored textbook for 15-year-olds at
Mercersburg with DJ's name on it, and the book's established voice is dry wit
(*Wheels Lie*, *The Drunk Robot Problem*, *Time Lies, Distance Doesn't*) rather
than swear jokes. DJ knows his school; this is his call, deferred, not refused.

Alternatives if the register is the sticking point: **"What F() Buys You"** or
**"The F() Wrapper"**.

---

## 8. APPLICATION COST — none of this is applied

| Artefact | Change |
|---|---|
| 16 lesson files | banner markup → eyebrow + headline; 237 emoji removed; every title/tail rewritten; Figures id; L04 quick-ref |
| `book_gates.py` | `_fence_title()` must find the section name in BOTH shapes; line 411 `image-index` |
| `gen_bonus_banner.py` | family mark comes off the banner |
| `css/book.css` | regenerated → full §27.8b restore → regenerate → apply `--include-held` |
| `ZUMO_SUPER_BIBLE.md` | supersede §6.5 (LOCKED) + §4.5 mark; Figures id ×3; NEW entry for the eyebrow/headline canon |
| `BookComponentStandard.md` | caps carry no marks |

**Gates that move:** 26, 27, 41, 43, 44, 45, §5b.
**Every lesson takes a MODERATE bump** (visible banner changes → §5b two homes).

**RECOMMENDED: apply to L03 alone first**, re-run all 45 gates, exercise the
stylesheet cycle at one-lesson blast radius, then the other fifteen. This is the
S104 pattern that made the CSS migration safe.

---

## 9. FINDINGS — none of these are visible to any of the 45 gates

1. **Two root orphan SVGs** byte-identical to `images/` copies, dragged in by the
   S106 close push. DJ deleted them at S107 open. The offered orphan gate keys on
   filename patterns (`PUSH_ME*` / `MD5*` / `* (1)*`) and would NOT have caught
   these — the filenames were legitimate. **Re-scope it to: any file outside
   `images/` whose bytes match a file inside `images/`.** `image_audit` already
   computes the hashes.
2. **237 caps carry a leading emoji; zero are bare.**
3. **Six banners render their icon twice** — `📚 📚 Glossary` ×2,
   `🖼️ 🖼️ Image Index` ×2, `⚡ ⚡ Quick Reference` ×2.
4. **L14 and L15 shipped byte-identical §8A titles.**
5. **L13, L14, L15 shipped byte-identical §5 tails** ("The Architecture").
6. **L15 titles its index "Graphic Index"** — accurate, being normalised anyway.
7. **L04 uses `id="quick-reference"`** where fifteen use `quick-ref`.
8. **`going_deeper.html` has no anchor ids** on any of its six entries.
9. **The roster documents 26 families; the live taxonomy has 30.** The 9 missing
   rows are the standing S94 queue item.
10. **`css/book.css` has 172 distinct colours and zero custom properties**, while
    `index.html` and `going_deeper.html` each carry a 12-token `:root`. Two files
    have a design language; sixteen do not.

### METHOD CORRECTION recorded per §24.6c

**`<h3>` count is not a proxy for whether a section has content.** I used it as
one and reported L08 §4, L11 §4 and L13 §3 as "empty". **All three have content**
— 523, 867 and 3,371 characters respectively, structured as tables and sustained
prose rather than subsections. L13 §3 is one of the strongest sections in the
book: it quotes four lines of Pololu library source and walks the
`if (x < 0) x = 0;` clamp to prove silver tape is invisible to calibrated
sensors. Retracted.

**Also retracted:** I called L03's adjacent 8px and 4px callout radii a defect
that "accumulated". **§6.5a rules exactly this** — inline callouts 4px, purple
glossary/term cards 8px. Both were correct and deliberate.

---

## 10. STILL OPEN

- **going_deeper anchor ids** — six entries, unlinkable
- **"What the F()"** — parked to after Sept 8 (§7 above)
- **§26's repaint** — 172 colours, `#f8f9fa` ×641, `#fffbe6` ×87, LEARN/INSIGHT
  sharing `#e3f2fd`, KEY TERM's purple colliding with MY PLAN. Untouched today.
- **The 9 missing roster rows**
- **Wiring the 41 marks** — the change that puts one line system in place of
  every emoji in the book. Not started.
- **L02 §1 whodunit restructure** — DJ tabled to after Sept 8. Three people's
  code, rank by error count. Matches §4.5's Observation family exactly
  (*"nothing is broken; predict, test, explain"*).
- **The seven September-8 images** — DJ deprioritised these in favour of this
  arc. They are still the only deadline-bearing items on `IMAGE_WORKLIST.md`.
