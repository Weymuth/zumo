# RoboLore Brand and Identity Record

**Record compiled:** 2026-08-01  
**Purpose:** Factual export of recoverable RoboLore brand and identity decisions from the available conversations, uploaded files, repository snapshots, packages, and conversation exports.  
**Method:** This record does not redesign, reconcile, or improve the work. Where a fact was not recoverable, it is marked **NOT DISCUSSED** or **NOT RECOVERED**. Where a later instruction conflicts with an earlier approved document, both are recorded.

## Status key

- **APPROVED** — explicitly approved or recorded as approved in an authoritative file.
- **PROPOSED** — explored, drafted, or presented for consideration without final approval.
- **REJECTED** — explicitly rejected or prohibited.
- **SUPERSEDED** — replaced by a later decision, document, or version.
- **NOT DISCUSSED** — no recoverable discussion or decision.

---

# 1. WORDMARK

## 1.1 Approved identity

| Item | Status | Recorded decision |
|---|---|---|
| Wordmark ID | **APPROVED** | `OX-6` |
| Typeface | **APPROVED** | Oxanium |
| Construction | **APPROVED** | All caps: `ROBOLORE` |
| Word division | **APPROVED** | No space between `ROBO` and `LORE` |
| `ROBO` master weight | **APPROVED** | Oxanium `200` |
| `LORE` weight | **APPROVED** | Oxanium `700` |
| Tracking | **APPROVED** | `0` — default font metrics |
| Kerning | **APPROVED** | Default kerning |
| Colour behavior | **APPROVED** | One flat colour; `ROBO` and `LORE` must not be coloured differently |
| Primary production colour | **APPROVED** | Solid black `#000000` |
| Primary brand colour | **APPROVED** | Deep Navy `#0B1A2E` |

The recorded rationale is:

> **ROBO** identifies the category.  
> **LORE** is the distinctive half of the name, so the visual emphasis rests there.

The outlined SVG production files contain paths rather than live font text and do not require Oxanium to be installed.

**Source:** `BRANDING/WordMark.md`, version `01.02.00`, status Approved.

## 1.2 Typeface metrics and licensing

| Property | Status | Exact value |
|---|---|---|
| Source | **APPROVED / RECORDED** | Google Fonts |
| Font format | **APPROVED / RECORDED** | Variable font |
| Weight axis | **APPROVED / RECORDED** | `200–800` |
| Units per em | **APPROVED / RECORDED** | `1000` |
| Cap height | **APPROVED / RECORDED** | `690` |
| Licence | **APPROVED / RECORDED** | SIL Open Font License 1.1 |

The wordmark specification states that outlined logo artwork does not ordinarily inherit the font-file distribution requirements, but also states that this is not legal advice and that licensing and trademark use should be confirmed with qualified counsel.

## 1.3 Completed lockups

### Horizontal lockup

| Item | Status | Exact value |
|---|---|---|
| Role | **APPROVED** | Primary lockup |
| Master file | **APPROVED** | `BRANDING/Assets/Wordmark/robolore-horizontal.svg` |
| Ink width | **APPROVED / RECORDED** | `5027` units |
| Ink height | **APPROVED / RECORDED** | `690` units |
| Spacing | **APPROVED** | Default kerning; no added letterspacing |
| Use | **APPROVED** | Use wherever space permits |

### Stacked lockup

| Item | Status | Exact value |
|---|---|---|
| Role | **APPROVED** | Secondary lockup |
| Master file | **APPROVED** | `BRANDING/Assets/Wordmark/robolore-stacked.svg` |
| Baseline pitch | **APPROVED / RECORDED** | `1030` units — `1.03 em` |
| `LORE` tracking | **APPROVED / RECORDED** | `+36` units per gap |
| Alignment method | **APPROVED** | Both lines match by ink width, not advance width; aligned by ink centres |
| Use | **APPROVED** | Constrained horizontal space or compact composition |

### Vertical lockup

| Item | Status | Exact value |
|---|---|---|
| Role | **APPROVED** | Narrow-format lockup |
| Master file | **APPROVED** | `BRANDING/Assets/Wordmark/robolore-vertical.svg` |
| Arrangement | **APPROVED** | One letter per line: `R O B O L O R E` |
| Baseline pitch | **APPROVED / RECORDED** | `1060` units — `1.06 em` |
| Alignment method | **APPROVED** | Each letter centred by its individual ink bounding box, not advance width |
| Use | **APPROVED** | Book spines, banners, narrow margins, other vertically constrained applications |

### Square lockup

| Item | Status | Exact value |
|---|---|---|
| Role | **APPROVED** | Moderate square applications |
| Master file | **APPROVED** | `BRANDING/Assets/Wordmark/robolore-square.svg` |
| Construction | **APPROVED** | Based on the stacked lockup; centred using complete ink bounds |
| Minimum internal margin | **APPROVED / RECORDED** | `12%` on every side |
| Use | **APPROVED** | App tiles, social avatars, profile images, square promotional graphics |
| Favicon status | **REJECTED as final favicon** | The square lockup is not the final favicon |

## 1.4 Optical-size variants and thresholds

All thresholds refer to **cap height**, not CSS font size.

| Cap height / production condition | Status | `ROBO` | `LORE` | Recorded role |
|---|---|---:|---:|---|
| `24 px` and above | **APPROVED** | `200` | `700` | Master digital variant |
| `16–23 px` | **APPROVED** | `300` | `700` | Small digital variant |
| Below `16 px` | **APPROVED as temporary fallback** | `400` | `700` | Micro digital variant, or future symbol |
| Production methods with spread or registration limits | **PROPOSED / PROVISIONAL** | `400` | `700` | Manufacturing variant pending physical validation |

The micro wordmark is explicitly a temporary solution until a standalone symbol exists. At `16 × 16 px`, the future standalone symbol is preferred over forcing the eight-letter wordmark into the space.

## 1.5 Approved production files

The completed outlined package contains twelve SVG files.

| Lockup | Master | Small digital | Manufacturing | Status |
|---|---|---|---|---|
| Horizontal | `BRANDING/Assets/Wordmark/robolore-horizontal.svg` | `BRANDING/Assets/Wordmark/robolore-horizontal-small.svg` | `BRANDING/Assets/Wordmark/robolore-horizontal-manufacturing.svg` | **APPROVED production package** |
| Stacked | `BRANDING/Assets/Wordmark/robolore-stacked.svg` | `BRANDING/Assets/Wordmark/robolore-stacked-small.svg` | `BRANDING/Assets/Wordmark/robolore-stacked-manufacturing.svg` | **APPROVED production package** |
| Vertical | `BRANDING/Assets/Wordmark/robolore-vertical.svg` | `BRANDING/Assets/Wordmark/robolore-vertical-small.svg` | `BRANDING/Assets/Wordmark/robolore-vertical-manufacturing.svg` | **APPROVED production package** |
| Square | `BRANDING/Assets/Wordmark/robolore-square.svg` | `BRANDING/Assets/Wordmark/robolore-square-small.svg` | `BRANDING/Assets/Wordmark/robolore-square-manufacturing.svg` | **APPROVED production package** |

The production manifest records these canvas dimensions:

| File | Recorded dimensions |
|---|---:|
| `robolore-horizontal.svg` | `5027.000 × 690.000` |
| `robolore-horizontal-small.svg` | `5042.000 × 690.000` |
| `robolore-horizontal-manufacturing.svg` | `5052.000 × 690.000` |
| `robolore-stacked.svg` | `2484.000 × 1720.000` |
| `robolore-stacked-small.svg` | `2501.000 × 1720.000` |
| `robolore-stacked-manufacturing.svg` | `2514.000 × 1720.000` |
| `robolore-vertical.svg` | `564.000 × 8110.000` |
| `robolore-vertical-small.svg` | `564.000 × 8110.000` |
| `robolore-vertical-manufacturing.svg` | `564.000 × 8110.000` |
| `robolore-square.svg` | `3268.421 × 3268.421` |
| `robolore-square-small.svg` | `3290.789 × 3290.789` |
| `robolore-square-manufacturing.svg` | `3307.895 × 3307.895` |

The manifest records zero text nodes in all twelve SVGs. The horizontal, stacked, and square assets contain two paths; the vertical assets contain eight paths.

## 1.6 Approved colour applications

### Preferred applications

| Application | Status |
|---|---|
| Deep Navy `#0B1A2E` wordmark on Parchment `#F5F2E9` or white `#FFFFFF` | **APPROVED** |
| Parchment `#F5F2E9` or white `#FFFFFF` wordmark on Deep Navy `#0B1A2E` | **APPROVED** |
| Solid black `#000000` on white `#FFFFFF` | **APPROVED** |
| Solid white `#FFFFFF` on black `#000000` | **APPROVED** |

### Controlled secondary applications

| Application | Status / condition |
|---|---|
| Slate Blue `#3D5266` on Parchment `#F5F2E9` | **APPROVED — controlled secondary** |
| Antique Bronze `#7B6240` on Parchment `#F5F2E9` | **APPROVED — moderate or large sizes** |
| Warm Brass `#C9A463` on Deep Navy `#0B1A2E` | **APPROVED — moderate or large sizes** |

### Wordmark colour prohibitions

- **REJECTED:** Different colours for `ROBO` and `LORE`.
- **REJECTED:** Gradients.
- **REJECTED:** Shadows, glows, textures, bevels, or three-dimensional effects.
- **REJECTED:** Digital simulated bronze or brass effects.
- **REJECTED:** Placement over low-contrast imagery.
- **REJECTED:** Warm Brass `#C9A463` on Parchment `#F5F2E9`.

Metallic ink, foil, engraving, anodizing, and brushed finishes were recorded as optional production treatments, not changes to the flat master artwork.

## 1.7 Clear space and minimum size

| Rule | Status | Exact value |
|---|---|---|
| Clear space | **APPROVED** | One full cap height around every lockup |
| Delivered master clear space | **APPROVED / RECORDED** | `690 units` |
| Physical minimum sizes | **NOT DISCUSSED as fixed values / PENDING** | Process-dependent; must be established through manufacturing tests |

No text, imagery, borders, or other visual elements may enter the clear-space area.

## 1.8 Prohibitions

The following are **REJECTED / PROHIBITED** for the wordmark:

- Recreating or typing a substitute wordmark.
- Changing the typeface.
- Adding tracking to the primary horizontal mark.
- Inserting a space between `ROBO` and `LORE`.
- Stretching, condensing, rotating, or distorting the mark.
- Colouring `ROBO` and `LORE` differently.
- Applying gradients, shadows, bevels, glows, textures, or simulated metal.
- Pairing it with an invented symbol or icon.
- Placing it inside a badge, seal, crest, or decorative container.
- Adding circuitry, gears, rays, brackets, or ornaments.
- Repeating it in both the header and footer of one instructional graphic.
- Reducing required clear space.

## 1.9 Version history and reversals

| Version | Status | Change |
|---|---|---|
| `01.00.00` | **SUPERSEDED** | Initial approved OX-6 wordmark specification |
| `01.01.00` | **SUPERSEDED** | Added digital size standards, optical-size variants, reverse use, and provisional manufacturing guidance |
| `01.02.00` | **APPROVED — current recovered specification** | Added Heritage Blue applications, confirmed one-colour behavior, recorded completed outlined package, and removed colour development from outstanding work |

The wordmark itself was not reversed after OX-6 approval. The later versions expanded implementation rules.

---

# 2. SYMBOL / LOGOMARK

## 2.1 Current status

| Item | Status | Record |
|---|---|---|
| Standalone RoboLore symbol / logomark | **NOT APPROVED / DEFERRED** | No final symbol was approved |
| Symbol-to-wordmark relationship | **NOT DISCUSSED as a final design / DEFERRED** | Must be resolved only after a symbol exists |
| Combined symbol-and-wordmark lockups | **NOT DISCUSSED as final / DEFERRED** | No approved combined lockups |
| Final favicon | **NOT APPROVED / DEFERRED** | Square OX-6 is only a moderate-size fallback |
| Interim symbol presented as final | **REJECTED** | Explicitly prohibited |

The approved detailed documents state plainly that a standalone symbol has not been selected and must not be improvised.

## 2.2 Evaluation criteria

The historical `Archive/BrandExploration/LogoConcepts.md`, version `01.00.00`, status Draft, last updated `2026-07-26`, listed these criteria:

- Represents RoboLore
- Represents Engineering
- Represents Shared Wisdom
- Represents Curiosity
- Represents Precision
- Represents Accessibility
- Simple and memorable
- Works in one color
- Scales to favicon size
- Looks good on books
- Looks good on apparel
- Timeless
- Unique

**Numerical scores or weighted scoring:** **NOT DISCUSSED / NOT RECOVERED.** The recovered file contains criteria, strengths, and weaknesses, but no numerical score table.

## 2.3 Historical territories explored

### Concept 01 — Compass Gear

