#!/usr/bin/env python3
"""
S64 pill sweep — structural converter.  v1.1

Matches an old-style difficulty pill by STRUCTURE (a <span> whose style contains
the old inline-block signature, whose text is a known tier label, sitting inside a
challenge block) rather than by an exact style string. L04-L16 carry 9 distinct
style strings for the same visual pill -- CSS property ORDER drifted between
lessons -- so an exact-match replace silently matches nothing on most lessons.

S110: the audit's "swept" detector counted the inline string `width: 4px`, which the
S103 class migration deleted from every lesson. It therefore reported *** MIXED *** on
15 of 16 lessons - an alarm that fires on everything says nothing, and it had been
printing in the session-open ritual unread. The detector is now migration-aware: it
counts the INLINE signature or the CLASS signature, and names which form it found, so
the next migration is visible instead of silent.

Usage:  python3 pill_sweep.py <lesson_html> <ratings_file>
        python3 pill_sweep.py --audit lessons/Lesson_*.html
        python3 pill_sweep.py --selftest
ratings_file: one line per challenge -> "<cid> <doing> <grasp>"
Dry-run by default; pass --write to save.
"""
import re, sys

DOING = {
    'easy':     ('#4A6B22', 'Easy'),
    'medium':   ('#9A6B10', 'Medium'),
    'tough':    ('#B85425', 'Tough'),
    'hard':     ('#8A2F18', 'Hard'),
    'advanced': ('#6B2545', 'Advanced'),
}
GRASP = {
    'light':    ('#4A7FB5', 'Light'),
    'moderate': ('#185FA5', 'Moderate'),
    'deep':     ('#0C3F6C', 'Deep'),
}
TIERS = {'EASY', 'MEDIUM', 'TOUGH', 'HARD', 'ADVANCED'}

# The canonical split pill (Bible 6.12b, slash halved S63: width 4px / margin -2px).
def split_pill(d, g):
    dc, dl = DOING[d]
    gc, gl = GRASP[g]
    return (
        '<span style="display: inline-flex; align-items: stretch; margin-left: 10px; '
        'font-size: 0.8em; border-radius: 999px; overflow: hidden; vertical-align: middle;">'
        f'<span style="background: {dc}; color: #ffffff; padding: 3px 13px 3px 11px;">{dl}</span>'
        '<span style="width: 4px; background: #ffffff; transform: skewX(-20deg); '
        'margin: 0 -2px; position: relative; z-index: 2;"></span>'
        f'<span style="background: {gc}; color: #ffffff; padding: 3px 11px 3px 13px;">{gl}</span>'
        '</span>')

OLD_PILL = re.compile(
    r'<span style="display: inline-block;[^"]*border-radius: 12px;[^"]*"[^>]*>\s*([A-Za-z]+)\s*</span>')


INLINE_SIG = 'width: 4px'                 # pre-S103: the skewed spacer, inline
CLASS_SIG = 'span-ai-stretch'             # post-S103: the split-pill wrapper class


def class_token(s, tok):
    """Whole-token class match. A substring match would count `span-ai-stretch-2`
    as `span-ai-stretch`; `-` is not a word character, so \b does NOT do this."""
    return len(re.findall(r'class="[^"]*(?<![-\w])' + re.escape(tok) + r'(?![-\w])', s))


def swept_pills(s):
    """-> (count, form). Counts the split pill in whichever form the corpus carries."""
    inline = s.count(INLINE_SIG)
    classed = class_token(s, CLASS_SIG)
    if inline and classed:
        return inline + classed, 'both'
    if classed:
        return classed, 'class'
    return inline, ('inline' if inline else 'none')


def challenge_blocks(s):
    """Yield (cid, start, end) for each challenge div, in document order."""
    starts = [(int(m.group(1)), m.start())
              for m in re.finditer(r'<div id="challenge-(\d+)"', s)]
    out = []
    for i, (cid, st) in enumerate(starts):
        en = starts[i + 1][1] if i + 1 < len(starts) else len(s)
        out.append((cid, st, en))
    return out


