#!/usr/bin/env python3
# VERSION below is the ONE home, and it sits ABOVE the changelog so a plain grep of this
# file returns the version and not a changelog line.
VERSION = 'v1.0'
# v1.0 (S103): NEW. Rewrites font-family declarations whose FIRST choice is a designer
#   face into the canon stacks. Bible 17.3a Recipe 1 check 4 and the RoboLore graphics
#   handoff 5 both already name the replacements; this instrument does not rule, it applies.
#   Value-only rewrite: the delimiter, the attribute name and every other byte are preserved.
#   Weight and style are NEVER touched -- Illustrator declares Arial-BoldMT alongside
#   font-weight:700 and Arial-ItalicMT alongside font-style:italic, so dropping the family
#   variant loses nothing. Verified on 1-10 and 8-1 before this file was written.

import re, sys, os, glob, collections

PROSE = 'Arial, Helvetica, sans-serif'
MONO  = 'Courier New, monospace'

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

DECL = re.compile(r'(font-family\s*[:=]\s*)("([^"]*)"|\'([^\']*)\'|([^;"\'>}]+))', re.I)


def _first(value):
    return value.split(',')[0].strip().strip('"\'').lower()


def rewrite(text):
    """Return (new_text, list of (old_value, new_value)). Value-only, delimiter preserved."""
    hits = []

    def sub(m):
        lead, whole, dq, sq, bare = m.group(1), m.group(2), m.group(3), m.group(4), m.group(5)
        value = dq if dq is not None else (sq if sq is not None else bare)
        target = MAP.get(_first(value))
        if target is None:
            return m.group(0)
        # already correct in substance -- do not churn the byte
        if value.strip() == target:
            return m.group(0)
        hits.append((value.strip(), target))
        if dq is not None:
            return lead + '"' + target + '"'
        if sq is not None:
            # canon stacks contain no apostrophe, so a single-quoted home stays single-quoted
            return lead + "'" + target + "'"
        # bare value in a <style> block: preserve any trailing whitespace the declaration had
        trail = bare[len(bare.rstrip()):]
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

    # CONTROL E -- idempotence: a second pass must change nothing
    twice, hits_t = rewrite(out)
    check('CONTROL E: second pass is a no-op', (twice == out, hits_t), (True, []))

    print()
    print('ALL CONTROLS PASS - loud on the four named faces, silent on safe stacks, '
          'weight and style intact.' if ok else '*** CONTROLS FAILED ***')
    return 0 if ok else 1


def main(argv):
    if '--selftest' in argv:
        return selftest()
    write = '--write' in argv
    paths = [a for a in argv[1:] if not a.startswith('-')] or sorted(
        glob.glob('images/**/*.svg', recursive=True))

    tot_files = 0
    tot_hits = 0
    tally = collections.Counter()
    print(f'font_stack_sweep {VERSION}   mode: {"WRITE" if write else "DRY RUN"}   '
          f'{len(paths)} file(s) scanned\n')
    for p in paths:
        with open(p, encoding='utf-8', errors='strict') as fh:
            src = fh.read()
        new, hits = rewrite(src)
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