- **Status:** **PROPOSED, then REJECTED / CLOSED as a direction.**
- Meaning: gear = engineering, craftsmanship, iteration; compass = guidance, discovery, mentorship, direction.
- Recorded strengths: instantly recognizable; strong symbolism; mechanical; timeless; easy to simplify.
- Recorded weaknesses: risk of appearing too industrial; compass points had to remain subtle.

### Concept 02 — Shared Gear

- **Status:** **PROPOSED, then REJECTED / CLOSED with the gear territory.**
- Meaning: two interlocking gears; mentor and learner; knowledge transferred through motion.
- Strengths: shared wisdom; collaboration; mechanical beauty.
- Weaknesses: common engineering symbol; needed a unique twist.

### Concept 03 — Compass Rose

- **Status:** **PROPOSED, then REJECTED / CLOSED with the compass territory.**
- Meaning: minimalist compass rose built from engineering geometry.
- Strengths: elegant; guidance; exploration.
- Weakness: less obviously engineering.

### Concept 04 — Engineering Compass

- **Status:** **PROPOSED, then REJECTED / CLOSED with the compass territory.**
- Meaning: drafting compass representing precision, design, measurement, engineering.
- Strengths: recognized by engineers; strong educational symbolism.
- Weakness: less connected to robotics.

### Concept 05 — Circuit Path

- **Status:** **PROPOSED; no final approval.**
- Meaning: a flowing circuit trace transforming into another form; knowledge flow, technology, motion.
- Weakness: easy to become generic.

### Concept 06 — Knowledge Bridge

- **Status:** **PROPOSED; no final approval.**
- Meaning: two geometric structures connected by a bridge; knowledge passing between them.
- Strengths: mentorship; accessibility.
- Weakness: hard to simplify.

### Concept 07 — Hidden R

- **Status:** **PROPOSED; no final approval.**
- Meaning: an abstract mark containing a discovered rather than obvious `R`.
- Strengths: memorable; clever; ownable.
- Weakness: may become too abstract.

### Concept 08 — Brain Gear

- **Status:** **PROPOSED; later explicitly prohibited as an improvised identity mark.**
- Meaning: engineering becoming understanding.
- Strength: strong educational message.
- Weakness: similar ideas already exist.

### Concept 09 — Open Codex

- **Status:** **PROPOSED; no final approval.**
- Meaning: an open book whose pages become engineering geometry.
- Strengths: represents learning; potentially unique.
- Weakness: more complex.

### Concept 10 — The Beacon

- **Status:** **PROPOSED; no final approval.**
- Meaning: a geometric beacon; knowledge radiates outward; students become mentors.
- Recorded detailed strengths/weaknesses beyond that summary: **NOT DISCUSSED / NOT RECOVERED.**

## 2.4 Closed gear-and-compass direction

The archived record says the gear, compass, spark, and combined gear-compass directions were explored extensively and then closed.

Reasons recorded:

- **REJECTED:** Gears introduced generic industrial associations and excessive symmetry.
- **REJECTED:** Compass structures repeatedly became conventional navigation emblems.
- **REJECTED:** Combining gear and compass created visual clutter and weakened small-size performance.
- **REJECTED:** The concepts did not produce a mark that felt uniquely RoboLore.

The record permits reconsideration only if a future concept uses such elements in a genuinely distinctive and simplified way.

## 2.5 Additional territories recovered from conversation context

The following were discussed in conversation but are not fully documented in the canonical repository snapshot:

| Territory | Status | Recovered outcome |
|---|---|---|
| Shield | **PROPOSED; no final approval** | Explored; exact elimination reason not recovered |
| Hidden gear / negative-space gear | **PROPOSED; no final approval** | Explored; no approved result |
| Six-point starburst with three large and three small points, rotated `45°` | **PROPOSED, then REJECTED** | Rejected after it evoked a radiation-like symbol |
| Nonagon container for multiple domain icons | **PROPOSED; no final approval** | Explored; no approved result |
| Bronze-gradient three-dimensional concepts, followed by flat variants | **PROPOSED, then SUPERSEDED / REJECTED for core identity** | Core artwork was later locked to flat colours with no gradients or simulated metal |
| “One abstract/object” exercise, including 30 concepts plus 10 more | **PROPOSED** | No final mark selected; exact full list and scoring not recovered |
| Compass motif related to Eagle Scout background | **PROPOSED** | Personal affinity recorded; did not result in approval |
| Symmetry, ratios, balance, precision | **PROPOSED evaluation preferences** | Desired qualities, not an approved symbol |
| Symbol need not visibly depict robotics | **PROPOSED preference** | No final symbol followed |

## 2.6 Explicitly prohibited symbol forms in current standards

The following are **REJECTED / PROHIBITED** as RoboLore identity marks until explicitly approved:

- Gear emblem
- Robot-head logo
- Brain-and-circuit mark
- Monogram
- Crest
- Shield
- Seal
- Badge
- Compass mark
- Circuit-logo device
- Footer medallion
- Mascot
- Substitute logo
- Decorative icon placed before, behind, or integrated with the wordmark
- Any temporary mark created for layout convenience

Instructional icons may depict a gear, speaker, clock, sensor, or robot component only when it explains the lesson and is not styled or positioned as the company logo.

## 2.7 Future-symbol requirements

The historical requirements state that a future symbol must:

- Be tested with OX-6.
- Complement the wordmark without overpowering the emphasis on `LORE`.
- Remain identifiable and reproducible at approximately `16 × 16 px`.
- Not depend on interior lettering or fine detail.

The symbol is intentionally deferred until one of the following occurs:

- A clear functional requirement emerges.
- A distinctive concept develops naturally.
- Favicon or app-icon limitations become a launch blocker.
- The website or product system reveals a specific geometric need.
- Adequate time is available for real vector construction and validation.

## 2.8 Final outcome

**No standalone symbol or logomark was approved.** OX-6 remains the only approved RoboLore identity mark.

---

# 3. COLOUR

## 3.1 Approved Heritage Blue palette

`BRANDING/ColorPalette.md`, version `01.00.00`, records Heritage Blue as approved.

| Colour | Status | Hex | RGB | Primary role |
|---|---|---:|---:|---|
| Deep Navy | **APPROVED** | `#0B1A2E` | `11, 26, 46` | Primary structural colour, dark backgrounds, primary text |
| Slate Blue | **APPROVED** | `#3D5266` | `61, 82, 102` | Secondary structure, supporting text, panels, diagrams |
| Antique Bronze | **APPROVED** | `#7B6240` | `123, 98, 64` | Brand accent, headings, icons, links, crafted details |
| Warm Brass | **APPROVED** | `#C9A463` | `201, 164, 99` | Calls to action, highlights, selected states, emphasis |
| Parchment | **APPROVED** | `#F5F2E9` | `245, 242, 233` | Primary light background and warm reverse colour |
| Black | **APPROVED production neutral** | `#000000` | **NOT DISCUSSED in RGB form** | One-colour artwork and neutral production |
| White | **APPROVED production neutral** | `#FFFFFF` | **NOT DISCUSSED in RGB form** | Reverse and one-colour production |

## 3.2 Recorded meaning and rationale

- **Deep Navy `#0B1A2E` — APPROVED:** technical credibility, stability, and precision.
- **Slate Blue `#3D5266` — APPROVED:** hierarchy without the severity of black.
- **Antique Bronze `#7B6240` — APPROVED:** craftsmanship, accumulated knowledge, and physical making.
- **Warm Brass `#C9A463` — APPROVED:** curiosity, energy, and controlled emphasis.
- **Parchment `#F5F2E9` — APPROVED:** warmth and readability for educational content.

The system was intended to feel “engineered and established” without becoming corporate, institutional, luxurious, or nostalgic.

## 3.3 Recommended composition percentages

| Colour | Status | Typical visual share |
|---|---|---:|
| Parchment `#F5F2E9` | **APPROVED guideline** | `45–60%` |
| Deep Navy `#0B1A2E` | **APPROVED guideline** | `20–35%` |
| Slate Blue `#3D5266` | **APPROVED guideline** | `8–15%` |
| Antique Bronze `#7B6240` | **APPROVED guideline** | `5–10%` |
| Warm Brass `#C9A463` | **APPROVED guideline** | `2–6%` |

These are composition guidelines, not fixed quotas. Warm Brass is intended to remain the rarest colour.

## 3.4 Detailed role definitions

### Deep Navy `#0B1A2E`

**APPROVED uses:**

- Primary navigation and footers
- Large dark panels
- Primary text on light backgrounds
- Preferred brand-colour wordmark
- Book-cover foundations
- Diagrams requiring a strong structural line
- High-priority UI controls when Warm Brass is inappropriate

**REJECTED:** using Deep Navy as a substitute for black in every application.

### Slate Blue `#3D5266`

**APPROVED uses:**

- Secondary text
- Supporting navigation
- Informational panels
- Rules, borders, and diagram layers
- Data-visualization foundations
- Secondary buttons with Parchment text
- Muted backgrounds where contrast remains sufficient

Long body text on dark backgrounds requires a contrast check.

### Antique Bronze `#7B6240`

**APPROVED uses:**

- Short headings and labels
- Links on Parchment
- Icons and line illustrations
- Section markers
- Book-cover details
- Rules and small crafted accents
- Limited wordmark use at generous sizes

**REJECTED:** dominating large areas without a functional reason.

### Warm Brass `#C9A463`

**APPROVED uses:**

- Primary calls to action with Deep Navy text
- Active or selected states
- Small highlights
- Key numbers
- Focus indicators when clearly visible
- Optional foil or metallic production treatment

**REJECTED:** ordinary text on Parchment `#F5F2E9` or white `#FFFFFF`.

### Parchment `#F5F2E9`

**APPROVED uses:**

- Primary page backgrounds
- Reading surfaces
- Cards and editorial panels
- Reverse text on Deep Navy or Slate Blue
- Warm negative space
- Preferred reverse wordmark colour on Deep Navy

**REJECTED:** heavy paper texture or artificial aging as part of the core system.

## 3.5 Approved contrast ratios

The source states that these are WCAG relative-luminance calculations.

| Foreground | Background | Status | Ratio | Approved use |
|---|---|---|---:|---|
| Deep Navy `#0B1A2E` | Parchment `#F5F2E9` | **APPROVED** | `15.61:1` | All text and interface sizes |
| Slate Blue `#3D5266` | Parchment `#F5F2E9` | **APPROVED** | `7.22:1` | All text and interface sizes |
| Antique Bronze `#7B6240` | Parchment `#F5F2E9` | **APPROVED** | `5.12:1` | Normal text, headings, links, icons |
| Parchment `#F5F2E9` | Deep Navy `#0B1A2E` | **APPROVED** | `15.61:1` | All reverse text and interface sizes |
| Parchment `#F5F2E9` | Slate Blue `#3D5266` | **APPROVED** | `7.22:1` | All reverse text and interface sizes |
| Deep Navy `#0B1A2E` | Warm Brass `#C9A463` | **APPROVED** | `7.47:1` | Primary buttons and all text sizes |
| Warm Brass `#C9A463` | Deep Navy `#0B1A2E` | **APPROVED** | `7.47:1` | Highlight text and icons |
| Parchment `#F5F2E9` | Antique Bronze `#7B6240` | **APPROVED** | `5.12:1` | Button labels and normal text |

## 3.6 Restricted and prohibited combinations

The original restricted-combination table uses slash notation rather than an explicit foreground/background column. The order below is preserved as written.

| Combination | Status | Ratio | Rule |
|---|---|---:|---|
| Antique Bronze `#7B6240` / Deep Navy `#0B1A2E` | **RESTRICTED** | `3.05:1` | Large text, large icons, or non-text UI only |
| Warm Brass `#C9A463` / Slate Blue `#3D5266` | **RESTRICTED** | `3.46:1` | Large text or non-text UI only |
| Warm Brass `#C9A463` / Parchment `#F5F2E9` | **REJECTED for text** | `2.09:1` | Decorative use only; never text |
| Deep Navy `#0B1A2E` / Slate Blue `#3D5266` | **RESTRICTED** | `2.16:1` | Decorative layering only |
| Antique Bronze `#7B6240` / Slate Blue `#3D5266` | **REJECTED** | `1.41:1` | Do not combine as foreground/background |
| Antique Bronze `#7B6240` / Warm Brass `#C9A463` | **REJECTED** | `2.45:1` | Do not combine as foreground/background |

Additional exact target:

- **APPROVED:** A Warm Brass `#C9A463` primary-button hover state may darken only while preserving at least `4.5:1` contrast against Deep Navy `#0B1A2E` text.

A named target such as “WCAG 2.1 AA,” “WCAG 2.2 AA,” or “AAA” was **NOT DISCUSSED** in the recovered palette specification.

## 3.7 Interface patterns using Heritage Blue

### Primary button

- Background: Warm Brass `#C9A463` — **APPROVED**
- Text: Deep Navy `#0B1A2E` — **APPROVED**
- Hover: darken Warm Brass while preserving `4.5:1` — **APPROVED**
- Focus: visible outline independent of colour alone — **APPROVED**

