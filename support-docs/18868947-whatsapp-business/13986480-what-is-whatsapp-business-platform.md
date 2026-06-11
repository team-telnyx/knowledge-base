---
source_url: https://support.telnyx.com/en/articles/13986480-what-is-whatsapp-business-platform
scraped: 2026-06-11
---

What is WhatsApp Business Platform? | Telnyx Help Center

[Skip to main content](#main-content)

# What is WhatsApp Business Platform?

Learn what WhatsApp Business Platform is and how Telnyx integrates with it as a Business Solution Provider.

Written by Telnyx Engineering

March 16, 2026

Table of contents

# Overview

WhatsApp Business Platform is Meta's API-based solution that lets businesses send and receive messages on WhatsApp at scale. Unlike the WhatsApp Business App (designed for small businesses), the Platform is built for programmatic integration — you connect via an API through a Business Solution Provider (BSP) like Telnyx.

# Key Components

## WhatsApp Business Account (WABA)

A WABA is the top-level container for your WhatsApp business presence. It holds your phone numbers, message templates, and business profile. Each WABA is linked to a Meta Business Manager account.

## Business Solution Provider (BSP)

Telnyx is an official Meta BSP. This means Telnyx provides the API infrastructure to send and receive WhatsApp messages, manage templates, and handle phone number registration — all through the Telnyx API and Portal.

## Meta Business Manager

Meta Business Manager is Meta's platform for managing business assets. You need a Meta Business Manager account to create a WABA and register phone numbers. During Telnyx's Embedded Signup flow, you'll connect your Meta Business Manager to authorize Telnyx as your BSP.

# How It Works on Telnyx

1. **Sign up** — Use the Embedded Signup flow in the Telnyx Portal to create your WABA and register a phone number
2. **Create templates** — Submit message templates for Meta's approval via the Telnyx API
3. **Send messages** — Use `POST /v2/messages/whatsapp` to send template or free-form messages
4. **Receive messages** — Configure webhooks to receive inbound messages and delivery status updates

# Conversation Types

WhatsApp uses a conversation-based billing model. There are four conversation categories:

* **Marketing** — Promotions, offers, informational updates, invitations to respond
* **Utility** — Transaction updates, order confirmations, shipping notifications, account alerts
* **Authentication** — One-time passwords (OTP) and verification codes
* **Service** — Customer-initiated conversations where you respond within a 24-hour window

Marketing, Utility, and Authentication conversations require pre-approved message templates. Service conversations allow free-form messages when the customer messages you first.

# Related Resources

* [WhatsApp Quickstart Guide](https://developers.telnyx.com/docs/messaging/whatsapp/quickstart)
* [Embedded Signup Guide](https://developers.telnyx.com/docs/messaging/whatsapp/embedded-signup)
* [Send WhatsApp Messages](https://developers.telnyx.com/docs/messaging/whatsapp/send-messages)

---

Related Articles

[WhatsApp Pricing on Telnyx](https://support.telnyx.com/en/articles/13986484-whatsapp-pricing-on-telnyx)[How to Set Up WhatsApp on Telnyx](https://support.telnyx.com/en/articles/13986485-how-to-set-up-whatsapp-on-telnyx)[WhatsApp FAQ](https://support.telnyx.com/en/articles/13986488-whatsapp-faq)[WhatsApp Troubleshooting Guide](https://support.telnyx.com/en/articles/13986489-whatsapp-troubleshooting-guide)[Enabling WhatsApp Business Calling on Telnyx Numbers](https://support.telnyx.com/en/articles/14668631-enabling-whatsapp-business-calling-on-telnyx-numbers)

Did this answer your question?

😞😐😃

Table of contents
