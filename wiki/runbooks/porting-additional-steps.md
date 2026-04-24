---
title: Porting additional steps
summary: Handle additional steps that may be required before submitting a porting order.
sources:
  - url: https://developers.telnyx.com/docs/numbers/porting/porting-additional-steps/index
    content_hash: 8dee8402c5f204bee86fa59da52aedd3fbcd99dbf0e9c015c3fbe1a14ecf5ab3
updated_at: 2026-04-10T00:00:00Z
---

# Porting additional steps

Handle additional steps that may be required before submitting a porting order

## Overview

After you create and populate a porting order, Telnyx may require additional steps depending on the phone numbers being ported and the details provided. These steps must be completed before you can submit the order.

Additional steps differ from [supplemental port order requirements](https://developers.telnyx.com/docs/numbers/porting/port-in-requirements), which cover documents and textual information needed for specific countries or number types. Additional steps involve actions or decisions that affect other phone numbers on your losing carrier's account.

## Checking for additional steps

The `additional_steps` array on a porting order indicates whether any additional steps are required.

| Value                          | Meaning                                                                                                                                                                                             |
| :----------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `[]` (empty array)             | No additional steps required. You can proceed with submission.                                                                                                                                      |
| `["associated_phone_numbers"]` | You must provide a list of phone numbers on your losing carrier's account that are not porting to Telnyx, and specify whether each should remain active or be deactivated after the port completes. |

Retrieve the porting order using the [GET /v2/porting\_orders/ endpoint](https://developers.telnyx.com/api-reference/porting-orders/retrieve-a-porting-order) and check the `additional_steps` field in the response.

## Associated phone numbers

This additional step applies to partial ports of GB local phone numbers. When porting only some phone numbers from an account, you must specify what happens to the remaining phone numbers on the losing carrier's account.

### When this step is required

The `associated_phone_numbers` step appears when both conditions are met:

* The porting order is for `GB` `local` phone numbers.
* The `port_type` is set to `partial_port`.

### How it works

You must provide a list of phone numbers on your losing carrier's account that are not being ported to Telnyx. For each phone number or range, you must indicate one of two outcomes:

* **Keep**: The phone number remains active with the losing carrier after the port completes.
* **Disconnect**: The phone number is disconnected from the losing carrier after the port completes.

If the billing telephone number (BTN) is included in the port, all remaining number ranges can only be disconnected.

### Completing this step

Use the [POST /v2/porting\_orders//associated\_phone\_numbers endpoint](https://developers.telnyx.com/api-reference/porting-orders/create-an-associated-phone-number) to specify ranges of phone numbers and their intended outcome (`keep` or `disconnect`). You can associate multiple number ranges by sending separate requests for each range.

The phone numbers you specify in this step are not being ported to Telnyx. This endpoint communicates what should happen to other phone numbers on the losing carrier's account. Without this information, the losing carrier will reject the porting order.

### Managing associated phone numbers

You can manage the phone numbers associated with your porting order using these endpoints:

| Action                            | Endpoint                                                                                                                                                |
| :-------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------ |
| List associated phone numbers     | [GET /v2/porting\_orders//associated\_phone\_numbers](https://developers.telnyx.com/api-reference/porting-orders/list-all-associated-phone-numbers)     |
| Remove an associated phone number | [DELETE /v2/porting\_orders//associated\_phone\_numbers/](https://developers.telnyx.com/api-reference/porting-orders/delete-an-associated-phone-number) |
