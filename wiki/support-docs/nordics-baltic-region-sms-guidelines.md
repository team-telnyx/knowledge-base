---
title: Nordics & Baltic Region SMS Guidelines
summary: Carrier policies for SMS in Denmark, Sweden, Norway, Finland, Iceland, Estonia,
  Latvia, Lithuania, the Faroe Islands, and Greenland. Includes MCC/dial codes, Sender
  ID rules, URL filtering/whitelisting, and content restrictions so you can prepare
  compliant traffic across the region.
sources:
- url: https://support.telnyx.com/en/articles/6560665-denmark-sms-guidelines
- url: https://support.telnyx.com/en/articles/6560689-sweden-sms-guidelines
- url: https://support.telnyx.com/en/articles/6560704-norway-sms-guidelines
- url: https://support.telnyx.com/en/articles/6560706-finland-sms-guidelines
- url: https://support.telnyx.com/en/articles/6560909-iceland-sms-guidelines
- url: https://support.telnyx.com/en/articles/6560919-estonia-sms-guidelines
- url: https://support.telnyx.com/en/articles/6560973-lithuania-sms-guidelines
- url: https://support.telnyx.com/en/articles/6561115-latvia-sms-guidelines
- url: https://support.telnyx.com/en/articles/6670775-faroe-islands-sms-guidelines
- url: https://support.telnyx.com/en/articles/6670885-greenland-sms-guidelines
updated_at: 2026-05-21T08:13:51Z
---

# Nordics & Baltic Region SMS Guidelines

Carrier policies for SMS in Denmark, Sweden, Norway, Finland, Iceland, Estonia, Latvia, Lithuania, the Faroe Islands, and Greenland. Includes MCC/dial codes, Sender ID rules, URL filtering/whitelisting, and content restrictions so you can prepare compliant traffic across the region.

## Overview and common rules
- Alphanumeric Sender IDs: Generally supported without registration across the region, except Norway (registration required) and Finland (registration will be required starting May 4, 2026 under regulation M28L).
- URL filtering: Operators in Denmark, Sweden, Norway, Finland, and Iceland filter messages containing URLs. Valid URLs can be whitelisted to improve deliverability — contact alpha_sender_id@telnyx.com.
- Content restrictions: Lottery and gambling traffic is blocked in Denmark, Sweden, Norway, Finland, and Iceland. Estonia, Latvia, Lithuania, Faroe Islands, and Greenland report no specific content restrictions via local operators; nonetheless, all messaging must comply with Telnyx’s Acceptable Use Policy.
- Always review the Telnyx Acceptable Use Policy for Messaging: https://support.telnyx.com/en/articles/1310359-acceptable-use-policy-for-messaging

## Denmark
- MCC: 238; Dial code: +45
- Sender ID: Alphanumeric supported; no registration required.
- URLs: Filtered; valid URLs can be whitelisted (alpha_sender_id@telnyx.com).
- Content: Lottery/gambling not allowed.

## Sweden
- MCC: 240; Dial code: +46
- Sender ID: Alphanumeric supported; no registration required.
- URLs: Filtered; valid URLs can be whitelisted (alpha_sender_id@telnyx.com).
- Content: Lottery/gambling not allowed.

## Norway
- MCC: 242; Dial code: +47
- Sender ID: Registration required; messages from unregistered alphanumeric Sender IDs are rejected.
- URLs: Filtered; valid URLs can be whitelisted.
- Content: Lottery/gambling not allowed.
- Compliance best practices: Obtain consent (proof of opt‑in) before marketing SMS; include clear opt‑out options.

### Norway Sender ID registration details
Send the following, along with a copy of your Business Registration, to alpha_sender_id@telnyx.com:
1) Sender ID to be registered
2) Message/content type
3) Message/content example
4) Company name (and brand name if different)
5) Website of brand or company
6) Company country of origin
7) Expected monthly volumes
8) Email linked to your Telnyx account

Notes: You must have a valid business case for the requested Sender ID. If the relationship between your company/brand and the requested ID is not obvious, include supporting documentation explaining the business case.

## Finland
- MCC: 244; Dial code: +358
- Sender ID: Upcoming regulation M28L mandates pre‑registration of all SMS sender IDs starting May 4, 2026.
- URLs: Filtered; valid URLs can be whitelisted (alpha_sender_id@telnyx.com).
- Content: Lottery/gambling not allowed.

## Iceland
- MCC: 274; Dial code: +354
- Sender ID: Alphanumeric supported; no registration required.
- URLs: Filtered; valid URLs can be whitelisted (alpha_sender_id@telnyx.com).
- Content: Lottery/gambling not allowed.

## Estonia
- MCC: 248; Dial code: +372
- Sender ID: Alphanumeric supported; no registration required.
- Content: No specific content restrictions reported by local operators (Telnyx Acceptable Use still applies).

## Latvia
- MCC: 247; Dial code: +371
- Sender ID: Alphanumeric supported; no registration required.
- Content: No specific content restrictions reported by local operators (Telnyx Acceptable Use still applies).

## Lithuania
- MCC: 246; Dial code: +370
- Sender ID: Alphanumeric supported; no registration required.
- Content: No specific content restrictions reported by local operators (Telnyx Acceptable Use still applies).

## Faroe Islands
- MCC: 288; Dial code: +298
- Sender ID: Alphanumeric supported; no registration required.
- Content: No specific content restrictions reported by local operators (Telnyx Acceptable Use still applies).

## Greenland
- MCC: 290; Dial code: +299
- Sender ID: Alphanumeric supported; no registration required. Generic/overly broad alphanumeric Sender IDs are not recommended; choose IDs clearly related to the message content.
- Content: No specific content restrictions reported by local operators (Telnyx Acceptable Use still applies).

## Contacts and support
- URL whitelisting and Sender ID questions (including Norway registration): alpha_sender_id@telnyx.com
- Telnyx Acceptable Use Policy for Messaging: https://support.telnyx.com/en/articles/1310359-acceptable-use-policy-for-messaging
