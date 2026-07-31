#!/usr/bin/env python3
# book_gates.py — whole-book consistency gates.
# VERSION below is the ONE home, and it sits ABOVE the changelog so a plain grep of this
# file lands on the live version, not on a changelog line (S98).
VERSION = 'v1.32'
# v1.32 (S99): GATE 38 hole closed. v1.31's label check is a floor of ONE, so a graphic
#   with 26 of 27 labels outlined passed it green — demonstrated, not argued, on an
#   lxml-built injection. GRAPHIC_ names now carry a path-data ceiling too. Found by
#   re-deriving gate 38's own numbers on xml.etree and lxml; all six figures agreed and
#   the SEVENTH thing, the one nobody had measured, was the hole. Arithmetic at the gate.
# v1.31 (S98): NEW GATE 38 — §21.2 a drawn graphic keeps live <text> and stays under a
#   60,000 B ceiling. Four referenced graphics shipped with every label OUTLINED,
#   +1.13 MB and a 50x growth, and passed 37/37 for a week; one rode in on the same
#   commit that carried this suite's own update. Thresholds at the gate, all measured.
# v1.30 (S98): GATE 37 REWRITTEN. The old §21.1 forbade any embedded raster in a
#   referenced .svg, which would have gone red on the first legitimate photo-plus-labels
#   composite. It now checks the three things that were actually wrong: a duplicated
#   payload, a byte ceiling, and a vector-content floor. Rationale at the gate.
# v1.29.1 (S98): version home moved ABOVE the changelog. No gate changed. A plain grep of
#   this file used to return v1.26.1 - a changelog line, three releases stale, and it read
#   exactly like an answer. session_versions.py grep_trap() now keeps the home on top.
# v1.26.1: §5.1 coverage 250 → 251. L01's AI-autocomplete block was on the one-off border
# #ffb300; the S95 repaint snapped it to WARNING's #ffc107, which brings it INTO this gate's
# scope (scheme + ⚠ glyph now agree). Its merged label was split into the canonical
# ⚠ WARNING label + separate title line. Control-run: the assert fired at 251/250 before
# this bump, so the number is doing work.
# v1.26.2: GEOM_BASELINE 115 → 114. L03's stop-motors block was 5px on #c0392b/#f8d7da; the
# S95 repaint moved it to #fdecea and normalised the rule to the canon 4px, so that debt is
# PAID, not moved, and its baseline row is gone. DJ ruling: from S95 on, a repaint that lands
# on one of the off-canon blocks normalises the width in the same edit.
# v1.28 (S97): NEW GATE 36 — every image reference resolves to a file on disk. Found by
# accident, not by any gate: Lesson_02 pointed at three .svg files and Lesson_05 at one that
# existed nowhere on main (an incomplete .svg -> .png migration; the originals survived only
# on the stranded branch Weymuth-patch-1). Four 404s were LIVE on the published site through a
# full 35/35 pass, in two of the first five lessons a student opens. Nothing checked img src.
# Control-run four ways before shipping: silent on the fixed tree; run against UNFIXED source
# at cd47f50 it independently rediscovered exactly those four with line numbers; a seeded
# break in each NON-lesson page (index/timer/going_deeper/tutor) was caught, proving the glob
# reaches past lessons/ — scope being the exact thing §12/§23 got wrong twice.
# v1.29 (S97): NEW GATE 37 — no REFERENCED .svg carries an embedded raster. Three files
# arrived in one session as PNG wrapped in an SVG envelope: valid XML, correct extension,
# zero drawing elements, the whole picture one base64 <image>. The memory ladder shipped that
# way at 4,879,809 B against the 4,517 B its true-vector replacement weighs — 1,080x — and it
# was LIVE in Lesson 02. Gate 36 stayed green throughout: a reference that resolves says
# nothing about what it resolves TO.
#   SCOPING, deliberate: this fails only on SVGs a page REFERENCES. Raw exports are staged in
# images/ before being wired up, and a gate that goes red on work-in-progress is a gate people
# learn to ignore. Unreferenced offenders are COUNTED and PRINTED, never fatal. Measured before
# choosing: strict would have failed on the two staged L05 sensor-array files the same day they
# landed; scoped passes and reports them. Protect the book, not the staging area.
# Usage:  python3 book_gates.py            (run from repo root)
# Exit 0 = all gates pass. Exit 1 = failures listed.
#
# Run at SESSION OPEN (health check) and before EVERY delivery (close gate).
# Each gate encodes a Bible rule; the Bible section is named on each line.
# When a new rule is canonized, add its gate here in the same session.

import re, glob, html, os, sys, collections

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from html.parser import HTMLParser as _HTMLParser
import lesson_inventory as LI          # §20.1 bounding: ONE definition, not a third regex

FAIL = []


def gate(name, bad):
    print(f'{"PASS" if not bad else "FAIL":>5}  {name}')
    for b in bad:
        print(f'         {b}')
    if bad:
        FAIL.append(name)


def txt(s):
    return re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', ' ', s)))


files = sorted(glob.glob('lessons/Lesson_*.html'))
site = files + ['going_deeper.html', 'index.html', 'tutor/tutor.html',
                'newproject.html', 'timer.html']
site = [f for f in site if os.path.exists(f)]


def L(f):
    return f[15:17]


# The 17 book pages that carry a version banner: 16 lessons + going_deeper.
# Stated explicitly and asserted, NOT inherited from whichever list is nearest.
pages17 = files + (['going_deeper.html'] if os.path.exists('going_deeper.html') else [])


def P(f):
    """Label for any of the 17 pages. L() slices lesson filenames and returns
    garbage for going_deeper.html — a gate that names the wrong file is a hazard."""
    return 'going_deeper' if f == 'going_deeper.html' else 'L' + L(f)


def visible(s):
    """What the reader can actually see: HTML comments removed.

    A gate that checks placement or visibility MUST strip what the reader
    cannot see before matching, or it reports a condition it never tested.
    """
    return re.sub(r'<!--.*?-->', '', s, flags=re.S)


R = {f: open(f, encoding='utf-8').read() for f in site}

# ---- §5b: hidden full version on line 1; exactly ONE visible banner carrying its major.minor
# S89: the build banner was deleted from all 17 pages. It was a COMMENT, so the old
# gate — which matched raw text and required exactly 2 hits — was counting a hidden
# string as a visible banner. Comments are stripped first now.
# S89: coverage moved from `files` (16) to `pages17` (17). going_deeper.html had drifted
# to a visible 01.0 against a hidden 01.1.0 and survived because it was never walked.
bad = []
if len(pages17) != 17:
    bad.append(f'COVERAGE: expected 17 versioned pages, found {len(pages17)}')
for f in pages17:
    s = R[f]
    hid = re.search(r'v(\d+\.\d+)\.\d+', s[:60])
    vis = re.findall(r'Version (\d+\.\d+)', visible(s))
    if not hid:
        bad.append(f'{P(f)}: no hidden version comment on line 1')
    elif len(vis) != 1:
        bad.append(f'{P(f)}: expected exactly 1 visible banner, found {len(vis)}: {vis}')
    elif vis[0] != hid.group(1):
        bad.append(f'{P(f)}: hidden={hid.group(1)} but visible={vis[0]} — they must agree')
gate('§5b  version: hidden == the one visible banner, all 17', bad)

# ---- §5b: the one visible banner carries exactly one date.
# S89: was an addendum about TWO banners agreeing. There is only one banner now,
# so "agreement" is not the property — presence and uniqueness are.
bad = []
if len(pages17) != 17:
    bad.append(f'COVERAGE: expected 17 versioned pages, found {len(pages17)}')
for f in pages17:
    d = re.findall(r'Version \d+\.\d+(?: &mdash;| —) (\w+ \d{4})', visible(R[f]))
    if len(d) != 1:
        bad.append(f'{P(f)}: expected exactly 1 dated visible banner, found {len(d)}: {d}')
gate('§5b  date: exactly one dated visible banner, all 17', bad)

# ---- §22: terminal blocks — [SUCCESS] green #6a9955, diagnostics red #f14c4c
bad = []
for f in files:
    s = R[f]
    for m in re.finditer(r'<pre.*?</pre>', s, re.S):
        blk = m.group(0)
        t = re.sub(r'<[^>]+>', '', blk)
        if re.search(r'error:|undefined reference|\[SUCCESS\]|\[FAILED\]|Writing \||Verifying \|', t):
            if '[SUCCESS]' in t and 'color: #6a9955;">[SUCCESS]' not in blk:
                bad.append(f'{L(f)}@{m.start()}: [SUCCESS] not green')
            if re.search(r'error:|undefined reference', t) and '#f14c4c' not in blk:
                bad.append(f'{L(f)}@{m.start()}: diagnostic not red')
gate('§22  terminal colors (SUCCESS green / errors red)', bad)

# ---- §4.2: data-challenge markers globally unique
bad = []
seen = collections.Counter()
for f in files:
    for m in re.findall(r'data-challenge="([^"]*)"', R[f]):
        seen[m] += 1
dups = [f'{k} x{v}' for k, v in seen.items() if v > 1]
if dups:
    bad.append('duplicates: ' + ', '.join(dups))
gate('§4.2 data-challenge markers globally unique', bad)

# ---- §4.3: picker labels (element textContent, 60 chars) unique per lesson
bad = []
for f in files:
    s = R[f]
    labels = collections.Counter()
    for m in re.finditer(r'<(\w+)([^>]*data-challenge="[^"]*"[^>]*)>', s):
        tag = m.group(1)
        close = s.find('</' + tag + '>', m.end())
        t = txt(s[m.end():close]).strip()[:60]
        labels[t] += 1
    for t, n in labels.items():
        if n > 1:
            bad.append(f'{L(f)}: "{t[:45]}" x{n}')
gate('§4.3 picker labels unique within each lesson', bad)

# ---- §4.1: retired construct names must not reappear
bad = []
for f in files:
    if re.search(r'CHALLENGE \(\d+ minute', R[f]):
        bad.append(f'{L(f)}: old "CHALLENGE (n min)" label (renamed TRY IT, S65)')
gate('§4.1 no retired construct names', bad)

# ---- §6.12b: two-axis pill parity per lesson
bad = []
for f in files:
    d = len(re.findall(r'data-difficulty=', R[f]))
    g = len(re.findall(r'data-grasp=', R[f]))
    if d != g:
        bad.append(f'{L(f)}: difficulty={d} grasp={g}')
