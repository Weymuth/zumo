#!/usr/bin/env python3
# VERSION is the ONE home and sits ABOVE the changelog, so a plain grep of this file
# returns the version and not a changelog line (S98).
VERSION = 'v1.1.0'
# v1.1.0 (S191): THE INSTRUMENT BUILT TO STOP A CONFIDENT WRONG NUMBER PRODUCED ONE.
#   `occurrences('lastPosition', 'lessons/Lesson_*.html')` returned `0 MATCHES` and
#   printed its population like any honest answer. A STRING is iterable, so
#   `for p in sorted(paths)` walked 24 single CHARACTERS, every open() raised, the
#   `except: continue` swallowed all 24, and the empty result was reported as a
#   measurement. The true figure was 6 lines in L08 and 1 in L10, and the row being
#   priced on that zero was L08-06. This is WORSE than `grep -c`: grep would have
#   said "No such file". Two changes, and the second is the load-bearing one:
#   a string argument is now a GLOB, and an UNREADABLE PATH RAISES. Silence about a
#   source you could not read is the entire failure class this file exists to close.
#   Caught by rules 83/84 - grep and census disagreed on an unrelated pattern.
# v1.0.1 (S190): CONTROL C asserted a SIDE EFFECT rather than the property. It did
#   `['x'][pop]` and caught TypeError; plant a working __index__ and that raises
#   IndexError instead, which the harness did not catch, so the selftest CRASHED and
#   read as silence to a caller checking stdout. Now asks operator.index() directly and
#   treats ANY other exception as a failure. Caught by a plant during S190's own
#   re-verification - rule 59 inside the instrument written to enforce rule 59.
# v1.0 (S190): first release. Built after DJ counted the recurrences: "WHY ARE WE STILL
#   USING GREP". A structural parse of the Bible changelog returns THIRTEEN prior entries
#   recording this same defect (v8.78/S91 through v8.184/S189); S190's `42 bank questions`
#   is the fourteenth. §24.22 ruled it at S182 and §24.22a at S186, and neither stopped it,
#   because BOTH ARE OPERATOR RULES WITH NO INSTRUMENT. Every rule in this project that
#   stuck got a comparator; this one got a paragraph. v8.139 already said it: "Writing the
#   rule down did not prevent committing it in the session that quoted it. The detector did."
"""census.py - THE ONE PLACE A COUNT COMES FROM.

WHY THIS EXISTS. The recurring defect is never "somebody used grep". It is
`grep -c` returning MATCHING LINES and that number being reported as a count of
something else - defects, questions, sites, payloads. S155 reported 13/8/1 as
occurrences when they were lines (true figures 15/10/2). S190 reported `extern`
in "42 bank questions" when 42 is occurrences across five files and the question
count is 27. Same shape, 35 sessions apart.

THE DEFINING PROPERTY, AND IT IS THE WHOLE DESIGN: NOTHING HERE RETURNS A BARE
INTEGER. Every function returns a Population, which carries its members and
REFUSES to be used as a number. `len(pop)` works; `int(pop)` raises; printing it
names what it counted and how. So the failure mode - obtaining a number while
meaning a different population - is not forbidden, it is UNAVAILABLE.

That is §25.2a ("name them, do not count them") expressed as a type rather than
as advice, and rule 20's discipline applied to ourselves: a rule that relies on
remembering is a rule that decays.

SCOPE LIMIT, STATED (rule 78). This cannot see a terminal. Nothing stops anyone
typing `grep -c` at a shell and pasting the answer into chat; §24.16 records the
same hole for checksums. What it does is make the CORRECT call the cheap one and
put the members in front of you when you make it. It closes the path, not the class.

THIS IS A LIBRARY AND IT DOES NOT EXIT. Nothing at import time may call
sys.exit(); other instruments import it. Run it directly for `--selftest`.
"""

import glob
import io
import os
import re
import sys
import contextlib

try:
    import yaml
except ImportError:                                     # pragma: no cover
    yaml = None


