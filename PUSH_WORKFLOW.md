# PUSH_WORKFLOW.md — Two-Click Pushes with GitHub Desktop

**For:** DJ · **Written:** S34 close · **Replaces:** the 6–8-click browser upload ritual
**Recommendation: GitHub Desktop** as the daily driver (purpose-built, shows diffs plainly).
VS Code's Source Control panel does the identical job if you're already in it.

---

## One-time setup (~5 minutes, do once, never again)

1. Open **GitHub Desktop** → sign in to your GitHub account (Preferences → Accounts) if it isn't already.
2. **File → Clone Repository** → pick `Weymuth/zumo` from the list → choose where it lives
   (e.g. `Documents\GitHub\zumo`) → **Clone**.
3. Done. You now have the whole live repo as a normal folder on disk:
   ```
   zumo\
     lessons\Lesson_01.html … Lesson_16.html
     images\
     newproject.html
     ROBOCUP_RESCUE_LINE_2026.md
     LIVE_ZUMO_TEXTBOOK.md
   ```

---

## Every push, from now on (2 clicks + a commit message)

1. **Copy the session's files into the folder**, overwriting what's there
   (Claude's delivery note always says which file replaces which).
2. Switch to GitHub Desktop. It has **already noticed** every change — each file is
   listed with a red/green diff you can eyeball.
3. Type a one-line summary in the box, bottom-left (e.g. `S35: header normalization L11-L16`)
   → **Commit to main** → **Push origin**.

That's it. One commit carries any number of files across any mix of folders —
lessons, images, the Maker, and root docs all go up together, in one shot.

---

## Why this kills two standing problems

- **The Maker rename bug is dead.** The 5.16 MB `newproject.html` truncation happened in the
  *browser's* rename step. On disk there is no rename step — the file goes up byte-exact.
  The Bible rule "never rename >1 MB files in the GitHub web UI" becomes moot.
- **Push order stops mattering for breakage windows.** SVGs + lessons + Maker land in ONE
  atomic commit, so there is no moment where a lesson is live but its images are not.
  (Claude will still list the ordered manifest out of habit; with single-commit pushes
  it's informational.)

## The renaming wrinkle (read once)

Claude's deliverables carry version names (`Lesson_10_Obstacles_v02_1_5.html`); the repo
uses stable names (`lessons/Lesson_10.html`). So the copy step includes a rename.
Two ways to make that painless:

- **Option A (proposed, needs your OK):** Claude delivers one **zip per session**, pre-arranged
  in repo layout with final names (`lessons/Lesson_10.html`, `images/…`). Your whole push:
  download zip → extract into the clone (overwrite) → Commit → Push. The versioned filenames
  still appear in the delivery table for the record; the zip carries the repo names.
- **Option B:** keep individual versioned files; you rename as you copy (Windows: F2, or
  copy-paste the name from Claude's table).

## Deletions — the one thing a file batch CANNOT carry

**A zip or a file-copy batch can only ADD and OVERWRITE. It can never delete.** So when a push
retires a file, the deletion is a separate act, and it is the step that gets missed — it has now
been missed twice (commit `fb70426`, and again at S84). Both times every overwrite went up cleanly
and only the deletion stayed behind, which is exactly what makes it easy to miss: the push *looks*
successful.

**Why it kept happening:** the procedure lived only in the session handoff — i.e. in the very file
being deleted. It disappeared at the moment it was needed and got re-authored from scratch each
session. That is why it now lives here instead.

**The procedure:**

1. **Delete the file in your local clone** (Windows Explorer / Finder — normal delete, not a rename).
2. In GitHub Desktop, the deleted file appears in the **Changes** list as **its own entry with its
   own checkbox**, usually marked with a red minus.
3. **Tick that checkbox.** If it is unticked the deletion stays out of the commit while every other
   change goes up.
4. Commit and push as normal.

**Verify a deletion exactly like a version — fresh clone, then list the root.** Never trust the
local working tree, and never assume a deletion rode along with a file-overwrite batch.

**The usual case is the session handoff.** After each push the repo root should carry exactly ONE
`ZUMO_SNN_HANDOFF.md`. `book_gates.py` gate 28 (§12.2) now asserts this, so a missed deletion fails
the gate at the next run instead of waiting to be noticed. Note `ZUMO_LEARNMODE_*_HANDOFF.md` also
matches "HANDOFF" but is a §19 learner-mode record, **not** a session handoff — leave it alone, and
the gate excludes it by construction.

## Verification is unchanged

After you push, Claude still fresh-clones and md5-verifies every file, and checks WHICH
version landed. Nothing about the safety net changes — only your click count.

## If something looks wrong before you push

GitHub Desktop shows the full diff of every changed file *before* commit.
If a diff looks insane (e.g. a 5 MB file showing as 2 bytes — the old truncation signature),
**don't commit** — right-click the file → Discard changes, and tell Claude.

## Matched pairs — some files cannot be pushed one at a time (S104)

`book_gates.py` calls `lesson_inventory.expand_classes()`. On S104 the gate file landed and the
parser did not, and the pushed tree could not run a single gate:

```
AttributeError: module 'lesson_inventory' has no attribute 'expand_classes'
```

Nothing rendered wrong, so nothing looked wrong. **A partial push of a matched pair is invisible
until something is run.** Known pairs: `book_gates.py` + `lesson_inventory.py`;
`build_css.py` + `css/book.css`; `image_audit.py` + `IMAGE_WORKLIST.md`; any instrument +
`session_versions.py` when the instrument is newly registered.

## Verify the DOWNLOADS, not just the push (S104)

S104 lost two pushes to stale browser downloads: older copies of the same filenames went up, and
one file landed as `lesson_inventory (1).py` — committed, unregistered, one character from the
real parser. Before committing, md5 each staged file against the list given in chat. A `(1)` in a
filename is the tell.

**After every push, not just at session open:**

```
python3 book_gates.py              # 41/41
python3 session_versions.py --selftest
python3 site_parity.py             # PARITY
```

`session_versions --selftest` CONTROL E is what caught the stray in seconds.