gate('§6.12b pill two-axis parity', bad)

# ---- structure: paired-tag balance across every site file
# v1.27: this gate used to count `<tag\\b` against `</tag>` for a FIXED LIST OF SEVEN
# tags. Two consequences, both found by the S95 triple-check with html.parser:
#   1. `p` was not on the list, so TWO orphan `</p>` tags with no opening `<p>` sat in
#      L06 and L15 through every 35/35 pass. Only 7 of the 41 paired tags in use were
#      checked at all.
#   2. The counting method reads inside HTML COMMENTS. index.html mentions `<h1>` in a
#      comment explaining why the h1 is sr-only, which counts as 2/1 and would have
#      failed the moment the list was widened. A false failure costs 3x a blank one.
# So the method is replaced, not the list: a real parser, every paired tag, comments and
# CDATA ignored for free, and crossed tags detected as well as unbalanced ones.
_VOID = {'area','base','br','col','embed','hr','img','input','link','meta','param',
         'source','track','wbr'}

class _Balance(_HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=False)
        self.stack = []; self.bad = []
    def handle_starttag(self, t, a):
        if t not in _VOID:
            self.stack.append((t, self.getpos()[0]))
    def handle_endtag(self, t):
        if t in _VOID:
            return
        if not self.stack:
            self.bad.append(f'orphan </{t}> line {self.getpos()[0]} (nothing open)')
        elif self.stack[-1][0] == t:
            self.stack.pop()
        else:
            for i in range(len(self.stack) - 1, -1, -1):
                if self.stack[i][0] == t:
                    self.bad.append(f'crossed </{t}> line {self.getpos()[0]}')
                    del self.stack[i:]
                    break
            else:
                self.bad.append(f'orphan </{t}> line {self.getpos()[0]} (no matching open)')

bad = []
for f in site:
    w = _Balance()
    w.feed(R[f])
    w.close()
    for m in w.bad:
        bad.append(f'{f}: {m}')
    for t, ln in w.stack:
        if t not in ('html', 'head', 'body'):
            bad.append(f'{f}: unclosed <{t}> opened line {ln}')
gate('tag balance (all site files)', bad)

# ---- timers: every iframe has min+label; labels unique per lesson
bad = []
for f in files:
    labs = collections.Counter()
    for m in re.finditer(r'<iframe[^>]*timer\.html([^"]*)"', R[f]):
        q = m.group(1)
        if 'min=' not in q or 'label=' not in q:
            bad.append(f'{L(f)}: timer missing param: {q[:50]}')
        lab = re.search(r'label=([^&"]*)', q)
        if lab:
            labs[lab.group(1)] += 1
    for t, n in labs.items():
        if n > 1:
            bad.append(f'{L(f)}: timer label "{t}" x{n}')
gate('timers: params present, labels unique per lesson', bad)

# ---- links: index.html relative links resolve to real files
bad = []
for m in re.finditer(r'href="([^"#][^"]*)"', R['index.html']):
    u = m.group(1)
    if u.startswith('http'):
        continue
    if not os.path.exists(u):
        bad.append(f'index.html -> {u} MISSING')
gate('index.html relative links resolve', bad)

# ---- links: going_deeper references use canonical URLs
bad = []
for f in site:
    for m in re.finditer(r'href="([^"]*going_deeper[^"]*)"', R[f]):
        if m.group(1) not in ('going_deeper.html',
                              'https://weymuth.github.io/zumo/going_deeper.html'):
            bad.append(f'{f}: {m.group(1)}')
gate('going_deeper links canonical', bad)

# ---- §24: cross-lesson promises — a forward-ref's topic must exist in the target lesson
bad = []
T = {f: txt(R[f]) for f in files}
for f in files:
    src = int(L(f))
    for m in re.finditer(r'([^.!?]{10,140}?)\b[Ll]esson (\d+)\b([^.!?]{0,110})[.!?]', T[f]):
        tgt = int(m.group(2))
        if tgt <= src or tgt > 16:
            continue
        sent = (m.group(1) + ' Lesson ' + m.group(2) + m.group(3)).strip()
        keys = re.findall(r'[a-zA-Z_]+\(\)|\b(?:gyro|encoder|PID|state machine|kill switch|silver|'
                          r'proximity|calibrat\w+|modulo|array|float|extern|header|P-control|Kp|EEPROM|'
                          r'for loop|==)\b', sent)
        keys = [k for k in set(keys) if len(k) > 2][:3]
        if not keys:
            continue
        tf = f'lessons/Lesson_{tgt:02d}.html'
        missing = [k for k in keys if k.lower() not in T[tf].lower()]
        if missing:
            bad.append(f'L{src:02d} -> L{tgt:02d}: promises {missing}')
gate('§24  cross-lesson promises land in target lesson', bad)

# ---- §24.4: verifiable arithmetic in prose
bad = []
for f in files:
    t = T[f]
    for m in re.finditer(r'(\d+)\s*characters?,?\s*(?:so|=|is|makes?)\s*(\d+)\s*bytes', t):
        a, b = int(m.group(1)), int(m.group(2))
        if b not in (a, a + 1):
            bad.append(f'{L(f)}: "{m.group(0)}"')
    for m in re.finditer(r'([\d,]+)\s*(?:ms|milliseconds?)\s*(?:=|is|equals?)\s*([\d.]+)\s*seconds?', t):
        a = int(m.group(1).replace(',', '')); b = float(m.group(2))
        if abs(a / 1000 - b) > 0.01:
            bad.append(f'{L(f)}: "{m.group(0)}" ({a}ms = {a/1000}s)')
    for m in re.finditer(r'([\d,]+)\s*(?:mV|millivolts?)[^.]{0,60}?([\d.]+)\s*volts?', t):
        a = int(m.group(1).replace(',', '')); b = float(m.group(2))
        if abs(a / 1000 - b) > 0.05:
            bad.append(f'{L(f)}: "{m.group(0)[:60]}" ({a}mV = {a/1000}V)')
gate('§24.4 arithmetic claims verify', bad)

# ---- §16: hardware constants match canon (wrong values that must never appear)
bad = []
WRONG = {'32,768 bytes usable': 'usable flash is 28,672'}
for f in files:
    for w, why in WRONG.items():
        if w in T[f]:
            bad.append(f'{L(f)}: "{w}" — {why}')
gate('§16  hardware constants match canon', bad)

# ---- structure: real HTML parse (S68). Supersedes count-based checks: an orphaned
# ---- close tag can BALANCE an unclosed box, so a count gate is satisfied by the bug itself.
from html.parser import HTMLParser as _HP
_VOID = {'area','base','br','col','embed','hr','img','input','link','meta','param','source','track','wbr'}
_STRICT = {'div','details','summary','table','section','article','span','a','pre','body','html','ul','ol','h1','h2','h3','h4'}

class _Struct(_HP):
    def __init__(self):
        super().__init__(convert_charrefs=True); self.stack=[]; self.err=[]
    def handle_starttag(self, t, a):
        if t not in _VOID: self.stack.append((t, self.getpos()[0]))
    def handle_endtag(self, t):
        if t in _VOID: return
        for i in range(len(self.stack)-1, -1, -1):
            if self.stack[i][0] == t:
                for tag, ln in self.stack[i+1:]:
                    if tag in _STRICT:
                        self.err.append(f'line {ln}: <{tag}> never closed (swallowed by </{t}> line {self.getpos()[0]})')
                del self.stack[i:]; return
        if t in _STRICT:
            self.err.append(f'line {self.getpos()[0]}: stray </{t}> with nothing open')

bad = []
for f in site:
    pr = _Struct(); pr.feed(R[f]); pr.close()
    for e in pr.err + [f'line {l}: <{t}> still open at EOF' for t, l in pr.stack if t in _STRICT]:
        bad.append(f'{f}: {e}')
    trail = R[f][R[f].rfind('</html>') + 7:].strip()
    if trail:
        bad.append(f'{f}: {trail[:40]!r} after </html>')
gate('structure: HTML parses to the intended shape', bad)

# ---- structure: end matter must not be sealed inside a section panel (S68).
# ---- Well-formed HTML can still be wrong: L06/L07 parsed clean with the footer
# ---- trapped inside the Image Index box. The parser cannot see this class.
bad = []
_d = re.compile(r'<div\b[^>]*>|</div\s*>')
for f in files:
    i = R[f].find('id="image-index"')
    if i < 0:
        continue
    j = R[f].find('border-top: none', i)
    j = R[f].rfind('<div', 0, j)
    depth = 0; close = None
    for m in _d.finditer(R[f], j):
        depth += 1 if m.group(0).startswith('<div') else -1
        if depth == 0:
            close = m.end(); break
    if close is None:
        bad.append(f'{L(f)}: Image Index panel never closes'); continue
    inside = R[f][j:close]
    if re.search(r'<hr\b|linear-gradient\(135deg, #6c757d', inside):
        bad.append(f'{L(f)}: lesson end matter is sealed INSIDE the Image Index panel')
gate('structure: end matter sits outside the section panel', bad)

# ---- §6.5a: the lesson strip is present in every lesson and byte-identical book-wide.
# It ships as ONE block (static links + self-hydrating script deriving the current lesson
# from the URL), so any hand-variation is drift. Marker comments bound the block.
bad = []
strips = []
for f in files:
    m = re.search(r'<!-- LESSON STRIP v1.*?<!-- /LESSON STRIP -->', R[f], re.S)
    if not m:
        bad.append(f'{L(f)}: lesson strip missing')
    else:
        strips.append((f, m.group(0)))
if strips:
    ref_f, ref = strips[0]
    for f, s2 in strips[1:]:
        if s2 != ref:
            bad.append(f'{L(f)}: lesson strip differs from L{L(ref_f)}')
gate('§6.5a lesson strip present and byte-identical in all 16', bad)

# ---- §25.6: header hero + footer, identical across all 17 pages (S89: build banner dropped)
import hashlib

PAGES = files + (['going_deeper.html'] if os.path.exists('going_deeper.html') else [])


def _close_of(s2, st, tag):
    d = 0
    for m in re.finditer(rf'<{tag}\b|</{tag}>', s2[st:]):
        d += 1 if m.group(0) != f'</{tag}>' else -1
        if d == 0:
            return st + m.end()
    return -1


def _skel(block):
    return hashlib.md5(re.sub(r'>[^<]*<', '><', block).encode()).hexdigest()[:8]


