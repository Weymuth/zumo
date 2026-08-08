#!/usr/bin/env python3
# VERSION is the ONE home and sits ABOVE the changelog, so a plain grep of this file
# returns the version and not a changelog line (S98).
VERSION = 'v1.0'
# v1.0 (S132): first release. Normalises the glossary to BookComponentStandard §7.4.
"""glossary_convert.py - one shape for every glossary entry (BookComponentStandard §7.4).

DJ, S132: "Just make them ALL the same." The glossary shipped in FIVE schemas across the
sixteen lessons - 97 KEY TERM callouts (themselves in four sub-shapes), 14 bare divs, 15
<dl>/<dt> pairs and 25 table rows - and 54 of the 151 carried no `data-family` and no
`data-callout` at all, which made a third of the book's vocabulary invisible to every
instrument that reads the family layer. Nothing could fail on them.

THE REQUIREMENT BEHIND THE RULING IS THE HARVEST. DJ wants to pull a glossary down later.
That needs one shape, and it needs a key. The key is NOT the family - `data-family="KEY
TERM"` returns the glossary entries AND the body teaching callouts together, 184 where the
glossary is 151. The key is the glossary REGION (lesson_inventory v1.3.5), which is
structural and gated. So this tool's job is the SHAPE; the region already answers the
question the shape was blocking.

WHAT IS PRESERVED, AND WHY EACH ONE MATTERS
  * An existing `data-callout` is NEVER reassigned. It is the authored identity (§24.14);
    reassigning it would break the pin, which keys on it.
  * An existing `id="term-*"` is NEVER renamed. 37 of the 97 cards carry one and §27.14
    asserts every link resolves - renaming a targeted anchor breaks a link silently in
    the source and loudly only in the gate.
  * The definition's inner HTML is copied VERBATIM. It carries <code>, <em>, <strong>,
    numeric entities and curly quotes, and §27.16 pins one spelling per character. A
    round-trip through any HTML library would re-encode them.

THE SEPARATOR DASH IS STRIPPED ONLY IN LEADING POSITION. DJ ruled no em dash (S131), and
43 of the 97 cards carried one in one of two places - inline after the term (L04, L16) or
immediately after the head div (L02). A definition may legitimately contain an em dash
mid-sentence: L04's "Light with a wavelength just beyond red - invisible to human eyes"
would lose its punctuation to a global strip. The pattern is anchored to the start of the
definition, where no real definition begins.

NO `data-callout` IS MINTED HERE. The 54 new blocks are written WITHOUT one and
callout_id.py --apply authors them afterwards at the next free ordinal per lesson. This
tool does not get to invent an identity - that is callout_id's single job, and a second
minter would be the third-copy defect (S83).
"""
import glob
import io
import os
import re
import sys
import contextlib
import collections

with contextlib.redirect_stdout(io.StringIO()):
    import lesson_inventory as LI

WRAPPER = 'callout-9b59b6-bg-e7d4ff'
HEAD = 'div-fs-105em'
MARK = '<img src="../images/marks/key.svg" alt="" data-mark="key">'
FAMILY = 'KEY TERM'

_BANNER = LI.BANNER_RE
_TAGS = re.compile(r'<[^>]+>')
_LEAD_DASH = re.compile(r'^(?:\s|&nbsp;|<br\s*/?>)*(?:\u2014|\u2013|&mdash;|&ndash;|-)(?:\s|&nbsp;)+')
_TERM_ID = re.compile(r'id="(term-[^"]+)"')


def flat(h):
    """Tag-stripped text, whitespace collapsed. For slugs and reports only."""
    return ' '.join(_TAGS.sub('', h).split())


def slug(term, taken):
    """`term-SLUG-gloss`, deterministic, asserted unique within the page.

    Deterministic beats pretty: the slug is a function of the term text, so re-running
    this tool on an unconverted lesson produces the same id and a diff shows nothing new.
    The `-gloss` suffix is NOT decoration - a lesson may define the same term in the body
    and in the glossary (seven such pairs live in L01 at S132), ids must be unique per
    page, and the suffix is what keeps them so (§7.4).
    """
    s = flat(term).lower()
    s = re.sub(r'[^a-z0-9]+', '-', s).strip('-')
    base = 'term-%s-gloss' % s
    out, n = base, 2
    while out in taken:
        out, n = '%s-%d' % (base, n), n + 1
    taken.add(out)
    return out


