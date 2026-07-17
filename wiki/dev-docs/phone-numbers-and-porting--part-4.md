---
title: Phone Numbers and Porting
summary: This page consolidates Telnyx developer documentation covering phone number
  search, ordering, reservations, bulk and advanced orders, regulatory requirements,
  requirement groups, documents, port-in and port-out workflows, and the notifications
  and events that track them. It provides an end-to-end reference for purchasing numbers,
  fulfilling regulatory requirements, transferring numbers in and out of Telnyx, and
  monitoring the lifecycle of those operations via webhooks and events.
sources:
- url: https://developers.telnyx.com/docs/numbers/phone-numbers/action-ordering-requirement
- url: https://developers.telnyx.com/docs/numbers/phone-numbers/advanced-orders
- url: https://developers.telnyx.com/docs/numbers/phone-numbers/bulk-ordering
- url: https://developers.telnyx.com/docs/numbers/phone-numbers/buy-phone-number
- url: https://developers.telnyx.com/docs/numbers/phone-numbers/documents/index
- url: https://developers.telnyx.com/docs/numbers/phone-numbers/getting-started/index
- url: https://developers.telnyx.com/docs/numbers/phone-numbers/number-orders
- url: https://developers.telnyx.com/docs/numbers/phone-numbers/number-reservations/index
- url: https://developers.telnyx.com/docs/numbers/phone-numbers/number-search/index
- url: https://developers.telnyx.com/docs/numbers/phone-numbers/regulatory-requirements/index
- url: https://developers.telnyx.com/docs/numbers/phone-numbers/requirement-groups
- url: https://developers.telnyx.com/docs/numbers/porting/allowed-foc-dates
- url: https://developers.telnyx.com/docs/numbers/porting/bundles-porting
- url: https://developers.telnyx.com/docs/numbers/porting/cancel-port-order
- url: https://developers.telnyx.com/docs/numbers/porting/extensions
- url: https://developers.telnyx.com/docs/numbers/porting/getting-started/index
- url: https://developers.telnyx.com/docs/numbers/porting/messaging-porting
- url: https://developers.telnyx.com/docs/numbers/porting/on-demand-activations
- url: https://developers.telnyx.com/docs/numbers/porting/port-in-blocks
- url: https://developers.telnyx.com/docs/numbers/porting/port-in-events
- url: https://developers.telnyx.com/docs/numbers/porting/port-in-notifications
- url: https://developers.telnyx.com/docs/numbers/porting/port-in-requirements
- url: https://developers.telnyx.com/docs/numbers/porting/port-out-events
- url: https://developers.telnyx.com/docs/numbers/porting/port-out-notifications
- url: https://developers.telnyx.com/docs/numbers/porting/port-out-quickstart/index
- url: https://developers.telnyx.com/docs/numbers/porting/porting-additional-steps/index
updated_at: 2026-07-17T09:16:33Z
---

# Phone Numbers and Porting

*Part 4 of 11 — see also: [Part 1](phone-numbers-and-porting--part-1.md), [Part 2](phone-numbers-and-porting--part-2.md), [Part 3](phone-numbers-and-porting--part-3.md), [Part 5](phone-numbers-and-porting--part-5.md), [Part 6](phone-numbers-and-porting--part-6.md), [Part 7](phone-numbers-and-porting--part-7.md), [Part 8](phone-numbers-and-porting--part-8.md), [Part 9](phone-numbers-and-porting--part-9.md), [Part 10](phone-numbers-and-porting--part-10.md), [Part 11](phone-numbers-and-porting--part-11.md)*

This page consolidates Telnyx developer documentation covering phone number search, ordering, reservations, bulk and advanced orders, regulatory requirements, requirement groups, documents, port-in and port-out workflows, and the notifications and events that track them. It provides an end-to-end reference for purchasing numbers, fulfilling regulatory requirements, transferring numbers in and out of Telnyx, and monitoring the lifecycle of those operations via webhooks and events.

## Regulatory Requirements

Prior to number activation, some phone numbers need additional information to satisfy regulatory requirements. These requirements are defined per country, phone number type, and action (ordering or porting). For example, porting a GB local phone number may have one set of requirements, while ordering a GB local phone number may have another set.

Use the [GET /requirements](https://developers.telnyx.com/api-reference/requirements/list-all-requirements) endpoint and accompanying filters to see what regulatory requirements need to be met. The API response will have two different `record_type` values:

- `"record_type": "requirement"`: The parent record indicating which country, phone number type, and action combination the regulatory requirements apply to.
- `"record_type": "requirement_type"`: Communicates the actual regulatory requirements that need to be fulfilled (e.g., a Proof of address).

### Fulfilling a Requirement Type

To complete your order, all regulatory requirements must be fulfilled and approved. You can satisfy these requirements individually for each order, or use a requirement group to apply all the values at once. To view additional information on a regulatory requirement, perform a [GET /requirement_types/](https://developers.telnyx.com/api-reference/requirement-types/retrieve-a-requirement-types) request. If a `requirement_type` includes `acceptance criteria`, ensure the value provided meets those criteria.

Each `requirement_type` has a `type` classification. There are four possible types: textual, address, document, and action.

**Textual type:** Any string can be provided (assuming it complies with the `acceptance_criteria` of the `requirement_type`).

**Address type:** An address id must be provided as the field value. Create an address using the [POST v2/addresses](https://developers.telnyx.com/api-reference/addresses/creates-an-address) endpoint. Upon successful creation, the address will have a unique id. Pass that id as the `field_value` for the address ordering requirement. You cannot write out the address as a string.

**Document type:** A document id must be provided as the field value. Upload the document using the [POST /documents](https://developers.telnyx.com/api-reference/documents/upload-a-document) endpoint. Upon successful upload, an id will be returned in the response. Pass that id as the `field_value` for the document ordering requirement.

**Action type:** An action requirement is unique and very rare. See the action ordering requirements guide for more information.

## Action Ordering Requirements

Action requirements are a special type of regulatory requirement for international phone number orders that cannot be fulfilled by submitting documents or text information. Instead, these requirements need the end user to complete an external action, such as identity verification through a third-party service.

### Australia Mobile ID Verification

Australia mobile number orders require end user identity verification to comply with local telecommunications regulations. Telnyx has partnered with [Onfido](https://onfido.com/) to facilitate this verification.

**Requirement ID:** `b7c72fb8-fa08-4529-aaf6-b9117d3f3698`

**Verification process:**

1. Generate a unique verification link by making a request to the [POST /v2/external_requirements//sub_number_orders/ endpoint](https://developers.telnyx.com/api-reference/overview). Include the end user's `first_name` and `last_name` in the request body.
2. The API returns a URL in the `requirement_action.value` field. Share this URL with the end user to access Onfido's secure ID verification portal.
3. The end user visits the provided URL and completes the identity verification process by submitting required identification documents through the Onfido portal.
4. Once submitted, the verification is reviewed. Upon approval, the requirement is automatically marked as completed on the number order.
5. The order's `requirements_met` field updates to `true`, allowing the order to proceed to the next stage.
