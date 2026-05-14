---
title: Telnyx SMS Deliverability, Compliance, and Automation Guide
summary: Practical guidance to maximize SMS deliverability on Telnyx, manage opt-outs
  and keywords, understand SMPP for high throughput, automate forwarding with Telnyx
  Flow, and integrate the U.S. Reassigned Numbers Database (RND) into compliant outreach
  workflows.
sources:
- url: https://support.telnyx.com/en/articles/1130617-sms-long-code-deliverability-best-practices
  content_hash: 07b2856f2afa4a9adb59d1ce86c089d2e2d080a0155e87e4d4d020baf6a26075
- url: https://support.telnyx.com/en/articles/1270091-sms-opt-out-keywords-and-stop-words
  content_hash: f7af4f1a86f999ec2bd84d27e110c87e6ebecc7307ba3a19bf7df4924f090d0b
- url: https://support.telnyx.com/en/articles/1667062-short-message-peer-to-peer-set-up-guide
  content_hash: 63dfc4eac60ef67badda87e391bd9cad9b90c54fbd13b4407a3dd9dbf5365eeb
- url: https://support.telnyx.com/en/articles/10523949-forwarding-sms-mms-automation-using-telnyx-flow
  content_hash: 9769f6366b7f4f8f658664e205004ff416426e27e5d9909a60b3a2d16e5d353d
- url: https://support.telnyx.com/en/articles/11358700-what-is-the-u-s-reassigned-numbers-database
  content_hash: f2d110b06387427c51135fded834c0288430df2acacb87e186d124b5f1d94581
updated_at: 2026-05-14T11:24:14Z
---

# Telnyx SMS Deliverability, Compliance, and Automation Guide

Practical guidance to maximize SMS deliverability on Telnyx, manage opt-outs and keywords, understand SMPP for high throughput, automate forwarding with Telnyx Flow, and integrate the U.S. Reassigned Numbers Database (RND) into compliant outreach workflows.

## Use the Right Channel for Your Content

- Long codes are for person-to-person or application-to-person messaging where a human initiates and content is unique to the recipient (e.g., live agent chats, appointment reminders, on-demand notifications).
- If your content is broadly similar or promotional, register and use 10DLC, or consider short code for true marketing campaigns.

## Send-Rate and Numbering Practices

- Long code per-number guidance: mobile operators typically accept about 10 messages per minute per long code (≈1 every 6 seconds). Telnyx also enforces an account-level default of 1 message per second; exceeding limits may trigger throttling. Contact sales@telnyx.com to discuss higher limits.
- Toll-free per-number throughput: up to 1200 messages per minute.
- Avoid sending high volumes from consecutive numbers. Spam filters flag sequential ranges; prefer discontiguous numbers for scale.

## URL and Content Hygiene

- Keep URLs short to avoid multipart segmentation and spam flags.
- Choose trustworthy domains. Some shorteners are blocked: messages containing bitlylinks.com or bit.ly will be blocked automatically.
- Always include clear opt-out language, especially for unregistered A2P traffic; lacking it can cause carrier filtering even when delivery receipts appear successful.
- Follow Telnyx’s acceptable use policy: https://support.telnyx.com/en/articles/1310359-acceptable-use-policy-for-messaging

## Opt-Out, Opt-In, and Keyword Management

- Automatic opt-out handling: Telnyx recognizes the following English stop words when they are the only content of the message: stop, stopall, stop all, unsubscribe, cancel, end, quit. Upon detection, the sender is blocked from messaging that recipient going forward.
- Scope: Opt-outs apply at the messaging profile level by default. If one number on a profile triggers an opt-out from a consumer, all numbers on that profile are blocked from messaging that consumer. Different profiles are not affected.
- Opt-in (to resume messaging): the recipient must text start or unstop to the exact same number they opted out from. With number pools, use messaging detail records to identify the number that received the opt-out.
- Auto-responses (default):
  - “You have successfully been unsubscribed, you will not receive any more messages from this number. Reply START to re-subscribe.”
  - “You have successfully been re-subscribed to this number. Reply STOP to unsubscribe. Msg&Data Rates May Apply.”
