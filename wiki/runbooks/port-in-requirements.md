---
title: Port-in requirements
summary: View and fulfill regulatory requirements on your port-in orders.
sources:
  - url: https://developers.telnyx.com/docs/numbers/porting/port-in-requirements/index
    content_hash: 5836ad669897fcf79f7b214ba56483814eaec9d22c1f159355e3e1bfa3158188
updated_at: 2026-04-10T00:00:00Z
---

# Port-in requirements

View and fulfill regulatory requirements on your port-in orders

## Overview

All port-in orders have regulatory requirements that must be fulfilled before the port can be completed. These requirements vary based on the country and phone number type you are porting.

## How it works

### Step 1: View requirements on your port order

When you create a port order, the `requirements` array is automatically populated based on the country and phone number type being ported. Each requirement includes a `requirement_type_id` that identifies what information is needed.

Use the `GET /v2/porting_orders/{id}/requirements` endpoint to view detailed information about all requirements on your port order, including descriptions and acceptance criteria.

### Step 2: Fulfill requirements

To fulfill a requirement, submit the appropriate `field_value` for each `requirement_type_id` using the [PATCH /v2/porting\_orders/ endpoint](https://developers.telnyx.com/api-reference/porting-orders/edit-a-porting-order).

The value you provide depends on the requirement type:

* **Document**: Provide a document ID from the [Documents API](https://developers.telnyx.com/api-reference/documents/upload-a-document).
* **Textual**: Provide a string value that meets the acceptance criteria.
* **Address**: Provide an address ID from the [Addresses API](https://developers.telnyx.com/api-reference/addresses/creates-an-address).

For detailed fulfillment instructions for each type, see the [regulatory requirements guide](https://developers.telnyx.com/docs/numbers/phone-numbers/regulatory-requirements).

## Requirement statuses

Each requirement on a port order has a status that indicates its current state:

| Status                          | Description                                                                                                       |
| :------------------------------ | :---------------------------------------------------------------------------------------------------------------- |
| `requirement-info-pending`      | Awaiting user submission. You need to provide information to fulfill the requirement.                             |
| `requirement-info-under-review` | Information has been submitted and is awaiting review by Telnyx Porting Operations.                               |
| `requirement-info-exception`    | The submitted information does not meet the acceptance criteria. You need to resubmit with corrected information. |
| `approved`                      | The requirement has been reviewed and validated by Telnyx Porting Operations.                                     |

## Order-level requirements status

For a high-level view of whether all requirements have been fulfilled and approved, check the `requirements_status` field on the port order:

* `true`: All requirements on the port order have been fulfilled and approved.
* `false`: One or more requirements have not been fulfilled or have not been approved yet.

Use the [GET /v2/porting\_orders/ endpoint](https://developers.telnyx.com/api-reference/porting-orders/retrieve-a-porting-order) to check this status.


## Related Pages

- [Port-in events](../runbooks/port-in-events.md)
- [Action ordering requirements](../runbooks/action-ordering-requirements.md)
- [Regulatory Requirements](../runbooks/regulatory-requirements.md)
