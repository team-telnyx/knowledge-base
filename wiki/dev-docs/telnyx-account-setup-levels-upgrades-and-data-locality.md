---
title: Telnyx Account Setup, Levels, Upgrades, and Data Locality
summary: Learn how to sign up for Telnyx, understand account frameworks and levels
  (Trial, Paid, Verified, Enterprise), upgrade requirements, practical trial usage,
  and how to control where your data is stored at rest with Data Locality.
sources:
- url: https://developers.telnyx.com/docs/account-setup/account-upgrade
  content_hash: 3f808ba07302802a7cd1a987ecc70eedc3f5445b5c0bddd7b191ac0ff729c4c1
- url: https://developers.telnyx.com/docs/account-setup/create-account
  content_hash: f873531ecb0530c75212afed9dd2f8d2f24aa748584d3581d16f1e8261cabfb0
- url: https://developers.telnyx.com/docs/account-setup/data-locality
  content_hash: f9cba3a2eda705135574eeae75b772c38ed0788ecde5f0cdbd244d617c408893
- url: https://developers.telnyx.com/docs/account-setup/levels-and-capabilities
  content_hash: 930689c5b93fcc6ae8779ac736c4c5a968e52a5d16b7827c321be4797321deb7
- url: https://developers.telnyx.com/docs/account-setup/levels-and-capabilities/paid
  content_hash: 70203441c259a2dbdb44a42b3b5fdf35e44c422eb2bb33c04903891bbbb9a7ee
- url: https://developers.telnyx.com/docs/account-setup/levels-and-capabilities/trial
  content_hash: 2c06d914371f57bf33923a7bdc567990b76257dfc2c3fa6cdcf74b6787094fe5
- url: https://developers.telnyx.com/docs/account-setup/levels-and-capabilities/verified
  content_hash: 108651193bc0bf75c46220c46f85a8a7c8a9b1e7f9f16186bda4875d2b0b9cc4
- url: https://developers.telnyx.com/docs/account-setup/signup
  content_hash: 0f65f7ba8a8dd18a82bd769af459ec98a6b840c772ebed9eb8456858ba27db14
- url: https://developers.telnyx.com/docs/account-setup/using-trial-account
  content_hash: 3ebe34654a4f52b37a68b203314fb32e1ff2838260413d0f7d477be7568f2282
updated_at: 2026-05-14T09:43:00Z
---

# Telnyx Account Setup, Levels, Upgrades, and Data Locality

Learn how to sign up for Telnyx, understand account frameworks and levels (Trial, Paid, Verified, Enterprise), upgrade requirements, practical trial usage, and how to control where your data is stored at rest with Data Locality.

## Understand account frameworks
After signup, an account is placed into one (and only one) of these frameworks:

- Level 1 / Level 2 framework: You’re in this framework if your Mission Control Portal shows a “Verifications” page at https://portal.telnyx.com/#/account/my-account/verifications.
- TPVE (Trial → Paid → Verified → Enterprise) framework: You’re in TPVE if your Portal shows an “Account Levels” page at https://portal.telnyx.com/#/account/account-levels. All level privileges and limits in this page refer to TPVE accounts.

The level is an organizational attribute—if the account is Paid, all organization members inherit Paid privileges and limits.

## Create your Telnyx account
1) Go to https://telnyx.com/sign-up. 2) Complete the form with contact, company, and password. 3) Verify your email by clicking the link sent to you. 4) Log in to the Mission Control Portal at https://portal.telnyx.com to finish onboarding. New accounts include USD $5 in testing credit so you can explore before adding payment.

## Signup trust and safety checks
Each signup is evaluated by automated trust-and-safety controls, including (non-exhaustive): domain age and reputation, host and IP reputation, signup origin, and reCAPTCHA. Failing any check will block signup. Some signups require additional steps, such as validating a legitimate mobile number or passing KYC (Know Your Customer) documentation. Telnyx continuously updates these controls to prevent abuse.

## Trial account: capabilities and limits
- Testing credit: USD $5.
- General access: Full platform access except where limited below; limits may change.
- Verified number: Required to test Voice and Messaging; limited to 1 verified number at a time, 10 changes per trial lifetime, and 15 delivery attempts per trial lifetime.
- Numbers
  - Search: Full display only for local numbers of the account’s country of origin; others are redacted. No number reservation.
  - Ordering: One local number (country of origin) per trial lifetime; activation depends on inventory, balance, and local documentation rules. Number is reclaimed within 30 days if the account isn’t upgraded; no port-out. Portability checks limited to 50 per trial lifetime.
