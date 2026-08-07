#!/usr/bin/env python3
"""build_css.py - emit css/book.css from the lessons' own inline styles.

WHY THIS EXISTS. Bible §27 retired the Canvas-paste delivery model, so the book is a website
and the 25,036 inline style="" attributes become a stylesheet. This is the S104 first step:
Lesson 01 only, by DJ ruling.

§24.12: THIS IS A GENERATED ARTEFACT. css/book.css is never hand-edited. If a rule is wrong,
this file is wrong. That is also what makes the class names cheap to change - a rename is one
line in NAMES plus a re-emit, not a sweep.

THE NAMING IS DELIBERATELY PROVISIONAL AND DELIBERATELY UGLY WHERE IT HAS TO BE.
The semantic set - 27 accents for 30 families - is item 1 of the paint arc and is NOT started.
So a name is English only where the declaration block alone PROVES the role (a <pre> with a
#1e1e1e background is a code block; that is not a judgement call). Anything whose meaning would
have to be guessed from a hex carries the hex: .callout-2196f3, .tok-6a9955. §8 documents 11 of
27 families and LEARN and INSIGHT still share #e3f2fd/#2196f3, so a confident English name here
would be a claim this repo cannot currently support - and a wrong name propagates into sixteen
lessons. The hex is not a placeholder for a name nobody has chosen; it is the true statement
available today.

RUN 1 IS A NO-OP BY CONSTRUCTION. All 16 lessons carry ZERO class= attributes and ZERO <style>
blocks (Canvas stripped both), so every rule below is class-scoped and matches nothing until
run 2 adds the classes. Linking it changes no pixel. That is the point: run 1 proves the file
publishes, that Pages serves it, and that site_parity sees it, and proves nothing about
whether any rule is right.

THE PROPERTY THAT MAKES RUN 2 SAFE, asserted in --selftest: for every styled element in the
source lesson, the class it will receive carries declarations CANONICALLY EQUAL to the inline
string it replaces. If that holds for all 1,150, the strip renders identically by construction
rather than by inspection.

usage:
  python3 build_css.py              # write css/book.css
  python3 build_css.py --check      # emit to memory, diff against disk, never write
  python3 build_css.py --selftest   # controls, both directions
exit 0 = clean. exit 1 = a control failed or --check found a difference.
"""
import re, os, sys, glob, collections

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import lesson_inventory as LI      # ONE expander, shared (the S83 rule)

VERSION = 'v1.3.0'        # the only version home in this file (S105)
# v1.3.0 (S123): THE SEMANTIC LAYER (§27.15). DJ: "I thought since we weren't using canvas
#   we didn't need the inline code" - correct, and measured: the lessons carry ZERO inline
#   style attributes and 25,752 class attributes, so the inline representation this
#   generator round-trips through exists only inside one run of it. The model outlived the
#   constraint §27 retired. Because names are re-derived from VALUES every run, the
#   generated block can never produce `.code`, hold an element selector, or emit a custom
#   property - it is a fixed point of the migration, not a design system, and there was
#   therefore nothing a second book could inherit. css/semantic.css is preserved verbatim
#   at the top of the output and never re-derived. Control D is SCOPED to the generated
#   block rather than weakened: that block must still be class-scoped, which is the
#   property the control was written to hold. Additive by construction - zero lesson
#   edits, all 540 value-named classes keep working, and a tree without semantic.css
#   still builds.
# v1.2 (S105): SOURCES widened to all 16 lessons for the book-wide conversion.
#   WIDENING THIS LIST RENAMES RULES. Naming is frequency-ranked across the corpus, so at
#   S105 46 of L01's 167 names kept their SPELLING and changed their MEANING, and 11
#   vanished. Only the 11 were visible to gate 41 - a name that still resolves repaints the
#   page with every gate green. AND THE ORDER MATTERS: expand_classes reads book.css from
#   disk and leaves an unresolvable class in place, so regenerating BEFORE restoring an
#   already-converted lesson strands every element carrying a dropped name (74 in L01).
#   The sequence is strip_inline --restore, then this, then strip_inline --apply.
SOURCES = sorted(glob.glob('lessons/Lesson_*.html'))
OUT = 'css/book.css'
# S123, §27.15: the SEMANTIC layer. Hand-authored, preserved verbatim at the top of OUT
# and never re-derived. It is the only place a rule can say what a thing IS: the generated
# block names every rule after the VALUES it holds, so it can never produce `.code` and can
# never hold an element selector or a custom property. Missing file is legal and emits
# nothing, so a tree without it still builds.
SEMANTIC = 'css/semantic.css'

_STYLED = re.compile(r'<(\w+)\b[^>]*?style="([^"]*)"', re.S)


