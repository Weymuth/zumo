#!/usr/bin/env python3
"""byte_audit.py — the only instrument in this repo that COMPILES.

Rule 33: no instrument reads prose, and none compiles either. S148 shipped a
Lesson 16 whose finished build could not be flashed while seventy gates and
gate_payload_match were green. This closes that hole.

It cannot live in book_gates.py: it needs the AVR toolchain, which a normal
session does not have. Run it whenever the harness is up.

  ARM 1  CEILING     compile EVERY payload the Maker defines. OVER or a compile
                     error is a hard failure. No parsing, no mapping, no
                     inference — this is the arm that would have caught L16.
  ARM 2  FIGURES     every byte figure a lesson promises for a build (step
                     headings and COMPILE CHECK callouts) must equal the
                     compiled size of a payload of that lesson.
  ARM 4  LABELS      every byte figure in a Maker KINDS label must equal the
                     compiled size of the payload that row points at. Nothing
                     else in this repo reads a label. S152 found all five
                     stale, each agreeing with its own arithmetic (rule 51).
  ARM 3  CONVENTION  measure, per lesson, whether the catch-up link under
                     Step N serves the file as it stands AT step N (IDENTITY)
                     or BEFORE it (OFFSET). A measurement, not a verdict.
  ARM 8  WARNINGS    report the whole compiler-warning population; ASSERT it
                     only in `finished` builds, where the build-up model cannot
                     explain a warning away. Arrived with the harness release
                     that stopped compiling with -w.
                     (No version token above this file's own VERSION home —
                      grep_trap caught exactly that here in S170.)

The step -> payload association is PARSED from the lesson's own catch-up link
(?lesson=N&kind=K), never typed into this script (rules 48, 49).

Usage:
  byte_audit.py --selftest            controls, both directions
  byte_audit.py --sizes               build/refresh the size table
  byte_audit.py --check               ARM 1 + ARM 2   (exit 1 on failure)
  byte_audit.py --discards            ARM 9 only - recompiles 105 payloads with
                                      warn_unused_result INJECTED AT STAGE TIME.
                                      Minutes, so it is deliberately NOT in --check.
  byte_audit.py --convention          ARM 3 report    (no exit code)
  byte_audit.py --lesson N            one lesson, all arms

Requires: harness at $ZUMO_HARNESS or /home/claude/harness (pio_harness.sh,
libcore_lto.a built by --setup), and extract_project.py beside this file.
"""
import re, sys, os, json, glob, subprocess, tempfile, shutil, collections
import html as H

VERSION = 'v1.9.1'

# The standing control build (rule 30): reproduce this BEFORE trusting any
# other figure. It MOVES whenever the book re-baselines - S158's option-C
# rollout took it from 20,516 to 20,592 and this constant was not moved with
# it, so --selftest was red for three sessions while --check printed PASS.
STANDING_CONTROL = 20592
# v1.2 (S152): ARM 4 NEW - every byte figure in a Maker KINDS label must equal the
#   compiled size of the payload its row points at. Nothing in this repo read a label:
#   gate_payload_match asserts payload BYTES against lesson <pre>, ARM 2 asserts the
#   LESSON's figures. All five L16 labels were stale (-180/-162/-162/-6/-6) and step_3's
#   read '28,662 bytes - TEN to spare' for a payload 152 OVER, in the step whose subject
#   is that it does not fit. They hid because each clause was arithmetically consistent
#   with its own stale figure - a label agreeing with itself (rule 51). Predicate DERIVED
#   from the size table, never typed (rule 19), so rewording a label moves nothing: the
#   BLINDING control in CONTROL H proves it. COVERAGE arm - zero labels scanned fails.
#   step_blocks() now picks a step's kind as the first door NOT declared non-canonical
#   (data-nobuild, data-midstep), because L16 Step 5 and L10 Step 4 each carry two and
#   neither property is inferable from the URL (the §16.23 shape).

HERE = os.path.dirname(os.path.abspath(__file__))
HARNESS = os.environ.get("ZUMO_HARNESS", "/home/claude/harness")
MAKER = os.path.join(HERE, "newproject.html")
LESSONS = os.path.join(HERE, "lessons")
CACHE = os.path.join(tempfile.gettempdir(), "zumo_byte_sizes.json")

sys.path.insert(0, HERE)
import extract_project as ep


# ---------------------------------------------------------------- the Maker

def payloads(maker=MAKER):
    return ep.brace_json(open(maker, encoding="utf-8").read(), "var PAYLOADS = ")


def head_includes(maker=MAKER):
    """The #include lines mainCpp() prepends to a single-file payload body.

    PARSED out of the Maker's own head literal, not typed here. The rest of
    that literal is comments; --selftest CONTROL D proves omitting them is
    byte-neutral.
    """
    t = open(maker, encoding="utf-8").read()
    i = t.index("function mainCpp")
    j = t.index("var P = PAYLOADS[", i)
    incs = re.findall(r"#include <[^>]+>", t[i:j])
    if not incs:
        raise SystemExit("byte_audit: no #include found in mainCpp() head")
    return "\n".join(dict.fromkeys(incs)) + "\n\n"


def kinds(P):
    out = []
    for L in sorted(P, key=int):
        for k in sorted(P[L]):
            if P[L][k]:
                out.append((int(L), k))
    return out


# ---------------------------------------------------------------- compiling

WSIG = re.compile(r"([^/\s]+\.(?:cpp|h|c)):\d+:\d+:\s+warning:\s+(.*?)\s*$")

def wsigs(errpath):
    """Warning signatures for one build: 'file.cpp: message [-Wflag]'.

    Returns None when there is NO err file — a harness older than pio_harness
    v3.1 writes none — and a (possibly empty) list when there is one. The two
    are not the same thing and ARM 8 depends on telling them apart.

    LINE AND COLUMN ARE DROPPED ON PURPOSE. A signature that carried them would
    change every time a line was added above it, which would make this a diff of
    file layout rather than of what the compiler objects to. The file and the
    message are what identify a warning; where it sits is not.
    """
    if not os.path.exists(errpath):
        return None
    out = set()
    for line in open(errpath, encoding="utf-8", errors="replace"):
        m = WSIG.search(line)
        if m:
            out.add("%s: %s" % (m.group(1), m.group(2)))
    return sorted(out)


def compile_kind(lesson, kind, P, incs, keep=None, transform=None):
    """-> (status, flash) where status in PASS | OVER | FAIL. flash None on FAIL.

    `transform(filename, body) -> body` runs on each file just before it is
    written. It exists for ARM 9, which must MODIFY a payload to measure it, and
    it defaults to a no-op so every existing caller compiles the real thing.
    S172: this is the only place a payload is staged, so a second staging path
    for ARM 9 would be a second thing to keep correct (rules 83/84)."""
    d = keep or tempfile.mkdtemp(prefix="ba_")
    if os.path.isdir(d) and keep is None:
        shutil.rmtree(d, ignore_errors=True)
        os.makedirs(d)
    files = ep.materialize(P, str(lesson), kind)
    for fn, body in files.items():
        body = body if body.endswith("\n") else body + "\n"
        # mainCpp() prepends its head to main.cpp UNCONDITIONALLY — string
        # payload or object payload alike ("return head + body"). Two earlier
        # attempts here guessed a condition the Maker does not have: first a
        # substring test that L01's comment boxes tripped, then a directive
        # test that L01 c01's own <EEPROM.h> tripped. Do what the Maker does.
        if fn == "main.cpp":
            body = incs + body          # single-file payload: mainCpp's wrapper
        if transform is not None:
            body = transform(fn, body)
        open(os.path.join(d, fn), "w", encoding="utf-8").write(body)
    r = subprocess.run(["bash", os.path.join(HARNESS, "pio_harness.sh"), d],
                       capture_output=True, text=True)
    out = r.stdout
    m = re.search(r"flash=(\d+)", out)          # PASS and OVER both print it
    if out.startswith("PASS") and m:
        st, fl = "PASS", int(m.group(1))
    elif out.startswith("OVER") and m:
        st, fl = "OVER", int(m.group(1))
    else:
        st, fl = "FAIL", None
    # pio_harness v3.1 writes stderr beside the build, so it must be read BEFORE
    # the tempdir goes. Under v3.0 there is no such file and this is [] — which
    # is why ARM 8 checks the harness version rather than reading an empty list
    # as "no warnings".
    ws = wsigs(os.path.join(d, "pbuild", "err.txt"))
    if keep is None:
        shutil.rmtree(d, ignore_errors=True)
    return st, fl, ws


def build_sizes(P, only=None, quiet=False):
    incs = head_includes()
    tbl, ks = {}, kinds(P)
    if only:
        ks = [x for x in ks if x[0] == only]
    for n, (L, k) in enumerate(ks, 1):
        st, fl, ws = compile_kind(L, k, P, incs)
        row = {"status": st, "flash": fl}
        # "warn" is written ONLY when the harness produced an err file to read.
        # An absent key means "not measured"; an empty list means "measured and
        # clean". Collapsing those two would let a v3.0 harness — which writes no
        # err file at all — read as a book with no warnings in it.
        if ws is not None:
            row["warn"] = ws
        tbl["%d/%s" % (L, k)] = row
        if not quiet:
            print("  [%3d/%3d] L%02d %-28s %-4s %s"
                  % (n, len(ks), L, k, st, fl if fl else "-"), flush=True)
    return tbl


def load_sizes():
    if not os.path.exists(CACHE):
        raise SystemExit("byte_audit: no size table. Run --sizes first.")
    return json.load(open(CACHE))


# ---------------------------------------------------------------- the lesson

FIG = r"(\d{1,3},\d{3})"

def lesson_path(L):
    return os.path.join(LESSONS, "Lesson_%02d.html" % L)