heroes, footers, bad = {}, {}, []
for f in PAGES:
    s2 = R[f]
    lab = 'GOING DEEPER' if f == 'going_deeper.html' else 'LESSON ' + L(f)
    m = re.search(r'>\s*' + lab + r'\s*<', s2)
    if not m:
        bad.append(f'{f}: no hero label "{lab}"')
        continue
    v = re.search(r'Version \d+\.\d+ &mdash; \w+ \d{4}', s2[m.start():m.start() + 2500])
    if not v:
        bad.append(f'{f}: hero has no dated Version line')
        continue
    vpos = m.start() + v.start()
    st = m.start()
    while True:
        st = s2.rfind('<div', 0, st)
        if st < 0:
            break
        en = _close_of(s2, st, 'div')
        if en > vpos:
            break
    heroes.setdefault(_skel(s2[st:en]), []).append(f)
    i = s2.find('&copy; 2026 RoboLore')
    if i < 0:
        bad.append(f'{f}: footer missing the credits line')
        continue
    a = s2.rfind('<p', 0, i)
    b = s2.find('</p>', i) + 4
    footers.setdefault(_skel(s2[a:b]), []).append(f)
    # S89: the BUILD BANNER and 'ZUMO Callout Standard v1.0 Applied' assertions were
    # removed here. The banner was a hidden third version home that the §5b gate was
    # miscounting as visible. The callout-standard string named no document that existed
    # — the gate asserted a string that existed only because the gate asserted it.
    # Its successor is BookComponentStandard.md at the repo root.
if len(heroes) > 1:
    bad.append(f'hero skeletons differ: { {k: [L(x) for x in v] for k, v in heroes.items()} }')
if len(footers) > 1:
    bad.append(f'footer skeletons differ: { {k: [L(x) for x in v] for k, v in footers.items()} }')
gate('§25.6 header/footer identical across all 17', bad)

# ---- §25.2: where a lesson has converted to the four exit blocks, it must conform
RETIRED = ['STOP &amp; PROCESS', 'Conceptual Understanding',
           'Check Your Understanding', 'Reflection Questions',
           'Explain It in Writing']
bad = []
for f in files:
    s2 = R[f]
    if 'MENTAL KNOWLEDGE CHECK' not in s2:
        continue                      # not yet converted — §25 does not bind it
    # S91: bound by the id §25.10h canonizes, NOT by the nearest preceding <div>.
    # rfind('<div') was correct only by accident -- it worked because the Brain Check
    # TITLE happened to be a <strong>. The S91 title sweep made every title a <div>,
    # so rfind landed on the title and the block collapsed to one line, reading 0 items
    # in all nine lessons while the lessons were untouched. Same defect the Bible
    # already recorded for §20.1(5) at S83, one gate over.
    i = s2.find('id="brain-check-01"')
    if i < 0:
        i = s2.find('MENTAL KNOWLEDGE CHECK')
    st = s2.rfind('<div', 0, i)
    en = _close_of(s2, st, 'div')
    blk = s2[st:en]
    n = blk.count('data-reveal="quiz"')
    if not 3 <= n <= 5:
        bad.append(f'{L(f)}: Mental has {n} items, §25.2 caps 3-5')
    for m in re.finditer(r'<summary[^>]*>(.*?)</summary>', blk, re.S):
        if not re.search(r'&sect;|§', m.group(1)):
            bad.append(f'{L(f)}: Mental item names no § — {txt(m.group(1))[:52]}')
    if s2.find('KNOWLEDGE CHECK &mdash; What You Just Built') < s2.find('id="section-10"'):
        bad.append(f'{L(f)}: §10 Knowledge Check is not inside §10')
    j = s2.find('REFLECTION &mdash; In Your Notebook')
    if j < 0:
        bad.append(f'{L(f)}: converted but has no Reflection block')
    else:
        rst = s2.rfind('<div', 0, j)
        if 'data-reveal' in s2[rst:_close_of(s2, rst, 'div')]:
            bad.append(f'{L(f)}: Reflection carries a reveal (§25.2: never)')
    for r in RETIRED:
        if r in s2:
            bad.append(f'{L(f)}: converted but retired name still present — "{html.unescape(r)}"')
    for k in range(1, 5):
        if f'id="brain-check-0{k}"' not in s2:
            bad.append(f'{L(f)}: converted but Brain Check anchor 0{k} missing (§25.10)')
        else:
            j = s2.find(f'id="brain-check-0{k}"')
            wrap = s2[s2.rfind('<div', 0, j + 30):s2.find('>', j) + 1]
            if 'border-left: 4px solid #3f51b5' not in wrap:
                bad.append(f'{L(f)}: Brain Check 0{k} wrapper is not Type 10 indigo (§25.10)')
    if 'BRAIN CHECK COLUMN START' not in s2:
        bad.append(f'{L(f)}: converted but Brain Check column block missing (§25.10)')
    j2 = s2.find('id="brain-check-02"')
    if j2 > 0:
        blk2 = s2[j2:_close_of(s2, s2.rfind('<div', 0, j2 + 30), 'div')]
        boxes = blk2.count('\u2610')
        tagged = blk2.count('data-bc-skill=')
        if boxes != tagged:
            bad.append(f'{L(f)}: BC02 has {boxes} checkbox items but {tagged} data-bc-skill tags (§25.10 skill gate)')
gate('§25.2 converted lessons conform to the four exit blocks + §25.10 Brain Check', bad)

# ---- §25.8: Brain Check 03 carries at least FOUR items (floor, no maximum — DJ ruling S77)
bad = []
for f in files:
    s2 = R[f]
    j3 = s2.find('id="brain-check-03"')
    if j3 < 0:
        continue                     # unconverted lessons are out of scope
    blk3 = s2[j3:_close_of(s2, s2.rfind('<div', 0, j3 + 30), 'div')]
    items = len(re.findall(r'<details data-reveal="\w+"', blk3))
    if items < 4:
        bad.append(f'{L(f)}: Brain Check 03 has {items} items, floor is 4 (§25.8)')
gate('§25.8 Brain Check 03 carries at least four items', bad)

# ---- §5b: every web tool carries a greppable in-file version line
WEB_TOOLS = {'timer.html': 'Timer', 'tutor/tutor.html': 'Tutor',
             'newproject.html': None, 'index.html': 'Index'}
bad = []
for f in WEB_TOOLS:
    if not os.path.exists(f):
        bad.append(f'{f}: MISSING from the repo')
        continue
    head = open(f, encoding='utf-8').read()[:600]
    if not re.search(r'<!--\s*\w[\w ]*version:\s*v[\d.]+\s*-->', head, re.I):
        bad.append(f'{f}: no in-file version comment in the first 600 bytes')
gate('§5b  web tools carry an in-file version line', bad)

# ---- §12/§23: canonical site layout — every page in its one correct place, no strays
EXPECTED = sorted(
    [f'lessons/Lesson_{n:02d}.html' for n in range(1, 17)] +
    ['going_deeper.html', 'index.html', 'newproject.html', 'timer.html', 'tutor/tutor.html'])
found = sorted(f for f in glob.glob('**/*.html', recursive=True)
               if not f.startswith('.git'))
bad = []
for f in sorted(set(found) - set(EXPECTED)):
    bad.append(f'STRAY page: {f}  (not a canonical location)')
for f in sorted(set(EXPECTED) - set(found)):
    bad.append(f'MISSING page: {f}')
gate('§12/§23 site layout: every page in its canonical place, no strays', bad)

# ---- §20.1: a challenge answer must not hide behind a KEPT reveal type.
# The tutor front-end strips ONLY <details data-reveal="solution">.  A finished,
# fill-nothing-in code block inside a `hint` is therefore shipped to the model
# while looking withheld to a reader.  Found live in L01 C11 at S79.
_LAND = ('<<<', 'GOES HERE', 'goes here', 'your code here', 'YOUR CODE HERE',
         '______', '_____', '&larr;', '&#8592;', 'write your', 'YOUR ')


# The card extent is the PARSE-TREE span from lesson_inventory (§24.6a), not a
# rfind('<div') window.  A construct is bounded two ways in this book and the old
# window only ever produced the first one by accident:
#   ELEMENT-BOUNDED  <div data-challenge="9.1">   span = that div open..close
#   HEADING-BOUNDED  <h4  data-challenge="9.m1">  span = heading .. FIRST of
#                    (next heading at level <= its own / next construct / parent close)
# With the window, every h4-borne marker inherited its enclosing PANEL: L09 9.m3-9.m5
# reported 3/8/17 code lines where reading gives 5/8/2, and L02 2.t4 -- a one-line
# <strong> holding zero <details> -- swallowed a §6 build-step `check` reveal 17 lines
# past its own end, which is where the "2.t4 holds the worked code" claim came from.


def _enclosing_reveal(card, pre_start):
    ctx, depth = None, 0
    for m in re.finditer(r'<details[^>]*data-reveal="([a-z]+)"|<details|</details>',
                         card[:pre_start]):
        if m.group().startswith('</details'):
            depth -= 1
            if depth <= 0:
                ctx, depth = None, 0
        else:
            depth += 1
            if depth == 1:
                ctx = m.group(1)
    return ctx


def _is_finished_code(code):
    body = html.unescape(re.sub(r'<[^>]+>', '', code))
    if any(k in code or k in body for k in _LAND):
        return 0
    return len([ln for ln in body.splitlines() if ln.strip().endswith((';', '{', '}'))])


bad = []
seen = 0
for f in files:
    s = R[f]
    inv = LI.build(f)
    assert inv['bytes'] == len(s), f'{f}: inventory/gate read disagree'
    for c in inv['constructs']:
        seen += 1
        card = s[c['start']:c['end']]
        # §25.10g is a SABOTAGE rule: those reveals carry the planted line.  Observation
        # reveals hold no code at all, so the zero-threshold branch must not chase them.
        mystery = c['kind'] == 'bonus-sabotage'
        for pm in re.finditer(r'<pre[^>]*>(.*?)</pre>', card, re.S):
            if _enclosing_reveal(card, pm.start()) != 'hint':
                continue
            n = _is_finished_code(pm.group(1))
            # §25.10g: a mystery's bug+fix reveal is a `solution`, full stop.  Its planted
            # snippets run 1-2 lines, so the >=3 threshold below is not an exemption --
            # it is why L08 passed this gate on luck for eight sessions (S80).
            if mystery and pm.group(1).strip():
                bad.append(f'{f} mystery {c["marker"]}: code block inside a '
                           f'data-reveal="hint" — §25.10g says a mystery reveal is a '
                           f'"solution"; ANY code here reaches the tutor')
            elif n >= 3:
                bad.append(f'{f} challenge {c["marker"]}: {n}-line finished code block '
                           f'inside a data-reveal="hint" — reaches the tutor; type it "solution"')
