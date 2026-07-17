---
source_url: https://support.telnyx.com/en/articles/13986483-whatsapp-message-templates-guide
title: "WhatsApp Message Templates Guide"
description: "How WhatsApp message templates work, the approval process, categories, and tips for getting templates approved. See Telnyx guidance and requirements."
scraped: 2026-07-08
content_hash: 634a8860642b2ab4a646a4abc5e096ac2d02e3e3e9096a061bc789c933edbc28
---







# WhatsApp Message Templates Guide

How WhatsApp message templates work, the approval process, categories, and tips for getting templates approved. See Telnyx guidance and requirements.




## What Are Message Templates?

Message templates are pre-approved message formats required by Meta to send business-initiated messages on WhatsApp. Every message sent outside the 24-hour conversation window must use an approved template.

## Template Structure

A template consists of these components:

|  |  |  |  |
| --- | --- | --- | --- |
| **Component** | **Required** | **Limits** | **Description** |
| Name | Yes | — | Unique identifier (lowercase, underscores only). Avoid "test", "sample", "demo" in names. |
| Language | Yes | — | Language code (e.g., en\_US, es, pt\_BR) |
| Category | Yes | — | Marketing, Utility, or Authentication |
| Header | No | 60 chars (text) | Text, image, video, or document |
| Body | Yes | 1,024 chars | Main message text (supports variables #{{1}}, #{{2}}) |
| Footer | No | 60 chars | Small text at the bottom. No variables. |
| Buttons | No | 3 QR / 2 CTA | Quick reply or call-to-action (URL or phone number) |
| Sample Values | **Strongly recommended** | — | Example values for each variable via the `example` field. Required for approval if template has parameters. |

## Template Categories

## Marketing

For promotions, offers, product recommendations, and general outreach. These have the highest per-conversation cost and the most scrutiny from Meta during review.

## Utility

For transactional messages: order confirmations, shipping updates, appointment reminders, account notifications. These typically have higher approval rates and lower per-conversation cost.

⚠️ **Category reclassification:** Since April 2025, Meta automatically reclassifies templates that contain promotional language (discounts, offers, sales, promo codes) from Utility to Marketing. This changes the per-conversation pricing. Choose the category that matches your content.

## Authentication

For one-time passwords (OTP) and verification codes. Meta provides a pre-built authentication template format. These are typically auto-approved and have the lowest per-conversation cost. The OTP must be in the body as a variable.

## Prerequisites for Template Approval

🔴 **Templates will be rejected if these are not completed first:**

1. **Display name** — The phone number must have an approved display name set in Meta Business Manager. Without it, all templates are rejected.
2. **Business profile** — Fill in the business website (HTTPS), description, industry category, and address.
3. **Sample values** — Include the `example` field with realistic sample data for each variable in the template. Meta's human reviewers use these to evaluate the rendered message.

## Approval Process

1. **Submit** — Create the template via the Telnyx API (`POST` to the Templates endpoint)
2. **Review** — Meta reviews the template. Authentication templates are typically auto-approved. Marketing and Utility go through human review (24–48 hours).
3. **Approved or Rejected** — The status updates via the API. If rejected, edit the template content and resubmit (unlimited edits for rejected templates).

Template status values: `PENDING`, `APPROVED`, `REJECTED`, `PAUSED`, `DISABLED`.

## Template Quality and Pacing

After approval, Meta monitors template performance based on user feedback (blocks, spam reports, engagement). Templates receive a quality rating:

* **High quality** (green) — Good engagement, low complaint rate
* **Medium quality** (yellow) — Some negative feedback, at risk of pausing
* **Low quality** (red) — High complaint rate, may be paused automatically

**Template pacing:** New templates and templates without a High quality rating may be subject to pacing — Meta gradually increases delivery volume while monitoring user feedback. If feedback is negative, delivery pauses.

**Pausing:** If a template receives too much negative feedback, Meta pauses it automatically. Pause durations escalate: 3 hours → 6 hours → permanently disabled.

## Common Rejection Reasons

* **Missing sample values** — Template has variables but no `example` field. This is the most common rejection cause.
* **Empty display name** — The phone number doesn't have a display name set or approved.
* **Incomplete business profile** — Missing website, description, or industry category.
* **Template name contains "test" or "sample"** — Meta reviewers flag these as test templates.
* **Vague or generic content** — Templates like "Hi #{{1}}, we have an update" with no specific purpose.
* **Wrong category** — Promotional content submitted as Utility. Meta may reclassify or reject.
* **Variable-only content** — Body is mostly variables with little fixed text.
* **Variables at start/end of body** — Body text cannot begin or end with a variable placeholder.
* **Adjacent variables** — `#{{1}}#{{2}}` without text between them is rejected.
* **URL in body text** — Use CTA buttons for links. Do not use URL shorteners or wa.me links.
* **Missing opt-out language** — Marketing templates should include an unsubscribe option.
* **Violates Meta Commerce Policy** — Content includes prohibited items (alcohol, gambling, etc.)
* **Duplicate content** — Too similar to an existing template in the same language.

💡 **Tip:** Meta's rejection messages are often generic ("This template was rejected by a Meta team"). Use the list above to troubleshoot. If rejected, fix the most likely cause, edit the template, and resubmit.

## Tips for Approval

* Always provide sample values in the `example` field for every variable
* Complete the business profile and display name before submitting any templates
* Use specific, descriptive template names (e.g., `shipping_update` not `notification_1`)
* Start with Authentication or Utility templates — they have higher approval rates
* Include clear, fixed text that makes the template's purpose obvious
* For Marketing templates, include opt-out text in the footer
* Use CTA buttons for URLs rather than embedding links in body text
* New WABAs face stricter review for the first 30 days — start simple

## Related Resources

* [Send Template Messages (API Guide)](https://developers.telnyx.com/docs/messaging/whatsapp/send-messages#template-messages)

---

Related Articles

[WhatsApp Message Types Explained](https://support.telnyx.com/en/articles/13986481-whatsapp-message-types-explained)[WhatsApp Pricing on Telnyx](https://support.telnyx.com/en/articles/13986484-whatsapp-pricing-on-telnyx)[How to Create WhatsApp Message Templates](https://support.telnyx.com/en/articles/13986486-how-to-create-whatsapp-message-templates)[WhatsApp FAQ](https://support.telnyx.com/en/articles/13986488-whatsapp-faq)[WhatsApp Troubleshooting Guide](https://support.telnyx.com/en/articles/13986489-whatsapp-troubleshooting-guide)

Did this answer your question?

😞😐😃