def step_blocks(L):
    """Parse Step blocks out of a lesson.

    Returns [{'step':int,'title':str,'heading_fig':int|None,
              'compile_figs':[int],'kind':str|None}]

    'kind' comes from the ?lesson=N&kind=K link inside the step's own catch-up
    <details>. Parsed from the lesson; never typed here.
    """
    t = open(lesson_path(L), encoding="utf-8").read()
    # Heading shapes differ book-wide: "Step 3 — Title" (L13–L16) and
    # "📁 Step 2b: Title" (L11, L12). A parser that saw only the first read
    # L11 and L12 as having no steps at all.
    heads = list(re.finditer(
        r"<h3[^>]*>[^<]*?\bStep\s+(\d+[a-z]?)\s*(?:[—–-]|:)\s*(.*?)</h3>", t, re.S))
    blocks = []
    for i, m in enumerate(heads):
        end = heads[i + 1].start() if i + 1 < len(heads) else len(t)
        body = t[m.end():end]
        htxt = m.group(2)
        hf = re.search(FIG + r"\s*bytes", htxt)
        cfs = [int(x.replace(",", "")) for x in
               re.findall(r"COMPILE CHECK</b>\s*[—–-]?\s*" + FIG, body)]
        # A step may carry more than one door. The step's OWN kind is the first
        # link not DECLARED non-canonical: data-nobuild (L10's RED build) or
        # data-midstep (L16 Step 5's between-the-trades state, S152). Neither is
        # inferable from the URL, so both are declared in markup (the §16.23 shape).
        kd = None
        for a in re.finditer(r"<a\b[^>]*?\?lesson=%d&(?:amp;)?kind=([A-Za-z0-9_]+)[^>]*>" % L, body):
            if "data-nobuild" in a.group(0) or "data-midstep" in a.group(0):
                continue
            kd = a
            break
        blocks.append({
            "step": m.group(1),
            "title": re.sub(r"<[^>]+>", "", htxt).strip(),
            "heading_fig": int(hf.group(1).replace(",", "")) if hf else None,
            "compile_figs": cfs,
            "kind": kd.group(1) if kd else None,
        })
    return blocks


# ---------------------------------------------------------------- the arms

CEILING = 28672


def stated_figures(L):
    """Every byte figure the lesson states anywhere. Used only to ask whether
    an overflow is DECLARED — never to decide what a payload should weigh."""
    if not os.path.exists(lesson_path(L)):
        return set()
    t = open(lesson_path(L), encoding="utf-8").read()
    return {int(x.replace(",", "")) for x in re.findall(FIG, t)}


def declared_nobuild(L):
    """kind -> reason, for payloads the LESSON declares unbuildable in markup.

    §16.23. Prose declarations are invisible to every instrument (rule 33), so
    the catch-up link carries the reason as an attribute. The reason is read,
    not just its presence: a bare boolean would be a label, not the thing
    (rule 31).
    """
    if not os.path.exists(lesson_path(L)):
        return {}
    t = open(lesson_path(L), encoding="utf-8").read()
    out = {}
    for m in re.finditer(r"<a\b[^>]*>", t):
        tag = m.group(0)
        k = re.search(r"kind=([A-Za-z0-9_]+)", tag)
        r = re.search(r'data-nobuild="([^"]*)"', tag)
        if k and r and r.group(1).strip():
            out[k.group(1)] = r.group(1)
    return out


def arm1(tbl, only=None):
    print("ARM 1 — CEILING: every payload the Maker defines must compile and fit")
    declared, undeclared, nolink = [], [], []
    n = 0
    for key, rec in sorted(tbl.items(), key=lambda x: (int(x[0].split("/")[0]), x[0])):
        L = int(key.split("/")[0])
        if only and L != only:
            continue
        n += 1
        if rec["status"] == "PASS":
            continue
        if rec["status"] == "OVER":
            # An overflow the lesson STATES is a lesson teaching the ceiling.
            # An overflow it does not state is L16's S148 defect.
            (declared if rec["flash"] in stated_figures(L) else undeclared
             ).append((key, rec))
        else:
            kind = key.split("/", 1)[1]
            nolink.append((key, rec, declared_nobuild(L).get(kind)))
    for key, rec in declared:
        print("   %-34s OVER %-6s  DECLARED — the lesson states this figure"
              % (key, "{:,}".format(rec["flash"])))
    for key, rec in undeclared:
        print("   %-34s OVER %-6s  UNDECLARED — over %s and the lesson never says so"
              % (key, "{:,}".format(rec["flash"]), "{:,}".format(CEILING)))
    undecl_nb = [x for x in nolink if not x[2]]
    for key, rec, reason in nolink:
        if reason:
            print("   %-34s DOES NOT LINK — DECLARED: %s" % (key, reason))
        else:
            print("   %-34s DOES NOT LINK — UNDECLARED. If this is deliberate, give its"
                  % key)
            print("   %-34s catch-up link a data-nobuild reason (Bible §16.23)." % "")
    ok = not undeclared and not undecl_nb
    print("   %d payload(s) compiled · %d declared overflow · %d undeclared overflow · "
          "%d declared unbuildable · %d undeclared unbuildable\n"
          % (n, len(declared), len(undeclared), len(nolink) - len(undecl_nb), len(undecl_nb)))
    return ok


def arm2(tbl, only=None):
    """Every build figure a lesson promises must be a real compiled size."""
    print("ARM 2 — FIGURES: every step figure must equal a compiled payload of that lesson")
    ok, checked, bad = True, 0, []
    for L in range(1, 17):
        if only and L != only:
            continue
        if not os.path.exists(lesson_path(L)):
            continue
        sizes = {k.split("/", 1)[1]: v["flash"] for k, v in tbl.items()
                 if int(k.split("/")[0]) == L and v["flash"]}
        if not sizes:
            continue
        rev = {}
        for k, v in sizes.items():
            rev.setdefault(v, []).append(k)
        for b in step_blocks(L):
            figs = ([b["heading_fig"]] if b["heading_fig"] else []) + b["compile_figs"]
            for f in figs:
                checked += 1
                if f not in rev:
                    ok = False
                    bad.append((L, b["step"], f, b["title"][:40]))
    for L, s, f, ti in bad:
        print("   L%02d Step %-2s claims %-7s — no payload of L%02d compiles to it   (%s)"
              % (L, s, "{:,}".format(f), L, ti))
    print("   %d figure(s) checked, %d unmatched" % (checked, len(bad)))
    print("   NOTE: only L15 and L16 state byte figures in step headings or")
    print("   COMPILE CHECK callouts, so this assertion reaches two lessons.")
    print("   Every other figure in the book is a LEAD below, not an assertion.\n")
    return ok


def arm2_leads(tbl, only=None):
    """Every figure in the plausible program-size band, matched or not.

    A LEAD, never a verdict (rule 38). The band's floor and ceiling are taken
    from the compiled corpus itself, not typed: nothing below the smallest
    payload or above the largest can be a claim about a build.
    """
    live = [v["flash"] for v in tbl.values() if v["flash"]]
    lo, hi = min(live), max(live)
    rev = {}
    for k, v in tbl.items():
        if v["flash"]:
            rev.setdefault(v["flash"], []).append(k)
    print("ARM 2b — LEADS: figures inside the compiled band %s..%s, book-wide"
          % ("{:,}".format(lo), "{:,}".format(hi)))
    tot = un = 0
    for L in range(1, 17):
        if only and L != only:
            continue
        if not os.path.exists(lesson_path(L)):
            continue
        t = open(lesson_path(L), encoding="utf-8").read()
        figs = sorted({int(x.replace(",", "")) for x in re.findall(FIG, t)})
        mine = {v["flash"] for k, v in tbl.items()
                if int(k.split("/")[0]) == L and v["flash"]}
        rows = []
        for f in figs:
            if not (lo <= f <= hi):
                continue
            tot += 1
            if f in mine:
                continue
            un += 1
            where = rev.get(f)
            rows.append((f, "matches " + ", ".join(where) if where
                         else "matches NO payload in the book"))
        if rows:
            print("   L%02d" % L)
            for f, w in rows:
                print("      %-8s %s" % ("{:,}".format(f), w))
    print("   %d figure(s) in band, %d not produced by their own lesson\n" % (tot, un))



# ------------------------------------------------- ARM 4: the Maker's labels

CEILING = 28672

def kind_rows(maker=MAKER):
    """Parse the KINDS registry: (lesson, kind id, decoded label, payloadRef).

    The label is what the STUDENT reads in the Maker's dropdown. Nothing else
    in this repo reads it -- gate_payload_match asserts payload BYTES against
    lesson <pre>, and ARM 2 asserts the LESSON's figures. A byte figure typed
    into a label was, until S152, unreachable by every instrument."""
    src = open(maker, encoding="utf-8").read()
    i = src.index("var KINDS")
    blk = src[i:i + 900000]
    out = []
    for L, body in re.findall(r'\n    (\d+): \[(.*?)\n    \]', blk, re.S):
        for m in re.finditer(r'\["([^"]+)",\s*"((?:[^"\\]|\\.)*)"(.*?)\]', body, re.S):
            kid, label, rest = m.group(1), m.group(2), m.group(3)
            refs = re.findall(r'"([^"]+)"', rest)
            out.append((int(L), kid, label.encode().decode("unicode_escape"),
                        refs[-1] if refs else None))
    return out


def expected_clause(n):
    """DERIVED from the compile and the ceiling -- never typed (rule 19)."""
    return ("%s to spare" % format(CEILING - n, ",")) if n <= CEILING else \
           ("%s OVER" % format(n - CEILING, ","))


