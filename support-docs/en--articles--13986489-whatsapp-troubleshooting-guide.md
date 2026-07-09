---
source_url: https://support.telnyx.com/en/articles/13986489-whatsapp-troubleshooting-guide
scraped: 2026-07-08
content_hash: ef49ad423dce5870a1ec3750586ab5e0d36e8fe0021539a57a44a99997dfc767
---

WhatsApp Troubleshooting Guide | Telnyx Help Center

[Skip to main content](#main-content)

# WhatsApp Troubleshooting Guide

Common WhatsApp issues and how to resolve them: signup, templates, delivery, and quality rating.

Written by Telnyx Engineering

March 16, 2026

Table of contents

# Signup Issues

## Embedded Signup flow fails or shows an error

* Ensure your Facebook account has **admin access** to the Meta Business Manager
* Clear browser cookies and try again in an incognito/private window
* Disable browser extensions that may block Facebook popups
* Check that you don't have an existing WABA linked to a different BSP for the same number

## Phone number verification fails

* Wait a few minutes between attempts — there is a rate limit on verification codes
* If using SMS verification on a landline, switch to **phone call verification** instead
* Ensure the number is not already registered with WhatsApp consumer app
* Verify the number can receive calls or SMS (check with your carrier)

## Number already in use error

The number is registered with WhatsApp on a phone. To use it with the Business Platform, first delete the WhatsApp account from the phone (WhatsApp → Settings → Account → Delete my account).

## Display name not set or rejected

If the display name was skipped during Embedded Signup or was rejected by Meta:

* Go to **Meta Business Manager** → WhatsApp Accounts → your WABA → Phone Numbers
* Click the phone number and set the display name
* The display name must match or relate to your verified business name
* Display name review takes up to 48 hours
* **Do not submit templates until the display name is approved** — they will be rejected

# Template Issues

## Template rejected by Meta

Meta's rejection messages are often generic. Check these common causes in order:

1. **Missing sample values** — Does the template have variables (###{{1}}, ###{{2}}) but no `example` field? This is the #1 cause of rejection. Edit the template, add sample values, and resubmit.
2. **No display name** — Is the phone number's display name approved? Check in Meta Business Manager.
3. **Incomplete business profile** — Is the website, description, and category filled in?
4. **Template name** — Does the name contain "test", "sample", or "demo"? Edit and rename if possible, or create a new template with a descriptive name.
5. **Wrong category** — Is promotional content submitted as Utility? Change the category to Marketing.
6. **Content too vague** — Does the template have a clear, specific purpose? Add more fixed text and context.
7. **Variable placement** — Are variables at the start/end of the body, or stacked together (###{{1}}###{{2}})? Restructure the text.

💡 **Tip:** Edit and resubmit rejected templates — there is no limit on edits. Do not delete and recreate, as the template name cannot be reused for 30 days.

## Template stuck in PENDING status

Meta's review typically takes 24–48 hours. Authentication templates are usually auto-approved within minutes.

If a template has been pending for more than 48 hours:

* Check the template status in **Meta Business Manager** directly — the status there is authoritative
* The template may have been approved or rejected on Meta's side but the status hasn't synced. Check in Meta Business Manager → WhatsApp Accounts → your WABA → Message Templates
* If pending for more than 7 days, delete and resubmit with improved content

## Template category was changed by Meta

Since April 2025, Meta auto-reclassifies templates that don't match their category. The most common change is Utility → Marketing, which affects per-conversation pricing. If a template contains promotional language (discounts, offers, sales, promo codes), submit it as Marketing from the start.

# Message Delivery Issues

## Error code 40008

Error `40008` indicates the template could not be used for sending. This is a general template error — possible causes include:

* **Template still pending review** — Check template status; it may not be approved yet
* **Template was rejected** — Review and fix the template, then resubmit
* **Template was paused** — Meta paused it due to low quality rating. Wait for the pause to lift or edit the template.
* **Template was disabled** — The template was permanently disabled due to repeated quality issues. Create a new template.
* **Template name or language mismatch** — Verify the template name and language code in the send request match exactly what was submitted

## Error code 40008

Error code `40008` is the general WhatsApp error code. The response body contains the specific Meta API error. Common causes:

* **24-hour window expired** — Use a template message to re-initiate the conversation
* **Invalid recipient** — Number doesn't have WhatsApp or has blocked your business
* **Rate limit exceeded** — You've hit your messaging limit tier
* **Phone number not registered** — Ensure your sender number is verified and registered with your WABA

## Free-form messages fail (text, media, interactive)

Non-template messages (text, media, interactive, location) can only be sent within the 24-hour conversation window. The window opens when:

* The recipient sends a message to your business number, OR
* You send a template message and the recipient replies

Outside this window, only approved template messages can be sent.

## Message sent but not delivered

* Recipient may be offline — WhatsApp will retry delivery
* Recipient may have blocked your number
* Recipient's phone may have no storage space
* Check the delivery status webhook for specific error details

## Message sent but not showing as "read"

Read receipts are only sent if the recipient has read receipts enabled in their WhatsApp settings. Many users disable this. A message can be delivered and read without you receiving a "read" status.

# Quality Rating Issues

## Quality rating dropped to Yellow or Red

* Customers are reporting or blocking your messages
* Review your message content — is it relevant to recipients?
* Ensure you have proper opt-in before messaging customers
* Reduce message frequency if you're sending too often
* Improve template content quality and targeting

## Messaging limit reduced

If your quality rating drops to Red, Meta may reduce your messaging limit tier. To recover, improve your quality rating by reducing blocks and reports, then your tier will gradually increase again.

## Template paused by Meta

Meta automatically pauses templates with high complaint rates. Pause durations escalate:

* **First pause:** 3 hours
* **Second pause:** 6 hours
* **Third pause:** Permanently disabled

During a pause, edit the template content to improve relevance and reduce complaints. Changes take effect within 2 minutes, allowing immediate reuse without waiting for the pause period to end.

# Need More Help?

If you're experiencing an issue not covered here, contact [Telnyx Support](https://support.telnyx.com) with:

* Your WABA ID
* Phone number
* Message ID or template name (if applicable)
* Error code and full error response
* Description of the problem

---

Related Articles

[What is WhatsApp Business Platform?](https://support.telnyx.com/en/articles/13986480-what-is-whatsapp-business-platform)[WhatsApp Message Templates Guide](https://support.telnyx.com/en/articles/13986483-whatsapp-message-templates-guide)[How to Set Up WhatsApp on Telnyx](https://support.telnyx.com/en/articles/13986485-how-to-set-up-whatsapp-on-telnyx)[How to Create WhatsApp Message Templates](https://support.telnyx.com/en/articles/13986486-how-to-create-whatsapp-message-templates)[WhatsApp FAQ](https://support.telnyx.com/en/articles/13986488-whatsapp-faq)

Did this answer your question?

😞😐😃

Table of contents
