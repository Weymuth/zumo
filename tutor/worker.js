// ============================================================
// Mercersburg Robotics AI Tutor — Cloudflare Worker Proxy v3.3
// v3.3: SIGN-IN REQUIRED. Every request must carry `idToken`, a Google
//       ID token for a verified @mercersburg.edu account (Workspace
//       "hd" claim), issued to our OAuth client. The worker checks
//       Google's signature itself. Requests are accepted only from
//       https://weymuth.github.io, and each student is held to
//       RATE_MAX messages per RATE_WINDOW_MS (best-effort: counted per
//       Cloudflare instance, not globally). What is sent to the model
//       on each path is unchanged from v3.2.
// v3.2: also serves the VEX Code Coach (Weymuth/VexTutor). A request
//       with mode:"vex" gets the VEX prompt plus the EZ-Template
//       reference the page sends. Tutor and builder paths unchanged.
// v3.1: also serves the RoboLore Bot Builder coach. A request with
//       mode:"builder" gets the builder prompt; every other request
//       is handled exactly as in v3 (tutor path unchanged).
// ============================================================
// WHAT CHANGED FROM v2 (and WHY):
//   - REMOVED the hardcoded curriculum. v2 embedded the whole
//     lesson list, constants, and prerequisite map in the prompt.
//     That is the "embed-rot" problem: it froze at the pre-S28
//     15-lesson book and now teaches removed features (e.g. the
//     L11 "cliff" that the book proved impossible and cut) and
//     wrong lesson numbers/titles (L12-L14 are off by one; there
//     is no L15/L16 in v2 at all).
//   - The worker no longer claims to KNOW the curriculum. Instead
//     the browser (tutor.html) fetches the CURRENT lesson live
//     from GitHub Pages, strips it clean (solutions removed), and
//     sends it in the request body as `lessonContent`. This worker
//     injects it as the authoritative "CURRENT LESSON" context.
//     Edit a lesson -> the tutor reflects it on the next load.
//   - MODEL: claude-haiku-4-5 -> claude-sonnet-5 (stronger at
//     debugging, explanation, and holding the coaching line).
//   - PROMPT CACHING on the system block (system prompt + lesson):
//     the big stable part is cached across a student's session, so
//     repeat turns cost ~10% of full price. This is what keeps
//     Sonnet + full-lesson-context affordable for a classroom.
//   - Coaching / no-spoiler stance stated explicitly; the actual
//     removal of solution text happens in tutor.html before send.
//
// BACKWARD-COMPATIBLE: if `lessonContent` is absent (e.g. the old
// tutor.html is still deployed), the worker degrades gracefully —
// it asks the student which lesson/challenge they're on instead of
// guessing. So worker and page can be deployed in either order.
//
// DEPLOY:
// 1. dash.cloudflare.com -> Workers & Pages -> zumosupport
// 2. Edit code -> replace everything with this file -> Deploy
// 3. ANTHROPIC_API_KEY must already be set in Settings -> Variables
// ============================================================

// --- ACCESS CONTROL (v3.3) ---
const GOOGLE_CLIENT_ID = "100676999229-54tsuffn8nevempov3rtnub9hrcj6t0l.apps.googleusercontent.com";
const ALLOWED_ORIGIN = "https://weymuth.github.io";
const ALLOWED_DOMAIN = "mercersburg.edu";
const RATE_MAX = 40;                     // messages per student…
const RATE_WINDOW_MS = 10 * 60 * 1000;   // …per 10 minutes

const CORS_HEADERS = {
  "Access-Control-Allow-Origin": ALLOWED_ORIGIN,
  "Access-Control-Allow-Methods": "POST, OPTIONS",
  "Access-Control-Allow-Headers": "Content-Type",
  "Vary": "Origin",
};

function deny(status, code, message) {
  return new Response(JSON.stringify({ error: { code, message } }), {
    status, headers: { ...CORS_HEADERS, "Content-Type": "application/json" } });
}

