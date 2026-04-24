---
title: Regulatory Requirements
summary: Tutorial for viewing and fulfilling regulatory requirements on phone number orders.
sources:
  - url: https://developers.telnyx.com/docs/numbers/phone-numbers/regulatory-requirements/index
    content_hash: 657fa5a4953c86098f0bde047268087062ae8cbede8ce595aba12f5b3c14cd5d
updated_at: 2026-04-10T00:00:00Z
---

# Regulatory Requirements

Tutorial for viewing and fulfilling regulatory requirements on phone number orders.

Prior to number activation, some phone numbers need additional information to satisfy regulatory requirements. 

These requirements are defined per:

* Country
* Phone number type
* Action (ordering a phone number, or porting a phone number)

For example, `porting` a `GB` `local` phone number may have one set of requirements, while `ordering` a `GB` `local` phone number may have another set of requirements.

Use the [GET /requirements](https://developers.telnyx.com/api-reference/requirements/list-all-requirements) endpoint and accompanying filters to see what regulatory requirements need to be met to purchase/port a phone number.

The API response will have two different `record_type`:

* `”record_type”: “requirement”`: This is the parent record. It indicates which country, phone number type, and action combination that the regulatory requirements apply to. For example, `DE` `local` `ordering`.
* `”record_type”: “requirement_type”`: Communicates the actual regulatory requirements that need to be fulfilled to unblock number activation in that particular country + phone number type + action combination. For example, a `Proof of address`.

Note: The regulatory landscape is constantly evolving. The regulatory requirements for phone numbers may change.

## Fulfilling a `requirement_type`

To complete your order, all regulatory requirements `requirement_type`) must be fulfilled and approved. You can satisfy these requirements individually for each order, or you can [use a requirement group](https://developers.telnyx.com/docs/numbers/phone-numbers/requirement-groups) to apply all the values at once.

To view additional information on a regulatory requirement (description, examples, etc.), perform a [GET /requirement\_types/](https://developers.telnyx.com/api-reference/requirement-types/retrieve-a-requirement-types) request.

If a `requirement_type` includes `acceptance criteria`, ensure the value provided meets those criteria.

Each `requirement_type` has a `type` classification. There are four possible types:

* textual
* address
* document
* action

Each type has different rules for fulfillment.

### Textual type

To fulfill a textual type, any string can be provided (assuming it complies with the `acceptance_criteria` of the `requirement_type`)

### Address type

To fulfill an address requirement, an address id must be provided as the field value.

Create an address using the [POST v2/addresses](https://developers.telnyx.com/api-reference/addresses/creates-an-address) endpoint. Upon successful creation, the address will have a unique id associated with it (for example 1293384261075731499). Pass that id as the field\_value for the address ordering requirement.

You cannot write out the address as a string (i.e. “312 W Superior St, Chicago, IL, 60654, US”). You must create the address with the `POST v2/addresses` endpoint, and pass the address id as the field\_value.

### Document type

To fulfill a document requirement, a document id must be provided as the field value.

Upload the document using the [POST /documents](https://developers.telnyx.com/api-reference/documents/upload-a-document) endpoint. Upon successful upload, an id will be returned in the response that corresponds to the document (for example 6a09cdc3-8948-47f0-aa62-74ac943d6c58). Pass that id as the field\_value for the document ordering requirement.

### Action type

An action requirement is unique, and very rare. Please see [our separate developer guide](https://developers.telnyx.com/docs/numbers/phone-numbers/action-ordering-requirement) to learn more about how to handle action requirement types.


## Related Pages

- [Port-in requirements](../runbooks/port-in-requirements.md)
- [Action ordering requirements](../runbooks/action-ordering-requirements.md)
