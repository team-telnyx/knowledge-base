---
title: Telnyx account setup, levels, upgrades, and data locality
summary: Learn how to create a Telnyx account, understand signup checks, navigate
  account frameworks, use a trial safely, meet requirements to upgrade to Paid or
  Verified (and Enterprise), and choose where your data is stored at rest.
sources:
- url: https://developers.telnyx.com/docs/account-setup/account-upgrade
  content_hash: 6d8c97852328720c6328ef6ff1944a253c52dc1d8089ad796b1d1cebfefae6b6
- url: https://developers.telnyx.com/docs/account-setup/create-account
  content_hash: 5c807b4579be1f24607f8254309fa778c7ba2157c90b9f4ba3c93e5d9d7557dc
- url: https://developers.telnyx.com/docs/account-setup/data-locality
  content_hash: 8ce0559184cc5d398fb0fe7fcc33a499cf83fc0e9ea9922becaba4735b0777cc
- url: https://developers.telnyx.com/docs/account-setup/levels-and-capabilities
  content_hash: 40b12f885e21555ba8201a33984008ed1ed1aa280dcf2345a8246e3f51908f5b
- url: https://developers.telnyx.com/docs/account-setup/levels-and-capabilities/paid
  content_hash: 2d4dfdcf1a2d63b50a1886c0e05a80a3135fa6b9424e95530187a0778fd12276
- url: https://developers.telnyx.com/docs/account-setup/levels-and-capabilities/trial
  content_hash: 90951e85758304c94e050b3da12495ae00ec0d492aba4a8dce0bc320f32cbffa
- url: https://developers.telnyx.com/docs/account-setup/levels-and-capabilities/verified
  content_hash: 91c1e16a8c49d0be7e828440729d80b11816b97b62c524a7e9c04671d7c1d28f
- url: https://developers.telnyx.com/docs/account-setup/signup
  content_hash: 42d2831ad57df7baba593fd4fe5c9afed1f1d608b923f215f30bc0dd89e2320e
- url: https://developers.telnyx.com/docs/account-setup/using-trial-account
  content_hash: fa48f4aaf0c96158850ba4acb320bdc199cadb04cba679821e1cddff7c95a94d
updated_at: 2026-05-08T13:02:07Z
---

# Telnyx account setup, levels, upgrades, and data locality

Learn how to create a Telnyx account, understand signup checks, navigate account frameworks, use a trial safely, meet requirements to upgrade to Paid or Verified (and Enterprise), and choose where your data is stored at rest.

