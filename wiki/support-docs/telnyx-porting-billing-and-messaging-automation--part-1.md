---
title: Telnyx Porting, Billing, and Messaging Automation
summary: This page consolidates Telnyx support documentation covering number porting
  (CSRs, LOAs, automated validation, porting requirements, and the auto-generated
  LOA feature), billing models (per-minute billing increments and channel billing
  with zone-based pricing), CLI/CLD validation for North American calls, and Zapier-based
  SMS automations including forwarding texts to mobile or email, automated replies,
  and the Textable integration.
sources:
- url: https://support.telnyx.com/en/articles/1130614-obtaining-a-csr-from-your-carrier
- url: https://support.telnyx.com/en/articles/1130659-billing-increments
- url: https://support.telnyx.com/en/articles/1130678-channel-billing-and-how-to-use-it
- url: https://support.telnyx.com/en/articles/1516776-automated-port-request-validation
- url: https://support.telnyx.com/en/articles/2034326-how-to-fill-out-an-loa
- url: https://support.telnyx.com/en/articles/3231942-forwarding-sms-to-your-mobile-number
- url: https://support.telnyx.com/en/articles/3232529-automated-replies-for-messages-using-zapier
- url: https://support.telnyx.com/en/articles/3685327-textable-setup-guide
- url: https://support.telnyx.com/en/articles/3723768-zapier-forward-texts-to-email
- url: https://support.telnyx.com/en/articles/6247033-cli-cld-validation-faq
- url: https://support.telnyx.com/en/articles/6460777-porting-requirements
- url: https://support.telnyx.com/en/articles/8268276-loa-template-download
- url: https://support.telnyx.com/en/articles/8428806-channel-billing
- url: https://support.telnyx.com/en/articles/8588086-auto-generated-letter-of-authorization-loa
updated_at: 2026-07-17T09:02:58Z
---

# Telnyx Porting, Billing, and Messaging Automation

*Part 1 of 7 — see also: [Part 2](telnyx-porting-billing-and-messaging-automation--part-2.md), [Part 3](telnyx-porting-billing-and-messaging-automation--part-3.md), [Part 4](telnyx-porting-billing-and-messaging-automation--part-4.md), [Part 5](telnyx-porting-billing-and-messaging-automation--part-5.md), [Part 6](telnyx-porting-billing-and-messaging-automation--part-6.md), [Part 7](telnyx-porting-billing-and-messaging-automation--part-7.md)*

This page consolidates Telnyx support documentation covering number porting (CSRs, LOAs, automated validation, porting requirements, and the auto-generated LOA feature), billing models (per-minute billing increments and channel billing with zone-based pricing), CLI/CLD validation for North American calls, and Zapier-based SMS automations including forwarding texts to mobile or email, automated replies, and the Textable integration.

## Obtaining a CSR From Your Carrier

A Customer Service Record (CSR) is a copy of how your telephone records appear in your current carrier's database. It contains information about each separate line charge (type of service, federal access charge, number portability charge, calling blocks, 911 charge, etc.) that makes up your monthly service charge. A CSR also reveals the service location of the account, the billing address, additional directory listings, PIC designations, hunting order, features being charged and on which line they appear, calling plans, and taxes applied to each item on the record.

The information on your CSR is important for the porting process. When you initiate a port-out request, your current carrier will match some of the information contained in the request with what they have on file in the CSR. If enough pieces of data match, they will allow the numbers to be ported away. Carriers generally match on the business name on the account, the zip or postal code of the service address (often not the same as the billing address), and the account number or BTN/ATN of the account.

Having your CSR handy before starting the porting process is the #1 way to speed up porting. Most delays are caused by submitting incorrect data when initiating the porting process. In some cases Telnyx can obtain a CSR for you, but carriers are not obligated to release them to other carriers, so it's always best to obtain one directly from your current carrier.

To request your CSR, call the customer service or support number for your carrier and clearly state that you'd like a copy of your CSR. Most carriers should provide a CSR upon request. Have the CSR sent to you over email so you get the full details rather than only part of the information over the phone. Once you have your CSR, upload it to the Telnyx Mission Control portal.

**Special Note for Canadian Customers:** Canadian telecom carriers are generally not willing to provide CSRs to other carriers.

## Automated Port Request Validation

Telnyx has built functionality that automatically validates your port request with the losing carrier to reduce porting delays and rejections. The flow works as follows:

1. When customers submit port requests, Telnyx checks if the losing (current) carrier supports automated CSR validation.
2. If supported, Telnyx requests a CSR using the Billing Telephone Number (BTN), account number, end customer name, and service address. It can take up to 30 minutes for a CSR to come back from the carrier.
3. Telnyx matches the submitted information with what was returned from the CSR. If the information matches, Telnyx's Porting Team starts working on the final port submission to the losing carrier.
4. If the information does not match, Telnyx puts the port request into Exception status and notifies you of the errors. Customers can use the port request comments feature to provide updates to any of the fields that failed validation. Once corrected, Telnyx re-submits the port request to the losing carrier.

A few things to note:

- Only major carriers support automated validation, such as Level 3, AT&T, and CenturyLink. Telnyx is regularly adding support for additional carriers.
- It can take up to 30 minutes for the data to come back from the carrier. If the data you provide is materially different from what is on file with the carrier, the carrier will likely not return any data. This is typically due to having an incorrect BTN, account number, or service address.
- For privacy reasons, Telnyx cannot share the corrected data with you. We can only tell you if the data matched. It is up to you to provide the correct data.
- Even if data validation fails, Telnyx will continue to work on the port request. Often the data has a minor inconsistency that Telnyx can resolve without the customer's help. We will notify you if we need further action from you.

## Porting Requirements

Before submitting a port request to Telnyx, ensure you have the required documents. The required documents are summarized below:

| Document | Purpose | Requirements |
| --- | --- | --- |
| Letter of Authorization (LOA) | Authorizes Telnyx to request the port | Required for ALL ports |
| Invoice or Bill | Proves ownership of the numbers | Required (alternatives available) |
| CSR (optional) | Verifies account details | Recommended, not required |

### Letter of Authorization (LOA)

The LOA is a legal document that gives Telnyx permission to request a port on your behalf. Requirements:

- **Signature:** Wet signature or valid electronic signature (DocuSign, Adobe Sign, etc.)
- **Signer:** Must be the authorized person on the account with the losing carrier
- **Numbers:** ALL numbers being ported must be listed
- **Information:** End user name and service address
- **Date:** Must be signed within the last 90 days

For toll-free numbers, the LOA must include: **"Port to RespOrg QIT02"**.

### Invoice or Bill

An invoice proves that the end user porting the numbers is the rightful owner. Requirements:

- Must be from your current carrier (the losing carrier)
- Must be within the last 30 days
- Should show the telephone numbers being ported (if possible)

If your invoice doesn't show the telephone numbers, provide ONE of these alternatives:

- **Portal Screenshot:** Screenshot from your current carrier's portal showing the numbers on your account
- **CSR:** Customer Service Record from your current carrier listing the numbers
- **Other Proof:** Contact porting@telnyx.com to discuss options

### Customer Service Record (CSR)

A CSR is an official record from your current carrier that contains your account details. It typically includes:

- Account holder name (exactly as on file)
- Service address
- Billing Telephone Number (BTN)
- List of telephone numbers
- Current carrier information

A CSR is not required, but it is highly recommended. It helps ensure your LOA information matches exactly what the losing carrier has on file, preventing rejections due to mismatched data.

### Document Validity Periods

| Document | Maximum Age |
| --- | --- |
| LOA (signature date) | 90 days |
| Invoice/Bill | 30 days |
| CSR | No strict limit, but recent is better |

### Common Rejection Reasons

| Issue | How to Prevent |
| --- | --- |
| LOA not signed | Ensure authorized person signs the LOA |
| Signature too old | Sign within the last 90 days |
| Name mismatch | Use exact name from CSR or carrier records |
| Address mismatch | Use service address, not billing address |
| Missing invoice | Upload a recent bill or acceptable alternative |
| Numbers not listed on LOA | Include ALL numbers you want to port |

### Special Requirements by Number Type

**Toll-Free Numbers**

- LOA must include "Port to RespOrg QIT02"
- RespOrg transfer may take 3-7 business days

**Wireless Numbers**

- Account PIN may be required (carrier-dependent)
- Last 4 of SSN may be requested

**International Numbers**

- Requirements vary by country
- May require country-specific LOA forms
- Additional documentation (VAT/Tax ID) often required

### Reseller Requirements

If you are porting numbers on behalf of your customers:

- Use your end customer's information on the LOA — not your business info
- The end customer must sign the LOA
- Invoice should be from the end customer's account

For questions about porting requirements or documentation, contact the porting team at porting@telnyx.com.
