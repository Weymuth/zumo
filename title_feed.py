#!/usr/bin/env python3
"""title_feed.py v1.0 - the §3.1b opener title is FED, not typed (Bible §6.8a's shape).

DJ, S123: "feed the title, don't type it." Gate 51 already FAILS when a §3.1b opener
disagrees with the §6.5a strip. What did not exist was the thing that makes it agree
again: the gate names the drift and a human retypes the title, which is the same
hand-typing the gate was written to catch, one step later.

This tool rewrites the title span inside
    <p>In <strong>Lesson N: TITLE</strong>,
from the §6.5a lesson strip, so a title change in the strip PROPAGATES into prose
instead of drifting away from it.

Entrypoint trap (§24 house rule): the real entrypoint is build(root), NOT main().

WHY THE TARGET IS SCOPED TO THE SECTION AND NEVER TO THE PAGE (S122, three times).
    Measured on the live tree at S123:
        page-wide 'In <strong>Lesson'  -> L03 = 3, L09 = 2, L12 = 3
        section-scoped, colon form     -> 1 in every lesson 01-15, 0 in L16
    The extras are BACKWARD references - L12's "In Lesson 4 you calibrated..." - and a
    page-wide rewriter would overwrite them with the wrong lesson's title. Control C
    below is that exact shape, run against the live file rather than a synthetic one.

WHAT THIS TOOL DOES NOT DECIDE.
    The strip is the source of truth by DJ ruling (S121, S122). If the strip is wrong,
    this tool propagates the wrong title faithfully and gate 51 agrees with it, because
    gate 51 derives from the strip too. That is not a defect to gate around; it is what
    "one source of truth" costs, and it is named here so nobody mistakes agreement
    between this tool and gate 51 for independent confirmation (§24.8).

THE APOSTROPHE IS RULED, AND THE DERIVATION IS NOW BYTE-FAITHFUL (DJ ruling B, S123).
    The transform inherited from next_pointer.esc() and from gate 51 rewrote an ASCII
    apostrophe to &rsquo;, so the emitted title was not a copy of the strip's. Exactly one
    title carries an apostrophe: L11's "Time Lies, Distance Doesn't". Measured before the
    ruling - that title was spelled straight in 21 places (the strip attribute in all
    sixteen lessons, plus L11's own <title>, <h1> and §5b footer, L16's table cell, and a
    JS string in newproject.html) and curly in exactly 3, ALL of them inside
    Lesson_10.html: the §3.1b opener, the generated next-lesson link, and the authored
    NEXT LESSON callout. The transform was turning the book's dominant spelling into a
    minority one on the single page that generated it. DJ ruled the straight form. Three
    owners had to move together - this file, next_pointer.esc(), and gate 51's matching
    expression - because any one of them left behind would have re-created the drift on
    the next apply.

Usage:
    python3 title_feed.py --selftest
    python3 title_feed.py --check      # exit 1 if any opener disagrees with the strip
    python3 title_feed.py --apply
"""

import glob
import os
import re
import shutil
import sys
import tempfile

# VERSION below is the ONE home read by session_versions. It sits ABOVE the changelog so a
# plain grep of this file returns the version and not a changelog line (S98). The docstring
# banner on line 2 is a LABEL, not a second home, and must carry the same string
# (next_pointer v1.0.2's finding); Control H is what keeps them equal.
VERSION = 'v1.0'
# v1.0 (S123): NEW. Feeds the §3.1b opener title from the §6.5a strip.

LESSON_DIR = 'lessons'
FIRST, LAST = 1, 16

# §3.1b's canonical heading, byte-for-byte as gate 51 spells it.
HEAD = '<h3 id="whats-next" class="h3-c-6f7582">What\'s Next?</h3>'

# The opener. The COLON is load-bearing: it is what separates a forward opener from a
# backward reference, which carries no title at all.
TARGET = re.compile(r'(<p>In <strong>Lesson (\d+): )([^<]*)(</strong>,)')


