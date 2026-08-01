#!/usr/bin/env python3
VERSION = 'v1.2'
# ---------------------------------------------------------------------------------------------
# flatten_alpha.py - drop a transparent photo onto the backdrop it actually sits on.
#
# WHY THIS EXISTS. DJ's source photographs come from Pololu product images with the background
# knocked out in Photoshop, so their PNGs carry a real alpha channel. A real alpha channel cannot
# become a JPEG, so fit_raster_svg.py correctly refuses to convert it - and the composites land
# 1.3 to 3.7 MB against gate 37's 500,000 B ceiling. Measured: the same photograph is roughly
# SEVEN TIMES heavier as PNG+alpha than as JPEG.
#
# The transparency is almost always doing nothing. These graphics put the robot on a panel; the
# knockout just means the panel shows through instead of the photo's own white studio background.
# Flatten it onto that panel and the file drops by 85-90% with no visible change.
#
# THE PART THAT IS EASY TO GET WRONG IS *WHAT* TO FLATTEN ONTO. Three real cases, all met in S99:
#   flat page colour      L09 9-3           #fafafa
#   an inner panel        hardware_diagram  #FBFBFC - and a first attempt picked #C9A463, a
#                                           3px brass rule that does not cover the photo at all,
#                                           which would have haloed the robot gold
#   a GRADIENT            L10 10-01         url(#matGrad) - no single colour can match it
#
# So: pick the SMALLEST rect that fully covers the image box, and if its fill is not a plain
# colour, render the page with the photo removed and composite onto the real pixels.
#
# ENTRYPOINT IS flatten(path) -> (svg_text, report). Nothing is written unless --write.
#
# CHANGELOG
# v1.1 (S99): HANDLE EVERY <image>, NOT JUST THE FIRST. v1.0 read imgs[0] and returned, so a
#   two-photograph composite whose FIRST image was an ordinary JPEG was skipped entirely -
#   'no alpha channel, nothing to flatten' - while the second sat there as a 2.7 MB transparent
#   PNG, the whole reason the file was 4.1 MB and over the gate. A false negative on the exact
#   defect this tool exists for, unnoticed because every file it had been shown until then
#   carried exactly one photograph. CONTROL 4 covers it.
#   NOTE: the behaviour shipped before this line did. The functional change landed in one edit
#   and the version bump was in another that aborted, so the file ran as v1.1 while reporting
#   v1.0 - caught only because session_versions was taught to read it. §5b: the version has one
#   home and it must move in the SAME edit as the behaviour.
# v1.0 (S99): new.
# ---------------------------------------------------------------------------------------------
import sys, os, io, base64, tempfile

try:
    from lxml import etree
except ImportError:
    sys.exit('flatten_alpha needs lxml')
try:
    from PIL import Image, ImageChops
except ImportError:
    sys.exit('flatten_alpha needs pillow')
try:
    import cairosvg
except ImportError:
    cairosvg = None      # only needed for the gradient case; we fail loudly there, not silently

NS = '{http://www.w3.org/2000/svg}'
XLINK = 'http://www.w3.org/1999/xlink'
QUALITY = 92             # pinned, same as fit_raster_svg - quality is the rule, size the consequence
GATE37 = 500_000


def _num(v, d=0.0):
    try:
        return float(v)
    except (TypeError, ValueError):
        return d


def _payload(im_el):
    key = next((k for k in im_el.keys() if k.endswith('href')), None)
    if key is None:
        return None, None
    uri = im_el.get(key) or ''
    if 'base64,' not in uri:
        return key, None
    return key, base64.b64decode(uri.split(',', 1)[1])


def _backdrop(root, im_el):
    """The smallest rect painted BEFORE the photo that fully covers it.

    Smallest matters: the page background also covers it, but an inner panel is what actually
    shows through. Painted-before matters: a rect drawn after the photo is on top of it.
    """
    ix, iy = _num(im_el.get('x')), _num(im_el.get('y'))
    iw, ih = _num(im_el.get('width')), _num(im_el.get('height'))
    best = None
    for e in root.iter():
        if e is im_el:
            break
        if not isinstance(e.tag, str) or e.tag != NS + 'rect':
            continue
        x, y = _num(e.get('x')), _num(e.get('y'))
        w, h = _num(e.get('width')), _num(e.get('height'))
        if x <= ix and y <= iy and x + w >= ix + iw and y + h >= iy + ih:
            if best is None or w * h < best[0]:
                best = (w * h, e.get('fill'), e)
    return (best[1], best[2]) if best else (None, None)


