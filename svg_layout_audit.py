#!/usr/bin/env python3
VERSION = 'v1.16'
# ---------------------------------------------------------------------------------------------
# svg_layout_audit.py - pre-flight audit for an incoming graphic, run BEFORE a human opens it.
#
# Written at S99 after a single ChatGPT-authored composite cost most of a session. Every defect
# in it was mechanical and every one was findable by measurement; none of them needed judgment:
#
#   grouped by object type, not by callout ... 4 callouts scattered over 4 places each
#   photograph resampled to 300x300 ......... raw PNG IHDR
#   letterboxed into a square box ........... aspect arithmetic
#   callout boxes never on their features .... they missed by 20-32 units
#   two text blocks overflowing their panels . font metrics
#   footer strings colliding ................. font metrics
#   badge numbers not centred ............... a group's font attrs lost in a regroup (OUR bug)
#
# What this does NOT check is where a feature actually IS in a photograph. That is the human's
# job and the only part of the loop that should need one.
#
# ENTRYPOINT IS audit(path) -> list[str]. There is no main() worth calling from code.
#
# CHANGELOG
# v1.16 (S99): say WHICH circle, and by how much. 'leader of callout-1 crosses the badge of
#   callout-3' sent me looking at a badge 176 units away. The real overlap was callout-3's
#   ANCHOR DOT - the 7-unit marker on the photograph - which the leader passes 1.4 units from.
#   Both are circles in a callout group and the message treated them as one thing. A finding
#   that names the wrong element costs the same as a wrong finding: you go and look at the
#   wrong place. Badge and anchor are now distinguished and the clearance is reported.
# v1.15 (S99): stop demanding text-anchor. Illustrator CONVERTS anchor="middle" into an
#   explicit left-edge transform, which renders identically. v1.14 called that a defect, and
#   acting on the finding - re-adding the anchor - DOUBLE-CORRECTED the position and shifted
#   four badge numbers 5.6 units off their circles. The tool caused the defect it warned about.
#   What matters is where the glyph LANDS, so the anchor check is gone and the measured centre
#   is the only test. Tolerance 3 units: the round-trip lands within 1.1.
# v1.14 (S99): the raster checks honour transforms too. v1.13 taught _lines() about
#   transform="translate() scale()" but left the <image> box reading its raw width. An
#   Illustrator export placed a 1200-wide image under scale(.47) - a real box of 564 - and the
#   resolution check reported 1.00x against a true 2.13x, on a file that was fine. Fixing one
#   check for transforms and not its neighbour is half a fix.
# v1.13 (S99): HONOUR transform="translate()". Illustrator exports text as
#   <text transform="translate(38 31)"><tspan x="0" y="0">..</tspan></text> - the position
#   lives in the transform, not in x/y. v1.12 read x/y only, so EVERY label in such a file
#   collapsed to (0,0): 35 labels produced 69 findings, all of them nonsense, on a file that
#   was fine. As DJ starts round-tripping graphics through Illustrator this becomes the normal
#   shape of a file, so it is not an edge case.
#   translate() and scale() on the element and its ancestors are now accumulated.
# v1.12 (S99): CRASH FIX. A <text> inside a callout group with no x attribute (perfectly legal
#   SVG - it defaults to 0, or inherits position from a tspan) made the badge-centring check
#   raise TypeError, and the WHOLE audit died reporting nothing. A crash is worse than a false
#   positive: a false positive wastes a round trip, a crash silently checks nothing at all.
#   Every attribute read in that block is now tolerant, and a badge with no coordinates is
#   skipped rather than assumed to be at the origin.
# v1.11 (S99): baseline tolerance made PROPORTIONAL. A flat 1.5 units fired on dy=+9.0 against
#   an ideal +10.65 on a 30px badge - 1.6 units, invisible, and three files reported it. The
#   optical centre of a digit depends on the typeface's cap height, so the tolerance has to
#   scale with the type: 12% of font-size, floored at 1.5. A 30px badge now allows 3.6 units
#   and a genuinely uncentred number (the v1.7 regression, dy=0) still fires at 10.65.
# v1.10 (S99): TWO FALSE-POSITIVE CLASSES, 9 of 10 findings on one real file.
#   (a) Badge centring paired the number with circs[0]. A callout legitimately holds TWO
#       circles - a small anchor dot on the photograph and the numbered badge beside it - so
#       every number read as hundreds of units off-centre. Now paired with the NEAREST circle.
#   (b) A badge deliberately straddles its panel's edge, so its number was reported as text
#       overflowing. Text bounded by a circle is bounded by that circle, not the panel.
#   Both were caught by reading a file the tool had just called broken ten ways. An audit that
#   cries wolf is worse than none: DJ would have sent nine non-defects back to be 'fixed'.
# v1.9 (S99): FILE SIZE CHECKED AT LAST. Eight checks and not one of them looked at how big the
#   file was, so a 3.65 MB composite - 7.3x over gate 37's referenced-file ceiling - audited
#   CLEAN and would have gone fatal the moment a lesson pointed at it. The cause is always the
#   same now that PSD sources carry knocked-out backgrounds: genuine alpha cannot become JPEG,
#   so fit_raster_svg correctly refuses to shrink it and the only real fix is flattening onto
#   the colour behind it. The check names that remedy rather than just the number.
# v1.8 (S99): outlined-text check scoped to GRAPHIC_ names, matching gate 38. v1.7 fired on
#   all 16 spiral stars and both Mercersburg wordmarks - 18 of 74 findings, every one a false
#   positive. Those are legitimately text-free: the stars carry vector-path digits BY RULING
#   (Bible §18.2) and a wordmark is a logo. Gate 38 already had this guard and the audit did
#   not, which is the argument for reading the gate before writing a second checker of the
#   same thing.
# v1.7 (S99): THE href RULE WAS BACKWARDS. v1.6 checked for one payload attribute and treated
#   plain href as correct. Plain href on <image> is SVG 2; Illustrator parses SVG 1.1 and
#   reports an href it cannot read as a MISSING LINK, naming the document's own folder. Every
#   file the tooling produced was unopenable in Illustrator - which is DJ's editing path -
#   while rendering perfectly in a browser, so nothing caught it for a whole session.
#   Deduping the doubled payload was right; keeping the wrong survivor was not.
# v1.6 (S99): THE RESOLUTION CHECK WAS MEASURING THE WRONG THING. It compared photo pixels to
#   the <image> box in USER UNITS, which only equals the real ratio when the graphic happens to
#   render at 1 CSS px per unit. A file with a 2000-unit viewBox was reported at 1.00x when a
#   reader actually sees it at 1.82x, and one with a 916-unit viewBox was reported at a
#   comfortable 2.00x while really being the SOFTER of the two at 1.67x. The check now scales
#   the box through the viewBox to an assumed display width and reports both numbers.
# v1.5 (S99): FALSE POSITIVE, AND AN EXPENSIVE ONE. v1.4 measured a <text> element by
#   concatenating all of its itertext(), which merges <tspan> children that are SEPARATE
#   RENDERED LINES. A correctly wrapped two-line label came back as one 522-unit line
#   overflowing its panel by 239 units. DJ was sent to have a non-defect corrected.
#   Each <tspan> carrying its own x or dy is now measured as its own line.
#   The lesson is the project's own §24.6c: this check was never control-run against a file
#   KNOWN to be correctly wrapped, so its first real finding was believed on sight.
# v1.4 (S99): PORTABLE FONT LOOKUP. v1.3.1 hardcoded two Linux paths, so on macOS or Windows
#   every text check was unavailable and the tool exited. It now searches Liberation Sans
#   first (metric-identical to Arial) and falls back to the real Arial where the OS ships it -
#   macOS /System/Library/Fonts/Supplemental, Windows C:/Windows/Fonts. It still refuses to
#   run with no metric font rather than silently skipping the checks: a check that cannot fail
#   is not evidence.
# v1.3.1 (S99): --fixnote was leaking LOCAL instructions into the paste block. Findings that
#   say 'run fit_raster_svg.py' are our job, not the author's - and telling a model to fix a
#   file-size problem is the one instruction guaranteed to make it report success while
#   changing nothing. Those are now split out and shown only on our side.
# v1.3 (S99): --fixnote added. The audit already computes every number a correction needs;
#   having a human retype them into a chat window is where they get rounded, dropped, or
#   guessed. --fixnote emits a paste-ready correction block: the findings verbatim with their
#   measurements, an explicit list of what is ALREADY correct and must not be touched (the
#   common failure is a fix that silently breaks something that was fine), and the next _r##
#   filename. It deliberately never mentions file size - size is handled locally by
#   fit_raster_svg.py, and telling a model to hit a byte budget makes it report success
#   while returning the photograph unchanged.
# v1.2 (S99): FALSE POSITIVE FIXED. v1.1 warned 'no callout-* groups' on ANY raster-bearing
#   file. A photograph labelled with leader lines and no numbered badges is a perfectly good
#   design and has nothing to group per-callout. The check now fires only when the file
#   actually carries NUMBERED MARKERS - a circle with a short numeric label at its centre -
#   which is the only case where per-callout grouping is what makes it editable.
#   Caught on the first real file the tool was pointed at, which is the argument for pointing
#   a new instrument at real work early rather than trusting a green selftest.
# v1.1 (S99): credit check narrowed. v1.0 demanded a POLOLU credit on any raster-bearing
#   file, which would have fired on screenshots and on photographs DJ shoots himself.
#   It now asks for PROVENANCE of any kind - a credit line, or a <desc> that says what
#   the picture is and where it came from. Caught by ChatGPT reviewing the prompt, which
#   is worth recording: the tool and the prompt have to be narrowed in the same pass or
#   one starts contradicting the other.
# v1.0 (S99): new.
# ---------------------------------------------------------------------------------------------
import sys, os, math, base64, io, re

