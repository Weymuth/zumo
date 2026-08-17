#!/usr/bin/env python3
"""
quiz_bank.py - validate the reading-quiz banks and REPORT STATUS BY DERIVATION.

    python3 quizzes/quiz_bank.py --status     what exists, derived from the tree
    python3 quizzes/quiz_bank.py --check      validate every bank; exit 1 on any problem
    python3 quizzes/quiz_bank.py --selftest   prove the checker is LOUD when broken

WHY STATUS IS DERIVED AND NOT WRITTEN DOWN
    A hand-maintained "done so far" list is wrong the first time someone forgets to
    update it, and it is wrong SILENTLY. This reads the actual files in quizzes/ and
    reports what is there. There is no list to keep in sync, so there is nothing to
    drift. Same reasoning as Bible s24.13: re-derive from the tree, do not re-read
    from a list presented in prose.

WHY THE COUNTS ARE NEVER TYPED
    Every number this prints is computed. Do not hand-type a count into a handoff or
    into LIVE.md - run --status and copy what it says.

A LIBRARY MAY NOT EXIT. Import-safe: no sys.exit() outside main().

ONE VERSION HOME. The version lives ONLY in the VERSION constant below; this
docstring deliberately does not repeat it. Two homes with nothing comparing them
is how a version goes stale silently, and every printer here interpolates the
constant rather than spelling a number.
"""

import os
import re
import sys
import glob

VERSION = "v1.4.0"

QUIZ_DIR = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(QUIZ_DIR)
LESSON_GLOB = os.path.join(REPO, "lessons", "Lesson_*.html")
BANK_GLOB = os.path.join(QUIZ_DIR, "ZUMO_QUIZ_L*.yaml")

ALLOWED_TYPES = {"multiple_choice", "true_false", "matching"}

# Ruled S136: fill-in-the-blank is banned. Canvas string-matches it, so a capital
# letter or a stray paren locks a student out of build time over spelling.
BANNED_TYPES = {"fill_in_blank", "fill_in_the_blank", "short_answer", "essay"}


def _yaml():
    try:
        import yaml
        return yaml
    except ImportError:
        return None


def load(path):
    """Parse one bank. Returns (data, error_string_or_None)."""
    y = _yaml()
    if y is None:
        return None, "pyyaml not installed (pip install pyyaml --break-system-packages)"
    try:
        with open(path, encoding="utf-8") as fh:
            return y.safe_load(fh), None
    except Exception as exc:                      # noqa: BLE001
        return None, "unparseable: %s" % exc


BANK_VER_RE = re.compile(r"^#\s*Bank version:\s*v?([0-9]+(?:\.[0-9]+)*)\s*$", re.M)


def version_homes(src, data, name):
    """A bank states its version TWICE and until S161 nothing compared them.

    The `# Bank version:` comment is the home a HUMAN reads; the
    `bank_version:` field is the home --status and every tool reads. At S161
    eight of nine bumped banks disagreed - seven fields still read 1.0.0 after
    two rounds of edits, so --status reported the ORIGINAL version of a bank
    that had been re-keyed twice. That is the sB version-homes shape in a new
    construct: a second home earns its keep only when something reads it that
    cannot read the first, and here BOTH are read, by different readers.

    The comparison is on the PARSED value against the RAW comment, because
    safe_load discards comments - the field alone can never see its twin.
    """
    bad = []
    hits = BANK_VER_RE.findall(src or "")
    field = str((data or {}).get("bank_version", "")).strip()
    if not hits:
        bad.append("%s: no '# Bank version:' comment - the human-read home "
                   "is missing, so nothing can disagree and nothing can check"
                   % name)
    elif len(hits) > 1:
        bad.append("%s: %d '# Bank version:' comments - one home, one spelling"
                   % (name, len(hits)))
    if not field:
        bad.append("%s: bank_version field is empty or absent" % name)
    if hits and field and hits[0] != field:
        bad.append("%s: version homes DISAGREE - comment says v%s, "
                   "bank_version field says %s. --status reads the FIELD, so "
                   "an edited bank keeps reporting its old version"
                   % (name, hits[0], field))
    return bad



