---
title: 'Telnyx Voice: Caller ID, Call Completion, and Pricing'
summary: A consolidated reference for Telnyx voice services covering Caller ID Number
  (CID) and Caller ID Name (CNAM) configuration, the Caller ID Number Policy, pricing
  and billing, LRN and number lookup, US local and rural call completion, PSTN replacement
  and local calling, and troubleshooting inbound and outbound call failures.
sources:
- url: https://support.telnyx.com/en/articles/1130656-set-up-inbound-caller-id-name-incoming
- url: https://support.telnyx.com/en/articles/1130720-caller-id-outbound-vs-cnam
- url: https://support.telnyx.com/en/articles/13795700-accessing-canadian-lrn-data
- url: https://support.telnyx.com/en/articles/2185372-where-can-i-see-pricing-options
- url: https://support.telnyx.com/en/articles/3317613-billing-decimal-values-considered
- url: https://support.telnyx.com/en/articles/3546251-caller-id-number-policy
- url: https://support.telnyx.com/en/articles/4096828-us-rural-call-completion
- url: https://support.telnyx.com/en/articles/4378813-us-local-call-completion
- url: https://support.telnyx.com/en/articles/5025298-troubleshooting-call-completion
- url: https://support.telnyx.com/en/articles/5073043-the-rate-sheet-and-lrn-explained
- url: https://support.telnyx.com/en/articles/6622229-pstn-replacement-local-calling-with-telnyx
updated_at: 2026-07-17T09:05:14Z
---

# Telnyx Voice: Caller ID, Call Completion, and Pricing

*Part 2 of 5 — see also: [Part 1](telnyx-voice-caller-id-call-completion-and-pricing--part-1.md), [Part 3](telnyx-voice-caller-id-call-completion-and-pricing--part-3.md), [Part 4](telnyx-voice-caller-id-call-completion-and-pricing--part-4.md), [Part 5](telnyx-voice-caller-id-call-completion-and-pricing--part-5.md)*

A consolidated reference for Telnyx voice services covering Caller ID Number (CID) and Caller ID Name (CNAM) configuration, the Caller ID Number Policy, pricing and billing, LRN and number lookup, US local and rural call completion, PSTN replacement and local calling, and troubleshooting inbound and outbound call failures.

## Caller ID Number Policy

Telnyx enforces a strict policy on Caller ID Numbers for outbound calls. All outbound calls with invalid Caller ID Numbers are rejected with the SIP response code **"403 Caller Origination Number is Invalid D35"**.

### Supported Number Formats

When creating a SIP Connection, the default localisation is **USA**, which accepts calls in national, 11-digit, or +E.164 format.

For example, with localisation set to **United States**:

- **United States** — accepted formats: national, 11-digit, +E.164 (e.g., `3129457420`, `1312945720`, `+1312945720`).
- **Ireland** — accepted format: +E.164 only (e.g., `+353-1-840-1234`).

With localisation set to **Ireland**:

- **Ireland** — accepted formats: national, 11-digit, +E.164 (e.g., `840-1234`, `01-840-1234`, `+353-1-840-1234`).
- **United States** — accepted format: +E.164 only (e.g., `+13129457420`).

If the connection's Caller ID Override is set and used for an outbound call, any format may be sent.

### How Telnyx Handles the Caller ID Number

- The Localisation Country is set through the Mission Control Portal under the connection's Outbound Settings.
- If a connection has no Localisation Country and the dialled number appears invalid, Telnyx attempts to validate the number using USA as the Localisation Country.
- If validation fails, Telnyx returns a **404 invalid destination** response.

### SIP Headers That Carry the Caller ID Number

Telnyx accepts the following SIP headers for Caller ID, ordered by priority (1 highest, 4 lowest):

1. `P-Preferred-Identity` User
2. `P-Asserted-Identity` User
3. `Remote-Party-Id` User
4. `FROM` User

If more than one header is provided, the highest-priority header is followed.

