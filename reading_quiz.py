#!/usr/bin/env python3
"""reading_quiz.py - build a Canvas reading quiz from an EXPLICIT bank-id selection.

  python3 quizzes/reading_quiz.py --check            validate every registered selection
  python3 quizzes/reading_quiz.py --status           print each lesson's in-scope pool
  python3 quizzes/reading_quiz.py --build L03        write the keyed .md and the QTI zip
  python3 quizzes/reading_quiz.py --selftest         bidirectional controls
  python3 quizzes/reading_quiz.py --help

exit 0 = clean.  exit 1 = a control failed or a selection is out of scope.
exit 2 = an argument this tool does not recognize.

AN UNRECOGNIZED ARGUMENT IS REFUSED, NOT IGNORED (S174 rule). There is no
fall-through branch: a typo of --check does not silently write a package.

WHY THIS EXISTS (S200)
    The reading quiz is a GATE OVER THE ASSIGNED READING. S199 found L01's quiz
    drawing two of eight questions from §6 and §7 - building and uploading - while
    Assignment 1 read §1-§5 and explicitly parked §6-§7 for class. A QUARTER OF THE
    POINTS WERE UNANSWERABLE BY A STUDENT WHO DID EXACTLY WHAT WAS ASKED.

    That was fixed by hand. The same defect was then measured, unshipped, in the
    L03 and L04 pools: 11 of L03's 61 `before` questions and 21 of L04's 51 cite
    §6, §8, §8A or §9. Nothing was broken yet because no quiz had been selected -
    and that is exactly the window in which a rule that lives only in a sentence
    gets forgotten. THE THIRD HAND-BUILD IS THE ONE THAT BECOMES AN INSTRUMENT.

    So the scope rule is not documentation here. It is a REFUSAL: a selection
    naming a question whose cite reaches outside §1-§5 does not build.

WHY THE SELECTION LIVES IN THIS FILE
    ONE HOME. The eight ids are the assessment. Kept in the .md they would be a
    description of an artefact rather than the artefact (S197), and S200 found
    exactly that failure in the other direction - two copies of L01's keyed .md,
    one carrying the retired S194 selection in the present tense.

WHAT THIS TOOL DOES NOT DO
    It does not rebuild L01's committed package. That zip is already imported into
    Canvas; its item idents were generated randomly in S194 and cannot be
    reproduced, so L01 is registered for --check coverage only. Rebuilding it would
    hand DJ a package whose questions are identical and whose idents are not.

ONE VERSION HOME. The version lives ONLY in the VERSION constant.
A LIBRARY MAY NOT EXIT: no sys.exit() outside main().
"""
import os
import re
import sys
import glob
import html
import hashlib
import zipfile
import tempfile
import xml.dom.minidom

try:
    import yaml
except ImportError:  # pragma: no cover - the repo ships PyYAML
    yaml = None

VERSION = 'v1.0'

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)

# THE SCOPE RULE, IN ONE PLACE. A cite token is IN SCOPE when it names a section
# numbered 1 through 5. Everything else - §6 Build, §7 Verify, §8 Diagnose,
# §8A Going Deeper, §9 Challenges, and the bare 'Glossary' / 'Quick Reference'
# tokens - is out, because none of it is what the assignment asked a student to
# read. THE TEST IS ON THE WHOLE CITE, NOT ON ITS FIRST TOKEN: a question citing
# '§5.4, §6 Step 7' is a §6 question wearing a §5 hat.
IN_SCOPE = re.compile(r'^§([1-5])(\.|$|\s)')


def _cites(q):
    return [c.strip() for c in re.split(r'[,;]', str(q.get('cite', ''))) if c.strip()]


def in_scope(q):
    cs = _cites(q)
    return bool(cs) and all(IN_SCOPE.match(c) for c in cs)


