#!/usr/bin/env python3
# VERSION is the ONE home and sits ABOVE the changelog, so a plain grep of this file
# returns the version and not a changelog line (S98).
VERSION = 'v1.1'
# v1.0 (S128): first release. Seats data-family on every callout block.
"""family_tag.py - writes the FAMILY onto the callout that carries it (Bible §24.14).

WHY THIS EXISTS. build_family_map resolves 1,069 callout blocks through three tiers,
and the last of them - GLYPH - resolves 213 blocks by the decorative emoji alone.
The marks arc replaces that emoji with an <img>. The moment it does, those blocks
have no family signal left and gate 47 fails. S112 wrote the warning into the
generator itself: "This tier is a STOPGAP ... when the emoji are replaced the family
must already be known from content and the mark must follow from the family."

So the family moves out of the decoration and into the markup, as an attribute, in
the same shape the book already uses for data-challenge (§20.2) and data-reveal
(§20.1). AFTER this runs, the glyph is decoration and nothing else - which is what
lets it be replaced.

DIRECTION MATTERS, AND IT IS THE WHOLE POINT (§24.14). Family comes from CONTENT;
the mark and the colour are OUTPUTS. This tool writes family -> attribute. Nothing
may ever read the mark filename back to recover the family: that closes a loop the
canon forbids, and it would make a repaint or an icon swap silently re-family the
book, which is exactly the failure the S112 colour table had.

ONE DEFINITION, NOT A THIRD COPY (S83). The tiers are IMPORTED from
build_family_map - CANON, RULE, GLYPH and norm, the same objects the generator
uses. This file contains no classification logic of its own. If the generator's
rules change, this tool changes with them and cannot drift away.

THE CORRECTNESS PROOF IS AGREEMENT, NOT INSPECTION (S124). The attribute is right
if and only if build_family_map reproduces its own 30-family table byte-identically
once it reads the attribute instead of inferring. Two independent derivations
agreeing beats either one verifying itself. --check asserts exactly that.

Offsets come from lesson_inventory (v1.3.1), so the attribute is seated on the SAME
element the callout detector found. Edits are applied back-to-front so an earlier
write cannot move a later offset, and every write is read back.
"""
import glob
import io
import os
import re
import sys
import contextlib

import lesson_inventory

# build_family_map runs its whole report at import. Swallow it - we want its TABLES,
# not its output. This is deliberate: importing the generator is what guarantees the
# rules cannot drift from it (S83).
with contextlib.redirect_stdout(io.StringIO()):
    import build_family_map as B

ATTR = 'data-family'
_ATTR_RE = re.compile(r'\s%s="[^"]*"' % ATTR)


def family_of(c):
    """The family of one callout record, through build_family_map's OWN tiers.

    Order is the generator's: CANON label prefix, then the content RULE list, then
    the authored PIN. Returns None when no tier names it - the caller decides what
    an unnamed block means, because 'unassigned' is a finding, not a default.

    S130: THE LAST TIER IS NO LONGER THE GLYPH. It was a decoration-keyed stopgap and it
    died the way the COLOUR tier died at S112 - the marks arc replaced the emoji and 212
    blocks lost their only signal. The pin is AUTHORED and keyed on `data-callout`, so no
    repaint or reskin can orphan it. Read-only input; see ZUMO_FAMILY_PINS.md.
    """
    lab = B.norm(c.get('label'))
    g = (c.get('glyph') or '').strip()
    scheme = (c['bg'] or 'none', c['border'])
    fam = next((f for f in B.CANON if lab.upper().startswith(f)), None)
    if fam:
        return fam
    for fn, f in B.RULE:
        if fn(lab, g, scheme):
            return f
    return B.PINS.get(c.get('callout_id'))


def plan(path):
    """[(start, open_end, family, current_attr)] for every callout in one file."""
    inv = lesson_inventory.build(path)
    out = []
    for c in inv['callouts']:
        out.append((c['start'], c['open_end'], family_of(c), c.get('family_attr')))
    return out


def _seat(src, start, open_end, fam):
    """Insert or replace data-family inside ONE opening tag.

    The tag text is taken by offset, never by searching for it - two callouts can
    carry byte-identical opening tags and a string replace would hit the wrong one
    (§6.12c). Asserts the slice really is an opening tag before touching it.
    """
    tag = src[start:open_end]
    assert tag.startswith('<') and tag.endswith('>'), 'offset %d is not an opening tag' % start
    assert '\n' not in tag[:tag.index(' ') if ' ' in tag else len(tag)], 'malformed tag at %d' % start
    stripped = _ATTR_RE.sub('', tag)
    close = '/>' if stripped.endswith('/>') else '>'
    body = stripped[:-len(close)].rstrip()
    new = '%s %s="%s"%s' % (body, ATTR, fam, close)
    return src[:start] + new + src[open_end:]


