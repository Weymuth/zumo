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

VERSION = 'v1.21.0'
# v1.19.0 (S123): title_feed registered in ARTEFACTS and added to BOTH emitted blocks.
#   Same shape as v1.18.0, and CONTROL E named the file the moment it landed in root —
#   an instrument written this session is exactly the kind that drifts unwatched, because
#   nothing else in the tree knows it exists yet.
# v1.21.0 (S128): family_tag and mark_wire registered in ARTEFACTS and in BOTH emitted
#   blocks. Control G named them as registered-but-not-emitted on the first run - the
#   control doing its job, for the third time in three sessions that added a tool.
# v1.18.0 (S121): next_pointer registered in ARTEFACTS and added to BOTH emitted blocks.
#   CONTROL E named it the moment the file landed in root, which is the control working as
#   designed - the tool was written this session and would otherwise have drifted unwatched.
#   Its VERSION literal was normalised to the house single-quoted form at the same time, so the
#   roster pattern is the standard one rather than a one-off.
# v1.17.0 (S114): session_numbers() - the session number lives in four hand-typed homes and
#   nothing compared them. It drifted three times in one day. Bible == LIVE.md == handoff-1.
# v1.16.0 (S113): _versions_in strips backticks. See the note in that function - the
#   comparator was blind to every backtick-wrapped entry, which is most of the STATE block.     # the only version home in this file (S96; v1.4 S98; v1.15 S110)
# v1.12 (S103): CONTROL G LOSES ITS ONLY EXEMPTION, and the handoff block gains the
#   syllabus. v1.11's G excused 'Syllabus' because it is emitted under its FILENAME - true
#   of --live, false of --handoff, where it appeared under neither name. The exemption
#   written to accommodate one block silently excused a real gap in the other, which is the
#   exact defect class G exists to catch. DJ ruling: it belongs in both. Syllabus added to
#   the handoff template; G now checks key OR filename with NO exemptions at all.
# v1.11 (S103): CONTROL G - REGISTERED IS NOT EMITTED. font_stack_sweep passed CONTROL E
#   (it WAS in ARTEFACTS) and still never reached LIVE.md or the handoff, because both emit
#   templates name every instrument BY HAND. Same drift CONTROL E exists to stop, one layer
#   downstream. Found while closing S103 by READING the emitted block - not by any control,
#   which is the S102 lesson again: compare the output against something. CONTROL G asserts
#   every ARTEFACTS key appears in BOTH emitted blocks; font_stack_sweep added to both.
# v1.10 (S103): CONTROL F - the Bible's version bookkeeping is now PARSED, not grepped.
#   Two defects shipped past this tool because it read ONE value off a line carrying TWO:
#   v8.88 had no changelog entry beneath it, and 'Current:' sat NINE versions stale inside
#   the very declaration line this tool was reading. A single-line grep cannot see a second
#   value on the line it matched. bible_consistency() parses the declaration line whole and
#   the changelog in file order, and requires header == Current == newest entry. Three
#   seeded breaks, plus a clean fixture, plus the live tree. font_stack_sweep registered.
# v1.9 (S102): regex_audit registered.
# v1.8 (S102): build_worklist registered. GPT_WORKLIST_S99.md was hand-assembled, so when
#   its ordering came under doubt there was nothing to re-run - the list that directs the
#   graphics chat's work could not be checked. It is a generate now, and a generate needs a
#   version home like every other instrument.
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
    ('build_css',             'build_css.py',             r"VERSION = '(v[\d.]+)'"),
    ('image_audit',           'image_audit.py',           r"VERSION = '(v[\d.]+)'"),
    ('strip_inline',          'strip_inline.py',          r"VERSION = '(v[\d.]+)'"),
    ('build_worklist',        'build_worklist.py',           r"VERSION = '(v[\d.]+)'"),
    ('font_stack_sweep',      'font_stack_sweep.py',      r"VERSION = '(v[\d.]+)'"),
    ('regex_audit',           'regex_audit.py',           r"VERSION = '(v[\d.]+)'"),
    ('build_palette',         'build_palette.py',         r"VERSION = '(v[\d.]+)'"),
    ('color_index',           'color_index.py',           r"VERSION = '(v[\d.]+)'"),
    ('entity_sweep',          'entity_sweep.py',          r"VERSION = '(v[\d.]+)'"),
    ('class_sweep',           'class_sweep.py',           r"VERSION = '(v[\d.]+)'"),
    ('next_pointer',          'next_pointer.py',          r"VERSION = '(v[\d.]+)'"),
    ('family_tag',            'family_tag.py',            r"VERSION = '(v[\d.]+)'"),
    ('mark_wire',             'mark_wire.py',             r"VERSION = '(v[\d.]+)'"),
    ('glyph_scan',            'glyph_scan.py',            r"VERSION = '(v[\d.]+)'"),
    ('title_feed',            'title_feed.py',            r"VERSION = '(v[\d.]+)'"),
    ('Timer',                 'timer.html',               r'Timer version: (v[\d.]+)'),
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
            f"build_css {vals['build_css']} · "
            f"image_audit {vals['image_audit']} · "
            f"strip_inline {vals['strip_inline']} · "
            f"build_worklist {vals['build_worklist']} · "
            f"regex_audit {vals['regex_audit']} · "
            f"build_palette {vals['build_palette']} · "
            f"class_sweep {vals['class_sweep']} · "
            f"color_index {vals['color_index']} · "
            f"entity_sweep {vals['entity_sweep']} · "
            f"font_stack_sweep {vals['font_stack_sweep']} · "
            f"next_pointer {vals['next_pointer']} · "
            f"family_tag {vals['family_tag']} · mark_wire {vals['mark_wire']} · "
            f"glyph_scan {vals['glyph_scan']} · "
            f"title_feed {vals['title_feed']} · "
            f"Timer {vals['Timer']} · "
            f"`ZUMO_Syllabus_WORKING.md` {vals['Syllabus']} · `images/marks/` **{marks}** · "
            f"`images/icons/` {icons} incl. LICENSE. **Verified by fresh clone at `{sha}`.**")


