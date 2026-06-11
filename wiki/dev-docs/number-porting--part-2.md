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

*Part 2 of 4 — see also: [Part 1](number-porting--part-1.md), [Part 3](number-porting--part-3.md), [Part 4](number-porting--part-4.md)*

Number porting at Telnyx covers both port-in orders (transferring phone numbers to Telnyx from another carrier) and port-out orders (when another carrier requests numbers away from your Telnyx account). The port-in process involves checking portability, creating and fulfilling orders, managing FOC dates, and optionally configuring messaging, bundles, extensions, and blocks. Port-out orders are initiated externally and require you to authorize or reject them. Both flows support webhook notifications and a queryable event history.

## On-Demand Activations

On-demand activations give you control over when ported numbers activate on the FOC date. Instead of automatic activation at a carrier-assigned time, you trigger activation yourself within a designated window.

If you don't initiate activation during the window, numbers automatically port at the end of the window, ensuring the order completes even if you miss the manual trigger.

### Constraints

- Only available for orders where `fast_port_eligible` is `true`.
- Currently available for US and Canada only.
- You can only initiate activation after the order reaches `foc-date-confirmed` status.
- Activation must occur within the designated window on the FOC date.

### Activation windows

| Country | Window start | Window end | Duration |
|---|---|---|---|
| US | 6:00 AM CT | 8:00 PM CT | 14 hours |
| Canada | 8:00 AM CT | 3:00 PM CT | 7 hours |

When the order reaches `foc-date-confirmed`, an activation job is created. The `activation_windows` array in the job response shows exact `start_at` and `end_at` times. The `activate_at` field defaults to the window end; it updates when you trigger on-demand activation.

### Activation job statuses

| Status | Description |
|---|---|
| `created` | Waiting for the activation window to open. |
| `in-process` | Activation initiated; numbers being ported. |
| `completed` | Activation finished; numbers active on Telnyx. |

### Enabling and triggering

1. Set `activation_settings.activation_type` to `on-demand` using the [Edit porting order endpoint](https://developers.telnyx.com/api-reference/porting-orders/edit-a-porting-order).
2. After `foc-date-confirmed`, retrieve the activation window via the [List porting activation jobs endpoint](https://developers.telnyx.com/api-reference/porting-orders/list-all-porting-activation-jobs).
3. Within the window, trigger the port using the [Activate porting order endpoint](https://developers.telnyx.com/api-reference/porting-orders/activate-every-number-in-a-porting-order-asynchronously).
4. Monitor progress via activation job status or [porting notifications](https://developers.telnyx.com/docs/numbers/porting/port-in-notifications).

## Messaging Porting

For US and Canada local and toll-free numbers, porting voice and porting messaging are separate processes. A `ported` status means voice has ported; it does not reflect messaging status.

Messaging routing is controlled by a NetNumber ID (NNID). In most cases both voice and messaging port simultaneously at the FOC date, but if the losing carrier fails to release the NNID, messaging continues through them after voice has ported. Telnyx provides visibility into messaging port status and automatically escalates issues.

### Constraints

- Messaging porting tracking is only applicable to US and Canada local and toll-free numbers.
- `messaging_capable` must be `true` on the porting order.
- A `messaging_profile_id` must be assigned when enabling messaging activation.
- Numbers from other countries port messaging and voice simultaneously.

### Messaging port statuses

The `messaging_port_status` field tracks messaging activation independently from the main order `status`:

| Status | Description |
|---|---|
| `pending` | Messaging activation is enabled but the FOC date has not yet been reached. |
| `activating` | Voice has ported; Telnyx is verifying messaging activation. |
| `ported` | Messaging has successfully ported to Telnyx. |
| `exception` | Messaging failed to port automatically; Telnyx is escalating with the losing carrier. |
| `not_applicable` | Messaging activation was not enabled. |

### Enabling messaging activation

1. Verify `messaging_capable` is `true` via a portability check or the order's `messaging` object.
2. Update the order with `enable_messaging: true` in the `messaging` object and assign a `messaging_profile_id` in `phone_number_configuration`. The order must be in `draft`, `in-process`, or `exception` status.
3. Monitor `messaging_port_status`. If it reaches `exception`, Telnyx automatically escalates—resolution typically occurs within 72 hours for local numbers and up to 5 business days for toll-free.

### Partial messaging ports

When an order contains multiple numbers, some may port messaging successfully while others do not. If any number fails, the order-level `messaging_port_status` is `exception`. Check individual number status via `GET /v2/porting_orders/{id}/associated_phone_numbers`.

### Hosted SMS alternative

To avoid messaging downtime, you can port SMS before voice via a Hosted SMS request:

1. Submit a Hosted SMS request at least 4 business days before the scheduled FOC date.
2. Create a porting order with a FOC date at least 4 business days out.
3. Once the Hosted SMS request completes, SMS routes through Telnyx while voice remains with the losing carrier.
4. When the FOC date arrives, voice ports and both services route through Telnyx with no downtime.

See the [Hosted SMS messaging process](https://support.telnyx.com/en/articles/5336668-hosted-sms-messaging-process) support article.

### Messaging timing expectations

- **US/Canada local**: ~90% activate within 10 minutes; remainder typically within 1–2 business days.
- **US/Canada toll-free**: usually within 10 minutes; if not, resolution may take 4–5 business days.
- **Other countries**: messaging ports simultaneously with voice.

### Porting voice only

To port only voice, leave `enable_messaging` as `null` and do not assign a `messaging_profile_id`. The `messaging_port_status` remains `not_applicable` and Telnyx does not attempt to override the NNID.

## Bundle Pre-Configuration

Bundle pre-configuration lets you associate bundles with phone numbers on a porting order before those numbers are active at Telnyx. When the port completes, the pre-configured bundles are automatically applied.

### Constraints

- Only available via API.
- Bundles can be pre-configured or updated at any point before the order reaches `ported` or `cancelled` status.
- Each bundle can only be associated with one phone number; if a pre-configured bundle is used elsewhere before the port completes, the assignment fails.
- Up to 20 phone numbers per API request.
- The bundle must be valid for the phone number type and characteristics.
- Pre-configuring bundles is optional—you can configure some, all, or none of the numbers.

### Steps

1. **Verify available bundles** – Use `GET /v2/bundle-pricing/user_bundles` or view bundles in the [Mission Control Portal](https://portal.telnyx.com/#/app/bundles). A bundle is available if its `resources` array is empty.
2. **Get porting phone number IDs** – Use `GET /v2/porting_phone_numbers` filtered by your porting order ID to retrieve each number's `porting_phone_number_id`.
3. **Pre-configure bundles** – Use `POST /v2/porting_orders/phone_number_configurations` with `porting_phone_number_id` and `user_bundle_id` for each association.
4. **Verify configurations** – Use `GET /v2/porting_orders/phone_number_configurations` to view which bundles are pre-configured with which numbers.
