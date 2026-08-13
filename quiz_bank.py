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

VERSION = "v1.0.1"

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
                    y.safe_dump(_good_bank(), fh)
                populated_silent = check(verbose=False) == []
    finally:
        BANK_GLOB = _saved_glob

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
