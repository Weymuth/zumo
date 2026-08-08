# The family pin — blocks whose family CONTENT cannot re-derive

**55 of 1,119 callout blocks.** Generated ONCE, at S130, from the verified state.

**87 ROWS RETIRED AT S132, and the reason is the only one that may retire a row.**
They were the glossary-side KEY TERM blocks. `build_family_map` v1.5.0 added a STRUCTURE
tier - a callout inside the glossary region is a KEY TERM - so those blocks now carry a
live signal that sits ABOVE this file, and gate 62's coverage arm reported the hold as
expired without being told to. A pin that something else satisfies is not a pin
(rule 20). **This is not a regeneration from `data-family`** - the value this file exists
to check was never consulted; a tier replaced the need, which is exactly how the glyph
tier's death created this file.
This file is a PRESERVED LAYER: it is read-only input to `build_family_map.py` and
must never be regenerated from `data-family`. A pin rebuilt from the value it exists
to check would agree with any drift by construction.

**70 ROWS RETIRED AT S134, for the same and only legal reason.**
They were the BODY-side KEY TERM blocks. DJ ruled (option A, S134) that a KEY TERM
callout in the lesson body opens its head with the literal `KEY TERM: `, so the family
this file was holding is now stated in the block's own label and `canon_of` names it
from CONTENT, reading nothing decorative. Gate 62's coverage arm reported the hold
expired without being told to, exactly as at S132. **The rows were retired BY THE
PROPERTY** - the surviving set is the gate's own `_need` derivation, never a hand list -
and the count reconciles: 83 blocks converted, 13 of which already named themselves and
were therefore never pinned, leaves 70.

## Why these blocks need a pin

Their family was only ever recoverable from a decorative emoji — `build_family_map`'s
GLYPH tier, which S112 shipped calling itself a stopgap. The marks arc replaced that
emoji with an `<img>`, so that signal is gone. The family itself is NOT lost: it sits in
`data-family`, and at S130 all 212 were verified against the pre-swap glyph with
**zero mismatches**. What the pin restores is the ability to catch a FUTURE change.

The key is `data-callout`, the authored identity added at S130. It is authored, never
derived, so it survives the edits that invalidate a file offset.

The retired glyph is recorded for provenance only. **Nothing may read it back to recover
a family** — §24.14 forbids closing that loop, and doing so would rebuild the very
decoration-keyed tier this file replaces.

## The pinned blocks

