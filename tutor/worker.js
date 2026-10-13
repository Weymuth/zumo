// ============================================================
// Mercersburg Robotics AI Tutor — Cloudflare Worker Proxy v3.1
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

const CORS_HEADERS = {
  "Access-Control-Allow-Origin": "*",
  "Access-Control-Allow-Methods": "POST, OPTIONS",
  "Access-Control-Allow-Headers": "Content-Type",
};

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

    try {
      const body = await request.json();
      const { messages, currentChallenge, lessonContent, lessonTitle } = body;

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
