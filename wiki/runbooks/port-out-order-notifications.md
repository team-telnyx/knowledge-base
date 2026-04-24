---
title: Port-Out Order Notifications
summary: Stay informed with Telnyx Port Out Notifications for seamless number port-out processes.
sources:
  - url: https://developers.telnyx.com/docs/numbers/porting/port-out-notifications/index
    content_hash: 526e45a20de6b7bffe48dbf52d306e090015c13efd3218b74e5a471df826858c
updated_at: 2026-04-10T00:00:00Z
---

# Port-Out Order Notifications

Stay informed with Telnyx Port Out Notifications for seamless number port-out processes. Access comprehensive documentation and resources to set up notifications and receive updates on the status of your port-out requests. Ensure smooth and efficient number porting with Telnyx's reliable notification system.

We understand the importance of being able to track the progress and status of your port orders. That is why we offer port-out notifications for the following events:

1. Port-out order status changes
2. New comments

Notifications can be emitted to either email or webhook addresses.

The following sections will discuss how to enable notification settings on your account, as well as provide example responses to the various webhook notification events.

## How to set up port-out notifications

If you are adding port-out notification settings in the portal, they will apply for all port orders that you create. Here is how to get started:

1. Sign in to the <a href="https://portal.telnyx.com/">Telnyx Portal</a>
2. Go to your `Account Settings` and click on the `Advanced Features` section. Then select <a href="https://portal.telnyx.com/#/app/advanced-features/notifications">Notifications</a>.
3. Click on the `New Profile` button to create a new `Notification Profile`
4. Click on the `New Channel` button to specify which email or webhook URL to send notifications to. Add as many notification channels as you would like!
5. Click on the `New Setting` button, select `Port Out Notifications` and select the profile and channel that you would like Telnyx to send port-out notifications to.

If you have further questions, check out <a href="https://support.telnyx.com/en/articles/4277896-notification-settings">
this support article
</a> or contact our customer support team.

## Example webhook notification events

### Transition to `pending` status

```json theme={null}
{
  "data": {
    "event_type": "portout.status_changed",
    "id": "3b19372e-38d4-4a9e-855f-a5a9ed5db4c2",
    "occurred_at": "2022-04-11T14:46:27Z",
    "payload": {
      "carrier_name": "Onvoy",
      "id": "477bf6c3-c6b9-478a-a035-33bd785d6ae7",
      "phone_numbers": [
        "{{phone_number}}"
      ],
      "spid": "073H",
      "status": "pending",
      "subscriber_name": null,
      "user_id": "40d68ba2-0847-4df2-be9c-b0e0cb673e75"
    },
    "record_type": "event"
  },
  "meta": {
    "attempt": 1,
    "delivered_to": "https://example.com/porting_webhooks"
  }
}
```

### Transition to `rejected-pending` status

```json theme={null}
{
  "data": {
    "event_type": "portout.status_changed",
    "id": "70d3c550-f4bd-4fa4-8502-d40d265355c4",
    "occurred_at": "2022-04-11T14:47:37Z",
    "payload": {
      "carrier_name": "Telnyx",
      "id": "477bf6c3-c6b9-478a-a035-33bd785d6ae7",
      "phone_numbers": [
        "{{phone_number}}"
      ],
      "rejection_reason": "Reason for rejection",
      "spid": "073H",
      "status": "rejected-pending",
      "subscriber_name": null,
      "user_id": "40d68ba2-0847-4df2-be9c-b0e0cb673e75"
    },
    "record_type": "event"
  },
  "meta": {
    "attempt": 1,
    "delivered_to": "https://example.com/porting_webhooks"
  }
}
```

### Transition to `rejected` status

```json theme={null}
{
  "data": {
    "event_type": "portout.status_changed",
    "id": "92db90da-409d-42bb-88a2-13741ac5f2cc",
    "occurred_at": "2022-04-11T14:48:02Z",
    "payload": {
      "carrier_name": "Telnyx",
      "id": "477bf6c3-c6b9-478a-a035-33bd785d6ae7",
      "phone_numbers": [
        "{{phone_number}}"
      ],
      "rejection_reason": "Reason for rejection",
      "spid": "073H",
      "status": "rejected",
      "subscriber_name": null,
      "user_id": "40d68ba2-0847-4df2-be9c-b0e0cb673e75"
    },
    "record_type": "event"
  },
  "meta": {
    "attempt": 1,
    "delivered_to": "https://example.com/porting_webhooks"
  }
}
```

### Transition to `canceled` status

