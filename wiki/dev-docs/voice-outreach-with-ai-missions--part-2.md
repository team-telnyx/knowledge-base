---
title: Voice Outreach with AI Missions
summary: AI Missions let an OpenClaw agent autonomously execute multi-step voice workflows
  — such as researching businesses, calling them, negotiating, and summarizing results
  — by orchestrating the Telnyx Missions, Assistants, and Numbers APIs. This page
  walks through the full lifecycle, from installing the Telnyx Missions skill and
  giving an agent a task, to monitoring progress in the Telnyx Portal and reviewing
  call transcripts and structured insights.
sources:
- url: https://developers.telnyx.com/docs/inference/missions/index
updated_at: 2026-08-05T13:46:34Z
---

# Voice Outreach with AI Missions

*Part 2 of 2 — see also: [Part 1](voice-outreach-with-ai-missions--part-1.md)*

AI Missions let an OpenClaw agent autonomously execute multi-step voice workflows — such as researching businesses, calling them, negotiating, and summarizing results — by orchestrating the Telnyx Missions, Assistants, and Numbers APIs. This page walks through the full lifecycle, from installing the Telnyx Missions skill and giving an agent a task, to monitoring progress in the Telnyx Portal and reviewing call transcripts and structured insights.

## How the voice calls work

Behind the scenes, your agent uses the Telnyx AI Assistants platform to make calls.

### Voice assistant creation

The agent creates a Telnyx AI Assistant with:

- A **system prompt** tailored to your specific request (e.g., *"You are calling catering companies to negotiate quotes for a 50-person corporate event…"*).
- A **greeting** that opens the conversation naturally (e.g., *"Hi, I'm calling to inquire about catering for a corporate event. Do you have a moment?"*).
- **Dynamic variables** that update between calls (e.g., injecting the current best quote before each negotiation call).
- **Telephony features** enabled for voice calls.

### Phone number assignment

The agent finds an available phone number from your Telnyx account and assigns it to the assistant's voice connection. This is the caller ID that businesses will see.

You need at least one phone number in your Telnyx account. If none are available, the agent will let you know and link you to the [number purchase page](https://portal.telnyx.com/#/app/numbers/search-numbers).

### Call scheduling

Calls are scheduled during business hours to maximize the chance of reaching someone. The agent handles timezone awareness and won't schedule calls at 3 AM.

### Call monitoring

After scheduling, the agent polls for call completion and retrieves:

- **Call status** — completed, failed, no answer, busy.
- **Conversation transcript** — full text of what was said.
- **Conversation insights** — structured extraction of key data points (quotes, availability, terms).

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

## What's next

- **AI Missions API Reference** — full API documentation for creating and managing missions programmatically.
- **AI Assistants** — learn about async tools and advanced assistant configurations.
- **AI Insights** — extract structured data from conversations.
- **[Telnyx Missions Skill on ClawHub](https://clawhub.ai/dotcom-squad/telnyx-toolkit)** — install the skill for your OpenClaw agent.
