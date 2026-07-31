#!/usr/bin/env python3
# fit_raster_svg.py - normalise a raster-wrapped SVG to a byte budget.
# VERSION below is the ONE home, and it sits ABOVE the changelog so a plain grep of this
# file lands on the live version, not on a changelog line (S98 convention).
VERSION = 'v1.1'
# v1.1 (S98): QUALITY IS THE RULE, SIZE IS THE CONSEQUENCE. v1.0 searched quality
#   downward until the file fitted a byte budget, which meant the one file carrying TWO
#   photographs got squeezed to q70 to protect a number — degrading the picture, which
#   is the exact complaint that started this work. Measured at q92, every single-photo
#   file in the repo lands between 128 KB and 350 KB, comfortably under the gate 37
#   ceiling; only the two-photo file exceeds it, and it does so at EVERY quality down
#   to q85. So the budget was never the binding constraint for real assets — it only
#   ever bit the one file that should be split. DJ ruling: pin quality, warn on size.
#
# WHY THIS EXISTS. A photograph cannot be redrawn as vector - S98 measured five staged files
# and every one carried photographic content, and the one true-vector redraw DJ has seen
# (zumo_32u4_oled_main_board_top_view_r02.svg) turned out to be a CARTOON of the board: its
# 39 text runs are the silkscreen, not labels. So photo-plus-overlay SVGs are a real asset
# class in this book, and they must base64-embed, because an SVG loaded through <img src>
# runs in secure static mode and cannot fetch an external file.
#
# What it is NOT allowed to be is four megabytes. Two wastes measured in the uploaded r01,
# both free to remove and neither visible on screen:
#   1. ONE <image> carrying the payload TWICE - href= and xlink:href= both hold the full
#      base64. Not two layers. The chassis file in images/ has the identical pattern.
#   2. An RGBA channel that is 100% opaque - zero transparent pixels, zero partial.
# Deduped, flattened to RGB and re-encoded, r01 went 4,262,718 B -> 350,471 B unchanged
# on screen. This script does that, to a budget, repeatably.
#
# THE BUDGET IS THE RULE, NOT A QUALITY NUMBER. Nobody should be choosing "q85 or q92" per
# file. Name the bytes a student may spend on one image; this searches for the best quality
# that fits and reports what it found.
#
# usage:
#   python3 fit_raster_svg.py FILE.svg                  report only, writes nothing
#   python3 fit_raster_svg.py FILE.svg --quality 88     override the pinned quality
#   python3 fit_raster_svg.py FILE.svg --write          write FILE.svg in place
#   python3 fit_raster_svg.py FILE.svg --write --out X  write to X
#   python3 fit_raster_svg.py images/*.svg              report on many
#   python3 fit_raster_svg.py --selftest                control run, both directions

import re, os, sys, base64, io, glob, tempfile

QUALITY = 92          # THE RULE. Never traded away to hit a size. Measured: q95 costs ~25%
                      # more bytes for no visible gain, q88 saves ~15% more but starts to
                      # risk the fine detail on a populated PCB, which is the whole point of
                      # photographing one. Override per run with --quality.
CEILING = 500_000     # a WARNING, not a squeeze — matches gate 37's ceiling. A file over it
                      # at full quality is carrying too much: split it, do not degrade it.
RETINA = 2.0          # keep at most this multiple of the on-screen box, then stop

IMG_RE = re.compile(r'<image\b[^>]*/?>', re.S)
DATA_RE = re.compile(r'data:image/(\w+);base64,([A-Za-z0-9+/=\s]+)')


def _attr(tag, name):
    m = re.search(r'\b%s="([^"]*)"' % name, tag)
    return m.group(1) if m else None


def analyse(path):
    """Read a .svg and describe every embedded raster. No writes, no judgement."""
    src = open(path, encoding='utf-8', errors='replace').read()
    out = {'path': path, 'bytes': os.path.getsize(path), 'images': [], 'src': src}
    out['draw'] = len(re.findall(
        r'<(rect|circle|ellipse|path|line|polygon|polyline|text)\b', src))
    for tag in IMG_RE.findall(src):
        payloads = DATA_RE.findall(tag)
        if not payloads:
            continue
        fmt, b64 = payloads[0]
        raw = base64.b64decode(re.sub(r'\s', '', b64))
        from PIL import Image
        im = Image.open(io.BytesIO(raw))
        alpha_used = False
        if im.mode in ('RGBA', 'LA'):
            h = im.getchannel('A').histogram()
            alpha_used = (sum(h) - h[255]) > 0
        out['images'].append({
            'tag': tag, 'fmt': fmt, 'raw': raw, 'size': im.size, 'mode': im.mode,
            'alpha_used': alpha_used,
            # the same payload written into href AND xlink:href is the generator quirk,
            # not a second layer: identical bytes, one drawn image, double the file.
            'dup_payload': len(payloads) > 1 and payloads[0][1] == payloads[1][1],
            'box_w': float(_attr(tag, 'width') or im.size[0]),
        })
    return out


