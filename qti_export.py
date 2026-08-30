#!/usr/bin/env python3
"""
qti_export.py - emit the sixteen reading-quiz banks as Canvas-importable QTI 1.2.

    python3 quizzes/qti_export.py --banks   [--out DIR]   Canvas QUESTION BANKS (default)
    python3 quizzes/qti_export.py --quizzes [--out DIR]   Canvas QUIZZES (fixed form)
    python3 quizzes/qti_export.py --both    [--out DIR]   both packages
    python3 quizzes/qti_export.py --selftest                controls
    python3 quizzes/qti_export.py --help

exit 0 = clean.  exit 1 = a control failed or a bank would not convert.
exit 2 = an argument this tool does not recognize.

AN UNRECOGNIZED ARGUMENT IS REFUSED, NOT IGNORED (S174 rule). There is no
fall-through branch: a typo of --banks does not silently write a package.

WHY BANKS ARE THE DEFAULT
    Every set in every bank carries `suggested_draw` - 10 of the `before` pool,
    8 of the `after` pool. A fixed quiz cannot express a random draw, so the
    artefact these files describe is a Canvas QUESTION BANK that a quiz then
    pulls from. --quizzes exists as a fallback for a Canvas instance that will
    not take an objectbank; it emits every question as a fixed form, which is
    NOT the assessment the banks were designed for.

WHY NOTHING IS COUNTED BY HAND
    Every figure this prints is derived from the parsed YAML. Same discipline as
    quiz_bank.py: run it and copy what it says.

ONE VERSION HOME. The version lives ONLY in the VERSION constant.
A LIBRARY MAY NOT EXIT: no sys.exit() outside main().
"""

import os
import re
import sys
import glob
import html
import zipfile

try:
    import yaml
except ImportError:                                          # pragma: no cover
    yaml = None

VERSION = '1.2'

HERE = os.path.dirname(os.path.abspath(__file__))
QTI_NS = 'http://www.imsglobal.org/xsd/ims_qtiasiv1p2'
CC_NS = 'http://canvas.instructure.com/xsd/cccv1p0'
CP_NS = 'http://www.imsglobal.org/xsd/imsccv1p1/imscp_v1p1'

# Canvas question_type strings. The YAML type is NOT the QTI type; this map is
# the only place the two vocabularies meet.
QTYPE = {
    'multiple_choice': 'multiple_choice_question',
    'true_false':      'true_false_question',
    'matching':        'matching_question',
}


# ----------------------------------------------------------------- text ------
def to_html(text):
    """Bank text -> QTI-safe HTML.

    ORDER IS LOAD-BEARING. Escape FIRST, so `#include <Zumo32U4.h>` becomes
    &lt;Zumo32U4.h&gt; and is not eaten as a tag; only then are the backtick
    pairs turned into <code>. Doing it the other way round would escape the
    <code> tags this function just wrote.

    Asterisks are left alone on purpose: every one in the corpus is a literal
    C comment delimiter (/* ... */), not markdown emphasis.
    """
    if text is None:
        return ''
    s = html.escape(str(text), quote=False)
    # backticks are proven paired by the parity control; alternate open/close
    out, open_span = [], False
    for ch in s:
        if ch == '`':
            out.append('</code>' if open_span else '<code>')
            open_span = not open_span
        else:
            out.append(ch)
    s = ''.join(out)
    # multi-line stems keep their shape: hard break + non-collapsing indent
    # NBSP MUST BE A NUMERIC REFERENCE. XML predefines exactly five entities and
    # &nbsp; is not one of them, so an &nbsp; here makes the package unparseable
    # and Canvas refuses the import. Caught by the round-trip arm, NOT by the
    # first version of control C - which asserted the defect rather than the fix.
    lines = s.split('\n')
    kept = []
    for ln in lines:
        lead = len(ln) - len(ln.lstrip(' '))
        kept.append('&#160;' * lead + ln.lstrip(' '))
    return '<br/>'.join(kept)


