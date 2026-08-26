#!/usr/bin/env python3
VERSION = 'v1.21.2'
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
# v1.19 (S102): TWO BLIND SPOTS, both found by auditing a real file and then render-checking
#   the tool's own output instead of believing it.
#   (a) SMALL CONTAINERS. Only rects >= 150x60 counted as bounding boxes, so a label on a
#       126x38 section pill was measured against the panel behind it. 11-02's SIDE VIEW and
#       TOP VIEW were reported as overflowing by 9 and 4 units; render says ink 51.4..154.6
#       inside a pill spanning 40..166. It overflows nothing.
#   (b) PHANTOM BADGES. Any group holding a circle and a text was assumed to be a numbered
#       badge. A leader callout has an anchor DOT plus a label box - 11-02's callout-4 is
#       r=4.5 with FRONT CLIFF SENSORS 136 units away, and the tool reported that label as a
#       badge number off-centre by 136 with a wrong baseline. A badge number is now required
#       to be short, alphanumeric, and to actually land inside its circle.
#   Four of five findings on one file were false. A wrong finding costs 3x a blank one.
# v1.18.1 (S102): DETERMINISM. The font check iterated a SET, so finding order varied
#   between processes and the generated work list never reproduced byte-for-byte.
#   Sorted now. Found by regenerating in a fresh clone and diffing, not by reading.
# v1.18 (S102): ROTATION, found by double-checking v1.17's own output against renders.
#   _ctm carries translate() and scale() only, so a rotate() label was measured as though
#   it lay flat. 10-07's "Turn complete" is rotate(90) - 14 units wide on the page, reported
#   as 95 wide and 79 past its panel, which ranked the file 3rd on the graphics work list.
#   Six <text> across four files are affected (5-07, 6-11, 8-1, 10-07). They are now SKIPPED
#   and the skip is REPORTED, because a checker that silently stops checking is the thing
#   §24.6b exists to forbid. Full rotated-AABB support is the better fix and is not done.
#   Also: the overflow floor is now proportional. Agreement with rendered ink is ~1%, so a
#   fixed 2-unit floor could not tell 9-6's 11-unit measurement error on a 945-unit line
#   from a real 11-unit overflow on a short one.
# v1.17 (S102): THE TOOL WAS CSS-BLIND. _inh() read presentation ATTRIBUTES only, so
#   font-size in a style="" attribute or in a <style> class rule was invisible and every such
#   label fell back to the 16px default. 371 of 2,469 <text> elements across 17 files - 15% of
#   the book's labels - were being measured at a size that was not theirs, in BOTH directions:
#   a .title{font-size:36px} measured as 16 under-reports by 2.25x, and 6-04's
#   class="mono" style="font-size:12px" measured as 16px sans over-reported by 7% (and only
#   that little because two errors partly cancelled - 16/12 inflation against mono being wider
#   than sans).
#   THE METRIC ITSELF WAS NEVER WRONG. Verified against isolated renders: estimated vs rendered
#   ink came out 1.01, 1.01, 0.99. The S101 note that this estimator "inflates real overflows
#   2-5x" was a wrong finding and is retracted here. Of its three cited proofs, 10-02 was
#   correct (est 81, rendered 80.7), 6-05 was correct and if anything UNDER-reported (est 43,
#   rendered 45.8), and only 6-04 was a genuine false positive - caused by this CSS blindness,
#   not by font metrics. Re-derive any worklist ordered by the old numbers.
#   Now resolved with real cascade order - inline style="" beats a <style> class rule beats a
#   presentation attribute - then inherited up the ancestor chain. Only .class selectors are
#   supported because only .class selectors exist in the corpus (295 of them, zero of any other
#   shape); anything else is REPORTED as unsupported rather than silently mis-resolved, because
#   a resolver that quietly returns the wrong size is the bug this entry exists to fix.
#   Also now honoured, all previously invisible: font-family (mono and serif are measured with
#   mono and serif metrics, not Arial's), font-style italic, font-weight, and letter-spacing
#   in px or em.
#   The FONT-SAFETY check is CSS-aware too, and that is a second defect class it could never
#   see: stacks declared in <style> lead with "Inter" 98 times and "JetBrains Mono" 14 times.
#   Neither loads through <img src>, which is exactly what §17.3b forbids.
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
# Liberation Mono is metric-compatible with Courier New and Liberation Serif with Times, which
# is what the mono and serif stacks in the corpus actually fall back to once the designer's
# first choice (JetBrains Mono, Inter) fails to load through <img src>. Measuring a monospace
# label with Arial's metrics was one half of the v1.17 bug.
_FONT_CANDIDATES = {
    ('sans', False, False): ('/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf',
                             '/usr/share/fonts/liberation-sans/LiberationSans-Regular.ttf',
                             '/System/Library/Fonts/Supplemental/Arial.ttf',
                             '/Library/Fonts/Arial.ttf',
                             'C:/Windows/Fonts/arial.ttf'),
    ('sans', True, False):  ('/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf',
                             '/usr/share/fonts/liberation-sans/LiberationSans-Bold.ttf',
                             '/System/Library/Fonts/Supplemental/Arial Bold.ttf',
                             '/Library/Fonts/Arial Bold.ttf',
                             'C:/Windows/Fonts/arialbd.ttf'),
    ('sans', False, True):  ('/usr/share/fonts/truetype/liberation/LiberationSans-Italic.ttf',
                             '/System/Library/Fonts/Supplemental/Arial Italic.ttf',
                             'C:/Windows/Fonts/ariali.ttf'),
    ('sans', True, True):   ('/usr/share/fonts/truetype/liberation/LiberationSans-BoldItalic.ttf',
                             '/System/Library/Fonts/Supplemental/Arial Bold Italic.ttf',
                             'C:/Windows/Fonts/arialbi.ttf'),
    ('mono', False, False): ('/usr/share/fonts/truetype/liberation/LiberationMono-Regular.ttf',
                             '/System/Library/Fonts/Supplemental/Courier New.ttf',
                             'C:/Windows/Fonts/cour.ttf'),
    ('mono', True, False):  ('/usr/share/fonts/truetype/liberation/LiberationMono-Bold.ttf',
                             '/System/Library/Fonts/Supplemental/Courier New Bold.ttf',
                             'C:/Windows/Fonts/courbd.ttf'),
    ('mono', False, True):  ('/usr/share/fonts/truetype/liberation/LiberationMono-Italic.ttf',
                             'C:/Windows/Fonts/couri.ttf'),
    ('mono', True, True):   ('/usr/share/fonts/truetype/liberation/LiberationMono-BoldItalic.ttf',
                             'C:/Windows/Fonts/courbi.ttf'),
    ('serif', False, False): ('/usr/share/fonts/truetype/liberation/LiberationSerif-Regular.ttf',
                              '/System/Library/Fonts/Supplemental/Times New Roman.ttf',
                              'C:/Windows/Fonts/times.ttf'),
    ('serif', True, False):  ('/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf',
                              'C:/Windows/Fonts/timesbd.ttf'),
    ('serif', False, True):  ('/usr/share/fonts/truetype/liberation/LiberationSerif-Italic.ttf',
                              'C:/Windows/Fonts/timesi.ttf'),
    ('serif', True, True):   ('/usr/share/fonts/truetype/liberation/LiberationSerif-BoldItalic.ttf',
                              'C:/Windows/Fonts/timesbi.ttf'),
}
_FONTS = {}
for _k, _paths in _FONT_CANDIDATES.items():
    for _p in _paths:
        if os.path.exists(_p):
            _FONTS[_k] = _p
            break