### Secondary button

- Light: transparent or Parchment, border/text Antique Bronze `#7B6240` — **APPROVED**
- Dark: Slate Blue `#3D5266`, text Parchment `#F5F2E9` — **APPROVED**

### Links

- Default on Parchment: Antique Bronze `#7B6240` — **APPROVED**
- Hover: Deep Navy `#0B1A2E` plus underline or another non-colour cue — **APPROVED**
- Colour alone is insufficient in body text — **APPROVED rule**

### Cards and panels

- Parchment `#F5F2E9` with Deep Navy `#0B1A2E` text — **APPROVED**
- Slate Blue `#3D5266` with Parchment `#F5F2E9` text — **APPROVED**
- Deep Navy `#0B1A2E` with Parchment `#F5F2E9` and restrained Warm Brass `#C9A463` — **APPROVED**

These general brand-interface patterns were later constrained for instructional graphics; see Sections 5 and 6 of this record.

## 3.8 Separate functional / semantic palette

### Original general interface-state position

In `BRANDING/ColorPalette.md` and the earlier `BRANDING/VisualIdentity.md`:

- Success, warning, error, destructive, disabled, and status colours were **NOT APPROVED / DEFERRED**.
- They were to be developed as interface-support colours.
- They were not additions to the five-colour brand palette.

### Later approved programming-graphic functional palette

On `20260729`, `BRANDING/Standards/InstructionalGraphicStandards.md`, version `01.00.00`, approved a separate PlatformIO / VS Code-inspired palette for programming instruction and code-centred technical graphics.

#### Core editor tokens

| Token | Status | Hex | Approved meaning |
|---|---|---:|---|
| Editor background | **APPROVED** | `#1E1E1E` | Primary code-panel background |
| Editor surface | **APPROVED** | `#252526` | Secondary code panel or title-bar surface |
| Editor border | **APPROVED** | `#3C3C3C` | Code-panel border and divider |
| Editor text | **APPROVED** | `#D4D4D4` | Default code text |
| Editor muted text | **APPROVED** | `#9D9D9D` | Secondary annotations inside dark panels |
| Light UI surface | **APPROVED** | `#F3F3F3` | Neutral instructional-card surface |
| Light UI border | **APPROVED** | `#D4D4D4` | Neutral border on light panels |
| Neutral dark text | **APPROVED** | `#1E1E1E` | Explanatory text on light cards |

#### Syntax and functional tokens

| Token | Status | Hex | Approved meaning |
|---|---|---:|---|
| Selection blue | **APPROVED** | `#007ACC` | Selected item, active connector, primary interface emphasis |
| Syntax blue | **APPROVED** | `#569CD6` | Frequency, first argument, keywords, or a blue-coded category |
| Syntax green | **APPROVED** | `#6A9955` | Duration, comments, positive result, or a green-coded category |
| Syntax orange | **APPROVED** | `#CE9178` | Volume, strings, or an orange-coded category |
| Function yellow | **APPROVED** | `#DCDCAA` | Function names or short highlighted code elements |
| Type cyan | **APPROVED** | `#4EC9B0` | Types, classes, hardware names, or a secondary category |
| Warning gold | **APPROVED** | `#CCA700` | Warning icon, warning border, or warning state |
| Error red | **APPROVED** | `#F44747` | Incorrect result, destructive outcome, or error state |

The default mapping for three ordered programming arguments is:

1. First argument — Syntax blue `#569CD6`
2. Second argument — Syntax green `#6A9955`
3. Third argument — Syntax orange `#CE9178`

This was approved as a default, not a universal semantic law. A different mapping is permitted where the technical content requires it, provided the graphic remains internally consistent.

Functional rules:

- **APPROVED:** Functional colours are not additions to the master brand palette.
- **APPROVED:** Pair colour with a number, label, icon, position, pattern, or connector.
- **REJECTED:** Long body text in syntax green, orange, yellow, or cyan.
- **REJECTED:** Replacing Warning Gold `#CCA700` with Warm Brass `#C9A463`.
- **REJECTED:** Presenting Error Red `#F44747` as a RoboLore brand colour.

### Purple

- Generic AI purple was **REJECTED** from the brand palette. No exact purple hex was recorded in the palette decision.
- An earlier `ImageryAndDiagramStandards.md` draft/foundation document stated: “Purple: category or functional grouping where needed,” but gave no hex value.
- The later authoritative programming-functional token table contains no purple token.
- Therefore, an exact approved purple is **NOT DISCUSSED**. The earlier generic permission was **SUPERSEDED / NOT CARRIED INTO THE APPROVED TOKEN TABLE**.

## 3.9 Derivation and palette exploration

### Early colour inspirations

The historical mood board listed these as inspirations, not approved palette values:

- Lawn-Boy Green — **PROPOSED inspiration**
- Dr Pepper Burgundy — **PROPOSED inspiration**
- Forest Green — **PROPOSED inspiration**
- Navy Blue — **PROPOSED inspiration**
- Charcoal Gray — **PROPOSED inspiration**
- Black — **PROPOSED inspiration; later approved as production neutral `#000000`**
- White — **PROPOSED inspiration; later approved as production neutral `#FFFFFF`**
- Brass accents — **PROPOSED material inspiration; later represented by Warm Brass `#C9A463`**

Exact hex values for these early inspirations were **NOT DISCUSSED / NOT RECOVERED**.

### Named candidate palettes

The following names were discussed:

- Heritage Bronze — **PROPOSED**
- Foundry Bronze — **PROPOSED, then SUPERSEDED**
- Midnight Sky — **PROPOSED**
- Ironclad Burgundy — **PROPOSED, then not selected**
- Blueprint Grove — **PROPOSED, then not selected**
- Charcoal Scholar — **PROPOSED, then not selected**

A recorded ranking was:

1. Foundry Bronze
2. Charcoal Scholar
3. Ironclad Burgundy
4. Blueprint Grove

Heritage Bronze and Midnight Sky were also liked; their exact positions in that ranking were **NOT DISCUSSED / NOT RECOVERED**.

Foundry was later displaced by the Heritage direction on readability grounds. Exact candidate-by-candidate contrast values or full rejection reasons were **NOT DISCUSSED / NOT RECOVERED**.

### Bronze-and-dark-blue preference

A bronze-and-dark-blue direction was explicitly preferred. This preference led to the Heritage Blue system. Exact date of the first statement is **NOT RECOVERED**; the palette was documented and approved by the late-July 2026 package.

### Two-site split and reversal

A split involving Heritage Bronze and Ironclad Burgundy for the two domains was considered.

- Original: separate colour treatment for `.com` and `.ai` — **PROPOSED**.
- Final: “stay with heritage blue. No split.” — **APPROVED**.
- Separate `.com` and `.ai` master palettes — **REJECTED**.

The exact assignment of Heritage Bronze versus Ironclad Burgundy to each domain is **NOT RECOVERED**.

## 3.10 Scope and production

### Scope recorded in the palette specification

Heritage Blue was approved for:

- `robolore.com`
- `robolore.ai`
- Books and instructional resources
- Digital interfaces
- Social and presentation materials
- Printed materials
- Merchandise and environmental applications

The sites may differ through content, hierarchy, imagery, interface density, interactions, calls to action, and labels, but not through separate master colours, wordmarks, or logo systems.

### Print and physical production

- HEX and RGB are the digital source of truth — **APPROVED**.
- CMYK, spot colour, thread, vinyl, paint, foil, and material matches — **NOT APPROVED as universal values / PENDING vendor proof**.
- Metallic inks, foils, anodizing, engraving, and brushed finishes — **APPROVED as optional treatments**, not definitions of the colours.
- Digital metallic gradients — **REJECTED**.
- Commercial print, spot matching, foil/ink proofs, embroidery thread, PCB solder-mask/silkscreen, projector/presentation, and dark mode — **PENDING**.

## 3.11 Later conflict: palette values formally parked

A later graphics-production handoff dated `2026-07-31` stated:

> **Do not apply a Heritage Blue palette from memory.** Two canon documents define that palette with **five different hex values for all five colours**, the conflict is formally parked, and nothing downstream of it may be ruled on until I say so.

Status of this later instruction:

- Use of the remembered five values for downstream graphics — **SUPERSEDED / PARKED pending conflict resolution**.
- The exact alternative five hex values — **NOT RECOVERED**.
- The earlier `BRANDING/ColorPalette.md` values remain a factual approved record, but this later instruction means this export cannot claim that they were the only uncontested values after `2026-07-31`.
- The separation between brand and functional colours remained explicitly settled.

---

# 4. TYPOGRAPHY

## 4.1 Final approved system

| Role | Typeface | Status | Required configuration |
|---|---|---|---|
| Wordmark and restrained brand accents | Oxanium | **APPROVED** | OX-6 weights; limited supporting use |
| Headings, body copy, navigation, interfaces, and AI tutor | Inter | **APPROVED** | OpenType `cv05` enabled globally |
| Code, terminal output, file paths, and technical annotations | JetBrains Mono | **APPROVED** | Programming ligatures disabled |

The approved typography system applies to `.com`, `.ai`, digital products, interfaces, presentations, social material, instructional resources, and future publishing templates subject to print testing.

## 4.2 Oxanium

### Approved uses

- OX-6 wordmark
- Short section labels
- Chapter or module numbers
- Technical category labels
- Small eyebrow text
- Large statistics or measurements
- Diagram identifiers
- Brief interface labels where a brand accent is useful

### Approved supporting treatment

| Item | Exact value |
|---|---:|
| Supporting weight | `500–600` |
| Case | All caps |
| Tracking | `0.08em–0.14em` |
| Digital size | `10–14 px` |

### Prohibitions

Oxanium is **REJECTED** for:

- Body paragraphs
- Long headings
- Dense instructions
- AI tutor conversations
- Form fields
- Long navigation labels
- Code
- Extended all-caps text
- Decorative pseudo-technical typography

### Licence

- SIL Open Font License 1.1 — **APPROVED / RECORDED**.

## 4.3 Inter

### Required OpenType feature

`cv05` must be enabled globally. It gives the lowercase `l` a tail to distinguish:

```text
l I 1 |
```

### Approved uses

- Website and application headings
- Body copy
- Navigation
- Buttons
- Forms
- Tables
- Captions
- Instructional explanations
- AI tutor prompts and responses
- Presentation text
- Digital reading surfaces

### Approved weights

| Weight | Status | Use |
|---|---|---|
| `400` Regular | **APPROVED** | Body copy, AI tutor text, descriptions, table content |
| `500` Medium | **APPROVED** | Labels, captions, emphasized body text, compact UI |
| `600` Semibold | **APPROVED** | Navigation, buttons, subheadings, card titles |
| `700` Bold | **APPROVED** | Major headings and strong emphasis |
| `300` | **RESTRICTED** | Large, nonessential display applications after testing; not ordinary reading or critical UI |

### Italics

Inter Italic is **APPROVED** for titles of works, limited emphasis, introduced terminology, and conventional editorial use. Long instructional passages in italics are **REJECTED**.

### Exact licence

The exact Inter licence name was **NOT DISCUSSED / NOT RECOVERED** in the approved typography specification. The repository rule says font delivery and packaging require licence review.

## 4.4 JetBrains Mono

### Approved uses

- C++ code
- Terminal output
- Console logs
- Commands
- File names and paths
- Variables outside code blocks
- Fixed-width technical annotations
- Character-comparison examples
- Inline code

### Approved weights

| Weight | Status | Use |
|---|---|---|
| `400` Regular | **APPROVED** | Code and terminal content |
| `500` Medium | **APPROVED** | Inline code requiring added emphasis |
| `600` Semibold | **APPROVED** | Short code labels or technical headings |

### Ligature decision

Programming ligatures are **REJECTED** in educational code. The literal sequences must remain visible:

```text
!=  ==  <=  >=  ->  =>  ::  &&  ||
```

Syntax highlighting remains **APPROVED** and independent of ligatures.

### Exact licence

The exact JetBrains Mono licence name was **NOT DISCUSSED / NOT RECOVERED** in the approved typography specification. Font distribution remained subject to review.

## 4.5 Fallback stacks

### Inter stack

```css
font-family:
  "Inter",
  -apple-system,
  BlinkMacSystemFont,
  "Segoe UI",
  Arial,
  sans-serif;
```

### JetBrains Mono stack

```css
font-family:
  "JetBrains Mono",
  "SFMono-Regular",
  Consolas,
  "Liberation Mono",
  monospace;
```

### Oxanium stack

```css
font-family:
  "Oxanium",
  sans-serif;
```

Fallbacks were approved for usability but were not considered exact brand matches.

## 4.6 Required CSS

### Inter `cv05`

```css
body {
  font-family: "Inter", -apple-system, BlinkMacSystemFont, "Segoe UI", Arial, sans-serif;
  font-feature-settings: "cv05" 1;
}
```

