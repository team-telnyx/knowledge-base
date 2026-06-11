---
title: WhatsApp Business Platform
summary: WhatsApp Business Platform is Meta's API-based solution for sending and receiving
  WhatsApp messages at scale. Telnyx integrates as an official Business Solution Provider
  (BSP), offering API infrastructure for messaging, template management, phone number
  registration, webhook delivery, and WhatsApp Business Calling — all through the
  Telnyx Portal and API.
sources:
- url: https://support.telnyx.com/en/articles/13986480-what-is-whatsapp-business-platform
  content_hash: e0dfd5a11bbda9ff91f7df2855b9014ff72d33baca35f781d78b0dd85ee3e9bb
- url: https://support.telnyx.com/en/articles/13986481-whatsapp-message-types-explained
  content_hash: b84d28529808c576a61aeada7084c8b65d5f9d1d15a70b1c8d12042e741b10f8
- url: https://support.telnyx.com/en/articles/13986482-whatsapp-24-hour-conversation-window
  content_hash: 2fe960b316229561d9e5c4d5e72ed3e97453f4146e10647d69e5a910dd51a413
- url: https://support.telnyx.com/en/articles/13986483-whatsapp-message-templates-guide
  content_hash: 634a8860642b2ab4a646a4abc5e096ac2d02e3e3e9096a061bc789c933edbc28
- url: https://support.telnyx.com/en/articles/13986484-whatsapp-pricing-on-telnyx
  content_hash: c5c2d8afa84fa2f3c8ffc41d130ad99378188500be16a63f43d53f87f776535c
- url: https://support.telnyx.com/en/articles/13986485-how-to-set-up-whatsapp-on-telnyx
  content_hash: b9ca1b42fad01cb5e8d456c64f5fcffe912ea4340988c5c059337afc0df07b99
- url: https://support.telnyx.com/en/articles/13986486-how-to-create-whatsapp-message-templates
  content_hash: 74058f9e355d530d49435da50f83446fe490c185dc4037bbdff4f573030f8ab2
- url: https://support.telnyx.com/en/articles/13986487-how-to-configure-whatsapp-webhooks
  content_hash: 3165ce048d08e449a328ce473f21437e7ae480a5538c6e42f26e248bbfc6b475
- url: https://support.telnyx.com/en/articles/13986488-whatsapp-faq
  content_hash: 3154493d577f0184d1eb3aada07d2d4a697e2aee678a15ce304768eccaf2ff21
- url: https://support.telnyx.com/en/articles/13986489-whatsapp-troubleshooting-guide
  content_hash: ef49ad423dce5870a1ec3750586ab5e0d36e8fe0021539a57a44a99997dfc767
- url: https://support.telnyx.com/en/articles/14668631-enabling-whatsapp-business-calling-on-telnyx-numbers
  content_hash: a2578fc25c4f85421f3ff1fa1e72d87f822a3c32562eeb46e5ceebc64dc25fe8
- url: https://support.telnyx.com/en/collections/18868947-whatsapp-business
  content_hash: a08410203f8a1c793e98f264117954f1dc3cbeac4a31512069af01c4fd6125f8
updated_at: 2026-06-11T11:36:03Z
---

# WhatsApp Business Platform

*Part 2 of 5 — see also: [Part 1](whatsapp-business-platform--part-1.md), [Part 3](whatsapp-business-platform--part-3.md), [Part 4](whatsapp-business-platform--part-4.md), [Part 5](whatsapp-business-platform--part-5.md)*

WhatsApp Business Platform is Meta's API-based solution for sending and receiving WhatsApp messages at scale. Telnyx integrates as an official Business Solution Provider (BSP), offering API infrastructure for messaging, template management, phone number registration, webhook delivery, and WhatsApp Business Calling — all through the Telnyx Portal and API.

## Message Templates

### Template Structure

| Component | Required | Limits | Description |
|---|---|---|---|
| Name | Yes | — | Unique identifier (lowercase, underscores only). Avoid "test", "sample", "demo", "billing" in names. |
| Language | Yes | — | Language code (e.g., `en_US`, `es`, `pt_BR`) |
| Category | Yes | — | Marketing, Utility, or Authentication |
| Header | No | 60 chars (text) | Text, image, video, or document |
| Body | Yes | 1,024 chars | Main message text (supports variables `{{1}}`, `{{2}}`) |
| Footer | No | 60 chars | Small text at the bottom. No variables. Often used for disclaimers or opt-out text. |
| Buttons | No | 3 QR / 2 CTA | Quick reply or call-to-action (URL or phone number) |
| Sample Values | Strongly recommended | — | Example values for each variable via the `example` field. Required for approval if template has parameters. |

### Template Naming Rules

- Lowercase letters, numbers, and underscores only (e.g., `order_confirmation_v2`)
- No spaces, hyphens, or special characters
- Avoid names containing "test", "sample", "demo", or "billing" — Meta's reviewers flag these as test templates
- Use descriptive, specific names (e.g., `shipping_update` instead of `notification_1`)
- After deleting a template, the name cannot be reused for 30 days