def to_prose(raw):
    """Strip attribute value -> the prose spelling. Shared by value with gate 51.

    DJ RULING B, S123: the apostrophe passes through UNTRANSFORMED. Measured before the
    ruling — L11's title was spelled with an ASCII apostrophe in 21 places and with
    &rsquo; in 3, all three inside Lesson_10.html, so the transform was making the book's
    dominant spelling into a minority one on the single page that generated it. The title
    is now a byte-faithful copy of the strip's, which is what "derived" was always
    claiming. The ampersand is NOT touched either: the strip attribute already carries
    &amp;, so escaping here would double it (Control A).

    Deliberately NOT an import: book_gates.py stands alone by design. Control D is the
    cross-check - if this function and gate 51 ever disagree, applying to the live tree
    stops being a no-op and the control fails loudly.
    """
    return raw


def titles(root='.'):
    """Lesson titles derived from the §6.5a strip, which is asserted byte-identical
    across all sixteen lessons rather than assumed to be."""
    bodies, out = set(), {}
    files = sorted(glob.glob(os.path.join(root, LESSON_DIR, 'Lesson_*.html')))
    if len(files) != LAST:
        raise SystemExit(f'expected {LAST} lessons under {root}/{LESSON_DIR}, found {len(files)}')
    canon = None
    for f in files:
        s = open(f, encoding='utf-8').read()
        i = s.find('LESSON STRIP')
        j = s.find('LESSON STRIP', i + 1) if i >= 0 else -1
        if i < 0 or j < 0:
            raise SystemExit(f'no lesson strip in {f}')
        blk = s[i:j]
        bodies.add(blk)
        if canon is None:
            canon = blk
    if len(bodies) != 1:
        raise SystemExit(f'lesson strip is NOT byte-identical ({len(bodies)} variants) - §6.5a')
    for m in re.finditer(r'href="Lesson_(\d\d)\.html"[^>]*title="([^"]*)"', canon):
        out[int(m.group(1))] = to_prose(m.group(2))
    if sorted(out) != list(range(FIRST, LAST + 1)):
        raise SystemExit(f'strip does not name all sixteen: {sorted(out)}')
    return out


def section(src):
    """The §3.1b What's Next? section as (start, end) absolute offsets, or None.

    Ends at the next <h3>, which is how gate 51 bounds it. Returning offsets rather
    than the substring is what lets apply_one() edit at an INDEX (§6.12c) instead of
    doing a string replace that could land anywhere on the page.
    """
    i = src.find(HEAD)
    if i < 0:
        return None
    j = src.find('<h3', i + len(HEAD))
    return (i, j if j > 0 else len(src))


def opener(src):
    """The one §3.1b opener match, section-scoped, or None.

    Raises when the section holds more than one: a rewriter that silently picks the
    first of several is the failure this whole tool exists to stop.
    """
    span = section(src)
    if span is None:
        return None
    lo, hi = span
    hits = list(TARGET.finditer(src, lo, hi))
    if len(hits) > 1:
        raise SystemExit(f'{len(hits)} openers inside one What\u2019s Next? section, expected 1')
    return hits[0] if hits else None


def build(root='.'):
    """{n: (path, src, match_or_None, want_or_None)} for every lesson. THE ENTRYPOINT."""
    tmap = titles(root)
    out = {}
    for n in range(FIRST, LAST + 1):
        p = os.path.join(root, LESSON_DIR, f'Lesson_{n:02d}.html')
        s = open(p, encoding='utf-8').read()
        m = opener(s)
        want = tmap.get(n + 1) if n < LAST else None
        out[n] = (p, s, m, want)
    return out


def apply_one(src, m, want):
    """Rewrite the title group at its absolute offset. Returns (new_src, delta)."""
    new = src[:m.start(3)] + want + src[m.end(3):]
    delta = len(want) - len(m.group(3))
    if len(new) - len(src) != delta:
        raise SystemExit('byte delta does not match the title delta (§6.12c)')
    return new, delta