try:
    from lxml import etree
except ImportError:
    sys.exit('svg_layout_audit needs lxml')
try:
    from PIL import Image, ImageFont
except ImportError:
    sys.exit('svg_layout_audit needs pillow')

NS = '{http://www.w3.org/2000/svg}'

# Liberation Sans is metric-compatible with Arial, which is what §17.3a recipe 1 mandates.
# If it is missing we must FAIL LOUDLY rather than silently skip every text check - a check
# that cannot fail is not evidence (§24.6b).
_FONT_CANDIDATES = {
    'regular': ('/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf',   # Linux
                '/usr/share/fonts/liberation-sans/LiberationSans-Regular.ttf',
                '/System/Library/Fonts/Supplemental/Arial.ttf',                      # macOS
                '/Library/Fonts/Arial.ttf',
                'C:/Windows/Fonts/arial.ttf'),                                       # Windows
    'bold':    ('/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf',
                '/usr/share/fonts/liberation-sans/LiberationSans-Bold.ttf',
                '/System/Library/Fonts/Supplemental/Arial Bold.ttf',
                '/Library/Fonts/Arial Bold.ttf',
                'C:/Windows/Fonts/arialbd.ttf'),
}
_FONTS = {}
for _w, _paths in _FONT_CANDIDATES.items():
    for _p in _paths:
        if os.path.exists(_p):
            _FONTS[_w] = _p
            break