def emit_handoff(vals, lessons, marks, icons, cen, sha):
    ls = ' · '.join(f"{k} {lessons[k]}" for k in sorted(lessons))
    return (f"Fresh-clone verified at **`{sha}`**. Census **{cen:,}**.\n"
            f"Bible **{vals['Bible']}** · `BookComponentStandard` **{vals['BookComponentStandard']}** · "
            f"Maker **{vals['Maker']}** ·\n`marks/` **{marks}** · `icons/` **{icons}** incl. LICENSE.\n"
            f"`ZUMO_Syllabus_WORKING.md` **{vals['Syllabus']}**.\n\n"
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
            f"`build_css` **{vals['build_css']}** ·\n"
            f"`image_audit` **{vals['image_audit']}** ·\n"
            f"`strip_inline` **{vals['strip_inline']}** ·\n"
            f"`build_worklist` **{vals['build_worklist']}** ·\n"
            f"`regex_audit` **{vals['regex_audit']}** ·\n"
            f"`build_palette` **{vals['build_palette']}** ·\n"
            f"`class_sweep` **{vals['class_sweep']}** ·\n"
            f"`color_index` **{vals['color_index']}** ·\n"
            f"`entity_sweep` **{vals['entity_sweep']}** ·\n"
            f"`font_stack_sweep` **{vals['font_stack_sweep']}** ·\n"
            f"`next_pointer` **{vals['next_pointer']}** ·\n"
            f"`family_tag` **{vals['family_tag']}** ·\n"
            f"`mark_wire` **{vals['mark_wire']}** ·\n"
            f"`glyph_scan` **{vals['glyph_scan']}** ·\n"
            f"`title_feed` **{vals['title_feed']}** ·\n"
            f"`timer.html` **{vals['Timer']}** ·\n"
            f"`going_deeper` **{vals['going_deeper']}**.\n\n"
            f"Lessons: {ls}.")



