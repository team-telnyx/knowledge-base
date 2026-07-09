---
source_url: https://support.telnyx.com/en/articles/13986482-whatsapp-24-hour-conversation-window
scraped: 2026-07-08
content_hash: 2fe960b316229561d9e5c4d5e72ed3e97453f4146e10647d69e5a910dd51a413
---

WhatsApp 24-Hour Conversation Window | Telnyx Help Center

[Skip to main content](#main-content)

# WhatsApp 24-Hour Conversation Window

How the WhatsApp 24-hour conversation window works, what opens it, and what happens when it expires.

Written by Telnyx Engineering

March 16, 2026

Table of contents

# How the Conversation Window Works

WhatsApp uses a 24-hour conversation window to control when businesses can send free-form messages. The window opens when a customer messages you, and it lasts for 24 hours from the customer's last message.

## What Opens the Window

* A customer sends you a message (text, image, button reply, etc.)
* A customer taps a call-to-action button in a previous message
* A customer replies to a template message

Each new message from the customer resets the 24-hour timer.

## During the Window (Open)

While the window is open, you can send:

* Free-form messages (text, media, location, contacts, interactive)
* Template messages (these still work within the window)

Free-form messages within the window create **Service** conversations, which are typically the lowest-cost conversation category.

## After the Window Closes (Expired)

Once 24 hours have passed since the customer's last message:

* Free-form messages will **fail**
* You must use an approved **template message** to re-initiate contact
* The template message opens a new conversation (billed at the template's category rate)

# Conversation Billing

Each conversation is billed once when it opens. The conversation type determines the rate:

|  |  |  |
| --- | --- | --- |
| Conversation Type | How It Opens | Duration |
| **Service** | Customer messages you, you reply with free-form | 24 hours from window open |
| **Marketing** | You send a Marketing template | 24 hours from template send |
| **Utility** | You send a Utility template | 24 hours from template send |
| **Authentication** | You send an Authentication template | 24 hours from template send |

# Tips

* **Respond promptly** — The 24-hour window starts from the customer's message, not your reply. Delays eat into your free-form messaging time.
* **Use templates strategically** — If you need to follow up after the window closes, have relevant templates pre-approved and ready.
* **Monitor via webhooks** — Use delivery status webhooks to track whether messages succeeded or failed due to window expiration.

---

Related Articles

[What is WhatsApp Business Platform?](https://support.telnyx.com/en/articles/13986480-what-is-whatsapp-business-platform)[WhatsApp Message Types Explained](https://support.telnyx.com/en/articles/13986481-whatsapp-message-types-explained)[WhatsApp Pricing on Telnyx](https://support.telnyx.com/en/articles/13986484-whatsapp-pricing-on-telnyx)[WhatsApp FAQ](https://support.telnyx.com/en/articles/13986488-whatsapp-faq)[WhatsApp Troubleshooting Guide](https://support.telnyx.com/en/articles/13986489-whatsapp-troubleshooting-guide)

Did this answer your question?

😞😐😃

Table of contents
