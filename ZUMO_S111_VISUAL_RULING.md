# Visual design ruled — S111, eight bands

**Session 111. DJ rulings, every one taken from a rendered specimen. Nothing applied to the
lessons yet; this file exists so the decisions survive the session (§24.13 — a set that
lives only in prose is not recorded).**

Every hex below is EMITTED from `build_palette.py` v1.1, not typed. `--check` re-derives and
compares against §2, so the table cannot drift from its generator. **SUPERSEDES
`ZUMO_S110_VISUAL_RULING.md` §3.** Recorded in `ZUMO_SUPER_BIBLE.md` as v8.99.

---

## 1. What was ruled, and what it cost

| # | decision | DJ |
|---|---|---|
| 1 | **The +18° Wrap Up rotation is dropped** | *"Drop the 18 degree blue."* |
| 2 | **Heritage Slate Blue leaves the band set**; Testing takes a new teal at 200° | *"Testing and theory are super close. Whats the difference"* |
| 3 | **Rose 337° and hunter green 148° join**; amber is rejected | *"Amber doesn't really work. Slate violet looks good Rose looks great Green looks great."* |
| 4 | **Chroma damping 0.62 → 0.90** | *"I don't love the dirt brown."* |
| 5 | **Rose and green stay at 0.62**, quieter than the wayfinding bands | *"I like the rose and green from A."* |
| 6 | **Challenges goes to 1.20**, the gamut ceiling | *"Can we change challenge to brass?"* |
| 7 | **Cap text stays white on every band, no exceptions** | *"mixing white and black font looks horrible"* |
| 8 | **Challenge-card headers take the §9 band**, superseding v8.87's Antique Bronze | *"go with the new #9 color we just created"* |

**Decision 7 is why decision 6 stops where it does.** Real Warm Brass is `#C9A463` at L* 69
and white on it is **2.34** — a band carrying white cap text can never be brass. `#7A5905` is
Warm Brass re-lit to L* 40 and is the most brass available.

## 2. The palette

Page **`#F5F2E9`** Parchment · body **`#1D1D1F`** (15.03) ·
headings **`#7B6240`** Antique Bronze (5.12) · cap text **white**.

| group | canon source | band | white on band | tint | text | text on tint |
|---|---|---|---:|---|---|---:|
| Theory & Concepts | Deep Navy | `#1F2A3D` | 14.41 | `#E9ECF5` | `#41495A` | 7.65 |
| Hardware & Code | Antique Bronze | `#433014` | 12.56 | `#F5EBE0` | `#57462F` | 7.68 |
| Testing | Teal 200 | `#00474B` | 10.48 | `#D9F1F2` | `#0B5154` | 7.68 |
| Troubleshoot | Forge Red | `#832920` | 9.12 | `#FFE4DC` | `#7A3328` | 7.46 |
| Rose | Rose 337 | `#6C4861` | 7.67 | `#F7E9F2` | `#5D4054` | 7.69 |
| Challenges | Warm Brass | `#7A5905` | 6.44 | `#FCEAD0` | `#5F4508` | 7.61 |
| Green | Hunter Green | `#4F7155` | 5.49 | `#E3F0E5` | `#354F3A` | 7.66 |
| Wrap Up & Reference | Deep Navy | `#6F7582` | 4.62 | `#E9ECF5` | `#41495A` | 7.65 |

**WARNING is unchanged and never reassigned:** `#C0392B` band, `#FCEBE9` tint,
`#5C1A13` text. Nearest band sits ΔE76 23.8 away — **down from 34.4 in the
ruled six**, because raising Troubleshoot's chroma moved it toward WARNING. DJ was shown the
number and the premise it rested on was WRONG in his favour's disfavour: he said *"Warning
doesn't show up much"*, and `build_family_map` counts **80 WARNING blocks**, the fifth most
common callout in the book. Re-ruled with the corrected number: *"Yeah, but i'm still ok with
it."*

**Rose and Green name COLOURS, not section groups.** What they label is UNRULED and must be
decided before either can appear on a page.

**The tint and text columns are OUT OF SCOPE for this repaint.** v8.87 Scope C is brand layer
only and leaves all 1,048 callouts untouched; the columns are derived and kept because the
callout arc will need them.

## 3. Why Slate Blue left — leave-one-out, all nine candidates

Deep Navy and Slate Blue are **15.6°** apart, and at this chroma 15.6° is invisible. DJ found
it by eye before any number said so.

| drop | tightest remaining pair |
|---|---|
| **Testing (Slate Blue)** | **18.9** |
| Theory (Deep Navy) | 17.5 |
| any of the other six | 9.4 |
| Hardware | **5.3 — worse** |

Only removing a navy helps, because the crowding IS the two navies. Dropping Hardware makes it
worse because Hardware is the band standing between them in the ramp.

## 4. What was measured and rejected

**Amber at 57°** — 20.4° from WARNING, and its band landed **ΔE76 11.6 from Challenges**,
indistinguishable from its own neighbour. **Burgundy** — 21.7° from Troubleshoot; its band
read as a sibling of Forge Red, not a category. **Reordering the ramp for separation** —
brute-forced all 40,320 orderings; the tightest pair is 18.9 either way, neighbour spacing
moves 23.7 → 24.5, and the cost is that lightness stops tracking progress through the lesson.
Reading order kept. **A third Heritage-style hue family** — members 5–16° apart yield ΔE76
9.6–12.3, which rebuilds the defect this ruling removes.

## 5. Floors, all computed

white on every band floor **4.62** · callout text on every tint floor **7.46** ·
body on parchment **15.03** · bronze headings on parchment **5.12** ·
min band separation ΔE76 **22.2** (Theory & Concepts / Testing) ·
darkest band vs code panel `#1E1E1E` ΔE76 14.8

## 6. Known clip, declared not hidden

`EXPECTED_CLIPS = ['Testing']`. Testing asks chroma 25.5 at L* 26 and carries 19.4 —
sRGB has no more teal there. Lowering the request until the numbers agree moves the band to
`#004648`, **which is not the hex DJ ruled on**, so the ruled hex is kept and the clip is
recorded. CONTROL D fails on any UNDECLARED clip and was control-run at chroma 2.0, where 3 of
8 bands clip.

## 7. Three claims of mine that were wrong, recorded

1. **"Eight bands is the ceiling."** Wrong. I tested band counts against fixed ramp
   parameters instead of asking whether the parameters could move; nine spread evenly at
   L0 31 / step 4.2. The count was never the constraint, the ramp was.
2. **"Gradients are unruled."** Wrong, and inherited from the S111 handoff rather than
   grepped. v8.87 banned them absolutely. A decided question was re-opened for most of a
   session.
3. **"WARNING is rare"** was accepted from a grep that returned zero because the label does
   not sit as bare text between tags. The parser says 80 blocks.
