#!/usr/bin/env python3
VERSION = 'v1.0'
# ---------------------------------------------------------------------------------------------
# regex_audit.py - find MATCH-AND-DISCARD: a regex that captures alternatives the surrounding
# code never handles.
#
# WHY. svg_layout_audit._ctm read transforms with
#     r'(translate|scale|matrix|rotate)\s*\(([^)]*)\)'
# and then branched on translate and scale only. rotate and matrix were MATCHED and silently
# dropped. The result was not a crash and not a gap - it was a confident wrong number: a
# rotate(90) label 14 units wide on the page was measured as 95 wide and reported 79 units past
# its panel, which ranked that file 3rd on the graphics work list. Three sessions of a human
# reading the code did not catch it; a render did.
#
# The shape generalises: whenever a pattern enumerates cases, the enumeration is a PROMISE about
# what the code understands. Handling a subset silently converts an unknown into a wrong answer,
# and per DJ's standing rule a wrong answer costs 3x a blank one.
#
# WHAT THIS IS NOT. It is a LEAD GENERATOR, not a verdict (§24.6a). An alternative can be
# legitimately unhandled - matched only to be skipped over, or handled through a dict, or named
# by a variable this tool cannot follow. Every hit must be read before it is believed. It is
# deliberately tuned to over-report: a missed match-and-discard is what it exists to prevent.
#
# ENTRYPOINT IS audit(paths) -> list[dict].
#
# CHANGELOG
# v1.0 (S102): written after the _ctm rotate/matrix find.
# ---------------------------------------------------------------------------------------------

import sys, os, re, ast, glob

RE_FUNCS = {'findall', 'finditer', 'search', 'match', 'fullmatch', 'sub', 'subn', 'split',
            'compile'}
# an alternation of bare words is the enumerating shape; anything with metacharacters in it is
# a pattern, not a case list, and is not what this looks for
WORD_ALT = re.compile(r'\(\s*([A-Za-z][\w-]*(?:\s*\|\s*[A-Za-z][\w-]*)+)\s*\)')


def _string_of(node):
    if isinstance(node, ast.Constant) and isinstance(node.value, str):
        return node.value
    if isinstance(node, ast.JoinedStr):          # f-string: take the literal parts only
        return ''.join(v.value for v in node.values
                       if isinstance(v, ast.Constant) and isinstance(v.value, str))
    return None


def _enclosing(tree, lineno):
    """Innermost function def containing a line, so 'handled nearby' means the same scope."""
    best = None
    for n in ast.walk(tree):
        if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef)):
            end = getattr(n, 'end_lineno', n.lineno)
            if n.lineno <= lineno <= end:
                if best is None or n.lineno > best.lineno:
                    best = n
    return best


def _code_only(src, tree, lo, hi):
    """The scope's CODE, with comments and DOCSTRINGS blanked - but not other string literals.

    Documenting a limitation is not handling it. _ctm's own docstring said "Only translate()
    and scale() are handled - a rotate() or a general matrix() would need more", and that one
    sentence made an earlier build of this tool score rotate and matrix as handled and stay
    silent on the very defect it was written to find. Prose about a case is evidence somebody
    KNEW, which is the opposite of evidence the code copes.

    Ordinary string literals must SURVIVE, because that is what the handling looks like:
    `if fn == 'translate'`. Blanking those made every alternative read as unhandled - the
    mirror-image error, and it failed the controls in the same run that found this one.
    """
    import tokenize, io
    lines = src.splitlines()
    body = lines[lo - 1:hi]
    out = list(body)

    def blank(sr, sc, er, ec):
        for r in range(sr, min(er + 1, len(out))):
            a = sc if r == sr else 0
            b = ec if r == er else len(out[r])
            if 0 <= r < len(out):
                out[r] = out[r][:a] + ' ' * max(0, b - a) + out[r][b:]

    for node in ast.walk(tree):                      # docstrings / bare string statements
        if isinstance(node, ast.Expr) and isinstance(node.value, ast.Constant) \
                and isinstance(node.value.value, str):
            n = node.value
            if lo <= n.lineno <= hi:
                blank(n.lineno - lo, n.col_offset,
                      getattr(n, 'end_lineno', n.lineno) - lo, getattr(n, 'end_col_offset', 0))
    try:
        for t in tokenize.generate_tokens(io.StringIO('\n'.join(body) + '\n').readline):
            if t.type == tokenize.COMMENT:
                blank(t.start[0] - 1, t.start[1], t.end[0] - 1, t.end[1])
    except (tokenize.TokenError, IndentationError):
        pass
    return '\n'.join(out)


