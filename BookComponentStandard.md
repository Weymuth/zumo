# RoboLore Book Component Standard

**Standard version: v01.9.0**

This document defines the visual components a RoboLore book is built from: what they are,
what they look like, how they are generated, and how conformance is proved.

It is written book-agnostic. The Zumo 32U4 curriculum appears throughout as illustration,
never as the rule.

---

## 1. Identity and conformance

**File:** `BookComponentStandard.md`, at the repository root, beside the book's canon document.

**Conformance stamp:** a file that conforms carries the string

```
RoboLore Book Component Standard vMAJOR.MINOR
```

**The stamp carries MAJOR.MINOR only.** A stamp that embedded the patch digit would be
invalidated by every patch bump, so every stamped file would need re-stamping for a fix that
changed nothing a stamp asserts — and the stamps would silently fall behind instead. This
mirrors the two-homes rule the book's own canon already applies to its visible version banner.

The stamp asserts conformance with a document that exists and can be read. A stamp that
names no readable document is circular and is prohibited — it asserts a string that exists
only because something asserts it.

**One authority.** The version line at the top of this document is the only version authority.
The stamp is derived from it and must agree with it on MAJOR.MINOR. Nothing else in this
document may carry a version.

**Predecessor.** This standard supersedes `ZUMO Callout Standard v1.0`, which named no
document. The stamp and every occurrence of it are removed as part of adopting this standard.

---

## 2. Versioning

One scheme. Three tiers.

```
v#        major      structural change to meaning or role
v#.#      moderate   approved addition or expanded rule
v#.#.#    minor      correction that does not change the decision
```

No letter suffixes. No parallel scheme. A book's delivery mechanics (visible banners, hidden
version comments, per-file bump rules) are defined in that book's own canon document and are
delivery mechanics, not a second versioning system.

---

## 3. Scope

### 3.1 What this standard governs

Components: the bounded visual objects that carry a family of meaning — callouts, marks, and
legend entries.

### 3.2 What this standard does not govern

**Sections are not components.** Section fences, part banners, and anchor spines are
structural. They are generated from the anchor spine and proved by byte gates, and they stay
with those generators. A section fence that happens to look like a callout is still a fence.

**Navigation is not a component.** Section pills, part banners, and nav colour groups run
their own scheme and are governed separately.

**Code-theme literals are out of scope.** Colours inside rendered code blocks reproduce the
reader's editor theme. They are not brand surface and must not be reinterpreted as drift.

### 3.3 The collapse rule

A **family** is a role, not a string. Multiple title wordings collapse into one family when
they name the same role.

- `Note`, `Note: setup() vs loop()`, `Accuracy Note` — one family, NOTE.
- `Translate it`, `Build from YOUR plan` — one family, WRITE IT.
- `Quick Reference`, `Quick Reference → Motors`, `Quick Reference → Timing` — one family.

A per-instance heading (`"expected ';' before..."` under a troubleshooting family) is an
**entry**, not a family.

Titles are carried by more than one HTML construct — a bold `<div>` and a `<strong>` are both
title carriers. A census that walks only one construct undercounts. Any count of families or
instances must state which carriers it walked.

---

## 4. The three primitives

Everything in this standard is built from three primitives. This is the core of the document.

### 4.1 The mark

A **mark** is one glyph, one family, no wrapper.

```
mark(family) -> <img> of the family's icon, pre-coloured to the family's role
```

One family has exactly one mark. The mark does not vary by placement, by lesson, by role
context, or by which wrapper contains it.

### 4.2 The callout

A **callout** is a mark plus a title plus a body, inside a role-coloured box.

```
callout(family, title, body) -> box + border + mark + title + body
```

### 4.3 The legend entry

A **legend entry** is a mark plus a family name, with no box.

```
legend_entry(family) -> mark + family name
```

### 4.4 Why the distinction matters

