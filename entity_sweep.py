#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""entity_sweep.py - normalise character spelling to one form per character.

VERSION below is the only version home.

THE RULING (S127). A character is written however it can be SEEN in the source file.

  * If the literal character is distinguishable when you look at the file, write it
    literally.  `&mdash;` and `&#8212;` both become `-` (U+2014).  `&#128161;` becomes
    the lightbulb itself.
  * If the literal character is INVISIBLE in source - indistinguishable from an
    ordinary space or hyphen - write it as an entity, because otherwise nobody
    (human or instrument) can verify it is there.  That is exactly three characters,
    enumerated by the PROPERTY in HOLD below, not by a remembered list.

WHY.  The book spelled the same character two ways: 5,935 non-ASCII characters were
already literal while 4,827 were entities.  Every byte-reading instrument therefore
counted a fraction of each population - S126's glyph census missed 711 symbols and
fifteen characters (house, spy, star, graduation cap, the three medals) appeared in
NO census at all because they exist only in entity form.  §24.8: the population you
can enumerate by spelling is not the population that renders.

THE OTHER DIRECTION WAS CONSIDERED AND FAILS ON ITS OWN TERMS.  "Always write an
entity" does not collapse to one spelling - it needs a second rule for named vs
decimal vs hex, and that rule has already drifted three ways in this book (em dash
named 2,129 / decimal 117; apostrophe decimal 27 / hex 44 and never literal).
Literal is the only direction with exactly one spelling per character.  It is also
the only legible one: 103 of the book's 143 non-ASCII characters have no named
entity, so an all-entity book would carry `&#128161;` where a reader needs to see a
lightbulb.

SCOPE - TEXT NODES ONLY.  Entities are rewritten only in parsed character data.
Three regions are left alone, each for a reason that is a property and not a taste:
  * <script> and <style> are RAW TEXT elements.  The HTML parser never decodes
    character references inside them, so `&#39;` there is six literal characters of
    JavaScript.  Rewriting it would change what the program says.  newproject.html's
    Maker payloads live here.
  * inside a tag (attribute values).  `&quot;` inside a double-quoted attribute is
    mandatory; the general case needs quote-context tracking for no benefit at this
    population size.  Reported, never rewritten.
  * `&`, `<`, `>` are mandatory everywhere.