class Population:
    """A counted thing that knows WHAT it counted and refuses to be a bare number.

    `int(pop)` raises on purpose. A caller who wants a figure must go through
    `len()`, which reads as a count of MEMBERS, or `.report()`, which prints the
    members beside it. The point is that you cannot obtain the number without
    having named the population it belongs to."""

    __slots__ = ('kind', 'members', 'note')

    def __init__(self, kind, members, note=''):
        self.kind = kind                       # what a member IS, in words
        self.members = list(members)
        self.note = note

    def __len__(self):
        return len(self.members)

    def __iter__(self):
        return iter(self.members)

    def __int__(self):
        raise TypeError(
            'census: refusing to hand back a bare integer for %r. A number with no '
            'population is how a LINE count gets reported as a DEFECT count '
            '(\u00a716.15). Use len(), or .report() to see the members.' % self.kind)

    __index__ = __int__

    def __repr__(self):
        return '<Population %d %s>' % (len(self.members), self.kind)

    def report(self, limit=12):
        out = ['%d %s%s' % (len(self.members), self.kind, (' - ' + self.note) if self.note else '')]
        for m in self.members[:limit]:
            out.append('    %s' % (m,))
        if len(self.members) > limit:
            out.append('    ... and %d more' % (len(self.members) - limit))
        return '\n'.join(out)


# ---------------------------------------------------------------------------
# TEXT: the two things `grep -c` conflates, as SEPARATE calls.
# You cannot get one while meaning the other, because you have to name which.
# ---------------------------------------------------------------------------
def _paths(paths):
    """Resolve `paths` to a concrete, READABLE file list, or RAISE.

    Two failure modes, both of which returned a silent zero before v1.1.0:

    A STRING IS A GLOB, NOT AN ITERABLE OF CHARACTERS. `sorted('a*.html')` is a
    list of characters, every one of which fails to open. S191 read that as
    `0 MATCHES` and nearly priced an edit on it.

    A PATH THAT CANNOT BE READ IS NOT A ZERO. It is an unknown, and an unknown
    reported as a measurement is the defect this whole file exists to prevent
    (rule 59: a control that stays quiet for the wrong reason is not a control).
    """
    if isinstance(paths, str):
        hits = sorted(glob.glob(paths))
        if not hits:
            raise ValueError(
                'census: %r matched no files. A pattern with no source is not a '
                'population of zero.' % paths)
        return hits
    hits = sorted(paths)
    if not hits:
        raise ValueError('census: empty path list - name the files you mean.')
    return hits


def _read(p):
    """Read one path. Unreadable RAISES; it is never skipped."""
    try:
        return open(p, encoding='utf-8').read()
    except (OSError, UnicodeDecodeError) as e:
        raise ValueError('census: cannot read %r (%s). A source you could not '
                         'read is not zero matches.' % (p, e.__class__.__name__))


def lines(pattern, paths, flags=0):
    """Every LINE matching `pattern`. This is what `grep -c` returns."""
    rx = re.compile(pattern, flags)
    out = []
    for p in _paths(paths):
        txt = _read(p)
        for n, ln in enumerate(txt.split('\n'), 1):
            if rx.search(ln):
                out.append('%s:%d' % (p, n))
    return Population('matching LINES', out, 'pattern %r' % pattern)


def occurrences(pattern, paths, flags=0):
    """Every MATCH of `pattern`. A line holding three matches contributes three."""
    rx = re.compile(pattern, flags)
    out = []
    for p in _paths(paths):
        txt = _read(p)
        for m in rx.finditer(txt):
            out.append('%s@%d' % (p, txt[:m.start()].count('\n') + 1))
    return Population('MATCHES', out, 'pattern %r' % pattern)


def rendered(pattern, paths, flags=0):
    """Matches in RENDERED text: tags stripped, entities resolved. A phrase broken
    across an inline element is invisible to a raw match - S162 lost a retired
    claim that way, split across <em> tags."""
    import html as _html
    rx = re.compile(pattern, flags)
    out = []
    for p in _paths(paths):
        raw = _read(p)
        txt = _html.unescape(re.sub(r'<[^>]+>', ' ', raw))
        out.extend('%s#%d' % (p, i) for i, _ in enumerate(rx.finditer(txt), 1))
    return Population('MATCHES in rendered text', out, 'pattern %r' % pattern)


# ---------------------------------------------------------------------------
# STRUCTURE: populations a text match cannot name at all.
# ---------------------------------------------------------------------------
def questions(pattern, bank_glob='quizzes/ZUMO_QUIZ_L*.yaml', assertive_only=False, flags=0):
    """QUESTIONS whose text matches. Returns question IDS, never lines.

    `assertive_only` narrows to what a question ASSERTS - a `#` comment is
    provenance and a declared-wrong option is the trap being taught, so neither
    claims anything (retired_claims' structural exemption, rule 20)."""
    if yaml is None:
        return Population('QUESTIONS', [], 'PyYAML absent - cannot parse')
    rx = re.compile(pattern, flags)
    text_of = None
    if assertive_only:
        with contextlib.redirect_stdout(io.StringIO()):
            import retired_claims as _RC
        text_of = _RC.assert_true_text

    def walk(o):
        if isinstance(o, dict):
            if 'stem' in o:
                yield o
            for v in o.values():
                yield from walk(v)
        elif isinstance(o, list):
            for v in o:
                yield from walk(v)

    out = []
    for f in sorted(glob.glob(bank_glob)):
        try:
            doc = yaml.safe_load(open(f, encoding='utf-8'))
        except Exception:
            continue
        for q in walk(doc):
            blob = text_of(q) if text_of else str(q)
            if rx.search(blob):
                out.append(q.get('id') or ('%s:<unnamed>' % os.path.basename(f)))
    return Population('QUESTIONS', out,
                      'assertive register only' if assertive_only else 'whole question')