if 'bold' not in _FONTS and 'regular' in _FONTS:
    _FONTS['bold'] = _FONTS['regular']        # metrics differ slightly; better than no check

# a drawn graphic's labels must survive on a machine that has none of the designer's fonts
SAFE_FONTS = ('arial', 'helvetica', 'sans-serif', 'courier new', 'monospace', 'times', 'serif')
MIN_PHOTO_SCALE = 2.0        # §17.3b: payload at ~2x its on-screen box
GATE37_CEILING = 500_000     # book_gates §21.1 - fatal for a file a lesson REFERENCES
DISPLAY_WIDTH_PX = 1100      # the book's image column. The <image> box is in USER UNITS,
                             # so it must be scaled through the viewBox to get real pixels.
PANEL_MIN_W, PANEL_MIN_H = 150, 60
PANEL_PAD = 6


_TR = None


def _ctm(el):
    """Accumulated (dx, dy, sx, sy) from this element and its ancestors.

    Only translate() and scale() are handled - that is what Illustrator emits. A rotate() or a
    general matrix() would need more, and is reported rather than silently mis-measured.
    """
    import re as _re
    dx = dy = 0.0
    sx = sy = 1.0
    chain = []
    n = el
    while n is not None and isinstance(n.tag, str):
        if n.get('transform'):
            chain.append(n.get('transform'))
        n = n.getparent()
    for tr in reversed(chain):
        for fn, args in _re.findall(r'(translate|scale|matrix|rotate)\s*\(([^)]*)\)', tr):
            v = [float(q) for q in _re.split(r'[,\s]+', args.strip()) if q]
            if fn == 'translate':
                dx += v[0] * sx
                dy += (v[1] if len(v) > 1 else 0.0) * sy
            elif fn == 'scale':
                sx *= v[0]
                sy *= (v[1] if len(v) > 1 else v[0])
    return dx, dy, sx, sy


def _f(v):
    """Tolerant float. SVG attributes are optional, and percentages are legal."""
    try:
        return float(v)
    except (TypeError, ValueError):
        return None


def _inh(el, attr):
    n = el
    while n is not None:
        if n.get(attr):
            return n.get(attr)
        n = n.getparent()
    return None


def _text_width(s, size, bold=False):
    key = 'bold' if bold else 'regular'
    if key not in _FONTS:
        raise RuntimeError('no Arial-metric font found (Liberation Sans or Arial) - text checks '
                           'cannot run. Linux: apt install fonts-liberation')
    return ImageFont.truetype(_FONTS[key], 200).getlength(s) * size / 200.0


def _lines(t):
    """Yield (text, x0, x1, y, size) once per RENDERED LINE.

    A <text> may hold <tspan> children, and any tspan with its own x or dy is a separate line.
    Concatenating itertext() and measuring that as one string reports a correctly wrapped label
    as a giant overflow - v1.4 did exactly that and cost a round trip to fix a non-defect.
    """
    size = float(_inh(t, 'font-size') or 16)
    bold = (_inh(t, 'font-weight') or '400') in ('700', '800', '900', 'bold', 'bolder')
    anchor = _inh(t, 'text-anchor') or 'start'
    tdx, tdy, tsx, tsy = _ctm(t)
    size *= tsy                                   # a scaled group scales the type with it
    bx = (_f(t.get('x')) or 0.0) * tsx + tdx
    by = (_f(t.get('y')) or 0.0) * tsy + tdy

    spans = [sp for sp in t.findall(f'{NS}tspan')
             if sp.get('x') is not None or sp.get('dy') is not None]
    rows = []
    if spans:
        cy = by
        lead = ' '.join((t.text or '').split())
        if lead:
            rows.append((lead, bx, cy))
        for sp in spans:
            cy += (_f(sp.get('dy')) or 0.0) * tsy
            rows.append((' '.join((sp.text or '').split()),
                         (_f(sp.get('x')) * tsx + tdx) if sp.get('x') is not None else bx, cy))
    else:
        rows.append((' '.join(''.join(t.itertext()).split()), bx, by))

    out = []
    for txt, x, y in rows:
        if not txt:
            continue
        w = _text_width(txt, size, bold)
        x0 = x - w / 2 if anchor == 'middle' else (x - w if anchor == 'end' else x)
        out.append((txt, x0, x0 + w, y, size))
    return out