def mattext(text, kind='text/html'):
    """Wrap text for QTI.

    THE HTML IS ENTITY-ENCODED INSIDE mattext, which is what Canvas's own
    exports do and what its importer expects. Emitting <code> as a real XML
    CHILD of mattext parses fine but is wrong: the importer takes the node's
    TEXT, so every tag would be silently stripped and the code formatting on
    42 sites would vanish without any error. Encoded, the tag survives as
    markup. Caught by the round-trip arm.

    text/plain is for matching labels, which Canvas renders literally - they
    get the raw string escaped once, with no <code> and no <br>.
    """
    if kind == 'text/plain':
        body = html.escape(str(text if text is not None else ''), quote=False)
    else:
        body = html.escape(to_html(text), quote=False)
    return '<material><mattext texttype="%s">%s</mattext></material>' % (kind, body)


# ------------------------------------------------------------- one item ------
def _meta(fields):
    rows = ''.join(
        '<qtimetadatafield><fieldlabel>%s</fieldlabel>'
        '<fieldentry>%s</fieldentry></qtimetadatafield>'
        % (k, html.escape(str(v), quote=False))
        for k, v in fields)
    return '<itemmetadata><qtimetadata>%s</qtimetadata></itemmetadata>' % rows


def item_choice(q):
    """multiple_choice and true_false share one QTI shape: single response_lid."""
    qid = q['id']
    if q['type'] == 'true_false':
        opts = [{'text': 'True',  'correct': q['correct'] is True},
                {'text': 'False', 'correct': q['correct'] is False}]
        # a true/false `why` explains what IS true, so it is general feedback
        general = q.get('why')
    else:
        opts = q['options']
        general = None

    labels, conds, feedbacks = [], [], []
    for i, o in enumerate(opts):
        aid = '%s_A%d' % (qid, i)
        labels.append(
            '<response_label ident="%s">%s</response_label>'
            % (aid, mattext(o['text'])))
        why = o.get('why')
        fb = ''
        if why:
            feedbacks.append(
                '<itemfeedback ident="%s_fb"><flow_mat>%s</flow_mat></itemfeedback>'
                % (aid, mattext(why)))
            fb = ('<displayfeedback feedbacktype="Response" linkrefid="%s_fb"/>'
                  % aid)
        if o.get('correct'):
            conds.append(
                '<respcondition continue="No">'
                '<conditionvar><varequal respident="response1">%s</varequal></conditionvar>'
                '<setvar action="Set" varname="SCORE">100</setvar>%s'
                '</respcondition>' % (aid, fb))
        elif fb:
            conds.append(
                '<respcondition continue="Yes">'
                '<conditionvar><varequal respident="response1">%s</varequal></conditionvar>'
                '%s</respcondition>' % (aid, fb))

    if general:
        feedbacks.append(
            '<itemfeedback ident="general_fb"><flow_mat>%s</flow_mat></itemfeedback>'
            % mattext(general))
        conds.insert(0,
                     '<respcondition continue="Yes"><conditionvar><other/></conditionvar>'
                     '<displayfeedback feedbacktype="Response" linkrefid="general_fb"/>'
                     '</respcondition>')

    return (
        '<item ident="%s" title="%s">%s'
        '<presentation>%s'
        '<response_lid ident="response1" rcardinality="Single">'
        '<render_choice>%s</render_choice></response_lid>'
        '</presentation>'
        '<resprocessing><outcomes>'
        '<decvar maxvalue="100" minvalue="0" varname="SCORE" vartype="Decimal"/>'
        '</outcomes>%s</resprocessing>%s</item>'
    ) % (qid, qid,
         _meta([('question_type', QTYPE[q['type']]),
                ('points_possible', '%.1f' % float(q['points'])),
                ('original_answer_ids', ','.join('%s_A%d' % (qid, i)
                                                 for i in range(len(opts)))),
                ('assessment_question_identifierref', qid + '_aq')]),
         mattext(q['stem']),
         ''.join(labels), ''.join(conds), ''.join(feedbacks))


