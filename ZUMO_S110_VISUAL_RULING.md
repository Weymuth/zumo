# Visual design ruled — H2, Heritage sun-faded

**Session 110. DJ ruling. Nothing applied yet; this file exists so the decision survives
the session (§24.13 — a set that lives only in prose is not recorded).**

Every hex below is EMITTED from the derivation script, not typed. Every contrast figure is
computed, and the asserts listed in §6 all pass.

---

## 1. What was ruled

| # | decision | DJ |
|---|---|---|
| 1 | **Sun-faded is the look** — low chroma, light page | *"Definitely D — Best of both worlds"* |
| 2 | **But the bands must be Heritage**, not warm tan | *"None of these really are blue heritage focused"* |
| 3 | **H2 — canon bands kept deep enough for white cap text** | *"I like H2"* |

## 2. Why D was withdrawn, measured

D was ruled first and then withdrawn once its brand link was measured rather than asserted.
**Hue gap is the test**, because lightening a colour moves lightness and chroma enormously
and hue barely at all.

**Every hue and ΔE figure in this document is CIELAB** — LCh hue and ΔE76. That matters,
because the counts are metric-dependent: recomputed in HSV the ruled palette scores **4/6**
and warm earth **2/6**. The ranking survives the change of instrument (the ruled palette is
twice as aligned either way); the exact counts do not, and quoting them bare would be a
count with no named instrument (§24.10).

| direction | mean CIELAB hue gap to nearest canon hue | bands within 20° (CIELAB) |
|---|---:|---:|
| A warm earth (S109 ruling) | 39.4° | 1/6 |
| B deep earth | 39.6° | 1/6 |
| C cool bands | 38.0° | 1/6 |
| D sun-faded | 40.0° | 1/6 |
| D2 / D3 (navy cap text) | 39.3° / 39.5° | 1/6 |
| E "Heritage frame" | 23.3° | 3/6 |
| **H2 (ruled)** | **10.4°** | **5/6** |

**Two claims of mine were wrong and are recorded as wrong.** E was presented as "the one
that reconciles book and brand" when it is 3/6. And swapping D's cap text to Deep Navy was
allowed to sound like a brand link — it moved the alignment by 0.7° and changed nothing,
because cap text is not a band.

## 3. The palette

Page **`#F5F2E9`** Parchment · body **`#1D1D1F`** (15.03) · headings **`#7B6240`** Antique
Bronze (5.12) · cap text **white**.

| group | canon source | band | white on band | tint | text | text on tint |
|---|---|---|---:|---|---|---:|
| Theory & Concepts | Deep Navy | `#323846` | 11.73 | `#EAECF2` | `#444955` | 7.63 |
| Hardware & Code | Antique Bronze | `#4F402C` | 9.99 | `#F2EBE4` | `#544737` | 7.62 |
| Testing | Slate Blue | `#424E5B` | 8.49 | `#E9EDF2` | `#414A54` | 7.66 |
| Troubleshoot | Forge Red | `#86463B` | 7.11 | `#FFE7E1` | `#6D3B32` | 7.65 |
| Challenges | Warm Brass | `#75603B` | 6.01 | `#F5EBDE` | `#57472B` | 7.61 |
| Wrap Up & Reference | Deep Navy +18 deg | `#6E6D7D` | 5.06 | `#ECECF2` | `#494854` | 7.63 |

**WARNING is unchanged and never reassigned:** `#C0392B` band, `#FCEBE9` tint, `#5C1A13`
text, white on band 5.44. Nearest H2 band sits ΔE76 34.4 away.

**Troubleshoot is Forge Red `#D46554`**, the sixth palette colour §26.4 already gives the
alert role — not an invention.

**`Wrap Up & Reference` is the one derived hue in the set.** Heritage supplies five colours
and the six groups need six; Wrap Up takes Deep Navy's hue rotated **+18°** so it does not
collide with Theory. Recorded because it will look arbitrary later.

## 4. The structural finding, which outlives this ruling

**Heritage Blue is five colours but only TWO hue families.** In CIELAB, Deep Navy 276° and
Slate Blue 260° are 15.6° apart; Antique Bronze 77° and Warm Brass 82° are 4.8° apart. The
same collapse is confirmed in HSV, where the gaps are 5.0° and 3.7° — different numbers,
same finding, which is why it is stated as a finding at all. **Six section
groups cannot be separated by hue out of two hues.** They separate by LIGHTNESS, which is
exactly what §5.0.1's band ramp already said — one hue, lightness carries location. A
Heritage-focused book is a lightness ramp by construction, not by preference.

Consequence for §5.0.1: S109 superseded the Frost/Mist/Fog/Harbor/Steel ramp because the
book would no longer have five blue bands. **The five specific blues stay dead. The ramp
PRINCIPLE is now load-bearing again**, and `BAND_END` remains the mechanism. Do not read
S109's supersession as retiring lightness-as-wayfinding.

## 5. The generator

**`build_palette.py` v1.0** (repo root) derives this palette; entrypoint **`build()`**.
No band hex exists as a literal anywhere — the only colour literals are the five canon
values plus Forge Red, each of which is present in `ZUMO_SUPER_BIBLE.md`. `--check`
re-derives and compares against §3 of this file, so the table cannot drift from its
generator; `--css` emits the custom properties for `build_css.py` when the repaint starts.
Eight controls, including a known answer this file cannot supply (canon navy on parchment
reproduces `ColorPalette.md`'s stated **15.61**, computed 15.6146).

**Verified by a second instrument, not by re-reading:** the palette was rasterised and the
stripe colours read back out of the pixels — all thirteen backgrounds reach the screen at
the derived hex, and contrast recomputed from measured pixels matches the derivation to
**0.0000**.

## 6. Asserts that pass

white on every band floor **5.06** · callout text on every tint floor
**7.61** · body on parchment **15.03** · bronze headings on parchment
**5.12** · min band separation ΔE76 **9.5** · nearest band to WARNING ΔE76 **34.4** ·
darkest band vs code panel `#1e1e1e` ΔE76 **15.5** · mean chroma C* **16.7**
(against warm earth's 32.0).

The code-panel figure is new to H2 and was not a risk in any earlier direction: H2's Theory
band is the darkest colour in the book outside the editor itself. 15.5 is separable and is
the tightest pair in the palette — if a band is ever re-lit, that is the one to re-measure.

## 7. Unchanged from `ZUMO_S109_VISUAL_SPEC.md`

Colour is not a code · six groups, five expandable plus unnumbered Troubleshoot · vertical
left rail on `<details>` with no JavaScript · no section numbers in the nav · the 4×4 lesson
grid · the measured cost (~4 rules in `css/book.css`, zero lesson files) · and all six of that
document's open items, none of which this ruling closes.

**§2 of that document — the warm-earth palette table — is SUPERSEDED by §3 above.**
Nothing else in it moves.