### Anonymising the Caller ID Number

To anonymise the caller ID on an outbound call, include the SIP header `Privacy: id` along with a valid caller ID in a supported number format. Telnyx will then change the caller ID to anonymous. If a valid caller ID is not received, the call is rejected with **403 Caller Origination Number is Invalid D35**.

Notes:

- The caller ID is anonymised downstream because the `Privacy: id` header is present.
- If the destination is a toll-free number, the caller ID is **not** anonymised — the toll-free owner is paying for the call and has the right to know who is calling. The same applies to emergency numbers.

### EEA Destinations

Calls terminating into the EEA internationally must include a valid `P-Asserted-Identity` (PAI) header containing a real, dialable CLI. This is used by downstream carriers for origination-based routing (OBR) billing. If the PAI header is missing, contains an anonymous value, or contains an invalid number, the call may be rejected or subject to surcharges from the terminating carrier, which will be passed on to the customer. Anonymous or invalid CLIs on these routes are not supported and can result in significant additional costs.

### International Spoofing

For outbound calls to international destinations, calls will be rejected because Telnyx and many downstream carriers do not support international spoofing. A **503 error response** is typically returned so that you can attempt to route advance on your side.

## Pricing and Billing

### Viewing Pricing Options

Pricing options are available on the **Pricing** page, accessed from your account icon (top right) within the Mission Control Portal. The page contains five tabs — **Voice**, **Numbers**, **Messaging**, **Telco Data**, and **Networking** — each with a usage toggle that adjusts pricing rates based on the selected volume:

- **Voice**: toggle between bucketed monthly minute volumes for inbound (origination) voice/fax usage for Standard DIDs and Toll-Free DIDs.
- **Numbers**: toggle between required number counts per month.
- **Messaging**: toggle between bucketed monthly message volumes.
- **Telco Data**: CNAM, LRN, and Switch Data pricing.
- **Networking**: select bandwidth options for Mbps per month.

### Billing Decimal Precision

Telnyx considers **4 decimal points** for billing. For example, the SMS rate is $0.0025 USD, and call rates are also considered up to 4 decimal points. More information is available on the [Telnyx pricing page](https://telnyx.com/pricing).

## Telco Data: LRN and Number Lookup

### The Rate Sheet and LRN

Call rates are based on the **Location Routing Number (LRN)**, not always the number you dial. In rare cases where the LRN and the dialled number do not match, the LRN destination prefix determines the cost.

The LRN of a number can be found using the Lookup tool in the Mission Control Portal — enter the number and the tool returns the associated LRN prefix, which should be used to determine the correct rate on the Rate Sheets. For example, numbers with the prefix `+1 941 529` may have an LRN beginning with `+1 813 568`, so the applicable pricing is listed under the `+1 813 568` destination prefix.

### Accessing Canadian LRN Data

Canadian LRN data is subject to regulatory restrictions and is not freely available. Telnyx holds a license to offer this data to customers, but the following requirements apply:

1. **Regulatory approval**: Customers must apply for and receive approval from the **Canadian Local Number Portability Consortium (CNLPC)** to access Canadian LRN data through Telnyx. Contracted customers can submit applications for Non-Member Access via the [CNLPC non-member access page](https://clnpc.ca/non-member-access/). This offering only applies to contracted customers.
2. **Associated costs**: There is an annual fee of approximately **$2,000 USD**, payable directly to the CNLPC. Default Telnyx Number Lookup pricing applies — there is no special pricing for CA LRN lookups.
3. **Usage requirements**: Telnyx applies a minimum lookup requirement due to the costs of facilitating access. Access is reviewed and granted on a case-by-case basis. The minimum monthly spend on LRN lookups is approximately **$225**, which works out to about **150,000 LRN lookups** at the base price of $0.0015.

Once these criteria are met, Telnyx requires proof of the CNLPC non-member access approval. Contact your CSM or [support@telnyx.com](mailto:support@telnyx.com) for more information.