def payloads(token, maker='newproject.html', filename=None, flags=0):
    """MAKER PAYLOAD ENTRIES containing `token`. One entry per stored file, so a
    token appearing eight times inside one payload counts ONCE - which is the
    figure that means anything when pricing an edit (rule 70)."""
    try:
        mk = open(maker, encoding='utf-8').read()
    except OSError:
        return Population('PAYLOAD ENTRIES', [], 'maker unreadable')
    fn = re.escape(filename) if filename else r'[A-Za-z0-9_.]+'
    rx = re.compile(r'"(%s)"\s*:\s*"(?:[^"\\]|\\.)*?%s' % (fn, token), flags)
    out = ['%s@%d' % (m.group(1), mk[:m.start()].count('\n') + 1) for m in rx.finditer(mk)]
    return Population('PAYLOAD ENTRIES', out,
                      'file %s, token %r' % (filename or '<any>', token))


def callouts(lesson_glob='lessons/Lesson_*.html'):
    """CALLOUT BLOCKS, via lesson_inventory - the authored identity, not a regex."""
    with contextlib.redirect_stdout(io.StringIO()):
        import lesson_inventory as _LI
    out = []
    for f in sorted(glob.glob(lesson_glob)):
        for c in _LI.build(f)['callouts']:
            out.append('%s@%s' % (os.path.basename(f), c.get('line')))
    return Population('CALLOUT BLOCKS', out, 'via lesson_inventory')


def agree(*pops):
    """Rules 83/84 for counting: two structurally different routes to one figure.
    Returns (bool, report). Disagreement is the finding, never the average."""
    sizes = [len(p) for p in pops]
    ok = len(set(sizes)) == 1
    rep = ' | '.join('%d %s' % (len(p), p.kind) for p in pops)
    return ok, ('AGREE: ' if ok else 'DISAGREE: ') + rep