- Customization: Per-profile custom block rules and auto-responses are available; contact sales@telnyx.com.
- Keyword Management portal: https://portal.telnyx.com/#/app/programmable-messaging/keywords-management
  - Add up to 20 custom keywords for opt-in/out and help, globally or per country/language, and define the associated auto-responses. Save changes before closing.
- Note: A “coming soon” API/portal capability will let you retrieve all phone numbers on your opt-out list.

## High-Throughput Messaging via SMPP

- SMPP is designed for high-throughput programmatic messaging and is available to contracted customers (minimum $5,000/month for 12 months). Coordinate with your account manager to enable SMPP.
- Credentials: Provide your Messaging Profile ID to receive a system_id and password.
- Connectivity: TLS required to the primary host smpp.telnyx.com on port 2775. A secondary host may be introduced; connect to both for resiliency (only one is guaranteed up at any time).
- Supported PDUs: bind_transmitter, bind_transceiver, bind_receiver, unbind, submit_sm, deliver_sm, enquire_link.
- Required bind parameters: system_id (Telnyx-provided), password (Telnyx-provided), host smpp.telnyx.com, port 2775, SSL/TLS yes, addr_ton=1 (International), addr_npi=1 (ISDN/E.163/E.164).
- Throughput still depends on sender type and carrier policy (e.g., long code ≈10 msg/min/number; toll-free up to 1200 msg/min/number). Adhere to carrier and Telnyx limits to avoid throttling.

## No-Code Forwarding of Inbound SMS/MMS with Telnyx Flow

- Prerequisites: messaging-enabled Telnyx number(s), assigned to a dedicated Messaging Profile; for U.S. A2P, ensure your number is on an approved 10DLC campaign.
- Steps:
  - Sign in at https://flow.telnyx.com (Mission Control credentials required) and create a workspace.
  - Create a new blank workflow.
  - Add nodes: Inbound Message (trigger) → Switch (route by `{{message.received.type}}` equals “SMS” or “MMS”) → Send Message (one for SMS; one for MMS).
  - Configure Send Message:
    - Type: SMS or MMS.
    - Messaging Profile ID: select the same profile as the inbound number if forwarding from that identity.
    - From/To: invert the inbound values so the Telnyx number sends to your mobile, or set a fixed From if preferred.
    - Text: compose the forwarded message; for MMS, also set Subject and Media URLs.
  - Save and test using the Run Workflow button on the Inbound Message node.

## U.S. Reassigned Numbers Database (RND) Compliance

- Purpose: The FCC-authorized RND (reassigned.us) lets you check if a number was permanently disconnected—and potentially reassigned—since the date you last had consent. Results are Yes (disconnected after your date), No (not disconnected; grants safe harbor), or No Data (no record; no safe harbor).
- Telnyx participation: As a voice service provider, Telnyx submits permanently disconnected U.S. numbers to the RND (typically monthly). Telnyx offers a 15-day window to reclaim a disconnected number before it’s reported in the next update.
- Who should use it: Any business placing outbound calls or texts to U.S. consumers based on prior consent (e.g., contact centers, sales/marketing platforms, debt collectors, auto-dialers) should integrate RND checks to comply with TCPA and FCC rules.
- How to register: Visit https://www.reassigned.us, review the Query section, and email support@reassigned.us to request access. Choose a prepaid subscription tier by query volume/term; pricing: https://reassigned.us/pricing. The database is administered by SomosGov.
- Compliance tips: If RND returns Yes, do not contact that number without new consent. If No, retain the query evidence for safe harbor. Skipping RND checks can lead to fines of $500–$1,500 per violating call/text.

## Quick Deliverability and Compliance Checklist

- Use appropriate sender: 10DLC or short code for campaigns; long code only for unique, human-initiated content.
- Respect rate limits: ~10 msg/min per long code; up to 1200 msg/min per toll-free; default 1 msg/sec account limit.
- Distribute volume across non-consecutive numbers; avoid sequential ranges.
- Keep URLs short; avoid risky domains (bitlylinks.com and bit.ly are blocked).
- Include explicit opt-out instructions in messages.
- Configure and test opt-out/opt-in keywords and auto-responses; manage custom keywords (max 20) in the portal.
- For U.S. outreach based on prior consent, run RND checks and retain results.
- For high throughput, consider SMPP (contract required) and still follow per-number carrier constraints.
