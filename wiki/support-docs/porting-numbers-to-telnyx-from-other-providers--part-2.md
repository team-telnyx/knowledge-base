---
title: Porting Numbers to Telnyx from Other Providers
summary: A comprehensive guide to porting phone numbers into Telnyx from carriers
  and resellers including Skype, Twilio, Bandwidth, Aircall, Intercom, RingCentral,
  Vonage, Grasshopper, Microsoft Teams, and voip.ms — covering required credentials,
  provider-specific steps, common rejection reasons, timelines, and how to get help.
sources:
- url: https://support.telnyx.com/en/articles/10715399-porting-away-from-skype
  content_hash: 0eaa5d64f012e269cfc92c25fabecd79113f27018437f0f68803e3a652c89aeb
- url: https://support.telnyx.com/en/articles/14708128-porting-numbers-away-from-aircall-to-telnyx
  content_hash: 91e6ca312538920f4144699a70403da23949cc0ace16123d772d52b132063541
- url: https://support.telnyx.com/en/articles/14708129-porting-numbers-away-from-intercom-to-telnyx
  content_hash: 583288b2e14ab3314e3b3b44c9a3bcac897212bf6c286018a5ebc7e7fb6eef4f
- url: https://support.telnyx.com/en/articles/14708130-porting-numbers-away-from-resellers-aircall-intercom-ringcentral-vonage-etc
  content_hash: 8a0e6f9aea8d92479f73828c2621674e6d12aa47e7621f74a33ce553624f1a70
- url: https://support.telnyx.com/en/articles/14790558-how-to-find-your-porting-pin-or-passcode
  content_hash: 0a7135f2ec825f2835292daa611265b50e1a34727e6b48a4b769df35ecf80acc
- url: https://support.telnyx.com/en/articles/3947850-porting-away-from-twilio
  content_hash: 207585e88e50a87f9573b4dc0448869b1411062dd99e1e3c2c034e8fabd5dfc7
- url: https://support.telnyx.com/en/articles/3947875-porting-away-from-bandwidth
  content_hash: 4242ae13a95cd35f50b9c7504662d423f899b11ec9f2586a488971fe83b54176
- url: https://support.telnyx.com/en/articles/5104103-port-your-microsoft-ms-teams-numbers
  content_hash: dcfa4ffc1a0f03f15995f08cbd4d812590bca274f64c46eeeb73e5cd36cd2b23
- url: https://support.telnyx.com/en/articles/5595770-port-away-from-voip-ms
  content_hash: 07b7d8ac9dcfd71a76ae92fc494699a0ee884d00f823964f367a5f872f600bf5
- url: https://support.telnyx.com/en/articles/5820338-best-practices-for-contacting-porting
  content_hash: bf80ed8805769d323eefa8a6ab909426503566685966b3fbf288cfe80a5ed87d
updated_at: 2026-06-11T11:12:50Z
---

# Porting Numbers to Telnyx from Other Providers

*Part 2 of 3 — see also: [Part 1](porting-numbers-to-telnyx-from-other-providers--part-1.md), [Part 3](porting-numbers-to-telnyx-from-other-providers--part-3.md)*

A comprehensive guide to porting phone numbers into Telnyx from carriers and resellers including Skype, Twilio, Bandwidth, Aircall, Intercom, RingCentral, Vonage, Grasshopper, Microsoft Teams, and voip.ms — covering required credentials, provider-specific steps, common rejection reasons, timelines, and how to get help.

## Provider-Specific Porting Instructions

### Skype

Only active **Skype Numbers** can be ported; regular Skype accounts or non-Skype numbers are not eligible.

1. **Request a Porting Authorization Code (PAC) from Skype** — Contact Skype customer support to request the PAC code. Ensure your Skype Number is linked to your current account and is in good standing.
2. **Submit your port request to Telnyx** — Include your Skype Number, PAC code, and account information. Coordinate a porting date with Telnyx.
3. **Prepare for potential service disruption** — There may be a brief disruption during the port. Avoid making critical calls during this window.
4. **Wait for completion** — Typically a few days, but can take up to a week or longer depending on Skype's processing.
5. **Confirm and test** — Once ported, test the number with Telnyx. The Skype Number will no longer be associated with your Skype account after porting.

Skype may charge a porting fee; Telnyx does not charge port-in fees.

### Twilio

1. **Request CSR information** — Contact Twilio porting support at [porting@twilio.com](mailto:porting@twilio.com) to request a copy of the CSR (Customer Service Record) information for the numbers you wish to port. This may take time as Twilio needs to confirm with their underlying partners.
2. **Submit your port-in request to Telnyx** — See [Port Numbers to Telnyx](port-numbers-to-telnyx.md) for the submission process.

**Credentials to use:**
- **Account Number:** Your Twilio Account SID (found in Twilio Console under Account > General Settings). For sub-accounts, you may need the sub-account SID.
- **PIN:** Your Twilio auth token, or a dedicated port-out passcode if one is set (Console > Phone Numbers > Port Out Settings in newer accounts). Twilio's PIN requirements vary — if you get a PIN rejection, ask Twilio support specifically for the current port-out passcode or auth token.
- **BTN / Account Number (for toll-free):** Twilio does not use BTNs or account numbers for toll-free. Use any of the numbers being ported as both the BTN and the account number.