def arm4(tbl, only=None):
    """Every byte figure in a KINDS label must equal its payload's compiled size.

    The expectation is DERIVED from the size table, so rewording a label moves
    nothing and only a real drift fires. The spare/over clause is checked too,
    because S152 found five labels whose clauses were arithmetically consistent
    with their own stale figures -- a label agreeing with itself (rule 51)."""
    print("ARM 4 - LABELS: every byte figure in a KINDS label equals its compile")
    bad, seen = [], 0
    for L, kid, label, ref in kind_rows():
        if only and L != only:
            continue
        figs = re.findall(r'\b(\d{2},\d{3})\b', label)
        if not figs:
            continue
        seen += 1
        rec = tbl.get("%d/%s" % (L, ref))
        got = rec.get("flash") if isinstance(rec, dict) else rec
        claim = int(figs[0].replace(",", ""))
        if got is None:
            bad.append((L, kid, claim, None, "no compiled size for ref %r" % ref))
            continue
        if claim != got:
            bad.append((L, kid, claim, got, "label figure != compile"))
            continue
        want = expected_clause(got)
        if re.search(r'\d{1,3},?\d*\s+(?:to spare|OVER)', label) and want not in label:
            bad.append((L, kid, claim, got, "clause should read %r" % want))
    for L, kid, claim, got, why in bad:
        print("   L%-2d %-24s label %s  compiled %s  -- %s"
              % (L, kid, format(claim, ","), got, why))
    print("   %d label(s) carry a figure, %d unmatched" % (seen, len(bad)))
    if not seen:
        print("   COVERAGE: ZERO labels scanned - the parser found nothing")
        return False
    print()
    return not bad



# ------------------------------------------------- ARM 6: the banks' figures

QUIZ_DIR = os.path.join(HERE, "quizzes")

# A figure that NAMES a build is a claim about that build. This is the whole
# predicate, and it is deliberately narrow: "appears in some lesson" is NOT the
# property (it convicts a legitimate synthetic distractor such as L16's 20,406),
# and "equals some compile" is not either. What a bank owes is that a figure it
# LABELS as a named build equals what that build compiles to.
_BANK_LABEL = re.compile(
    r"(?:Lesson[\s\u00a0]*(\d{1,2})(?:'s)?[\s\u00a0]*finished"
    r"|finished[\s\u00a0]*Lesson[\s\u00a0]*(\d{1,2}))", re.I)
_BANK_FIG = re.compile(r"\b(\d{2},\d{3})\b")


def _bank_units(q):
    """The text units a claim can live in.

    A label and its figure are frequently split across an option's `text` and
    its own `why` (that is exactly where S165 found three of them), so an
    option is read as ONE unit as well as two."""
    out = []
    for k in ("stem",):
        if isinstance(q.get(k), str):
            out.append(q[k])
    for o in q.get("options", []) or []:
        t, w = o.get("text") or "", o.get("why") or ""
        out += [t, w, t + " || " + w]
    for pr in q.get("pairs", []) or []:
        out.append((pr.get("left") or "") + " || " + (pr.get("right") or ""))
    for e in q.get("extra_answers", []) or []:
        if isinstance(e, str):
            out.append(e)
    return [u for u in dict.fromkeys(out) if u]


def bank_claims(quiz_dir=None):
    """Yield (bankfile, qid, lesson_n, claimed_figure, unit) for every figure
    that sits beside a name of a lesson's finished build."""
    import yaml
    seen, out = set(), []
    for f in sorted(glob.glob(os.path.join(quiz_dir or QUIZ_DIR, "ZUMO_QUIZ_L*.yaml"))):
        try:
            d = yaml.safe_load(open(f, encoding="utf-8"))
        except Exception:
            continue
        if not isinstance(d, dict) or "sets" not in d:
            continue
        for _sn, S in (d.get("sets") or {}).items():
            for q in (S.get("questions") or []):
                for u in _bank_units(q):
                    m = _BANK_LABEL.search(u)
                    if not m:
                        continue
                    figs = _BANK_FIG.findall(u)
                    if not figs:
                        continue
                    n = int(m.group(1) or m.group(2))
                    key = (os.path.basename(f), q.get("id"), n, figs[0])
                    if key in seen:
                        continue
                    seen.add(key)
                    out.append((os.path.basename(f), q.get("id"), n,
                                int(figs[0].replace(",", "")), u))
    return out


def arm6(tbl, only=None, quiz_dir=None):
    """ARM 6 - BANK FIGURES: a bank figure that names a build must equal it.

    Nothing in this repo compared a bank's numbers to anything. ARM 2 asserts
    the LESSON's figures against a compile and has never read a bank; §24.18
    compares a `source:` PIN and is silent on what the questions say. S165 found
    four stale figures across two banks by hand, one of them a CORRECT answer -
    so a student reading the live lesson was marked wrong.

    STATED SCOPE LIMIT (rule 78): this reaches a figure only where the text
    NAMES a lesson's finished build. A figure labelled by something the Maker
    does not define - L16's "what cutting the buzzer would give" - is a real
    claim this arm cannot see, because there is no payload to compile against
    it. Recorded rather than papered over with an exemption list (rule 20)."""
    print("ARM 6 - BANK FIGURES: a bank figure that names a build equals that build")
    claims = bank_claims(quiz_dir)
    bad, seen = [], 0
    for bank, qid, n, claim, unit in claims:
        if only and n != only:
            continue
        seen += 1
        rec = tbl.get("%d/finished" % n)
        got = rec.get("flash") if isinstance(rec, dict) else rec
        if got is None:
            bad.append((bank, qid, n, claim, None, "no compiled size for %d/finished" % n))
        elif claim != got:
            bad.append((bank, qid, n, claim, got, "bank figure != compile"))
    for bank, qid, n, claim, got, why in bad:
        print("   %-24s %-10s names L%-2d finished: bank %s  compiled %s  -- %s"
              % (bank, qid, n, format(claim, ","), got, why))
    print("   %d labelled bank figure(s) checked, %d unmatched" % (seen, len(bad)))
    if not seen:
        print("   COVERAGE: ZERO labelled bank figures scanned - the parser found nothing")
        return False
    print()
    return not bad



# ---------------------------------------------------------------- ARM 7

# ARM 7's patterns are DELIBERATELY TIGHT. The bare "By N." form is ARM 5's and
# STAYS there: inside a COMPILE CHECK window it is unambiguous, and in ARM 7's
# book-wide scope it matched ordinary arithmetic prose in three banks. A loose "By N." pattern was tried
# first and matched "0.9 divided by 10." in QUIZ_L14 and "divided by 12.25" in
# QUIZ_L06 - arithmetic prose that is not a headroom claim at all. Measured
# before it was narrowed: the loose form returned 4 leads of which 2 were that
# false positive. A predicate that convicts prose it does not understand trains
# its reader to skip it (rule 20).
A7_SPARE = re.compile(r"([\d,]{2,6})\s*(?:bytes\s*)?to spare", re.I)
A7_HAVE  = re.compile(r"you have\s+(?:<b>\s*)?([\d,]{2,6})\s*bytes", re.I)
A7_OVER  = re.compile(r"still\s+(?:over,?\s+by\s+|([\d,]{2,6})\s+over)|"
                      r"\bover,?\s+by\s+([\d,]{2,6})\b", re.I)


def a7_sentences(text):
    """Split on sentence enders so a claim can be judged with its own context."""
    return re.split(r"(?<=[.!?])\s+", text)


A7_BOUND = re.compile(r"(?:^|\s)-\s+(?:text|left|id):|(?:^|\s)stem:")


def a7_clause(sent, n):
    """The OPTION-sized window around one claim, for judging the conditional.

    S172. a7_sentences() splits on sentence enders, and a YAML option ends with a
    quote and a newline rather than a full stop - so a whole run of options
    concatenates into one "sentence" and a `would` in a distant `why` silenced a
    claim six options away. MEASURED, not argued: seven claims were being skipped
    as conditional and only ONE of them was, so six live assertions - among them
    L16's 336-over, 972-over and two 24-spare claims - were reaching no check at
    all, and were correct today by luck rather than by assertion (rule 59).

    The window is bounded by the option markers themselves, so `text` and its
    sibling `why` are judged together: the subjunctive that governs a distractor
    usually lives in the rationale beneath it, not in the option text.
    """
    m = re.search(re.escape(format(n, ",") if n >= 1000 else str(n)) + r"\b", sent)
    if not m:
        return sent
    starts = [x.start() for x in A7_BOUND.finditer(sent) if x.start() <= m.start()]
    ends = [x.start() for x in A7_BOUND.finditer(sent) if x.start() > m.end()]
    return sent[(starts[-1] if starts else 0):(ends[0] if ends else len(sent))]


def headroom_claims(quiz_dir=None):
    """-> [(file, kind, n, sentence)] for every spare/over claim in the corpus.

    Scope is the RENDERED lesson text and the LIVE bank questions. A bank's `#`
    header is provenance and is excluded, because S169 measured that region and
    found every superseded figure in the book living there legitimately - it
    narrates what the figures USED to be (rule 37). An arm that reads history as
    a claim reports the record as a defect.
    """
    out = []
    for p in sorted(glob.glob(os.path.join(HERE, "lessons", "Lesson_*.html"))):
        txt = H.unescape(re.sub(r"<[^>]+>", " ", open(p, encoding="utf-8").read()))
        for s in a7_sentences(txt):
            for m in A7_SPARE.finditer(s):
                out.append((os.path.basename(p), "spare", _a7n(m.group(1)), s))
            for m in A7_HAVE.finditer(s):
                out.append((os.path.basename(p), "spare", _a7n(m.group(1)), s))
            for m in A7_OVER.finditer(s):
                g = next((x for x in m.groups() if x), None)
                if g:
                    out.append((os.path.basename(p), "over", _a7n(g), s))
    qd = quiz_dir or QUIZ_DIR
    for p in sorted(glob.glob(os.path.join(qd, "ZUMO_QUIZ_L*.yaml"))):
        body = "\n".join(l for l in open(p, encoding="utf-8").read().splitlines()
                         if not l.lstrip().startswith("#"))
        for s in a7_sentences(body):
            for m in A7_SPARE.finditer(s):
                out.append((os.path.basename(p), "spare", _a7n(m.group(1)), s))
            for m in A7_HAVE.finditer(s):
                out.append((os.path.basename(p), "spare", _a7n(m.group(1)), s))
            for m in A7_OVER.finditer(s):
                g = next((x for x in m.groups() if x), None)
                if g:
                    out.append((os.path.basename(p), "over", _a7n(g), s))
    return sorted(set(out))


def _a7n(s):
    return int(str(s).replace(",", ""))


