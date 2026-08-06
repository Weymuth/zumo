# ZUMO — COLOUR LEDGER

**Ledger version: v1.0** — the single list of every outstanding colour decision in the book.
Opened S122 by DJ ruling. Increment on every substantive edit.

> **Why this file exists.** Colour decisions kept arriving one at a time, inside arcs about
> something else, and each one was priced as if it were local. It is not local. Every number
> below is MEASURED against the live tree at S122, never recalled — see §0 for how.

---

## 0. HOW TO READ THIS FILE

Every count names the instrument that produced it (§24.10). Nothing here is a ruling unless it
says **RULED**. An item marked **BLOCKED** must not be decided on its own, because deciding it
in isolation is the S91 failure this ledger exists to prevent: hand-patching one value out of a
palette whose base has not been settled.

Re-measure before acting. A count in a document is a lead, not a finding (§24.6c).

---

## 1. THE BLOCKING FACT — A REPAINT IS A RENAME, NOT A SUBSTITUTION

`css/book.css` is a GENERATED artefact (`build_css.py`, §24.12) and **it has no
value-substitution layer.** Class names are derived from the values they carry, so:

| measured at S122 | value | instrument |
|---|---|---|
| distinct colour values in `css/book.css` | **169** | `grep -oE '#[0-9a-fA-F]{3,8}'` + Counter |
| total colour tokens | **708** | same |
| **distinct hexes appearing INSIDE class names** | **155** | selector parse of `book.css` |
| **class names that encode a hex** | **562** | same |
| custom properties (`--var`) in `book.css` | **0** | `grep -c -- '--'` |
| raw hex literals remaining in the sixteen lessons | **0** | per-lesson scan |

**So changing one colour renames every class that carries it, in every lesson that uses it.**
Worked examples, measured:

- `#ddd` → **38 class names** (`td-ddd`, `td-ddd-2`, `th-ddd`, …)
- `#6f7582` → **23 class names**
- `#2e86ab` → **21 class names**
- `#433014` → **20 class names**
- `#ccc` → **17 class names**
- `#1f2a3d` → **16 class names**

**The first move of the colour arc is therefore NOT a colour.** It is deciding whether
`build_css` emits custom properties, so that a repaint becomes one file instead of 562 renames.
`build_palette.py --css` already emits them and nothing consumes them.

---

## 2. THE LEDGER

Status: **RULED** · **OPEN** (needs a DJ ruling) · **BLOCKED** (must wait on §1) ·
**PARKED** (deliberately deferred, with a reason).

### 2.1 — Palette foundation

| # | Item | Measured | Status |
|---|---|---|---|
| C01 | `build_css` emits custom properties so a repaint is one file, not 562 renames | 0 custom properties today; `build_palette --css` already emits them | **OPEN — do this first** |
| C02 | Heritage Blue: `BookComponentStandard` §5.0 vs RoboLore canon disagree **five ways** | Parked Bible §26 at S93; nothing renders either palette | **BLOCKED** |
| C03 | `build_css` names rules by usage RANK, so the digest moves when no rule changes | S113's shape, seen 5× (S113, S115, S121, S122 ×2) | **OPEN** |

### 2.2 — Values with no ruling

| # | Item | Measured | Status |
|---|---|---|---|
| C04 | 16 colours spelled in **uppercase**, everything else lowercase | 19 occurrences, 16 distinct: `#DEEAF6`×2 `#2E74B5`×2 `#E2F0D9`×2, thirteen at ×1 | **OPEN** |
| C05 | The `#666` footer colour | 17 declarations; 8 class families whose NAMES encode the hex | **BLOCKED by C01** |
| C06 | Callout colours re-examined — v8.87 Scope C | never closed | **OPEN** |
| C07 | 12 callout schemes carry unresolved colour conflicts (S94) | recorded S94, not re-measured since | **OPEN — re-measure first** |
| C08 | LEARN and INSIGHT share `#e3f2fd` / `#2196f3` | `#e3f2fd` 9 declarations · `#2196f3` 10 | **OPEN — re-measure first** |
| C09 | KEY TERM spans three purples, one of which is MY PLAN's colour | recorded S94, not re-measured since | **OPEN — re-measure first** |

### 2.3 — Constructs whose paint splits by era

| # | Item | Measured | Status |
|---|---|---|---|
| C10 | **Engineer's Log stripe**: `#0e1a2c` in L01–L11, `#6f7582` in L12–L16 | `.div-0e1a2c` 12 declarations · `.div-6f7582-3` part of 27 | **PARKED S122** — surfaced by the Tier-1 census, deliberately not ruled because it is one value out of an unsettled palette. Majority says navy; `#6f7582` is the §10+ band colour and Engineer's Log sits in §10. |

### 2.4 — Ruled, applied, do not reopen

| # | Item | Status |
|---|---|---|
| C11 | §22 terminal colours: SUCCESS `#6a9955`, ERROR `#f14c4c` | **RULED** v8.45 — `#6a9955` is deliberate, do not "correct" it to `#23d18b` |
| C12 | Forge Red `#D46554` is FUNCTIONAL, not a sixth brand colour | **RULED** v8.88/v8.89 |
| C13 | Challenge-card header takes the §9 band `#7A5905` | **RULED** v8.99, superseding v8.87's Antique Bronze |
| C14 | Gradients are banned in lesson chrome | **RULED** v8.87 |

### 2.5 — Adjacent, colour-shaped, not `book.css`

| # | Item | Measured | Status |
|---|---|---|---|
| C15 | Gradient definitions inside SVG assets | **26 across 18 files**, 5 referenced by nothing | **OPEN** |
| C16 | 41 marks in `images/marks/`, not one wired into a lesson | against 2,701 emoji glyphs in the sixteen lessons | **OPEN** — the glyph arc DJ queued at S122 |

---

## 3. SEQUENCING

1. **C01 first.** Until the stylesheet carries custom properties, every other item costs a
   rename sweep instead of an edit, and each one re-opens §27.8b.
2. **C02 next.** The base palette must be settled before any value derived from it is ruled,
   or the ruling is patched from a moving base — the S91 failure, on the record in §26.
3. **Re-measure C07, C08, C09 before ruling them.** They were recorded at S94, before the
   §27 migration moved every value out of the lessons and into a generated stylesheet. Their
   numbers are from a tree that no longer exists.
4. **C04 and C15 are independent** and can be closed any time.
5. **C10 resolves for free** once the palette is ruled. Do not spend a session on it.

---

## 4. WHAT MUST NOT HAPPEN

- **Do not rule a single colour because an arc surfaced it.** That is how C10 arrived, and it
  was parked for exactly this reason.
- **Do not hand-edit `css/book.css`.** It is generated (§24.12). A repaint is
  restore → regenerate → `strip_inline --apply --include-held`, in that order, and the flag is
  not optional: without it 624 held strings revert to inline and innocent lessons are rewritten.
- **Do not trust a count in this file without re-running it.** §24.6c.

---

*Opened S122. Referenced from Bible §26 so it is not an ungated orphan in the repo root (§12.2).*
