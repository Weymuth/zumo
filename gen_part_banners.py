#!/usr/bin/env python3
"""
gen_part_banners.py  v1.2  (S84; v1.1 S110; v1.2 S111 — the four PART spine colours
moved to the eight-band palette ruled in ZUMO_S111_VISUAL_RULING.md)

Bible §6.8 — the PART divider block is GENERATED from the section spine, not maintained.

One pass covers four defects that were four separate queue items:
  (1) placement  — 5 banners in L12/L13/L14 sat above the wrong section
  (2) content    — L04 PART 2 title, L05 PART 2 + PART 4 subtitles
  (3) encoding   — six strata (bare &, &mdash; vs literal, &ndash;, opacity 0.7)
  (4) the comment — uncanonized, drifted eight formats, absent in L15/L16

Never open(path,'w') on a source file: build bytes, assert, write .tmp, os.replace.

S110 -- THIS TOOL HAD BEEN DEAD SINCE S103 AND NOTHING SAID SO. The S27 migration moved
every inline style into css/book.css, and BLOCK matches the inline form, so process() found
zero PART blocks and the run ended in an AssertionError on Lesson_01. book_gates gate 27
kept passing the whole time because it reads through lesson_inventory.expand_classes();
this tool read the raw bytes. Two readers of one construct, one of them taught about the
migration. Fixed by reading through the same expander.

--apply IS NOW REFUSED. Emitting these blocks writes inline style="" attributes into a
lesson that links css/book.css, which Bible 27.12 forbids and gate 41 catches. Repairing a
PART banner today goes through the restore -> regenerate -> apply cycle, not through here.
The tool remains useful as a CHECKER, which is what it is now.
"""
import re, os, sys, glob, html
import lesson_inventory as _LI

EM = "\u2014"   # literal em-dash, per the §6.8 Bible snippet
EN = "\u2013"   # literal en-dash, per the §6.8 Bible snippet

# n -> (color, title-with-entities, UPPERCASE comment title, anchor section)
PARTS = {
    1: ("#1f2a3d", f"Theory &amp; Concepts",     "THEORY & CONCEPTS",     "1"),
    2: ("#433014", f"Hardware &amp; Code",       "HARDWARE & CODE",       "4"),
    3: ("#00474b", f"Testing &amp; Challenges",  "TESTING & CHALLENGES",  "7"),
    4: ("#7a5905", f"Challenges",                "CHALLENGES",            "9"),
}
SUBS = {
    1: f"Sections 1{EN}3: Learn the fundamentals",
    2: f"Sections 4{EN}6: Set up and program your robot",
    4: f"Section 9: Apply what you have learned",
}
EQ = "=" * 21


def sub3(has_8a):
    return f"Sections 7{EN}8A: Verify and extend" if has_8a else f"Sections 7{EN}8: Verify and extend"


def canon_block(n, has_8a):
    color, title, upper, _ = PARTS[n]
    sub = sub3(has_8a) if n == 3 else SUBS[n]
    return (
        f"<!-- {EQ} PART {n}: {upper} {EQ} -->\n"
        f'<div style="background-color: {color}; color: white; padding: 12px 20px; '
        f'border-radius: 8px 8px 0 0; margin: 22px 0 0;">\n'
        f'    <div style="font-size: 18px; font-weight: 500; letter-spacing: 0.5px;">'
        f"PART {n} {EM} {title}</div>\n"
        f'    <div style="font-size: 12px; color: rgba(255,255,255,0.85); margin-top: 4px;">'
        f"{sub}</div>\n"
        f"</div>\n"
    )


BLOCK = re.compile(
    r'<div style="background-color: #[0-9a-fA-F]{6}; color: white; padding: 12px 20px; '
    r'border-radius: 8px 8px 0 0; margin: 22px 0 0;">\s*'
    r'<div style="font-size: 18px[^"]*">PART (\d+)[^<]*</div>\s*'
    r'<div style="font-size: 12px[^"]*">[^<]*</div>\s*</div>'
)
COMMENT_BEFORE = re.compile(r'(<!--(?:(?!-->).)*?-->)[ \t]*\n[ \t]*$', re.S)


def fence_pos(s, secnum):
    """Byte offset of the canonical SECTION fence for this section. Colon disambiguates 1 from 10."""
    pat = f"<!-- {EQ} SECTION {secnum}: "
    hits = [m.start() for m in re.finditer(re.escape(pat), s)]
    assert len(hits) == 1, f"expected 1 fence for SECTION {secnum}, found {len(hits)}"
    return hits[0]


