#!/usr/bin/env python3
"""prose_canon.py - does the book's PROSE still agree with canon?

WHY THIS EXISTS. All 78 gates run PAYLOAD -> LESSON. `gate_payload_match` asks whether every
payload line derives from its lesson, which is a SUBSET test (Bible 16.45): a lesson may carry
any number of extra lines no payload has, so STALE PROSE IS INVISIBLE TO THE WHOLE SUITE BY
CONSTRUCTION. That is the direction every S182 defect travelled, S183's rename defect travelled,
and S184's eleven sites travelled.

FOUR ARMS ARE OWED (S182, Bible 24.22). Only ARM 3 is built:

  ARM 1  printed banner SEQUENCES vs canon order   -- NOT BUILT
  ARM 2  placement claims ("above setup()")        -- NOT BUILT
  ARM 3  RETIRED NAMES                             -- BUILT HERE
  ARM 4  section-count claims ("seven sections")   -- NOT BUILT

Shipping one arm and calling the instrument done is exactly the failure 16.50 records, so the
three unbuilt arms are named in --check's own output rather than left for a reader to discover.

--- ARM 3, AND WHY ITS PREDICATE IS SHAPED THE WAY IT IS -------------------------------------

Bible 18.3a retires three SECTION names: CONFIGURATION -> CONSTANTS, STATE VARIABLES ->
GLOBAL VARIABLES, bare LOOP -> MAIN LOOP. 18.3b records that the retirement has failed three
times in three registers, each time because the predicate was the spelling somebody last saw.

THE HARD PART IS NOT FINDING THE WORDS, IT IS NOT CONVICTING THE LEGITIMATE ONES (16.15).
Measured before this file was written, over the live tree:

  "state variable"  L08 1 . L09 1 . L10 1 . L11 2 . bank L09 2 . bank L10 1   -- ALL state MACHINE
  "configuration"   L01 2 . L04 28 . L05 4 . L06 2 . L07 3 . L10 2 . L14 1    -- mostly JUMPERS

`state` is Lesson 9's word (`RobotState`, `currentState`, state machine) and `configuration` is
correct about sensor jumpers in L04/L05. A predicate that convicted those is a predicate somebody
switches off inside a session (rule 20), so the exemptions here are STRUCTURAL rather than a name
list somebody has to maintain:

  1. BANNER FORM is always a section reference, in any lesson: `// ===== CONFIGURATION =====`,
     `// ===== STATE VARIABLES =====`, `// ===== LOOP =====`. Unambiguous by construction.
  2. A HEADING or a Maker LABEL carrying a retired name is naming a section. Prose can be about
     a config file; a step title reading "Configuration Constants" cannot.
  3. ALL-CAPS in body text is a section reference - that is how this book writes section names.
  4. LOWERCASE prose is judged BY LESSON SCOPE, and the scope is 18.3a's own: it governs
     L01-L06. A state machine is not born until L09, so lowercase "state variable" in L01-L06
     is naming the section and the same words in L08+ are naming a RobotState.

STATED SCOPE LIMIT (rule 78). Lowercase "configuration" is NOT judged anywhere, because
"the three-sensor configuration" is correct English about hardware in exactly the band where the
section name would also be wrong, and no structural property separates them. S184's L06 finding
("Step 5 - Distance Configuration") is reached by arm 3 only because it sits in a HEADING. A
lowercase section reference to CONFIGURATION in running L01-L06 prose is a hole, and it is
declared here rather than papered over with a looser regex.

usage:
  python3 prose_canon.py            # ARM 3 over the whole book
  python3 prose_canon.py --check    # same, exit 1 on any finding
  python3 prose_canon.py --selftest # controls, both directions
exit 0 = no finding. exit 1 = a finding, or a control failed.
"""
import os, re, sys, glob, html

VERSION = 'v1.1.0'

ROOT = os.path.dirname(os.path.abspath(__file__))

# 18.3a's retired names. Spelled ONCE (rules 83/84).
RETIRED = {
    'CONFIGURATION':   'CONSTANTS',
    'STATE VARIABLES': 'GLOBAL VARIABLES',
    'LOOP':            'MAIN LOOP',
}

# 18.3a's own declared scope: "single-file programs, L01-L06".
SCOPE_LESSONS = set(range(1, 7))


