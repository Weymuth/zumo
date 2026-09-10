<!-- ZUMO_SHOOT_LIST_F26_Sep3.md v1.2 — derived from IMAGE_WORKLIST.md (image_audit v1.3),
     which is generated. Fourteen tags outstanding of 144 planned. This file sorts those
     fourteen by whether DJ can shoot them tomorrow morning; it invents no tag and drops none.
     v1.1 (S201): DJ answered both gates — the walled rescue zone and the delrin sheet are in the
     room, and a robot will be running the TRIM sketch. 13.1, 12.1 and 3.6 moved into section A.
     v1.2 (S201): DJ ruled TILES — students place them. L04 §4.3 is rewritten and IMAGE 4.3 is
     now a single shot of a straight-line tile. Working document — not a book artefact. -->

# Shoot List — Thursday September 3 AM
### Fourteen outstanding figure tags, sorted by what tomorrow can actually close

**Read this first.** Shooting a photo does not land it. A tag is LANDED only when an `<img>`
in that lesson points at a file whose name encodes the tag. Shoot and name; I wire.

**Filename rule — exact, or the audit will not see the file.**
`L{lesson, two digits}_IMAGE_{lesson}-{number, two digits}_snake_case_words.jpg`
Second number is zero-padded. Examples: `L03_IMAGE_3-02_floor_test_setup.jpg`,
`L04_IMAGE_4-03_test_surface.jpg`. A `GRAPHIC` and an `IMAGE` with the same number are
different figures — never rename one into the other.

Shoot landscape, phone is fine, room lighting, no flash. Fill the frame with the subject.

---

## A — SHOOT TOMORROW (6 photos, one robot, one table, one floor)

### 1. `L03_IMAGE_3-02_*` — Motor testing setup, clear floor space
**Lesson 3 §4, "Recommended motor testing setup showing clear floor space."**
Floor, robot at a starting line, clear runway ahead. The lesson tells students to use a
Post-it as the start line and more Post-its to mark where each run ends — so put the Post-it
start line in the shot. One run is about 59 cm; frame enough floor to show the runway is clear.

### 2. `L03_IMAGE_3-05_*` — Testing setup with tape start line
**Lesson 3 §7 checklist, "robot on floor, tape starting line marking start position, clear path ahead."**
Same floor, but a **tape** start line rather than Post-its, robot squared up on it, path ahead
empty. Shoot low, roughly at robot height, looking down the runway.
*Distinct from 3.2 on purpose: 3.2 is the setup you build, 3.5 is the robot in position at check time.*

### 3. `L03_IMAGE_3-06_*` — Serial Monitor log, several TRIM trials
**Screen capture, not a room photo.** The Serial Monitor showing several test runs with TRIM
climbing — the placeholder names 0 → 15. Needs a robot running the L03 TRIM Finder, which you
said to plan on. Capture the window with **several trials visible in one scroll** — the pattern
across trials is the point, not any single line. Crop to the log, not the whole screen.

### 4. `L04_IMAGE_4-03_*` — A ready test surface
**Lesson 4 §4.3, rewritten this session to your ruling.** One **straight-line course tile** — a
single black line running edge to edge, no curve, no intersection, no gap. Lay it flat, shoot
from **directly above**, whole tile in frame, the full white margin visible on **both** sides of
the line. No window light crossing it. No robot in the shot; this figure is the surface.

Do not shoot a curve, an intersection or a gap tile — everything in L04 is a hand slide across
one straight line, and the figure has to show the student which tile to reach for.

### 5. `L13_IMAGE_13-01_*` — The rescue space
**Lesson 13 §4, "walled zone, silver entrance strip across the line, silver and black victim
balls on the floor."** Only shootable if the walled zone is built. Wide shot, walls visible,
the silver entrance strip crossing the line, victim balls on the floor.
**Confirmed in the room.** Shoot it wide enough that the walls read as walls.

---

### 6. `L12_IMAGE_12-01_*` — Delrin sheet with a Zumo mid-turn
**Lesson 12 §7A.** The slick surface, robot mid-turn on it. **Sheet is confirmed in the room.**
Shoot at a low angle so the sheet reads as slick — a flat overhead shot makes delrin look like
paper. The robot should be visibly angled, not square to the frame.