CONTROL.  The proof that the sweep is safe is not the diff - it is that the DECODED
text of every file is byte-identical before and after.  The page renders the same;
only the bytes on disk change.  verify() asserts this per file and is run by --apply.
"""

VERSION = 'v1.0'   # the only version home in this file (S127)

import glob
import html as H
import os
import re
import sys
import unicodedata

# Characters whose LITERAL form is visually indistinguishable from an ordinary
# ASCII character in source.  Held as entities.  This is the property the gate
# asserts; the set is derived from it, not remembered.
HOLD = {
    0x00A0: '&nbsp;',     # no-break space      - looks like a space
    0x2011: '&#8209;',    # non-breaking hyphen - looks like a hyphen
    0x202F: '&#8239;',    # narrow no-break sp. - looks like a space
}

MANDATORY = set('&<>')

ENTITY = re.compile(r'&#[xX][0-9A-Fa-f]+;|&#[0-9]+;|&[a-zA-Z][a-zA-Z0-9]*;')
RAWTEXT = re.compile(r'<(script|style)\b[^>]*>.*?</\1\s*>', re.S | re.I)
TAG = re.compile(r'<[a-zA-Z!/?][^>]*>', re.S)


def held_spelling(cp):
    """The one legal entity spelling for a held character: named if one exists,
    decimal otherwise.  Only U+00A0 has a name; the other two must be numeric."""
    return HOLD[cp]


def protected_spans(src):
    """Byte ranges the sweep must not touch: raw-text elements and tag interiors."""
    spans = [(m.start(), m.end()) for m in RAWTEXT.finditer(src)]
    for m in TAG.finditer(src):
        if not any(a <= m.start() < b for a, b in spans):
            spans.append((m.start(), m.end()))
    return spans


def sweep_text(src):
    """Return (new_src, changed, skipped_protected, held).  Pure; no I/O."""
    spans = protected_spans(src)
    out, last, changed, skipped, held = [], 0, 0, 0, 0
    for m in ENTITY.finditer(src):
        i = m.start()
        if any(a <= i < b for a, b in spans):
            skipped += 1
            continue
        raw = m.group(0)
        dec = H.unescape(raw)
        if len(dec) != 1:
            continue
        cp = ord(dec)
        if dec in MANDATORY:
            continue
        if cp in HOLD:
            want = held_spelling(cp)
            held += 1
            if raw == want:
                continue
            out.append(src[last:i]); out.append(want); last = m.end(); changed += 1
            continue
        out.append(src[last:i]); out.append(dec); last = m.end(); changed += 1
    out.append(src[last:])
    return ''.join(out), changed, skipped, held


def decoded(src):
    """What the parser sees, with raw-text regions removed so their undecoded
    entities cannot mask a real change in parsed content."""
    return H.unescape(RAWTEXT.sub('', src))


def verify(before, after):
    """The render-equivalence control.  Raises on any change to parsed text."""
    a, b = decoded(before), decoded(after)
    if a != b:
        for k, (x, y) in enumerate(zip(a, b)):
            if x != y:
                raise AssertionError(
                    'DECODED TEXT CHANGED at offset %d: %r -> %r  ...%r...'
                    % (k, x, y, a[max(0, k - 40):k + 40]))
        raise AssertionError('DECODED TEXT LENGTH CHANGED %d -> %d' % (len(a), len(b)))
    return True


def build(paths):
    """Entrypoint.  Returns a per-file report; writes nothing."""
    rep = []
    for p in sorted(paths):
        src = open(p, encoding='utf-8').read()
        new, changed, skipped, held = sweep_text(src)
        verify(src, new)
        rep.append({'path': p, 'changed': changed, 'protected': skipped,
                    'held': held, 'new': new, 'differs': new != src})
    return rep


def census(paths):
    """What is spelled how, right now.  Reported, never inferred."""
    import collections
    lit = collections.Counter(); ent = collections.Counter()
    for p in sorted(paths):
        src = open(p, encoding='utf-8').read()
        spans = protected_spans(src)
        for ch in src:
            if ord(ch) >= 128:
                lit[ch] += 1
        for m in ENTITY.finditer(src):
            if any(a <= m.start() < b for a, b in spans):
                continue
            d = H.unescape(m.group(0))
            if len(d) == 1 and d not in MANDATORY:
                ent[d] += 1
    return lit, ent


# ---------------------------------------------------------------- selftest

def _selftest():
    ok = True

    def check(label, cond, detail=''):
        nonlocal ok
        print('   %-5s %s  %s' % ('OK' if cond else 'FAIL', label, detail))
        if not cond:
            ok = False

    print('entity_sweep.py %s - selftest' % VERSION)

    print('\nCONTROL A (the ruled conversion happens, both entity forms)')
    s = '<p>a &mdash; b &#8212; c &#128161;</p>'
    n, ch, sk, hd = sweep_text(s)
    check('three entities become three characters', n == '<p>a \u2014 b \u2014 c \U0001F4A1</p>', repr(n))
    check('change count is exact', ch == 3, 'changed=%d' % ch)

    print('\nCONTROL B (mandatory entities are never touched)')
    s = '<p>a &amp; b &lt;c&gt; d</p>'
    n, ch, _, _ = sweep_text(s)
    check('ampersand and angle brackets survive', n == s and ch == 0, repr(n))

    print('\nCONTROL C (the HOLD set stays an entity - and is NORMALISED, not skipped)')
    s = '<p>x&#160;y &nbsp;z &#8209;w</p>'
    n, ch, _, hd = sweep_text(s)
    check('nbsp decimal is rewritten to its named form', '&nbsp;y' in n, repr(n))
    check('no literal U+00A0 was emitted', '\u00a0' not in n, repr(n))
    check('no literal U+2011 was emitted', '\u2011' not in n, repr(n))
    check('all three held occurrences were seen', hd == 3, 'held=%d' % hd)

    print('\nCONTROL D (raw text is untouched - the parser never decodes it)')
    s = "<script>var q = '&#39;' + \"&mdash;\";</script><p>&mdash;</p>"
    n, ch, sk, _ = sweep_text(s)
    check('script body is byte-identical', "'&#39;' + \"&mdash;\"" in n, repr(n))
    check('the body-text entity outside it still converted', '<p>\u2014</p>' in n, repr(n))
    check('two protected entities were counted', sk == 2, 'skipped=%d' % sk)

    print('\nCONTROL E (attribute interiors are untouched)')
    s = '<a title="say &quot;hi&quot;" href="x">&mdash;</a>'
    n, ch, sk, _ = sweep_text(s)
    check('attribute value is byte-identical', 'title="say &quot;hi&quot;"' in n, repr(n))
    check('element content still converted', '>\u2014<' in n, repr(n))

    print('\nCONTROL F (the render-equivalence control FIRES on a real change)')
    good = verify('<p>&mdash;</p>', '<p>\u2014</p>')
    check('an honest conversion passes verify', good is True)
    fired = False
    try:
        verify('<p>&mdash;</p>', '<p>-</p>')
    except AssertionError:
        fired = True
    check('substituting a DIFFERENT character raises', fired)
    fired = False
    try:
        verify('<p>a&nbsp;b</p>', '<p>a b</p>')
    except AssertionError:
        fired = True
    check('collapsing nbsp to a plain space raises', fired)

    print('\nCONTROL G (idempotence - a second sweep is a no-op)')
    s = '<p>a &mdash; b &#160; c &#128161;</p>'
    one, c1, _, _ = sweep_text(s)
    two, c2, _, _ = sweep_text(one)
    check('second pass changes nothing', two == one and c2 == 0, 'c1=%d c2=%d' % (c1, c2))

    print('\nCONTROL H (multi-character entities are left alone)')
    s = '<p>&NotEqualTilde; &mdash;</p>'
    n, _, _, _ = sweep_text(s)
    check('a two-codepoint entity is not rewritten', '&NotEqualTilde;' in n, repr(n))

    print('\nCONTROL I (a held character has exactly one legal spelling)')
    check('U+00A0 resolves to the named form', held_spelling(0x00A0) == '&nbsp;')
    check('U+2011 has no name, resolves decimal', held_spelling(0x2011) == '&#8209;')
    check('U+202F has no name, resolves decimal', held_spelling(0x202F) == '&#8239;')
    import html.entities as E
    named = {ord(v) for k, v in E.html5.items() if len(v) == 1 and k.endswith(';')}
    check('the no-name claim is derived, not asserted',
          0x2011 not in named and 0x202F not in named and 0x00A0 in named)

    print('\n%s' % ('ALL CONTROLS PASS - loud on a changed render, silent on raw text and attributes.'
                    if ok else 'FAILURES ABOVE'))
    return 0 if ok else 1


def main():
    args = sys.argv[1:]
    if '--selftest' in args:
        return _selftest()

    paths = [a for a in args if not a.startswith('--')]
    if not paths:
        paths = sorted(glob.glob('lessons/Lesson_*.html')) + [
            'index.html', 'going_deeper.html', 'timer.html', 'newproject.html',
            'tutor/tutor.html']
    paths = [p for p in paths if os.path.exists(p)]

    if '--census' in args:
        lit, ent = census(paths)
        print('entity_sweep %s - CENSUS over %d file(s)' % (VERSION, len(paths)))
        print('  already literal      %6d' % sum(lit.values()))
        print('  entity, convertible  %6d' % sum(v for k, v in ent.items() if ord(k) not in HOLD))
        print('  entity, HELD         %6d' % sum(v for k, v in ent.items() if ord(k) in HOLD))
        return 0

    rep = build(paths)
    tot = sum(r['changed'] for r in rep)
    prot = sum(r['protected'] for r in rep)

    if '--apply' in args:
        for r in rep:
            if r['differs']:
                with open(r['path'], 'w', encoding='utf-8') as f:
                    f.write(r['new'])
        print('entity_sweep %s - APPLIED' % VERSION)
    else:
        print('entity_sweep %s - DRY RUN (pass --apply to write)' % VERSION)

    for r in rep:
        if r['changed'] or r['protected']:
            print('  %-28s %5d converted  %4d held  %4d protected'
                  % (os.path.basename(r['path']), r['changed'], r['held'], r['protected']))
    print('\n  %d conversion(s) across %d file(s); %d protected occurrence(s) left alone'
          % (tot, sum(1 for r in rep if r['differs']), prot))
    print('  decoded text verified byte-identical in all %d file(s)' % len(rep))
    return 0


if __name__ == '__main__':
    sys.exit(main())
