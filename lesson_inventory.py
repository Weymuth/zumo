#!/usr/bin/env python3
# lesson_inventory.py — exhaustive structural ENUMERATION of the lesson files.
# VERSION below is the ONE home: it sits ABOVE the changelog so a plain grep of this
# file lands on the live version, not on a changelog line (S98).
VERSION = 'v1.1.2'
#
# v1.1.1 (S94): the visible-banner expectation was still the pre-S89 value of 2, so --anomalies
#   printed a false lead for all sixteen lessons. §5b and book_gates have required exactly ONE
#   visible banner since the build banner was deleted at S89. Corrected 2 -> 1. A uniform anomaly
#   across every file is a lead about the INSTRUMENT, not the book (§24.8) — and sixteen false
#   leads bought cover for the two real ones beside them (§24.11).
#
# Usage:
#   python3 lesson_inventory.py                     summary table, all 16 lessons
#   python3 lesson_inventory.py 09                  full detail dump for one lesson
#   python3 lesson_inventory.py 09 --headings       one view only
#   python3 lesson_inventory.py --reveals           one view, all lessons
#   python3 lesson_inventory.py --json > inv.json   machine-readable, for querying
#   python3 lesson_inventory.py --anomalies         enumeration-derived oddities (still NOT a verdict)
#
#   Views: --versions --sections --headings --constructs --reveals --braincheck --callouts
#          --anomalies --schemes
#
# WHAT THIS IS, AND WHAT IT IS NOT  (Bible §24.6a)
# -----------------------------------------------
# A PARSER IS NECESSARY AND NOT SUFFICIENT. L06/L07 parsed clean and were still wrong.
# This tool therefore has NO exit code, NO PASS/FAIL, and NO verdict. Its only job is to
# ENUMERATE structure exhaustively so that session work QUERIES A TABLE instead of grepping
# the HTML — because at S80 a keyword-filtered <h4> grep hid two live ancestor blocks, a
# single-line heading regex found 35 headings where the truth was 63, .index() matched the
# first of three occurrences, and a fixed-width window bled into the next list.
#
# Pass/fail belongs in book_gates.py. Reading belongs here.
#
# WHY THE BOUNDING IS THE POINT
# -----------------------------
# A construct is bounded two different ways in this book:
#   ELEMENT-BOUNDED  — <div data-challenge="9.1" ...>   span = the div's own open..close
#   HEADING-BOUNDED  — <h4  data-challenge="9.m1" ...>  span = heading .. the FIRST of
#                      (next heading at level <= its own) / (next data-challenge element) /
#                      (the close of its enclosing element)
# The §20.1 gate has no heading-bounded case, which is why it reported 3/8/17-line code
# blocks recurring across 9.m3/9.m4/9.m5 when the truth is one block each at 5/8/2 lines.
# Every span below is computed from the parse tree, never from a fixed-width window.

import sys, os, re, glob, json, hashlib
import html as _html
from html.parser import HTMLParser

VOID = {'area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input', 'link',
        'meta', 'param', 'source', 'track', 'wbr'}
HEADINGS = {'h1', 'h2', 'h3', 'h4', 'h5', 'h6'}


def close_angle(src, i):
    """Offset just past the '>' that closes the tag starting at i, ignoring quoted '>'."""
    q = None
    j = i
    while j < len(src):
        c = src[j]
        if q:
            if c == q:
                q = None
        elif c in '"\'':
            q = c
        elif c == '>':
            return j + 1
        j += 1
    return len(src)


def flat(s):
    """Tag-stripped, entity-preserved, whitespace-collapsed text."""
    return re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', s)).strip()


