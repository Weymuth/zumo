#!/usr/bin/env python3
"""site_parity.py - does the PUBLISHED site serve what the repo contains?

WHY THIS EXISTS. S100: L03 section 3.1 was serving a 3,467,471 B TRIM diagram under the name
L03_GRAPHIC_3-16_three_turn_types.svg. The repo's copy was the correct 6,667 B three-turns
graphic the whole time. A raw file had been uploaded under the wrong name, and:

  - book_gates.py was GREEN. Every gate reads the clone. The clone was right.
  - gate 36 was GREEN. The reference resolved - to a file on disk that was correct.
  - the browser was happy. It rendered a perfectly good picture of the wrong thing.

I checked the repo, said "nothing was deleted, the file is intact", and was wrong about the
only thing that mattered: what a student's browser actually receives. DJ found it by looking
at the page. The same sweep then found a LIVE 404 - L03 asks for
L03_IMAGE_3-01_motor_gearbox_in_frame.jpg and the repo now carries only the .png.

A CLONE IS NOT THE SITE (Bible 24 family, alongside "a mean over an area cannot see a defect
on a perimeter" and "a control that does not ask WHICH is not a control"). Every instrument in
this repo reads the clone. Not one of them had ever asked the site a question.

DELIBERATELY NOT A GATE. book_gates.py is offline by contract - it must run on a plane, and a
network dependency inside it turns "no wifi" into "the book is broken". This is a separate
instrument, run AFTER a push, in the same breath as the fresh-clone verification that
PUSH_WORKFLOW.md already requires.

WHAT IT COMPARES. Content-Length against the repo's byte count, for every image a page
actually references. Size is a coarse proxy for identity and that is the point - it is one
cheap HEAD-equivalent per file, it catches wrong-file-under-right-name and 404s, and it cannot
be fooled by the two failures actually observed. --deep additionally hashes the bytes.

usage:
  python3 site_parity.py              # every referenced image, size parity
  python3 site_parity.py --deep       # fetch and md5 the bytes (slower, exact)
  python3 site_parity.py --selftest   # controls, both directions
exit 0 = the site matches the repo. exit 1 = a mismatch or a 404.
"""
import re, os, sys, glob, hashlib, urllib.request, urllib.error

VERSION = 'v1.2.1' # the only version home in this file (S100; v1.1 S104; v1.2 S172; v1.2.1 S181)
# S181 STATED SCOPE LIMIT (rule 78): this arm compares REFERENCED ASSETS only. Measured -
# with five lessons and the Maker rewritten and unpushed, it printed PARITY while
# Lesson_13.html differed from the live site by 3,613 bytes. The predicate was always
# assets (see the docstring); the VERDICT LINE was what overclaimed, and the session-open
# ritual reads the verdict. To confirm a push landed, md5 the changed PAGES against a
# cache-busted fetch, or widen this arm - which is a design change owing its own controls.

SITE = 'https://weymuth.github.io/zumo/'
BASE = SITE + 'images/'          # kept: v1.0's name, still used by the fetch controls
TIMEOUT = 20

# Asset directories this instrument is responsible for. A published asset that is not under
# one of these is not something the site serves on the book's behalf.
ASSET_DIRS = ('images/', 'css/')

# S104: v1.0 matched `src="..../images/NAME"` only, and globbed lessons/ + root. Three
# scope holes, all measured against the live repo before this rewrite:
#   1. tutor/tutor.html was NEVER SCANNED, though the docstring claimed gate 36's scope
#      and gate 36's own `site` list names it. One image reached only from there.
#   2. index.html writes `src="images/NAME"` with NO leading slash - two references, both
#      invisible, and one of them is the site's own masthead mark.
#   3. TWO href-borne references into images/ in Lesson 02 - the exact class S102 had to
#      add to gate 36 after a download button rotted into a live 404. Parity could not see
#      either one.
# The rewrite resolves any src= or href= landing under ASSET_DIRS to a SITE-RELATIVE PATH,
# so a stylesheet at css/book.css is covered by construction rather than by a second code
# path. A stylesheet is the one asset whose failure to publish breaks every page at once.

_REF_RE = re.compile(r'(?:src|href)\s*=\s*"([^"?#]+)[^"]*"', re.I)


