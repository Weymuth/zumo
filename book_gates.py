#!/usr/bin/env python3
# book_gates.py v1.15 (S84) — whole-book consistency gates.
# Usage:  python3 book_gates.py            (run from repo root)
# Exit 0 = all gates pass. Exit 1 = failures listed.
#
# Run at SESSION OPEN (health check) and before EVERY delivery (close gate).
# Each gate encodes a Bible rule; the Bible section is named on each line.
# When a new rule is canonized, add its gate here in the same session.

import re, glob, html, os, sys, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
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


R = {f: open(f, encoding='utf-8').read() for f in site}

# ---- §5b: hidden full version present; both visible banners carry its major.minor
bad = []
for f in files:
    s = R[f]
    hid = re.search(r'v(\d+\.\d+)\.\d+', s[:60])
    vis = re.findall(r'Version (\d+\.\d+)', s)
    if not hid or len(vis) != 2 or any(v != hid.group(1) for v in vis):
        bad.append(f'{L(f)}: hidden={hid.group(1) if hid else None} visible={vis}')
gate('§5b  version: hidden == both visible banners', bad)

# ---- §5b addendum (S65): where BOTH banners carry a date, the dates must agree.
# (L11–L16 footers carry no date by design — that is legal.)
bad = []
for f in files:
    d = re.findall(r'Version \d+\.\d+(?: &mdash;| —) (\w+ \d{4})', R[f])
    if len(d) >= 2 and len(set(d)) != 1:
        bad.append(f'{L(f)}: {d}')
    if len(d) == 0:
        bad.append(f'{L(f)}: no dated banner at all')
gate('§5b  date: dates agree where both banners carry one', bad)

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
bad = []
for f in site:
    s = R[f]
    for tag in ['div', 'pre', 'details', 'table', 'iframe', 'strong', 'h3']:
        o = len(re.findall(f'<{tag}\\b', s))
        c = s.count(f'</{tag}>')
        if o != c:
            bad.append(f'{f}: {tag} {o}/{c}')
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

# ---- §25.6: header hero + footer + hidden build banner, identical across all 17 pages
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
    if 'BUILD BANNER' not in s2 or 'ZUMO Callout Standard' not in s2:
        bad.append(f'{f}: no hidden build banner')
if len(heroes) > 1:
    bad.append(f'hero skeletons differ: { {k: [L(x) for x in v] for k, v in heroes.items()} }')
if len(footers) > 1:
    bad.append(f'footer skeletons differ: { {k: [L(x) for x in v] for k, v in footers.items()} }')
gate('§25.6 header/footer/hidden banner identical across all 17', bad)

# ---- §25.2: where a lesson has converted to the four exit blocks, it must conform
RETIRED = ['STOP &amp; PROCESS', 'Conceptual Understanding',
           'Check Your Understanding', 'Reflection Questions',
           'Explain It in Writing']
bad = []
for f in files:
    s2 = R[f]
    if 'MENTAL KNOWLEDGE CHECK' not in s2:
        continue                      # not yet converted — §25 does not bind it
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
        mystery = c['kind'] == 'mystery'
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

print('=' * 52)

if FAIL:
    print(f'{len(FAIL)} GATE(S) FAILED: {", ".join(FAIL)}')
    sys.exit(1)
print('ALL GATES PASS')