def arm7(tbl, only=None, quiz_dir=None):
    """ARM 7 - HEADROOM: a stated spare/over claim equals ceiling minus a compile.

    THE HOLE THIS CLOSES. ARM 2 asserts a lesson's byte FIGURES and ARM 5 asserts
    the delta/spare/over clauses BESIDE them - but both are scoped to step
    headings and COMPILE CHECK windows, so a headroom claim written in ordinary
    prose or inside a bank option is reached by nothing. S169 found three such
    claims stale in one lesson and its bank, all of them survivors of S168's +54
    rebaseline: Lesson_16 SS7.4 promised 108 bytes of reserve where the compiled
    finished build leaves 54 - contradicting SS5 of the same lesson, which says
    "Green. 54 to spare" - and QUIZ_L16 A07 and B44 both said "still 210 over"
    where the compile says 264. A07 keyed that as its CORRECT answer while its
    OWN distractor rationale said 264: a question disagreeing with itself
    (rule 51), and the exact shape v8.130 forbids, because a student reading the
    live lesson and answering 264 was marked wrong.

    WHY A COMMA SWEEP COULD NEVER HAVE FOUND THEM. 210, 108 and 54 carry no
    comma and sit below the byte band, so every figure-shaped predicate in this
    tool is structurally blind to them. What makes them checkable is not their
    shape but their RELATION: a headroom claim is ceiling minus a build, so the
    expectation is DERIVED from the size table and never typed (rule 19).

    STATED SCOPE LIMITS (rule 78), both real and neither papered over:
      1. It is blind to a claim naming the WRONG build, exactly as ARM 6 is: a
         stale figure that still equals SOME build's headroom is silent.
      2. A CONDITIONAL claim is out of scope by property, not by name list
         (rule 20). L16 offers "26,798 bytes with 1,874 to spare" as a
         distractor and explains it as "what cutting the buzzer WOULD give" -
         a hypothetical the book hands to the student, with no payload by
         design. The subjunctive is what separates a hypothetical from an
         assertion, so the arm reads it rather than carrying an exemption.
      3. AND THE SUBJUNCTIVE TEST IS A WORD TEST, WHICH OVER-CATCHES (S172).
         `would` is ordinary English, so a flat assertion sharing a sentence
         with it is skipped: L16's CORRECT answer "28,626 bytes with 46 to
         spare - three trades: one you WOULD have made anyway" is an assertion
         the arm does not check, and no windowing can separate those two, because
         the word sits inside the claim's own string. TWO claims skip for this
         reason today, both equal to a real headroom. Narrowing the window to the
         option (S172) took the skip list from 7 to 3 and gained four real
         assertions; the residue is stated rather than papered over, because the
         honest fix is not a better word test. S167's rule from the far side:
         a word test cannot report what it OVER-catches either.
      4. AND THE CONDITIONAL'S FIGURE IS STILL DERIVED FROM A COMPILE, WHICH IS
         WHY 1,882 WENT STALE. S171 moved 16/finished +8 and the hypothetical
         moved with it - measured, not inferred: finished with all twelve
         playNote() lines removed weighs 26,798, so the buzzer still costs
         exactly 1,828 and only the base moved. The subjunctive tells you the
         ROBOT never does this. It does not tell you the NUMBER is free.
    """
    print("ARM 7 - HEADROOM: a stated spare/over claim equals ceiling minus a compile")
    flash = [v.get("flash") for v in tbl.values() if isinstance(v, dict) and v.get("flash")]
    spare = {CEILING - f for f in flash if f <= CEILING}
    over = {f - CEILING for f in flash if f > CEILING}
    bad, seen, skipped = [], 0, 0
    for fn, kind, n, sent in headroom_claims(quiz_dir):
        if n < 10 or n > 5000:
            continue
        if re.search(r"\bwould\b", a7_clause(sent, n), re.I):   # conditional, judged on its OWN option
            skipped += 1
            continue
        seen += 1
        if n not in (spare if kind == "spare" else over):
            bad.append((fn, kind, n, sent.strip()[:96]))
    for fn, kind, n, sent in bad:
        print("   %-24s %-5s %-7s no build has that headroom -- %s"
              % (fn, kind, format(n, ","), sent))
    print("   %d headroom claim(s) checked, %d conditional skipped, %d unmatched"
          % (seen, skipped, len(bad)))
    if not seen:
        print("   COVERAGE: ZERO headroom claims scanned - the parser found nothing")
        return False
    print()
    return not bad

# ---------------------------------------------------------------- ARM 8

# ARM 8 IS DELIBERATELY NARROW, AND THE REASON IS THE BUILD-UP MODEL.
#
# For its whole life pio_harness.sh compiled with -w. The header claimed -Wall —
# which is what PlatformIO really passes, so every warning this book's students
# see on their own machines was discarded here. v3.1 turned the flag on. The
# population that appeared was measured before any of this was written (rule 34):
# 113 warnings across 70 of 216 payloads, in two classes and fourteen sites.
#
# 109 OF THOSE 113 ARE THE BUILD-UP MODEL WORKING AS DESIGNED. A state enters
# RobotState in the lesson that declares it and gets its `case` a step or two
# later, so the intermediate payload legitimately does not handle it; L08 step 4
# declares two variables that step 5 fills. That is signal a student SHOULD get,
# and asserting on it would mean this arm fired on every correct lesson edit that
# added a step. An arm that cries at correct work gets switched off.
#
# ONE MORE IS CORRECT AND USEFUL: 11/b1_onewheel's unused `right` is the compiler
# pointing straight at that payload's deliberate `// <-- PLANTED` bug. Worth
# knowing that a student's real PlatformIO has always handed them that hint.
#
# SO ARM 8 ASSERTS ONLY WHERE THE BUILD-UP MODEL CANNOT EXPLAIN A WARNING: the
# `finished` payloads. A finished build is the terminal, student-facing program
# of its lesson; nothing is coming later to use the thing being warned about.
# Intermediate steps are COUNTED AND REPORTED but never asserted.
#
# WHAT THIS ARM IS BLIND TO, STATED SO NOBODY DISCOVERS IT LATER (rule 78):
#   1. A warning that appears in an intermediate step and is genuinely wrong will
#      be printed in the population line and asserted by nothing. The build-up
#      model is an explanation, not a proof, and this arm takes it on trust.
#   2. It reads only what the compiler chose to say. A defect gcc has no warning
#      for is invisible here, exactly as it is to every other arm.
#   3. It cannot tell a signature that MOVED from one that was fixed and a new
#      one raised, because the signature drops line numbers on purpose.
#   4. IT COUNTS SIGNATURES, NOT LINES, and the two differ. The book's raw
#      population is 113 warning lines; this arm reports 99, over the same 70
#      payloads. The gap is 14 lines in 6 payloads where the SAME enum value is
#      unhandled in TWO switches in one file — the showStatus() display switch
#      and the loop() dispatch switch — which collapse to one signature. So this
#      arm cannot distinguish "unhandled in one switch" from "unhandled in two."
#      Both numbers are right; they answer different questions, and the payload
#      count is the one that agrees across both.

# The adjudicated baseline. Every entry is a warning in a `finished` build that
# was read, understood and left standing on purpose. An entry here is a claim
# that somebody looked; it is not a claim that the code is right.
FINISHED_WARN_BASELINE = {
    # EMPTY, AND THAT IS THE RESTING STATE THIS ARM WAS BUILT FOR. S171 closed
    # the only entries it has ever carried.
    #
    # S170 recorded four: SWEEP_DONE was the one RobotState member with no case
    # in the loop() dispatch switch, in the terminal build of L13, L14, L15 and
    # L16. S171 gave it one - read B, return to STOPPED, the shape LINE_LOST
    # already uses in the same file - and the four signatures went with it.
    #
    # ONE CLAIM IN THE S170 ENTRY WAS TOO STRONG AND IS CORRECTED HERE RATHER
    # THAN CARRIED FORWARD: it said the sweep ending was the only one yielding
    # no scorecard. It was not. VICTIM_FOUND routes to STOPPED in L15 and L16
    # too, and only two paths ever reach RUN_REPORT - the kill switch during
    # FOLLOWING_LINE, and the TUNING_RUN_MS bell. SWEEP_DONE was never uniquely
    # unscored. It was uniquely UNRECOVERABLE: the one state in the enum the
    # program could not leave, whose only exit was the power switch, in the
    # lesson that spends a paragraph teaching that a dead B is TEMPORARY.
    #
    # AN EMPTY BASELINE IS NOT A WEAKER CONTROL. arm8() fails on an empty TABLE
    # and on a table carrying no warning data, so "nothing to adjudicate" and
    # "nothing was measured" cannot be confused. CONTROL K now carries its own
    # synthetic baseline for exactly this reason: a control that needed the live
    # baseline to be non-empty is a control that gets deleted the day somebody
    # cleans one up.
}