SOURCE_PIN_RE = re.compile(r"^\s*(lesson_\d{2})\s*:\s*[\"']?(v[\d.]+)[\"']?\s*$", re.M)



# ---------------------------------------------------------------------------
# THE S162 UNREAD-PIN BACKLOG, NAMED RATHER THAN COUNTED (§25.2a).
#
# 52 pins were stale at S162. FOUR were bumped on EVIDENCE - lesson_04
# v04.29.0 -> v04.29.1, whose entire diff is the version comment plus S151's
# `<title>` em-dash separator, a tag that does not render and that no bank
# cites - and the diff was READ, not inferred from a section-level "(none)".
#
# THE OTHER 48 OWE A REAL READ AND S162 DID NOT DO IT. The scoping attempt is
# recorded because its FAILURE is the finding: flagging questions that share
# vocabulary with text that moved returned **3,146 of ~3,400 question-instances**,
# naming 71 of 75 questions off a 30-sentence diff. A predicate that returns
# nearly the whole population has measured nothing (rule 79). No cheap predicate
# separates an at-risk question from a safe one here, so the honest cost is the
# READ -> FIX -> QUIZ arc, per lesson, and that is not one session's work.
#
# WHY A NAMED BACKLOG RATHER THAN A HARD FAIL OR NO GATE AT ALL:
#   * A permanently red gate trains its readers to ignore red, which is worse
#     than no gate (v8.130's shape: a check that punishes the attentive).
#   * Bulk-bumping 48 pins would assert 3,146 reads nobody performed - rule 37
#     at scale, and exactly what S161 correctly declined for 3 of 52.
#   * Naming them means NEW drift fails immediately, a pin bumped WITHOUT its
#     read fails (the name no longer matches), and the list can only SHRINK.
#     A count could do none of those three.
UNREAD_PINS = {
        ("ZUMO_QUIZ_L01.yaml", "lesson_01"): "v03.28.3",
        ("ZUMO_QUIZ_L02.yaml", "lesson_01"): "v03.28.2",
        ("ZUMO_QUIZ_L02.yaml", "lesson_02"): "v03.21.2",
        ("ZUMO_QUIZ_L03.yaml", "lesson_02"): "v03.21.2",
        ("ZUMO_QUIZ_L03.yaml", "lesson_03"): "v03.41.0",
        ("ZUMO_QUIZ_L04.yaml", "lesson_02"): "v03.21.2",
        ("ZUMO_QUIZ_L04.yaml", "lesson_03"): "v03.41.0",
        ("ZUMO_QUIZ_L06.yaml", "lesson_06"): "v04.32.1",
        ("ZUMO_QUIZ_L07.yaml", "lesson_06"): "v04.32.1",
        ("ZUMO_QUIZ_L07.yaml", "lesson_07"): "v04.31.2",
        ("ZUMO_QUIZ_L08.yaml", "lesson_07"): "v04.31.3",
        ("ZUMO_QUIZ_L09.yaml", "lesson_06"): "v04.32.1",
        ("ZUMO_QUIZ_L09.yaml", "lesson_08"): "v04.31.0",
        ("ZUMO_QUIZ_L09.yaml", "lesson_09"): "v05.27.0",
        ("ZUMO_QUIZ_L10.yaml", "lesson_06"): "v04.32.1",
        ("ZUMO_QUIZ_L10.yaml", "lesson_08"): "v04.31.0",
        ("ZUMO_QUIZ_L10.yaml", "lesson_09"): "v05.27.0",
        ("ZUMO_QUIZ_L10.yaml", "lesson_10"): "v02.29.1",
        ("ZUMO_QUIZ_L11.yaml", "lesson_03"): "v03.41.0",
        ("ZUMO_QUIZ_L11.yaml", "lesson_06"): "v04.32.1",
        ("ZUMO_QUIZ_L11.yaml", "lesson_08"): "v04.31.1",
        ("ZUMO_QUIZ_L11.yaml", "lesson_10"): "v02.29.1",
        ("ZUMO_QUIZ_L11.yaml", "lesson_11"): "v02.30.0",
        ("ZUMO_QUIZ_L12.yaml", "lesson_06"): "v04.32.1",
        ("ZUMO_QUIZ_L12.yaml", "lesson_09"): "v05.27.0",
        ("ZUMO_QUIZ_L12.yaml", "lesson_11"): "v02.30.0",
        ("ZUMO_QUIZ_L12.yaml", "lesson_12"): "v01.31.3",
        ("ZUMO_QUIZ_L13.yaml", "lesson_03"): "v03.41.0",
        ("ZUMO_QUIZ_L13.yaml", "lesson_06"): "v04.32.1",
        ("ZUMO_QUIZ_L13.yaml", "lesson_10"): "v02.29.1",
        ("ZUMO_QUIZ_L13.yaml", "lesson_11"): "v02.30.0",
        ("ZUMO_QUIZ_L13.yaml", "lesson_12"): "v01.31.3",
        ("ZUMO_QUIZ_L13.yaml", "lesson_13"): "v02.29.0",
        ("ZUMO_QUIZ_L14.yaml", "lesson_08"): "v04.31.1",
        ("ZUMO_QUIZ_L14.yaml", "lesson_11"): "v02.30.0",
        ("ZUMO_QUIZ_L14.yaml", "lesson_12"): "v01.31.3",
        ("ZUMO_QUIZ_L14.yaml", "lesson_13"): "v02.29.0",
        ("ZUMO_QUIZ_L14.yaml", "lesson_14"): "v02.34.0",
        ("ZUMO_QUIZ_L15.yaml", "lesson_06"): "v04.32.1",
        ("ZUMO_QUIZ_L15.yaml", "lesson_08"): "v04.31.1",
        ("ZUMO_QUIZ_L15.yaml", "lesson_11"): "v02.30.0",
        ("ZUMO_QUIZ_L15.yaml", "lesson_14"): "v02.34.0",
        ("ZUMO_QUIZ_L15.yaml", "lesson_15"): "v02.31.0",
        ("ZUMO_QUIZ_L16.yaml", "lesson_01"): "v03.28.3",
        ("ZUMO_QUIZ_L16.yaml", "lesson_02"): "v03.21.2",
        ("ZUMO_QUIZ_L16.yaml", "lesson_14"): "v02.34.0",
        ("ZUMO_QUIZ_L16.yaml", "lesson_15"): "v02.31.0",
        ("ZUMO_QUIZ_L16.yaml", "lesson_16"): "v02.23.0",
}