def fit(path, quality=QUALITY, verbose=True):
    """Return (new_svg_text, report). One pass at the pinned quality. Never writes."""
    a = analyse(path)
    rep = {'before': a['bytes'], 'draw': a['draw'], 'n_images': len(a['images']),
           'dup': sum(1 for i in a['images'] if i['dup_payload']),
           'alpha_waste': sum(1 for i in a['images']
                              if i['mode'] in ('RGBA', 'LA') and not i['alpha_used'])}
    if not a['images']:
        rep['note'] = 'no embedded raster - nothing to do'
        return None, rep
    from PIL import Image
    for q in (quality,):
        src = a['src']
        for im_info in a['images']:
            im = Image.open(io.BytesIO(im_info['raw']))
            keep_alpha = im_info['alpha_used']
            cap = int(im_info['box_w'] * RETINA)
            if im.size[0] > cap:
                im = im.resize((cap, int(im.size[1] * cap / im.size[0])), Image.LANCZOS)
            buf = io.BytesIO()
            if keep_alpha:
                im.save(buf, 'PNG', optimize=True)          # transparency cannot go to JPEG
                mime = 'png'
            else:
                im.convert('RGB').save(buf, 'JPEG', quality=q, optimize=True,
                                       progressive=True)
                mime = 'jpeg'
            uri = 'data:image/%s;base64,%s' % (
                mime, base64.b64encode(buf.getvalue()).decode())
            tag = im_info['tag']
            # ONE payload: drop the duplicated legacy attribute, keep geometry byte-for-byte
            new_tag = re.sub(r'\s*xlink:href="data:image/[^"]*"', '', tag)
            new_tag = re.sub(r'href="data:image/[^"]*"', 'href="%s"' % uri, new_tag, count=1)
            assert src.count(tag) >= 1, 'fit: the <image> tag moved between passes'
            src = src.replace(tag, new_tag, 1)
        n = len(src.encode('utf-8'))
        if True:
            # NEVER ENLARGE. Re-encoding is not always a win: content that JPEG handles
            # badly (noise, hard edges, screenshots) comes back bigger, and the selftest
            # caught exactly that on its first run. If the best pass is not smaller than
            # what is already on disk, the right answer is to leave the file alone.
            if n >= rep['before']:
                rep['note'] = ('re-encoding does not help this content '
                               f'(best pass {n:,} B >= current {rep["before"]:,} B) - left alone')
                return None, rep
            rep['after'] = n
            rep['quality'] = q if not all(i['alpha_used'] for i in a['images']) else 'png'
            rep['fits'] = n <= CEILING
            return src, rep
    return None, rep


def show(rep):
    if 'after' not in rep:
        print(f"  {rep.get('note', 'no change')}")
        return
    pct = 100 * (1 - rep['after'] / rep['before'])
    flag = ('' if rep['fits'] else
            f"   OVER THE {CEILING:,} B CEILING at full quality — "
            f"{'split it' if rep['n_images'] > 1 else 'check the display box'}, "
            f'do not lower the quality')
    print(f"  {rep['before']:>10,} -> {rep['after']:>9,} B  ({pct:5.1f}% smaller)  "
          f"quality={rep['quality']}  dup_payload={rep['dup']}  "
          f"dead_alpha={rep['alpha_waste']}  vector_elems={rep['draw']}{flag}")


