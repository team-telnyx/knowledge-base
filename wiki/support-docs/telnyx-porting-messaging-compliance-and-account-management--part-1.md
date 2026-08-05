---
title: Telnyx Porting, Messaging Compliance, and Account Management
summary: This page consolidates Telnyx guidance on porting numbers from Skype and
  VoIP resellers, resolving Canadian reseller porting errors, cancelling accounts,
  configuring Skype for Business SIP trunks, toll-free messaging verification and
  opt-in workflows, SMS opt-out keywords, WhatsApp conversation windows, and handling
  toll-free carrier rejections.
sources:
- url: https://support.telnyx.com/en/articles/10715399-porting-away-from-skype
- url: https://support.telnyx.com/en/articles/1130619-invalid-reseller-error
- url: https://support.telnyx.com/en/articles/1130689-how-do-i-cancel-my-account
- url: https://support.telnyx.com/en/articles/1130698-skype-set-up-skype-for-biz-sip-trunk
- url: https://support.telnyx.com/en/articles/11898569-toll-free-opt-in-workflow-description
- url: https://support.telnyx.com/en/articles/1270091-sms-opt-out-keywords-and-stop-words
- url: https://support.telnyx.com/en/articles/13986482-whatsapp-24-hour-conversation-window
- url: https://support.telnyx.com/en/articles/14708130-porting-numbers-away-from-resellers-aircall-intercom-ringcentral-vonage-etc
- url: https://support.telnyx.com/en/articles/15138019-toll-free-carrier-rejections
- url: https://support.telnyx.com/en/articles/5353868-toll-free-messaging
- url: https://support.telnyx.com/en/articles/6989758-toll-free-opt-out-words
updated_at: 2026-08-05T13:26:16Z
---

# Telnyx Porting, Messaging Compliance, and Account Management

*Part 1 of 5 — see also: [Part 2](telnyx-porting-messaging-compliance-and-account-management--part-2.md), [Part 3](telnyx-porting-messaging-compliance-and-account-management--part-3.md), [Part 4](telnyx-porting-messaging-compliance-and-account-management--part-4.md), [Part 5](telnyx-porting-messaging-compliance-and-account-management--part-5.md)*

This page consolidates Telnyx guidance on porting numbers from Skype and VoIP resellers, resolving Canadian reseller porting errors, cancelling accounts, configuring Skype for Business SIP trunks, toll-free messaging verification and opt-in workflows, SMS opt-out keywords, WhatsApp conversation windows, and handling toll-free carrier rejections.

## Porting a Number from Skype to Telnyx

To port a phone number from Skype to Telnyx, you must have an active Skype Number — regular Skype accounts or non-Skype numbers cannot be ported. Before starting, confirm that your Telnyx account is set up to receive the ported number and verify that your Skype Number is eligible for porting using Telnyx's Check Portability feature or by contacting Telnyx support.

The porting process follows these steps:

1. **Request a Porting Authorization Code (PAC) from Skype.** Contact Skype customer support to request the PAC. Make sure your Skype Number is linked to your current account and is in good standing with no unpaid balances.
2. **Submit your porting request to Telnyx.** Fill out the port request form with your Skype Number, PAC code, and account information, then coordinate with Telnyx on a porting date. The process usually takes a few days but can vary by region and provider.
3. **Prepare for potential service disruption.** A brief disruption in service is possible during the porting window. Inform your contacts about the timeline and avoid making critical calls during this period. Keep your Skype account active and in good standing — any account issues such as pending payments will delay or disrupt the port.
4. **Wait for porting to complete.** Porting typically takes a few days but can take up to a week or longer depending on Skype's processing time. Skype and Telnyx will both send notifications about progress.
5. **Confirm successful porting.** Once Telnyx notifies you that the port is complete, test the number to confirm it is active and receiving calls. After porting, the Skype Number will no longer be associated with your Skype account; deactivate the Skype account or cancel associated services if no longer needed.

Key considerations:

- Skype may charge a fee for porting. Telnyx does not charge port-in fees.
- Only Skype Numbers can be ported to Telnyx.
- Keep your Skype account active until porting is finalized; suspension or cancellation before completion may cause the transfer to fail.

For assistance, contact the Telnyx Support Portal or customer service team.

## Porting Numbers Away from VoIP Resellers

A reseller is a company that provides phone numbers to customers without owning the underlying network infrastructure. Resellers lease numbers from carriers such as Twilio, Bandwidth, or Inteliquent and resell them under their own brand. Common resellers include Aircall, Intercom, RingCentral, Grasshopper, and Google Voice for Business.