# A retired name is retired as a NAME, and English inflects. `STATE VARIABLES` must also
# match `STATE VARIABLE`: S184's double check found `QUIZ_L03` B37 reading "a STATE VARIABLE"
# while the plural-only pattern stayed SILENT - the arm missing a site the HAND pass had
# caught. That is rule 59's shape inside the instrument built to end the guessing, and it
# was found by pointing the arm at the pre-fix clone rather than by re-reading it.
# ONE definition, every reader (rules 83/84).
def _pat(name):
    return r'\b' + re.escape(name).replace('VARIABLES', 'VARIABLES?') + r'\b'


def _lesson_no(path):
    m = re.search(r'Lesson_(\d+)\.html$', path)
    return int(m.group(1)) if m else None


def _strip_scripts(s):
    return re.sub(r'<(script|style)\b.*?</\1>', ' ', s, flags=re.S | re.I)


def _rendered(s):
    return re.sub(r'[ \t]+', ' ', html.unescape(re.sub(r'<[^>]+>', ' ', _strip_scripts(s))))


def _headings(s):
    """(text, raw) for every h1-h6 in the file, tags stripped."""
    out = []
    for m in re.finditer(r'<h([1-6])\b[^>]*>(.*?)</h\1>', _strip_scripts(s), re.S | re.I):
        out.append(html.unescape(re.sub(r'<[^>]+>', '', m.group(2))).strip())
    return out


def _maker_labels(maker_text):
    """Every KINDS label and comment title. Read from the ROW SHAPE rather than by
    evaluating JS, so this stays a text instrument with no node dependency."""
    out = []
    for m in re.finditer(r'\[\s*"([a-z0-9_]+)"\s*,\s*"((?:[^"\\]|\\.)*)"\s*,'
                         r'\s*(?:null|"(?:[^"\\]|\\.)*")\s*,'
                         r'\s*(?:null|"((?:[^"\\]|\\.)*)")', maker_text):
        kid, label, title = m.group(1), m.group(2), m.group(3) or ''
        for field, val in (('label', label), ('comment title', title)):
            if val:
                out.append((kid, field, val.encode().decode('unicode_escape')))
    return out


def _rows_in_scope(maker_text):
    """KINDS row ids belonging to lessons in 18.3a's scope band. Read from the
    `N: [` block structure, because a row id alone does not name its lesson."""
    ids = set()
    for m in re.finditer(r'^\s*(\d+):\s*\[', maker_text, re.M):
        if int(m.group(1)) not in SCOPE_LESSONS:
            continue
        depth, i = 0, m.end() - 1
        while i < len(maker_text):
            c = maker_text[i]
            if c == '[':
                depth += 1
            elif c == ']':
                depth -= 1
                if depth == 0:
                    break
            i += 1
        for r in re.finditer(r'\[\s*"([a-z0-9_]+)"\s*,', maker_text[m.end():i]):
            ids.add(r.group(1))
    return ids