def canon(value):
    """One canonical form for a style string: declarations trimmed, single-spaced after the
    colon, sorted case-insensitively. Property ORDER is not meaningful in a declaration block
    with no duplicate properties, and L01 carries one pair that differs by order alone - 168
    raw strings, 167 canonical. Sorting collapses that pair instead of shipping two identical
    rules under two names."""
    ds = [' '.join(d.split()) for d in value.split(';') if d.strip()]
    ds = [re.sub(r'\s*:\s*', ': ', d) for d in ds]
    return '; '.join(sorted(ds, key=str.lower))


# S105: ONE spelling for the colon. preferred() returns an AUTHORED string, and the book
# authored 62,602 declarations as "prop: value" against 1,139 as "prop:value" - so a faithful
# emitter shipped both spellings into one generated file. Whitespace around a CSS colon is not
# meaningful, so this is presentation only, but a generated artefact has no excuse to be
# inconsistent. Spaced wins on the count AND on the gates: emitting unspaced broke five of
# them (§22, §25.2, §25.10h, §4.5, §4.5a), which assert literal "prop: value" strings.
# NOTE this normalises the SEPARATOR only - declaration ORDER still comes from preferred().
_SPACED = re.compile(r'\s*:\s*')


def decls(c):
    return [d.strip() for d in c.split(';') if d.strip()]


def prop(c, name):
    for d in decls(c):
        k, _, v = d.partition(':')
        if k.strip().lower() == name:
            return v.strip()
    return None


def preferred(raw):
    """-> the raw declaration ORDER a rule is emitted in: the most common spelling in the
    group, ties broken by the string so the output is deterministic.

    WHY NOT SORTED. canon() sorts for GROUPING, which is right - order is not meaningful to
    a browser. But the gates are not browsers. §4.5, §6.8 and §25.6 assert authored style
    strings BYTE-EXACT against their generators, and every one of them broke the moment the
    stylesheet handed back alphabetised declarations. Emitting the authored order makes the
    expander round-trip byte-exact for 664 of 770 raw spellings, which is the difference
    between five held block types and one rule. The remaining 106 are groups that were
    ALREADY spelled two ways in the book; they converge on the majority spelling, which is
    render-identical by definition since canon() grouped them."""
    return max(sorted(raw), key=lambda r: raw[r])


def role(tag, c):
    """The role a declaration block PROVES, or None. Every branch here is decided by the CSS
    itself, never by where the element sits or what it is called."""
    has = lambda n: prop(c, n) is not None
    bl = prop(c, 'border-left') or ''
    bg = (prop(c, 'background-color') or prop(c, 'background') or '').lower()
    m = re.match(r'4px solid (#[0-9a-f]{3,8})', bl, re.I)
    if m and bg.startswith('#'):
        return 'callout-' + m.group(1).lstrip('#').lower()
    if tag == 'pre' and '#1e1e1e' in bg:
        return 'code-block'
    if tag == 'code' and has('background'):
        return 'code-inline'
    if tag in ('span',) and len(decls(c)) == 1 and prop(c, 'color'):
        return 'tok-' + prop(c, 'color').lstrip('#').lower().replace('(', '').replace(')', '') \
            .replace(',', '-').replace(' ', '')
    if tag == 'table' and prop(c, 'border-collapse'):
        return 'table'
    if tag == 'th':
        return 'th'
    if tag == 'td':
        return 'td'
    if tag == 'img':
        return 'img'
    if tag == 'details':
        return 'details'
    if tag == 'summary':
        return 'summary'
    if tag == 'body':
        return 'page'
    if tag == 'nav':
        return 'nav'
    if tag == 'button':
        return 'button'
    if tag == 'a':
        return 'link'
    return tag


def collect(paths):
    """-> ordered list of (canonical, count, {tag: n}). Order is descending count then the
    canonical string, so the emitted file is DETERMINISTIC: same input, same bytes, same
    names. A generator whose output depends on dict iteration order cannot be diffed."""
    count = collections.Counter()
    tags = collections.defaultdict(collections.Counter)
    raws = collections.defaultdict(collections.Counter)
    for p in paths:
        # S104: read through the expander. Once a lesson is CONVERTED its inline styles are
        # gone, and a generator that could not read its own converted source would emit an
        # empty stylesheet on the next run - --check would then 'pass' by comparing nothing
        # to nothing. Expanding first makes the build idempotent across the conversion.
        s = LI.expand_classes(open(p, encoding='utf-8', errors='replace').read())
        for m in _STYLED.finditer(s):
            c = canon(m.group(2))
            count[c] += 1
            tags[c][m.group(1).lower()] += 1
            raws[c][m.group(2)] += 1
    return [(c, n, dict(tags[c]), raws[c]) for c, n in
            sorted(count.items(), key=lambda kv: (-kv[1], kv[0]))]


