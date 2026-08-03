#!/usr/bin/env python3
"""class_sweep.py v1.0 — class-scope questions answered by a PARSER, not a regex.

Entrypoint is sweep(paths) — not main(), not index().        (S110)

WHY THIS EXISTS. Every class-scope number in S110 was first derived by regex over raw
HTML, and the method failed three separate times in one session:

  1. `\\b` matched `div-ai-center` INSIDE `div-ai-center-2` and produced five phantom
     non-nav uses — a wrong finding, reported before it was caught.
  2. `startswith('#section-1')` matched `#section-10`.
  3. A stray `.html$` folded into a stray-file grep counted four legitimate root pages.

`-` and `#` are not word characters, so `\\b` does not bound a class name or a fragment.
The corpus makes this expensive rather than theoretical: **292 pairs of class tokens where
one name is a prefix of another**, out of 657 tokens. A substring audit miscounts all 292.

This walks the real DOM with html.parser, which knows what an attribute is, and compares
whole tokens only.

  python3 class_sweep.py --selftest        controls, loud on planted defects
  python3 class_sweep.py <token> [...]     where is this class used, and inside what
  python3 class_sweep.py --traps           every prefix collision in the corpus
  python3 class_sweep.py --nav             the nav container of every lesson
"""
import glob, sys
from html.parser import HTMLParser
from collections import Counter, defaultdict

VERSION = 'v1.0'
VOID = {'br', 'img', 'hr', 'meta', 'link', 'input', 'source', 'col', 'area', 'base'}