A legend **cites** families; it does not instantiate them. A legend that shows a different
glyph than the callout it documents has failed at its only job.

Therefore: **the mark is identical in every wrapper.** This is not a tolerance for two
rendering contexts — there is one mark, and the wrappers differ.

Legend entries are **generated**, never hand-authored. Hand-authored legends drift from the
components they document, and the drift is silent because nothing compares them. Two
observed failure modes, both from hand-authoring:

- **Over-declaration** — the legend names families that do not appear in the scope it
  documents.
- **Omission** — families ship without appearing in the legend that claims to cover them.

Generation from the mark table makes both impossible by construction.

---

## 5. The palette

### 5.0 Heritage Blue

**Heritage Blue is the approved RoboLore palette. It is a named palette, not a single hex.**

| Name | Hex |
|---|---|
| Deep Navy | `#162337` |
| Slate Blue | `#43566B` |
| Antique Bronze | `#8C6A43` |
| Warm Brass | `#C3A36A` |
| Parchment | `#F4EBDD` |

Heritage Blue governs **structural identity** — navigation, lesson and section headers, table
framing, neutral instructional UI, and branded surfaces.

**It does not replace semantic callout colour.** NOTE, TIP, INSIGHT, WARNING, THE WALL and
their kind may hold distinct functional colours where the colour supports meaning. They sit
*beneath* Heritage Blue; they do not compete with it.

Of the seven roles below, four are structural and carry a Heritage Blue border exactly —
**slate, bronze, brass, navy**. Three are semantic — **green, amber, purple**. The page
colour is Parchment and body text is Deep Navy.

**Red was retired at S91**, with the SAFETY family that was its only member (DJ ruling:
*"get rid of safety and make them all warning"*). A role with no families is not a spare
slot, it is an unasserted colour — so it left the table with its family. The seven SAFETY
callouts were reassigned to WARNING in L01, L06, L07, L08 and L09.

**Titles are contrast-corrected derivations, not palette hexes.** Slate Blue at title weight
does not clear the contrast floor, so slate's title is `#3C4D60`, a darkened Slate Blue; bronze
and brass share `#725637`, a darkened Antique Bronze. Only navy's title is a Heritage Blue hex,
because Deep Navy already clears it. A title that has been pulled back to its palette hex has
been broken, not corrected — see §7.1, where exactly that had happened.

### 5.0.1 Section band ramp

Wayfinding is not meaning. A reader asking *where am I* and a reader asking *what is this*
are asking different questions, and answering both with hue makes one answer interfere with
the other.

**Hue carries meaning. Lightness carries location.** One axis each, never both.

The section bands are therefore a single derived scale in Heritage Blue's own hue, not five
peer colours. They run light to dark across the lesson arc, so the page opens light and
deepens as the work does.

| Band | Hex | Name |
|---|---|---|
| learn | `#CBD3DE` | Frost Blue |
| build | `#AFBCCE` | Mist Blue |
| verify | `#96A8C0` | Fog Blue |
| extend | `#7E95B4` | Harbor Blue |
| close | `#708BAF` | Steel Blue |

**Rules the ramp must satisfy:**

- Every band sits in Heritage Blue's hue family. A band is a step on one scale, not a colour
  of its own.
- **No band may land within 30° of any semantic role.** This is what keeps a green section
  from arguing with a green callout inside it.
- Deep Navy is the text colour on every band, and the bar the bands sit on. One text colour
  throughout — a scale that needs the text to switch partway is two scales.
- Lightness is monotonic across the ramp. A step that reverses is not a step.
- No gradients on any banded surface.

The ramp deliberately carries no accent marks. A brass or bronze edge measures under 1.4:1
against the lighter steps and reads as dirt rather than emphasis; bronze and brass occupy the
same lightness region the ramp passes through, so no shade of them separates across the whole
scale.

---

Seven roles. Backgrounds are 10% accent mixed into the book's page colour. Body text is
always the book's primary text colour.

