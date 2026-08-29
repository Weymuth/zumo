"""retired_claims.py - THE RETIRED-CLAIM REGISTRY.

WHY THIS EXISTS (S186). Closing a GPT row often RETIRES a claim: a sentence the
book used to assert and no longer may. The closing session verifies the claim is
at zero, records the zero in `ZUMO_GPT_REVIEW_WORKLIST.md` Part 0, and then
NOTHING ASSERTS IT AGAIN.

  `L03-09` IS THE PROOF THE VERIFICATION DOES NOT HOLD. It was recorded SHIPPED
  at S179 - "the unsourced +/-10% battery figure removed" - and the figure
  SURVIVED in L03's Quick Reference for SIX SESSIONS, contradicting `L03_B35`'s
  keyed answer the whole time. S185 found it by reading the bank, not the lesson.
  A gate would have named it at S180.

THREE RETIREMENTS ALREADY HAVE A GATE AND THE REST HAVE NOTHING. Gate 74 holds
the C1 slogan (§16.31), gate 76 the hardware identity (§16.25), gate 79 the
retired section names (§18.3b). Each was hand-built for one ruling. Part 0 now
carries 59 closed rows; the retirements below had no comparator at all.

THIS FILE IS THE TABLE THOSE THREE GATES SHOULD HAVE BEEN. Appending a row when
you close a row is one line, which is the only way a registry survives contact
with a session that is in a hurry.

SCOPE LIMIT, STATED (rule 78): a registry entry asserts that a RETIRED SPELLING
has not come back. It cannot see a claim RESTATED IN OTHER WORDS - which is
exactly how §16.25 survived its own fix in two sites, and how §18.3b survived in
three registers. This closes one direction and not the class. When an entry
first fires on a paraphrase somebody wrote in good faith, the answer is a
ruling on the claim, not a looser pattern.

THIS IS A LIBRARY AND IT DOES NOT EXIT. Nothing at import time may call
sys.exit(); `book_gates` imports it, and a library that exits kills the suite
silently. Run it directly for `--selftest` / a live sweep.
"""

import glob
import os
import re
import sys

VERSION = 'v1.1.2'
# v1.1.2 note (S194): the DOCSTRING used to open 'retired_claims.py v1.0'. VERSION had
#   moved four times and that line never did, so a naive version grep found v1.0 while
#   the home said v1.1.x - the SS5b two-homes defect, in the one file whose whole job is
#   noticing that a claim moved in one place and not another. `session_versions --selftest`
#   CONTROL D (grep_trap) had been RED on the clean tree for an unknown number of sessions
#   because that selftest is not in the session-open ritual. Every other instrument in the
#   suite carries NO version in its docstring; this one is now consistent with them.
# v1.1.2 (S194): 23 -> 24. THE VARIANT, NOT THE BOARD - AND 82/82 PASSED OVER IT.
#   Gate 76 (SS16.25) watches for A-Star being called the brain. It says nothing about
#   WHICH Zumo main board, so the whole suite read ALL GATES PASS with the wrong product
#   named in fourteen sites. Proved by control: restoring the short name to L03 left
#   82/82 green. The fleet carries the `Zumo 32U4 OLED Main Board`, a different Pololu
#   product from the plain `Zumo 32U4 Main Board` SS16.25 canonised at S162 - which
#   stopped one word short of the variant and then carried the short spelling in its own
#   canon line. NEGATIVE LOOKAHEAD ON PURPOSE: the retired thing is the name WITHOUT
#   OLED, so `Zumo 32U4 OLED Main Board` must not fire. If a future lesson teaches the
#   difference between the two products it will need the bare phrase, and per the scope
#   note above the answer then is a ruling, not a looser pattern.
# v1.1.1 (S193): 21 -> 23. A FIFTH L10-12 SPELLING, AND L08-15.
#   The four L10-12 spellings registered at S192 read CLEAN over a LIVE instance of the
#   claim: not in prose, in the `why:` attached to a wrong ANSWER in L10_B21. That field
#   asserts what the book says, so the structural exemption below never covered it - and
#   all four predicates missed it because all four were keyed on the prose the sweep had
#   just finished reading. FOUR SPELLINGS SHARED ONE BLIND SPOT: they were four readings
#   of one corpus, not four readings of the claim (rules 83/84). The explanation attached
#   to a distractor is prose too, and nothing was looking at it.
#   L08-15 is the SAME FAMILY INVERTED: C1 called feed-forward a rival of the loop; this
#   called a feed-forward rule a loop. Registered as the PROPORTIONAL spelling only,
#   because L15 GRAPHIC 15.2's "two controllers" (P vs PD) is TRUE and stays - it is the
#   standing negative control, and it is why this run still prints CLEAN.
# v1.1.0 (S192): THE C1 RESIDUE REGISTERED - FOUR SPELLINGS FOR ONE CLAIM, ON PURPOSE.
#   16.31 retired the TRIM SLOGAN at S161 and the MECHANISM under it survived in five
#   lessons for 31 sessions, because that sweep was keyed on the phrasings table. The
#   predicate hunting it widened THREE TIMES in one session - 6 sites, then 7 (the L12
#   KEY TERM, 16.56), then 13 (all of L10) - so ONE pattern here would inherit whichever
#   blind spot the last widening happened to leave. Four are registered instead, each
#   measured at zero first and each blinding-controlled by planting it into L08 in turn.
#   REGISTERED AFTER THE FIX, NOT BEFORE: register-first was ruled and this file's own
#   header refuted it - an entry that is already firing is a backlog, not a gate. 21, was 17.

