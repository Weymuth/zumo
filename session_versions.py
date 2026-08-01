#!/usr/bin/env python3
"""session_versions.py - reads every version from its own file and EMITS the
canonical blocks that LIVE_ZUMO_TEXTBOOK.md and the session handoff both use.

WHY THIS EXISTS. S96 produced three false alarms in one close-out, all from the same shape:
an unanchored search over a whole file, whose hit count was then treated as a fact. A regex
for the Bible version matched historical per-session blocks; a scan for '**Versions:**' found
a second, legitimate, pre-existing line in an S64 block; a substring test missed a name
written in backticks. None was a defect in the book. All three cost review time, and a wrong
finding costs 3x a blank one (Bible 24.6c).

THE FIX IS NOT A BETTER CHECKER, IT IS NOT CHECKING. If LIVE.md's Versions line and the
handoff's STATE block are both generated from this one reader, they cannot disagree, and
version drift stops being something to detect.

TWO RULES THIS FILE OBEYS, BOTH LEARNED THE HARD WAY:

1. EVERY READ IS BOUNDED AND ASSERTED. Each version has ONE home, in a bounded header
   window. The pattern must match EXACTLY ONCE in that window. Zero matches or two matches
   is a hard error that names the file - never a silently missing value, and never a value
   picked from a search that wandered into the document's history. Bible 24.10: the parser
   is the default instrument and grep reads ONE line of known format.

2. THE SELFTEST CONTROLS IN BOTH DIRECTIONS. Bible 24.8 is usually asked one way - 'if the
   answer were the opposite, would this instrument look different?' - which catches a false
   PASS. It was never asked in the mirror: 'if there were NO defect, would this thing say
   so?' That is what catches a false FAIL, and it is the check that would have caught all
   three S96 alarms in one second each. --selftest runs both:
     control A (false-pass):  seed a corrupted version -> the reader MUST report it
     control B (false-fail):  run against untouched files -> the reader MUST be silent

NOTE ON THE HOMES THEMSELVES. Nine scripts carry their version in six different shapes:
a '# name.py vX' comment, a '\"\"\"name.py vX' docstring, a VERSION constant, a prose line, a
banner. That inconsistency is why hand-checking kept misfiring. This file does not fix it -
it absorbs it in one place so nothing else has to know.

THE SHA IS NOT A VERSION. --live and --handoff end with the commit they were verified at,
and LIVE.md can never name the commit that CONTAINS LIVE.md - so a naive comparison of
generated-now against written-then always differs by that one field and reads as a defect.
That happened once, immediately, on the S96 close-out. --check exists so nobody compares
these by hand again: it normalises the sha away and compares only versions. Every ad-hoc
comparison written in a shell today produced a false alarm; this one is written once, has a
control run, and is the only comparison anyone should use.

usage:
  python3 session_versions.py              # human-readable table
  python3 session_versions.py --live       # the Versions: line for LIVE_ZUMO_TEXTBOOK.md
  python3 session_versions.py --handoff    # the STATE block for the handoff
  python3 session_versions.py --check      # do LIVE.md + the handoff still match the files?
  python3 session_versions.py --selftest   # bidirectional control run
"""
import re, os, sys, glob, subprocess, tempfile, shutil

