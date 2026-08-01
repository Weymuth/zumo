# S103 — PUSH 3 · §27 THE CANVAS RULING

**One file. One modify. No deletions. CLI only.**

| Action | File | Note |
|---|---|---|
| modify | `ZUMO_SUPER_BIBLE.md` | **v8.89.1 → v8.90** — new §27, plus a conditional pointer on §6's inline rule |

---

## Push

```
cd /path/to/zumo
git add ZUMO_SUPER_BIBLE.md
git status --short          # expect exactly ONE line: M ZUMO_SUPER_BIBLE.md
git commit -m "S103: Bible v8.90 - 27 the book is a website, not a Canvas paste"
git push
```

## Verify

```
cd /tmp && rm -rf zumo_verify3
git clone --depth 1 https://github.com/Weymuth/zumo.git zumo_verify3
cd zumo_verify3
python3 session_versions.py --selftest    # ALL SIX CONTROLS PASS (CONTROL F checks v8.90)
python3 book_gates.py | tail -2           # ALL GATES PASS
```

`md5` should be `6305e844023d01a7f69eaac6651db657`.

---

## What §27 says

**The ruling.** Lessons live at one address — the published site. Canvas links to them and keeps
quizzes, grades, syllabus, submissions.

**§27.1 — the justification.** `site_parity.py` compares the repo to Pages. **Nothing has ever
compared Pages to Canvas.** A re-paste that did not happen was invisible to all 40 gates and to
you. One copy, one push, one truth.

**§27.2 — what it retires,** with the price that constraint has been charging, measured:

| | |
|---|---|
| inline `style=""` attributes | 25,036 |
| CSS declarations inside them | ~67,000 |
| share of lesson bytes | 44% (1.56 MB of 3.58 MB) |
| `font-family` declarations | 2,828, where a stylesheet needs 1 |
| absolute `weymuth.github.io` links | 473 |

Plus the line that matters most: **§26's repaint was never too hard, it was priced against the
wrong delivery model.**

**§27.3 — verified, not assumed.** Zero of the 40 gates enforce Canvas-safety. Checked before the
section was written.

**§27.4 — Canvas links point at the INDEX,** not sixteen deep links, which would rebuild the exact
update problem this solves. Also caps the exposure from a later robolore.com move, recorded as
your "later decision".

**§27.5 — fonts.** §17.3's SVG rule is untouched; an `<img>`-loaded graphic still cannot fetch a
webfont. The **page** is what changes. Recorded so nobody sweeps it twice: 2,828 declarations, 8
stacks, **0 broken** — the 422 Consolas-first code stacks are **parked**, because in a stylesheet
they are one line.

**§27.6 — the passages that rest on the retired constraint**, listed so they are annotated rather
than silently contradicted. §6's inline rule already carries its pointer; it is **not** rewritten
(§26.7).

**The section says plainly that the migration is not done by the ruling.** 25,036 attributes and
473 links are scheduled work with their own instrument and controls.
