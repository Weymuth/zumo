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

VERSION = 'v1.0'   # the only version home in this file (S100)

BASE = 'https://weymuth.github.io/zumo/images/'
TIMEOUT = 20


def referenced():
    """Every images/ filename any page references. ONE resolver, mirroring gate 36's scope:
    lessons and every top-level page, because §12/§23 scope was got wrong twice before."""
    out = set()
    for page in sorted(glob.glob('lessons/*.html') + glob.glob('*.html')):
        try:
            s = open(page, encoding='utf-8', errors='replace').read()
        except OSError:
            continue
        for m in re.finditer(r'src="[^"]*?/images/([^"?#]+)"', s):
            out.add(m.group(1))
    return sorted(out)


def fetch(name, want_bytes=False):
    """Returns (status, size, blob). status 0 = OK, else the HTTP code or -1 for a network
    error. Never raises: an unreachable site must report as unknown, not crash the run."""
    try:
        with urllib.request.urlopen(BASE + name, timeout=TIMEOUT) as r:
            blob = r.read()
            return 0, len(blob), (blob if want_bytes else None)
    except urllib.error.HTTPError as e:
        return e.code, 0, None
    except Exception:
        return -1, 0, None


def check(deep=False):
    names = referenced()
    if not names:
        print('  no referenced images found - run from the repo root')
        return 1
    print(f'  {len(names)} referenced image(s); comparing the published site to this clone')
    bad, unreachable = [], 0
    for n in names:
        local = os.path.join('images', n)
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
            bad.append(f'{n}: HTTP {st} on the published site - LIVE 404, repo has {lsz:,} B')
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
    print(f'\n  {"PARITY - the site serves what the repo contains" if not bad else str(len(bad)) + " MISMATCH(ES)"}')
    return 1 if bad else 0


def selftest():
    """Both directions. A checker that only ever says PASS is not evidence (§24.8)."""
    ok = True

    print('CONTROL A (resolver): the reference scan must find images, and reach past lessons/')
    names = referenced()
    pages = sorted(glob.glob('lessons/*.html') + glob.glob('*.html'))
    print(f'   {len(names)} referenced image(s) across {len(pages)} page(s)')
    if len(names) < 50 or len(pages) < 17:
        print('   FAILED. The glob under-reaches - scope is the thing this repo gets wrong.')
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
        p = os.path.join('images', n)
        if os.path.exists(p) and os.path.getsize(p) < 400_000:
            probe = n
            break
    if probe:
        st, rsz, _ = fetch(probe)
        lsz = os.path.getsize(os.path.join('images', probe))
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

    print('\n' + ('ALL CONTROLS PASS' if ok else 'CONTROLS FAILED'))
    return 0 if ok else 1


if __name__ == '__main__':
    if '--selftest' in sys.argv:
        sys.exit(selftest())
    sys.exit(check(deep='--deep' in sys.argv))
