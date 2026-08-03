# Visual design — warm earth, five groups, expandable rail

**Session 109. Ruled in conversation, nothing applied. This document exists so the decisions
survive the session.**

> **⚠️ SUPERSEDED IN PART, S110 — see `ZUMO_S110_VISUAL_RULING.md`.** §2's warm-earth
> palette table is replaced: DJ ruled a sun-faded palette whose bands come from Heritage
> canon. Warm earth measured **1 of 6 bands within 20° of a canon hue**; the replacement
> measures 5 of 6. **Everything else in this document stands** — colour is not a code, the
> six groups, the rail, the `<details>` mechanism, the numbers-off-the-nav ruling, the
> measured cost, and all six open items in §4. Annotated, not rewritten, per §26.7.

Written per §24.13, canonized earlier in this same session: a set that lives only in prose is not
recorded. Six linked decisions were made here and every one of them existed only in chat until
this file. Every hex below was contrast-checked in code, not chosen by eye.

---

## 1. What was ruled

| # | decision | DJ |
|---|---|---|
| 1 | **Warm earth palette** — specimen A of three | *"I like the look of A best"* |
| 2 | **Not the current colours** — B rejected *because* it resembles today | *"I don't like the colors on the current book"* |
| 3 | **WARNING stays a red tone** — the one place colour carries meaning | *"warning has to be a red tone"* |
| 4 | **Nav collapses to five groups**, students scroll within a group | *"Kids link into the grouping… they can scroll"* |
| 5 | **Troubleshoot keeps its own pill**, unnumbered | *"keep trouble shooting seperate 6th pill"* / *"remove 8. infront of"* |
| 6 | **Groups expand** to reach an individual section | *"allow them to be expanded"* |
| 7 | **No section numbers in the nav** — words only; numbers stay on the page | *"get rid of all the section numbers in the drop down menu. Keep them in the site"* |

**And the ruling underneath all of them, which reframes everything:** DJ, S109 — *"I'm not
expecting the kids to memorize that burgandy is note, red is warning. I just want the book to be
visually appealing and not boring."*

**Colour is not a code.** The label on every callout already says `WARNING` or `KEY TERM` in
words; swapping the colours between blocks loses nothing. Therefore families may SHARE colours,
the palette can be small, and **family count is an authoring question, never a palette question.**
The only exception is WARNING red, which is cultural rather than learned.

## 2. The palette

Six groups. Band = the section cap. Tint/text = callouts sitting inside that group.

| group | band | tint | text | white on band | text on tint |
|---|---|---|---|---:|---:|
| Theory & Concepts | `#844A31` | `#F2E6E0` | `#5B3322` | 6.99 | 8.84 |
| Hardware & Code | `#6D572A` | `#EFEADC` | `#4B3B1D` | 6.89 | 8.99 |
| Testing | `#48602B` | `#E7EEE0` | `#31421E` | 7.04 | 9.18 |
| **Troubleshoot** | `#A34A32` | `#F6E9E4` | `#5C2A1A` | 5.86 | 9.82 |
| Challenges | `#2E615D` | `#E2EEEC` | `#204441` | 7.04 | 9.00 |
| Wrap Up & Reference | `#824664` | `#F1E7EB` | `#5A3145` | 6.98 | 8.86 |

Minimum ΔE between the six bands: **15.1**. Every pair clears the 4.5 contrast floor with room.

**Fixed regardless of group:**

- **WARNING** — `#FCEBE9` on `#C0392B`, text `#5C1A13`, contrast 11.29. Never reassigned.
- **Headings (h3/h4)** — bronze `#725637`, contrast 6.77. This **fixes a live defect**: today's
  heading colours run 3.15–4.92 and **341 of 814 heading uses are below the 4.5 floor**.
- **Body** `#1d1d1f` · **code block** `#1e1e1e` / `#d4d4d4` / comment `#6a9955` (§22, unchanged).

**Troubleshoot's rust sits ΔE 19.5 from WARNING's red** — near enough to read as alert, far
enough not to be confused with it. That was checked, not assumed.

Within a group, member sections step darker (≈6 Lab L* per step) so §7 is distinguishable from
§8A while still reading as one region.

## 3. Navigation

**Six pills in a fixed vertical rail on the left**, replacing the sticky horizontal nav.