def source_pins(data, name, lesson_versions):
    """A bank's `source:` block is its VERIFIED-AGAINST pin, and until S162
    nothing compared it to anything.

    §24.18 one layer along: a pin nothing compares is a version home with no
    comparator. Measured at S161 close and again at S162 open: **52 of 57 pins
    were stale**, drift accumulated S148-S161, and `--status` printed every one
    of them as provenance.

    S162 also found the banks stating provenance TWICE and disagreeing - the
    header `# Authored against:` comment against this YAML block - in SEVEN of
    sixteen banks, and **the disagreement ran BOTH directions** (six
    header-newer, L08 field-newer), so neither home was reliably the fresher
    one and neither could simply be preferred. Ruled at S162:

      * `source:`               = VERIFIED against. Gated. Must equal live.
      * `# Authored against:`   = HISTORY. Ungated, never rewritten (rule 37).

    Bumping a pin therefore ASSERTS A READ. That is why S161 correctly declined
    to bump 3 of 52: a tree where some pins are verified and some are stale with
    nothing marking which is worse than one uniformly out of date and known to
    be (S148's L14 reasoning).

    `lesson_versions` is passed IN rather than derived here, so the caller owns
    the denominator (rule 29) and this function has exactly one job.
    """
    bad = []
    src = (data or {}).get("source") or {}
    if not src:
        bad.append("%s: no `source:` block - a bank with no pin cannot be stale "
                   "and cannot be checked" % name)
        return bad
    for key in sorted(src):
        pinned = str(src[key]).strip()
        if key not in lesson_versions:
            bad.append("%s: `source:` pins %s, which is not a lesson in this "
                       "book" % (name, key))
            continue
        live = lesson_versions[key]
        # The backlog is keyed on (bank, lesson) and CARRIES the version it was
        # recorded stale at. Keying it on the pinned version instead was the first
        # draft, and CONTROL C2 killed it: bumping a pin made its own backlog entry
        # unfindable, so the gate went SILENT on exactly the move it exists to catch.
        # A backlog you can abandon by editing the thing it tracks is not a backlog.
        recorded = UNREAD_PINS.get((name, key))
        if recorded is None:
            if pinned != live:
                bad.append("%s: `source:` pins %s at %s but the live lesson is %s, "
                           "and this pin is NOT in the S162 UNREAD_PINS backlog - it "
                           "is NEW drift. Either read the bank against the live "
                           "lesson and bump the pin, or add it to the backlog "
                           "deliberately (§24.18)" % (name, key, pinned, live))
        elif pinned != recorded:
            bad.append("%s: `source:` pins %s at %s, but UNREAD_PINS records it stale "
                       "at %s. The pin MOVED while still in the backlog. If the read "
                       "was done, delete the backlog entry in the same commit; if it "
                       "was not, the bump asserts a read nobody performed (rule 37)"
                       % (name, key, pinned, recorded))
    return bad


