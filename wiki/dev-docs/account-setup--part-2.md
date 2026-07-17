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

*Part 2 of 2 — see also: [Part 1](account-setup--part-1.md)*

This page covers the full Telnyx account setup workflow, including creating an account, passing trust and safety checks, understanding the TPVE account framework (Trial, Paid, Verified, Enterprise), upgrading between levels, using trial account features, and configuring data locality for stored data.

## Using Your Trial Account

To make the most of your trial credit and stay within trial limitations:

1. **Verify a phone number.** A [verified number](https://portal.telnyx.com/#/numbers/verified-numbers) is essential to test Voice and Messaging. Use a mobile phone number that you control. Trial accounts have limits on delivery attempts and the number of changes allowed. Once the allowance is depleted, [upgrade your account](https://developers.telnyx.com/docs/account-setup/account-upgrade).
2. **Search for and purchase a phone number.** Search results show only local (to the signup origin) numbers in full +E164; other results appear partially redacted. A successful purchase depends on inventory availability, sufficient account balance, and local jurisdiction [documentation rules](https://portal.telnyx.com/#/numbers/requirements). Only one phone number order is allowed during the trial, regardless of the outcome.
3. **Test calling workflows.** Use one of the following tutorials to place calls:
   - [SIP Trunking](https://developers.telnyx.com/docs/voice/sip-trunking/get-started)
   - [Programmable Voice](https://developers.telnyx.com/docs/voice/programmable-voice/get-started)
   - [TeXML](https://developers.telnyx.com/docs/voice/programmable-voice/texml-setup)

   Regardless of how the call is created, the destination is limited to the verified phone number from Step 1, and inbound calls must also originate from that number.
4. **Test messaging workflows.** Use the [Send Message](https://developers.telnyx.com/docs/messaging/messages/send-message) tutorial to send SMS. Outbound messages must target the verified phone number you configured, and inbound messages must also originate from that number.

## Data Locality

Data Locality lets you choose the geographic region where your Telnyx data is stored at rest.

### Available Regions

| Region | Location | Default |
| --- | --- | --- |
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

This setting can only be changed once and cannot be undone. After you save, Telnyx migrates your data to the new location. Some features may become temporarily unavailable during migration — the process can take a few minutes to several hours depending on your data size.

All existing accounts default to the US. If you do not change the setting, your data remains in the US.
