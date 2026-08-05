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

*Part 5 of 6 — see also: [Part 1](whatsapp-business-on-telnyx--part-1.md), [Part 2](whatsapp-business-on-telnyx--part-2.md), [Part 3](whatsapp-business-on-telnyx--part-3.md), [Part 4](whatsapp-business-on-telnyx--part-4.md), [Part 6](whatsapp-business-on-telnyx--part-6.md)*

A consolidated reference for using the WhatsApp Business Platform through Telnyx as a Meta Business Solution Provider. It covers account setup, message types and templates, conversation-based billing, webhooks, voice calling, troubleshooting, and frequently asked questions.

## Troubleshooting

### Template Issues

**Template rejected by Meta** — Meta's rejection messages are often generic. Check these common causes in order:

1. **Missing sample values** — Does the template have variables but no `example` field? This is the #1 cause of rejection. Edit the template, add sample values, and resubmit.
2. **No display name** — Is the phone number's display name approved? Check in Meta Business Manager.
3. **Incomplete business profile** — Is the website, description, and category filled in?
4. **Template name** — Does the name contain "test", "sample", or "demo"? Edit and rename if possible, or create a new template with a descriptive name.
5. **Wrong category** — Is promotional content submitted as Utility? Change the category to Marketing.
6. **Content too vague** — Does the template have a clear, specific purpose? Add more fixed text and context.
7. **Variable placement** — Are variables at the start/end of the body, or stacked together? Restructure the text.

Edit and resubmit rejected templates — there is no limit on edits. Do not delete and recreate, as the template name cannot be reused for 30 days.

**Template stuck in PENDING status** — Meta's review typically takes 24–48 hours. Authentication templates are usually auto-approved within minutes. If a template has been pending for more than 48 hours, check the template status in Meta Business Manager directly — the status there is authoritative. The template may have been approved or rejected on Meta's side but the status hasn't synced. If pending for more than 7 days, delete and resubmit with improved content.

**Template category was changed by Meta** — Since April 2025, Meta auto-reclassifies templates that don't match their category. The most common change is Utility → Marketing, which affects per-conversation pricing. If a template contains promotional language (discounts, offers, sales, promo codes), submit it as Marketing from the start.

### Message Delivery Issues

**Error code 40008** — Indicates the template could not be used for sending. This is a general template error — possible causes include:

- **Template still pending review** — Check template status; it may not be approved yet
- **Template was rejected** — Review and fix the template, then resubmit
- **Template was paused** — Meta paused it due to low quality rating. Wait for the pause to lift or edit the template.
- **Template was disabled** — The template was permanently disabled due to repeated quality issues. Create a new template.
- **Template name or language mismatch** — Verify the template name and language code in the send request match exactly what was submitted

Error code `40008` is also the general WhatsApp error code. The response body contains the specific Meta API error. Common causes:

- **24-hour window expired** — Use a template message to re-initiate the conversation
- **Invalid recipient** — Number doesn't have WhatsApp or has blocked your business
- **Rate limit exceeded** — You've hit your messaging limit tier
- **Phone number not registered** — Ensure your sender number is verified and registered with your WABA

**Free-form messages fail (text, media, interactive)** — Non-template messages can only be sent within the 24-hour conversation window. The window opens when the recipient sends a message to your business number, or when you send a template message and the recipient replies. Outside this window, only approved template messages can be sent.

**Message sent but not delivered** — Recipient may be offline (WhatsApp will retry delivery), may have blocked your number, or their phone may have no storage space. Check the delivery status webhook for specific error details.

**Message sent but not showing as "read"** — Read receipts are only sent if the recipient has read receipts enabled in their WhatsApp settings. Many users disable this. A message can be delivered and read without you receiving a "read" status.

### Quality Rating Issues

**Quality rating dropped to Yellow or Red** — Customers are reporting or blocking your messages. Review your message content for relevance, ensure you have proper opt-in before messaging customers, reduce message frequency if you're sending too often, and improve template content quality and targeting.

**Messaging limit reduced** — If your quality rating drops to Red, Meta may reduce your messaging limit tier. To recover, improve your quality rating by reducing blocks and reports, then your tier will gradually increase again.

**Template paused by Meta** — Meta automatically pauses templates with high complaint rates. Pause durations escalate: first pause 3 hours, second pause 6 hours, third pause permanently disabled. During a pause, edit the template content to improve relevance and reduce complaints; changes take effect within 2 minutes, allowing immediate reuse without waiting for the pause period to end.

### Getting More Help

If you're experiencing an issue not covered here, contact [Telnyx Support](https://support.telnyx.com) with:

- Your WABA ID
- Phone number
- Message ID or template name (if applicable)
- Error code and full error response
- Description of the problem