if seen < 100:
    bad.append(f'COVERAGE: only {seen} constructs bounded book-wide — the span port is broken, '
               f'so this gate is passing an empty population')
gate('§20.1 no finished answer hidden behind a hint reveal', bad)


# ---- §8/§6.12c: two reveals stacked as siblings must agree on summary padding.
# One padded and one not makes the disclosure triangle and label sit at different
# left insets on adjacent rows -- visible, and invisible to every other gate.
# Introduced at S79 by adding a padded solution beneath an unpadded hint (L01 C11).
_DET = re.compile(r'<details\b[^>]*>|</details>', re.I)


def _sibling_reveals(s):
    spans, stack = [], []
    for m in _DET.finditer(s):
        if m.group().startswith('</'):
            if stack:
                spans.append((stack.pop(), m.end()))
        else:
            stack.append(m.start())
    out = []
    for a, b in sorted(spans):
        blk = s[a:b]
        t = re.search(r'data-reveal="([a-z]+)"', blk[:400])
        sm = re.search(r'<summary([^>]*)>', blk)
        out.append((a, b, t.group(1) if t else None, sm.group(1) if sm else ''))
    return out


bad = []
for f in files:
    s = R[f]
    rs = _sibling_reveals(s)
    for k in range(len(rs) - 1):
        a, b = rs[k], rs[k + 1]
        if b[0] < a[1]:
            continue                                    # nested, not a sibling
        if re.sub(r'\s+', '', re.sub(r'<[^>]+>', '', s[a[1]:b[0]])):
            continue                                    # prose between them
        if ('padding' in a[3]) != ('padding' in b[3]):
            bad.append(f'{f}: {a[2]} reveal stacked directly above {b[2]} reveal, '
                       f'but only one <summary> carries padding — the triangle and '
                       f'label sit at different left insets')
gate('§6.12c stacked sibling reveals agree on summary padding', bad)


print()

# ---- §25.11 (S81 DJ ruling): a reveal's VISIBLE LABEL must agree with its data-reveal
# ---- TYPE. "If it's a hint, then say hint. If it's a solution, then call it a solution."
# ---- Found live in nine mystery reveals (L08 x4, L09 x5) that S80 retyped to `solution`
# ---- attribute-only, leaving the label reading "Hint" on a block the tutor now strips.
# ---- L11 was the model again: solution + "Answer" in all four of its mysteries.
# ---- Deliberately NARROW per §24.6c — the label vocabulary is legitimately varied
# ---- (62 "reveal solution", 13 "Answer", 9 "worked version"), so this asserts only the
# ---- one contradiction shape that was verified by reading, not a label whitelist.
bad = []
_HINTY = ('hint',)
_ANSWERY = ('answer', 'solution', 'worked')
for f in files:
    for m in re.finditer(r'<details\b([^>]*)>\s*<summary\b[^>]*>(.*?)</summary>', R[f], re.S):
        attrs, label = m.group(1), txt(m.group(2)).strip().lower()
        tm = re.search(r'data-reveal="([^"]+)"', attrs)
        if not tm:
            continue
        t = tm.group(1)
        ln = R[f].count('\n', 0, m.start()) + 1
        if t == 'solution' and any(w in label for w in _HINTY):
            bad.append(f'{L(f)} line {ln}: data-reveal="solution" but label says hint')
        if t == 'hint' and any(w in label for w in _ANSWERY):
            bad.append(f'{L(f)} line {ln}: data-reveal="hint" but label promises an answer')
gate('§25.11 reveal label agrees with reveal type', bad)

# ---- §6.8a (S82 DJ ruling): THE SECTION FENCE IS GENERATED FROM THE ANCHOR SPINE.
# ---- DJ, on being offered a widened detector: "Why widen the fence. Can't we just fix
# ---- the issues that are causing the fence issues." The fence had never been canonized
# ---- (zero rules in the Bible before v8.68), so it drifted five ways across ten lessons
# ---- and lesson_inventory.py's narrow matcher was blind in five of them — which is why
# ---- L09's missing §7 looked like the only fence gap when there were nine.
# ---- The fence is DERIVED, so this gate compares the file against a regenerated
# ---- expectation rather than against a vocabulary: number and title must both agree
# ---- with the anchor the fence precedes, and any near-miss comment fails loudly.
bad = []
_EQ = '=' * 21
_FENCE = re.compile(r'<!-- ' + re.escape(_EQ) + r' SECTION (\S+): (.*?) ' + re.escape(_EQ) + r' -->')
_CORE = ('1', '2', '3', '4', '5', '6', '7', '8', '8a', '9', '10')


def _fence_title(s):
    t = html.unescape(s).strip()
    while t and not t[0].isalnum():
        t = t[1:].lstrip()
    if t.lower().startswith('section'):
        c = t.find(':')
        if c >= 0:
            t = t[c + 1:].strip()
    for d in ('\u2014', '\u2013', ' - '):
        if d in t:
            t = t.split(d, 1)[0].strip()
    return re.sub(r'\s+', ' ', t).upper()


for f in files:
    s = R[f]
    for m in re.finditer(r'<!--(.*?)-->', s, re.S):
        body = re.sub(r'\s+', ' ', m.group(1)).strip().strip('= ').strip()
        p = body.split(None, 1)
        if len(p) > 1 and p[0].upper() == 'SECTION' and not body.upper().startswith('TITLE'):
            if not _FENCE.fullmatch(m.group(0)):
                ln = s.count('\n', 0, m.start()) + 1
                bad.append(f'{L(f)} line {ln}: non-canonical section fence: {body[:44]}')
    want = []
    for am in re.finditer(r'id="section-([0-9]+[a-z]?)"', s):
        if am.group(1) not in _CORE:
            continue
        num = am.group(1).upper()
        gt = s.find('>', am.start())
        title = _fence_title(s[gt + 1:s.find('<', gt)])
        want.append((num, title))
        # --- S82b: the anchor must SIT INSIDE its banner, and the fence must be
        # --- ADJACENT to that banner with nothing but whitespace between them.
        # --- The earlier ordered-list form verified content and order but not
        # --- placement, and passed L06/L07 while their §5 anchor had fallen out
        # --- of its banner into the content panel — a live layout defect that
        # --- tag balance and the structural gates also passed.
        wrap = s.rfind('<div', 0, s.rfind('<', 0, am.start()) + 1)
        ln = s.count('\n', 0, am.start()) + 1
        if 'background-color' not in s[wrap:wrap + 220]:
            bad.append(f'{L(f)} line {ln}: §{num} anchor is not seated in a banner div')
            continue
        # The nearest preceding <div> is NOT necessarily the parent: L06/L07 §5 had a
        # </div> between the banner and the anchor, closing the banner early and leaving
        # the anchor in the content panel. Require the anchor to open IMMEDIATELY inside.
        gap = s[s.find('>', wrap) + 1:s.rfind('<', 0, am.start())]
        if gap.strip():
            bad.append(f'{L(f)} line {ln}: §{num} anchor is not immediately inside its '
                       f'banner — {gap.strip()[:44]!r} intervenes')
            continue
        before = s[:wrap].rstrip()
        if not before.endswith('-->'):
            bad.append(f'{L(f)} line {ln}: §{num} banner is not preceded by a fence '
                       f'(found {before[-40:]!r})')
            continue
        fstart = before.rfind('<!--')
        expect = f'<!-- {_EQ} SECTION {num}: {title} {_EQ} -->'
        if before[fstart:] != expect:
            bad.append(f'{L(f)} line {ln}: §{num} fence is {before[fstart:][:56]!r}, '
                       f'expected {expect[:56]!r}')
    got = [(m.group(1).upper(), m.group(2)) for m in _FENCE.finditer(s)]
    if len(got) != len(want):
        bad.append(f'{L(f)}: {len(got)} canonical fences vs {len(want)} core anchors')
gate('§6.8a section fence generated from the anchor spine, adjacent to a seated anchor', bad)

# ---- §6.8: the PART divider block is GENERATED from the section spine (v8.70, S84)
# Asserts the WHOLE block byte-identically, not just colour and count: the six encoding
# strata found at S84 (bare &, &mdash; vs literal, &ndash;, subtitle opacity 0.7) all
# rendered "fine" and all were drift. Placement is asserted too — L12/L13/L14 shipped
# five banners capping the wrong section, fused to it by border-radius/margin.
_PEQ = '=' * 21
_PART_SPEC = {
    1: ('#3498db', 'Theory &amp; Concepts', 'THEORY & CONCEPTS', '1',
        'Sections 1\u20133: Learn the fundamentals'),
    2: ('#3a7d5c', 'Hardware &amp; Code', 'HARDWARE & CODE', '4',
        'Sections 4\u20136: Set up and program your robot'),
    3: ('#c45d76', 'Testing &amp; Challenges', 'TESTING & CHALLENGES', '7', None),
    4: ('#9b6a9e', 'Challenges', 'CHALLENGES', '9',
        'Section 9: Apply what you have learned'),
}
_ANYPART = re.compile(
    r'<div style="background-color: #[0-9a-fA-F]{6}; color: white; padding: 12px 20px; '
    r'border-radius: 8px 8px 0 0; margin: 22px 0 0;">\s*'
    r'<div style="font-size: 18px[^"]*">PART (\d+)[^<]*</div>\s*'
    r'<div style="font-size: 12px[^"]*">[^<]*</div>\s*</div>')
_DIVCMT = re.compile(r'^PART\s+\d+(?:\s+DIVIDER|\s*:\s*.+)?$', re.I)


def _part_expect(n, has_8a):
    color, title, upper, _sec, sub = _PART_SPEC[n]
    if n == 3:
        sub = ('Sections 7\u20138A: Verify and extend' if has_8a
               else 'Sections 7\u20138: Verify and extend')
    return (
        f'<!-- {_PEQ} PART {n}: {upper} {_PEQ} -->\n'
        f'<div style="background-color: {color}; color: white; padding: 12px 20px; '
        f'border-radius: 8px 8px 0 0; margin: 22px 0 0;">\n'
        f'    <div style="font-size: 18px; font-weight: 500; letter-spacing: 0.5px;">'
        f'PART {n} \u2014 {title}</div>\n'
        f'    <div style="font-size: 12px; color: rgba(255,255,255,0.85); margin-top: 4px;">'
        f'{sub}</div>\n'
        f'</div>\n')