def _render_without_photo(path, root_copy_src, width_px):
    """Render the page with the <image> removed, so we can sample what is really behind it."""
    if cairosvg is None:
        raise RuntimeError('this file needs a rendered backdrop (its background is not a plain '
                           'colour) and cairosvg is not installed: pip install cairosvg')
    t = etree.parse(root_copy_src)
    r = t.getroot()
    im = r.find(f'.//{NS}image')
    if im is not None:
        im.getparent().remove(im)
    buf = io.BytesIO()
    t.write(buf, encoding='utf-8', xml_declaration=True)
    out = io.BytesIO()
    cairosvg.svg2png(bytestring=buf.getvalue(), write_to=out, output_width=width_px)
    out.seek(0)
    return Image.open(out).convert('RGB')


def flatten(path, quality=QUALITY):
    """Return (new_svg_text_or_None, report). Never writes.

    EVERY <image> is considered, not just the first. v1.0 read imgs[0] and returned, so a
    composite whose first photograph was an ordinary JPEG was skipped whole while a 2.7 MB
    transparent PNG sat beside it untouched.
    """
    rep = {'before': os.path.getsize(path), 'reason': None, 'mode': None, 'fill': None,
           'n_images': 0, 'n_flattened': 0}
    tree = etree.parse(path)
    root = tree.getroot()
    imgs = root.findall(f'.//{NS}image')
    rep['n_images'] = len(imgs)
    if not imgs:
        rep['reason'] = 'no embedded raster - nothing to flatten'
        return None, rep

    todo, skipped = [], []
    for el in imgs:
        _k, rw = _payload(el)
        if rw is None:
            skipped.append('linked, not embedded'); continue
        pp = Image.open(io.BytesIO(rw))
        if pp.mode not in ('RGBA', 'LA'):
            skipped.append('no alpha'); continue
        if pp.convert('RGBA').getchannel('A').getextrema()[0] == 255:
            skipped.append("dead alpha - fit_raster_svg's job"); continue
        todo.append([el, rw, pp.convert('RGBA')])
    if not todo:
        rep['reason'] = ('nothing to flatten across %d image(s): %s'
                         % (len(imgs), '; '.join(sorted(set(skipped)))))
        return None, rep

    modes, fills, pb, pa = [], [], 0, 0
    for entry in todo:
        im_el, raw, pic = entry
        ix, iy = _num(im_el.get('x')), _num(im_el.get('y'))
        iw, _ih = _num(im_el.get('width')), _num(im_el.get('height'))
        PW, PH = pic.size
        fill, _rect = _backdrop(root, im_el)
        fills.append(fill)

        if fill and fill.startswith('#') and len(fill) in (4, 7):
            h = fill.lstrip('#')
            if len(h) == 3:
                h = ''.join(c * 2 for c in h)
            col = tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))
            under = Image.new('RGB', (PW, PH), col)
            modes.append(f'flat colour {fill}')
        else:
            vb = (root.get('viewBox') or '').split()
            vbw = _num(vb[2]) if len(vb) == 4 else iw
            if not (iw and vbw):
                rep['reason'] = 'cannot locate an image box in the viewBox'
                return None, rep
            scale = PW / iw
            full = _render_without_photo(path, path, int(round(vbw * scale)))
            x0, y0 = int(round(ix * scale)), int(round(iy * scale))
            under = full.crop((x0, y0, x0 + PW, y0 + PH))
            modes.append(f'rendered backdrop ({fill or "no covering rect"})')

        flat = under.copy()
        flat.paste(pic, mask=pic.getchannel('A'))
        buf = io.BytesIO()
        flat.save(buf, 'JPEG', quality=quality, optimize=True)
        entry.append(buf.getvalue())
        pb += len(raw); pa += len(buf.getvalue())

    if 'xlink' not in (root.nsmap or {}):
        ns = dict(root.nsmap or {})
        ns['xlink'] = XLINK
        new = etree.Element(root.tag, nsmap=ns)
        for k, v in root.attrib.items():
            new.set(k, v)
        new.text = root.text
        for c in list(root):
            new.append(c)
        tree = etree.ElementTree(new)
        fresh = new.findall(f'.//{NS}image')
        for i, entry in enumerate(todo):
            entry[0] = fresh[imgs.index(entry[0])] if entry[0] in imgs else fresh[i]
        root = new

    for im_el, _raw, _pic, jpg in todo:
        for k in list(im_el.keys()):
            if k.endswith('href'):
                del im_el.attrib[k]
        im_el.set(f'{{{XLINK}}}href', 'data:image/jpeg;base64,' + base64.b64encode(jpg).decode())

    out = etree.tostring(tree, encoding='utf-8', xml_declaration=True).decode('utf-8')
    rep['n_flattened'] = len(todo)
    rep['mode'] = ' + '.join(modes)
    rep['fill'] = fills[0] if fills else None
    rep['payload_before'] = pb
    rep['payload_after'] = pa
    rep['after'] = len(out.encode('utf-8'))
    return out, rep