def arm3(lessons=None, banks=None, maker=None):
    """-> list of (where, name, evidence). Empty list means every member matched or excused."""
    findings = []
    lessons = lessons if lessons is not None else sorted(glob.glob(os.path.join(ROOT, 'lessons', 'Lesson_*.html')))
    banks = banks if banks is not None else sorted(glob.glob(os.path.join(ROOT, 'quizzes', 'ZUMO_QUIZ_*.yaml')))
    maker = maker if maker is not None else os.path.join(ROOT, 'newproject.html')

    def frag(t, i, j):
        return re.sub(r'\s+', ' ', t[max(0, i - 70):j + 70]).strip()

    # ---- 1. BANNER FORM, every file, every lesson --------------------------------
    for path in lessons + [maker]:
        s = open(path, encoding='utf-8').read()
        t = _rendered(s) if path.endswith('.html') and 'Lesson_' in path else s
        for name in RETIRED:
            for m in re.finditer(r'//\s*=====\s*' + re.escape(name) + r'\s*=====', t):
                findings.append((os.path.basename(path), name,
                                 'retired BANNER: ' + frag(t, m.start(), m.end())))

    # ---- 2. HEADINGS -------------------------------------------------------------
    for path in lessons:
        if _lesson_no(path) not in SCOPE_LESSONS:
            continue   # 18.3a: "SCOPE: single-file programs, L01-L06"
        s = open(path, encoding='utf-8').read()
        for h in _headings(s):
            for name in RETIRED:
                if name == 'LOOP':
                    continue  # "The loop() Function" is the FUNCTION, not the section
                if re.search(_pat(name), h, re.I):
                    findings.append((os.path.basename(path), name,
                                     'retired name in a HEADING: ' + h))

    # ---- 3. MAKER LABELS ---------------------------------------------------------
    mtext = open(maker, encoding='utf-8').read()
    in_scope_rows = _rows_in_scope(mtext)
    for kid, field, val in _maker_labels(mtext):
        if kid not in in_scope_rows:
            continue   # 18.3a scope, same reason as the heading arm
        for name in RETIRED:
            if name == 'LOOP':
                continue
            if re.search(_pat(name), val, re.I):
                findings.append(('newproject.html', name,
                                 f'retired name in a Maker {field} ({kid}): {val}'))

    # ---- 4. ALL-CAPS IN BODY TEXT, and lowercase inside 18.3a's scope ------------
    for path in lessons:
        n = _lesson_no(path)
        t = _rendered(open(path, encoding='utf-8').read())
        if n not in SCOPE_LESSONS:
            continue   # 18.3a scope
        for name in RETIRED:
            if name == 'LOOP':
                continue
            for m in re.finditer(_pat(name), t):
                findings.append((os.path.basename(path), name,
                                 'retired name in CAPS: ' + frag(t, m.start(), m.end())))
        # lowercase, scope-judged: see the docstring for why only STATE VARIABLES
        if n in SCOPE_LESSONS:
            for m in re.finditer(r'\bstate variables?\b', t, re.I):
                if t[m.start():m.end()].isupper():
                    continue  # already reported above
                findings.append((os.path.basename(path), 'STATE VARIABLES',
                                 'retired name in L01-L06 prose: ' + frag(t, m.start(), m.end())))

    # ---- 5. BANKS ----------------------------------------------------------------
    for path in banks:
        bm = re.search(r'ZUMO_QUIZ_L(\d+)\.yaml$', path)
        if bm and int(bm.group(1)) not in SCOPE_LESSONS:
            continue   # 18.3a scope
        s = open(path, encoding='utf-8').read()
        body = '\n'.join(l for l in s.split('\n') if not l.lstrip().startswith('#'))  # 16.37: history
        for name in RETIRED:
            if name == 'LOOP':
                continue
            for m in re.finditer(_pat(name), body):
                findings.append((os.path.basename(path), name,
                                 'retired name in CAPS: ' + frag(body, m.start(), m.end())))

    # de-duplicate identical (where, name, evidence) triples
    seen, out = set(), []
    for f in findings:
        if f not in seen:
            seen.add(f)
            out.append(f)
    return out


# ---------------------------------------------------------------------------------
# KNOWN RESIDUE. S162's UNREAD_PINS shape, and for its reason: a gate that is red on a
# tree nobody is about to fix trains its readers to ignore red (v8.130), while deleting
# the finding loses it. Each entry is PINNED WITH A REASON and the list CAN ONLY SHRINK -
# new drift fails immediately, and a pin whose site no longer exists fails too, so the
# table cannot rot quietly.
#
# THE HUMAN-FACING TRACKER IS `ZUMO_FIX_TRACKER.md`, and it deliberately does NOT restate
# these rows - it points at `--residue`. Two homes with no comparator is two versions
# (24.18), which is the defect this file exists to stop.
# ---------------------------------------------------------------------------------
RESIDUE = {
    ('Lesson_05.html', 'CONFIGURATION',
     'retired name in a HEADING: 5.3 Configuration Constants'):
        'S184: real, out of the L01-L03 pass. Fix with the L04-L08 sweep.',
    ('Lesson_06.html', 'CONFIGURATION',
     'retired name in a HEADING: Step 5 \u2014 Distance Configuration (Discovery 6.4)'):
        'S184: real, out of the L01-L03 pass. Couples to the Maker label below.',
    ('Lesson_06.html', 'CONFIGURATION',
     'retired name in a HEADING: Step 9 \u2014 Turn Configuration (Discovery 6.7)'):
        'S184: real, out of the L01-L03 pass. Couples to the Maker label below.',
    ('newproject.html', 'CONFIGURATION',
     'retired name in a Maker label (discovery_6_4): Discovery 6.4 \u2014 Distance Configuration (Step 5)'):
        'S184: moves with L06 Step 5 - a label and its step title are one fix.',
    ('newproject.html', 'CONFIGURATION',
     'retired name in a Maker comment title (discovery_6_4): Discovery 6.4: Distance Configuration'):
        'S184: moves with L06 Step 5.',
    ('newproject.html', 'CONFIGURATION',
     'retired name in a Maker label (discovery_6_7): Discovery 6.7 \u2014 Turn Configuration (Step 9)'):
        'S184: moves with L06 Step 9.',
    ('newproject.html', 'CONFIGURATION',
     'retired name in a Maker comment title (discovery_6_7): Discovery 6.7: Turn Configuration'):
        'S184: moves with L06 Step 9.',
}