# ---------------------------------------------------------------------------
def _selftest():
    import tempfile
    fails = []

    def chk(name, cond, detail=''):
        print('  %-58s %s' % (name, 'PASS' if cond else 'FAIL ' + detail))
        if not cond:
            fails.append(name)

    d = tempfile.mkdtemp()
    f = os.path.join(d, 'a.txt')
    open(f, 'w').write('extern extern extern\nnothing\nextern\n')

    # CONTROL A - the defect itself: lines and occurrences MUST differ, and the
    # API makes you say which one you meant.
    ln, oc = lines('extern', [f]), occurrences('extern', [f])
    chk('A  lines(2) != occurrences(4) on the same pattern',
        len(ln) == 2 and len(oc) == 4, '(%d, %d)' % (len(ln), len(oc)))

    # CONTROL B - a Population REFUSES to be a bare integer. This is the whole design.
    try:
        int(oc)
        chk('B  int(Population) raises', False, '(it returned a number)')
    except TypeError:
        chk('B  int(Population) raises', True)

    # CONTROL C - and it refuses in the sneaky places too (indexing, %d).
    # ASKS THE PREDICATE DIRECTLY. The first draft did `['x'][oc]`, which raises
    # IndexError once __index__ starts working - a DIFFERENT exception the harness
    # did not catch, so the selftest CRASHED and a caller grepping stdout for
    # 'FAILED' read the crash as silence. Found by planting a working __index__
    # during S190's re-verification: rule 59, inside the instrument built to
    # enforce rule 59. A control must assert the property, not a side effect of it.
    import operator as _op
    try:
        _op.index(oc)
        chk('C  Population refuses __index__', False, '(it yielded an index)')
    except TypeError:
        chk('C  Population refuses __index__', True)
    except Exception as _e:                      # any other exception is ALSO a fail
        chk('C  Population refuses __index__', False, '(raised %s)' % type(_e).__name__)

    # CONTROL D - len() works, so a caller who names the population gets a figure.
    chk('D  len(Population) works', len(oc) == 4)

    # CONTROL E - members are NAMED, not just counted (§25.2a).
    chk('E  report() names members', 'a.txt' in oc.report())

    # CONTROL F - BLINDING: a pattern that is absent returns an EMPTY population
    # rather than raising or guessing.
    chk('F  BLINDING absent pattern -> empty, not error',
        len(occurrences('zzznotpresent', [f])) == 0)

    # CONTROL G - rendered() sees a phrase split across an inline element, which a
    # raw match cannot (S162's <em>-split retired claim).
    h = os.path.join(d, 'b.html')
    open(h, 'w').write('<p>measures <em>intent</em>, not result</p>')
    chk('G  rendered() sees a tag-split phrase raw text cannot',
        len(occurrences(r'intent, not result', [h])) == 0 and
        len(rendered(r'intent\s*, not result', [h])) == 1)

    # CONTROL H - agree() reports DISAGREEMENT rather than picking a winner.
    ok, rep = agree(ln, oc)
    chk('H  agree() flags a disagreement', (not ok) and 'DISAGREE' in rep)
    ok2, _ = agree(oc, occurrences('extern', [f]))
    chk('H2 agree() confirms a real agreement', ok2)

    # CONTROL I - the live defect, reproduced: `extern` in the banks is 42
    # occurrences and 27 QUESTIONS. If this ever agrees, one of them is broken.
    if yaml is not None and glob.glob('quizzes/ZUMO_QUIZ_L*.yaml'):
        occ = occurrences('extern', glob.glob('quizzes/ZUMO_QUIZ_L*.yaml'))
        qs = questions('extern')
        chk('I  live: occurrences(42) != questions(27) - the S190 defect',
            len(occ) == 42 and len(qs) == 27, '(%d, %d)' % (len(occ), len(qs)))
    else:
        print('  I  live bank check skipped (no banks / no PyYAML)')

    # CONTROL J - payloads() counts ENTRIES, not raw tokens. 326 raw `followLine`
    # tokens live in 135 main.cpp payloads; the second is the number that prices work.
    if os.path.exists('newproject.html'):
        pe = payloads('followLine', filename='main.cpp')
        raw = occurrences('followLine', ['newproject.html'])
        chk('J  payload ENTRIES(135) != raw tokens(326)',
            len(pe) == 135 and len(raw) == 326, '(%d, %d)' % (len(pe), len(raw)))
    else:
        print('  J  payload check skipped (no newproject.html)')

    # CONTROL K - THE v1.1.0 DEFECT, BOTH DIRECTIONS. A string is a GLOB. Before
    # v1.1.0 `sorted('lessons/Lesson_*.html')` walked 24 CHARACTERS, every open()
    # failed, `except: continue` ate all 24, and the call reported `0 MATCHES`.
    # K1 is the positive direction: the glob must find what the explicit list finds.
    open(os.path.join(d, 'b.txt'), 'w').write('extern\n')
    g = occurrences('extern', os.path.join(d, '*.txt'))
    e = occurrences('extern', [f, os.path.join(d, 'b.txt')])
    chk('K1 a string path is a GLOB, agreeing with the explicit list',
        len(g) == len(e) == 5, '(%d, %d)' % (len(g), len(e)))

    # K2 - the NEGATIVE direction, and the load-bearing one. An unreadable path must
    # RAISE. A source you could not read is an unknown; reporting it as zero is the
    # whole failure class. This control FAILS against v1.0.1 by construction.
    try:
        r = occurrences('extern', [os.path.join(d, 'does_not_exist.txt')])
        chk('K2 an unreadable path RAISES, it is not a silent zero', False,
            '(returned %d)' % len(r))
    except ValueError:
        chk('K2 an unreadable path RAISES, it is not a silent zero', True)
    except Exception as _e:
        chk('K2 an unreadable path RAISES, it is not a silent zero', False,
            '(raised %s, wanted ValueError)' % type(_e).__name__)

    # K3 - a glob matching nothing is the same unknown wearing a different hat.
    try:
        r = lines('extern', os.path.join(d, 'no_such_*.zzz'))
        chk('K3 a glob matching nothing RAISES', False, '(returned %d)' % len(r))
    except ValueError:
        chk('K3 a glob matching nothing RAISES', True)

    print()
    print('  %s' % ('ALL CONTROLS PASS' if not fails else 'FAILED: ' + ', '.join(fails)))
    return 1 if fails else 0


if __name__ == '__main__':
    print('census.py %s - a count comes with its population or it does not come.' % VERSION)
    if '--selftest' in sys.argv:
        sys.exit(_selftest())
    print('  usage: import census; census.questions("extern").report()')
    print('  run --selftest for the controls')