def _face(family='sans', bold=False, italic=False):
    """Best available face, degrading along axes rather than giving up.

    A missing italic must not silently become 'no text check at all' - degrading to the roman
    of the SAME FAMILY keeps the width within a percent, whereas falling back to sans for a
    monospace label is the v1.17 bug all over again. Family is therefore the last axis dropped.
    """
    for key in ((family, bold, italic), (family, bold, False),
                (family, False, italic), (family, False, False),
                ('sans', bold, italic), ('sans', bold, False), ('sans', False, False)):
        if key in _FONTS:
            return _FONTS[key]
    return None

# a drawn graphic's labels must survive on a machine that has none of the designer's fonts
SAFE_FONTS = ('arial', 'helvetica', 'sans-serif', 'courier new', 'monospace', 'times', 'serif')
MIN_PHOTO_SCALE = 2.0        # §17.3b: payload at ~2x its on-screen box
GATE37_CEILING = 500_000     # book_gates §21.1 - fatal for a file a lesson REFERENCES
DISPLAY_WIDTH_PX = 1100      # the book's image column. The <image> box is in USER UNITS,
                             # so it must be scaled through the viewBox to get real pixels.
PANEL_MIN_W, PANEL_MIN_H = 150, 60
PANEL_PAD = 6
# Smaller than the instrument's own error is not a finding. Once v1.17 resolved CSS, predicted
# extents were checked against browser-equivalent renders on five files (10-02, 6-05, 6-04,
# 9-1, 14-03) and agreed to 0.3, 0.1, 1.7, 1.3 and 0.9 units. Anything under 2.0 is inside that
# band, and a 1-unit "overflow" sends a human to look at nothing - which costs 3x a blank.
MIN_OVERFLOW = 2.0
# ...and a PROPORTIONAL floor beside it. Absolute agreement with rendered ink is ~1%, so
# the error grows with the string: on 9-6's 945-unit line the estimate sat 11 units high,
# which is 1.2% and not a defect. A fixed floor cannot tell those apart from a real 11-unit
# overflow on a short label, so the floor scales.
OVERFLOW_REL = 0.015


_TR = None


