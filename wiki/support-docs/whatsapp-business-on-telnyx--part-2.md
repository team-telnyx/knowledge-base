---
title: WhatsApp Business on Telnyx
summary: A consolidated reference for using the WhatsApp Business Platform through
  Telnyx as a Meta Business Solution Provider. It covers account setup, message types
  and templates, conversation-based billing, webhooks, voice calling, troubleshooting,
  and frequently asked questions.
sources:
- url: https://support.telnyx.com/en/articles/13986480-what-is-whatsapp-business-platform
- url: https://support.telnyx.com/en/articles/13986481-whatsapp-message-types-explained
- url: https://support.telnyx.com/en/articles/13986483-whatsapp-message-templates-guide
- url: https://support.telnyx.com/en/articles/13986484-whatsapp-pricing-on-telnyx
- url: https://support.telnyx.com/en/articles/13986485-how-to-set-up-whatsapp-on-telnyx
- url: https://support.telnyx.com/en/articles/13986486-how-to-create-whatsapp-message-templates
- url: https://support.telnyx.com/en/articles/13986487-how-to-configure-whatsapp-webhooks
- url: https://support.telnyx.com/en/articles/13986488-whatsapp-faq
- url: https://support.telnyx.com/en/articles/13986489-whatsapp-troubleshooting-guide
- url: https://support.telnyx.com/en/articles/14668631-enabling-whatsapp-business-calling-on-telnyx-numbers
- url: https://support.telnyx.com/en/collections/18868947-whatsapp-business
updated_at: 2026-08-05T13:34:13Z
---

# WhatsApp Business on Telnyx

*Part 2 of 6 — see also: [Part 1](whatsapp-business-on-telnyx--part-1.md), [Part 3](whatsapp-business-on-telnyx--part-3.md), [Part 4](whatsapp-business-on-telnyx--part-4.md), [Part 5](whatsapp-business-on-telnyx--part-5.md), [Part 6](whatsapp-business-on-telnyx--part-6.md)*

A consolidated reference for using the WhatsApp Business Platform through Telnyx as a Meta Business Solution Provider. It covers account setup, message types and templates, conversation-based billing, webhooks, voice calling, troubleshooting, and frequently asked questions.

## Message Templates

### Template Structure

A template consists of these components:

| Component | Required | Limits | Description |
| --- | --- | --- | --- |
| Name | Yes | — | Unique identifier (lowercase, underscores only). Avoid "test", "sample", "demo" in names. |
| Language | Yes | — | Language code (e.g., `en_US`, `es`, `pt_BR`) |
| Category | Yes | — | Marketing, Utility, or Authentication |
| Header | No | 60 chars (text) | Text, image, video, or document |
| Body | Yes | 1,024 chars | Main message text (supports variables `#{{1}}`, `#{{2}}`) |
| Footer | No | 60 chars | Small text at the bottom. No variables. |
| Buttons | No | 3 QR / 2 CTA | Quick reply or call-to-action (URL or phone number) |
| Sample Values | Strongly recommended | — | Example values for each variable via the `example` field. Required for approval if template has parameters. |

### Template Categories

- **Marketing** — For promotions, offers, product recommendations, and general outreach. These have the highest per-conversation cost and the most scrutiny from Meta during review.
- **Utility** — For transactional messages: order confirmations, shipping updates, appointment reminders, account notifications. These typically have higher approval rates and lower per-conversation cost. Since April 2025, Meta automatically reclassifies templates that contain promotional language (discounts, offers, sales, promo codes) from Utility to Marketing, which changes the per-conversation pricing. Choose the category that matches your content.
- **Authentication** — For one-time passwords (OTP) and verification codes. Meta provides a pre-built authentication template format. These are typically auto-approved and have the lowest per-conversation cost. The OTP must be in the body as a variable.

### Prerequisites for Template Approval

Templates will be rejected if these are not completed first:

1. **Display name** — The phone number must have an approved display name set in Meta Business Manager. Without it, all templates are rejected.
2. **Business profile** — Fill in the business website (HTTPS), description, industry category, and address.
3. **Sample values** — Include the `example` field with realistic sample data for each variable in the template. Meta's human reviewers use these to evaluate the rendered message.
4. **Business verification** — Complete Meta's business verification process. Unverified businesses face stricter review and lower messaging limits.

### Approval Process

1. **Submit** — Create the template via the Telnyx API (`POST` to the Templates endpoint).
2. **Review** — Meta reviews the template. Authentication templates are typically auto-approved. Marketing and Utility go through human review (24–48 hours).
3. **Approved or Rejected** — The status updates via the API. If rejected, edit the template content and resubmit (unlimited edits for rejected templates).

Template status values: `PENDING`, `APPROVED`, `REJECTED`, `PAUSED`, `DISABLED`.

### Template Components in Detail