def item_matching(q):
    """Canvas matching: one response_lid per LEFT, every RIGHT (plus the
    distractors) rendered in each choice list, one respcondition per pair.

    `extra_answers` are the unmatched distractors. Canvas reads them from the
    matching_answer_incorrect_matches metadata field, newline separated, AND
    needs them present as response_labels so they can be picked."""
    qid = q['id']
    pairs = q['pairs']
    extras = q.get('extra_answers', []) or []

    rights = [p['right'] for p in pairs] + list(extras)
    rid = {r: '%s_R%d' % (qid, i) for i, r in enumerate(rights)}
    choices = ''.join('<response_label ident="%s">%s</response_label>'
                      % (rid[r], mattext(r, 'text/plain')) for r in rights)

    lids, conds = [], []
    share = 100.0 / len(pairs)
    for i, p in enumerate(pairs):
        lid = '%s_L%d' % (qid, i)
        lids.append('<response_lid ident="%s">%s<render_choice>%s</render_choice>'
                    '</response_lid>'
                    % (lid, mattext(p['left'], 'text/plain'), choices))
        conds.append(
            '<respcondition>'
            '<conditionvar><varequal respident="%s">%s</varequal></conditionvar>'
            '<setvar action="Add" varname="SCORE">%.2f</setvar>'
            '</respcondition>' % (lid, rid[p['right']], share))

    fields = [('question_type', 'matching_question'),
              ('points_possible', '%.1f' % float(q['points'])),
              ('assessment_question_identifierref', qid + '_aq')]
    if extras:
        fields.append(('matching_answer_incorrect_matches', '\n'.join(extras)))

    return ('<item ident="%s" title="%s">%s<presentation>%s%s</presentation>'
            '<resprocessing><outcomes>'
            '<decvar maxvalue="100" minvalue="0" varname="SCORE" vartype="Decimal"/>'
            '</outcomes>%s</resprocessing></item>'
            ) % (qid, qid, _meta(fields), mattext(q['stem']),
                 ''.join(lids), ''.join(conds))


def item_xml(q):
    if q['type'] == 'matching':
        return item_matching(q)
    if q['type'] in ('multiple_choice', 'true_false'):
        return item_choice(q)
    raise ValueError('unconvertible question type %r in %s' % (q['type'], q['id']))


# ----------------------------------------------------------- containers ------
HEAD = ('<?xml version="1.0" encoding="UTF-8"?>\n'
        '<questestinterop xmlns="%s" '
        'xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" '
        'xsi:schemaLocation="%s http://www.imsglobal.org/xsd/ims_qtiasiv1p2p1.xsd">'
        % (QTI_NS, QTI_NS))


def objectbank_xml(res_id, title, items):
    return (HEAD + '<objectbank ident="%s">'
            '<qtimetadata><qtimetadatafield>'
            '<fieldlabel>bank_title</fieldlabel><fieldentry>%s</fieldentry>'
            '</qtimetadatafield></qtimetadata>%s</objectbank></questestinterop>'
            ) % (res_id, html.escape(title, quote=False), ''.join(items))


def assessment_xml(res_id, title, items):
    return (HEAD + '<assessment ident="%s" title="%s">'
            '<qtimetadata><qtimetadatafield>'
            '<fieldlabel>cc_maxattempts</fieldlabel><fieldentry>1</fieldentry>'
            '</qtimetadatafield></qtimetadata>'
            '<section ident="root_section">%s</section></assessment></questestinterop>'
            ) % (res_id, html.escape(title, quote=False), ''.join(items))


def assessment_meta_xml(res_id, title, description, points):
    return ('<?xml version="1.0" encoding="UTF-8"?>\n'
            '<quiz identifier="%s" xmlns="%s" '
            'xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" '
            'xsi:schemaLocation="%s https://canvas.instructure.com/xsd/cccv1p0.xsd">'
            '<title>%s</title><description>%s</description>'
            '<shuffle_answers>true</shuffle_answers>'
            '<scoring_policy>keep_highest</scoring_policy>'
            '<quiz_type>assignment</quiz_type>'
            '<points_possible>%.1f</points_possible>'
            '<allowed_attempts>1</allowed_attempts>'
            '<one_question_at_a_time>false</one_question_at_a_time>'
            '<show_correct_answers>true</show_correct_answers>'
            '<available>false</available>'
            '<published>false</published>'
            '</quiz>'
            ) % (res_id, CC_NS, CC_NS,
                 html.escape(title, quote=False),
                 to_html(description), points)