- Five pills are `<details>` groups that expand to their member sections.
- **The rail carries WORDS ONLY — no section numbers anywhere in it.** The page keeps its
  numbered banners. The split is deliberate: **the nav is for finding, the page is for referring
  to.** This also RESOLVES open item 3 as it was first written — with nothing numbered in the rail,
  Troubleshoot is no longer the sole exception, so the nav is internally consistent and only the
  nav-vs-page difference remains, which is now intended rather than accidental.
- **Troubleshoot is a direct link, unnumbered** — it is not a step in the sequence, it is where a
  student goes when the build is red and they are under time pressure mid-class.
- The 16-lesson strip becomes a **4×4 grid** at the foot of the rail. Stacked as a column, 32
  links run ≈960px and overflow the viewport; as a grid it fits.

**`<details>` is the mechanism, with no JavaScript.** It works with JS disabled, has native
keyboard and screen-reader support, and the book already contains 403 `<details>` elements, so
students meet the interaction in Lesson 1.

### Cost, measured not estimated

- **`css/book.css`: ~4 rules.** `.nav` is ONE class with ONE rule (`position: sticky; top: 0`).
  Fixed-left plus a `.page` left margin, inner flex rows to columns, strip to grid.
- **Lesson files: zero.** The markup already carries the structure — 32 links in grouped
  containers. **This is the S103 migration paying off**: before it, this was 16 files and a gate
  fight.
- **A media query is mandatory.** Below ~700px a 150px rail eats a phone. It must collapse.
- `css/book.css` is GENERATED (§24.12) — this is a change to `build_css.py` plus a regenerate,
  then the S108 staging cycle before any md5 is presented.

## 4. Open, and deliberately not decided here

1. **Nav `<details>` carry no `data-reveal`.** The AI Tutor queries `<details>` and §20.1 strips
   by type, so nav elements would be a new untyped case. **§25.12 exists because exactly one
   untyped `<details>` slipped through before.** Needs a ruling before build.
2. ~~**`div-d-flex-2` scope unverified.**~~ **MEASURED S110 — safe to flip, but flip TWO
   classes, not one.** `div-d-flex-2` is used 7 times in 7 lessons and every one is the nav
   (L02–L08); there is no over-reach. But the nav is split: L01 and L09–L16 use
   **`div-ai-center`** instead, 9 uses in 9 lessons, also nav-only. The two rules differ by a
   single declaration, `align-items: center`, which was rendered both ways against the real
   14-anchor L09 nav and is **pixel-identical** — inert here. (Control: the same comparison
   flipped to column changed the block 54px → 378px, so it can detect a difference.)
   **Therefore §3's cost stands with one correction: the rail is TWO selectors, not one, and
   lesson files remain zero.** Unifying them would mean editing 9 lessons to drop an inert
   declaration, which costs more than writing the selector twice.

   *Recorded because it nearly became a wrong finding:* a first pass matched `div-ai-center`
   with a `\b` boundary, which also matches inside **`div-ai-center-2`** — a different class
   carrying L10's five MYSTERY headers — and reported five phantom non-nav uses. `-` is not a
   word character. Class audits must match whole class tokens, never substrings (§24.6c).
3. ~~**§8's in-page banner still reads "Section 8"** while the nav says "Troubleshoot".~~
   **RESOLVED S109 by ruling 7** — the nav carries no numbers at all, so the nav/page split is
   uniform and deliberate rather than a single inconsistency. Kept here as the record of why.
4. **"Testing" swallows §8A Concepts**, which is deep-dive teaching, not testing. The existing
   PART 3 name was already `Testing & Challenges`; grouping makes the imprecision more visible.
5. **§6.5's "nav button count is 12–14" becomes obsolete**, not violated. Needs retiring, not
   arguing with.
6. **Callout tints follow their section group** in these specimens. The alternative — fixed
   book-wide tints — is calmer but less varied. Unruled.
7. **Heritage Blue.** Warm earth is the furthest of the three specimens from RoboLore canon, so
   book and brand would look unrelated. DJ chose warm earth knowing this; recorded, not reopened.

## 5. Names come from canon, not from me

The five group names are the **existing PART banner titles** in `gen_part_banners.py` —
`Theory & Concepts` · `Hardware & Code` · `Testing & Challenges` · `Challenges` — plus the
previously unnamed §10+ group, here called `Wrap Up & Reference`.

Invented alternatives (`LEARN IT / BUILD IT / TEST IT / PROVE IT`) were drafted and **rejected**:
the book would then hold two vocabularies for the same five things, which is precisely the §4.1
defect that once gave the word "Challenge" three meanings.

---

*Session 109 · every hex contrast-checked in code · nothing applied · recorded per §24.13*