def arm8(tbl, only=None, baseline=None):
    """ARM 8 - WARNINGS: a finished build warns only where somebody adjudicated it.

    -> True/False. Reports the whole population; asserts the finished builds.

    `baseline` is injectable so CONTROL K can supply its own fixture instead of
    depending on whatever the live baseline happens to hold - which today is
    nothing at all.
    """
    base = FINISHED_WARN_BASELINE if baseline is None else baseline
    print("ARM 8 - WARNINGS: every warning in a finished build is one somebody read")
    rows = {k: v for k, v in tbl.items()
            if only is None or k.split("/")[0] == str(only)}

    unmeasured = [k for k, v in rows.items() if "warn" not in v]
    if unmeasured:
        # Not a failure: --lesson writes a partial table, and an older harness
        # writes none at all. But it MUST be said, because an arm that silently
        # scanned nothing is the shape S169 caught inside its own control suite.
        print("   %d payload(s) carry no warning data - harness older than "
              "pio_harness v3.1, or a partial --sizes. Re-run --sizes." % len(unmeasured))
        if len(unmeasured) == len(rows):
            print("   COVERAGE: NOTHING was measured. Not a pass.")
            return False

    measured = {k: v["warn"] for k, v in rows.items() if "warn" in v}
    total = sum(len(v) for v in measured.values())
    classes = collections.Counter()
    for sigs in measured.values():
        for s in sigs:
            m = re.search(r"\[-W[^\]]+\]", s)
            classes[m.group(0) if m else "(unclassified)"] += 1
    print("   population: %d warning(s) over %d of %d payload(s)   %s"
          % (total, sum(1 for v in measured.values() if v), len(measured),
             "  ".join("%s x%d" % (c, n) for c, n in classes.most_common())))

    bad = []
    fin = {k: v for k, v in measured.items() if k.endswith("/finished")}
    for k in sorted(fin, key=lambda x: int(x.split("/")[0])):
        want = base.get(k, [])
        got = fin[k]
        for s in got:
            if s not in want:
                bad.append((k, "NEW", s))
        for s in want:
            if s not in got:
                bad.append((k, "GONE", s))
    # A baseline entry for a finished build that no longer exists is stale too.
    for k in base:
        if k not in fin and (only is None or k.split("/")[0] == str(only)):
            bad.append((k, "GONE", "the whole payload"))

    for k, why, s in bad:
        print("   %-16s %-5s %s" % (k, why, s))
    if bad:
        print("   %d unadjudicated - a NEW warning needs reading; a GONE one needs "
              "the baseline updated." % len(bad))
    else:
        print("   %d finished build(s) checked, %d adjudicated warning(s), 0 unadjudicated"
              % (len(fin), sum(len(v) for v in fin.values())))
    if not fin:
        print("   COVERAGE: ZERO finished builds scanned - the table has none")
        return False
    print()
    return not bad


# ---------------------------------------------------------------- ARM 5

DELTA_RE = re.compile(r"\b(?:up|down)\s+([\d,]+)|(?<![\w,])([+\u2212-])\s?([\d,]{2,6})\b")
SPARE_RE = re.compile(r"([\d,]+)\s*(?:B\s*)?to spare", re.I)
OVER_RE  = re.compile(r"\bBy\s+([\d,]+)\.|over(?:flowed)?[^.]{0,24}?by\s+([\d,]+)", re.I)


def checkpoints(L):
    """Every CHECKPOINT a lesson states, in document order.

    A checkpoint is a step <h3> heading or the 230 characters following the
    literal COMPILE CHECK - the two places this book puts a build figure next
    to a claim about it. Both are PARSED; neither is typed here (rule 19).

    Returns [{'pos','kind','fig','delta','spare','over','text'}].
    """
    if not os.path.exists(lesson_path(L)):
        return []
    t = open(lesson_path(L), encoding="utf-8").read()
    sites = []
    for m in re.finditer(r"<h3[^>]*>(.*?)</h3>", t, re.S):
        sites.append((m.start(), "heading", H.unescape(re.sub(r"<[^>]+>", "", m.group(1)))))
    for m in re.finditer(r"COMPILE CHECK", t):
        win = H.unescape(re.sub(r"<[^>]+>", " ", t[m.start():m.start() + 700]))[:230]
        sites.append((m.start(), "check", win))
    sites.sort()
    out = []
    for pos, kind, txt in sites:
        f = re.search(FIG, txt)
        if not f:
            continue
        d = DELTA_RE.search(txt)
        sp = SPARE_RE.search(txt)
        ov = OVER_RE.search(txt)
        def num(x):
            return int(x.replace(",", "").rstrip(".")) if x else None
        delta = None
        if d:
            if d.group(1):
                delta = num(d.group(1))
                if re.search(r"\bdown\s+" + re.escape(d.group(1)), txt, re.I):
                    delta = -delta
            else:
                delta = num(d.group(3))
                if d.group(2) in ("-", "\u2212"):
                    delta = -delta
        out.append({"pos": pos, "kind": kind, "fig": num(f.group(1)),
                    "delta": delta, "spare": num(sp.group(1)) if sp else None,
                    "over": num(ov.group(1) or ov.group(2)) if ov else None,
                    "text": re.sub(r"\s+", " ", txt)[:56]})
    return out


def arm5(tbl, only=None):
    """ARM 5 - CLOSURE: the arithmetic AROUND a figure must close.

    ARM 2 asserts that a figure equals a compile. It is BLIND to the middle:
    S146 proved that reverting one figure inside a chain leaves the endpoints
    and the stated total intact and every gate green. This arm asserts the
    three claims a lesson makes NEXT TO a figure:

      DELTA   'up 270' / '+164' / 'down 42'  ==  fig - the previous figure
      SPARE   'N to spare'                   ==  CEILING - fig
      OVER    'over by N' / 'By N.'          ==  fig - CEILING

    Every one is derived from the lesson's own text and the compiled sizes.
    Nothing here is pinned to a value.
    """
    print("ARM 5 - CLOSURE: every delta, spare and over-figure must close on its own figure")
    ok, checked, bad = True, 0, []
    for L in range(1, 17):
        if only and L != only:
            continue
        cps = checkpoints(L)
        # A DELTA is a claim about the previous STEP, not the previous mention.
        # A step heading and its own COMPILE CHECK restate one build state, so
        # walking mentions makes every such pair read as +0 (found by the arm's
        # own first run, on L16 Step 2).
        # EVERY h3, not only the ones that carry a figure. Segmenting on the
        # figure-bearing headings alone mis-assigns L13, whose step headings
        # state no figure at all - and the DELTA arm then goes silent on a
        # seeded wrong delta, which is how this was caught (rule 59).
        heads = [m.start() for m in re.finditer(r"<h3[^>]*>", 
                 open(lesson_path(L), encoding="utf-8").read())] if os.path.exists(lesson_path(L)) else []
        def step_of(pos):
            n = 0
            for h in heads:
                if h <= pos:
                    n += 1
            return n
        step_fig = {}
        for c in cps:
            step_fig.setdefault(step_of(c["pos"]), c["fig"])
        for c in cps:
            n = step_of(c["pos"])
            prev = step_fig.get(n - 1)
            if c["delta"] is not None and prev is not None:
                checked += 1
                if step_fig[n] - prev != c["delta"]:
                    ok = False
                    bad.append((L, "DELTA", c["delta"], step_fig[n] - prev, c["text"]))
            if c["spare"] is not None:
                checked += 1
                if CEILING - c["fig"] != c["spare"]:
                    ok = False
                    bad.append((L, "SPARE", c["spare"], CEILING - c["fig"], c["text"]))
            if c["over"] is not None:
                checked += 1
                if c["fig"] - CEILING != c["over"]:
                    ok = False
                    bad.append((L, "OVER", c["over"], c["fig"] - CEILING, c["text"]))
    for L, what, said, real, ti in bad:
        print("   L%02d %-5s states %-7s  arithmetic gives %-7s   (%s)"
              % (L, what, "{:+,}".format(said), "{:+,}".format(real), ti))
    print("   %d closure claim(s) checked, %d broken" % (checked, len(bad)))
    if checked == 0:                      # rule 27: a scan of zero passes
        print("   COVERAGE: zero closure claims parsed - the parser is blind, not the book clean")
        ok = False
    return ok

def arm3(tbl, only=None):
    """Measure the catch-up convention. Report, not verdict."""
    print("ARM 3 — CONVENTION: does Step N's catch-up link serve the file AT step N?")
    print("   IDENTITY = link size equals Step N's own figure")
    print("   OFFSET   = link size equals the PREVIOUS step's figure\n")
    rows = []
    for L in range(1, 17):
        if only and L != only:
            continue
        if not os.path.exists(lesson_path(L)):
            continue
        sizes = {k.split("/", 1)[1]: v["flash"] for k, v in tbl.items()
                 if int(k.split("/")[0]) == L and v["flash"]}
        bl = step_blocks(L)
        ident = off = neither = 0
        for i, b in enumerate(bl):
            if not b["kind"] or b["kind"] not in sizes or b["heading_fig"] is None:
                continue
            s = sizes[b["kind"]]
            prev = bl[i - 1]["heading_fig"] if i else None
            if s == b["heading_fig"]:
                ident += 1
            elif prev is not None and s == prev:
                off += 1
            else:
                neither += 1
        tot = ident + off + neither
        if tot:
            verdict = ("IDENTITY" if ident == tot else
                       "OFFSET" if off == tot else "MIXED")
            rows.append((L, ident, off, neither, tot, verdict))
    print("   %-5s %8s %8s %9s %7s  %s" % ("", "IDENTITY", "OFFSET", "NEITHER", "rows", "verdict"))
    for L, i, o, n, t, v in rows:
        print("   L%02d   %8d %8d %9d %7d  %s" % (L, i, o, n, t, v))
    print()
    return rows


# ---------------------------------------------------------------- selftest

