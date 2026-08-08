#!/usr/bin/env python3
"""keyterm_prefix.py v1.0.1 - the body KEY TERM callout names its own family.

DJ ruling, S134, option A: a KEY TERM callout sitting in the LESSON BODY opens
its head with the literal `KEY TERM: ` and then the term; a KEY TERM entry sitting
in the GLOSSARY region does not, because the section banner already says Glossary.

The rule exists because KEY TERM was the only large family in the book that did not
name itself. Measured across all 1,119 live callouts: NOTE 113/133, CHECKPOINT
102/112, TIP 79/85, DO THIS NOW 55/58, WARNING 67/80, LEARN 38/47, and BRAIN CHECK
/ THE GOAL / MY PLAN / BUILDS ON at 100%. KEY TERM sat at 13 of 238, and those 13
were exactly the blocks a normalisation pass was about to strip.

SHAPE. One shape for every body block:

    <div STYLE><img data-mark="key">KEY TERM: <strong ID?>Term</strong></div>Definition

THE PREFIX IS OUTSIDE THE <strong>, AND THAT IS LOAD-BEARING, NOT COSMETIC.
19 body head anchors sit on that <strong> - 18 spelled id="term-*" and one, L03 3.44,
spelled id="glossary-trim" - and those ids are the targets
of the ruled body->glossary link direction that gate §27.14 enforces. Wrapping the
prefix would also put it inside the string the end-of-book glossary harvest extracts
as the term. Renders identically either way, because the head div is already bold.

SCOPE IS THE REGION, NOT THE FAMILY (§24.14b). `lesson_inventory` v1.3.5 reports
`region`; a block whose region is `glossary` is never touched by this tool.

HELD BY NAME (§25.2a), NOT BY A COUNT. Four body blocks carry the KEY TERM family
and are not term cards - a question, an operator announcement, a formula and a
procedural list. DJ held constrain (3.31) explicitly at S134 and the other three are
the same shape. Prefixing them would label them as something they are not. They are
listed here so a future session finds a NAME rather than a silent gap, and so the
gate can except exactly them and nothing else.

NOT IN SCOPE: the head text colour. 16 body heads carry `color: #6a1b9a` in a clean
lesson strata (L04 5/5, L09 6/6, L10 5/5, and 0 of 59 elsewhere). That is a paint
question DJ parked at S133 alongside the five KEY TERM grounds. This tool does not
touch paint, and a repaint does not spend this tool.
"""

import os
import re
import sys
import glob
import html as H

import lesson_inventory as LI

VERSION = "v1.0.1"

PREFIX = "KEY TERM: "

# §25.2a - the exceptions are NAMED. Four blocks whose head is not a term.
HELD = {
    "3.31":   "a provenance question - 'Where Does constrain() Come From?'",
    "3.101":  "an operator announcement - 'New operator: % (modulo)'",
    "6.24":   "a formula box - 'The Formula'",
    "14.28":  "a procedural list - 'When to Call LoP'",
}

# THE LOCATOR IS THE AUTHORED ATTRIBUTE, NEVER A CLASS NAME (S133 rule 25).
# The first draft matched the head by its style declarations, which only exist in the
# EXPANDED source - the file carries `class="div-fs-105em"`. Keying on that class
# instead would have been worse than a bug: `-N` suffixes are assigned by usage RANK,
# so the name this tool depended on could be handed to a different rule by an
# unrelated edit and the tool would go silently blind. `data-mark` is authored.
_MARK_RE = re.compile(r'<img\b[^>]*\bdata-mark="key"[^>]*>')
_TAG_RE = re.compile(r'</?([a-zA-Z][a-zA-Z0-9]*)\b[^>]*?(/?)>')

_STRONG = re.compile(r'<strong\b[^>]*>.*?</strong>', re.S)
_LEAD = re.compile(r'(?i)^\s*key\s*term\s*[:\u2014\u2013-]*\s*')
_TRAILCOLON = re.compile(r'\s*:\s*$')


class Head(object):
    """The element wrapping the key mark: its open tag, the mark, interior, close."""

    def __init__(self, block, a, b, open_end, close_start, tag):
        self.tag = tag
        self._a, self._b = a, b
        self.open = block[a:open_end]
        mm = _MARK_RE.search(block, open_end, close_start)
        self.mark = mm.group(0)
        self.interior = block[mm.end():close_start]
        self.close = block[close_start:b]
        self.whole = block[a:b]

    def start(self):
        return self._a

    def end(self):
        return self._b


def head_of(block):
    """Return (kind, Head) by walking OUT from the mark, or (None, None).

    Structural, not textual: find the mark, take the tag that opens immediately
    before it, then depth-walk forward to that tag's own close. This reads the
    same for a <div> head and for L15's inline <b>, and it does not care what
    the head is painted with or what class stands for that paint.
    """
    mm = _MARK_RE.search(block)
    if mm is None:
        return None, None
    # nearest opening tag before the mark, with only whitespace between
    opens = [m for m in _TAG_RE.finditer(block, 0, mm.start())
             if not m.group(0).startswith('</') and not m.group(2)]
    if not opens:
        return None, None
    o = opens[-1]
    if block[o.end():mm.start()].strip():
        return None, None
    tag = o.group(1).lower()
    depth = 1
    close_start = None
    for m in _TAG_RE.finditer(block, mm.end()):
        if m.group(1).lower() != tag:
            continue
        if m.group(0).startswith('</'):
            depth -= 1
            if depth == 0:
                close_start = m.start()
                end = m.end()
                break
        elif not m.group(2):
            depth += 1
    if close_start is None:
        return None, None
    kind = "div" if tag == "div" else "b"
    return kind, Head(block, o.start(), end, o.end(), close_start, tag)


