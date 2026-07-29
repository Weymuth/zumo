# ZUMO — S89 HANDOFF (written at S88 close · paste at top of Session 89)

## Session open ritual (do this without being asked)
1. `git clone --depth 1 https://github.com/Weymuth/zumo.git`
2. Read `LIVE_ZUMO_TEXTBOOK.md` — verify date / status / versions.
3. `grep -oE "Bible version: v[0-9.]+" ZUMO_SUPER_BIBLE.md`
4. `python3 book_gates.py` · `python3 pill_sweep.py --audit lessons/Lesson_*.html` · `python3 lesson_inventory.py`
5. **Every version in this handoff is a LEAD. Grep the files. The files win.**

---

## LIVE AT S88 CLOSE — NOTHING CHANGED

**S88 WAS A DECISION SESSION. ZERO FILES WERE EDITED, ZERO PUSHED.**
Verified at open, unchanged at close:

Bible **v8.76** · book_gates **v1.20 (32 gates, 32/32 PASS)** · gen_bonus_banner v1.2 ·
lesson_inventory v1.0.5 · tutor v1.1.0 · Maker v2.45.1 · pill_sweep v1.0 · Harness v3.0

L01 v03.10.4 · L02 v03.2.0 · L03 v03.16.0 · L04 v04.9.1 · L05 v04.11.1 · L06 v04.14.0 ·
L07 v04.10.0 · L08 v04.9.0 · L09 v05.7.0 · L10 v02.7.0 · L11 v02.9.0 · L12 v01.10.0 ·
L13 v02.9.0 · L14 v02.11.0 · L15 v02.8.0 · L16 v02.5.4

Census identical to S87: lines 39,865 · headings 1,025 · anchors 174 · fences 174 · part 64 ·
constructs 171 · mystery 56 · reveals 403. pill_sweep 16/16 SWEPT, 0 old pills.

**EVERYTHING BELOW IS APPROVED AND UNWRITTEN. That is the §12.4 exposure — act on it first.**

---

# PART 1 — THE ROBOLORE BOOK COMPONENT STANDARD

## Identity (DJ ruled)
- **Title:** RoboLore Book Component Standard
- **File:** `BookComponentStandard.md`, **zumo repo root**, beside the Bible (Bible §12: everything lives in the repo)
- **Conformance stamp:** `RoboLore Book Component Standard v01.0.0` — applied only once the standard exists
- **NOT** `BookComponentAndLessonTemplateStandard.md`; **NOT** in RoboLore; `BOOKS/` folder cancelled
- Written book-agnostic. Zumo appears as illustration, never as the rule.

## Scope
**Sections are NOT components.** TEST IT (§7) and CHALLENGES (§9) are sections; PART banners and
section fences stay with the anchor-spine generators and byte gates (§6.8, §6.8a).

**22 callout families.** GPT's original list of 13 was missing 12 and mis-typed 2.

## Versioning (DJ ruled, then re-confirmed)
RoboLore converts to Zumo's scheme: `01.00.00` → `v01.0.0`. **One system.**
GPT argued for keeping both (RoboLore MINOR ≠ Zumo moderate; PATCH ≠ minor). DJ overruled twice.
The standard names the tiers explicitly so they cannot drift:

```
v#      major     — structural change to meaning or role
v#.#    moderate  — approved addition or expanded rule
v#.#.#  minor     — correction that does not change the decision
```

Zumo lesson HTML additionally carries §5b delivery mechanics — not a second scheme.

---

# PART 2 — THE PALETTE (APPROVED)

Eight roles derived from Heritage Blue. Backgrounds = 10% accent mixed into Parchment `#F5F2E9`.
Body text always Deep Navy `#0B1A2E` (≥12.7:1 on every tint).
Authored as **interface-support colours**, which `ColorPalette.md` explicitly permits.

| Role | bg | border | title | title:bg |
|---|---|---|---|---|
| slate | `#E3E2DC` | `#3D5266` | `#364A5E` | 7.04 |
| bronze | `#E9E4D8` | `#7B6240` | `#6A573D` | 5.44 |
| brass | `#F1EADC` | `#C9A463` | `#6A573D` | 5.44 |
| green | `#E3E4DA` | `#3F6B52` | `#375F4D` | 5.63 |
| amber | `#EAE4D5` | `#8A6420` | `#775922` | 5.12 |
| red | `#EAE0D6` | `#8C3A2E` | `#79352E` | 6.83 |
| purple | `#E6E1DE` | `#5B4B7A` | `#4F446F` | 6.78 |
| navy | `#DEDCD6` | `#0B1A2E` | `#0B1A2E` | 12.75 |

Brass fails as a title colour (2.57:1) — exactly as `ColorPalette.md` warns — so DO THIS NOW and
MY PLAN take a brass border with a bronze title. **The palette bent to the standard, not the reverse.**

