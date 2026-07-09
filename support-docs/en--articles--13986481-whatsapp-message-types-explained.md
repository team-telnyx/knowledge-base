---
source_url: https://support.telnyx.com/en/articles/13986481-whatsapp-message-types-explained
scraped: 2026-07-08
content_hash: b84d28529808c576a61aeada7084c8b65d5f9d1d15a70b1c8d12042e741b10f8
---

WhatsApp Message Types Explained | Telnyx Help Center

[Skip to main content](#main-content)

# WhatsApp Message Types Explained

Understand the difference between template messages and free-form messages, and when to use each conversation type.

Written by Telnyx Engineering

March 16, 2026

Table of contents

# Two Categories of Messages

WhatsApp messages fall into two categories based on how conversations are initiated:

## Template Messages (Business-Initiated)

Template messages are pre-approved message formats that you submit to Meta for review. They are **required** to start a new conversation with a customer or to message a customer outside the 24-hour conversation window.

Templates have three categories, each with different billing rates:

|  |  |  |
| --- | --- | --- |
| Category | Use Cases | Examples |
| **Marketing** | Promotions, offers, updates | "Hi ##{{1}}, our spring sale starts tomorrow! Get 20% off with code SPRING20." |
| **Utility** | Transaction updates, alerts | "Your order ##{{1}} has shipped. Track it here: ##{{2}}" |
| **Authentication** | OTP, verification codes | "Your verification code is ##{{1}}. It expires in 10 minutes." |

Templates support variable substitution using `##{{1}}`, `##{{2}}`, etc. They can include headers (text, image, video, or document), body text, footers, and buttons (quick reply or call-to-action).

## Free-form Messages (Session Messages)

Free-form messages can be sent **only within a 24-hour window** after the customer last messaged you. These create "Service" conversations and support rich content types:

* **Text** — Plain text up to 4,096 characters
* **Image** — JPEG, PNG (with optional caption up to 1,024 characters)
* **Video** — MP4 (with optional caption)
* **Document** — PDF, DOC, etc. (with optional caption and filename)
* **Audio** — OGG, MP3, etc.
* **Sticker** — WebP format
* **Location** — GPS coordinates with name and address
* **Contacts** — Contact cards (1–257 per message)
* **Interactive** — Quick reply buttons, CTA URL buttons, list messages

# When to Use Which

|  |  |
| --- | --- |
| Scenario | Message Type |
| Customer hasn't messaged you yet | Template (required) |
| 24-hour window has expired | Template (required) |
| Customer messaged within last 24 hours | Free-form or Template (your choice) |
| Sending OTP or verification code | Authentication Template |
| Sending order update or receipt | Utility Template |
| Sending promotion or offer | Marketing Template |
| Responding to a customer's question | Free-form (within 24hr window) |

---

Related Articles

[WhatsApp Message Templates Guide](https://support.telnyx.com/en/articles/13986483-whatsapp-message-templates-guide)[WhatsApp Pricing on Telnyx](https://support.telnyx.com/en/articles/13986484-whatsapp-pricing-on-telnyx)[How to Create WhatsApp Message Templates](https://support.telnyx.com/en/articles/13986486-how-to-create-whatsapp-message-templates)[WhatsApp FAQ](https://support.telnyx.com/en/articles/13986488-whatsapp-faq)[WhatsApp Troubleshooting Guide](https://support.telnyx.com/en/articles/13986489-whatsapp-troubleshooting-guide)

Did this answer your question?

😞😐😃

Table of contents