def selftest():
    P = payloads()
    incs = head_includes()
    fails = []

    def chk(name, cond, detail=""):
        print("   %-58s %s %s" % (name, "PASS" if cond else "FAIL", detail))
        if not cond:
            fails.append(name)

    print("CONTROL A (the control build): L11 after_step_1 must be %s"
          % f"{STANDING_CONTROL:,}")
    st, fl, _ = compile_kind(11, "after_step_1", P, incs)
    chk("harness reproduces the control", (st, fl) == ("PASS", STANDING_CONTROL),
        str(fl) if (st, fl) == ("PASS", STANDING_CONTROL) else
        "%s - the harness may be wrong, or STANDING_CONTROL may be STALE after a "
        "re-baseline. Check the Bible's control list before blaming the harness "
        "(S166: this constant sat at 20,516 for three sessions after S158 moved it "
        "to 20,592, and --selftest was red the whole time while --check said PASS)"
        % fl)

    print("\nCONTROL B (an OVER build is read as OVER, not as a crash)")
    P2 = json.loads(json.dumps(P))
    body = P2["16"]["finished"]["main.cpp"]
    # The pad must survive -Wl,--gc-sections, so it lives in PROGMEM and is
    # READ at runtime. An unreferenced array is collected and pads nothing —
    # that first attempt reported PASS and would have been a control that
    # never fired (rule 59).
    pad = ("\nconst long ba_pad[600] PROGMEM = {"
           + ",".join(str(i * 7 + 1) for i in range(600)) + "};\n"
           "volatile long ba_sink;\n")
    assert "void setup()" in body, "control B: no setup() to inject the read into"
    last = max(m.end() for m in re.finditer(r"^#include.*$", body, re.M))
    body = body[:last] + "\n" + pad + body[last:]   # PROGMEM needs the includes first
    i = body.index("void setup()")
    j = body.index("{", i) + 1
    body = body[:j] + "\n  ba_sink = pgm_read_dword(&ba_pad[millis() % 600]);\n" + body[j:]
    P2["16"]["finished"]["main.cpp"] = body
    st0, fl0, _ = compile_kind(16, "finished", P, incs)      # the UNPADDED baseline
    st, fl, _ = compile_kind(16, "finished", P2, incs)
    chk("padded L16 finished reports OVER with a flash figure",
        st == "OVER" and fl is not None and fl > CEILING, "%s %s" % (st, fl))
    # DERIVED, never pinned (rule 19): the seed fired iff the padded image is
    # bigger than the same payload compiled without the pad. The old form
    # compared against a literal 28,600, which is a spelling of a baseline.
    chk("the pad actually grew the image (the seed fired)",
        fl is not None and fl0 is not None and fl > fl0, "%s vs %s" % (fl, fl0))

    print("\nCONTROL C (a broken build is read as FAIL, not silently sized)")
    P3 = json.loads(json.dumps(P))
    P3["16"]["finished"]["main.cpp"] = "this is not c++\n"
    st, fl, _ = compile_kind(16, "finished", P3, incs)
    chk("unbuildable payload reports FAIL and no size", st == "FAIL" and fl is None)

    print("\nCONTROL D (the omitted wrapper comments are byte-neutral)")
    d1 = tempfile.mkdtemp(prefix="ba_d1_")
    st1, f1, _ = compile_kind(3, "finished", P, incs)
    fat = ("/*\n a comment block exactly like mainCpp's head\n*/\n\n"
           "// ==== MY PLAN ====\n// 1.\n// 2.\n\n") + incs
    st2, f2, _ = compile_kind(3, "finished", P, fat)
    chk("comments before the payload change nothing", f1 == f2 and f1, "%s vs %s" % (f1, f2))
    shutil.rmtree(d1, ignore_errors=True)

    print("\nCONTROL E (ARM 2 is LOUD on a seeded wrong figure, SILENT when clean)")
    tbl = {"16/finished": {"status": "PASS", "flash": 28600}}
    src = open(lesson_path(16), encoding="utf-8").read()
    bak = src
    try:
        clean = arm2_probe(tbl, 16)
        # The seed target is DERIVED, never spelled (rule 19). Pinning the literal
        # "28,600" left this control unable to land from S158 to S166.
        m = re.search(r"COMPILE CHECK</b> — ([\d,]+)", src)
        chk("the seed target was found by pattern, not by spelling", bool(m),
            m.group(1) if m else "no COMPILE CHECK figure in L16")
        seeded = src.replace(m.group(0), "COMPILE CHECK</b> — 27,999", 1) if m else src
        tbl = {"16/finished": {"status": "PASS",
                               "flash": int(m.group(1).replace(",", ""))}} if m else tbl
        chk("the seed landed in the intended shape", seeded != src)   # §24.6b
        open(lesson_path(16), "w", encoding="utf-8").write(seeded)
        loud = arm2_probe(tbl, 16)
        chk("seeded wrong figure is LOUD", 27999 in loud)
        chk("the same probe on the clean file did not report it", 27999 not in clean)
    finally:
        open(lesson_path(16), "w", encoding="utf-8").write(bak)
    chk("the lesson was restored byte-for-byte",
        open(lesson_path(16), encoding="utf-8").read() == bak)

    print("\nCONTROL F (the step->kind link is PARSED, and its absence is visible)")
    bl = step_blocks(16)
    chk("every L16 step block yielded a kind from its own catch-up link",
        all(b["kind"] for b in bl), "%d blocks" % len(bl))

    print("\nCONTROL G (the §16.23 declaration is READ, and its absence is LOUD)")
    d2 = declared_nobuild(2)
    chk("L02 declares broken_code with a reason", d2.get("broken_code"), str(d2.get("broken_code"))[:40])
    src = open(lesson_path(2), encoding="utf-8").read()
    bak = src
    try:
        stripped = re.sub(r' data-nobuild="[^"]*"', '', src, count=1)
        chk("the strip landed in the intended shape", stripped != src)
        open(lesson_path(2), "w", encoding="utf-8").write(stripped)
        chk("removing the attribute is LOUD", not declared_nobuild(2).get("broken_code"))
        empty = src.replace(re.search(r'data-nobuild="[^"]*"', src).group(0),
                            'data-nobuild=""', 1)
        open(lesson_path(2), "w", encoding="utf-8").write(empty)
        chk("an EMPTY reason does not count as a declaration",
            not declared_nobuild(2).get("broken_code"))
    finally:
        open(lesson_path(2), "w", encoding="utf-8").write(bak)
    chk("Lesson_02 restored byte-for-byte",
        open(lesson_path(2), encoding="utf-8").read() == bak)



    print("\nCONTROL I (ARM 6: a bank figure that NAMES a build is asserted)")
    import tempfile as _tf, shutil as _sh, glob as _g
    tbl6 = {"12/finished": {"status": "PASS", "flash": 24790},
            "10/finished": {"status": "PASS", "flash": 20592}}

    def _fixture(body):
        d = _tf.mkdtemp()
        open(os.path.join(d, "ZUMO_QUIZ_L99.yaml"), "w", encoding="utf-8").write(body)
        return d

    good = ('lesson: L99\nbank_version: "1.0.0"\nsets:\n  before:\n    questions:\n'
            '      - id: L99_B01\n        type: multiple_choice\n'
            '        stem: "Which build is it?"\n        options:\n'
            '          - text: "24,790 bytes"\n            correct: true\n'
            '            why: "That is Lesson 12 finished."\n')
    d = _fixture(good)
    try:
        cl = arm6(tbl6, quiz_dir=d)
        chk("clean labelled figure is SILENT", cl is True)
    finally:
        _sh.rmtree(d)

    d = _fixture(good.replace('"24,790 bytes"', '"24,694 bytes"'))
    try:
        chk("a stale figure beside its own label is LOUD", arm6(tbl6, quiz_dir=d) is False)
    finally:
        _sh.rmtree(d)

    # BLINDING: reword the sentence, keep the figure and the label correct.
    d = _fixture(good.replace('"Which build is it?"', '"Name the build this figure belongs to."'))
    try:
        chk("BLINDING: rewording a question is SILENT (the predicate is the claim)",
            arm6(tbl6, quiz_dir=d) is True)
    finally:
        _sh.rmtree(d)

    # The label and the figure split across text and why -- S165's actual shape.
    split = good.replace('            why: "That is Lesson 12 finished."',
                         '            why: "That is Lesson 12 finished, and it is 24,694."')
    d = _fixture(split)
    try:
        chk("a figure carried in the `why` beside the label is reached",
            arm6(tbl6, quiz_dir=d) is False)
    finally:
        _sh.rmtree(d)

    d = _tf.mkdtemp()   # no banks at all
    try:
        chk("ZERO labelled figures scanned does not pass (rule 27)",
            arm6(tbl6, quiz_dir=d) is False)
    finally:
        _sh.rmtree(d)

    chk("the real banks were never touched by this control",
        all(os.path.exists(f) for f in _g.glob(os.path.join(QUIZ_DIR, "ZUMO_QUIZ_L*.yaml"))))

    print("\nCONTROL H (ARM 4: the label figure is DERIVED, and drift is LOUD)")
    mbak = open(MAKER, encoding="utf-8").read()
    tbl_h = load_sizes() if os.path.exists(CACHE) else {}
    try:
        rows = [(L, k, lb, rf) for L, k, lb, rf in kind_rows()
                if re.search(r'\b\d{2},\d{3}\b', lb)]
        chk("the KINDS parser finds labels carrying a figure", bool(rows),
            "%d row(s)" % len(rows))
        chk("clean tree is SILENT", arm4(tbl_h) is True)

        # a wrong FIGURE is loud
        L, kid, lab, ref = rows[0]
        fig = re.search(r'\b(\d{2},\d{3})\b', lab).group(1)
        esc = lab.replace("\u2014", "\\u2014")
        bad = esc.replace(fig, format(int(fig.replace(",", "")) + 1, ","), 1)
        s2 = mbak.replace(esc, bad, 1)
        chk("the seed landed in the intended shape", s2 != mbak)
        open(MAKER, "w", encoding="utf-8").write(s2)
        chk("a wrong label figure is LOUD", arm4(tbl_h) is False)
        open(MAKER, "w", encoding="utf-8").write(mbak)

        # a wrong CLAUSE with a correct figure is loud (the S152 shape)
        m = re.search(r'(\d{1,3}(?:,\d{3})?) to spare', mbak)
        if m:
            s3 = mbak.replace(m.group(0),
                              format(int(m.group(1).replace(",", "")) + 1, ",")
                              + " to spare", 1)
            open(MAKER, "w", encoding="utf-8").write(s3)
            chk("a stale spare/over CLAUSE is LOUD (rule 51)", arm4(tbl_h) is False)
            open(MAKER, "w", encoding="utf-8").write(mbak)

        # BLINDING: reword a label, leave the figure alone -> must stay silent
        word = re.search(r'"(Step \d \\u2014 [A-Za-z ]+)', mbak)
        if word:
            s4 = mbak.replace(word.group(1), word.group(1) + " Now", 1)
            open(MAKER, "w", encoding="utf-8").write(s4)
            chk("BLINDING: rewording a label is SILENT (predicate is derived)",
                arm4(tbl_h) is True)
            open(MAKER, "w", encoding="utf-8").write(mbak)

        # COVERAGE: a parser that finds nothing must not pass
        chk("ZERO labels scanned does not pass", arm4({}, only=99) is False)
    finally:
        open(MAKER, "w", encoding="utf-8").write(mbak)
    chk("newproject.html restored byte-for-byte",
        open(MAKER, encoding="utf-8").read() == mbak)

    # ---- CONTROL J (ARM 7: a headroom claim equals ceiling minus a compile) ----
    # These live HERE, not in a session transcript. S167 and S168 each wrote a
    # claim-audit arm, each paid for it, and each threw it away with the session,
    # so S169 rebuilt it from scratch a third time. An arm whose controls do not
    # ship is an arm the next session pays for again.
    print("\nCONTROL J (ARM 7: HEADROOM claims)")
    l16 = os.path.join(HERE, "lessons", "Lesson_16.html")
    q16 = os.path.join(QUIZ_DIR, "ZUMO_QUIZ_L16.yaml")
    lbak = open(l16, encoding="utf-8").read()
    qbak = open(q16, encoding="utf-8").read()
    try:
        chk("clean tree is SILENT", arm7(tbl_h) is True)

        # the REAL S169 defect: SS7.4 promised the pre-rebaseline reserve
        chk("anchor: the SS7.4 reserve line is uniquely findable",
            lbak.count("You have <b>46 bytes</b>") == 1)
        if True:
            open(l16, "w", encoding="utf-8").write(
                lbak.replace("You have <b>46 bytes</b>", "You have <b>108 bytes</b>", 1))
            chk("a stale PROSE reserve is LOUD (the S169 defect)", arm7(tbl_h) is False)
            open(l16, "w", encoding="utf-8").write(lbak)

        # the REAL S169 bank defect, in a CORRECT answer
        chk("anchor: the A07 over-claim is uniquely findable",
            qbak.count("and still 272 over.") == 1)
        if True:
            open(q16, "w", encoding="utf-8").write(
                qbak.replace("and still 272 over.", "and still 210 over.", 1))
            chk("a stale OVER claim in a bank option is LOUD", arm7(tbl_h) is False)
            open(q16, "w", encoding="utf-8").write(qbak)

        # The conditional skip must be a PROPERTY, not a hole: drop the
        # subjunctive and the same sentence becomes an assertion, and fires.
        # ANCHORED ON THE LIVE OPTION, not the bare phrase. S169: the bare
        # phrase also occurs in this bank's own header narration, so the
        # first draft's count==1 guard SILENTLY SKIPPED this control and
        # printed nothing - which reads exactly like a control that passed.
        # A guard is an ASSERTION here, never a condition (rule 59).
        _cond = "buzzer would give \u2014 and the buzzer is left"
        chk("anchor: the conditional claim is uniquely findable",
            qbak.count(_cond) == 1)
        open(q16, "w", encoding="utf-8").write(
            qbak.replace(_cond, "buzzer gives \u2014 and the buzzer is left", 1))
        chk("a hypothetical made ASSERTIVE is LOUD (the skip is a property)",
            arm7(tbl_h) is False)
        open(q16, "w", encoding="utf-8").write(qbak)

        # STATED BLIND SPOT (rule 78), demonstrated rather than claimed: a wrong
        # build's headroom is still SOME build's headroom, and is silent.
        if True:
            open(l16, "w", encoding="utf-8").write(
                lbak.replace("You have <b>54 bytes</b>", "You have <b>270 bytes</b>", 1))
            chk("BLIND SPOT: a claim naming the WRONG build is SILENT",
                arm7(tbl_h) is True)
            open(l16, "w", encoding="utf-8").write(lbak)

        # COVERAGE: a parser that finds nothing must not pass (rule 27).
        # An empty quiz dir is NOT enough - the lessons still supply claims, so
        # that form of the control could never fail. Blind the patterns instead.
        import tempfile as _tf
        _sv = (A7_SPARE, A7_HAVE, A7_OVER)
        try:
            globals()["A7_SPARE"] = globals()["A7_HAVE"] = globals()["A7_OVER"] = \
                re.compile(r"(?!x)x")
            chk("ZERO headroom claims scanned does not pass",
                arm7(tbl_h, quiz_dir=_tf.mkdtemp()) is False)
        finally:
            globals()["A7_SPARE"], globals()["A7_HAVE"], globals()["A7_OVER"] = _sv
        chk("and the un-blinded arm is SILENT again", arm7(tbl_h) is True)
    finally:
        open(l16, "w", encoding="utf-8").write(lbak)
        open(q16, "w", encoding="utf-8").write(qbak)
    chk("Lesson_16.html restored byte-for-byte",
        open(l16, encoding="utf-8").read() == lbak)
    chk("ZUMO_QUIZ_L16.yaml restored byte-for-byte",
        open(q16, encoding="utf-8").read() == qbak)

    # ---- CONTROL K (ARM 8: a finished build warns only where somebody read) ----
    # ARM 8 takes a TABLE and touches no file, so these controls are synthetic
    # and cheap. That is a property worth keeping: a control that has to compile
    # is a control somebody eventually skips.
    #
    # S171: the baseline is now EMPTY, so this control supplies its OWN. It used
    # to lean on the live baseline holding four SWEEP_DONE entries; the day those
    # were fixed, a control written that way either fails or gets deleted. It
    # plants its own signature in its own fixture instead, and therefore tests
    # the ARM rather than the state of the book.
    print("\nCONTROL K (ARM 8: WARNINGS in finished builds)")
    import copy as _copy
    PLANT = "main.cpp: unused variable \u2018plantedByControlK\u2019 [-Wunused-variable]"

    # The fixture: the live table with ONE planted signature in ONE finished
    # build, and a synthetic baseline that adjudicates exactly that signature.
    # ANCHOR FIRST, as an ASSERTION - if fixture and baseline disagree, every
    # control below tests a fiction. S169's lesson: a guard is never a
    # condition (rule 59).
    fixture = _copy.deepcopy(tbl_h)
    fixture["16/finished"]["warn"] = sorted(fixture["16/finished"].get("warn", []) + [PLANT])
    BASE = {"16/finished": [PLANT]}

    chk("anchor: the LIVE table matches the LIVE baseline",
        arm8(tbl_h) is True)
    chk("anchor: the fixture matches its own synthetic baseline",
        arm8(fixture, baseline=BASE) is True)

    t = _copy.deepcopy(fixture)
    t["16/finished"]["warn"] = sorted(t["16/finished"]["warn"] +
        ["main.cpp: enumeration value \u2018MADE_UP\u2019 not handled in switch [-Wswitch]"])
    chk("a NEW warning in a finished build is LOUD", arm8(t, baseline=BASE) is False)

    t = _copy.deepcopy(fixture)
    t["16/finished"]["warn"] = [x for x in t["16/finished"]["warn"] if x != PLANT]
    chk("a baseline warning that VANISHED is LOUD (the baseline is stale too)",
        arm8(t, baseline=BASE) is False)

    # The build-up model is taken on trust in intermediate steps, and that is a
    # STATED blind spot (rule 78). Demonstrated, not claimed: the same planted
    # signature in a step payload is correctly SILENT.
    t = _copy.deepcopy(fixture)
    t["16/after_step_2"]["warn"] = sorted(t["16/after_step_2"].get("warn", []) + [PLANT])
    chk("BLIND SPOT: the same plant in an INTERMEDIATE step is SILENT",
        arm8(t, baseline=BASE) is True)

    # An EMPTY baseline must still assert. This is the live shape as of S171, and
    # it is the one a reader is most likely to mistake for "switched off".
    t = _copy.deepcopy(tbl_h)
    t["16/finished"]["warn"] = sorted(t["16/finished"].get("warn", []) + [PLANT])
    chk("with an EMPTY baseline, ANY finished warning is LOUD",
        arm8(t, baseline={}) is False)

    # COVERAGE, two ways. An empty table could pass vacuously, and a table whose
    # rows carry no warning data at all is what an older harness produces - the
    # exact condition under which "no warnings" is a lie.
    chk("an EMPTY table does not pass", arm8({}) is False)
    t = {k: {"status": v["status"], "flash": v["flash"]} for k, v in tbl_h.items()}
    chk("a table with NO warning data anywhere does not pass", arm8(t) is False)
    chk("and the un-blinded arm is SILENT again", arm8(tbl_h) is True)

    # ---- CONTROL L (ARM 9: an ignored StopReason is one somebody adjudicated) ----
    # ARM 9 recompiles 105 payloads and costs minutes, so its controls run on ONE
    # payload and on synthetic baselines. The alternative - a control that made
    # --selftest take four minutes - is a control somebody eventually skips
    # (S170's reason for keeping CONTROL K synthetic).
    print("\nCONTROL L (ARM 9: DISCARDED StopReason values)")

    # ANCHOR FIRST, as an ASSERTION. The transform must actually mark the header,
    # and it must leave every other file alone. If the marking silently failed,
    # every control below would pass on a payload that was never modified - the
    # exact way S169's guard-as-condition read like success (rule 59).
    _P = payloads()
    _h = ep.materialize(_P, "13", "after_step_5")["RobotMotion.h"]
    _marked = _discard_mark("RobotMotion.h", _h)
    chk("anchor: the transform marks all seven declarations",
        _marked.count("warn_unused_result") == 7 and _h.count("warn_unused_result") == 0)
    chk("anchor: the transform leaves main.cpp untouched",
        _discard_mark("main.cpp", "StopReason x();\n") == "StopReason x();\n")

    # Full-population runs belong to --discards. These use --lesson 13, which
    # stages 19 payloads rather than 105 and still exercises the real compile.

    chk("an EMPTY baseline makes every discard UNADJUDICATED",
        arm9(_P, head_includes(), only=13, baseline={}, quiet=True) is False)
    chk("the real baseline is SILENT on the same lesson",
        arm9(_P, head_includes(), only=13,
             baseline={k: v for k, v in DISCARD_BASELINE.items()
                       if k.startswith("13/")}, quiet=True) is True)
    # THE STANDING ASSERTION HAD NEVER BEEN EXERCISED. S172's double check found
    # it: arm9 refuses a discard in a `finished` build no matter what the baseline
    # says, and until this control that branch had never once run. An unexercised
    # branch is not a check - it is code that has never been asked a question.
    # The plant is a REAL one: the guard is stripped from one interruptible move
    # in 13/finished and the payload is really compiled, so this exercises the
    # compiler too, not just the bookkeeping.
    _real_mat = ep.materialize

    def _plant_finished(_P, _L, _k):
        f = dict(_real_mat(_P, _L, _k))
        if (_L, _k) == ("13", "finished") and isinstance(f.get("main.cpp"), str):
            f["main.cpp"] = f["main.cpp"].replace(
                "if (turnDegreesGyro(90.0 * sweepDir) == STOP_KILL) break;",
                "turnDegreesGyro(90.0 * sweepDir);", 1)
        return f

    _b13 = {k: v for k, v in DISCARD_BASELINE.items() if k.startswith("13/")}
    ep.materialize = _plant_finished
    try:
        chk("a discard in a FINISHED build is LOUD even when the baseline blesses it",
            arm9(_P, head_includes(), only=13,
                 baseline=dict(_b13, **{"13/finished": 1}), quiet=True) is False)
    finally:
        ep.materialize = _real_mat
    chk("and with the plant removed the same lesson is SILENT again",
        arm9(_P, head_includes(), only=13, baseline=_b13, quiet=True) is True)

    chk("a baseline expecting a discard that is NOT there is LOUD "
        "(a stale baseline is a defect the same way a stale figure is)",
        arm9(_P, head_includes(), only=13,
             baseline=dict({"13/finished": 2},
                           **{k: v for k, v in DISCARD_BASELINE.items()
                              if k.startswith("13/")}), quiet=True) is False)

    print()
    if fails:
        print("SELFTEST FAILED: " + ", ".join(fails))
        return 1
    print("ALL CONTROLS PASS - silent when clean, loud when broken.")
    return 0