VERSION = 'v1.7'   # the only version home in this file (S96; v1.4 S98)
# v1.7 (S100): site_parity registered. Written this same session and NOT in the block this
#   file emits - the third time in three sessions a new instrument was missed (v1.4.1
#   fit_raster_svg, v1.5 flatten_alpha + svg_layout_audit, now this). The registry is the
#   thing that gets forgotten, so the fix is a CONTROL, not more care: control E compares
#   ARTEFACTS against the .py files actually in root and names any that carry a VERSION
#   constant but are not registered.
# v1.6 (S100): CONTROL C's clean direction ran check() against the LIVE tree and reported a
#   non-zero exit as "FAILED. --check reports drift on a clean tree." It could not tell a
#   wrong READER from a wrong BOOK, which is the one question it existed to answer, and it
#   returned 1 before CONTROL D ran - so a duplicate handoff in the repo both misattributed
#   to this tool AND silently skipped the last control in the suite. Now: a fixture made
#   clean by construction (one handoff, LIVE.md line 6 and the handoff block both GENERATED
#   from the emitter), both directions run inside it, and the live tree read afterwards as a
#   labelled report that cannot mask what follows it.
#   §24 corollary, alongside S99's "a control that does not ask WHICH is not a control":
#   A CONTROL THAT DEPENDS ON THE STATE OF WHAT IT AUDITS IS NOT A CONTROL.
# v1.5 (S99): flatten_alpha and svg_layout_audit registered. Two instruments were written
#   this session and neither appeared in the block this file EMITS, so LIVE.md and the
#   handoff would have recorded a toolchain that no longer matched the repo - the exact
#   failure v1.4.1 registered fit_raster_svg to prevent, one session later.
# v1.4.1 (S98): fit_raster_svg registered as an artefact. A new instrument absent from
#   ARTEFACTS has no reader, so its version could only be hand-typed - the exact failure
#   this file exists to prevent.
# v1.4 (S98): grep_trap(). A version home the tooling reads correctly can still be
#   MISREAD BY A HUMAN, and was: a plain grep of book_gates.py returned v1.26.1 from a
#   changelog comment while the live version was v1.29 - three releases stale, and it read
#   exactly like an answer. Measured across all 15 artefacts: 2 misread that way
#   (book_gates, build_family_map), both because the changelog sits ABOVE the home. Fixed
#   by moving the home above the changelog in each; this check is what keeps it fixed.
#   NOT fatal, and NOT applied to the labelled homes: the Bible carries per-session
#   history and its first token is v8.63 BY DESIGN, which is exactly why the ritual's
#   grep is ANCHORED to 'Bible version:'. Scoped to the VERSION-constant files, where a
#   bare grep is a thing people actually do.

ROOT = os.path.dirname(os.path.abspath(__file__))
WINDOW = 90          # header lines searched. Widened in v1.3: this file's own constant sits
                     # below its docstring. A wider window cannot hide anything - read_one
                     # asserts EXACTLY ONE match, so a second home errors loudly.


class VersionError(Exception):
    pass


def read_one(relpath, pattern, window=WINDOW, label=None):
    """Read exactly one version from a bounded header window. Ambiguity is an error."""
    label = label or relpath
    path = os.path.join(ROOT, relpath)
    if not os.path.exists(path):
        raise VersionError(f"{label}: file not found at {relpath}")
    with open(path, encoding='utf-8') as fh:
        head = [next(fh, '') for _ in range(window)]
    hits = [m.group(1) for line in head for m in [re.search(pattern, line)] if m]
    if len(hits) == 0:
        raise VersionError(f"{label}: version home not found in first {window} lines "
                           f"(pattern {pattern!r}) - the home moved, or the file changed shape")
    if len(hits) > 1:
        raise VersionError(f"{label}: {len(hits)} version homes found in the header {hits} - "
                           f"ambiguous, and a search would have silently taken the first")
    return hits[0]


# (label, relpath, regex) - one home each, all bounded to the header
ARTEFACTS = [
    ('Bible',                 'ZUMO_SUPER_BIBLE.md',      r'Bible version: (v[\d.]+)'),
    ('BookComponentStandard', 'BookComponentStandard.md', r'Standard version: (v[\d.]+)'),
    ('Maker',                 'newproject.html',          r'Maker version: (v[\d.]+)'),
    ('going_deeper',          'going_deeper.html',        r'Going Deeper version: (v[\d.]+)'),
    ('Syllabus',              'ZUMO_Syllabus_WORKING.md', r'ZUMO_Syllabus_WORKING\.md (v[\d.]+)'),
    ('session_versions',      'session_versions.py',      r"VERSION = '(v[\d.]+)'"),
    ('book_gates',            'book_gates.py',            r"VERSION = '(v[\d.]+)'"),
    ('lesson_inventory',      'lesson_inventory.py',      r"VERSION = '(v[\d.]+)'"),
    ('gen_component',         'gen_component.py',         r"VERSION = '(v[\d.]+)'"),
    ('pill_sweep',            'pill_sweep.py',            r'pill sweep .*?  (v[\d.]+)'),
    ('gate_payload_match',    'gate_payload_match.py',    r'PAYLOAD BYTE-MATCH GATE .*?— (v[\d.]+)'),
    ('build_family_map',      'build_family_map.py',      r"VERSION = '(v[\d.]+)'"),
    ('build_mark_index',      'build_mark_index.py',      r"VERSION = '(v[\d.]+)'"),
    ('gen_bonus_banner',      'gen_bonus_banner.py',      r"VERSION = '(v[\d.]+)'"),
    ('gen_part_banners',      'gen_part_banners.py',      r'gen_part_banners\.py  (v[\d.]+)'),
    ('fit_raster_svg',        'fit_raster_svg.py',        r"VERSION = '(v[\d.]+)'"),
    ('flatten_alpha',         'flatten_alpha.py',         r"VERSION = '(v[\d.]+)'"),
    ('svg_layout_audit',      'svg_layout_audit.py',      r"VERSION = '(v[\d.]+)'"),
    ('site_parity',           'site_parity.py',           r"VERSION = '(v[\d.]+)'"),
]


