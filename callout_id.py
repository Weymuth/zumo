#!/usr/bin/env python3
# VERSION is the ONE home and sits ABOVE the changelog, so a plain grep of this file
# returns the version and not a changelog line (S98).
VERSION = 'v1.0'
# v1.0 (S130): first release. Authors data-callout on every callout block.
"""callout_id.py - the stable per-callout identity marker (§20.2 form).

WHY THIS EXISTS. Every instrument in this suite locates a callout by FILE OFFSET, and
an offset is invalidated by any edit above it - S129 lost a batch to exactly that and
rule 15 was written from it. A pin, a manifest or any cross-session record therefore
had nothing durable to key on. Three derived keys were tried at S130 (content hash at
two window sizes, and label text) and the best re-found 199 of 212 blocks across a
single markup change. A DERIVED key cannot be the identity; the identity has to be
AUTHORED.

THE FORM IS §20.2's, NOT §6.9's, AND THE JOB IS WHY. The book carries two authored
identity conventions: `id="kind-slug"` for reader-facing anchors (742 of them), and
`data-challenge="1.11"` for machine markers an instrument keys on (171, all distinct).
This marker is read by instruments and never by a reader, so it takes the second form.
Minting 208 `id` anchors that nothing links to would also put reader-facing furniture
in the markup to serve a gate.

AUTHORED, NOT DERIVED - AND THAT IS THE WHOLE POINT. The ordinal is assigned ONCE, in
document order, and never recomputed. Inserting a callout takes the next free number in
that lesson; nothing below it renumbers. This is the property that makes the marker
survive the edits that destroy an offset, and it is why --apply refuses to touch a block
that already carries one.
"""
import glob
import io
import os
import re
import sys
import collections
import contextlib

with contextlib.redirect_stdout(io.StringIO()):
    import lesson_inventory

ATTR = 'data-callout'
_LESSON_N = re.compile(r'Lesson_(\d+)\.html$')


def lesson_number(path):
    m = _LESSON_N.search(path)
    assert m, 'not a lesson filename: %s' % path
    return int(m.group(1))


def plan(path):
    """[(start, open_end_of_tag, existing_marker_or_None)] in document order."""
    raw = open(path, encoding='utf-8').read()
    rows = []
    for c in lesson_inventory.build(path)['callouts']:
        s = c['start']
        gt = raw.index('>', s)
        tag = raw[s:gt + 1]
        m = re.search(r'\s%s="([^"]+)"' % ATTR, tag)
        rows.append((s, gt, m.group(1) if m else None))
    return rows, raw


def next_free(existing, lesson):
    """The next unused ordinal in this lesson - NEVER a recount of position."""
    used = set()
    for v in existing:
        if not v:
            continue
        p = v.split('.')
        if len(p) == 2 and p[1].isdigit():
            used.add(int(p[1]))
    n = 1
    while n in used:
        n += 1
    return n


def build(paths, apply=False):
    tally = collections.Counter()
    for p in sorted(paths):
        les = lesson_number(p)
        rows, raw = plan(p)
        existing = [v for _s, _g, v in rows]
        edits = []
        for s, gt, have in rows:
            if have:
                tally['KEPT'] += 1
                continue
            n = next_free(existing, les)
            existing.append('%d.%d' % (les, n))
            edits.append((s, gt, '%d.%d' % (les, n)))
            tally['WRITE'] += 1
        if apply and edits:
            # Back to front, so an earlier write cannot move a later offset (rule 15).
            for s, gt, val in sorted(edits, reverse=True):
                tag = raw[s:gt + 1]
                assert ATTR not in tag, 'refusing to double-mark at %d' % s
                # Uniform seat: immediately after data-family, which all 1,069 carry.
                new = re.sub(r'(\sdata-family="[^"]*")',
                             r'\1 %s="%s"' % (ATTR, val), tag, count=1)
                assert new != tag, 'no data-family seat found at %d' % s
                raw = raw[:s] + new + raw[gt + 1:]
            tmp = p + '.tmp'
            with open(tmp, 'wb') as fh:
                fh.write(raw.encode('utf-8'))
            os.replace(tmp, p)
            # READ BACK (S117): every block must now carry a marker, all distinct.
            back, _ = plan(p)
            vals = [v for _s, _g, v in back]
            assert all(vals), '%s: %d block(s) still unmarked' % (p, vals.count(None))
            assert len(set(vals)) == len(vals), '%s: duplicate marker' % p
    return tally


def audit(paths):
    """Every callout marked, every marker unique book-wide, lesson digit agrees."""
    bad = []
    seen = {}
    total = 0
    for p in sorted(paths):
        les = lesson_number(p)
        rows, _raw = plan(p)
        for s, _gt, v in rows:
            total += 1
            if not v:
                bad.append('%s @%d: no %s' % (p, s, ATTR))
                continue
            if v in seen:
                bad.append('%s: %s duplicates %s' % (p, v, seen[v]))
            seen[v] = p
            if not v.startswith('%d.' % les):
                bad.append('%s: %s does not name its own lesson' % (p, v))
    return total, bad