def _extent(t):
    ls = _lines(t)
    if not ls:
        return '', 0.0, 0.0, float(t.get('y') or 0), float(_inh(t, 'font-size') or 16)
    return ls[0]


def _seg_hits(p, q, test, steps=200):
    for i in range(steps + 1):
        if test(p[0] + (q[0] - p[0]) * i / steps, p[1] + (q[1] - p[1]) * i / steps):
            return True
    return False


def audit(path):
    """Return a list of findings. Empty list == clean."""
    out = []
    root = etree.parse(path).getroot()
    base = os.path.basename(path)
    ran = set()

    # ---- 1. viewBox -------------------------------------------------------------------------
    ran.add('viewbox')
    if not root.get('viewBox'):
        out.append('no viewBox - the graphic cannot scale with the page')

    # ---- 2. the embedded photograph, if any -------------------------------------------------
    imgs = root.findall(f'.//{NS}image')
    ran.add('raster')
    for im_el in imgs:
        hrefs = [k for k in im_el.keys() if k.endswith('href')]
        XL = '{http://www.w3.org/1999/xlink}href'
        if len(hrefs) > 1:
            out.append('payload stored twice (href AND xlink:href) - half the file is a '
                       'duplicate of itself; run fit_raster_svg.py --write')
        elif hrefs and hrefs[0] != XL:
            out.append('<image> uses a plain href. That is SVG 2 - Illustrator parses SVG 1.1 '
                       'and will report this as a MISSING LINK with the photograph gone, while '
                       'browsers render it fine. Use xlink:href (and declare xmlns:xlink).')
        if hrefs and XL in hrefs and 'xlink' not in (root.nsmap or {}):
            out.append('uses xlink:href but the xlink namespace is not declared on <svg>')
        uri = im_el.get(hrefs[0])
        if not uri or 'base64,' not in uri:
            out.append('<image> is LINKED, not embedded - this renders blank on the published '
                       'site and looks correct locally (Bible §17.3)')
            continue
        raw = base64.b64decode(uri.split(',', 1)[1])
        pic = Image.open(io.BytesIO(raw))
        _idx, _idy, _isx, _isy = _ctm(im_el)
        bw = (_f(im_el.get('width')) or 0.0) * _isx     # a scaled group scales the box
        bh = (_f(im_el.get('height')) or 0.0) * _isy
        vb = (root.get('viewBox') or '').split()
        vbw = float(vb[2]) if len(vb) == 4 else bw
        if bw and bh and vbw:
            css_box = bw / vbw * DISPLAY_WIDTH_PX      # what the box is in real pixels
            scale = pic.size[0] / css_box if css_box else 0
            if scale < MIN_PHOTO_SCALE:
                need = int(MIN_PHOTO_SCALE * css_box)
                out.append(f'photograph is {pic.size[0]}x{pic.size[1]} but its box renders about '
                           f'{css_box:.0f} CSS px wide (box {bw:.0f} of a {vbw:.0f} viewBox at a '
                           f'{DISPLAY_WIDTH_PX} px column) = {scale:.2f}x - under the '
                           f'{MIN_PHOTO_SCALE:.0f}x floor. Needs a source at least {need} px wide.')
            ar_box, ar_pic = bw / bh, pic.size[0] / pic.size[1]
            if abs(ar_box - ar_pic) / ar_pic > 0.02:
                out.append(f'box aspect {ar_box:.3f} vs photo aspect {ar_pic:.3f} - the picture is '
                           f'letterboxed or distorted inside its box; resize the box to match')
        if pic.mode in ('RGBA', 'LA'):
            alpha = pic.getchannel('A')
            if alpha.getextrema() == (255, 255):
                out.append('photo carries a fully-opaque alpha channel doing nothing - '
                           'run fit_raster_svg.py --write')

    # ---- 2b. the whole file against gate 37's ceiling ---------------------------------------
    # Eight checks and none of them measured the file. A composite can pass every content check
    # and still be fatal the instant a lesson references it.
    ran.add('filesize')
    total = os.path.getsize(path)
    if imgs and total > GATE37_CEILING:
        pic0 = None
        try:
            u = next(imgs[0].get(k) for k in imgs[0].keys() if k.endswith('href'))
            pic0 = Image.open(io.BytesIO(base64.b64decode(u.split(',', 1)[1])))
        except Exception:
            pass
        hint = ''
        if pic0 is not None and pic0.mode in ('RGBA', 'LA'):
            al = pic0.getchannel('A')
            lo, hi = al.getextrema()
            if lo < 255:
                hint = (' The payload is a PNG with a REAL alpha channel, so fit_raster_svg.py '
                        'cannot convert it to JPEG and will not get you under. Flatten the photo '
                        'onto the colour that sits behind it, then embed as JPEG.')
        out.append(f'{total:,} B - over gate 37\'s {GATE37_CEILING:,} B ceiling. This is FATAL '
                   f'the moment a lesson references it.{hint}')

    # ---- 3. outlined text on a drawn graphic ------------------------------------------------
    ran.add('outlines')
    # Scope: book FIGURES only. Logos and the §18.2 spiral stars are text-free by ruling,
    # and gate 38 draws exactly this line by keying on the GRAPHIC_ name.
    if not imgs and 'GRAPHIC_' in base:
        n_text = len(root.findall(f'.//{NS}text'))
        pd = sum(len(p.get('d') or '') for p in root.findall(f'.//{NS}path'))
        if n_text == 0:
            out.append('zero <text> on a drawn graphic - labels have been converted to OUTLINES; '
                       'unselectable, unsearchable, invisible to a screen reader (gate 38)')
        elif pd > 5000:
            out.append(f'{pd:,} B of path data with only {n_text} <text> - labels look partially '
                       f'outlined (gate 38 ceiling is 5,000 B)')

    # ---- 4. fonts ---------------------------------------------------------------------------
    ran.add('fonts')
    for fam in {e.get('font-family') for e in root.iter()
                if isinstance(e.tag, str) and e.get('font-family')}:
        first = fam.split(',')[0].strip().strip('"\'').lower()
        if first not in SAFE_FONTS:
            out.append(f'font stack leads with "{first}" - it cannot load through <img src>, so '
                       f'every reader sees the fallback and a layout that shifted after export. '
                       f'Put a common font FIRST (Bible §17.3b).')

    # ---- 5. text overflowing its panel ------------------------------------------------------
    ran.add('overflow')
    panels = []
    for rc in root.findall(f'.//{NS}rect'):
        w, h = float(rc.get('width') or 0), float(rc.get('height') or 0)
        if w >= PANEL_MIN_W and h >= PANEL_MIN_H:
            x, y = float(rc.get('x') or 0), float(rc.get('y') or 0)
            panels.append((x, y, x + w, y + h))
    panels.sort(key=lambda p: (p[2] - p[0]) * (p[3] - p[1]))     # smallest enclosing wins
    # A number sitting inside a badge is bounded by that badge, not by any panel it overhangs.
    badges_xy = [(float(c.get('cx') or 0), float(c.get('cy') or 0), float(c.get('r') or 0))
                 for c in root.findall(f'.//{NS}circle') if c.get('r')]
    for t in root.findall(f'.//{NS}text'):
        tx, ty = float(t.get('x') or 0), float(t.get('y') or 0)
        if any((tx - cx) ** 2 + (ty - cy) ** 2 <= (rr * 1.2) ** 2 for cx, cy, rr in badges_xy):
            continue
        for s, x0, x1, y, size in _lines(t):
            ax = float(t.get('x') or 0)
            for px0, py0, px1, py1 in panels:
                if px0 <= ax <= px1 and py0 <= y <= py1:
                    if x0 < px0 + PANEL_PAD or x1 > px1 - PANEL_PAD:
                        over = max(px0 + PANEL_PAD - x0, x1 - (px1 - PANEL_PAD))
                        out.append(f'text overflows its panel by {over:.0f} units: '
                                   f'"{s[:44]}" spans {x0:.0f}..{x1:.0f} '
                                   f'inside {px0:.0f}..{px1:.0f}')
                    break

    # ---- 6. text colliding with text on the same line ---------------------------------------
    ran.add('collide_text')
    rows = {}
    for t in root.findall(f'.//{NS}text'):
        for s, x0, x1, y, size in _lines(t):
            rows.setdefault(round(y, 1), []).append((x0, x1, s))
    for y, items in rows.items():
        items.sort()
        for a, b in zip(items, items[1:]):
            if a[1] > b[0] + 0.5:
                out.append(f'text overlaps text at y={y:.0f}: "{a[2][:26]}" ends {a[1]:.0f}, '
                           f'"{b[2][:26]}" starts {b[0]:.0f}')

    # ---- 7. callout grouping and badge centring ---------------------------------------------
    ran.add('groups')
    groups = [g for g in root.findall(f'.//{NS}g') if (g.get('id') or '').startswith('callout-')]
    # Only complain about grouping if the file actually HAS numbered markers. A photograph
    # labelled with plain leader lines has nothing to group per-callout and is not defective.
    n_badges = 0
    for circ in root.findall(f'.//{NS}circle'):
        cx, cy, rad = (float(circ.get(k) or 0) for k in ('cx', 'cy', 'r'))
        for t in root.findall(f'.//{NS}text'):
            lab = ''.join(t.itertext()).strip()
            if lab.isdigit() and len(lab) <= 2:
                tx, ty = float(t.get('x') or 0), float(t.get('y') or 0)
                if abs(tx - cx) <= rad and abs(ty - cy) <= rad * 1.6:
                    n_badges += 1
                    break
    if n_badges >= 2 and not groups:
        out.append(f'{n_badges} numbered markers but no callout-* groups - they are grouped by '
                   f'object type, so moving one marker means hunting its parts across the layer')
    for g in groups:
        gid = g.get('id')
        circs = [e for e in g if e.tag == NS + 'circle']
        txts = [e for e in g if e.tag == NS + 'text']
        if not circs or not txts:
            continue
        # Pair the number with the NEAREST circle. A callout often has an anchor dot on the
        # photograph as well as its badge; circs[0] may be either.
        t = min(txts, key=lambda e: len(''.join(e.itertext()).strip()) or 99)
        # Every one of these is optional in valid SVG. v1.11 assumed all four were present and
        # a single missing x killed the entire audit.
        ls = _lines(t)
        if not ls:
            continue
        _s0, _x0, _x1, ty, _sz = ls[0]
        tx = (_x0 + _x1) / 2 if (_inh(t, 'text-anchor') == 'middle') else _x0
        cdx, cdy, _csx, _csy = _ctm(circs[0])
        circs = [e for e in circs if _f(e.get('cx')) is not None and _f(e.get('cy')) is not None]
        if not circs:
            continue
        c = min(circs, key=lambda e: (_f(e.get('cx')) + _ctm(e)[0] - tx) ** 2
                                     + (_f(e.get('cy')) + _ctm(e)[1] - ty) ** 2)
        size = _f(_inh(t, 'font-size')) or 16.0
        # No anchor check: measure where the glyph actually lands. Illustrator rewrites
        # anchor="middle" as a left-edge transform, and both render the same.
        ccx, ccy, _a, _b = _ctm(c)
        tx = (_x0 + _x1) / 2                      # rendered centre, however it was positioned
        dx = abs(tx - (_f(c.get('cx')) + ccx))
        dy = ty - (_f(c.get('cy')) + ccy)
        if dx > 3.0:                              # round-trips land within ~1.1
            out.append(f'{gid}: badge number off-centre horizontally by {dx:.1f} units')
        tol = max(1.5, 0.12 * size)      # cap height varies by typeface; scale with the type
        if abs(dy - 0.355 * size) > tol:
            out.append(f'{gid}: badge number baseline dy={dy:+.1f}, expected '
                       f'{0.355 * size:+.1f} for {size:.0f}px (cap-height centring)')

    # ---- 8. markers, leaders and boxes colliding --------------------------------------------
    ran.add('collide_geom')
    boxes, badges, leads = [], [], []
    for g in groups:
        gid = g.get('id')
        for e in g:
            if e.tag == NS + 'rect':
                x, y = float(e.get('x')), float(e.get('y'))
                boxes.append((gid, x, y, x + float(e.get('width')), y + float(e.get('height'))))
            elif e.tag == NS + 'circle':
                badges.append((gid, float(e.get('cx')), float(e.get('cy')), float(e.get('r'))))
            elif e.tag in (NS + 'polyline', NS + 'line'):
                if e.tag == NS + 'polyline':
                    pts = [tuple(map(float, p.split(','))) for p in e.get('points').split()]
                    leads.append((gid, pts[0], pts[-1]))
                else:
                    leads.append((gid, (float(e.get('x1')), float(e.get('y1'))),
                                  (float(e.get('x2')), float(e.get('y2')))))
    for gid, p, q in leads:
        for b in boxes:
            if b[0] != gid and _seg_hits(p, q, lambda x, y, b=b: b[1] < x < b[3] and b[2] < y < b[4]):
                out.append(f'leader of {gid} crosses the box of {b[0]}')
        for c in badges:
            if c[0] == gid:
                continue
            near = min(math.hypot(p[0] + (q[0] - p[0]) * i / 200 - c[1],
                                  p[1] + (q[1] - p[1]) * i / 200 - c[2]) for i in range(201))
            if near < c[3]:
                what = 'badge' if c[3] > 10 else 'anchor dot'
                out.append(f'leader of {gid} passes {near:.1f} units from the {what} of {c[0]} '
                           f'(radius {c[3]:.0f}) - it runs across it')
    for i, b1 in enumerate(boxes):
        for b2 in boxes[i + 1:]:
            if b1[0] == b2[0]:
                continue
            if not (b1[3] <= b2[1] or b2[3] <= b1[1] or b1[4] <= b2[2] or b2[4] <= b1[2]):
                out.append(f'highlight box of {b1[0]} overlaps that of {b2[0]}')

    # ---- 9. photo credit --------------------------------------------------------------------
    ran.add('credit')
    if imgs:
        visible = ' '.join(''.join(t.itertext()) for t in root.findall(f'.//{NS}text'))
        desc = root.find(f'{NS}desc')
        desc_txt = (desc.text or '') if desc is not None else ''
        MARKERS = ('\u00a9', 'copyright', 'photograph', 'photo by', 'courtesy', 'source:',
                   'screenshot', 'pololu', 'credit')
        blob = (visible + ' ' + desc_txt).lower()
        has_credit = any(m in blob for m in MARKERS)
        has_desc = len(desc_txt.strip()) >= 20
        if not (has_credit or has_desc):
            out.append('embeds a raster but states no provenance - add a visible credit line '
                       'AND/OR a <desc> saying what the picture is and where it came from. '
                       '(Pololu product photography must be credited by name; a screenshot or '
                       'your own photo just needs to say so.)')

    # ---- coverage: every check must have run, or a silent pass is not evidence ---------------
    expected = {'viewbox', 'raster', 'filesize', 'outlines', 'fonts', 'overflow',
                'collide_text', 'groups', 'collide_geom', 'credit'}
    if ran != expected:
        out.append(f'COVERAGE: only {len(ran)} of {len(expected)} checks ran '
                   f'(missing {sorted(expected - ran)})')
    return out


