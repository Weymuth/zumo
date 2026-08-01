# S103 — PUSH 4 · session_versions v1.12

**One file. One modify. No deletions. CLI only.**

| Action | File | Note |
|---|---|---|
| modify | `session_versions.py` | **v1.10 → v1.12** — CONTROL G, plus the syllabus added to the handoff block |

## Push

```
cd /path/to/zumo
git add session_versions.py
git status --short          # expect exactly ONE line: M session_versions.py
git commit -m "S103: session_versions v1.12 - CONTROL G registered-is-not-emitted; syllabus added to handoff block"
git push
```

## Verify

```
cd /tmp && rm -rf zv4
git clone --depth 1 https://github.com/Weymuth/zumo.git zv4
cd zv4
python3 session_versions.py --selftest    # ALL SEVEN CONTROLS PASS
python3 book_gates.py | tail -2           # ALL GATES PASS
```

`md5` should match `MD5_S103_push4.txt`.

## Why

`font_stack_sweep` was registered in `ARTEFACTS` and still never appeared in LIVE.md or the
handoff, because both emit templates name every instrument **by hand**. CONTROL E asks
"is it registered?"; nothing asked "is it emitted?". Found by reading the emitted block.

**CONTROL G** asserts every registered artefact appears in **both** blocks.

**And the second finding, which is the better one.** v1.11's G carried one exemption —
`Syllabus`, on the grounds it is emitted under its filename. True of `--live`. **False of
`--handoff`, where it appeared under neither name.** The exemption written to accommodate one
block silently excused a real gap in the other: the exact defect class G exists to catch.

DJ ruling: it belongs in both. So the syllabus is now in the handoff block and **G has no
exemptions at all.**

Both directions proved: strip `font_stack_sweep` from the templates → G fails on both blocks.
Strip the syllabus back out of the handoff → G fails by name. Restore → silent.

## This must land BEFORE the handoff is written

The handoff's version block is emitted **by this file**. Written against v1.10 it would omit
`font_stack_sweep` and the syllabus. Write-ordering rule, in a new place: the tool that emits
the record has to be correct before the record is written.