def lesson_versions():
    """Lessons carry TWO homes (Bible 5b): hidden comment line 1 = full v##.#.#,
    visible banner = MAJOR.MINOR. Both must exist and agree. Disagreement is the
    exact drift 5b was written to prevent, so it is an error, not a note."""
    out, errs = {}, []
    for path in sorted(glob.glob(os.path.join(ROOT, 'lessons', 'Lesson_*.html'))):
        name = os.path.basename(path)
        key = 'L' + name[7:9]
        src = open(path, encoding='utf-8').read()
        first = src.split('\n', 1)[0]
        m = re.search(r'Lesson version: (v[\d.]+)', first)
        if not m:
            errs.append(f"{name}: no hidden version comment on line 1 (5b home 1)")
            continue
        full = m.group(1)
        banners = set(re.findall(r'Version ([\d]+\.[\d]+)(?![\d.])', src))
        if not banners:
            errs.append(f"{name}: no visible Version banner (5b home 2)")
            continue
        if len(banners) > 1:
            errs.append(f"{name}: {len(banners)} disagreeing visible banners {sorted(banners)}")
            continue
        banner = banners.pop()
        if not full.lstrip('v').startswith(banner):
            errs.append(f"{name}: 5b VIOLATION - hidden {full} vs visible banner {banner}")
            continue
        out[key] = full
    if len(out) + len(errs) != 16:
        errs.append(f"expected 16 lesson files, saw {len(out) + len(errs)}")
    return out, errs


def assets():
    marks = len(os.listdir(os.path.join(ROOT, 'images', 'marks')))
    icons = len(os.listdir(os.path.join(ROOT, 'images', 'icons')))
    return marks, icons


def census():
    r = subprocess.run([sys.executable, 'lesson_inventory.py'],
                       capture_output=True, text=True, cwd=ROOT)
    m = re.search(r'TOTAL\s+(\d+)', r.stdout)
    if not m:
        raise VersionError("census: lesson_inventory.py produced no TOTAL row - "
                           "an absent number is not a zero")
    return int(m.group(1))


def head_sha():
    r = subprocess.run(['git', 'rev-parse', '--short=7', 'HEAD'],
                       capture_output=True, text=True, cwd=ROOT)
    return r.stdout.strip() or 'UNKNOWN'


def gather():
    vals, errs = {}, []
    for label, rel, pat in ARTEFACTS:
        try:
            vals[label] = read_one(rel, pat, label=label)
        except VersionError as e:
            errs.append(str(e))
    lessons, lerrs = lesson_versions()
    return vals, lessons, errs + lerrs


def emit_live(vals, lessons, marks, icons, cen, sha):
    ls = ' · '.join(f"{k} {lessons[k]}" for k in sorted(lessons))
    return (f"**Versions:** {ls} · going_deeper {vals['going_deeper']} — census "
            f"**{cen:,}** · Bible **{vals['Bible']}** · BookComponentStandard "
            f"{vals['BookComponentStandard']} · gen_component {vals['gen_component']} · Maker "
            f"{vals['Maker']} · **book_gates {vals['book_gates']}** · lesson_inventory "
            f"{vals['lesson_inventory']} · pill_sweep {vals['pill_sweep']} · gate_payload_match "
            f"{vals['gate_payload_match']} · build_family_map {vals['build_family_map']} · "
            f"build_mark_index {vals['build_mark_index']} · gen_bonus_banner "
            f"{vals['gen_bonus_banner']} · gen_part_banners {vals['gen_part_banners']} · "
            f"session_versions {vals['session_versions']} · "
            f"fit_raster_svg {vals['fit_raster_svg']} · flatten_alpha {vals['flatten_alpha']} · "
            f"svg_layout_audit {vals['svg_layout_audit']} · "
            f"site_parity {vals['site_parity']} · "
            f"`ZUMO_Syllabus_WORKING.md` {vals['Syllabus']} · `images/marks/` **{marks}** · "
            f"`images/icons/` {icons} incl. LICENSE. **Verified by fresh clone at `{sha}`.**")