def verify(before_path, after_text, width=1100):
    """Render both and report how far the flattened version drifted. Trust nothing unmeasured."""
    if cairosvg is None:
        return None
    import numpy as np
    a_io, b_io = io.BytesIO(), io.BytesIO()
    cairosvg.svg2png(url=before_path, write_to=a_io, output_width=width)
    cairosvg.svg2png(bytestring=after_text.encode('utf-8'), write_to=b_io, output_width=width)
    a_io.seek(0); b_io.seek(0)
    import numpy
    A = numpy.array(Image.open(a_io).convert('RGB')).astype(int)
    B = numpy.array(Image.open(b_io).convert('RGB')).astype(int)
    d = numpy.abs(A - B).sum(axis=2)
    return {'mean': float(d.mean()), 'over12': int((d > 12).sum()), 'total': int(d.size)}


def _selftest():
    _skipped = []
    """Controls both ways: a flat backdrop, a gradient backdrop, and files that must be REFUSED."""
    ok = True
    tmp = tempfile.mkdtemp()
    # a photo-like RGBA payload with a genuinely transparent border
    # Photograph-LIKE content, not noise. A first cut used pure random pixels and control 2
    # failed at 6.4 drift - because q92 JPEG mangles random noise, not because the flatten was
    # wrong. The fixture has to represent what the tool is actually for: smooth photographic
    # tone. The threshold stays where it is; the fixture was the thing that was unrealistic.
    im = Image.new('RGBA', (400, 300), (0, 0, 0, 0))
    px = im.load()
    for y in range(40, 260):
        for x in range(40, 360):
            u, v = (x - 40) / 320.0, (y - 40) / 220.0
            px[x, y] = (int(40 + 180 * u), int(60 + 150 * v), int(90 + 120 * (1 - u) * v), 255)
    b = io.BytesIO(); im.save(b, 'PNG')
    uri = 'data:image/png;base64,' + base64.b64encode(b.getvalue()).decode()

    def build(bg_def, bg_fill, name):
        p = os.path.join(tmp, name)
        open(p, 'w').write(
            '<svg xmlns="http://www.w3.org/2000/svg" '
            'xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 1000 750">'
            f'{bg_def}'
            f'<rect x="0" y="0" width="1000" height="750" fill="#ffffff"/>'
            f'<rect x="50" y="50" width="900" height="650" fill="{bg_fill}"/>'
            f'<image x="100" y="100" width="400" height="300" xlink:href="{uri}"/>'
            '<text x="10" y="740">label</text></svg>')
        return p

    print('CONTROL 1 (flat backdrop: must flatten onto the INNER panel, not the page)')
    p = build('', '#FBFBFC', 'flat.svg')
    new, rep = flatten(p)
    hit = new is not None and rep['fill'] == '#FBFBFC'
    print(f"   backdrop chosen: {rep['fill']}  mode: {rep['mode']}")
    print(f"   {rep['before']:,} -> {rep.get('after', 0):,} B")
    if not hit:
        print('   FAILED - wrong backdrop'); ok = False
    if new and 'xlink:href="data:image/jpeg' not in new:
        print('   FAILED - must re-embed as JPEG under xlink:href'); ok = False

    print('CONTROL 2 (gradient backdrop: no single colour can match, must render)')
    if cairosvg is None:
        # SKIP, LOUDLY. This control is the only one that needs a renderer, and until v1.2 its
        # RuntimeError aborted the whole selftest - so on a fresh sandbox the remaining controls
        # never ran and the operator saw a traceback instead of a result. A checker that cannot
        # run a check must say which check it skipped, not take the rest of the suite down.
        print('   SKIPPED - cairosvg is not installed, so the gradient path was NOT tested.')
        print('            pip install cairosvg --break-system-packages, then re-run.')
        _skipped.append('CONTROL 2 gradient backdrop')
    else:
      grad = ('<defs><linearGradient id="g"><stop offset="0" stop-color="#ffffff"/>'
              '<stop offset="1" stop-color="#cccccc"/></linearGradient></defs>')
      p2 = build(grad, 'url(#g)', 'grad.svg')
      new2, rep2 = flatten(p2)
      if new2 is None or 'rendered backdrop' not in (rep2['mode'] or ''):
          print(f"   FAILED - fell back to a flat fill: {rep2}"); ok = False
      else:
          print(f"   mode: {rep2['mode']}   {rep2['before']:,} -> {rep2['after']:,} B")
          v = verify(p2, new2)
          if v:
              print(f"   drift vs the transparent original: mean {v['mean']:.3f}, "
                    f"{v['over12']:,}/{v['total']:,} pixels over 12")
              if v['mean'] > 3.0:
                  print('   FAILED - the flatten visibly changed the page'); ok = False

    print('CONTROL 3 (must REFUSE what is not its job)')
    novec = os.path.join(tmp, 'novec.svg')
    open(novec, 'w').write('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 10 10">'
                           '<text x="1" y="5">hi</text></svg>')
    _n, r3 = flatten(novec)
    print(f"   pure vector      -> {r3['reason']}")
    if _n is not None:
        print('   FAILED'); ok = False
    opaque = Image.new('RGBA', (60, 60), (10, 20, 30, 255))
    bb = io.BytesIO(); opaque.save(bb, 'PNG')
    ou = 'data:image/png;base64,' + base64.b64encode(bb.getvalue()).decode()
    op = os.path.join(tmp, 'opaque.svg')
    open(op, 'w').write('<svg xmlns="http://www.w3.org/2000/svg" '
                        'xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 100 100">'
                        f'<rect x="0" y="0" width="100" height="100" fill="#fff"/>'
                        f'<image x="0" y="0" width="60" height="60" xlink:href="{ou}"/></svg>')
    _n2, r4 = flatten(op)
    print(f"   dead alpha       -> {r4['reason']}")
    if _n2 is not None:
        print('   FAILED - a dead alpha channel belongs to fit_raster_svg, not here'); ok = False

    print('CONTROL 4 (TWO images, only the second transparent: must flatten the SECOND)')
    op2 = Image.new('RGB', (200, 150), (30, 60, 90))            # image 1: no alpha at all
    bo = io.BytesIO(); op2.save(bo, 'JPEG', quality=90)
    u1 = 'data:image/jpeg;base64,' + base64.b64encode(bo.getvalue()).decode()
    p4 = os.path.join(tmp, 'two.svg')
    open(p4, 'w').write(
        '<svg xmlns="http://www.w3.org/2000/svg" '
        'xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 1000 750">'
        '<rect x="0" y="0" width="1000" height="750" fill="#ffffff"/>'
        '<rect x="50" y="50" width="900" height="650" fill="#FBFBFC"/>'
        f'<image x="600" y="100" width="200" height="150" xlink:href="{u1}"/>'
        f'<image x="100" y="100" width="400" height="300" xlink:href="{uri}"/>'
        '<text x="10" y="740">label</text></svg>')
    n4, r4 = flatten(p4)
    print(f"   images seen {r4['n_images']}   flattened {r4['n_flattened']}   mode {r4['mode']}")
    if n4 is None or r4['n_images'] != 2 or r4['n_flattened'] != 1:
        print('   FAILED - v1.0 skipped this whole file on the strength of imgs[0]'); ok = False
    elif n4.count('data:image/jpeg') != 2:
        print('   FAILED - both images must survive'); ok = False

    if _skipped:
        print('\n*** NOT FULLY TESTED: ' + ', '.join(_skipped) + ' ***')
    print('\n' + (('ALL CONTROLS PASS' + (' (with skips)' if _skipped else ''))
                  if ok else '*** SELFTEST FAILED ***'))
    return ok