bad, seen_blocks = [], 0
for f in files:
    s = R[f]
    has_8a = 'id="section-8a"' in s
    found = _ANYPART.findall(s)
    seen_blocks += len(found)
    if sorted(int(x) for x in found) != [1, 2, 3, 4]:
        bad.append(f'{L(f)}: PART blocks present are {sorted(found)}, expected 1-4')
        continue
    # Byte-canonicity and placement are checked INDEPENDENTLY. Chaining them (bail on a
    # byte failure, skip the placement check) would let an encoding drift hide a misplaced
    # banner — the S83 lesson that a gate must not be satisfied by the bug it should catch.
    for n in (1, 2, 3, 4):
        blk = _part_expect(n, has_8a)
        c = s.count(blk)
        if c != 1:
            bad.append(f'{L(f)}: PART {n} block+comment is not byte-canonical '
                       f'(exact matches: {c})')
    for m in _ANYPART.finditer(s):
        n = int(m.group(1))
        i = m.end()
        while i < len(s) and s[i] in ' \t\n':
            i += 1
        nxt = re.match(r'<!-- =+ SECTION ([0-9A-Za-z]+):', s[i:i + 120])
        if not nxt:
            bad.append(f'{L(f)}: PART {n} is not followed by a SECTION fence')
        elif nxt.group(1) != _PART_SPEC[n][3]:
            bad.append(f'{L(f)}: PART {n} caps SECTION {nxt.group(1)}, '
                       f'expected SECTION {_PART_SPEC[n][3]}')
    # no stray divider-shaped PART comment outside the four canonical ones
    for m in re.finditer(r'<!--((?:(?!-->).)*?)-->', s, re.S):
        body = m.group(1).strip().strip('=').strip()
        if not re.search(r'\bPART\b', body, re.I) or not _DIVCMT.match(body):
            continue
        if not re.fullmatch(r'PART \d: [A-Z &]+', body):
            bad.append(f'{L(f)}: stray PART divider comment {body!r}')
# COVERAGE — a gate whose population silently empties is an ungated rule (S83)
if seen_blocks != 64:
    bad.append(f'COVERAGE: {seen_blocks} PART blocks scanned book-wide, expected 64')
gate('§6.8  PART divider block generated from the spine, byte-exact and correctly placed', bad)


# ---- §12.2 the repo root carries exactly ONE session handoff (v8.71, S84 batch 2)
# The deletion is the half of a push that a file-overwrite batch cannot carry, and it has
# now been missed twice (fb70426, and again this session). The procedure lived only in the
# session handoff — i.e. in the very file being deleted — so it vanished exactly when needed.
bad = []
_HO = sorted(g for g in glob.glob('ZUMO_S*_HANDOFF.md') if re.fullmatch(r'ZUMO_S\d+_HANDOFF\.md', g))
if len(_HO) != 1:
    bad.append(f'root carries {len(_HO)} session handoffs ({", ".join(_HO) or "none"}), expected 1'
               + ('  — the prior one\'s deletion checkbox was probably not ticked' if len(_HO) > 1 else ''))
_LM = [g for g in glob.glob('ZUMO_LEARNMODE_*_HANDOFF.md')]
if _HO and any(h in _LM for h in _HO):
    bad.append('a §19 learner-mode record was counted as a session handoff')
gate('§12.2 repo root carries exactly one session handoff', bad)

# ---- §25.10h Brain Check family placement (v8.71 — NEW, S84 batch 2, DJ ruling)
# BC01 is a direct child of <body> whose NEXT SIBLING is the banner seating #section-6.
# BC02/03/04 sit one div deep, inside the gray #6c757d §10 content panel.
# Unanimous 9/9 across the converted lessons once S83 lifted L06's BC01 out of §5's panel —
# which is the exact defect this gate exists to catch, and which no gate could see.
# Previous-sibling is deliberately NOT asserted: it legitimately varies (L01/L02 a subsection
# banner, L03 a predict box, L04-L09 §5's green panel).
bad, converted = [], 0
for f in files:
    s = R[f]
    if 'id="brain-check-01"' not in s:
        continue                     # §25.2 governs converted lessons only; L10-L16 pending
    converted += 1
    soup = LI.BeautifulSoup(s, 'html.parser') if hasattr(LI, 'BeautifulSoup') else None
    if soup is None:
        from bs4 import BeautifulSoup as _BS
        soup = _BS(s, 'html.parser')
    for i in ('01', '02', '03', '04'):
        el = soup.find(id=f'brain-check-{i}')
        if el is None:
            bad.append(f'{L(f)}: brain-check-{i} missing')
            continue
        depth = sum(1 for a in el.parents if a.name == 'div')
        if i == '01':
            if depth != 0:
                where = el.parent.get('style', '')[:44] if el.parent else '?'
                bad.append(f'{L(f)}: brain-check-01 is {depth} div(s) deep — it is inside '
                           f'{where!r}, not a child of <body>')
            nxt = el.find_next_sibling()
            seats = nxt.find(id='section-6') if nxt else None
            if seats is None:
                bad.append(f'{L(f)}: brain-check-01 next sibling does not seat #section-6')
        else:
            if depth != 1:
                bad.append(f'{L(f)}: brain-check-{i} is {depth} div(s) deep, expected 1')
            st = el.parent.get('style', '') if el.parent else ''
            if 'border: 2px solid #6c757d' not in st:
                bad.append(f'{L(f)}: brain-check-{i} is not in the gray §10 panel '
                           f'(host style {st[:44]!r})')
if converted != 9:
    bad.append(f'COVERAGE: {converted} converted lessons scanned, expected 9')
gate('§25.10h Brain Check 01 seats above §6 at body level; 02-04 sit in the §10 panel', bad)

BONUS_CAP = ('<div style="background-color: #6c757d; color: white; padding: 13px 18px; '
             'border-radius: 8px 8px 0 0; margin-top: 24px;">')

# ---- §4.5: the bonus-block banner is generated from the three-family table.
# Three families, one mark and one word each. Byte-canonicity and PLACEMENT are asserted
# INDEPENDENTLY (the S84 lesson: an encoding drift must never be able to hide a misplaced
# banner), and the count word is verified against the real card count.
def _bonus_cards(s2, after):
    """Count the cards in a bonus block.  ONE definition, used by gate 30 (is the banner's
    count word true?) and gate 31 (is a HELD lesson still under the family floor?)."""
    g = s2.find('id="glossary"')
    seg = s2[after:g] if g > after else s2[after:]
    tagged = re.findall(r'<h[34][^>]*data-challenge="([^"]*)"', seg)
    bnum = set(re.findall(r'\bB([1-9])\b\s*&mdash;', seg))
    h4 = [x for x in re.findall(r'<h4[^>]*>(.*?)</h4>', seg, re.S)
          if 'Reveal' not in x and 'verbatim' not in x]
    return len(tagged) or len(bnum) or len(h4)


BONUS_MARK = {'practice': '&#128296;', 'observation': '&#128269;',
              'sabotage': '&#128373;&#65039;'}
BONUS_WORD = {'practice': 'Extra Practice', 'observation': 'Observation',
              'sabotage': 'Sabotage'}
BONUS_NUM = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7}
BONUS_TABLE = {
    '02': ('practice', 'Six', 'Code Challenges'),
    '03': ('practice', 'Six', 'Motor Challenges'),
    '04': ('observation', 'Five', 'Sensor Experiments'),
    '05': ('observation', 'Six', 'Proximity Experiments'),
    '06': ('observation', 'Five', 'Encoder Experiments'),
    '07': ('observation', 'Five', 'Multi-File Experiments'),
    '08': ('sabotage', 'Five', 'Line-Following Mysteries'),
    '09': ('sabotage', 'Five', 'State-Machine Mysteries'),
    '10': ('sabotage', 'Five', 'Obstacle Mysteries'),
    '11': ('sabotage', 'Four', 'Gap Mysteries'),
    '12': ('sabotage', 'Four', 'Gyro Mysteries'),
    '13': ('sabotage', 'Four', 'Messed Up Files'),
    '14': ('sabotage', 'Four', 'Messed Up Files'),
    '15': ('sabotage', 'Four', 'Messed Up Files'),
}
BONUS_HELD = {'16'}          # DJ ruling S85: 2 cards, revisit at 4.
NAVSIG = 'text-decoration: none; padding: 5px 12px'
bad = []
seen = 0
for f in files:
    lg, s2 = L(f), R[f]
    if lg not in BONUS_TABLE:
        if lg in BONUS_HELD and 'id="bonus-challenges"' in s2:
            continue
        if 'id="bonus-challenges"' in s2:
            bad.append(f'{lg}: has a bonus block but is not in the family table')
        continue
    seen += 1
    fam, count, noun = BONUS_TABLE[lg]

    # (a) byte-canonicity of the banner block
    want = ('<div id="bonus-challenges" style="font-size: 1.15em; font-weight: bold;">'
            f'{BONUS_MARK[fam]} {BONUS_WORD[fam]}: {count} {noun}</div>')
    m = re.search(r'<div id="bonus-challenges".*?</div>', s2, re.S)
    if not m:
        bad.append(f'{lg}: no bonus banner div')
        continue
    if m.group(0) != want:
        bad.append(f'{lg}: banner not byte-canonical\n           got  {m.group(0)}'
                   f'\n           want {want}')

    # (b) PLACEMENT, asserted independently of the bytes above.
    #     The cap is compared BYTE-EXACT, not by substring: a
    #     `background: linear-gradient(135deg, #6c757d, #4d5358)` cap CONTAINS
    #     '#6c757d' and passed the old substring test for its whole life (L03,
    #     found S87).  A substring test cannot distinguish flat from gradient.
    cap = s2.rfind('<div', 0, m.start())
    capopen = s2[cap:s2.find('>', cap) + 1]
    if capopen != BONUS_CAP:
        bad.append(f'{lg}: bonus cap div not byte-canonical\n           got  {capopen}'
                   f'\n           want {BONUS_CAP}')
    after = s2[m.end():m.end() + 260]
    if not re.match(r'\s*</div>\s*<div style="border: 2px solid #6c757d', after):
        bad.append(f'{lg}: gray cap is not fused to the bordered bonus panel')

    # (c) the count word is true
    real = _bonus_cards(s2, m.end())
    if real != BONUS_NUM[count]:
        bad.append(f'{lg}: banner claims {count} ({BONUS_NUM[count]}) '
                   f'but the block holds {real} cards')

    # (d) no stray or doubled mark, and the retired label is gone
    inner = m.group(0)[m.group(0).find('>') + 1:-6]
    for stray in ['\U0001f528', '\U0001f50d', '\U0001f9e9', '\U0001f575']:
        if stray in inner:
            bad.append(f'{lg}: raw UTF-8 mark survived in the banner')
    if inner.count('&#128373;') > 1 or inner.count('&#128296;') > 1:
        bad.append(f'{lg}: banner mark is doubled')
    if 'Bonus' in inner:
        bad.append(f'{lg}: banner still carries the retired label "Bonus"')

    # (e) the nav pill carries the family word
    navs = [mm for mm in re.finditer(r'<a href="#bonus-challenges"([^>]*)>([^<]*)</a>', s2)
            if NAVSIG in mm.group(1)]
    if len(navs) != 1:
        bad.append(f'{lg}: expected exactly 1 bonus nav pill, found {len(navs)}')
    elif navs[0].group(2) != BONUS_WORD[fam]:
        bad.append(f'{lg}: nav pill reads {navs[0].group(2)!r}, '
                   f'expected {BONUS_WORD[fam]!r}')