## Geometry — UNCHANGED from live
```
box:   background-color: {bg}; border-left: 4px solid {br}; padding: 15px; margin: 20px 0; border-radius: 4px;
title: font-weight: bold; margin-bottom: 8px; font-size: 1.05em; color: {ti};
```
This is byte-identical to the live callout shape. **The change is a repaint, not a redesign.**

## Mechanism
Canvas strips `<style>` and `class=` (verified: 0 `<style>`, 0 `class=`, 24,174 inline `style=`),
so output is complete inline HTML **generated from one table** — the `gen_bonus_banner.py` /
§4.5a pattern. Prototype `gen_component.py` v1.0 was written and run in S88; re-author it.

---

# PART 3 — THE ICON SET (APPROVED, 45 MARKS)

**Bootstrap Icons — MIT, 2,078 icons, 16px grid, outline + fill variants. ONE library, ZERO exceptions.**
Keep the MIT `LICENSE` file in `images/icons/`. Ship as `<img>` per the BrainGear precedent
(`height: 1.35em; vertical-align: -0.3em`), pre-coloured per role — `currentColor` does not work
through `<img>`. Generated from the same table as the callouts.

**Heroicons was the earlier recommendation and was REVERSED.** Bootstrap has 6× the coverage and
outline/fill pairs; every Heroicons compromise dissolved (`map`→`compass`, `viewfinder-circle`→
`bullseye`, `variable`→`braces`, `language`→`journal-bookmark`, and `hammer`, which Heroicons lacks).

## The 22 callout families
| Family | Icon | Role |
|---|---|---|
| LEARN | `book` | slate |
| NOTE | `info-circle` | slate |
| EXPLANATION | `chat-square-text` | slate |
| BUILDS ON | `arrow-repeat` | slate |
| WHERE THIS GOES | `rocket` | slate |
| KEY TERM | `key` | bronze |
| GLOSSARY | `journal-bookmark` | bronze |
| INSIGHT | `stars` | bronze |
| DO THIS NOW | `play-circle` | brass |
| MY PLAN | `pencil-square` | brass |
| TIP | `lightbulb` | green |
| HINT | `compass` | green |
| IF YOU'RE STUCK | `life-preserver` | green |
| CHECKPOINT | `check-circle` | green |
| ANSWER | `unlock` | green |
| WARNING | `exclamation-triangle` | amber |
| COMMON PITFALLS | `slash-circle` | amber |
| SAFETY | `shield-exclamation` | red |
| BRAIN CHECK | `bookmark` / `bookmark-check-fill` | purple |
| THE LOGIC | `braces` | purple |
| THE GOAL | `bullseye` | navy |
| FINISHED EARLY? | `flag` | navy |

## Everything else
- **Brain Check, two states:** `bookmark` outline Slate `#3D5266` incomplete → `bookmark-check-fill`
  solid Deep Navy `#0B1A2E` complete. **State carried by fill + check + colour — three signals**,
  so §25.10's "never colour-alone" rule is satisfied by construction. Replaces the two
  `BrainGear_*.png` rasters. DJ ruled Heritage Blue over green.
- **Bonus families:** `tools` Practice · `flask` Observation · `bug` Sabotage — build it, test it,
  find what broke. Replaces 🔨 / 🔍 / 🕵️ in `gen_bonus_banner.py`.
- **Challenge card:** `bullseye` Goal · `braces` Logic · `puzzle` Template ·
  `folder2-open` Work-in · `search` Where-to-look
- **Battery §13:** `battery-full` 5,400 · `battery-half` 4,800 · `battery` 4,200 mV
- **Prose markers:** `code` CODE · `hammer` BUILD · `play` TEST · `eye` SEE · `arrow-right-circle` NEXT
- **Systems:** `ticket-perforated` Exit Ticket · `stopwatch` Timer · `chat-dots` Tutor ·
  `box-seam` Maker · `file-earmark-plus` Going Deeper · `images` Image Index ·
  `table` Quick Reference · `journal-text` TDP · `trophy` Milestones

## Collisions resolved (all were live drift, not new)
- **⚠️ ×3** → WARNING `exclamation-triangle` · PITFALLS `slash-circle` · SAFETY `shield-exclamation`.
  **This was the important one** — WARNING and PITFALLS are both amber, so the icon was the ONLY
  separator, and both RoboLore standards forbid meaning carried by colour alone.
- **📖 ×3** → `book` · `info-circle` · `chat-square-text`
- **📝 ×2** → `play-circle` · `pencil-square`
- **🧭 ×2** → `compass` · `life-preserver`
- **eye ×2** → `flask` (Observation) frees `eye` for the SEE marker
- **magnifier ×3** → only `search` survives, on Where-to-look. INSIGHT took `stars`.