class Tree(HTMLParser):
    """Builds a node tree carrying line, div depth, and exact byte span for every element."""

    def __init__(self, src):
        super().__init__(convert_charrefs=False)
        self.src = src
        self.line_off = [0]
        for line in src.splitlines(keepends=True):
            self.line_off.append(self.line_off[-1] + len(line))
        self.nodes = []
        self.comments = []
        self.stack = []

    def off(self):
        ln, col = self.getpos()
        return self.line_off[ln - 1] + col

    def handle_starttag(self, tag, attrs):
        start = self.off()
        node = {
            'tag': tag,
            'attrs': dict(attrs),
            'line': self.getpos()[0],
            'start': start,
            'open_end': close_angle(self.src, start),
            'depth': len(self.stack),
            'div_depth': sum(1 for n in self.stack if n['tag'] == 'div'),
            'parent': self.stack[-1] if self.stack else None,
            'end': None,
        }
        self.nodes.append(node)
        if tag not in VOID:
            self.stack.append(node)

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
        if self.nodes and self.nodes[-1]['tag'] == tag:
            self.nodes[-1]['end'] = self.nodes[-1]['open_end']
        if self.stack and self.stack[-1] is self.nodes[-1]:
            self.stack.pop()

    def handle_endtag(self, tag):
        if tag in VOID:
            return
        start = self.off()
        for i in range(len(self.stack) - 1, -1, -1):
            if self.stack[i]['tag'] == tag:
                self.stack[i]['end'] = close_angle(self.src, start)
                for orphan in self.stack[i + 1:]:
                    orphan['end'] = start          # swallowed by an outer close
                    orphan['unclosed'] = True
                del self.stack[i:]
                return

    def handle_comment(self, data):
        self.comments.append({'line': self.getpos()[0], 'off': self.off(), 'text': data.strip()})

    def finish(self):
        for node in self.stack:
            node['end'] = len(self.src)
            node['unclosed'] = True
        return self


# ---- CALLOUTS (§24.10, S91). The book marks a callout with a left border rule; the family
# is carried by the (background, border, glyph) TRIPLE, not by a name — L11/L12 label theirs
# with a bold lead SENTENCE and no family name at all. Collected off the node tree so the
# glyph and label come from the element's OWN span; a text search for a family name matches
# prose and reports the construct in lessons it is absent from (S91, THE WALL).
CALLOUT_RE = re.compile(r'border-left:\s*(\d+)px\s+solid\s+([^;"]+)')
CALLOUT_BG_RE = re.compile(r'background(?:-color)?:\s*([^;"]+)')


SECTION_RE = re.compile(r'=+\s*(SECTION\s+[0-9]+[A-Z]?|PART\s+[0-9]+[^=]*?)\s*:?\s*([^=]*?)\s*=*$', re.I)