if seen != 14:
    bad.append(f'COVERAGE: {seen} lessons scanned against the family table, expected 14')
gate('\u00a74.5  bonus banner generated from the three-family table, placement asserted', bad)

# ---- §4.2 COVERAGE: every bonus card is tagged, and its kind names its family.
# Gate 4 asserts markers are UNIQUE, never PRESENT -- which is why 28 untagged cards
# sat inside a 30/30 book for a year.  This gate rides gate 30's already-verified card
# count: the banner count is true, so the tagged count must equal it.
BONUS_KIND = {'practice': 'bonus-practice', 'observation': 'bonus-observation',
              'sabotage': 'bonus-sabotage'}
bad = []
seen = 0
for f in files:
    lg, s2 = L(f), R[f]
    if lg not in BONUS_TABLE:
        # A held lesson is skipped BY NAME, never absorbed by COVERAGE -- and the hold
        # expires by itself: DJ's S85 ruling was "revisit when it has four cards", so
        # reaching the floor is what makes this gate speak up.
        if lg in BONUS_HELD and 'id="bonus-challenges"' in s2:
            mh = re.search(r'<div id="bonus-challenges".*?</div>', s2, re.S)
            held = _bonus_cards(s2, mh.end()) if mh else 0
            if held >= 4:
                bad.append(f'{lg}: HELD out of the family by the S85 ruling at 2 cards, '
                           f'but it now holds {held} -- the floor is 4, so bring it into '
                           f'§4.5 (banner, pill, tagging) or re-rule the hold')
            continue
        if 'id="bonus-challenges"' in s2:
            bad.append(f'{lg}: has a bonus block but is neither in the family table '
                       f'nor held')
        continue
    seen += 1
    fam, count, _ = BONUS_TABLE[lg]
    m = re.search(r'<div id="bonus-challenges".*?</div>', s2, re.S)
    if not m:
        continue
    g = s2.find('id="glossary"')
    seg = s2[m.end():g] if g > m.end() else s2[m.end():]
    want = BONUS_KIND[fam]
    marked = re.findall(r'data-challenge="([^"]*)"', seg)
    kinds = re.findall(r'data-kind="([^"]*)"', seg)
    if len(marked) != BONUS_NUM[count]:
        bad.append(f'{lg}: banner says {BONUS_NUM[count]} cards but only {len(marked)} '
                   f'carry data-challenge -- an untagged card is invisible to the picker (§20.2)')
    if len(kinds) != BONUS_NUM[count]:
        bad.append(f'{lg}: {len(kinds)} data-kind in the block, expected {BONUS_NUM[count]}')
    off = sorted(set(k for k in kinds if k != want))
    if off:
        bad.append(f'{lg}: block is family {fam!r}, expected every card {want!r}, '
                   f'found {off}')
if seen != 14:
    bad.append(f'COVERAGE: {seen} lessons scanned, expected 14')
gate('\u00a74.2  every bonus card is tagged and its data-kind names its family', bad)


# ---- §4.5a: every bonus block is announced in the flow of the lesson.
#      Before S87 the FINISHED EARLY pointer existed in L02-L09 and was ABSENT in
#      L10-L15, so in six lessons the only route into the bonus block was one nav
#      pill among twelve to fourteen.  The livery had also drifted into three
#      strata (2/2/4) that cut across the families rather than along them.
#      Byte-canonical, like the cap: a substring test cannot see a drift.
FE_BOX = ('<div style="background-color: #f8f9fa; border: 2px solid #6c757d; '
          'border-radius: 10px; padding: 15px 20px; margin: 25px 0;">')
bad = []
seen = 0
for f in files:
    lg, s2 = L(f), R[f]
    if lg not in BONUS_TABLE:
        continue
    seen += 1
    n = s2.upper().count('FINISHED EARLY')
    if n != 1:
        bad.append(f'{lg}: expected exactly 1 FINISHED EARLY pointer, found {n}')
        continue
    i = s2.upper().find('FINISHED EARLY')
    st = s2.rfind('<div', 0, i)
    box = s2[st:s2.find('>', st) + 1]
    if box != FE_BOX:
        bad.append(f'{lg}: FINISHED EARLY box not byte-canonical\n           got  {box}'
                   f'\n           want {FE_BOX}')
    b = s2.find('id="bonus-challenges"')
    if b < 0 or st > b:
        bad.append(f'{lg}: FINISHED EARLY pointer does not precede the bonus block')
    seg = s2[st:s2.find('</div>', i) + 6]
    if 'href="#bonus-challenges"' not in seg:
        bad.append(f'{lg}: FINISHED EARLY pointer carries no link to the bonus block')
if seen != 14:
    bad.append(f'COVERAGE: {seen} lessons checked for the pointer, expected 14')
gate('\u00a74.5a every bonus block is announced by a canonical FINISHED EARLY pointer', bad)

# ---- §5.1 CALLOUT GEOMETRY, AGAINST A FROZEN BASELINE (v1.22 — NEW, S91, DJ ruling)
# ---- The standard fixes the callout rule at `border-left: 4px solid`. 115 live blocks are
# ---- off it — 112 at 5px, 3 at 3px — and 83 of those sit in L11/L12, authored entirely in a
# ---- second design system. Shipping this ABSOLUTE would fail every run until the repaint,
# ---- and the repaint is blocked on an unapproved semantic palette: a gate that cries wolf
# ---- gets ignored (S90), and it would drag the other 32 down with it.
# ---- So the existing debt is FROZEN as a baseline and anything NEW fails. This is NOT the
# ---- S82 "widen the matcher" move DJ ruled against — widening would accept 5px forever and
# ---- everywhere. A baseline names the debt that exists, rejects the 116th block, and is
# ---- built to go to ZERO at the repaint, at which point the baseline empties and the gate
# ---- becomes absolute. Signatures are (lesson, px, border, bg) so they survive line shifts.
# ---- Note not all 115 are drift: `#1a5276`/`#f8f9fa` is one block per lesson in L01-L11 and
# ---- `#6c757d`/`#f8f9fa` one per lesson in L12-L16 — uniform constructs that happen to be
# ---- 5px. Geometry is read through lesson_inventory's parser (§24.10), never a regex here.
GEOM_BASELINE = {
    ('01', 5, '#1a5276', '#f8f9fa'): 1,
    ('02', 3, '#fbc02d', '#fffde7'): 2,
    ('02', 5, '#1a5276', '#f8f9fa'): 1,
    ('03', 5, '#1a5276', '#f8f9fa'): 1,
    ('03', 5, '#2e86ab', '#f4f9fc'): 1,
    ('03', 5, '#ffc107', '#fff8e1'): 1,
    ('04', 5, '#1a5276', '#f8f9fa'): 1,
    ('05', 5, '#1a5276', '#f8f9fa'): 1,
    ('05', 5, '#607d8b', '#eceff1'): 1,
    ('05', 5, '#ffc107', '#fff8e1'): 1,
    ('06', 5, '#1a5276', '#f8f9fa'): 1,
    ('06', 5, '#c0392b', '#fdecea'): 1,
    ('07', 5, '#1a5276', '#f8f9fa'): 1,
    ('08', 5, '#1a5276', '#f8f9fa'): 1,
    ('09', 5, '#1a5276', '#f8f9fa'): 1,
    ('10', 5, '#1a5276', '#f8f9fa'): 1,
    ('11', 3, '#ccc', None): 1,
    ('11', 5, '#1a5276', '#f8f9fa'): 1,
    ('11', 5, '#27ae60', '#eafaf1'): 6,
    ('11', 5, '#607d8b', '#eceff1'): 7,
    ('11', 5, '#6b8e6b', '#f0f7f0'): 3,
    ('11', 5, '#e74c3c', '#fdecea'): 5,
    ('12', 5, '#27ae60', '#eafaf1'): 13,
    ('12', 5, '#607d8b', '#eceff1'): 20,
    ('12', 5, '#6b8e6b', '#f0f7f0'): 8,
    ('12', 5, '#6c757d', '#f5eef8'): 4,
    ('12', 5, '#6c757d', '#f8f9fa'): 1,
    ('12', 5, '#e74c3c', '#fdecea'): 13,
    ('12', 5, '#ffc107', '#fff8e1'): 1,
    ('13', 5, '#6c757d', '#f8f9fa'): 1,
    ('14', 5, '#6c757d', '#f8f9fa'): 1,
    ('15', 5, '#2e86ab', '#f4f9fc'): 3,
    ('15', 5, '#3a7d5c', '#eef7f1'): 1,
    ('15', 5, '#6c757d', '#f8f9fa'): 1,
    ('16', 5, '#3a7d5c', '#eef7f1'): 5,
    ('16', 5, '#6c757d', '#f8f9fa'): 1,
    ('16', 5, '#ffc107', '#fff8e1'): 1,
}
bad = []
seen_lessons = set()
live = collections.Counter()
for f in sorted(glob.glob('lessons/Lesson_*.html')):
    inv = LI.build(f)
    seen_lessons.add(inv['lesson'])
    if not inv['callouts']:
        bad.append(f'L{inv["lesson"]}: parser returned ZERO callouts — coverage defect')
    for c in inv['callouts']:
        if c['px'] != 4:
            live[(inv['lesson'], c['px'], c['border'], c['bg'])] += 1