### JetBrains Mono without ligatures

```css
code,
pre,
kbd,
samp {
  font-family: "JetBrains Mono", "SFMono-Regular", Consolas, "Liberation Mono", monospace;
  font-variant-ligatures: none;
  font-feature-settings: "liga" 0, "calt" 0;
}
```

## 4.7 Approved digital type scale

| Role | Status | Suggested size | Weight | Line height |
|---|---|---:|---:|---:|
| Display hero | **APPROVED starting range** | `48–72 px` | `700` | `1.00–1.08` |
| H1 | **APPROVED starting range** | `40–56 px` | `700` | `1.05–1.12` |
| H2 | **APPROVED starting range** | `30–40 px` | `700` | `1.10–1.18` |
| H3 | **APPROVED starting range** | `22–28 px` | `600` | `1.18–1.28` |
| H4 / card title | **APPROVED starting range** | `18–22 px` | `600` | `1.25–1.35` |
| Lead paragraph | **APPROVED starting range** | `18–21 px` | `400` | `1.55–1.70` |
| Body copy | **APPROVED starting range** | `16–18 px` | `400` | `1.55–1.70` |
| Compact UI | **APPROVED starting range** | `14–16 px` | `500–600` | `1.30–1.50` |
| Caption | **APPROVED starting range** | `13–14 px` | `400–500` | `1.40–1.55` |
| Code block | **APPROVED starting range** | `14–16 px` | `400` | `1.50–1.70` |
| Inline code | **APPROVED starting range** | `0.90–0.95 em` | `400–500` | Inherit |

Minimum digital sizes:

- Ordinary body copy: `16 px` — **APPROVED minimum**
- Compact interface text: `14 px` — **APPROVED minimum**
- Code: `14 px` — **APPROVED general minimum**

## 4.8 Reading measure and spacing

- Preferred line length: `55–75` characters — **APPROVED**
- Maximum target: approximately `80` characters — **APPROVED**
- Example measure: `max-width: 68ch;` — **APPROVED implementation example**

Heading letterspacing:

| Heading class | Approved range |
|---|---:|
| Large | `-0.04em` to `-0.02em` |
| Medium | `-0.025em` to `-0.01em` |
| Small | `0` to `-0.01em` |

Sentence case is preferred. Full-uppercase headings, excessive tracking, artificial condensed styling, outline text, gradient text, and mixing Oxanium and Inter in one headline are **REJECTED**.

## 4.9 Typography exploration before approval

### Wordmark-family candidates

| Typeface / term | Status | Recorded outcome |
|---|---|---|
| Oxanium | **APPROVED** | Selected for OX-6 |
| Rajdhani | **PROPOSED, then SUPERSEDED by Oxanium** | Finalist; no final use approved |
| Russo One | **PROPOSED, then SUPERSEDED** | Single-weight family; could not produce genuine light/bold contrast within one family |
| Audiowide | **PROPOSED, then SUPERSEDED** | Single-weight family; same limitation |
| Saira | **PROPOSED, then SUPERSEDED** | Evaluated; no final approval |
| Eurostile | **REJECTED** | User associated it strongly with VEX Robotics branding |
| Exo 2 | **REJECTED** | Exact rejection reason not recovered |
| Microgramma | **REJECTED** | Exact rejection reason not recovered |
| “Quantium” | **SUPERSEDED / CORRECTED TYPO** | Earlier reference was corrected to Oxanium |

The candidate exercise specified five families by eight treatments, `40` specimens total, with no space between Robo and Lore. The eight treatments varied case and which half was light or bold.

### Reading/UI candidates

| Typeface | Status | Recorded assessment or outcome |
|---|---|---|
| Inter | **APPROVED** | Final primary reading/UI family |
| Inter with `cv05` | **APPROVED final configuration** | Selected as the best compromise for Apple-like neutrality and lowercase-`l` clarity |
| Inter default lowercase `l` | **SUPERSEDED** | Retained as a comparison, not final implementation |
| Geist | **PROPOSED, then SUPERSEDED** | Described as cleanest minimalist / Apple-adjacent; risked feeling software-led rather than educational |
| Manrope | **PROPOSED, then SUPERSEDED** | Warm geometric option; risked being too rounded beside Oxanium |
| IBM Plex Sans | **PROPOSED, then SUPERSEDED** | Strong technical-editorial direction; recognizable IBM character was a risk |
| Google Sans | **PROPOSED, then SUPERSEDED** | Polished product-system / Apple-like comparison |
| Source Sans 3 | **PROPOSED, then SUPERSEDED** | Calmer long-form reading comparison |
| Atkinson Hyperlegible Next | **PROPOSED, then SUPERSEDED** | Strongest character-recognition benchmark; polish relative to brand was evaluated |

### Monospace candidates

| Typeface | Status | Outcome |
|---|---|---|
| JetBrains Mono | **APPROVED** | Final code and technical family |
| Geist Mono | **PROPOSED, then SUPERSEDED** | Paired with Geist in comparison |
| IBM Plex Mono | **PROPOSED, then SUPERSEDED** | Technical-editorial comparison |
| Source Code Pro | **PROPOSED, then SUPERSEDED** | Paired with Source Sans 3 |
| Atkinson Hyperlegible Mono | **PROPOSED, then SUPERSEDED** | Character-recognition benchmark |

Exact licence names for these nonfinal candidates were **NOT DISCUSSED / NOT RECOVERED**.

## 4.10 Later project-specific safe-font instruction

A later project-specific graphics defect instruction required:

```text
font-family must stay in the safe list (Arial, Helvetica, sans-serif).
```

Status:

- For that named SVG repair, the safe-list requirement was **APPROVED as a project-specific constraint**.
- It did not explicitly repeal the brand-wide Inter/JetBrains/Oxanium system.
- The authoritative instructional standard gives current project-specific requirements precedence over the general standard.
- A general replacement of Inter with Arial for all RoboLore work was **NOT DISCUSSED**.

---

# 5. INSTRUCTIONAL GRAPHIC STANDARDS

## Document identity

| Item | Status | Exact record |
|---|---|---|
| Canonical path | **APPROVED** | `BRANDING/Standards/InstructionalGraphicStandards.md` |
| Draft version | **SUPERSEDED** | `00.90.00`, Draft for Approval |
| Approved version | **APPROVED** | `01.00.00` |
| Approval date | **APPROVED / RECORDED** | `20260729` |
| Role | **APPROVED** | Authoritative detailed specification |

The following is a section-by-section factual reproduction of its substantive requirements.

## Purpose — **APPROVED**

The document applies to:

- Technical diagrams
- Programming graphics
- Code-call anatomy graphics
- Schematics
- Flowcharts
- Explanatory illustrations
- Annotated screenshots
- Charts and comparison graphics
- Book figures
- Website learning graphics
- AI-tutor instructional visuals
- Presentation graphics that teach a technical concept

The goal is not to make every graphic heavily branded. The goal is to make it recognizably RoboLore through clarity, accuracy, restraint, consistency, and respect for the learner.

## 5.1 Authority and precedence — **APPROVED**

Governing order:

1. Current project-specific instructional requirements
2. `BRANDING/Standards/InstructionalGraphicStandards.md`
3. Approved wordmark, colour, and typography specifications
4. `BRANDING/VisualIdentity.md`
5. `Foundation/CODEX.md`
6. Older examples, drafts, experiments, and generated concepts

Older graphics are references, not authority. A treatment must not be repeated merely because it already exists.

## 5.2 Core principle — **APPROVED**

> Simplify the explanation, not the engineering.

Priority order:

1. Technical accuracy
2. Instructional clarity
3. Readability at final size
4. Meaningful hierarchy
5. Accessibility
6. Brand consistency
7. Visual polish

Decoration may not outrank understanding.

A successful graphic should let the learner answer:

- What am I looking at?
- What matters first?
- How are these parts related?
- What does each value, label, or component mean?
- What mistake is the graphic helping me avoid?
- What should I understand after viewing it?

## 5.3 Approved identity assets — **APPROVED**

Approved assets:

- OX-6 wordmark
- Heritage Blue palette
- Approved typography system

A standalone symbol is not approved. The following improvised identity assets are prohibited:

- Gear emblem
- Robot-head logo
- Brain-and-circuit mark
- Monogram
- Crest
- Shield
- Seal
- Badge
- Compass mark
- Circuit-logo device
- Footer medallion
- Any icon presented as a RoboLore symbol

An instructional icon may depict an object only when it explains the lesson and is not acting as a logo.

## 5.4 Wordmark use — **APPROVED**

Use only the approved outlined OX-6 asset.

Prohibited:

- Typed substitute wordmark
- Live-text reconstruction of OX-6
- Pairing with an invented icon
- Badge, seal, crest, or decorative container
- Added circuitry, gears, rays, brackets, or ornaments
- Wordmark repeated in both header and footer
- Different colours for `ROBO` and `LORE`
- Gradients, shadows, bevels, glows, textures, or simulated metal
- Reduced clear space

Frequency:

- No wordmark when the surrounding publication or interface already establishes the brand.
- One authentic wordmark when the graphic must stand alone.
- Do not add a wordmark merely to make a graphic feel more branded.

Branding should normally be carried through typography, page structure, spacing, restraint, and the surrounding publication system.

## 5.5 Brand layer and instructional layer — **APPROVED**

### Brand layer

May use Heritage Blue for:

- Page or canvas background
- Title text
- Figure identifiers
- Small section labels
- Thin dividers
- Page-level structural rules
- Restrained caption bar
- One approved OX-6 wordmark
- Outer publication context

### Instructional layer

Includes:

- Teaching cards
- Parameter boxes
- Code panels
- Warning panels
- Success and error examples
- Callouts
- Arrows
- Status indicators
- Syntax highlighting
- Functional icons

The instructional layer must not use Heritage Blue as category colour merely to look branded.

Separation rule:

> Brand colours identify RoboLore.  
> Functional colours communicate meaning.

One colour must not perform both jobs in the same graphic unless its use is clearly structural and cannot be confused with instructional meaning.

## 5.6 Heritage Blue in instructional graphics — **APPROVED**

| Colour | Exact hex | Approved instructional-graphic role |
|---|---:|---|
| Deep Navy | `#0B1A2E` | Page title, primary structural text, restrained header or footer area |
| Slate Blue | `#3D5266` | Secondary page structure, dividers, captions, supporting labels |
| Antique Bronze | `#7B6240` | Rare crafted detail, short brand label, restrained rule or marker |
| Warm Brass | `#C9A463` | Rare emphasis outside functional teaching panels |
| Parchment | `#F5F2E9` | Primary page or canvas background |

Required restraint:

- Parchment or white should normally dominate.
- Deep Navy may establish title hierarchy.
- Slate Blue may support page structure.
- Antique Bronze and Warm Brass must remain rare.
- Warm Brass must not become the warning colour.
- Heritage Blue must not be distributed equally across every box.
- Large dark brand frames around light instructional content are prohibited.
- Decorative borders, circuit traces, corner ornaments, and badge treatments are prohibited.

Instructional box rule:

- Teaching cards, parameter boxes, and code examples must not be filled or headed with Heritage Blue merely because the graphic belongs to RoboLore.
- Neutral surfaces and the functional palette must be used instead.

## 5.7 PlatformIO / VS Code-inspired functional palette — **APPROVED**

### Core editor colours

| Token | Hex | Approved use |
|---|---:|---|
| Editor background | `#1E1E1E` | Primary code panel background |
| Editor surface | `#252526` | Secondary code panel or title-bar surface |
| Editor border | `#3C3C3C` | Code-panel border and divider |
| Editor text | `#D4D4D4` | Default code text |
| Editor muted text | `#9D9D9D` | Secondary annotations inside dark panels |
| Light UI surface | `#F3F3F3` | Neutral instructional-card surface |
| Light UI border | `#D4D4D4` | Neutral border on light panels |
| Neutral dark text | `#1E1E1E` | Explanatory text on light cards |

### Syntax and functional colours

| Token | Hex | Approved use |
|---|---:|---|
| Selection blue | `#007ACC` | Selected item, active connector, primary interface emphasis |
| Syntax blue | `#569CD6` | Frequency, first argument, keywords, or blue-coded category |
| Syntax green | `#6A9955` | Duration, comments, positive result, or green-coded category |
| Syntax orange | `#CE9178` | Volume, strings, or orange-coded category |
| Function yellow | `#DCDCAA` | Function names or short highlighted code elements |
| Type cyan | `#4EC9B0` | Types, classes, hardware names, or secondary category |
| Warning gold | `#CCA700` | Warning icon, warning border, or warning state |
| Error red | `#F44747` | Incorrect result, destructive outcome, or error state |

Use rules:

