---
source_url: https://support.telnyx.com/en/articles/14708129-porting-numbers-away-from-intercom-to-telnyx
title: "Porting Numbers Away from Intercom to Telnyx"
description: "How to port numbers from Intercom's calling product, including Twilio-backed number instructions and common PIN issues. See Telnyx guidance and requirements."
scraped: 2026-07-08
content_hash: 583288b2e14ab3314e3b3b44c9a3bcac897212bf6c286018a5ebc7e7fb6eef4f
---







# Porting Numbers Away from Intercom to Telnyx

How to port numbers from Intercom's calling product, including Twilio-backed number instructions and common PIN issues. See Telnyx guidance and requirements.




## Overview

Intercom provides phone numbers as part of its calling product, but like most software platforms, Intercom doesn't own the underlying phone number infrastructure. The numbers are hosted on a carrier (commonly Twilio), which means porting away from Intercom requires carrier-level authorization — not just your Intercom credentials.

## Before You Start

Contact **Intercom support** and ask for:

1. The **underlying carrier** for your phone numbers
2. Your **account number** as registered with the underlying carrier
3. The **PIN or passcode** needed to authorize a port-out

**Note:** The information you need is at the carrier level — it's different from your Intercom login credentials, subscription ID, or workspace ID.

## What to Enter in Your Telnyx Port Request

|  |  |
| --- | --- |
| Field | What to Enter |
| Account Number | Carrier account number (provided by Intercom support) |
| PIN / Passcode | Carrier-level port-out PIN (provided by Intercom support) |
| Authorized Name | Exact name on the Intercom carrier account |
| Service Address | Address registered with the underlying carrier |

## Twilio-Backed Intercom Numbers

If Intercom tells you your numbers are on Twilio, use these specific instructions:

* **Account Number:** Twilio Account SID (starts with "AC...") — found in Twilio Console, or ask Intercom to provide it
* **PIN:** Twilio auth token or a dedicated port-out passcode (set under Console > Phone Numbers > Port Out Settings in newer Twilio accounts)
* **Authorized Name:** The legal name on the Twilio/Intercom account

**⚠️** Twilio's PIN requirements have changed over time. If you get a PIN rejection, ask Intercom support specifically: *"What is the current port-out passcode or auth token for my account?"*

## Why Does Porting from Intercom Feel Different?

Intercom (like Aircall and other calling-enabled platforms) sits as an additional layer on top of a carrier. This means:

* The underlying carrier may vary by country or account type
* The required credentials are carrier-specific, not Intercom-specific
* Intercom's support team may need to look up your carrier details internally before they can provide the right information

## I Got a PIN Rejection — What Now?

1. Contact Intercom support and ask specifically for the carrier-level port-out PIN
2. Ask them to confirm whether your numbers are on Twilio and if so, which Twilio account
3. Once you have the correct PIN, update your port order in the Telnyx portal and resubmit

## Estimated Timeline

* **1–5 numbers:** 3–7 business days from acceptance
* **6+ numbers:** 5–15 business days

---

Related Articles

[Port numbers away from Telnyx](https://support.telnyx.com/en/articles/2033789-port-numbers-away-from-telnyx)[Porting away from Twilio](https://support.telnyx.com/en/articles/3947850-porting-away-from-twilio)[Porting Numbers Away from Aircall to Telnyx](https://support.telnyx.com/en/articles/14708128-porting-numbers-away-from-aircall-to-telnyx)[Porting Numbers Away from Resellers (Aircall, Intercom, RingCentral, Vonage, etc.)](https://support.telnyx.com/en/articles/14708130-porting-numbers-away-from-resellers-aircall-intercom-ringcentral-vonage-etc)[How to Find Your Porting PIN or Passcode](https://support.telnyx.com/en/articles/14790558-how-to-find-your-porting-pin-or-passcode)

Did this answer your question?

😞😐😃
