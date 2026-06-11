---
title: Telnyx Messaging Features
summary: Covers Telnyx messaging capabilities including MMS SMIL templates, Sticky
  Sender, URL Shortening, Zapier integration, toll-free verification, and the full
  WhatsApp Business messaging workflow from embedded signup through template management
  and message sending.
sources:
- url: https://developers.telnyx.com/docs/messaging/messages/smil-template
  content_hash: d29aa01a72d9457e2c15bca36d1a114fad0d8a8fd2d7b721484dbeb7d7ea9663
- url: https://developers.telnyx.com/docs/messaging/messages/sticky-sender/index
  content_hash: b60693e817349ec8df4be29ac868e8661434934e8c3047b7acc28151d7d666ae
- url: https://developers.telnyx.com/docs/messaging/messages/url-shortening/index
  content_hash: 4c488d1b1e1c401b24857bbee9b2dc380feeb3307e7bce07ecaa412fe56d304f
- url: https://developers.telnyx.com/docs/messaging/messages/zapier-integration
  content_hash: aad83743cb42ebbc89f6978b6f626af75781bd0d86f1dc76eec2c92463a1daa1
- url: https://developers.telnyx.com/docs/messaging/toll-free-verification/index
  content_hash: 4252b4aba3308d22e312c4bfc31ff2bf8b9dad3363bc6fa0d6dd8cc1765f4379
- url: https://developers.telnyx.com/docs/messaging/toll-free-verification/troubleshooting
  content_hash: 73f55d4531a2ff98fb6c9a7234dfb34e6b4429f9a1fdbc66b6c62d286cb29463
- url: https://developers.telnyx.com/docs/messaging/whatsapp/embedded-signup
  content_hash: 2ed927e07af5e37713ddd6b340998cd8842b6303ef28e2428218537475463b8c
- url: https://developers.telnyx.com/docs/messaging/whatsapp/embedded-signup/tech-provider
  content_hash: bb93e5d911b134f7064cd7997b82d901cca70eae5ee880c925434e16bb05f284
- url: https://developers.telnyx.com/docs/messaging/whatsapp/manage-templates
  content_hash: ed0efe6efb4a082f13f54662244ee901249886ad4eed11780a77d535efca8e89
- url: https://developers.telnyx.com/docs/messaging/whatsapp/quickstart/index
  content_hash: abd0f4264c0b578171e98a4800bc241b283f1640a411eb55d283297c41637ae9
- url: https://developers.telnyx.com/docs/messaging/whatsapp/send-messages/index
  content_hash: 6c916c387118b87a1258ad874d5461c0bf493edb141be63764cac4cb36a2cdcb
updated_at: 2026-06-11T10:38:44Z
---

# Telnyx Messaging Features

*Part 4 of 5 — see also: [Part 1](telnyx-messaging-features--part-1.md), [Part 2](telnyx-messaging-features--part-2.md), [Part 3](telnyx-messaging-features--part-3.md), [Part 5](telnyx-messaging-features--part-5.md)*

Covers Telnyx messaging capabilities including MMS SMIL templates, Sticky Sender, URL Shortening, Zapier integration, toll-free verification, and the full WhatsApp Business messaging workflow from embedded signup through template management and message sending.

## WhatsApp Message Templates

WhatsApp requires pre-approved message templates for business-initiated conversations. Meta review typically takes 24–48 hours.

Before submitting templates, set a display name for your phone number—templates from numbers without an approved display name are rejected. Always include sample values in the `example` field when templates contain parameters; templates without examples are typically rejected. Complete your business profile (website, description, category) before submitting.

### Template Categories

| Category | Use Case | Requires Opt-in | Pricing Tier |
|---|---|---|---|
| AUTHENTICATION | OTP codes, login verification | No | Lowest |
| UTILITY | Order updates, shipping, account alerts | Yes | Medium |
| MARKETING | Promotions, newsletters, product launches | Yes | Highest |

Choose the most specific category—Meta may reclassify miscategorized templates, affecting pricing and delivery.