| Role | Background | Border | Title | Title contrast |
|---|---|---|---|---|
| slate | `#E2DCD2` | `#43566B` | `#3C4D60` | 6.36 |
| bronze | `#EADECE` | `#8C6A43` | `#725637` | 5.11 |
| brass | `#EFE4D2` | `#C3A36A` | `#725637` | 5.38 |
| green | `#E2DECF` | `#3F6B52` | `#386049` | 5.30 |
| amber | `#E9DDCA` | `#8A6420` | `#74541B` | 5.17 |
| purple | `#E5DBD3` | `#5B4B7A` | `#53446F` | 6.35 |
| navy | `#DED7CC` | `#162337` | `#162337` | 11.05 |

Page colour: `#F4EBDD`. Body text: `#162337`, contrast at or above 11.0:1 on every tint.

**Brass carries a bronze title.** Brass at title weight measures 1.90:1 and fails. Rather
than lighten the role or lower the contrast requirement, brass borrows bronze's title colour.
The palette bends to the standard, not the reverse.

### 5.1 Geometry

```
box:    background-color: {bg}; border-left: 4px solid {border};
        padding: 15px; margin: 20px 0; border-radius: 4px;
label:  font-weight: bold; font-size: 0.9em; color: {title};
title:  font-weight: bold; margin-bottom: 8px; font-size: 1.05em; color: {title};
```

**The label and the title are TWO separate block elements (Option C, DJ ruling S92).** The
label holds the family word and NOTHING else; the descriptive title, if the block has one,
is its own element beneath. A block with no descriptive title carries the label ALONE, and
that lone element keeps the title geometry above — `margin-bottom: 8px; font-size: 1.05em` —
because there is nothing to subordinate it to. **The last element in the stack always carries
the 8px gap to the body**, which is what lets the body start without a `<br>`.

**Why two elements and not one.** The label element now contains exactly one string, so
`lesson_inventory` and `gen_component` can read a block's family by **exact match** instead
of parsing a family word out of the front of authored prose. That parsing was what made the
amber scheme unclassifiable at S91 — one scheme found doing six jobs — and it is the whole
return on this change.

**Both elements are BLOCK elements.** `<strong>` is not acceptable, because it is inline and
therefore carries none of the three properties the spec names: the 8px gap under the title,
the 1.05em size, and block display so the body starts on its own line without a `<br>`.

**The family word is authored in CAPS, literally (DJ ruling S92).** No `text-transform`. The
source string and the rendered string are the same string, so the exact-match guarantee above
holds against the file rather than against the file plus a stylesheet. This reverses an earlier
S92 ruling for normal text, taken and then withdrawn once counting showed the three §6.6a
families are themselves Icon Guide entries: 262 of 999 callout titles render caps, and the
guide has been the source of that convention since before 📘 NOTE existed. **Caps everywhere
was chosen over normal text everywhere because the latter is 229 further labels in families
this sweep never opens.**

**The cost, recorded.** 178 blocks gained a line, so titled callouts now stack two bold lines.
A standalone bold label arguably reads more like a heading than an inline suffix did — the
"more categories" worry DJ raised when the option was first framed. He accepted it. §5.1 also
grew from one title element to two, which is why this section, not just the book, changed.

**Correction, S91.** The sentence that stood here — *"Geometry is unchanged from prior
practice"* — was **false for the title element**. The live book carried **794 titles as
`<strong>` against 55 in this form**, so this section specified the minority shape while
claiming it was the norm. Found by counting, not by reading; the claim had been approved
the same day without being checked against the book (§24.10).

Swept S91 on DJ's ruling (*"make all the strong categories div to keep it conical"*): 794
titles converted, **119 now-redundant `<br>` removed** — each existed only to break an
inline title. Structure only; every existing `color:` declaration and every other attribute
carried over verbatim. `book_gates` gate 34 holds it.