def manifest_xml(resources):
    """resources: list of (res_id, href, meta_href_or_None)"""
    out = []
    for res_id, href, meta in resources:
        if meta:
            out.append(
                '<resource identifier="%s" type="imsqti_xmlv1p2" href="%s">'
                '<file href="%s"/><dependency identifierref="%s_meta"/></resource>'
                '<resource identifier="%s_meta" '
                'type="associatedcontent/imscc_xmlv1p1/learning-application-resource" '
                'href="%s"><file href="%s"/></resource>'
                % (res_id, href, href, res_id, res_id, meta, meta))
        else:
            out.append('<resource identifier="%s" type="imsqti_xmlv1p2" href="%s">'
                       '<file href="%s"/></resource>' % (res_id, href, href))
    return ('<?xml version="1.0" encoding="UTF-8"?>\n'
            '<manifest identifier="ZUMO_QTI" xmlns="%s" '
            'xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">'
            '<metadata><schema>IMS Content</schema>'
            '<schemaversion>1.1.3</schemaversion></metadata>'
            '<organizations/><resources>%s</resources></manifest>'
            ) % (CP_NS, ''.join(out))


# --------------------------------------------------------------- driver ------
def load_banks(src=None):
    src = src or HERE
    banks = []
    for f in sorted(glob.glob(os.path.join(src, 'ZUMO_QUIZ_L*.yaml'))):
        banks.append((f, yaml.safe_load(open(f, encoding='utf-8'))))
    return banks


def build_practice(out_dir, src=None):
    """One ungraded PRACTICE quiz per lesson.

    Contents: the whole `after` set, PLUS the `before` set's MATCHING items.
    The before-set matching items are deliberately excluded from the graded
    gate draw - a four-pair item is several times the work of one multiple
    choice, and equal credit for unequal work is the thing being avoided.
    That left 68 authored questions with nothing pointing at them. Practice
    has no draw and no grade, so unequal length costs nobody anything, and
    this is where they belong.

    The before set's CHOICE items are NOT here on purpose: they are the live
    gate pool, and handing students the exact bank the gate draws from turns
    the gate into a memory test.
    """
    banks = load_banks(src)
    if not banks:
        return None, ['no ZUMO_QUIZ_L*.yaml found']
    files, resources, rows, problems = {}, [], [], []
    n_items = 0
    for _path, d in banks:
        lesson = d['lesson']
        after = d['sets'].get('after', {}).get('questions', [])
        bmatch = [q for q in d['sets'].get('before', {}).get('questions', [])
                  if q['type'] == 'matching']
        qs = list(after) + list(bmatch)
        if not qs:
            continue
        res_id = '%s_practice' % lesson
        title = '%s Post-Build Check (practice, not graded): %s' % (lesson,
                                                                    d['title'])
        items = []
        for q in qs:
            try:
                items.append(item_xml(q))
            except Exception as exc:                          # noqa: BLE001
                problems.append('%s %s: %s' % (lesson, q.get('id'), exc))
        n_items += len(items)
        href = '%s/%s.xml' % (res_id, res_id)
        files[href] = assessment_xml(res_id, title, items)
        meta = '%s/assessment_meta.xml' % res_id
        files[meta] = assessment_meta_xml(
            res_id, title,
            'Ungraded practice. Unlimited attempts. Run this before a '
            'milestone so a checkpoint is not where you find a gap.',
            float(sum(float(q['points']) for q in qs)))
        resources.append((res_id, href, meta))
        rows.append((res_id, len(qs), 0))
    if problems:
        return None, problems
    files['imsmanifest.xml'] = manifest_xml(resources)
    os.makedirs(out_dir, exist_ok=True)
    zpath = os.path.join(out_dir, 'ZUMO_QTI_practice.zip')
    with zipfile.ZipFile(zpath, 'w', zipfile.ZIP_DEFLATED) as z:
        for name in sorted(files):
            z.writestr(name, files[name])
    return (zpath, rows, n_items), []