# ---------------------------------------------------------------------------
# THE REGISTRY.
#
# One entry per retired claim. `pattern` is the SPELLING that must not come
# back; `label` is what a failure message calls it; `row` and `since` are the
# provenance so a reader can find the ruling that retired it.
#
# EVERY ENTRY WAS MEASURED AT ZERO IN THE ASSERTIVE REGISTER BEFORE IT WAS
# ADDED (rule 34). An entry that is already firing is not a gate, it is a
# backlog, and the two must not be confused.
#
# DO NOT ADD A PATTERN THAT MATCHES ORDINARY BOOK VOCABULARY. The probe that
# built this table returned hits for all of these in four banks and every one
# was a `#` provenance comment; the structural exemption below is what made the
# measurement mean anything.
# ---------------------------------------------------------------------------
REGISTRY = [
    # (row, pattern, label, since)
    ('L02-13', r'fight over',
     'two objects would fight over it (fabled mechanism; the real cost is SRAM)', 'S180'),
    ('L13-13', r'spoken for',
     'the servo channel is spoken for (a servo never asks a DRV8838 for a channel)', 'S181'),
    ('L03-09', r'\u00b1\s*10\s*%|\+/-\s*10\s*%',
     'the unsourced +/-10% figure on readBatteryMillivolts()', 'S179'),
    ('L03-10', r'below\s*4,?200[^.]{0,60}damag|damag[^.]{0,60}below\s*4,?200',
     'below 4,200 damages the cells (the mechanism is cell reversal)', 'S185'),
    ('L01-09', r'very first programmers',
     'the very first programmers in history', 'S177'),
    ('L03-08', r'30[- ]second cool|cool ?down for 30',
     'the unsourced 30-second cooldown rule', 'S179'),
    ('L13-14', r'already flown it',
     'you have already flown it (the sweep is not SLAM)', 'S181'),
    ('L13-04', r'every row starts from truth',
     'every row starts from truth (a row-end is a bound on error, not a pose)', 'S181'),
    ('L13-06', r'door never trigger',
     'the door never triggers (silverDetected() returns TRUE, it does not fail shut)', 'S181'),
    ('L13-09', r'invisible to every sensor',
     'nearly invisible to every sensor this robot carries', 'S181'),
    ('L05-01', r'10\s*pushups|push-?up',
     'the push-up-coach analogy re-teaching for-loop anatomy in L05 '
     '(it counted from 1, against the zero-counting rule L04 8A.6 teaches)', 'S188'),
    ('L05-02', r'all six of today|add all six|all six in one trip',
     'Step 4 hands you all six prototypes in one trip (five are pasted; the sixth is the student\'s)', 'S188'),
    # --- S190, the L07 C++-correctness block. Every one was COMPILER-VERIFIED false
    # --- before it was retired, each with a blinding control (see LIVE.md S190).
    ('L07-04', r'extern[^.]{0,40}\.cpp[^.]{0,40}linker error|extern in the \.cpp[^.]{0,30}error',
     'extern in a .cpp is a linker error (it is legal; the error is that nothing DEFINES the object)', 'S190'),
    ('L07-04', r'only goes in the \.h',
     'extern only goes in the .h file (a house rule stated as a language restriction)', 'S190'),
    ('L07-05', r"expected ';' before '\{'",
     "a function body in a header produces expected ';' before '{' (bodies in headers are legal; "
     "the real failure is multiple definition across two translation units)", 'S190'),
    ('L07-02', r'modern standard',
     '#pragma once is the modern standard (it is a compiler extension; include guards are the standard)', 'S190'),
    ('L07-03', r'prevents this automatically',
     '#pragma once prevents circular includes automatically (it stops the preprocessor loop, not the design problem)', 'S190'),
    # --- S192, THE C1 RESIDUE. Five rows, five lessons, 12 prose sites and 5 bank
    # --- questions. §16.31 retired the SLOGAN in S161 and the MECHANISM underneath it
    # --- survived, because the sweep was keyed on the phrasings table. FOUR SPELLINGS
    # --- ARE REGISTERED, NOT ONE: the predicate widened three times in one session
    # --- (6 -> 7 -> 13 sites), and a single pattern would inherit whichever blind spot
    # --- the last widening happened to leave. All four measured at ZERO first.
    # --- The claim is BACKWARDS, not loose: TRIM is feed-forward and enters the same
    # --- additive channel as the P-term, so it removes the disturbance the P-term is
    # --- otherwise stuck holding a standing offset against. L15 §3.4 says so in the
    # --- book's own words, and L15 §3.6 already prescribes "check TRIM" for a line-loop
    # --- offset. Simulated: mismatch 12 with TRIM 0 settles at error 75, with TRIM 12
    # --- at 0, and error x Kp is constant across a fourfold Kp sweep.
    ('L08-08', r'fight[a-z]*\s+(its|it|a|the)\s*(own)?\s*(controller|correction)|fight[a-z]*\s+itself',
     'adding TRIM would make the robot fight its own controller '
     '(feed-forward and feedback sum; they are not rivals)', 'S192'),
    ('L10-12', r'correcting\s+(motor\s+)?bias\s+is\s+(already|its entire)|already\s+(its|the)\s+job',
     'correcting motor bias is already the loop\'s job '
     '(a P-term settles at a STANDING offset against a constant bias - L15 3.4)', 'S192'),
    ('L11-08', r'spend (its|the) day undoing|constant to spend',
     'TRIM gives the P-term a constant to spend the day undoing', 'S192'),
    ('L12-18', r'second correction that fight|controller that is already (right|correct)',
     'TRIM is a second correction fighting a controller that is already right', 'S192'),
    # --- S193. A FIFTH L10-12 SPELLING. The four above all reached zero at S192 and
    # --- the registry still read CLEAN over a live instance: L10_B21's DISTRACTOR
    # --- `why:` said "the stated mechanism is two controllers correcting the same
    # --- thing at once" - an ASSERTION about the book, not a declared-wrong option,
    # --- so the structural exemption never applied. Four spellings inherited one
    # --- blind spot between them because all four were keyed on the PROSE the sweep
    # --- had just read. The explanation attached to a wrong answer is prose too.
    ('L10-12', r'two controllers correcting',
     'the stated mechanism is two controllers correcting the same thing at once '
     '(the line sensors read the LINE, not the motors)', 'S193'),
    # --- S193, L08-15. A DIFFERENT CLAIM FROM THE C1 FAMILY ABOVE, AND THE OPPOSITE
    # --- ERROR: C1 called feed-forward a RIVAL of the loop; this calls a feed-forward
    # --- rule a LOOP. L08 C6 maps line error to a throttle command and NOTHING
    # --- measures the robot's actual speed, so no loop closes on speed. Two spellings.
    # --- NOT registered as a bare (two|second) + controller: L15 GRAPHIC 15.2 says
    # --- "the same step, two controllers: P alone oscillates, PD glides" about P and
    # --- PD, which ARE two controllers of one loop. A predicate that cannot tell those
    # --- apart would retire a true sentence (rule 34).
    ('L08-15', r'second proportional controller|[Tt]wo proportional controllers',
     'the Racing Line throttle rule is a second proportional controller '
     '(it is proportional, but nothing measures speed, so no loop closes on it)', 'S193'),
    # --- S194. NOT A WORKLIST ROW - a Bible canon correction (SS16.25, v8.190).
    # --- DJ ruling S194: "Fix it everywhere." The photograph's own silkscreen reads
    # --- `Zumo 32U4 OLED`, which is the evidence; the product page is corroboration.
    # --- Measured morphologically before it was edited: every `Zumo 32U4` plus its next
    # --- three words, 394 mentions across sixteen lessons, the correct product name
    # --- appearing ZERO times and all 14 sites carrying the short one.
    ('16.25', r'Zumo\s*32U4\s+(?!OLED)[Mm]ain\s*[Bb]oard',
     'the board named as the plain Zumo 32U4 Main Board '
     '(the fleet carries the OLED Main Board, a different Pololu product)', 'S194'),
]