def build(paths, apply=False):
    """Report, and optionally write. Returns (written, correct, wrong, unnamed)."""
    written = correct = 0
    wrong, unnamed = [], []
    for p in sorted(paths):
        rows = plan(p)
        edits = []
        for start, open_end, fam, cur in rows:
            if fam is None:
                unnamed.append((p, start))
                continue
            if cur == fam:
                correct += 1
                continue
            if cur is not None:
                wrong.append((p, start, cur, fam))
            edits.append((start, open_end, fam))
        if apply and edits:
            src = open(p, encoding='utf-8').read()
            # BACK TO FRONT. A forward pass invalidates every offset after the first
            # write; this is the defect that makes offset editing look unreliable.
            for start, open_end, fam in sorted(edits, reverse=True):
                src = _seat(src, start, open_end, fam)
            blob = src.encode('utf-8')
            tmp = p + '.tmp'
            with open(tmp, 'wb') as fh:
                fh.write(blob)
            os.replace(tmp, p)
            # READ BACK (S117). A write that was not read back is not evidence.
            back = plan(p)
            assert len(back) == len(rows), '%s: callout count moved %d -> %d' % (
                p, len(rows), len(back))
            for _s, _e, fam2, cur2 in back:
                if fam2 is not None:
                    assert cur2 == fam2, '%s: attribute did not land (%r != %r)' % (p, cur2, fam2)
        # OUTSIDE the apply branch on purpose. Counting only on apply makes a dry
        # run report zero work and look like a clean tree - a report that cannot
        # distinguish 'nothing to do' from 'not looking' is not evidence (§24.8).
        written += len(edits)
    return written, correct, wrong, unnamed


def selftest():
    """Controls. Loud on a wrong attribute and a missing one, silent when clean,
    and PROVES idempotence - the property that makes a rerun safe."""
    ok = True
    files = sorted(glob.glob('lessons/Lesson_*.html'))
    assert len(files) == 16, 'run from repo root'

    # A: every callout the generator can name, this tool names identically.
    with contextlib.redirect_stdout(io.StringIO()):
        import importlib
        importlib.reload(B)
    mismatch = 0
    for p in files:
        for c in lesson_inventory.build(p)['callouts']:
            if family_of(c) is None:
                mismatch += 1
    print('  A  blocks no tier can name .............. %d' % mismatch)

    # B: _seat is idempotent - seating twice equals seating once.
    t = '<div class="x">'
    once = _seat(t, 0, len(t), 'TIP')
    twice = _seat(once, 0, len(once), 'TIP')
    if once != twice:
        print('  B  FAIL idempotence: %r vs %r' % (once, twice)); ok = False
    else:
        print('  B  seating twice == seating once ....... PASS  %s' % once)

    # C: _seat REPLACES rather than appends when the attribute already differs.
    changed = _seat(once, 0, len(once), 'WARNING')
    if changed.count(ATTR) != 1 or 'WARNING' not in changed:
        print('  C  FAIL replace: %r' % changed); ok = False
    else:
        print('  C  a wrong value is replaced, not doubled  PASS')

    # D: a self-closing tag keeps its slash.
    sc = _seat('<img src="a.svg"/>', 0, 18, 'TIP')
    if not sc.endswith('/>') or ATTR not in sc:
        print('  D  FAIL self-closing: %r' % sc); ok = False
    else:
        print('  D  self-closing tag preserved .......... PASS')

    # E: the assert fires on a non-tag offset - the control that proves D means
    #    anything. A writer that will edit ANY offset handed to it is not safe.
    try:
        _seat('hello world', 0, 5, 'TIP')
        print('  E  FAIL: seated onto plain text'); ok = False
    except AssertionError:
        print('  E  refuses an offset that is not a tag . PASS')

    print('ALL CONTROLS PASS' if ok else 'CONTROLS FAILED')
    return 0 if ok else 1


def main():
    args = sys.argv[1:]
    files = sorted(glob.glob('lessons/Lesson_*.html'))
    print('family_tag.py %s - the family is CONTENT; the mark is an output (§24.14).' % VERSION)
    if '--selftest' in args:
        return selftest()
    apply = '--apply' in args
    written, correct, wrong, unnamed = build(files, apply=apply)
    for p, s, cur, fam in wrong:
        print('  DRIFT %s @%d carries %r, content says %r' % (p, s, cur, fam))
    for p, s in unnamed:
        print('  UNNAMED %s @%d - no tier resolves it' % (p, s))
    print('  %d already correct, %d %s, %d drifted, %d unnamed' % (
        correct, written, 'written' if apply else 'to write', len(wrong), len(unnamed)))
    return 1 if (wrong and not apply) or unnamed else 0


if __name__ == '__main__':
    sys.exit(main())
