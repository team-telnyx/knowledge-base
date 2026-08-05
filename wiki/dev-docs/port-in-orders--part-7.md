---
title: Port-in orders
summary: Port-in orders transfer existing phone numbers from another carrier to Telnyx.
  This page covers the end-to-end port-in workflow via the V2 porting API, including
  creating and submitting orders, requesting FOC dates, on-demand activations, block
  and extension porting, bundle pre-configuration, messaging activation, cancellation,
  and webhook notifications and events.
sources:
- url: https://developers.telnyx.com/docs/numbers/porting/allowed-foc-dates
- url: https://developers.telnyx.com/docs/numbers/porting/bundles-porting
- url: https://developers.telnyx.com/docs/numbers/porting/cancel-port-order
- url: https://developers.telnyx.com/docs/numbers/porting/extensions
- url: https://developers.telnyx.com/docs/numbers/porting/getting-started
- url: https://developers.telnyx.com/docs/numbers/porting/messaging-porting
- url: https://developers.telnyx.com/docs/numbers/porting/on-demand-activations
- url: https://developers.telnyx.com/docs/numbers/porting/port-in-blocks
- url: https://developers.telnyx.com/docs/numbers/porting/port-in-events
- url: https://developers.telnyx.com/docs/numbers/porting/port-in-notifications
updated_at: 2026-08-05T14:01:21Z
---

# Port-in orders

*Part 7 of 8 — see also: [Part 1](port-in-orders--part-1.md), [Part 2](port-in-orders--part-2.md), [Part 3](port-in-orders--part-3.md), [Part 4](port-in-orders--part-4.md), [Part 5](port-in-orders--part-5.md), [Part 6](port-in-orders--part-6.md), [Part 8](port-in-orders--part-8.md)*

Port-in orders transfer existing phone numbers from another carrier to Telnyx. This page covers the end-to-end port-in workflow via the V2 porting API, including creating and submitting orders, requesting FOC dates, on-demand activations, block and extension porting, bundle pre-configuration, messaging activation, cancellation, and webhook notifications and events.

## Port-in order notifications

Telnyx offers port-in notifications for the following events:

1. Port order status changes
2. New comments
3. Split port orders
4. Messaging activation
5. Deleted "draft" porting orders

Notifications can be emitted to either email or webhook addresses.

### How to setup notifications via the Portal for all port orders (email and webhook)

If you are adding port-in notification settings in the portal, they will apply for all port orders that you create. Here is how to get started:

1. Sign in to the [Telnyx Portal](https://portal.telnyx.com/).
2. Go to your `Account Settings` and click on the `Advanced Features` section. Then select [Notifications](https://portal.telnyx.com/#/app/advanced-features/notifications).
3. Click on the `New Profile` button to create a new `Notification Profile`.
4. Click on the `New Channel` button to specify which email or webhook URL to send notifications to. Add as many notification channels as you would like.
5. Click on the `New Setting` button, select `Port In Notifications` and select the profile and channel that you would like Telnyx to send port-in notifications to.

If you have further questions, check out [this support article](https://support.telnyx.com/en/articles/4277896-notification-settings) or contact customer support.

### How to setup notifications on specific port orders (webhook only)

If your use case or integration requires each port order to have its own webhook URL for port-in notifications, you can specify a unique URL as the value for the `webhook_url` parameter in the port order form. This will allow you to receive notifications of updates to the specified order at the webhook URL you provided.

An example PATCH request:

```
curl --location --request PATCH 'https://api.telnyx.com/v2/porting_orders/{{id}}' \
--header 'Authorization: Bearer [REDACTED] \
--header 'Content-Type: application/json' \
--data-raw '{
    "webhook_url": "https://webhook.site/98e5e9e2-4921-4a64-b3c8-da0c6ce760f3"
}'
```

### Example webhook notification events

The following example payloads illustrate the structure of webhook events emitted during the port-in lifecycle.

**Transition to `in-process` status:**

```json
{
  "data": {
    "event_type": "porting_order.status_changed",
    "id": "8179f546-d479-42be-822b-8c78e1e89a59",
    "occurred_at": "2023-01-11T16:08:31.804886Z",
    "payload": {
      "customer_reference": "1-alpha-2-bravo-3-charlie",
      "id": "f6e10519-4664-4119-bb03-bbe73cf26ed3",
      "status": {
        "details": [],
        "value": "in-process"
      },
      "support_key": "sr_ac8c24",
      "updated_at": "2023-01-11T16:08:31.804886Z",
      "webhook_url": "https://example.com/porting_webhooks"
    },
    "record_type": "event"
  },
  "meta": {
    "attempt": 1,
    "delivered_to": "https://example.com/porting_webhooks"
  }
}
```

**Transition to `submitted` status:**

```json
{
  "data": {
    "event_type": "porting_order.status_changed",
    "id": "12ae614e-ed37-4a19-9fe3-2b69bf33d429",
    "occurred_at": "2021-01-19T19:52:13.874635Z",
    "payload": {
      "customer_reference": "1-alpha-2-bravo-3-charlie",
      "id": "3594c6c3-51a7-4306-b715-ca3765f13464",
      "status": {
        "details": [],
        "value": "submitted"
      },
      "support_key": "sr_98f022",
      "updated_at": "2021-03-19T19:52:13+00:00",
      "webhook_url": "https://example.com/porting_webhooks"
    },
    "record_type": "event"
  },
  "meta": {
    "attempt": 1,
    "delivered_to": "https://example.com/porting_webhooks"
  }
}
```

**Transition to `exception` status:** A port-in order can have multiple underlying exception reasons. When resolved, the order will transition back to a `submitted` status.

```json
{
  "data": {
    "event_type": "porting_order.status_changed",
    "id": "72322cb3-b6c6-46a4-a571-21a759c02da0",
    "occurred_at": "2021-01-19T19:51:37.844234Z",
    "payload": {
      "customer_reference": "1-alpha-2-bravo-3-charlie",
      "id": "3594c6c3-51a7-4306-b715-ca3765f13464",
      "status": {
        "details": [
          {
            "code": "ACCOUNT_NUMBER_MISMATCH",
            "description": "Account number does not match that on the CSR"
          },
          {
            "code": "PORTING_ORDER_SPLIT_REQUIRED",
            "description": "The OSP requires this Porting Order to be split map_exception_detail and submitted as separate orders"
          },
          {
            "code": "LOA_ILLEGIBLE",
            "description": "The LOA is illegible"
          }
        ],
        "value": "exception"
      },
      "support_key": "sr_98f022",
      "updated_at": "2021-03-19T19:51:37+00:00",
      "webhook_url": "https://example.com/porting_webhooks"
    },
    "record_type": "event"
  },
  "meta": {
    "attempt": 1,
    "delivered_to": "https://example.com/porting_webhooks"
  }
}
```

**Transition to `foc-date-confirmed` status:**

```json
{
  "data": {
    "event_type": "porting_order.status_changed",
    "id": "80227461-b684-4e89-a1a9-5055a2b4d8ef",
    "occurred_at": "2021-03-19T19:48:58.261079Z",
    "payload": {
      "customer_reference": "1-alpha-2-bravo-3-charlie",
      "id": "3594c6c3-51a7-4306-b715-ca3765f13464",
      "status": {
        "details": [],
        "value": "foc-date-confirmed"
      },
      "support_key": "sr_98f022",
      "updated_at": "2021-03-19T19:48:57+00:00",
      "webhook_url": "https://example.com/porting_webhooks"
    },
    "record_type": "event"
  },
  "meta": {
    "attempt": 1,
    "delivered_to": "https://example.com/porting_webhooks"
  }
}
```

**Transition to `ported` status:**

```json
{
  "data": {
    "event_type": "porting_order.status_changed",
    "id": "334e12a2-a016-489e-a2b6-7abb46637327",
    "occurred_at": "2021-03-19T19:48:58.261079Z",
    "payload": {
      "customer_reference": "1-alpha-2-bravo-3-charlie",
      "id": "3594c6c3-51a7-4306-b715-ca3765f13464",
      "status": {
        "details": [],
        "value": "ported"
      },
      "support_key": "sr_98f022",
      "updated_at": "2021-03-19T19:48:57+00:00",
      "webhook_url": "https://example.com/porting_webhooks"
    },
    "record_type": "event"
  },
  "meta": {
    "attempt": 1,
    "delivered_to": "https://example.com/porting_webhooks"
  }
}
```

**Transition to `cancel-pending` status:**

```json
{
  "data": {
    "event_type": "porting_order.status_changed",
    "id": "4f0c225d-3892-4e0e-9524-7625dfc20b19",
    "occurred_at": "2022-04-11T15:50:53.869432Z",
    "payload": {
      "customer_reference": "Test1234",
      "id": "f17074cb-72ee-48b4-bb45-64894e756f01",
      "status": {
        "details": [],
        "value": "cancel-pending"
      },
      "support_key": "sr_602ae7",
      "updated_at": "2022-04-11T15:50:52+00:00",
      "webhook_url": "https://example.com/porting_webhooks"
    },
    "record_type": "event"
  },
  "meta": {
    "attempt": 1,
    "delivered_to": "https://example.com/porting_webhooks"
  }
}
```

**Transition to `cancelled` status:**

```json
{
  "data": {
    "event_type": "porting_order.status_changed",
    "id": "6cac3a83-dc30-45a9-ab51-32e1882f4d04",
    "occurred_at": "2022-04-11T15:52:52.596025Z",
    "payload": {
      "customer_reference": "Test1234",
      "id": "f17074cb-72ee-48b4-bb45-64894e756f01",
      "status": {
        "details": [],
        "value": "cancelled"
      },
      "support_key": "sr_602ae7",
      "updated_at": "2022-04-11T15:52:47+00:00",
      "webhook_url": "https://example.com/porting_webhooks"
    },
    "record_type": "event"
  },
  "meta": {
    "attempt": 1,
    "delivered_to": "https://example.com/porting_webhooks"
  }
}
```

**New comment:**

```json
{
  "data": {
    "event_type": "porting_order.new_comment",
    "id": "6cafaed2-05f4-4791-9bcf-2392a0c912ef",
    "occurred_at": "2021-11-04T17:37:43.145988Z",
    "payload": {
      "comment": {
        "body": "Testing Webhooks 123",
        "id": "ca4b9cf6-d840-4ba9-ba38-95f4bc971164",
        "inserted_at": "2021-11-04T17:37:42Z",
        "user_id": null,
        "user_type": "admin"
      },
      "porting_order_id": "b3d55519-25c8-4af4-a50a-c92a9ddf7da4",
      "support_key": "sr_acdabe"
    },
    "record_type": "event"
  },
  "meta": {
    "attempt": 1,
    "delivered_to": "https://example.com/porting_webhooks"
  }
}
```

**Split port-in order:** You will receive one webhook for each number that is split from a port order and added to another port order. For example, if you originally submitted a port order with 5 numbers, and 3 numbers were split away from the original port order, then you would receive 3 split port order event notifications.

```json
{
  "data": {
    "event_type": "porting_order.split",
    "id": "a98be460-2d1e-42b7-8c0d-d516c352efd2",
    "occurred_at": "2021-11-15T19:37:37.131727Z",
    "payload": {
      "from": {
        "id": "a6efe074-0a3a-4522-8512-d0e004cf6c7d"
      },
      "to": {
        "id": "ef245340-da3d-4212-8769-1fa7672a675f"
      }
    },
    "record_type": "event"
  },
  "meta": {
    "attempt": 1,
    "delivered_to": "https://example.com/porting_webhooks"
  }
}
```

### Messaging activation

Enabling the messaging activation feature for your port order makes you eligible to receive `porting_order.messaging_changed` webhook events. If there is an issue with the messaging activation when the phone numbers port in, you will receive a webhook with `messaging_port_status: exception`:

```json
{
  "id": "626110d0-fab6-4a13-9183-3b331c41ccac",
  "event_type": "porting_order.messaging_changed",
  "occurred_at": "2022-01-01T00:00:00Z",
  "urls": ["https://testing.com/callback"],
  "organization_id": "dbdbc891-dc82-4c39-b9a1-e51e830c4352",
  "format": "v2",
  "payload": {
    "id": "ce2f4509-d166-4834-a0b9-e3ecb469a537",
    "customer_reference": "my_ref_001",
    "messaging": {
      "messaging_capable": true,
      "enable_messaging": true,
      "messaging_port_status": "exception"
    },
    "support_key": "sr_abc123"
  }
}
```

Once Telnyx validates that messaging successfully ported for all phone numbers on the port order, you will receive a webhook with `messaging_port_status: ported`:

```json
{
  "id": "626110d0-fab6-4a13-9183-3b331c41ccac",
  "event_type": "porting_order.messaging_changed",
  "occurred_at": "2022-01-01T00:00:00Z",
  "urls": ["https://testing.com/callback"],
  "organization_id": "dbdbc891-dc82-4c39-b9a1-e51e830c4352",
  "format": "v2",
  "payload": {
    "id": "ce2f4509-d166-4834-a0b9-e3ecb469a537",
    "customer_reference": "my_ref_001",
    "messaging": {
      "messaging_capable": true,
      "enable_messaging": true,
      "messaging_port_status": "ported"
    },
    "support_key": "sr_abc123"
  }
}
```

### Porting order deletion

A `draft` porting order may be deleted in two ways:

1. The user issues a `DELETE /porting_orders/{id}` [API request](https://developers.telnyx.com/api-reference/porting-orders/delete-a-porting-order).
2. The `draft` porting order is deleted automatically when it fails to be submitted within 30 days.

In either case, Telnyx will emit a webhook notification to communicate that the `draft` porting order has been deleted:

```json
{
  "id": "4da7b0e3-1a3c-4111-8335-dc436f6a0a00",
  "event_type": "porting_order.deleted",
  "occurred_at": "2023-01-01T00:00:00Z",
  "urls": ["https://example.com/webhook"],
  "organization_id": "dbdbc891-dc82-4c39-b9a1-e51e830c4352",
  "format": "v2",
  "payload": {
    "id": "74cc03c8-ab01-4887-bc31-9563e482d1e3",
    "customer_reference": "my_ref_123",
    "deleted_at": "2023-01-01T00:00:00Z"
  }
}
```