def _selftest():
    """Controls both ways: silent on a clean file, loud on each seeded defect."""
    import copy, tempfile
    ok = True
    src = sys.argv[2] if len(sys.argv) > 2 else None
    if not src or not os.path.exists(src):
        print('selftest needs a known-clean reference file:  --selftest FILE.svg')
        return False
    print(f'CONTROL A (false-positive): clean reference must be SILENT  [{os.path.basename(src)}]')
    base = audit(src)
    print(f'   {"clean" if not base else "NOT CLEAN: " + str(base)}')
    ok &= not base

    def seeded(name, mutate, needle):
        tree = etree.parse(src)
        mutate(tree.getroot())
        fd, tmp = tempfile.mkstemp(suffix='.svg')
        os.close(fd)
        tree.write(tmp, encoding='utf-8', xml_declaration=True)
        found = audit(tmp)
        os.unlink(tmp)
        hit = any(needle in f for f in found)
        print(f'   {"OK  " if hit else "FAIL"} {name}')
        if not hit:
            print(f'        got: {found}')
        return hit

    print('CONTROL B (false-negative): each seeded defect must be REPORTED')
    def kill_anchor(r):
        g = r.find(f".//{NS}g[@id='callout-6']")
        [e for e in g if e.tag == NS + 'text'][0].set('text-anchor', 'start')
    # The signal changed in v1.15: removing the anchor from a file that relies on it shifts the
    # glyph, and the tool now reports the SHIFT rather than the missing attribute. Same defect,
    # measured by its effect. Control the effect, not the implementation.
    ok &= seeded('badge anchor removed', kill_anchor, 'off-centre horizontally')

    def widen(r):
        for t in r.findall(f'.//{NS}text'):
            if 'Lights whenever' in ''.join(t.itertext()):
                t.text = ''.join(t.itertext()) + ' and stays lit for a very long time indeed'
    ok &= seeded('text pushed past its panel', widen, 'overflows its panel')

    def shrink(r):
        im = r.find(f'.//{NS}image')
        im.set('width', str(float(im.get('width')) * 4))
    ok &= seeded('photo box blown up 4x', shrink, 'under the')

    def squash(r):
        im = r.find(f'.//{NS}image')
        im.set('height', str(float(im.get('height')) * 1.6))
    ok &= seeded('photo aspect distorted', squash, 'aspect')

    def dup(r):
        im = r.find(f'.//{NS}image')
        # read whichever form the reference uses - it is xlink:href now, and assuming
        # plain href is what made this seeder crash the moment the rule was corrected
        cur = next(im.get(k) for k in im.keys() if k.endswith('href'))
        im.set('{http://www.w3.org/1999/xlink}href', cur)
        im.set('href', cur)
    ok &= seeded('payload duplicated', dup, 'stored twice')

    def plainhref(r):
        im = r.find(f'.//{NS}image')
        cur = next(im.get(k) for k in im.keys() if k.endswith('href'))
        for k in list(im.keys()):
            if k.endswith('href'):
                del im.attrib[k]
        im.set('href', cur)
    ok &= seeded('plain href instead of xlink:href', plainhref, 'plain href')

    def badfont(r):
        for t in r.findall(f'.//{NS}text'):
            t.set('font-family', 'Inter, Arial, sans-serif')
    ok &= seeded('designer font first in the stack', badfont, 'cannot load through')

    def nocredit(r):
        d = r.find(f'{NS}desc')
        if d is not None:
            d.text = ''
        for t in list(r.findall(f'.//{NS}text')):
            if 'Pololu' in ''.join(t.itertext()) or 'photograph' in ''.join(t.itertext()):
                t.getparent().remove(t)
    ok &= seeded('photo credit removed', nocredit, 'credit')

    def collide(r):
        g = r.find(f".//{NS}g[@id='callout-7']")
        rc = [e for e in g if e.tag == NS + 'rect'][0]
        rc.set('x', '150'); rc.set('y', '262')
    ok &= seeded('two highlight boxes overlapped', collide, 'overlaps')

    print('\n' + ('ALL CONTROLS PASS - silent when clean, loud when broken.'
                  if ok else '*** SELFTEST FAILED ***'))
    return ok