def arm2_probe(tbl, L):
    """Return the set of figures ARM 2 would call unmatched for one lesson."""
    sizes = {v["flash"] for k, v in tbl.items()
             if int(k.split("/")[0]) == L and v["flash"]}
    out = set()
    for b in step_blocks(L):
        for f in ([b["heading_fig"]] if b["heading_fig"] else []) + b["compile_figs"]:
            if f not in sizes:
                out.add(f)
    return out


# ---------------------------------------------------------------- main


# ============================ ARM 9 =========================================
# DISCARDS: a StopReason that nobody reads is a kill switch nobody hears.
#
# S167 named this debt and handed it forward three times as "mark the
# declarations warn_unused_result". S172 measured it and RULED AGAINST SHIPPING
# THAT (Bible SS16.43): the flag would put warnings into four student-facing
# downloads whose lessons consider that code correct, and it would preempt L13
# Step 6b, which is built as DISCOVERY - run it, press B, watch the robot ignore
# you. A build-log line is a weaker teacher than a robot that will not stop, and
# this book has already measured that students read past build-log text.
#
# The debt was never "the attribute is not in the header". It was "nobody knows
# whether return values are being discarded". An ARM answers that permanently
# and the header stays clean.

DISCARD_DECL = re.compile(r'^(StopReason\s+\w+\([^;]*\));', re.M)
DISCARD_SIG = re.compile(r"ignoring return value of \u2018(\w+ \w+)")