```json theme={null}
{
  "data": {
    "event_type": "portout.status_changed",
    "id": "480fd3a5-c580-48c4-b724-84a3170fc043",
    "occurred_at": "2022-04-11T14:50:39Z",
    "payload": {
      "carrier_name": "Telnyx",
      "id": "d17ac097-fc58-41f4-aab3-6dcd16cafae9",
      "phone_numbers": [
        "{{phone_number}}"
      ],
      "spid": "073H",
      "status": "canceled",
      "subscriber_name": null,
      "user_id": "40d68ba2-0847-4df2-be9c-b0e0cb673e75"
    },
    "record_type": "event"
  },
  "meta": {
    "attempt": 1,
    "delivered_to": "https://example.com/porting_webhooks"
  }
}
```

### Transition to `authorized` status

```json theme={null}
{
  "data": {
    "event_type": "portout.status_changed",
    "id": "c147c471-e051-4cda-a547-c2f7e12b3445",
    "occurred_at": "2022-04-11T14:51:53Z",
    "payload": {
      "carrier_name": "Telnyx",
      "id": "b31bf5a7-cebb-4ae1-a34f-e3f6af550413",
      "phone_numbers": [
        "{{phone_number}}"
      ],
      "spid": "073H",
      "status": "authorized",
      "subscriber_name": null,
      "user_id": "40d68ba2-0847-4df2-be9c-b0e0cb673e75"
    },
    "record_type": "event"
  },
  "meta": {
    "attempt": 1,
    "delivered_to": "https://example.com/porting_webhooks"
  }
}
```

### Transition to `ported` status

```json theme={null}
{
  "data": {
    "event_type": "portout.status_changed",
    "id": "8ed7a709-3659-41fe-8c49-7af0037ebf2d",
    "occurred_at": "2022-04-11T14:53:39Z",
    "payload": {
      "carrier_name": "Telnyx",
      "id": "b31bf5a7-cebb-4ae1-a34f-e3f6af550413",
      "phone_numbers": [
        "{{phone_number}}"
      ],
      "spid": "073H",
      "status": "ported",
      "subscriber_name": null,
      "user_id": "40d68ba2-0847-4df2-be9c-b0e0cb673e75"
    },
    "record_type": "event"
  },
  "meta": {
    "attempt": 1,
    "delivered_to": "https://example.com/porting_webhooks"
  }
}
```

### New Comment

```json theme={null}
{
  "data": {
    "event_type": "portout.new_comment",
    "id": "0a9af296-a217-498c-a1ac-651a9fb0b2f5",
    "occurred_at": "2022-12-16T19:06:34Z",
    "payload": {
      "comment": "test comment",
      "id": "10ecb41e-c7b6-49a7-bf4a-23d8688b3ed6",
      "portout_id": "330f47af-4296-417a-84f6-05cec6ea5a8d",
      "user_id": "40d68ba2-0847-4df2-be9c-b0e0cb673e75"
    },
    "record_type": "event"
  },
  "meta": {
    "attempt": 1,
    "delivered_to": "https://webhook.site/98e5e9e2-4921-4a64-b3c8-da0c6ce760f3"
  }
}
```

### FOC Date change

If the gaining carrier requests a FOC date change, we will emit the following notification.

<Callout type="info">
  For port-out orders, the gaining carrier is allotted a grace period of 10 days, which means the gaining carrier can port the phone number at any point between the FOC date listed and the following 10 days.

While most port out orders are expected to occur on the listed FOC date, there is no guarantee that they will be completed on that day.

```json theme={null}
{
  "data": {
    "event_type": "portout.foc_date_changed",
    "id": "0a9af296-a217-498c-a1ac-651a9fb0b2f5",
    "occurred_at": "2022-12-16T19:06:34Z",
    "payload": {
      "foc_date": "2022-12-20T00:00:00Z",
      "id": "330f47af-4296-417a-84f6-05cec6ea5a8d",
      "user_id": "40d68ba2-0847-4df2-be9c-b0e0cb673e75"
    },
    "record_type": "event"
  },
  "meta": {
    "attempt": 1,
    "delivered_to": "https://webhook.site/98e5e9e2-4921-4a64-b3c8-da0c6ce760f3"
  }
}
```


## Related Pages

- [Port-in order notifications](../runbooks/port-in-order-notifications.md)
- [Port-out orders](../tutorial/port-out-orders.md)
- [Flutter Push Notifications](../runbooks/flutter-push-notifications.md)
- [Data Usage Notifications](../runbooks/data-usage-notifications.md)
- [iOS Push Notifications](../runbooks/ios-push-notifications.md)
