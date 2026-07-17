---
title: Telnyx Voice, Messaging, and Billing Reference
summary: This page consolidates Telnyx documentation covering VoIP and telecommunications
  protocols (RTP, UDP, TCP, SIP, SDP), audio codecs and SDP parameters, external call
  transfers, webhooks (including WhatsApp webhooks and signing key rotation), A2P
  vs P2P traffic types and the P2P exemption process, toll-free opt-in workflow templates,
  and payment methods including ACH Direct Debit and Bitcoin.
sources:
- url: https://support.telnyx.com/en/articles/1130723-voip-telecommunications-protocols
- url: https://support.telnyx.com/en/articles/11898569-toll-free-opt-in-workflow-description
- url: https://support.telnyx.com/en/articles/13117410-how-external-call-transfers-work
- url: https://support.telnyx.com/en/articles/13986487-how-to-configure-whatsapp-webhooks
- url: https://support.telnyx.com/en/articles/3192298-audio-and-codecs
- url: https://support.telnyx.com/en/articles/3199007-guide-to-using-our-traffic-type-feature
- url: https://support.telnyx.com/en/articles/4334722-how-to-leverage-webhooks
- url: https://support.telnyx.com/en/articles/7045419-ach-direct-debit-payment-method
- url: https://support.telnyx.com/en/articles/8370064-update-webhook-sign-key-guide
- url: https://support.telnyx.com/en/articles/8379618-bitcoin-payment-method
- url: https://support.telnyx.com/en/articles/8685561-p2p-definition-and-exemption-process
updated_at: 2026-07-17T09:07:29Z
---

# Telnyx Voice, Messaging, and Billing Reference

*Part 6 of 8 — see also: [Part 1](telnyx-voice-messaging-and-billing-reference--part-1.md), [Part 2](telnyx-voice-messaging-and-billing-reference--part-2.md), [Part 3](telnyx-voice-messaging-and-billing-reference--part-3.md), [Part 4](telnyx-voice-messaging-and-billing-reference--part-4.md), [Part 5](telnyx-voice-messaging-and-billing-reference--part-5.md), [Part 7](telnyx-voice-messaging-and-billing-reference--part-7.md), [Part 8](telnyx-voice-messaging-and-billing-reference--part-8.md)*

This page consolidates Telnyx documentation covering VoIP and telecommunications protocols (RTP, UDP, TCP, SIP, SDP), audio codecs and SDP parameters, external call transfers, webhooks (including WhatsApp webhooks and signing key rotation), A2P vs P2P traffic types and the P2P exemption process, toll-free opt-in workflow templates, and payment methods including ACH Direct Debit and Bitcoin.

## P2P Definition and Exemption Process

P2P (Person-to-Person) SMS traffic refers to the exchange of text messages between individuals, typically using mobile devices. This is the traditional and most common use of SMS, where one person sends a text message to another person's mobile phone number.

Characteristics of P2P SMS traffic:

1. **Individual Use** — Messages are sent from one individual to another, rather than from a business or application to an individual.
2. **Two-Way Communication** — P2P SMS allows for a conversation-like flow, with both parties able to send and receive messages.
3. **Phone Numbers** — P2P SMS uses regular mobile phone numbers, rather than short codes or alphanumeric sender IDs often used in A2P messaging.
4. **Non-Commercial** — These messages must be non-commercial in nature, meaning they are not used for marketing, notifications, automated alerts, or anything related to business or on behalf of a business.
5. **Standard SMS Rates** — P2P SMS traffic typically incurs standard messaging fees from mobile carriers, unlike A2P messages that might have different pricing models and often involve bulk messaging services.
6. **Regulatory Compliance** — P2P SMS is subject to different regulations than A2P SMS. Carriers often have more stringent rules regarding A2P to prevent spam, while P2P is treated more leniently as it is considered personal communication.

The distinction between P2P and A2P SMS traffic is important for telecom operators, as they may have different infrastructure and billing models for each type of traffic. If your P2P exemption is approved, there is no requirement to register with The Campaign Registry for campaigns.

### P2P Exemption Questionnaire

To qualify for P2P exemption from 10DLC requirements, walk through the following questionnaire:

1. Does your messaging exclude business communication of any kind? If yes, continue.
2. Are you not a Cloud Communication Suite? If yes, continue.
3. Will traffic be roughly symmetrical (User to User, 1:1 - 1:3)? If yes, continue.
4. Are there no automated text messages in your workflow? If yes, continue.
5. Do you have a Telnyx contract? If yes, continue.

If you fit the above criteria and would like to apply, reach out to your Customer Success Manager to proceed.

If you fit the above criteria except that you need a Telnyx contract:

1. If you do not have an agreement in place, contact [sales@telnyx.com](mailto:sales@telnyx.com) to discuss commercial agreement and the P2P exemption requirements.
2. For context, commercial agreements start at $1,000 per month in spend with Telnyx — that is, you would need to be willing to commit to spending at least $1,000 per month or more for at least 12 months.

There are strict requirements from the mobile operators in order to qualify for P2P Exemption and the process for approval can take up to several months. Review the up-to-date TCR P2P requirements prior to applying.

## Toll-Free Opt-In Workflow

The Toll-Free Opt-In Workflow Description should follow one of four templates: Digital, Verbal, Paper, or Inbound Message. Choose one of those four opt-in methods and follow its corresponding template below. Replace any bracketed variable like `[variable]` with the actual value — for example, `[URL]` becomes `https://www.example.com/opt-in`.

Anywhere it says to share a hosted URL, upload your screenshot to a hosting service like Dropbox or Imgur and use the link to the screenshot in the URL field. Make sure the link is publicly accessible or it will fail review.

### Digital Opt-In

If the opt-in form is publicly available on the Internet:

> "Subscribers opt in digitally, they start at [URL] and navigate to [URL] where the opt in form is located."

If you must sign in to see the opt-in form, add a public link to a hosted screenshot:

> "Subscribers opt in digitally, they sign in at [URL] and navigate to where the opt in form is located in the system, Here is a screenshot of the opt in form: [URL]."

### Verbal Opt-In

For the location variable, use a Web or social media URL, or a hosted screenshot of a Google/Bing search, advertisement, email signature, business card, flyer, poster, etc.

> "Subscribers [call/visit] the [actual phone number/actual address] which is published at [location]. If they request to receive sms then we read a script. Please see the Opt in Image URL for the full script."

### Paper Opt-In

A paper opt-in can be something like a contract, onboarding document, or other paper form where you gather SMS opt-in. Upload a copy of the related section of the paper form and host it somewhere like Dropbox, then share the link to the screenshot as the URL. Make sure the link is publicly accessible or it will fail review.

> "Subscribers opt in via paper form. Please see screenshot of paper form at [URL]."

### Inbound Message Opt-In

An inbound message means that you do not initiate conversations with subscribers with an outbound text message. Instead, all of your messages are sent in response to a text that was sent to you. For the location variable, use a Web or social media URL, or a hosted screenshot of a Google/Bing search, advertisement, email signature, business card, flyer, poster, etc.

> "Subscribers opt in by sending us the first text message. They find the number to text us at [location]."
