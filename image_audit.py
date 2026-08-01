#!/usr/bin/env python3
"""image_audit.py - what visual assets does the book still need?

WHY THIS EXISTS. `IMAGE_SHOT_LIST.md` went stale because it was hand-maintained, and the
fallback - "each lesson's Image Index Status column is the record" - does not survive a read:
the index table ships in FIVE different schemas across the sixteen lessons and only ten of them
carry a Status column at all. A record that exists in six lessons and not the other ten is not
a record. §24.12: this emits a generated artefact, never hand-edited.

WHAT IT MEASURES, and it is deliberately not the status column. A figure is PLANNED when the
lesson prints its tag - [IMAGE 4.3], [GRAPHIC 1.10], [VIDEO 3.1]. It is LANDED when an <img>
in that lesson points at a file whose name encodes the same tag. Everything planned and not
landed is outstanding. That question is schema-independent, so it can be asked of all sixteen
lessons the same way.

TWO TRAPS, BOTH HIT WHILE WRITING THIS, BOTH RECORDED SO THE NEXT READER DOES NOT REPEAT THEM:

  1. THE TAG'S LESSON NUMBER IS NOT THE HOST LESSON'S. L07 prints [GRAPHIC 6.11], which is
     L06's figure quoted in a later lesson. Keying the expected filename off the FILE gave a
     phantom "L07 GRAPHIC 6.11 outstanding". Key off the TAG.

  2. IMAGE AND GRAPHIC ARE SEPARATE NUMBER SPACES (§10), SO A GRAPHIC WITH THE SAME
     NUMBER IS NOT THE MISSING IMAGE. A first draft reported ten "type mismatches" - tag says
     IMAGE, a GRAPHIC file with that number exists - which looked like the defect just fixed in
     L15. Reading all ten killed every one: [IMAGE 13.1] wants a photo of the rescue space and
     L13_GRAPHIC_13-01 is a lawnmower-sweep diagram. L04 says so IN THE LESSON: "[IMAGE 4.1]
     and [GRAPHIC 4.1] are two different figures, by design." A cross-space match is therefore
     NOT evidence of anything and this tool does not report one. §24.6c: the count was
     plausible, well-formed and wrong, and only a read could tell.

usage:
  python3 image_audit.py              # write IMAGE_WORKLIST.md
  python3 image_audit.py --check      # compare to disk, write nothing
  python3 image_audit.py --selftest   # controls, both directions
exit 0 = clean. exit 1 = a control failed or --check found a difference.
"""
import re, os, sys, glob, collections

VERSION = 'v1.1'          # the only version home in this file (S104)
OUT = 'IMAGE_WORKLIST.md'

TAG_RE = re.compile(r'\[(IMAGE|GRAPHIC|VIDEO)\s+(\d+)\.(\d+)([a-z]?)\]')
SRC_RE = re.compile(r'<img[^>]+src="[^"]*/images/([^"?#]+)"')
IMG_ANY = re.compile(r'<img[^>]+src="[^"]*/images/([^"?#]+)"')


def lessons():
    return sorted(glob.glob('lessons/Lesson_*.html'))


def expected(kind, a, b, suf):
    """The filename prefix a tag's own asset must carry. Zero-padded second number, matching
    the live convention (L01_GRAPHIC_1-10_, L15_GRAPHIC_15-01_)."""
    return re.compile(rf'^L{a:02d}_{kind}_{a}-0*{b}{suf}_', re.I)


