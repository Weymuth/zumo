#!/usr/bin/env python3
"""glyph_scan.py - AST scan for GLYPH-PINNED LOCATORS.  v1.1, S130 (v1.0, S129).

WHY THIS EXISTS (S127 rule 19, S128's marks arc):
    The marks arc replaces a callout's decorative leading emoji with an <img>.  Any
    instrument that FINDS something THROUGH that emoji stops finding it - and the
    S128 L04 control proved the failure is SILENT: §5.1's coverage fell 251 -> 240
    because the glyph is a SCOPE FILTER there, so eleven labels went un-inspected
    rather than failing.  Eleven, in one lesson, from 34 marks.

    The same shape has now been seen three times: `strip_inline`'s locator dropping
    L01's held attributes 39 -> 32 (S127, found by AST scan and by NO gate), `_LAND`
    missing the literal left arrow (S127), and §5.1 (S128).

LEADS, NOT VERDICTS (§24.6a).  This scan enumerates; a human reads.  What it DOES
decide is NEW vs KNOWN: every site below is either in the named ACCEPTED table with a
recorded reason, or it is reported as NEW and must be read before the swap runs.

TWO DETECTORS, and they catch DIFFERENT shapes - neither subsumes the other:

  D1  GLYPH-FIELD READ.  Any read of lesson_inventory's `glyph` field: c['glyph'],
      c.get('glyph').  SPELLING-INDEPENDENT - it does not matter WHICH emoji, only
      that code steers on the field at all.  This is the PROPERTY (S128 rule 18).

  D2  GLYPH LITERAL IN A LOCATOR.  A character >= U+2100 reaching a comparison,
      containment or search - directly, or through a MODULE-LEVEL table.  Catches
      pins that never touch the parser (book_gates' `blk2.count('\u2610')`), which
      D1 cannot see.

Usage:  python3 glyph_scan.py             report; exit 1 if any lead is NEW
        python3 glyph_scan.py --selftest  controls, both directions
"""
import ast
import os
import pathlib
import sys

VERSION = 'v1.1'
GLYPH_FLOOR = 0x2100          # lesson_inventory's own threshold; see queue item 2
SEARCH = {'count', 'find', 'rfind', 'index', 'startswith', 'endswith',
          'replace', 'split', 'search', 'match', 'findall', 'sub', 'finditer'}
VIEW = {'values', 'keys', 'items'}     # a table VIEW feeding a containment test
FIXTURE_HINTS = ('selftest', 'control', '_test', 'test_')

# ---- ACCEPTED: named, with the reason.  Keyed by (file, shape, expression) - NOT by
# ---- line number, which moves.  A site absent from here is NEW and the scan exits 1.
# ---- §25.2a: a named set, not a count.  Every entry has to say WHY it is allowed.
ACCEPTED = {
    ('lesson_inventory.py', 'D1', "c['glyph']"):
        'PRODUCER. The parser is where the glyph field is born; it is not a consumer.',
    ('build_family_map.py', 'D1', "c.get('glyph')"):
        'VESTIGIAL. The GLYPH tier is DELETED (S130, §24.14c). What still reads the '
        'field is the value passed to the RULE lambdas, and NONE of them uses it: '
        'blanking the glyph changes the resolution of 0 of 1069 callouts, measured '
        'behaviourally rather than by reading source. '
        'THE S129 REASON HERE WAS THE ONE THAT MISLED S130 AND IS REPLACED: it read '
        '"GLYPH={} still returns 1069/1069, so no family depends on it" - a TRUE '
        'statement whose conclusion was false, because this module reads data-family '
        'FIRST and therefore cannot fail that test. The auditor could, and did, at 212. '
        'Run a blinding control against the consumer that CAN fail.',
    ('family_tag.py', 'D1', "c.get('glyph')"):
        'VESTIGIAL. Imports build_family_map\'s tiers (§83), so it inherits the above. '
        'Its own last tier is now the AUTHORED pin, not the glyph (S130).',
    ('book_gates.py', 'D1', "_c.get('glyph')"):
        'VESTIGIAL. Gate 60 re-runs the CONTENT tiers to derive which callouts need a '
        'pin, and passes the glyph only because the RULE lambdas take three arguments. '
        'Measured: blanking it changes 0 of 1069 resolutions, so the pinned/unpinned '
        'split is glyph-independent. Caught by this scanner in the very gate written to '
        'retire the glyph tier, which is the scanner working.',
    ('mark_wire.py', 'D1', "c.get('glyph')"):
        'BY DESIGN. The swapper reads the glyph in order to REPLACE it. If this stopped '
        'reading the glyph the arc would not work.',
    # RETIRED S129: mark_wire's `win[j:j + 1] == '\ufe0f'` became a run-consumer
    # (`in ('\ufe0f', '\u200b', ' ')`), which the D2 detector does not see as a locator,
    # so the key stopped matching a real site and Control F said so. The acceptance is
    # deleted rather than rewritten -- a hold for a site that no longer exists is exactly
    # what Control F exists to catch.
}