def check(root='.'):
    bad = []
    seen = 0
    for n, (p, s, m, want) in build(root).items():
        name = os.path.basename(p)
        if n == LAST:
            if m is not None:
                bad.append(f'{name}: carries a §3.1b opener; L16 ends the book (§3.1)')
            continue
        seen += 1
        if m is None:
            bad.append(f'{name}: no §3.1b opener found in the What\u2019s Next? section')
            continue
        if int(m.group(2)) != n + 1:
            bad.append(f'{name}: opener points at Lesson {m.group(2)}, expected {n + 1}')
        elif m.group(3) != want:
            bad.append(f'{name}: title is {m.group(3)!r}, strip says {want!r}')
    if seen != LAST - 1:
        bad.append(f'COVERAGE: {seen} lessons scanned, expected {LAST - 1}')
    return bad


def write(p, s):
    """Encode first, then atomic replace (§12: a truncating open must not be reachable)."""
    data = s.encode('utf-8')
    tmp = p + '.tmp'
    with open(tmp, 'wb') as fh:
        fh.write(data)
    os.replace(tmp, p)


def apply_all(root='.', dry=False):
    """Returns [(name, old_title, new_title, delta)] for every lesson rewritten."""
    done = []
    for n, (p, s, m, want) in build(root).items():
        if n == LAST or m is None or m.group(3) == want:
            continue
        if int(m.group(2)) != n + 1:
            raise SystemExit(f'{os.path.basename(p)}: opener points at the wrong lesson; not rewriting')
        new, delta = apply_one(s, m, want)
        if not dry:
            write(p, new)
        done.append((os.path.basename(p), m.group(3), want, delta))
    return done


# ----------------------------------------------------------------------------- selftest

def _scratch(root='.'):
    d = tempfile.mkdtemp(prefix='title_feed_')
    shutil.copytree(os.path.join(root, LESSON_DIR), os.path.join(d, LESSON_DIR))
    return d