- **Body (Required)** — Maximum 1,024 characters. Use `#{{1}}`, `#{{2}}`, etc. for variable placeholders. Variables must be numbered sequentially starting at `#{{1}}`; do not skip numbers. Do not place variables at the very start or end of the body, and do not stack variables without text between them (e.g., `#{{1}}#{{2}}` is rejected). Keep more fixed text than variables — high variable density looks like spam to reviewers.
- **Header (Optional)** — Appears above the body. Maximum 60 characters for text headers. Can be text (supports one variable), image (JPEG or PNG), video (MP4), or document (PDF or other).
- **Footer (Optional)** — Small text below the body. Maximum 60 characters. Does not support variables. Often used for disclaimers or opt-out text.
- **Buttons (Optional)** — Quick Reply (up to 3 buttons that send a predefined response when tapped) or Call-to-Action (up to 2 buttons that open a URL or dial a phone number).

### Sample Values

Templates with parameters that do not include sample values are almost always rejected. Meta's reviewers need sample values to see what the rendered message will look like. When a template contains variables, include the `example` field in each component that uses variables.

Body example format:

```
"components": [{
  "type": "BODY",
  "text": "Hi #{{1}}, your order #{{2}} has been confirmed.",
  "example": {
    "body_text": ["Barry Reynolds", "ORD-12345"](barry-reynolds-ord-12345.md)
  }
}]
```

Text header example format:

```
"components": [{
  "type": "HEADER",
  "format": "TEXT",
  "text": "Order #{{1}} Update",
  "example": {
    "header_text": ["ORD-12345"]
  }
}]
```

Media header example format:

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

### Template Naming Rules

- Lowercase letters, numbers, and underscores only (e.g., `order_confirmation_v2`)
- No spaces, hyphens, or special characters
- Avoid names containing "test", "sample", "demo", or "billing" — Meta's reviewers flag these as test templates and reject them
- Use descriptive, specific names that reflect the template's purpose (e.g., `shipping_update` instead of `notification_1`)
- After deleting a template, the name cannot be reused for 30 days

### Template Quality and Pacing

After approval, Meta monitors template performance based on user feedback (blocks, spam reports, engagement). Templates receive a quality rating:

- **High quality** (green) — Good engagement, low complaint rate
- **Medium quality** (yellow) — Some negative feedback, at risk of pausing
- **Low quality** (red) — High complaint rate, may be paused automatically

New templates and templates without a High quality rating may be subject to pacing — Meta gradually increases delivery volume while monitoring user feedback. If feedback is negative, delivery pauses.

If a template receives too much negative feedback, Meta pauses it automatically. Pause durations escalate: 3 hours → 6 hours → permanently disabled. During a pause, edit the template content to improve relevance and reduce complaints; changes take effect within 2 minutes, allowing immediate reuse without waiting for the pause period to end.

### Common Rejection Reasons

- **Missing sample values** — Template has variables but no `example` field. This is the most common rejection cause.
- **Empty display name** — The phone number doesn't have a display name set or approved.
- **Incomplete business profile** — Missing website, description, or industry category.
- **Template name contains "test" or "sample"** — Meta reviewers flag these as test templates.
- **Vague or generic content** — Templates like "Hi #{{1}}, we have an update" with no specific purpose.
- **Wrong category** — Promotional content submitted as Utility. Meta may reclassify or reject.
- **Variable-only content** — Body is mostly variables with little fixed text.
- **Variables at start/end of body** — Body text cannot begin or end with a variable placeholder.
- **Adjacent variables** — `#{{1}}#{{2}}` without text between them is rejected.
- **URL in body text** — Use CTA buttons for links. Do not use URL shorteners or wa.me links.
- **Missing opt-out language** — Marketing templates should include an unsubscribe option.
- **Violates Meta Commerce Policy** — Content includes prohibited items (alcohol, gambling, etc.)
- **Duplicate content** — Too similar to an existing template in the same language.

Meta's rejection messages are often generic ("This template was rejected by a Meta team"). If rejected, fix the most likely cause, edit the template, and resubmit — do not delete and recreate with the same name, as deleted template names cannot be reused for 30 days.

### Tips for Approval

- Always provide sample values in the `example` field for every variable
- Complete the business profile and display name before submitting any templates
- Use specific, descriptive template names (e.g., `shipping_update` not `notification_1`)
- Start with Authentication or Utility templates — they have higher approval rates
- Include clear, fixed text that makes the template's purpose obvious
- For Marketing templates, include opt-out text in the footer
- Use CTA buttons for URLs rather than embedding links in body text
- New WABAs face stricter review for the first 30 days — start simple

### Managing Templates

You can list, update, and delete templates via the Telnyx API. Template names are immutable — if you need to change the name, create a new template and delete the old one (note the 30-day name reuse restriction).

Rejected templates can be edited and resubmitted unlimited times. Approved templates can also be edited, but edits trigger a new review cycle and the template cannot be used for sending while under re-review. Changes to the body or category require re-approval; in many cases, it's easier to create a new template.

Meta allows up to 6,000 templates per WABA. In practice, keep your template library focused and well-organized.