### Authentication Rules

- Must contain a one-time code or password
- Must include a copy-code or one-tap button
- Cannot include URLs or media (except the OTP button)
- Limited to one code parameter

### Naming Rules

- Lowercase letters, numbers, and underscores only
- Maximum 512 characters
- Must be unique within your WABA for each language
- Avoid words like `test`, `sample`, `demo`—Meta flags these for extra review

### Managing Templates

**List templates**:

```bash
curl -X GET "https://api.telnyx.com/v2/whatsapp/message_templates" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

Filter by status: `?filter[status]=APPROVED` or search by name: `?filter[search]=welcome`

**Create an authentication template** with OTP button:

```bash
curl -X POST "https://api.telnyx.com/v2/whatsapp/message_templates" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "login_verification",
    "category": "AUTHENTICATION",
    "language": "en_US",
    "components": [
      {"type": "BODY", "text": "Your verification code is {{1}}. Do not share this code.",
       "example": {"body_text": ["123456"](123456.md)}},
      {"type": "BUTTONS", "buttons": [{"type": "OTP", "otp_type": "COPY_CODE", "text": "Copy Code"}]}
    ]
  }'
```

**Create a marketing template** with header, body parameters, footer, and URL button.

**Create a utility template** for transactional updates like order confirmations.

**Multi-language templates**: Create the same template name in multiple languages; each variant is reviewed independently.

**Update a template**: Only `APPROVED` or `REJECTED` templates can be updated. Editing an approved template resets its status to `PENDING`. Edit and resubmit rejected templates rather than creating new ones—Meta enforces a 30-day restriction on reusing template names.

**Delete a template**: `DELETE /v2/whatsapp/message_templates/{template_id}` — permanent and irreversible.

### Error Handling

| Error Code | Description | Resolution |
|---|---|---|
| `40008` | Template operation failed | Check template status and Meta error details |
| `10004` | Missing required parameter | Ensure all required fields are included |
| `10032` | Invalid enumerated value | Check category and language codes |

## WhatsApp Quickstart

This end-to-end guide covers account setup through sending your first message.

### Step 1 — Set Up Telnyx Account

Create an account at [telnyx.com/sign-up](https://telnyx.com/sign-up), complete verification, add billing, and generate an API key from **Developer Center → API Keys**.

### Step 2 — Connect WhatsApp Business Account

Navigate to **Messaging → WhatsApp** in the Portal, click **Connect WhatsApp Business Account**, and follow the [WhatsApp Embedded Signup](whatsapp-embedded-signup.md) flow. If registering a landline, choose phone call verification instead of SMS.

### Step 3 — Create a Message Template

Create your first template via API (see [WhatsApp Message Templates](whatsapp-message-templates.md) above). Start with simple templates for faster approval.

### Step 4 — Send Your First Message

```bash
curl -X POST "https://api.telnyx.com/v2/messages/whatsapp" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "from": "+15551234567",
    "to": "+15557654321",
    "whatsapp_message": {
      "type": "template",
      "template": {
        "name": "welcome_message",
        "language": {"policy": "deterministic", "code": "en_US"},
        "components": [{"type": "body", "parameters": [{"type": "text", "text": "John"}]}]
      }
    }
  }'
```

The messaging profile is automatically resolved from the `from` number.

### Step 5 — Set Up Webhooks

Configure a webhook URL on your messaging profile to receive real-time events: `message.sent`, `message.delivered`, `message.read`, `message.failed`, and `message.received`.

### Step 6 — Handle Webhook Events

Implement a webhook endpoint to track delivery status and respond to inbound messages. Within the 24-hour conversation window (opened when the recipient messages you), you can send free-form messages without a template.

### Common Issues

- **Template not approved**: Verify template status, ensure exact name match, wait for Meta approval
- **Phone number not verified**: Complete verification in the Portal
- **Outside 24-hour window**: Use approved templates; free-form messages only work within 24 hours of the recipient's last message
- **Invalid recipient**: Verify recipient has WhatsApp, check number format with country code
