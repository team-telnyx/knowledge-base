---
title: Account Setup
summary: This page covers the full Telnyx account setup workflow, including creating
  an account, passing trust and safety checks, understanding the TPVE account framework
  (Trial, Paid, Verified, Enterprise), upgrading between levels, using trial account
  features, and configuring data locality for stored data.
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
updated_at: 2026-07-17T09:12:21Z
---

# Account Setup

*Part 1 of 2 — see also: [Part 2](account-setup--part-2.md)*

This page covers the full Telnyx account setup workflow, including creating an account, passing trust and safety checks, understanding the TPVE account framework (Trial, Paid, Verified, Enterprise), upgrading between levels, using trial account features, and configuring data locality for stored data.

## Account Setup Overview

Before using any Telnyx services, you need to create an account and complete onboarding through the [Mission Control Portal](https://portal.telnyx.com). New accounts come with free testing credits so you can explore the platform before adding payment methods.

## Creating Your Account

To create a Telnyx account:

1. Navigate to [telnyx.com/sign-up](https://telnyx.com/sign-up) to start the signup process.
2. Complete the signup form with your contact information, company details, and a secure password.
3. Verify your email by clicking the confirmation link sent to your inbox.
4. Log in to the [Mission Control Portal](https://portal.telnyx.com) with your new credentials to finish onboarding.

If you encounter issues during account creation, review the [Account Setup FAQ](https://support.telnyx.com), contact support through the Mission Control Portal, or join the [Telnyx Slack community](https://joinslack.telnyx.com) for developer support.

## Signup Trust and Safety Checks

Every signup attempt is subjected to a battery of trust and safety checks. An attempt will be unsuccessful if **any** of the following fails:

- Domain age
- Domain reputation
- Host reputation
- IP reputation
- Signup origin
- reCAPTCHA verification

Some attempts may also be subjected to additional requirements, including:

- Successfully validating a legitimate mobile number
- Successfully passing Know Your Customer (KYC) documentation verification

Telnyx constantly adjusts the logic, sequence, and thresholds to combat signup abuse and fraudulent usage of the platform.

## Account Frameworks

A successful signup may be placed in one of the following frameworks (but never both):

- **Level 1 / Level 2 account framework** — identified by the presence of the [verification page](https://portal.telnyx.com/#/account/my-account/verifications) in Mission Control.
- **Trial-Paid-Verified-Enterprise (TPVE) framework** — identified by the presence of the [Account Levels page](https://portal.telnyx.com/#/account/account-levels) in Mission Control.

The remainder of this account setup section is only relevant to accounts in the TPVE framework. The level of an account is an organizational attribute — if the account is paid, all organization members share the privileges and limits of a paid account.

## TPVE Account Levels

The TPVE framework includes four account levels: Trial, Paid, Verified, and Enterprise. Each level has different privileges and limitations.

### Trial Account

Trial accounts receive **USD $5** in testing credit and have full access except where otherwise specified.

**Numbers:**

- **Verified numbers:** Limited to 1 verified number at any one time, 10 changes per trial account lifetime, and 15 delivery attempts per trial account lifetime.
- **Number searching:** Full number display limited to local numbers of the account's country of origin; all other numbers are redacted (e.g., +49351xxxxxxx).
- **Number reservation:** Not available.
- **Number ordering:** Limited to 1 local number of the account's country of origin per trial account lifetime. The number is reclaimed within 30 days of purchase if the account has not upgraded. No port out is allowed.
- **Number porting:** Limited to 50 portability check attempts per trial account lifetime. Users do not have proprietary rights to their trial telephone number.
- **Bundles:** Not available.

**Messaging:**

- Limited to 1 messaging profile at any one time.
- **Outbound:** Long code sending only, destination limited to verified number, capped at 100 messages a day.
- **Inbound:** Limited to receiving from the verified number.

**Verify:**

- Limited to 1 verified profile at any one time.
- Only SMS is allowed.
- Destination limited to verified number.
- Limited to a max of 50 verifications a day.

**Voice:**

- Limited to 1 instance per connection type at any one time.
- Limited to 1 outbound voice profile at any one time.
- Outbound limited to dialing only the verified phone number; inbound limited to receiving from the verified phone number.
- Limited to 2 concurrent outbound calls across all connection instances.
- Limited to a maximum of 10 minutes per call.
- All machine-generated voices are prepended with: *"This is an automated call generated on the Telnyx platform, please report any abuse to fraud@telnyx.com"*. This applies to `/v2/calls`, `/v2/calls/:call_control_id/actions/transfer`, `/v2/calls/:call_control_id/actions/gather_using_audio`, `/v2/calls/:call_control_id/actions/gather_using_speak`, `/v2/calls/:call_control_id/actions/playback_start`, `/v2/calls/:call_control_id/actions/speak`, `/v2/calls/:call_control_id/actions/gather_using_ai`, `/v2/calls/:call_control_id/actions/ai_assistant_start`, and TeXML verbs `Play`, `Say`, and `AIGather`.
- Limited to a maximum of 100 outbound calls a day and 10 outbound calls per hour.
- Microsoft Operator Connect, Microsoft Direct Routing, and Zoom Phone Provider Exchange are not available.

**LRN / Number Lookup:** Not available.

**Cloud Storage:**

- Limited to non-public policy or ACL on buckets or objects.
- Limited to 5 minutes of TTL on pre-signed URLs.
- Limited to the documented free tier of used capacity across all buckets and regions.

**Wireless:** No access to physical SIM registration or eSIM purchase.

**Account features:**

- Organizations and sub-users: Not available.
- ManagED Accounts: Not available.
- Payment methods: Limited to credit cards.
- Billing groups: Not available.
- API keys: Limited to 1 API key at any one time.
- DDoS mitigation: Not available.

### Paid Account

Paid accounts have full access except where otherwise specified.

**Numbers:**

- **Number searching:** No access to number blocks.
- **Number ordering:** Limited to local numbers whose country code matches the account's country of origin.
- **Number porting:** No access to LRN migration.

**Messaging:** No access to 10DLC, Toll-Free verification, or hosted messaging.

**Voice:**

- Limited set of outbound destination country codes.
- Limited to 5 concurrent outbound calls across all connection types.
- All machine-generated voices are prepended with the same automated call notice as trial accounts, applied to the same endpoints and TeXML verbs.
- Limited to a maximum of 100 outbound calls a day and 10 outbound calls per hour.

**Cloud Storage:**

- Limited to non-public policy or ACL on buckets or objects.
- Limited to 5 minutes of TTL on pre-signed URLs.

**Account features:**

- ManagED Accounts: Not available.
- Payment methods: Credit card and PayPal.
- DDoS mitigation: Not available.

### Verified Account

Verified accounts have full access except where otherwise specified.

**Numbers:**

- **Number searching:** No access to number blocks.
- **Number ordering:** No access to number blocks.
- **Number porting:** No access to LRN migration.

**Account features:**

- ManagED Accounts: Not available.
- Payment methods: Credit card, PayPal, and BTC.
- DDoS mitigation: Not available.

### Enterprise Account

Qualification by the Telnyx sales team is required to upgrade to the enterprise level. [Contact Telnyx](https://telnyx.com/contact-us) to start the process.

## Upgrading Your Account

The criteria required for each account level are:

| Criteria | Trial | Paid | Verified |
| --- | --- | --- | --- |
| Verified email | X | X | X |
| Verified mobile number |  | X | X |
| Made a payment with CC/Debit Card |  | X | X |
| Enabled 2FA for the account |  | X | X |
| Provided Service Address |  | X | X |
| Successfully passed KYC |  |  | X |
| Successfully passed AI agent eval |  |  | X |

Identify the desired account level and complete **all** [required actions](https://portal.telnyx.com/#/account/account-levels). For enterprise upgrades, qualification by the Telnyx sales team is required.
