---
title: Telnyx Number Porting Guide
summary: A consolidated reference for porting phone numbers to and from Telnyx, covering
  best practices, FastPort® activation, port request statuses, common error messages,
  SMS porting behavior, Port Out PIN protection, bundle pre-configuration, and how
  to contact the Porting team.
sources:
- url: https://support.telnyx.com/en/articles/1130610-btn-or-atn-mismatch-error
- url: https://support.telnyx.com/en/articles/1130623-authorized-name-mismatch-error
- url: https://support.telnyx.com/en/articles/1618776-porting-error-messages
- url: https://support.telnyx.com/en/articles/2021334-your-guide-to-fastport
- url: https://support.telnyx.com/en/articles/2030770-port-in-best-practices
- url: https://support.telnyx.com/en/articles/2042977-porting-in-day-of-port-foc
- url: https://support.telnyx.com/en/articles/2054704-fastport-faqs
- url: https://support.telnyx.com/en/articles/3284588-port-request-statuses
- url: https://support.telnyx.com/en/articles/3561993-using-telnyx-fastport
- url: https://support.telnyx.com/en/articles/5170721-best-practices-for-contacting-support
- url: https://support.telnyx.com/en/articles/5820338-best-practices-for-contacting-porting
- url: https://support.telnyx.com/en/articles/7183887-sms-for-ported-in-phone-numbers
- url: https://support.telnyx.com/en/articles/8006189-port-out-pin-protection
- url: https://support.telnyx.com/en/articles/8340760-bundles-bundle-pricing
- url: https://support.telnyx.com/en/articles/8709331-porting-bundles
updated_at: 2026-08-05T13:27:12Z
---

# Telnyx Number Porting Guide

*Part 2 of 5 — see also: [Part 1](telnyx-number-porting-guide--part-1.md), [Part 3](telnyx-number-porting-guide--part-3.md), [Part 4](telnyx-number-porting-guide--part-4.md), [Part 5](telnyx-number-porting-guide--part-5.md)*

A consolidated reference for porting phone numbers to and from Telnyx, covering best practices, FastPort® activation, port request statuses, common error messages, SMS porting behavior, Port Out PIN protection, bundle pre-configuration, and how to contact the Porting team.

## Porting Error Messages

A wide range of error conditions can occur during porting. The most common include:

- **ACCOUNT_NUMBER_MISMATCH:** The account number provided did not match what the losing carrier has on file. For some carriers, the account number may be the same as the Billing Telephone Number (BTN).
- **ACCOUNT_NUMBER_REQUIRED:** The account number was not provided but is required.
- **AUTH_NAME_MISMATCH:** The authorized user name provided did not match what the losing carrier has on file. Names must match exactly or the carrier will likely reject the port out.
- **BTN_ATN_MISMATCH:** The Billing Telephone Number (BTN) or Account Telephone Number (ATN) did not match what the losing carrier has on file. The BTN or ATN is rarely found on the invoice; in some cases it may be one of the phone numbers on the account.
- **BUSINESS_NAME_MISMATCH:** The business name or end user name provided did not match what the losing carrier has on file.
- **DIFFERENT_ACCOUNTS:** One or more phone numbers in the port request were part of separate accounts. Carriers only allow port requests for a single account at a time. The customer must identify which numbers belong to each account.
- **DIFFERENT_RATE_CENTERS:** One or more phone numbers were in different rate centers. Some carriers require port requests to be split by rate center. This is typically corrected by Telnyx's porting team without customer assistance.
- **FOC_REJECTED:** The FOC date requested was not accepted by the losing carrier.
- **ILLEGIBLE_LOA:** The LOA provided was illegible or unreadable.
- **INVALID_RESELLER:** For Canadian number porting, the reseller specified did not match what the losing carrier has on file.
- **LOSING_CARRIER_NO_RESPONSE:** The losing carrier did not respond to the port out request. Typically corrected by Telnyx's porting team without customer assistance.
- **OTHER:** An unspecified error condition occurred when validating the port out information.
- **PASSCODE_PIN_INVALID:** The passcode or PIN provided did not match what the losing carrier has on file.
- **PENDING_ORDER:** One or more phone numbers are already in the process of being ported out or have another pending service change.
- **PORTING_MAIN_BTN:** The port request was specified as a partial port out but one of the phone numbers is the BTN, which would leave stranded numbers on the account without a BTN.
- **REQUEST_INCORRECT:** The port request was incorrectly specified as a partial or full port out.
- **SERVICE_ADDRESS_MISMATCH:** The service address did not match what the losing carrier has on file.
- **TN_HAS_SPECIAL_FEATURE:** One of the phone numbers has a special feature (such as a DSL line or special bundled pricing) that must be removed before the number can be ported.
- **TN_MISMATCH:** One of the phone numbers in the port request is not on the account specified.
- **TN_NOT_PORTABLE:** One of the phone numbers is not portable.
- **UNSUPPORTED_RATE_CENTER:** Telnyx cannot port one of the phone numbers because the rate center is not supported. This typically happens with rural rate centers where the incumbent carrier has a monopoly.
- **ZIP_POSTAL_CODE_MISMATCH:** The zip or postal code did not match what the losing carrier has on file.