# ---------------------------------------------------------------------------
# THE STRUCTURAL EXEMPTION (rule 20). ONE DEFINITION, TWO READERS (rules 83/84):
# gate 76 imports this rather than keeping its own copy.
#
# A bank may quote a retired form in a `#` comment (that is PROVENANCE, history,
# never rewritten - rule 37) or as a DECLARED-WRONG option (that is the TRAP
# being taught - `QUIZ_L03` B18 does exactly this with L03-10's retired claim).
# Neither asserts anything. Everything else does.
# ---------------------------------------------------------------------------
def assert_true_text(q):
    """The strings in one question that ASSERT something. A declared-wrong option
    asserts nothing - it is the trap - so it is excluded BY STRUCTURE and never
    by a name list."""
    out, typ = [], q.get('type')
    correct = q.get('correct')
    if typ == 'true_false':
        if correct is True:
            out.append(str(q.get('stem', '')))
            out.append(str(q.get('why', '')))
    else:
        out.append(str(q.get('stem', '')))
        if correct is True:
            out.append(str(q.get('why', '')))
    for _o in q.get('options', []) or []:
        if isinstance(_o, dict) and _o.get('correct') is True:
            out.append(str(_o.get('text', '')))
            out.append(str(_o.get('why', '')))
    for _p in q.get('pairs', []) or []:
        if isinstance(_p, dict):
            out.append(str(_p.get('left', '')))
            out.append(str(_p.get('right', '')))
    return '\n'.join(out)