SHAPES = ('D1', 'D2')


# ---------------------------------------------------------------------------------------
def has_glyph(s):
    return any(ord(c) >= GLYPH_FLOOR for c in s)


def norm_expr(s):
    r"""Spell every glyph as \uXXXX in the reported/keyed expression.

    TWO REASONS, and the second is the one that bit:
      1. §27.16's own principle - escape when the character is invisible in source.
         `win[j:j + 1] == '\ufe0f'` renders as `== ''` otherwise, which is unreadable.
      2. It keeps raw glyphs OUT of this file's ACCEPTED table, so the scanner does
         not report its own lookup table as a glyph-pinned locator.  It did, on the
         first run after the table gained a U+FE0F entry.
    """
    return ''.join(c if ord(c) < GLYPH_FLOOR
                   else ('\\u%04x' % ord(c) if ord(c) <= 0xFFFF else '\\U%08x' % ord(c))
                   for c in s)


def _parents(tree):
    p = {}
    for n in ast.walk(tree):
        for ch in ast.iter_child_nodes(n):
            p[ch] = n
    return p


def _enclosing_def(node, parents):
    n = parents.get(node)
    while n is not None:
        if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef)):
            return n.name
        n = parents.get(n)
    return None


def _is_fixture(node, parents):
    name = _enclosing_def(node, parents)
    return bool(name) and any(h in name.lower() for h in FIXTURE_HINTS)


def _locator_context(node, parents):
    """Is this node an operand of a comparison / containment / search call?"""
    par = parents.get(node)
    # table.values() / .keys() / .items() -> step over the Attribute AND its Call
    if isinstance(par, ast.Attribute) and par.attr in VIEW:
        call = parents.get(par)
        if isinstance(call, ast.Call):
            par = parents.get(call)
    elif isinstance(par, ast.Attribute):
        par = parents.get(par)
    if isinstance(par, ast.Compare):
        return 'compare'
    if isinstance(par, ast.Subscript):
        return 'subscript'
    if isinstance(par, ast.Call) and isinstance(par.func, ast.Attribute) \
            and par.func.attr in SEARCH:
        return 'search'
    return None


def _module_glyph_tables(tree):
    """Module-level names bound to a container holding a glyph literal.

    MODULE LEVEL ONLY.  A function-local bound from a glyph operation (`boxes =
    blk2.count(...)`) is the RESULT of a pin, not a pin, and reporting it doubles
    every finding.
    """
    tables = {}
    for stmt in tree.body:
        if not isinstance(stmt, ast.Assign):
            continue
        if not any(isinstance(c, ast.Constant) and isinstance(c.value, str)
                   and has_glyph(c.value) for c in ast.walk(stmt.value)):
            continue
        for tgt in stmt.targets:
            if isinstance(tgt, ast.Name):
                tables[tgt.id] = stmt.lineno
    return tables


