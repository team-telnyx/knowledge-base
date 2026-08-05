---
title: RCS Getting Started
summary: RCS (Rich Communication Services) is a messaging protocol that delivers app-like
  experiences in the native messaging app without requiring a download. This guide
  covers the Telnyx RCS approval process, how to create a messaging profile, send
  rich cards and suggested replies, and handle incoming RCS messages via webhooks.
sources:
- url: https://developers.telnyx.com/docs/messaging/messages/rcs-getting-started/index
- url: https://developers.telnyx.com/docs/messaging/messages/receive-message
updated_at: 2026-08-05T13:57:03Z
---

# RCS Getting Started

*Part 4 of 4 — see also: [Part 1](rcs-getting-started--part-1.md), [Part 2](rcs-getting-started--part-2.md), [Part 3](rcs-getting-started--part-3.md)*

RCS (Rich Communication Services) is a messaging protocol that delivers app-like experiences in the native messaging app without requiring a download. This guide covers the Telnyx RCS approval process, how to create a messaging profile, send rich cards and suggested replies, and handle incoming RCS messages via webhooks.

## RCS vs SMS comparison

| Feature | RCS | SMS |
| --- | --- | --- |
| Rich media | ✅ Images, video, files | ❌ Text only (MMS for media) |
| Interactive buttons | ✅ Suggested replies & actions | ❌ |
| Read receipts | ✅ | ❌ |
| Typing indicators | ✅ | ❌ |
| Branding | ✅ Logo, colors, verified sender | ❌ |
| Character limit | None | 160 (GSM-7) |
| Carrier registration | Required | 10DLC/Toll-free required |

## Next steps

- [RCS with AI Assistant](rcs-with-ai-assistant.md) — Add AI-powered responses to your RCS agent
- [RCS Webhooks](rcs-webhooks.md) — Handle incoming RCS messages
- [RCS Capabilities](rcs-capabilities.md) — Check if a number supports RCS
- [API Reference](https://developers.telnyx.com/docs/messaging/messages/rcs-getting-started/index) — Explore all RCS parameters
- [Send Messages](send-messages.md) — Send outbound SMS and MMS messages
- [Webhooks Reference](webhooks-reference.md) — All webhook event types and payload details
- [Message Encoding](message-encoding.md) — Understand GSM-7, UCS-2, and message segmentation
- [Auto-Reply with Opt-Out](auto-reply-with-opt-out.md) — Handle STOP/HELP keywords automatically