- Use syntax colours mainly on dark editor panels, connectors, icons, borders, large values, and short labels.
- Use `#1E1E1E` for ordinary explanatory text on light cards.
- Do not use syntax green, orange, yellow, or cyan for long body text.
- A colour may be mixed with white for a restrained card tint, but the full-strength colour must remain visible as a border, icon, heading marker, or value.
- Colour may not be the only cue.
- Warning Gold `#CCA700` must not be replaced with Warm Brass `#C9A463`.
- Error Red `#F44747` must not be presented as a brand colour.

Default three-argument mapping:

1. Syntax blue `#569CD6`
2. Syntax green `#6A9955`
3. Syntax orange `#CE9178`

A different mapping is allowed where the technical meaning requires it.

## 5.8 Typography — **APPROVED**

### Inter with `cv05`

Use for titles, headings, labels, explanations, captions, callouts, tables, warning text, and supporting notes.

Weights:

- `400` body
- `500` labels/captions
- `600` subheadings
- `700` major headings

### JetBrains Mono

Use for source code, function calls, parameters, variable names, commands, file paths, terminal output, and fixed-width technical annotations. Programming ligatures must be disabled.

### Oxanium

Use only for OX-6, a brief figure identifier, a short module/chapter label, or a restrained technical category label.

Do not use for paragraphs, long headings, code, dense labels, explanatory text, or decorative pseudo-technical type.

Minimum digital sizes:

- Explanatory text: `16 px`
- Compact labels/captions: `14 px`
- Code: `14 px`

Print graphics must be proofed at actual reproduction size.

## 5.9 Layout and composition — **APPROVED**

Use:

- Clear grid
- Strong alignment
- Generous margins
- Consistent spacing
- One obvious reading order
- Controlled grouping
- Simple geometric divisions
- Warm negative space
- Clear source-to-explanation connection
- Limited panel styles within one graphic

Avoid:

- Decorative frames
- Repeated corner ornaments
- Circuit-trace wallpaper
- Random angled cuts
- Gaming-interface decoration
- Sci-fi dashboard styling
- Excessive dark background area
- Multiple competing title bars
- Repeated logos
- Decorative dotted lines without meaning
- Equal emphasis on every element
- Icons that compete with the lesson

Recommended code-explanation sequence:

1. Title
2. Primary code example
3. Direct code-to-explanation mapping
4. Supporting examples or warnings
5. Concise takeaway or comparison

Deviation is allowed if another structure teaches more clearly.

## 5.10 Instructional cards and panels — **APPROVED**

Default light card:

- Surface: white `#FFFFFF` or `#F3F3F3`
- Text: `#1E1E1E`
- Border: `#D4D4D4`
- Category cue: one functional colour
- Radius: restrained and consistent
- Shadow: none or extremely subtle
- Header: neutral with a coloured marker, rule, icon, or border

Dark panels are primarily for source code, terminal output, editor comparisons, and literal code results. Decorative dark filler is rejected.

A concept/parameter card should normally include:

- Numbered or named heading
- Exact value or object
- Unit or type
- Plain-language meaning
- One or two consequences, examples, or comparisons

The key instructional sentence must not be hidden beneath decoration.

## 5.11 Code accuracy and presentation — **APPROVED**

Character-level verification is required for:

- Function name
- Object name
- Capitalization
- Periods
- Commas
- Parentheses
- Semicolons
- Operators
- Spaces
- Numeric values
- Argument order
- Comments
- Arrows and result labels

Exact example:

```cpp
buzzer.playFrequency(440, 800, 15);
```

The following approximation is explicitly wrong:

```cpp
buzzer .playFrequency(440, 800, 15);
```

Code-panel rules:

- JetBrains Mono
- Ligatures disabled
- Dark editor background
- Syntax highlighting preserved
- No wrapping unless code itself requires it
- No fake window controls unless they help compare editor states
- No decorative terminal chrome
- Do not alter code to fit; change layout instead
- Explanatory labels outside code where possible
- Annotations sparse and away from punctuation

Production rule:

- Exact code, equations, dimensions, pin labels, file paths, or numerous technical labels require live text and vector/layout tools.
- Generative raster imagery may be used for concept exploration.
- Generative raster imagery as the production master for exact technical text is **REJECTED / PROHIBITED**.

## 5.12 Connectors, arrows, and callouts — **APPROVED**

Use:

- Consistent line weight
- Clear start and end points
- Minimal crossings
- Arrowheads only when direction matters
- Elbows or curves that avoid text
- Matching labels or numbers
- Functional colour plus a non-colour cue

Avoid:

- Decorative arrows
- Ambiguous start or end
- Lines touching the wrong code token
- Connectors hidden behind panels
- Multiple line styles without defined meaning
- Arrowheads used as decoration

When mapping ordered arguments, the line must terminate at the exact argument it explains.

## 5.13 Icons — **APPROVED**

Icons must be functional, simple, geometric, clear at final size, consistent, secondary to text, and distinguishable without colour alone.

Permitted examples:

- Waveform/tuning reference for frequency
- Clock/timer for duration
- Speaker for volume
- Warning triangle
- Check/success indicator
- Error/stop indicator
- Gear only when the concept is settings, mechanism, or motion

Prohibited:

- Icon as improvised RoboLore logo
- Generic robot heads as decoration
- AI brains
- Generic learning lightbulbs
- Decorative gears
- Decorative circuitry
- Icons implying the wrong technical meaning

## 5.14 Editing and revision workflow — **APPROVED**

For precision edits:

- Use the full original asset.
- Treat crops, screenshots, arrows, markup, and annotations as diagnostic references unless the user explicitly says to edit the crop.
- Preserve the full canvas and composition unless redesign is authorized.
- Preserve unaffected text, icons, colours, and layout.
- Change only explicitly requested elements.
- Preserve the exact uploaded filename unless a new name is requested.
- Verify output before declaring completion.
- Confirm that the file is accessible and has the correct extension.
- Never claim an edit is complete when only a concept image or preview exists.

When redesign is authorized:

- Preserve complete instructional meaning.
- Preserve exact technical facts.
- Preserve required examples and warnings.
- Rebuild hierarchy for clarity.
- Do not preserve weak visual decisions merely because they were in the source.
- Do not invent brand assets or decorative branding.

## 5.15 File formats and naming — **APPROVED in version `01.00.00`**

Preferred formats:

- Photographs: JPG
- Screenshots and raster interface captures: PNG
- Diagrams, schematics, line art, charts, instructional graphics: SVG
- Print masters or archival exports: PDF when required

SVG is preferred for graphics containing text, labels, arrows, code, or line work. PNG is used only when SVG is impractical. JPG is rejected for text-heavy graphics.

Naming example:

```text
L01_GRAPHIC_1-19_playfrequency_anatomy.svg
```

Prohibited unless the repository standard explicitly requires it:

- `final`
- `new`
- `fixed`
- `v2`
- Changed capitalization
- Changed underscores or hyphens
- Replaced description
- Changed extension without approval

The standard originally stated that version history belongs in source control and metadata, not improvised suffixes.

### Later revision-suffix operational rule

A later handoff introduced this project rule:

- If a source has no revision suffix, deliver `_r01`.
- If it ends in `_r##`, increment the number.
- Never append a second suffix.
- `_r##` means staged, not live.

Status:

- The original no-improvised-suffix rule is **SUPERSEDED for the later graphics workflow** where `_r##` is explicitly required.
- The canonical base filename must still be preserved.

## 5.16 Accessibility and final-size testing — **APPROVED**

A graphic must not rely on colour alone. Add at least one of:

- Number
- Label
- Icon
- Position
- Shape
- Pattern
- Connector
- Text explanation

Verify:

- Contrast
- Text size
- Code legibility
- Arrow visibility
- Label separation
- Reading order
- Grayscale comprehension
- Final print or screen size
- Projector visibility when relevant

Do not place:

- Warm Brass text on Parchment
- Thin Antique Bronze text on dark backgrounds
- Syntax green or orange as ordinary small body text on white
- Important labels over images or textures without a solid reading surface

## 5.17 Branding pattern for standalone graphics — **APPROVED**

Normal pattern:

- Parchment or white overall canvas
- Deep Navy title
- Inter for title and explanations
- JetBrains Mono for code
- Neutral instructional cards
- PlatformIO / VS Code functional accents
- One thin Slate Blue or neutral divider when needed
- Optional single authentic OX-6 wordmark
- No decorative border
- No invented symbol
- No circuit ornament
- No repeated footer badge

The intended result should feel like “a clear page from an excellent robotics textbook, not a branded game interface.”

## 5.18 Preflight checklist — **APPROVED**

### Source and scope

- Correct full original target used
- Crops/annotations treated as references unless instructed otherwise
- Exact filename preserved
- Required instructional content preserved
- Only requested elements changed unless redesign authorized

### Branding

- No invented RoboLore symbol
- Any wordmark is the authentic outlined OX-6 asset
- Wordmark is not typed, decorated, enclosed, or paired with an icon
- Heritage Blue restrained to brand layer
- Functional boxes do not use brand colours as category colours
- No decorative circuit traces, ornate frame, or gaming/sci-fi treatment

### Typography and code

- Inter with `cv05` for instructional text
- JetBrains Mono with ligatures disabled for code
- Oxanium limited to approved uses
- Every code character verified
- Function names, punctuation, values, and argument order exact
- Code legible at final size

### Instruction

- Reading order obvious
- Arrows/connectors terminate correctly
- Colour not the only cue
- Icons explain rather than decorate
- Graphic teaches the concept more clearly than the source

### Production

- SVG used when appropriate
- Output extension matches requirement
- No watermark or unintended artifact
- Complete canvas preserved unless redesign authorized
- Delivered file opens correctly
- Final output inspected before completion claim

## 5.19 Decision register — **APPROVED version `01.00.00`**

| Decision | Status in standard |
|---|---|
| Clarity and technical accuracy outrank decoration | Approved foundation |
| Heritage Blue remains the master brand palette | Approved |
| Brand colours and instructional functional colours serve separate roles | Approved |
| PlatformIO / VS Code-inspired colours for programming graphics | Approved |
| Neutral surfaces for instructional cards | Approved |
| Dark editor panels for exact code | Approved |
| OX-6 is the only approved identity mark | Approved |
| Improvised RoboLore symbols and badges | Prohibited |
| Decorative circuit traces and gaming/sci-fi frames | Prohibited |
| Inter for explanations and JetBrains Mono for code | Approved |
| Generative raster output as production master for exact technical text | Prohibited |
| SVG as preferred format for instructional diagrams | Approved production direction |
| Exact filename preservation during revisions | Approved working rule |

## 5.20 Draft-to-approval reversal

Original draft `00.90.00` marked several items as proposed. On `20260729`, approval explicitly locked:

1. The listed PlatformIO / VS Code-inspired functional values.
2. Blue, green, orange as the default three-argument order.
3. Prohibition of generative raster production masters for exact technical text.
4. Authentic OX-6 as optional, not mandatory, on standalone graphics.
5. Precision-edit and exact-filename workflow remaining in the standard.

The approved package updated:

- `Foundation/CODEX.md` to `01.01.00`
- `BRANDING/VisualIdentity.md` to `01.02.00`
- `BRANDING/Standards/InstructionalGraphicStandards.md` to `01.00.00`

---

# 6. SCOPE AND LAYER RULES

## 6.1 One brand across both domains

| Statement | Status |
|---|---|
| `robolore.com` and `robolore.ai` use one wordmark system | **APPROVED** |
| They use one colour system | **APPROVED** |
| They use one typography system | **APPROVED** |
| They use one educational philosophy and brand voice | **APPROVED** |
| They may differ in content, hierarchy, imagery, interface density, interaction, and calls to action | **APPROVED** |
| Separate master colours, wordmarks, or logo systems | **REJECTED** |

`robolore.com` was defined as the home of books and practical instructional resources. `robolore.ai` was defined as the home of the AI tutor.

## 6.2 Where Heritage Blue applies

The palette specification records Heritage Blue as applying to:

- Websites
- AI tutor
- Books
- Instructional resources
- Digital interfaces
- Presentations and social materials
- Print
- Merchandise
- Environmental applications

This broad scope was later refined by the instructional-layer rules.

## 6.3 Brand identity versus functional meaning

### Brand layer — **APPROVED**

Brand identity may govern:

- Overall canvas/background
- Title hierarchy
- Figure identifiers
- Small labels
- Thin dividers
- Page structure
- Caption bar
- Authentic OX-6
- Outer publication context

### Instructional / functional layer — **APPROVED**

Functional meaning governs:

- Teaching cards
- Code panels
- Parameter boxes
- Warning/success/error examples
- Callouts
- Instruction-bearing arrows
- Status indicators
- Syntax highlighting
- Functional icons

The governing statement is:

> Brand colours identify RoboLore. Functional colours communicate meaning.

Therefore, Heritage Blue governs ownership and page-level structure in teaching content, but it must not be used merely as the category or semantic system inside the lesson.

## 6.4 Wordmark frequency in educational content

- No wordmark when the surrounding book/page/interface already identifies RoboLore — **APPROVED**.
- One authentic OX-6 when a graphic must stand alone — **APPROVED**.
- Adding repeated wordmarks merely to increase branding — **REJECTED**.