def sweep(page_texts, bank_questions, registry=None):
    """page_texts: {name: ALREADY TAG-STRIPPED text}. The caller owns the strip,
    because `notags` has ONE home in book_gates and this file must not become a
    second one (S168).

    bank_questions: {name: [question dict, ...]}.

    registry: injectable so a control can test the ARM rather than the state of
    the book (S171's lesson - a control whose fixture is borrowed from the
    population it audits fails the day you succeed).

    Returns a list of finding strings. Empty means clean.
    """
    reg = REGISTRY if registry is None else registry
    out = []
    for name, text in sorted(page_texts.items()):
        for row, pat, label, since in reg:
            n = len(re.findall(pat, text, re.S))
            if n:
                out.append('%s carries the RETIRED claim "%s" x%d - %s, retired %s'
                           % (name, label, n, row, since))
    for name, qs in sorted(bank_questions.items()):
        for q in qs:
            txt = assert_true_text(q)
            for row, pat, label, since in reg:
                if re.search(pat, txt, re.S):
                    out.append('%s: %s ASSERTS the RETIRED claim "%s" - %s, retired %s'
                               % (name, q.get('id', '?'), label, row, since))
    return out


# ---------------------------------------------------------------------------
def _controls():
    """One mutation per assertion. Every arm must be shown to FIRE and to be
    SILENT, because an arm that has not been made to fail has not been tested
    (rule 59)."""
    ok = True

    def check(tag, cond, detail=''):
        nonlocal ok
        print('  %-58s %s%s' % (tag, 'PASS' if cond else 'FAIL',
                                ('' if cond else ' - ' + detail)))
        if not cond:
            ok = False

    TOY = [('X-01', r'zzretiredzz', 'the toy claim', 'S000')]

    # A: a retired spelling in page prose FIRES.
    f = sweep({'Toy.html': 'a sentence with zzretiredzz in it'}, {}, TOY)
    check('CONTROL A (retired spelling in prose FIRES)', len(f) == 1, str(f))

    # B: clean prose is SILENT - the blinding arm.
    f = sweep({'Toy.html': 'a sentence with nothing wrong with it'}, {}, TOY)
    check('CONTROL B (clean prose SILENT)', not f, str(f))

    # C: a KEYED CORRECT option asserting it FIRES. This is L03-10's shape and
    #    the whole reason the file exists.
    q = {'id': 'T_B1', 'type': 'multiple_choice', 'stem': 'q?',
         'options': [{'text': 'zzretiredzz', 'correct': True},
                     {'text': 'fine', 'correct': False}]}
    f = sweep({}, {'Toy.yaml': [q]}, TOY)
    check('CONTROL C (keyed CORRECT option FIRES)', len(f) == 1, str(f))

    # D: the SAME string as a DECLARED-WRONG option is SILENT. B18 does exactly
    #    this on purpose; an arm that convicted it would be switched off.
    q = {'id': 'T_B2', 'type': 'multiple_choice', 'stem': 'q?',
         'options': [{'text': 'zzretiredzz', 'correct': False},
                     {'text': 'fine', 'correct': True}]}
    f = sweep({}, {'Toy.yaml': [q]}, TOY)
    check('CONTROL D (declared-WRONG distractor SILENT)', not f, str(f))

    # E: a true_false keyed TRUE asserting it FIRES; keyed FALSE is SILENT.
    qt = {'id': 'T_A1', 'type': 'true_false', 'stem': 'zzretiredzz', 'correct': True}
    qf = {'id': 'T_A2', 'type': 'true_false', 'stem': 'zzretiredzz', 'correct': False}
    f1 = sweep({}, {'Toy.yaml': [qt]}, TOY)
    f2 = sweep({}, {'Toy.yaml': [qf]}, TOY)
    check('CONTROL E (true_false TRUE fires, FALSE silent)',
          len(f1) == 1 and not f2, '%s / %s' % (f1, f2))

    # F: an EMPTY registry does not pass on no truth. A sweep with nothing to
    #    assert must be caught by the CALLER's coverage arm, so this control
    #    records the property rather than asserting a finding.
    f = sweep({'Toy.html': 'zzretiredzz'}, {}, [])
    check('CONTROL F (empty registry finds nothing - coverage is the caller\'s)',
          not f, str(f))

    # G: the LIVE registry over the LIVE tree is clean. An anchor, asserted
    #    rather than assumed (S169) - if this fails the book has regressed.
    pages, banks, err = live_inputs()
    check('CONTROL G (live tree readable)', not err, str(err))
    if not err:
        f = sweep(pages, banks)
        check('CONTROL G2 (live tree CLEAN under the live registry)', not f,
              '; '.join(f[:4]))
        check('CONTROL G3 (registry is non-empty)', len(REGISTRY) > 0)
        check('CONTROL G4 (scope reached 17 pages / 16 banks)',
              len(pages) == 17 and len(banks) == 16,
              '%d pages, %d banks' % (len(pages), len(banks)))

    # H: THE LIFTED notags MUST ACTUALLY STRIP. A lift that silently returned
    # the raw source, or the empty string, would make every arm above report
    # CLEAN on any tree - the sweep would be blind and green. This is the
    # failure the plant caught and the controls did not, promoted to a control.
    probe = ('<p>alpha <span class="x">beta</span></p><!-- gamma -->')
    lifted = _lift_notags()
    if isinstance(lifted, str):
        check('CONTROL H (notags lifted out of book_gates.py)', False, lifted)
    else:
        keep = lifted(probe, comments='keep')
        drop = lifted(probe, comments='drop')
        check('CONTROL H1 (tags stripped, text kept)',
              'alpha' in keep and 'beta' in keep and '<span' not in keep, repr(keep))
        check('CONTROL H2 (comments=keep keeps, comments=drop drops)',
              'gamma' in keep and 'gamma' not in drop,
              'keep=%r drop=%r' % (keep, drop))
    return ok


