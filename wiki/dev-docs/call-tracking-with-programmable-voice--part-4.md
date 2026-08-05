---
title: Call Tracking with Programmable Voice
summary: A tutorial for building a Call Tracking application using the Telnyx Programmable
  Voice API and Numbers API, available in both Python (Flask) and Node.js (Express).
  The app searches and orders local phone numbers, forwards inbound calls to designated
  destinations, and stores call metadata. The page also covers command retry best
  practices for handling 5XX errors, latency, and duplicate webhooks.
sources:
- url: https://developers.telnyx.com/docs/voice/programmable-voice/call-tracking
- url: https://developers.telnyx.com/docs/voice/programmable-voice/command-retries
updated_at: 2026-08-05T14:03:06Z
---

# Call Tracking with Programmable Voice

*Part 4 of 4 — see also: [Part 1](call-tracking-with-programmable-voice--part-1.md), [Part 2](call-tracking-with-programmable-voice--part-2.md), [Part 3](call-tracking-with-programmable-voice--part-3.md)*

A tutorial for building a Call Tracking application using the Telnyx Programmable Voice API and Numbers API, available in both Python (Flask) and Node.js (Express). The app searches and orders local phone numbers, forwards inbound calls to designated destinations, and stores call metadata. The page also covers command retry best practices for handling 5XX errors, latency, and duplicate webhooks.

## Command retries for reliability

Telnyx actively monitors the Voice API for 5XX errors, latency, and duplicate webhooks, but applications should still handle these edge cases. Three situations to plan for:

- **5XX errors** — Telnyx monitors and alerts on 500, 501, 503, and 504 responses.
- **Duplicate webhooks** — identical webhooks may occasionally be delivered more than once.
- **Latency** — responses can occasionally exceed 500ms.

To make your call tracking app more reliable:

- **`command_id`** — send a unique `command_id` (UUIDv4 is recommended) with every command so retries are idempotent.
- **Retry on 5XX** — if you receive a 500-series response, immediately retry the same command.
- **Retry on latency** — if no HTTP response arrives within 500ms, send an identical command.

## Next steps

Once the basic app is working, you can extend it in many directions:

- Persist additional webhook fields (IDs, recording URLs, CNAM data) by adding more tables or columns.
- Add inbound messaging routes to handle SMS on the same numbers.
- Enable dual-channel recording or auto-answer behavior.
- Build a richer UI on top of the bindings and call data.

Join the [Telnyx developer Slack community](https://joinslack.telnyx.com/) to see what other developers are building.
