<!-- ROBOLORE_BRAND_CARD_S201.md v1.0 — a portable extract for a chat that does not have the
     repo. Every value below is EXTRACTED from a named file in Weymuth/zumo at commit cff7475
     plus this session's edits; nothing is recalled. Where a value is derived rather than
     stated, the derivation is named on the line. Working document, not a book artefact. -->

# RoboLore — Colours, Type, and What Not To Invent
### Portable card · derived from the repo at S201 · paste into another chat

**Read section 0 before using any hex below.** Two files in the repo state the Heritage Blue
palette and they disagree. One is withdrawn. A chat handed the wrong one will be confidently
wrong for the whole session.

---

## 0. THE ONE TRAP — two palettes, one withdrawn

| Source | Deep Navy | Slate Blue | Antique Bronze | Warm Brass | Parchment | Status |
|---|---|---|---|---|---|---|
| `ROBOLORE_UPSTREAM_DELTA_S102.md` §1 · `build_palette.py` `CANON` | `#0B1A2E` | `#3D5266` | `#7B6240` | `#C9A463` | `#F5F2E9` | **APPROVED — use these** |
| `BookComponentStandard.md` v01.13.0 §5.0 | `#162337` | `#43566B` | `#8C6A43` | `#C3A36A` | `#F4EBDD` | **WITHDRAWN at S102** |

**The approved five are DJ-stated** (Bible §26.4 item 1). The withdrawn five entered through a
single undocumented commit; S102 records them as withdrawn and notes they were never
*arithmetically* wrong, only unowned — the case against them rested on provenance alone.

**Which one the book actually renders — derived, not quoted.** `build_palette.py --css` emits
`--page: #F5F2E9` and `--heading: #7B6240`. Those are Parchment and Antique Bronze from the
**approved** row. The generator that paints the book agrees with the delta, so three independent
things agree and only `BookComponentStandard` §5.0 dissents.

> ⚠️ **Two live defects in the repo, unfixed as of S201.** `BookComponentStandard.md` v01.13.0
> §5.0 still prints the withdrawn table, and `ROBOLORE_GRAPHICS_CHAT_HANDOFF.md` §7 still carries
> the "palette is formally parked, do not apply Heritage Blue from memory" hold that S102
> explicitly released. **If you paste either of those files into a chat, paste this card too.**

---

## 1. HERITAGE BLUE — the brand palette

| Name | Hex | Role |
|---|---|---|
| Deep Navy | `#0B1A2E` | body text on light, darkest structure |
| Slate Blue | `#3D5266` | structural framing |
| Antique Bronze | `#7B6240` | headings |
| Warm Brass | `#C9A463` | accent; the palette's saturation ceiling at **49%** |
| Parchment | `#F5F2E9` | page |

**The governing rule, and it is the one most often broken:** Heritage Blue carries **structural
identity only** — navigation, headers, table framing, dividers, branded surfaces. It **never**
carries instructional meaning. Code syntax, callout highlights, state indicators and
instruction-bearing arrows use the functional palette below, not this one.

**Titles are contrast-corrected derivations, not palette hexes.** Slate Blue at title weight
fails the contrast floor, so slate's title is `#3C4D60`; bronze and brass share `#725637`. Only
navy's title is a raw palette hex, because Deep Navy already clears it. *Pulling a title back to
its palette hex breaks it — that exact regression has shipped once.*

---

## 2. FUNCTIONAL COLOUR — separate system, does not compete with the brand

| Token | Hex | Where |
|---|---|---|
| **Forge Red** | `#D46554` | danger / terminal error in graphics. **Functional, not a sixth brand colour** (Bible §26.9 reversed an earlier filing that called it one). Replaces `#F44747`, which measured 89% saturation against the palette ceiling of 49%. |
| Warning | `#C0392B` band · `#FCEBE9` tint · `#5C1A13` text | never reassigned since S109 |
| **Success green** | `#6A9955` | DJ-ruled, **deliberately the same green as a `//` comment**. The real terminal is brighter (~`#23d18b`). **Do not "correct" it.** One success green in the whole system. |
| Error (book UI) | `#f14c4c` | the diagnostic line of a compiler message. Distinct from Forge Red — different scope, don't merge them. |
| Body text | `#1D1D1F` | near-black, not Deep Navy |
| Code panel | `#1E1E1E` | the editor background |
| Contrast floor | **4.5:1** | non-negotiable; 3:1 for non-text boundaries |