def validate(data, name):
    """Return a list of problem strings. Empty list means clean."""
    bad = []
    if not isinstance(data, dict):
        return ["%s: top level is not a mapping" % name]

    for key in ("lesson", "bank_version", "source", "sets"):
        if key not in data:
            bad.append("%s: missing top-level key '%s'" % (name, key))
    if bad:
        return bad

    seen = set()
    for set_name, block in data["sets"].items():
        if set_name not in ("before", "after"):
            bad.append("%s: unknown set '%s' (expected before/after)" % (name, set_name))
        questions = block.get("questions") or []
        if not questions:
            bad.append("%s/%s: no questions" % (name, set_name))
        for q in questions:
            qid = q.get("id", "<no id>")
            tag = "%s/%s/%s" % (name, set_name, qid)

            if qid in seen:
                bad.append("%s: duplicate question id" % tag)
            seen.add(qid)

            qtype = q.get("type")
            if qtype in BANNED_TYPES:
                bad.append("%s: type '%s' is BANNED - Canvas string-matches it "
                           "and a capital letter fails a correct answer" % (tag, qtype))
                continue
            if qtype not in ALLOWED_TYPES:
                bad.append("%s: unknown type '%s'" % (tag, qtype))
                continue

            # Every question owes a citation. A miss has to tell the student
            # where to re-read - that is the whole contract of a soft gate.
            if not q.get("cite"):
                bad.append("%s: no cite - a wrong answer cannot point anywhere" % tag)
            if not q.get("stem"):
                bad.append("%s: no stem" % tag)
            if not isinstance(q.get("points"), int):
                bad.append("%s: points missing or not an integer" % tag)

            if qtype == "multiple_choice":
                opts = q.get("options") or []
                n_right = sum(1 for o in opts if o.get("correct"))
                if len(opts) < 3:
                    bad.append("%s: only %d options" % (tag, len(opts)))
                if n_right != 1:
                    bad.append("%s: %d correct options, expected exactly 1" % (tag, n_right))
                texts = [o.get("text") for o in opts]
                if len(set(texts)) != len(texts):
                    bad.append("%s: duplicate option text" % tag)

            elif qtype == "true_false":
                if not isinstance(q.get("correct"), bool):
                    bad.append("%s: 'correct' must be true or false" % tag)

            elif qtype == "matching":
                pairs = q.get("pairs") or []
                if len(pairs) < 3:
                    bad.append("%s: only %d pairs" % (tag, len(pairs)))
                rights = [p.get("right") for p in pairs]
                if len(set(rights)) != len(rights):
                    bad.append("%s: duplicate right-hand answers - two prompts "
                               "would both be correct" % tag)
                # Without distractors, knowing n-1 pairs gives the last one free.
                if not q.get("extra_answers"):
                    bad.append("%s: matching with no extra_answers - elimination "
                               "hands the last pair to anyone who knows the rest" % tag)
    return bad


def summarize(data):
    """Counts per set. Every number here is computed, never typed."""
    out = {}
    for set_name, block in (data.get("sets") or {}).items():
        questions = block.get("questions") or []
        mix = {}
        points = 0
        for q in questions:
            mix[q.get("type")] = mix.get(q.get("type"), 0) + 1
            points += q.get("points") or 0
        out[set_name] = {"n": len(questions), "mix": mix, "points": points}
    return out