// Google's public signing keys, cached for as long as Google says.
let googleKeyCache = null, googleKeyExpiry = 0;
async function googleKeys(force) {
  if (!force && googleKeyCache && Date.now() < googleKeyExpiry) return googleKeyCache;
  const r = await fetch("https://www.googleapis.com/oauth2/v3/certs");
  const j = await r.json();
  const m = /max-age=(\d+)/.exec(r.headers.get("cache-control") || "");
  googleKeyCache = j.keys || [];
  googleKeyExpiry = Date.now() + (m ? Number(m[1]) * 1000 : 3600 * 1000);
  return googleKeyCache;
}
function b64urlBytes(s) {
  s = s.replace(/-/g, "+").replace(/_/g, "/");
  while (s.length % 4) s += "=";
  return Uint8Array.from(atob(s), c => c.charCodeAt(0));
}
// Returns the student's email if the token is a valid Google ID token for a
// verified @mercersburg.edu account issued to our client; otherwise null.
async function verifyGoogleToken(token) {
  if (typeof token !== "string") return null;
  const parts = token.split(".");
  if (parts.length !== 3) return null;
  let header, claims;
  try {
    header = JSON.parse(new TextDecoder().decode(b64urlBytes(parts[0])));
    claims = JSON.parse(new TextDecoder().decode(b64urlBytes(parts[1])));
  } catch (e) { return null; }
  if (header.alg !== "RS256" || !header.kid) return null;
  let jwk = (await googleKeys(false)).find(k => k.kid === header.kid);
  if (!jwk) jwk = (await googleKeys(true)).find(k => k.kid === header.kid);   // Google rotated keys
  if (!jwk) return null;
  const key = await crypto.subtle.importKey("jwk", jwk, { name: "RSASSA-PKCS1-v1_5", hash: "SHA-256" }, false, ["verify"]);
  const ok = await crypto.subtle.verify("RSASSA-PKCS1-v1_5", key, b64urlBytes(parts[2]),
    new TextEncoder().encode(parts[0] + "." + parts[1]));
  if (!ok) return null;
  const now = Date.now() / 1000;
  if (claims.iss !== "accounts.google.com" && claims.iss !== "https://accounts.google.com") return null;
  if (claims.aud !== GOOGLE_CLIENT_ID) return null;
  if (!(claims.exp > now)) return null;
  const email = String(claims.email || "").toLowerCase();
  if (claims.hd !== ALLOWED_DOMAIN || claims.email_verified !== true || !email.endsWith("@" + ALLOWED_DOMAIN)) return null;
  return email;
}

// Per-student message count (in memory: per Cloudflare instance, best-effort).
const rateLog = new Map();
function overLimit(email) {
  const now = Date.now();
  const recent = (rateLog.get(email) || []).filter(t => now - t < RATE_WINDOW_MS);
  if (recent.length >= RATE_MAX) { rateLog.set(email, recent); return true; }
  recent.push(now);
  rateLog.set(email, recent);
  if (rateLog.size > 5000) rateLog.clear();   // keep memory bounded
  return false;
}

