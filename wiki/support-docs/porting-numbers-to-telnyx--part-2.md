---
title: Porting Numbers to Telnyx
summary: A consolidated reference for porting numbers to Telnyx from Skype, Twilio,
  Microsoft Teams, and VoIP resellers (Aircall, Intercom, RingCentral, Vonage, Grasshopper),
  including carrier-specific credentials, common porting errors (TN Not Portable,
  Invalid Reseller, Authorized Name Mismatch), and related voice features such as
  Repeat Call Guard, Branded Calling, and Inbound Call Screening.
sources:
- url: https://support.telnyx.com/en/articles/10715399-porting-away-from-skype
- url: https://support.telnyx.com/en/articles/1130616-number-not-portable-tn-not-portable-error
- url: https://support.telnyx.com/en/articles/1130619-invalid-reseller-error
- url: https://support.telnyx.com/en/articles/1130623-authorized-name-mismatch-error
- url: https://support.telnyx.com/en/articles/12580667-configure-repeat-call-guard-on-outbound-voice-profiles-beta
- url: https://support.telnyx.com/en/articles/14708128-porting-numbers-away-from-aircall-to-telnyx
- url: https://support.telnyx.com/en/articles/14708129-porting-numbers-away-from-intercom-to-telnyx
- url: https://support.telnyx.com/en/articles/14708130-porting-numbers-away-from-resellers-aircall-intercom-ringcentral-vonage-etc
- url: https://support.telnyx.com/en/articles/15138152-making-calls-with-branded-calling
- url: https://support.telnyx.com/en/articles/3947850-porting-away-from-twilio
- url: https://support.telnyx.com/en/articles/5104103-port-your-microsoft-ms-teams-numbers
- url: https://support.telnyx.com/en/articles/8037040-inbound-call-screening
updated_at: 2026-07-17T09:01:08Z
---

# Porting Numbers to Telnyx

*Part 2 of 5 — see also: [Part 1](porting-numbers-to-telnyx--part-1.md), [Part 3](porting-numbers-to-telnyx--part-3.md), [Part 4](porting-numbers-to-telnyx--part-4.md), [Part 5](porting-numbers-to-telnyx--part-5.md)*

A consolidated reference for porting numbers to Telnyx from Skype, Twilio, Microsoft Teams, and VoIP resellers (Aircall, Intercom, RingCentral, Vonage, Grasshopper), including carrier-specific credentials, common porting errors (TN Not Portable, Invalid Reseller, Authorized Name Mismatch), and related voice features such as Repeat Call Guard, Branded Calling, and Inbound Call Screening.

## Porting from VoIP Resellers (Aircall, Intercom, RingCentral, Vonage, etc.)

A reseller is a company that provides phone numbers but does not own the underlying network infrastructure — they lease numbers from a carrier (such as Twilio, Bandwidth, or Inteliquent) and resell them under their own brand. Common resellers include Aircall, Intercom, RingCentral, Grasshopper, and Google Voice for Business.

When porting away from a reseller, authorization must come from the underlying carrier, not the reseller. The account number and PIN you need are carrier-level credentials, not your login to the reseller's platform.

### Finding the Underlying Carrier

Contact your current provider and ask: "I want to port my numbers to another carrier. What is the underlying carrier for my numbers, and what account number and PIN do I need to authorize the port?" Most providers are required to give you this information. If they are unresponsive or obstructive, this may be a violation of FCC porting rules — contact porting@telnyx.com for help escalating.

The losing carrier determines whether a PIN is required and what format it takes. Telnyx submits whatever information you provide; if it does not match the losing carrier's records, the order is rejected. The losing carrier's records are the source of truth.

### Carrier-Specific Requirements

**Twilio**
- Account Number: Twilio Account SID (found in Twilio Console under Account > General Settings)
- PIN: Twilio auth token, or a port-out passcode if one is set (Console > Phone Numbers > Port Out Settings)
- For sub-accounts, you may need the sub-account SID and auth token

**Aircall**
- Account Number: Provided by Aircall support (not your Aircall account ID)
- PIN: Carrier-level passcode from Aircall support
- Most Aircall numbers are on Twilio infrastructure — contact Aircall support before submitting

**Intercom**
- Account Number: Provided by Intercom support (carrier-level, not workspace ID)
- PIN: Carrier-level port-out PIN from Intercom support
- Intercom numbers are commonly on Twilio; the underlying carrier can vary by region

