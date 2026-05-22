---
title: 'Telnyx SMS/MMS: MDRs, Deliverability, Throughput, APIs, and Tools'
summary: 'A practical guide to running SMS/MMS on Telnyx: where to find message logs
  and analytics, how statuses, encoding and parts affect billing, best practices for
  long-code deliverability, MMS capabilities and limits, receiving via webhooks, high‑throughput
  SMPP, automation options, compliance considerations (10DLC/P2P), and key error codes
  for troubleshooting.'
sources:
- url: https://support.telnyx.com/en/articles/1130611-understand-telnyx-sms-mdr-report-log
- url: https://support.telnyx.com/en/articles/1130617-sms-long-code-deliverability-best-practices
- url: https://support.telnyx.com/en/articles/1667062-short-message-peer-to-peer-set-up-guide
- url: https://support.telnyx.com/en/articles/3102823-mms-sending-and-receiving
- url: https://support.telnyx.com/en/articles/3154822-number-pooling
- url: https://support.telnyx.com/en/articles/3231942-forwarding-sms-to-your-mobile-number
- url: https://support.telnyx.com/en/articles/3232529-automated-replies-for-messages-using-zapier
- url: https://support.telnyx.com/en/articles/4348981-receiving-sms-on-your-telnyx-number
- url: https://support.telnyx.com/en/articles/4450150-faqs-about-mms-at-telnyx
- url: https://support.telnyx.com/en/articles/6505121-telnyx-messaging-error-codes
- url: https://support.telnyx.com/en/articles/6969802-message-deliverability-dashboard
- url: https://support.telnyx.com/en/articles/6986625-easy-text-marketing-and-telnyx-integration
- url: https://support.telnyx.com/en/articles/8685561-p2p-definition-and-exemption-process
updated_at: 2026-05-20T14:24:46Z
---

# Telnyx SMS/MMS: MDRs, Deliverability, Throughput, APIs, and Tools

*Part 1 of 2 — see also: [Part 2](telnyx-sms-mms-mdrs-deliverability-throughput-apis-and-tools--part-2.md)*

A practical guide to running SMS/MMS on Telnyx: where to find message logs and analytics, how statuses, encoding and parts affect billing, best practices for long-code deliverability, MMS capabilities and limits, receiving via webhooks, high‑throughput SMPP, automation options, compliance considerations (10DLC/P2P), and key error codes for troubleshooting.

## Accessing Message Detail Records (MDRs)

- Location: Mission Control Portal > Reports > Reporting. Generate per-message MDRs for all sent and received messages.
- Format: MDRs are JSON objects with key fields such as id, direction (inbound/outbound), to, from, messaging_profile_id, status, delivery_status, parts, rate, cost, and an embedded body object (e.g., text, text_hash, media_urls, media_hash).
- Privacy: Message body text is retained up to 10 days; afterward, use hash fields to identify messages.
- Status: Outbound and inbound messages move through distinct status values; delivery_status adds detail about confirmation (outbound) or delivery attempt (inbound).
- Encoding (coding): Chosen based on characters. GSM 7-bit when possible; otherwise UTF‑16.
- Parts and billing: Long messages are segmented by encoding. Outbound messages have a maximum of 10 parts. Billing is based on parts: cost = rate × parts. Rate limiting and billing apply per part.

## Throughput, Rate Limits, and Number Pooling

- Typical long code guidance: Mobile operators commonly accept about 10 messages per minute per long code. Some locales/carriers enforce lower caps; Telnyx documentation notes scenarios with 6 SMS/min/number. Plan conservatively and test.
- Telnyx account defaults: Overall account limit commonly starts at 1 message/second for SMS and 1 MMS/second; contact sales to raise. MMS may also be subject to account‑wide limits (e.g., 15 messages/second mentioned in MMS FAQs).
- Toll‑Free throughput: Up to 1200 messages per number per minute (other account‑wide limits can still apply).
- Number Pooling: Enable on a messaging profile to spread traffic across assigned numbers and maintain number health.
  - Weights: Bias selection between toll‑free and long codes by ratio.
  - Skip Unhealthy Numbers: Auto‑removes numbers with poor health (e.g., deliverability below ~25% or spam detection above ~75%).
  - Sticky Sender: Reuse the same originating number per destination when possible.
  - Geomatch: Prefer a local area code match (US area codes only) when available.

## Long‑Code Deliverability Best Practices

- Use long codes for unique, conversational or recipient‑specific messages (P2P or human‑initiated A2P). Use short code or registered 10DLC for marketing/bulk.
- Respect send rate: Keep within human‑like pacing and carrier caps; Telnyx will throttle if you exceed configured limits.
- Avoid consecutive number blocks: Use discontiguous numbers to reduce spam‑filter suspicion.
- Limit URLs: Long URLs increase parts and spam risk. Some domains are blocked (e.g., bitlylinks.com, bit.ly). Choose reputable domains.
- Include opt‑out language: Especially for unregistered A2P traffic; lack of opt‑out often leads to filtering. Honor STOP and related keywords.
- Follow acceptable use policies and complete 10DLC registration where applicable.