- Messaging: One messaging profile; outbound limited to long code and to the verified number; max 100 messages/day. Inbound must originate from the verified number.
- Verify: One Verify profile; SMS only; destination limited to the verified number; max 50 verifications/day.
- Voice (connection instances and profiles)
  - Limits: 1 instance per connection type; 1 outbound voice profile; outbound/inbound restricted to the verified number; max 2 concurrent outbound calls; max 10 minutes per call.
  - Programmable Voice: All machine-generated voices are prefixed with “This is an automated call generated on the Telnyx platform, please report any abuse to fraud@telnyx.com”; applies to relevant Call Control APIs and TeXML (Play, Say, AIGather). Max 100 outbound calls/day and 10/hour.
  - No Microsoft Operator Connect, Direct Routing, or Zoom PPE.
- LRN/Number Lookup: No access.
- Cloud Storage: Only non-public bucket/object policies; pre-signed URL TTL up to 5 minutes; limited to documented free tier capacity across regions.
- Wireless: No physical SIM registration or eSIM purchase.
- Account features: No organizations/sub-users; no Managed Accounts; payment methods limited to credit card; no billing groups; limited to 1 API key; no DDoS mitigation.

## How to use your trial effectively
1) Verify a mobile number you control at https://portal.telnyx.com/#/numbers/verified-numbers; keep in mind trial change and attempt limits. 2) Search and purchase a local number (results outside your local country are redacted). Only one phone number order is allowed during the trial; activation depends on inventory, balance, and any local documentation requirements shown at https://portal.telnyx.com/#/numbers/requirements. 3) Test calling via SIP Trunking, Programmable Voice, or TeXML using the verified number as both the allowed destination for outbound and the source for inbound calls. 4) Test messaging with the Send Message workflow; outbound and inbound must involve the verified number. If you hit limits, upgrade your account.

- Helpful tutorials: SIP Trunking (https://developers.telnyx.com/docs/voice/sip-trunking/get-started), Programmable Voice (https://developers.telnyx.com/docs/voice/programmable-voice/get-started), TeXML (https://developers.telnyx.com/docs/voice/programmable-voice/texml-setup), Send Message (https://developers.telnyx.com/docs/messaging/messages/send-message).

## Upgrade paths and requirements
Choose your target level and complete all required actions at the Account Levels page: https://portal.telnyx.com/#/account/account-levels.

- Trial → Paid: Requires verified email, verified mobile number, a successful debit/credit card payment, 2FA enabled, and a service address on file.
- Paid → Verified: Requires all Paid actions plus successful KYC and successful AI agent evaluation.
- Enterprise: Requires qualification by the Telnyx sales team. Contact Telnyx at https://telnyx.com/contact-us.

Notes
- Complete all listed actions for the desired level; partially completed actions do not upgrade your level.
- For enterprise upgrades, sales qualification is mandatory even if other actions are complete.

## Paid account: capabilities and limits
- General access: Full platform access except where limited below; limits may change.
- Numbers
  - Search: No access to number blocks.
  - Ordering: Limited to local numbers whose country code matches the account’s country of origin.
  - Porting: No access to LRN migration.
- Messaging: No access to 10DLC, Toll-Free verification, or hosted messaging.
- Voice
  - General: Limited set of outbound destination country codes; max 5 concurrent outbound calls across all connection types.
  - Programmable Voice: Automated-voice disclaimer prefix (same as Trial) on relevant APIs/verbs; max 100 outbound calls/day and 10/hour.
- Cloud Storage: Only non-public bucket/object policies; pre-signed URL TTL up to 5 minutes.
- Account features: No Managed Accounts; payment methods: credit card and PayPal; no DDoS mitigation.

## Verified (and Enterprise) accounts
- General access: Full platform access except where limited below; limits may change.
- Numbers
  - Search: No access to number blocks.
  - Ordering: No access to number blocks.
  - Porting: No access to LRN migration.
- Account features
  - Managed Accounts: No access.
  - Payment methods: credit card, PayPal, BTC.
  - DDoS mitigation: No access.
- Enterprise upgrade: Needed to unlock features not available at Verified; qualification by the Telnyx sales team is required. Contact Telnyx at https://telnyx.com/contact-us.

## Data Locality
Control where your Telnyx data is stored at rest.

- Available regions
  - US (default)
  - EU (Germany)
  - APAC (Australia)
- Covered data types (stored at rest): CDRs, MDRs, conference records, forking CDRs, media storage (recordings), Premium AMD, Speech-to-Text, Verify, Video, WhatsApp, Wireless.
- How to select a region
  1) Log in to https://portal.telnyx.com. 2) Go to Account settings → Profile. 3) Under Data Storage Location, choose a country. 4) Click Save Location.
- Important behavior
  - The setting can be changed only once and cannot be undone.
  - Telnyx migrates your data after saving; some features may be temporarily unavailable during migration (duration varies with data size, from minutes to hours).
  - All existing accounts default to US unless you change it.

## Help and support
- Account Setup FAQ: https://support.telnyx.com
- Contact Support via the Mission Control Portal.
- Join the Telnyx Slack community: https://joinslack.telnyx.com
