#!/usr/bin/env python3
# VERSION below is the ONE home, and it sits ABOVE the changelog so a plain grep of this
# file returns the version and not a changelog line.
VERSION = 'v1.3.0'
# v1.3.0 (S123): DJ ruling B - MONO_BOOK, the book's one mono stack, and the tool pages
#   JOIN THE SCAN. Two findings drove it. (1) 422 declarations across 12 lessons carried
#   FIVE Consolas spellings resolving to THREE different fallbacks off Windows and to one
#   face on Windows, which is why nobody saw it. (2) going_deeper/newproject/timer held
#   four more that NO instrument could see - this sweep never opened them and build_css
#   does not model them (25.6a). The mono target is now CONTEXT-dependent, because an SVG
#   cannot use the `ui-monospace` keyword, and the web-served exemption is DERIVED per
#   file rather than blanket: going_deeper serves Inter, timer and newproject do not.
#   Controls I/J/K are new because every pre-existing control called rewrite() without a
#   path and therefore could not see any of this.
# v1.2.0 (S110): THE VALUE PARSER COULD NOT READ A QUOTED MULTI-FACE STACK, and the
#   consequence was a CORRUPTING WRITE, not merely a miscount. DECL's alternation tried
#   "..." then '...' then a bare run, so `'Consolas','Monaco','Courier New',monospace`
#   matched only the FIRST QUOTED FACE and the rest of the stack was left dangling outside
#   the match. A --write pass would have produced
#       font-family: 'Courier New, monospace','Monaco','Courier New',monospace
#   and, on `'Consolas', monospace`, a family LITERALLY NAMED "Courier New, monospace",
#   which no browser resolves. The tool sits in the session-open ritual and had reported
#   `8 x Consolas` as bare for seven sessions - a false finding that CONTRADICTED a standing
#   note ("15 declarations, all with a fallback, zero bare"). The note was right and the
#   instrument was wrong. Value now parsed whole, faces split on commas OUTSIDE quotes.
# v1.0 (S103): NEW. Rewrites font-family declarations whose FIRST choice is a designer
#   face into the canon stacks. Bible 17.3a Recipe 1 check 4 and the RoboLore graphics
#   handoff 5 both already name the replacements; this instrument does not rule, it applies.
#   Value-only rewrite: the delimiter, the attribute name and every other byte are preserved.
#   Weight and style are NEVER touched -- Illustrator declares Arial-BoldMT alongside
#   font-weight:700 and Arial-ItalicMT alongside font-style:italic, so dropping the family
#   variant loses nothing. Verified on 1-10 and 8-1 before this file was written.

import re, sys, os, glob, collections

PROSE = 'Arial, Helvetica, sans-serif'
MONO  = 'Courier New, monospace'          # SVG target: no web font, no ui-* keyword
# S123, DJ ruling B: the BOOK's mono stack. Distinct from MONO because an SVG cannot
# rely on `ui-monospace` (a CSS keyword) and Illustrator resolves none of these, while a
# browser picks the best face present and falls through to a generic. Measured before the
# ruling: 422 declarations across 12 lessons carried FIVE Consolas stacks resolving to
# THREE different fallbacks off Windows, identical on Windows - which is why it survived.
MONO_BOOK = ("ui-monospace, SFMono-Regular, Menlo, Consolas, "
             "'Liberation Mono', 'Courier New', monospace")

# first-choice face -> canon replacement
MAP = {
    'inter':            PROSE,
    'segoe ui':         PROSE,
    'arialmt':          PROSE,
    'arial-boldmt':     PROSE,
    'arial-italicmt':   PROSE,
    'helvetica neue':   PROSE,
    'roboto':           PROSE,
    'open sans':        PROSE,
    'lato':             PROSE,
    'oxanium':          PROSE,   # wordmark asset only -- never typeset (graphics handoff 5)
    'consolas':         MONO,
    'jetbrains mono':   MONO,
    'monaco':           MONO,
    'menlo':            MONO,
    'sf mono':          MONO,
}

# S108: A FACE THE SITE ACTUALLY SERVES IS NOT A SUBSTITUTION RISK.
# MAP was written for SVGs, where no web font can be relied on, so it rewrites every named
# face to a system stack. That is right for an SVG and WRONG for css/book.css, which now
# joins the scan: index.html, going_deeper.html and all sixteen lessons load Inter from
# fonts.googleapis.com, so proposing Inter -> Arial there would undo the thing the link tag
# exists to do. Exempt only in a stylesheet, and only for faces the repo can be shown to
# serve -- an exemption list is a claim, and this one is checkable against the link tags.
WEB_SERVED = {'inter'}