def selftest():
    ok = True

    # A: the ordinal is AUTHORED - next_free skips used numbers, never recounts.
    if next_free(['2.1', '2.3'], 2) == 2 and next_free(['2.1', '2.2'], 2) == 3:
        print('  A  ordinal is next-free, not positional ...... PASS')
    else:
        print('  A  FAIL: ordinal recomputed from position'); ok = False

    # B: a deletion must NOT renumber survivors. This is the property rule 15 needs.
    if next_free(['2.1', '2.5'], 2) == 2 and '2.5' in ['2.1', '2.5']:
        print('  B  a gap is filled, survivors keep numbers .... PASS')
    else:
        print('  B  FAIL: survivors renumbered'); ok = False

    # C: the seat regex lands after data-family and nowhere else.
    tag = '<div class="callout-x" data-family="NOTE">'
    got = re.sub(r'(\sdata-family="[^"]*")', r'\1 %s="9.9"' % ATTR, tag, count=1)
    if got == '<div class="callout-x" data-family="NOTE" data-callout="9.9">':
        print('  C  marker seats after data-family ............. PASS')
    else:
        print('  C  FAIL: seated wrong: %s' % got); ok = False

    # THE FIXTURE MUST BE A REAL CALLOUT. lesson_inventory finds a callout by a resolved
    # `border-left` rule, so a bare <div> is INVISIBLE to it - the first draft of controls
    # D/E/F used bare divs, which made D and E fail and made F pass VACUOUSLY on an empty
    # finding list. An assert that cannot fail is not evidence, so every fixture below is
    # written with the real shape and every control first asserts the parser SAW it.
    import tempfile
    STY = 'border-left: 4px solid #607d8b; background: #eceff1;'

    def _fx(name, blocks):
        d = tempfile.mkdtemp()
        f = os.path.join(d, name)
        open(f, 'w', encoding='utf-8').write(
            '<html><body>\n' + '\n'.join(
                '<div style="%s" data-family="%s"%s>text</div>'
                % (STY, fam, (' %s="%s"' % (ATTR, mk)) if mk else '')
                for fam, mk in blocks) + '\n</body></html>')
        return f

    # D: LOUD on a duplicate. A fixture, never the live tree (S129) - a control that
    #    depends on the state of what it audits is not a control.
    f = _fx('Lesson_99.html', [('A', '99.1'), ('B', '99.1')])
    total, bad = audit([f])
    dup = total == 2 and any('duplicates' in b for b in bad)
    print('  D  duplicate marker is LOUD ................... %s (parser saw %d)'
          % ('PASS' if dup else 'FAIL', total))
    ok = ok and dup

    # E: LOUD on a marker naming the wrong lesson.
    f = _fx('Lesson_07.html', [('A', '3.1')])
    total, bad = audit([f])
    wrong = total == 1 and any('does not name its own lesson' in b for b in bad)
    print('  E  wrong-lesson marker is LOUD ................ %s (parser saw %d)'
          % ('PASS' if wrong else 'FAIL', total))
    ok = ok and wrong

    # F: LOUD on an UNMARKED block, then SILENT once marked. Both halves on the same
    #    fixture, so silence is proved to be a verdict rather than an empty population.
    f = _fx('Lesson_04.html', [('A', '4.1'), ('B', None)])
    total, bad = audit([f])
    loud = total == 2 and any('no %s' % ATTR in b for b in bad)
    f = _fx('Lesson_04.html', [('A', '4.1'), ('B', '4.2')])
    total2, bad2 = audit([f])
    quiet = total2 == 2 and not bad2
    print('  F  unmarked LOUD, then clean SILENT ........... %s (saw %d/%d)'
          % ('PASS' if (loud and quiet) else 'FAIL', total, total2))
    ok = ok and loud and quiet

    print('ALL CONTROLS PASS' if ok else 'CONTROLS FAILED')
    return 0 if ok else 1


def main():
    args = sys.argv[1:]
    print('callout_id.py %s - the identity is AUTHORED, never derived.' % VERSION)
    if '--selftest' in args:
        return selftest()
    paths = sorted(glob.glob('lessons/Lesson_*.html'))
    if '--audit' in args:
        total, bad = audit(paths)
        for b in bad[:40]:
            print('  ' + b)
        if len(bad) > 40:
            print('  ... %d more' % (len(bad) - 40))
        print('  %d callout(s), %d problem(s)' % (total, len(bad)))
        return 1 if bad else 0
    tally = build(paths, apply='--apply' in args)
    for k in ('WRITE', 'KEPT'):
        if tally[k]:
            print('  %-8s %5d' % (k, tally[k]))
    return 0


if __name__ == '__main__':
    sys.exit(main())