## Spiral stars — custom, NOT Bootstrap
Numbering defeats every icon library (no room for two digits inside a star). Purpose-built geometry
stays, repainted on-brand:
```
outer radius 9.6 · inner radius 6.2 · fill #7B6240 flat (gradient REMOVED)
number: font-size 9, bold, #F5F2E9
centring: x=10, y=10, dominant-baseline="central"
two-digit (10–16): x = 9.7  (dx 0.3)
render: 1.1em inline, unchanged
```
The old gold gradient `#FFD34D → #F5A623` is **prohibited** by `ColorPalette.md` and off-palette.
Generated from a rule — 16 hand-drawn files become one function.

---

# PART 4 — THE BUILD BANNER REMOVAL (DJ RULED)

## The finding
Bible §5b says *"BOTH VISIBLE BANNER HOMES ARE MANDATORY: header AND footer."* **Neither half is
true.** There are THREE homes and only ONE is visible:

| Home | Where | Reads | Visible |
|---|---|---|---|
| 1 | HTML comment, line 1 | `v04.10.0` — 3 fields | no |
| 2 | header banner ~line 85 | `Version 04.10` — 2 fields | **yes** |
| 3 | BUILD BANNER comment near `</body>` | `Version 04.10` — 2 fields | no |

Uniform across all 16. **No lesson has a version in its visible footer.**

## Why it survived
The §5b gate is named *"hidden == both visible banners"* and **never checks visibility** —
it regexes the raw file and requires exactly 2 matches of `Version \d+\.\d+`, one of which is
inside a comment. The build banner's own text admits it: *"keeps the §5b two-homes gate honest."*
**Same class as S87's substring-vs-gradient lesson: the instrument could not distinguish the
two states, so it reported a condition it was never testing.**

## The plan
**Delete the BUILD BANNER block from 17 files** (16 lessons + `going_deeper.html`). Survivors:
hidden line-1 comment + visible header.

**THREE gates change, not one — all in the same commit or the book fails:**
| Gate | Now | Becomes |
|---|---|---|
| §5b version | exactly **2** matches, comments included | home 1 + exactly **one visible** match, comments stripped first |
| §5b date | assumes two dated banners | single dated header |
| §25.6 | asserts `BUILD BANNER` **and** `ZUMO Callout Standard` present in all 17 | both assertions removed |

**`ZUMO Callout Standard v1.0 Applied` dies with it.** No such document exists — 18 occurrences,
never bumped, and the only other mention is a passing phrase at Bible line 1193 pointing at §8.
The gate is circular: it asserts a string that exists because the gate asserts it. **The
Book Component Standard is its real successor.**

**Bump:** minor, third digit — the block is invisible, so nothing renders differently and the
visible banner stays put per §5b.

## §5b's own text is also wrong
It states the format as `vXX.XX.XX` / `vXX.XX` then gives `v03.2.5` / `v03.2` as its own examples.
The format string says pad every field; the examples say don't. **The files followed the examples.**
9 of 16 lessons have an unpadded minor (L02, L04, L08, L09, L10, L11, L13, L15, L16).

**DJ ruled: DO NOT CHANGE THE BOOK.** Correct §5b's wording to match live practice:
```
Hidden comment, line 1:   v + major(2-digit) . minor . patch   →  v03.16.0 · v03.2.0
Visible header:           "Version " + major(2-digit) . minor  →  Version 03.16 · Version 03.2
```
Only the major is zero-padded. `v03.2.0` is correct and is **not** a defect.

---

# PART 5 — OTHER S88 RULINGS

- **IMAGE/GRAPHIC numbering — LEAVE ENTIRELY ALONE.** Bible §10 and §17 and `IMAGE_SHOT_LIST.md`
  all rule separate number spaces; matching decimals are permitted by design and *"must not be
  fixed."* No renumbering, no old-to-new map, no reference campaign. Uneven starting points are
  recorded as observed legacy practice. `_v01` asset suffix stays **PAUSED** — separate policy,
  needs its own approval. Zumo asset naming stays; RoboLore's lowercase-hyphen rule gets amended.
- **All caps permitted** — amend RoboLore `Typography.md`, not the book.
- **Mono font stack** — adopt RoboLore's verbatim:
  `"JetBrains Mono", "SFMono-Regular", Consolas, "Liberation Mono", monospace`.
  Canvas strips `<style>` so no webfont loads there and it falls through to Consolas/SFMono —
  **VS Code's actual default, which is what §22 requires.** Renders JetBrains Mono on Pages.
  Both standards satisfied with no compromise. Replaces 2,315 `'Courier New'` + 9 other variants.