def scan_file(path):
    """Return a list of leads for one file.  Never raises on a parse failure."""
    src = pathlib.Path(path).read_text(encoding='utf-8')
    try:
        tree = ast.parse(src)
    except SyntaxError as e:
        return [dict(file=os.path.basename(path), shape='PARSE-FAIL', line=e.lineno or 0,
                     expr=str(e), fixture=False)]
    parents = _parents(tree)
    name = os.path.basename(path)
    leads = []

    # ---- D1: any read of the parser's `glyph` field
    for n in ast.walk(tree):
        hit = False
        if isinstance(n, ast.Subscript) and isinstance(n.slice, ast.Constant) \
                and n.slice.value == 'glyph':
            hit = True
        elif isinstance(n, ast.Call) and isinstance(n.func, ast.Attribute) \
                and n.func.attr == 'get' and n.args \
                and isinstance(n.args[0], ast.Constant) and n.args[0].value == 'glyph':
            hit = True
        if hit:
            leads.append(dict(file=name, shape='D1', line=n.lineno,
                              expr=norm_expr(ast.unparse(n)), fixture=_is_fixture(n, parents)))

    # ---- D2: a glyph literal reaching a locator, directly or via a module-level table
    for n in ast.walk(tree):
        if isinstance(n, ast.Constant) and isinstance(n.value, str) and has_glyph(n.value):
            ctx = _locator_context(n, parents)
            if ctx:
                par = parents.get(n)
                leads.append(dict(file=name, shape='D2', line=n.lineno,
                                  expr=norm_expr(ast.unparse(par)),
                                  fixture=_is_fixture(n, parents)))
    tables = _module_glyph_tables(tree)
    for n in ast.walk(tree):
        if isinstance(n, ast.Name) and isinstance(n.ctx, ast.Load) and n.id in tables:
            ctx = _locator_context(n, parents)
            if ctx:
                par = parents.get(n)
                if isinstance(par, ast.Attribute) and par.attr in VIEW:
                    par = parents.get(parents.get(par))
                elif isinstance(par, ast.Attribute):
                    par = parents.get(par)
                leads.append(dict(file=name, shape='D2', line=n.lineno,
                                  expr=norm_expr(ast.unparse(par)),
                                  fixture=_is_fixture(n, parents)))

    # de-duplicate: one lead per (shape, expression), keeping the earliest line
    seen = {}
    for ld in leads:
        k = (ld['shape'], ld['expr'])
        if k not in seen or ld['line'] < seen[k]['line']:
            seen[k] = ld
    return sorted(seen.values(), key=lambda d: (d['shape'], d['line']))


def scan(paths):
    out = []
    for p in paths:
        out.extend(scan_file(p))
    return out


# ---------------------------------------------------------------------------------------
def _report(root='.'):
    paths = sorted(str(p) for p in pathlib.Path(root).glob('*.py'))
    leads = scan(paths)
    new = []
    print(f'glyph_scan {VERSION} - LEADS, NOT VERDICTS. Read each before acting '
          f'(\u00a724.6a).')
    print(f'  {len(paths)} instrument(s) scanned; glyph floor U+{GLYPH_FLOOR:04X}\n')
    by_file = {}
    for ld in leads:
        by_file.setdefault(ld['file'], []).append(ld)
    for f in sorted(by_file):
        print(f'{f}')
        for ld in by_file[f]:
            key = (ld['file'], ld['shape'], ld['expr'])
            if key in ACCEPTED:
                tag = 'ACCEPTED'
            elif ld['fixture']:
                tag = 'FIXTURE '
            else:
                tag = '** NEW **'
                new.append(ld)
            print(f'   {ld["line"]:>5}  {ld["shape"]}  {tag}  {ld["expr"][:88]}')
            if key in ACCEPTED:
                print(f'          {ACCEPTED[key]}')
        print()
    print(f'  {len(leads)} lead(s): {len(ACCEPTED)} accepted by name, '
          f'{sum(1 for l in leads if l["fixture"])} in selftest fixtures, '
          f'{len(new)} NEW.')
    if new:
        # S130: THIS LINE NAMED `mark_wire --apply` AND THAT ARC HAS RUN. A message pinned to
        # one arc expires with it and then quietly misinstructs whoever reads it next - the
        # same shape as an acceptance keyed on a site that no longer exists (S129 Control F).
        # The RULE is not about that tool: a NEW lead is an unread dependency on how a
        # character is SPELLED, and it must be read before ANY sweep that rewrites one.
        print('\n  A NEW lead is an UNREAD dependency on a character\'s spelling.')
        print('  Read every one before running any sweep that rewrites a glyph, mark or')
        print('  entity, and accept it BY NAME with a reason (S127 rule 19).')
    return 1 if new else 0