def _lift_notags():
    """Return book_gates' notags callable, or an error STRING.

    NOTAGS HAS ONE HOME AND THIS FILE MUST NOT BECOME A SECOND (S168) - BUT
    `book_gates` IS A PROGRAM, NOT A LIBRARY: importing it RUNS the whole suite
    and then calls sys.exit(). That was caught by planting a real defect, NOT by
    the controls, every one of which passed - because on a CLEAN tree the suite
    falls off the end without exiting, so the fixture was borrowed from a
    healthy population and could not fail (rule 59, S171's shape).
    So: parse the source and exec ONLY the notags FunctionDef plus the
    module-level constants it reads. Nothing else in that file executes.
    """
    try:
        import ast
        _src = open('book_gates.py', encoding='utf-8').read()
        _tree = ast.parse(_src)
        _fn = next((n for n in _tree.body
                    if isinstance(n, ast.FunctionDef) and n.name == 'notags'), None)
        if _fn is None:
            return 'book_gates.py defines no notags() - it may have been renamed'
        # A lambda parameter is BOUND, not free - notags passes a lambda to
        # re.sub and its `m` would otherwise read as a missing global.
        _local = {n.id for n in ast.walk(_fn)
                  if isinstance(n, ast.Name) and isinstance(n.ctx, ast.Store)}
        for _n in ast.walk(_fn):
            if isinstance(_n, (ast.FunctionDef, ast.Lambda)):
                _a = _n.args
                for _grp in (_a.args, _a.posonlyargs, _a.kwonlyargs):
                    _local |= {x.arg for x in _grp}
                for _x in (_a.vararg, _a.kwarg):
                    if _x:
                        _local.add(_x.arg)
            if isinstance(_n, ast.comprehension):
                _local |= {c.id for c in ast.walk(_n.target)
                           if isinstance(c, ast.Name)}
        _free = {n.id for n in ast.walk(_fn)
                 if isinstance(n, ast.Name) and isinstance(n.ctx, ast.Load)} - _local
        # DERIVE which constants to lift rather than pinning a list (rule 19).
        _pre = [n for n in _tree.body
                if isinstance(n, ast.Assign) and n.lineno < _fn.lineno
                and any(isinstance(t, ast.Name) and t.id in _free for t in n.targets)]
        _ns = {'re': re}
        exec(compile(ast.Module(body=_pre + [_fn], type_ignores=[]),
                     'book_gates.py:notags', 'exec'), _ns)          # noqa: S102
        _missing = sorted(_free - set(_ns) - {'re'})
        if _missing:
            return ('notags needs %s from book_gates.py and it was not liftable'
                    % ', '.join(_missing))
        return _ns['notags']
    except Exception as e:                                      # noqa: BLE001
        return 'could not lift notags out of book_gates.py: %s' % e