# (lesson, title, closes, ids, why) - the ids ARE the quiz.
SELECTIONS = {
    'L01': dict(
        title='Lesson 1 Reading Quiz — Hello, Robot!',
        closes='when class starts **Wednesday September 9, 9:50 AM**',
        # S199's rescope, registered here for --check coverage. NOT rebuilt: see the
        # module docstring. The committed zip is the artefact Canvas already holds.
        rebuild=False,
        ids=['L01_B04', 'L01_B10', 'L01_B37', 'L01_B38',
             'L01_B15', 'L01_B21', 'L01_B17', 'L01_B32'],
        why=('Every one of them is answerable from the assigned reading, §1–§5, and none of them '
             'needs the robot. **Ruled S199: this quiz is over the reading, not the build.** '
             'Q8 is the can\'t-skim question: it asks the student to trace a loop rather than '
             'recognise a sentence.'),
    ),
    'L03': dict(
        title='Lesson 3 Reading Quiz — Motors & TRIM',
        closes='when class starts **Wednesday September 16, 9:50 AM**',
        rebuild=True,
        ids=['L03_B01', 'L03_B07', 'L03_B13', 'L03_B15',
             'L03_B18', 'L03_B22', 'L03_B33', 'L03_B38'],
        why=('Eight sections, eight questions — §1, §3.2, §3.3, §3.5, §3.6, §3.7, §4.2 and §5.5. '
             'Nothing here draws on §6–§9: building the TRIM Finder, measuring the number and the '
             'challenges are all class work. **Q4 is the one that must not be misremembered** — '
             'TRIM adjusts the LEFT motor, in this lesson and every lesson after it. Q8 is the '
             'can\'t-skim question: it asks what `if (trimValue = 5)` actually does, which a '
             'student who skimmed will read as a comparison.'),
    ),
    'L04': dict(
        title='Lesson 4 Reading Quiz — Line Sensors',
        closes='when class starts **Monday September 21, 1:15 PM**',
        rebuild=True,
        ids=['L04_B01', 'L04_B02', 'L04_B06', 'L04_B11',
             'L04_B15', 'L04_B17', 'L04_B21', 'L04_B19'],
        why=('Seven sections across §3, §4 and §5. Nothing here draws on §6–§9: the build, the '
             'three-versus-five comparison, the exit ritual and the challenges are all class work. '
             '**Q4 is the operationally important one** — calibration lives in RAM and does not '
             'survive power-off, which is the fact a student will otherwise rediscover the hard '
             'way in Lesson 8 and again at a competition. Q8 is the can\'t-skim question: the '
             'centre sensor is `lineSensorValues[1]` in three-sensor mode, and `[2]` — the '
             'plausible wrong answer — is the five-sensor answer.'),
    ),
}


def load_bank(lesson):
    path = os.path.join(HERE, 'ZUMO_QUIZ_%s.yaml' % lesson)
    with open(path, encoding='utf-8') as fh:
        return yaml.safe_load(fh)


def pool(lesson):
    """Every `before` question whose whole cite is inside §1-§5."""
    bank = load_bank(lesson)
    return [q for q in bank['sets']['before']['questions'] if in_scope(q)]


def validate(lesson, ids=None):
    """Findings for one selection. EMPTY LIST = clean.

    Reports rather than raises, because a caller that wants every finding must not
    be stopped by the first one - a suite that dies on entry number one cannot tell
    you whether entry number two was also broken.
    """
    sel = SELECTIONS[lesson]
    ids = list(sel['ids'] if ids is None else ids)
    bank = load_bank(lesson)
    before = {q['id']: q for q in bank['sets']['before']['questions']}
    after = {q['id'] for q in bank['sets'].get('after', {}).get('questions', [])}
    out = []
    seen = set()
    for qid in ids:
        if qid in seen:
            out.append((qid, 'named twice in the same selection'))
            continue
        seen.add(qid)
        if qid in after:
            out.append((qid, 'is in the AFTER set - that is the post-build check, not the gate'))
        elif qid not in before:
            out.append((qid, 'is not in this bank\'s before set'))
        elif not in_scope(before[qid]):
            out.append((qid, 'cites %s - OUTSIDE the assigned reading §1-§5'
                        % ', '.join(_cites(before[qid]))))
    if len(ids) != 8:
        out.append(('(selection)', 'has %d questions; the quiz is 8 points' % len(ids)))
    return out


