---
source_url: https://support.telnyx.com/en/articles/14708130-porting-numbers-away-from-resellers-aircall-intercom-ringcentral-vonage-etc
scraped: 2026-06-11
---

Porting Numbers Away from Resellers (Aircall, Intercom, RingCentral, Vonage, etc.) | Telnyx Help Center

[Skip to main content](#main-content)

# Porting Numbers Away from Resellers (Aircall, Intercom, RingCentral, Vonage, etc.)

A complete guide to porting numbers from VoIP resellers — what a reseller is, how to find your underlying carrier, and carrier-specific PIN and account requirements.

Written by Patrick Budzinski

April 21, 2026

Table of contents

# What Is a Reseller?

A **reseller** is a company that provides phone numbers to customers but doesn't own the underlying network infrastructure. Instead, they lease numbers from a carrier (like Twilio, Bandwidth, or Inteliquent) and resell them under their own brand.

**Common resellers include:** Aircall, Intercom, RingCentral, Grasshopper, Google Voice for Business, and many VoIP providers.

**Why this matters for porting:** When you port a number away from a reseller, the authorization must come from the **underlying carrier**, not the reseller. The account number and PIN you need are carrier-level credentials — not your login to the reseller's platform.

## How to Find Your Underlying Carrier

Before submitting a port request, contact your current provider and ask:

"I want to port my numbers to another carrier. What is the underlying carrier for my numbers, and what account number and PIN do I need to authorize the port?"

Most providers are required to give you this information. If they're unresponsive or obstructive, this may be a violation of FCC porting rules — contact [porting@telnyx.com](mailto:porting@telnyx.com) and we can help escalate.

## Who Decides If a PIN Is Required?

The **losing carrier** (your current provider) determines whether a PIN is required and what format it takes. Telnyx (as the gaining carrier) submits whatever information you provide. If it doesn't match the losing carrier's records, the order is rejected. **The losing carrier's records are the source of truth.**

## Carrier-Specific Requirements

### Twilio

* **Account Number:** Your Twilio Account SID (found in Twilio Console under Account > General Settings)
* **PIN:** Twilio auth token, OR a port-out passcode if one is set (Console > Phone Numbers > Port Out Settings)
* **Notes:** Twilio PIN requirements vary depending on whether you're on a standard account or a sub-account. For sub-accounts, you may need the sub-account SID and auth token.

### Aircall

* **Account Number:** Provided by Aircall support (not your Aircall account ID)
* **PIN:** Carrier-level passcode from Aircall support
* **Notes:** Most Aircall numbers are on Twilio infrastructure. Contact Aircall support before submitting.

### Intercom

* **Account Number:** Provided by Intercom support (carrier-level, not workspace ID)
* **PIN:** Carrier-level port-out PIN from Intercom support
* **Notes:** Intercom numbers are commonly on Twilio. The underlying carrier can vary by region.

### Vonage (including Vonage Business)

* **Account Number:** Your Vonage account number (found on invoices)
* **PIN:** PIN set in the Vonage portal (Account > Security > Port-Out PIN)
* **Notes:** Vonage requires a Letter of Authorization (LOA). Attach it when submitting.

### RingCentral

* **Account Number:** Your RingCentral account number (Admin Portal > Account Details)
* **PIN:** Port-out PIN set in Admin Portal > Phone Numbers > Port Numbers
* **Notes:** RingCentral requires the PIN to be set *before* initiating a port. Set it first if you haven't.

### Grasshopper

* **Account Number:** Your Grasshopper account number
* **PIN:** Contact Grasshopper support — not exposed in the portal
* **Notes:** Grasshopper numbers typically run on Bandwidth or Inteliquent. Support can tell you which.

## Checklist Before Submitting

* ☐ Confirmed the underlying carrier with your current provider
* ☐ Obtained the correct account number (carrier-level, not reseller login)
* ☐ Obtained the correct PIN/passcode
* ☐ Verified the authorized name matches exactly what's on the carrier account
* ☐ Verified the service address matches the carrier's records
* ☐ LOA signed and ready to upload (if required)

## Common Rejection Reasons

|  |  |  |
| --- | --- | --- |
| Rejection | What It Means | Action |
| PASSCODE\_PIN\_INVALID | Wrong PIN | Contact your provider for the correct carrier-level PIN |
| ACCOUNT\_NUMBER\_MISMATCH | Wrong account number | Reseller account IDs ≠ carrier account numbers — confirm with provider |
| BUSINESS\_NAME\_MISMATCH | Name doesn't match | Get exact legal name from your provider |
| SERVICE\_ADDRESS\_MISMATCH | Address doesn't match | Get the address on file with the carrier, not your billing address |

## Need Help?

Contact [porting@telnyx.com](mailto:porting@telnyx.com) with your port order number and we can help identify the exact rejection cause and guide you through resubmission.

---

Related Articles

[Port numbers away from Telnyx](https://support.telnyx.com/en/articles/2033789-port-numbers-away-from-telnyx)[Porting away from Bandwidth](https://support.telnyx.com/en/articles/3947875-porting-away-from-bandwidth)[Port Out PIN Protection](https://support.telnyx.com/en/articles/8006189-port-out-pin-protection)[Porting Numbers Away from Aircall to Telnyx](https://support.telnyx.com/en/articles/14708128-porting-numbers-away-from-aircall-to-telnyx)[Porting Numbers Away from Intercom to Telnyx](https://support.telnyx.com/en/articles/14708129-porting-numbers-away-from-intercom-to-telnyx)

Did this answer your question?

😞😐😃

Table of contents