**Vonage (including Vonage Business)**
- Account Number: Vonage account number (found on invoices)
- PIN: PIN set in the Vonage portal (Account > Security > Port-Out PIN)
- Vonage requires a Letter of Authorization (LOA) — attach it when submitting

**RingCentral**
- Account Number: RingCentral account number (Admin Portal > Account Details)
- PIN: Port-out PIN set in Admin Portal > Phone Numbers > Port Numbers
- The PIN must be set before initiating a port

**Grasshopper**
- Account Number: Grasshopper account number
- PIN: Contact Grasshopper support — not exposed in the portal
- Grasshopper numbers typically run on Bandwidth or Inteliquent

### Porting from Aircall Specifically

Contact Aircall support and ask for the underlying carrier (most commonly Twilio), your account number as it appears on their carrier records, and the carrier-level PIN or passcode. The PIN is not your Aircall login password.

In your Telnyx port request, enter:

| Field | What to Enter |
| --- | --- |
| Account Number | The account number provided by Aircall (not your Aircall account ID) |
| PIN / Passcode | The carrier-level PIN provided by Aircall |
| Authorized Name | The name on the Aircall account (exactly as it appears) |
| Service Address | The address on file with Aircall |

Common rejection reasons include `PASSCODE_PIN_INVALID`, `ACCOUNT_NUMBER_MISMATCH`, `BUSINESS_NAME_MISMATCH`, and `SERVICE_ADDRESS_MISMATCH`. Simple ports (1–5 numbers) typically take 3–7 business days; complex ports (6+ numbers or mixed rate centers) take 5–15 business days. Do not cancel Aircall before the port completes.

### Porting from Intercom Specifically

Contact Intercom support and ask for the underlying carrier, your carrier-level account number, and the carrier-level port-out PIN. This information is different from your Intercom login credentials, subscription ID, or workspace ID.

If Intercom tells you your numbers are on Twilio:
- Account Number: Twilio Account SID (starts with "AC...") — found in Twilio Console, or ask Intercom to provide it
- PIN: Twilio auth token or a dedicated port-out passcode (set under Console > Phone Numbers > Port Out Settings in newer Twilio accounts)
- Authorized Name: The legal name on the Twilio/Intercom account

If you get a PIN rejection, ask Intercom support specifically: "What is the current port-out passcode or auth token for my account?" Timelines are 3–7 business days for 1–5 numbers and 5–15 business days for 6+ numbers.

### Pre-Submission Checklist

- Confirmed the underlying carrier with your current provider
- Obtained the correct account number (carrier-level, not reseller login)
- Obtained the correct PIN/passcode
- Verified the authorized name matches exactly what's on the carrier account
- Verified the service address matches the carrier's records
- LOA signed and ready to upload (if required)

## Common Porting Errors

### TN Not Portable Error

The "TN not portable" error is a catch-all for several underlying issues. The losing carrier is intentionally unspecific about the cause. Common reasons include:

- The number is inactive with the losing carrier (no longer assigned or deactivated)
- The number is stuck in a pending state from another recent action
- The number has a special feature associated with it (such as a signal ring)
- The number is on a special rate plan (often bundled with TV, voice, and Internet)
- A recent informational update was made to the account

Call your existing carrier and ask if any numbers on your account may not be portable. If a number is inactive, you will likely need to re-activate it before a port-out can continue.

### Invalid Reseller Error (Canada)

Many customers buy numbers from a telecom reseller, VoIP provider, or managed service provider, which in turn purchases them from the underlying carrier. The end customer's name and service address may not be on file with the underlying carrier.

When submitting a port-out request, Canadian carriers require the reseller's name. If the name does not match exactly what is on file, the port-out request may be rejected. Call your reseller and ask for the exact spelling of their name with the losing carrier — this may or may not match the brand name on your bill or in their marketing materials.

### Authorized Name Mismatch Error

Each account has one or more authorized users — employees or officers allowed to make changes to the account. The authorized user is not always the person who receives the bill. Call the current carrier to confirm the authorized user's name. In some cases, Telnyx may be able to request a CSR on your behalf and determine the authorized user's name.

For retailers, banks, and chains with many locations, the authorized user may be the current or former manager of the individual location, since accounts are often not set up by the corporate parent.