**The cost, recorded so nobody reverts it as a bug.** `<strong>` is semantic and a bold div
is not, so 794 titles lost their emphasis cue for screen readers. The title remains the
first text inside the block, so nothing became unreachable. DJ ruled the block form for
consistency; this paragraph is the price of that ruling, not an argument against it.

**Standing note, S92.** The 1.05em size is carried on **990 of 1,048** live callout titles and
is generated by `gen_component`. DJ raised moving it to 1.0em and it is **PARKED, not
declined** — it is a 990-block change plus an amendment here, and it would reduce the three
properties named above to two, taking one leg out of S91's justification for the block form.
It is not an Option C setting and must not be folded into one.

Otherwise geometry is unchanged. **Adopting this standard is a repaint, not a redesign.**

### 5.2 Colour is never the only signal

No meaning may be carried by colour alone. Where two families share a role, the mark is the
only separator and must be silhouette-distinct at rendered size. Where a component has
states, the states must differ by at least two signals — for example fill, glyph, and colour
together, not colour alone.

---

## 6. The icon library

**Bootstrap Icons.** One library, zero exceptions.

- 2,078 icons, 16px grid, outline and fill variants
- Free for commercial use, modification, recolouring, and inclusion in a sold work
- No attribution required on the page
- **One obligation:** a `LICENSE` file containing the permission text must be kept alongside
  the icon assets

The permission wording is the MIT license, a standard template used by many unrelated
projects. MIT is not an organisation and has no connection to Bootstrap Icons.

### 6.1 Shipping form

Marks ship as `<img>`, pre-coloured per role:

```
height: 1.35em; vertical-align: -0.3em
```

`currentColor` does not resolve through `<img>`, so colour is baked at generation time. This
is why the mark and its role are generated together from one table.

**The library folder is the generator's input, not the shipped marks.** Two folders, and the
distinction is load-bearing:

- **`icons/`** — the unmodified library files, one `fill="currentColor"` each, plus the
  `LICENSE` required above. The generator never writes here. This folder is asserted against
  the table in §7.3.
- **`marks/`** — generated output, one file per shipped mark, colour baked. Regenerating must
  reproduce it byte-for-byte.

A generator that writes over its own input destroys the only copy that can prove what it
started from.

### 6.2 Outline by default

Marks are outline variants. Fill variants are reserved for state changes, where the fill
itself is one of the required signals.

---

## 7. The families

Twenty-five families. Forty-eight marks.

**APPROVED — DJ ruling, S91, 29 July 2026.** The roster below is canon: twenty-five families,
their marks, and their role assignments. THE WALL's name was raised for rename at the same
ruling and DJ kept it. This records the roster only. **The semantic palette — green, amber,
red, purple — is a separate gate and is NOT approved by this entry.**

| Family | Icon | Role |
|---|---|---|
| LEARN | `book` | slate |
| NOTE | `sticky` | slate |
| EXPLANATION | `chat-square-text` | slate |
| BUILDS ON | `arrow-repeat` | slate |
| WHERE THIS GOES | `rocket` | slate |
| HOW THIS SECTION WORKS | `pin-angle` | slate |
| KEY TERM | `key` | bronze |
| GLOSSARY | `journal-bookmark` | bronze |
| INSIGHT | `stars` | bronze |
| DO THIS NOW | `play-circle` | brass |
| MY PLAN | `pencil-square` | brass |
| WRITE IT | `keyboard` | brass |
| ENGINEER'S LOG | `journal-text` | brass |
| TIP | `lightbulb` | green |
| HINT | `compass` | green |
| IF YOU'RE STUCK | `life-preserver` | green |
| CHECKPOINT | `check-circle` | green |
| ANSWER | `unlock` | green |
| WARNING | `exclamation-triangle` | amber |
| COMMON PITFALLS | `slash-circle` | amber |
| BRAIN CHECK | `bookmark` / `bookmark-check-fill` | purple |
| THE LOGIC | `braces` | purple |
| THE WALL | `bricks` | purple |
| THE GOAL | `bullseye` | navy |
| FINISHED EARLY? | `flag` | navy |