**The eight section bands** are generated, not authored — `build_palette.py` re-lights canon
colours so groups separate by **lightness for location** and **hue for meaning**, one axis each,
never both. Run `build_palette.py --css` for the current 32 custom properties rather than copying
them; they have moved.

---

## 3. TYPE

**For SVG graphics — the common stack goes FIRST, always:**

```
font-family="Arial, Helvetica, sans-serif"     body / labels / prose
font-family="Courier New, monospace"           code, file paths, terminal
```

This is the default for every graphic, not a special mode. Figures load through `<img src>`,
which runs in secure static mode and **cannot fetch a webfont** — so any designer face placed
first is guaranteed to fall back on the reader's machine and the layout shifts after export.
**Never lead with** Inter, JetBrains Mono, Segoe UI, Consolas, Roboto, or any other designer face.

**For web pages** (the stylesheet, which *can* load fonts):

```
'Inter', -apple-system, sans-serif                                          body
ui-monospace, SFMono-Regular, Menlo, Consolas, 'Liberation Mono',
  'Courier New', monospace                                                  code and pre
```

**Oxanium appears only in the approved RoboLore wordmark**, which is an existing asset. Never
typeset it yourself.

---

## 4. CODE TREATMENT — ruled, with no exception list

| | |
|---|---|
| `<pre>` | bg `#1E1E1E` · border `1px solid #696969` · radius 6px · padding 15px · text `#e8e8e8` · 0.9em · line-height 1.8 |
| inline `<code>` | **translucent wash** `rgba(0,0,0,0.08)`, padding 2px 6px, radius 4px, 0.9em |
| `pre code` | resets the pill off — background none, padding 0, radius 0, 1em |

The inline pill is a wash rather than an opaque grey **on purpose**: inline code sits on 43
distinct backgrounds and only 46% of it is on the cream page. A wash inherits its ground instead
of fighting it, so one rule works on cream, on 40 callout colours, and on eight dark headers
where an opaque light pill rendered white text on light grey, silently. Ruled cost: on a coloured
callout the pill tints to that colour.

---

## 5. THINGS A FRESH CHAT WILL GET WRONG

1. **Real-world object colours are not palette colours.** A competition field has red goal tape,
   green markers, silver and black victims, red and green triangles. None is in Heritage Blue.
   The rule: **draw it in the palette, say the real colour in the words** — the goal strip is
   drawn Forge Red and captioned *red tape*. Green markers, when drawn, take `#6A9955`.
2. **Precedence.** RoboLore canon in `BRANDING/` is upstream on every brand value. The book
   applies and never redefines. Anything the book records about a brand value is provisional and
   an upstream ruling supersedes it.
3. **`css/book.css` is generated** (`build_css.py`) and class names are **derived from the values
   they carry** — `.td-ddd`, `.div-c-2e86ab`. So changing one colour renames every class carrying
   it, in every lesson. At last count 562 class names encode a hex. **A repaint is a rename, not a
   substitution.** Never hand-edit that file.
4. **Don't over-brand.** These are instructional graphics, not posters. Priorities in order:
   **clarity, hierarchy, consistency, polish.**

---

## 6. WHERE EACH VALUE CAME FROM

| Value | File |
|---|---|
| Approved five, withdrawal of the other five | `ROBOLORE_UPSTREAM_DELTA_S102.md` §1 |
| Same five as generator input | `build_palette.py` `CANON`, lines 32–37 |
| Forge Red, Warning triple, body, code panel, floor | `build_palette.py` lines 38–43 |
| Forge Red filed functional, not brand | Bible §26.9 |
| Graphic font stacks, Oxanium rule, over-branding | `ROBOLORE_GRAPHICS_CHAT_HANDOFF.md` §5, §7, §16 |
| Web font stacks, pre/code treatment | `css/semantic.css` |
| Structural-vs-semantic rule, title derivations | `BookComponentStandard.md` §5.0 *(prose only — its hex table is the withdrawn one)* |
| Success green ruling | Bible §22 |
| 562 hex-encoding class names | `ZUMO_COLOR_LEDGER.md` §1 |

---
*Extracted at S201 from `Weymuth/zumo`. Re-derive before acting — a count in a document is a lead,
not a finding.*