def build(path):
    src = open(path, encoding='utf-8').read()
    tree = Tree(src)
    tree.feed(src)
    tree.close()
    tree.finish()
    nodes = tree.nodes

    # ---- SECTIONS: attributed from the id="section-N" anchors, which exist in all 16
    # lessons (and section-8a in exactly the 14 the §8A map names). The `<!-- ===== SECTION
    # N ===== -->` fence comments are NOT the spine and are enumerated separately below
    # rather than used for attribution. NOTE the reason changed at S82 and this comment was
    # left behind twice: pre-S82 the fences were unusable because they were SPARSE (the
    # "only 6 lessons carry any" claim here was itself the matcher artifact §6.8a was
    # written to kill — ten lessons carried them). Since §6.8a all sixteen carry one per
    # core anchor, 174 book-wide, and they are still not the spine — now because they are
    # GENERATED from it, so attributing sections to them would be circular.
    sections = []
    for n in nodes:
        m = re.fullmatch(r'section-(\d+)([a-z]?)', n['attrs'].get('id', '') or '')
        if m:
            sections.append({'name': f'§{m.group(1)}{m.group(2).upper()}',
                             'line': n['line'], 'off': n['start'], 'tag': n['tag']})
    sections.sort(key=lambda s: s['off'])

    fences = []
    for c in tree.comments:
        m = SECTION_RE.match(c['text'])
        if m and c['text'].startswith('='):
            fences.append({'name': m.group(1).upper().replace('  ', ' '),
                           'title': m.group(2).strip(),
                           'line': c['line'], 'off': c['off']})

    def section_of(off):
        cur = None
        for s in sections:
            if s['off'] <= off:
                cur = s['name']
            else:
                break
        return cur or '(front matter)'

    # ---- constructs: every element carrying data-challenge
    constructs = []
    for n in nodes:
        if 'data-challenge' not in n['attrs']:
            continue
        heading_bounded = n['tag'] in HEADINGS
        if not heading_bounded:
            span_end, how = n['end'], 'element'
        else:
            level = int(n['tag'][1])
            span_end = n['parent']['end'] if n['parent'] else len(src)
            how = 'heading→parent-close'
            for m in nodes:
                if m['start'] <= n['start'] or m['start'] >= span_end:
                    continue
                if m['tag'] in HEADINGS and int(m['tag'][1]) <= level:
                    span_end, how = m['start'], f'heading→next <{m["tag"]}>'
                    break
                if 'data-challenge' in m['attrs']:
                    span_end, how = m['start'], f'heading→next construct {m["attrs"]["data-challenge"]}'
                    break
        constructs.append({
            'marker': n['attrs']['data-challenge'],
            'kind': n['attrs'].get('data-kind', '(none → canonical card)'),
            'difficulty': n['attrs'].get('data-difficulty'),
            'grasp': n['attrs'].get('data-grasp'),
            'tag': n['tag'], 'id': n['attrs'].get('id'),
            'line': n['line'], 'div_depth': n['div_depth'],
            'start': n['start'], 'end': span_end, 'bounding': how,
            'lines': src.count('\n', n['start'], span_end) + 1,
            'section': section_of(n['start']),
            'label': flat(src[n['start']:n['open_end'] + 200])[:70],
        })

    def construct_of(off):
        hit = None
        for c in constructs:
            if c['start'] <= off < c['end']:
                if hit is None or c['start'] > hit['start']:
                    hit = c
        return hit

    # ---- reveals: every <details>
    reveals = []
    for n in nodes:
        if n['tag'] != 'details':
            continue
        body = src[n['open_end']:n['end'] or len(src)]
        summ = re.search(r'<summary\b[^>]*>(.*?)</summary>', body, re.S)
        after = body[summ.end():] if summ else body
        pres = re.findall(r'<pre\b.*?</pre>', after, re.S)
        code_lines = 0
        for p in pres:
            code_lines += sum(1 for ln in flat_lines(p) if ln.strip())
        parent = construct_of(n['start'])
        reveals.append({
            'type': n['attrs'].get('data-reveal', '(MISSING)'),
            'line': n['line'], 'div_depth': n['div_depth'],
            'section': section_of(n['start']),
            'construct': parent['marker'] if parent else None,
            'construct_kind': parent['kind'] if parent else None,
            'summary': flat(summ.group(1))[:60] if summ else '(no summary)',
            'body_lines': body.count('\n') + 1,
            'pre_blocks': len(pres),
            'code_lines': code_lines,
            'summary_padding': bool(re.search(r'padding', summ.group(0))) if summ else None,
        })

    # ---- version homes
    versions = []
    hid = re.search(r'<!--[^>]*?v(\d+\.\d+\.\d+)[^>]*?-->', src[:400])
    if hid:
        versions.append({'home': 'hidden comment', 'value': 'v' + hid.group(1),
                         'line': src.count('\n', 0, hid.start()) + 1})
    for m in re.finditer(r'Version (\d+\.\d+)', src):
        versions.append({'home': 'visible banner', 'value': 'v' + m.group(1),
                         'line': src.count('\n', 0, m.start()) + 1})

    # ---- brain check family
    bc = {'anchors': [], 'skills': 0, 'pills': 0, 'column': None}
    for n in nodes:
        i = n['attrs'].get('id', '')
        if re.fullmatch(r'brain-check-0[1-4]', i or ''):
            bc['anchors'].append({'id': i, 'line': n['line'], 'div_depth': n['div_depth'],
                                  'heading': flat(src[n['start']:n['start'] + 300])[:60]})
        if 'data-bc-skill' in n['attrs']:
            bc['skills'] += 1
        if 'data-bc-pill' in n['attrs']:
            bc['pills'] += 1
    col = re.search(r'<!-- BRAIN CHECK COLUMN.*?-->', src, re.S)
    if col:
        bc['column'] = {'chars': len(col.group(0)),
                        'md5': hashlib.md5(col.group(0).encode()).hexdigest()[:8],
                        'ends_with': col.group(0)[-3:]}

    callouts = []
    for nd in nodes:
        m = CALLOUT_RE.search(nd['attrs'].get('style', ''))
        if not m:
            continue
        body = src[nd['open_end']:nd['end'] or nd['open_end']]
        txt = flat(body)
        # Glyphs are literal characters in some lessons and NUMERIC ENTITIES in others
        # (L11/L12 write &#128721;). flat() preserves entities by design, so unescape for
        # glyph detection or the triple silently loses its third field. S91.
        gtxt = _html.unescape(txt)
        bg = CALLOUT_BG_RE.search(nd['attrs'].get('style', ''))
        callouts.append({
            'line': nd['line'], 'tag': nd['tag'], 'div_depth': nd['div_depth'],
            'section': section_of(nd['start']),
            'construct': (construct_of(nd['start']) or {}).get('marker'),
            'px': int(m.group(1)),
            'border': m.group(2).strip().lower(),
            'bg': bg.group(1).strip().lower() if bg else None,
            'glyph': next((c for c in gtxt if ord(c) > 0x2100), ''),
            'label': txt[:70],
            'bytes': (nd['end'] or nd['open_end']) - nd['start'],
        })

    heads = [{'tag': n['tag'], 'line': n['line'], 'div_depth': n['div_depth'],
              'id': n['attrs'].get('id'), 'section': section_of(n['start']),
              'construct': (construct_of(n['start']) or {}).get('marker'),
              'text': flat(src[n['open_end']:n['end'] or n['open_end']])[:70]}
             for n in nodes if n['tag'] in HEADINGS]

    return {
        'file': path,
        'lesson': os.path.basename(path)[7:9],
        'bytes': len(src), 'lines': src.count('\n') + 1,
        'versions': versions,
        'sections': sections,
        'fences': fences,
        'headings': heads,
        'constructs': constructs,
        'reveals': reveals,
        'braincheck': bc,
        'callouts': callouts,
        'unclosed': [{'tag': n['tag'], 'line': n['line']} for n in nodes if n.get('unclosed')],
        'max_div_depth': max((n['div_depth'] for n in nodes), default=0),
    }


