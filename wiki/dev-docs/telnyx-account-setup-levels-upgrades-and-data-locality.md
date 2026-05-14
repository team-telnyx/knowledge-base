---
title: Telnyx Account Setup, Levels, Upgrades, and Data Locality
summary: Learn how to sign up for Telnyx, understand account frameworks and levels
  (Trial, Paid, Verified, Enterprise), upgrade requirements, practical trial usage,
  and how to control where your data is stored at rest with Data Locality.
sources:
- url: https://developers.telnyx.com/docs/account-setup/account-upgrade
- url: https://developers.telnyx.com/docs/account-setup/create-account
- url: https://developers.telnyx.com/docs/account-setup/data-locality
- url: https://developers.telnyx.com/docs/account-setup/levels-and-capabilities
- url: https://developers.telnyx.com/docs/account-setup/levels-and-capabilities/paid
- url: https://developers.telnyx.com/docs/account-setup/levels-and-capabilities/trial
- url: https://developers.telnyx.com/docs/account-setup/levels-and-capabilities/verified
- url: https://developers.telnyx.com/docs/account-setup/signup
- url: https://developers.telnyx.com/docs/account-setup/using-trial-account
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
