---
title: Advanced Orders
summary: Submit and track Advanced Order Requests when phone number searches return zero results - request Telnyx to acquire unavailable numbers on your behalf.
sources:
  - url: https://developers.telnyx.com/docs/numbers/phone-numbers/advanced-orders/index
    content_hash: 03da7c935ab32d625a17df54317740a7b800c163f339adfeda38651ae0a03697
updated_at: 2026-04-10T00:00:00Z
---

# Advanced Orders

Submit and track Advanced Order Requests when phone number searches return zero results - request Telnyx to acquire unavailable numbers on your behalf.

## **Overview**

When you search for numbers, four outcomes are possible:

1. The search returns available phone numbers that you can purchase.
2. The search targets a region where Telnyx has no coverage, resulting in a `4xx` response.
3. The request errors out due to a server issue (`5xx`) or a timeout.
4. Telnyx has coverage but no available numbers matching the given search criteria. This is when the Advanced Order Request API is useful.

In case (4), you can submit an Advanced Order request. Telnyx's Number Operations team will attempt to acquire the phone numbers that are currently unavailable. If successful, the team will order and activate the numbers on your account. This process is asynchronous.

## Constraints

* Not eligible for US or CA toll free phone numbers. The search API reflects all possible inventory.
* Not eligible for unique phone numbers (i.e. I request phone number 123-456-7890, I request a phone number that ends in 0000, etc.).
* Advanced orders are best effort. Telnyx cannot guarantee that we will be able to procure the phone numbers you request.

## Advanced Order Statuses

* **pending**: The Advanced Order has been created but is not yet being processed by Telnyx.
* **processing**: The Advanced Order is currently being processed by Telnyx.
* **exception**: There is an issue with the advanced order. Please review it and take the appropriate actions to resolve the issue.
* **hold**: Telnyx needs to replenish our inventory to fulfill your request. This process can take some time. No further action is needed on your end, the order will remain in this status until Telnyx is able to replenish those phone numbers.
* **ordered**: The Advanced Order has been successfully placed and fulfilled.
* **failed**: The Advanced Order could not be completed.

## **How it works**

### **1. Search for phone numbers to purchase**