def flat_lines(pre):
    """Rendered text lines of a <pre> block, tags stripped, entities left alone."""
    inner = re.sub(r'^<pre\b[^>]*>|</pre>$', '', pre.strip(), flags=re.S)
    return re.sub(r'<[^>]+>', '', inner).split('\n')


# ---------------------------------------------------------------- reporting

BANNER = (f'lesson_inventory.py {VERSION} — ENUMERATION, NOT A VERDICT (Bible §24.6a).\n'
          'No exit code, no PASS/FAIL. A parser is necessary and not sufficient: read the table.\n')


def w(s=''):
    print(s)


def view_versions(inv):
    w(f'--- VERSION HOMES  (L{inv["lesson"]}) ---')
    for v in inv['versions']:
        w(f'  line {v["line"]:>5}  {v["home"]:<16} {v["value"]}')
    w(f'  homes: {len(inv["versions"])}')


def view_sections(inv):
    w(f'--- SECTIONS  (L{inv["lesson"]}) ---')
    w('  anchors (id="section-N") — the spine, present book-wide:')
    for s in inv['sections']:
        w(f'    line {s["line"]:>5}  {s["name"]:<6} <{s["tag"]}>')
    w(f'    {len(inv["sections"])} anchors')
    w('  fence comments (present in only some lessons; enumerated, not used for attribution):')
    if not inv['fences']:
        w('    (none)')
    for f in inv['fences']:
        w(f'    line {f["line"]:>5}  {f["name"]:<12} {f["title"]}')
    names = [f['name'] for f in inv['fences']]
    dup = sorted({n for n in names if names.count(n) > 1})
    if dup:
        w(f'    REPEATED fence: {dup}')


def view_headings(inv):
    w(f'--- HEADINGS  (L{inv["lesson"]}) ---')
    w(f'  {"line":>5}  {"tag":<4} {"dd":>2}  {"section":<12} {"construct":<8} text')
    for h in inv['headings']:
        w(f'  {h["line"]:>5}  {h["tag"]:<4} {h["div_depth"]:>2}  {h["section"]:<12} '
          f'{(h["construct"] or ""):<8} {h["text"]}')
    by = {}
    for h in inv['headings']:
        by[h['tag']] = by.get(h['tag'], 0) + 1
    w(f'  total {len(inv["headings"])}   ' + '  '.join(f'{k}={v}' for k, v in sorted(by.items())))


