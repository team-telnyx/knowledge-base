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

*Part 3 of 3 — see also: [Part 1](account-setup--part-1.md), [Part 2](account-setup--part-2.md)*

Walks through creating a Telnyx account, the trust and safety checks applied at signup, the Pretrial–Trial–Paid–Verified–Enterprise (PTPVE) account framework, the privileges and limitations at each level, data locality options, and how to upgrade between levels.

## Upgrading your account

The criteria for each PTPVE level are summarized below.

| Criteria | Pretrial | Trial | Paid | Verified |
| --- | --- | --- | --- | --- |
| Verified email | X | X | X | X |
| Passed fraud review (LinkedIn/GitHub verification or AI agent eval) |  | X | X | X |
| Verified mobile number |  |  | X | X |
| Made a payment with CC/Debit Card |  |  | X | X |
| Enabled 2FA for the account |  |  | X | X |
| Provided Service Address |  |  | X | X |
| Successfully passed KYC |  |  |  | X |
| Successfully passed AI agent eval |  |  |  | X |

Identify the desired account level and complete **all** [required actions](https://portal.telnyx.com/#/account/account-levels). For enterprise upgrades, qualification by the Telnyx sales team is required — [contact Telnyx](https://telnyx.com/contact-us) to begin the process.

## Data locality

Data Locality lets you choose the geographic region where your Telnyx data is stored at rest.

### Available regions

| Region | Location | Default |
| --- | --- | --- |
| US | United States | Yes |
| EU | Germany | No |
| APAC | Australia | No |
| Middle East | UAE | No |

### Covered data types

Data locality applies to the following data stored at rest:

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

### Selecting a region

1. Log in to the [Mission Control Portal](https://portal.telnyx.com).
2. Go to **Account settings** > **Profile**.
3. Scroll to **Data Storage Location** and select a country from the dropdown.
4. Click **Save Location**.

This setting can only be changed once and cannot be undone. After you save, Telnyx migrates your data to the new location. Some features may become temporarily unavailable during migration — the process can take a few minutes to several hours depending on your data size.

All existing accounts default to the US. If you do not change the setting, your data remains in the US.
