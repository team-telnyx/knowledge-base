---
title: Telnyx Messaging
summary: Telnyx Messaging provides a comprehensive API for sending and receiving SMS
  and MMS messages, with features including messaging profiles, alphanumeric sender
  IDs, geomatching, group messaging, two-factor authentication, appointment reminders,
  advanced opt-in/out handling, configurable spend limits, hosted SMS, and detailed
  error handling.
sources:
- url: https://developers.telnyx.com/docs/messaging/messages/2fa/index
  content_hash: e660dfc64ea2a2d6911f7d1a970f5a932c04da65aae78776e3c1ca3b18448b6d
- url: https://developers.telnyx.com/docs/messaging/messages/advanced-opt-in-out/index
  content_hash: 5fd82d8d9312b6ac6e28c0c73d0a00bf774769a0dd423127c48f73f591d7b3b9
- url: https://developers.telnyx.com/docs/messaging/messages/alphanumeric-sender-id/index
  content_hash: abbae58584ee6800d04c5231b8e3b77d97f8af428a35e1c1433eb2378e318112
- url: https://developers.telnyx.com/docs/messaging/messages/appointment-reminder
  content_hash: 6985fd062cf97e7e1fbaad7066a3bf2314c4f3753dd0115043ce47f104d1701e
- url: https://developers.telnyx.com/docs/messaging/messages/configurable-spend-limits/index
  content_hash: 3debaf7e27ff822d9bbebe435006ae4d2d6d8b93ce63335ec32a07d69af3b79f
- url: https://developers.telnyx.com/docs/messaging/messages/configuration-and-usage/index
  content_hash: 1689fb1fb284ac9037440148c10c18cf7db9961ed4a23dc6b836eadbc54eb215
- url: https://developers.telnyx.com/docs/messaging/messages/error-codes/index
  content_hash: e1967e40b4a047d11b5125f1a52bc6d4e705bb3c9091fea33b0be3327dce7b6e
- url: https://developers.telnyx.com/docs/messaging/messages/geomatch
  content_hash: 482afc03676e3bc869ddc8ddcdc2e664b63ccf582eee0d99dc25181db71831b7
- url: https://developers.telnyx.com/docs/messaging/messages/group-messaging
  content_hash: 39a6ee872f771c4a346c0ea1af391c578a9a69489623cf565ace914e877ab528
- url: https://developers.telnyx.com/docs/messaging/messages/hosted-sms/index
  content_hash: 183a7b2c87a6b2c0609b46d90d10746ff0ec211ef8ba7a7b4d481130f51b73ba
- url: https://developers.telnyx.com/docs/messaging/messages/hosted-sms/internal-transfer
  content_hash: 178148332abbc910363f6baca179c2f8701f9fae87ddda430a5727b8c5bddc83
updated_at: 2026-06-11T10:36:31Z
---

# Telnyx Messaging

*Part 3 of 4 — see also: [Part 1](telnyx-messaging--part-1.md), [Part 2](telnyx-messaging--part-2.md), [Part 4](telnyx-messaging--part-4.md)*

Telnyx Messaging provides a comprehensive API for sending and receiving SMS and MMS messages, with features including messaging profiles, alphanumeric sender IDs, geomatching, group messaging, two-factor authentication, appointment reminders, advanced opt-in/out handling, configurable spend limits, hosted SMS, and detailed error handling.

## Hosted SMS

Hosted SMS lets you add messaging capabilities to phone numbers that stay with your current voice provider. Your voice service continues uninterrupted — Telnyx handles only the SMS and MMS routing. This is ideal for landline numbers needing texting, business numbers where you want to keep your voice provider, or gradual migration.

Hosting a number is **not** the same as porting. Your voice service stays with your current provider.

### Order Process

| Step | What Happens | Timeline |
|---|---|---|
| 1. Eligibility check | Verify numbers can be hosted | Instant |
| 2. Create order | Submit a hosted SMS order | Instant |
| 3. Verify ownership | Confirm you own the numbers via SMS code | 5 minutes |
| 4. Upload documents | Submit LOA and recent provider bill | Instant |
| 5. Telnyx review | Team reviews and activates | 1–3 business days |