def _desha(text):
    """A 7-hex commit hash is a verification fact, not a version. Normalise it away so a
    comparison reports version drift and nothing else."""
    return re.sub(r'`[0-9a-f]{7}`', '`SHA`', text)


def _versions_in(text):
    # S113: BACKTICKS WERE OPAQUE, AND THE STATE BLOCK IS WRITTEN IN BACKTICKS.
    # The old body stripped '**' and nothing else, so `book_gates` **v1.43.2** never matched -
    # the name ended at a backtick, not a space. Measured on the live S114 handoff: the
    # comparator extracted 22 keys from a block naming ~44, and every instrument version in it
    # was invisible. --check could not have failed on any of them. §24.8: if the answer were
    # the opposite - a handoff naming book_gates v1.0.0 - this function returned the same dict.
    # Backticks are now stripped exactly as '**' already was. Nothing else changed.
    return dict(re.findall(r'([A-Za-z_][\w./]*) \*{0,2}(v[\d.]+)',
                           text.replace('**', '').replace('`', '')))


# Root scripts that carry NO version by design: one-off utilities and surgery tools,
# not instruments. Listed rather than ignored, because ROSTER_COVERAGE below fails on
# anything that is in neither list — a roster that only checks what it already names
# cannot notice a missing instrument, which is exactly how build_palette.py and
# class_sweep.py sat unregistered and invisible to --check for a whole session (S110).
UNVERSIONED = {'engine.py', 'extract_project.py'}


def roster_coverage():
    """-> list of root .py files in neither ARTEFACTS nor UNVERSIONED."""
    rostered = {rel for _, rel, _ in ARTEFACTS}
    found = {os.path.basename(p) for p in glob.glob(os.path.join(ROOT, '*.py'))}
    return sorted(found - rostered - UNVERSIONED)


def session_numbers():
    """-> list of disagreements about WHICH SESSION THIS IS.

    S114: the number drifted THREE TIMES IN ONE DAY and no instrument could see it, because it
    lives in four hand-typed homes with no relation asserted between them. The relation is
    simple and fully derivable:

        newest Bible changelog entry  = the session that just ran        (N)
        LIVE.md's "Session N"         = the same session                 (N)
        handoff filename and title    = the session that READS it        (N + 1)

    Gate 28 already checks that the handoff agrees with ITSELF. It cannot check whether that
    number is the RIGHT number, because nothing else it can see names a session. This does.
    §24.8: if the answer were the opposite - a handoff numbered for a session that already ran -
    every other instrument returns exactly what it returns now.
    """
    import glob as _g
    bad = []
    bible = open(os.path.join(ROOT, 'ZUMO_SUPER_BIBLE.md'), encoding='utf-8').read()
    m = re.search(r'^v[\d.]+,\s*S(\d+),\s*(?:major|moderate|minor)\b', bible, re.M)
    if not m:
        return ['ZUMO_SUPER_BIBLE.md: no "vX.Y, SNN, kind" changelog entry to read the session from']
    n = int(m.group(1))

    live = open(os.path.join(ROOT, 'LIVE_ZUMO_TEXTBOOK.md'), encoding='utf-8').read()
    lm = re.search(r'Session (\d+)', live)
    if not lm:
        bad.append('LIVE.md: no "Session NN" to check against the Bible')
    elif int(lm.group(1)) != n:
        bad.append(f'LIVE.md says Session {lm.group(1)} but the newest Bible entry says S{n}')

    hos = sorted(g for g in _g.glob(os.path.join(ROOT, 'ZUMO_S*_HANDOFF.md'))
                 if re.fullmatch(r'ZUMO_S\d+_HANDOFF\.md', os.path.basename(g)))
    if len(hos) == 1:
        hn = int(re.fullmatch(r'ZUMO_S(\d+)_HANDOFF\.md', os.path.basename(hos[0])).group(1))
        if hn != n + 1:
            bad.append(f'{os.path.basename(hos[0])} is numbered S{hn}, but the newest Bible entry '
                       f'says S{n} just ran - the outgoing handoff is read by S{n + 1}')
    return bad


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

    for problem in session_numbers():
        print("  SESSION:", problem)
        bad += 1

    unrostered = roster_coverage()
    for f in unrostered:
        print("  ROSTER: %s is in the repo root and in no version roster - add it to"
              " ARTEFACTS, or to UNVERSIONED if it carries no version by design" % f)
    bad += len(unrostered)

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