def _exempt(value, path, src=''):
    """S110: this took a FACE and was called with a whole VALUE. It only ever agreed
    because the old parser truncated a quoted stack to its first face — so fixing the
    parser silently un-exempted `'Inter', -apple-system, sans-serif` in the stylesheet.
    An exemption keyed on the first face is what was always meant.

    S123: the scan widened to the tool pages, so the exemption is DERIVED per file rather
    than assumed. A blanket .html exemption would have been wrong: going_deeper.html links
    fonts.googleapis.com and declares Inter, while newproject.html and timer.html link
    nothing — so an Inter declaration is safe in the first and a real substitution risk in
    the other two. css/book.css stays exempt on the S108 reasoning: it is linked only by
    pages that serve the font, and it carries no <link> of its own to read."""
    if _first(value) not in WEB_SERVED:
        return False
    if path.endswith('.css'):
        return True
    if path.endswith('.html'):
        return 'fonts.googleapis.com' in src
    return False


# The VALUE is everything up to the declaration terminator. Quotes are part of the value,
# never a boundary of it -- treating a quote as a boundary is what truncated the stack.
DECL = re.compile(r"""(font-family\s*[:=]\s*)((?:[^;>}"']|"[^"]*"|'[^']*')+)""", re.I)

def faces(value):
    """Split a font-family value into faces, splitting on commas OUTSIDE quotes."""
    out, buf, q = [], '', None
    for ch in value:
        if q:
            if ch == q:
                q = None
            else:
                buf += ch
        elif ch in '"\'':
            q = ch
        elif ch == ',':
            out.append(buf.strip()); buf = ''
        else:
            buf += ch
    if buf.strip():
        out.append(buf.strip())
    return [f for f in out if f]


def _first(value):
    f = faces(value)
    return f[0].lower() if f else ''



def rewrite(text, path=''):
    """Return (new_text, list of (old_value, new_value)). Value-only; the DELIMITER is
    preserved for an XML attribute and dropped for a CSS declaration, because they are
    not the same thing. `font-family="X"` uses the quote as the attribute delimiter and
    must keep it; `font-family: 'X'` quotes a FAMILY NAME, and a canon stack contains a
    comma, so re-quoting it would declare one family literally named
    "Courier New, monospace" - which no browser resolves."""
    hits = []

    def sub(m):
        lead, raw = m.group(1), m.group(2)
        # peel trailing whitespace AND a self-closing slash: `font-family="X"/>` ends the
        # match at `/`, so the closing quote is not the last character and the delimiter
        # would go undetected. font-family values never contain a slash.
        trail, val = '', raw
        while val and val[-1] in ' \t\n/':
            trail = val[-1] + trail
            val = val[:-1]
        is_attr = '=' in lead
        delim = None
        if len(val) >= 2 and val[0] in '"\'' and val[-1] == val[0] and val[0] not in val[1:-1]:
            delim, val = val[0], val[1:-1]
        target = MAP.get(_first(val))
        # S123: the mono target depends on the CONTEXT, not on the face. A browser can use
        # `ui-monospace`; an SVG consumer cannot, so SVGs keep the plain system stack.
        if target == MONO and (path.endswith('.css') or path.endswith('.html')):
            target = MONO_BOOK
        if target is None:
            return m.group(0)
        if faces(val) == faces(target):
            return m.group(0)          # already correct in substance - do not churn
        hits.append((val.strip(), target))
        if is_attr and delim:
            return lead + delim + target + delim + trail
        return lead + target + trail

    return DECL.sub(sub, text), hits