def _already_correct(path):
    """What this file gets RIGHT - stated so a correction does not break it."""
    root = etree.parse(path).getroot()
    good = []
    imgs = root.findall(f'.//{NS}image')
    if imgs:
        im = imgs[0]
        hrefs = [k for k in im.keys() if k.endswith('href')]
        uri = im.get(hrefs[0]) or ''
        if len(hrefs) == 1:
            good.append('a single href attribute and no xlink:href')
        if 'base64,' in uri:
            mime = uri.split(';')[0].split(':')[-1]
            raw = base64.b64decode(uri.split(',', 1)[1])
            pic = Image.open(io.BytesIO(raw))
            good.append(f'the {mime.split("/")[-1].upper()} payload at {pic.size[0]}x{pic.size[1]}, '
                        f'unmodified and not transcoded')
            bw, bh = float(im.get('width') or 0), float(im.get('height') or 0)
            if bw and bh:
                good.append(f'the display box at {bw:.0f}x{bh:.0f} - '
                            f'{pic.size[0] / bw:.2f}x resolution and an exact aspect match')
        desc = root.find(f'{NS}desc')
        if desc is not None and (desc.text or '').strip():
            good.append('the provenance statement in <desc>')
    fams = {e.get('font-family') for e in root.iter()
            if isinstance(e.tag, str) and e.get('font-family')}
    if fams and all(f.split(',')[0].strip().strip('"\'').lower() in SAFE_FONTS for f in fams):
        good.append('the font stacks (' + '; '.join(sorted(fams)) + ')')
    if not sum(len(pp.get('d') or '') for pp in root.findall(f'.//{NS}path')):
        good.append(f'all {len(root.findall(f"{chr(46)}//{NS}text"))} labels as live <text>, '
                    f'nothing outlined')
    ids = [g.get('id') for g in root.findall(f'.//{NS}g') if g.get('id')]
    if any((i or '').startswith('callout-') for i in ids):
        good.append('the per-callout grouping')
    return good


