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

*Part 1 of 2 — see also: [Part 2](requirement-groups--part-2.md)*

Requirement groups let you pre-fill and reuse regulatory requirement information across multiple number orders or porting orders. Each group is scoped to a specific country, phone number type, and action, and can optionally be submitted for pre-approval to enable automatic activation of orders that use it.

## Overview

Requirement groups allow you to view, manage, and fulfill [Regulatory requirements](regulatory-requirements.md) in advance for a particular order type. By creating a requirement group, you can pre-fill all necessary information and documentation just once, and then reuse this group across multiple orders.

Each requirement group is specific to a combination of `country_code`, `phone_number_type`, and `action` (ordering or porting). Once created and fulfilled, the group can be associated with any number order or porting order that matches those criteria. The pre-filled requirements are automatically applied to the order, which then undergoes the standard regulatory review process.

## Constraints

- Requirement groups are optional in most countries. You can [fulfill requirements individually on each order](https://developers.telnyx.com/docs/numbers/phone-numbers/regulatory-requirements) or use requirement groups to pre-fill requirements.
- In the following countries, it is mandatory to use fulfilled requirement groups when placing a number order: **CH (Switzerland)**, **DK (Denmark)**, **IT (Italy)**, **NO (Norway)**, **PT (Portugal)**, and **SE (Sweden)**.
- A **fulfilled** requirement group means that every requirement in the group has an associated value. You cannot create an order with an empty requirement group in countries where requirement groups are mandatory.
- Requirement groups can only be associated with orders that match the group's `country_code`, `phone_number_type`, and `action` combination. For example, a `DE` `local` `ordering` requirement group can only be applied to `DE` `local` number orders.
- Number orders do not automatically synchronize with requirement group changes. You must make another API request to apply updated requirement group values to existing orders.

## Requirement group statuses

Each requirement group has a status that indicates its current state and what review process orders using it will undergo. All requirement groups except `no-longer-eligible` can be used for orders.

| Status | Description |
| --- | --- |
| unapproved | Default status after creation. Has not been submitted for pre-approval. Orders using this group go through standard review. |
| pending-approval | Submitted and under review. Orders using this group go through standard review. |
| approved | Passed review. Orders using this group activate automatically within a few minutes. |
| declined | One or more requirements were rejected during pre-approval. Orders using this group go through standard review. Expect similar rejections on orders using this group. |
| expired | Requirement(s) exceeded validity window. Orders using this group go through standard review. Expect similar rejections on orders using this group. Review `regulatory_requirements.expires_at` for expiration dates. |
| no-longer-eligible | Regulatory requirements have changed. Cannot be used for orders. Create a new requirement group with current requirements. |

## Pre-approval

By default, orders using requirement groups go through standard review, where Number Ops manually reviews the requirements on each individual order after it is placed. This review process can take time before numbers activate.

Pre-approval is an optional feature that allows you to submit a requirement group for review before placing orders. Once a requirement group is pre-approved, orders using it can activate automatically within a few minutes, bypassing the standard review process.

You do not need to pre-approve a requirement group to use it for ordering. Any requirement group (except `no-longer-eligible`) can be associated with orders immediately after creation and fulfillment.

**When to use pre-approval:**

Pre-approval makes sense when you will reuse the same requirement group for multiple orders AND you need quick number activation. Orders using `approved` requirement groups will activate automatically within a few minutes, bypassing the standard review process.

**When to skip pre-approval:**

If you're only using a requirement group for a few orders or don't need immediate activation, you can skip pre-approval entirely. Orders using `unapproved`, `pending-approval`, `declined`, or `expired` requirement groups will go through the standard review process.

**Pre-approval limitations:**

- **Country coverage**: Requirement group pre-approval is supported in most countries, but not all. Some countries, such as Italy, do not support pre-approval. If you attempt to submit a requirement group for pre-approval in a country where it is not supported, you will receive an error.
- **Address validation**: If the requirement group has an address requirement, ensure that ordered phone numbers comply with that address requirement. For example, if the requirement specifies an address matching the DID area code and the approved address is in Munich, order a phone number in Munich. Ordering a number in a different area (e.g., Berlin) will cause the order to undergo standard review instead of immediate activation. If the requirement specifies a national address, the address must be within the same country as the ordered phone number.