def convert(path, ratings, write=False):
    s = open(path).read()
    orig = s
    blocks = challenge_blocks(s)
    assert blocks, "no challenge blocks found"

    got = {c for c, _, _ in blocks}
    want = set(ratings)
    assert got == want, f"challenge id mismatch: file has {sorted(got)}, ratings has {sorted(want)}"

    # Work back-to-front so earlier offsets stay valid.
    for cid, st, en in reversed(blocks):
        d, g = ratings[cid]
        assert d in DOING, f"C{cid}: bad doing tier {d!r}"
        assert g in GRASP, f"C{cid}: bad grasp tier {g!r}"
        block = s[st:en]

        # --- the visible pill -------------------------------------------------
        hits = [m for m in OLD_PILL.finditer(block) if m.group(1).upper() in TIERS]
        assert len(hits) == 1, f"C{cid}: expected 1 old pill in block, found {len(hits)}"
        m = hits[0]
        old_label = m.group(1).upper()
        block = block[:m.start()] + split_pill(d, g) + block[m.end():]

        # --- the machine attribute -------------------------------------------
        dm = re.search(r'(<div id="challenge-%d"[^>]*?data-difficulty=")([a-z]+)(")' % cid, block)
        assert dm, f"C{cid}: data-difficulty attribute not found"
        file_tier = dm.group(2)
        assert 'data-grasp=' not in block[:dm.end() + 200], f"C{cid}: already has data-grasp"
        block = block[:dm.end()] + f' data-grasp="{g}"' + block[dm.end():]

        # If the doing axis is being RE-RATED, the attribute must be rewritten too.
        if file_tier != d:
            block = re.sub(r'(<div id="challenge-%d"[^>]*?data-difficulty=")[a-z]+(")' % cid,
                           lambda mm: mm.group(1) + d + mm.group(2), block, count=1)
            note = f"  (RE-RATE {file_tier} -> {d}; label was {old_label})"
        else:
            note = ""

        s = s[:st] + block + s[en:]
        print(f"  C{cid}: {DOING[d][1]}/{GRASP[g][1]}{note}")

    # --- whole-file verification ---------------------------------------------
    n_old = len([m for m in OLD_PILL.finditer(s) if m.group(1).upper() in TIERS])
    assert n_old == 0, f"{n_old} old pills remain"
    n_split = s.count('width: 4px')
    n_grasp = len(re.findall(r'data-grasp=', s))
    n_diff = len(re.findall(r'data-difficulty=', s))
    assert n_split == len(blocks), f"split pill count {n_split} != {len(blocks)}"
    assert n_grasp == len(blocks), f"data-grasp count {n_grasp} != {len(blocks)}"
    assert n_diff == len(blocks), f"data-difficulty count {n_diff} != {len(blocks)}"

    for tag in ('div', 'pre', 'span'):
        o = len(re.findall(r'<%s\b' % tag, s))
        c = len(re.findall(r'</%s>' % tag, s))
        assert o == c, f"{tag} unbalanced: {o}/{c}"

    # stack depth walk (open==close does not prove nesting -- Bible 11)
    st_stack, mx, bad = [], 0, 0
    for close, tag in re.findall(r'<(/?)(div|pre)\b[^>]*>', s):
        if not close:
            st_stack.append(tag); mx = max(mx, len(st_stack))
        else:
            if not st_stack or st_stack[-1] != tag: bad += 1
            else: st_stack.pop()
    assert bad == 0 and not st_stack, f"nesting broken: residual={len(st_stack)} mismatched={bad}"

    print(f"  [verify] {len(blocks)} pills · balance OK · depth residual 0 · maxdepth {mx}")
    print(f"  [bytes]  {len(orig)} -> {len(s)}  (+{len(s)-len(orig)})")

    if write:
        open(path, 'w').write(s)
        print("  [WRITTEN]")
    else:
        print("  [dry run -- not written]")
    return s


def audit(paths):
    """Report pill inventory + style-string strata across lessons. Read-only."""
    from collections import Counter
    strata = Counter()
    forms = set()
    print(f"{'file':28s} {'old':>4s} {'new':>4s} {'diff':>5s} {'grasp':>6s} {'form':>7s}  status")
    for p in paths:
        s = open(p).read()
        blocks = challenge_blocks(s)
        old = len([m for m in OLD_PILL.finditer(s) if m.group(1).upper() in TIERS])
        new, form = swept_pills(s)
        nd = len(re.findall(r'data-difficulty=', s))
        ng = len(re.findall(r'data-grasp=', s))
        for m in OLD_PILL.finditer(s):
            if m.group(1).upper() in TIERS:
                strata[m.group(0)[:m.group(0).find('"', 13)]] += 1
        if old == 0 and new == len(blocks) and ng == nd == len(blocks) and blocks:
            st = "SWEPT"
        elif not blocks:
            st = "no challenges"
        elif old == len(blocks) and ng == 0:
            st = "not swept"
        else:
            st = "*** MIXED ***"
        forms.add(form if blocks else '-')
        print(f"{p.split('/')[-1]:28s} {old:4d} {new:4d} {nd:5d} {ng:6d} {form:>7s}  {st}")
    live = {f for f in forms if f != '-'}
    mixed_form = len(live) > 1 or 'both' in live
    print(f"\npill form in use: {', '.join(sorted(live)) or 'none'}"
          + ("   <-- MIGRATION IN PROGRESS, two forms live" if mixed_form else ""))
    print(f"distinct old-pill style strings still live: {len(strata)}")
    for i, (k, v) in enumerate(strata.most_common(), 1):
        print(f"  [{i}] x{v:3d}  {k[13:110]}")


