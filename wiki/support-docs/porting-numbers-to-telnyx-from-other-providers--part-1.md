---
title: Porting Numbers to Telnyx from Other Providers
summary: A comprehensive guide to porting phone numbers into Telnyx from carriers
  and resellers including Skype, Twilio, Bandwidth, Aircall, Intercom, RingCentral,
  Vonage, Grasshopper, Microsoft Teams, and voip.ms — covering required credentials,
  provider-specific steps, common rejection reasons, timelines, and how to get help.
sources:
- url: https://support.telnyx.com/en/articles/10715399-porting-away-from-skype
- url: https://support.telnyx.com/en/articles/14708128-porting-numbers-away-from-aircall-to-telnyx
- url: https://support.telnyx.com/en/articles/14708129-porting-numbers-away-from-intercom-to-telnyx
- url: https://support.telnyx.com/en/articles/14708130-porting-numbers-away-from-resellers-aircall-intercom-ringcentral-vonage-etc
- url: https://support.telnyx.com/en/articles/14790558-how-to-find-your-porting-pin-or-passcode
- url: https://support.telnyx.com/en/articles/3947850-porting-away-from-twilio
- url: https://support.telnyx.com/en/articles/3947875-porting-away-from-bandwidth
- url: https://support.telnyx.com/en/articles/5104103-port-your-microsoft-ms-teams-numbers
- url: https://support.telnyx.com/en/articles/5595770-port-away-from-voip-ms
- url: https://support.telnyx.com/en/articles/5820338-best-practices-for-contacting-porting
updated_at: 2026-06-11T11:12:50Z
---

# Porting Numbers to Telnyx from Other Providers

*Part 1 of 3 — see also: [Part 2](porting-numbers-to-telnyx-from-other-providers--part-2.md), [Part 3](porting-numbers-to-telnyx-from-other-providers--part-3.md)*

A comprehensive guide to porting phone numbers into Telnyx from carriers and resellers including Skype, Twilio, Bandwidth, Aircall, Intercom, RingCentral, Vonage, Grasshopper, Microsoft Teams, and voip.ms — covering required credentials, provider-specific steps, common rejection reasons, timelines, and how to get help.

## Before You Begin

Before initiating any port, confirm the following:

- Your number is eligible for porting (use Telnyx's Check Portability feature or contact support).
- Your Telnyx account is set up and ready to receive the ported number.
- Your current provider account is active and in good standing — do **not** cancel service until the port is fully complete, or the transfer may fail.
- You have gathered the correct credentials from your current provider (account number, PIN/passcode, authorized name, service address).

## Understanding Resellers and Underlying Carriers

A **reseller** provides phone numbers but doesn't own the underlying network infrastructure — they lease numbers from a carrier (such as Twilio, Bandwidth, or Inteliquent) and resell them under their own brand. Common resellers include Aircall, Intercom, RingCentral, Grasshopper, and Google Voice for Business.

When porting away from a reseller, the authorization must come from the **underlying carrier**, not the reseller. The account number and PIN you submit must be carrier-level credentials — not your login to the reseller's platform. Always contact your current provider and ask: "I want to port my numbers to another carrier. What is the underlying carrier for my numbers, and what account number and PIN do I need?"

Most providers are required to give you this information. If they're unresponsive or obstructive, this may violate FCC porting rules — contact [porting@telnyx.com](mailto:porting@telnyx.com) for help escalating.

The **losing carrier** (your current provider) determines whether a PIN is required and what format it takes. Telnyx submits whatever information you provide; if it doesn't match the losing carrier's records, the order is rejected. The losing carrier's records are the source of truth.

## Finding Your Porting PIN or Passcode

A porting PIN is a security code that prevents unauthorized number transfers. It is **not** your carrier account password or login PIN — it's a separate code specifically for number porting. A mismatched PIN is the number-one cause of porting delays, resulting in a `PASSCODE_PIN_INVALID` rejection.

### Major Carrier PIN Retrieval

| Carrier | How to Get Your PIN |
|---|---|
| **AT&T** | Log in at [att.com](https://att.com) → My AT&T → Account profile → Wireless passcode, or call 611 and ask for your "wireless passcode" |
| **Verizon** | Log in at [verizon.com](https://verizon.com) → Account → Security → Account PIN, or call 611 and ask for your "account transfer PIN" |
| **T-Mobile / Metro by T-Mobile** | My T-Mobile → Account → Transfer your number (generates a temporary PIN valid for 7 days — generate it right before submitting) |
| **Spectrum / Charter** | No self-service option — call 1-833-949-0036 and ask for your "number transfer PIN" |
| **Lumen / CenturyLink** | Call 1-800-244-1111 and ask for your "account transfer authorization code" |
| **Bandwidth / Wholesale Carriers** | Contact your account manager or reseller directly |
| **CLEC / Regional Carriers** | Call the carrier's business support line and ask for the PIN or passcode needed to port your number |

**Tips:**
- Some carriers have a default PIN (often the last 4 digits of your account number or phone number).
- Some carriers generate a new PIN each time — don't reuse an old one.
- If your port keeps getting rejected, ask the carrier to verify the PIN they have on file rather than guessing.