def lesson_numbers():
    return sorted(re.search(r"_(\d+)\.html", p).group(1)
                  for p in glob.glob(LESSON_GLOB))


def bank_for(num):
    path = os.path.join(QUIZ_DIR, "ZUMO_QUIZ_L%s.yaml" % num)
    return path if os.path.exists(path) else None


def status():
    """Derived progress report. Reads the tree; keeps no list."""
    nums = lesson_numbers()
    print("quiz_bank.py %s - status DERIVED from %s" % (VERSION, QUIZ_DIR))
    print()
    done = 0
    total_q = 0
    for num in nums:
        path = bank_for(num)
        if not path:
            print("  L%s   -- no bank" % num)
            continue
        data, err = load(path)
        if err:
            print("  L%s   !! %s" % (num, err))
            continue
        problems = validate(data, os.path.basename(path))
        s = summarize(data)
        b = s.get("before", {})
        a = s.get("after", {})
        n = b.get("n", 0) + a.get("n", 0)
        total_q += n
        done += 1
        flag = "OK " if not problems else "%d PROBLEM(S)" % len(problems)
        print("  L%s   before=%-3d after=%-3d  total=%-3d  bank v%s  [%s]"
              % (num, b.get("n", 0), a.get("n", 0), n,
                 data.get("bank_version", "?"), flag))
        src = data.get("source") or {}
        pin = ", ".join("%s=%s" % (k, v) for k, v in sorted(src.items()))
        print("         authored against: %s" % pin)
    print()
    print("  %d of %d lessons have a bank. %d questions total."
          % (done, len(nums), total_q))
    if done < len(nums):
        missing = [n for n in nums if not bank_for(n)]
        print("  STILL TO WRITE: %s" % " ".join("L" + m for m in missing))
    return done, len(nums), total_q


def check(verbose=True):
    """Validate every bank. Returns a list of problems.

    A SCAN THAT FOUND NOTHING IS NOT A SCAN THAT FOUND NOTHING WRONG.
    Until S153 an empty glob returned [] and main() exited 0, so moving every
    bank aside - or running from the wrong tree, or a rename - read as "banks
    are fine" to anyone checking by hand. A hold that is also satisfied by an
    accident is not a hold. Zero banks scanned is now a PROBLEM.
    """
    all_bad = []
    banks = sorted(glob.glob(BANK_GLOB))
    if not banks:
        all_bad.append("no banks found in %s - zero banks scanned is a "
                       "PROBLEM, not a clean result" % QUIZ_DIR)
        if verbose:
            print("  %s" % all_bad[0])
        return all_bad
    for path in banks:
        name = os.path.basename(path)
        data, err = load(path)
        if err:
            all_bad.append("%s: %s" % (name, err))
            continue
        all_bad.extend(validate(data, name))
        try:
            with open(path, encoding="utf-8") as fh:
                all_bad.extend(version_homes(fh.read(), data, name))
        except OSError as exc:                          # noqa: BLE001
            all_bad.append("%s: could not re-read for version homes: %s"
                           % (name, exc))
    if verbose:
        if all_bad:
            print("  %d problem(s):" % len(all_bad))
            for b in all_bad:
                print("    - %s" % b)
        else:
            print("  %d bank(s) valid" % len(banks))
    return all_bad


# ----------------------------------------------------------------------
# SELFTEST
# Break a synthetic bank on purpose and confirm the checker is LOUD.
# The controls run against banks built in memory - they never touch the
# real files, because a control that depends on the state of what it
# audits is not a control.
# ----------------------------------------------------------------------
def _good_bank():
    return {
        "lesson": "L99", "bank_version": "1.0.0",
        "source": {"lesson_99": "v01.0.0"},
        "sets": {"before": {"questions": [
            {"id": "X1", "type": "multiple_choice", "cite": "1", "points": 1,
             "stem": "s", "options": [{"text": "a", "correct": True},
                                      {"text": "b"}, {"text": "c"}]},
            {"id": "X2", "type": "true_false", "cite": "1", "points": 1,
             "stem": "s", "correct": False},
            {"id": "X3", "type": "matching", "cite": "1", "points": 3, "stem": "s",
             "pairs": [{"left": "p", "right": "1"}, {"left": "q", "right": "2"},
                       {"left": "r", "right": "3"}],
             "extra_answers": ["4"]},
        ]}},
    }


