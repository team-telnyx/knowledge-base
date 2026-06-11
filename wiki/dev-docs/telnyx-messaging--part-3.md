---
title: Telnyx Messaging
summary: Telnyx Messaging provides a comprehensive API for sending and receiving SMS
  and MMS messages, with features including messaging profiles, alphanumeric sender
  IDs, geomatching, group messaging, two-factor authentication, appointment reminders,
  advanced opt-in/out handling, configurable spend limits, hosted SMS, and detailed
  error handling.
sources:
- url: https://developers.telnyx.com/docs/messaging/messages/2fa/index
- url: https://developers.telnyx.com/docs/messaging/messages/advanced-opt-in-out/index
- url: https://developers.telnyx.com/docs/messaging/messages/alphanumeric-sender-id/index
- url: https://developers.telnyx.com/docs/messaging/messages/appointment-reminder
- url: https://developers.telnyx.com/docs/messaging/messages/configurable-spend-limits/index
- url: https://developers.telnyx.com/docs/messaging/messages/configuration-and-usage/index
- url: https://developers.telnyx.com/docs/messaging/messages/error-codes/index
- url: https://developers.telnyx.com/docs/messaging/messages/geomatch
- url: https://developers.telnyx.com/docs/messaging/messages/group-messaging
- url: https://developers.telnyx.com/docs/messaging/messages/hosted-sms/index
- url: https://developers.telnyx.com/docs/messaging/messages/hosted-sms/internal-transfer
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