# ---------------------------------------------------------------------------------------
def _selftest():
    import tempfile
    ok = True

    def check(label, cond, detail=''):
        nonlocal ok
        ok = ok and bool(cond)
        print(f'   {"OK  " if cond else "FAIL"}  {label}  {detail}')

    def scratch(body):
        d = tempfile.mkdtemp()
        p = os.path.join(d, 'probe.py')
        pathlib.Path(p).write_text(body, encoding='utf-8')
        return scan_file(p)

    print(f'glyph_scan.py {VERSION} - selftest\n')

    print('CONTROL A (LOUD on the S128 defect SHAPE, reproduced as a fixture)')
    # The original version of this control asserted that §5.1's two pins were present in
    # the live book_gates.py. S129 REMOVED those pins, and the control failed -- correctly,
    # but for the wrong reason: it was pinned to a defect that was supposed to go away.
    # A control that depends on the state of what it audits is not a control. The shape is
    # reproduced here verbatim instead, so this stays loud forever.
    r = scratch(
        "_FAMGLYPH = {'TIP': '\\U0001F4A1'}\n"
        "for c in blocks:\n"
        "    if c['glyph'] not in _FAMGLYPH.values():\n"
        "        continue\n"
        "    want = _FAMGLYPH[fam]\n"
        "    if not label.startswith(want):\n"
        "        bad.append('x')\n")
    d1 = [l for l in r if l['shape'] == 'D1']
    d2 = [l for l in r if l['shape'] == 'D2']
    check('D1 finds the glyph-field scope filter', len(d1) == 1,
          d1[0]['expr'] if d1 else 'NOT FOUND')
    check('D2 reaches the .values() view, not stepped past',
          any('_FAMGLYPH' in l['expr'] and 'values' in l['expr'] for l in d2),
          next((l['expr'] for l in d2 if 'values' in l['expr']), 'NOT FOUND'))
    check('and the table subscript is found too',
          any(l['expr'] == '_FAMGLYPH[fam]' for l in d2),
          str([l['expr'] for l in d2]))

    print('\nCONTROL B (SILENT on decoration): an emoji that is only EMITTED is not a pin')
    r = scratch("print('\\U0001F4A1 TIP')\nx = f'{1} \\U0001F4D8'\n")
    check('emitted emoji produces no lead', len(r) == 0, f'{len(r)} lead(s)')

    print('\nCONTROL C (the two detectors are INDEPENDENT - neither subsumes the other)')
    only1 = scratch("for c in blocks:\n    g = c['glyph']\n")
    only2 = scratch("MARKS = {'a': '\\U0001F4A1'}\nif s.count(MARKS['a']):\n    pass\n")
    check('D1 fires where no glyph literal appears',
          [l['shape'] for l in only1] == ['D1'], str([l['shape'] for l in only1]))
    check('D2 fires where the glyph field is never read',
          [l['shape'] for l in only2] == ['D2'], str([l['shape'] for l in only2]))

    print('\nCONTROL D (a function-LOCAL derived from a pin is not itself reported twice)')
    r = scratch("def f(s):\n    n = s.count('\\u2610')\n    return n != 3\n")
    check('one lead, not two', len(r) == 1, f'{len(r)} lead(s): {[l["expr"] for l in r]}')

    print('\nCONTROL E (a NEW site is loud even when it looks exactly like an accepted one)')
    r = scratch("for c in blocks:\n    g = c.get('glyph')\n")
    key = ('probe.py', 'D1', "c.get('glyph')")
    check('identical expression in an UNNAMED file is NOT accepted',
          key not in ACCEPTED and len(r) == 1,
          'acceptance is keyed by file, not by spelling')

    print('\nCONTROL F (the ACCEPTED table cannot certify a site that no longer exists)')
    live = {(l['file'], l['shape'], l['expr'])
            for l in scan(sorted(str(p) for p in pathlib.Path('.').glob('*.py')))}
    stale = [k for k in ACCEPTED if k not in live]
    check('every accepted key still matches a real site', not stale, str(stale))

    print('\nCONTROL G (a parse failure is reported, never swallowed)')
    r = scratch("def f(:\n")
    check('malformed source yields a PARSE-FAIL lead',
          len(r) == 1 and r[0]['shape'] == 'PARSE-FAIL', str([l['shape'] for l in r]))

    print('\nALL CONTROLS PASS' if ok else '\nSELFTEST FAILED')
    return 0 if ok else 1


if __name__ == '__main__':
    here = os.path.dirname(os.path.abspath(__file__))
    os.chdir(here)
    sys.exit(_selftest() if '--selftest' in sys.argv else _report())
