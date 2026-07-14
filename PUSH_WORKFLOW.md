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

## Verification is unchanged

After you push, Claude still fresh-clones and md5-verifies every file, and checks WHICH
version landed. Nothing about the safety net changes — only your click count.

## If something looks wrong before you push

GitHub Desktop shows the full diff of every changed file *before* commit.
If a diff looks insane (e.g. a 5 MB file showing as 2 bytes — the old truncation signature),
**don't commit** — right-click the file → Discard changes, and tell Claude.