def emit_handoff(vals, lessons, marks, icons, cen, sha):
    ls = ' · '.join(f"{k} {lessons[k]}" for k in sorted(lessons))
    return (f"Fresh-clone verified at **`{sha}`**. Census **{cen:,}**.\n"
            f"Bible **{vals['Bible']}** · `BookComponentStandard` **{vals['BookComponentStandard']}** · "
            f"Maker **{vals['Maker']}** ·\n`marks/` **{marks}** · `icons/` **{icons}** incl. LICENSE.\n\n"
            f"Instruments: `book_gates` **{vals['book_gates']}** · `lesson_inventory` "
            f"**{vals['lesson_inventory']}** ·\n`gen_component` **{vals['gen_component']}** · "
            f"`pill_sweep` **{vals['pill_sweep']}** · `gate_payload_match` **{vals['gate_payload_match']}** ·\n"
            f"`build_family_map` **{vals['build_family_map']}** · `build_mark_index` "
            f"**{vals['build_mark_index']}** · `gen_bonus_banner` **{vals['gen_bonus_banner']}** ·\n"
            f"`gen_part_banners` **{vals['gen_part_banners']}** · `session_versions` "
            f"**{vals['session_versions']}** · `fit_raster_svg` **{vals['fit_raster_svg']}** ·\n"
            f"`flatten_alpha` **{vals['flatten_alpha']}** · "
            f"`svg_layout_audit` **{vals['svg_layout_audit']}** · "
            f"`site_parity` **{vals['site_parity']}** ·\n"
            f"`going_deeper` **{vals['going_deeper']}**.\n\n"
            f"Lessons: {ls}.")



def _desha(text):
    """A 7-hex commit hash is a verification fact, not a version. Normalise it away so a
    comparison reports version drift and nothing else."""
    return re.sub(r'`[0-9a-f]{7}`', '`SHA`', text)


def _versions_in(text):
    return dict(re.findall(r'([A-Za-z_][\w./]*) \*{0,2}(v[\d.]+)', text.replace('**', '')))


def check():
    """Compare LIVE.md's Versions line and the handoff's STATE block against the files.
    Silent when clean; names every disagreement when not. Never compares the sha."""
    vals, lessons, errs = gather()
    if errs:
        for e in errs:
            print("  VERSION HOME ERROR", e)
        return 1
    marks, icons = assets()
    cen, sha = census(), head_sha()
    bad = 0

    live_lines = open(os.path.join(ROOT, 'LIVE_ZUMO_TEXTBOOK.md'), encoding='utf-8').read().split('\n')
    written = live_lines[5]
    if not written.startswith('**Versions:**'):
        print("  LIVE.md: line 6 is not the Versions line - the file changed shape")
        return 1
    gen = emit_live(vals, lessons, marks, icons, cen, sha)
    w, g = _versions_in(_desha(written)), _versions_in(_desha(gen))
    for k in sorted(set(w) | set(g)):
        if w.get(k) != g.get(k):
            print(f"  LIVE.md {k}: written={w.get(k)} files={g.get(k)}")
            bad += 1

    handoffs = [f for f in glob.glob(os.path.join(ROOT, 'ZUMO_S*_HANDOFF.md'))]
    if len(handoffs) != 1:
        print(f"  expected exactly one session handoff in root, found {len(handoffs)}")
        return 1
    hw = _versions_in(_desha(open(handoffs[0], encoding='utf-8').read()))
    hg = _versions_in(_desha(emit_handoff(vals, lessons, marks, icons, cen, sha)))
    for k in sorted(hg):
        if k in hw and hw[k] != hg[k]:
            print(f"  {os.path.basename(handoffs[0])} {k}: written={hw[k]} files={hg[k]}")
            bad += 1

    if bad:
        print(f"\n  {bad} disagreement(s). Regenerate with --live / --handoff.")
        return 1
    written_sha = re.search(r'`([0-9a-f]{7})`', written)
    if written_sha and written_sha.group(1) != sha:
        print(f"  note: LIVE.md was verified at {written_sha.group(1)}, HEAD is now {sha}. "
              f"Expected -\n        a document cannot name the commit that contains it. "
              f"Not drift; versions all agree.")
    print("  LIVE.md and the handoff agree with every file on every version.")
    return 0


