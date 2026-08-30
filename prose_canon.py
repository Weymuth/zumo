#!/usr/bin/env python3
"""prose_canon.py - does the book's PROSE still agree with canon?

WHY THIS EXISTS. All 78 gates run PAYLOAD -> LESSON. `gate_payload_match` asks whether every
payload line derives from its lesson, which is a SUBSET test (Bible 16.45): a lesson may carry
any number of extra lines no payload has, so STALE PROSE IS INVISIBLE TO THE WHOLE SUITE BY
CONSTRUCTION. That is the direction every S182 defect travelled, S183's rename defect travelled,
and S184's eleven sites travelled.

FOUR ARMS ARE OWED (S182, Bible 24.22). Three are built:

  ARM 1  printed banner SEQUENCES vs canon order   -- BUILT (S195)
  ARM 2  placement claims ("above setup()")        -- NOT BUILT
  ARM 3  RETIRED NAMES                             -- BUILT
  ARM 4  section-count claims ("seven sections")   -- BUILT (S195)

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

VERSION = 'v1.3.0'

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


# ---------------------------------------------------------------------------------
# ARM 4 - SECTION-COUNT CLAIMS
#
# WHY THIS SAT UNBUILT SINCE S182. The obvious predicate - "compare the number in
# the prose against the banner count of that lesson's payload" - CONVICTS L02 EIGHT
# TIMES AND L06 ONCE, all on correct prose. Measured S195 before a line was written.
#
# THE TWO NUMBERS ARE BOTH RIGHT AND THEY RECONCILE EXACTLY:
#
#   L02 teaches NINE:  Header . Includes . Objects . Constants . Global Variables .
#                      Prototypes . setup() . loop() . Helpers
#   A payload body ships SEVEN banners, starting at HARDWARE OBJECTS. The Maker's
#   mainCpp() wrapper AUTO-PREPENDS the header comment and the #include (S44), so
#   7 stored + 2 wrapper-supplied = 9. The canon and the file agree.
#
# So the discriminator is not the number, it is WHAT THE SENTENCE IS COUNTING:
#
#   CANON claim  ("every program", "always", "in this book")  -> expect CANON_TOTAL
#   FILE claim   ("your main.cpp", "against Section N")       -> expect banner count
#
# ANYTHING THIS CANNOT CLASSIFY IS REPORTED UNADJUDICATED, NOT CONVICTED (rule 78).
# A count claim whose subject is ambiguous is a question for a human, and printing
# it as a FINDING would be the same false conviction in a new costume.
# ---------------------------------------------------------------------------------
CANON_TOTAL = 9
WRAPPER_SUPPLIED = 2          # header comment + #include, prepended by mainCpp()

_CANON_CUE = re.compile(r'every program|any program|in this book|always|'
                        r'well-organized|an Arduino (?:program|sketch)|'
                        r'of an Arduino', re.I)
_FILE_CUE = re.compile(r'your main\.cpp|your program|your file|against Section|'
                       r'top to bottom|in this program', re.I)
# PLURAL, LOWERCASE, AND NOT CASE-FOLDED - ON PURPOSE. The book writes a section
# REFERENCE capitalised and singular ("Section 5", "the Version 2 section"), and a
# section COUNT lowercase and plural ("nine sections"). That is a structural
# separator, not a word list somebody has to maintain (16.15). Case-folding here
# dragged in "Five Section 5 showed", "one Section 3" and four "Version 2 section"
# hits, none of which counts anything.
_COUNT = re.compile(r'\b(one|two|three|four|five|six|seven|eight|nine|ten|\d{1,2})'
                    r'\s+(?:numbered\s+)?sections\b')
_WORD = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5,
         'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10}


def _banner_count(payload_body):
    return len(re.findall(r'// ===== ([A-Z][A-Z0-9 /_]*[A-Z]) =====',
                          payload_body or ''))


def arm4(lessons=None, payloads=None):
    """-> (findings, unadjudicated). findings are (where, claimed, expected, kind, ev).

    payloads: {lesson_no_str: banner_count}. Injectable so the controls can drive
    the arm without the Maker, and so a control can move the count underneath it.
    """
    findings, unknown = [], []
    lessons = lessons if lessons is not None else sorted(
        glob.glob(os.path.join(ROOT, 'lessons', 'Lesson_*.html')))
    if payloads is None:
        payloads = _live_payload_counts()

    for path in lessons:
        n = _lesson_no(path)
        text = _rendered(open(path, encoding='utf-8').read())
        text = re.sub(r'\s+', ' ', text)
        for m in _COUNT.finditer(text):
            raw = m.group(1).lower()
            claimed = _WORD.get(raw) or int(raw)
            lo = max((text.rfind(c, 0, m.start()) for c in '.!?:'), default=-1)
            hi = min((x for x in (text.find(c, m.end()) for c in '.!?')
                      if x != -1), default=len(text))
            ctx = text[lo + 1:hi + 1]
            ev = re.sub(r'\s+', ' ', ctx).strip()
            where = os.path.basename(path)
            is_canon = bool(_CANON_CUE.search(ctx))
            is_file = bool(_FILE_CUE.search(ctx))
            if is_canon and not is_file:
                if claimed != CANON_TOTAL:
                    findings.append((where, claimed, CANON_TOTAL, 'canon', ev))
            elif is_file and not is_canon:
                exp = payloads.get(str(n))
                if exp is None:
                    unknown.append((where, claimed, None, 'no payload', ev))
                elif claimed != exp:
                    findings.append((where, claimed, exp, 'file', ev))
            else:
                unknown.append((where, claimed, None,
                                'ambiguous subject', ev))
    return findings, unknown


def selftest_arm1():
    """CONTROLS FOR ARM 1.

    THE FIRST VERSION OF CONTROL A FAILED FOR THE WRONG REASON AND THAT IS THE
    LESSON HERE. It planted an inversion into an L03 block holding ONE banner - a
    block this arm correctly declines to judge - so the arm was silent and the
    control read as a failure of the arm. A control must plant where the arm
    LOOKS, and the plant must be asserted to have landed. Both are done below.
    """
    bad = []

    def check(name, ok, detail=''):
        print('   %-58s %s' % (name, 'PASS' if ok else 'FAIL ' + detail))
        if not ok:
            bad.append(name)

    import tempfile
    import shutil

    def one(text):
        with tempfile.TemporaryDirectory() as td:
            p = os.path.join(td, 'Lesson_02.html')
            open(p, 'w', encoding='utf-8').write(text)
            return arm1([p])[0]

    # A - a reversed PAIR fires; the same pair in canon order does not.
    check('A1 a reversed pair FIRES',
          len(one('<pre>// ===== MAIN LOOP =====\n'
                  '// ===== SETUP =====</pre>')) == 1)
    check('A2 the same pair in canon order is SILENT',
          not one('<pre>// ===== SETUP =====\n'
                  '// ===== MAIN LOOP =====</pre>'))

    # B - SUBSEQUENCE, not equality. Omitted sections are legal (18.3).
    check('B  a listing that omits sections is SILENT',
          not one('<pre>// ===== HARDWARE OBJECTS =====\n'
                  '// ===== SETUP =====\n// ===== MAIN LOOP =====</pre>'))

    # C - THE THREE SPINES ARE DISTINCT. A RobotConfig.h order is legal on its own
    #     spine and would be nonsense on main.cpp's - this is the control that
    #     would have caught a flat single-canon predicate.
    check('C1 a RobotConfig.h order is SILENT on its own spine',
          not one('<pre>// ===== PHYSICAL PROPERTIES =====\n'
                  '// ===== SPEED SETTINGS =====</pre>'))
    check('C2 a RobotConfig.h order REVERSED still FIRES',
          len(one('<pre>// ===== SPEED SETTINGS =====\n'
                  '// ===== PHYSICAL PROPERTIES =====</pre>')) == 1)

    # D - a banner repeated back-to-back is one section shown twice, not an order.
    check('D  a doubled banner is not an order claim',
          not one('<pre>// ===== SETUP =====\n// ===== SETUP =====</pre>'))

    # E - PLANT INTO A REAL, JUDGEABLE BLOCK. Swap the first and last banner of a
    #     block the arm actually examines, assert the substitution landed, and
    #     demand a restore is silent.
    live = sorted(glob.glob(os.path.join(ROOT, 'lessons', 'Lesson_*.html')))
    target = None
    for path in live:
        raw = open(path, encoding='utf-8').read()
        for m in _CODEBLOCK.finditer(raw):
            body = html.unescape(m.group(1) or m.group(2) or '')
            if len(set(_BANNER.findall(body))) >= 2:
                target = (path, m.group(0))
                break
        if target:
            break
    if not target:
        check('E  a judgeable block exists to plant into', False)
    else:
        path, block = target
        with tempfile.TemporaryDirectory() as td:
            p = os.path.join(td, os.path.basename(path))
            shutil.copy(path, p)
            raw = open(p, encoding='utf-8').read()
            seq = _BANNER.findall(html.unescape(block))
            a, z = seq[0], seq[-1]
            nb = (block.replace('// ===== %s =====' % a, '// ===== ZZ =====', 1)
                       .replace('// ===== %s =====' % z, '// ===== %s =====' % a, 1)
                       .replace('// ===== ZZ =====', '// ===== %s =====' % z, 1))
            check('E0 the plant actually landed', nb != block)
            open(p, 'w', encoding='utf-8').write(raw.replace(block, nb, 1))
            check('E1 a swap in a REAL judgeable block FIRES',
                  len(arm1([p])[0]) == 1)
            shutil.copy(path, p)
            check('E2 the restored file is SILENT', not arm1([p])[0])

    # F - the live tree, and its declared limit.
    f, judged, blind = arm1()
    check('F1 live tree has no arm-1 finding', not f, str(f[:1]))
    check('F2 the arm judged something at all', judged >= 20, '%d' % judged)
    check('F3 the blind lessons are REPORTED, not hidden',
          blind == [6, 10, 11, 12, 13, 14, 15], str(blind))

    print()
    print('  %d CONTROL(S) FAILED' % len(bad) if bad
          else '  ALL ARM-1 CONTROLS PASS - loud when broken, silent when clean.')
    return 1 if bad else 0


def selftest_arm4():
    """CONTROLS FOR ARM 4. Each must FIRE on a planted defect and be SILENT on its
    legitimate twin. Fixtures are synthetic - a control that leans on the corpus it
    audits breaks the moment the corpus is fixed (the S166/S171 defect)."""
    bad = []

    def check(name, ok, detail=''):
        print('   %-58s %s' % (name, 'PASS' if ok else 'FAIL ' + detail))
        if not ok:
            bad.append(name)

    import tempfile

    def run(prose, counts):
        with tempfile.TemporaryDirectory() as td:
            fp = os.path.join(td, 'Lesson_02.html')
            open(fp, 'w', encoding='utf-8').write('<p>%s</p>' % prose)
            return arm4([fp], counts)

    # A - a CANON claim with the wrong number FIRES; the right number is SILENT.
    f, _u = run('Every program in this book has eight sections.', {'2': 7})
    check('A1 canon claim with a wrong count FIRES', len(f) == 1, str(f))
    f, _u = run('Every program in this book has nine sections.', {'2': 7})
    check('A2 canon claim with the right count is SILENT', not f, str(f))

    # B - a FILE claim is judged against the PAYLOAD, not the canon. The number
    #     nine is CORRECT for the canon and WRONG for a file, so this pair also
    #     proves the two branches are actually distinct.
    f, _u = run('Compare your main.cpp top to bottom - nine sections.', {'2': 7})
    check('B1 file claim judged against the payload FIRES', len(f) == 1, str(f))
    f, _u = run('Compare your main.cpp top to bottom - seven sections.', {'2': 7})
    check('B2 file claim matching the payload is SILENT', not f, str(f))

    # C - THE CONTROL THAT WOULD HAVE CAUGHT THE FIRST DRAFT. The count must be
    #     read from the payload, not hardcoded: move the payload underneath the
    #     same prose and the verdict must flip.
    f7, _ = run('Compare your main.cpp top to bottom - seven sections.', {'2': 7})
    f9, _ = run('Compare your main.cpp top to bottom - seven sections.', {'2': 9})
    check('C  moving the payload count flips the verdict',
          not f7 and len(f9) == 1, '%s / %s' % (f7, f9))

    # D - AMBIGUOUS IS REPORTED, NEVER CONVICTED (rule 78).
    f, u = run('This section walks the nine sections one at a time.', {'2': 7})
    check('D1 an unclassifiable claim is not a finding', not f, str(f))
    check('D2 an unclassifiable claim IS reported', len(u) == 1, str(u))

    # E - a section REFERENCE is not a section COUNT. Capitalised and singular.
    f, u = run('Section 5 showed the code. The Version 2 section closes it.',
               {'2': 7})
    check('E  a capitalised singular reference is not counted',
          not f and not u, '%s / %s' % (f, u))

    # F - the live tree, priced by the live parser, is CLEAN.
    lf, lu = arm4()
    check('F  live tree has no arm-4 finding', not lf, str(lf[:2]))
    check('G  every lesson with a finished payload got a count',
          len(_live_payload_counts()) >= 14,
          '%d priced' % len(_live_payload_counts()))

    print()
    print('  %d CONTROL(S) FAILED' % len(bad) if bad
          else '  ALL ARM-4 CONTROLS PASS - loud when broken, silent when clean.')
    return 1 if bad else 0


def _live_payload_counts():
    """Banner count of each lesson's `finished` payload, via the SAME brace parser
    gate_payload_match uses. A regex over newproject.html would find banners in
    changelog prose too - the parser is the only thing that answers (24.22)."""
    import importlib.util
    p = os.path.join(ROOT, 'gate_payload_match.py')
    sp = importlib.util.spec_from_file_location('_gpm', p)
    g = importlib.util.module_from_spec(sp)
    sp.loader.exec_module(g)
    js = open(os.path.join(ROOT, 'newproject.html'), encoding='utf-8').read()
    P, _ = g.brace_json(js, 'var PAYLOADS = ')
    out = {}
    for k, v in (P or {}).items():
        b = (v or {}).get('finished')
        if isinstance(b, dict):
            # L07+ ship the eight-file architecture: `finished` is keyed by
            # FILENAME, and a section-count claim is about main.cpp.
            b = b.get('main.cpp') or b.get('main') or ''
        if isinstance(b, str) and b:
            out[k] = _banner_count(b)
    return out


# ---------------------------------------------------------------------------------
# ARM 1 - PRINTED BANNER SEQUENCES vs CANON ORDER
#
# THERE IS NO SINGLE CANON ORDER, AND ASSUMING ONE IS THE TRAP. Derived S195 from
# all 367 payload bodies carrying 2+ banners: EIGHT distinct orderings, resolving to
# THREE spines. A flat canon would have convicted 292 of the 367.
#
#   main.cpp        INCLUDES > HARDWARE OBJECTS > CONSTANTS > GLOBAL VARIABLES >
#                   FUNCTION PROTOTYPES > SETUP > MAIN LOOP > HELPER FUNCTIONS
#   RobotConfig.h   PHYSICAL PROPERTIES > TURNING PROPERTIES > SPEED SETTINGS >
#                   BATTERY THRESHOLDS
#   setup-sub       GLOBAL VARIABLES > SETUP > BATTERY REPORT > LINE SENSOR SETUP >
#                   CALIBRATION > MAIN LOOP        (sub-banners INSIDE setup())
#
# THE TEST IS SUBSEQUENCE, NOT EQUALITY. A listing legitimately omits sections it
# does not need - 18.3's "an empty section is not a mistake" - so the observed order
# must be a SUBSEQUENCE of some spine, never equal to one.
#
# BOUNDARIES ARE <pre>/<code> ELEMENTS, NOT BANNER NAMES. A first draft segmented on
# banner names and reported 22 findings, every one an artefact of gluing two separate
# listings together. Measured: 203 of 203 banner occurrences in the book sit inside a
# <pre> or <code>, so the element boundary is total coverage of the phenomenon.
#
# STATED COVERAGE LIMIT (rule 78). A block needs 2+ DISTINCT banners to have an order
# at all, so this arm judges 23 blocks and SEVEN LESSONS HAVE NONE (L06, L10-L15).
# CLEAN HERE DOES NOT MEAN THOSE LESSONS WERE CHECKED. The count and the blind
# lessons are printed by report() rather than left for a reader to infer.
# ---------------------------------------------------------------------------------
SPINES = {
    'main.cpp': ['INCLUDES', 'HARDWARE OBJECTS', 'CONSTANTS', 'GLOBAL VARIABLES',
                 'FUNCTION PROTOTYPES', 'SETUP', 'MAIN LOOP', 'HELPER FUNCTIONS'],
    'RobotConfig.h': ['PHYSICAL PROPERTIES', 'TURNING PROPERTIES',
                      'SPEED SETTINGS', 'BATTERY THRESHOLDS'],
    'setup-sub': ['GLOBAL VARIABLES', 'SETUP', 'BATTERY REPORT',
                  'LINE SENSOR SETUP', 'CALIBRATION', 'MAIN LOOP'],
}
_BANNER = re.compile(r'// ===== ([A-Z][A-Z0-9 /_]*[A-Z]) =====')
_CODEBLOCK = re.compile(r'<pre[^>]*>(.*?)</pre>|<code[^>]*>(.*?)</code>', re.S)


def _subsequence(observed, spine):
    it = iter(spine)
    return all(x in it for x in observed)


def arm1(lessons=None):
    """-> (findings, judged, blind).

    findings: (where, observed_order, evidence)
    judged:   how many blocks actually had an order to check
    blind:    lesson numbers with NO judgeable block - the declared limit
    """
    findings, judged, seen = [], 0, set()
    lessons = lessons if lessons is not None else sorted(
        glob.glob(os.path.join(ROOT, 'lessons', 'Lesson_*.html')))
    for path in lessons:
        raw = open(path, encoding='utf-8').read()
        for m in _CODEBLOCK.finditer(raw):
            body = html.unescape(m.group(1) or m.group(2) or "")
            seq = _BANNER.findall(body)
            # a banner repeated back-to-back is one section shown twice, not an
            # order claim; collapse before judging.
            ded = [x for i, x in enumerate(seq) if i == 0 or x != seq[i - 1]]
            if len(set(ded)) < 2:
                continue
            judged += 1
            seen.add(_lesson_no(path))
            if not any(_subsequence(ded, s) for s in SPINES.values()):
                findings.append((os.path.basename(path), ded,
                                 ' > '.join(ded)))
    blind = [n for n in range(1, 17) if n not in seen]
    return findings, judged, blind


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
    f1, judged1, blind1 = arm1()
    print(f'  ARM 1 (printed banner sequences): {len(f1)} finding(s), '
          f'{judged1} block(s) judged')
    for where, _obs, ev in f1:
        print(f'  FINDING  {where}: banner order is not a subsequence of any spine')
        print(f'           {ev[:100]}')
    if blind1:
        print('      COVERAGE LIMIT: no judgeable block in lesson(s) '
              + ', '.join(str(x) for x in blind1)
              + ' - clean here does NOT mean they were checked')

    f4, u4 = arm4()
    print(f'  ARM 4 (section-count claims): {len(f4)} finding(s), '
          f'{len(u4)} unadjudicated')
    for where, claimed, exp, kind, ev in f4:
        print(f'  FINDING  {where}: claims {claimed} sections, {kind} expects {exp}')
        print(f'           {ev[:100]}')
    for where, claimed, _e, kind, ev in u4:
        print(f'      unadjudicated ({kind}) {where}: "{ev[:74]}"')
    print('  NOT BUILT: arm 2 (placement claims)')
    return 1 if ((new or orphan or f4 or f1) and strict) else 0


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
