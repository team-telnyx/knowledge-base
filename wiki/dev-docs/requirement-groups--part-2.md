---
title: Requirement groups
summary: Requirement groups let you pre-fill and reuse regulatory requirement information
  across multiple number orders or porting orders. Each group is scoped to a specific
  country, phone number type, and action, and can optionally be submitted for pre-approval
  to enable automatic activation of orders that use it.
sources:
- url: https://developers.telnyx.com/docs/numbers/phone-numbers/requirement-groups
updated_at: 2026-08-05T13:59:46Z
---

# Requirement groups

*Part 2 of 2 — see also: [Part 1](requirement-groups--part-1.md)*

Requirement groups let you pre-fill and reuse regulatory requirement information across multiple number orders or porting orders. Each group is scoped to a specific country, phone number type, and action, and can optionally be submitted for pre-approval to enable automatic activation of orders that use it.

## How it works

### Step 1: Create a requirement group

Use the [POST /v2/requirement_groups endpoint](https://developers.telnyx.com/api-reference/requirement-groups/create-a-new-requirement-group) to create a requirement group. Each group requires `country_code` (ISO Alpha-2 format), `phone_number_type` (`local`, `toll_free`, `national`, `mobile`, or `shared_cost`), and `action` (`ordering` or `porting`).

Optionally include a `customer_reference` to label the requirement group for your own tracking purposes.

### Step 2: View the requirement group

List all requirement groups using [GET /v2/requirement_groups](https://developers.telnyx.com/api-reference/requirement-groups/list-requirement-groups), or retrieve a specific group by ID using [GET /v2/requirement_groups/:id](https://developers.telnyx.com/api-reference/requirement-groups/get-a-single-requirement-group-by-id).

The `regulatory_requirements` array lists each requirement that needs to be fulfilled for your order. Each requirement has a unique `requirement_id`. For detailed information about requirement types, see the [Regulatory requirements](regulatory-requirements.md) guide.

### Step 3: Fulfill the requirement group

Update the requirement group with values using [PATCH /v2/requirement_groups/:id](https://developers.telnyx.com/api-reference/requirement-groups/update-requirement-values-in-requirement-group). In the request body, specify each `requirement_id` and its associated value. For more information, check out the [Regulatory requirements](regulatory-requirements.md) guide.

### Step 4: Associate the requirement group with an order

You can associate a requirement group with number orders or porting orders.

**For new number orders:**

First, [search for available phone numbers](https://developers.telnyx.com/api-reference/phone-number-search/list-available-phone-numbers) and identify the number(s) you would like to purchase. Then create a number order using [POST /v2/number_orders](https://developers.telnyx.com/api-reference/phone-number-orders/create-a-number-order), including the `requirement_group_id` in each `phone_number` object. The requirement group values will populate the order and undergo regulatory review.

**For existing pending sub number orders:**

Update a `pending` sub number order using [POST /v2/sub_number_orders/:id/requirement_group](https://developers.telnyx.com/api-reference/requirement-groups/update-requirement-group-for-a-sub-number-order). Include the `requirement_group_id` in the request body.

When updating an existing order, the requirement group must be fulfilled. The request will only update non-approved requirements. If a requirement is already `approved`, its value remains unchanged.

**For porting orders:**

Associate a requirement group with a porting order using [PATCH /v2/porting_orders/:id](https://developers.telnyx.com/api-reference/porting-orders/edit-a-porting-order), including the `requirement_group_id` in the request body. This request can be performed when the order is in `draft`, `in-process`, or `exception` status. Any existing requirement values will be overwritten by the requirement group.

### Step 5 (Optional): Submit for pre-approval

To submit a requirement group for pre-approval, use the [POST /v2/requirement_groups/:id/submit_for_approval endpoint](https://developers.telnyx.com/api-reference/requirement-groups/submit-a-requirement-group-for-approval). The requirement group will transition to `pending-approval` status after submission.

Telnyx will review the submitted group. If all requirements are met, the group's `status` is set to `approved`. If requirements are rejected, the status will move to `declined`.

If the requirement group is rejected, Number Ops will communicate feedback via comments on the requirement group. You can view and respond to these comments using the comments API:

- [POST /v2/comments](https://developers.telnyx.com/api-reference/phone-number-orders/create-a-comment) to create a comment.
- [GET /v2/comments](https://developers.telnyx.com/api-reference/phone-number-orders/retrieve-all-comments) to retrieve all comments.

When using the comments API for requirement groups, set `comment_record_type` to `requirement_group` and `comment_record_id` to the `requirement_group_id`.

Once a requirement group is `approved`, associate the `requirement_group_id` with orders following the process described in Step 4.

## Webhook notifications

You can configure webhook notifications to receive updates about requirement group status changes. [Follow this support article](https://support.telnyx.com/en/articles/4277896-notification-settings) to set up webhook notifications.

Select the "Requirement Group Status Change" notification setting to receive webhooks when a requirement group transitions between statuses (e.g., from `pending-approval` to `approved` or `declined`).