TOKEN = re.compile(r'\bv\d+\.[\d.]*\d\b')


def grep_trap():
    """Would a PLAIN grep of this file return its live version?

    read_one() is anchored and bounded, so the TOOLING is never wrong here. A person at a
    terminal is, and a stale answer looks identical to a right one. Scoped to the files whose
    home is a VERSION constant: for those, first-token and home should be the same line, and
    a difference means a changelog line got prepended above the home.
    """
    out = []
    for label, relpath, pattern in ARTEFACTS:
        if "VERSION = '" not in pattern:
            continue
        path = os.path.join(ROOT, relpath)
        if not os.path.exists(path):
            continue
        text = open(path, encoding='utf-8', errors='replace').read()
        first = TOKEN.search(text)
        try:
            true = read_one(relpath, pattern, label=label)
        except VersionError:
            continue
        if first and first.group(0) != true:
            out.append((label, relpath, first.group(0), true))
    return out


def _fixture_clean(work, probe):
    """Make a COPIED tree clean by construction on every axis check() tests, so that
    silence from --check inside it is evidence about the reader rather than a reading of
    whatever state the live repo happens to be in on the day.

    Three axes, because check() tests three: exactly one handoff in root; LIVE.md's
    Versions line agreeing with the files; the handoff's versions agreeing with the files.
    Each is normalised by GENERATING it from the emitter, never by hoping it is already so.
    """
    hs = glob.glob(os.path.join(work, 'ZUMO_S*_HANDOFF.md'))
    assert hs, "fixture: the tree carries no session handoff to keep"

    def _sess(p):
        m = re.search(r'ZUMO_S(\d+)_HANDOFF', os.path.basename(p))
        assert m, f"fixture: handoff name changed shape - {os.path.basename(p)}"
        return int(m.group(1))

    keep = max(hs, key=_sess)          # numeric, not lexical: S100 must beat S99
    for p in hs:
        if p != keep:
            os.remove(p)

    def _emit(flag):
        r = subprocess.run([sys.executable, probe, flag],
                           capture_output=True, text=True, cwd=work)
        assert r.returncode == 0, f"fixture: {flag} did not emit - {r.stderr.strip()}"
        return r.stdout

    line = _emit('--live').strip().split('\n')[0]
    assert line.startswith('**Versions:**'), \
        "fixture: --live no longer emits the Versions line first"
    p = os.path.join(work, 'LIVE_ZUMO_TEXTBOOK.md')
    L = open(p, encoding='utf-8').read().split('\n')
    assert L[5].startswith('**Versions:**'), "fixture: LIVE.md line 6 is not the Versions line"
    L[5] = line
    open(p, 'w', encoding='utf-8').write('\n'.join(L))

    open(keep, 'w', encoding='utf-8').write(_emit('--handoff'))


