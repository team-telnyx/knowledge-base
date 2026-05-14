---
title: Porting to Telnyx from Resellers, Skype, and French Overseas Territories
summary: This guide explains how to port numbers to Telnyx from reseller-backed services
  (Aircall, Intercom, RingCentral, Vonage, Grasshopper), from Skype, and from select
  French overseas territories — covering required carrier-level credentials, PIN/PAC
  specifics, timelines, common rejection reasons, and country documentation requirements.
sources:
- url: https://support.telnyx.com/en/articles/10715399-porting-away-from-skype
  content_hash: c6c29c49f44d2c985f38848316df4cf18ce3784f1b1e7a137cce1effc497ac54
- url: https://support.telnyx.com/en/articles/14708128-porting-numbers-away-from-aircall-to-telnyx
  content_hash: 4c4089c00d134dd3936cc5a6ffe4fbbbff32395cde5ed1bd68a2255421a44af8
- url: https://support.telnyx.com/en/articles/14708129-porting-numbers-away-from-intercom-to-telnyx
  content_hash: bd6d4896dfb0333528e3b92beff28e7e9bac7ae1a419d8b32a8cb4dc4828756f
- url: https://support.telnyx.com/en/articles/14708130-porting-numbers-away-from-resellers-aircall-intercom-ringcentral-vonage-etc
  content_hash: 215326da17500f8a6256780be4ad0a09030e3140ba1ab4e60803465a015e75e0
- url: https://support.telnyx.com/en/articles/13194814-french-guiana-number-porting
  content_hash: ad1a3e3ca988eae2a645c160e8be6536cca8e8b708a8cdc304794fe67ecc4c5c
- url: https://support.telnyx.com/en/articles/13194884-mayotte-number-porting
  content_hash: ddfcad14a4b4e2282dfcff11049d86e6e695257c3fa6556fa0f126fa25014bec
- url: https://support.telnyx.com/en/articles/13194922-reunion-number-porting
  content_hash: 75619dd097b774ecc2bf42177324774abc4f49c7bf4ef048e82db17934e5875f
- url: https://support.telnyx.com/en/articles/13194951-saint-barth-and-saint-martin-number-porting
  content_hash: 2ae39411dc4c7c2d031334a81d9bf533a5076628e27f726f49b991688e998bc8
updated_at: 2026-05-14T11:33:13Z
---

# Porting to Telnyx from Resellers, Skype, and French Overseas Territories

This guide explains how to port numbers to Telnyx from reseller-backed services (Aircall, Intercom, RingCentral, Vonage, Grasshopper), from Skype, and from select French overseas territories — covering required carrier-level credentials, PIN/PAC specifics, timelines, common rejection reasons, and country documentation requirements.

## Overview
When porting to Telnyx from many software/VoIP providers, your numbers usually sit on an underlying carrier (e.g., Twilio, Bandwidth, Inteliquent). Authorization for the port must match the losing carrier’s records — not just your app login. Skype ports are different: you’ll use a Porting Authorization Code (PAC) issued by Skype. The losing carrier/provider’s records are the source of truth for account numbers, PINs, names, and service addresses.

## What you need before you submit
- A Telnyx account set up to receive numbers (and selected service plan).
- Confirm portability for your numbers via Telnyx’s Check Portability or by contacting support.
- Keep your current provider account active until the port completes.
- Gather carrier-level details: underlying carrier, account number, and required PIN/passcode.
- Prepare a signed LOA and recent invoice when required (see regional notes and Vonage).

## Resellers and underlying carriers
If your current provider is a reseller (Aircall, Intercom, RingCentral, Grasshopper, Google Voice for Business, etc.), first ask: “What is the underlying carrier for my numbers, and what account number and PIN do I need to authorize a port?” If they’re unresponsive, contact porting@telnyx.com for help. The losing carrier decides if a PIN is required and its format; Telnyx must submit exactly what their records expect.

## Carrier-specific credentials
### Twilio
- Account Number: Twilio Account SID (AC…).
- PIN: Twilio auth token, or a port‑out passcode if configured (Console > Phone Numbers > Port Out Settings). PIN requirements can vary by account/sub‑account; sub‑accounts may need their own SID/token.

