---
title: Porting Errors and Rejections
summary: A comprehensive guide to the error messages, rejection reasons, and resolution
  steps that can arise when porting telephone numbers to or from Telnyx—including
  BTN/ATN mismatches, authorized-name errors, reseller issues, port-out notifications,
  and PIN protection settings.
sources:
- url: https://support.telnyx.com/en/articles/1130610-btn-or-atn-mismatch-error
  content_hash: dd197611f6deddd780556f81ed9ca2303f68532e11f7224ad133ea847da91cf8
- url: https://support.telnyx.com/en/articles/1130616-number-not-portable-tn-not-portable-error
  content_hash: 87a1abebb1660ce5503a8cbf48c93ac77ab6c074b9c1306c7c7228566464ec66
- url: https://support.telnyx.com/en/articles/1130619-invalid-reseller-error
  content_hash: c8d800276ec2262dfe56b49017ccfc90b789d0a5d00071df7e101b1dc7429a3a
- url: https://support.telnyx.com/en/articles/1130623-authorized-name-mismatch-error
  content_hash: eaf76d4ba07f4ba2e0753ae24ae4bcd5d0a7e9cf6b03c8364cccafb0edd5a541
- url: https://support.telnyx.com/en/articles/1618776-porting-error-messages
  content_hash: e995c27656b18d949682abda7b3fd4feada949a94ad51daa4865edcfc703f237
- url: https://support.telnyx.com/en/articles/1782930-port-request-rejected
  content_hash: 0dae4420c866bf253de7684d3430b52bd72bd1fffe9e54e6dd1d648b55cf75ef
- url: https://support.telnyx.com/en/articles/2030667-i-received-a-port-out-notification
  content_hash: d7d18abe4b2c5278b6a7afb4f70839b6e137756068c609d6af3be740d232d144
- url: https://support.telnyx.com/en/articles/2047076-carrier-refusing-to-port-your-number
  content_hash: a6d6160ebadb7eb87c8497d436dab4b680d50838e8aa193a8eec7e2e93eeeb52
- url: https://support.telnyx.com/en/articles/8006189-port-out-pin-protection
  content_hash: eb1d7318d82fd58122691a71778ceb79ca09ec0d9a267c43c8f65346e57588b3
updated_at: 2026-06-11T11:12:13Z
---

# Porting Errors and Rejections

*Part 1 of 2 — see also: [Part 2](porting-errors-and-rejections--part-2.md)*

A comprehensive guide to the error messages, rejection reasons, and resolution steps that can arise when porting telephone numbers to or from Telnyx—including BTN/ATN mismatches, authorized-name errors, reseller issues, port-out notifications, and PIN protection settings.

## Common Porting Error Messages

The table below lists the error identifiers you may encounter during the porting process, along with their meaning and typical resolution path.

| Error | Description |
|---|---|
| **ACCOUNT_NUMBER_MISMATCH** | The account number provided did not match what the losing carrier has on file. For some carriers the account number may be the same as the BTN. |
| **ACCOUNT_NUMBER_REQUIRED** | The account number was not provided but is required. |
| **AUTH_NAME_MISMATCH** | The authorized user name did not match what the losing carrier has on file. Names must match exactly or the carrier will likely reject the port-out. |
| **BTN_ATN_MISMATCH** | The Billing Telephone Number (BTN) or Account Telephone Number (ATN) did not match what the losing carrier has on file. The BTN/ATN is rarely found on the invoice; in some cases it may be one of the phone numbers on the account. |
| **BUSINESS_NAME_MISMATCH** | The business name or end-user name provided did not match what the losing carrier has on file. |
| **DIFFERENT_ACCOUNTS** | One or more phone numbers in the port request belong to separate accounts. Carriers only allow port requests for a single account at a time. It is up to the customer to identify which numbers belong to each account. |
| **DIFFERENT_RATE_CENTERS** | Numbers in the request are in different rate centers. Some carriers require requests to be split by rate center. This is typically corrected by the Telnyx porting team without customer assistance. |
| **FOC_REJECTED** | The Firm Order Commitment (FOC) date requested was not accepted by the losing carrier. |
| **ILLEGIBLE_LOA** | The Letter of Authorization (LOA) provided was illegible or unreadable. |
| **INVALID_RESELLER** | For Canadian number porting, the reseller specified did not match what the losing carrier has on file. |
| **LOSING_CARRIER_NO_RESPONSE** | The losing carrier did not respond to the port-out request. Typically corrected by the Telnyx porting team without customer assistance. |
| **OTHER** | An unspecified error condition occurred during validation. |
| **PASSCODE_PIN_INVALID** | The passcode or PIN number provided did not match what the losing carrier has on file. |
| **PENDING_ORDER** | One or more numbers are already being ported out or have another service change pending. |
| **PORTING_MAIN_BTN** | The request was specified as a partial port-out but one of the numbers is the BTN, which would leave stranded numbers on the account without a BTN. |
| **REQUEST_INCORRECT** | The port request was incorrectly specified as either a partial or a full port-out. |
| **SERVICE_ADDRESS_MISMATCH** | The service address did not match what the losing carrier has on file. |
| **TN_HAS_SPECIAL_FEATURE** | A number in the request has a special feature (e.g., DSL line, bundled pricing) that must be removed before the number can be ported. |
| **TN_MISMATCH** | One of the phone numbers specified is not on the account specified. |
| **TN_NOT_PORTABLE** | One of the numbers is not portable. This is a catch-all error; see the dedicated section below. |
| **UNSUPPORTED_RATE_CENTER** | Telnyx cannot port the number because the rate center is not supported (typically rural rate centers where the incumbent carrier has a monopoly). |
| **ZIP_POSTAL_CODE_MISMATCH** | The zip or postal code did not match what the losing carrier has on file. |