# --- QTI ---------------------------------------------------------------------
# IDENTS ARE DERIVED, NOT RANDOM. S194 generated L01's idents with a random source,
# which means that package cannot be rebuilt - the questions would match and the
# idents would not, and a second import into Canvas would land as a different quiz.
# A hash of (lesson, bank id) makes a rebuild byte-stable, so regenerating after a
# typo fix produces the SAME package rather than a new one.
def _ident(prefix, *parts):
    h = hashlib.sha256('\u241f'.join(parts).encode('utf-8')).hexdigest()[:32]
    return prefix + h


def _esc(text):
    return html.escape('<p>%s</p>' % html.escape(str(text)), quote=False)


def build_xml(lesson):
    sel = SELECTIONS[lesson]
    bank = load_bank(lesson)
    before = {q['id']: q for q in bank['sets']['before']['questions']}
    aid = _ident('g', lesson, sel['title'])
    parts = ['<?xml version="1.0" encoding="UTF-8"?>',
             '<questestinterop xmlns="http://www.imsglobal.org/xsd/ims_qtiasiv1p2"',
             ' xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"',
             ' xsi:schemaLocation="http://www.imsglobal.org/xsd/ims_qtiasiv1p2'
             ' http://www.imsglobal.org/xsd/ims_qtiasiv1p2p1.xsd">',
             ' <assessment ident="%s" title="%s">' % (aid, html.escape(sel['title'])),
             '  <qtimetadata>',
             '   <qtimetadatafield><fieldlabel>cc_maxattempts</fieldlabel>'
             '<fieldentry>1</fieldentry></qtimetadatafield>',
             '  </qtimetadata>',
             '  <section ident="root_section">']
    for qid in sel['ids']:
        q = before[qid]
        iid = _ident('i', lesson, qid)
        opts = q['options']
        # THE CORRECT ANSWER SHIPS IN SLOT a0 (S194 canon) and Canvas shuffles at
        # delivery. A slot number is not a position on the student's screen.
        ordered = ([o for o in opts if o.get('correct')] +
                   [o for o in opts if not o.get('correct')])
        labels = ''.join(
            '<response_label ident="%s_a%d"><material><mattext texttype="text/html">%s'
            '</mattext></material></response_label>' % (iid, i, _esc(o['text']))
            for i, o in enumerate(ordered))
        parts += [
            '   <item ident="%s" title="%s">' % (iid, qid),
            ' <itemmetadata><qtimetadata>',
            '  <qtimetadatafield><fieldlabel>question_type</fieldlabel>'
            '<fieldentry>multiple_choice_question</fieldentry></qtimetadatafield>',
            '  <qtimetadatafield><fieldlabel>points_possible</fieldlabel>'
            '<fieldentry>1.0</fieldentry></qtimetadatafield>',
            ' </qtimetadata></itemmetadata>',
            ' <presentation>',
            '  <material><mattext texttype="text/html">%s</mattext></material>' % _esc(q['stem']),
            '  <response_lid ident="response1" rcardinality="Single">',
            '   <render_choice>%s</render_choice>' % labels,
            '  </response_lid>',
            ' </presentation>',
            ' <resprocessing>',
            '  <outcomes><decvar maxvalue="100" minvalue="0" varname="SCORE"'
            ' vartype="Decimal"/></outcomes>',
            '  <respcondition continue="No">',
            '   <conditionvar><varequal respident="response1">%s_a0</varequal></conditionvar>'
            % iid,
            '   <setvar action="Set" varname="SCORE">100</setvar>',
            '  </respcondition>',
            ' </resprocessing>',
            '</item>']
    parts += ['  </section>', ' </assessment>', '</questestinterop>']
    return aid, '\n'.join(parts)