def selftest():
    import copy
    controls = []

    base = _good_bank()
    controls.append(("A  clean bank is SILENT", validate(base, "t") == []))

    b = copy.deepcopy(base)
    b["sets"]["before"]["questions"][0]["options"][1]["correct"] = True
    controls.append(("B  two correct options is LOUD",
                     any("2 correct options" in x for x in validate(b, "t"))))

    b = copy.deepcopy(base)
    del b["sets"]["before"]["questions"][0]["cite"]
    controls.append(("C  missing cite is LOUD",
                     any("no cite" in x for x in validate(b, "t"))))

    b = copy.deepcopy(base)
    del b["sets"]["before"]["questions"][2]["extra_answers"]
    controls.append(("D  matching without distractors is LOUD",
                     any("no extra_answers" in x for x in validate(b, "t"))))

    b = copy.deepcopy(base)
    b["sets"]["before"]["questions"][2]["pairs"][1]["right"] = "1"
    controls.append(("E  duplicate right-hand answer is LOUD",
                     any("duplicate right-hand" in x for x in validate(b, "t"))))

    b = copy.deepcopy(base)
    b["sets"]["before"]["questions"][1]["type"] = "fill_in_blank"
    controls.append(("F  a banned type is LOUD",
                     any("BANNED" in x for x in validate(b, "t"))))

    b = copy.deepcopy(base)
    b["sets"]["before"]["questions"][1]["id"] = "X1"
    controls.append(("G  duplicate id is LOUD",
                     any("duplicate question id" in x for x in validate(b, "t"))))

    b = copy.deepcopy(base)
    b["sets"]["before"]["questions"][0]["options"] = [{"text": "a", "correct": True},
                                                      {"text": "b"}]
    controls.append(("H  too few options is LOUD",
                     any("only 2 options" in x for x in validate(b, "t"))))

    b = copy.deepcopy(base)
    b["sets"]["before"]["questions"][1]["correct"] = "yes"
    controls.append(("I  non-boolean true_false answer is LOUD",
                     any("must be true or false" in x for x in validate(b, "t"))))

    # CONTROL J - BOTH DIRECTIONS, and it must fire for the RIGHT reason.
    # A control that is loud on an empty directory is worthless if it is also
    # loud on a populated one, so J asserts the silent direction too. It runs
    # against temp directories and never reads or writes quizzes/ - a control
    # that depends on the state of what it audits is not a control.
    import tempfile
    global BANK_GLOB
    _saved_glob = BANK_GLOB
    try:
        with tempfile.TemporaryDirectory() as td:
            BANK_GLOB = os.path.join(td, "ZUMO_QUIZ_L*.yaml")
            empty_loud = any("zero banks scanned" in x
                             for x in check(verbose=False))

            y = _yaml()
            if y is None:
                populated_silent = None
            else:
                with open(os.path.join(td, "ZUMO_QUIZ_L99.yaml"), "w",
                          encoding="utf-8") as fh:
                    # safe_dump writes no comments, so the fixture must state
                    # the human-read home itself or version_homes fires on it
                    # (correctly) and J2 reports a defect that is its own.
                    fh.write("# Bank version: v%s\n"
                             % _good_bank()["bank_version"])
                    y.safe_dump(_good_bank(), fh)
                populated_silent = check(verbose=False) == []
    finally:
        BANK_GLOB = _saved_glob

    # ---- VERSION HOMES (S161). In-memory: a control that depends on the
    # state of what it audits is not a control.
    _vsrc = "# Bank version: v1.0.2\nlesson: L99\n"
    _vdat = {"bank_version": "1.0.2"}
    controls.append(("K  agreeing version homes are SILENT",
                     version_homes(_vsrc, _vdat, "t") == []))
    controls.append(("L  disagreeing version homes are LOUD",
                     any("DISAGREE" in x for x in
                         version_homes(_vsrc, {"bank_version": "1.0.0"}, "t"))))
    controls.append(("M  a MISSING version comment is LOUD",
                     any("no '# Bank version:'" in x for x in
                         version_homes("lesson: L99\n", _vdat, "t"))))
    controls.append(("N  TWO version comments are LOUD",
                     any("one home, one spelling" in x for x in
                         version_homes(_vsrc + "# Bank version: v1.0.3\n",
                                       _vdat, "t"))))
    controls.append(("O  an ABSENT bank_version field is LOUD",
                     any("field is empty or absent" in x for x in
                         version_homes(_vsrc, {}, "t"))))
    # BLINDING CONTROL: the arm measures VERSIONS, not banks. Rewriting a
    # question must leave it silent, or it is not measuring the property.
    controls.append(("P  rewording a QUESTION is SILENT to version homes",
                     version_homes(_vsrc + 'stem: "reworded"\n',
                                   _vdat, "t") == []))

    # ---- source_pins controls (S162). ADDED BECAUSE THE S162 DOUBLE CHECK FOUND
    # THE FUNCTION CONTROLLED ONLY FROM book_gates AND NOT HERE - S153's shape, a
    # function whose only control lives in a different tool. Each control builds its
    # OWN fixture rather than reusing _good_bank(), whose `source:` deliberately
    # carries `lesson_99`: source_pins would correctly flag that, so reusing it
    # would fail and read as an ARM defect when it is a FIXTURE defect (S161's
    # control-J2 finding verbatim - the fixture was incomplete, not the arm).
    _plive = {"lesson_07": "v04.31.4"}
    controls.append(("Q  a pin MATCHING the live lesson is SILENT",
                     source_pins({"source": {"lesson_07": "v04.31.4"}}, "t",
                                 _plive) == []))
    controls.append(("R  a stale pin NOT in the backlog is LOUD",
                     any("NEW drift" in x for x in
                         source_pins({"source": {"lesson_07": "v04.31.2"}}, "t",
                                     _plive))))
    controls.append(("S  a pin naming a NON-lesson is LOUD",
                     any("not a lesson in this book" in x for x in
                         source_pins({"source": {"lesson_99": "v01.0.0"}}, "t",
                                     _plive))))
    controls.append(("T  a MISSING source: block is LOUD",
                     any("no `source:` block" in x for x in
                         source_pins({}, "t", _plive))))
    # A backlog entry whose pin has MOVED is loud even when it moved to the RIGHT
    # value - because the read is what earns the bump, and the entry must be
    # deleted in the same commit. This is the arm CONTROL C2 forced into existence.
    _bk = list(UNREAD_PINS.items())[0]
    (_bname, _blesson), _bver = _bk
    controls.append(("U  a BACKLOG pin that has moved is LOUD",
                     any("MOVED while still in the backlog" in x for x in
                         source_pins({"source": {_blesson: "v99.99.99"}}, _bname,
                                     {_blesson: "v99.99.99"}))))
    # BLINDING CONTROL: the arm measures PINS. Rewording a question must be silent.
    controls.append(("V  rewording a QUESTION is SILENT to source pins",
                     source_pins({"source": {"lesson_07": "v04.31.4"},
                                  "sets": {"before": {"questions":
                                      [{"stem": "reworded"}]}}}, "t", _plive) == []))

    controls.append(("J  an EMPTY scan is LOUD", empty_loud))
    controls.append(("J2 a populated scan is still SILENT",
                     populated_silent is not False))

    ok = True
    print("quiz_bank.py %s SELFTEST - silent when clean, loud when broken" % VERSION)
    for label, passed in controls:
        print("   %-46s %s" % (label, "PASS" if passed else "*** FAIL ***"))
        ok = ok and passed
    print()
    print("ALL CONTROLS PASS" if ok else "*** SELFTEST FAILED - do not trust --check ***")
    return ok


def main(argv):
    if "--selftest" in argv:
        return 0 if selftest() else 1
    if "--check" in argv:
        print("quiz_bank.py %s --check" % VERSION)
        problems = check()
        return 1 if problems else 0
    if "--status" in argv or len(argv) == 1:
        status()
        return 0
    print("quiz_bank.py %s" % VERSION)
    print(__doc__)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
