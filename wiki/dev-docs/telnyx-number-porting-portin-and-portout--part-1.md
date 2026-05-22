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

*Part 1 of 2 — see also: [Part 2](telnyx-number-porting-portin-and-portout--part-2.md)*

End‑to‑end guide to porting phone numbers with Telnyx, covering port‑in and port‑out workflows, FOC dates, FastPort on‑demand activations, messaging activation and tracking, regulatory requirements, German extensions and blocks, bundle pre‑configuration, cancellations, notifications, and events.

## Key concepts and terminology
- Firm Order Commitment (FOC) date: The date/time the losing carrier releases numbers to Telnyx; the port completes and numbers activate at Telnyx.
- Requested vs actual FOC: You request a time, but the losing carrier confirms the final date/time.
- FastPort eligibility: Enables on‑demand activations within a same‑day window (US/CA only).
- Activation types: Scheduled (auto at FOC) or on‑demand (you trigger within the window).
- NNID (NetNumber ID): Controls SMS routing for US/CA numbers; messaging may lag voice if the losing carrier doesn’t release NNID.
- Order splitting: Telnyx may split a multi‑number request into separate port orders by country, type, SPID (US/CA), and FastPort eligibility.

## Port‑in workflow
1) Check portability
- Use the Portability Check API to confirm numbers are portable and whether they’re FastPort‑eligible and messaging‑capable.

2) Create a draft order
- Create a porting order with your numbers. The API may split numbers into multiple orders; handle each order independently.

3) Fulfill the order
- Provide end‑user and service address details, attach required regulatory documents (LOA, recent invoice, etc.), and optionally set phone number configuration for the whole order (connection_id, messaging_profile_id, emergency_address_id).

4) Choose your FOC date
- Retrieve allowed windows and set activation_settings.foc_datetime_requested. Requested dates must be within allowed windows and are not guaranteed.

5) Submit and monitor
- Submit the order; statuses progress asynchronously while Telnyx coordinates with the losing carrier. Monitor via API and webhooks. Resolve any exceptions (rejections) and resubmit if needed.

## Regulatory requirements
- Each order has a requirements array derived from country and number type. Fulfill requirements by submitting:
  - Document values (Document ID from the Documents API)
  - Text values (must meet acceptance criteria)
  - Address values (Address ID from the Addresses API)
- Per‑requirement statuses: requirement‑info‑pending, requirement‑info‑under‑review, requirement‑info‑exception, approved.
- Order‑level requirements_status is true only when all are approved.

## Additional steps for GB partial ports
- When porting some (not all) GB local numbers and port_type is partial_port, you must supply associated_phone_numbers that remain with the losing carrier:
  - For each number or range not porting: mark keep (stay active) or disconnect (deactivate after port).
  - If the BTN is included in the port, remaining ranges can only be disconnected.

## Choosing and confirming FOC dates
- Retrieve allowed FOC windows for an order and request a preferred ISO 8601 timestamp via activation_settings.foc_datetime_requested.
- After the losing carrier confirms, the order moves to foc‑date‑confirmed and the foc_datetime_actual field reflects the confirmed time (may differ from requested).
- Monitor via the Retrieve Porting Order API and port‑in webhooks (porting_order.status_changed).

## On‑demand activations (FastPort, US/CA)
- Eligibility and timing
  - Available only when fast_port_eligible is true, and only in US/CA.
  - You can trigger activation after the order is foc‑date‑confirmed, within the country‑specific window:
    - US: 6:00 AM–8:00 PM CT (14 hours)
    - Canada: 8:00 AM–3:00 PM CT (7 hours)
- Flow
  - Set activation_settings.activation_type to on‑demand (otherwise it’s scheduled).
  - When foc‑date‑confirmed, an activation job is created. Use activation jobs APIs to view activation_windows and activate_at (defaults to end of window).
  - Initiate activation during the window; activate_at updates and the job progresses created → in‑process → completed. If you don’t trigger it, activation runs automatically at window end.

## Messaging during porting (US/CA)
- Voice and messaging are separate for US/CA local and toll‑free. At FOC, the losing carrier should release the NNID so messaging routes to Telnyx.
- If they don’t, voice may show ported while messaging continues at the losing carrier. Telnyx detects, escalates, and updates messaging_port_status.
- Enabling and tracking messaging activation
  - messaging_capable must be true.
  - Update the order to set messaging.enable_messaging = true and assign a messaging_profile_id (order must be draft, in‑process, or exception).
  - Messaging statuses: pending (pre‑FOC), activating (verifying after voice ports), ported, exception, not_applicable.
- Partial messaging ports
  - Multi‑number orders can have mixed outcomes; check order‑level and per‑number messaging_port_status.
- Hosted SMS alternative
  - To avoid downtime, request Hosted SMS 4+ business days before FOC so SMS routes via Telnyx before voice ports, then complete the voice port on FOC.
- Troubleshooting highlights
  - If messaging shows ported but messages fail, confirm a valid messaging_profile_id is assigned.
  - If unable to enable messaging, verify messaging_capable is true and order status allows changes.
  - Typical timing: most US/CA activations occur within minutes; some take 1–5 business days depending on local vs toll‑free.

## Bundle pre‑configuration (apply bundles at port‑in)
- Purpose
  - Associate purchased bundles with phone numbers on a port order so they auto‑apply when numbers activate.
- Constraints
  - API‑only; can be added/updated any time before ported or cancelled.
  - Each bundle can attach to one number; if used elsewhere before port completes, assignment fails.
  - Up to 20 numbers per request; bundle must be eligible for the number type.
- Flow
  - List available bundles and confirm resources array is empty (unassigned).
  - Get porting_phone_number_id values for the order’s numbers.
  - Create phone_number_configurations mapping porting_phone_number_id → user_bundle_id.
  - Verify configurations; bundles apply automatically at completion.

## Porting extended numbers (Germany)
- Concept
  - A route number (main DID) has short‑digit extensions. Port the route number and define an extension_range; all extensions in that range port together.
  - activation_ranges specify which extensions activate immediately on completion; others remain inactive.
- Constraints
  - Available only for German port orders.
  - Add/remove extensions only while the order is draft, in‑process, or exception.
  - Extension range max 0–999; activation ranges must be within the extension range and non‑overlapping.
- Flow
  - Create the order with the route number.
  - Retrieve the route’s porting_phone_number_id.
  - Create extensions by providing porting_phone_number_id, extension_range, and activation_ranges.
  - Submit the order; manage/view extensions via dedicated endpoints (extensions don’t appear in the generic phone numbers list).

## Port‑in blocks (Germany)
- Concept
  - Port consecutive number ranges (blocks) of typically 10/100/1,000 numbers. Some countries require full‑block porting even if only some are in use.
  - activation_ranges let you activate subsets on completion; others remain inactive but belong to your account.
- Constraints
  - Available only for Germany; max block size 1,000 (000–999).
  - Activation ranges must be subsets, non‑overlapping.
  - Blocks must match the order’s country and number type; add/remove only while draft, in‑process, or exception.
- Flow
  - Create an order with phone_number_blocks: define phone_number_range (start_at/end_at, E.164) and activation_ranges.
  - If an individual‑number order is rejected for block rules, add a block to the existing order; contained numbers are auto‑incorporated.
  - View blocks on the order; numbers in a block include a block_reference_id. Deleting a block removes grouping but leaves the numbers on the order.