def build(mode, out_dir, src=None, only=None, split=False):
    """only: substring filter on the resource id (e.g. 'L01_before', 'L01').
    Exists so a SINGLE bank can be test-imported before committing 1,245
    questions to a Canvas course whose import settings have not been proven."""
    banks = load_banks(src)
    if not banks:
        return None, ['no ZUMO_QUIZ_L*.yaml found']

    files, resources, rows, problems = {}, [], [], []
    n_items = 0
    for path, d in banks:
        lesson = d['lesson']
        for setname in ('before', 'after'):
            blk = d['sets'].get(setname)
            if not blk:
                continue
            res_id = '%s_%s' % (lesson, setname)
            if only and only not in res_id:
                continue
            qs = blk['questions']
            # SPLIT: matching is several times the work of one multiple choice.
            # In a randomised gate draw that is unequal work for equal credit,
            # so the two kinds get separate banks and the gate draws from the
            # CHOICE bank only. Measured before choosing this: the matching
            # pools are tiny (median two, one set has none), so a separate
            # RANDOM group is not available - a draw of one from one is not a
            # draw. The matching bank is for deliberate, evenly-weighted use.
            groups = [('', qs)]
            if split:
                ch = [q for q in qs if q['type'] != 'matching']
                mt = [q for q in qs if q['type'] == 'matching']
                groups = [(' choice', ch)] + ([(' matching', mt)] if mt else [])
            # COLON, not a dash. Several lesson titles already contain an
            # em-dash ("Hello, Robot! - Your First Program"), so joining with
            # another produced a doubled dash in the bank name.
            base_title = '%s %s: %s' % (lesson,
                                        'Reading Quiz' if setname == 'before'
                                        else 'Post-Build Check',
                                        d['title'])
            for suffix, group_qs in groups:
                if not group_qs:
                    continue
                gid = res_id + suffix.replace(' ', '_')
                title = base_title + (' [%s]' % suffix.strip() if suffix else '')
                items = []
                for q in group_qs:
                    try:
                        items.append(item_xml(q))
                    except Exception as exc:                  # noqa: BLE001
                        problems.append('%s %s: %s'
                                        % (lesson, q.get('id'), exc))
                n_items += len(items)
                href = '%s/%s.xml' % (gid, gid)
                if mode == 'banks':
                    files[href] = objectbank_xml(gid, title, items)
                    resources.append((gid, href, None))
                else:
                    files[href] = assessment_xml(gid, title, items)
                    meta = '%s/assessment_meta.xml' % gid
                    pts = float(sum(float(q['points']) for q in group_qs))
                    files[meta] = assessment_meta_xml(
                        gid, title, blk.get('description', ''), pts)
                    resources.append((gid, href, meta))
                draw = blk.get('suggested_draw') if suffix != ' matching' else 0
                rows.append((gid, len(group_qs), draw))

    if problems:
        return None, problems

    if not resources:
        return None, ['--only %r matched no set' % only]
    files['imsmanifest.xml'] = manifest_xml(resources)
    os.makedirs(out_dir, exist_ok=True)
    tag = ('_' + only if only else '') + ('_split' if split else '')
    zpath = os.path.join(out_dir, 'ZUMO_QTI_%s%s.zip' % (mode, tag))
    with zipfile.ZipFile(zpath, 'w', zipfile.ZIP_DEFLATED) as z:
        for name in sorted(files):
            z.writestr(name, files[name])
    return (zpath, rows, n_items), []