if __name__ == '__main__':
    if '--selftest' in sys.argv:
        sys.exit(0 if _selftest() else 1)
    paths = [a for a in sys.argv[1:] if not a.startswith('--')]
    if not paths:
        sys.exit(f'flatten_alpha {VERSION}\n'
                 f'usage: flatten_alpha.py FILE.svg [--write]\n'
                 f'       flatten_alpha.py --selftest')
    write = '--write' in sys.argv
    rc = 0
    for p in paths:
        new, rep = flatten(p)
        print(f'\n{os.path.basename(p)}')
        if new is None:
            print(f'   skipped: {rep["reason"]}')
            continue
        print(f'   backdrop : {rep["mode"]}')
        print(f'   payload  : {rep["payload_before"]:,} -> {rep["payload_after"]:,} B')
        print(f'   file     : {rep["before"]:,} -> {rep["after"]:,} B'
              + ('' if rep['after'] <= GATE37 else
                 f'   STILL OVER the {GATE37:,} B ceiling - check the display box'))
        v = verify(p, new)
        if v:
            print(f'   drift    : mean {v["mean"]:.3f}, {v["over12"]:,} of {v["total"]:,} '
                  f'pixels differ by more than 12')
            if v['mean'] > 3.0:
                print('   WARNING: that is a visible change - inspect before shipping')
                rc = 1
        if write:
            fd, t = tempfile.mkstemp(dir=os.path.dirname(os.path.abspath(p)), suffix='.tmp')
            os.close(fd)
            open(t, 'w', encoding='utf-8').write(new)
            os.replace(t, p)
            print(f'   written  : {p}')
    sys.exit(rc)