## 6.5 Scope of icons

- Instructional icons that directly explain a concept — **APPROVED**.
- Icons presented as RoboLore identity marks — **REJECTED**.
- Robot identity/hardware should remain consistent across figures — **APPROVED operational rule**.

## 6.6 Photography versus drawings

A later operational rule established:

- Drawings must be rebuilt as true editable vector SVGs — **APPROVED operational rule**.
- Photographs must remain raster images embedded in SVG with editable vector labels/callouts — **APPROVED operational rule**.
- Tracing, redrawing, or vectorizing a photograph — **REJECTED**.
- Raster-wrapped SVG is correct and required for photographs — **APPROVED operational rule**.

This later rule supersedes any earlier broad language suggesting that every source could be freely redrawn.

## 6.7 Precision editing scope

- Full original asset is the target — **APPROVED working rule**.
- Crops/redlines/screenshots are diagnostic references — **APPROVED working rule**.
- Preserve canvas, composition, and unaffected elements — **APPROVED working rule**.
- Change only the requested elements unless redesign is authorized — **APPROVED working rule**.
- Direct SVG-source editing for surgical vector changes — **APPROVED working rule**.
- Generative redraw for precise line spacing, connectors, arrowheads, and alignment — **REJECTED**.

## 6.8 Later parked palette scope

On `2026-07-31`, applying Heritage Blue exact values from memory was parked because of a stated canon conflict. The layer separation remained settled:

- Brand colours for page-level structure — **APPROVED**.
- Functional palette for syntax, callouts, status, and instruction-bearing arrows — **APPROVED**.
- Choosing exact Heritage Blue values downstream before the conflict is resolved — **REJECTED / PARKED**.

---

# 7. NAMING, POSITIONING, VOICE

## 7.1 Company name and meaning

| Item | Status | Record |
|---|---|---|
| Company name | **APPROVED** | RoboLore |
| Prose spelling | **APPROVED** | `RoboLore` |
| Wordmark spelling | **APPROVED** | `ROBOLORE`, all caps, no space |
| Domain spelling | **APPROVED** | `robolore.com`, `robolore.ai` |

Meaning:

- **Robo:** robots, robotics, building, coding, mechanisms, electronics, real engineered systems.
- **Lore:** knowledge, reasoning, experience, judgment, lessons learned, and understanding accumulated through practice.

Fantasy/mythology interpretation of “lore” was explicitly rejected. In this name, lore means practical wisdom earned through building, testing, failing, observing, troubleshooting, improving, and understanding.

## 7.2 Canonical company description

**APPROVED:**

> RoboLore creates practical books, resources, and learning tools that help people build, program, and understand real robots.

## 7.3 Mission, vision, and promise

### Mission — **APPROVED**

> Make building and coding robots accessible to everyone.

### Vision — **APPROVED**

> To inspire the next generation of roboticists by making robotics education engaging, practical, understandable, relatable, and accessible to everyone.

A long-term goal of helping move girls’ participation in robotics and STEM toward equal representation was stated.

### Brand promise — **APPROVED**

> RoboLore helps learners move from following instructions to understanding the engineering behind them.

## 7.4 Positioning framework

| Positioning element | Status | Approved wording |
|---|---|---|
| What RoboLore is | **APPROVED** | Practical robotics education built around real robots, real code, and understanding why the engineering works. |
| What RoboLore does | **APPROVED** | Helps people build, program, and understand real robots. |
| Difference | **APPROVED** | RoboLore goes beyond instructions to explain the reasoning behind them. |
| Learner gain | **APPROVED** | Practical skill, lasting understanding, and confidence. |
| Ultimate teaching goal | **APPROVED** | How to think like a roboticist. |

## 7.5 Anchor lines and taglines

| Line | Status | Approved role |
|---|---|---|
| “We don’t teach robots. We teach roboticists.” | **APPROVED** | Primary brand line; larger purpose |
| “Documentation tells you what. Lore tells you why.” | **APPROVED** | Explanatory line; name and difference |
| “Real robots. Real code.” | **APPROVED** | Practical proof line |
| “Confidence through understanding.” | **APPROVED** | Outcome line |
| “Educational Engineering for Everyone.” | **APPROVED** | Inclusion line |
| “Lore is earned.” | **APPROVED with restricted use** | Internal culture, editorial/chapter contexts, accumulated experience |
| “Learn by doing.” | **APPROVED principle / messaging foundation** | Educational philosophy |
| “Engineering belongs to everyone.” | **APPROVED belief** | Inclusion principle |
| “Engineering without limits.” | **PROPOSED; not recorded as final anchor line** | Earlier tagline direction |
| “Educational Engineering without Limitations.” | **PROPOSED; not approved as final** | Earlier candidate |
| “Build Boldly. Understand Deeply.” | **PROPOSED / historical** | Historical tagline exploration |
| “Engineering Without Intimidation.” | **PROPOSED / historical** | Historical tagline exploration |

Usage rule:

- Use no more than one primary anchor line in a hero/headline area — **APPROVED**.
- A second line may appear elsewhere only if it serves a different necessary purpose — **APPROVED**.
- Presenting all anchor lines together as a public-facing slogan list — **REJECTED**.

## 7.6 Messaging pillars

All **APPROVED**:

1. Learn by Doing
2. Understand Why
3. Real Robots. Real Code.
4. Engineering for Everyone
5. Think Like a Roboticist

## 7.7 Educational philosophy lines

Approved or recorded beliefs include:

- We learn by doing.
- We build before we memorize.
- Curiosity drives innovation.
- Every mistake teaches something valuable.
- Understanding lasts longer than memorization.
- Real robots teach real engineering.
- Great roboticists never stop asking “Why?”
- Engineering is for everyone willing to learn.
- Knowledge is shared.
- Lore is earned.
- Engineering should never be intimidating.
- Great engineering begins with curiosity.
- Documentation tells you what. Lore tells you why.
- Simplify the explanation, not the engineering.

## 7.8 Communication principles

All **APPROVED**:

- We do not lecture; we guide.
- We do not assume knowledge; we build it.
- We do not merely tell learners how; we explain why.
- We do not avoid mistakes; we learn from them.
- We do not simplify the engineering; we simplify the explanation.
- We do not replace the learner’s thinking; we support it.
- We do not confuse completing instructions with understanding.

## 7.9 Brand voice model

**APPROVED description:**

- Bill Nye’s enthusiasm
- Adam Savage’s curiosity
- The experience of a robotics mentor
- The clarity and encouragement of a favorite high-school engineering teacher

The source explicitly says these are qualities, not an instruction to imitate any person.

## 7.10 Voice characteristics

RoboLore should be:

- Technically accurate
- Inquisitive
- Encouraging
- Practical
- Clear without being simplistic
- Confident without boasting
- Fun without being goofy
- Serious about engineering without becoming intimidating
- Human without becoming overly casual
- Direct without becoming abrupt

## 7.11 Visual personality

RoboLore should feel:

- Engineered
- Intelligent
- Balanced
- Approachable
- Practical
- Curious
- Established
- Clear
- Precise
- Modern without becoming trendy

RoboLore should not feel:

- Corporate and impersonal
- Childish
- Futuristic for its own sake
- Mystical or fantasy-driven
- Militaristic
- Gaming-oriented
- Like a generic AI startup
- Like a generic robotics team
- Decorative without purpose

## 7.12 Preferred language

Preferred verbs:

- Build
- Code
- Understand
- Guide
- Explore
- Test
- Observe
- Discover
- Learn
- Reason
- Improve
- Troubleshoot
- Connect
- Practice
- Explain

Preferred example:

> Test the sensor and compare the readings.

Rejected example:

> Unlock the power of advanced sensing technology.

## 7.13 Language and style to avoid

Explicitly rejected:

- Revolutionary
- Disruptive
- Magical
- Effortless
- Instant expert
- Master robotics overnight
- The ultimate solution
- Guaranteed success
- Industry-leading without evidence
- Professional-grade when unclear
- “AI-powered” as an empty claim
- Corporate jargon
- Empty motivational language
- Excessive exclamation points
- Forced humor
- Condescending explanations
- Unnecessary acronyms
- Unsupported claims
- Dense promotional walls of text

## 7.14 Domain positioning

### `robolore.com` — **APPROVED**

Home of books and practical instructional resources.

Purpose statement:

> Practical robotics books and resources built around real robots, real code, and the reasoning that turns instructions into understanding.

Homepage hero:

> Learn by doing. Understand why.

### `robolore.ai` — **APPROVED**

Home of the AI tutor for guided concept exploration, code explanation, troubleshooting, and engineering reasoning.

Purpose statement:

> An AI robotics tutor built to explain, question, and guide—not merely provide answers.

Homepage hero:

> Guidance that helps you understand.

Positioning the tutor as magical, effortless, all-knowing, or a replacement for teachers, mentors, experimentation, or learner thought is **REJECTED**.

## 7.15 Naming conventions for files and documents

### Documentation

Recovered approved standards specify:

- Semantic-style document versions: `MAJOR.MINOR.PATCH`, e.g. `01.00.00`.
- Major = structural/foundational change.
- Minor = approved addition or expanded rule.
- Patch = correction without changed meaning.
- Version near both top and bottom of major documents.

Repository naming standards in the repaired repository include:

- Canonical folder names such as `BRANDING`, `DISCOVERY`, `Foundation`, `HISTORY`, `Messaging`, `Standards`.
- Markdown filenames generally use stable canonical names without “Final” or “Latest.”
- Case consistency is required.

### Instructional assets

Base pattern:

```text
L##_GRAPHIC_#-##_short_name.svg
L##_IMAGE_#-##_short_name.svg
```

- `GRAPHIC` = drawing/diagram.
- `IMAGE` = photograph/screenshot.
- Preserve uppercase lesson/type, underscores, number hyphen, and lowercase snake-case description.
- `IMAGE` and `GRAPHIC` have separate numbering spaces per lesson.

Later staged revision rule:

```text
_r01, _r02, …
```

- `_r##` means staged, not live.
- Increment an existing suffix.
- Never append a second suffix.

---

# 8. FILES

This section lists every recoverable brand/identity file or package by identifiable name. Files with opaque names such as `image(23).png` are listed separately because their exact brand role cannot be established from the filename alone.

## 8.1 Current or latest recovered canonical files

| Full path | Version | Status | Date if stated | Contents |
|---|---:|---|---:|---|
| `Foundation/CODEX.md` | `01.01.00` | **APPROVED Foundation** | `20260729` approval package | High-level brand source of truth; replaces `01.00.00` recovered repository copy |
| `BRANDING/VisualIdentity.md` | `01.02.00` | **APPROVED** | `20260729` approval package | Visual identity and instructional-standard authority link; replaces `01.01.00` |
| `BRANDING/WordMark.md` | `01.02.00` | **APPROVED** | Not stated | Complete OX-6 specification, optical sizes, colours, clear space, production files |
| `BRANDING/ColorPalette.md` | `01.00.00` | **APPROVED, later exact-value conflict parked** | Not stated | Heritage Blue values, roles, ratios, interface uses, production rules |
| `BRANDING/Typography.md` | `01.00.00` | **APPROVED** | Not stated | Oxanium/Inter/JetBrains Mono system, sizes, stacks, CSS features |
| `BRANDING/Standards/InstructionalGraphicStandards.md` | `01.00.00` | **APPROVED / authoritative** | `20260729` | Full instructional-graphic standard and functional colour tokens |
| `Messaging/PublicMessaging.md` | `01.01.00` | **APPROVED** | Not stated | Canonical company descriptions, domain messaging, voice, anchor lines, claims rules |
| `Foundation/BrandVoice.md` | `01.00.00` | **APPROVED** | Not stated | Voice characteristics and language rules |
| `Foundation/CorePrinciples.md` | `01.00.00` | **APPROVED** | Not stated | Core brand/education principles |
| `Foundation/Lexicon.md` | `01.00.00` | **APPROVED** | Not stated | Approved terminology |
| `Foundation/Mission.md` | `01.00.00` | **APPROVED** | Not stated | Mission |
| `Foundation/Philosophy.md` | `01.00.00` | **APPROVED** | Not stated | Educational philosophy |
| `Foundation/Taglines.md` | `01.00.00` | **APPROVED reference** | Not stated | Anchor-line/tagline reference |
| `Foundation/Vision.md` | `01.00.00` | **APPROVED** | Not stated | Vision |
| `Foundation/FounderStory.md` | `01.00.00` | **PROPOSED / Draft; claims require verification** | Not stated | Founder narrative |
| `Foundation/OnTheWall.md` | `01.00.00` | **APPROVED internal reference** | Not stated | Internal foundational statements |
| `BRANDING/Assets/Fonts.md` | `01.00.00` | **APPROVED roles; delivery review pending** | Not stated | Font-source and delivery guidance |
| `BRANDING/Assets/README.md` | `01.00.00` | **APPROVED / Active** | Not stated | Asset-folder guidance |
| `BRANDING/Validation/ColorPaletteValidation.md` | `01.00.00` | **APPROVED digital direction; physical pending** | Not stated | Colour ratios and validation record |
| `BRANDING/Validation/TypographyValidation.md` | `01.00.00` | **APPROVED digital direction; print/production pending** | Not stated | Typography validation |
| `BRANDING/Validation/WordMarkValidation.md` | `01.01.00` | **APPROVED digital and brand-colour validation; manufacturing pending** | Not stated | Wordmark validation |
| `BRANDING/Tokens/robolore-colors.css` | Not stated | **APPROVED implementation token file** | Not stated | Palette CSS variables |
| `BRANDING/Tokens/robolore-typography.css` | Not stated | **APPROVED implementation token file** | Not stated | Inter `cv05`, JetBrains ligature settings, typography variables |
| `BRANDING/Validation/RoboLore_Color_Validation_Lab.html` | Not stated | **APPROVED supporting validation artifact** | Not stated | Interactive colour review |
| `BRANDING/Validation/RoboLore_Typography_Validation_Lab.html` | Not stated | **APPROVED supporting validation artifact** | Not stated | Interactive typography review |
| `BRANDING/Validation/RoboLore_Wordmark_Validation_Lab_v2.html` | Not stated | **APPROVED supporting validation artifact** | Not stated | Interactive wordmark review |
| `PROJECT_ROADMAP.md` | `01.02.00` | **APPROVED / Active** | Not stated | Project status and next work |
| `README.md` | `01.02.00` | **APPROVED / Active Development** | Not stated | Repository overview |
| `Standards/DocumentStandards.md` | `01.00.00` | **APPROVED** | Not stated | Documentation rules |
| `Standards/MarkdownStyleGuide.md` | `01.00.00` | **APPROVED** | Not stated | Markdown rules |
| `Standards/NamingConventions.md` | `01.00.00` | **APPROVED** | Not stated | Canonical naming rules |
| `Standards/VersioningStandard.md` | `01.00.00` | **APPROVED** | Not stated | Versioning rules |
| `Standards/README.md` | `01.00.00` | **APPROVED / Active** | Not stated | Standards overview |
| `DISCOVERY/DiscoveryVault.md` | `01.00.00` | **APPROVED internal history** | Not stated | Discovery notes |
| `HISTORY/2026-07-27 - Repository Cleanup.md` | `01.00.00` | **APPROVED / Completed** | `2026-07-27` | Cleanup record |

