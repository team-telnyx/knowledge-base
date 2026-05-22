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

*Part 2 of 2 — see also: [Part 1](telnyx-sms-mms-mdrs-deliverability-throughput-apis-and-tools--part-1.md)*

A practical guide to running SMS/MMS on Telnyx: where to find message logs and analytics, how statuses, encoding and parts affect billing, best practices for long-code deliverability, MMS capabilities and limits, receiving via webhooks, high‑throughput SMPP, automation options, compliance considerations (10DLC/P2P), and key error codes for troubleshooting.

## Compliance, 10DLC, Toll‑Free, and P2P Exemption

- 10DLC: For A2P traffic on US long codes, register your brand/campaigns. Unregistered A2P traffic may be filtered or blocked; errors like “Unregistered 10DLC Message” can occur.
- Toll‑Free: Many carriers require toll‑free messaging verification for higher trust and deliverability. Ensure your toll‑free number is registered/verified; unverified sends may be blocked.
- STOP/Opt‑out: Carriers enforce opt‑out handling. Telnyx blocks sending to numbers that issued STOP/variants (CANCEL, END, QUIT, STOP, UNSUBSCRIBE).
- P2P Exemption: For true non‑commercial, person‑to‑person, human‑to‑human texting (roughly symmetrical traffic, no automation), you may apply for a P2P exemption from 10DLC. Requires review by carriers and typically a Telnyx commercial agreement (e.g., ≥$1,000/month, 12‑month term). Approval can take months.

## Troubleshooting and Common Error Codes

- Categories:
  - 1XXXX Invalid Request (formatting/auth issues). Examples: 10003 Invalid URL, 10011 Too many requests, 10016 E.164 required.
  - 2XXXX Account Level (status/permissions). Examples: 20002 API key revoked, 20100 Insufficient funds, 20014/20016 account verification required.
  - 4XXXX Delivery (carrier/route/content). Examples:
    - 40001 Not routable (landline/no messaging capability).
    - 40002/40003 Blocked as spam (temporary/permanent). Review opt‑ins, content, and send patterns.
    - 40010 Unregistered 10DLC Message.
    - 40100 Number not messaging enabled (assign a Messaging Profile).
    - 40151 Message enablement pending with other provider.
    - 40300 Blocked due to STOP message (respect opt‑outs).
    - 40302/40328 Message too large (consider MMS or shorten content).
    - 40305 Invalid from address (ensure the number is on the profile and healthy; pooling may skip unhealthy numbers).
    - 40308 Invalid from for MMS (ensure MMS capability).
    - 40317 Invalid MMS content (≤10 media URLs, total size < ~1 MB).
    - 40318 Message queue full (throttle per throughput guidance).
    - 40329 Toll‑free not yet verified.
- Important: Messages that leave the Telnyx network (fail downstream) are typically billable. Align use cases with best practices to reduce filtering.

## Practical Tips and Reminders

- Always use E.164 formatting for phone numbers.
- Prefer GSM‑7 characters to maximize characters per part; non‑GSM characters trigger UTF‑16 and fewer characters per part.
- Multi‑part SMS increases costs and can impact deliverability; keep messages concise and URLs short.
- For MMS, pre‑optimize media to fit carrier limits; enable transcoding as needed and consider fallback when recipients lack MMS support.
- Monitor number health and deliverability using Number Pooling features and the Deliverability Dashboard; rotate or replace unhealthy numbers.
- For integrations fetching your media, secure access and whitelist Telnyx media fetcher IPs if needed.
- For US A2P messaging, complete 10DLC registration and include opt‑out instructions to reduce filtering.