def live_inputs():
    """Read the tree the way the gates do. Returns (pages, banks, error)."""
    notags = _lift_notags()
    if isinstance(notags, str):
        return {}, {}, notags
    import html as _html
    pages = {}
    for f in sorted(glob.glob('lessons/Lesson_*.html')) + ['newproject.html']:
        try:
            pages[os.path.basename(f)] = _html.unescape(
                notags(open(f, encoding='utf-8').read(), comments='keep'))
        except Exception as e:                                  # noqa: BLE001
            return {}, {}, '%s could not be read (%s)' % (f, e)
    banks = {}
    try:
        sys.path.insert(0, 'quizzes')
        import quiz_bank as _QB
    except Exception as e:                                      # noqa: BLE001
        return pages, {}, 'could not import quiz_bank: %s' % e
    for b in sorted(glob.glob(os.path.join('quizzes', 'ZUMO_QUIZ_*.yaml'))):
        d, e = _QB.load(b)
        if e:
            return pages, {}, '%s: %s' % (b, e)
        qs = []
        for s in (d.get('sets') or {}).values():
            qs.extend((s or {}).get('questions', []) or [])
        banks[os.path.basename(b)] = qs
    return pages, banks, ''


def main(argv):
    print('retired_claims.py %s - %d registered retirements' % (VERSION, len(REGISTRY)))
    if '--selftest' in argv:
        return 0 if _controls() else 1
    if '--list' in argv:
        for row, pat, label, since in REGISTRY:
            print('  %-8s %-6s %s' % (row, since, label))
        return 0
    pages, banks, err = live_inputs()
    if err:
        print('  ERROR: %s' % err)
        return 1
    f = sweep(pages, banks)
    print('  scope: %d pages, %d banks' % (len(pages), len(banks)))
    if f:
        for x in f:
            print('  FAIL  %s' % x)
        return 1
    print('  CLEAN - every registered retirement is still at zero')
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
