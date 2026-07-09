---
source_url: https://support.telnyx.com/en/articles/13986486-how-to-create-whatsapp-message-templates
scraped: 2026-07-08
content_hash: 74058f9e355d530d49435da50f83446fe490c185dc4037bbdff4f573030f8ab2
---

How to Create WhatsApp Message Templates | Telnyx Help Center

[Skip to main content](#main-content)

# How to Create WhatsApp Message Templates

Step-by-step guide to creating, managing, and getting WhatsApp message templates approved.

Written by Telnyx Engineering

March 16, 2026

Table of contents

# Before You Start

⚠️ **Complete these steps before creating templates.** Templates submitted without these prerequisites are likely to be rejected by Meta.

* **Set a display name** — The phone number must have an approved display name. Templates submitted from numbers without a display name are rejected automatically. Set this in Meta Business Manager under your phone number settings.
* **Complete the business profile** — Fill in the business website (must be HTTPS), description, industry category, and address. Incomplete profiles significantly increase rejection rates, especially for new WABAs.
* **Verify your business** — Complete Meta's business verification process. Unverified businesses face stricter review and lower messaging limits.

# Creating a Template via the API

Use the Telnyx Message Templates API to create templates. Each template requires:

* **Name** — Unique identifier (lowercase letters, numbers, and underscores only)
* **Language** — Language code (e.g., `en_US`, `es`, `pt_BR`)
* **Category** — `MARKETING`, `UTILITY`, or `AUTHENTICATION`
* **Components** — The template structure (header, body, footer, buttons)

## Template Naming Rules

* Lowercase letters, numbers, and underscores only (e.g., `order_confirmation_v2`)
* No spaces, hyphens, or special characters
* **Avoid names containing "test", "sample", "demo", or "billing"** — Meta's reviewers flag these as test templates and reject them
* Use descriptive, specific names that reflect the template's purpose (e.g., `shipping_update` instead of `notification_1`)
* After deleting a template, the name cannot be reused for 30 days

# Template Components

## Body (Required)

The main message text. Maximum 1,024 characters. Use `#{{1}}`, `#{{2}}`, etc. for variable placeholders that get filled in when sending.

Example: `Hi #{{1}}, your order #{{2}} has shipped and will arrive by #{{3}}.`

**Variable rules:**

* Variables must be numbered sequentially starting at `#{{1}}`
* Do not skip numbers (e.g., `#{{1}}` then `#{{3}}` is invalid)
* Do not place variables at the very start or end of the body
* Do not stack variables without text between them (e.g., `#{{1}}#{{2}}` is rejected)
* Keep more fixed text than variables — high variable density looks like spam to reviewers

## Header (Optional)

Appears above the body. Maximum 60 characters for text headers. Can be:

* **Text** — Short text (supports one variable)
* **Image** — JPEG or PNG
* **Video** — MP4
* **Document** — PDF or other document

## Footer (Optional)

Small text below the body. Maximum 60 characters. Does not support variables. Often used for disclaimers or opt-out text.

## Buttons (Optional)

* **Quick Reply** — Up to 3 buttons that send a predefined response when tapped
* **Call-to-Action** — Up to 2 buttons that open a URL or dial a phone number

# Sample Values (Critical for Approval)

🔴 **Templates with parameters that do not include sample values are almost always rejected.** Meta's reviewers need sample values to see what the rendered message will look like.

When a template contains variables (`#{{1}}`, `#{{2}}`, etc.), include the `example` field in each component that uses variables. This tells Meta's reviewers what the message will look like with real data.

**Body example format:**

```
"components": [{
  "type": "BODY",
  "text": "Hi #{{1}}, your order #{{2}} has been confirmed.",
  "example": {
    "body_text": [["Barry Reynolds", "ORD-12345"]]
  }
}]
```

**Text header example format:**

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

**Media header example format:**

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

# Approval Process

1. Submit the template via the API
2. Template status changes to `PENDING`
3. Meta reviews the template (typically within 24 hours, sometimes up to 48)
4. Status changes to `APPROVED` or `REJECTED`

**Authentication templates** are typically auto-approved by Meta if they follow the standard OTP format. Marketing and Utility templates go through human review.

If rejected, you can edit the template content and resubmit — there is no limit on edits to rejected templates. Do not delete and recreate with the same name, as deleted template names cannot be reused for 30 days.

# Tips for Getting Templates Approved

* **Always include sample values** — Provide the `example` field for every component that uses variables. This is the single most common reason for rejection.
* **Choose the right category** — Don't submit promotional content as Utility. Since April 2025, Meta auto-reclassifies miscategorized templates from Utility to Marketing, which changes the pricing.
* **Include meaningful fixed text** — Templates that are mostly variables with little fixed text are rejected.
* **Add opt-out for Marketing** — Include "Reply STOP to unsubscribe" or similar in the footer.
* **Use CTA buttons for links** — Don't put URLs in the body text. Use a URL button instead. Do not use URL shorteners or wa.me links.
* **Be specific and realistic** — Vague templates like "Hi #{{1}}, we have an update for you" are rejected. Make the purpose clear.
* **Use descriptive template names** — Names like `test_template` or `template_1` get flagged.
* **Complete your business profile first** — Display name, website, description, and category should all be filled in before submitting templates.

# Managing Templates

You can list, update, and delete templates via the Telnyx API. Template names are immutable — if you need to change the name, create a new template and delete the old one (note the 30-day name reuse restriction).

**Editing rejected templates:** Rejected templates can be edited and resubmitted unlimited times. Edit the content, fix the issues, and resubmit — do not create a new template with the same name.

**Editing approved templates:** Approved templates can also be edited, but edits trigger a new review cycle. The template cannot be used for sending while under re-review.

# Related Resources

* [Send Template Messages (API Guide)](https://developers.telnyx.com/docs/messaging/whatsapp/send-messages#template-messages)
* [Template Components Reference](https://developers.telnyx.com/docs/messaging/whatsapp/send-messages#template-components)

---

Related Articles

[WhatsApp Message Types Explained](https://support.telnyx.com/en/articles/13986481-whatsapp-message-types-explained)[WhatsApp Message Templates Guide](https://support.telnyx.com/en/articles/13986483-whatsapp-message-templates-guide)[How to Set Up WhatsApp on Telnyx](https://support.telnyx.com/en/articles/13986485-how-to-set-up-whatsapp-on-telnyx)[WhatsApp FAQ](https://support.telnyx.com/en/articles/13986488-whatsapp-faq)[WhatsApp Troubleshooting Guide](https://support.telnyx.com/en/articles/13986489-whatsapp-troubleshooting-guide)

Did this answer your question?

😞😐😃

Table of contents