def _counted_only(tree, call):
    """True if the match result is merely COUNTED, e.g. len(re.findall(...)).

    A count is not a case list. fit_raster_svg does
        len(re.findall(r'<(rect|circle|ellipse|path|line|polygon|polyline|text)\\b', src))
    to size up a drawing; nothing there is supposed to branch per shape, and reporting it would
    train the reader to skim this tool's output - which is how a real lead gets missed.
    """
    for n in ast.walk(tree):
        if isinstance(n, ast.Call) and isinstance(n.func, ast.Name) and n.func.id == 'len':
            for a in n.args:
                if a is call:
                    return True
    return False


def audit(paths):
    out = []
    for path in paths:
        src = open(path, encoding='utf-8').read()
        try:
            tree = ast.parse(src)
        except SyntaxError as exc:
            out.append({'file': path, 'line': 0, 'pattern': '', 'alts': [],
                        'unhandled': [f'SYNTAX ERROR: {exc}'], 'scope': ''})
            continue
        lines = src.splitlines()
        for node in ast.walk(tree):
            if not isinstance(node, ast.Call):
                continue
            fn = node.func
            name = fn.attr if isinstance(fn, ast.Attribute) else \
                (fn.id if isinstance(fn, ast.Name) else None)
            if name not in RE_FUNCS or not node.args:
                continue
            pat = _string_of(node.args[0])
            if not pat:
                continue
            if _counted_only(tree, node):
                continue
            alts_found = WORD_ALT.findall(pat)
            if not alts_found:
                continue
            scope = _enclosing(tree, node.lineno)
            if scope is None:
                lo, hi = 1, len(lines)
                scope_name = '<module>'
            else:
                lo, hi = scope.lineno, getattr(scope, 'end_lineno', scope.lineno)
                scope_name = scope.name
            body = _code_only(src, tree, lo, hi)
            for group in alts_found:
                alts = [a.strip() for a in group.split('|')]
                unhandled = []
                for a in alts:
                    # handled if the alternative appears as a literal ANYWHERE else in the
                    # scope - a comparison, a dict key, a membership test, anything
                    others = len(re.findall(r'(?<![\w-])' + re.escape(a) + r'(?![\w-])', body))
                    if others <= 1:              # 1 == its occurrence in the pattern itself
                        unhandled.append(a)
                if unhandled and len(unhandled) < len(alts):
                    out.append({'file': path, 'line': node.lineno, 'pattern': pat[:76],
                                'alts': alts, 'unhandled': unhandled, 'scope': scope_name})
    return out