## 8.2 Wordmark production files

All are **APPROVED production assets**; individual internal version numbers and approval dates are **NOT STATED**.

- `BRANDING/Assets/Wordmark/robolore-horizontal.svg`
- `BRANDING/Assets/Wordmark/robolore-horizontal-small.svg`
- `BRANDING/Assets/Wordmark/robolore-horizontal-manufacturing.svg`
- `BRANDING/Assets/Wordmark/robolore-stacked.svg`
- `BRANDING/Assets/Wordmark/robolore-stacked-small.svg`
- `BRANDING/Assets/Wordmark/robolore-stacked-manufacturing.svg`
- `BRANDING/Assets/Wordmark/robolore-vertical.svg`
- `BRANDING/Assets/Wordmark/robolore-vertical-small.svg`
- `BRANDING/Assets/Wordmark/robolore-vertical-manufacturing.svg`
- `BRANDING/Assets/Wordmark/robolore-square.svg`
- `BRANDING/Assets/Wordmark/robolore-square-small.svg`
- `BRANDING/Assets/Wordmark/robolore-square-manufacturing.svg`
- `BRANDING/Assets/Wordmark/RoboLore_Outlined_Production_Manifest.md` — **APPROVED supporting record**, version not stated
- `BRANDING/Assets/Wordmark/RoboLore_Outlined_Production_Proof.png` — **APPROVED proof artifact**, version not stated

## 8.3 Superseded and historical repository files

| Full path | Version | Status | Date | Contents |
|---|---:|---|---:|---|
| `Archive/BrandExploration/BrandMoodBoard.md` | `01.00.00` | **SUPERSEDED / historical exploration** | `2026-07-26` | Mood, early colour inspirations, symbol inspiration |
| `Archive/BrandExploration/LogoConcepts.md` | `01.00.00` | **SUPERSEDED / historical Draft** | `2026-07-26` | Ten symbol territories, evaluation criteria, closed gear/compass direction |
| `Archive/BrandExploration/LogoRequirements.md` | Not stated | **SUPERSEDED / historical exploration** | Not stated | Future symbol requirements |
| `Archive/Drafts/FoundationMessaging.md` | Not stated | **SUPERSEDED** | Not stated | Replaced by `Messaging/PublicMessaging.md` |
| `Foundation/CODEX.md` recovered repository copy | `01.00.00` | **SUPERSEDED** | Created in late July 2026 | Replaced by approved `01.01.00` package update |
| `BRANDING/VisualIdentity.md` recovered repository copy | `01.01.00` | **SUPERSEDED** | Created in late July 2026 | Replaced by approved `01.02.00` package update |
| `BRANDING/Standards/InstructionalGraphicStandards.md` draft | `00.90.00` | **SUPERSEDED / Draft for Approval** | `20260729` | Replaced by `01.00.00` approved |
| `REVIEW_AND_PUSH_NOTES.md` | Not stated | **SUPERSEDED / Draft review record** | `20260729` | Five approval questions and installation notes |

## 8.4 Approval and administrative records

| File | Version | Status | Date | Contents |
|---|---:|---|---:|---|
| `APPROVAL_AND_PUSH_NOTES.md` | Not stated | **APPROVED administrative record** | `20260729` | Locks five instructional-standard decisions and approved versions |
| `PACKAGE_MANIFEST.json` | Not stated | **APPROVED supporting package record / repository inclusion optional** | `20260729` package | Exact content not recovered |
| `RoboLore_Repository_Audit.md` | Not stated | **APPROVED factual audit record** | `2026-07-27` | Repository consistency, duplicates, validation findings |
| `RoboLore_Repaired_Repository_Instructions.md` | Not stated | **APPROVED administrative instructions** | `2026-07-27` | Installation instructions for repaired repository |
| `RoboLore_Clean_Rebuild_Validation.md` | Not stated | **APPROVED validation record** | `2026-07-27` | Validation of 59-file clean tree |
| `RoboLore_Brand_Asset_Control_Update.md` | `01.00.00` | **APPROVED Addition** | `2026-07-28` | Prohibits unapproved identity assets; target `BRANDING/ImageryAndDiagramStandards.md` |
| `ImageryAndDiagramStandards.md` | `01.00.00` | **APPROVED Foundation — Calibration in Progress** | Not stated | Early imagery/diagram rules; partially superseded by the later authoritative standard |
| `RoboLore Name Interpretation.txt` | Not stated | **APPROVED conversation export / supporting record** | File created `2026-07-29` in recovered library | Wordmark candidate discussion and specimen structure |
| `RoboLore Logomark Development.txt` | Not stated | **APPROVED conversation export / supporting record** | Multiple recovered copies | Heritage package record and later workflow record; not itself canonical |

## 8.5 Packages produced

| Package / folder | Version | Status | Date | Recoverable contents |
|---|---:|---|---:|---|
| `RoboLore_Heritage_Blue_Update.zip` | Not stated | **APPROVED delivery package** | Late July 2026 | `Branding/ColorPalette.md`, validation MD/HTML, CSS tokens, updated WordMark, WordMarkValidation, README, roadmap, draft PublicMessaging, update notes |
| `RoboLore_Heritage_Blue_Update/Branding/ColorPalette.md` | `01.00.00` | **APPROVED** | Late July 2026 | Full palette values |
| `RoboLore_Heritage_Blue_Update/Branding/Validation/ColorPaletteValidation.md` | `01.00.00` | **APPROVED digital validation** | Late July 2026 | Ratios and checks |
| `RoboLore_Heritage_Blue_Update/Branding/Validation/RoboLore_Color_Validation_Lab.html` | Not stated | **APPROVED supporting artifact** | Late July 2026 | Interactive palette validation |
| `RoboLore_Heritage_Blue_Update/Branding/Tokens/robolore-colors.css` | Not stated | **APPROVED implementation artifact** | Late July 2026 | Palette tokens |
| `RoboLore_Heritage_Blue_Update/Branding/WordMark.md` | `01.02.00` | **APPROVED** | Late July 2026 | Wordmark colour update |
| `RoboLore_Heritage_Blue_Update/Branding/Validation/WordMarkValidation.md` | `01.01.00` | **APPROVED digital / manufacturing pending** | Late July 2026 | Wordmark validation |
| `RoboLore_Heritage_Blue_Update/README.md` | `01.00.00` in package record | **SUPERSEDED by later root `01.02.00`** | Late July 2026 | Repository overview |
| `RoboLore_Heritage_Blue_Update/PROJECT_ROADMAP.md` | `01.00.00` in package record | **SUPERSEDED by later `01.02.00`** | Late July 2026 | Roadmap |
| `RoboLore_Heritage_Blue_Update/Messaging/PublicMessaging.md` | `01.00.00` draft in package record | **SUPERSEDED by approved `01.01.00`** | Late July 2026 | Messaging draft |
| `RoboLore_Heritage_Blue_Update/HERITAGE_BLUE_UPDATE_NOTES.md` | `01.00.00` | **APPROVED administrative record** | Late July 2026 | Merge notes and palette list |
| `RoboLore_Typography_Update.zip` | Not stated | **APPROVED delivery package** | `2026-07-27` | Typography, CSS, validation, VisualIdentity update, CODEX insert, placement notes, README/roadmap updates |
| `RoboLore_Codex_VisualIdentity_Fix.zip` | Not stated | **APPROVED corrective package** | Late July 2026 | Three corrective files; exact list beyond folder name not fully recovered |
| `RoboLore_Repaired_Repository.zip` | Not stated | **APPROVED repaired repository delivery** | `2026-07-27` | Complete repaired repo with Git history |
| `RoboLore_Clean_Rebuild_From_d8f7b8f.zip` | Not stated | **APPROVED clean rebuild delivery** | `2026-07-27` | 59-file clean repository tree |
| `RoboLore.zip` | Not stated | **SUPERSEDED uploaded repository snapshot** | `2026-07-27` audit source | Repository before cleanup |
| `RoboLore-d8f7b8f1c8253a02c48ced71d473714b93eee1b9.zip` | Git checkpoint ID | **SUPERSEDED checkpoint source** | `2026-07-27` | Exact source checkpoint for clean rebuild |

## 8.6 Typography study files

| File | Version | Status | Date | Contents |
|---|---:|---|---:|---|
| `RoboLore_Typography_Comparison.html` | Not stated | **PROPOSED study; superseded by final choice** | `2026-07-27` | Round-one Inter, Geist, Manrope, IBM Plex comparisons and monospace pairings |
| `RoboLore_Typography_Comparison_Round_2.html` | Not stated | **PROPOSED study; superseded by final choice** | `2026-07-27` | Inter default/cv05, Geist, Google Sans, Source Sans 3, Atkinson comparisons |
| `RoboLore_Typography_Update/BRANDING/Typography.md` | `01.00.00` | **APPROVED** | `2026-07-27` | Final typography specification |
| `RoboLore_Typography_Update/BRANDING/Tokens/robolore-typography.css` | Not stated | **APPROVED** | `2026-07-27` | Typography CSS tokens |
| `RoboLore_Typography_Update/BRANDING/Validation/TypographyValidation.md` | `01.00.00` | **APPROVED digital / print pending** | `2026-07-27` | Validation record |
| `RoboLore_Typography_Update/BRANDING/Validation/RoboLore_Typography_Validation_Lab.html` | Not stated | **APPROVED supporting artifact** | `2026-07-27` | Typography validation lab |

## 8.7 Palette and brand-concept image files

These are concept or study artifacts. Unless separately identified above, they are **PROPOSED / SUPERSEDED**, with no internal version number or approval date stated.

- `RoboLore_Bronze_Navy_Palette_Study.png`
- `four_robolore_palette_concepts.png`
- `palette_explorations_for_robolore.png`
- `two_tone_robolore_website_mockup.png` — filename recovered from conversation context; current local path not confirmed
- `a_clean_flat_infographic_brand_guideline_poster.png`
- `a_clean_professional_brand_guideline_poster_inf.png`
- `a_clean_graphic_design_board_presentation_image.png`
- `a_clean_graphic_design_presentation_board_on_a_dar.png`
- `a_clean_graphic_design_presentation_brand_concep.png`
- `a_clean_white_infographic_typography_comparison_pa.png`
- `a_high_resolution_mockup_image_showing_two_side_by.png`
- `photography_style_review_board.png`
- `four_caption_styles_compared.png`

Exact content, dates, and decision outcomes for each image are **NOT DISCUSSED / NOT RECOVERED** beyond their role as concept studies.

