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

*Part 2 of 2 — see also: [Part 1](account-setup--part-1.md)*

How to create a Telnyx account, understand the Trial-Paid-Verified-Enterprise (TPVE) account levels and their capabilities, upgrade your account, and configure data locality.

## Verified Account Privileges and Limitations

Verified accounts have full access except as specified below. Telnyx reserves the right to modify limitations without notification.

### Numbers

- **Number searching** — No access to number blocks.
- **Number ordering** — No access to number blocks.
- **Number porting** — No access to LRN migration.

### Account Features

- **ManagED Accounts** — No access.
- **Payment methods** — Credit card, PayPal, and BTC.
- **DDoS mitigation** — No access.

Qualification by the Telnyx sales team is required to upgrade to the enterprise level to gain access to the above restricted features. [Contact Telnyx](https://telnyx.com/contact-us) to start the process.

## Upgrading Your Account

Each account level requires specific criteria to be met:

| Criteria | Trial | Paid | Verified |
|---|---|---|---|
| Verified email | X | X | X |
| Verified mobile number | | X | X |
| Made a payment with CC/Debit Card | | X | X |
| Enabled 2FA for the account | | X | X |
| Provided Service Address | | X | X |
| Successfully passed KYC | | | X |
| Successfully passed AI agent eval | | | X |

Identify the desired account level and complete **all** [required actions](https://portal.telnyx.com/#/account/account-levels). For enterprise upgrades, qualification by the Telnyx sales team is required. [Contact Telnyx](https://telnyx.com/contact-us) to begin the process.

## Data Locality

Data Locality lets you choose the geographic region where your Telnyx data is stored at rest.

### Available Regions

| Region | Location | Default |
|---|---|---|
| US | United States | Yes |
| EU | Germany | No |
| APAC | Australia | No |

### Covered Data Types

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

### Selecting a Region

1. Log in to the [Mission Control Portal](https://portal.telnyx.com).
2. Go to **Account settings** > **Profile**.
3. Scroll to **Data Storage Location** and select a country from the dropdown.
4. Click **Save Location**.

This setting can only be changed once and cannot be undone. After you save, Telnyx migrates your data to the new location. Some features may become temporarily unavailable during migration — the process can take a few minutes to several hours depending on your data size. All existing accounts default to the US; if you do not change the setting, your data remains in the US.