def _ctm(el):
    """Accumulated (dx, dy, sx, sy) from this element and its ancestors.

    Only translate() and scale() are handled - that is what Illustrator emits.

    S110 CORRECTION: this docstring used to claim a rotate() or matrix() 'is reported rather
    than silently mis-measured'. It is not reported HERE - _ctm matches both in its regex and
    then drops them with no branch and no word. The reporting lives in _rotated(), and v1.18
    wired _rotated() into the TEXT check only. Say what the function does, not what the
    module does somewhere else.
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
        # S110: this used to match matrix|rotate and then drop them with no branch, which
        # is what regex_audit flags - a pattern that captures more than the code handles.
        # Rotation is handled by _rotated()/_quarter_turns() at the call sites; matching it
        # here only made the reader think this function knew about it.
        for fn, args in _re.findall(r'(translate|scale)\s*\(([^)]*)\)', tr):
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


_CSS_CACHE = {}


def _css_index(root):
    """Parse every <style> block into ordered (class, declarations) pairs.

    Returns (rules, unsupported). Only .class selectors are handled, because a survey of the
    corpus found 295 .class selectors and zero of any other shape. Anything else is collected
    and REPORTED - never silently ignored - since a resolver that quietly returns the wrong
    size is precisely the defect v1.17 exists to fix.
    """
    tree = root.getroottree()
    if id(tree) in _CSS_CACHE:
        return _CSS_CACHE[id(tree)][1:]
    rules, unsupported = [], []
    css = '\n'.join((s.text or '') for s in root.iter(f'{NS}style'))
    css = re.sub(r'/\*.*?\*/', '', css, flags=re.S)
    for m in re.finditer(r'([^{}]+)\{([^{}]*)\}', css):
        decls = {}
        for d in m.group(2).split(';'):
            if ':' in d:
                k, v = d.split(':', 1)
                decls[k.strip().lower()] = v.strip()
        for sel in m.group(1).split(','):
            sel = sel.strip()
            if not sel:
                continue
            if re.fullmatch(r'\.[A-Za-z_][\w-]*', sel):
                rules.append((sel[1:], decls))
            else:
                unsupported.append(sel)
    # hold the tree so its id() cannot be recycled under us while the cache is live
    _CSS_CACHE[id(tree)] = (tree, rules, unsupported)
    return rules, unsupported


def _own(el, name):
    """This element's own value for a property, in CSS cascade order.

    inline style="" beats a <style> class rule beats a presentation attribute. Among several
    class rules the LAST DECLARED wins, which is document order and not class-attribute order.
    """
    st = el.get('style')
    if st:
        for d in st.split(';'):
            if ':' in d:
                k, v = d.split(':', 1)
                if k.strip().lower() == name:
                    return v.strip()
    cls = el.get('class')
    if cls:
        want = set(cls.split())
        hit = None
        for cname, decls in _css_index(el.getroottree().getroot())[0]:
            if cname in want and name in decls:
                hit = decls[name]
        if hit is not None:
            return hit
    return el.get(name)


def _inh(el, attr):
    """Resolve a property here, else inherit it from the nearest ancestor that sets one.

    An element's OWN presentation attribute beats a value inherited from an ancestor, which is
    why the cascade is applied per-element on the way up rather than gathered first.
    """
    n = el
    while n is not None:
        v = _own(n, attr) if isinstance(n.tag, str) else None
        if v:
            return v
        n = n.getparent()
    return None


def _px(v, size=16.0):
    """A CSS length in px or em. Returns None for anything else rather than guessing."""
    if not v:
        return None
    v = v.strip().lower()
    try:
        if v.endswith('px'):
            return float(v[:-2])
        if v.endswith('em'):
            return float(v[:-2]) * size
        return float(v)
    except ValueError:
        return None


def _family_kind(stack):
    """Which metric family a stack lands in once the designer's first choice fails to load.

    Inter and JetBrains Mono do not travel through <img src>, so what a reader actually gets is
    the first GENERIC or system name in the stack. Judge by the whole stack, not its head.
    """
    if not stack:
        return 'sans'
    for name in stack.split(','):
        n = name.strip().strip('"\'').lower()
        if n in ('courier new', 'monospace', 'consolas', 'courier'):
            return 'mono'
        if n in ('times', 'times new roman', 'serif', 'georgia'):
            return 'serif'
        if n in ('arial', 'helvetica', 'sans-serif', 'verdana', 'tahoma'):
            return 'sans'
    return 'sans'


def _quarter_turns(el):
    """Total rotation as a count of quarter turns, or None if it is not axis-aligned.

    A 90 or 270 turn swaps an element's on-page width and height; a 180 leaves them. That is
    exactly enough to measure a rotated <image> correctly instead of skipping it, and it is
    NOT the general rotated-AABB problem, which stays undone. Returns None for any angle off
    the axes, for matrix() and for skew() - those are still refused rather than guessed at.
    """
    import re as _re
    total = 0.0
    n = el
    while n is not None and isinstance(n.tag, str):
        tf = n.get('transform') or ''
        if 'matrix' in tf or 'skew' in tf:
            return None
        for a in _re.findall(r'rotate\s*\(([^)]*)\)', tf):
            v = [q for q in _re.split(r'[,\s]+', a.strip()) if q]
            try:
                total += float(v[0])
            except (ValueError, IndexError):
                return None
        n = n.getparent()
    if abs(total % 90.0) > 1e-6:
        return None
    return int(round(total / 90.0)) % 4


def _rotated(el):
    """True if this element or an ancestor carries a transform _ctm cannot represent.

    _ctm accumulates translate() and scale() only. A rotate() or matrix() turns a label off the
    horizontal, and every check below measures horizontal extent - so measuring one of these as
    though it were flat does not produce a slightly-wrong number, it produces a fictional one.
    10-07's "Turn complete" is rotate(90): 14 units wide on the page, reported as 95 wide and
    79 units past its panel, which put the file 3rd on a work list. A wrong finding costs 3x a
    blank one, so these are SKIPPED and SAID OUT LOUD rather than guessed at.
    """
    n = el
    while n is not None:
        if isinstance(n.tag, str):
            tf = n.get('transform') or ''
            if 'rotate' in tf or 'matrix' in tf or 'skew' in tf:
                return True
        n = n.getparent()
    return False


def _text_width(s, size, bold=False, italic=False, family='sans', letter_spacing=0.0):
    path = _face(family, bold, italic)
    if path is None:
        raise RuntimeError('no Arial-metric font found (Liberation Sans or Arial) - text checks '
                           'cannot run. Linux: apt install fonts-liberation')
    w = ImageFont.truetype(path, 200).getlength(s) * size / 200.0
    # letter-spacing adds a gap BETWEEN glyphs; the trailing one does not widen the ink
    if letter_spacing and len(s) > 1:
        w += letter_spacing * (len(s) - 1)
    return w


def _lines(t):
    """Yield (text, x0, x1, y, size) once per RENDERED LINE.

    A <text> may hold <tspan> children, and any tspan with its own x or dy is a separate line.
    Concatenating itertext() and measuring that as one string reports a correctly wrapped label
    as a giant overflow - v1.4 did exactly that and cost a round trip to fix a non-defect.
    """
    size = _px(_inh(t, 'font-size'))
    if size is None:
        size = 16.0
    bold = (_inh(t, 'font-weight') or '400') in ('600', '700', '800', '900', 'bold', 'bolder')
    italic = (_inh(t, 'font-style') or 'normal').strip().lower().startswith('italic')
    family = _family_kind(_inh(t, 'font-family'))
    lsp = _px(_inh(t, 'letter-spacing'), size) or 0.0
    anchor = _inh(t, 'text-anchor') or 'start'
    tdx, tdy, tsx, tsy = _ctm(t)
    size *= tsy                                   # a scaled group scales the type with it
    bx = (_f(t.get('x')) or 0.0) * tsx + tdx
    by = (_f(t.get('y')) or 0.0) * tsy + tdy

    spans = [sp for sp in t.findall(f'{NS}tspan')
             if sp.get('x') is not None or sp.get('dy') is not None or sp.get('y') is not None]
    rows = []
    if spans:
        cy = by
        lead = ' '.join((t.text or '').split())
        if lead:
            rows.append((lead, bx, cy, None))   # the lead run is not what a text-level
                                                # textLength governs; measure it
        for sp in spans:
            # ABSOLUTE y wins over relative dy - a wrapped label written as
            # <tspan x=".." y="468"> is the normal hand-authored form, and v1.16 read only dy,
            # so every such line collapsed onto the first baseline and the collision check
            # then reported the label as overlapping ITSELF. Blind to one of two legal forms
            # is the same defect as v1.17's CSS blindness, found the same way: on a real file.
            if sp.get('y') is not None:
                cy = (_f(sp.get('y')) or 0.0) * tsy + tdy
            else:
                cy += (_f(sp.get('dy')) or 0.0) * tsy
            rows.append((' '.join((sp.text or '').split()),
                         (_f(sp.get('x')) * tsx + tdx) if sp.get('x') is not None else bx, cy,
                         _f(sp.get('textLength'))))
    else:
        # ONE rendered row, so a text-level textLength governs exactly this row
        rows.append((' '.join(''.join(t.itertext()).split()), bx, by, _f(t.get('textLength'))))

    out = []
    for txt, x, y, tlen in rows:
        if not txt:
            continue
        if tlen is not None:
            # v1.21: textLength is a DECLARED advance. The renderer stretches or squeezes the
            # run to hit it exactly, so the font estimate is not what lands on the page.
            # Reading the estimate instead reported three overlaps in
            # L03_GRAPHIC_3-11_command_anatomy.svg whose spans abut at 0.0px (S188). Both
            # lengthAdjust values ('spacing', the default, and 'spacingAndGlyphs') produce the
            # same total advance, so the attribute alone settles the width.
            w = tlen * tsx
        else:
            w = _text_width(txt, size, bold, italic, family, lsp * tsx)
        x0 = x - w / 2 if anchor == 'middle' else (x - w if anchor == 'end' else x)
        out.append((txt, x0, x0 + w, y, size, tlen is not None))
    return out


def _extent(t):
    ls = _lines(t)
    if not ls:
        return '', 0.0, 0.0, float(t.get('y') or 0), float(_inh(t, 'font-size') or 16), False
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
        # S110: the resolution check below divides the box width by the viewBox width, so a
        # quarter-turned <image> was measured on the wrong edge. v1.18 guarded <text> against
        # this and left <image> unguarded; 3 images in the corpus sit under a rotation, and on
        # the two at 90 degrees the box read 16% too wide, which UNDERSTATES the resolution
        # ratio by 14% and biases the check toward a false 'under the floor'. Silent today,
        # which is why it needed measuring rather than waiting for a complaint.
        if _rotated(im_el):
            qt = _quarter_turns(im_el)
            if qt is None:
                out.append('<image> sits under a rotate()/matrix() this tool cannot represent, '
                           'so its resolution and aspect were NOT checked (§24.6b: a checker '
                           'that silently stops checking is worse than one that says so)')
                continue
        # The swap belongs to the RESOLUTION check only. That one divides the on-page box
        # width by the viewBox width, so a quarter turn matters. The ASPECT check below
        # compares the element's own box against the photo's own aspect - both rotate
        # together, so swapping there INVERTS a correct comparison. Measured: swapping for
        # both produced two new false 'letterboxed or distorted' findings on 10-02 and 10-03.
        pw, ph = bw, bh
        if _rotated(im_el) and _quarter_turns(im_el) % 2:
            pw, ph = bh, bw
        vb = (root.get('viewBox') or '').split()
        vbw = float(vb[2]) if len(vb) == 4 else bw
        if bw and bh and vbw:
            css_box = pw / vbw * DISPLAY_WIDTH_PX      # on-page width, quarter turns applied
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
    rules, unsupported = _css_index(root)
    if unsupported:
        out.append(f'{len(unsupported)} CSS selector(s) this tool does not resolve '
                   f'({", ".join(sorted(set(unsupported))[:4])}) - every text measurement in '
                   f'this file may be against the wrong size. Reported, not guessed at.')
    stacks = {e.get('font-family') for e in root.iter()
              if isinstance(e.tag, str) and e.get('font-family')}
    stacks |= {d['font-family'] for _c, d in rules if 'font-family' in d}
    for e in root.iter():                       # inline style="" declarations
        if isinstance(e.tag, str) and e.get('style') and 'font-family' in e.get('style'):
            m = re.search(r'font-family:\s*([^;]+)', e.get('style'))
            if m:
                stacks.add(m.group(1))
    # SORTED, not set order. Python randomises string hashing per process, so iterating the
    # set emitted this file's findings in a different order on every run - and
    # GPT_WORKLIST regenerated with a different byte count each time. A generate that does
    # not reproduce cannot be diffed, and 'has anything changed since last session?' stops
    # being answerable. No file ever moved rank; the defect was invisible until the output
    # was regenerated twice and compared.
    for fam in sorted({s for s in stacks if s}):
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
    # ...but a PANEL is not the only thing that can bound a label. A section tab, a coloured
    # pill, a legend chip - all are filled boxes far under PANEL_MIN_W, and a label sitting on
    # one is bounded by IT, not by the panel it happens to sit on top of. 11-02 puts "SIDE VIEW"
    # on a 126x38 blue pill at the panel's corner; the pill is 24 units under the panel
    # threshold, so the label was measured against the panel behind it and reported as
    # overflowing by 9 units. It overflows nothing. Render-verified: ink 51.4..154.6 inside a
    # pill spanning 40..166.
    holders = []
    for rc in root.findall(f'.//{NS}rect'):
        if not rc.get('fill') or rc.get('fill') == 'none':
            continue
        w, h = float(rc.get('width') or 0), float(rc.get('height') or 0)
        if w <= 0 or h <= 0 or (w >= PANEL_MIN_W and h >= PANEL_MIN_H):
            continue                       # panels are handled above; this is the small stuff
        x, y = float(rc.get('x') or 0), float(rc.get('y') or 0)
        holders.append((x, y, x + w, y + h))

    def _held(x0, x1, ycent, size):
        """Is this line fully inside a small filled box? Then that box is its container."""
        top, bot = ycent - 0.80 * size, ycent + 0.25 * size
        return any(hx0 <= x0 and x1 <= hx1 and hy0 <= top and bot <= hy1
                   for hx0, hy0, hx1, hy1 in holders)
    # A number sitting inside a badge is bounded by that badge, not by any panel it overhangs.
    badges_xy = [(float(c.get('cx') or 0), float(c.get('cy') or 0), float(c.get('r') or 0))
                 for c in root.findall(f'.//{NS}circle') if c.get('r')]
    skipped_rot = 0
    for t in root.findall(f'.//{NS}text'):
        if _rotated(t):
            skipped_rot += 1
            continue
        tx, ty = float(t.get('x') or 0), float(t.get('y') or 0)
        if any((tx - cx) ** 2 + (ty - cy) ** 2 <= (rr * 1.2) ** 2 for cx, cy, rr in badges_xy):
            continue
        for s, x0, x1, y, size, _declared in _lines(t):
            ax = float(t.get('x') or 0)
            for px0, py0, px1, py1 in panels:
                if px0 <= ax <= px1 and py0 <= y <= py1:
                    if x0 < px0 + PANEL_PAD or x1 > px1 - PANEL_PAD:
                        if _held(x0, x1, y, size):
                            break          # bounded by its own pill/tab, not by this panel
                        over = max(px0 + PANEL_PAD - x0, x1 - (px1 - PANEL_PAD))
                        # the floor scales with the string: measured relative error against
                        # rendered ink runs to ~1.3%, so on a 900-unit line a 10-unit "overflow"
                        # is inside the instrument, not a defect in the file
                        #
                        # v1.21.2: that relative term is an ERROR model, and a row whose width
                        # is DECLARED by textLength has no measurement error - the renderer
                        # hits the declared advance exactly. Applying an error allowance to a
                        # number that carries no error is simply wrong, so declared rows get
                        # the absolute floor only. MIN_OVERFLOW stays for them as a VISIBILITY
                        # floor, not an error one: a sub-2-unit sliver is arithmetically real
                        # and visually nothing, and an instrument that reports it teaches
                        # people to skim past it.
                        # MEASURED AT S188: this changes ZERO findings on the current corpus -
                        # no declared row anywhere in images/ falls between the two floors.
                        # It is a correctness fix with no present effect. Do not credit it
                        # with the L07 file-tree findings, which clear either floor.
                        floor = (MIN_OVERFLOW if _declared
                                 else max(MIN_OVERFLOW, OVERFLOW_REL * (x1 - x0)))
                        if over < floor:
                            break
                        out.append(f'text overflows its panel by {over:.0f} units: '
                                   f'"{s[:44]}" spans {x0:.0f}..{x1:.0f} '
                                   f'inside {px0:.0f}..{px1:.0f}')
                    break
    if skipped_rot:
        out.append(f'{skipped_rot} rotated/skewed <text> NOT checked for overflow or collision - '
                   f'this tool measures horizontal extent only. Eyeball them.')

    # ---- 6. text colliding with text on the same line ---------------------------------------
    ran.add('collide_text')
    rows = {}
    for t in root.findall(f'.//{NS}text'):
        for s, x0, x1, y, size, _d in _lines(t):
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
        # A group with a circle and a text is NOT automatically a numbered badge. A leader
        # callout has an anchor DOT on the photograph plus a label box, and 11-02's callout-4
        # is exactly that: r=4.5 with the words FRONT CLIFF SENSORS 136 units away. v1.18 called
        # that label a badge number and reported it off-centre by 136 and mis-baselined - two
        # confident numbers about a badge that does not exist. A badge number is SHORT and it
        # sits INSIDE its circle; anything else is a dot with a caption.
        _label = ''.join(t.itertext()).strip()
        if len(_label) > 3 or not _label[:1].isalnum():
            continue
        # Every one of these is optional in valid SVG. v1.11 assumed all four were present and
        # a single missing x killed the entire audit.
        ls = _lines(t)
        if not ls:
            continue
        _s0, _x0, _x1, ty, _sz, _d = ls[0]
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
        _r = _f(c.get('r')) or 0.0
        if dx > _r or abs(dy) > 2 * _r:
            continue                              # the text is not in the circle: a dot, not a badge
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
    skipped = []
    print(f'CONTROL A (false-positive): clean reference must be SILENT  [{os.path.basename(src)}]')
    base = audit(src)
    print(f'   {"clean" if not base else "NOT CLEAN: " + str(base)}')
    ok &= not base

    def seeded(name, mutate, needle):
        # v1.21.2: a seed can only run where the reference HAS the structure it mutates. That
        # is not a pass and it is not a failure - it is a control that did not run, and the
        # verdict must say so out loud. Aborting the whole selftest instead (v1.21.1) meant
        # one absent badge stopped the other eight seeds from running at all.
        tree = etree.parse(src)
        try:
            mutate(tree.getroot())
        except AttributeError:
            # A photo seed on a photo-free reference: the structure is absent, same as a
            # RuntimeError refusal. Report it as NOT RUN rather than killing the sweep.
            skipped.append((name, 'this reference has no <image> to seed'))
            print(f'   SKIP {name}  (structure absent in this reference)')
            return True
        except RuntimeError as exc:
            skipped.append((name, str(exc).split(' - ')[0]))
            print(f'   SKIP {name}  (structure absent in this reference)')
            return True
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
        # v1.21.1: this control used to hardcode callout-6. Only two clean files in images/
        # carry that id, so every other reference file crashed the whole selftest with a
        # TypeError on None before CONTROL B had run a single seed. Find ANY callout group
        # that actually holds a centred label - that is the structure this control mutates -
        # and refuse loudly if the reference has none, because a control that quietly finds
        # nothing to seed is a control that passes for the wrong reason.
        # Seed EXACTLY what the arm measures. Picking any centred text is not enough: on
        # 11-02 the first centred text in callout-1 is the LABEL "SENSOR / READS DARK", and
        # unanchoring a label produces panel-overflow findings, not an off-centre badge - the
        # control would then fail while reporting nothing about the thing it names. The badge
        # arm's own test is a SHORT alphanumeric label sitting inside a sibling circle, so use
        # that test here and nothing looser.
        for g in r.findall(f'.//{NS}g'):
            if not (g.get('id') or '').startswith('callout-'):
                continue
            circs = [e for e in g if e.tag == NS + 'circle'
                     and _f(e.get('cx')) is not None and _f(e.get('cy')) is not None]
            if not circs:
                continue
            for e in g:
                if e.tag != NS + 'text' or (e.get('text-anchor') or '') != 'middle':
                    continue
                lab = ''.join(e.itertext()).strip()
                if not lab or len(lab) > 3 or not lab[:1].isalnum():
                    continue
                ls = _lines(e)
                if not ls:
                    continue
                _s0, _x0, _x1, ty, _sz, _d = ls[0]
                tx = (_x0 + _x1) / 2
                c = min(circs, key=lambda q: (_f(q.get('cx')) + _ctm(q)[0] - tx) ** 2
                                             + (_f(q.get('cy')) + _ctm(q)[1] - ty) ** 2)
                ccx, ccy, _a, _b = _ctm(c)
                rr = _f(c.get('r')) or 0.0
                if abs(tx - (_f(c.get('cx')) + ccx)) > rr:
                    continue                      # a dot with a caption, not a badge
                e.set('text-anchor', 'start')
                return
        raise RuntimeError(
            'selftest reference has no callout-* group holding a NUMBERED BADGE (a short '
            'label centred inside its own circle), so the badge-anchor control has nothing to '
            'seed. Pick a reference file that has one - it cannot be skipped silently.')
    # The signal changed in v1.15: removing the anchor from a file that relies on it shifts the
    # glyph, and the tool now reports the SHIFT rather than the missing attribute. Same defect,
    # measured by its effect. Control the effect, not the implementation.
    ok &= seeded('badge anchor removed', kill_anchor, 'off-centre horizontally')

    def widen(r):
        # v1.21.2: this used to grep the literal string 'Lights whenever', which exists in one
        # reference file. Seed by STRUCTURE instead: find a label the overflow arm can actually
        # bound - one that sits inside a PANEL-sized rect and is not itself held by a small
        # pill or badge - and lengthen it until it must run past that panel's edge.
        panels = []
        for rc in r.findall(f'.//{NS}rect'):
            w, h = _f(rc.get('width')) or 0.0, _f(rc.get('height')) or 0.0
            if w >= PANEL_MIN_W and h >= PANEL_MIN_H:
                x, y = _f(rc.get('x')) or 0.0, _f(rc.get('y')) or 0.0
                panels.append((x, y, x + w, y + h))
        # A candidate must be ALONE on its baseline. Lengthening a label that has a neighbour
        # on the same row makes it collide before it overflows, and the run then reports
        # 'overlaps text' - a real finding, but not the one this control is proving.
        occupied = {}
        for t in r.findall(f'.//{NS}text'):
            for _s, _x0, _x1, _y, _sz, _d in _lines(t):
                occupied[round(_y, 1)] = occupied.get(round(_y, 1), 0) + 1
        for t in r.findall(f'.//{NS}text'):
            if _rotated(t) or t.get('textLength') is not None or t.findall(f'{NS}tspan'):
                continue                       # keep the seed on the simple, unambiguous form
            body = ''.join(t.itertext()).strip()
            if not body:
                continue
            ls = _lines(t)
            if not ls:
                continue
            _s0, x0, x1, y, _sz, _d = ls[0]
            ax = _f(t.get('x'))
            if ax is None:
                continue
            for px0, py0, px1, py1 in panels:
                if px0 <= ax <= px1 and py0 <= y <= py1 and x1 <= px1 - PANEL_PAD \
                        and occupied.get(round(y, 1), 0) == 1:
                    t.text = body + ' ' + 'W' * 90   # 90 wide glyphs clears any panel
                    for sp in list(t):
                        t.remove(sp)
                    return
        raise RuntimeError(
            'selftest reference has no plain label sitting inside a panel with room to grow, '
            'so the panel-overflow control has nothing to seed. Pick a reference file that '
            'has one - it cannot be skipped silently.')
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
        # v1.21.2: a file with no <text> has no font stack to spoil. Setting font-family on an
        # empty list mutates nothing, the seed produces no finding, and the control reported
        # FAIL for a file that simply has no text - a decorative mark, not a defect.
        texts = r.findall(f'.//{NS}text')
        if not texts:
            raise RuntimeError('this reference carries no <text>, so it has no font stack')
        for t in texts:
            t.set('font-family', 'Inter, Arial, sans-serif')
    ok &= seeded('designer font first in the stack', badfont, 'cannot load through')

    def nocredit(r):
        # v1.21.2: the credit arm only applies to a file that HAS a photograph. On a drawn
        # graphic there is no credit to remove, so stripping text proves nothing and the
        # control failed on 62 of 82 clean references for lack of an <image>, not a defect.
        if r.find(f'.//{NS}image') is None:
            raise RuntimeError('this reference has no <image>, so it owes no photo credit')
        d = r.find(f'{NS}desc')
        if d is not None:
            d.text = ''
        for t in list(r.findall(f'.//{NS}text')):
            if 'Pololu' in ''.join(t.itertext()) or 'photograph' in ''.join(t.itertext()):
                t.getparent().remove(t)
    ok &= seeded('photo credit removed', nocredit, 'credit')

    def collide(r):
        # v1.21.2: this named callout-7 and wrote the fixed coordinates x=150, y=262, which
        # only collide with something in one particular file. Seed by STRUCTURE: the arm
        # compares the rects of two DIFFERENT callout groups, so take the first two such rects
        # and move the second onto the first. That overlaps by construction, in any file.
        found = []
        for g in r.findall(f'.//{NS}g'):
            if not (g.get('id') or '').startswith('callout-'):
                continue
            for e in g:
                if e.tag == NS + 'rect' and _f(e.get('x')) is not None \
                        and _f(e.get('y')) is not None:
                    found.append((g.get('id'), e))
                    break
            if len({gid for gid, _ in found}) == 2:
                (_gid1, r1), (_gid2, r2) = found[0], found[-1]
                r2.set('x', r1.get('x')); r2.set('y', r1.get('y'))
                return
        raise RuntimeError(
            'selftest reference has fewer than two callout-* groups holding a positioned '
            '<rect>, so the box-collision control has nothing to seed. Pick a reference file '
            'that has two - it cannot be skipped silently.')
    ok &= seeded('two highlight boxes overlapped', collide, 'overlaps')

    # ---- v1.19 controls: the two blind spots, tested in BOTH directions ---------------------
    import tempfile

    def synth(name, body):
        d = tempfile.mkdtemp()
        fp = os.path.join(d, name)
        with open(fp, 'w', encoding='utf-8') as fh:
            fh.write('<svg xmlns="http://www.w3.org/2000/svg" '
                     'xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 900 500" '
                     'font-family="Arial, Helvetica, sans-serif">'
                     '<rect x="40" y="40" width="700" height="400" fill="#FFFFFF"/>'
                     + body + '</svg>')
        return fp

    # (a) a label on a SMALL pill must be SILENT - the v1.19 fix
    pill = synth('pill.svg',
                 '<rect x="40" y="40" width="126" height="38" fill="#0E5AA7"/>'
                 '<text x="103" y="66" font-size="20" fill="#FFFFFF" '
                 'text-anchor="middle">SIDE VIEW</text>')
    if any('overflows' in f for f in audit(pill)):
        print('   FAIL  CONTROL: a label inside its own pill was called an overflow'); ok = False
    else:
        print('   OK    CONTROL: a label bounded by a small pill is not an overflow')

    # (a-inverse) a label that ESCAPES its pill must still be LOUD
    esc = synth('esc.svg',
                '<rect x="40" y="40" width="126" height="38" fill="#0E5AA7"/>'
                '<text x="700" y="66" font-size="20" fill="#111111">'
                'this label is far outside every box it could belong to</text>')
    if not any('overflows' in f for f in audit(esc)):
        print('   FAIL  CONTROL: a genuine overflow went silent - the pill rule is too broad')
        ok = False
    else:
        print('   OK    CONTROL: a label outside every box is still reported')

    # ---- v1.21 controls: textLength, tested in BOTH directions -----------------------------
    # (e) a DECLARED textLength that squeezes the run must be SILENT - the v1.21 fix.
    # 'WIDEWIDEWIDE' estimates ~150 units at font-size 20; declaring 60 makes it end at 160,
    # so the neighbour at x=170 does NOT collide. v1.20 measured the estimate and fired.
    tl_ok = synth('textlength_ok.svg',
                  '<text x="100" y="200" font-size="20" textLength="60">WIDEWIDEWIDE</text>'
                  '<text x="170" y="200" font-size="20" textLength="60">SECONDSECOND</text>')
    if any('overlaps text' in f for f in audit(tl_ok)):
        print('   FAIL  CONTROL: a declared textLength was ignored and read as a collision')
        ok = False
    else:
        print('   OK    CONTROL: a run squeezed by textLength is measured at its DECLARED width')

    # (e-inverse) a real overlap must still be LOUD, whether textLength is declared or not.
    # Declared 120 wide from x=100 ends at 220; the neighbour starts at 150. That IS a collision
    # and honouring the attribute must not silence it.
    tl_bad = synth('textlength_bad.svg',
                   '<text x="100" y="200" font-size="20" textLength="120">WIDEWIDEWIDE</text>'
                   '<text x="150" y="200" font-size="20" textLength="120">SECONDSECOND</text>')
    if not any('overlaps text' in f for f in audit(tl_bad)):
        print('   FAIL  CONTROL: a genuine overlap went silent - textLength is being trusted '
              'to mean "no collision" rather than to mean "this wide"')
        ok = False
    else:
        print('   OK    CONTROL: a genuine overlap still fires when textLength is declared')

    # (e-control) the same two runs with NO textLength must behave as v1.20 did - the new path
    # is additive, and a file that declares nothing is measured exactly as before.
    tl_none = synth('textlength_none.svg',
                    '<text x="100" y="200" font-size="20">WIDEWIDEWIDE</text>'
                    '<text x="170" y="200" font-size="20">SECONDSECOND</text>')
    if not any('overlaps text' in f for f in audit(tl_none)):
        print('   FAIL  CONTROL: the undeclared path changed - v1.21 is not additive'); ok = False
    else:
        print('   OK    CONTROL: with no textLength the font estimate still governs')

    # ---- v1.21.2 controls: the DECLARED-width floor, tested in BOTH directions -------------
    # A declared row that pokes 3 units past its panel must be LOUD. Under the old rule the
    # floor would have been 0.015 * 300 = 4.5 and this would have gone silent.
    fl_loud = synth('floor_declared_loud.svg',
                    '<rect x="40" y="40" width="400" height="300" fill="#FFFFFF" '
                    'stroke="#333333"/>'
                    '<text x="60" y="200" font-size="20" textLength="389">DECLARED WIDE RUN'
                    '</text>')
    if not any('overflows' in f for f in audit(fl_loud)):
        print('   FAIL  CONTROL: a declared row 3 units past its panel went silent - the '
              'relative floor is still being applied to a number that has no error')
        ok = False
    else:
        print('   OK    CONTROL: a declared row past its panel is reported, however long it is')

    # (inverse) a declared row inside its panel must stay SILENT - the absolute floor still
    # holds, so the fix did not turn every declared row into a finding.
    fl_quiet = synth('floor_declared_quiet.svg',
                     '<rect x="40" y="40" width="400" height="300" fill="#FFFFFF" '
                     'stroke="#333333"/>'
                     '<text x="60" y="200" font-size="20" textLength="300">DECLARED SAFE RUN'
                     '</text>')
    if any('overflows' in f for f in audit(fl_quiet)):
        print('   FAIL  CONTROL: a declared row well inside its panel was called an overflow')
        ok = False
    else:
        print('   OK    CONTROL: a declared row inside its panel stays silent')

    # (b) an anchor DOT plus a long label must be SILENT - not a badge
    dot = synth('dot.svg',
                '<g id="callout-4"><circle cx="300" cy="200" r="4.5" fill="#0E5AA7"/>'
                '<text x="500" y="200" font-size="14" text-anchor="middle">FRONT SENSORS</text>'
                '</g>')
    if any('badge number' in f for f in audit(dot)):
        print('   FAIL  CONTROL: an anchor dot was read as a numbered badge'); ok = False
    else:
        print('   OK    CONTROL: an anchor dot with a caption is not a badge')

    # (b-inverse) a REAL badge, genuinely off-centre, must still be LOUD
    badge = synth('badge.svg',
                  '<g id="callout-1"><circle cx="300" cy="200" r="14" fill="#0E5AA7"/>'
                  '<text x="309" y="205" font-size="14" fill="#FFFFFF" '
                  'text-anchor="middle">3</text></g>')
    if not any('badge number' in f for f in audit(badge)):
        print('   FAIL  CONTROL: a real off-centre badge number went silent'); ok = False
    else:
        print('   OK    CONTROL: a real off-centre badge number is still reported')

    # ---- S110: quarter-turned <image> ------------------------------------------------
    # v1.18 guarded <text> against rotation and left <image> unguarded. The whole-corpus
    # findings are IDENTICAL before and after this fix, which is also exactly what a DEAD
    # change produces (§24.8) - so the path is exercised here directly.
    from lxml import etree as _et

    def _img(tf):
        x = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 800">'
             '<g transform="%s"><image width="100" height="50" x="0" y="0"/></g></svg>' % tf)
        return _et.fromstring(x.encode()).find('.//{http://www.w3.org/2000/svg}image')

    cases = [('rotate(90)', 1), ('rotate(180)', 2), ('rotate(270)', 3),
             ('translate(10,10) rotate(90)', 1), ('rotate(45)', None),
             ('matrix(1,0,0,1,5,5)', None), ('skewX(10)', None)]
    bad = [(tf, _quarter_turns(_img(tf)), want) for tf, want in cases
           if _quarter_turns(_img(tf)) != want]
    if bad:
        print('   FAIL  CONTROL: _quarter_turns misread %s' % (bad,)); ok = False
    else:
        print('   OK    CONTROL: quarter turns read, 45 deg / matrix / skew refused as None')

    # the swap must apply to the RESOLUTION edge and NOT to the aspect comparison -
    # swapping both inverted a correct check and produced two false findings in the corpus
    e90 = _img('rotate(90)')
    w = _f(e90.get('width')); h = _f(e90.get('height'))
    pw = h if _quarter_turns(e90) % 2 else w
    if (pw, w / h) != (50.0, 2.0):
        print('   FAIL  CONTROL: on-page width %s or box aspect %s wrong' % (pw, w / h)); ok = False
    else:
        print('   OK    CONTROL: a quarter turn moves the measured EDGE, not the box aspect')

    e0 = _img('translate(5,5)')
    if _quarter_turns(e0) != 0 or _rotated(e0):
        print('   FAIL  CONTROL: an unrotated image was treated as rotated'); ok = False
    else:
        print('   OK    CONTROL: an unrotated image is untouched by the new path')

    if not ok:
        print('\n*** SELFTEST FAILED ***')
    elif skipped:
        # Never report a clean sweep over a shrunken population: a gate that reads a shrunken
        # population passes for the wrong reason (16.44), and that applies to a selftest too.
        print(f'\nCONTROLS PASS, BUT {len(skipped)} DID NOT RUN - this reference lacks the '
              f'structure they seed:')
        for nm, why in skipped:
            print(f'   NOT RUN  {nm}  -  {why}')
        print('   Run --selftest again against a reference that HAS those structures before '
              'treating the tool as fully controlled.')
    else:
        print('\nALL CONTROLS PASS - silent when clean, loud when broken.')
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