### Body Variable Rules

- Variables must be numbered sequentially starting at `{{1}}`
- Do not skip numbers (e.g., `{{1}}` then `{{3}}` is invalid)
- Do not place variables at the very start or end of the body
- Do not stack variables without text between them (e.g., `{{1}}{{2}}` is rejected)
- Keep more fixed text than variables — high variable density looks like spam to reviewers

### Sample Values (Critical for Approval)

Templates with parameters that do not include sample values are almost always rejected. When a template contains variables, include the `example` field in each component that uses variables.

**Body example:**

```
"components": [{
  "type": "BODY",
  "text": "Hi {{1}}, your order {{2}} has been confirmed.",
  "example": {
    "body_text": ["Barry Reynolds", "ORD-12345"](barry-reynolds-ord-12345.md)
  }
}]
```

**Text header example:**

```
"components": [{
  "type": "HEADER",
  "format": "TEXT",
  "text": "Order {{1}} Update",
  "example": {
    "header_text": ["ORD-12345"]
  }
}]
```

**Media header example:**

```
"components": [{
  "type": "HEADER",
  "format": "IMAGE",
  "example": {
    "header_handle": ["https://example.com/product-image.jpg"]
  }
}]
```

Use realistic sample values that reflect actual use. Generic samples like "name" or "value" may still lead to rejection.

### Prerequisites for Template Approval

Templates will be rejected if these are not completed first:

1. **Display name** — The phone number must have an approved display name set in Meta Business Manager.
2. **Business profile** — Fill in the business website (HTTPS), description, industry category, and address.
3. **Business verification** — Complete Meta's business verification process. Unverified businesses face stricter review and lower messaging limits.

### Approval Process

1. **Submit** — Create the template via the Telnyx API (`POST` to the Templates endpoint)
2. **Review** — Meta reviews the template. Authentication templates are typically auto-approved. Marketing and Utility go through human review (24–48 hours).
3. **Approved or Rejected** — Status updates via the API. If rejected, edit the template content and resubmit (unlimited edits for rejected templates).

Template status values: `PENDING`, `APPROVED`, `REJECTED`, `PAUSED`, `DISABLED`.

**Editing rejected templates:** Rejected templates can be edited and resubmitted unlimited times. Edit the content, fix the issues, and resubmit — do not create a new template with the same name.

**Editing approved templates:** Approved templates can also be edited, but edits trigger a new review cycle. The template cannot be used for sending while under re-review.

Meta allows up to 6,000 templates per WABA.

### Template Quality and Pacing

After approval, Meta monitors template performance based on user feedback (blocks, spam reports, engagement). Templates receive a quality rating:

- **High quality** (green) — Good engagement, low complaint rate
- **Medium quality** (yellow) — Some negative feedback, at risk of pausing
- **Low quality** (red) — High complaint rate, may be paused automatically

**Template pacing:** New templates and templates without a High quality rating may be subject to pacing — Meta gradually increases delivery volume while monitoring user feedback.

**Pausing:** If a template receives too much negative feedback, Meta pauses it automatically. Pause durations escalate: 3 hours → 6 hours → permanently disabled. During a pause, editing the template content to improve relevance takes effect within 2 minutes, allowing immediate reuse without waiting for the pause period to end.

### Common Rejection Reasons

- **Missing sample values** — Template has variables but no `example` field. This is the most common rejection cause.
- **Empty display name** — The phone number doesn't have a display name set or approved.
- **Incomplete business profile** — Missing website, description, or industry category.
- **Template name contains "test" or "sample"** — Meta reviewers flag these as test templates.
- **Vague or generic content** — Templates like "Hi {{1}}, we have an update" with no specific purpose.
- **Wrong category** — Promotional content submitted as Utility. Since April 2025, Meta auto-reclassifies miscategorized templates from Utility to Marketing, which changes the per-conversation pricing.
- **Variable-only content** — Body is mostly variables with little fixed text.
- **Variables at start/end of body** — Body text cannot begin or end with a variable placeholder.
- **Adjacent variables** — `{{1}}{{2}}` without text between them is rejected.
- **URL in body text** — Use CTA buttons for links. Do not use URL shorteners or wa.me links.
- **Missing opt-out language** — Marketing templates should include an unsubscribe option.
- **Violates Meta Commerce Policy** — Content includes prohibited items (alcohol, gambling, etc.).
- **Duplicate content** — Too similar to an existing template in the same language.

### Tips for Getting Templates Approved

- Always provide sample values in the `example` field for every variable
- Complete the business profile and display name before submitting any templates
- Use specific, descriptive template names
- Start with Authentication or Utility templates — they have higher approval rates
- Include clear, fixed text that makes the template's purpose obvious
- For Marketing templates, include opt-out text in the footer
- Use CTA buttons for URLs rather than embedding links in body text
- New WABAs face stricter review for the first 30 days — start simple
