---
title: WhatsApp Business on Telnyx
summary: A comprehensive guide to using WhatsApp Business Platform on Telnyx, covering
  account setup via Embedded Signup, message types (template and free-form), the 24-hour
  conversation window, template creation and approval, per-message billing, WhatsApp
  Business Calling, troubleshooting, and frequently asked questions.
sources:
- url: https://support.telnyx.com/en/articles/13986480-what-is-whatsapp-business-platform
- url: https://support.telnyx.com/en/articles/13986481-whatsapp-message-types-explained
- url: https://support.telnyx.com/en/articles/13986482-whatsapp-24-hour-conversation-window
- url: https://support.telnyx.com/en/articles/13986483-whatsapp-message-templates-guide
- url: https://support.telnyx.com/en/articles/13986484-whatsapp-pricing-on-telnyx
- url: https://support.telnyx.com/en/articles/13986485-how-to-set-up-whatsapp-on-telnyx
- url: https://support.telnyx.com/en/articles/13986486-how-to-create-whatsapp-message-templates
- url: https://support.telnyx.com/en/articles/13986488-whatsapp-faq
- url: https://support.telnyx.com/en/articles/13986489-whatsapp-troubleshooting-guide
- url: https://support.telnyx.com/en/articles/14668631-enabling-whatsapp-business-calling-on-telnyx-numbers
- url: https://support.telnyx.com/en/collections/18868947-whatsapp-business
updated_at: 2026-07-17T09:09:49Z
---

# WhatsApp Business on Telnyx

*Part 2 of 7 — see also: [Part 1](whatsapp-business-on-telnyx--part-1.md), [Part 3](whatsapp-business-on-telnyx--part-3.md), [Part 4](whatsapp-business-on-telnyx--part-4.md), [Part 5](whatsapp-business-on-telnyx--part-5.md), [Part 6](whatsapp-business-on-telnyx--part-6.md), [Part 7](whatsapp-business-on-telnyx--part-7.md)*

A comprehensive guide to using WhatsApp Business Platform on Telnyx, covering account setup via Embedded Signup, message types (template and free-form), the 24-hour conversation window, template creation and approval, per-message billing, WhatsApp Business Calling, troubleshooting, and frequently asked questions.

## 24-Hour Conversation Window

WhatsApp uses a 24-hour conversation window to control when businesses can send free-form messages. The window opens when a customer messages you, and it lasts for 24 hours from the customer's last message.

### What Opens the Window

- A customer sends you a message (text, image, button reply, etc.)
- A customer taps a call-to-action button in a previous message
- A customer replies to a template message

Each new message from the customer resets the 24-hour timer.

### During the Window (Open)

While the window is open, you can send:

- Free-form messages (text, media, location, contacts, interactive)
- Template messages (these still work within the window)

Free-form messages within the window create Service conversations, which are typically the lowest-cost conversation category.

### After the Window Closes (Expired)

Once 24 hours have passed since the customer's last message:

- Free-form messages will fail
- You must use an approved template message to re-initiate contact
- The template message opens a new conversation (billed at the template's category rate)

### Tips

- **Respond promptly** — The 24-hour window starts from the customer's message, not your reply. Delays eat into your free-form messaging time.
- **Use templates strategically** — If you need to follow up after the window closes, have relevant templates pre-approved and ready.
- **Monitor via webhooks** — Use delivery status webhooks to track whether messages succeeded or failed due to window expiration.