def view_constructs(inv):
    w(f'--- CONSTRUCTS  (L{inv["lesson"]}) ---')
    w(f'  {"marker":<8} {"kind":<24} {"tag":<4} {"dd":>2} {"line":>5} {"lines":>5}  '
      f'{"doing/grasp":<18} bounding')
    for c in inv['constructs']:
        pill = f'{c["difficulty"] or "-"}/{c["grasp"] or "-"}'
        w(f'  {c["marker"]:<8} {c["kind"]:<24} {c["tag"]:<4} {c["div_depth"]:>2} '
          f'{c["line"]:>5} {c["lines"]:>5}  {pill:<18} {c["bounding"]}')
    w(f'  total {len(inv["constructs"])}')


def view_reveals(inv):
    w(f'--- REVEALS  (L{inv["lesson"]}) ---')
    w(f'  {"line":>5}  {"type":<12} {"dd":>2} {"construct":<8} {"kind":<10} '
      f'{"body":>5} {"pre":>3} {"code":>4}  summary')
    for r in inv['reveals']:
        w(f'  {r["line"]:>5}  {r["type"]:<12} {r["div_depth"]:>2} '
          f'{(r["construct"] or "-"):<8} {(r["construct_kind"] or "-")[:10]:<10} '
          f'{r["body_lines"]:>5} {r["pre_blocks"]:>3} {r["code_lines"]:>4}  {r["summary"]}')
    by = {}
    for r in inv['reveals']:
        by[r['type']] = by.get(r['type'], 0) + 1
    w(f'  total {len(inv["reveals"])}   ' + '  '.join(f'{k}={v}' for k, v in sorted(by.items())))


def view_braincheck(inv):
    bc = inv['braincheck']
    w(f'--- BRAIN CHECK  (L{inv["lesson"]}) ---')
    if not bc['anchors']:
        w('  no brain-check anchors — lesson not converted')
    for a in bc['anchors']:
        w(f'  line {a["line"]:>5}  {a["id"]}  div_depth={a["div_depth"]}  {a["heading"]}')
    w(f'  data-bc-skill={bc["skills"]}  data-bc-pill={bc["pills"]}')
    if bc['column']:
        c = bc['column']
        w(f'  column: {c["chars"]} chars  md5 {c["md5"]}  ends {c["ends_with"]!r}')
    else:
        w('  column: absent')


def view_callouts(inv):
    cs = inv['callouts']
    w(f'--- CALLOUTS ({len(cs)}) --- family is the (bg, border, glyph) triple, not a name')
    w(f'{"line":>6} {"sec":>5} {"dd":>3} {"px":>3} {"border":9} {"background":11} {"g":2} label')
    for c in cs:
        w(f'{c["line"]:>6} {str(c["section"] or "-"):>5} {c["div_depth"]:>3} {c["px"]:>3} '
          f'{(c["border"] or "-"):9} {(c["bg"] or "-"):11} {c["glyph"] or " ":2} {c["label"][:42]}')


def view_schemes(invs):
    from collections import Counter, defaultdict
    tri = Counter(); where = defaultdict(set); geom = Counter(); total = 0
    for inv in invs:
        for c in inv['callouts']:
            total += 1
            geom[c['px']] += 1
            k = (c['bg'], c['border'], c['glyph'])
            tri[k] += 1
            where[k].add(inv['lesson'])
    w(f'--- CALLOUT SCHEMES --- {total} blocks, {len(tri)} distinct (bg, border, glyph) triples')
    w()
    w('geometry:  ' + '  '.join(f'{k}px {v}' for k, v in sorted(geom.items())))
    off = sum(v for k, v in geom.items() if k != 4)
    w(f'off-canon geometry (not 4px): {off}')
    w()
    w(f'{"n":>5} {"L":>3}  {"background":11} {"border":9} {"g":2} lessons')
    for k, c in tri.most_common():
        ls = sorted(where[k])
        w(f'{c:>5} {len(ls):>3}  {(k[0] or "-"):11} {(k[1] or "-"):9} {k[2] or " ":2} '
          f'{",".join(ls) if len(ls) <= 8 else str(len(ls)) + " lessons"}')