def selftest():
    """Controls, not re-reads. The failure mode of the S110 detector fix is an alarm
    that never fires instead of one that always fires, so MIXED is planted and must
    still be reachable."""
    import glob, tempfile, os, io, contextlib
    ok = True

    def rep(label, passed, detail=''):
        nonlocal ok
        ok = ok and passed
        print('   %-5s %s%s' % ('OK' if passed else 'FAIL', label, ('  ' + detail) if detail else ''))

    def run_audit(paths):
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            audit(paths)
        return buf.getvalue()

    def synth(n_old, n_new, form='class'):
        """A minimal file with n_old unswept and n_new swept challenges."""
        out = []
        for i in range(1, n_old + n_new + 1):
            swept = i > n_old
            pill = (('<span class="span-ai-stretch"><span></span></span>' if form == 'class'
                     else '<span style="width: 4px;"></span>') if swept else
                    '<span style="display: inline-block; padding: 2px; border-radius: 12px;">Easy</span>')
            out.append('<div id="challenge-%d" data-difficulty="easy"%s>%s</div>'
                       % (i, ' data-grasp="light"' if swept else '', pill))
        return '\n'.join(out)

    def write(text):
        f = tempfile.NamedTemporaryFile('w', suffix='.html', delete=False)
        f.write(text); f.close(); return f.name

    print('CONTROL A (the fix changed something): the OLD detector must call the live')
    print('  corpus MIXED and the NEW one must not - otherwise nothing was fixed')
    live = sorted(glob.glob('lessons/Lesson_*.html'))
    if not live:
        rep('corpus present', False, 'no lessons/ found - run from the repo root'); return 1
    old_style = sum(1 for p in live if open(p).read().count(INLINE_SIG) == 0
                    and len(challenge_blocks(open(p).read())) > 0)
    new_out = run_audit(live)
    rep('old detector would flag 15, new detector flags 0',
        old_style == 15 and '*** MIXED ***' not in new_out,
        'stale-signature lessons %d, MIXED lines now %d' % (old_style, new_out.count('MIXED')))

    print('CONTROL B (MIXED is still REACHABLE): a genuinely half-swept file must trip it')
    t = write(synth(2, 2)); out = run_audit([t]); os.unlink(t)
    rep('half-swept file reports MIXED', '*** MIXED ***' in out)

    print('CONTROL C (not-swept is still reachable): an all-old file must say so')
    t = write(synth(3, 0)); out = run_audit([t]); os.unlink(t)
    rep('all-old file reports not swept', 'not swept' in out)

    print('CONTROL D (both forms detected): inline and class signatures both count')
    t1 = write(synth(0, 3, 'class')); t2 = write(synth(0, 3, 'inline'))
    o1, o2 = run_audit([t1]), run_audit([t2]); os.unlink(t1); os.unlink(t2)
    rep('class form swept', 'SWEPT' in o1 and 'class' in o1)
    rep('inline form swept', 'SWEPT' in o2 and 'inline' in o2)

    print('CONTROL E (a migration in progress is VISIBLE, not silent)')
    t = write(synth(0, 2, 'class') + '\n' + synth(0, 2, 'inline').replace('challenge-1', 'challenge-3').replace('challenge-2', 'challenge-4'))
    out = run_audit([t]); os.unlink(t)
    rep('two live forms are announced', 'MIGRATION IN PROGRESS' in out)

    print('CONTROL F (whole-token class matching): the counter must not match a longer name')
    rep('span-ai-stretch-2 is not span-ai-stretch',
        class_token('<i class="span-ai-stretch-2">', CLASS_SIG) == 0
        and class_token('<i class="span-ai-stretch">', CLASS_SIG) == 1)

    print('CONTROL G (split_pill is well formed): every tier pair balances its spans')
    bad = [(d, g) for d in DOING for g in GRASP
           if split_pill(d, g).count('<span') != split_pill(d, g).count('</span>')]
    rep('all %d tier pairs balanced' % (len(DOING) * len(GRASP)), not bad, str(bad[:3]))

    print('CONTROL H (challenge_blocks spans the file): blocks are contiguous and ordered')
    s3 = open(live[2]).read(); b = challenge_blocks(s3)
    contig = all(b[i][2] == b[i + 1][1] for i in range(len(b) - 1)) and b[-1][2] == len(s3)
    rep('blocks contiguous, ids ascending',
        contig and [c for c, _, _ in b] == sorted(c for c, _, _ in b), '%d blocks' % len(b))

    print('\n%s' % ('ALL CONTROLS PASS - MIXED and "not swept" both still reachable.'
                     if ok else 'CONTROLS FAILED'))
    return 0 if ok else 1


if __name__ == '__main__':
    if '--selftest' in sys.argv:
        sys.exit(selftest())
    if '--audit' in sys.argv:
        audit([a for a in sys.argv[1:] if not a.startswith('--')])
        sys.exit(0)
    path = sys.argv[1]
    ratings = {}
    for line in open(sys.argv[2]):
        line = line.split('#')[0].strip()
        if not line:
            continue
        cid, d, g = line.split()
        ratings[int(cid)] = (d, g)
    convert(path, ratings, write='--write' in sys.argv)
