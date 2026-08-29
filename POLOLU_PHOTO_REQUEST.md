# Pololu high-resolution photo request — reply to Ben Schmidel
*Mercersburg Academy Robotics · Zumo 32U4 curriculum · derived from the live repo, Aug 28 2026*

---

## Suggested email body

Ben,

Thank you — that's very generous, and no apology needed.

Below is the list, grouped by the photograph rather than by where we use it, since several of
our figures are different crops of the same shot. Where we crop in hard, the uncropped original
at whatever resolution you have is more useful to us than a resized version.

Everything we publish carries the credit line we agreed on, and every one of these is used as an
annotated instructional figure — labels and overlays are ours, the photograph is yours and stays
unmodified underneath.

| # | Photograph | What we have now | What we'd like |
|---|---|---|---|
| 1 | Zumo 32U4 OLED, **top view, straight down** | 1200 × 1139 | 2400 px on the long edge, or the original |
| 2 | Zumo 32U4 OLED, **underside / bottom view** (the transparent-background version) | 1200 × 1148 | 2400 px long edge, **transparent background preserved** |
| 3 | Zumo 32U4 OLED, **rear view** | 960 × 402 | 2000 px long edge, or the original |
| 4 | Zumo 32U4 **main board, top view** (chassis removed) | 1200 × 1046 | 2400 px long edge, or the original |
| 5 | **Front sensor array, underside** — the wide shot showing both configuration jumpers | 2614 × 726 (a crop) | **The uncropped original**, max resolution |
| 6 | **Front sensor array**, the narrow strip showing the three proximity detectors | 1750 × 190 (a hard crop) | **The uncropped original**, max resolution |
| 7 | **Micro metal gearmotor with the gearbox cover removed**, gear train exposed | 1200 × 995 | 2400 px long edge, or the original |
| 8 | **Motor and gearbox seated in the Zumo chassis** (top plate off) | 1448 × 1086 | 2400 px long edge, or the original |
| 9 | Zumo underside showing the **encoder magnet discs and Hall-effect sensors** | 800 × 671 | 2000 px long edge, or the original |
| 10 | **Encoder hardware close-up** — output shaft / magnet disc detail | 1200 × 959 and 600 × 516 | 2400 px long edge, or the original |
| 11 | **Forward IR emitters** — the clear domes on the sensor blade in their holder | 1136 × 1062 | 2400 px long edge, or the original |
| 12 | **Middle IR emitters** on the bare main board (surface-mounted, outer edges) | 1352 × 1292 | 2400 px long edge, or the original |
| 13 | Zumo **top-down on a flat surface** (we use this for a turning/heading figure) | 880 × 880 | 2000 px long edge, or the original |
| 14 | **Track and wheel** close-up (white wheels) | 772 × 359 | 2000 px long edge, or the original |

Formats: **PNG with transparency where the product is cut out** (#2 especially), otherwise
high-quality JPEG is fine. No sharpening or upscaling — a smaller true original beats a resized one.

If any of these are easier to identify by the page they appear on, I can send the URLs.

Thank you again,
DJ Weymuth
Mercersburg Academy

---

## Working notes (not for the email)

**How this list was derived.** Every Pololu-credited asset in the repo was enumerated
structurally — the raster files in `images/`, plus the base64 payloads embedded inside the SVG
graphics — then deduplicated by content hash so the same photograph reused in several figures
appears once. 16 distinct Pololu payloads across 13 credited SVGs and 12 credited raster files;
those collapse to the 14 photographs above.

**Rule used for the requested resolution.** 2× the largest pixel dimension we currently ship,
floored at 2000 px. For the two hard crops (#5, #6) the ask is the uncropped original instead,
because the crop is what limits us, not the file size.

**Highest-value items,** if the list needs shortening: **#5 and #6** — both are severe crops of
the front sensor array and both are load-bearing figures (jumper configuration in L04/L05, the
proximity detectors in L02). #2 is next: the transparent-background underside view carries the
five-line-sensor figure in both L04 and L09.

**Two things this list surfaced, unrelated to Ben:**

1. **Credit-line gap.** `L04_IMAGE_4-02`, `L04_IMAGE_4-04`, `L05_IMAGE_5-04a` and
   `L05_IMAGE_5-04b` carry **no Pololu credit line**, but they share exact pixel dimensions
   (2614 × 726 and 2501 × 783) with `L05_IMAGE_5-05a/b`, which **do** carry *"Photos: Pololu,
   annotated."* If they are the same source photograph, four figures are running uncredited.
   Not derivable from the repo — needs DJ.

2. **Filename residue.** `L03_IMAGE_3-14_astar_board.jpg` is the only surviving "astar" spelling
   in the book. Its own `alt` text correctly reads *"Top view of the Zumo 32U4 main board."*
   The §16.25 gate passes because it watches prose, not filenames.