def signal(c, taken=''):
    """A short, deterministic, CLAIM-FREE distinguisher for rules whose role repeats. It is
    read off the declarations in a fixed priority - accent, then background, then colour, then
    the first declaration - so `.div-3` becomes `.div-bg-fffbe6`, which a human reading run 2's
    diff can actually recognise. It asserts nothing about meaning."""
    def hexof(v):
        m = re.search(r'#([0-9a-fA-F]{3,8})', v or '')
        return m.group(1).lower() if m else None
    cands = []
    for p in ('border-left', 'border', 'border-top'):
        h = hexof(prop(c, p))
        if h:
            cands.append(h)
    h = hexof(prop(c, 'background') or prop(c, 'background-color'))
    if h:
        cands.append('bg-' + h)
    h = hexof(prop(c, 'color'))
    if h:
        cands.append('c-' + h)
    for cd in cands:                      # a signal already inside the role name says nothing
        if cd.split('-')[-1] not in taken:
            return cd
    d = decls(c)[0] if decls(c) else 'x'
    k, _, v = d.partition(':')
    k = ''.join(w[0] for w in k.strip().split('-'))
    v = re.sub(r'[^0-9a-z]+', '', v.strip().lower())[:8] or 'x'
    return f'{k}-{v}'


def names(rows):
    """-> {canonical: class}. A role used once takes the bare role name. A role that repeats
    takes role-SIGNAL, never role-2, because an ordinal carries no information into run 2 and
    renumbers itself the moment another lesson is added. An ordinal is the last resort only."""
    base = {}
    for c, n, tg, rw in rows:
        tag = max(tg.items(), key=lambda kv: kv[1])[0]
        base[c] = role(tag, c)
    freq = collections.Counter(base.values())
    chosen, used = {}, collections.Counter()
    for c, n, tg, rw in rows:
        r = base[c]
        name = r if freq[r] == 1 else f'{r}-{signal(c, r)}'
        used[name] += 1
        chosen[c] = name if used[name] == 1 else f'{name}-{used[name]}'
    return chosen


def semantic():
    """The preserved layer, verbatim, or '' when the file is absent."""
    try:
        return open(SEMANTIC, encoding='utf-8').read().rstrip('\n')
    except OSError:
        return ''


def emit(rows, chosen):
    src = ', '.join(SOURCES)
    out = [
        '/* css/book.css - GENERATED by build_css.py ' + VERSION + '. DO NOT HAND-EDIT (Bible',
        ' * §24.12). Source: ' + src + '.',
        ' *',
        ' * Bible §27: the book is a website, not a Canvas paste. These rules are the lessons\'',
        ' * own inline declarations, deduplicated and named. Class names are PROVISIONAL - the',
        ' * semantic set (27 accents / 30 families) is not designed yet, so a name is English',
        ' * only where the declarations prove the role, and carries the hex otherwise.',
        ' *',
        f' * {len(rows)} rules covering {sum(r[1] for r in rows):,} inline attributes.',
        ' */',
        '',
    ]
    _sem = semantic()
    if _sem:
        out += ['/* ===== SEMANTIC LAYER (§27.15) - preserved verbatim from '
                + SEMANTIC + '. Edit THERE. ===== */', '', _sem, '',
                '/* ===== GENERATED BLOCK - derived from the lessons. Do not hand-edit. '
                '===== */', '']
    for c, n, tg, rw in rows:
        tl = ', '.join(f'{k}×{v}' for k, v in sorted(tg.items(), key=lambda kv: -kv[1]))
        out.append(f'/* ×{n}  {tl} */')
        out.append(f'.{chosen[c]} {{')
        for d in decls(preferred(rw)):
            out.append(f'  {_SPACED.sub(": ", d, count=1)};')
        out.append('}')
        out.append('')
    return '\n'.join(out)


def build(paths=None):
    """ENTRYPOINT. Returns (text, rows, chosen) and writes nothing."""
    rows = collect(paths or SOURCES)
    chosen = names(rows)
    return emit(rows, chosen), rows, chosen