## BTN or ATN Mismatch

Carriers require that a single telephone number be designated as the primary number for the account — typically called the Billing Telephone Number (BTN) or Account Telephone Number (ATN). Accounts with multiple accounts will likely have different BTNs/ATNs.

When submitting a port request, the existing carrier may require Telnyx to provide the BTN or ATN as a way of validating the port request. A BTN/ATN mismatch error occurs when the number submitted does not match what the carrier has on the Customer Service Record (CSR). The BTN is typically not found on a bill copy (except in wireless or toll-free porting).

For large port requests, some of the telephone numbers may belong to a different account with a different BTN/ATN. The carrier is unlikely to specify which numbers belong to another account.

### Next Steps

Check whether the BTN/ATN is specified at the top of the most recent carrier bill or invoice. If the numbers are serviced by a reseller, the BTN/ATN listed may not match what the underlying carrier has on file in the CSR. If it is not found on the bill or invoice, contact the carrier directly to request a CSR.

### Special Note for Resellers

When an end customer purchased service through a reseller, mismatched BTNs can occur because the end customer submits the reseller's phone number as their own BTN. When a losing reseller is involved, the number may actually belong to the reseller rather than the end customer. The customer may submit their own BTN and service address instead of the reseller's.

## Authorized Name Mismatch

Each account has one or more authorized users — employees or officers allowed to make changes to the account. Authorized users are typically specified when an account is set up. Related error names include "Auth Name Error", "Authorized User Error", and "Name Mismatch".

The authorized user name is not always the name of the person who receives the bill or invoice. The best way to obtain the authorized user name is to call the current carrier and ask. In some cases Telnyx may be able to request a CSR on the customer's behalf and determine the authorized user's name.

For retailers, banks, and chains with many locations, the authorized user may be the current or former manager of the individual location. Accounts are often not set up by the corporate parent.

## Day of Port (FOC)

On the day numbers are set to be ported, a few checks help ensure everything is in order:

1. Ensure a connection has been assigned to all numbers set to be ported.
2. Ensure internal systems or hardware are set up and ready at the time of the port.

There may be a slight delay between the scheduled FOC time and the actual port time, especially during periods of high request volume. If numbers must be ported as close to the FOC time as possible, inform the porting team a few days before the scheduled port. If the port request is eligible for FastPort®, see [Your Guide to FastPort®](your-guide-to-fastport.md).

### Not SMS Capable?

During the port process, the Customer Portal may show a "Not SMS Capable" note beside a pending number. All US numbers are SMS capable, and this status will change during the activation of the port request.