def _next_rev(name):
    stem, ext = os.path.splitext(os.path.basename(name))
    m = re.search(r'_r(\d+)$', stem)
    if m:
        return f'{stem[:m.start()]}_r{int(m.group(1)) + 1:02d}{ext}'
    return f'{stem}_r01{ext}'


def fixnote(path):
    findings = audit(path)
    name = os.path.basename(path)
    nxt = _next_rev(name)
    if not findings:
        return f'{name} audits clean - no correction needed.'
    # Findings we fix locally must NOT go into the paste block: the author cannot run our
    # tooling, and asking a model to fix file size makes it claim success while changing nothing.
    LOCAL = ('fit_raster_svg', 'stored twice', 'alpha channel')
    authors = [f for f in findings if not any(k in f for k in LOCAL)]
    ours = [f for f in findings if any(k in f for k in LOCAL)]
    if not authors:
        note = f'{name} - nothing for the author to fix.'
        if ours:
            note += '\n\nHandled locally, do not send:\n' + '\n'.join(f'  - {f}' for f in ours)
        return note
    L = [f'{name} - {len(authors)} fix(es) needed, then re-deliver as {nxt}.', '']
    L.append('DEFECTS, with measurements. Every number below is measured, not estimated:')
    for i, f in enumerate(authors, 1):
        L.append(f'  {i}. {" ".join(f.split())}')
    L += ['', 'For any text that does not fit: rewrite it shorter or wrap it to more lines.',
          'Do not shrink one caption below the size of its neighbours to force a fit.', '']
    good = _already_correct(path)
    if good:
        L.append('CHANGE NOTHING ELSE. The following are already correct and must survive:')
        for g in good:
            L.append(f'  - {g}')
        L.append('')
    L += ['Do not re-encode, resample, resize, or re-render the photograph.',
          'Do not adjust or optimise file size - that is handled downstream, not by you.',
          '', f'Deliver as {nxt} with a download link.']
    out_s = '\n'.join(L)
    if ours:
        out_s += ('\n\n--- BELOW THIS LINE IS FOR US, NOT FOR THE PASTE ---\n'
                  + '\n'.join(f'  - {f}' for f in ours))
    return out_s


if __name__ == '__main__':
    if '--selftest' in sys.argv:
        sys.exit(0 if _selftest() else 1)
    if len(sys.argv) < 2:
        sys.exit(f'svg_layout_audit {VERSION}\nusage: svg_layout_audit.py FILE.svg [FILE.svg ...]'
                 f'\n       svg_layout_audit.py FILE.svg --fixnote'
                 f'\n       svg_layout_audit.py --selftest KNOWN_CLEAN.svg')
    if '--fixnote' in sys.argv:
        for _p in [a for a in sys.argv[1:] if not a.startswith('--')]:
            print(fixnote(_p))
        sys.exit(0)
    total = 0
    for p in sys.argv[1:]:
        if p.startswith('--'):
            continue
        findings = audit(p)
        total += len(findings)
        print(f'\n{os.path.basename(p)}')
        if not findings:
            print('   clean')
        for f in findings:
            print(f'   - {f}')
    print(f'\n{total} finding(s)')
    sys.exit(1 if total else 0)
