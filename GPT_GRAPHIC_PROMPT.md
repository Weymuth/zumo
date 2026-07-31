# ChatGPT prompt — Zumo book graphics

Two recipes. Pick by **subject**, not by what you want the file to look like.
A populated board, the chassis, jumper positions, a wired-up robot → **photograph**.
A memory ladder, flowchart, folder tree, state machine, comparison panel → **drawing**.

Everything in these prompts is checked mechanically by `svg_layout_audit.py` on arrival.
Nothing here is a matter of taste, so nothing here is negotiable.

---

## RECIPE 1 — A DRAWING

> Produce an SVG file, not an image.
>
> **Absolute rules**
> - The file must contain **no `<image>` tag and no `data:image/…;base64` string**. Draw the
>   subject with `<rect>`, `<circle>`, `<line>`, `<polyline>`, `<path>` and `<text>`.
> - **All label text must be live `<text>` elements.** Do not convert any text to outlines,
>   paths, or curves. Total `<path>` `d` data in the file must stay under 5,000 characters.
> - `font-family="Arial, Helvetica, sans-serif"` for prose and
>   `font-family="Courier New, monospace"` for code. **The first font in the stack must be one
>   of those two.** Do not lead with Inter, Segoe UI, Consolas, Roboto or any designer font —
>   the file is loaded through `<img src>`, which cannot fetch a webfont, so whatever you put
>   first is what fails.
> - `viewBox="0 0 1100 850"`. No `width`/`height` attributes.
>
> **Text must fit its box.** Every string has to sit fully inside whatever panel or rectangle
> it belongs to, with at least 6 units of padding on each side, measured in Arial at the size
> you set. If a line does not fit, rewrite it shorter or wrap it — do not let it hang over the
> edge, and do not shrink one caption to 60% of its neighbours to force it.
>
> **No two strings on the same baseline may overlap.**

---

## RECIPE 2 — A PHOTOGRAPH WITH LABELS

> Attached is a photograph and (where one exists) the current SVG.
>
> **Do not redraw the photograph. Do not trace the board. Do not reproduce silkscreen text as
> vector shapes. Do not resample, resize, crop, or re-render the photograph in any way.**
>
> If you cannot embed the photograph at its original pixel dimensions, say so and stop. Do not
> return a smaller version. *(This has happened: a 1200×503 source came back embedded at
> 300×300, letterboxed into a square box, and every label was then positioned against the
> distorted result.)*
>
> **Geometry**
> - Embed the photo as base64 JPEG in a single `href` attribute. Do **not** also write
>   `xlink:href` — that stores the payload twice and doubles the file.
> - The `<image>` box must match the photo's aspect ratio to within 2%. Never letterbox a wide
>   photo into a square box.
>
> **Grouping — this is the part that decides whether the file is editable**
> - One `<g>` per callout, `id="callout-1"`, `id="callout-2"`, and so on. Each group holds
>   **that callout's** badge circle, its number, its leader line, and its highlight rectangle.
> - One `<g>` per legend row, `id="legend-1"`, `id="legend-2"`, …
> - **Never group by object type.** All badges in one group and all leader lines in another
>   means moving a single marker requires hunting its parts across four places in the layer,
>   and the leader is left behind pointing at nothing.
>
> **Badges**
> - Each number needs `text-anchor="middle"`, its own `font-size`, and
>   `y = circle_cy + 0.355 × font-size`. Put these on the `<text>` element itself, not on a
>   parent group, so they survive regrouping.
>
> **Leaders** — one straight segment from badge edge to box edge, 3 units of clearance at each
> end. No elbows. No leader may cross another callout's badge or box. No two highlight boxes
> may overlap.
>
> **Text fitting and fonts** — same rules as Recipe 1.
>
> **Credit** — the photograph is Pololu's. Include a visible footer line reading
> `Robot photograph © Pololu Corporation — pololu.com` and repeat the attribution in `<desc>`.
>
> **Filename** — `L##_IMAGE_#-##_short_name.svg` for a photograph,
> `L##_GRAPHIC_#-##_short_name.svg` for a drawing. Suffix `_r01`, `_r02` for revisions.

---

## Never say these two things

**Never give it a byte budget.** Told to hit a size, it reports success and returns the
photograph byte-identical, having reworked only the vector overlay. File size is handled
locally by `fit_raster_svg.py`, with gate 37 as the backstop.

**Never ask for "high quality" or "high resolution" as a phrase.** Give the pixel number:
*at least 2× the on-screen box, so ≥ 640 px wide for a 320-unit box.*

---

## What it cannot be asked to do

Place a highlight box on a real component. It does not know where the power switch is in your
photograph and will put the box somewhere plausible-looking and wrong. Positions come from a
human reading a coordinate sheet. Everything else on this page is mechanical.
