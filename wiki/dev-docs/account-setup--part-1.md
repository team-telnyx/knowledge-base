---
title: Account Setup
summary: How to create a Telnyx account, understand the Trial-Paid-Verified-Enterprise
  (TPVE) account levels and their capabilities, upgrade your account, and configure
  data locality.
sources:
- url: https://developers.telnyx.com/docs/account-setup/account-upgrade
- url: https://developers.telnyx.com/docs/account-setup/create-account
- url: https://developers.telnyx.com/docs/account-setup/data-locality
- url: https://developers.telnyx.com/docs/account-setup/levels-and-capabilities/index
- url: https://developers.telnyx.com/docs/account-setup/levels-and-capabilities/paid
- url: https://developers.telnyx.com/docs/account-setup/levels-and-capabilities/trial
- url: https://developers.telnyx.com/docs/account-setup/levels-and-capabilities/verified
- url: https://developers.telnyx.com/docs/account-setup/signup
- url: https://developers.telnyx.com/docs/account-setup/using-trial-account
updated_at: 2026-06-11T10:23:30Z
---

# Account Setup

*Part 1 of 2 — see also: [Part 2](account-setup--part-2.md)*

How to create a Telnyx account, understand the Trial-Paid-Verified-Enterprise (TPVE) account levels and their capabilities, upgrade your account, and configure data locality.

## Creating an Account

Before using any Telnyx services, you must create an account to access the APIs and Mission Control Portal.