# ADJUDICATED, and every line of this is a reading, not a tolerance. S172.
DISCARD_BASELINE = {
    # L13 Step 6b EXISTS to fix these two. They are the blind corner itself -
    # the builds a student runs to feel the kill switch do nothing. A discard
    # here is the lesson working.
    "13/after_step_5": 3,
    "13/after_step_6": 3,
    # A ladder rung: one gyro turn, no state machine, no kill machinery to hand
    # a reason back to.
    "13/ladder_7c_leg_and_turn": 1,
    # L12's encoder-vs-gyro comparison rungs. Bare fixed maneuvers, measured
    # against each other; there is no caller to report to.
    "12/cal_7d": 1,
    "12/cal_7e": 4,
    # L11 has NOT TAUGHT THE GUARD CONTRACT YET. These are correct for where the
    # STUDENT is, and they resolve on their own at L13. Guarding them would
    # import a rule from a lesson not yet read (SS24.19).
    "11/c1_backup": 1,
    "11/c2_hunt": 2,
}


def _discard_mark(fn, body):
    """Stage-time transform: mark the StopReason declarations, nothing else."""
    if fn == "RobotMotion.h":
        return DISCARD_DECL.sub(r"\1 __attribute__((warn_unused_result));", body)
    return body


def arm9(P, incs, only=None, baseline=None, quiet=False):
    """ARM 9 - DISCARDS: every ignored StopReason is one somebody adjudicated.

    -> True/False. The attribute is injected AT STAGE TIME and never lands in
    the repo, so what students download is unchanged. This is the arm's whole
    design: the instrument reads the book, the book does not wear the tool.

    THREE STATED SCOPE LIMITS (rule 78):
      1. IT COUNTS DISCARDS, NOT SITES THAT SHOULD GUARD. A move that is not
         called at all cannot discard, so deleting a maneuver LOWERS this count.
         Read it beside ARM 1, never alone.
      2. IT IS BLIND TO A DISCARD THE COMPILER CANNOT SEE - a return value
         assigned to a variable that is then never read is not -Wunused-result.
      3. IT RECOMPILES 105 PAYLOADS AND COSTS MINUTES, so it is NOT in --check's
         default path. An arm that made the routine run slower is an arm someone
         eventually skips (S170's reason for keeping CONTROL K synthetic).
    """
    base = DISCARD_BASELINE if baseline is None else baseline
    print("ARM 9 - DISCARDS: every ignored StopReason is one somebody adjudicated")
    ks = kinds(P)
    if only:
        ks = [x for x in ks if x[0] == only]
    got, staged = {}, 0
    for n, (L, k) in enumerate(ks, 1):
        d = tempfile.mkdtemp(prefix="ba9_")
        try:
            files = ep.materialize(P, str(L), k)
            if not isinstance(files.get("RobotMotion.h"), str):
                continue
            if "StopReason " not in files["RobotMotion.h"]:
                continue
            staged += 1
            for fn, body in files.items():
                body = body if body.endswith("\n") else body + "\n"
                if fn == "main.cpp":
                    body = incs + body
                body = _discard_mark(fn, body)
                open(os.path.join(d, fn), "w", encoding="utf-8").write(body)
            subprocess.run(["bash", os.path.join(HARNESS, "pio_harness.sh"), d],
                           capture_output=True, text=True)
            ep_err = os.path.join(d, "pbuild", "err.txt")
            txt = (open(ep_err, encoding="utf-8", errors="replace").read()
                   if os.path.exists(ep_err) else "")
            c = txt.count("unused-result")
            if c:
                got["%d/%s" % (L, k)] = c
        finally:
            shutil.rmtree(d, ignore_errors=True)
        if not quiet and n % 40 == 0:
            print("   ... %d payload(s) staged" % n, flush=True)

    if staged == 0:
        print("   NO payload carried the declarations - nothing was measured, "
              "and that is NOT a pass")
        return False

    tot = sum(got.values())
    print("   population: %d discard(s) over %d of %d payload(s) carrying the "
          "declarations" % (tot, len(got), staged))
    bad = False
    for k in sorted(set(got) | set(base), key=lambda x: (int(x.split("/")[0]), x)):
        want, have = base.get(k, 0), got.get(k, 0)
        if want == have:
            continue
        bad = True
        if want == 0:
            print("   %-34s %d discard(s), ADJUDICATED BY NOBODY" % (k, have))
        elif have == 0:
            print("   %-34s baseline expects %d and there are NONE - a stale "
                  "baseline is a defect the same way a stale figure is" % (k, want))
        else:
            print("   %-34s baseline %d, measured %d" % (k, want, have))
    # A finished build is the terminal, student-facing program. One discard
    # there is never explained by "something later fixes it".
    for k, v in got.items():
        if k.endswith("/finished"):
            print("   %-34s a FINISHED build discards - nothing comes later "
                  "to read it" % k)
            bad = True
    print("   %d adjudicated, %d unexplained" % (len(base), 0 if not bad else 1))
    return not bad


def main():
    a = sys.argv[1:]
    if not a or a[0] in ("-h", "--help"):
        print(__doc__)
        return 0
    if not os.path.exists(os.path.join(HARNESS, "libcore_lto.a")):
        print("byte_audit: no harness at %s — run pio_harness.sh --setup" % HARNESS)
        return 2
    print("byte_audit.py %s — the only instrument here that compiles.\n" % VERSION)

    if a[0] == "--selftest":
        return selftest()

    only = None
    if "--lesson" in a:
        only = int(a[a.index("--lesson") + 1])

    if a[0] == "--sizes" or not os.path.exists(CACHE):
        P = payloads()
        print("Compiling every payload the Maker defines...")
        tbl = build_sizes(P, only=only)
        if only and os.path.exists(CACHE):
            old = json.load(open(CACHE)); old.update(tbl); tbl = old
        json.dump(tbl, open(CACHE, "w"), indent=1)
        print("\n  size table -> %s\n" % CACHE)
        if a[0] == "--sizes":
            return 0

    if a[0] == "--discards":
        P = payloads()
        ok9 = arm9(P, head_includes(), only)
        print("byte_audit: " + ("PASS" if ok9 else "FAIL"))
        return 0 if ok9 else 1

    tbl = load_sizes()
    if a[0] == "--convention":
        arm3(tbl, only)
        return 0
    ok1 = arm1(tbl, only)
    ok2 = arm2(tbl, only)
    ok4 = arm4(tbl, only)
    ok5 = arm5(tbl, only)
    ok6 = arm6(tbl, only)
    ok7 = arm7(tbl, only)
    ok8 = arm8(tbl, only)
    arm2_leads(tbl, only)
    if a[0] == "--lesson" or "--convention" in a:
        arm3(tbl, only)
    ok = ok1 and ok2 and ok4 and ok5 and ok6 and ok7 and ok8
    print("byte_audit: " + ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