First, search for your phone numbers using the `GET v2/available_phone_numbers` endpoint ([API reference here](https://developers.telnyx.com/api-reference/phone-number-search/list-available-phone-numbers), [developer guide here](https://developers.telnyx.com/docs/numbers/phone-numbers/number-search)).

If no results are returned, you can try to adjust your search filters to find similar phone numbers that are immediately available.

### **2. If no results are returned, create an Advanced Order**

If no results are returned for your search (even after attempting to find alternatives), create an Advanced Order using the `POST /v2/advanced_orders` endpoint ([API reference here](https://developers.telnyx.com/api-reference/advanced-number-orders/create-advanced-order)). In the body of the request, include the same values that you were using as search parameters previously.

### **3. Add regulatory requirements to an Advanced Order**

In most countries, our Number Ops team can only procure phone numbers if you provide the necessary regulatory requirements. In these cases, Number Ops will reach out and ask you to provide the applicable regulatory requirements.

1. Create a [requirement group](https://developers.telnyx.com/docs/numbers/phone-numbers/requirement-groups) that matches the "country" and "phone number type" of your Advanced Order.
2. Make a `PATCH https://api.telnyx.com/v2/advanced_orders/:order_id/requirement_group` request ([API reference here](https://developers.telnyx.com/api-reference/advanced-number-orders/update-advanced-order)). Use the requirement group `id` as the "requirement\_group\_id" value in the request body.
3. If you need to edit the requirements associated with the Advanced Order, edit them on the requirement group first. Then `PATCH v2/advanced_orders/:order_id/requirement_group` the Advanced Order again. The updated requirements will override the original ones you submitted.

After you PATCH the order with a fulfilled requirement group, the `advanced_order_requirements` array will contain the values from your requirement group.

### **4. Finish the number ordering process**

When an Advanced Order transitions to `ordered` status, Number Ops has placed number order(s) on your account for the requested phone numbers.

Check the `orders` array in the Advanced Order API response to see which number orders were placed. The `orders` array lists the Number Order IDs for the orders that were placed.

You can then use the `GET v2/number_orders/:number_order_id` request ([API reference here](https://developers.telnyx.com/api-reference/phone-number-orders/retrieve-a-number-order)) to:

* View details about the actual number order that was placed.
* View which phone numbers were ordered.
* View the status of the order.
* View if there are any regulatory requirements to be fulfilled.

At this point, treat these new number orders like any other number order. It may require further actions by you to complete the order.

## **Comments**

You can communicate with the Number Operations team about your request through the Comments API. Use `filter[comment_record_type]=advanced_number_order` and specify the advanced order ID as the `comment_record_id` in the API requests.

* [View comments](https://developers.telnyx.com/api-reference/phone-number-orders/retrieve-all-comments)
* [Create a comment](https://developers.telnyx.com/api-reference/phone-number-orders/create-a-comment)

## **Notifications**

You can set up email and/or webhook notifications for your Advanced Orders. These notifications provide status updates on your requests. [Follow this guide](https://support.telnyx.com/en/articles/4277896-notification-settings) to learn more about configuring notifications.

### **Webhook events**

**Advanced Order is created:**

```
{
  "data": {
    "event_type": "advanced_order.status_update",
    "id": "83996511-474b-4cbe-afc3-14c9c0144404",
    "occurred_at": "2025-09-23T20:18:04.789361Z",
    "payload": {
      "new_status": "pending",
      "old_status": "created",
      "order_id": "a6d6633e-824b-4042-a2b7-5ac0cccd799b"
    },
    "record_type": "event"
  },
  "meta": {
    "attempt": 1,
    "delivered_to": "https://webhook.site/a61372df-394b-4c61-a601-79b35421824a"
  }
}
```

**Transition from pending to processing:**

```
{
  "data": {
    "event_type": "advanced_order.status_update",
    "id": "e5704883-c9d5-40f4-b089-d48495b1e14e",
    "occurred_at": "2025-09-23T20:36:40.616041Z",
    "payload": {
      "new_status": "processing",
      "old_status": "pending",
      "order_id": "a6d6633e-824b-4042-a2b7-5ac0cccd799b"
    },
    "record_type": "event"
  },
  "meta": {
    "attempt": 1,
    "delivered_to": "https://webhook.site/a61372df-394b-4c61-a601-79b35421824a"
  }
}
```

**Transition from one status (in this example, processing) into hold:**

```
{
  "data": {
    "event_type": "advanced_order.status_update",
    "id": "ac65655a-897d-439e-8fe7-32a5c3fc5f13",
    "occurred_at": "2025-11-26T18:42:40.436059Z",
    "payload": {
      "new_status": "hold",
      "old_status": "processing",
      "order_id": "44b6f0f6-6a0c-412b-b015-55e3c2df47c6"
    },
    "record_type": "event"
  },
  "meta": {
    "attempt": 3,
    "delivered_to": "https://webhook.site/c9b32d02-db83-4af1-ab86-b8acdd8daabf"
  }
}
```

**Transition from one status (in this example, hold) into exception:**

```
{
  "data": {
    "event_type": "advanced_order.status_update",
    "id": "f4252145-9f49-4c4a-bb1f-028a387dfc50",
    "occurred_at": "2025-11-26T18:42:46.867446Z",
    "payload": {
      "new_status": "exception",
      "old_status": "hold",
      "order_id": "44b6f0f6-6a0c-412b-b015-55e3c2df47c6"
    },
    "record_type": "event"
  },
  "meta": {
    "attempt": 3,
    "delivered_to": "https://webhook.site/c9b32d02-db83-4af1-ab86-b8acdd8daabf"
  }
}
```

**Transition from one status (in this example, processing) into ordered:**

```
{
  "data": {
    "event_type": "advanced_order.status_update",
    "id": "b2f454f0-99b8-45df-81e6-1384f4233549",
    "occurred_at": "2025-09-23T20:38:19.742838Z",
    "payload": {
      "new_status": "ordered",
      "old_status": "processing",
      "order_id": "a6d6633e-824b-4042-a2b7-5ac0cccd799b"
    },
    "record_type": "event"
  },
  "meta": {
    "attempt": 1,
    "delivered_to": "https://webhook.site/a61372df-394b-4c61-a601-79b35421824a"
  }
}
```

**Transition from one status (in this example, processing) into failed:**

```
{
  "data": {
    "event_type": "advanced_order.status_update",
    "id": "607d5f1b-2763-4dd1-8ced-ebf786f70996",
    "occurred_at": "2025-09-23T20:39:10.729398Z",
    "payload": {
      "new_status": "failed",
      "old_status": "processing",
      "order_id": "7c179258-e676-4844-81a4-a6cb626075db"
    },
    "record_type": "event"
  },
  "meta": {
    "attempt": 1,
    "delivered_to": "https://webhook.site/a61372df-394b-4c61-a601-79b35421824a"
  }
}
```

**New Comment:**

```
{
  "data": {
    "event_type": "advanced_order.new_comment",
    "id": "236a47ea-ac71-4df0-aa3e-55f249c72818",
    "occurred_at": "2025-09-23T20:38:07.990291Z",
    "payload": {
      "advanced_order_id": "a6d6633e-824b-4042-a2b7-5ac0cccd799b",
      "comment": "This is an admin comment"
    },
    "record_type": "event"
  },
  "meta": {
    "attempt": 1,
    "delivered_to": "https://webhook.site/a61372df-394b-4c61-a601-79b35421824a"
  }
}
```


## Related Pages

- [Number Orders](../runbooks/number-orders.md)