def selftest():
    """Bidirectional control run. Neither direction alone is evidence."""
    print("CONTROL B (false-fail): reader against untouched files - must be SILENT")
    vals, lessons, errs = gather()
    if errs:
        for e in errs:
            print("   ERROR", e)
        print("\n   FAILED. The reader reports a defect on known-good files, which means the\n"
              "   READER is wrong, not the book. This is the direction S96 never checked.")
        return 1
    print(f"   clean - {len(vals)} artefacts + {len(lessons)} lessons, no errors\n")

    print("CONTROL A (false-pass): seed a corrupted version - reader MUST report it")
    tmp = tempfile.mkdtemp()
    try:
        work = os.path.join(tmp, 'repo')
        shutil.copytree(ROOT, work, ignore=shutil.ignore_patterns(
            '.git', '__pycache__', 'images', 'tutor'))
        # break Bible's home, and break one lesson's 5b agreement
        p = os.path.join(work, 'ZUMO_SUPER_BIBLE.md')
        s = open(p, encoding='utf-8').read()
        open(p, 'w', encoding='utf-8').write(s.replace('Bible version: v', 'Bible VERSION: v', 1))
        p = os.path.join(work, 'lessons', 'Lesson_03.html')
        s = open(p, encoding='utf-8').read()
        open(p, 'w', encoding='utf-8').write(s.replace('Lesson version: v03.20.0',
                                                       'Lesson version: v09.99.9', 1))
        # run the COPY inside the corrupted tree. Running the original with cwd=work reads
        # the original's files, because ROOT is derived from __file__ and not from cwd -
        # the control would then test the clean tree and report a false pass.
        probe = os.path.join(work, os.path.basename(__file__))
        assert os.path.exists(probe), "control run: the script did not copy into the work tree"
        r = subprocess.run([sys.executable, probe, '--_probe'],
                           capture_output=True, text=True, cwd=work)
        caught_bible = 'Bible' in r.stdout and 'version home not found' in r.stdout
        caught_5b = '5b VIOLATION' in r.stdout
        print(f"   corrupted Bible home detected: {caught_bible}")
        print(f"   seeded 5b disagreement detected: {caught_5b}")
        if not (caught_bible and caught_5b):
            print("\n   FAILED. A seeded defect did not surface - an assert that cannot fail\n"
                  "   is not evidence.")
            return 1
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    print("CONTROL C (--check, both ways, against a fixture BUILT clean)")
    # S100. This control's clean direction used to be `if check() != 0` against the LIVE
    # tree, printing "FAILED. --check reports drift on a clean tree." Two defects in one line.
    #   MISATTRIBUTION - a duplicate handoff in the REPO printed as a fault in this TOOL.
    #   MASKING        - it returned 1 before CONTROL D ever ran, so one unrelated repo
    #                    defect silently skipped the last control in the suite. Observed:
    #                    at S100 open, D did not execute and I could not tell it apart
    #                    from D passing.
    # A control whose clean direction depends on the state of the thing it audits is not a
    # control. It cannot distinguish "the reader is wrong" from "the book is wrong", which
    # is the only question it was built to answer. The fixture below is clean BY
    # CONSTRUCTION, so silence inside it is evidence; the live tree is then read as a
    # REPORT, which is all it ever was.
    #
    # The copy keeps images/: check() calls assets(), which counts images/marks and
    # images/icons. Controls A and D exclude images deliberately and must keep doing so -
    # see the --_grep note in main(), where that exclusion once produced a bogus failure.
    tmp2 = tempfile.mkdtemp()
    try:
        work = os.path.join(tmp2, 'repo')
        shutil.copytree(ROOT, work, ignore=shutil.ignore_patterns('.git', '__pycache__'))
        probe = os.path.join(work, os.path.basename(__file__))
        assert os.path.exists(probe), "control C: the script did not copy into the work tree"
        _fixture_clean(work, probe)

        r = subprocess.run([sys.executable, probe, '--check'],
                           capture_output=True, text=True, cwd=work)
        if r.returncode != 0:
            print("   FAILED. --check is not silent on a tree built clean, so the READER\n"
                  "   is wrong, not the book. What it said:")
            for ln in (r.stdout.strip() or r.stderr.strip()).split('\n'):
                print("     " + ln)
            return 1
        print("   silent on a fixture built clean")

        # seed drift INTO that same known-clean fixture, so the two directions differ by
        # exactly one edit and nothing else
        p = os.path.join(work, 'LIVE_ZUMO_TEXTBOOK.md')
        L = open(p, encoding='utf-8').read().split('\n')
        before = L[5]
        L[5] = re.sub(r'(book_gates )v[\d.]+', r'\g<1>v9.99.9', L[5])
        assert L[5] != before, "control C: could not seed a disagreement - the line changed shape"
        open(p, 'w', encoding='utf-8').write('\n'.join(L))
        r = subprocess.run([sys.executable, probe, '--check'],
                           capture_output=True, text=True, cwd=work)
        if r.returncode == 0 or 'book_gates' not in r.stdout:
            print("   FAILED. A seeded version disagreement did not surface.")
            return 1
        print("   seeded disagreement detected, exit 1\n")
    finally:
        shutil.rmtree(tmp2, ignore_errors=True)

    # The live tree, read as what it is: a report on the REPO, never a verdict on this
    # tool, and never able to skip a control below it.
    print("   live tree (report, not a control):")
    live_rc = check()
    if live_rc != 0:
        print("   ^ that is a finding about the REPO. The controls above still stand.\n")
    else:
        print("")

    print("CONTROL D (grep_trap, both ways): clean must be silent, a prepended changelog loud")
    live = grep_trap()
    if live:
        for lab, rel, first, true in live:
            print(f"   FAILED on the clean tree: {rel} greps as {first}, home is {true}")
        return 1
    tmp3 = tempfile.mkdtemp()
    try:
        work = os.path.join(tmp3, "repo")
        shutil.copytree(ROOT, work, ignore=shutil.ignore_patterns(
            ".git", "__pycache__", "images", "tutor"))
        p = os.path.join(work, "book_gates.py")
        s = open(p, encoding="utf-8").read()
        # seed by SHAPE, not by the literal version: a hardcoded 'v1.29' silently stops
        # matching the day book_gates bumps, and the control would fail on its own anchor.
        seeded = re.sub(r"(?m)^(VERSION = ')", "# v1.00.0 seeded control\\n\\1", s, count=1)
        assert seeded != s, "control D: could not seed - book_gates home changed shape"
        open(p, "w", encoding="utf-8").write(seeded)
        probe = os.path.join(work, os.path.basename(__file__))
        r = subprocess.run([sys.executable, probe, '--_grep'],
                           capture_output=True, text=True, cwd=work)
        if "book_gates.py returns v1.00.0" not in r.stdout:
            print("   FAILED. A home buried under a changelog did not surface.")
            return 1
        print("   silent when clean, named the seeded file and both versions\n")
    finally:
        shutil.rmtree(tmp3, ignore_errors=True)

    print("CONTROL E (registry completeness): a root .py with a VERSION constant must be "
          "REGISTERED")
    # Three sessions running, a new instrument was written and left out of ARTEFACTS, so its
    # version never reached LIVE.md or the handoff and the recorded toolchain silently stopped
    # matching the repo. Care did not fix it twice; this asks the question mechanically.
    import glob as _glob
    _registered = {rel for _lab, rel, _pat in ARTEFACTS}
    _unregistered = []
    for _f in sorted(_glob.glob('*.py')):
        try:
            _src = open(_f, encoding='utf-8', errors='replace').read()
        except OSError:
            continue
        if re.search(r"^VERSION = '", _src, re.M) and _f not in _registered:
            _unregistered.append(_f)
    if _unregistered:
        for _u in _unregistered:
            print(f"   FAILED. {_u} declares a VERSION but is not in ARTEFACTS - its version "
                  f"will never be emitted.")
        return 1
    print(f"   all {len(_registered)} registered; no root .py carries an unregistered VERSION\n")

    print("ALL FIVE CONTROLS PASS - silent when clean, loud when broken, both directions.")
    return 0


