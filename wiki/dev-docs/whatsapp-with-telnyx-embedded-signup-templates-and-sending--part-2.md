---
title: 'WhatsApp with Telnyx: Embedded Signup, Templates, and Sending'
summary: 'End-to-end guide to set up WhatsApp Business with Telnyx: connect via Embedded
  Signup, provision a WABA and number, create and manage message templates, send messages
  (text, media, interactive, and templates), configure webhooks, and troubleshoot
  common issues.'
sources:
- url: https://developers.telnyx.com/docs/messaging/whatsapp/embedded-signup
- url: https://developers.telnyx.com/docs/messaging/whatsapp/manage-templates
- url: https://developers.telnyx.com/docs/messaging/whatsapp/quickstart/index
- url: https://developers.telnyx.com/docs/messaging/whatsapp/send-messages/index
updated_at: 2026-05-20T09:11:51Z
---

# WhatsApp with Telnyx: Embedded Signup, Templates, and Sending

*Part 2 of 2 — see also: [Part 1](whatsapp-with-telnyx-embedded-signup-templates-and-sending--part-1.md)*

End-to-end guide to set up WhatsApp Business with Telnyx: connect via Embedded Signup, provision a WABA and number, create and manage message templates, send messages (text, media, interactive, and templates), configure webhooks, and troubleshoot common issues.

## Webhooks and Delivery Reporting

Configure delivery/inbound callbacks in Portal → Messaging → Messaging Profiles:
- Set your primary Webhook URL (and optional Failover URL), then save.
- Expect events like message.sent, message.delivered, message.read, message.failed, and inbound message events (e.g., button replies with their IDs).
- For signup progress, listen for whatsapp.signup.state_updated events (contains signup_id, new state, WABA ID, and phone number).

Verification paths:
- Portal: Messaging → Message Logs; filter by Channel: WhatsApp to see status, timestamps, and error details.
- Webhooks: Track message lifecycle and correlate via biz_opaque_callback_data.

## Common Errors and Troubleshooting

Facebook OAuth permission denied:
- Ensure Business Manager admin access and required WhatsApp permissions; resolve any account restrictions; try a different Business Manager; confirm business verification status.

WABA creation failed:
- Complete Business Manager verification; resolve policy violations; remove unused WABAs if quota exceeded; contact Telnyx Support with your signup session ID.

Phone number already registered:
- Disconnect from prior provider or ask them to release the number; use a different number; escalate with Meta Business Support if needed.

Verification timeout/failure:
- Ensure the number can receive calls and SMS; remove carrier blocks; retry or use another number; contact Telnyx Support with verification details.

Webhook delivery issues:
- Confirm webhook URL is publicly reachable; check firewall and signature validation; verify Portal configuration; test with manual POST; inspect logs for failures.

Browser extensions blocking signup flow:
- Disable ad/privacy blockers for the duration; allowlist facebook.com and meta.com; try a clean browser profile or Incognito; permit popups for the Telnyx Portal domain.

Messaging errors (sending):
- Template not approved or paused (40008): wait for approval, check exact template name/language, review guidelines.
- Number not verified (40008): complete verification and confirm WABA linkage; ensure the number isn’t tied to personal WhatsApp.
- Outside 24-hour window: use an approved template to initiate; reserve free-form messages for within 24 hours of the customer’s last message.
- Invalid recipient: ensure E.164 format, active WhatsApp account, and that the recipient hasn’t blocked you.

## Best Practices and Notes

- Start simple for first templates; avoid heavy promotional language or special characters to speed approvals.
- Always include examples for parameters and set an approved display name before submitting templates.
- Maintain a complete business profile in Meta to reduce review friction.
- Prefer call verification for landlines.
- Use template_id when sending to avoid name/language mismatches.
- Implement robust webhook handling, idempotency, and signature verification; configure a failover URL.

## Next Steps and Related Pages

- [Quickstart: Send Your First WhatsApp Message](quickstart-send-your-first-whatsapp-message.md) — End-to-end setup and first send.
- [WhatsApp Embedded Signup](whatsapp-embedded-signup.md) — Deep dive on the signup flow.
- [Manage WhatsApp Message Templates](manage-whatsapp-message-templates.md) — Create, update, and govern templates.
- [Send WhatsApp Messages](send-whatsapp-messages.md) — All message types, parameters, and validation rules.