- **Code carve-out — OUT OF SCOPE in the standard's own text.** Preserve `#6a9955` and `#f14c4c`
  (§22). Do not reinterpret the ~10,000 VS Code theme literals as brand drift.
- **Robot icons (§21)** — colours to be repicked against Heritage Blue. A goal, not scheduled.
  Not blocking: the five bordered icons were never pushed.
- **Navigation colours are a SEPARATE SECOND BATCH.** Section pills and PART banners run their own
  five-colour group scheme (L03: `#3498db` `#3a7d5c` `#c45d76` `#9b6a9e` `#6c757d`). Callouts and
  nav will look mismatched until both land. Do not fold nav into the component pass.
- **RoboLore repo stays PRIVATE**, not published. It is therefore **ungreppable from the sandbox** —
  anything changed there must be re-uploaded. That is a standing §24.6c exposure.
- **GPT now reads the public repo** at `raw.githubusercontent.com/Weymuth/zumo/main/<path>`.
  Do not send it `newproject.html` (5.2 MB). It can read but cannot run — treat its counts as
  leads, run the command to settle disagreements.

## The 12-icon legend
L01–L10 carry a legend of exactly 12 icons; **L11–L16 have none.** It covers 8 of the 22 families,
declares 4 that are not callouts (CODE, BUILD, TEST, SEE), and omits 14 that ship.
**Bible §6.6 v8.40 claims the guide gained 📘 NOTE and has 13 — it does not. Zero lessons carry 📘.**
The L10/L11 seam is the same one where the FINISHED EARLY pointer stopped and the mono font flips.
**DJ leaned toward full cohesion, so the legend should be regenerated from the table showing all 22 —
but that specific wording was never explicitly ruled. Confirm before writing.**

---

# PART 6 — STANDING QUEUE (carried)

Difficulty-progression audit (L01–L03 easy → consistently harder, DJ's stated big goal) ·
challenge-card redesign Part B (~80–100 cards to the L06 Goal→Logic→Template pattern) ·
Maker batch (bulk starters DL · `?lesson=N` gate · C## labels) · L01 VS Code multi-root step ·
TDP template v3 (A5 Lab Log) · day-by-day grid + syllabus · L03 open items (1000 ms explainer,
modulo explainer, two Coach's Tips, C01/C05/C06 starter `finished`-payload debt shared with
L08/L09/L10) · BC03 weeding criterion (L02 7 items, L07 6, L08 6) · L16 outside the bonus family
(2 cards vs 4, DJ: *"Let's wait."*) · S87's six logged-not-fixed leads (back-to-top drifted three
ways with L10 missing it · bonus card titles drifted four ways · L12 zero `<details>` ·
L15 hint-only reveals · four `data-reveal="mechanism"` blocks reach the tutor · committed `.pyc`) ·
S86's eight PART-seam readings still need re-deriving, not inheriting.

---

# PART 7 — LESSONS FROM S88

- **A GATE THAT CANNOT SEE THE DIFFERENCE REPORTS THE CONDITION IT WAS NOT TESTING.** The §5b gate
  counts `Version X.Y` matches without stripping comments, so a hidden build banner silently became
  the second "visible" banner. Same shape as S87's substring-vs-gradient. **When a gate checks
  placement or visibility, strip what the reader cannot see before matching.**
- **§24.6c PAID THREE TIMES, ALL MINE.** (1) I called S87's "IMAGE/GRAPHIC are separate number
  spaces" wrong after a filename census — **the Bible has ruled it since S33 in three places and I
  had not grepped for it.** GPT caught it by reading the Bible. (2) I reported 17 orphan images;
  the real figure is 14 — `Zumo_Robot_Mark.png` is referenced by relative path and my regex only
  matched absolute URLs. My own sanity check caught it. (3) I read grep line numbers near the end
  of a file and called the build banner a visible footer without checking whether it sat inside a
  comment. DJ caught it with a screenshot. **A container is not its contents; a line number is not
  a location.**
- **A REGEX CHARACTER CLASS THAT EXCLUDES QUOTES SILENTLY TRUNCATES.** `font-family:[^;"']*` returned
  2,724 empty matches because every real declaration contains `'Courier New'`. The correct census
  is 2,315 Courier-first vs 393 Consolas-first. **An implausibly round or empty result is the tell.**
- **THE INSTRUMENT CAN BE THE ANSWER.** Repeatedly this session the productive move was to *render
  the thing and look* rather than argue — the ⚠️ collision, the spiral-star centring, the
  bookmark silhouette registration. DJ's corrections landed on rendered output every time.
- **ASKING A SETTLED QUESTION COSTS TRUST.** I re-opened the versioning ruling because GPT argued
  the other side. DJ had already ruled. **A new argument is not a new decision.**
