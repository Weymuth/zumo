#!/usr/bin/env python3
"""
S64 pill sweep — structural converter.  v1.0

Matches an old-style difficulty pill by STRUCTURE (a <span> whose style contains
the old inline-block signature, whose text is a known tier label, sitting inside a
challenge block) rather than by an exact style string. L04-L16 carry 9 distinct
style strings for the same visual pill -- CSS property ORDER drifted between
lessons -- so an exact-match replace silently matches nothing on most lessons.

Usage:  python3 pill_sweep.py <lesson_html> <ratings_file>
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
    print(f"{'file':28s} {'old':>4s} {'new':>4s} {'diff':>5s} {'grasp':>6s}  status")
    for p in paths:
        s = open(p).read()
        blocks = challenge_blocks(s)
        old = len([m for m in OLD_PILL.finditer(s) if m.group(1).upper() in TIERS])
        new = s.count('width: 4px')
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
        print(f"{p.split('/')[-1]:28s} {old:4d} {new:4d} {nd:5d} {ng:6d}  {st}")
    print(f"\ndistinct old-pill style strings still live: {len(strata)}")
    for i, (k, v) in enumerate(strata.most_common(), 1):
        print(f"  [{i}] x{v:3d}  {k[13:110]}")


if __name__ == '__main__':
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