def selftest(root='.'):
    ok = True

    def rep(good, label, detail=''):
        nonlocal ok
        ok = ok and good
        print(f"   {'OK  ' if good else 'FAIL'}  {label}  {detail}")

    print(f'title_feed.py {VERSION} \u2014 selftest')

    # A: the derivation.
    tmap = titles(root)
    rep(len(tmap) == LAST, 'titles derived from the strip, all sixteen', str(len(tmap)))
    rep(tmap[7] == 'Code Organization', 'a known title round-trips', repr(tmap[7]))
    rep(tmap[3] == 'Motors &amp; TRIM', 'an ampersand title is NOT double-escaped', repr(tmap[3]))

    tree = build(root)

    # B: the target is unique inside the section, and absent from L16.
    counts = {n: (0 if m is None else 1) for n, (p, s, m, w) in tree.items()}
    rep(all(counts[n] == 1 for n in range(1, LAST)), 'one opener in every lesson 01-15',
        str(sorted(set(counts[n] for n in range(1, LAST)))))
    rep(counts[LAST] == 0, 'L16 carries no opener (§3.1)')

    # C: THE SCOPE CONTROL. A page-wide search finds backward references; this must not.
    #    Run against the live files, not a synthetic doc - these are the real defect shape.
    loose = {}
    for n in (3, 9, 12):
        loose[n] = len(re.findall(r'In <strong>Lesson', tree[n][1]))
    rep(loose == {3: 3, 9: 2, 12: 3},
        'the live backward-reference counts are still what scoping is for', str(loose))
    l12 = tree[12][1]
    lo, hi = section(l12)
    back = [m.start() for m in re.finditer(r'<p>In <strong>Lesson \d+</strong>', l12)]
    rep(bool(back) and all(not (lo <= b < hi) for b in back),
        'L12 backward references sit OUTSIDE the section and are untouchable', str(len(back)))

    # D: NO-OP ON THE LIVE TREE. This is the cross-check against gate 51: the two derive
    #    the title separately, so any divergence turns this control red.
    rep(apply_all(root, dry=True) == [], 'applying to the live tree rewrites NOTHING',
        'agrees with gate 51')
    rep(check(root) == [], '--check is clean on the live tree')

    # E: LOUD ON A DRIFTED TITLE, using the REAL historical defect (L07 said
    #    "Line Following" while the strip said "Line Following with P-Control").
    d = _scratch(root)
    p7 = os.path.join(d, LESSON_DIR, 'Lesson_07.html')
    s7 = open(p7, encoding='utf-8').read()
    before = len(s7)
    write(p7, s7.replace('<strong>Lesson 8: Line Following with P-Control</strong>,',
                         '<strong>Lesson 8: Line Following</strong>,', 1))
    bad = check(d)
    rep(len(bad) == 1 and 'Lesson_07' in bad[0] and 'Line Following' in bad[0],
        'a drifted title is REPORTED and named', bad[0] if bad else 'nothing reported')
    done = apply_all(d)
    rep(len(done) == 1 and done[0][0] == 'Lesson_07.html', 'exactly one file rewritten',
        str([x[0] for x in done]))
    rep(len(open(p7, encoding='utf-8').read()) == before, 'byte length restored exactly')
    rep(check(d) == [], 'a second --check is clean')
    rep(apply_all(d) == [], 'a second --apply is a no-op, not a second edit')

    # F: THE FEATURE ITSELF - a title changed in the STRIP propagates into prose.
    d2 = _scratch(root)
    for n in range(FIRST, LAST + 1):
        q = os.path.join(d2, LESSON_DIR, f'Lesson_{n:02d}.html')
        t = open(q, encoding='utf-8').read()
        write(q, t.replace('title="Code Organization"', 'title="Code Architecture"'))
    done = apply_all(d2)
    s6 = open(os.path.join(d2, LESSON_DIR, 'Lesson_06.html'), encoding='utf-8').read()
    rep(len(done) == 1 and done[0][0] == 'Lesson_06.html',
        'a strip title change propagates to exactly the one lesson that names it',
        str([x[0] for x in done]))
    rep('<strong>Lesson 7: Code Architecture</strong>,' in s6,
        'the new title is in L06 prose')
    rep('Code Organization' not in (opener(s6).group(3) or ''), 'the old title is gone')

    # G: a strip that is not byte-identical is REJECTED, not averaged.
    d3 = _scratch(root)
    q = os.path.join(d3, LESSON_DIR, 'Lesson_05.html')
    t = open(q, encoding='utf-8').read()
    write(q, t.replace('title="Encoders"', 'title="Encoders "', 1))
    try:
        titles(d3)
        rep(False, 'a drifted strip raises')
    except SystemExit as e:
        rep('NOT byte-identical' in str(e), 'a drifted strip raises rather than guessing', str(e))

    # H: missing tree raises rather than returning empty.
    try:
        titles('/nonexistent-path-for-control-h')
        rep(False, 'missing tree raises')
    except SystemExit:
        rep(True, 'missing tree raises rather than returning empty')

    # I: GREP TRAP (next_pointer v1.0.2's finding) - the banner is a label, not a home.
    src = open(os.path.abspath(__file__), encoding='utf-8').read()
    banner = re.search(r'title_feed\.py (v[\d.]+)', src)
    rep(banner is not None and banner.group(1) == VERSION,
        'docstring banner and VERSION constant agree',
        f'{banner.group(1) if banner else None} vs {VERSION}')

    for tmpdir in (d, d2, d3):
        shutil.rmtree(tmpdir, ignore_errors=True)

    print('\n' + ('ALL CONTROLS PASS - loud on a drifted title and a drifted strip, '
                  'silent on the live tree, blind to backward references.'
                  if ok else 'SELFTEST FAILED'))
    return 0 if ok else 1


def main():
    root = '.'
    if '--selftest' in sys.argv:
        return selftest(root)
    if '--apply' in sys.argv:
        done = apply_all(root)
        for name, old, new, delta in done:
            print(f'  {name}: {old!r} -> {new!r}  ({delta:+d} bytes)')
        print(f'rewrote {len(done)} opener(s)')
        bad = check(root)
        print('VERIFY: clean' if not bad else 'VERIFY FAILED:\n  ' + '\n  '.join(bad))
        return 1 if bad else 0
    bad = check(root)
    if bad:
        print('\n'.join(bad))
        return 1
    print('every §3.1b opener title matches the §6.5a strip; L16 correctly has none')
    return 0


if __name__ == '__main__':
    sys.exit(main())
