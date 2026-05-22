---
title: 'Telnyx Messaging: Setup, Sending Options, and Integrations'
summary: 'A practical guide to get Telnyx messaging ready end‑to‑end: prepare your
  account, create and assign a Messaging Profile, test and send via the Portal, API,
  SDKs and no‑code tools, understand porting/hosted SMS nuances, and review key compliance
  and feature controls.'
sources:
- url: https://support.telnyx.com/en/articles/3562059-setting-up-a-messaging-profile
  content_hash: aa34ff90f76a15ee7d2bf9af5180bf966364481c0a299655356bbb9d403c4bf3
- url: https://support.telnyx.com/en/articles/3562061-send-a-text-with-the-telnyx-python-sdk
  content_hash: 2f8418ab1159e3217d2cf5825a9b2bfe2f0d52942276a8bc19a9dcfbcbefe09f
- url: https://support.telnyx.com/en/articles/3562066-receive-a-text-with-the-telnyx-python-sdk
  content_hash: 00e98248fa9d6b2033e21916ed13907c44587f73fadcdd3e2105b5252a79cbed
- url: https://support.telnyx.com/en/articles/3685327-textable-setup-guide
  content_hash: be9ea16aa3592c7fe80c95d0197798698ee6b0bdfee29a186f5dc1c93f3d06bf
- url: https://support.telnyx.com/en/articles/3723768-zapier-forward-texts-to-email
  content_hash: 7ad9572a930d73ff6f3dbddab1b36e4155ae7327dc84fc3d8e0460cb2f5b6b96
- url: https://support.telnyx.com/en/articles/4287554-sms-setup-with-postman
  content_hash: 22cfd8f20e858a82a4ed5c8e3bb0c530391fc56c387439433ca9085d5672cd8f
- url: https://support.telnyx.com/en/articles/7183887-sms-for-ported-in-phone-numbers
  content_hash: 90ddeba650dcedf970a636ed3f72761d545049909ab66b77e2451cedfa4d70a1
- url: https://support.telnyx.com/en/articles/8219294-messaging-in-mission-control
  content_hash: e656a0304e86302b75eaa282824b9e5228425d0014923ab6bc949d058b5d20c1
- url: https://support.telnyx.com/en/articles/8255134-group-messaging-bulk-sending-mms
  content_hash: 62f4c57ce8f57d37bf054374b009d9af17a5571928f93124406909a2068989e8
- url: https://support.telnyx.com/en/articles/8268223-bulk-messaging-with-sheets
  content_hash: 7a0853f155d617c9da2a4baf20765126a5208ed52cbdf6f6ba01b10dc843867a
- url: https://support.telnyx.com/en/articles/5336668-hosted-sms-messaging-process
  content_hash: 7de41c4cff709c280eb160524c8299a8efbdbab5bc91bb4a0b270fb42cfbd65f
- url: https://support.telnyx.com/en/articles/9767793-sending-a-test-message-with-learn-and-build
  content_hash: da9316aca19025388915c0c695c93c6d08af42d3f1bc20f0d4e5b0dcbad1b1e7
- url: https://support.telnyx.com/en/articles/10523949-forwarding-sms-mms-automation-using-telnyx-flow
  content_hash: 9305c7d07dada70a40def46178ac551ae7d8f5886edfa1890b955cd680bb8282
- url: https://support.telnyx.com/en/collections/133103-telnyx-sms-guide
  content_hash: a45ce6e0d88c4ef16226913a8d21ec716b713173a849a20ad5c7e320ec6b9313
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