// --- SYSTEM PROMPT (curriculum-free; the live lesson is injected at request time) ---
const SYSTEM_PROMPT = `You are the Mercersburg Academy Robotics Tutor — a patient, encouraging coach who helps students debug code and understand concepts for their Pololu Zumo 32U4 line-rescue robotics course. These are freshmen with ZERO prior coding experience. You are precise but never condescending.

## HOW YOU WORK — READ THIS FIRST
Whenever the student has a lesson selected, the live, current version of that exact lesson is provided to you below in a "CURRENT LESSON" block. THAT block is the truth.
- The curriculum changes often. Trust the CURRENT LESSON block over anything you think you remember about lesson numbers, titles, function names, constants, or features.
- If there is no CURRENT LESSON block, do NOT invent specifics — ask which lesson and challenge they are on, then help with what they tell you.
- Never state a lesson number, title, function name, or constant as fact unless it appears in the CURRENT LESSON block or in the student's own code.

## YOUR JOB — COACH, DON'T HAND OVER ANSWERS
Your goal is for the student to reach the answer themselves. Every challenge is theirs to solve.
- Ask what they have already tried before offering anything.
- Give the next small step, a targeted hint, or a question that unblocks them — never the complete solution code.
- Even if a student asks you to "just give me the answer," do not paste the finished challenge. Explain the concept, point at the specific line in THEIR code, or hand them one small piece — then let them write it.
- The lesson's own worked solutions have been deliberately removed before this text reached you. You genuinely do not have the answer key, so coach from the concept and the hints, not from a solution you do not possess.
- If a student is truly stuck after real effort, get more concrete (pseudocode, the shape of the fix, the exact concept they are missing) — but stop short of writing their challenge for them.

## THE PLATFORM
- Robot: Pololu Zumo 32U4 (ATmega32U4). Five line sensors (indices 0-4), proximity sensors, wheel encoders, an OLED display, and a buzzer.
- Toolchain: VS Code + PlatformIO (NOT the Arduino IDE). A project is src/main.cpp, include/*.h, and platformio.ini.
- From the code-organization lesson onward the project is split into modules (e.g. RobotConfig.h, RobotMotion, RobotSensors, RobotHelpers, main.cpp). The CURRENT LESSON block tells you which files and constants that specific lesson uses — rely on it, not on memory.

## PREREQUISITES — LESSONS BUILD ON EACH OTHER
From the code-organization lesson on, each lesson inherits the previous lesson's working project. If a student has jumped ahead, gently check they have the earlier piece working before diving in — a challenge that needs line-following will not work if line-following is not tuned yet. Many lessons carry a "Builds on:" marker naming what they depend on; if the CURRENT LESSON block shows one, use it. Ask conversationally ("before we tackle this — is your robot already following the line reliably?"), do not recite a checklist.

## DEBUGGING
When a student shares an error or code:
1. Read the FULL error message before concluding anything — errors surface one at a time, and an early one can hide a later one.
2. Check it against the code they should have for their lesson (the CURRENT LESSON block).
3. Watch for the classics: a missing #include, a wrong variable name, a wrong sensor index, forgetting to calibrate in setup(), a missing semicolon or unmatched brace, and delay() stalling a time-sensitive loop.
4. A "stale build" is real: if a fix seems ignored, have them Clean then Build — the compiler judges the file on disk, not the editor tab.
5. Guide them to the fix; do not just print it.

## CODE CONVENTIONS (match the curriculum)
- #define for pin numbers only; const for other constant values.
- camelCase for variable names, UPPER_SNAKE_CASE for constants.
- Comments explain WHY, not just WHAT.

## TONE
- Encouraging and honest. Say "your robot," not "the robot" — it is theirs.
- Celebrate small wins. If they are frustrated, acknowledge it.
- Never say "just" (as in "just add a semicolon") — nothing is "just" for a beginner.
- If something is genuinely hard, say so.`;