## 8.8 Symbol-concept image files

The following named raster concepts were generated during symbol exploration. All are **PROPOSED / NOT APPROVED** unless a rejection is stated in Section 2. No internal versions or exact creation dates were recovered.

- `abstract_navy_and_bronze_geometric_logo.png`
- `amber_core_polyhedral_artifact.png`
- `angular_navy_gold_monogram_emblem.png`
- `ascending_geometric_staircase_emblem.png`
- `beacon_signal_emblem.png`
- `beacontower_emblem.png`
- `black_and_gold_mechanical_monolith.png`
- `bridge_arch_emblem.png`
- `bridge_of_knowledge_and_engineering.png`
- `bronze_and_navy_geometric_rotor_logo.png`
- `bronze_and_navy_octagonal_r_logo.png`
- `bronze_book_circuit_shield.png`
- `bronze_network_shield_emblem.png`
- `bronze_shutter_navy_r_emblem.png`
- `futuristic_amber_core_lantern.png`
- `futuristic_blue_core_beacon_monument.png`
- `futuristic_blue_lit_techno_key.png`
- `futuristic_bronze_data_core_medallion.png`
- `futuristic_golden_signal_beacon.png`
- `futuristic_steampunk_circuit_key.png`
- `geometric_navy_and_bronze_totem_emblem.png`
- `geometric_navy_and_gold_monogram_emblem.png`
- `geometric_navy_and_gold_r_emblem.png`
- `geometric_navy_and_gold_r_monogram.png`
- `golden_labyrinth_medallion.png`
- `hexagonal_navy_and_bronze_tech_emblem.png`
- `icosahedral_emblem_with_bronze_and_navy_facets.png`
- `interlocking_bronze_and_steel_arch_mechanism.png`
- `interlocking_navy_bronze_r_shield.png`
- `labyrinth_question_mark_emblem.png`
- `maze_emblem_with_golden_path.png`
- `mechanical_bronze_accented_letter_r.png`
- `mechanical_iris_aperture_in_steel_and_gold.png`
- `mechanical_navy_and_bronze_eye.png`
- `metallic_cybernetic_eye_lens.png`
- `monochrome_octagon_logo_exploration_board.png`
- `monogrammed_navy_and_gold_octagon.png`
- `navy_and_gold_geometric_r_mark.png`
- `navy_and_gold_octagonal_r_emblem.png`
- `navy_and_gold_octagonal_r_logo.png`
- `navy_bronze_geometric_r_logo.png`
- `navy_octagonal_r_logo_with_gold_accent.png`
- `neon_blue_sci_fi_beacon.png`
- `neon_core_futuristic_shield.png`
- `octagonal_navy_and_gold_monogram.png`
- `octagonal_navy_and_gold_r_emblem.png`
- `robolore_core_mark_exploration_board.png`
- `shape_studies_brand_exploration_board.png`
- `shielded_geometric_crest_logo.png`

Several names themselves reflect directions later rejected by the standards—monograms, shields, gears, brains, neon sci-fi, metallic three-dimensional effects—but the exact image-by-image rejection event is **NOT DISCUSSED**.

## 8.9 Opaque or unrecoverable artifact names

The available working directory contains files named `image(23).png` through `image(48).png`, plus `imagegen.png` and other automatically named outputs. Their precise brand concept, version, date, and decision status cannot be established from their filenames alone.

Status: **NOT DISCUSSED / NOT RECOVERED**.

---

# 9. OPEN, UNRESOLVED, AND REJECTED

## 9.1 Open / deferred

| Item | Status | Record |
|---|---|---|
| Standalone symbol / logomark | **NOT APPROVED / DEFERRED** | No final mark |
| Symbol-to-wordmark relationship | **NOT DISCUSSED as final / DEFERRED** | Awaiting symbol |
| Combined symbol-and-wordmark lockups | **NOT DISCUSSED as final / DEFERRED** | Awaiting symbol |
| Final favicon | **NOT APPROVED / DEFERRED** | Square OX-6 is not final |
| Physical manufacturing minimums | **NOT DISCUSSED as fixed values / PENDING** | Process testing required |
| PCB silkscreen validation | **PENDING** | No approved sample result |
| Embroidery validation | **PENDING** | No approved sample result |
| Rubber-stamp validation | **PENDING** | No approved sample result |
| Foil, embossing, debossing | **PENDING** | No approved sample result |
| Laser engraving | **PENDING** | No approved sample result |
| Commercial print proofs | **PENDING** | No approved sample result |
| Projector/classroom display | **PENDING** | No approved validation result |
| CMYK / spot / thread / vinyl / paint conversions | **NOT APPROVED / PENDING** | Vendor proof required |
| Trademark review | **PENDING** | No final legal result |
| Font and asset licensing review | **PENDING** | Oxanium OFL known; broader packaging review pending |
| Extended-character and multilingual testing | **PENDING** | No result |
| Dark-mode expansion | **PENDING** | No approved system |
| General product interface-state colours | **PENDING** | Programming tokens approved; full success/destructive/disabled/status system not approved |
| Final book-series architecture | **DEFERRED** | Await manuscript/product need |
| Final cover system | **DEFERRED** | Await manuscript readiness |
| Photography standards | **PLANNED / PARTIALLY DISCUSSED** | Foundation work exists; final calibration not complete |
| Specialized illustration templates | **PLANNED** | No final set recovered |
| Website architecture | **PLANNED** | No final architecture recovered |
| AI tutor interaction standards | **PLANNED** | High-level boundaries approved; full standard unresolved |
| Publishing templates | **PLANNED** | Await manuscript readiness |
| Heritage Blue canon-value conflict | **OPEN / PARKED as of 2026-07-31** | Alternative five values not recovered |
| Exact approved purple token | **NOT DISCUSSED** | No hex; not in final functional token table |

## 9.2 Explicitly rejected

### Identity and symbol

- Separate `.com` and `.ai` identities or palettes.
- Generic robot-head logo.
- Improvised gear emblem.
- Brain-and-circuit identity mark.
- Monogram, shield, crest, seal, badge, compass mark, circuit-logo device, footer medallion, mascot, substitute logo.
- Interim symbol presented as final.
- Icon before or integrated with OX-6 without approval.
- Gear/compass direction as previously explored, because it became generic, conventional, cluttered, and weak at small sizes.
- Radiation-like starburst resemblance.

### Wordmark

- Any wordmark other than OX-6.
- Eurostile because of the VEX Robotics association.
- Exo 2 and Microgramma as wordmark choices; exact individual reasons not recovered.
- Space between `ROBO` and `LORE`.
- Added tracking in the master horizontal mark.
- Split-colour `ROBO` / `LORE`.
- Gradient, glow, shadow, bevel, texture, or simulated metal.
- Distortion or manual recreation.

### Colour

- Separate `.ai` palette.
- Generic AI purple as a brand colour.
- Neon cyan and electric gradients.
- Turning bronze into construction orange.
- Distressed antique-paper Parchment.
- Equal visual use of all five colours.
- Warm Brass body text on Parchment.
- Large bronze fields without purpose.
- Unapproved accents used only to separate products.
- Colour as the sole cue for status or meaning.
- Warning Gold replaced by Warm Brass.
- Error Red treated as a brand colour.

### Typography

- Programming ligatures in educational code.
- Oxanium body copy or long instructional text.
- Multiple competing sans-serif families.
- Ultra-light body text.
- Tiny code examples.
- Decorative coding fonts.
- All-caps paragraphs.
- Excessive tracking.
- Multiple typefaces mixed inside one headline.

### Instructional graphics

- Brand colours used as functional teaching categories.
- Decorative circuit traces, ornate frames, corner ornaments, gaming/sci-fi dashboard treatment.
- Generative raster images as production masters for exact code or technical text.
- Decorative arrows, ambiguous connectors, or connectors to the wrong token.
- Fake terminal chrome that competes with the lesson.
- Altering code to make it fit.
- Icons used as decoration or improvised branding.
- Editing a crop instead of the full asset unless explicitly instructed.
- Renaming or changing unaffected elements during a precision edit.
- Claiming completion without inspecting the actual output.
- Tracing or redrawing a photograph for SVG delivery.

## 9.3 Reversals and supersessions

| Original | Final | Status change / when |
|---|---|---|
| Separate `.com` / `.ai` palette idea | One Heritage Blue system; “stay with heritage blue. No split.” | **PROPOSED → REJECTED / APPROVED final**, late July 2026 |
| Foundry Bronze ranked first | Heritage direction selected on readability grounds | **PROPOSED → SUPERSEDED**, exact date not recovered |
| Wordmark colour unresolved in earlier spec | Heritage Blue applications added to `WordMark.md` `01.02.00` | **OPEN → APPROVED**, late July 2026 |
| OX-6 `01.00.00` | OX-6 `01.01.00`, then `01.02.00` | **SUPERSEDED by expanded versions**, late July 2026 |
| Inter default lowercase `l` | Inter with `cv05` globally | **PROPOSED → APPROVED final**, `2026-07-27` typography work |
| Functional syntax colours deferred in typography/palette docs | Programming-graphic functional palette approved | **DEFERRED → APPROVED for programming graphics**, `20260729` |
| InstructionalGraphicStandards `00.90.00` | `01.00.00` Approved | **PROPOSED → APPROVED**, `20260729` |
| CODEX `01.00.00` | CODEX `01.01.00` | **SUPERSEDED**, `20260729` approval package |
| VisualIdentity `01.01.00` | VisualIdentity `01.02.00` | **SUPERSEDED**, `20260729` approval package |
| No improvised filename suffixes in standard | `_r##` staged revision suffix required in later graphics workflow | **SUPERSEDED for that workflow**, `2026-07-31` handoff |
| Heritage Blue exact values treated as settled | Later handoff says two canon sets conflict; application from memory parked | **APPROVED record → OPEN/PARKED for downstream use**, `2026-07-31` |
| Broad source-redraw language in early imagery foundation | Photos remain embedded raster; drawings are vectorized | **SUPERSEDED by subject-based rule**, late July 2026 |

---

# Items believed to exist but not fully recoverable

1. **The second canon document containing the conflicting five Heritage Blue hex values.**  
   - **Status:** **NOT RECOVERED**.  
   - Likely source: graphics-chat handoff created around `2026-07-31`.  
   - The handoff explicitly says all five values conflict, but the alternate values are not in the recoverable excerpt.

2. **Complete numerical scoring, if any, for symbol concepts.**  
   - **Status:** **NOT DISCUSSED / NOT RECOVERED**.  
   - Likely conversation: logomark exploration around `2026-07-25` to `2026-07-27`.  
   - The archived file contains criteria and strengths/weaknesses but no numerical scores.

3. **Complete advancement/elimination sequence for every generated symbol image.**  
   - **Status:** **NOT RECOVERED**.  
   - Likely conversation: “RoboLore Logomark Development,” late July 2026.  
   - Dozens of concept image filenames survive, but not every image’s explicit disposition.

4. **Exact candidate-palette hex values for Heritage Bronze, Foundry Bronze, Midnight Sky, Ironclad Burgundy, Blueprint Grove, and Charcoal Scholar.**  
   - **Status:** **NOT RECOVERED**.  
   - Likely conversation: palette exploration before the Heritage Blue package, approximately `2026-07-25` to `2026-07-27`.

5. **Exact first date and full wording of the bronze-and-dark-blue preference.**  
   - **Status:** **NOT RECOVERED**.  
   - The preference is preserved in project context and study-file names, but the original message is not in the accessible source set.

6. **Exact rejection reasons for Exo 2, Microgramma, Saira, Rajdhani, and several body-font candidates.**  
   - **Status:** **PARTIALLY RECOVERED**.  
   - Eurostile’s VEX association and the single-weight limitation of Russo One/Audiowide are recoverable; the remaining exact reasons are not.

7. **Exact licence names for Inter, JetBrains Mono, and the nonfinal typography candidates.**  
   - **Status:** **NOT DISCUSSED / NOT RECOVERED** in the approved typography document.  
   - The repository records that packaging and distribution require review.

8. **Full content of `PACKAGE_MANIFEST.json` from the instructional-standards approval package.**  
   - **Status:** **NOT RECOVERED**.  
   - Likely date: `20260729`.

9. **Exact contents of `RoboLore_Codex_VisualIdentity_Fix.zip`.**  
   - **Status:** **PARTIALLY RECOVERED**.  
   - The folder/package exists, but this export did not infer missing file roles beyond what was visibly recoverable.

10. **Opaque auto-generated files named `image(23).png` through `image(48).png`.**  
    - **Status:** **NOT RECOVERED**.  
    - Likely from logo/brand exploration conversations in late July 2026.

11. **Any brand decisions made in conversations not present in the accessible project history, uploaded exports, File Library, or repository snapshots.**  
    - **Status:** **NOT RECOVERABLE FROM THIS THREAD**.  
    - No attempt has been made to reconstruct them from general design knowledge.
