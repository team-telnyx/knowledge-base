---
title: Account Setup
summary: How to create a Telnyx account, understand the Trial-Paid-Verified-Enterprise
  (TPVE) account levels and their capabilities, upgrade your account, and configure
  data locality.
sources:
- url: https://developers.telnyx.com/docs/account-setup/account-upgrade
  content_hash: 6fc6483e714d069f3d54c110137f41039c7e735ccf7de5a00501df88fda0401a
- url: https://developers.telnyx.com/docs/account-setup/create-account
  content_hash: 685d6e4748abe65bb617357869c041ef2794163305cbab7a9cc9b34c63c333c3
- url: https://developers.telnyx.com/docs/account-setup/data-locality
  content_hash: 6dfe2e7310ed18ac10bcd516d71d3bf0a1d630807f0ae28978a759e00d04c968
- url: https://developers.telnyx.com/docs/account-setup/levels-and-capabilities/index
  content_hash: 6fe0740e9f547fd386fd3e370a286085eb37a0dc94c7e4f84442566b9d66dcab
- url: https://developers.telnyx.com/docs/account-setup/levels-and-capabilities/paid
  content_hash: b6cc578f16726956d109ea96579b0ecc04fdeeb790dbe22b8a0ef0038f2e20c4
- url: https://developers.telnyx.com/docs/account-setup/levels-and-capabilities/trial
  content_hash: 09b6fa8b90a8055f10297192686c40927990b84960f408d2db1b089d6cc7af24
- url: https://developers.telnyx.com/docs/account-setup/levels-and-capabilities/verified
  content_hash: 2a0a503b45c72adbdc5a65e657693f425554e3e1a368bd820c1e8c02897ee513
- url: https://developers.telnyx.com/docs/account-setup/signup
  content_hash: e29e4a1651c9533ae48c954616b75432c2673a9579e8d0d02d557286267374a8
- url: https://developers.telnyx.com/docs/account-setup/using-trial-account
  content_hash: cfac7d607f5a2fbccf422b84b62b6a5e2f088e6eb6e6ce86462bed8bacecc08d
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
