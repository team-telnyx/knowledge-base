---
title: 'Telnyx Messaging: Setup, Sending Options, and Integrations'
summary: 'A practical guide to get Telnyx messaging ready end‑to‑end: prepare your
  account, create and assign a Messaging Profile, test and send via the Portal, API,
  SDKs and no‑code tools, understand porting/hosted SMS nuances, and review key compliance
  and feature controls.'
sources:
- url: https://support.telnyx.com/en/articles/3562059-setting-up-a-messaging-profile
- url: https://support.telnyx.com/en/articles/3562061-send-a-text-with-the-telnyx-python-sdk
- url: https://support.telnyx.com/en/articles/3562066-receive-a-text-with-the-telnyx-python-sdk
- url: https://support.telnyx.com/en/articles/3685327-textable-setup-guide
- url: https://support.telnyx.com/en/articles/3723768-zapier-forward-texts-to-email
- url: https://support.telnyx.com/en/articles/4287554-sms-setup-with-postman
- url: https://support.telnyx.com/en/articles/7183887-sms-for-ported-in-phone-numbers
- url: https://support.telnyx.com/en/articles/8219294-messaging-in-mission-control
- url: https://support.telnyx.com/en/articles/8255134-group-messaging-bulk-sending-mms
- url: https://support.telnyx.com/en/articles/8268223-bulk-messaging-with-sheets
- url: https://support.telnyx.com/en/articles/5336668-hosted-sms-messaging-process
- url: https://support.telnyx.com/en/articles/9767793-sending-a-test-message-with-learn-and-build
- url: https://support.telnyx.com/en/articles/10523949-forwarding-sms-mms-automation-using-telnyx-flow
- url: https://support.telnyx.com/en/collections/133103-telnyx-sms-guide
updated_at: 2026-05-20T14:28:29Z
---

# Telnyx Messaging: Setup, Sending Options, and Integrations

*Part 2 of 2 — see also: [Part 1](telnyx-messaging-setup-sending-options-and-integrations--part-1.md)*

A practical guide to get Telnyx messaging ready end‑to‑end: prepare your account, create and assign a Messaging Profile, test and send via the Portal, API, SDKs and no‑code tools, understand porting/hosted SMS nuances, and review key compliance and feature controls.

## Hosted SMS (port messaging only)
- Host messaging with Telnyx while leaving voice with the current provider (US/CA locals and Toll‑Free). Requires Level 2 Verification.
- Submit an order in Mission Control (Messaging → Hosted Messaging), add up to 200 numbers, select your Messaging Profile, and upload a signed LOA (≤30 days old) plus a matching invoice. Processing typically within 24–48 business hours.
- Some providers (e.g., Bandwidth, Aerialink, Callfire) block messaging transfers and require manual release by the underlying provider/customer.
- Toll‑Free hosting is supported; expect at least 72 hours to gain messaging.
- Not supported when voice/messaging are with wireless providers (e.g., Google Voice), for international numbers, or for inter‑Telnyx account transfers.
- If you already have voice with Telnyx, simply assign a Messaging Profile—no hosted request needed. Full guide: https://support.telnyx.com/en/articles/5336668-hosted-sms-messaging-process

## Troubleshooting and next steps
- If a number shows Not SMS Capable, acquire a different number with SMS support.
- If assigning a profile fails (“Could not enable messaging on the number.”), wait and retry; NNID/central provisioning may still be updating.
- Review Telnyx Messaging Error Codes: https://support.telnyx.com/en/articles/6505121-telnyx-messaging-error-codes
- Country‑specific SMS guidelines: https://support.telnyx.com/en/collections/3731154-country-specific-sms-guidelines
- 10DLC and Toll‑Free compliance hub: https://support.telnyx.com/en/collections/3147004-10dlc-and-toll-free-text-messaging-compliance-guide
- SMS Guide (index to many messaging resources): https://support.telnyx.com/en/collections/133103-telnyx-sms-guide
- Scale considerations: obtain Level 2 Verification for higher default sending rates, enable Number Pooling, and use Allowed Destinations and Daily Spend Limits to manage risk.