## BTN or ATN Mismatch

Related errors: "Wrong BTN", "Wrong ATN".

Carriers require a single telephone number to be designated as the primary number for the account—known as the Billing Telephone Number (BTN) or Account Telephone Number (ATN). When submitting a port request, the losing carrier may require that Telnyx provide the BTN/ATN as validation. A mismatch occurs when the number submitted does not match what the carrier has on the Customer Service Record (CSR). The BTN is typically not found on a bill copy (except in wireless or toll-free porting).

If you submitted a large port request, some of the telephone numbers may belong to a different account with a different BTN/ATN. The carrier is unlikely to specify which numbers belong to another account.

**Resolution steps:**

1. Check whether the BTN/ATN is specified at the top of the most recent carrier bill or invoice.
2. If the numbers are serviced by a reseller, the BTN/ATN on the bill may differ from what the underlying carrier has on the CSR.
3. If not found on the bill, contact the carrier directly and request a CSR. See [Obtaining a CSR From Your Carrier](obtaining-a-csr-from-your-carrier.md).

**Reseller note:** When end customers purchase service through a reseller, they may wrongly submit their own phone number as the BTN instead of the reseller's. The number might actually belong to the reseller, so the BTN and service address should reflect the reseller's information.

## Authorized Name Mismatch

Related errors: "Auth Name Error", "Authorized User Error", "Name Mismatch".

Each account has one or more *authorized users*—employees or officers allowed to make changes to the account, typically specified when the account was set up. The authorized user name is not always the name of the person who receives the bill.

**Resolution steps:**

- The best way to obtain the authorized user name is to call the current carrier and ask.
- In some cases, Telnyx can request a CSR on your behalf and determine the authorized user's name.

**Retailers, banks, and chains:** For businesses with many locations, the authorized user may be the *current or former manager* of the individual location. Accounts are often not set up by the corporate parent.

## Invalid Reseller Error (Canada)

Many customers buy their numbers from a telecom reseller, VoIP provider, or managed service provider, which in turn purchases the numbers from the carrier. In this case, the end customer's name and service address may not be on file with the underlying carrier.

When submitting a port-out request, Canadian carriers require the reseller's name. If the name does not match exactly what is on file, the request may be rejected.

**Resolution steps:**

- Call your reseller and ask for the exact spelling of their name with the losing carrier. This may not match the brand name used on their bill, invoice, or marketing materials.

## TN Not Portable

The "TN Not Portable" error is a catch-all. The carrier is intentionally being unspecific about why the number is not portable. Common underlying reasons include:

- The number is **inactive** with the losing carrier (no longer assigned or deactivated).
- The number is stuck in a **pending** state (another action was recently initiated and is still pending).
- The number has a **special feature** such as a signal ring.
- The number is on a **special rate plan** (e.g., bundled TV/voice/Internet plans).
- A recent **informational update** was made to the account.

**Resolution steps:**

- Call your existing carrier and ask if any numbers on your account are not portable. They should be able to identify features or inactive numbers that could hold up a port request.
- If a number is inactive, you will likely need to re-activate it before a port-out can proceed.