def selftest():
    ok = True

    def check(label, got, want):
        nonlocal ok
        good = got == want
        ok &= good
        print(f"   {'OK  ' if good else 'FAIL'}  {label}")
        if not good:
            print(f"          got  {got!r}\n          want {want!r}")

    # CONTROL A -- the four named offenders are rewritten, each delimiter preserved
    src = ('<text font-family="Inter, Arial, sans-serif"/>'
           "<text font-family='Consolas, monospace'/>"
           '<style>.a{font-family: Segoe UI, Arial, sans-serif;}'
           '.b{font-family:JetBrains Mono;}</style>')
    out, hits = rewrite(src)
    check('CONTROL A: all four designer faces rewritten', len(hits), 4)
    check('CONTROL A: double quote preserved', '"Arial, Helvetica, sans-serif"' in out, True)
    check('CONTROL A: single quote preserved', "'Courier New, monospace'" in out, True)
    check('CONTROL A: bare style-block value stays bare',
          'font-family: Arial, Helvetica, sans-serif;' in out, True)

    # CONTROL B -- innocent stacks are left byte-identical (the other direction)
    safe = ('<text font-family="Arial, Helvetica, sans-serif"/>'
            '<text font-family="Courier New, monospace"/>'
            '<text font-family="Georgia, serif"/>'
            '<text font-family="\'Courier New\', Courier, monospace"/>')
    out_b, hits_b = rewrite(safe)
    check('CONTROL B: nothing safe is touched', (out_b == safe, hits_b), (True, []))

    # CONTROL C -- a designer face that is NOT first is not a violation and is left alone
    later = '<text font-family="Arial, Inter, sans-serif"/>'
    out_c, hits_c = rewrite(later)
    check('CONTROL C: designer face in fallback position is left alone', out_c, later)

    # CONTROL D -- weight and style must survive, since they live outside the family
    weighted = '.st2{font-family: Arial-BoldMT, Arial; font-weight: 700;}'
    out_d, _ = rewrite(weighted)
    check('CONTROL D: font-weight survives the family rewrite',
          'font-weight: 700' in out_d and 'Arial, Helvetica, sans-serif' in out_d, True)
    italic = '.st8{font-family: Arial-ItalicMT, Arial; font-style: italic;}'
    out_e, _ = rewrite(italic)
    check('CONTROL D: font-style survives the family rewrite',
          'font-style: italic' in out_e and 'Arial, Helvetica, sans-serif' in out_e, True)

    # CONTROL F -- THE DEFECT THIS VERSION EXISTS FOR. A quoted multi-face CSS stack
    # must rewrite to ONE clean value: no faces left dangling after the replacement, and
    # no comma-bearing family name left inside quotes.
    stack = ".code{font-family: 'Consolas','Monaco','Courier New',monospace;}"
    out_f, hits_f = rewrite(stack)
    val_f = out_f.split('font-family:')[1].split(';')[0].strip()
    check('CONTROL F: quoted multi-face stack yields one clean value',
          (faces(val_f), '"' in val_f or "'" in val_f, len(hits_f)),
          (['Courier New', 'monospace'], False, 1))
    quoted_one = ".code{font-family: 'Consolas', monospace;}"
    out_g = rewrite(quoted_one)[0]
    check('CONTROL F: no family is left literally named "Courier New, monospace"',
          "'Courier New, monospace'" in out_g, False)

    # CONTROL G -- every rewritten value parses to EXACTLY the target's face list, so a
    # leftover face can never survive a substitution anywhere in the corpus.
    import glob as _g
    leftovers = []
    for _p in sorted(_g.glob('images/*.svg')) + ['css/book.css']:
        try:
            _src = open(_p, encoding='utf-8', errors='replace').read()
        except OSError:
            continue
        _new, _h = rewrite(_src)
        for _m in DECL.finditer(_new):
            _v = _m.group(2).rstrip(' \t\n/').strip('"\'')
            if MAP.get(_first(_v)) and faces(_v) != faces(MAP[_first(_v)]):
                leftovers.append((_p, _v))
    check('CONTROL G: no leftover faces after a whole-corpus rewrite', leftovers, [])

    # CONTROL H -- control of the control: the v1.1.0 parser MUST fail CONTROL F, or this
    # version fixed nothing. Its alternation tried a quoted run before a bare one, so it
    # matched only the first quoted face.
    _old = re.compile(r'(font-family\s*[:=]\s*)("([^"]*)"|\'([^\']*)\'|([^;"\'>}]+))', re.I)
    _m = _old.search(stack)
    _oldval = _m.group(3) if _m.group(3) is not None else (
        _m.group(4) if _m.group(4) is not None else _m.group(5))
    check('CONTROL H: the old parser read only the first quoted face',
          (_oldval, faces(_oldval)), ('Consolas', ['Consolas']))

    # CONTROL E -- idempotence: a second pass must change nothing
    twice, hits_t = rewrite(out)
    check('CONTROL E: second pass is a no-op', (twice == out, hits_t), (True, []))

    # ---- S123 controls. Everything above calls rewrite() WITHOUT a path, so it only ever
    # exercised the SVG target; the ruling's behaviour was invisible to all of it. An
    # assert that cannot fail is not evidence (27.13's precedent).
    mono = "font-family: Consolas, monospace;"

    # CONTROL I -- the mono target depends on the CONTEXT, both directions.
    css_out, _ = rewrite(mono, 'css/book.css')
    svg_out, _ = rewrite(mono, 'images/x.svg')
    check('CONTROL I: a .css mono stack takes the ruled book stack',
          MONO_BOOK in css_out, True)
    check('CONTROL I: an SVG keeps the plain system stack (no ui-monospace)',
          ('ui-monospace' not in svg_out, MONO in svg_out), (True, True))
    check('CONTROL I: the two contexts genuinely differ', css_out != svg_out, True)

    # CONTROL J -- the ruling is a FIXED POINT. Without this the sweep could "fix" the book
    # and then propose fixing it again forever, which is how a canon stack churns.
    ruled = f'font-family: {MONO_BOOK};'
    fixed, fixed_hits = rewrite(ruled, 'css/book.css')
    check('CONTROL J: the ruled stack is a fixed point', (fixed == ruled, fixed_hits),
          (True, []))

    # CONTROL K -- the exemption is DERIVED, and it must fall BOTH ways. A blanket .html
    # rule would have passed the first of these and wrongly passed the second.
    inter = "'Inter', -apple-system, sans-serif"
    check('CONTROL K: Inter is exempt in a page that SERVES it',
          _exempt(inter, 'going_deeper.html', 'x fonts.googleapis.com y'), True)
    check('CONTROL K: Inter is REPORTED in a page that does not serve it',
          _exempt(inter, 'timer.html', 'no font link here'), False)
    check('CONTROL K: css/book.css stays exempt (S108 reasoning)',
          _exempt(inter, 'css/book.css', ''), True)
    check('CONTROL K: a non-web-served face is never exempt',
          _exempt('Consolas, monospace', 'going_deeper.html', 'fonts.googleapis.com'), False)

    print()
    print('ALL CONTROLS PASS - loud on the four named faces, silent on safe stacks, '
          'weight and style intact.' if ok else '*** CONTROLS FAILED ***')
    return 0 if ok else 1