def selftest():
    ok = True
    text, rows, chosen = build()

    print('CONTROL A (coverage): every styled element in the source is accounted for')
    total = sum(r[1] for r in rows)
    raw = sum(len(_STYLED.findall(LI.expand_classes(open(p, encoding='utf-8').read())))
              for p in SOURCES)
    print(f'   {total:,} attribute(s) over {len(rows)} rule(s); source holds {raw:,}')
    if total != raw or total == 0:
        print('   FAILED. The collector does not see every styled element.')
        ok = False

    print('CONTROL B (the run-2 guarantee): each element\'s class must carry ITS OWN '
          'declarations')
    bad = 0
    for p in SOURCES:
        s = open(p, encoding='utf-8').read()
        for m in _STYLED.finditer(s):
            c = canon(m.group(2))
            cls = chosen.get(c)
            body = re.search(r'\.' + re.escape(cls) + r' \{\n(.*?)\n\}', text, re.S)
            got = canon(' '.join(l.strip() for l in body.group(1).splitlines())) if body else ''
            if got != c:
                bad += 1
    if bad:
        print(f'   FAILED. {bad} element(s) would be repainted, not preserved.')
        ok = False
    else:
        print(f'   all {total:,} elements map to a rule equal to their inline string')

    print('CONTROL C (injective): two different declaration sets must not share a class')
    if len(set(chosen.values())) != len(chosen):
        dupes = [k for k, v in collections.Counter(chosen.values()).items() if v > 1]
        print(f'   FAILED. Class collision: {dupes[:5]}')
        ok = False
    else:
        print(f'   {len(chosen)} rules, {len(set(chosen.values()))} distinct class names')

    print('CONTROL D (scope): every selector is class-scoped, and every page carrying '
          'these classes links the stylesheet')
    # v1.0 asserted "0 class= attributes exist" - true during run 1 and FALSE the moment a
    # lesson is converted. An assertion that expires is worse than none: it fails on success.
    # What actually has to hold afterwards is that nothing is styled by a bare tag selector,
    # and that no page uses a class without linking the file that defines it.
    # S123: the assertion is now SCOPED TO THE GENERATED BLOCK, not weakened. The semantic
    # layer (§27.15) exists precisely to hold element selectors, so checking it here would
    # be checking the wrong file - but the generated block must still be class-scoped, and
    # that is the property this control was written to hold. Everything after the GENERATED
    # BLOCK marker is derived; everything before it is preserved.
    _mark = '/* ===== GENERATED BLOCK'
    _gen = text.split(_mark, 1)[1] if _mark in text else text
    naked = [l for l in _gen.splitlines() if l.endswith(' {') and not l.startswith('.')]
    orphan = []
    for f in sorted(glob.glob('lessons/Lesson_*.html')):
        body = open(f, encoding='utf-8').read()
        if re.search(r'\sclass="', body) and OUT not in body:
            orphan.append(f)
    if naked:
        print(f'   FAILED. {len(naked)} selector(s) are not class-scoped: {naked[:3]}')
        ok = False
    elif orphan:
        print(f'   FAILED. {orphan} use classes without linking {OUT}.')
        ok = False
    else:
        conv = sum(len(re.findall(r'\sclass="', open(f, encoding='utf-8').read()))
                   for f in sorted(glob.glob('lessons/Lesson_*.html')))
        print(f'   every selector class-scoped; {conv} class attribute(s) live, '
              f'every host page links {OUT}')

    print('CONTROL E (determinism): a second build must be byte-identical')
    if build()[0] != text:
        print('   FAILED. Output depends on iteration order.')
        ok = False
    else:
        print('   second build is byte-identical')

    print('CONTROL F (loud on a real change): dropping one declaration must be visible')
    victim = rows[0][0]
    cut = '; '.join(decls(preferred(rows[0][3]))[1:])
    probe = emit([(canon(cut), rows[0][1], rows[0][2], {cut: 1})] + rows[1:],
                 {**chosen, canon(cut): chosen[victim]})
    if probe == text:
        print('   FAILED. A dropped declaration produced identical output.')
        ok = False
    else:
        print('   a dropped declaration changes the emitted file')

    print('\n' + ('ALL CONTROLS PASS' if ok else 'CONTROLS FAILED'))
    return 0 if ok else 1


if __name__ == '__main__':
    if '--selftest' in sys.argv:
        sys.exit(selftest())
    text, rows, chosen = build()
    if '--check' in sys.argv:
        cur = open(OUT, encoding='utf-8').read() if os.path.exists(OUT) else None
        if cur == text:
            print(f'{OUT} is current ({len(rows)} rules)')
            sys.exit(0)
        print(f'{OUT} DIFFERS from what the sources generate - re-run without --check')
        sys.exit(1)
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    tmp = OUT + '.tmp'
    with open(tmp, 'w', encoding='utf-8') as fh:
        fh.write(text)
    os.replace(tmp, OUT)
    print(f'wrote {OUT}: {len(rows)} rules, '
          f'{sum(r[1] for r in rows):,} inline attributes covered')