def build_manifest(lesson, aid):
    return '\n'.join([
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<manifest identifier="zumo_%s_reading_quiz_manifest"' % lesson.lower(),
        ' xmlns="http://www.imsglobal.org/xsd/imsccv1p1/imscp_v1p1"',
        ' xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"',
        ' xsi:schemaLocation="http://www.imsglobal.org/xsd/imsccv1p1/imscp_v1p1'
        ' http://www.imsglobal.org/profile/cc/ccv1p1/ccv1p1_imscp_v1p2_v1p0.xsd">',
        ' <metadata><schema>IMS Content</schema><schemaversion>1.1.3</schemaversion></metadata>',
        ' <organizations/>',
        ' <resources>',
        '  <resource identifier="%s" type="imsqti_xmlv1p2">' % aid,
        '   <file href="%s/%s.xml"/>' % (aid, aid),
        '  </resource>',
        ' </resources>',
        '</manifest>'])


def build_md(lesson):
    sel = SELECTIONS[lesson]
    bank = load_bank(lesson)
    before = {q['id']: q for q in bank['sets']['before']['questions']}
    n_pool = len(pool(lesson))
    n_before = len(bank['sets']['before']['questions'])
    zipname = 'ZUMO_%s_Reading_Quiz_CANVAS_QTI.zip' % lesson
    L = [
        '<!-- ZUMO_%s_Reading_Quiz.md %s — GENERATED by quizzes/reading_quiz.py %s.'
        % (lesson, 'v1.0', VERSION),
        '     Do not hand-edit: the selection lives in that script, which refuses an id',
        '     citing anything outside §1–§5. Rebuild with --build %s. -->' % lesson,
        '',
        '# %s' % sel['title'].replace('Reading Quiz — ', 'Reading Quiz — '),
        '### Fall 2026 · D Block · closes %s' % sel['closes'],
        '',
        '> **Fallback copy.** The importable package is `%s`. If Canvas' % zipname,
        '> refuses the import, build the quiz by hand from this page — the correct answer is'
        ' marked **✅**.',
        '> **One attempt, auto-graded, 8 points.** This is a gate, not an exam.',
        '',
        '**Why these eight.** %s' % sel['why'],
        '',
        '---',
        '']
    for n, qid in enumerate(sel['ids'], 1):
        q = before[qid]
        L += ['### %d. %s' % (n, q['stem']),
              '*Source: %s · bank id `%s` · %d point*' % (q['cite'], qid, q.get('points', 1)),
              '']
        opts = ([o for o in q['options'] if o.get('correct')] +
                [o for o in q['options'] if not o.get('correct')])
        for o in opts:
            L.append('- **✅ %s**' % o['text'] if o.get('correct') else '- %s' % o['text'])
        L.append('')
    L += ['---',
          '',
          '## If you swap a question',
          '',
          'The full %s bank is `quizzes/ZUMO_QUIZ_%s.yaml` — **%d questions in the `before` set,'
          ' of which %d cite §1–§5 and nothing else.** That is the pool.'
          % (lesson, lesson, n_before, n_pool),
          '',
          '**Do not draw from §6, §7, §8 or §9** — those are class work, not the assigned reading,'
          ' and a question from them tests something the assignment never asked for. You do not'
          ' have to remember this: edit `SELECTIONS` in `quizzes/reading_quiz.py` and an'
          ' out-of-scope id refuses to build.',
          '',
          '---',
          '*Generated from the %s bank by `reading_quiz.py` %s · Fall Term 2026*'
          % (lesson, VERSION),
          '']
    return '\n'.join(L)


