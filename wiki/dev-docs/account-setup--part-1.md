---
title: Account Setup
summary: Walks through creating a Telnyx account, the trust and safety checks applied
  at signup, the Pretrial–Trial–Paid–Verified–Enterprise (PTPVE) account framework,
  the privileges and limitations at each level, data locality options, and how to
  upgrade between levels.
sources:
- url: https://developers.telnyx.com/docs/account-setup/account-upgrade
- url: https://developers.telnyx.com/docs/account-setup/create-account
- url: https://developers.telnyx.com/docs/account-setup/data-locality
- url: https://developers.telnyx.com/docs/account-setup/levels-and-capabilities/index
- url: https://developers.telnyx.com/docs/account-setup/levels-and-capabilities/paid
- url: https://developers.telnyx.com/docs/account-setup/levels-and-capabilities/pretrial
- url: https://developers.telnyx.com/docs/account-setup/levels-and-capabilities/trial
- url: https://developers.telnyx.com/docs/account-setup/levels-and-capabilities/verified
- url: https://developers.telnyx.com/docs/account-setup/signup
- url: https://developers.telnyx.com/docs/account-setup/using-trial-account
updated_at: 2026-08-05T13:38:21Z
---

# Account Setup

*Part 1 of 3 — see also: [Part 2](account-setup--part-2.md), [Part 3](account-setup--part-3.md)*

Walks through creating a Telnyx account, the trust and safety checks applied at signup, the Pretrial–Trial–Paid–Verified–Enterprise (PTPVE) account framework, the privileges and limitations at each level, data locality options, and how to upgrade between levels.

## Overview

A successful Telnyx signup is placed in one of two frameworks (but never both):

- **Level 1 / Level 2** — used when the [verification page](https://portal.telnyx.com/#/account/my-account/verifications) is present in Mission Control.
- **Pretrial–Trial–Paid–Verified–Enterprise (PTPVE)** — used when the [Account Levels page](https://portal.telnyx.com/#/account/account-levels) is present in Mission Control.

The account level is an organizational attribute. For paid accounts, every member of the organization inherits the privileges and limits of that paid level. For a complete picture of what is available at each level, consult the per-level pages together with the V2 APIs and S3 Compatible Storage APIs tables.

## Creating an account

Before using any Telnyx service you need an account that grants access to the APIs and the Mission Control Portal.

1. Open the [signup page](https://telnyx.com/sign-up).
2. Complete the signup form with your contact information, company details, and a secure password.
3. Verify your email by clicking the confirmation link sent to the address you provided.
4. Log in to the [Mission Control Portal](https://portal.telnyx.com) to finish onboarding and explore the dashboard.

New accounts come with free testing credits so you can explore the platform before adding a payment method.

If you run into trouble during signup, review the [Account Setup FAQ](https://support.telnyx.com), contact support through the Mission Control Portal, or join the [Telnyx Slack community](https://joinslack.telnyx.com) for developer help.

## Signup trust and safety checks

Every signup attempt is subjected to a battery of trust and safety checks. An attempt is unsuccessful if **any** of the following fails:

- Domain age
- Domain reputation
- Host reputation
- IP reputation
- Signup origin
- reCAPTCHA verification

Some attempts may also be required to complete additional steps, including:

- Successfully validating a legitimate mobile number
- Successfully passing Know Your Customer (KYC) documentation verification

Telnyx constantly adjusts the logic, sequence, and thresholds of these checks to combat signup abuse and fraudulent usage of the platform.

## Pretrial account

Pretrial accounts are designed for exploring the AI Suite before committing to a full trial.

### Testing credit

- **USD $25** in AI credits is provided.

### Access

- Full access to the AI Suite (AI Assistant, Inference, Cloud Storage) except where noted below.
- Telnyx reserves the right to modify limitations without notification.

### Numbers

- **Searching** — Full number display is limited to USA local numbers only. All other numbers are shown redacted (e.g., `+49351xxxxxxx`). No access to other APIs or features in this category.
- **Reservation** — No access.
- **Ordering** — Limited to **1 USA local number** per pretrial account lifetime. No access to global numbers. No port out is allowed on this number. The number is reclaimed within 30 days of purchase if the account has not upgraded. No access to other APIs or features in this category.
- **Porting** — No access.
- **Bundles** — No access.

### Messaging

- Limited to **1 messaging profile** at any one time.
- **Outbound** — Long code sending only, destination limited to the verified number, capped at **10 messages a day**.
- **Inbound** — Limited to receiving from the verified number.
- No access to other APIs or features in this category.

### Verify

- No access.

### Voice

- **General limits** — Limited to **1 TeXML Application** and **1 outbound voice profile** at any one time. Outbound calls are limited to dialing only the verified phone number; inbound calls are limited to receiving from the verified phone number. Limited to **2 concurrent outbound calls** and a maximum of **10 minutes per call**.
- **Programmable Voice** — All machine-generated voices are prepended with: *"This is an automated call generated on the Telnyx platform, please report any abuse to [fraud@telnyx.com](mailto:fraud@telnyx.com)"*. This applies to `/v2/calls`, `/v2/calls/:call_control_id/actions/transfer`, `/v2/calls/:call_control_id/actions/gather_using_audio`, `/v2/calls/:call_control_id/actions/gather_using_speak`, `/v2/calls/:call_control_id/actions/playback_start`, `/v2/calls/:call_control_id/actions/speak`, `/v2/calls/:call_control_id/actions/gather_using_ai`, `/v2/calls/:call_control_id/actions/ai_assistant_start`, and the TeXML verbs `Play`, `Say`, and `AIGather`. Limited to a maximum of **10 outbound calls a day**.
- **Call Control Applications, Microsoft Operator Connect, Microsoft Direct Routing, Zoom Phone Provider Exchange** — No access.

### LRN / Number Lookup

- No access.

### Cloud Storage

- Limited to non-public policy or ACL on buckets or objects.
- Limited to **5 minutes of TTL** on pre-signed URLs.
- Limited to the documented free tier of used capacity across all buckets and regions.

### Wireless

- No access.

### Account features

- **Organizations and sub-users** — No access.
- **ManagED Accounts** — No access.
- **Payment methods** — No access. Credit is not required; AI credits are provided.
- **Billing groups** — No access.
- **API keys** — Limited to **1 API key** at any one time. No access to other APIs or features in this category.
- **DDoS mitigation** — No access.
