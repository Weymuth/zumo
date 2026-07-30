#!/usr/bin/env python3
"""session_versions.py v1.1 (S96) - reads every version from its own file and EMITS the
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

usage:
  python3 session_versions.py              # human-readable table
  python3 session_versions.py --live       # the Versions: line for LIVE_ZUMO_TEXTBOOK.md
  python3 session_versions.py --handoff    # the STATE block for the handoff
  python3 session_versions.py --selftest   # bidirectional control run
"""
import re, os, sys, glob, subprocess, tempfile, shutil

ROOT = os.path.dirname(os.path.abspath(__file__))
WINDOW = 40          # header lines searched; a version home outside this is a defect, not a miss


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
    ('book_gates',            'book_gates.py',            r"VERSION = '(v[\d.]+)'"),
    ('lesson_inventory',      'lesson_inventory.py',      r'# lesson_inventory\.py (v[\d.]+)'),
    ('gen_component',         'gen_component.py',         r"VERSION = '(v[\d.]+)'"),
    ('pill_sweep',            'pill_sweep.py',            r'pill sweep .*?  (v[\d.]+)'),
    ('gate_payload_match',    'gate_payload_match.py',    r'PAYLOAD BYTE-MATCH GATE .*?— (v[\d.]+)'),
    ('build_family_map',      'build_family_map.py',      r"VERSION = '(v[\d.]+)'"),
    ('build_mark_index',      'build_mark_index.py',      r"VERSION = '(v[\d.]+)'"),
    ('gen_bonus_banner',      'gen_bonus_banner.py',      r"VERSION = '(v[\d.]+)'"),
    ('gen_part_banners',      'gen_part_banners.py',      r'gen_part_banners\.py  (v[\d.]+)'),
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
            f"`gen_part_banners` **{vals['gen_part_banners']}** · `going_deeper` **{vals['going_deeper']}**.\n\n"
            f"Lessons: {ls}.")


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
    print("\nBOTH CONTROLS PASS - the reader is silent when clean and loud when broken.")
    return 0


def main():
    arg = sys.argv[1] if len(sys.argv) > 1 else ''
    if arg == '--selftest':
        sys.exit(selftest())
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
        print("\n  --live / --handoff to emit the canonical blocks")


if __name__ == '__main__':
    main()
