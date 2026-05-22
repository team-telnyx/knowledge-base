---
title: 'Telnyx Number Porting: Port‑In and Port‑Out'
summary: End‑to‑end guide to porting phone numbers with Telnyx, covering port‑in and
  port‑out workflows, FOC dates, FastPort on‑demand activations, messaging activation
  and tracking, regulatory requirements, German extensions and blocks, bundle pre‑configuration,
  cancellations, notifications, and events.
sources:
- url: https://developers.telnyx.com/docs/numbers/porting/allowed-foc-dates
  content_hash: 69e112782b0e9e9c6688251278767aca9ce5ae1cb1d9410857488d8ccd0f8ed9
- url: https://developers.telnyx.com/docs/numbers/porting/bundles-porting
  content_hash: e789c26e2fd8cd1ced96949f2f87738e0e560c9f82f0e0ee45ebf31dda3ad9e1
- url: https://developers.telnyx.com/docs/numbers/porting/cancel-port-order
  content_hash: 4fbef8100ce82c79c06638db966c25bd7894e9a2268166d210f0b69790fb31be
- url: https://developers.telnyx.com/docs/numbers/porting/extensions
  content_hash: b6044c3a0d4ef6768ec2c71190aff5ba98be0e11b92c72c2abbf121df3783124
- url: https://developers.telnyx.com/docs/numbers/porting/getting-started/index
  content_hash: 8ce79bcb8961e8e62453b9b00ba0d43dd5ecb1745c9eddeb0cdab2f2f8db9dc5
- url: https://developers.telnyx.com/docs/numbers/porting/messaging-porting
  content_hash: e3f353f73dfd24466f34d052cc55069994dd3ad8ab41a9f0f4a0c8e0e4b195cb
- url: https://developers.telnyx.com/docs/numbers/porting/on-demand-activations
  content_hash: b5a564cb0eb0ca13546767cf2f90e539d2c77f4d5e0a3e06a15fc3f9f53f25bf
- url: https://developers.telnyx.com/docs/numbers/porting/port-in-blocks
  content_hash: 457bfba37f8919f7f53ca18f419ee1b3d8f077f3ecec25d72077a0b079a4cbae
- url: https://developers.telnyx.com/docs/numbers/porting/port-in-events
  content_hash: 17d60f90ce57a4dc8ae137bdb62e6b7733ae7f354556978102076c82ea969486
- url: https://developers.telnyx.com/docs/numbers/porting/port-in-notifications
  content_hash: 3bf551d4b41d5a5364ed3c10695744ba90dca47f60160aa9713f1380281b04e9
- url: https://developers.telnyx.com/docs/numbers/porting/port-in-requirements
  content_hash: 1b4436a06f1aab5f531bdc006d03a7a03796b54a42a75e90d641d145db3c04bb
- url: https://developers.telnyx.com/docs/numbers/porting/port-out-events
  content_hash: ad34b4166c56cb86761de70ace5116521317235798c9cd3b4f277c6f7613cc77
- url: https://developers.telnyx.com/docs/numbers/porting/port-out-notifications
  content_hash: ffb18d45817e90a17608b37d56d9735c91849674486073e70c23ecb6e9735cef
- url: https://developers.telnyx.com/docs/numbers/porting/port-out-quickstart/index
  content_hash: 0e38e56d785c9864dcaced6781425ec00654695a09106ba9309a7084c7c4abc4
- url: https://developers.telnyx.com/docs/numbers/porting/porting-additional-steps/index
  content_hash: 6f897ab75044ffba11235fe79de0a7798935d3eb69781f92cb99c0a894e0bc2e
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