def partition(findings=None):
    """-> (new_drift, pinned_seen, orphan_pins).

    ORPHANS MATTER AS MUCH AS DRIFT (S138): a pin naming a site that no longer exists
    certifies nothing, and silently keeping it means the day somebody fixes the site the
    table still claims it is broken. Both directions are reported.
    """
    fs = findings if findings is not None else arm3()
    seen = set(fs)
    new = [f for f in fs if f not in RESIDUE]
    pinned = [f for f in fs if f in RESIDUE]
    orphan = [k for k in RESIDUE if k not in seen]
    return new, pinned, orphan


def coverage():
    """Rule 27: a scan of zero files passes. Take the denominator from the tree."""
    ls = glob.glob(os.path.join(ROOT, 'lessons', 'Lesson_*.html'))
    bs = glob.glob(os.path.join(ROOT, 'quizzes', 'ZUMO_QUIZ_*.yaml'))
    mk = os.path.exists(os.path.join(ROOT, 'newproject.html'))
    return len(ls), len(bs), mk


def report(strict=False):
    nl, nb, mk = coverage()
    print(f'prose_canon.py {VERSION} - ARM 3 (retired names)')
    print(f'  scanned {nl} lesson(s), {nb} bank(s), Maker present: {mk}')
    if nl != 16 or nb != 16 or not mk:
        print('  FAIL coverage: expected 16 lessons, 16 banks and the Maker')
        return 1
    new, pinned, orphan = partition()
    for where, name, ev in new:
        print(f'  FINDING  {where}: `{name}` is retired (-> {RETIRED[name]})')
        print(f'           {ev}')
    for k in orphan:
        print(f'  ORPHAN PIN  {k[0]}: pinned but no longer found - remove it from RESIDUE')
        print(f'              {k[2]}')
    print(f'  {len(new)} new finding(s) | {len(pinned)} pinned residue | {len(orphan)} orphan pin(s)')
    if pinned:
        print('  pinned residue (see ZUMO_FIX_TRACKER.md; --residue lists it):')
        for where, name, ev in pinned:
            print(f'      {where}: {ev[:88]}')
    print('  NOT BUILT: arm 1 (printed banner sequences) . arm 2 (placement claims) '
          '. arm 4 (section-count claims)')
    return 1 if ((new or orphan) and strict) else 0