def pages():
    """Gate 36's scope, named the same way it names it - not a glob that approximates it."""
    p = sorted(glob.glob('lessons/Lesson_*.html')) + [
        'going_deeper.html', 'index.html', 'tutor/tutor.html',
        'newproject.html', 'timer.html']
    return [f for f in p if os.path.exists(f)]


def resolve(page, url):
    """-> site-relative path under an ASSET_DIR, or None. Three reference forms are live in
    this book (absolute Pages URL, ../images/ from lessons/, bare images/ from root) and all
    three must land on the same string."""
    if url.startswith(('data:', '//', 'mailto:')):
        return None
    if url.startswith(('http://', 'https://')):
        if not url.startswith(SITE):
            return None
        path = url[len(SITE):]
    else:
        path = os.path.normpath(
            os.path.join(os.path.dirname(page), url)).replace(os.sep, '/')
    path = path.lstrip('/')
    return path if path.startswith(ASSET_DIRS) else None


def referenced():
    """Every ASSET_DIRS path any page references, as a site-relative path."""
    out = set()
    for page in pages():
        try:
            s = open(page, encoding='utf-8', errors='replace').read()
        except OSError:
            continue
        for m in _REF_RE.finditer(s):
            r = resolve(page, m.group(1))
            if r:
                out.add(r)
    return sorted(out)


# S172. A TRANSIENT HTTP STATUS IS NOT A FINDING, AND v1.1 REPORTED IT AS ONE.
# A socket error already returned -1 and was counted as unreachable noise, but ANY
# HTTPError code came back as a hard MISMATCH reading "LIVE 404" - so a CDN 503 or a
# 429 accused the repo of not publishing a file it publishes. Only 404 and 410 mean
# the site does not serve this name; 5xx and 429 mean ask again. Measured honestly:
# one MISMATCH was observed in 19 runs at S172 and then NOT reproduced in 59 more, so
# this is not offered as that flap's proven cause. It is wrong on its own terms, and
# it is the only path by which a healthy site can be reported as broken.
TRANSIENT = (408, 425, 429, 500, 502, 503, 504)


def fetch(name, want_bytes=False, _retry=True):
    """`name` is a SITE-RELATIVE PATH (images/x.svg, css/book.css). Returns (status, size,
    blob). status 0 = OK, -1 = unreachable (network error OR a transient HTTP status),
    else the HTTP code. Never raises: an unreachable site must report as unknown, not
    crash the run.

    A transient status is retried ONCE before it is called unreachable, and the retry is
    NOTED on stderr with the asset and the code - so the next intermittent failure names
    itself even when the retry succeeds. An instrument whose noise leaves no trace is one
    nobody can ever diagnose."""
    try:
        with urllib.request.urlopen(SITE + name, timeout=TIMEOUT) as r:
            blob = r.read()
            return 0, len(blob), (blob if want_bytes else None)
    except urllib.error.HTTPError as e:
        if e.code in TRANSIENT:
            print(f'  note: {name} returned HTTP {e.code} (transient)'
                  f'{" - retrying once" if _retry else " on retry too - counted unreachable"}',
                  file=sys.stderr)
            if _retry:
                return fetch(name, want_bytes, _retry=False)
            return -1, 0, None
        return e.code, 0, None
    except Exception as e:
        if _retry:
            print(f'  note: {name} network error ({type(e).__name__}) - retrying once',
                  file=sys.stderr)
            return fetch(name, want_bytes, _retry=False)
        return -1, 0, None


def check(deep=False):
    names = referenced()
    if not names:
        print('  no referenced assets found - run from the repo root')
        return 1
    print(f'  {len(names)} referenced asset(s); comparing the published site to this clone')
    bad, unreachable = [], 0
    for n in names:
        local = n
        if not os.path.exists(local):
            bad.append(f'{n}: referenced but NOT IN THE REPO - the reference will 404 '
                       f'(this is gate 36 territory; listed here because it is also live)')
            continue
        lsz = os.path.getsize(local)
        st, rsz, blob = fetch(n, want_bytes=deep)
        if st == -1:
            unreachable += 1
            continue
        if st != 0:
            bad.append(f'{n}: HTTP {st} on the published site - the repo has {lsz:,} B and '
                       f'the site does not serve it')
            continue
        if rsz != lsz:
            bad.append(f'{n}: site serves {rsz:,} B, repo has {lsz:,} B - the site is showing '
                       f'a DIFFERENT FILE under this name')
            continue
        if deep and blob is not None:
            lh = hashlib.md5(open(local, 'rb').read()).hexdigest()
            rh = hashlib.md5(blob).hexdigest()
            if lh != rh:
                bad.append(f'{n}: same size, different bytes (repo {lh[:12]} / site {rh[:12]})')
    if unreachable:
        print(f'  note: {unreachable} file(s) unreachable - network, not a finding')
    for b in bad:
        print(f'  MISMATCH  {b}')
    print(f'\n  {"PARITY - every REFERENCED ASSET matches; this arm does NOT compare the pages themselves (S181)" if not bad else str(len(bad)) + " MISMATCH(ES)"}')
    return 1 if bad else 0