**For geographic numbers:** Put your own company information on the Letter of Authorization (LOA) — your business name, address, authorized person's name, and signature.

**For toll-free numbers:** Twilio handles these directly and will usually reach out to confirm the port-out.

**For large ports:** In the LOA's "Numbers to be ported" field, write "Numbers provided in spreadsheet."

### Bandwidth

1. **Request CSR information** — Raise a support ticket with Bandwidth porting support to request the CSR for the numbers you wish to port. If Bandwidth does not leverage their port-out validation API, they typically grant automatic FOC (port approval) without confirming submitted information.
2. **Submit your port-in request to Telnyx.**

**Credentials to use:**
- **BTN / Account Number:** Bandwidth does not use BTNs or account numbers. Use any of the numbers being ported as both the BTN and the account number.
- **LOA:** Put your own company information — business name, address, authorized person's name, signature, and date.

**For large ports:** In the LOA's "Numbers to be ported" field, write "Numbers provided in spreadsheet."

### Aircall

Aircall is a reseller — numbers typically sit on Twilio infrastructure. You must obtain carrier-level credentials, not Aircall login credentials.

1. **Contact Aircall support** and ask for the underlying carrier, the carrier-level account number, and the carrier-level PIN/passcode.
2. **Submit your port request to Telnyx** with the information below.

| Field | What to Enter |
|---|---|
| Account Number | The account number provided by Aircall (not your Aircall account ID) |
| PIN / Passcode | The carrier-level passcode provided by Aircall support |
| Authorized Name | The name on the Aircall account exactly as it appears |
| Service Address | The address on file with Aircall (not your billing address) |

If Aircall is unresponsive, contact [porting@telnyx.com](mailto:porting@telnyx.com) — Telnyx can help identify the underlying carrier.

### Intercom

Intercom is a reseller — numbers are commonly on Twilio. You need carrier-level authorization, not Intercom credentials.

1. **Contact Intercom support** and ask for the underlying carrier, the carrier-level account number, and the carrier-level port-out PIN.
2. **Submit your port request to Telnyx.**

| Field | What to Enter |
|---|---|
| Account Number | Carrier account number provided by Intercom support |
| PIN / Passcode | Carrier-level port-out PIN provided by Intercom support |
| Authorized Name | Exact name on the Intercom carrier account |
| Service Address | Address registered with the underlying carrier |

**If your numbers are on Twilio:** Use the Twilio Account SID (starts with "AC…") as the account number, and the Twilio auth token or dedicated port-out passcode as the PIN. If you get a PIN rejection, ask Intercom support: "What is the current port-out passcode or auth token for my account?"

### RingCentral

- **Account Number:** Your RingCentral account number (Admin Portal > Account Details).
- **PIN:** Port-out PIN set in Admin Portal > Phone Numbers > Port Numbers. **Set this before initiating the port** if you haven't already.

### Vonage (Including Vonage Business)

- **Account Number:** Your Vonage account number (found on invoices).
- **PIN:** PIN set in the Vonage portal (Account > Security > Port-Out PIN).
- **LOA:** Vonage requires a Letter of Authorization — attach it when submitting.

### Grasshopper

- **Account Number:** Your Grasshopper account number.
- **PIN:** Contact Grasshopper support — the PIN is not exposed in the portal.
- Grasshopper numbers typically run on Bandwidth or Inteliquent. Support can confirm which.

### Microsoft MS Teams

1. **Set a porting PIN** in the Microsoft Teams admin center: Voice > Phone numbers > Manage porting PIN > enter a 10-digit PIN.
2. **Submit your port-in request to Telnyx.**

**Credentials to use:**
- **Account Number:** If you don't have one, use one of the numbers being ported as the account number.
- **BTN:** If you don't have one, use one of the numbers being ported as the BTN.
- **PIN:** In the comments section of the port request, add: "PIN is [your 10-digit PIN]" (e.g., "PIN is 1234567890").

Once submitted, the port is usually automatically approved and Telnyx receives FOC immediately. Porting from MS Teams can take as little as 1 business day depending on the underlying provider.

**Microsoft Calling Plan for Teams:** If you want the number assigned to Operator Connect, open a ticket with Telnyx so Telnyx can open one with Microsoft to migrate the number to Operator Connect — otherwise Microsoft will not allow it. Details needed: the ID of the external connection, the numbers to migrate, and whether you want "Calling User Assignment" or "First Party App Assignment."

### voip.ms

voip.ms leverages different providers depending on number type (US, Canada, toll-free, international). Your account information may vary — if you have sub-accounts, each may have different information on file and require individual port requests.

**How to retrieve your information:**
- **Company name and address:** Listed on the top-left of your voip.ms invoice.
- **PIN number:** Located under Main Menu > Account Settings > Security tab. If you haven't enabled a PIN, you don't need to provide one.
- **Account number:** Listed within the portal (not on your invoice). If you haven't set a PIN, an account number is generally not required.
- **Phone numbers:** Available in the portal and on your invoice.

Once you have this information, fill out an LOA and submit your port via the Telnyx portal (Numbers > Port Numbers).