### Aircall
- Most numbers ride on Twilio.
- Account Number and PIN: Provided by Aircall support (not your Aircall login/ID). Ask specifically for the carrier‑level passcode.

### Intercom
- Often Twilio‑backed; varies by region.
- Account Number and PIN: Carrier‑level details provided by Intercom support. If Twilio‑backed, the Account SID and auth token or port‑out passcode typically apply.

### Vonage (incl. Vonage Business)
- Account Number: Found on invoices.
- PIN: Set in the Vonage portal (Account > Security > Port‑Out PIN).
- Note: Vonage requires an LOA attached to the port request.

### RingCentral
- Account Number: In Admin Portal > Account Details.
- PIN: Set in Admin Portal > Phone Numbers > Port Numbers. Set it before you initiate the port.

### Grasshopper
- Account Number: Your Grasshopper account number.
- PIN: Obtain from Grasshopper support (not exposed in the portal). Numbers often ride on Bandwidth or Inteliquent.

## Skype number ports (PAC‑based)
- You must have an active Skype Number (non‑Skype numbers/accounts can’t be ported).
- Request your Porting Authorization Code (PAC) from Skype support and ensure your account is in good standing (no unpaid balances).
- Submit your port request to Telnyx with the Skype Number and PAC, and coordinate your preferred port date. See Telnyx’s Porting Policy & Procedure for submission steps: https://support.telnyx.com/en/articles/1130630-porting-policy-procedure
- Expect a brief service disruption during cutover; keep your Skype account active until completion.
- Skype may charge a port‑out fee; Telnyx does not charge Port‑In fees.
- After completion, test inbound calls with Telnyx, then cancel any unneeded Skype services.

## What to enter in your Telnyx port request
Provide details exactly as they appear on the losing carrier’s records:
- Account Number: Carrier account number (e.g., Twilio SID; the number provided by Aircall/Intercom; your RingCentral/Vonage/Grasshopper account number).
- PIN/Passcode: Carrier‑level PIN (e.g., Twilio auth token or port‑out passcode; Aircall/Intercom carrier passcode; Vonage/RingCentral portal PIN; Grasshopper support‑issued PIN).
- Authorized Name: Exact legal or account name on the carrier record.
- Service Address: Address on file with the carrier (not necessarily billing).
- LOA: Attach when required (e.g., Vonage, some international ports).

## Timelines and expectations
- US/CA simple ports (about 1–5 numbers): typically 3–7 business days from acceptance.
- Complex ports (6+ numbers or mixed rate centers): typically 5–15 business days.
- Skype ports commonly complete within a few days but can take a week or more depending on their processing and region.
- Timelines vary by country, provider responsiveness, and document accuracy.

## Avoiding service disruption
- Don’t cancel your current service until all numbers have ported and tested.
- Gather correct credentials before submitting to avoid multi‑day rejection delays.
- Coordinate a cutover window and inform stakeholders; avoid mission‑critical calls during the FOC window.
- After completion, test inbound/outbound calling and any routing/feature configurations.

## Common rejection reasons and fixes
- PASSCODE_PIN_INVALID: The submitted PIN is wrong. Obtain the carrier‑level PIN from your provider and resubmit.
- ACCOUNT_NUMBER_MISMATCH: The account number doesn’t match carrier records. Reseller IDs often differ from carrier account numbers — confirm with support.
- BUSINESS_NAME_MISMATCH: Authorized name doesn’t match. Use the exact legal or account name on file.
- SERVICE_ADDRESS_MISMATCH: Address doesn’t match. Use the service address on the carrier’s record (not billing/shipping).

## French overseas territories: document requirements
For Local, National, and Toll‑Free numbers in the following territories — French Guiana, Mayotte, Réunion, Saint Barthélemy & Saint Martin — you must provide:
- Signed LOA (international template)
- National address (mandatory)
- Latest invoice from the current provider

Download LOA template: https://assets.ctfassets.net/taysl255dolk/6YYtHkPiDoOfhR8Vp3QxUz/3f7b77cf78ecdebe280c6c0226ac12ea/LoA_-_Telnyx_-_INTL.pdf

## Help and escalation
- Telnyx Support Portal: https://support.telnyx.com
- Email porting@telnyx.com with your port order number for help identifying the underlying carrier, resolving rejections, or escalating unresponsive providers.
