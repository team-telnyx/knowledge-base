---
title: 'Telnyx Number Porting: Port‑In and Port‑Out'
summary: End‑to‑end guide to porting phone numbers with Telnyx, covering port‑in and
  port‑out workflows, FOC dates, FastPort on‑demand activations, messaging activation
  and tracking, regulatory requirements, German extensions and blocks, bundle pre‑configuration,
  cancellations, notifications, and events.
sources:
- url: https://developers.telnyx.com/docs/numbers/porting/allowed-foc-dates
- url: https://developers.telnyx.com/docs/numbers/porting/bundles-porting
- url: https://developers.telnyx.com/docs/numbers/porting/cancel-port-order
- url: https://developers.telnyx.com/docs/numbers/porting/extensions
- url: https://developers.telnyx.com/docs/numbers/porting/getting-started/index
- url: https://developers.telnyx.com/docs/numbers/porting/messaging-porting
- url: https://developers.telnyx.com/docs/numbers/porting/on-demand-activations
- url: https://developers.telnyx.com/docs/numbers/porting/port-in-blocks
- url: https://developers.telnyx.com/docs/numbers/porting/port-in-events
- url: https://developers.telnyx.com/docs/numbers/porting/port-in-notifications
- url: https://developers.telnyx.com/docs/numbers/porting/port-in-requirements
- url: https://developers.telnyx.com/docs/numbers/porting/port-out-events
- url: https://developers.telnyx.com/docs/numbers/porting/port-out-notifications
- url: https://developers.telnyx.com/docs/numbers/porting/port-out-quickstart/index
- url: https://developers.telnyx.com/docs/numbers/porting/porting-additional-steps/index
updated_at: 2026-05-20T09:24:58Z
---

# Telnyx Number Porting: Port‑In and Port‑Out

*Part 2 of 2 — see also: [Part 1](telnyx-number-porting-portin-and-portout--part-1.md)*

End‑to‑end guide to porting phone numbers with Telnyx, covering port‑in and port‑out workflows, FOC dates, FastPort on‑demand activations, messaging activation and tracking, regulatory requirements, German extensions and blocks, bundle pre‑configuration, cancellations, notifications, and events.

## Canceling a port‑in order
- Use the cancel action to request cancellation. Status flows cancel‑pending → cancelled after Porting Ops review.
- You cannot cancel via API within 48 hours of the FOC date/time; contact support for late cancellations.
- Cancelled orders cannot be reactivated; create a new order if needed.

## Monitoring, notifications, and events
- Webhooks and email
  - Configure Port In Notifications to receive:
    - Status changes (draft/submitted/in‑process/exception/foc‑date‑confirmed/ported/cancel‑pending/cancelled)
    - New comments from Porting Ops
    - Order splits
    - Messaging activation changes
    - Deletions of draft orders (manual or 30‑day auto‑cleanup)
  - Optionally set a per‑order webhook_url.
- Events API (port‑in)
  - List all events, filter by order or time, and republish specific events to your current notification channels. Republish resends notifications but does not create new events.
- Comments
  - Create and list comments on an order to collaborate with Porting Ops; subscribe to new‑comment webhooks for updates.

## Port‑out orders (numbers leaving Telnyx)
- Overview
  - When another carrier initiates a port‑in, Telnyx creates a port‑out order in your account. You must authorize or reject promptly (usually within 24–48 hours) or it will auto‑authorize.
- Statuses
  - pending → authorized → ported
  - rejected‑pending (awaiting review of your rejection) → rejected
  - canceled (by the gaining carrier or Telnyx)
- Actions
  - Authorize: approve port‑out to proceed on its FOC date.
  - Reject: choose an eligible rejection_code (order‑specific list); if using “Other,” include a reason. Porting Ops validates rejections.
- Notifications and events
  - Configure Port Out Notifications for status changes and new comments.
  - Port‑out Events API: list/filter events and republish. FOC date changes emit a dedicated event.
  - Note: For port‑outs, the gaining carrier has a 10‑day grace period after the listed FOC date to complete the port; completion on the exact listed date is not guaranteed.

## Best practices and tips
- Run portability checks before creating orders; include numbers in E.164 format.
- Expect order splitting; update and submit each split order independently.
- Upload clear, recent LOA and invoice documents; ensure end‑user and service address data match the losing carrier’s records.
- Choose a requested FOC within allowed windows and schedule cutovers during on‑demand windows if FastPort‑eligible.
- Pre‑assign connection, messaging profile, emergency address, and (optionally) bundles so configuration is ready at activation.
- For US/CA, enable messaging activation if you want Telnyx to take over SMS at FOC; consider Hosted SMS ahead of time to avoid downtime.
- Keep services active with the losing carrier until you confirm voice and (if enabled) messaging have ported.
- Set up webhooks and monitor events/comments to respond quickly to exceptions or carrier inquiries.
- For GB partial ports, complete associated_phone_numbers or the losing carrier will reject the order.
- For DE, use extensions or blocks when applicable; carefully define activation ranges to match operational needs.
