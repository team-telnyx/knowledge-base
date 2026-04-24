---
title: Voice Outreach with AI Missions
summary: Give your AI agent a mission to research businesses, make phone calls, and report back with results — all tracked and auditable through the Telnyx Missions API.
sources:
  - url: https://developers.telnyx.com/docs/inference/missions/index
    content_hash: cf39062d3d5f7e10f2323239510e3b2be6ea313751a9a04a48bdd69b1f8696b4
updated_at: 2026-04-10T00:00:00Z
---

# Voice Outreach with AI Missions

Give your AI agent a mission to research businesses, make phone calls, and report back with results — all tracked and auditable through the Telnyx Missions API.

Your AI agent can do more than answer questions — it can go out into the world and get things done. With **AI Missions** and the **Telnyx Missions skill**, you can give your agent a task like *"Find catering companies in Chicago and call them to negotiate quotes for a corporate event"* and watch it execute the entire workflow: research, phone calls, follow-ups, and a final summary.

This guide walks you through the full lifecycle — from setting up your agent with the Missions skill to reviewing call results in the Telnyx Portal.

***

## What you'll need

Before you start, make sure you have:

1. **An OpenClaw agent** — This is the AI agent that will execute your mission. If you don't have one yet, follow the [OpenClaw quickstart](https://docs.openclaw.ai) to get set up.

