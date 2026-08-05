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

*Part 4 of 4 — see also: [Part 1](whatsapp-on-telnyx--part-1.md), [Part 2](whatsapp-on-telnyx--part-2.md), [Part 3](whatsapp-on-telnyx--part-3.md)*

Telnyx provides a complete WhatsApp Business Platform integration covering embedded signup (for direct customers and Tech Providers), WhatsApp Business Calling, and message template management. This page consolidates the onboarding flows, API endpoints, voice calling setup, and template lifecycle into a single reference.

## Manage WhatsApp Message Templates

WhatsApp requires pre-approved message templates for business-initiated conversations. Use the Telnyx Management API to create, review, and manage templates programmatically. Templates must be approved by Meta before use; review typically takes 24–48 hours.

### List Templates

```
curl -X GET "https://api.telnyx.com/v2/whatsapp/message_templates" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

Filter by status or search by name:

```
curl -X GET "https://api.telnyx.com/v2/whatsapp/message_templates?filter[status]=APPROVED" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

### Create a Template

Submit a new template for Meta review. Set a display name for the phone number before submitting templates — templates submitted from numbers without an approved display name are rejected by Meta. Always include sample values in the `example` field when your template contains parameters; templates without examples are typically rejected.

**Authentication template** — includes an OTP code with a copy-code button:

```
curl -X POST "https://api.telnyx.com/v2/whatsapp/message_templates" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "login_verification",
    "category": "AUTHENTICATION",
    "language": "en_US",
    "components": [
      {
        "type": "BODY",
        "text": "Your verification code is {{1}}. Do not share this code.",
        "example": { "body_text": ["123456"](123456.md) }
      },
      {
        "type": "BUTTONS",
        "buttons": [
          { "type": "OTP", "otp_type": "COPY_CODE", "text": "Copy Code" }
        ]
      }
    ]
  }'
```

**Marketing template** — supports rich media headers, body text with parameters, and call-to-action buttons (HEADER, BODY, FOOTER, BUTTONS components).

**Utility template** — for transactional updates like order confirmations, shipping notifications, and account alerts.

### Get, Update, and Delete a Template

- **Get** — `GET /v2/whatsapp/message_templates/{template_id}`
- **Update** — `PATCH /v2/whatsapp/message_templates/{template_id}`. Only templates in `APPROVED` or `REJECTED` status can be updated. Editing an approved template resets its status to `PENDING` while Meta reviews the changes, and the template is temporarily unavailable for sending. Edit and resubmit rejected templates rather than creating new ones — Meta enforces a 30-day restriction on reusing template names.
- **Delete** — `DELETE /v2/whatsapp/message_templates/{template_id}`. This action cannot be undone.

### Template Categories

| Category | Use Case | Requires Opt-in | Pricing Tier |
| --- | --- | --- | --- |
| **AUTHENTICATION** | OTP codes, login verification | No | Lowest |
| **UTILITY** | Order updates, shipping, account alerts | Yes | Medium |
| **MARKETING** | Promotions, newsletters, product launches | Yes | Highest |

Choose the most specific category. Meta may reclassify templates that don't match their declared category, which can affect pricing and delivery.

**Authentication rules:** Must contain a one-time code or password, must include a copy-code or one-tap button, cannot include URLs or media (except the OTP button), and is limited to one code parameter.

**Naming rules:** Lowercase letters, numbers, and underscores only; maximum 512 characters; must be unique within your WABA for each language; avoid words like `test`, `sample`, `demo` — Meta flags these for extra review.

### Approval Tips

- **Always include sample values** — Templates with parameters but no `example` field are almost always rejected.
- **Set a display name first** — Templates submitted from numbers without an approved display name get rejected.
- **Complete your business profile** — Add website, description, and category before submitting. Incomplete profiles increase rejection rates.
- **Edit rejected templates, don't recreate** — Meta enforces a 30-day restriction on reusing template names.
- **Match category to content** — Meta may reclassify miscategorized templates, affecting pricing and delivery.

### Multi-Language Templates

Create the same template in multiple languages. Each language variant is reviewed independently. Template names must be unique per language within a WABA.

### Error Handling

| Error Code | Description | Resolution |
| --- | --- | --- |
| `40008` | Template operation failed (catch-all) | Check template status and Meta error details |
| `10004` | Missing required parameter | Ensure all required fields are included |
| `10032` | Invalid enumerated value | Check category and language codes |

Common issues include rejected templates (review best practices), duplicate names (must be unique per language within a WABA), and invalid parameters (ensure `example` values match parameter count in template body).