def _selftest():
    """Both directions. A detector that cannot miss is not evidence either (§24.6b)."""
    import tempfile
    ok = True
    seeded = (
        "import re\n"
        "def ctm(tr):\n"
        "    for fn, a in re.findall(r'(translate|scale|matrix|rotate)\\\\s*\\\\(([^)]*)\\\\)', tr):\n"
        "        if fn == 'translate':\n"
        "            pass\n"
        "        elif fn == 'scale':\n"
        "            pass\n"
        "    return 0\n"
    )
    clean = (
        "import re\n"
        "def kinds(t):\n"
        "    for fn in re.findall(r'(alpha|beta)', t):\n"
        "        if fn == 'alpha':\n"
        "            pass\n"
        "        elif fn == 'beta':\n"
        "            pass\n"
        "    return 0\n"
    )
    none_handled = (
        "import re\n"
        "def passthru(t):\n"
        "    return re.findall(r'(cat|dog|emu)', t)\n"
    )
    docstringed = (
        "import re\n"
        "def ctm(tr):\n"
        "    \"\"\"Only translate and scale are handled; a rotate or matrix would need more.\"\"\"\n"
        "    for fn, a in re.findall(r'(translate|scale|matrix|rotate)', tr):\n"
        "        if fn == 'translate':\n"
        "            pass\n"
        "        elif fn == 'scale':\n"
        "            pass\n"
        "    return 0\n"
    )
    counted = (
        "import re\n"
        "def analyse(path):\n"
        "    out = {'path': path}\n"
        "    return len(re.findall(r'<(rect|circle|path|text)', path))\n"
    )
    with tempfile.TemporaryDirectory() as d:
        for nm, body in (('seeded.py', seeded), ('clean.py', clean),
                         ('none.py', none_handled), ('doc.py', docstringed),
                         ('counted.py', counted)):
            open(os.path.join(d, nm), 'w', encoding='utf-8').write(body)
        res = audit(sorted(glob.glob(os.path.join(d, '*.py'))))
        by = {os.path.basename(r['file']): r for r in res}

        if 'seeded.py' not in by:
            print('   FAIL  CONTROL A: the known _ctm shape was NOT detected')
            ok = False
        elif sorted(by['seeded.py']['unhandled']) != ['matrix', 'rotate']:
            print(f'   FAIL  CONTROL A: wrong alternatives named '
                  f'({by["seeded.py"]["unhandled"]})')
            ok = False
        else:
            print('   OK    CONTROL A: names exactly matrix and rotate on the real _ctm shape')

        if 'doc.py' not in by:
            print('   FAIL  CONTROL D: a docstring mention masked the unhandled case')
            ok = False
        elif sorted(by['doc.py']['unhandled']) != ['matrix', 'rotate']:
            print(f'   FAIL  CONTROL D: wrong alternatives ({by["doc.py"]["unhandled"]})')
            ok = False
        else:
            print('   OK    CONTROL D: prose about a case does not count as handling it')

        if 'counted.py' in by:
            print('   FAIL  CONTROL E: a len(re.findall(...)) count was reported as a case list')
            ok = False
        else:
            print('   OK    CONTROL E: a counted match is not treated as a case list')

        if 'clean.py' in by:
            print('   FAIL  CONTROL B: a fully-handled alternation was reported')
            ok = False
        else:
            print('   OK    CONTROL B: fully-handled alternation stays silent')

        if 'none.py' in by:
            print('   FAIL  CONTROL C: a pure extraction regex was reported')
            ok = False
        else:
            print('   OK    CONTROL C: extraction regex (nothing handled) stays silent')
    print()
    print('ALL CONTROLS PASS - loud on the known defect, silent on three innocent shapes.' if ok
          else 'CONTROLS FAILED.')
    return ok


if __name__ == '__main__':
    if '--selftest' in sys.argv:
        sys.exit(0 if _selftest() else 1)
    args = [a for a in sys.argv[1:] if not a.startswith('-')]
    paths = args or sorted(glob.glob('*.py'))
    res = audit(paths)
    print(f'regex_audit {VERSION} - LEADS, NOT VERDICTS. Read each before acting (§24.6a).\n')
    for r in res:
        print(f'{os.path.basename(r["file"])}:{r["line"]}  in {r["scope"]}()')
        print(f'   pattern    {r["pattern"]}')
        print(f'   matched    {" | ".join(r["alts"])}')
        print(f'   NOT handled anywhere in scope: {", ".join(r["unhandled"])}')
        print()
    print(f'{len(res)} lead(s) across {len(paths)} file(s).')