def audit(paths=None):
    """ENTRYPOINT. -> (planned, outstanding, orphans, dupes) with no side effects."""
    paths = paths or lessons()
    on_disk = sorted(os.path.basename(p) for p in glob.glob('images/*.*'))
    planned, outstanding, referenced = [], [], set()
    for f in paths:
        host = os.path.basename(f)[7:9]
        src = open(f, encoding='utf-8', errors='replace').read()
        refs = set(SRC_RE.findall(src))
        referenced |= refs
        # KIND IS PART OF THE SORT KEY, and leaving it out cost a real defect: [IMAGE 4.1]
        # and [VIDEO 4.1] share the key (4, 1, ''), so their order fell out of SET iteration
        # and flipped between processes. The written file and the next --check disagreed at
        # random. CONTROL E had "proved" determinism by auditing twice in ONE process, where
        # the hash seed is fixed - a check that could not distinguish the two answers (§24.8).
        seen = sorted({(m.group(1), int(m.group(2)), int(m.group(3)), m.group(4))
                       for m in TAG_RE.finditer(src)},
                      key=lambda t: (t[1], t[2], t[3], t[0]))
        for kind, a, b, suf in seen:
            tag = f'{kind} {a}.{b}{suf}'
            planned.append((host, tag))
            if kind == 'VIDEO':                       # no <img> can satisfy a video
                outstanding.append((host, tag, 'video'))
                continue
            pat = expected(kind, a, b, suf)
            if any(pat.match(r) for r in refs):
                continue
            # A tag can be satisfied by ANOTHER lesson's asset, deliberately. L10's
            # [IMAGE 10.1] prints "this is the same photo you met in Lesson 5" and wires
            # L05_IMAGE_5-04b directly. Counting that as missing would have sent DJ out to
            # re-shoot a photograph the book already ships. If an <img> sits within the
            # tag's own paragraph, the figure is LANDED whatever the filename says.
            j = src.find(f'[{tag}]')
            if j >= 0 and SRC_RE.search(src[max(0, j - 700):j + 400]):
                continue
            staged = [d for d in on_disk if pat.match(d)]
            outstanding.append((host, tag, 'on disk, unwired: ' + staged[0] if staged
                                else 'no asset'))
    orphans = sorted(d for d in on_disk if d not in referenced)
    dupes = []
    for p in glob.glob('lessons/*.svg') + glob.glob('lessons/*.png'):
        n = os.path.basename(p)
        twin = os.path.join('images', n)
        if os.path.exists(twin):
            import hashlib
            h = lambda q: hashlib.md5(open(q, 'rb').read()).hexdigest()[:12]
            dupes.append((p, h(p), h(twin), h(p) == h(twin)))
    return planned, outstanding, orphans, dupes


def emit(planned, outstanding, orphans, dupes):
    by = collections.defaultdict(list)
    for host, tag, why in outstanding:
        by[host].append((tag, why))
    L = ['# IMAGE WORKLIST', '',
         f'GENERATED by `image_audit.py` {VERSION}. Do not hand-edit (Bible §24.12) - if a '
         'line is wrong, the generator is wrong.', '',
         f'**{len(outstanding)} outstanding** of {len(planned)} planned figure tags across '
         f'{len(lessons())} lessons.', '',
         'A figure is PLANNED when a lesson prints its tag and LANDED when an `<img>` in that '
         'lesson points at a file whose name encodes the same tag. IMAGE and GRAPHIC are '
         'separate number spaces (§10), so a GRAPHIC carrying the same number is a different '
         'figure and is never counted as the missing one.', '',
         '## Outstanding, by lesson', '', '| Lesson | Tag | State |', '|---|---|---|']
    for host in sorted(by):
        for tag, why in by[host]:
            L.append(f'| L{host} | {tag} | {why} |')
    L += ['', '## Unreferenced files in `images/`', '',
          f'{len(orphans)} file(s) on disk that no page points at. Not a defect by itself - '
          'staging is legitimate - but every one is either future work or litter.', '']
    for o in orphans:
        L.append(f'- `{o}`')
    if dupes:
        L += ['', '## Copies of an `images/` file sitting in `lessons/`', '']
        for p, h1, h2, same in dupes:
            L.append(f'- `{p}` — {"IDENTICAL" if same else "**DIFFERENT BYTES**"} '
                     f'({h1} vs images/ {h2})')
    return '\n'.join(L) + '\n'