def main():
    arg = sys.argv[1] if len(sys.argv) > 1 else ''
    if arg == '--selftest':
        sys.exit(selftest())
    if arg == '--check':
        sys.exit(check())
    if arg == '--_grep':
        # internal: grep_trap only. The full table calls assets(), which needs images/,
        # and control D's work tree deliberately omits it - the first version of that
        # control 'failed' for that reason alone, with nothing wrong in what it tested.
        for _lab, _rel, _first, _true in grep_trap():
            print(f'NOTE: a plain grep of {_rel} returns {_first}, not {_true}')
        sys.exit(0)
    if arg == '--_probe':
        # internal: gather and report, never re-enter selftest. Without this the control
        # run spawns itself, and a seeded defect that failed to register would recurse.
        _v, _l, _e = gather()
        for _x in _e:
            print("ERROR", _x)
        sys.exit(1 if _e else 0)
    vals, lessons, errs = gather()
    if errs:
        print("VERSION HOME ERRORS - resolve before emitting anything:")
        for e in errs:
            print("  ", e)
        sys.exit(1)
    marks, icons = assets()
    cen, sha = census(), head_sha()
    if arg == '--live':
        print(emit_live(vals, lessons, marks, icons, cen, sha))
    elif arg == '--handoff':
        print(emit_handoff(vals, lessons, marks, icons, cen, sha))
    else:
        for k in sorted(vals):
            print(f"  {k:24} {vals[k]}")
        for k in sorted(lessons):
            print(f"  {k:24} {lessons[k]}")
        print(f"\n  census {cen:,} · marks/ {marks} · icons/ {icons} · HEAD {sha}")
        for _lab, _rel, _first, _true in grep_trap():
            print(f"\n  NOTE: a plain grep of {_rel} returns {_first}, not {_true} -"
                  f" its home sits\n        below a changelog line.")
        print("\n  --live / --handoff to emit the canonical blocks")


if __name__ == '__main__':
    main()
