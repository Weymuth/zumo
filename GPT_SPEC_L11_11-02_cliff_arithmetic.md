# SPEC — rebuild `L11_GRAPHIC_11-02_cliff_arithmetic.svg`

**Paste this into the graphics chat alongside `ROBOLORE_GRAPHICS_CHAT_HANDOFF.md`.**
This replaces a graphic that is already live. The design below already exists as a PNG mockup
and is good — the job is to rebuild it as a real SVG, not to redesign it.

---

## Why a rebuild is needed

The mockup is a flat raster with the text baked into the pixels. It cannot ship:

- **§21.2** — a drawn graphic must keep live `<text>`. A raster has none.
- The target filename is **`L11_GRAPHIC_11-02_cliff_arithmetic.svg`**. Lesson 11 references
  that exact name. Anything else lands as an orphan and the page keeps showing the old file.

---

## Keep exactly as designed

The layout is right. Reproduce it:

- Banner across the top, **flat `#0B1A2E`**, gold rule beneath, title
  **"GRAPHIC 11.2 — Why the Cliff Alarm Always Fires Too Late"** in white.
- Standfirst under the banner: *"The sensor sees white. It cannot tell you the floor is missing."*
- **Two photo panels side by side**, each with a small navy tab label: **SIDE VIEW** (robot at a
  table edge) and **TOP VIEW** (robot approaching a gap, 4.5 cm dimension arrow).
- **Two arithmetic boxes below them**, blue on the left, red on the right:
  - TIME YOU HAVE — sensor-to-wheel 4.5 cm · speed 25 cm/s · `4.5 ÷ 25 =` **180 ms** ·
    *"…before the wheels leave the table."*
  - TIME YOU MUST WAIT — widest legal gap 10 cm · same speed 25 cm/s · `10 ÷ 25 =` **400 ms** ·
    *"…before you may CALL it a cliff."*
- **Payoff bar**, cream/amber: **400 ms > 180 ms** and *"The alarm is not allowed to go off until
  220 ms AFTER the robot has already fallen."*
- **Conclusion strip**, flat `#0B1A2E`, white text: *"There is no threshold that works. Not a badly
  chosen one — there is NO SUCH NUMBER."* with the sub-line *"Going slower shrinks BOTH numbers.
  The ratio never changes. You cannot fix this by tuning."*

Every number above was checked against Lesson 11 §8A.4 and matches it verbatim. **Do not adjust
any of them.** The arithmetic is the point of the graphic.

---

## ONE content change

The speed row currently reads **"Robot speed at BASE_SPEED 150: 25 cm/s."**

`BASE_SPEED 150` is not in the book. Lesson 11 says the 25 cm/s came from *"a demo robot"*.
Change that row to:

> **Robot speed: 25 cm/s**

Nothing else about the row changes. (Full reasoning is parked in `ZUMO_PARKED_EXIT_ITEMS.md`.)

---

## Technical requirements — these are what break files

1. **Live `<text>`.** Every label, number and sentence is a real text element. No outlined text,
   no text baked into a photo. Use `<tspan>` for wrapped lines rather than separate `<text>`
   elements at hand-set positions.
2. **`xlink:href` on every `<image>`, never plain `href`.** Plain `href` is SVG 2; Illustrator
   parses SVG 1.1, cannot read it, and reports a MISSING LINK — the file renders perfectly in a
   browser and will not open for editing. Declare `xmlns:xlink="http://www.w3.org/1999/xlink"`
   on the root `<svg>`.
3. **Common font first**: `font-family="Arial, Helvetica, sans-serif"`. A stack that leads with
   Segoe UI or Inter cannot load through `<img src>` and every reader sees a shifted layout.
4. **Never resample a photograph.** Place it at its native resolution in a box of the right
   aspect ratio. A previous file came back with a 1200×503 source squashed into a 300×300 box.
5. **Photographs must be real Zumo photos.** Do not generate a robot. A generated board shows
   garbled silkscreen and a different OLED wordmark in each copy, and Pololu's credit line
   cannot be applied to an image that is not theirs.
6. **No byte budget is being given to you.** Do not compress, do not downscale to hit a size.
   Send it full-size; fitting happens after.
7. **Group each callout.** Put each numbered marker or labelled leader in its own
   `<g id="callout-1">` etc., so a marker and its leader move together.
8. **Corrections EDIT the element.** Do not paint a white rectangle over a defect and draw the
   fix on top — element count is how this is checked.
9. **Never render the `_r##` revision suffix as visible text** anywhere in the artwork.

---

## Photographs needed

Two, both of a real Zumo 32U4:

- **Side view** at a table edge, wheels still on the surface, front sensors overhanging.
- **Top view** approaching a gap, so the 4.5 cm sensor-to-wheel distance can be dimensioned.

If suitable photos are not available yet, build the file with correctly sized empty photo boxes
and everything else final — the images can be dropped in afterwards without touching the layout.

---
*Spec written S100 · target `L11_GRAPHIC_11-02_cliff_arithmetic.svg` · numbers verified against
Lesson 11 §8A.4*
