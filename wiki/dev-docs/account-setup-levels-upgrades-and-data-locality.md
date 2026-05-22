---
title: Account Setup, Levels, Upgrades, and Data Locality
summary: End-to-end guide to creating a Telnyx account, understanding account level
  frameworks, key privileges and limits for Trial/Paid/Verified (TPVE), how to upgrade,
  how to use your trial effectively, and how to choose where your data is stored at
  rest.
sources:
- url: https://developers.telnyx.com/docs/account-setup/account-upgrade
  content_hash: 6b94859567f7d1b4e847eddb0e15fe4d2f0ae4067b6b2bcc2715c29452d24725
- url: https://developers.telnyx.com/docs/account-setup/create-account
  content_hash: f7ddfa2c75a23c6550152d6e1ece7b492181f58af994ea82c07ad9824a89a390
- url: https://developers.telnyx.com/docs/account-setup/data-locality
  content_hash: 94d213f227aff5a30b581a456d6bfdc28f944a44fc25f2f1f32344c85626dd8d
- url: https://developers.telnyx.com/docs/account-setup/levels-and-capabilities/index
  content_hash: dba3977c044d14263ba39f7e74c6cd1dc87653333909f4673f39119e16fef0f7
- url: https://developers.telnyx.com/docs/account-setup/levels-and-capabilities/paid
  content_hash: 913d753248d3d1a718f2e60bb2f03d3be76c83610839c0455c40c7236ef8ac00
- url: https://developers.telnyx.com/docs/account-setup/levels-and-capabilities/trial
  content_hash: 3a4318b873d7feb17afc462e0240775e32b3fc77c76faebb5bb7174637ec8316
- url: https://developers.telnyx.com/docs/account-setup/levels-and-capabilities/verified
  content_hash: 37754b969dbc01c505b4342ce2f335d1382ab7585a72f086e722e15b03fc2946
- url: https://developers.telnyx.com/docs/account-setup/signup
  content_hash: 766d51285d919d6b9a58c192aa068bcf489477e431b692e11b6bcb295667cdfc
- url: https://developers.telnyx.com/docs/account-setup/using-trial-account
  content_hash: 2dd95422a7aaf4ceaaf03835ef6a29ab3678a302cf7a5e5b034965148f568599
updated_at: 2026-05-19T15:53:31Z
---

# Account Setup, Levels, Upgrades, and Data Locality

End-to-end guide to creating a Telnyx account, understanding account level frameworks, key privileges and limits for Trial/Paid/Verified (TPVE), how to upgrade, how to use your trial effectively, and how to choose where your data is stored at rest.

## Account creation and onboarding

- Go to telnyx.com/sign-up to start, complete the form with your contact/company details and a secure password, verify your email, then log in to the Mission Control Portal to finish onboarding. New accounts include USD $5 in testing credit.
- See [Create Your Telnyx Account](create-your-telnyx-account.md) and [Account Signup](account-signup.md) for step-by-step guidance.

## Trust and safety during signup

Every signup attempt passes automated checks (domain age/reputation, host/IP reputation, signup origin, reCAPTCHA). If any check fails, signup is unsuccessful. Some signups must also validate a legitimate mobile number and/or pass KYC. Telnyx updates controls and thresholds over time to prevent abuse.

## Account level frameworks

After signup, your account is placed in exactly one framework (never both):
- Level 1 / Level 2 framework — you’ll see a “Verifications” page in Mission Control.
- Trial–Paid–Verified–Enterprise (TPVE) framework — you’ll see an “Account Levels” page in Mission Control.

The remainder of this page focuses on TPVE. For framework context, see [Account Levels and Capabilities](account-levels-and-capabilities.md).

## TPVE levels at a glance

For full, authoritative details, consult:
- [Trial Account Privileges & Limitations](trial-account-privileges-limitations.md)
- [Paid Account Privileges & Limitations](paid-account-privileges-limitations.md)
- [Verified Account Privileges & Limitations](verified-account-privileges-limitations.md)

Note: Telnyx may modify limitations without notice.

### Trial (highlights)

- Credit and access
  - USD $5 testing credit; “full access except as limited below.”
  - 1 API key at any time; payment methods limited to credit cards.
- Numbers
  - 1 verified number at a time; up to 10 changes per trial lifetime; 15 delivery attempts per lifetime.
  - Number search: full display limited to local numbers of the signup country; others are redacted.
  - Ordering: 1 local number (of account’s country) per trial lifetime; may be reclaimed within 30 days if not upgraded; no port-out; activation subject to inventory, balance, and local documentation rules.
  - Porting: up to 50 portability checks per lifetime.