class Walker(HTMLParser):
    """Records (tag, token, parent_tag, parent_tokens, href) for every classed element,
    and keeps a real element stack so 'parent' means parent, not 'nearby in the bytes'."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack = []
        self.rows = []
        self.links = []          # (href, parent_tag, parent_tokens)

    def _open(self, tag, attrs, selfclosing=False):
        d = dict(attrs)
        toks = (d.get('class') or '').split()
        ptag, ptoks = self.stack[-1] if self.stack else ('', [])
        for t in toks:
            self.rows.append((tag, t, ptag, tuple(ptoks)))
        if tag == 'a' and 'href' in d:
            self.links.append((d['href'], ptag, tuple(ptoks)))
        if tag not in VOID and not selfclosing:
            self.stack.append((tag, toks))

    def handle_starttag(self, tag, attrs):
        self._open(tag, attrs)

    def handle_startendtag(self, tag, attrs):
        self._open(tag, attrs, selfclosing=True)

    def handle_endtag(self, tag):
        for i in range(len(self.stack) - 1, -1, -1):
            if self.stack[i][0] == tag:
                del self.stack[i:]
                return


def walk(path=None, text=None):
    w = Walker()
    w.feed(text if text is not None else open(path, encoding='utf-8').read())
    return w


def sweep(paths):
    """ENTRYPOINT. -> (per_class, per_tag, links) with no side effects.
    per_class: token -> Counter(filename)   per_tag: token -> Counter(tag)"""
    per_class = defaultdict(Counter)
    per_tag = defaultdict(Counter)
    links = defaultdict(list)
    for f in paths:
        short = f.split('/')[-1]
        w = walk(f)
        for tag, tok, ptag, ptoks in w.rows:
            per_class[tok][short] += 1
            per_tag[tok][tag] += 1
        links[short] = w.links
    return per_class, per_tag, links


def traps(per_class):
    """Pairs where one class name is a strict prefix of another. Every one of these is
    a place a substring audit silently double-counts."""
    names = sorted(per_class)
    return [(a, b) for a in names for b in names
            if a != b and a.startswith(b) and len(a) > len(b)]


def nav_container(path):
    """The class tokens on the PARENT of the anchor whose href is exactly '#section-1'.
    Exact match: '#section-1'.startswith is a trap, it also accepts '#section-10'."""
    w = walk(path)
    out = set()
    for href, ptag, ptoks in w.links:
        if href == '#section-1':
            out |= set(ptoks)
    return out


def lessons():
    return sorted(glob.glob('lessons/Lesson_*.html'))


def selftest():
    ok = True

    def rep(label, passed, detail=''):
        nonlocal ok
        ok = ok and passed
        print('   %-5s %s%s' % ('OK' if passed else 'FAIL', label, ('  ' + detail) if detail else ''))

    print('CONTROL A (whole tokens, not substrings): the exact failure that started this')
    doc = ('<div class="div-ai-center">a</div>'
           '<div class="div-ai-center-2">b</div>'
           '<div class="div-ai-center-2">c</div>')
    pc, _, _ = _sweep_text(doc)
    rep('div-ai-center counted once, not three times',
        sum(pc['div-ai-center'].values()) == 1 and sum(pc['div-ai-center-2'].values()) == 2,
        'got %d / %d' % (sum(pc['div-ai-center'].values()), sum(pc['div-ai-center-2'].values())))

    print('CONTROL B (multi-class attributes): each token counted separately, once')
    pc, _, _ = _sweep_text('<p class="alpha beta alpha-2">x</p>')
    rep('three tokens, one element',
        all(sum(pc[t].values()) == 1 for t in ('alpha', 'beta', 'alpha-2')) and len(pc) == 3)

    print('CONTROL C (parent is PARENT, not proximity): a sibling must not be reported')
    doc = '<div class="wrap"><a href="#section-1">n</a></div><div class="decoy"></div>'
    _, _, lk = _sweep_text(doc)
    par = {t for h, pt, pts in lk['<text>'] if h == '#section-1' for t in pts}
    rep('parent is wrap, decoy absent', par == {'wrap'}, str(sorted(par)))

    print('CONTROL D (href exact match): #section-10 must NOT satisfy #section-1')
    doc = '<div class="realnav"><a href="#section-1">a</a></div>' \
          '<div class="notnav"><a href="#section-10">b</a></div>'
    _, _, lk = _sweep_text(doc)
    par = {t for h, pt, pts in lk['<text>'] if h == '#section-1' for t in pts}
    rep('only realnav matched', par == {'realnav'}, str(sorted(par)))

    print('CONTROL E (the sweep can DISAGREE): a deliberately wrong count must not pass')
    pc, _, _ = _sweep_text('<i class="solo"></i>')
    rep('claiming 2 uses of a 1-use class disagrees', sum(pc['solo'].values()) != 2)

    print('CONTROL F (unclosed tags do not corrupt the stack)')
    doc = '<div class="outer"><p class="para"><b class="bold">x</div><span class="after"></span>'
    pc, _, _ = _sweep_text(doc)
    rep('all four tokens seen despite bad nesting',
        all(sum(pc[t].values()) == 1 for t in ('outer', 'para', 'bold', 'after')))

    print('CONTROL G (cross-method agreement on the LIVE corpus): the parser and a')
    print('  WHOLE-TOKEN regex must agree on every class in the book, and substring')
    print('  matching must disagree with both. Stated as an invariant, not as counts —')
    print('  hard-coding today\'s numbers would fail the day the rail renames a class,')
    print('  and the obvious repair would be to update the numbers, which is drift.')
    import re
    ls = lessons()
    if not ls:
        rep('corpus present', False, 'run from the repo root')
    else:
        per_class, _, _ = sweep(ls)
        text = {f: open(f, encoding='utf-8').read() for f in ls}
        mismatch, trap_seen = [], 0
        for tok in per_class:
            exact = sum(len(re.findall(
                r'class="[^"]*(?<![-\w])' + re.escape(tok) + r'(?![-\w])', text[f]))
                for f in ls)
            if exact != sum(per_class[tok].values()):
                mismatch.append(tok)
            loose = sum(t.count('"' + tok) + t.count(' ' + tok) for t in text.values())
            if loose > sum(per_class[tok].values()):
                trap_seen += 1
        rep('parser == whole-token regex for all %d classes' % len(per_class),
            not mismatch, str(mismatch[:4]))
        rep('substring matching over-counts at least one class', trap_seen > 0,
            '%d classes over-counted by a substring audit' % trap_seen)
        rep('every lesson has a nav (an anchor whose href is exactly #section-1)',
            all(nav_container(f) for f in ls))
        rep('prefix collisions exist, so the trap is live', len(traps(per_class)) > 0,
            '%d pairs' % len(traps(per_class)))

    print('\n%s' % ('ALL CONTROLS PASS' if ok else 'CONTROLS FAILED'))
    return 0 if ok else 1


def _sweep_text(doc):
    per_class, per_tag = defaultdict(Counter), defaultdict(Counter)
    w = walk(text=doc)
    for tag, tok, ptag, ptoks in w.rows:
        per_class[tok]['<text>'] += 1
        per_tag[tok][tag] += 1
    return per_class, per_tag, {'<text>': w.links}


def main():
    args = sys.argv[1:]
    if '--selftest' in args:
        return selftest()
    ls = lessons()
    if not ls:
        print('run from the repo root'); return 1

    if '--nav' in args:
        print('nav container per lesson, by parse (anchor href == "#section-1")')
        for f in ls:
            print('  %-6s %s' % (f.split('/')[-1].replace('Lesson_', 'L').replace('.html', ''),
                                 ', '.join(sorted(nav_container(f))) or '(none)'))
        return 0

    per_class, per_tag, _ = sweep(ls)
    if '--traps' in args:
        tr = traps(per_class)
        print('%d prefix collision(s) among %d class tokens.' % (len(tr), len(per_class)))
        print('A substring audit miscounts every one of these.\n')
        for a, b in tr:
            print('  %-30s contains %-26s (%d vs %d uses)'
                  % (a, b, sum(per_class[a].values()), sum(per_class[b].values())))
        return 0

    toks = [a for a in args if not a.startswith('--')]
    if not toks:
        print('class_sweep.py %s — %d lessons, %d class tokens, %d uses, %d prefix collisions'
              % (VERSION, len(ls), len(per_class),
                 sum(sum(c.values()) for c in per_class.values()), len(traps(per_class))))
        print('\n  --selftest   --nav   --traps   <class-token> [...]')
        return 0
    for t in toks:
        c = per_class.get(t)
        if not c:
            print('%s: not used in any lesson' % t); continue
        print('%s — %d use(s) in %d lesson(s), on <%s>'
              % (t, sum(c.values()), len(c),
                 '>, <'.join(k for k, _ in per_tag[t].most_common())))
        for f, n in sorted(c.items()):
            print('   %-18s %d' % (f, n))
        near = [a for a, b in traps(per_class) if b == t]
        if near:
            print('   PREFIX COLLISION: a substring audit would also count %s' % ', '.join(near))
    return 0


if __name__ == '__main__':
    sys.exit(main())