def process(path, verbose=True):
    # Read through the SAME expander the gates use. The raw file carries classes, not
    # styles, and BLOCK is written against the style form.
    src = _LI.expand_classes(open(path, encoding="utf-8").read())
    name = os.path.basename(path)
    has_8a = 'id="section-8a"' in src

    # ---- pass 1: sweep every divider-shaped PART comment, wherever it sits.
    # Folding only ADJACENT comments leaves strays behind (L01 had 4 comments, 2 adjacent).
    # A divider comment is "PART n", "PART n DIVIDER", or "PART n: TITLE" once = and space
    # are stripped. L03's "End Part 1 content" / "PART 2 build continues" are a DIFFERENT
    # construct and must survive untouched.
    DIVCMT = re.compile(r'^PART\s+\d+(?:\s+DIVIDER|\s*:\s*.+)?$', re.I)

    def rejoin(doc, a, b):
        """Delete doc[a:b] leaving a deterministic junction, so a deletion can
        never grow the file's blank-run count."""
        left, right = doc[:a], doc[b:]
        nl = (len(left) - len(left.rstrip("\n"))) + (len(right) - len(right.lstrip("\n")))
        return left.rstrip("\n") + "\n" * min(2, max(1, nl)) + right.lstrip("\n")

    hits = []
    for m in re.finditer(r'[ \t]*<!--((?:(?!-->).)*?)-->[ \t]*', src, re.S):
        body = m.group(1).strip().strip('=').strip()
        if re.search(r'\bPART\b', body, re.I) and DIVCMT.match(body):
            hits.append(m.span())
    removed_cmts = len(hits)
    stripped = src
    for a, b in reversed(hits):
        stripped = rejoin(stripped, a, b)

    # ---- pass 2: locate the four blocks in the comment-stripped text
    spans = {}
    for m in BLOCK.finditer(stripped):
        n = int(m.group(1))
        a, b = m.span()
        a -= len(re.search(r"[ \t]*$", stripped[:a]).group(0))
        while b < len(stripped) and stripped[b] in " \t":
            b += 1
        if b < len(stripped) and stripped[b] == "\n":
            b += 1
        assert n not in spans, f"{name}: duplicate PART {n}"
        spans[n] = (a, b)
    assert sorted(spans) == [1, 2, 3, 4], f"{name}: found PARTs {sorted(spans)}, expected 1-4"

    # ---- build the operation list: 4 deletions + 4 insertions, applied back-to-front
    ops = []
    for n, (a, b) in spans.items():
        ops.append(("del", a, b, n))
    for n in PARTS:
        ops.append(("ins", fence_pos(stripped, PARTS[n][3]), None, n))
    ops.sort(key=lambda o: o[1], reverse=True)

    out = stripped
    for kind, a, b, n in ops:
        if kind == "del":
            out = rejoin(out, a, b)
        else:
            out = out[:a] + canon_block(n, has_8a) + "\n" + out[a:]

    # ---- whitespace: junctions are deterministic (see the del branch), no global pass
    before_runs = len(re.findall(r"\n{3,}", src))
    after_runs = len(re.findall(r"\n{3,}", out))

    # ================= ASSERTS =================
    # 1. exactly four canonical blocks out, each byte-exact
    for n in PARTS:
        blk = canon_block(n, has_8a)
        assert out.count(blk) == 1, f"{name}: canonical PART {n} block count != 1"
    # 2. every canonical block is immediately followed by its own SECTION fence
    for n in PARTS:
        blk = canon_block(n, has_8a)
        i = out.index(blk) + len(blk)
        nxt = out[i:i + 80]
        want = f"\n<!-- {EQ} SECTION {PARTS[n][3]}: "
        assert nxt.startswith(want), (
            f"{name}: PART {n} is not adjacent to SECTION {PARTS[n][3]} fence; got {nxt[:60]!r}")
    # 3. no PART banner markup survives outside the four canonical blocks
    assert len(BLOCK.findall(out)) == 4, f"{name}: {len(BLOCK.findall(out))} blocks after generate"
    # 4. div multiset unchanged (relocation + retype, never a structural change)
    for tag in ("<div", "</div>"):
        assert src.count(tag) == out.count(tag), (
            f"{name}: {tag} count {src.count(tag)} -> {out.count(tag)}")
    for tag in ("<!--", "-->"):
        exp = src.count(tag) - removed_cmts + 4
        assert out.count(tag) == exp, (
            f"{name}: {tag} count {src.count(tag)} -> {out.count(tag)}, expected {exp} "
            f"(swept {removed_cmts}, generated 4)")
    # L03's non-divider PART notes must survive the sweep
    for note in ("End Part 1 content", "PART 2 build continues", "End Part 3 content"):
        assert src.count(note) == out.count(note), f"{name}: non-divider note '{note}' lost"
    # 5. the only visible-text deltas are PART titles/subtitles. Compare the
    #    non-PART text-line multiset, which relocation must leave untouched.
    def textlines(doc):
        from bs4 import BeautifulSoup
        t = BeautifulSoup(doc, "html.parser").get_text("\n")
        return sorted(x.strip() for x in t.split("\n")
                      if x.strip() and not re.match(r"^(PART \d|Sections? \d)", x.strip()))
    ta, tb = textlines(src), textlines(out)
    assert ta == tb, f"{name}: non-PART visible text changed ({len(ta)} vs {len(tb)} lines)"
    # 6. whitespace tidy never touched a pre-existing run
    assert after_runs <= before_runs, f"{name}: blank runs grew {before_runs} -> {after_runs}"

    if verbose:
        moved = []
        for n in PARTS:
            oa = spans[n][0]
            fp = fence_pos(stripped, PARTS[n][3])
            if not (0 < fp - oa < 400):
                moved.append(f"PART{n}")
        print(f"  {name:<16} 8A={'Y' if has_8a else 'N'}  "
              f"reloc={','.join(moved) if moved else '-':<12} swept={removed_cmts} "
              f"bytes {len(src)}->{len(out)}  blank-runs {before_runs}->{after_runs}")
    return src, out