### Eligibility Statuses

Key statuses include `eligible`, `number_is_not_a_us_number` (only US numbers supported), `number_can_not_be_wireless`, `number_can_not_be_in_telnyx` (already on Telnyx), and various billing/format errors.

### Verification

Request verification codes via `POST /v2/messaging_hosted_number_orders/{order_id}/verification_codes`, then submit them via `POST /v2/messaging_hosted_number_orders/{order_id}/validation_codes`. Successful verification changes status to `ownership_successful`.

### Document Upload

Upload a Letter of Authorization (LOA) and a recent bill as PDFs. Telnyx reviews and activates, typically within 1–3 business days.

### Order Statuses

| Status | Meaning |
|---|---|
| `pending` | Awaiting verification and documents |
| `loa_file_successful` | Documents uploaded successfully |
| `successful` | Numbers are active |
| `failed` | Activation failed |
| `deleted` | Order was cancelled |

### Webhook Notifications

Hosted SMS orders trigger webhooks including `messaging_hosted_numbers_orders.created`, `.updated`, `.deleted`, and internal transfer-specific events (see below).

### Troubleshooting Failed Orders

- **carrier_rejected** — losing carrier rejected the request; contact your voice provider
- **ineligible_carrier** — carrier doesn't support hosted SMS; consider full porting
- **failed_carrier_rejected** — specific number rejected; check account ownership
- **failed_number_already_hosted** — already hosted by another account; contact support
- **failed_timeout** — activation timed out; create a new order
- **Verification code not received** — ensure the number can receive SMS; request the code again
- **LOA rejected** — download the latest template; ensure signer matches account holder
- **Hosted numbers not visible in Portal** — known limitation; use the API to list hosted numbers

## Internal Hosted SMS Transfer

Internal Hosted SMS Transfer allows moving messaging-enabled numbers between two Telnyx accounts without standard carrier porting. This is useful when managing multiple accounts, consolidating numbers, or migrating messaging between organizations.

Internal transfers are automatically detected when the number(s) in your hosted SMS order already belong to another Telnyx account.

### Transfer Flow

1. **Create hosted SMS order** — the system automatically detects that the number belongs to another Telnyx account and flags it as an internal transfer
2. **Current owner is notified** — via email and portal notification with approval link
3. **Approval window (72 hours)** — the current owner can approve or reject; if no action, transfer is auto-approved
4. **Verify ownership (2FA)** — the receiving account must complete phone number ownership verification
5. **Upload documents** — submit LOA and recent bill
6. **Activation** — Telnyx team reviews and activates; the number's `user_id` is updated to the new account

When a number is internally transferred, any **10DLC campaign registrations** are automatically deleted. The receiving account must re-register the number with a campaign after the transfer completes.

### Approve or Reject

The current owner uses the link in their notification email or the API. The `token` parameter is a one-time use token that expires after 72 hours.

| Decision | Result |
|---|---|
| Approved | Transfer proceeds; receiving account must complete 2FA and document upload |
| Rejected | Order marked as `failed`; receiving account is notified |
| No action (72h) | Transfer is auto-approved; receiving account must still complete verification |

### Lifecycle Webhook Events

| Event | Fired When |
|---|---|
| `messaging_hosted_numbers_orders.internal_transfer_detected` | Order classified as internal transfer |
| `messaging_hosted_numbers_orders.internal_transfer_approval_requested` | Approval requested, 72h window started |
| `messaging_hosted_numbers_orders.internal_transfer_approved` | Losing account approved |
| `messaging_hosted_numbers_orders.internal_transfer_rejected` | Losing account rejected, or receiving account cancelled |
| `messaging_hosted_numbers_orders.internal_transfer_auto_approved` | 72h elapsed with no response, or bypass allowlist |