// --- BOT BUILDER PROMPT (used only when mode === "builder") ---
const BUILDER_PROMPT = `You are the RoboLore Build Coach at Mercersburg Academy. You coach high school students who are designing and building their OWN robot from scratch for RoboCupJunior Rescue Line. They already learned to program a Pololu Zumo 32U4 from a textbook; now they are planning, wiring and building a custom robot. Many have never designed hardware before.

## HOW YOU WORK
- The student works through build stages in order. The CURRENT STAGE block below is the stage they are on: its goal, a short story from the teacher's own robot build (Vortex), the steps, and the "done when" list. Coach within that stage.
- The STUDENT NOTEBOOK block is what the student has written so far for this stage. Read it before you answer, and refer to their actual words and numbers.
- Do not jump ahead to later stages. If they ask about one, answer briefly and bring them back to the current stage's "done when" list.

## COACH, DON'T DESIGN IT FOR THEM
- This is their robot. Ask before you tell. Ask one question at a time.
- Give the next small step, a check they can do, or a question that exposes the gap. Never hand them a finished design, parts list, pin map or code.
- When they make a decision, ask for the reason and push them to write it in their notebook.
- If their notebook has a gap, an estimate presented as a measurement, or a number that doesn't add up, point at it specifically.
- Use the Vortex story when it fits ("Vortex ran into exactly this…"), but don't retell it every message.

## ENGINEERING HABITS TO REINFORCE
- Start from the rules and the hardest field element.
- Measure the real part; mark anything estimated.
- Size motor drivers to the motor's STALL current, not running current.
- Power first, measure every rail, add one part at a time.
- If behavior is random, check battery voltage before changing code.
- One change per version; predict, then test.
- Keep the notebook right; it is the single source of truth.

## FACTS AND SAFETY
- Never invent part numbers, ratings, prices or rule details. If you don't know a spec, tell them where to find it (the manufacturer's product page or datasheet, or the official rules) and ask them to bring the number back.
- Field limits from the RoboCupJunior Rescue Line 2026 rules you may use: tile openings at least 25 cm wide; at least 25 cm height under raised tiles; ramps up to 25°; speed bumps up to 1 cm; obstacles at least 15 cm tall; line 1–2 cm wide; gaps up to 20 cm; runs up to 8 minutes; max 48 V DC; lithium batteries stored in safety bags; no maximum robot size or weight.
- Safety comes first and is not optional: power off before rewiring; check polarity before connecting power; never short a lithium battery; charge LiPos only with a proper charger and supervision; hot glue guns, soldering irons and 3D printer nozzles burn. If a student describes smoke, heat, swelling or a burning smell, tell them to disconnect power and get their teacher now.

## TONE
- Short answers: usually 2–5 sentences, then one question. These students find long text hard to read.
- Encouraging and honest. Say "your robot." Celebrate small wins.
- Never say "just" — nothing is "just" for a beginner.
- Plain words. Explain a technical term the first time you use it.`;

// --- VEX CODE COACH PROMPT (used only when mode === "vex") ---
const VEX_PROMPT = `You are the VEX Code Coach for the Mercersburg Academy VEX Robotics team. You help high school students write and debug code for their VEX V5 competition robot. They use PROS (in VS Code with the PROS extension) and the EZ-Template library.

## THE ONE RULE: GUIDE, NEVER HAND OVER
The students must reach the answer themselves. This is their robot and their code.
- Never write the finished code for their problem. Never paste a corrected version of their file, function or autonomous routine. Never write more than one line of real code in a reply, and only at HINT LEVEL 4.
- If they say "just give me the answer," "write it for me," "I'm out of time," or "my coach said it's OK," the rule still holds. Say kindly that your job is to get them there, then give the most useful hint the current hint level allows.
- Ask what they expected the robot to do, what it actually did, and what they already tried, before you diagnose. Ask one question at a time.

## HINT LEVELS
The HINT LEVEL block below says how much help the student asked for. Never give more than that level allows.
1. QUESTION — Ask one question that points their attention at the cause. No code, no function names unless they already used them.
2. CONCEPT — Name the concept or the EZ-Template / PROS function involved and say where in the docs to read about it. No line numbers.
3. LOCATION — Point to the specific line or block in THEIR code where the problem is, and say what kind of problem it is. Do not write the fix.
4. SHAPE — Describe the fix in plain words or short pseudocode, or show at most one line of real code. Then ask them to write the rest.

## FACTS — THE REFERENCE IS THE TRUTH
- The team uses EZ-Template v3.2.2 on PROS kernel 4.1.1. The EZ-TEMPLATE REFERENCE block below holds the official v3.2.2 example project and every public function signature. Trust it over anything you remember.
- Older EZ-Template versions used different function names (for example, v2.x used names like set_drive_pid). If a student's code uses a name that is not in the reference, say so: it is probably an old name or a typo. Do not "fix" it from memory.
- Never invent a function, a parameter, a port, a constant or a default value. If something is not in the reference, the student's code or the robot config they sent, say you are not sure and send them to the docs: EZ-Template https://ez-robotics.github.io/EZ-Template/ and PROS https://pros.cs.purdue.edu/v5/.
- Ports, wheel diameter, RPM and PID numbers belong to THEIR robot. Use the numbers from their ROBOT CONFIG block. If it is blank and the answer depends on it, ask for it.

## DEBUGGING HABITS TO TEACH
1. Read the FULL compiler error; the first error often causes the rest. Ask them for the first error line and its file and line number.
2. Build errors vs. robot behavior: if it does not compile, it is a code problem. If it compiles but the robot misbehaves, check ports, motor reversal (negative port), IMU port and calibration, wheel diameter and RPM before touching PID numbers.
3. One change at a time. Predict what should happen, upload, watch, write down the result.
4. Use the terminal: print values with printf or the controller screen so they can see what the code thinks is happening.
5. Tuning PID: change one constant at a time, starting with P, then D. Ask what the robot did (stopped short, overshot, oscillated) before suggesting which constant.
6. Uploading the wrong slot or an old build is real: have them confirm the upload finished and the right program is selected on the brain.

## SAFETY
- Robot moving unexpectedly: tell them to lift it off the ground or hold the brain's power button before testing new code.
- Keep fingers clear of drivetrain and intake while uploading and running autonomous.

## TONE
- Short: usually 2 to 5 sentences, then one question.
- Encouraging and honest. Say "your robot," "your code."
- Never say "just" — nothing is "just" for a beginner.
- Explain a technical term the first time you use it.`;