### 7.1 Two-state families

**BRAIN CHECK** carries two states:

| State | Icon | Colour |
|---|---|---|
| incomplete | `bookmark` outline | slate title `#3C4D60` |
| complete | `bookmark-check-fill` solid | deep navy `#162337` |

**Two signals separate the states — fill and the added check.** Colour does not separate them
and never did: the two values measure **1.82:1** against each other, and the superseded pair
(`#3D5266` / `#0B1A2E`) measured **2.16:1**. Both sit far below any threshold at which colour
carries meaning. §5.2 is satisfied by fill and glyph alone.

This entry previously read `#3D5266`, slate's *border*, and claimed colour as a third signal.
It was the only mark in the standard not drawn from its role's title colour, and the exception
was protecting a signal that measurement shows was never present. Corrected at v01.1.0: **every
mark takes its role's title colour, with no exceptions.**

### 7.2 Supporting marks

Not callout families. Generated from the same table, same shipping form.

**Bonus families:** `tools` practice · `flask` observation · `bug` sabotage

**Challenge card:** `bullseye` goal · `braces` logic · `puzzle` template ·
`folder2-open` work-in · `search` where-to-look

**Prose markers:** `code` · `hammer` build · `play` test · `eye` see ·
`arrow-right-circle` next

**Systems:** `ticket-perforated` exit ticket · `stopwatch` timer · `chat-dots` tutor ·
`box-seam` maker · `file-earmark-plus` going deeper · `images` image index ·
`table` quick reference · `trophy` milestones

**Battery levels:** `battery-full` full · `battery-half` half · `battery` low

**A supporting mark promoted to a family leaves the supporting list.** ENGINEER'S LOG was
carried under Systems as *notebook*. The nav affordance and the callout name one thing — the
student's engineering notebook — so they are one family, and the nav entry CITES it under §4.4
rather than holding a second copy of the glyph. Two entries would have put one glyph on two
grounds in two colours, which §4.1 forbids.

**Grounds.** Each group above sits on one ground, and the ground decides whether the group is
in scope for this table.

| Group | Ground | In scope |
|---|---|---|
| Bonus families | page tint | yes |
| Challenge card | page tint | yes |
| Prose markers | page tint | yes |
| Battery levels | page tint | yes |
| Systems | filled band | no |

**Colour.** A supporting mark belongs to no family and therefore inherits no role. It takes
its colour from what sits behind it:

- **On the page colour or a role tint** — body text. Supporting marks are separated from one
  another by glyph, never by colour, so §5.2 is satisfied without a role.
- **On a filled band or any other coloured ground** — the mark belongs to whatever scheme owns
  that ground, not to this table. It is out of scope here and must be generated with that
  scheme, not ahead of it.

The second case is not a deferral of convenience. A mark coloured before the ground it sits on
has been decided is a guess that a later pass has to find and undo.

### 7.3 Mark inventory

48 distinct icon files: 26 for the 25 families (BRAIN CHECK carries two), and 22 supporting
marks. The shipped icon folder holds exactly these and nothing else — a library ships
thousands of icons; a book ships the ones it uses, so that the folder can be asserted
against this table in both directions.

---

## 8. Collisions

A collision is one glyph carrying more than one meaning. Every collision below was live
practice, not a new problem introduced by this standard.

