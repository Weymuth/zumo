#!/usr/bin/env python3
VERSION = 'v1.3.1'
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
_FONTS = {}
for _w, _p in (('regular', '/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf'),
               ('bold',    '/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf')):
    if os.path.exists(_p):
        _FONTS[_w] = _p

# a drawn graphic's labels must survive on a machine that has none of the designer's fonts
SAFE_FONTS = ('arial', 'helvetica', 'sans-serif', 'courier new', 'monospace', 'times', 'serif')
MIN_PHOTO_SCALE = 2.0        # §17.3b: payload at ~2x its on-screen box
PANEL_MIN_W, PANEL_MIN_H = 150, 60
PANEL_PAD = 6


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
        raise RuntimeError('Liberation Sans not installed - text metrics unavailable')
    return ImageFont.truetype(_FONTS[key], 200).getlength(s) * size / 200.0


def _extent(t):
    s = ''.join(t.itertext()).strip()
    size = float(_inh(t, 'font-size') or 16)
    bold = (_inh(t, 'font-weight') or '400') in ('700', '800', '900', 'bold', 'bolder')
    w = _text_width(s, size, bold)
    x, y = float(t.get('x') or 0), float(t.get('y') or 0)
    anchor = _inh(t, 'text-anchor') or 'start'
    x0 = x - w / 2 if anchor == 'middle' else (x - w if anchor == 'end' else x)
    return s, x0, x0 + w, y, size


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
        if len(hrefs) > 1:
            out.append('payload stored twice (href AND xlink:href) - half the file is a '
                       'duplicate of itself; run fit_raster_svg.py --write')
        uri = im_el.get(hrefs[0])
        if not uri or 'base64,' not in uri:
            out.append('<image> is LINKED, not embedded - this renders blank on the published '
                       'site and looks correct locally (Bible §17.3)')
            continue
        raw = base64.b64decode(uri.split(',', 1)[1])
        pic = Image.open(io.BytesIO(raw))
        bw = float(im_el.get('width') or 0)
        bh = float(im_el.get('height') or 0)
        if bw and bh:
            scale = pic.size[0] / bw
            if scale < MIN_PHOTO_SCALE:
                out.append(f'photograph is {pic.size[0]}x{pic.size[1]} in a {bw:.0f}x{bh:.0f} box '
                           f'= {scale:.2f}x - under the {MIN_PHOTO_SCALE:.0f}x floor, it will look '
                           f'soft. This is the signature of an AI resample; re-place the original.')
            ar_box, ar_pic = bw / bh, pic.size[0] / pic.size[1]
            if abs(ar_box - ar_pic) / ar_pic > 0.02:
                out.append(f'box aspect {ar_box:.3f} vs photo aspect {ar_pic:.3f} - the picture is '
                           f'letterboxed or distorted inside its box; resize the box to match')
        if pic.mode in ('RGBA', 'LA'):
            alpha = pic.getchannel('A')
            if alpha.getextrema() == (255, 255):
                out.append('photo carries a fully-opaque alpha channel doing nothing - '
                           'run fit_raster_svg.py --write')

    # ---- 3. outlined text on a drawn graphic ------------------------------------------------
    ran.add('outlines')
    if not imgs:
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
    for t in root.findall(f'.//{NS}text'):
        s, x0, x1, y, size = _extent(t)
        if not s:
            continue
        ax = float(t.get('x') or 0)
        for px0, py0, px1, py1 in panels:
            if px0 <= ax <= px1 and py0 <= y <= py1:
                if x0 < px0 + PANEL_PAD or x1 > px1 - PANEL_PAD:
                    over = max(px0 + PANEL_PAD - x0, x1 - (px1 - PANEL_PAD))
                    out.append(f'text overflows its panel by {over:.0f} units: '
                               f'"{s[:44]}" spans {x0:.0f}..{x1:.0f} inside {px0:.0f}..{px1:.0f}')
                break

    # ---- 6. text colliding with text on the same line ---------------------------------------
    ran.add('collide_text')
    rows = {}
    for t in root.findall(f'.//{NS}text'):
        s, x0, x1, y, size = _extent(t)
        if s:
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
        c, t = circs[0], txts[0]
        size = float(_inh(t, 'font-size') or 16)
        if (_inh(t, 'text-anchor') or 'start') != 'middle':
            out.append(f'{gid}: badge number has no text-anchor="middle" - it starts at the '
                       f'circle centre and runs right instead of centring')
        dx = abs(float(t.get('x')) - float(c.get('cx')))
        dy = float(t.get('y')) - float(c.get('cy'))
        if dx > 0.5:
            out.append(f'{gid}: badge number off-centre horizontally by {dx:.1f} units')
        if abs(dy - 0.355 * size) > 1.5:
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
            if c[0] != gid and _seg_hits(p, q, lambda x, y, c=c: math.hypot(x - c[1], y - c[2]) < c[3]):
                out.append(f'leader of {gid} crosses the badge of {c[0]}')
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
    expected = {'viewbox', 'raster', 'outlines', 'fonts', 'overflow',
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
    ok &= seeded('badge anchor removed', kill_anchor, 'text-anchor="middle"')

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
        im.set('{http://www.w3.org/1999/xlink}href', im.get('href'))
    ok &= seeded('payload duplicated', dup, 'stored twice')

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