1. **Open the signup page** — Navigate to [telnyx.com/sign-up](https://telnyx.com/sign-up).
2. **Complete the signup form** — Enter your contact information, company details, and a secure password.
3. **Verify your email** — Click the confirmation link in the verification email.
4. **Log in to Mission Control** — Access the [Mission Control Portal](https://portal.telnyx.com) with your new credentials to finish onboarding.

New accounts come with free testing credits so you can explore the platform before adding payment methods.

If you encounter issues during account creation, review the [Account Setup FAQ](https://support.telnyx.com), contact support through the Mission Control Portal, or join the [Telnyx Slack community](https://joinslack.telnyx.com).

## Signup Trust and Safety Checks

Every signup attempt is subjected to a battery of trust and safety checks, including (in no particular order):

- Domain age
- Domain reputation
- Host reputation
- IP reputation
- Signup origin
- reCAPTCHA verification

An attempt will be unsuccessful if **any** of the above fails. Some attempts may also require:

- Successfully validating a legitimate mobile number
- Successfully passing Know Your Customer (KYC) documentation verification

Telnyx constantly adjusts the logic, sequence, and thresholds to combat signup abuse and fraudulent usage of the platform.

## Account Level Frameworks

A successful signup may be placed in one of two frameworks (**never both**):

- **Level 1 / Level 2 framework** — Identified when the [verification page](https://portal.telnyx.com/#/account/my-account/verifications) exists in Mission Control.
- **Trial-Paid-Verified-Enterprise (TPVE) framework** — Identified when the [Account Levels page](https://portal.telnyx.com/#/account/account-levels) exists in Mission Control.

The account level is an organizational attribute. If the account is a paid account, all organization members have the privileges and limits of a paid account.

## Trial Account Privileges and Limitations

Trial accounts receive **USD $5** in testing credit and have full access except as specified below. Telnyx reserves the right to modify limitations without notification.

### Numbers

- **Verified numbers** — Limited to 1 verified number at any time, 10 changes per trial account lifetime, and 15 delivery attempts per trial account lifetime.
- **Number searching** — Full display limited to local numbers of the account's country of origin; other numbers appear redacted (e.g., +49351xxxxxxx). No access to other number search APIs or features.
- **Number reservation** — No access.
- **Number ordering** — Limited to 1 local number of the account's country of origin per trial account lifetime. Activation depends on inventory, balance, and local jurisdiction documentation rules. The number will be reclaimed within 30 days if the account has not upgraded. No port-out allowed. No access to other ordering features.
- **Number porting** — Limited to 50 portability check attempts per trial account lifetime. No other porting access. Users do not have proprietary rights to their trial telephone number and cannot port it out.
- **Bundles** — No access.

### Messaging

- Limited to 1 messaging profile at any time.
- **Outbound** — Limited to long code sending, destination limited to the verified number, capped at 100 messages per day.
- **Inbound** — Limited to receiving from the verified number.
- No access to other messaging features.

### Verify

- Limited to 1 verified profile at any time.
- Only SMS is allowed; destination limited to the verified number.
- Limited to 50 verifications per day.
- No access to other Verify features.

### Voice

- **General limits** — Limited to 1 instance per connection type, 1 outbound voice profile, outbound calling only to the verified number, inbound only from the verified number, 2 concurrent outbound calls across all connection instances, and a maximum of 10 minutes per call.
- **Programmable Voice** — All machine-generated voices are prepended with: "*This is an automated call generated on the Telnyx platform, please report any abuse to fraud@telnyx.com*." This applies to Call Control actions (`speak`, `playback_start`, `gather_using_audio`, `gather_using_speak`, `gather_using_ai`, `ai_assistant_start`, `transfer`) and TeXML verbs (`Play`, `Say`, `AIGather`). Limited to 100 outbound calls per day and 10 outbound calls per hour.
- **Microsoft Operator Connect, Direct Routing, and Zoom Phone Provider Exchange** — No access.

### LRN / Number Lookup

- No access.

### Cloud Storage

- Limited to non-public policy or ACL on buckets or objects.
- Limited to 5 minutes of TTL on pre-signed URLs.
- Limited to the documented free tier of used capacity across all buckets and regions.

### Wireless

- No access to physical SIM registration or eSIM purchase.

### Account Features

- **Organizations and sub-users** — No access.
- **ManagED Accounts** — No access.
- **Payment methods** — Limited to credit cards.
- **Billing groups** — No access.
- **API keys** — Limited to 1 API key at any time.
- **DDoS mitigation** — No access.

## Using a Trial Account

Follow these steps to make the most of your trial credit while staying within trial limitations:

1. **Verify a phone number** — A [verified number](https://portal.telnyx.com/#/numbers/verified-numbers) is essential to test Voice and Messaging. Use a mobile number you control. Trial accounts have limits on delivery attempts and changes; once depleted, upgrade your account.
2. **Search for and purchase a phone number** — Search results show only local numbers (relative to signup origin) in full +E164 format; other results appear partially redacted. A successful purchase depends on inventory, balance, and local jurisdiction [documentation rules](https://portal.telnyx.com/#/numbers/requirements). Only one phone number order is allowed during the trial, regardless of outcome.
3. **Test calling workflows** — Use tutorials for [SIP Trunking](https://developers.telnyx.com/docs/voice/sip-trunking/get-started), [Programmable Voice](https://developers.telnyx.com/docs/voice/programmable-voice/get-started), or [TeXML](https://developers.telnyx.com/docs/voice/programmable-voice/texml-setup). The destination is limited to the verified number, and inbound calls must also originate from that number.
4. **Test messaging workflows** — Use the [Send Message](https://developers.telnyx.com/docs/messaging/messages/send-message) tutorial. Outbound messages must target the verified number, and inbound messages must originate from it.

## Paid Account Privileges and Limitations

Paid accounts have full access except as specified below. Telnyx reserves the right to modify limitations without notification.

### Numbers

- **Number searching** — No access to number blocks.
- **Number ordering** — Limited to local numbers whose country code matches the account's country of origin.
- **Number porting** — No access to LRN migration.

### Messaging

- No access to 10DLC, Toll-Free verification, or hosted messaging.

### Voice

- **General limits** — Limited set of outbound destination country codes; limited to 5 concurrent outbound calls across all connection types.
- **Programmable Voice** — All machine-generated voices are prepended with: "*This is an automated call generated on the Telnyx platform, please report any abuse to fraud@telnyx.com*." This applies to the same Call Control actions and TeXML verbs as trial accounts. Limited to 100 outbound calls per day and 10 outbound calls per hour.

### Cloud Storage

- Limited to non-public policy or ACL on buckets or objects.
- Limited to 5 minutes of TTL on pre-signed URLs.

### Account Features

- **ManagED Accounts** — No access.
- **Payment methods** — Credit card and PayPal.
- **DDoS mitigation** — No access.