def selftest():
    """Both directions: a fat file must shrink, an already-lean file must not be touched."""
    from PIL import Image
    ok = True
    tmp = tempfile.mkdtemp()

    # direction 1 - a fat raster-wrapped SVG with the href/xlink duplication MUST shrink
    # photographic content, synthesised: random noise under a heavy blur. PNG stores this
    # badly (tens of thousands of colours, no runs) and JPEG stores it well - which is the
    # property that makes a photo a photo, for compression purposes.
    import random
    from PIL import ImageFilter
    random.seed(7)
    small = Image.new('RGB', (250, 188))
    small.putdata([(random.randrange(256), random.randrange(256), random.randrange(256))
                   for _ in range(250 * 188)])
    im = small.resize((2000, 1500), Image.BICUBIC).filter(ImageFilter.GaussianBlur(3))
    im = im.convert('RGBA')
    buf = io.BytesIO(); im.save(buf, 'PNG')
    uri = 'data:image/png;base64,' + base64.b64encode(buf.getvalue()).decode()
    fat = os.path.join(tmp, 'fat.svg')
    open(fat, 'w').write(
        '<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" '
        'viewBox="0 0 1000 750"><image x="0" y="0" width="1000" height="750" '
        f'href="{uri}" xlink:href="{uri}"/><text x="10" y="20">label</text></svg>')
    new, rep = fit(fat)
    print('CONTROL 1 (fat file must shrink, and the duplicate must be seen)')
    print(f"   dup_payload seen: {rep['dup']}   dead_alpha seen: {rep['alpha_waste']}")
    show(rep)
    if not (new and rep['dup'] == 1 and rep['alpha_waste'] == 1
            and rep['after'] < rep['before'] / 2):
        print('   FAILED'); ok = False
    if new and 'xlink:href="data:' in new:
        print('   FAILED - the duplicate payload survived'); ok = False
    if new and ('width="1000"' not in new or 'x="0"' not in new):
        print('   FAILED - geometry was not preserved'); ok = False

    # direction 2 - a pure-vector SVG must come back untouched, or the tool would
    # "improve" the 194 files that are already right
    print('CONTROL 2 (pure vector must be left alone)')
    thin = os.path.join(tmp, 'thin.svg')
    open(thin, 'w').write('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 10 10">'
                          '<rect x="1" y="1" width="8" height="8"/></svg>')
    new2, rep2 = fit(thin)
    print(f"   returned: {new2 is None}  note: {rep2.get('note')}")
    if new2 is not None:
        print('   FAILED - rewrote a file with no raster in it'); ok = False

    # direction 3 - real transparency must NOT be flattened into a JPEG
    print('CONTROL 3 (genuine alpha must survive as PNG)')
    im2 = Image.new('RGBA', (400, 400), (255, 0, 0, 0))
    for y in range(200):
        for x in range(400):
            im2.putpixel((x, y), ((x * 5) % 256, 40, 90, 255))
    b2 = io.BytesIO(); im2.save(b2, 'PNG')
    u2 = 'data:image/png;base64,' + base64.b64encode(b2.getvalue()).decode()
    alp = os.path.join(tmp, 'alpha.svg')
    open(alp, 'w').write('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400">'
                         f'<image x="0" y="0" width="400" height="400" href="{u2}"/></svg>')
    new3, rep3 = fit(alp)
    kept = new3 is not None and 'data:image/png;base64' in new3
    print(f"   stayed PNG: {kept}   quality field: {rep3.get('quality')}")
    if not kept:
        print('   FAILED - transparency was flattened'); ok = False

    print('CONTROL 4 (content JPEG cannot help must be left alone, never enlarged)')
    im4 = Image.new('RGB', (900, 700))
    im4.putdata([((x * 7) % 256, (x * 13) % 256, (x * 3) % 256)
                 for x in range(900 * 700)])
    b4 = io.BytesIO(); im4.save(b4, 'PNG', optimize=True)
    u4 = 'data:image/png;base64,' + base64.b64encode(b4.getvalue()).decode()
    pat = os.path.join(tmp, 'pattern.svg')
    open(pat, 'w').write('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 700">'
                         f'<image x="0" y="0" width="900" height="700" href="{u4}"/></svg>')
    new4, rep4 = fit(pat)
    left_alone = new4 is None and 'does not help' in rep4.get('note', '')
    print(f"   left alone: {left_alone}  {rep4.get('note', '')}")
    if not left_alone:
        print('   FAILED - the tool would have written a file no smaller than it found')
        ok = False

    print('\n' + ('ALL CONTROLS PASS' if ok else 'SELFTEST FAILED'))
    return 0 if ok else 1


def main():
    args = [a for a in sys.argv[1:]]
    if '--selftest' in args:
        sys.exit(selftest())
    write = '--write' in args
    out = None
    if '--out' in args:
        out = args[args.index('--out') + 1]
    quality = QUALITY
    if '--quality' in args:
        quality = int(args[args.index('--quality') + 1])
    files = []
    for a in args:
        if a.startswith('--') or a == out or a.isdigit():
            continue
        files.extend(sorted(glob.glob(a)))
    if not files:
        print(__doc__ or 'give me one or more .svg paths'); sys.exit(2)
    for f in files:
        print(os.path.basename(f))
        new, rep = fit(f, quality)
        show(rep)
        if write and new:
            target = out or f
            tmp = target + '.tmp'
            open(tmp, 'w', encoding='utf-8').write(new)
            os.replace(tmp, target)
            print(f"   written: {target}")


if __name__ == '__main__':
    main()