| `data-callout` | Family | Retired glyph | Label (first 58 chars) |
|---|---|---|---|
| `1.83` | GOING DEEPER | 🔬 | Curious how any of this actually works? The Going Deeper p |
| `2.11` | ENGINEER'S LOG | 📓 | For your engineering notebook The PNG is sized to drop str |
| `2.96` | TRY THIS | 🎯 | CHALLENGE: Write a function beep(int count) that buzzes th |
| `2.122` | GOING DEEPER | 🔬 | Curious how any of this actually works? The Going Deeper p |
| `3.45` | INSIGHT | 🔍 | Why four small functions instead of one big loop() ? Each  |
| `3.91` | TRY THIS | 🎯 | CHALLENGE: Add a calibration constant SETTLE_TIME (try 300 |
| `3.96` | NOTE | 📘 | Testing on USB? The reading lies. readBatteryMillivolts()  |
| `3.98` | NOTE | 📘 | const and constrain() are two different jobs. They start w |
| `6.24` | KEY TERM | 🔑 | The Formula Turn at each corner = 360 ÷ number of sides |
| `7.103` | GOING DEEPER | 🔬 | Curious how any of this actually works? The Going Deeper p |
| `8.70` | GOING DEEPER | 🔬 | Curious how any of this actually works? The Going Deeper p |
| `9.1` | LEARN | 📖 | A Different Kind of Thinking This lesson marks a fundament |
| `9.2` | LEARN | 📖 | RoboCup Junior Connection In RoboCup Junior Line Rescue co |
| `9.6` | LEARN | 📖 | Why Green Works Green surfaces absorb some IR light but re |
| `9.23` | LEARN | 📖 | Avoiding False Positives: Debouncing Sensor noise can caus |
| `11.2` | THE WALL | 🛑 | It depends on the battery. And that is fatal. A fresh batt |
| `11.5` | THE WALL | 🛑 | The alarm is not allowed to go off until the robot has alr |
| `11.9` | THE WALL | 🛑 | Read the last line. That TRIM is not decoration. Inside a  |
| `11.16` | THE WALL | 🛑 | This is the moment TRIM stops being homework. For three le |
| `11.22` | THE WALL | 🛑 | There is no threshold that works. Not a badly chosen one - |
| `12.1` | THE WALL | 🛑 | The encoder is not broken. It is doing its job perfectly.  |
| `12.4` | THE WALL | 🛑 | This is a structural limit, not a tuning problem. You cann |
| `12.6` | THE WALL | 🛑 | Do the arithmetic on that. A bias of 20°/sec, accumulated  |
| `12.9` | THE WALL | 🛑 | And therefore: A SPIN CANNOT CALIBRATE A GYRO. If the robo |
| `12.16` | THE WALL | 🛑 | Notice what is NOT in there: TRIM. There is no TRIM in tur |
| `12.28` | THE WALL | 🛑 | Build it. The binary did not change. AT ALL. Step 5 grew t |
| `12.31` | THE WALL | 🛑 | This block MUST come before waitForStart(). Here is why. T |
| `12.38` | THE WALL | 🛑 | The number climbs anyway. The robot is motionless . The an |
| `12.41` | THE WALL | 🛑 | Now put it on the delrin. Press B. Encoder: 90 Gyro: |
| `12.45` | THE WALL | 🛑 | Button A on delrin: the square collapses. Each corner slip |
| `12.51` | THE WALL | 🛑 | Notice what you did NOT do in this lesson. You did not rep |
| `12.60` | THE WALL | 🛑 | What B4 should teach you for the rest of your life Three o |
| `12.77` | GOING DEEPER | 🔬 | Curious how any of this actually works? The Going Deeper p |
| `14.1` | WHAT YOU SHOULD SEE | 👀 | The Reality Check At every RoboCup Junior competition, the |
| `14.6` | NOTE | 📘 | Read that formula again, because it overturns the obvious  |
| `14.12` | WHAT YOU SHOULD SEE | 👀 | Healthy Battery Readings ~5,400 mV: Fresh off the charger. |
| `14.13` | IF YOU'RE STUCK | 🔌 | Why these numbers and not round ones. Your fleet runs enel |
| `14.28` | KEY TERM | 🔑 | When to Call LoP Call Lack of Progress when: Robot is clea |
| `15.2` | WARNING | ⚠ | The honest warning up front. Most PID chapters end with a  |
| `15.5` | NOTE | 📘 | D is often called the damper , and that is exactly right.  |
| `15.7` | WARNING | ⚠ | And I is the most dangerous term in the equation. If the e |
| `15.10` | NOTE | 📘 | The general rule, and it is worth more than this lesson: i |
| `15.15` | WARNING | ⚠ | That last row is the whole reason this lesson uses micros( |
| `15.16` | WARNING | ⚠ | Ziegler–Nichols is a starting point, not an answer. It is  |
| `15.17` | WARNING | ⚠ | This rung is designed to fail. Build it anyway. Section 3. |
| `15.18` | NOTE | 📘 | An instrument is not “good” or “bad.” It is matched or mis |
| `15.19` | WARNING | ⚠ | Nothing is free. The filter also delays the derivative - y |
| `15.25` | GOING DEEPER | 🔬 | Curious how any of this actually works? The Going Deeper p |
| `16.6` | WARNING | ⚠ | The classic TDP mistakes: “it works because it works” (exp |
| `16.7` | WARNING | ⚠ | Two rules the hardware enforces. First: an EEPROM write ta |
| `16.8` | NOTE | 📘 | Design pattern worth stealing: the mode does not change wh |
| `16.12` | WARNING | ⚠ | Do not “fix” this by deleting the EEPROM code you just typ |
| `16.14` | TIP | 💡 | Write this trade down in your journal tonight. It is the s |
| `16.16` | WARNING | ⚠ | The #1 project killer is not a bug. It is the working robo |
| `16.29` | GOING DEEPER | 🔬 | Curious how any of this actually works? The Going Deeper p |

## Count by family

| Family | Blocks |
|---|---|
| KEY TERM | 159 |
| THE WALL | 17 |
| WARNING | 10 |
| GOING DEEPER | 7 |
| NOTE | 7 |
| LEARN | 4 |
| TRY THIS | 2 |
| WHAT YOU SHOULD SEE | 2 |
| ENGINEER'S LOG | 1 |
| INSIGHT | 1 |
| IF YOU'RE STUCK | 1 |
| TIP | 1 |

---
*Generated once at S130 from the verified state. Preserved layer — do not regenerate.*