## Sending and Receiving MMS

- Quick starts: See developer docs for sending and receiving with API v1/v2.
- Supported content types include: text/plain, text/vcard, image/jpeg, image/png, image/gif, video/3gpp, video/mp4.
- Size limits (vary by destination carrier):
  - Tier 1 (Verizon, T‑Mobile, AT&T, Sprint): up to 1 MB (best practice: ≤ ~900 KB to allow overhead).
  - Tier 2: up to 600 KB; Tier 3: up to 300 KB.
  - Total media_urls per message: up to 10; total message size capped at ~1 MB.
- MMS scope and throughput: MMS currently supported within USA and Canada. Default account limit is often 1 MMS/second (contact sales to increase). Toll‑free can send MMS; short‑code MMS depends on carrier provisioning and campaign approval.
- DLRs: Expect internal “sent”, MM4_forward.RES (“delivered” to destination carrier), and sometimes MM4_delivery_report.REQ (handset outcome).
- Fallback (MMS → SMS) and Transcoding:
  - MMS fallback can auto‑convert MMS to SMS when the destination doesn’t support MMS; webhooks indicate which protocol was sent. SMS will include original media URLs on new lines.
  - MMS transcoding can resize images/videos to fit destination size limits (animated GIFs not resized; must be small enough). Images become JPEG; videos become H.264 MP4; quality may be reduced.
- Security and caching: Outbound media may be cached by Telnyx for ~1 hour; changing media URLs (e.g., query params) invalidates cache. To restrict access to your media, you can whitelist Telnyx fetcher IPs (e.g., 192.76.120.192/193).
- Long text as MMS: You can send long text as MMS (no attachments) by setting the message type to MMS.
- Inbound detection: Your webhook should distinguish MMS vs SMS; MMS requests typically use Content‑Type: multipart/form-data.

## Receiving Messages via Webhooks

- There is no inbox in the Portal for reading messages. To receive SMS/MMS, attach a webhook to the Messaging Profile assigned to your number (Portal > Messaging > Programmable Messaging > select profile > Inbound).
- Test with a temporary endpoint (e.g., webhook.site) to observe payloads. Ensure numbers are in E.164 format and profiles are correctly assigned.

## High‑Throughput SMPP

- Fit: Best for customers needing high throughput; available to contracted customers (e.g., $5,000/month minimum, 12‑month term). Coordinate with your Telnyx account team.
- Connectivity: smpp.telnyx.com:2775 over TLS. Supported PDUs: bind_transmitter, bind_transceiver, bind_receiver, unbind, submit_sm, deliver_sm, enquire_link.
- Required parameters: system_id and password (provided by Telnyx), addr_ton=1 (International), addr_npi=1 (ISDN/E.164).
- Throughput per number varies by type (e.g., long code about 10 mpm/number; toll‑free far higher). Plan capacity accordingly and use pooling where appropriate.

## Dashboards and Reporting

- Message Deliverability Dashboard: Portal > Reports > Reporting > Messaging Deliverability. View real‑time deliverability by Messaging Profile, including Delivered, Not Delivered, Parts, and In‑Flight counts.
- Filters: Direction (Outbound), Type (All/SMS/MMS), Product (All/Toll‑Free/Short Code/Long Code/Alphanumeric), and time range. Note the dashboard operates in UTC, which may differ from other reports.

## Automation with Zapier

- Forward inbound SMS to your mobile:
  - Trigger: Telnyx “Receive a Message”. Action: Telnyx “Send SMS”. Use your Telnyx number as Source and your mobile as Destination. Message example: "FWD FROM: {{From Phone Number}} BODY: {{Text}}".
  - Use a dedicated Messaging Profile with a single number to avoid unintended triggers.
- Automated replies:
  - Trigger: “Receive a Message”. Action: “Send SMS” back to the original sender (Destination = From Phone Number). Include your auto‑reply text.
  - For US long codes, ensure your number is tied to a registered 10DLC campaign to avoid filtering.
- Best practices: Always use E.164 formatting, monitor Zapier task history, and test before publishing.

## Easy Text Marketing (BYOC) Integration

- Steps overview: Create a Telnyx account, add funds (prepaid), copy your API v2 key, configure Easy Text Marketing to use Telnyx as the SMS gateway, “Get a Number” in their dashboard (auto‑creates a Messaging Profile), then assign that profile to your number in the Telnyx Portal.
- For managed accounts/sub‑accounts or assistance, reach out to the listed contacts in the integration guide.