- Messaging and Verify
  - Messaging: 1 messaging profile; outbound limited to the verified number; inbound must originate from that number; cap 100 messages/day.
  - Verify: 1 verify profile; SMS only; destination limited to verified number; up to 50 verifications/day.
- Voice
  - 1 instance per connection type and 1 outbound voice profile at a time.
  - Outbound may dial only the verified number; inbound must originate from that number.
  - Up to 2 concurrent outbound calls; max 10 minutes per call.
  - Programmable Voice: a disclosure is prepended to machine-generated speech; capped at 100 outbound calls/day and 10/hour; applies to V2 calls/Call Control actions and TeXML Play/Say/AIGather.
  - No access to Microsoft Operator Connect, Microsoft Direct Routing, or Zoom Phone Provider Exchange.
- Cloud Storage and wireless
  - Cloud Storage: buckets/objects must be non-public; pre-signed URL TTL up to 5 minutes; limited to documented free-tier capacity across buckets/regions.
  - Wireless: no physical SIM registration; no eSIM purchase.
- Account features
  - No organizations/sub-users, no ManagED Accounts, no billing groups, no DDoS mitigation.

### Paid (highlights)

- Access generally open, with notable limits:
  - Numbers: no access to number blocks; ordering limited to local numbers whose country code matches the account’s country of origin; no LRN migration in porting.
  - Messaging: no access to 10DLC, Toll-Free verification, or hosted messaging.
  - Voice: limited set of outbound destination country codes; up to 5 concurrent outbound calls; Programmable Voice disclosure applies; 100 outbound calls/day and 10/hour caps.
  - Cloud Storage: non-public policies/ACLs only; pre-signed URL TTL up to 5 minutes.
  - Account features: no ManagED Accounts; payment methods: credit card and PayPal; no DDoS mitigation.

### Verified (highlights)

- Access generally open, with noted exceptions:
  - Numbers: no access to number blocks (searching/ordering); no LRN migration in porting.
  - Account features: no ManagED Accounts; payment methods include credit card, PayPal, and BTC; no DDoS mitigation.
- Enterprise upgrade requires Telnyx sales qualification. Contact Telnyx to begin.

## How to upgrade your account

Identify your target level and complete all required actions in Mission Control (Account Levels page):
- Trial (default after signup): requires verified email.
- Paid: requires all of the following — verified email, verified mobile number, payment made with a credit/debit card, 2FA enabled, and a service address on file.
- Verified: requires successful KYC and successful AI agent evaluation (in addition to the Paid requirements).
- Enterprise: requires sales team qualification; contact Telnyx to start the process.

Tip: Use the in-portal checklist to confirm completion of each requirement.

## Using your trial effectively

1) Verify a phone number — add a mobile number you control as a verified number in Mission Control. Trial allowances for verified numbers are limited; once exhausted, upgrade your account.

2) Search and purchase a number — search shows local-to-signup-country numbers in full +E.164, others redacted. A successful purchase depends on inventory, balance, and local documentation rules. Only one phone number order is allowed during trial, regardless of outcome.

3) Test calling — try SIP Trunking, Programmable Voice, or TeXML quickstarts. Regardless of method, outbound calls can only target your verified number, and inbound must originate from it. Observe the trial voice limits above.

4) Test messaging — send SMS using the Messages API quickstart. Outbound must target, and inbound must originate from, your verified number. Observe the trial messaging limits above.

## Data locality

Choose where Telnyx stores your data at rest.

### Available regions

- US (United States) — default
- EU (Germany)
- APAC (Australia)

### Covered data types

Applies to stored-at-rest data including: CDRs, MDRs, conference records, forking CDRs, media storage (recordings), Premium AMD, Speech-to-Text, Verify, Video, WhatsApp, and Wireless.

### Selecting a region

1) Log in to the Mission Control Portal.
2) Go to Account settings > Profile.
3) In Data Storage Location, choose a country and save.

Important: You can change this setting only once and it cannot be undone. After saving, Telnyx migrates your data to the new region; some features may be temporarily unavailable during migration, which can take minutes to hours depending on data size. Existing accounts default to US if not changed.

## Related references

- [Trial Account Privileges & Limitations](trial-account-privileges-limitations.md)
- [Paid Account Privileges & Limitations](paid-account-privileges-limitations.md)
- [Verified Account Privileges & Limitations](verified-account-privileges-limitations.md)
- [Account Upgrade](account-upgrade.md)
- [Data Locality](data-locality.md)
- [Account Levels and Capabilities](account-levels-and-capabilities.md)
- [Using Your Trial Account](using-your-trial-account.md)
- [Create Your Telnyx Account](create-your-telnyx-account.md)
- [Account Signup](account-signup.md)

External quickstarts: SIP Trunking, Programmable Voice, TeXML, and Send Message tutorials are available on developers.telnyx.com.