def view_anomalies(invs):
    """Enumeration-derived oddities. Leads, never verdicts (§24.6c)."""
    w('--- ANOMALIES (LEADS, NOT FINDINGS \u2014 verify each by reading) ---')
    # The Brain Check family norm is the MODAL depth per anchor across the converted
    # lessons, so the outlier surfaces instead of all four reading as anomalies.
    seen = {}
    for inv in invs:
        for a in inv['braincheck']['anchors']:
            seen.setdefault(a['id'], []).append(a['div_depth'])
    BC_NORM = {k: max(set(v), key=v.count) for k, v in seen.items()}
    # v1.1.2: the norm was PRINTED here every run, inside the ANOMALIES header, so this
    # view was never silent when clean and the line had to be re-dismissed as "not a
    # finding" at every session open. It is not information this view owes the reader:
    # the outlier message below names the norm itself ("family norm is {norm}"), so
    # the header was redundant the moment it mattered and noise the rest of the time.
    # An anomalies list that always prints something is a list people stop reading.
    for inv in invs:
        L, out = inv['lesson'], []
        for n in inv['unclosed']:
            out.append(f'unclosed <{n["tag"]}> line {n["line"]}')
        for r in inv['reveals']:
            if r['type'] == '(MISSING)':
                out.append(f'line {r["line"]}: <details> with NO data-reveal')
        fnames = [f['name'] for f in inv['fences']]
        for n in sorted(set(fnames)):
            if fnames.count(n) > 1:
                out.append(f'{n} fence comment appears {fnames.count(n)}x')
        # Core 10 per Bible §4.4; §8A is CONDITIONAL so it is never "missing".
        have = {s['name'] for s in inv['sections']}
        miss = [f'§{i}' for i in range(1, 11) if f'§{i}' not in have]
        if miss:
            out.append(f'no section anchor for: {", ".join(miss)}')
        # A lesson that USES fence comments but skips one is the L09 case worth surfacing.
        # Fence usage is stratified, not uniform: L01/L09/L10 fence 9-10 sections,
        # L03/L07 fence one or two. A gap only means something inside COMPREHENSIVE
        # usage, so require >=5 before reporting one (L09's missing §7 is the case).
        secf = [f for f in inv['fences'] if f['name'].startswith('SECTION')]
        if len(secf) >= 5:
            fsec = {re.sub(r'SECTION ', '§', f['name']) for f in secf}
            gap = sorted(have - fsec - {'§8A'}, key=lambda x: int(re.sub(r'\D', '', x) or 0))
            if gap:
                out.append(f'uses fence comments but none for: {", ".join(gap)}')
        vis = [v['value'] for v in inv['versions'] if v['home'] == 'visible banner']
        if len(vis) != 1:
            out.append(f'{len(vis)} visible banner(s), expected 1')
        for a in inv['braincheck']['anchors']:
            norm = BC_NORM.get(a['id'])
            if norm is not None and a['div_depth'] != norm:
                out.append(f'{a["id"]} sits at div_depth {a["div_depth"]}, '
                           f'family norm is {norm}')
        for c in inv['constructs']:
            if c['kind'] == '(none → canonical card)':
                out.append(f'{c["marker"]}: no data-kind')
        if out:
            w(f'  L{L}:')
            for o in out:
                w(f'      {o}')
    w('  (a lead is not a defect — §24.6c: control-run and read before acting)')


def _sf(inv):
    return sum(1 for f in inv['fences'] if f['name'].startswith('SECTION'))


def _pf(inv):
    return sum(1 for f in inv['fences'] if f['name'].startswith('PART'))


