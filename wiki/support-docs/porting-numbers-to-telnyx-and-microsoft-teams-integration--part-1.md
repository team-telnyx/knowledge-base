---
title: Porting Numbers to Telnyx and Microsoft Teams Integration
summary: This page covers how to find a porting PIN or passcode from common carriers,
  port numbers away from specific providers (Twilio, voip.ms, Microsoft Teams) into
  Telnyx, and configure Microsoft Teams with Telnyx using Direct Routing, Operator
  Connect, or Call2Teams, including emergency call routing.
sources:
- url: https://support.telnyx.com/en/articles/14790558-how-to-find-your-porting-pin-or-passcode
- url: https://support.telnyx.com/en/articles/3947850-porting-away-from-twilio
- url: https://support.telnyx.com/en/articles/5104103-port-your-microsoft-ms-teams-numbers
- url: https://support.telnyx.com/en/articles/5253876-configuring-telnyx-with-microsoft-teams-direct-routing
- url: https://support.telnyx.com/en/articles/5595770-port-away-from-voip-ms
- url: https://support.telnyx.com/en/articles/6133589-ms-teams-call2teams-telnyx
- url: https://support.telnyx.com/en/articles/7048813-tls-sip-warnings-for-teams
- url: https://support.telnyx.com/en/articles/7260976-operator-connect-guide-microsoft-teams
- url: https://support.telnyx.com/en/articles/9718403-microsoft-teams-emergency-call-routing
updated_at: 2026-08-05T13:34:20Z
---

# Porting Numbers to Telnyx and Microsoft Teams Integration

*Part 1 of 6 — see also: [Part 2](porting-numbers-to-telnyx-and-microsoft-teams-integration--part-2.md), [Part 3](porting-numbers-to-telnyx-and-microsoft-teams-integration--part-3.md), [Part 4](porting-numbers-to-telnyx-and-microsoft-teams-integration--part-4.md), [Part 5](porting-numbers-to-telnyx-and-microsoft-teams-integration--part-5.md), [Part 6](porting-numbers-to-telnyx-and-microsoft-teams-integration--part-6.md)*

This page covers how to find a porting PIN or passcode from common carriers, port numbers away from specific providers (Twilio, voip.ms, Microsoft Teams) into Telnyx, and configure Microsoft Teams with Telnyx using Direct Routing, Operator Connect, or Call2Teams, including emergency call routing.

## Porting PINs and Passcodes

When porting a number to Telnyx, your current carrier may require a PIN, passcode, or transfer code to authorize the move. This is a security feature that prevents unauthorized number transfers. **This is not your carrier account password or login PIN** — it is a separate code specifically for number porting.

If the PIN does not match your carrier's records, the port will be rejected with `PASSCODE_PIN_INVALID`. This is the most common cause of porting delays, but it is always fixable.

### How to Get Your PIN by Carrier

- **AT&T** — Log in at [att.com](https://att.com) → My AT&T → Account profile → Wireless passcode, or call 611 and ask for your "wireless passcode."
- **Verizon** — Log in at [verizon.com](https://verizon.com) → Account → Security → Account PIN, or call 611 and ask for your "account transfer PIN."
- **T-Mobile / Metro by T-Mobile** — T-Mobile generates a temporary transfer PIN: My T-Mobile → Account → Transfer your number. The PIN is valid for 7 days, so generate it right before submitting your port request.
- **Spectrum / Charter** — No self-service option. Call 1-833-949-0036 and ask for your "number transfer PIN."
- **Lumen / CenturyLink** — Call 1-800-244-1111 and ask for your "account transfer authorization code."
- **Bandwidth / Wholesale Carriers** — Contact your account manager or reseller directly.
- **CLEC / Regional Carriers** — Call the carrier's business support line and ask: "What is the PIN or passcode needed to port my number to a new carrier?"

### Tips

- Your carrier may have a default PIN (often the last 4 digits of your account number or phone number).
- Some carriers generate a new PIN each time — do not use an old one.
- If your port keeps getting rejected, ask the carrier to verify what PIN they have on file rather than guessing.

If you are still having issues, contact the Telnyx porting team at [porting@telnyx.com](mailto:porting@telnyx.com) with the PIN you are using and your carrier's name. See also [Porting Error Messages](porting-error-messages.md) and [Port Out PIN Protection](port-out-pin-protection.md).

## Porting Away from Twilio

To port numbers away from Twilio, you must first obtain CSR (Customer Service Record) information.

1. Reach out to Twilio porting support at [porting@twilio.com](mailto:porting@twilio.com) to request a copy of the CSR information for the numbers on your account. This may take time, as Twilio must reach out to its underlying partners to confirm the information.
2. Once you receive the CSR information, submit your port-in request to Telnyx. See [Port numbers to Telnyx](port-numbers-to-telnyx.md) for instructions.

If you are porting a large amount of numbers into Telnyx, when filling out the LOA, state "*Numbers provided in spreadsheet*" in the **Numbers to be ported** field.

### Geographic Numbers (Area codes 312, etc.)

Twilio mostly has its own company name on file with its underlying providers. Put your own company information on the LOA, including your business name, address, authorized person's name and signature, and the date. The CSR info can be used to submit to different providers.

### Toll-Free Numbers (800, etc.)

Twilio handles toll-free port-out requests directly. When they receive a port-out request, they will usually reach out to their user confirming the port-out. Twilio does not leverage BTNs (billing telephone numbers) or account numbers — you can use any of the numbers you are porting away from Twilio as the BTN and as the account number.

## Porting Away from voip.ms

voip.ms is a service provider that leverages different providers depending on the type of phone number (US, Canada, toll-free, or international). Porting away from voip.ms is straightforward once you have the correct information.

### Account Information

Your account information may vary depending on your voip.ms setup. Your account may have numbers under a single account's details, or if you have sub-accounts, each number or set of numbers may have different information on file. If you do not have sub-accounts, you only need to use your own business information to port the phone numbers out. If you do leverage sub-accounts, you may need to submit individual ports for each sub-account.

### How to Retrieve This Information

- **Company name and address** — Listed on the top-left of your voip.ms invoice.
- **PIN Number** — If you have set up a PIN number in your voip.ms account, you will need it to port your numbers away. This is located under "Main Menu" → "Account Settings" → "Security" tab. If you have not enabled this, you do not need to provide a PIN number when porting into Telnyx.
- **Account number** — Not listed on your invoice. It should be listed within the portal. However, if you have not implemented a PIN number on your account, an account number is generally not required to port away from voip.ms.
- **Phone numbers** — Find a list of phone numbers via the voip.ms portal and on your invoice.

Once you have retrieved this information, fill out a Letter of Authorization with Telnyx. See [How to Fill Out an LOA](how-to-fill-out-an-loa.md) for details.

### Submitting Your Port to Telnyx

Submit your port to Telnyx via Numbers > Port Numbers, or use the [port request page](https://portal.telnyx.com/#/app/numbers/port-numbers-react/new).

### Time to Port

| Type | Average time to port | Possible expedite time to port | Expedite Fee |
| --- | --- | --- | --- |
| Canadian | 3 days | Same day (if submitted in the morning) | $150 expedite fee per order |
| US | As little as 6 hours | As little as 6 business hours | No charge |
| Toll-free | 1–2 days | Same day | No charge |

To request an expedite, submit your port request and open a live chat with the porting team. Live chat is located in the bottom-right corner of your screen when logged into your Telnyx account.

**Important:** Expedites cannot guarantee same-day porting. The losing carrier may prevent it. Ensure that all information submitted in the port request is accurate — rejections will cause delays, and the expedite fee still applies even if same-day porting cannot be provided.