def term_of(interior):
    """The term, and whether it already sits in a <strong>."""
    s = _STRONG.search(interior)
    if s:
        return s.group(0), True
    txt = interior.strip()
    return txt, False


def rebuild(interior):
    """Head interior -> canonical interior. Idempotent by construction."""
    body, in_strong = term_of(interior)
    if in_strong:
        # prefix (if any) is the text before the <strong>; drop and re-emit
        return PREFIX + body
    txt = H.unescape(body) if False else body
    txt = _LEAD.sub('', txt)            # strip 'Key Term:' / 'KEY TERM —' in any case
    txt = _TRAILCOLON.sub('', txt)      # L15 writes 'Term:'
    txt = txt.strip()
    return PREFIX + '<strong>' + txt + '</strong>'


def plan(path):
    """Return a list of (a, b, old, new, cid, kind) FILE offsets for one lesson."""
    src = open(path, encoding='utf-8').read()
    expanded, to_file = LI.expand_classes_mapped(src)
    tree = LI.build(path)
    jobs = []
    for c in tree['callouts']:
        if c['family_attr'] != 'KEY TERM':
            continue
        if c['region'] == 'glossary':
            continue
        cid = c['callout_id']
        if cid in HELD:
            continue
        fs = to_file(int(c['exp_start']))
        raw = src[fs:fs + int(c['bytes']) * 3]
        kind, h = head_of(raw)
        if kind is None:
            raise SystemExit("no head found for %s in %s" % (cid, path))
        new_interior = rebuild(h.interior)
        if kind == "div":
            old = h.whole
            newtxt = h.open + h.mark + new_interior + h.close
        else:
            # AN INLINE HEAD BECOMING ITS OWN LINE TAKES THE PROSE WITH IT.
            # These three read `<b>KEY TERM - Term:</b> a control algorithm that...`,
            # so the definition is lowercase because it was grammatically continuing
            # the head's own sentence. Lift the head onto its own line and that
            # lowercase letter is a defect the reader sees. Every other body block's
            # definition opens with a capital. The span therefore extends past the
            # head to consume the first letter of the definition, and asserts it.
            tail = h.end()
            j = tail
            while j < len(raw) and raw[j].isspace():
                j += 1
            assert j < len(raw) and raw[j].isalpha(), "no definition letter after %s" % cid
            assert raw[j].islower(), "%s definition already capitalised" % cid
            old = raw[h.start():j + 1]
            newtxt = ('<div style="font-weight: bold; margin-bottom: 8px; '
                      'font-size: 1.05em;">' + h.mark + new_interior + '</div>'
                      + raw[tail:j] + raw[j].upper())
        if old == newtxt:
            continue
        a = fs + h.start()
        b = a + len(old)
        assert src[a:b] == old, "offset mismatch on %s" % cid
        jobs.append((a, b, old, newtxt, cid, kind))
    return src, jobs


def apply(path, write=False):
    src, jobs = plan(path)
    if not jobs:
        return 0, src
    out = src
    # §6.12c - DESCENDING, so an edit never invalidates a target below it
    for a, b, old, new, cid, kind in sorted(jobs, key=lambda j: -j[0]):
        assert out[a:b] == old, "target moved for %s" % cid
        out = out[:a] + new + out[b:]
    if write:
        blob = out.encode('utf-8')          # encode FIRST (§12), then replace
        tmp = path + '.tmp'
        with open(tmp, 'wb') as f:
            f.write(blob)
        os.replace(tmp, path)
    return len(jobs), out


def audit():
    """Report, never write. Exit code is meaningless here by design (§24.6a)."""
    tot = held = ok = todo = gloss = 0
    for path in sorted(glob.glob('lessons/Lesson_*.html')):
        src = open(path, encoding='utf-8').read()
        expanded, to_file = LI.expand_classes_mapped(src)
        tree = LI.build(path)
        for c in tree['callouts']:
            if c['family_attr'] != 'KEY TERM':
                continue
            tot += 1
            if c['region'] == 'glossary':
                gloss += 1
                continue
            if c['callout_id'] in HELD:
                held += 1
                continue
            fs = to_file(int(c['exp_start']))
            raw = src[fs:fs + int(c['bytes']) * 3]
            kind, h = head_of(raw)
            if (kind == "div" and h.interior.startswith(PREFIX)
                    and _STRONG.search(h.interior)):
                ok += 1
            else:
                todo += 1
    print("keyterm_prefix.py %s - the body block names its family; the glossary does not." % VERSION)
    print("  %d KEY TERM callouts" % tot)
    print("    %4d glossary   (out of scope, §24.14b region tier)" % gloss)
    print("    %4d held       (%s)" % (held, ', '.join(sorted(HELD))))
    print("    %4d canonical" % ok)
    print("    %4d to convert" % todo)
    assert gloss + held + ok + todo == tot, "population does not reconcile"
    return todo


def main():
    args = sys.argv[1:]
    if '--audit' in args or not args:
        audit()
        return
    write = '--apply' in args
    total = 0
    for path in sorted(glob.glob('lessons/Lesson_*.html')):
        n, _ = apply(path, write=write)
        if n:
            print("  %s  %d block(s)%s" % (os.path.basename(path), n,
                                           "" if write else "  (dry run)"))
            total += n
    print("%d block(s) %s" % (total, "written" if write else "would change"))


if __name__ == '__main__':
    main()