def build(lesson, outdir=None):
    outdir = outdir or ROOT
    findings = validate(lesson)
    if findings:
        return findings
    aid, xml_text = build_xml(lesson)
    # WELL-FORMEDNESS IS ASSERTED BEFORE THE ZIP IS WRITTEN, not after. A malformed
    # package that reaches DJ's hands is discovered by Canvas, which reports it as an
    # import failure ten minutes before class.
    xml.dom.minidom.parseString(xml_text.encode('utf-8'))
    md = build_md(lesson)
    with open(os.path.join(outdir, 'ZUMO_%s_Reading_Quiz.md' % lesson), 'w',
              encoding='utf-8') as fh:
        fh.write(md)
    zpath = os.path.join(outdir, 'ZUMO_%s_Reading_Quiz_CANVAS_QTI.zip' % lesson)
    # A ZIP RECORDS A TIMESTAMP. Left to default it is the clock, so two builds of the
    # same selection would differ in bytes and control H could never pass - the very
    # property that makes a rebuild safe to hand over.
    with zipfile.ZipFile(zpath, 'w', zipfile.ZIP_DEFLATED) as z:
        for name, payload in (('%s/%s.xml' % (aid, aid), xml_text),
                              ('imsmanifest.xml', build_manifest(lesson, aid))):
            info = zipfile.ZipInfo(name, date_time=(1980, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            z.writestr(info, payload)
    return []


# --- CONTROLS ----------------------------------------------------------------
def selftest():
    ok = True

    def report(name, passed, note=''):
        nonlocal ok
        ok = ok and passed
        print('   %-4s %-56s %s%s' % ('PASS' if passed else 'FAIL', name,
                                      'PASS' if passed else 'FAIL',
                                      (' - ' + note) if note else ''))

    # A - every registered selection is clean. The blinding control: silence here
    #     is only meaningful if the loud controls below actually go loud.
    for lesson in sorted(SELECTIONS):
        report('A %s registered selection is clean' % lesson,
               validate(lesson) == [])

    # B - an id from §6/§8/§9 is REFUSED. This is the S199 defect, planted.
    bank = load_bank('L04')
    outsiders = [q['id'] for q in bank['sets']['before']['questions'] if not in_scope(q)]
    report('B an out-of-scope id is LOUD',
           bool(outsiders) and any('OUTSIDE' in why for _, why in
                                   validate('L04', SELECTIONS['L04']['ids'][:7] + outsiders[:1])),
           'planted %s' % (outsiders[0] if outsiders else 'nothing'))

    # C - an id that does not exist is LOUD. A typo is not a silent drop.
    report('C an unknown id is LOUD',
           any('not in this bank' in why for _, why in
               validate('L03', SELECTIONS['L03']['ids'][:7] + ['L03_B999'])))

    # D - an AFTER-set id is LOUD even though it is a real question in a real bank.
    after = [q['id'] for q in load_bank('L03')['sets']['after']['questions']]
    report('D an AFTER-set id is LOUD',
           bool(after) and any('AFTER set' in why for _, why in
                               validate('L03', SELECTIONS['L03']['ids'][:7] + after[:1])))

    # E - the same id twice is LOUD. Eight slots filled by seven questions still
    #     counts to eight, so a length check alone cannot see this.
    dup = SELECTIONS['L03']['ids'][:7] + [SELECTIONS['L03']['ids'][0]]
    report('E a duplicated id is LOUD',
           any('twice' in why for _, why in validate('L03', dup)))

    # F - a mixed cite is out of scope. '§5.4, §6 Step 7' is a §6 question wearing
    #     a §5 hat, and testing only the first token would pass it.
    report('F a mixed cite is OUT of scope',
           not in_scope({'cite': '§5.4, §6 Step 7'}) and in_scope({'cite': '§5.4, §3.1'}))

    # G - §5 is in and §6 is out at the BOUNDARY, and a bare word is out.
    report('G the scope boundary holds',
           in_scope({'cite': '§5'}) and not in_scope({'cite': '§6'})
           and not in_scope({'cite': 'Quick Reference'})
           and not in_scope({'cite': '§8A.6'}))

    # H - a built package parses, and REBUILDING IT IS BYTE-IDENTICAL. A random
    #     ident makes a rebuild a different artefact; that is why L01 cannot be
    #     rebuilt at all, and this control is what keeps L03/L04 out of that trap.
    with tempfile.TemporaryDirectory() as d1, tempfile.TemporaryDirectory() as d2:
        f1, f2 = build('L03', d1), build('L03', d2)
        z1 = open(os.path.join(d1, 'ZUMO_L03_Reading_Quiz_CANVAS_QTI.zip'), 'rb').read()
        z2 = open(os.path.join(d2, 'ZUMO_L03_Reading_Quiz_CANVAS_QTI.zip'), 'rb').read()
        report('H a rebuild is byte-identical', f1 == [] and f2 == [] and z1 == z2)

    # I - the correct answer really is in slot a0, read back out of the XML rather
    #     than asserted. A generator that scores a1 would pass every other control.
    _, x = build_xml('L03')
    d = xml.dom.minidom.parseString(x.encode('utf-8'))
    good = True
    bank3 = {q['id']: q for q in load_bank('L03')['sets']['before']['questions']}
    for item in d.getElementsByTagName('item'):
        iid = item.getAttribute('ident')
        first = item.getElementsByTagName('response_label')[0].getAttribute('ident')
        keyed = item.getElementsByTagName('varequal')[0].firstChild.data
        want = [o['text'] for o in bank3[item.getAttribute('title')]['options']
                if o.get('correct')][0]
        shown = item.getElementsByTagName('response_label')[0] \
            .getElementsByTagName('mattext')[0].firstChild.data
        # THE HTML LAYER IS DECODED BY A DIFFERENT DECODER THAN THE ONE THAT WROTE IT.
        # Comparing against this module's own escaper would agree with a mangled
        # generator - the S199 failure where three strippers agreed because they were
        # identical on the step that was wrong. minidom undoes the XML layer,
        # html.unescape undoes the HTML layer, and neither is _esc.
        good = good and first == iid + '_a0' and keyed == iid + '_a0' \
            and want in html.unescape(shown)
    report('I the keyed slot a0 holds the correct text', good)

    print()
    print('  ALL CONTROLS PASS' if ok else '  CONTROLS FAILED')
    return 0 if ok else 1


def status():
    print('reading_quiz.py %s - the selection is the assessment.' % VERSION)
    for lesson in sorted(SELECTIONS):
        bank = load_bank(lesson)
        b = bank['sets']['before']['questions']
        p = pool(lesson)
        sel = SELECTIONS[lesson]
        print('  %s  before=%-3d in-scope §1-§5=%-3d selected=%d  rebuild=%s'
              % (lesson, len(b), len(p), len(sel['ids']), sel['rebuild']))
        bad = validate(lesson)
        for qid, why in bad:
            print('        %s %s' % (qid, why))
    return 0


def check():
    findings = []
    for lesson in sorted(SELECTIONS):
        for qid, why in validate(lesson):
            findings.append((lesson, qid, why))
    for lesson, qid, why in findings:
        print('   %s %s %s' % (lesson, qid, why))
    print('  %d selection(s) checked, %d finding(s)' % (len(SELECTIONS), len(findings)))
    return 1 if findings else 0


def main(argv):
    if not argv or argv[0] in ('-h', '--help'):
        print(__doc__)
        return 0
    a = argv[0]
    if a == '--selftest':
        return selftest()
    if a == '--status':
        return status()
    if a == '--check':
        return check()
    if a == '--build':
        if len(argv) < 2 or argv[1] not in SELECTIONS:
            print('  --build needs a registered lesson: %s' % ', '.join(sorted(SELECTIONS)))
            return 2
        lesson = argv[1]
        if not SELECTIONS[lesson]['rebuild']:
            print('  %s is registered for --check only; see the module docstring.' % lesson)
            return 2
        findings = build(lesson)
        for qid, why in findings:
            print('   %s %s' % (qid, why))
        if findings:
            return 1
        print('  wrote ZUMO_%s_Reading_Quiz.md and ZUMO_%s_Reading_Quiz_CANVAS_QTI.zip'
              % (lesson, lesson))
        return 0
    print('  unrecognized argument %r - refused, not ignored. --help for usage.' % a)
    return 2


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