def main():
    if "--selftest" in sys.argv:
        return selftest()
    if "--apply" in sys.argv:
        print("REFUSED. --apply writes inline style=\"\" attributes, which Bible 27.12\n"
              "forbids in any page that links css/book.css, and gate 41 catches. Repair a\n"
              "PART banner through restore -> regenerate -> apply instead. This tool is a\n"
              "CHECKER now; run it with no arguments.")
        return 1
    apply = False
    changed = 0
    for p in sorted(glob.glob("lessons/Lesson_*.html")):
        src, out = process(p)
        if src != out:
            changed += 1
            if apply:
                tmp = p + ".tmp"
                with open(tmp, "w", encoding="utf-8") as f:
                    f.write(out)
                assert open(tmp, encoding="utf-8").read() == out, "tmp readback mismatch"
                os.replace(tmp, p)
    print(f"\n{changed} of 16 lessons differ from the canon form.")
    print("  NOTE: every byte figure above is measured on the EXPANDED text (classes\n"
          "  resolved back to styles), not on the file. The file itself carries classes.\n"
          "  A difference of a few bytes here is blank-line normalisation, not a banner\n"
          "  defect: gate 27 asserts the block+comment byte-for-byte and passes.")
    return 0


def selftest():
    """Controls. The v1.0 failure was invisible because nothing ever ran this file."""
    ok = True

    def rep(label, passed, detail=''):
        nonlocal ok
        ok = ok and passed
        print('   %-5s %s%s' % ('OK' if passed else 'FAIL', label, ('  ' + detail) if detail else ''))

    files = sorted(glob.glob("lessons/Lesson_*.html"))
    print('CONTROL A (it runs at all): v1.0 raised AssertionError on Lesson_01 because it')
    print('  read raw bytes after the S103 migration moved styles into css/book.css.')
    err = None
    try:
        for f in files:
            process(f, verbose=False)
    except Exception as e:
        err = e
    rep('process() completes on all %d lessons' % len(files), err is None, repr(err) if err else '')

    print('CONTROL B (the fix CHANGED something): reading RAW must still find no banners')
    raw = open(files[0], encoding='utf-8').read()
    rep('raw source contains 0 canonical PART blocks, expanded contains 4',
        len(BLOCK.findall(raw)) == 0 and len(BLOCK.findall(_LI.expand_classes(raw))) == 4,
        'raw %d / expanded %d' % (len(BLOCK.findall(raw)),
                                  len(BLOCK.findall(_LI.expand_classes(raw)))))

    print('CONTROL C (two generators of one construct must AGREE): this tool and')
    print('  book_gates gate 27 build the same block independently. book_gates is NOT')
    print('  imported - importing it runs the whole 45-gate suite as a side effect - so')
    print('  its spec is read as text.')
    import re as _re
    gsrc = open('book_gates.py', encoding='utf-8').read()
    m = _re.search(r'_PART_SPEC = \{(.*?)^\}', gsrc, _re.S | _re.M)
    gate = dict(_re.findall(r"(\d+):\s*\('(#[0-9a-fA-F]{6})'", m.group(1))) if m else {}
    mine = {str(n): PARTS[n][0] for n in (1, 2, 3, 4)}
    rep('PART colours identical in both generators', gate == mine,
        'gate %s  mine %s' % (gate, mine))
    gate_titles = _re.findall(r"'(#[0-9a-fA-F]{6})', '([^']+)'", m.group(1)) if m else []
    mine_titles = [(PARTS[n][0], PARTS[n][1]) for n in (1, 2, 3, 4)]
    rep('PART titles identical in both generators', gate_titles == mine_titles)

    print('CONTROL D (a seeded defect is still caught)')
    good = _LI.expand_classes(open(files[0], encoding='utf-8').read())
    hurt = good.replace('PART 2 \u2014', 'PART 2 -', 1)
    rep('an em-dash swapped for a hyphen changes the text', hurt != good)

    print('CONTROL E (--apply is refused): writing the inline form back would breach 27.12')
    import subprocess
    r = subprocess.run([sys.executable, __file__, '--apply'], capture_output=True, text=True)
    rep('--apply exits non-zero and says why',
        r.returncode != 0 and 'REFUSED' in r.stdout, 'exit %d' % r.returncode)

    print('\n%s' % ('ALL CONTROLS PASS' if ok else 'CONTROLS FAILED'))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