def selftest():
    ok = True
    planned, outstanding, orphans, dupes = audit()

    print('CONTROL A (coverage): every lesson is read and every lesson plans figures')
    hosts = {h for h, _ in planned}
    print(f'   {len(planned)} planned tag(s) across {len(hosts)} lesson(s)')
    if len(hosts) != 16 or len(planned) < 100:
        print('   FAILED. The scan under-reaches.')
        ok = False

    print('CONTROL B (trap 1): a tag naming ANOTHER lesson resolves to that lesson\'s file')
    src = open('lessons/Lesson_07.html', encoding='utf-8').read()
    if '[GRAPHIC 6.11]' not in src:
        print('   INCONCLUSIVE: L07 no longer quotes GRAPHIC 6.11 - re-point this control.')
    elif any(t == 'GRAPHIC 6.11' for h, t, _ in outstanding):
        print('   FAILED. A cross-lesson tag was reported outstanding - the host prefix bug.')
        ok = False
    else:
        print('   L07\'s [GRAPHIC 6.11] resolves against L06 and is NOT called outstanding')

    print('CONTROL C (trap 2): a same-numbered GRAPHIC must NOT satisfy an IMAGE tag')
    hit = [t for h, t, w in outstanding if h == '13' and t == 'IMAGE 13.1']
    if hit and os.path.exists('images/L13_GRAPHIC_13-01_lawnmower_sweep.svg'):
        print('   IMAGE 13.1 stays outstanding though GRAPHIC 13-01 exists (separate spaces)')
    else:
        print('   FAILED. A cross-space match was accepted as the missing figure.')
        ok = False

    print('CONTROL D (false-pass): a landed figure must NOT be reported')
    if any(t == 'GRAPHIC 1.10' for h, t, _ in outstanding):
        print('   FAILED. A figure with a live asset was reported outstanding.')
        ok = False
    else:
        print('   L01 GRAPHIC 1.10, which is live, is absent from the outstanding list')

    print('CONTROL D2 (reuse): a tag wired to ANOTHER lesson\'s asset is not outstanding')
    if any(h == '10' and t == 'IMAGE 10.1' for h, t, _ in outstanding):
        print('   FAILED. L10 IMAGE 10.1 is wired to L05_IMAGE_5-04b and was called missing.')
        ok = False
    else:
        print('   L10 IMAGE 10.1, served by L05\'s photo, is not reported outstanding')

    print('CONTROL E (determinism): a SECOND PROCESS must emit the same bytes')
    # In-process repetition is not a determinism test. PYTHONHASHSEED is fixed for the life
    # of a process, so set-iteration order cannot vary and the check passes on a generator
    # that is not deterministic at all - which is exactly what happened here.
    import subprocess, hashlib
    mine = hashlib.md5(emit(planned, outstanding, orphans, dupes).encode()).hexdigest()
    theirs = set()
    for seed in ('0', '1', '12345'):
        env = dict(os.environ, PYTHONHASHSEED=seed)
        r = subprocess.run([sys.executable, '-c',
                            'import image_audit as I,hashlib,sys;'
                            'sys.stdout.write(hashlib.md5('
                            'I.emit(*I.audit()).encode()).hexdigest())'],
                           capture_output=True, text=True, env=env, cwd=os.getcwd())
        theirs.add(r.stdout.strip())
    if theirs != {mine}:
        print(f'   FAILED. Emission varies with the hash seed: {sorted(theirs)}')
        ok = False
    else:
        print(f'   three hash seeds, one output ({mine[:12]})')

    print('\n' + ('ALL CONTROLS PASS' if ok else 'CONTROLS FAILED'))
    return 0 if ok else 1


if __name__ == '__main__':
    if '--selftest' in sys.argv:
        sys.exit(selftest())
    text = emit(*audit())
    if '--check' in sys.argv:
        cur = open(OUT, encoding='utf-8').read() if os.path.exists(OUT) else None
        print(f'{OUT} is current' if cur == text else f'{OUT} DIFFERS - re-run without --check')
        sys.exit(0 if cur == text else 1)
    tmp = OUT + '.tmp'
    with open(tmp, 'w', encoding='utf-8') as fh:
        fh.write(text)
    os.replace(tmp, OUT)
    p, o, orp, d = audit()
    print(f'wrote {OUT}: {len(o)} outstanding of {len(p)} planned; {len(orp)} unreferenced')
