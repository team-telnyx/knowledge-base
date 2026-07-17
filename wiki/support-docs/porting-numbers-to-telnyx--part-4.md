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

*Part 4 of 5 — see also: [Part 1](porting-numbers-to-telnyx--part-1.md), [Part 2](porting-numbers-to-telnyx--part-2.md), [Part 3](porting-numbers-to-telnyx--part-3.md), [Part 5](porting-numbers-to-telnyx--part-5.md)*

A consolidated reference for porting numbers to Telnyx from Skype, Twilio, Microsoft Teams, and VoIP resellers (Aircall, Intercom, RingCentral, Vonage, Grasshopper), including carrier-specific credentials, common porting errors (TN Not Portable, Invalid Reseller, Authorized Name Mismatch), and related voice features such as Repeat Call Guard, Branded Calling, and Inbound Call Screening.

## Branded Calling

Branded Calling helps recipients recognize your outbound SIP trunking calls by showing approved brand information — such as your business name, and where supported, a logo or call reason — on eligible receiving devices and networks.

**Important:** Branded Calling currently applies to US-to-US calls placed to US mobile numbers serviced by T-Mobile and Verizon only. It is a verified feature: your brand details and phone numbers must be reviewed before they can be used, and display is not guaranteed on every call.

### How It Works

When you place an outbound call through your Telnyx SIP connection from an approved number, Telnyx attaches verified identity information to the call signaling before routing it to the destination network. This identity information is delivered using industry-standard protocols built on top of STIR/SHAKEN.

STIR/SHAKEN is the regulatory framework for call authentication in the United States, using digital certificates and cryptographic signatures to verify that the calling party is authorized to use the originating phone number. Telnyx signs calls according to STIR/SHAKEN attestation levels (A, B, or C) based on the verified relationship between the caller and the calling number.

Branded Calling extends this foundation by adding additional identity fields beyond standard STIR/SHAKEN:

- **Display name:** your verified business name shown to the called party
- **Call reason:** a brief description of why the call is being placed (e.g., "Account notification" or "Delivery update")
- **Logo:** a verified brand logo rendered on supported devices
- **Business identifiers:** additional verification metadata that downstream carriers and devices can use to validate the caller's identity

### Why Branded Calling May Not Appear on Every Call

Even when your Display Identity Record (DIR) is approved, your numbers are active, and your call signaling is fully RFC-compliant, the branded information may not reach the recipient's screen:

1. **Receiving carrier support varies.** Not all carriers have implemented the infrastructure to consume and render Branded Calling identity fields. Unsupported carriers ignore the fields and route the call normally.
2. **Device support varies.** Older devices, unsupported operating systems, or alternative dialer apps may not display branded content.
3. **Network path differences.** Some paths may pass through intermediate carriers that strip or do not forward the additional identity fields.
4. **Provisioning and propagation delays.** After approval, your branded identity must be provisioned and propagated across carrier databases.
5. **Destination and carrier limitations.** Branded Calling currently applies to US-to-US calls placed to US mobile numbers serviced by Verizon and T-Mobile only.

Approval means your brand and numbers are eligible to send verified identity information — it does not guarantee that every carrier, device, or network path will present it.

### Setup

1. Sign in to Mission Control Portal with a user that has permission to manage Enterprises and phone numbers.
2. Go to **Other Products → Branded Calling**.
3. Accept the Branded Calling terms.
4. Create or select an Enterprise profile, entering business information, contact details, and address.
5. Create a Display Identity Record (DIR) under the Enterprise.
6. Enter your branded calling identity details: display name, logo or logo URL, call reason options, business certifications or attestations, brand contact information, and any supporting details.
7. Submit the DIR for review.
8. Wait for status updates in Mission Control Portal. If rejected, review comments and update before resubmitting.
9. After approval, add the Telnyx phone numbers you use for outbound SIP trunking calls. Wait for the phone number status to show approved or active.
10. Place outbound calls through your SIP connection as normal. No additional SIP headers or configuration changes are required.

### Troubleshooting

**Brand is approved but not showing on calls:** Check that the DIR is approved, the calling number is added to the approved DIR, the phone number status is approved or active, you are placing the outbound call from the approved number through your SIP connection, and enough time has passed for provisioning and downstream propagation.

**Cannot add a phone number:** Confirm the DIR is approved, the number belongs to your Telnyx account, the number is active and eligible, the number is not already assigned to another DIR, and you entered the number exactly as requested.

**DIR was rejected or marked unsuccessful:** Common causes include incomplete business information, display names that do not match the verified business, unsupported or mismatched logos, missing contact details, or unverifiable brand information.

**Branded Calling works for some recipients but not others:** This is expected. Presentation depends on the receiving carrier, device, and network path.

### FAQ

- **Does Branded Calling guarantee my business name or logo will appear on every call?** No. Whether the information is displayed depends on the receiving carrier's infrastructure, the recipient's device, and the network path.
- **Can I use any Telnyx number?** Only eligible, verified Telnyx numbers that belong to your account can be used.
- **Can one phone number be assigned to multiple branded identities?** No. A phone number can only be associated with one approved DIR at a time.
- **Can I change my display name or logo after approval?** Yes, you can edit certain details. Changes to display name, logo, or call reasons may require another review.
- **Do I need to change my SIP connection configuration?** No. Branded Calling is applied automatically based on the approved DIR and number association.
