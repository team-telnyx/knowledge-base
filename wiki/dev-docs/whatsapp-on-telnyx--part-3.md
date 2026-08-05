---
title: WhatsApp on Telnyx
summary: Telnyx provides a complete WhatsApp Business Platform integration covering
  embedded signup (for direct customers and Tech Providers), WhatsApp Business Calling,
  and message template management. This page consolidates the onboarding flows, API
  endpoints, voice calling setup, and template lifecycle into a single reference.
sources:
- url: https://developers.telnyx.com/docs/messaging/whatsapp/business-calling/index
- url: https://developers.telnyx.com/docs/messaging/whatsapp/embedded-signup
- url: https://developers.telnyx.com/docs/messaging/whatsapp/embedded-signup/tech-provider
- url: https://developers.telnyx.com/docs/messaging/whatsapp/manage-templates
updated_at: 2026-08-05T13:58:27Z
---

# WhatsApp on Telnyx

*Part 3 of 4 — see also: [Part 1](whatsapp-on-telnyx--part-1.md), [Part 2](whatsapp-on-telnyx--part-2.md), [Part 4](whatsapp-on-telnyx--part-4.md)*

Telnyx provides a complete WhatsApp Business Platform integration covering embedded signup (for direct customers and Tech Providers), WhatsApp Business Calling, and message template management. This page consolidates the onboarding flows, API endpoints, voice calling setup, and template lifecycle into a single reference.

## WhatsApp Business Calling

WhatsApp Business Calling lets you receive and place voice calls over WhatsApp using your existing Telnyx phone numbers. Calls route through your configured Voice API, SIP, or TeXML connection — the same infrastructure used for programmable voice.

### How It Works

- **Inbound calls** — When a WhatsApp user calls your business number, the call routes through your existing voice connection (Voice API, SIP, TeXML, or AI agent).
- **Outbound calls** — Place calls to WhatsApp users using a SIP URI with the format `<destination>@whatsapp-<your_telnyx_number_without_plus>.sip.telnyx.com`.
- **On-net routing** — All WhatsApp voice calls route through Meta's network. These are not PSTN calls.
- **Concurrent call limit** — Meta allows a maximum of 1,000 concurrent calls per business number.

Outbound WhatsApp calling is not available for numbers in the United States, Canada, Egypt, Vietnam, and Nigeria. This is a Meta platform restriction.

### Prerequisites

- A Telnyx account with an [API key](https://portal.telnyx.com).
- A WhatsApp Business Account connected via [WhatsApp Embedded Signup](whatsapp-embedded-signup.md).
- A verified phone number added to your WABA.
- A voice connection (Voice API, SIP, or TeXML) configured in the [Telnyx Portal](https://portal.telnyx.com).
- A WABA daily messaging limit of at least **2,000 unique recipients** — Meta requires this minimum before calling APIs can be enabled.

### Enable WhatsApp Calling

**Step 1 — Check current calling status:**

```
GET https://api.telnyx.com/v2/whatsapp/phone_numbers/{phone_number}/calling_settings
```

The response includes an `enabled` field — `false` means calling is not yet active.

**Step 2 — Enable calling** by setting `enabled` to `true`:

```
PATCH https://api.telnyx.com/v2/whatsapp/phone_numbers/{phone_number}/calling_settings
```

**Step 3 — Configure inbound routing.** Inbound WhatsApp calls route through your voice connection. Configure one of:

- [Voice API](/docs/voice/programmable-voice) — Handle calls programmatically with webhooks.
- [SIP Trunking](/docs/sip-trunking) — Route calls to your SIP infrastructure.
- [TeXML](/docs/voice/texml) — Control calls with XML-based instructions.

### Make Outbound Calls

The WhatsApp user must grant calling permission before you can place an outbound call. Permission can be obtained in three ways:

- **Permission request message** — Send a calling permission request via WhatsApp message (rate-limited to 1 request per 24 hours and 2 requests per 7 days per user).
- **Callback permission** — The user calls your business first, granting temporary permission for 7 days. Requires "Allow Callbacks" to be enabled in Meta Business Suite.
- **User grants via profile** — The user enables calling from your WhatsApp Business Profile settings, granting permanent permission.

Temporary permission (from callback or accepted request) lasts 7 days. Permission granted via profile settings is permanent until revoked. After 2 consecutive unanswered outbound calls, WhatsApp sends the user a nudge notification. After 4 consecutive unanswered calls, permission is automatically revoked.

To place an outbound WhatsApp call, use the SIP URI format:

```
<destination>@whatsapp-<your_telnyx_number_without_plus>.sip.telnyx.com
```

For example, to call `+442071234567` from your Telnyx number `+15551234567`:

```
+442071234567@whatsapp-15551234567.sip.telnyx.com
```

```
curl -X POST https://api.telnyx.com/v2/calls \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "connection_id": "YOUR_CONNECTION_ID",
    "to": "sip:+442071234567@whatsapp-15551234567.sip.telnyx.com",
    "from": "+15551234567"
  }'
```

### Disable Calling

Set `enabled` to `false`:

```
curl -X PATCH "https://api.telnyx.com/v2/whatsapp/phone_numbers/+15551234567/calling_settings" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{ "enabled": false }'
```

### Troubleshooting

- **Calling enabled but inbound calls not arriving** — Verify the phone number has an active voice connection configured.
- **Outbound calls fail with a geo-restriction error** — Outbound WhatsApp calling is not available for numbers in the US, Canada, Egypt, Vietnam, or Nigeria.
- **`enabled` returns false after a PATCH** — Ensure the phone number is verified and actively registered with your WABA.
- **Call quality issues** — WhatsApp calls route through Meta's network, not the PSTN. Quality depends on the end user's internet connection.
- **Calling APIs cannot be enabled** — Your WABA must have a daily messaging limit of at least 2,000 unique recipients.
- **Outbound call fails despite having permission** — Verify the phone number is associated with the voice connection used in the API call, and check the SIP URI format — the Telnyx number in the host portion must not include the leading `+`.
- **Permission revoked after unanswered calls** — After 2 consecutive unanswered outbound calls, WhatsApp sends a nudge notification. After 4 consecutive unanswered calls, permission is automatically revoked.
