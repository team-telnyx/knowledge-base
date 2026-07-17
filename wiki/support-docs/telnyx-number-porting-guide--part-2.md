---
title: Telnyx Number Porting Guide
summary: A comprehensive guide to porting telephone numbers to and from Telnyx, covering
  port-in best practices, FastPort® activation, common porting error messages, BTN/ATN
  mismatch resolution, porting PINs and passcodes, port-out notifications and tracking,
  Port Out PIN Protection, bundle pricing and pre-configuration, and best practices
  for contacting Telnyx support and the porting team.
sources:
- url: https://support.telnyx.com/en/articles/1130610-btn-or-atn-mismatch-error
- url: https://support.telnyx.com/en/articles/14790558-how-to-find-your-porting-pin-or-passcode
- url: https://support.telnyx.com/en/articles/1618776-porting-error-messages
- url: https://support.telnyx.com/en/articles/2021334-your-guide-to-fastport
- url: https://support.telnyx.com/en/articles/2030667-i-received-a-port-out-notification
- url: https://support.telnyx.com/en/articles/2030770-port-in-best-practices
- url: https://support.telnyx.com/en/articles/2042977-porting-in-day-of-port-foc
- url: https://support.telnyx.com/en/articles/2054704-fastport-faqs
- url: https://support.telnyx.com/en/articles/2906030-port-out-tracking
- url: https://support.telnyx.com/en/articles/3561993-using-telnyx-fastport
- url: https://support.telnyx.com/en/articles/5170721-best-practices-for-contacting-support
- url: https://support.telnyx.com/en/articles/5820338-best-practices-for-contacting-porting
- url: https://support.telnyx.com/en/articles/8006189-port-out-pin-protection
- url: https://support.telnyx.com/en/articles/8340760-bundles-bundle-pricing
- url: https://support.telnyx.com/en/articles/8709331-porting-bundles
updated_at: 2026-07-17T09:02:30Z
---

# Telnyx Number Porting Guide

*Part 2 of 4 — see also: [Part 1](telnyx-number-porting-guide--part-1.md), [Part 3](telnyx-number-porting-guide--part-3.md), [Part 4](telnyx-number-porting-guide--part-4.md)*

A comprehensive guide to porting telephone numbers to and from Telnyx, covering port-in best practices, FastPort® activation, common porting error messages, BTN/ATN mismatch resolution, porting PINs and passcodes, port-out notifications and tracking, Port Out PIN Protection, bundle pricing and pre-configuration, and best practices for contacting Telnyx support and the porting team.

## Porting Error Messages

A wide range of error conditions may occur during the porting process. Common errors include:

- **ACCOUNT_NUMBER_MISMATCH:** The account number provided did not match what the losing carrier has on file. For some carriers, the account number may be the same as the Billing Telephone Number (BTN).
- **ACCOUNT_NUMBER_REQUIRED:** The account number was not provided but is required.
- **AUTH_NAME_MISMATCH:** The authorized user name provided did not match what the losing carrier has on file. Names must match exactly.
- **BTN_ATN_MISMATCH:** The Billing Telephone Number (BTN) or Account Telephone Number (ATN) did not match what the losing carrier has on file. The BTN or ATN is rarely found on the invoice and may be one of the phone numbers on the account.
- **BUSINESS_NAME_MISMATCH:** The business name or end user name provided did not match what the losing carrier has on file.
- **DIFFERENT_ACCOUNTS:** One or more phone numbers in the port request were part of separate accounts. Carriers only allow port requests for a single account at a time.
- **DIFFERENT_RATE_CENTERS:** One or more phone numbers were in different rate centers. Some carriers require port requests to be split by rate center. This is typically corrected by Telnyx's porting team without customer assistance.
- **FOC_REJECTED:** The FOC date requested was not accepted by the losing carrier.
- **ILLEGIBLE_LOA:** The LOA provided was illegible or unreadable.
- **INVALID_RESELLER:** For Canadian number porting, the reseller specified did not match what the losing carrier has on file.
- **LOSING_CARRIER_NO_RESPONSE:** The losing carrier did not respond to the port-out request. Typically corrected by Telnyx's porting team without customer assistance.
- **OTHER:** An unspecified error condition occurred when validating the port-out information.
- **PASSCODE_PIN_INVALID:** The passcode or PIN provided did not match what the losing carrier has on file.
- **PENDING_ORDER:** One or more phone numbers are already in the process of being ported out or have another pending service change.
- **PORTING_MAIN_BTN:** The port request was specified as a partial port out, but one of the phone numbers is the Billing Telephone Number (BTN), which would leave stranded numbers on the account.
- **REQUEST_INCORRECT:** The port request was incorrectly specified as a partial or full port out.
- **SERVICE_ADDRESS_MISMATCH:** The service address did not match what the losing carrier has on file.
- **TN_HAS_SPECIAL_FEATURE:** One of the phone numbers has a special feature (such as a DSL line or special bundled pricing) that must be removed before the number can be ported.
- **TN_MISMATCH:** One of the phone numbers in the port request is not on the specified account.
- **TN_NOT_PORTABLE:** One of the phone numbers is not portable.
- **UNSUPPORTED_RATE_CENTER:** Telnyx cannot port one of the phone numbers because the rate center is not supported, typically with rural rate centers where the incumbent carrier has a monopoly.
- **ZIP_POSTAL_CODE_MISMATCH:** The zip or postal code did not match what the losing carrier has on file.