def region(src):
    """(start, end) of the glossary region, by the banner PROPERTY (rule 19)."""
    bans = [(m.start(), m.group(1)) for m in _BANNER.finditer(src)]
    for i, (off, bid) in enumerate(bans):
        if bid == 'glossary':
            return off, (bans[i + 1][0] if i + 1 < len(bans) else len(src))
    return None


def element(src, start):
    """(end, ) of the div element opening at `start`, by depth walk."""
    depth = 0
    for m in re.finditer(r'</?div\b[^>]*>', src[start:]):
        depth += -1 if m.group(0).startswith('</') else 1
        if depth == 0:
            return start + m.end()
    raise AssertionError('unclosed div at %d' % start)


def card(term_html, definition, cid, tid):
    """The canon term card. ONE emitter, so every schema converges on one string."""
    ident = ' data-callout="%s"' % cid if cid else ''
    return ('<div class="%s" data-family="%s"%s>'
            '<div class="%s">%s<strong id="%s">%s</strong></div>'
            '%s</div>' % (WRAPPER, FAMILY, ident, HEAD, MARK, tid,
                          term_html, definition))


def plan(path):
    """[(start, end, new, kind, term, id)] for one lesson, in document order."""
    src = open(path, encoding='utf-8').read()
    reg = region(src)
    if not reg:
        return src, []
    lo, hi = reg
    taken = set(_TERM_ID.findall(src))
    out = []

    # ---- SCHEMA 1: the existing KEY TERM callouts. lesson_inventory finds them, so the
    # detector is the canonical one and not a fifth regex.
    inv = LI.build(path)
    for c in inv['callouts']:
        if c.get('region') != 'glossary':
            continue
        s = c['start']
        e = element(src, s)
        body = src[c['open_end']:e - len('</div>')]
        h = re.search(r'<div class="%s">(.*?)</div>' % HEAD, body, re.S)
        if h:
            head_inner, definition = h.group(1), body[h.end():]
        else:
            # the L16 shape: no head div, term inline in <b>, definition after a dash
            b = re.search(r'<(b|strong)\b[^>]*>(.*?)</\1>', body, re.S)
            assert b, 'no head and no inline term at %s:%d' % (path, s)
            head_inner, definition = b.group(0), body[b.end():]
        # the term is the innermost text of the head, minus the mark
        term_html = re.sub(r'<img[^>]*>', '', head_inner)
        term_html = re.sub(r'^\s*<span>\s*</span>\s*', '', term_html)
        # `em` was in this alternation and regex_audit flagged the branch as unhandled.
        # VERIFIED DEAD before narrowing (§24.6c): zero term heads in the book wrap the
        # term in <em>, measured on the converted tree. A dead branch in a matcher is a
        # claim about the corpus that nothing checks.
        m = re.search(r'<(strong|b|span)\b[^>]*>(.*?)</\1>', term_html, re.S)
        term_txt = m.group(2) if m else flat(term_html)
        existing = _TERM_ID.search(head_inner)
        tid = existing.group(1) if existing else slug(term_txt, taken)
        out.append((s, e, card(term_txt, _LEAD_DASH.sub('', definition.strip()),
                               c.get('callout_id'), tid),
                    'callout', flat(term_txt), tid))

    # ---- SCHEMA 2: the bare div (L04).
    for m in re.finditer(r'<div class="div-9b59b6">(.*?)</div>\n?', src[lo:hi], re.S):
        s = lo + m.start()
        inner = m.group(1)
        t = re.match(r'\s*<(strong|b)\b[^>]*>(.*?)</\1>', inner, re.S)
        assert t, 'bare div with no term at %s:%d' % (path, s)
        term_txt = t.group(2)
        tid = slug(term_txt, taken)
        out.append((s, lo + m.end(), card(term_txt,
                                          _LEAD_DASH.sub('', inner[t.end():].strip()),
                                          None, tid) + '\n',
                    'bare-div', flat(term_txt), tid))

    # ---- SCHEMA 3: <dt>/<dd> (L13, L14). The whole <dl> is replaced, once, by its cards.
    for dl in re.finditer(r'<dl\b[^>]*>(.*?)</dl>', src[lo:hi], re.S):
        cards = []
        for pair in re.finditer(r'<dt\b[^>]*>(.*?)</dt>\s*<dd\b[^>]*>(.*?)</dd>',
                                dl.group(1), re.S):
            term_txt = pair.group(1).strip()
            tid = slug(term_txt, taken)
            cards.append((card(term_txt, _LEAD_DASH.sub('', pair.group(2).strip()),
                               None, tid), flat(term_txt), tid))
        assert cards, 'a <dl> with no dt/dd pair at %s' % path
        out.append((lo + dl.start(), lo + dl.end(),
                    '\n'.join(c[0] for c in cards),
                    'dl:%d' % len(cards), ' | '.join(c[1] for c in cards),
                    ' '.join(c[2] for c in cards)))

    # ---- SCHEMA 4: the table (L11, L15). A HEADER row is not an entry.
    for tb in re.finditer(r'<table\b[^>]*>(.*?)</table>', src[lo:hi], re.S):
        cards = []
        for row in re.finditer(r'<tr\b[^>]*>(.*?)</tr>', tb.group(1), re.S):
            if '<th' in row.group(1):
                continue
            tds = re.findall(r'<td\b[^>]*>(.*?)</td>', row.group(1), re.S)
            assert len(tds) == 2, 'glossary row with %d cells at %s' % (len(tds), path)
            t = re.match(r'\s*<(strong|b)\b[^>]*>(.*?)</\1>\s*$', tds[0].strip(), re.S)
            term_txt = t.group(2) if t else tds[0].strip()
            tid = slug(term_txt, taken)
            cards.append((card(term_txt, _LEAD_DASH.sub('', tds[1].strip()), None, tid),
                          flat(term_txt), tid))
        assert cards, 'a glossary table with no data row at %s' % path
        out.append((lo + tb.start(), lo + tb.end(),
                    '\n'.join(c[0] for c in cards),
                    'table:%d' % len(cards), ' | '.join(c[1] for c in cards),
                    ' '.join(c[2] for c in cards)))

    out.sort(key=lambda r: r[0])
    return src, out