2. **A Telnyx account with an API key** — Your agent needs API access to create assistants, schedule calls, and track missions. [Create a Telnyx account](https://telnyx.com/sign-up) if you don't have one, then [generate an API key](https://portal.telnyx.com/#/app/api-keys).

3. **The Telnyx Missions skill installed** — Install it from [ClawHub](https://clawhub.ai/dotcom-squad/telnyx-toolkit) and configure your `TELNYX_API_KEY` as an environment variable for your agent.

That's it. The skill handles phone number selection and assignment automatically — your agent will pick an available number from your account when it needs to make calls.

***

## How it works

Your agent uses several Telnyx APIs to orchestrate the work:

* **Missions API** — creates a mission, plans steps, logs events, and tracks status
* **Assistants API** — creates a voice assistant with custom prompts and schedules calls
* **Numbers API** — finds an available phone number and assigns it to the assistant

The Missions API tracks every step — what your agent planned, what it did, what succeeded, and what failed. You get a complete audit trail without having to monitor the agent in real time.

***

## Give your agent a mission

Once your agent has the Telnyx Missions skill installed, you can describe tasks in natural language. The agent handles the rest.

### Example: Catering quote negotiation

Here's a real example — asking your agent to find caterers and negotiate pricing:

> *"Find catering companies in Chicago for a corporate event with 50 people. Call Lakefront Catering, Chicago Grill Co, and Prairie Table Events. Get a baseline quote from the first one, then use that to negotiate better rates with the others. Compare all quotes and recommend the best option."*

Your agent will:

1. **Create a mission** in the Telnyx Missions API to track the work
2. **Build an execution plan** with steps (assistant setup → baseline call → negotiation calls → comparison)
3. **Create a voice assistant** — a Telnyx AI Assistant configured as a "Catering Quote Negotiator" with a professional script tailored to your request
4. **Assign a phone number** from your account to the assistant for outbound calling
5. **Call the first caterer** to establish a baseline price
6. **Call remaining caterers** armed with the best quote so far, negotiating for better rates
7. **Monitor call completions** and capture conversation insights
8. **Summarize results** — comparing quotes and recommending the best option

### What the agent plans

When the mission starts, your agent creates a structured plan. In the Portal, you can see each step and its status:

<img alt="Mission plan view showing completed steps: create assistant, call Lakefront Catering (baseline), call Chicago Grill Co (with best quote), call Prairie Table Events (with best quote), compare and recommend" />

Each step has a status (`pending`, `in_progress`, `completed`, `failed`) so you can see exactly where things stand at any point. In this example, the agent's plan was:

1. Create catering negotiation assistant with dynamic variable placeholders
2. Call Lakefront Catering (baseline, no leverage)
3. Call Chicago Grill Co (with best quote from call 1)
4. Call Prairie Table Events (with best quote so far)
5. Compare quotes and recommend best option

Notice how the agent strategically ordered the calls — getting a baseline first, then using that price as leverage in subsequent negotiations.

***

## Monitor progress in the Portal

You don't need to watch your agent work. The Telnyx Portal gives you a dashboard view of every mission.

### Mission overview

Navigate to the **AI Missions** section in the [Telnyx Portal](https://portal.telnyx.com) to see all missions, their status, and when they were last updated. The dashboard shows recent runs with result summaries at a glance:

<img alt="AI Missions overview showing recent runs including Corporate Catering Quotes (succeeded), Restaurant Reservation Screening, and Weather IVR Sweep missions" />

### Run details

Click **View Run** to see the full run detail — status, timing, the original input, and structured result payload. This is where you'll find the agent's final analysis:

<img alt="Mission Run Detail showing succeeded status, result summary with quotes from 3 caterers, and structured result payload with per-person pricing and recommendation" />

The result payload includes structured data — per-person quotes, negotiation notes, conversation IDs linking back to call recordings, and the agent's recommendation. This data is also accessible via the API.

### Linked agents and conversation history

Scrolling down, the Portal shows which Telnyx AI Assistants your agent created and linked to the mission run. Below that, you can see every conversation — including which caterer was called, the call channel, and timestamps.

### Conversation playback

Click any conversation to open the full transcript with audio playback. Here's the Chicago Grill Co negotiation — watch the agent use the Lakefront's \$65 quote as leverage to negotiate down to \$62:

<img alt="Conversation detail showing the Catering Quote Negotiator negotiating with Chicago Grill Co — starting at 58/person without dessert, then negotiating to 62 all-inclusive using the $65 competitor quote as leverage" />

The conversation panel shows the full back-and-forth, audio waveform with playback controls, and latency metrics (STT, LLM, TTS) for each assistant turn.

***

## Review call results

After calls complete, your agent captures conversation insights — structured summaries of what was discussed.

### Conversation insights

For each completed call, the Missions skill can extract structured information using the [AI Insights API](creating-insights.md) — pulling out key data points like pricing, availability, and terms into a structured format.

### The final summary

When all calls are done, your agent compiles everything into a summary with recommendations. Here's what that looks like for our catering example:

> **Mission Complete: Catering Quote Negotiation**
>
> Called 3 caterers for a 50-person corporate event:
>
> | Caterer              | Quote (per person) | Negotiated?           | Notes                                           |
> | -------------------- | ------------------ | --------------------- | ----------------------------------------------- |
> | Lakefront Catering   | \$65               | Baseline              | First call, established reference price         |
> | Chicago Grill Co     | \$62               | ✅ Yes, down from \$68 | Beat the Lakefront quote when presented with it |
> | Prairie Table Events | \$65               | ❌ No match            | Couldn't beat \$65, matched it                  |
>
> **Recommendation:** Chicago Grill Co offers the best value at $62/person — $150 savings over the baseline for 50 guests.

This summary is also stored as the mission's `result_summary` and `result_payload`, so it's permanently accessible via the API and Portal.

***

## How the voice calls work

Behind the scenes, your agent uses the Telnyx AI Assistants platform to make calls. Here's what it sets up:

### Voice assistant creation

The agent creates a Telnyx AI Assistant with:

* A **system prompt** tailored to your specific request (e.g., *"You are calling catering companies to negotiate quotes for a 50-person corporate event..."*)
* A **greeting** that opens the conversation naturally (e.g., *"Hi, I'm calling to inquire about catering for a corporate event. Do you have a moment?"*)
* **Dynamic variables** that update between calls (e.g., injecting the current best quote before each negotiation call)
* **Telephony features** enabled for voice calls

### Phone number assignment

The agent finds an available phone number from your Telnyx account and assigns it to the assistant's voice connection. This is the caller ID that businesses will see.

> **Note:** You need at least one phone number in your Telnyx account. If none are available, the agent will let you know and link you to the [number purchase page](https://portal.telnyx.com/#/app/numbers/search-numbers).

### Call scheduling

Calls are scheduled during business hours to maximize the chance of reaching someone. The agent handles timezone awareness and won't schedule calls at 3 AM.

### Call monitoring

After scheduling, the agent polls for call completion and retrieves:

* **Call status** — completed, failed, no answer, busy
* **Conversation transcript** — full text of what was said
* **Conversation insights** — structured extraction of key data points (quotes, availability, terms)

***

## Tips for effective missions

### Be specific in your request

The more detail you give, the better your agent performs:

```
❌ "Find me a caterer"

✅ "Find 3 catering companies in downtown Chicago for a 50-person
    corporate lunch. Call each one, get per-person pricing, ask about
    dietary accommodation options, and negotiate using the best quote
    you get as leverage."
```

### Let the agent plan first

Your agent will create a plan before executing. If you want to review the plan before calls go out, say so:

> *"Find caterers and create a plan, but wait for my approval before making any calls."*

### Check the Portal for real-time status

You don't need to keep chatting with your agent. The Portal shows live progress — check back when you get a notification that the mission is complete.

### Start small

Try a mission with 2-3 calls first to see how it works. You can always scale up once you're comfortable with the workflow.

***

## What's next

* **[AI Missions API Reference](voice-outreach-with-ai-missions.md)** — Full API documentation for creating and managing missions programmatically
* **[AI Assistants](async-tools-deferred-context.md)** — Learn about async tools and advanced assistant configurations
* **[AI Insights](creating-insights.md)** — Extract structured data from conversations
* **[Telnyx Missions Skill on ClawHub](https://clawhub.ai/dotcom-squad/telnyx-toolkit)** — Install the skill for your OpenClaw agent
