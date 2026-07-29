# RoboLore Book Component Standard

**Standard version: v01.0.1**

This document defines the visual components a RoboLore book is built from: what they are,
what they look like, how they are generated, and how conformance is proved.

It is written book-agnostic. The Zumo 32U4 curriculum appears throughout as illustration,
never as the rule.

---

## 1. Identity and conformance

**File:** `BookComponentStandard.md`, at the repository root, beside the book's canon document.

**Conformance stamp:** a file that conforms carries the string

```
RoboLore Book Component Standard v01.0.1
```

The stamp asserts conformance with a document that exists and can be read. A stamp that
names no readable document is circular and is prohibited — it asserts a string that exists
only because something asserts it.

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

Eight roles. Backgrounds are 10% accent mixed into the book's page colour. Body text is
always the book's primary text colour.

| Role | Background | Border | Title | Title contrast |
|---|---|---|---|---|
| slate | `#E3E2DC` | `#3D5266` | `#364A5E` | 7.04 |
| bronze | `#E9E4D8` | `#7B6240` | `#6A573D` | 5.44 |
| brass | `#F1EADC` | `#C9A463` | `#6A573D` | 5.44 |
| green | `#E3E4DA` | `#3F6B52` | `#375F4D` | 5.63 |
| amber | `#EAE4D5` | `#8A6420` | `#775922` | 5.12 |
| red | `#EAE0D6` | `#8C3A2E` | `#79352E` | 6.83 |
| purple | `#E6E1DE` | `#5B4B7A` | `#4F446F` | 6.78 |
| navy | `#DEDCD6` | `#0B1A2E` | `#0B1A2E` | 12.75 |

Page colour: `#F5F2E9`. Body text: `#0B1A2E`, contrast at or above 12.7:1 on every tint.

**Brass carries a bronze title.** Brass at title weight measures 2.57:1 and fails. Rather
than lighten the role or lower the contrast requirement, brass borrows bronze's title colour.
The palette bends to the standard, not the reverse.

### 5.1 Geometry

```
box:    background-color: {bg}; border-left: 4px solid {border};
        padding: 15px; margin: 20px 0; border-radius: 4px;
title:  font-weight: bold; margin-bottom: 8px; font-size: 1.05em; color: {title};
```

Geometry is unchanged from prior practice. **Adopting this standard is a repaint, not a
redesign.**

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

### 6.2 Outline by default

Marks are outline variants. Fill variants are reserved for state changes, where the fill
itself is one of the required signals.

---

## 7. The families

Twenty-four families. Forty-seven marks.

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

### 7.1 Two-state families

**BRAIN CHECK** carries two states:

| State | Icon | Colour |
|---|---|---|
| incomplete | `bookmark` outline | slate `#3D5266` |
| complete | `bookmark-check-fill` solid | deep navy `#0B1A2E` |

Three signals separate the states — fill, added check, and colour — so §5.2 is satisfied by
construction rather than by inspection.

### 7.2 Supporting marks

Not callout families. Generated from the same table, same shipping form.

**Bonus families:** `tools` practice · `flask` observation · `bug` sabotage

**Challenge card:** `bullseye` goal · `braces` logic · `puzzle` template ·
`folder2-open` work-in · `search` where-to-look

**Prose markers:** `code` · `hammer` build · `play` test · `eye` see ·
`arrow-right-circle` next

**Systems:** `ticket-perforated` exit ticket · `stopwatch` timer · `chat-dots` tutor ·
`box-seam` maker · `file-earmark-plus` going deeper · `images` image index ·
`table` quick reference · `journal-text` notebook · `trophy` milestones

**Battery levels:** `battery-full` full · `battery-half` half · `battery` low

### 7.3 Mark inventory

48 distinct icon files: 25 for the 24 families (BRAIN CHECK carries two), and 23 supporting
marks. The shipped icon folder holds exactly these and nothing else — a library ships
thousands of icons; a book ships the ones it uses, so that the folder can be asserted
against this table in both directions.

---

## 8. Collisions

A collision is one glyph carrying more than one meaning. Every collision below was live
practice, not a new problem introduced by this standard.

| Glyph | Meanings | Resolution |
|---|---|---|
| warning triangle | 3 | WARNING `exclamation-triangle` · PITFALLS `slash-circle` · SAFETY `shield-exclamation` |
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

*RoboLore Book Component Standard v01.0.1*