for sig, cnt in sorted(live.items()):
    allowed = GEOM_BASELINE.get(sig, 0)
    if cnt > allowed:
        bad.append(f'L{sig[0]}: {cnt - allowed} NEW off-canon block(s) at {sig[1]}px '
                   f'border {sig[2]} bg {sig[3]} (baseline {allowed}, found {cnt})')
if len(seen_lessons) != 16:
    bad.append(f'COVERAGE: {len(seen_lessons)} lessons parsed, expected 16')
_shrunk = sum(GEOM_BASELINE.values()) - sum(live.values())
gate('\u00a75.1 callout geometry: no NEW off-canon border width'
     + (f' (debt {sum(live.values())}/{sum(GEOM_BASELINE.values())}, '
        f'{_shrunk} retired — tighten the baseline)' if _shrunk > 0
        else f' (frozen debt {sum(live.values())}, zero at the repaint)'), bad)

# ---- §5.1 THE CALLOUT TITLE IS A BLOCK ELEMENT, ONE FORM BOOK-WIDE (NEW, S91, DJ ruling)
# ---- DJ: "Why would i want a div bold?" -- the answer is §5.1's three properties, which a
# ---- bare <strong> carries none of: margin-bottom 8px, font-size 1.05em, and block display
# ---- so the body needs no <br>. The live book had it backwards: 794 titles were <strong>
# ---- against 55 in §5.1's form, while §5.1 claimed "Geometry is unchanged from prior
# ---- practice." Swept S91 -- 794 converted, 119 now-redundant <br> removed.
# ---- Recorded so nobody reverts it: <strong> is SEMANTIC and a bold div is not, so this
# ---- costs the emphasis cue on 794 titles. The title is still the first text in the block,
# ---- so nothing became unreachable. DJ ruled the div for consistency; §5.1 records the cost.
bad = []
seen = 0
for f in sorted(glob.glob('lessons/Lesson_*.html')):
    src = R[f]
    lines = src.split('\n')
    for c in LI.build(f)['callouts']:
        off = sum(len(l) + 1 for l in lines[:c['line'] - 1])
        # v1.26.3: anchor on the callout's OWN opening tag, not the first '>' after the line
        # start. L14's THE ONE IDEA shares its line with the </div> that closes the block
        # above it, so find('>') landed on THAT tag, the check ran one element late, and a
        # bare <strong> title passed unseen. c['tag'] names the element; search for it.
        _open = src.find('<' + c['tag'], off)
        gt = src.find('>', _open) if _open >= 0 else src.find('>', off)
        if gt < 0:
            continue
        seen += 1
        i = re.match(r'\s*', src[gt + 1:]).end() + gt + 1
        # S91 second pass: the first version rejected only a bare <strong>, so 120 <span>-led
        # and 44 <b> titles walked straight through -- the same construct in three shapes.
        # A <b> that is NOT followed by <br> or a block element is a sentence SUBJECT, not a
        # title, and must be left alone; 22 of those are legitimate.
        if src.startswith('<strong', i) or src.startswith('<span', i):
            bad.append(f'{L(f)} line {c["line"]}: callout title is inline, \u00a75.1 requires '
                       f'the block form')
        elif re.match(r'<b\b(?![a-z])', src[i:]):
            m = re.match(r'<b\b(?![a-z])[^>]*>.*?</b>', src[i:], re.S)
            if m and re.match(r'\s*(?:<br|<p\b|<ul\b|<ol\b|<div\b|<h[1-6]\b)', src[i + m.end():]):
                bad.append(f'{L(f)} line {c["line"]}: callout title is <b>, \u00a75.1 requires '
                           f'the block form')
if seen < 900:
    bad.append(f'COVERAGE: only {seen} callouts inspected, expected 1000+')
gate('\u00a75.1 callout title uses the block form, never a bare <strong>', bad)

# ---- §5.1 OPTION C: THE LABEL ELEMENT HOLDS THE FAMILY WORD AND NOTHING ELSE (NEW, S92)
# ---- DJ ruling. The whole return on Option C is that a block's family is readable by EXACT
# ---- MATCH instead of by parsing a family word off the front of authored prose -- which is
# ---- what made the amber scheme unclassifiable at S91 (one scheme, six jobs). This gate is
# ---- what makes that guarantee real; without it the label silently reacquires prose.
# ---- Censused before writing, per S91's lesson that gate 34 covered one shape of three:
# ---- the live shapes are (a) label alone, 72 blocks, and (b) label + title, 178 blocks.
# ---- Scope is the (bg, border) scheme, NOT the glyph -- the scheme is the family of record
# ---- (S92 ruling), and 3 blocks on non-canonical schemes are deliberately OUT of scope and
# ---- logged for the family-table batch, so a COVERAGE assert pins the count at 250.
_SCHEME = {('#f0f7f0', '#6b8e6b'): 'TIP',
           ('#eceff1', '#607d8b'): 'NOTE',
           ('#fff8e1', '#ffc107'): 'WARNING'}
_FAMGLYPH = {'TIP': '\U0001F4A1', 'NOTE': '\U0001F4D8', 'WARNING': '\u26A0'}
bad = []
seen = 0
for f in sorted(glob.glob('lessons/Lesson_*.html')):
    src = R[f]
    lines = src.split('\n')
    for c in LI.build(f)['callouts']:
        fam = _SCHEME.get((c['bg'], c['border']))
        if fam is None or c['glyph'] not in _FAMGLYPH.values():
            # S92: scope is blocks where GLYPH AND SCHEME AGREE. The scheme alone is NOT the
            # family of record -- 24 blocks borrow §6.6a paint while carrying another
            # family's glyph (7x the going_deeper hook, 7x DO THIS NOW, 2x WHAT YOU NEED,
            # 8 one-offs). Asserting scheme-as-family would require breaking the rule 24
            # times, so the gate holds the agreeing set and the 24 are logged for the
            # family-table batch. The earlier ruling was tested only on blocks that COULD
            # NOT disagree; an assert that cannot fail is not evidence.
            continue
        off = sum(len(l) + 1 for l in lines[:c['line'] - 1])
        # v1.26.3: anchor on the callout's OWN opening tag, not the first '>' after the line
        # start. L14's THE ONE IDEA shares its line with the </div> that closes the block
        # above it, so find('>') landed on THAT tag, the check ran one element late, and a
        # bare <strong> title passed unseen. c['tag'] names the element; search for it.
        _open = src.find('<' + c['tag'], off)
        gt = src.find('>', _open) if _open >= 0 else src.find('>', off)
        if gt < 0:
            continue
        i = re.match(r'\s*', src[gt + 1:]).end() + gt + 1
        m = re.match(r'<div\b[^>]*>(.*?)</div>', src[i:], re.S)
        if not m:
            continue          # titleless / sentence-lead <b>; gate 34 owns those
        seen += 1
        # unescape: glyphs are numeric entities in some lessons (L11/L12), and a matcher that
        # forgets that reports every entity-encoded block as broken. S92 hit this exact bug.
        label = re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', '', m.group(1)))).strip()
        want = _FAMGLYPH[fam]
        if not label.startswith(want):
            bad.append(f'{L(f)} line {c["line"]}: label glyph disagrees with the '
                       f'{fam} scheme, \u00a75.1')
            continue
        rest = label[len(want):].lstrip('\ufe0f').strip()
        if rest != fam:
            bad.append(f'{L(f)} line {c["line"]}: label carries {rest[:40]!r}, '
                       f'\u00a75.1 requires exactly {fam!r}')
if seen != 251:
    bad.append(f'COVERAGE: {seen} labels inspected, expected 251 '
               f'(3 off-canon blocks are out of scope by ruling)')
gate('\u00a75.1 callout label holds exactly the family word, matched to its scheme', bad)


# ---------------------------------------------------------------- gate 36 (S97)
# Every image reference resolves to a file on disk.
# Two reference forms occur in the book, surveyed not assumed: 193 absolute site URLs
# and 23 relative (favicon). A THIRD form appearing later would be invisible to this
# matcher, so the resolved-count assert below is what makes that hole loud instead of
# silent — if a page starts writing refs some other way, the count moves and the gate
# says so. An assert that cannot fail is not evidence.
_SITE_PREFIX = 'https://weymuth.github.io/zumo/'
_REF_RE = re.compile(
    r'(?:src|href|xlink:href)\s*=\s*["\']([^"\']+?\.(?:png|jpe?g|svg|gif|webp|ico))'
    r'(?:[?#][^"\']*)?["\']', re.I)
from urllib.parse import unquote as _unquote

bad, _seen = [], 0
_REFERENCED = set()          # consumed by gate 37; built here so there is ONE resolver
for _page in site:
    if not os.path.exists(_page):
        continue
    _src = open(_page, encoding='utf-8', errors='replace').read()
    for _m in _REF_RE.finditer(_src):
        _u = _m.group(1)
        if _u.startswith(_SITE_PREFIX):
            _p = _unquote(_u[len(_SITE_PREFIX):])
        elif _u.startswith(('http://', 'https://', 'data:', '//')):
            continue                       # off-site, not ours to resolve
        elif _u.startswith('/'):
            _p = _unquote(_u.lstrip('/'))
        else:
            _p = os.path.normpath(os.path.join(os.path.dirname(_page), _unquote(_u)))
        _seen += 1
        _REFERENCED.add(_p.replace(os.sep, '/'))
        if not os.path.isfile(_p):
            _ln = _src.count('\n', 0, _m.start()) + 1
            # L() is the fixed slice f[15:17] and is meaningful ONLY for
            # lessons/Lesson_NN.html; on index.html it returns ''. A gate that
            # reports a defect it cannot name is half a gate. Caught by the S97
            # scope control, which seeded breaks into the non-lesson pages.
            _who = L(_page) if _page in files else _page
            bad.append(f'{_who} line {_ln}: image reference -> {_p} does not exist')
if _seen != 216:
    bad.append(f'COVERAGE: {_seen} image references resolved, expected 216 — a reference '
               f'was added, removed, or written in a form this gate cannot see')