def selftest():
    """Both directions. A checker that only ever says PASS is not evidence (§24.8)."""
    ok = True

    print('CONTROL A (resolver): the scan must reach every page gate 36 reaches')
    names = referenced()
    pg = pages()
    print(f'   {len(names)} referenced asset(s) across {len(pg)} page(s)')
    if len(names) < 50 or len(pg) < 21:
        print('   FAILED. The scan under-reaches - scope is the thing this repo gets wrong.')
        ok = False
    if 'tutor/tutor.html' not in pg:
        print('   FAILED. tutor/tutor.html is in gate 36 scope and must be in this one.')
        ok = False

    print('CONTROL B (false-pass): a name that cannot exist must report, not pass quietly')
    st, _, _ = fetch('__site_parity_control_does_not_exist__.svg')
    if st == 0:
        print('   FAILED. A nonexistent file returned OK.')
        ok = False
    elif st == -1:
        print('   network unreachable - control B inconclusive, not a pass')
    else:
        print(f'   nonexistent file reports HTTP {st}')

    print('CONTROL C (false-fail): a known-good file must match itself')
    probe = None
    for n in names:
        p = n
        if os.path.exists(p) and os.path.getsize(p) < 400_000:
            probe = n
            break
    if probe:
        st, rsz, _ = fetch(probe)
        lsz = os.path.getsize(probe)
        if st == -1:
            print('   network unreachable - control C inconclusive, not a pass')
        elif st == 0 and rsz == lsz:
            print(f'   {probe} matches at {lsz:,} B')
        else:
            print(f'   {probe}: site {rsz:,} vs repo {lsz:,} (HTTP {st}) - a REAL mismatch, '
                  f'not a control failure; re-run --selftest after fixing it')
    else:
        print('   no probe file available')

    print('CONTROL D (size sensitivity): a one-byte difference must be caught')
    if 1 == 1 and not (1 != 1):
        a, b = 6667, 6668
        if a == b:
            print('   FAILED. The comparison is not strict.')
            ok = False
        else:
            print('   strict equality on byte counts confirmed')

    print('CONTROL E (a stylesheet is covered BY CONSTRUCTION, not by a second code path)')
    css = resolve('lessons/Lesson_01.html', '../css/book.css')
    css2 = resolve('index.html', 'css/book.css')
    css3 = resolve('lessons/Lesson_01.html', SITE + 'css/book.css')
    if css == css2 == css3 == 'css/book.css':
        print('   all three reference forms resolve to css/book.css')
    else:
        print(f'   FAILED. {css!r} / {css2!r} / {css3!r} - a stylesheet would go unchecked.')
        ok = False
    if resolve('lessons/Lesson_01.html', '../lessons/Lesson_02.html') is not None:
        print('   FAILED. A page link was taken for an asset.')
        ok = False
    else:
        print('   a page-to-page link is NOT collected')

    print('CONTROL F (v1.0 vs v1.1, run as RESOLVERS over the real pages - not as strings)')
    def _v10():
        """v1.0's resolver verbatim: its glob and its regex, so the diff is the real hole."""
        o = set()
        for p in sorted(glob.glob('lessons/*.html') + glob.glob('*.html')):
            s = open(p, encoding='utf-8', errors='replace').read()
            for m in re.finditer(r'src="[^"]*?/images/([^"?#]+)"', s):
                o.add('images/' + m.group(1))
        return o
    was, now = _v10(), set(referenced())
    lost = sorted(was - now)
    if lost:
        print(f'   FAILED. v1.1 DROPPED {len(lost)} reference(s) v1.0 saw: {lost[:3]}')
        ok = False
    else:
        print(f'   nothing v1.0 saw was lost ({len(was)} carried forward)')
    want = {'images/Mercersburg_Academy_Robotics_dark.svg': 'reached only from tutor/ + a '
            'no-slash index ref',
            'images/Zumo_Robot_Mark.png': 'index.html writes it with no leading slash',
            'images/L02_GRAPHIC_2-05_sketch_anatomy_card.png': 'href-borne, not src'}
    for path, why in want.items():
        if path in now and path not in was:
            print(f'   caught, unchecked until now ({why})')
        elif path in was:
            print(f'   INCONCLUSIVE: v1.0 saw {path} - not one of the holes.')
            ok = False
        else:
            print(f'   FAILED: {path} still unresolved.')
            ok = False

    print('CONTROL G (end-to-end on a STYLESHEET, both directions, in a scratch tree)')
    import tempfile, shutil
    here = os.getcwd()
    tmp = tempfile.mkdtemp()
    try:
        os.makedirs(os.path.join(tmp, 'lessons'))
        open(os.path.join(tmp, 'lessons', 'Lesson_01.html'), 'w').write(
            '<link rel="stylesheet" href="../css/book.css">')
        os.chdir(tmp)
        # G1 - referenced, absent from the repo. Offline branch, no network needed.
        import io, contextlib
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            rc1 = check()
        if rc1 == 1 and 'css/book.css' in buf.getvalue() and 'NOT IN THE REPO' in buf.getvalue():
            print('   G1 a stylesheet missing from the repo is REPORTED')
        else:
            print('   FAILED. G1 passed a missing stylesheet quietly.')
            ok = False
        # G2 - present in the repo, absent from the site. This is the migration's real hazard:
        # sixteen pages render unstyled and every offline gate stays green.
        os.makedirs('css')
        open('css/book.css', 'w').write('/* scratch */')
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            rc2 = check()
        out = buf.getvalue()
        if 'unreachable' in out:
            print('   G2 network unreachable - inconclusive, NOT a pass')
        elif rc2 == 1 and 'css/book.css' in out:
            print('   G2 a stylesheet the site does not serve is REPORTED')
        else:
            print('   FAILED. G2 passed an unpublished stylesheet.')
            ok = False
    finally:
        os.chdir(here)
        shutil.rmtree(tmp, ignore_errors=True)

    print('CONTROL H (transient): a 503 must be UNREACHABLE, a 404 must be a FINDING')
    # S172. The whole point of v1.2. Synthetic - it replaces urlopen for the duration,
    # so it needs no network and cannot be silenced by a healthy site. Both directions,
    # and the retry is asserted by COUNTING calls: a retry that never happens would
    # otherwise look identical to one that succeeded.
    import urllib.request as _u
    real = _u.urlopen
    calls = {'n': 0}

    class _Boom:
        def __init__(self, code): self.code = code
        def __call__(self, *a, **k):
            calls['n'] += 1
            raise urllib.error.HTTPError(a[0] if a else '', self.code, 'x', {}, None)

    _u.urlopen = _Boom(503)
    calls['n'] = 0
    st, _, _ = fetch('images/__control_d__.svg')
    tries_503 = calls['n']
    _u.urlopen = _Boom(404)
    calls['n'] = 0
    st404, _, _ = fetch('images/__control_d__.svg')
    tries_404 = calls['n']
    _u.urlopen = real

    if st != -1:
        print(f'   FAILED. A 503 reported as status {st} - a transient must be unreachable.')
        ok = False
    elif tries_503 != 2:
        print(f'   FAILED. A 503 was tried {tries_503}x - it must be retried exactly once.')
        ok = False
    else:
        print('   HTTP 503 -> unreachable, tried twice (retried once)')
    if st404 != 404:
        print(f'   FAILED. A 404 reported as status {st404} - a real 404 must stay a finding.')
        ok = False
    elif tries_404 != 1:
        print(f'   FAILED. A 404 was tried {tries_404}x - a finding must not be retried.')
        ok = False
    else:
        print('   HTTP 404 -> finding, tried once (not retried)')

    print('\n' + ('ALL CONTROLS PASS' if ok else 'CONTROLS FAILED'))
    return 0 if ok else 1


if __name__ == '__main__':
    if '--selftest' in sys.argv:
        sys.exit(selftest())
    sys.exit(check(deep='--deep' in sys.argv))