# ------------------------------------------------------------ selftest -------
def selftest():
    """Controls. Each must be LOUD when broken and silent when clean."""
    bad = []

    def check(name, ok, detail=''):
        print('   %-56s %s' % (name, 'PASS' if ok else 'FAIL ' + detail))
        if not ok:
            bad.append(name)

    import xml.etree.ElementTree as _ET
    # A - escaping happens BEFORE code spans, both directions
    got = to_html('`#include <Zumo32U4.h>`')
    check('A  angle brackets escaped, backticks became a code span',
          got == '<code>#include &lt;Zumo32U4.h&gt;</code>', repr(got))
    check('A2 a bare ampersand is escaped', to_html('K&R') == 'K&amp;R')

    # B - asterisks are NOT markdown
    check('B  a C comment delimiter survives verbatim',
          to_html('/* ... */') == '/* ... */')

    # C - multi-line stems keep their break and their indent, in VALID XML
    got = to_html('a\n  b')
    check('C  newline became a break and the indent did not collapse',
          got == 'a<br/>&#160;&#160;b', repr(got))

    # C2 - THE ONE THE FIRST DRAFT GOT WRONG. XML predefines five entities and
    # &nbsp; is not among them. This asserts the emitted text PARSES, which is
    # what Canvas actually requires; asserting the literal string is what let
    # an unparseable package look clean.
    try:
        _ET.fromstring('<r>%s</r>' % to_html('a\n  b'))
        check('C2 the emitted indent is a PARSEABLE character reference', True)
    except _ET.ParseError as exc:
        check('C2 the emitted indent is a PARSEABLE character reference',
              False, str(exc))
    # and it must be LOUD the other way: a bare &nbsp; must not parse
    try:
        _ET.fromstring('<r>a&nbsp;b</r>')
        check('C3 BLINDING a bare &nbsp; is rejected by the parser', False,
              'it parsed, so C2 proves nothing')
    except _ET.ParseError:
        check('C3 BLINDING a bare &nbsp; is rejected by the parser', True)

    # C4 - THE SECOND ONE THE FIRST DRAFT GOT WRONG. mattext must carry the
    # markup ENCODED, so that reading the node's text yields the HTML rather
    # than the tag-stripped remains. Both directions asserted.
    m = mattext('use `x` here')
    node = _ET.fromstring(m.replace('<material>', '<r>').replace('</material>', '</r>'))
    mt = node.find('mattext')
    check('C4 mattext text() yields MARKUP, not tag-stripped remains',
          mt.text == 'use <code>x</code> here' and len(list(mt)) == 0,
          '%r / %d child(ren)' % (mt.text, len(list(mt))))
    check('C5 BLINDING a raw child tag would NOT survive text()',
          _ET.fromstring('<mattext>use <code>x</code> here</mattext>').text
          == 'use ', 'the blind spot this arm exists for did not reproduce')
    check('C6 a matching label is escaped once and carries no code span',
          mattext('i >= 1', 'text/plain')
          == '<material><mattext texttype="text/plain">i &gt;= 1</mattext></material>',
          mattext('i >= 1', 'text/plain'))

    # D - BLINDING: a planted unconvertible type must RAISE, not pass silently
    try:
        item_xml({'id': 'X', 'type': 'essay', 'points': 1, 'stem': 's'})
        check('D  BLINDING an unknown question type raises', False,
              'it returned instead')
    except ValueError:
        check('D  BLINDING an unknown question type raises', True)

    # E - every corpus type is in the map, derived not assumed
    if yaml is None:
        check('E  every type in the corpus has a QTI mapping', False, 'no yaml')
    else:
        seen = set()
        for _p, d in load_banks():
            for blk in d['sets'].values():
                for q in blk['questions']:
                    seen.add(q['type'])
        check('E  every type in the corpus has a QTI mapping',
              seen and seen <= set(QTYPE), repr(sorted(seen - set(QTYPE))))

        # F - backtick parity across the whole corpus (to_html assumes it)
        odd = 0
        for _p, d in load_banks():
            for blk in d['sets'].values():
                for q in blk['questions']:
                    ts = [q['stem'], q.get('why') or '']
                    for o in q.get('options', []):
                        ts += [o['text'], o.get('why') or '']
                    for pr in q.get('pairs', []):
                        ts += [pr['left'], pr['right']]
                    ts += q.get('extra_answers', []) or []
                    odd += sum(1 for t in ts if t and str(t).count('`') % 2)
        check('F  every backtick in the corpus is paired', odd == 0,
              '%d odd field(s)' % odd)

        # G - COUNT AGREEMENT: items emitted == questions parsed
        import tempfile
        with tempfile.TemporaryDirectory() as td:
            res, probs = build('banks', td)
            if probs or not res:
                check('G  emitted item count equals parsed question count',
                      False, str(probs[:2]))
            else:
                _z, rows, n = res
                check('G  emitted item count equals parsed question count',
                      n == sum(r[1] for r in rows), '%d vs %d'
                      % (n, sum(r[1] for r in rows)))
                check('G2 every set produced a resource', len(rows) == 32,
                      '%d resource(s)' % len(rows))
                # G3 - EVERY EMITTED FILE PARSES. Not a sample: all of them,
                # both modes. This is the arm that caught the &nbsp; defect.
                import zipfile as _zf
                nbad = []
                for mode in ('banks', 'quizzes'):
                    r2, p2 = build(mode, td)
                    if p2 or not r2:
                        nbad.append('%s: %s' % (mode, p2[:1]))
                        continue
                    with _zf.ZipFile(r2[0]) as z:
                        for nm in z.namelist():
                            try:
                                _ET.fromstring(z.read(nm))
                            except _ET.ParseError as exc:
                                nbad.append('%s/%s: %s' % (mode, nm, exc))
                check('G3 every emitted XML file in BOTH packages parses',
                      not nbad, '; '.join(nbad[:2]))

                # G4 - THE SPLIT LOSES NOTHING AND MIXES NOTHING. Every
                # question still appears exactly once, and no choice bank
                # contains a matching item or vice versa.
                r4, p4 = build('banks', td, split=True)
                if p4 or not r4:
                    check('G4 --split-matching keeps every question exactly once',
                          False, str(p4[:1]))
                else:
                    with _zf.ZipFile(r4[0]) as z:
                        seen, mixed = [], []
                        for nm in z.namelist():
                            if nm == 'imsmanifest.xml':
                                continue
                            body = z.read(nm).decode()
                            ids = re.findall(r'<item ident="([^"]+)"', body)
                            seen += ids
                            is_m = 'matching' in nm.split('/')[0]
                            for t in re.findall(
                                    r'<fieldlabel>question_type</fieldlabel>'
                                    r'<fieldentry>([^<]+)</fieldentry>', body):
                                if (t == 'matching_question') != is_m:
                                    mixed.append(nm)
                    check('G4 --split-matching keeps every question exactly once',
                          len(seen) == len(set(seen)) == n,
                          '%d seen, %d unique, %d expected'
                          % (len(seen), len(set(seen)), n))
                    check('G5 no bank mixes matching with choice items',
                          not mixed, str(sorted(set(mixed))[:2]))

                # G6 - PRACTICE CONTENT. Must hold every `after` question and
                # every `before` MATCHING question, and must leak NO
                # before-set choice question - those are the live gate pool,
                # and shipping them as practice turns the gate into a memory
                # test. Both directions asserted.
                r6, p6 = build_practice(td)
                if p6 or not r6:
                    check('G6 practice = after set + before-matching, no leak',
                          False, str(p6[:1]))
                else:
                    want_in, want_out = set(), set()
                    for _pp, dd in load_banks():
                        for q in dd['sets'].get('after', {}).get('questions', []):
                            want_in.add(q['id'])
                        for q in dd['sets'].get('before', {}).get('questions', []):
                            (want_in if q['type'] == 'matching'
                             else want_out).add(q['id'])
                    with _zf.ZipFile(r6[0]) as z:
                        got = set()
                        for nm in z.namelist():
                            if nm == 'imsmanifest.xml' or nm.endswith('_meta.xml'):
                                continue
                            got |= set(re.findall(r'<item ident="([^"]+)"',
                                                  z.read(nm).decode()))
                    check('G6 practice = after set + before-matching, no leak',
                          got == want_in,
                          '%d missing, %d extra' % (len(want_in - got),
                                                    len(got - want_in)))
                    check('G7 no gate-pool question leaks into practice',
                          not (got & want_out),
                          '%d leaked' % len(got & want_out))

    # H - a matching item shares 100 across its pairs and carries its distractors
    q = {'id': 'M1', 'type': 'matching', 'points': 4, 'stem': 's',
         'pairs': [{'left': 'a', 'right': 'A'}, {'left': 'b', 'right': 'B'}],
         'extra_answers': ['Z']}
    x = item_matching(q)
    check('H  matching splits the score evenly across its pairs',
          x.count('<setvar action="Add" varname="SCORE">50.00</setvar>') == 2)
    check('H2 a distractor is rendered AND declared in the metadata',
          'M1_R2' in x and 'matching_answer_incorrect_matches' in x)

    # I - true/false keys the declared side, both directions
    t = item_choice({'id': 'T', 'type': 'true_false', 'points': 1,
                     'stem': 's', 'correct': True})
    f = item_choice({'id': 'F', 'type': 'true_false', 'points': 1,
                     'stem': 's', 'correct': False})
    check('I  TRUE keys answer 0 and FALSE keys answer 1',
          '<varequal respident="response1">T_A0</varequal>' in t
          and '<varequal respident="response1">F_A1</varequal>' in f)

    print()
    if bad:
        print('  %d CONTROL(S) FAILED' % len(bad))
    else:
        print('  ALL CONTROLS PASS - loud when broken, silent when clean.')
    return 1 if bad else 0


