---
title: 'East Asia SMS Guidelines: China, Hong Kong, Japan, Macao, Mongolia, Taiwan,
  South Korea'
summary: This page consolidates Telnyx SMS requirements for select East Asian destinations,
  covering MCC/dial codes, Sender ID handling and registration, content restrictions,
  delivery nuances, and key contacts. Always ensure campaigns comply with Telnyx’s
  Acceptable Use Policy and local regulations.
sources:
- url: https://support.telnyx.com/en/articles/6601144-china-sms-guidelines
  content_hash: 21c03844e539e93b692d67d93149bf1f13a67c38a2f03a9476a90e7f70903ee6
- url: https://support.telnyx.com/en/articles/6674367-hong-kong-sms-guidelines
  content_hash: 5e2267997a3741215d2acd4fcbcf7edf75173afe29cd8046f797df0e614abc94
- url: https://support.telnyx.com/en/articles/6674476-japan-sms-guidelines
  content_hash: 631768dffb2b184952813ac9195e9d9d81db736e59a8030c5919d9d665bed92d
- url: https://support.telnyx.com/en/articles/6675024-macao-sms-guidelines
  content_hash: 98c6f2ce8cd708e9219c88db0538f4dfeb91ad78dd23013a43d0fe16c7f643c2
- url: https://support.telnyx.com/en/articles/6677958-mongolia-sms-guidelines
  content_hash: fc07a16ad456958c3a4eeb40b9946c8e03193c8cd07e2b71c86458a6df01bf08
- url: https://support.telnyx.com/en/articles/6683277-taiwan-sms-guidelines
  content_hash: a7c097439fec21529412b170bc51c8e8879bae87830e14e752bb059c60da5edb
- url: https://support.telnyx.com/en/articles/6683734-korea-sms-guidelines
  content_hash: 941ef643e806d43bfbdec63394b3f8baea67729514b3505bb9dd15653cbd28f2
updated_at: 2026-05-21T08:29:07Z
---

# East Asia SMS Guidelines: China, Hong Kong, Japan, Macao, Mongolia, Taiwan, South Korea

This page consolidates Telnyx SMS requirements for select East Asian destinations, covering MCC/dial codes, Sender ID handling and registration, content restrictions, delivery nuances, and key contacts. Always ensure campaigns comply with Telnyx’s Acceptable Use Policy and local regulations.

## Overview
- Sender ID policies vary widely across these markets. Some require registration, some support Alphanumeric as-is, and others overwrite to local long codes (or short codes) to ensure delivery.
- Where required, pre-register content templates and obtain consent; include clear opt-out instructions for marketing traffic.
- For questions or Sender ID/content registration support, contact alpha_sender_id@telnyx.com and review the Telnyx Acceptable Use Policy.

## China (MCC 460, +86)
- Sender ID: Alphanumeric not supported; overwritten to a random local long code or a short code to ensure delivery.
- Content: All message content must be whitelisted by local operators; pre-registration of message templates is strongly advised.
- Support: For content whitelisting guidance, contact alpha_sender_id@telnyx.com.

## Hong Kong (MCC 454, +852)
- Sender ID: Alphanumeric registration required; unregistered Sender IDs are rejected.
- How to register: Email alpha_sender_id@telnyx.com with Business Registration and:
  1) Sender ID to register
  2) Message/content type
  3) Example message/content
  4) Company name (and brand, if different)
  5) Company/brand website
  6) Company country of origin
  7) Expected monthly volumes
  8) Email linked to your Telnyx account
- Eligibility: Must have a valid business case tied to the requested Sender ID; provide supporting documentation if the brand relationship is not obvious.
- Recommendations: Obtain opt-in and include clear opt-out options. Dual-number “2 numbers 1 SIM” handsets (one +86 and one +852) are common and can introduce delivery quirks.

## Japan (MCC 440, +81)
- Sender ID: Alphanumeric supported and preserved; no registration required.
- Filtering: Messages containing URLs may be filtered; use care with links.

## Macao (MCC 455, +853)
- Sender ID: Alphanumeric supported; no registration required.
- Network note: For deliveries toward China Telecom (45507), Sender IDs may be overwritten to a random Hong Kong long code.
- Content: No specific restrictions noted.

## Mongolia (MCC 428, +976)
- Sender ID: Alphanumeric supported and preserved; no registration required.
- Content: No specific restrictions noted.

## Taiwan (MCC 466, +886)
- Sender ID: All Alphanumeric Sender IDs are overwritten to a random local long code to ensure delivery.

## Republic of Korea (South Korea) (MCC 450, +82)
- Sender ID: All Alphanumeric Sender IDs are overwritten to a random local long code to ensure delivery.
- Mandatory tags: Messages will include by default:
  - [Web 발신] — indicates A2P traffic
  - [국제발신] — indicates the message was sent from abroad
- Content: Gambling and adult content are prohibited.

## Contacts and helpful links
- Sender ID/content registration and guidance: alpha_sender_id@telnyx.com
- Telnyx Acceptable Use Policy for Messaging: https://support.telnyx.com/en/articles/1310359-acceptable-use-policy-for-messaging
- A2P messaging overview: https://telnyx.com/resources/what-is-a2p-messaging
- Telnyx Short Code product (relevant for China short code delivery): https://telnyx.com/products/sms-short-code
