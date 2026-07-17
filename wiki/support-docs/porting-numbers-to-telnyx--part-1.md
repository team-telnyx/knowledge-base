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

*Part 1 of 5 — see also: [Part 2](porting-numbers-to-telnyx--part-2.md), [Part 3](porting-numbers-to-telnyx--part-3.md), [Part 4](porting-numbers-to-telnyx--part-4.md), [Part 5](porting-numbers-to-telnyx--part-5.md)*

A consolidated reference for porting numbers to Telnyx from Skype, Twilio, Microsoft Teams, and VoIP resellers (Aircall, Intercom, RingCentral, Vonage, Grasshopper), including carrier-specific credentials, common porting errors (TN Not Portable, Invalid Reseller, Authorized Name Mismatch), and related voice features such as Repeat Call Guard, Branded Calling, and Inbound Call Screening.

## Porting Numbers to Telnyx

Telnyx supports porting numbers from a wide range of carriers, VoIP providers, and resellers. The general workflow is to gather the right account credentials from your current provider, submit a port-in request to Telnyx, and wait for the losing carrier to approve and schedule the port. The articles below cover provider-specific instructions, common porting errors, and related voice features.

## Porting from Skype

To port a number from Skype to Telnyx, you must have an active Skype Number — regular Skype accounts and non-Skype numbers cannot be ported. Confirm that your Telnyx account is set up to receive the ported number, and verify portability using Telnyx's Check Portability feature or by contacting Telnyx support.

The porting process has five steps:

1. **Request a Porting Authorization Code (PAC) from Skype.** Contact Skype support and verify that your Skype Number is linked to your account and in good standing.
2. **Submit your porting request to Telnyx.** Fill out the porting form with your Skype Number, PAC code, and account information, and coordinate a porting date with Telnyx.
3. **Prepare for potential service disruption.** There may be a brief outage during the port. Keep your Skype account active and in good standing until the port completes.
4. **Wait for porting to complete.** This typically takes a few days but can take up to a week or longer depending on Skype's processing.
5. **Confirm successful porting.** Test the number on Telnyx, and deactivate your Skype account if you no longer need it.

Skype may charge a fee for porting. Telnyx does not charge port-in fees. See [Porting Policy & Procedure](porting-policy-procedure.md) for the full submission process.

## Porting from Twilio

To port numbers away from Twilio, request a copy of the CSR (Customer Service Record) information from Twilio porting support at porting@twilio.com. Twilio may take time to confirm this with their underlying partners.

Once you have the CSR, submit a port-in request to Telnyx. For large numbers of numbers, write "*Numbers provided in spreadsheet*" in the "Numbers to be ported" field of the LOA.

- **Geographic numbers (e.g., area code 312):** Twilio usually has its own company name on file with underlying providers. Put your own company information on the LOA — business name, address, authorized person's name and signature, and date.
- **Toll-free numbers (800, etc.):** Twilio handles toll-free port-outs directly and usually contacts the user to confirm. Twilio does not use BTNs or account numbers — you can use any of the numbers being ported as both the BTN and the Account Number.

## Porting from Microsoft Teams

To port VoIP, Google Voice, or Skype numbers to Telnyx, submit a port request.

1. In the Microsoft Teams admin center, go to **Voice** > **Phone numbers**, select **Manage porting PIN** in the upper-right corner, and enter a 10-digit PIN.
2. Submit a port-in request to Telnyx. If you do not have an account number or BTN, use one of the numbers you are porting as the account number.
3. In the comments section of the port-in request, add: `PIN is [10-digit PIN]` (for example, `PIN is 1234567890`).

Once submitted with the PIN, the port is usually auto-approved and FOC is received immediately. Porting can take as little as one business day depending on the underlying provider.

For numbers being ported from Microsoft's Calling Plan for Teams, if the customer wants the number assigned to Operator Connect, they should open a ticket with Telnyx so Telnyx can open one with Microsoft. Microsoft will not allow the number to be added to Operator Connect otherwise. Required details include the ID of the external connection, the numbers to migrate, and whether the assignment should be "Calling User Assignment" or "First Party App Assignment."