# ---------------------------------------------------------------- main -------
def main(argv):
    args = argv[1:]
    if not args or '--help' in args or '-h' in args:
        print(__doc__.strip().replace('qti_export.py -', 'qti_export.py v%s -'
                                      % VERSION, 1))
        return 0
    known = {'--banks', '--quizzes', '--both', '--selftest', '--out',
             '--only', '--split-matching', '--practice'}
    for a in args:
        if a.startswith('--') and a not in known:
            print('qti_export.py: unrecognized argument %r' % a)
            return 2

    if '--selftest' in args:
        return selftest()

    out = os.path.join(HERE, '..', 'qti_out')
    if '--out' in args:
        i = args.index('--out')
        if i + 1 >= len(args):
            print('qti_export.py: --out needs a directory')
            return 2
        out = args[i + 1]
    out = os.path.abspath(out)

    only = None
    if '--only' in args:
        i = args.index('--only')
        if i + 1 >= len(args):
            print('qti_export.py: --only needs a resource id fragment')
            return 2
        only = args[i + 1]

    split = '--split-matching' in args

    if '--practice' in args:
        print('qti_export.py v%s' % VERSION)
        res, problems = build_practice(os.path.abspath(out))
        if problems:
            print('  practice: REFUSED')
            for pr in problems[:20]:
                print('     ' + pr)
            return 1
        zpath, rows, n = res
        print('  practice -> %s' % zpath)
        print('     %d quiz(zes), %d item(s)' % (len(rows), n))
        for res_id, count, _d in rows:
            print('       %-14s %3d question(s)' % (res_id, count))
        return 0

    modes = []
    if '--both' in args:
        modes = ['banks', 'quizzes']
    else:
        if '--banks' in args:
            modes.append('banks')
        if '--quizzes' in args:
            modes.append('quizzes')
    if not modes:
        modes = ['banks']

    print('qti_export.py v%s' % VERSION)
    rc = 0
    for mode in modes:
        res, problems = build(mode, out, only=only, split=split)
        if problems:
            print('  %s: REFUSED' % mode)
            for p in problems[:20]:
                print('     ' + p)
            rc = 1
            continue
        zpath, rows, n = res
        print('  %s -> %s' % (mode, zpath))
        print('     %d resource(s), %d item(s)' % (len(rows), n))
        for res_id, count, draw in rows:
            print('       %-12s %3d question(s)   suggested draw %s'
                  % (res_id, count, draw))
    return rc


if __name__ == '__main__':
    sys.exit(main(sys.argv))
