---
title: 'Mexico and Central America: SMS Guidelines'
summary: Key SMS rules for Mexico, Belize, Costa Rica, El Salvador, Guatemala, Honduras,
  Nicaragua, and Panama, including MCC, country dial codes, and how Alphanumeric Sender
  IDs are handled or registered to ensure delivery and compliance.
sources:
- url: https://support.telnyx.com/en/articles/6531664-mexico-sms-guidelines
  content_hash: c43f41dfd20e16a008f2f33a64116d68e87b07c16c1b07a99e1e40b7dc26a2b9
- url: https://support.telnyx.com/en/articles/6564226-costa-rica-sms-guidelines
  content_hash: 01c6782166b6cf3dca31835af121e3edd55a7233ecba9c63b894a007bde13157
- url: https://support.telnyx.com/en/articles/6573677-panama-sms-guidelines
  content_hash: 8dcd2263f371a0271bb7d90d7338a4e7d4c2cdcc279e21ca448cabd8ecd288ac
- url: https://support.telnyx.com/en/articles/6574032-guatemala-sms-guidelines
  content_hash: f2df797ea71c2ed6b528932a0300a2e9a680d4076b9c2b06579ccb36cd6d3322
- url: https://support.telnyx.com/en/articles/6574037-belize-sms-guidelines
  content_hash: d60dc3a30cf35ef10dac492e855dc70832f26d04431517adb68e190df177fb4b
- url: https://support.telnyx.com/en/articles/6574078-el-salvador-sms-guidelines
  content_hash: 2efa4b90eb25a8cbefcc7b95b1e73e4a4feb14e4b36fa53ffa6a0a42f3c330e8
- url: https://support.telnyx.com/en/articles/6574081-honduras-sms-guidelines
  content_hash: d96de2cc9c35b7baca0a28d257059a89aadeb0abda243161ba79872ad87536cc
- url: https://support.telnyx.com/en/articles/6574098-nicaragua-sms-guidelines
  content_hash: 500e7f3af22ff6df04d6789b40817b784a96347fab29dc745181a09ea3ddc4e7
updated_at: 2026-05-21T08:17:43Z
---

# Mexico and Central America: SMS Guidelines

Key SMS rules for Mexico, Belize, Costa Rica, El Salvador, Guatemala, Honduras, Nicaragua, and Panama, including MCC, country dial codes, and how Alphanumeric Sender IDs are handled or registered to ensure delivery and compliance.

## At-a-glance sender ID rules
- In most markets here (Mexico, Costa Rica, El Salvador, Nicaragua), Alphanumeric Sender IDs are not preserved and will be overwritten to a random local long code or a short code to ensure delivery.
- Belize requires Alphanumeric Sender ID registration; unregistered traffic is rejected.
- Guatemala and Panama do not support Alphanumeric Sender IDs and do not offer registration; traffic is overwritten to a local long code or short code.
- Honduras only partially supports Alphanumeric Sender IDs and does not offer registration; traffic can be overwritten to a local long code or short code to ensure delivery.
- Always adhere to Telnyx’s Acceptable Use Policy for Messaging: https://support.telnyx.com/en/articles/1310359-acceptable-use-policy-for-messaging. Consider using short codes where appropriate: https://telnyx.com/products/sms-short-code.

## Belize
- MCC: 702
- Dial code: 501
- Sender ID policy: Alphanumeric Sender ID registration is required. Messages from unregistered Sender IDs will be rejected.
- Registration: Email alpha_sender_id@telnyx.com with:
  1) Sender ID to be registered
  2) Message/content type
  3) Message/content example
  4) Company name (and brand name if different)
  5) Website of brand or company
  6) Company country of origin
  7) Expected monthly volumes
  8) Email linked to your Telnyx account
- Business case: A valid business case is required. If the relationship between your company/brand and the requested Sender ID isn’t clear, include supporting documentation.
- Recommendations: Obtain opt-in consent and include clear opt-out options in your messaging.

## Costa Rica
- MCC: 712
- Dial code: 506
- Sender ID policy: All Alphanumeric Sender IDs will be overwritten to a random local long code or a short code to ensure delivery.

## El Salvador
- MCC: 706
- Dial code: 503
- Sender ID policy: All Alphanumeric Sender IDs will be overwritten to a random local long code or a short code to ensure delivery.

## Guatemala
- MCC: 704
- Dial code: 502
- Sender ID policy: Alphanumeric Sender IDs are not supported; registration is not possible. Alphanumeric Sender IDs will be overwritten to a random local long code or a short code to ensure delivery.

## Honduras
- MCC: 708
- Dial code: 504
- Sender ID policy: Alphanumeric Sender IDs are partially supported; registration is not possible. Alphanumeric Sender IDs can be overwritten to a random local long code or a short code to ensure delivery.

## Mexico
- MCC: 334
- Dial code: 52
- Sender ID policy: All Alphanumeric Sender IDs will be overwritten to a random local long code or a short code to ensure delivery.

## Nicaragua
- MCC: 710
- Dial code: 505
- Sender ID policy: All Alphanumeric Sender IDs will be overwritten to a random local long code or a short code to ensure delivery.

## Panama
- MCC: 714
- Dial code: 507
- Sender ID policy: Alphanumeric Sender IDs are not supported; registration is not possible. Alphanumeric Sender IDs will be overwritten to a random local long code or a short code to ensure delivery.

## Acceptable use and delivery best practices
- Follow Telnyx’s Acceptable Use Policy for Messaging: https://support.telnyx.com/en/articles/1310359-acceptable-use-policy-for-messaging.
- Where Alphanumeric Sender IDs are unsupported or overwritten, plan to send from a local long code or consider a short code (https://telnyx.com/products/sms-short-code) to improve deliverability.
- Obtain and retain proof of opt-in consent and provide clear opt-out instructions, especially for marketing traffic (strongly recommended and explicitly noted for Belize).