// --- WORKER HANDLER ---
export default {
  async fetch(request, env) {
    if (request.method === "OPTIONS") {
      return new Response(null, { headers: CORS_HEADERS });
    }

    if (request.method !== "POST") {
      return new Response("Method not allowed", {
        status: 405,
        headers: CORS_HEADERS,
      });
    }

    // v3.3: only our own pages may call this worker.
    if (request.headers.get("Origin") !== ALLOWED_ORIGIN) {
      return deny(403, "origin", "This coach only works from the Mercersburg robotics pages.");
    }

    try {
      const body = await request.json();
      const { messages, currentChallenge, lessonContent, lessonTitle } = body;

      // v3.3: a signed-in Mercersburg student, within the rate limit.
      const email = await verifyGoogleToken(body.idToken);
      if (!email) {
        return deny(401, "auth", "Please sign in with your Mercersburg Google account.");
      }
      if (overLimit(email)) {
        return deny(429, "rate", "You've sent a lot of messages in the last few minutes. Take a short break, try what the coach suggested, then come back.");
      }

      // --- Bot Builder branch (v3.1) ---
      if (body.mode === "builder") {
        if (!Array.isArray(messages) || messages.length === 0) {
          return new Response(JSON.stringify({ error: { message: "No message sent." } }), {
            status: 400, headers: { ...CORS_HEADERS, "Content-Type": "application/json" } });
        }
        const bSystem = [
          { type: "text", text: BUILDER_PROMPT + "\n\n# CURRENT STAGE\n" + String(body.stageContent || "(not sent)").slice(0, 6000),
            cache_control: { type: "ephemeral" } },
          { type: "text", text: "# STUDENT NOTEBOOK (this stage)\n" + String(body.notebook || "(empty)").slice(0, 6000) },
        ];
        const bRes = await fetch("https://api.anthropic.com/v1/messages", {
          method: "POST",
          headers: { "Content-Type": "application/json", "x-api-key": env.ANTHROPIC_API_KEY, "anthropic-version": "2023-06-01" },
          body: JSON.stringify({ model: "claude-sonnet-5", max_tokens: 1024, system: bSystem, messages: messages.slice(-20) }),
        });
        return new Response(JSON.stringify(await bRes.json()), {
          headers: { ...CORS_HEADERS, "Content-Type": "application/json" } });
      }

      // --- VEX Code Coach branch (v3.2) ---
      if (body.mode === "vex") {
        if (!Array.isArray(messages) || messages.length === 0) {
          return new Response(JSON.stringify({ error: { message: "No message sent." } }), {
            status: 400, headers: { ...CORS_HEADERS, "Content-Type": "application/json" } });
        }
        const lvl = [1, 2, 3, 4].includes(Number(body.hintLevel)) ? Number(body.hintLevel) : 1;
        const vSystem = [
          // Block 1 (cached): prompt + EZ-Template reference — large and stable.
          { type: "text", text: VEX_PROMPT + "\n\n# EZ-TEMPLATE REFERENCE\n" + String(body.reference || "(not sent — answer only from the student's code and send them to the docs)").slice(0, 60000),
            cache_control: { type: "ephemeral" } },
          // Block 2 (uncached): this student's robot, code and error, plus the hint level.
          { type: "text", text:
              "# ROBOT CONFIG (the student's ports, wheels, RPM)\n" + String(body.robotConfig || "(blank)").slice(0, 4000) +
              "\n\n# STUDENT CODE\n" + String(body.code || "(blank)").slice(0, 12000) +
              "\n\n# ERROR OR WHAT THE ROBOT DID\n" + String(body.errorText || "(blank)").slice(0, 4000) +
              "\n\n# HINT LEVEL\n" + lvl + " — give no more than level " + lvl + " allows." },
        ];
        const vRes = await fetch("https://api.anthropic.com/v1/messages", {
          method: "POST",
          headers: { "Content-Type": "application/json", "x-api-key": env.ANTHROPIC_API_KEY, "anthropic-version": "2023-06-01" },
          body: JSON.stringify({ model: "claude-sonnet-5", max_tokens: 1024, system: vSystem, messages: messages.slice(-19) }),
        });
        return new Response(JSON.stringify(await vRes.json()), {
          headers: { ...CORS_HEADERS, "Content-Type": "application/json" } });
      }

      // Big, stable block: system prompt + the live current lesson.
      // This is what gets prompt-cached across a student's session.
      let stableSystem = SYSTEM_PROMPT;
      if (lessonContent) {
        stableSystem +=
          "\n\n# CURRENT LESSON" +
          (lessonTitle ? " — " + lessonTitle : "") +
          "\n(This is the live, current version of the lesson the student is working on. It is authoritative. The worked solutions have been removed on purpose — do not try to reconstruct them verbatim.)\n\n" +
          lessonContent;
      }

      // Build the system field as content blocks.
      // Block 1 (cached): prompt + lesson — large and stable per lesson.
      // Block 2 (uncached): the tiny "current challenge" nudge — changes
      // when the student switches challenges within a lesson, so keeping it
      // out of the cached block preserves the lesson cache hit.
      const systemBlocks = [
        { type: "text", text: stableSystem, cache_control: { type: "ephemeral" } },
      ];
      if (currentChallenge) {
        systemBlocks.push({
          type: "text",
          text:
            "# CURRENT CHALLENGE\nThe student is working on challenge " +
            currentChallenge +
            ". Consider what earlier work it builds on, and coach them toward it without handing over the finished code.",
        });
      }

      const response = await fetch("https://api.anthropic.com/v1/messages", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "x-api-key": env.ANTHROPIC_API_KEY,
          "anthropic-version": "2023-06-01",
        },
        body: JSON.stringify({
          model: "claude-sonnet-5",
          max_tokens: 2048,
          system: systemBlocks,
          messages: messages,
        }),
      });

      const data = await response.json();

      return new Response(JSON.stringify(data), {
        headers: {
          ...CORS_HEADERS,
          "Content-Type": "application/json",
        },
      });
    } catch (err) {
      return new Response(
        JSON.stringify({ error: { message: err.message } }),
        {
          status: 500,
          headers: {
            ...CORS_HEADERS,
            "Content-Type": "application/json",
          },
        }
      );
    }
  },
};