def apply_to(path, rows):
    """Write DESCENDING (rule 12) and read back. Atomic: tempfile then os.replace."""
    src = open(path, encoding='utf-8').read()
    for s, e, new, kind, term, tid in sorted(rows, key=lambda r: -r[0]):
        src = src[:s] + new + src[e:]
    tmp = path + '.tmp'
    with open(tmp, 'w', encoding='utf-8') as fh:
        fh.write(src)
    os.replace(tmp, path)
    back = open(path, encoding='utf-8').read()
    assert back == src, 'read-back mismatch on %s' % path
    return len(rows)


def main():
    args = sys.argv[1:]
    paths = sorted(p for p in args if p.endswith('.html')) or \
        sorted(glob.glob('lessons/Lesson_*.html'))
    do = '--apply' in args
    print('glossary_convert.py %s - one shape for every entry '
          '(BookComponentStandard §7.4).' % VERSION)
    kinds = collections.Counter()
    entries = 0
    ids = collections.Counter()
    # IDS ARE PAGE-SCOPED, so the collision test is PER PAGE. A book-wide tally would
    # report six false positives: `term-serial-monitor-gloss` is legitimately in L01 and
    # L02 today, and `term-dead-reckoning-gloss` lands in three lessons because S128 ruled
    # the per-lesson entry additive and topic-disambiguated. A cross-page repeat is not a
    # collision - a link that reaches it names the page (§24.6c: verify before acting).
    cross = collections.defaultdict(set)
    collisions = []
    for p in paths:
        src, rows = plan(p)
        if not rows:
            continue
        n = 0
        page = collections.Counter()
        for s, e, new, kind, term, tid in rows:
            kinds[kind.split(':')[0]] += 1
            n += int(kind.split(':')[1]) if ':' in kind else 1
            for one in tid.split():
                ids[one] += 1
                page[one] += 1
                cross[one].add(os.path.basename(p))
        for k, v in page.items():
            if v > 1:
                collisions.append('%s carries %s %d times' % (os.path.basename(p), k, v))
        entries += n
        if '--verbose' in args:
            for s, e, new, kind, term, tid in rows:
                print('   %-10s %s' % (kind, term[:88]))
        print('  %-22s %3d entr%s from %d block(s)'
              % (os.path.basename(p), n, 'y' if n == 1 else 'ies', len(rows)))
        if do:
            apply_to(p, rows)
    print('\n  entries: %d   source blocks by schema: %s' % (entries, dict(kinds)))
    print('  distinct term ids: %d   ids reused across pages (legal): %d'
          % (len(ids), sum(1 for v in cross.values() if len(v) > 1)))
    if collisions:
        print('  IN-PAGE ID COLLISION - a page may not carry an id twice:')
        for c in collisions:
            print('     %s' % c)
        return 1
    print('  APPLIED' if do else '  DRY RUN - nothing written')
    return 0


if __name__ == '__main__':
    sys.exit(main())
