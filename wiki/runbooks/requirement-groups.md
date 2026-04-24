---
title: Requirement groups
summary: Manage and reuse regulatory requirements across multiple phone number orders by creating requirement groups.
sources:
  - url: https://developers.telnyx.com/docs/numbers/phone-numbers/requirement-groups/index
    content_hash: 94d97c95b7fce5ab933d22d21461196669ff408b6a7b24313e9e07e0eecd40e3
updated_at: 2026-04-10T00:00:00Z
---

# Requirement groups

Manage and reuse regulatory requirements across multiple phone number orders by creating requirement groups

## Overview

Requirement groups allow you to view, manage, and fulfill [regulatory requirements](https://developers.telnyx.com/docs/numbers/phone-numbers/regulatory-requirements) in advance for a particular order type. By creating a requirement group, you can pre-fill all necessary information and documentation just once, and then reuse this group across multiple orders.

Each requirement group is specific to a combination of `country_code`, `phone_number_type`, and `action` (ordering or porting). Once created and fulfilled, the group can be associated with any number order or porting order that matches those criteria. The pre-filled requirements are automatically applied to the order, which then undergoes the standard regulatory review process.

## Constraints

* Requirement groups are optional in most countries. You can [fulfill requirements individually on each order](https://developers.telnyx.com/docs/numbers/phone-numbers/regulatory-requirements) or use requirement groups to pre-fill requirements.
* In the following countries, it is mandatory to use fulfilled requirement groups when placing a number order: **CH (Switzerland)**, **DK (Denmark)**, **IT (Italy)**, **NO (Norway)**, **PT (Portugal)**, and **SE (Sweden)**.
* A **fulfilled** requirement group means that every requirement in the group has an associated value. You cannot create an order with an empty requirement group in countries where requirement groups are mandatory.
* Requirement groups can only be associated with orders that match the group's `country_code`, `phone_number_type`, and `action` combination. For example, a `DE` `local` `ordering` requirement group can only be applied to `DE` `local` number orders.
* Number orders do not automatically synchronize with requirement group changes. You must make another API request to apply updated requirement group values to existing orders.

## Requirement group statuses

Each requirement group has a status that indicates its current state and what review process orders using it will undergo. All requirement groups except `no-longer-eligible` can be used for orders.

| Status             | Description                                                                                                                                                                                                          |
| :----------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| unapproved         | Default status after creation. Has not been submitted for pre-approval. Orders using this group go through standard review.                                                                                          |
| pending-approval   | Submitted and under review. Orders using this group go through standard review.                                                                                                                                      |
| approved           | Passed review. Orders using this group activate automatically within a few minutes.                                                                                                                                  |
| declined           | One or more requirements were rejected during pre-approval. Orders using this group go through standard review. Expect similar rejections on orders using this group.                                                |
| expired            | Requirement(s) exceeded validity window. Orders using this group go through standard review. Expect similar rejections on orders using this group. Review `regulatory_requirements.expires_at` for expiration dates. |
| no-longer-eligible | Regulatory requirements have changed. Cannot be used for orders. Create a new requirement group with current requirements.                                                                                           |

## Pre-approval

By default, orders using requirement groups go through standard review, where Number Ops manually reviews the requirements on each individual order after it is placed. This review process can take time before numbers activate.

Pre-approval is an optional feature that allows you to submit a requirement group for review before placing orders. Once a requirement group is pre-approved, orders using it can activate automatically within a few minutes, bypassing the standard review process.

You do not need to pre-approve a requirement group to use it for ordering. Any requirement group (except `no-longer-eligible`) can be associated with orders immediately after creation and fulfillment.

**When to use pre-approval:**

Pre-approval makes sense when you will reuse the same requirement group for multiple orders AND you need quick number activation. Orders using `approved` requirement groups will activate automatically within a few minutes, bypassing the standard review process.

**When to skip pre-approval:**

If you're only using a requirement group for a few orders or don't need immediate activation, you can skip pre-approval entirely. Orders using `unapproved`, `pending-approval`, `declined`, or `expired` requirement groups will go through the standard review process.

**Pre-approval limitations:**

* **Country coverage**: Requirement group pre-approval is supported in most countries, but not all. Some countries, such as Italy, do not support pre-approval. If you attempt to submit a requirement group for pre-approval in a country where it is not supported, you will receive an error.
* **Address validation**: If the requirement group has an address requirement, ensure that ordered phone numbers comply with that address requirement. For example, if the requirement specifies an address matching the DID area code and the approved address is in Munich, order a phone number in Munich. Ordering a number in a different area (e.g., Berlin) will cause the order to undergo standard review instead of immediate activation. If the requirement specifies a national address, the address must be within the same country as the ordered phone number.

## How it works

### Step 1: Create a requirement group

Use the [POST /v2/requirement\_groups endpoint](https://developers.telnyx.com/api-reference/requirement-groups/create-a-new-requirement-group) to create a requirement group. Each group requires `country_code` (ISO Alpha-2 format), `phone_number_type` (`local`, `toll_free`, `national`, `mobile`, or `shared_cost`), and `action` (`ordering` or `porting`).

Optionally include a `customer_reference` to label the requirement group for your own tracking purposes.

### Step 2: View the requirement group

List all requirement groups using [GET /v2/requirement\_groups](https://developers.telnyx.com/api-reference/requirement-groups/list-requirement-groups), or retrieve a specific group by ID using [GET /v2/requirement\_groups/:id](https://developers.telnyx.com/api-reference/requirement-groups/get-a-single-requirement-group-by-id).

The `regulatory_requirements` array lists each requirement that needs to be fulfilled for your order. Each requirement has a unique `requirement_id`. For detailed information about requirement types, see the [regulatory requirements guide](https://developers.telnyx.com/docs/numbers/phone-numbers/regulatory-requirements).

### Step 3: Fulfill the requirement group

Update the requirement group with values using [PATCH /v2/requirement\_groups/:id](https://developers.telnyx.com/api-reference/requirement-groups/update-requirement-values-in-requirement-group). In the request body, specify each `requirement_id` and its associated value. For more information, check out the [regulatory requirements guide](https://developers.telnyx.com/docs/numbers/phone-numbers/regulatory-requirements).

### Step 4: Associate the requirement group with an order

You can associate a requirement group with number orders or porting orders.

**For new number orders:**

First, [search for available phone numbers](https://developers.telnyx.com/api-reference/phone-number-search/list-available-phone-numbers) and identify the number(s) you would like to purchase. Then create a number order using [POST /v2/number\_orders](https://developers.telnyx.com/api-reference/phone-number-orders/create-a-number-order), including the `requirement_group_id` in each `phone_number` object. The requirement group values will populate the order and undergo regulatory review.

**For existing pending sub number orders:**

Update a `pending` sub number order using [POST /v2/sub\_number\_orders/:id/requirement\_group](https://developers.telnyx.com/api-reference/requirement-groups/update-requirement-group-for-a-sub-number-order). Include the `requirement_group_id` in the request body.

When updating an existing order, the requirement group must be fulfilled. The request will only update non-approved requirements. If a requirement is already `approved`, its value remains unchanged.

**For porting orders:**

Associate a requirement group with a porting order using [PATCH /v2/porting\_orders/:id](https://developers.telnyx.com/api-reference/porting-orders/edit-a-porting-order), including the `requirement_group_id` in the request body. This request can be performed when the order is in `draft`, `in-process`, or `exception` status. Any existing requirement values will be overwritten by the requirement group.

### Step 5 (Optional): Submit for pre-approval

To submit a requirement group for pre-approval, use the [POST /v2/requirement\_groups/:id/submit\_for\_approval endpoint](https://developers.telnyx.com/api-reference/requirement-groups/submit-a-requirement-group-for-approval). The requirement group will transition to `pending-approval` status after submission.

Telnyx will review the submitted group. If all requirements are met, the group's `status` is set to `approved`. If requirements are rejected, the status will move to `declined`.

If the requirement group is rejected, Number Ops will communicate feedback via comments on the requirement group. You can view and respond to these comments using the comments API:

* [POST /v2/comments](https://developers.telnyx.com/api-reference/phone-number-orders/create-a-comment) to create a comment.
* [GET /v2/comments](https://developers.telnyx.com/api-reference/phone-number-orders/retrieve-all-comments) to retrieve all comments.

When using the comments API for requirement groups, set `comment_record_type` to `requirement_group` and `comment_record_id` to the `requirement_group_id`.

Once a requirement group is `approved`, associate the `requirement_group_id` with orders following the process described in Step 4.

## Webhook notifications

You can configure webhook notifications to receive updates about requirement group status changes. [Follow this support article](https://support.telnyx.com/en/articles/4277896-notification-settings) to set up webhook notifications.

Select the "Requirement Group Status Change" notification setting to receive webhooks when a requirement group transitions between statuses (e.g., from `pending-approval` to `approved` or `declined`).


## Related Pages

- [Insight Groups](../runbooks/insight-groups.md)