def bible_consistency(path='ZUMO_SUPER_BIBLE.md'):
    """PARSE the Bible's version bookkeeping and return a list of disagreements.

    Deliberately NOT a grep. Bible 24.10 makes the parser the default instrument and
    allows grep only to read ONE line of KNOWN format -- and the defect this exists to
    catch was a SECOND value on that same line, which is precisely what a single-line
    grep cannot see. session_versions read 'Bible version: v8.88' correctly for nine
    versions while 'Current: **v8.79.1**' sat eleven words to its right, unread.

    Returns [] when the header version, the Current: field and the newest changelog
    entry all agree. Never raises on a missing field; a field that is absent is
    reported as absent, because silence would be indistinguishable from agreement.
    """
    problems = []
    try:
        lines = open(path, encoding='utf-8', errors='replace').read().splitlines()
    except OSError as e:
        return [f'{path}: cannot read ({e})']

    header = current = None
    header_line = None
    changelog = []          # (line_no, version) in file order

    for n, line in enumerate(lines, 1):
        st = line.strip()
        # The declaration line: the ONE home. Parse the WHOLE line, not its first match.
        if header is None and st.startswith('**Bible version:'):
            header_line = n
            m = re.search(r'\*\*Bible version:\s*v([\d.]+)\*\*', line)
            if m:
                header = m.group(1)
            c = re.search(r'Current:\s*\*\*v([\d.]+)\*\*', line)
            if c:
                current = c.group(1)
            continue
        # A changelog entry opens its own line: "v8.89, S103, moderate - ..."
        m = re.match(r'v([\d.]+),\s*S\d+,\s*(major|moderate|minor)\b', st)
        if m:
            changelog.append((n, m.group(1)))

    if header is None:
        problems.append(f'{path}: no "**Bible version: vX.Y**" declaration found')
        return problems
    if not changelog:
        problems.append(f'{path}: no changelog entries found to check the header against')
        return problems

    newest = changelog[0][1]
    if newest != header:
        problems.append(
            f'{path}:{header_line} header says v{header} but the newest changelog entry '
            f'(line {changelog[0][0]}) is v{newest} - a version with no entry beneath it')
    if current is None:
        problems.append(f'{path}:{header_line} the declaration line has no "Current:" field')
    elif current != header:
        problems.append(
            f'{path}:{header_line} header says v{header} but "Current:" on the SAME LINE '
            f'says v{current} - the one home disagrees with itself')
    return problems


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
        # S105: this seed named 'v03.20.0' as a LITERAL and stopped seeding anything the
        # moment L03 bumped - the control then reported a clean tree and FAILED loudly,
        # which is the right direction but the wrong reason. Seed by PATTERN so the control
        # cannot expire on a version bump (S104's rule: write controls for the world the
        # change creates).
        p = os.path.join(work, 'lessons', 'Lesson_03.html')
        s = open(p, encoding='utf-8').read()
        s2, n = re.subn(r'Lesson version: v[0-9.]+', 'Lesson version: v09.99.9', s, count=1)
        assert n == 1, 'control run: nothing was seeded, so nothing could be detected'
        open(p, 'w', encoding='utf-8').write(s2)
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

    print("CONTROL F (Bible self-consistency, both ways): header, Current: and the newest "
          "changelog entry must agree")
    # TWO defects shipped past this tool because it read one value off a line carrying two.
    # v8.88 had no changelog entry, and Current: sat nine versions stale INSIDE the
    # declaration line. Both are cheap to assert and neither ever was.
    _live = bible_consistency('ZUMO_SUPER_BIBLE.md')
    if _live:
        for _p in _live:
            print(f"   FAILED (clean direction). {_p}")
        return 1
    print("   clean direction: the live Bible agrees with itself")

    _tmpf = tempfile.mkdtemp()
    try:
        _fix = os.path.join(_tmpf, 'ZUMO_SUPER_BIBLE.md')
        # A fixture built CLEAN, then broken one way at a time. Bible 24.6b: a control
        # that never sees the clean state cannot tell a catch from a false alarm.
        _clean = ('# Bible\n\n'
                  '**Bible version: v9.02** - blah blah. Current: **v9.02**\n\n'
                  'v9.02, S200, moderate - newest entry.\n\n'
                  'v9.01, S199, moderate - older entry.\n')
        open(_fix, 'w', encoding='utf-8').write(_clean)
        if bible_consistency(_fix):
            print("   FAILED. A clean fixture was reported as broken:",
                  bible_consistency(_fix))
            return 1
        print("   clean fixture: silent")

        # BREAK 1 - header ahead of the changelog (the v8.88 defect exactly)
        open(_fix, 'w', encoding='utf-8').write(
            _clean.replace('**Bible version: v9.02**', '**Bible version: v9.03**'))
        _r = bible_consistency(_fix)
        if not any('no entry beneath it' in x for x in _r):
            print("   FAILED. A header with no changelog entry was NOT caught.")
            return 1
        print("   break 1 (header ahead of changelog): caught")

        # BREAK 2 - Current: stale on the same line (the v8.79.1 defect exactly)
        open(_fix, 'w', encoding='utf-8').write(
            _clean.replace('Current: **v9.02**', 'Current: **v8.79.1**'))
        _r = bible_consistency(_fix)
        if not any('disagrees with itself' in x for x in _r):
            print("   FAILED. A stale Current: field on the declaration line was NOT caught.")
            return 1
        print("   break 2 (stale Current: on the same line): caught")

        # BREAK 3 - Current: removed entirely. Absent must not read as agreeing.
        open(_fix, 'w', encoding='utf-8').write(
            _clean.replace(' Current: **v9.02**', ''))
        _r = bible_consistency(_fix)
        if not any('no "Current:" field' in x for x in _r):
            print("   FAILED. A MISSING Current: field was silently treated as agreement.")
            return 1
        print("   break 3 (Current: absent): caught, not mistaken for agreement\n")
    finally:
        shutil.rmtree(_tmpf, ignore_errors=True)

    print("CONTROL G (registered is not emitted): every ARTEFACTS key must appear in BOTH "
          "emitted blocks")
    # CONTROL E asks whether a tool is REGISTERED. font_stack_sweep was, and still never
    # reached LIVE.md or the handoff, because both emit templates name each instrument BY
    # HAND. Registration and emission are two different questions and only one was asked.
    # Found while closing S103 by reading the emitted block, not by any control - which is
    # the S102 lesson again: compare the output against something, do not trust the code.
    _missing = []
    _vals, _lessons, _errs = gather()
    if _errs:
        print(f"   SKIPPED: gather() reported {len(_errs)} error(s) - CONTROL A/B own that")
        _missing = None
    else:
        for _name, _fn in (('--live', emit_live), ('--handoff', emit_handoff)):
            _out = _fn(_vals, _lessons, 0, 0, 0, 'deadbee')
            for _lab, _rel, _pat in ARTEFACTS:
                # NO EXEMPTIONS. The first draft of this control excused 'Syllabus' on the
                # grounds that it is emitted under its filename - true of --live, FALSE of
                # --handoff, where it appeared under neither. An exemption that is not itself
                # checked is a hole, which is the very defect this control exists to catch.
                # DJ ruling S103: "to be safe shouldn't it be in both places?" - so it is,
                # and the exemption is gone rather than narrowed.
                if _lab not in _out and _rel not in _out:
                    _missing.append(f"{_lab} missing from {_name}")
    if _missing:
        for _m in _missing:
            print(f"   FAILED. {_m} - it is registered but will never be seen.")
        return 1
    if _missing is not None:
        print("   every registered artefact appears in both emitted blocks\n")

    print("ALL SEVEN CONTROLS PASS - silent when clean, loud when broken, both directions.")
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
