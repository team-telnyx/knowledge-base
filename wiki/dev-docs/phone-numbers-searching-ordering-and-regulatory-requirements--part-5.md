---
title: 'Phone Numbers: Searching, Ordering, and Regulatory Requirements'
summary: This page covers the end-to-end workflow for purchasing phone numbers on
  Telnyx, including searching inventory, reserving numbers, placing standard, bulk,
  and advanced orders, fulfilling regulatory requirements (textual, address, document,
  and action types), uploading supporting documents, and configuring webhook notifications.
sources:
- url: https://developers.telnyx.com/docs/numbers/phone-numbers/action-ordering-requirement
- url: https://developers.telnyx.com/docs/numbers/phone-numbers/advanced-orders
- url: https://developers.telnyx.com/docs/numbers/phone-numbers/bulk-ordering
- url: https://developers.telnyx.com/docs/numbers/phone-numbers/buy-phone-number
- url: https://developers.telnyx.com/docs/numbers/phone-numbers/documents/index
- url: https://developers.telnyx.com/docs/numbers/phone-numbers/getting-started
- url: https://developers.telnyx.com/docs/numbers/phone-numbers/number-orders
- url: https://developers.telnyx.com/docs/numbers/phone-numbers/number-reservations/index
- url: https://developers.telnyx.com/docs/numbers/phone-numbers/number-search/index
- url: https://developers.telnyx.com/docs/numbers/phone-numbers/regulatory-requirements
updated_at: 2026-08-05T14:00:16Z
---

# Phone Numbers: Searching, Ordering, and Regulatory Requirements

*Part 5 of 6 — see also: [Part 1](phone-numbers-searching-ordering-and-regulatory-requirements--part-1.md), [Part 2](phone-numbers-searching-ordering-and-regulatory-requirements--part-2.md), [Part 3](phone-numbers-searching-ordering-and-regulatory-requirements--part-3.md), [Part 4](phone-numbers-searching-ordering-and-regulatory-requirements--part-4.md), [Part 6](phone-numbers-searching-ordering-and-regulatory-requirements--part-6.md)*

This page covers the end-to-end workflow for purchasing phone numbers on Telnyx, including searching inventory, reserving numbers, placing standard, bulk, and advanced orders, fulfilling regulatory requirements (textual, address, document, and action types), uploading supporting documents, and configuring webhook notifications.

## Regulatory Requirements

Prior to number activation, some phone numbers need additional information to satisfy regulatory requirements. These requirements are defined per:

- Country
- Phone number type
- Action (ordering a phone number, or porting a phone number)

For example, porting a GB local phone number may have one set of requirements, while ordering a GB local phone number may have another set. Use the [GET /requirements](https://developers.telnyx.com/api-reference/requirements/list-all-requirements) endpoint and accompanying filters to see what regulatory requirements need to be met to purchase or port a phone number.

The API response will have two different `record_type` values:

- `"record_type": "requirement"`: The parent record. It indicates which country, phone number type, and action combination the regulatory requirements apply to (e.g., `DE` `local` `ordering`).
- `"record_type": "requirement_type"`: Communicates the actual regulatory requirements that need to be fulfilled to unblock number activation in that particular combination (e.g., a Proof of address).

The regulatory landscape is constantly evolving. The regulatory requirements for phone numbers may change.

### Fulfilling a Requirement Type

To complete your order, all regulatory requirements must be fulfilled and approved. You can satisfy these requirements individually for each order, or you can [use a requirement group](https://developers.telnyx.com/docs/numbers/phone-numbers/requirement-groups) to apply all the values at once. To view additional information on a regulatory requirement (description, examples, etc.), perform a [GET /requirement_types/](https://developers.telnyx.com/api-reference/requirement-types/retrieve-a-requirement-types) request. If a `requirement_type` includes `acceptance criteria`, ensure the value provided meets those criteria.

Each `requirement_type` has a `type` classification. There are four possible types: `textual`, `address`, `document`, and `action`. Each type has different rules for fulfillment.

**Textual type:** Any string can be provided (assuming it complies with the `acceptance_criteria` of the `requirement_type`).

**Address type:** An address id must be provided as the field value. Create an address using the [POST v2/addresses](https://developers.telnyx.com/api-reference/addresses/creates-an-address) endpoint. Upon successful creation, the address will have a unique id (for example `1293384261075731499`). Pass that id as the `field_value` for the address ordering requirement. You cannot write out the address as a string; you must create the address with the `POST v2/addresses` endpoint and pass the address id as the `field_value`.

**Document type:** A document id must be provided as the field value. Upload the document using the [POST /documents](https://developers.telnyx.com/api-reference/documents/upload-a-document) endpoint. Upon successful upload, an id will be returned in the response (for example `6a09cdc3-8948-47f0-aa62-74ac943d6c58`). Pass that id as the `field_value` for the document ordering requirement.

**Action type:** An action requirement is unique and very rare. See [Action Ordering Requirements](action-ordering-requirements.md) to learn more about how to handle action requirement types.

## Action Ordering Requirements

Action requirements are a special type of regulatory requirement for international phone number orders that cannot be fulfilled by submitting documents or text information. Instead, these requirements need the end user to complete an external action, such as identity verification through a third-party service. Each action requirement type may have different fulfillment steps depending on the specific verification needed.

### Australia Mobile ID Verification

Australia mobile number orders require end user identity verification to comply with local telecommunications regulations. Telnyx has partnered with [Onfido](https://onfido.com/), a trusted identity verification provider.

**Requirement ID:** `b7c72fb8-fa08-4529-aaf6-b9117d3f3698`

This ID is used when initiating the verification process through the external requirements endpoint.

**Verification process:**

1. Generate a unique verification link by making a request to the [POST /v2/external_requirements//sub_number_orders/ endpoint](https://developers.telnyx.com/api-reference/overview). Include the end user's `first_name` and `last_name` in the request body.
2. The API returns a URL in the `requirement_action.value` field. Share this URL with the end user to access Onfido's secure ID verification portal.
3. The end user visits the provided URL and completes the identity verification process by submitting required identification documents through the Onfido portal.
4. Once submitted, the verification is reviewed. Upon approval, the requirement is automatically marked as completed on the number order.
5. The order's `requirements_met` field updates to `true`, allowing the order to proceed to the next stage.