## Create an account
- Go to the signup page: [telnyx.com/sign-up](https://telnyx.com/sign-up)
- Complete the form with contact details, company info, and a secure password
- Verify your email via the confirmation link
- Log in to the Mission Control Portal: [portal.telnyx.com](https://portal.telnyx.com)

New accounts include free testing credits so you can explore before adding a payment method.

## Signup trust and safety checks
Every signup is evaluated by trust-and-safety controls. An attempt fails if any of the following fail:
- Domain age and reputation
- Host and IP reputation
- Signup origin
- reCAPTCHA verification

Some signups may require additional steps:
- Validate a legitimate mobile number
- Pass Know Your Customer (KYC) documentation verification

Telnyx regularly adjusts logic and thresholds to deter abuse and fraud.

## Account frameworks
A successful signup is placed in one — and only one — of these frameworks:
- Level 1 / Level 2 framework (you’ll see a “Verifications” page in Mission Control)
- Trial–Paid–Verified–Enterprise (TPVE) framework (you’ll see an “Account Levels” page in Mission Control)

The remainder of this page focuses on the TPVE framework.

## Account levels in the TPVE framework
Levels are organizational: if the account is Paid, all members inherit Paid privileges and limits. Telnyx may modify limits without notice.

Trial (highlights)
- Testing credit: USD $5
- Numbers: 1 verified number at a time; up to 10 changes per trial lifetime; up to 15 delivery attempts per trial lifetime. Can order 1 local number (country of signup origin) during trial; reclaimed in 30 days if not upgraded; cannot port out; up to 50 portability checks total
- Messaging: 1 messaging profile; outbound/inbound restricted to the verified number; up to 100 messages/day
- Verify: 1 verify profile; SMS only; restricted to verified number; up to 50 verifications/day
- Voice (general): 1 instance per connection type; 1 outbound voice profile; outbound and inbound restricted to the verified number; up to 2 concurrent outbound calls; max 10 minutes per call
- Voice (programmable): Automated disclaimer is prepended to machine-generated audio (TeXML Say/Play/AIGather and the listed Call Control actions); up to 100 outbound calls/day and 10/hour
- Cloud Storage: non-public bucket/object policies only; pre-signed URL TTL up to 5 minutes; limited to free-tier capacity
- Wireless: no physical SIM registration; no eSIM purchase
- Account features: no organizations/sub-users; 1 API key; credit card only; no billing groups; no DDoS mitigation; no ManagED Accounts

Paid (highlights)
- Access: Generally full except where limited below
- Numbers: Searching—no number blocks; Ordering—limited to local numbers matching the account’s country of origin; Porting—no LRN migration
- Messaging: No 10DLC, no Toll-Free verification, no hosted messaging
- Voice (general): Limited set of outbound destination country codes; up to 5 concurrent outbound calls
- Voice (programmable): Automated disclaimer is prepended to machine-generated audio (same surfaces as trial); up to 100 outbound calls/day and 10/hour
- Cloud Storage: non-public bucket/object policies only; pre-signed URL TTL up to 5 minutes
- Account features: Payment methods—credit card, PayPal; no DDoS mitigation; no ManagED Accounts

Verified (highlights)
- Access: Generally full except where limited below
- Numbers: Searching—no number blocks; Ordering—no number blocks; Porting—no LRN migration
- Account features: Payment methods—credit card, PayPal, BTC; no DDoS mitigation; no ManagED Accounts
- Enterprise upgrade is required (via sales qualification) to gain access to features not available at Verified (e.g., number blocks, LRN migration, certain managed/enterprise-only capabilities)

For granular, evolving limits and surfaces, consult the dedicated Trial, Paid, and Verified reference pages.

## Trial account usage guide
Make the most of your trial credit within trial limits:
1) Verify a phone number: Add a [verified number](https://portal.telnyx.com/#/numbers/verified-numbers) you control. Trial limits apply to changes and delivery attempts; upgrade once you exhaust allowances.
2) Search and purchase a phone number: Results fully display only local-to-signup numbers; others are redacted. Success depends on inventory, balance, and local [documentation rules](https://portal.telnyx.com/#/numbers/requirements). Only one order is allowed during trial.
3) Test calling workflows: Try [SIP Trunking](https://developers.telnyx.com/docs/voice/sip-trunking/get-started), [Programmable Voice](https://developers.telnyx.com/docs/voice/programmable-voice/get-started), or [TeXML](https://developers.telnyx.com/docs/voice/programmable-voice/texml-setup). Calls are restricted to/from your verified number; see Trial voice limits.
4) Test messaging workflows: Use the [Send Message](https://developers.telnyx.com/docs/messaging/messages/send-message) tutorial. Messaging is restricted to/from your verified number; see Trial messaging limits.

## Upgrading your account
Use the Account Levels page in Mission Control to see your current level and required actions.

Required actions by level
- Trial → baseline: Verify email (required for all levels)
- Paid → complete all of:
  - Verify a mobile number
  - Add a credit/debit card and make a payment
  - Enable 2FA for the account
  - Provide a service address
- Verified → everything for Paid, plus:
  - Successfully pass KYC
  - Successfully pass AI agent evaluation

Enterprise upgrade requires qualification by the Telnyx sales team. [Contact Telnyx](https://telnyx.com/contact-us) to begin.

## Data locality
Choose where Telnyx stores your data at rest.

Available regions
- US (United States) — default
- EU (Germany)
- APAC (Australia)

Covered data types
- Call Detail Records (CDRs)
- Message Detail Records (MDRs)
- Conference records
- Forking CDRs
- Media Storage (recordings)
- Premium AMD
- Speech-to-Text
- Verify
- Video
- WhatsApp
- Wireless

How to select a region
1) Log in to [Mission Control](https://portal.telnyx.com)
2) Go to Account settings → Profile
3) Under Data Storage Location, choose a country and click Save Location

Important
- You can change this setting only once; it cannot be undone
- Telnyx migrates existing data after you save; some features may be temporarily unavailable during migration
- If you do nothing, your account remains in the US region

## Getting help
- Browse the [Account Setup FAQ](https://support.telnyx.com)
- Open a ticket via the Mission Control Portal
- Join the [Telnyx Slack community](https://joinslack.telnyx.com) for developer support