When porting a number away from a reseller, the authorization must come from the underlying carrier, not the reseller. The account number and PIN required are carrier-level credentials, not your login to the reseller's platform.

### Finding the Underlying Carrier

Before submitting a port request, contact your current provider and ask: "I want to port my numbers to another carrier. What is the underlying carrier for my numbers, and what account number and PIN do I need to authorize the port?" Most providers are required to provide this information. If a provider is unresponsive or obstructive, this may violate FCC porting rules — contact porting@telnyx.com for help escalating.

### PIN Requirements

The losing carrier determines whether a PIN is required and what format it takes. Telnyx submits whatever information you provide; if it does not match the losing carrier's records, the order is rejected. The losing carrier's records are the source of truth.

### Carrier-Specific Requirements

- **Twilio** — Account Number: Twilio Account SID (found in Twilio Console under Account > General Settings). PIN: Twilio auth token, or a port-out passcode if one is set (Console > Phone Numbers > Port Out Settings). PIN requirements vary for standard accounts versus sub-accounts; sub-accounts may need the sub-account SID and auth token.
- **Aircall** — Account Number: provided by Aircall support (not your Aircall account ID). PIN: carrier-level passcode from Aircall support. Most Aircall numbers run on Twilio infrastructure; contact Aircall support before submitting.
- **Intercom** — Account Number: provided by Intercom support (carrier-level, not workspace ID). PIN: carrier-level port-out PIN from Intercom support. Intercom numbers are commonly on Twilio, though the underlying carrier can vary by region.
- **Vonage (including Vonage Business)** — Account Number: your Vonage account number (found on invoices). PIN: PIN set in the Vonage portal (Account > Security > Port-Out PIN). Vonage requires a Letter of Authorization (LOA); attach it when submitting.
- **RingCentral** — Account Number: your RingCentral account number (Admin Portal > Account Details). PIN: port-out PIN set in Admin Portal > Phone Numbers > Port Numbers. The PIN must be set before initiating a port.
- **Grasshopper** — Account Number: your Grasshopper account number. PIN: contact Grasshopper support — not exposed in the portal. Grasshopper numbers typically run on Bandwidth or Inteliquent; support can confirm which.

### Pre-Submission Checklist

- Confirmed the underlying carrier with your current provider
- Obtained the correct account number (carrier-level, not reseller login)
- Obtained the correct PIN/passcode
- Verified the authorized name matches exactly what is on the carrier account
- Verified the service address matches the carrier's records
- LOA signed and ready to upload (if required)

### Common Rejection Reasons

- `PASSCODE_PIN_INVALID` — Wrong PIN. Contact your provider for the correct carrier-level PIN.
- `ACCOUNT_NUMBER_MISMATCH` — Wrong account number. Reseller account IDs are not the same as carrier account numbers; confirm with provider.
- `BUSINESS_NAME_MISMATCH` — Name does not match. Get the exact legal name from your provider.
- `SERVICE_ADDRESS_MISMATCH` — Address does not match. Get the address on file with the carrier, not your billing address.

For help identifying the exact rejection cause and resubmission guidance, contact porting@telnyx.com with your port order number.

## Resolving Canadian Reseller Porting Errors

When porting Canadian telephone numbers, many customers buy their numbers from a telecom reseller, VoIP provider, or managed service provider. The end customer's name and service address may not be on file with the underlying carrier. Canadian carriers require the reseller's name on port-out requests, and if the name does not match exactly what is on file, the request may be rejected.

The reseller name submitted to the current carrier must match exactly with what is on file. The best way to obtain this information is to call your reseller and ask for the exact spelling of their name with the losing carrier. This may or may not match the brand name used on their bill, invoice, or marketing materials.

## Cancelling a Telnyx Account

To remove a member from your organization, use the Organization and Members section in the Telnyx portal.

To cancel your own account, email support@telnyx.com with the Security Passphrase for the account.

### What Is the Security Passphrase?

A security passphrase is a sequence of words or other text used to control access to a system, program, or data. It functions similarly to a password but is generally longer and composed of multiple words, making it both more secure and easier to remember.

### Where Is the Security Passphrase?

The Security Passphrase is not the account password used to log in. It can be found in the Account Security section of the portal.

These actions can only be approved from the email address of the account owner.

### Re-enabling a Cancelled Account

To un-cancel or re-enable a cancelled account, email support@telnyx.com from the email address you would like to activate again. If you are the organisation owner of a sub-member who has been cancelled, provide their email address.