| Glyph | Meanings | Resolution |
|---|---|---|
| warning triangle | 2 | WARNING `exclamation-triangle` · PITFALLS `slash-circle` |
| open book | 3 | LEARN `book` · GLOSSARY `journal-bookmark` · EXPLANATION `chat-square-text` |
| blue book | 2 | NOTE `sticky` · HOW THIS SECTION WORKS `pin-angle` |
| pencil / memo | 2 | DO THIS NOW `play-circle` · MY PLAN `pencil-square` |
| compass | 2 | HINT `compass` · IF YOU'RE STUCK `life-preserver` |
| eye | 2 | observation `flask`, freeing `eye` for the see marker |
| magnifier | 3 | only `search` survives, on where-to-look; INSIGHT takes `stars` |

**The warning collision is the load-bearing one.** WARNING and COMMON PITFALLS share the
amber role, so the glyph is their only separator. Under §5.2 a shared glyph there would make
the two families indistinguishable.

**The open-book collision crosses a role boundary.** LEARN and EXPLANATION are slate;
GLOSSARY is bronze. The colour difference is not sufficient on its own, because LEARN and
EXPLANATION remain same-role siblings.

### 8.1 Near-collisions to hold

These are distinct but close, and any future assignment must not narrow the gap:

- Four circle-outline marks ship: `play-circle`, `check-circle`, `slash-circle`,
  `arrow-right-circle`. Adding a fifth requires an explicit decision.
- Two journal marks ship: GLOSSARY `journal-bookmark` and ENGINEER'S LOG `journal-text`. They
  share an identical cover outline and binding spine and are separated by their interior mark
  alone. A third journal requires an explicit decision.
- THE WALL `bricks` and quick reference `table` are the only rectangular-grid marks. They do
  not share a context today — `table` is a Systems mark on a filled band — but any future
  assignment must keep them apart.
- MY PLAN `pencil-square` and WRITE IT `keyboard` are adjacent items in the same list and
  share the brass role. They are separated by glyph alone, and deliberately encode the
  book's own distinction between planning in prose and writing code.

---

## 9. Numbered marks

Numbering defeats icon libraries — there is no room for two digits inside a 16px glyph.
Numbered marks are therefore purpose-built geometry, generated from a rule rather than
hand-drawn per number.

```
outer radius       9.6
inner radius       6.2
fill               #7B6240 flat
number             font-size 9, bold, #F5F2E9
centring           x = 10, y = 10, dominant-baseline central
two-digit          x = 9.7  (dx 0.3)
render             1.1em inline
```

Gradients are prohibited. A set of hand-drawn numbered files is replaced by one function.

---

## 10. Generation

All components are generated from one table by one generator.

**Why generation, not authoring.** Delivery targets may strip `<style>` blocks and `class=`
attributes, so output must be complete inline HTML. Inline HTML authored by hand cannot be
kept consistent across a book, and cannot be repainted at all — every change would be a
find-and-replace across every file. Generated from a table, a palette change is a table edit
and a re-run.

**One table, one generator, three emitters** — mark, callout, legend entry.

### 10.1 What conformance requires

1. Every mark in the book is emitted by the generator.
2. Every family has exactly one mark.
3. No glyph carries two families.
4. Every legend entry is generated, and names only families in scope.
5. Every component's role comes from the palette in §5.
6. Geometry matches §5.1 byte-for-byte.

### 10.2 Gate design

A gate must be able to distinguish the states it reports.

A gate that matches raw file text cannot tell a visible element from a commented-out one, and
will report a condition it never tested. **When a gate checks placement or visibility, it
must strip what the reader cannot see before matching.**

A substring test cannot distinguish a flat fill from a gradient containing that substring.
Where a gate asserts an exact value, it must compare the whole value.

Every gate is control-run against the real historical defect it exists to catch, in both
directions — confirmed failing on the defect, confirmed passing on the fix — before its
verdict is trusted.

---

## 11. Change procedure

1. Amend the table in this document.
2. Bump this standard's version per §2.
3. Re-run the generator.
4. Re-run the gates.
5. Bump the affected book files per that book's own delivery mechanics.

A component may not be changed in a book file directly. The table is the source; the files
are output.

---

*RoboLore Book Component Standard v01.9*