# ---------------------------------------------------------------------------------
# CONTROLS. 16.50: a predicate built to confirm is not a control. Each control runs
# ONE mutation per invocation against a scratch copy, and every restore is md5-exact.
# Two directions per case: the defect must FIRE and the legitimate twin must be SILENT.
# ---------------------------------------------------------------------------------
def selftest():
    """CONTROLS. 16.50: a predicate built to confirm is not a control.

    EVERY CONTROL MEASURES A DELTA AGAINST THE LIVE BASELINE, NEVER AGAINST ZERO.
    An earlier draft asserted a CLEAN tree and would therefore have failed the moment
    the book had a real finding in it - the borrowed-fixture defect S166 found in
    `_good_bank()` and S171 found in `FINISHED_WARN_BASELINE`, where a control that
    leans on the population it audits breaks when you succeed. These test the ARM.

    One mutation per invocation, the plant asserted to have LANDED before the verdict
    is read, and every restore md5-exact.
    """
    import hashlib
    ok = True

    def md5(p):
        return hashlib.md5(open(p, 'rb').read()).hexdigest()

    baseline = arm3()
    bset = set(baseline)
    print(f'prose_canon.py {VERSION} --selftest')
    print(f'  BASELINE: {len(baseline)} finding(s) in the live tree '
          f'(controls measure the DELTA against this, never against zero)')

    def run(tag, path, old, new, expect_fire, needle=None):
        nonlocal ok
        before = md5(path)
        src = open(path, encoding='utf-8').read()
        if src.count(old) != 1:
            print(f'  CONTROL {tag}: FIXTURE BROKEN - anchor appears {src.count(old)} time(s)')
            ok = False
            return
        open(path, 'w', encoding='utf-8').write(src.replace(old, new))
        try:
            if md5(path) == before:
                print(f'  CONTROL {tag}: FAIL - the plant did not land')
                ok = False
                return
            delta = [f for f in arm3() if f not in bset]
            if needle is not None:
                delta = [f for f in delta if needle in f[2] or needle in f[0]]
            fired = bool(delta)
            good = (fired == expect_fire)
            note = f': {delta[0][2][:66]}' if delta else ''
            print(f'  CONTROL {tag}: {"PASS" if good else "FAIL"} '
                  f'(expected {"FIRE" if expect_fire else "SILENT"}, got '
                  f'{"FIRE" if fired else "SILENT"}{note})')
            if not good:
                ok = False
        finally:
            open(path, 'w', encoding='utf-8').write(src)
            if md5(path) != before:
                print(f'  CONTROL {tag}: RESTORE NOT md5-EXACT')
                ok = False

    L03 = os.path.join(ROOT, 'lessons', 'Lesson_03.html')
    L10 = os.path.join(ROOT, 'lessons', 'Lesson_10.html')
    MK = os.path.join(ROOT, 'newproject.html')
    B03 = os.path.join(ROOT, 'quizzes', 'ZUMO_QUIZ_L03.yaml')

    # A. STABILITY: two consecutive runs on an untouched tree must agree. If the arm
    #    is not deterministic, no delta below means anything.
    again = arm3()
    same = (again == baseline)
    print(f'  CONTROL A (determinism): {"PASS" if same else "FAIL"} - '
          f'two runs on the untouched tree {"agree" if same else "DISAGREE"}')
    ok = ok and same

    # B. S184's ACTUAL defect restored: a retired name in a step heading. Must FIRE.
    run('B (real S184 defect: heading)', L03,
        '<h3 class="h3-c-433014">Step 6: Global Variables</h3>',
        '<h3 class="h3-c-433014">Step 6: State Variables</h3>',
        True, needle='HEADING')

    # C. S184's OTHER real defect: a Maker label. Must FIRE.
    run('C (real S184 defect: Maker label)', MK,
        '"Discovery 3.3 \\u2014 Global Variables (Step 6)"',
        '"Discovery 3.3 \\u2014 State Variables (Step 6)"',
        True, needle='Maker')

    # D. lowercase prose INSIDE 18.3a's scope. Must FIRE.
    run('D (lowercase prose, in scope)', L03,
        '<p>Three new <strong>global variables</strong> remember',
        '<p>Three new <strong>state variables</strong> remember',
        True, needle='L01-L06 prose')

    # E. THE SAME WORDS OUTSIDE THE SCOPE BAND. Must be SILENT. This is the exemption
    #    proving itself rather than being asserted - L10 is a state-machine lesson.
    run('E (same words, L10 state machine)', L10,
        'It has a state machine that knows what it is doing',
        'It has state variables and a state machine that knows what it is doing',
        False)

    # F. banner form. Must FIRE.
    run('F (banner form)', L03,
        '<pre class="pre-m-0"><span class="tok-6a9955">// ===== CONSTANTS =====</span>',
        '<pre class="pre-m-0"><span class="tok-6a9955">// ===== CONFIGURATION =====</span>',
        True, needle='BANNER')

    # G. a bank asserting a retired name in caps. Must FIRE.
    run('G (bank, caps)', B03,
        'stem: "Which of these is a GLOBAL VARIABLE',
        'stem: "Which of these lives in the STATE VARIABLES section',
        True, needle='QUIZ_L03')

    # G2. THE SINGULAR, found by the S184 double check where the plural-only pattern
    #     was SILENT on `QUIZ_L03` B37's "a STATE VARIABLE". Must FIRE.
    run('G2 (singular caps form)', B03,
        'stem: "Which of these is a GLOBAL VARIABLE',
        'stem: "Which of these is a STATE VARIABLE',
        True, needle='QUIZ_L03')

    # H. BLINDING: reword prose carrying no retired name. Must be SILENT.
    run('H (blinding: no retired name)', L03,
        'These constants control the test behavior.',
        'These constants govern the test behavior.',
        False)

    # I. a legitimate lowercase "configuration" about jumpers, IN the scope band.
    #    Must be SILENT - the stated scope limit demonstrated, not claimed.
    run('I (jumper configuration, in band, legitimate)', L03,
        'These constants control the test behavior.',
        'These constants control the test behavior in the three-sensor configuration.',
        False)

    # J. L07+ is NOT governed by 18.3a. A retired name in an L07 heading must be SILENT.
    #    This is the scope exclusion that removed the false positive, proving itself.
    L07 = os.path.join(ROOT, 'lessons', 'Lesson_07.html')
    run('J (L07 out of scope: its heading really does carry the word)', L07,
        '<h3 class="h3-c-00474b">Configuration Constants (RobotConfig.h)</h3>',
        '<h3 class="h3-c-00474b">Configuration Constants and STATE VARIABLES (RobotConfig.h)</h3>',
        False)

    # ---- controls for the RESIDUE table itself -----------------------------------
    # K. A PINNED SITE MUST NOT COUNT AS NEW DRIFT. Without this the gate is red on a
    #    tree nobody is about to fix, which is what v8.130 says trains readers to
    #    ignore red. Asserted rather than assumed.
    new, pinned, orphan = partition()
    k_ok = (not new) and len(pinned) == len(RESIDUE) and not orphan
    print(f'  CONTROL K (residue absorbs, nothing else): '
          f'{"PASS" if k_ok else "FAIL"} - {len(new)} new, {len(pinned)} pinned, {len(orphan)} orphan')
    ok = ok and k_ok

    # L. AN ORPHAN PIN MUST FIRE. S138: a pin naming a site that no longer exists
    #    certifies nothing, and a table that cannot go stale loudly will go stale quietly.
    RESIDUE[('Lesson_99.html', 'CONFIGURATION', 'a site that does not exist')] = 'control L'
    try:
        _, _, orph = partition()
        l_ok = any(x[0] == 'Lesson_99.html' for x in orph)
        print(f'  CONTROL L (orphan pin fires): {"PASS" if l_ok else "FAIL"}')
        ok = ok and l_ok
    finally:
        del RESIDUE[('Lesson_99.html', 'CONFIGURATION', 'a site that does not exist')]

    # M. AN EMPTY TABLE MUST NOT PASS ON NO TRUTH - the residue must reappear as drift,
    #    which proves the table is ABSORBING findings rather than the arm having stopped
    #    seeing them (S166's "an emptied baseline still fires" shape).
    saved = dict(RESIDUE)
    RESIDUE.clear()
    try:
        nw, pn, _ = partition()
        m_ok = len(nw) == len(saved) and not pn
        print(f'  CONTROL M (emptied table re-reports {len(saved)}): '
              f'{"PASS" if m_ok else "FAIL"} - got {len(nw)} new, {len(pn)} pinned')
        ok = ok and m_ok
    finally:
        RESIDUE.update(saved)

    # N. A REAL NEW DEFECT MUST STILL FIRE WITH THE TABLE ARMED - the pin must not
    #    have blinded the arm. This is the whole risk of a residue table.
    run('N (new drift with the table armed)', L03,
        '<h3 class="h3-c-433014">Step 5: Constants</h3>',
        '<h3 class="h3-c-433014">Step 5: Configuration Constants</h3>',
        True, needle='HEADING')

    print('  ALL CONTROLS PASS' if ok else '  CONTROL FAILURE')
    return 0 if ok else 1


if __name__ == '__main__':
    args = sys.argv[1:]
    if '--selftest' in args:
        sys.exit(selftest())
    if '--residue' in args:
        new, pinned, orphan = partition()
        print(f'prose_canon.py {VERSION} --residue: {len(pinned)} pinned, '
              f'{len(new)} unpinned, {len(orphan)} orphan')
        for where, name, ev in pinned:
            print(f'  {where}\n      {ev}\n      reason: {RESIDUE[(where, name, ev)]}')
        sys.exit(0)
    sys.exit(report(strict='--check' in args))
