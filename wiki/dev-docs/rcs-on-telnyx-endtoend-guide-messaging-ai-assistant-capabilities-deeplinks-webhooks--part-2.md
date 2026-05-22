---
title: 'RCS on Telnyx: end‑to‑end guide (Messaging, AI Assistant, Capabilities, Deeplinks,
  Webhooks)'
summary: Build and launch Rich Communication Services (RCS) on Telnyx—from agent approval
  and sending rich messages to device capability checks, deeplinks, webhooks, and
  optional AI Assistant integration for no-code conversational replies.
sources:
- url: https://developers.telnyx.com/docs/messaging/messages/rcs-ai-assistant
  content_hash: 5039b349d6faabf9972f41a04d1de56f3ee2f8a40332c5ce6f10e905693b229b
- url: https://developers.telnyx.com/docs/messaging/messages/rcs-capabilities/index
  content_hash: 6db6e84317092f1b6b9a9fc31f5976c50c89e93786dd2245c8dc16e2dc438218
- url: https://developers.telnyx.com/docs/messaging/messages/rcs-deeplinks
  content_hash: c10492c441f3e12d56c2f06d828dcd65644d5dd6bfe1af1c1cc25341481a80f1
- url: https://developers.telnyx.com/docs/messaging/messages/rcs-getting-started/index
  content_hash: 62edd2dc217194d6d4e74b1ea186a18d434c093300e1ec69d326c545c35e68d7
- url: https://developers.telnyx.com/docs/messaging/messages/receiving-rcs-webhooks/index
  content_hash: 1fac49cc3430f838929b09ed83ca4b7955432331a077f61706adc02b6d7d7041
- url: https://developers.telnyx.com/docs/messaging/messages/send-an-rcs-message/index
  content_hash: bd80adb102952b25eba6c10c6e870272a0a62299a078d46f675b543dc89f7fae
updated_at: 2026-05-20T09:08:21Z
---

# RCS on Telnyx: end‑to‑end guide (Messaging, AI Assistant, Capabilities, Deeplinks, Webhooks)

*Part 2 of 2 — see also: [Part 1](rcs-on-telnyx-endtoend-guide-messaging-ai-assistant-capabilities-deeplinks-webhooks--part-1.md)*

Build and launch Rich Communication Services (RCS) on Telnyx—from agent approval and sending rich messages to device capability checks, deeplinks, webhooks, and optional AI Assistant integration for no-code conversational replies.

## Deeplinks to start RCS chats (links, QR, email)
Generate an RCS deeplink (optionally include a fallback phone number and starter body):
```bash
# With fallback phone number and message body
curl -s 'https://api.telnyx.com/v2/messages/rcs/deeplinks/{agent_id}?phone_number=%2B15554443333&body=hello%20world' \
  -H "Authorization: Bearer YOUR_API_KEY"

# RCS‑only (no fallback)
curl -s 'https://api.telnyx.com/v2/messages/rcs/deeplinks/{agent_id}' \
  -H "Authorization: Bearer YOUR_API_KEY"
```
Usage patterns:
- Website: embed the URL in an <a> element or button (won’t open if pasted directly in the address bar)
- QR code: encode the deeplink for print/in‑store signage
- Email CTA: opens RCS directly on supported Android devices

Requirements:
- Device: Android with Google Messages
- OS build: messages.android_20241029_00 or later
- Fallback: include phone_number param to open SMS on non‑RCS devices

More examples in [RCS Capabilities & Deeplinks](rcs-capabilities-deeplinks.md) and [RCS Deeplinks](rcs-deeplinks.md).

## Webhooks, delivery statuses, and read receipts
Structural differences vs. SMS/MMS:
- RCS body is nested under payload.body (text, user_file, location, suggestion_response)
- Media for inbound RCS is under payload.body.user_file (with full‑res and thumbnail URIs)
- RCS supports message.read events (read receipts); SMS/MMS does not
- JSON field naming follows snake‑case aligned to Google’s RCS schema

Event types:
- message.sent (outbound)
- message.finalized (delivery confirmed/failed by carrier)
- message.read (recipient read the message)
- message.received (inbound to your agent)

Status values include: queued, sending, sent, delivered, read, sending_failed, delivery_failed, delivery_unconfirmed.

Inbound message types you may receive:
- Text
- File/Image (user_file with mime type, size, full and thumbnail URIs)
- Location (latitude/longitude)
- Suggestion response (text + postback_data for routing)

Best practices:
- Respond quickly—return 2xx within ~2 seconds; process asynchronously and idempotently (dedupe by event.data.id)
- Verify webhook signatures (telnyx-signature-ed25519, telnyx-timestamp)
- Implement SMS fallback when delivery_failed
- Allowlist webhook IPs: 192.76.120.192/27

Full payload examples and SDK handlers: [Receiving RCS Webhooks](receiving-rcs-webhooks.md).

## Monitoring, analytics, and optimization
- AI Assistants → Insights in the portal: review conversations, identify knowledge gaps, monitor response times
- Use read receipts strategically (not guaranteed—some users disable)
- Test with real FAQs, ticket history, and edge cases before launch

## Platform support and comparison
- Devices: Android today; Apple announced RCS support in iOS 18
- RCS vs SMS highlights: rich media, carousels, suggested actions, read receipts, typing indicators, verified branding, no character limit (vs. 160 GSM‑7 for SMS)
See overviews in [RCS Getting Started](rcs-getting-started.md) and [Send RCS Messages](send-rcs-messages.md).

## Pricing
- RCS messaging: see Telnyx pricing pages
- AI Assistant: priced by tokens processed; simple Q&A often costs fractions of a cent per exchange

Links: [RCS pricing](https://telnyx.com/pricing/messaging), [AI pricing](https://telnyx.com/pricing/conversational-ai)

## Try the live demo
Chat with the Telnyx support bot via an RCS deeplink or QR code.
- Requirements: US phone number and an RCS‑enabled device (Android with Google Messages, or iOS 18+)
- Example of fetching a demo deeplink URL:
```bash
curl -L 'https://api.telnyx.com/v2/messages/rcs/deeplinks/telnyx_support_v9d1aaax_agent' \
  -H 'Authorization: Bearer YOUR_API_KEY'
```
The demo combines Telnyx AI Assistant (LLM + retrieval) with RCS rich messaging for a native chat experience.

## Related pages
- [RCS Getting Started](rcs-getting-started.md)
- [Send RCS Messages](send-rcs-messages.md)
- [RCS Capabilities & Deeplinks](rcs-capabilities-deeplinks.md)
- [RCS Deeplinks](rcs-deeplinks.md)
- [Receiving RCS Webhooks](receiving-rcs-webhooks.md)
- [RCS with AI Assistant](rcs-with-ai-assistant.md)