---

## C — NOT SHOOTABLE BY YOU, AND EACH NEEDS A RULING (3 tags)

These three ask for photographs of things that do not exist in your room and will not exist
tomorrow. Each is shoot-later, source-elsewhere, or cut — **cutting is yours (§24.17)**.

| Tag | What it asks for | Realistic options |
|---|---|---|
| `L13 IMAGE 13.2` | Servo gripper, modified blade, competition robots with arms | Source from RoboCup media with permission · redraw as a graphic · cut |
| `L14 IMAGE 14.1` | Robots competing at a RoboCup Junior event | Same three · this one is atmosphere, not instruction |
| `L16 IMAGE 16.1` | Showcase day — student robots, posters, bracket on the whiteboard | **Shoot it in May.** It is a photograph of a day that has not happened. Park until the first Showcase. |

---

## D — NOT A PHOTO (1 tag)

### `L15 GRAPHIC 15.4` — Proportional control under a spotlight
A drawn diagram, not a camera job: P control lit in a spotlight, past and future dark.
**Mine to build, not yours.** Listed here only so the fourteen add up.

---

## E — THE FOUR VIDEOS

`image_audit` counts these in the fourteen. Two are shootable tomorrow; two need working code.

| Tag | Shot | Tomorrow? |
|---|---|---|
| `L03 VIDEO 3.1` — `L03_VIDEO_3-01_crooked_vs_straight.mp4` (**filename declared in the lesson — use exactly this**) | Robot curving left with TRIM 0, then straight with TRIM applied. Same floor, same frame, cut together. | **Yes**, if a robot runs the TRIM sketch |
| `L04 VIDEO 4.1` | Close-up: both jumpers lifted straight up and reseated on DN2 / DN4. Power off, USB out, robot on its back over the table, tweezers. | **Yes** — desk, two minutes, needs a macro-steady hand |
| `L06 VIDEO 6.1` | Robot navigating a maze on encoder counts alone | No — needs the L06 build |
| `L08 VIDEO 8.1` | Side by side: bang-bang oscillating vs. P-control smooth | No — needs the L08 build |

---

## THE TILE RULING — MADE, AND EXECUTED IN L04

**Ruled: tiles, students place them.** L04 §4.3 is rewritten and the lesson is **v04.30.0**.
It no longer has students build a surface; it has them *choose and check* one — pick a straight
tile, confirm it sits flat, confirm the line is unbroken, confirm the white margins are at least
a robot's width. The reasons were always the content and all four survived.

Measured before and after, in L04: **poster board 7 → 0**, **electrical tape 4 → 2** (both
survivors are physics — black tape absorbs infrared, a tape strip is narrow enough to fall in a
sensor gap — and both are true on a tile). Four quiz banks pin L04's version and were repinned
and bumped.

**The same assumption still lives in two other lessons** — measured, not guessed:

| Lesson | Where | What it says |
|---|---|---|
| **L08** | §6 WHAT YOU NEED | "a line track: black electrical tape on a white surface, with at least one curve" — one line, easy |
| **L09** | §4.1 Test Course Materials | A three-row materials table: white poster board, 3/4" black tape, **green tape or paper for intersection markers** — plus a "Green Color Matters" tip that has students test their own green against the sensors |

L08 is a one-line fix. **L09 is not**, and that is question 1 below.

---

## Tomorrow's realistic total

**Six photos and two videos** — both gates answered, both open. That is 3.2, 3.5, 3.6, 4.3,
12.1, 13.1, plus `VIDEO 3.1` and `VIDEO 4.1`. Shooting all eight closes **eight of the fourteen
outstanding tags**, and **all six that sit in L01–L08** — the half of the book your students
actually reach this trimester.

Of the six that would remain: one is a diagram I draw (15.4), two need working L06 and L08 code
(VIDEO 6.1, 8.1), and three are the not-shootable set in section C.

**Send me the files and I wire them.** Correct filenames matter more than perfect framing.

---
*Working document · Fall 2026 · derived from `IMAGE_WORKLIST.md`, which is generated by `image_audit.py` v1.3*