gate('\u00a721   every image reference resolves to a file on disk', bad)


# ---------------------------------------------------------------- gate 37 (S97, rewritten S98)
# §21.1 was "no REFERENCED .svg carries an embedded raster", and that rule was WRONG —
# it forbade an asset class this book needs. Measured in S98: every one of the five staged
# raster-in-SVG files carries PHOTOGRAPHIC content (top-50 colours cover 9–48% of pixels),
# and the one true-vector redraw of a board (…_top_view_r02.svg, 194 elements, zero raster)
# turned out to be a CARTOON — its 39 text runs are the silkscreen, not labels. A photograph
# of a populated PCB cannot be redrawn, and DJ's ruling is that these stay raster.
#   They must also EMBED. An SVG loaded through <img src> runs in secure static mode and
# cannot fetch an external file, so photo-plus-crisp-vector-labels in one file has no
# external-href option. A gate forbidding base64 forbids the composite itself.
#
# What S97 actually found was not "a raster" but THREE separable defects, and this gate now
# names each one. Every threshold below comes from measurement, not taste:
#   DUP     one <image> carrying the payload TWICE, href= and xlink:href= both holding the
#           full base64. Not two layers — identical bytes, one drawn image, double the file.
#           Free to fix, invisible on screen, present in 2 of 5 staged files.
#   CEILING the student-facing cost. fit_raster_svg.py takes the uploaded board photo from
#           4,262,718 B to 350,471 B with no visible change, so a real composite lands well
#           under this; 500,000 B leaves room without licensing a megabyte.
#   FLOOR   the S97 defect proper: the memory ladder had ZERO drawing elements — a bitmap in
#           an envelope, 4.9 MB, claiming to be a diagram. A composite has labels on it. A
#           file with a raster and almost no vector is a PHOTOGRAPH and belongs at .jpg/.png
#           under the IMAGE_ name, which is already this book's convention (IMAGE = photo,
#           GRAPHIC = drawn).
# Scoping is unchanged and deliberate: fatal for REFERENCED files, counted for staged ones.
CEILING = 500_000
FLOOR = 3
_svgs = sorted(f.replace(os.sep, '/') for f in glob.glob('images/**/*.svg', recursive=True))
_staged, bad = [], []
for _f in _svgs:
    _s = open(_f, encoding='utf-8', errors='replace').read()
    if 'base64' not in _s:
        continue
    _sz = os.path.getsize(_f)
    _draw = len(re.findall(r'<(?:path|rect|text|circle|line|polygon|polyline|ellipse)\b', _s))
    _faults = []
    for _tag in re.findall(r'<image\b[^>]*>', _s):
        _uris = re.findall(r'href="(data:image/[a-z]+;base64,[^"]*)"', _tag)
        if len(_uris) > 1 and len(set(_uris)) == 1:
            _faults.append('payload stored twice in one <image> (href and xlink:href) — '
                           'half this file is a duplicate of itself')
            break
    if _sz > CEILING:
        _faults.append(f'{_sz:,} B, over the {CEILING:,} B ceiling — run fit_raster_svg.py')
    if _draw < FLOOR:
        _faults.append(f'{_draw} drawing element(s): this is a photograph, not a graphic — '
                       f'ship it as .jpg/.png under an IMAGE_ name')
    if not _faults:
        continue
    _msg = f'{_f}: ' + '; '.join(_faults)
    (bad if _f in _REFERENCED else _staged).append(_msg)
gate('\u00a721.1 embedded rasters are deduped, under the ceiling, and carry vector content', bad)
if _staged:
    print(f'         note: {len(_staged)} unreferenced .svg would fail this gate if wired in '
          f'(staged, not fatal)')
    for _m in _staged:
        print(f'           - {_m}')


# ---------------------------------------------------------------- gate 38 (S98)
# §21.2 A DRAWN GRAPHIC KEEPS ITS TEXT AND STAYS SMALL.
# Written for a defect that was LIVE for a week and passed 37/37 every run. Four referenced
# graphics — L06 6-09, 6-10, 6-12 and L07 7-02 — came back from a redo with every label
# converted to OUTLINES: 23,066 B -> 1,148,110 B, a 50x growth and +1.13 MB on the published
# site. One of them rode in on 09a33f8, the same commit that carried the gate suite's own
# update, and post-push verification missed it because it byte-matched the files on the push
# list and never diffed the rest of the tree.
#   The cause is defensible: a graphic drawn in Inter or JetBrains Mono renders wrong on a
# student's machine, and outlining is a real fix for that. It is the WRONG fix — the cheap one
# is a common font stack, and all five files came back at 6–11 KB with 32–42 LIVE labels once
# asked for Arial/Courier New. Outlined text is also unselectable, unsearchable and invisible
# to a screen reader, which is the same objection §17.3 raises against prose baked into pixels.
#
# Gate 37 owns the files that CONTAIN a raster. This gate owns the complement: true vector.
# Three checks, every threshold measured against the whole book this session, none inherited:
#   CEILING   60,000 B. The largest true-vector file in the book is the Mercersburg wordmark
#             at 12,904 B and the largest GRAPHIC_ is 10,943 B, so this sits 4.6x above
#             anything legitimate and 3.5x below the smaller of the two real defects
#             (209,178 B and 319,014 B, restored from 0b3f070^ and used as control A).
#   LABELS    a file named GRAPHIC_ carries at least one <text>. Measured: 83 GRAPHIC_ vector
#             files, ZERO of them text-less, minimum label count 7. The two legitimate
#             text-less families need no exemption because neither is named GRAPHIC_ — the
#             wordmark is a logo and the §18.2 spiral stars carry vector-path digits BY RULING.
#   OUTLINED  zero <text> AND more than 50,000 B of path data, for anything NOT named GRAPHIC_
#             — the same defect arriving under a different filename. The largest legitimate
#             text-less path payload in the book is the wordmark's 11,173 B (next: 2,396 B, an
#             icon; the stars are all under 962 B); the defect files carry 197,247 B and
#             304,159 B. The line sits 4.5x above the first and 3.9x below the second.
#
# Scoping mirrors gate 37 and for the same reason: fatal on files a page REFERENCES, counted
# and printed for staged ones. Raw exports land in images/ before being wired up, and a gate
# that reddens on work-in-progress is a gate people learn to ignore.
VEC_CEILING = 60_000
OUTLINE_PD = 50_000
# GRAPHIC_PD closes a hole in v1.31 found by re-deriving that gate's own findings on a second
# and third parser (S99). The label check above is a FLOOR OF ONE, so a graphic with 26 of its
# 27 labels outlined and one left live satisfied it: measured, that file sat at 19,225 B with
# 15,730 B of path data and passed the whole suite green. Threshold from arithmetic, not taste —
# outlining a SINGLE label cost 5,190 B (L06 6-09, 38 labels) and 9,216 B (L07 7-02, 33 labels)
# on the two real S98 defect files, while the largest path payload on any legitimate drawn
# graphic in the book is 960 B and 55 of the 83 carry exactly zero. 5,000 B therefore sits 5.2x
# above anything legitimate and still fires on the outlining of one label.
#   The cost is stated: a future graphic built from genuinely path-heavy vector art — curved
# arrows, traced silhouettes — could reach this honestly. That is a threshold to RAISE with a
# measurement, not a reason to leave partial outlining ungated.
GRAPHIC_PD = 5_000
_vec, _staged38, bad = [], [], []
for _f in _svgs:                              # same population gate 37 walked, complemented
    _s = open(_f, encoding='utf-8', errors='replace').read()
    if 'base64' in _s:
        continue                              # gate 37's file, not this one's
    _vec.append(_f)
    _base = os.path.basename(_f)
    _isg = 'GRAPHIC_' in _base
    _sz = os.path.getsize(_f)
    _ntext = len(re.findall(r'<text\b', _s))
    _pd = sum(len(_m) for _m in re.findall(r'\bd\s*=\s*"([^"]*)"', _s))
    _faults = []
    if _sz > VEC_CEILING:
        _faults.append(f'{_sz:,} B, over the {VEC_CEILING:,} B ceiling for a drawn graphic '
                       f'(largest legitimate in the book is 12,904 B)')
    if _isg and _ntext == 0:
        _faults.append('named GRAPHIC_ but carries zero <text>: its labels have been converted '
                       'to outlines — re-export with live text in a common stack '
                       '(Arial / Courier New), per Bible §17.3a recipe 1')
    if _isg and _pd > GRAPHIC_PD:
        _faults.append(f'{_pd:,} B of path data on a drawn graphic, over the {GRAPHIC_PD:,} B '
                       f'ceiling: labels appear to be outlined. The >=1 <text> floor above is '
                       f'satisfied by a SINGLE surviving label, so it does not catch partial '
                       f'outlining — this check is the half that does')
    if not _isg and _ntext == 0 and _pd > OUTLINE_PD:
        _faults.append(f'zero <text> over {_pd:,} B of path data — this looks like outlined '
                       f'text under a non-GRAPHIC_ name')
    if not _faults:
        continue
    _msg = f'{_f}: ' + '; '.join(_faults)
    (bad if _f in _REFERENCED else _staged38).append(_msg)

# COVERAGE. An assert that cannot fail is not evidence (§24.6b): if the glob breaks, the
# population empties and every check above passes vacuously. Both numbers are STATED, not
# inherited, and both are expected to move when a graphic is added or removed — bump them
# in the same edit, the way gate 36's reference count is maintained.
if len(_vec) != 196:
    bad.append(f'COVERAGE: {len(_vec)} true-vector .svg walked, expected 196 — a file was '
               f'added, removed, or now carries a raster (which moves it to gate 37)')
_ngraphic = sum(1 for _f in _vec if 'GRAPHIC_' in os.path.basename(_f))
if _ngraphic != 85:
    bad.append(f'COVERAGE: {_ngraphic} GRAPHIC_ vector files walked, expected 85 — the label '
               f'check is the one that binds on every one of them, so this number is load-bearing')
gate('\u00a721.2 drawn graphics keep live text and stay under the ceiling', bad)
if _staged38:
    print(f'         note: {len(_staged38)} unreferenced .svg would fail this gate if wired in '
          f'(staged, not fatal)')
    for _m in _staged38:
        print(f'           - {_m}')


print('=' * 52)



if FAIL:
    print(f'{len(FAIL)} GATE(S) FAILED: {", ".join(FAIL)}')
    sys.exit(1)
print('ALL GATES PASS')