def main(argv):
    if '--selftest' in argv:
        return selftest()
    write = '--write' in argv
    # S108: css/book.css JOINS THE DEFAULT SCAN. The Windows-only Segoe UI stack that
    # every non-Windows reader had been silently substituting away from lived in .page,
    # in this file, and this sweep reported 0 rewrites for its whole life because it only
    # ever opened SVGs. An instrument that cannot see a file cannot clear it (24.8).
    # S123: THE TOOL PAGES JOIN THE SCAN, for the reason S108 put book.css in it. Their
    # four Consolas declarations were invisible to every instrument: the sweep never
    # opened them, and build_css does not model them (25.6a exempts tool pages from the
    # class migration), so nothing in the tree could see or clear them.
    paths = [a for a in argv[1:] if not a.startswith('-')] or (
        sorted(glob.glob('images/**/*.svg', recursive=True))
        + [f for f in ['css/book.css', 'going_deeper.html', 'newproject.html',
                       'timer.html', 'index.html'] if os.path.exists(f)])

    tot_files = 0
    tot_hits = 0
    tally = collections.Counter()
    print(f'font_stack_sweep {VERSION}   mode: {"WRITE" if write else "DRY RUN"}   '
          f'{len(paths)} file(s) scanned\n')
    for p in paths:
        with open(p, encoding='utf-8', errors='strict') as fh:
            src = fh.read()
        new, hits = rewrite(src, p)
        # pass the RAW value: pre-stripping quotes here left an unbalanced quote that
        # the face splitter then read as an opening delimiter (S110).
        hits = [h for h in hits if not _exempt(h[0], p, src)]
        if not hits:
            continue
        tot_files += 1
        tot_hits += len(hits)
        print(f'  {os.path.basename(p)}')
        for old, target in sorted(set(hits)):
            n = hits.count((old, target))
            tally[old] += n
            print(f'      {n:>3} x  {old}  ->  {target}')
        if write:
            before = len(src.encode())
            tmp = p + '.tmp'
            with open(tmp, 'w', encoding='utf-8') as fh:
                fh.write(new)
            os.replace(tmp, p)
            with open(p, encoding='utf-8') as fh:
                back = fh.read()
            assert back == new, f'{p}: write did not land'
            after = len(back.encode())
            # the only bytes that may move are inside font-family values
            stripped_before = DECL.sub('', src)
            stripped_after = DECL.sub('', back)
            assert stripped_before == stripped_after, \
                f'{p}: bytes changed OUTSIDE a font-family declaration -- reverted expectation'
            print(f'      written  {before:,} B -> {after:,} B  '
                  f'(delta {after - before:+,}; nothing outside font-family moved)')

    print(f'\n  {tot_hits} declaration(s) rewritten across {tot_files} file(s)')
    if tally:
        print('  by first-choice face:')
        for k, v in tally.most_common():
            print(f'      {k:<18}{v}')
    if not write and tot_hits:
        print('\n  DRY RUN - re-run with --write to apply.')
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