## BTN or ATN Mismatch Error

Carriers require that a single telephone number be designated as the primary number for the account, typically referred to as the Billing Telephone Number (BTN) or Account Telephone Number (ATN). Accounts with multiple BTNs/ATNs are common. When submitting a port request, the existing carrier may require Telnyx to provide the BTN or ATN to validate the port request. A BTN/ATN mismatch error occurs when the number submitted does not match what the carrier has on the Customer Service Record (CSR). The BTN is typically not found on a bill copy (except in wireless or toll-free porting).

For large port requests, some telephone numbers may belong to a different account with a different BTN/ATN. The carrier is unlikely to specify which numbers belong to another account.

### Next Steps for BTN/ATN Errors

Check whether the BTN/ATN is specified at the top of the most recent carrier bill or invoice. If the numbers are serviced by a reseller, the BTN/ATN listed may differ from what the underlying carrier has on file in the CSR. If not found on the bill or invoice, contact the carrier directly to request a CSR.

### Special Note for Resellers

When an end customer purchased service through a reseller, mismatched BTNs can occur because the end customer submits the reseller's phone number as their own BTN. When a losing reseller is involved, the number might belong to the reseller rather than the end customer. The customer may use their own BTN and service address instead of the reseller's.

## Porting PIN or Passcode

When porting a number to Telnyx, the current carrier may require a PIN, passcode, or transfer code to authorize the move. This is a security feature that prevents unauthorized number transfers. This is not the carrier account password or login PIN; it is a separate code specifically for number porting.

If the PIN does not match the carrier's records, the port will be rejected with `PASSCODE_PIN_INVALID`. This is the most common cause of porting delays but is always fixable.

### How to Get Your PIN by Carrier

- **AT&T:** Log in at att.com → My AT&T → Account profile → Wireless passcode, or call 611 and ask for the "wireless passcode."
- **Verizon:** Log in at verizon.com → Account → Security → Account PIN, or call 611 and ask for the "account transfer PIN."
- **T-Mobile / Metro by T-Mobile:** T-Mobile generates a temporary transfer PIN via My T-Mobile → Account → Transfer your number. The PIN is valid for 7 days, so generate it right before submitting the port request.
- **Spectrum / Charter:** No self-service option. Call 1-833-949-0036 and ask for the "number transfer PIN."
- **Lumen / CenturyLink:** Call 1-800-244-1111 and ask for the "account transfer authorization code."
- **Bandwidth / Wholesale Carriers:** Contact the account manager or reseller directly.
- **CLEC / Regional Carriers:** Call the carrier's business support line and ask: "What is the PIN or passcode needed to port my number to a new carrier?"

### Tips

- Carriers may have a default PIN (often the last 4 digits of the account number or phone number).
- Some carriers generate a new PIN each time; do not use an old one.
- If the port keeps getting rejected, ask the carrier to verify what PIN they have on file rather than guessing.

## Port-Out Notifications

When a carrier receives a port-in request, they send the current carrier a port-out notification to indicate that they wish to port out a number, usually with the end user's authorization. Telnyx automatically creates a Port-Out request and sends a notification via email or webhook depending on notification settings. By default, email notifications go to the main account owner's email address.

Respond to the port-out notification within 24 to 48 hours via email. If the numbers should not be ported out, notify Telnyx as soon as possible to prevent the port-out from being processed. Service providers and resellers should verify whether the end user has submitted a port request with a new carrier and ensure port-out requests are actioned and responded to correctly.

To decline a port-out, respond to the notification by rejecting the request and providing a valid reason. Numbers will not be ported out provided the request is declined within the timeframe given with a valid reason.