def summary(invs):
    # "sect" = id="section-N" ANCHORS (the spine, all 16 lessons). The fence comments are
    # now SPLIT: "sfnc" = <!-- ===== SECTION N: TITLE ===== --> section fences (Bible §6.8a,
    # canonized S82 — one per anchor in all 16), "part" = §6.8 PART divider comments
    # (canonized S84 — 64 book-wide, four per lesson in all 16, byte-enforced by
    # book_gates gate 27, so this matcher no longer rests on a format nothing
    # guarantees; pre-S84 it read zero for L02 and L06, which each had comments in
    # an unwrapped format — the §6.8a blindness one construct over). v1.0.5
    # ran them together in one "fnce" column reading 75, which was 34 section fences plus 41
    # PART banners — two constructs under one label. The pre-S82 claim that "only six lessons
    # carry any" was an artifact of the matcher: ten lessons carried them, five in a bare
    # format it could not see, which is why L09 looked like the only lesson with a fence gap.
    w(f'{"L":<4}{"lines":>7}{"heads":>7}{"h3":>5}{"h4":>5}{"sect":>6}{"sfnc":>6}{"part":>6}{"cons":>6}'
      f'{"myst":>6}{"reveal":>8}{"sol":>5}{"hint":>6}{"quiz":>6}{"BC":>4}{"skill":>7}{"maxdd":>7}')
    for inv in invs:
        h3 = sum(1 for h in inv['headings'] if h['tag'] == 'h3')
        h4 = sum(1 for h in inv['headings'] if h['tag'] == 'h4')
        myst = sum(1 for c in inv['constructs'] if c['kind'] in ('bonus-observation', 'bonus-sabotage'))
        t = {}
        for r in inv['reveals']:
            t[r['type']] = t.get(r['type'], 0) + 1
        w(f'{inv["lesson"]:<4}{inv["lines"]:>7}{len(inv["headings"]):>7}{h3:>5}{h4:>5}'
          f'{len(inv["sections"]):>6}{_sf(inv):>6}{_pf(inv):>6}{len(inv["constructs"]):>6}{myst:>6}'
          f'{len(inv["reveals"]):>8}{t.get("solution", 0):>5}{t.get("hint", 0):>6}'
          f'{t.get("quiz", 0):>6}{len(inv["braincheck"]["anchors"]):>4}'
          f'{inv["braincheck"]["skills"]:>7}{inv["max_div_depth"]:>7}')
    w()
    w(f'{"TOTAL":<4}{sum(i["lines"] for i in invs):>7}'
      f'{sum(len(i["headings"]) for i in invs):>7}{"":>5}{"":>5}'
      f'{sum(len(i["sections"]) for i in invs):>6}'
      f'{sum(_sf(i) for i in invs):>6}{sum(_pf(i) for i in invs):>6}'
      f'{sum(len(i["constructs"]) for i in invs):>6}'
      f'{sum(1 for i in invs for c in i["constructs"] if c["kind"] in ("bonus-observation", "bonus-sabotage")):>6}'
      f'{sum(len(i["reveals"]) for i in invs):>8}')


def main():
    args = sys.argv[1:]
    views = [a[2:] for a in args if a.startswith('--')]
    picks = [a for a in args if not a.startswith('--')]

    files = sorted(glob.glob('lessons/Lesson_*.html'))
    if picks:
        keep = []
        for p in picks:
            keep += [f for f in files if p in f or re.sub(r'\D', '', p).zfill(2) == os.path.basename(f)[7:9]]
        files = sorted(set(keep)) or files
    if not files:
        sys.exit('no lesson files found — run from repo root')

    invs = [build(f) for f in files]

    if 'json' in views:
        print(json.dumps(invs if len(invs) > 1 else invs[0], indent=1))
        return

    print(BANNER)
    known = ['versions', 'sections', 'headings', 'constructs', 'reveals', 'braincheck',
             'callouts']
    want = [v for v in views if v in known]

    if 'schemes' in views:
        view_schemes(invs)
        if not want:
            return

    if 'anomalies' in views:
        view_anomalies(invs)
        if not want:
            return

    if not want:
        if len(invs) == 1:
            want = known
        else:
            summary(invs)
            w()
            w('one lesson for detail:  python3 lesson_inventory.py 09')
            w('single view, all 16:    python3 lesson_inventory.py --reveals')
            w('leads to read:          python3 lesson_inventory.py --anomalies')
            return

    for inv in invs:
        w(f'================ {inv["file"]}  ({inv["lines"]} lines, {inv["bytes"]} bytes) ================')
        for v in want:
            globals()[f'view_{v}'](inv)
            w()


if __name__ == '__main__':
    main()
