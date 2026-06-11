---
title: Number Porting
summary: Number porting at Telnyx covers both port-in orders (transferring phone numbers
  to Telnyx from another carrier) and port-out orders (when another carrier requests
  numbers away from your Telnyx account). The port-in process involves checking portability,
  creating and fulfilling orders, managing FOC dates, and optionally configuring messaging,
  bundles, extensions, and blocks. Port-out orders are initiated externally and require
  you to authorize or reject them. Both flows support webhook notifications and a
  queryable event history.
sources:
- url: https://developers.telnyx.com/docs/numbers/porting/allowed-foc-dates
  content_hash: c57d04ef8e55bf70f85d691716151e30f2269f5617cc5b890a08a3b02d8b97f7
- url: https://developers.telnyx.com/docs/numbers/porting/bundles-porting
  content_hash: 42415df5ca6fab87fb39deb17ad1095c7b17bcff8eb34205cb4cb045bdda5129
- url: https://developers.telnyx.com/docs/numbers/porting/cancel-port-order
  content_hash: f78fb88a5a55f83b02c1a393d324e00db0fa1d5ef7574f724a1fa95d151c72d3
- url: https://developers.telnyx.com/docs/numbers/porting/extensions
  content_hash: 5ccdea42739f096fff42a94c477bb735791253ef005b501201a62590f6527c6c
- url: https://developers.telnyx.com/docs/numbers/porting/getting-started/index
  content_hash: ba6cc1f079d5d8b5bf6edf528e15cb7966f54d483cf4355d45cef759c1dfb961
- url: https://developers.telnyx.com/docs/numbers/porting/messaging-porting
  content_hash: db74f412411b32614ca0191df8f2a8da628f2964cc6d4c27f6a2a649dd40f2ff
- url: https://developers.telnyx.com/docs/numbers/porting/on-demand-activations
  content_hash: 3e790c6cb3ba41b7580d5f87af025906ec71d6ab399bbd1dfca753fe9394ea91
- url: https://developers.telnyx.com/docs/numbers/porting/port-in-blocks
  content_hash: 35b440b6af71ff23b789929d8cfb955fae9e530fa73a9dc434d20a39ecda061c
- url: https://developers.telnyx.com/docs/numbers/porting/port-in-events
  content_hash: f3e4b2c3940588fc3b2266a2a9ca69b01a962f4ca5e1b6d87cf0ec33265003d8
- url: https://developers.telnyx.com/docs/numbers/porting/port-in-notifications
  content_hash: 4122729cf6748c535219fb6949b2794fa0383dd3e58160f098448159f24c06e5
- url: https://developers.telnyx.com/docs/numbers/porting/port-in-requirements
  content_hash: 12c93a7143e8dab1d4250af66007af051eb7dd70e83bc1ffafe2a7577f3abeac
- url: https://developers.telnyx.com/docs/numbers/porting/port-out-events
  content_hash: b52f2d40d95f86a5ea703fdd249fa76d568eb7f3da0ba05066aec6f9185bb35f
- url: https://developers.telnyx.com/docs/numbers/porting/port-out-notifications
  content_hash: c5a9cd86d7f047458f86c67ebebf504529c162d4685c3ffcb42754a629908460
- url: https://developers.telnyx.com/docs/numbers/porting/port-out-quickstart/index
  content_hash: cd0410d6fe502cc0e334002c3d91a0736a01d729700ece288fcb0fd238cdc7ce
- url: https://developers.telnyx.com/docs/numbers/porting/porting-additional-steps/index
  content_hash: 939ebc3a4092308abcc1b152f2d66a799afea7aa9c634ed3b51b3e0e3751913d
updated_at: 2026-06-11T10:40:42Z
---

# Number Porting

*Part 4 of 4 — see also: [Part 1](number-porting--part-1.md), [Part 2](number-porting--part-2.md), [Part 3](number-porting--part-3.md)*

Number porting at Telnyx covers both port-in orders (transferring phone numbers to Telnyx from another carrier) and port-out orders (when another carrier requests numbers away from your Telnyx account). The port-in process involves checking portability, creating and fulfilling orders, managing FOC dates, and optionally configuring messaging, bundles, extensions, and blocks. Port-out orders are initiated externally and require you to authorize or reject them. Both flows support webhook notifications and a queryable event history.

## Port-Out Orders

A port-out order is created when another carrier requests to transfer phone numbers away from your Telnyx account. Telnyx automatically creates the order in your account, and you can authorize or reject it.

Port-out orders require a response within 24–48 hours. If you do not respond, the port-out is automatically authorized and proceeds on the FOC date.

### Port-out order statuses

| Status | Description |
|---|---|
| `pending` | Request received; awaiting your review. |
| `authorized` | You approved the request; numbers will port on the FOC date. |
| `rejected-pending` | You submitted a rejection; Porting Ops is reviewing the reason. |
| `rejected` | Request formally rejected; will not proceed. |
| `canceled` | Request canceled by the gaining carrier or Telnyx. |
| `ported` | Numbers successfully ported to the gaining carrier. |

### Reviewing and responding

1. **Review** – Use `GET /v2/portouts` to list orders, or `GET /v2/portouts/{id}` for a specific order. Check `phone_numbers`, `carrier_name`, `requested_foc_date`, and subscriber information.
2. **Authorize** – Use `PATCH /v2/portouts/{id}/authorized` to approve the port-out.
3. **Reject** – First, retrieve eligible rejection codes with `GET /v2/portouts/rejections/{portout_id}`. Then use `PATCH /v2/portouts/{id}/rejected-pending` with the appropriate `rejection_code`. If using code `1001` ("Other"), you must include a `reason` field. The Porting Ops team validates the reason; if invalid, the order returns to `pending`.

### FOC date changes for port-outs

The gaining carrier is allotted a 10-day grace period, meaning they can port the number at any point between the listed FOC date and the following 10 days. Most port-outs occur on the listed FOC date, but there is no guarantee.

## Port-Out Notifications and Events

Port-out notifications can be sent via email or webhook for status changes and new comments.

### Setting up port-out notifications

1. Sign in to the [Telnyx Portal](https://portal.telnyx.com/).
2. Go to **Account Settings → Advanced Features → [Notifications](https://portal.telnyx.com/#/app/advanced-features/notifications)**.
3. Create a **New Profile**.
4. Add **New Channel(s)** for email or webhook URLs.
5. Add a **New Setting**, select **Port Out Notifications**, and choose the profile and channel.

### Port-out event types

| Event type | Description |
|---|---|
| `portout.status_changed` | The port-out order transitioned to a new status. |
| `portout.new_comment` | A new comment was added to the port-out order. |
| `portout.foc_date_changed` | The FOC date for the port-out was updated. |

### Querying and republishing port-out events

- **List events** – `GET /v2/portout/events` with optional filters by `portout_id`, event type, or date range.
- **Republish** – `POST /v2/portout/events/{id}/republish` resends notifications to currently subscribed channels without creating a new event.
