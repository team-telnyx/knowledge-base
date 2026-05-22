---
title: Telnyx Billing, Payments, Channel Billing, Bundles, Invoices, and Managed Accounts
summary: 'End‑to‑end guide to Telnyx billing: funding your account, invoices and records,
  Billing Groups, Channel Billing (concepts, setup, zones, and pricing), Bundles for
  Operator Connect and Zoom Phone, and Managed Accounts options for multi-tenant administration.'
sources:
- url: https://support.telnyx.com/en/articles/1130678-channel-billing-and-how-to-use-it
  content_hash: 173e1a524e7c92d0bbd0715b21082800fd0ab963890e718bc0629a3826c89329
- url: https://support.telnyx.com/en/articles/4280500-billing-setup-billing-groups
  content_hash: 7085f752419d5075233a33ae3d67a372107ef2024a204baeac5460248b957b5b
- url: https://support.telnyx.com/en/articles/6987563-invoice-overview
  content_hash: cea331a7449170378dd8a96b48f83a818539757b262a395e3deb03b9b05f5542
- url: https://support.telnyx.com/en/articles/7045419-ach-direct-debit-payment-method
  content_hash: c457c1a29435566cc4843d4501b1f091436d8e826a54cb5ff16af88c38a8f2f5
- url: https://support.telnyx.com/en/articles/8340760-bundles-bundle-pricing
  content_hash: d0b82b2eff93f96c95ae39af8fdee467ebe28378ed17d0e3b346fbafbe9a4430
- url: https://support.telnyx.com/en/articles/8379618-bitcoin-payment-method
  content_hash: 378d53ebfb9bb214021eafab01e18c578aa10868d36b6218877cd6562bc21468
- url: https://support.telnyx.com/en/articles/8428806-channel-billing
  content_hash: accbc5287d6c9785a7314dc031d6a1cb79e7f8d721714a21a934b85a8739adaf
- url: https://support.telnyx.com/en/articles/4951492-managed-accounts
  content_hash: 32d5fdbafda931eefd19002e3d21b30e462387f288fa295f5e6c6a213593bb4b
updated_at: 2026-05-20T14:52:16Z
---

# Telnyx Billing, Payments, Channel Billing, Bundles, Invoices, and Managed Accounts

*Part 1 of 2 — see also: [Part 2](telnyx-billing-payments-channel-billing-bundles-invoices-and-managed-accounts--part-2.md)*

End‑to‑end guide to Telnyx billing: funding your account, invoices and records, Billing Groups, Channel Billing (concepts, setup, zones, and pricing), Bundles for Operator Connect and Zoom Phone, and Managed Accounts options for multi-tenant administration.

## Key Billing Concepts
- Prepaid balance funds usage and monthly recurring charges (MRCs).
- Payment methods include credit card, PayPal, ACH Direct Debit, and Bitcoin (BTC on Bitcoin mainnet only).
- Invoices are generated monthly (USD) and detail numbers, features, usage, and ledger activity.
- Billing Groups let you categorize charges across Numbers and Outbound Profiles for reporting.
- You can mix billing models per number: pay‑per‑minute, Channel Billing, and (for supported use cases) Bundles.

## Payment Methods and Funding
- Where: Portal > Billing > Payments (Manage Billing).
- Methods: Credit Card, PayPal, ACH Direct Debit, Bitcoin.
- Receipts: Payment receipt PDFs are available for all supported methods via manual top‑up or auto‑recharge; view in Payment History (last 12 months) and download by payment type.
- Replacing a saved method: Only one saved card is kept; delete the current method (trash icon), then make a new payment to add another. Minimum online payment is $10 USD (excludes Bitcoin, which has its own minimum).
- Top‑up limits for new users: $100 on day one, increasing by $50/day across all methods. Request Level 2 Verification to remove limits.
- Payment method review: New accounts undergo a payment-method review (up to 48 business hours). You’ll be emailed when approved or if suspended pending KYC review.
- Address rules: The billing address must match the country of the phone number used to verify your account unless Level 2 verified.
- PayPal fee: 3% applies to customers who have access to ACH.

### ACH Direct Debit (USD, US bank accounts)
- Availability: Not enabled by default; contact support@telnyx.com to enable.
- Linking: Manage Billing > Make a Payment > ACH Direct Debit, complete mandate and link via secure flow. Instant verification when supported; otherwise micro‑deposits (1–3 business days).
- Settlement timing (US Central Time):
  - Initiated between 9am–3pm on a business day: same‑day settlement.
  - After 3pm on a business day: next business day.
  - No processing on weekends/bank holidays.
- Behavior: You can submit multiple manual ACH payments; ACH auto‑recharge won’t run if a prior ACH charge is still pending. Pending ACH increases “ACH pending balance” and available credit but not the main balance until settled.
- Fees: Currently no ACH fee. You may still keep a backup card so auto‑recharge can fail over if ACH is pending/failed.
- Access: Sub‑members with appropriate permissions can manage ACH.

### Bitcoin Payments
- How: Billing > Payments > choose Bitcoin.
- Network: Only BTC on the Bitcoin blockchain (no Lightning; no other coins).
- Minimum: $100 per Bitcoin invoice; amounts below the minimum won’t post until cumulative settlement meets/exceeds $100.
- Confirmations & timing: Typically ~10 minutes (1 confirmation; applies up to $1000). Longer during network congestion.
- QR code: Expires in 15 minutes; BTC amount is locked at generation time.
- Refunds: Not supported for Bitcoin transactions.
- Statuses: No Payment, Processing, Settled, Invalid.
- History: View on the Payment History page.

## Auto‑Recharge and Scheduled Payments
- Auto‑recharge triggers when available credit reaches your threshold and charges the saved method to bring balance up to Threshold + Recharge amount (can exceed the nominal recharge amount if balance fell far below threshold).
- Limits: Max 10 auto‑recharges in a 24‑hour period. If 10 runs can’t cover daily usage, service may be disrupted.
- Scheduled Payments: Enable to auto‑pay a fixed amount on a chosen day each month via your selected method.
- Best practices: Enable portal notifications for low balance and invoice availability.

## Invoices and Records
- Access: Profile menu > Manage Billing > Invoices or go directly to the Invoices tab.
- Timing: Prior month’s invoices appear in the first few days of the new month; prices are in USD.
- Contents overview:
  - Summary: Total charges, top‑ups, start/end balance, and convenience fees (e.g., 3% card/PayPal fee).
  - Numbers Summary: Monthly Recurring Charges (MRCs) and prorations for owned numbers; one‑time purchase fees; port‑in/out fees.
  - Existing Features: Recurring charges for previously‑enabled features (e.g., inbound channels, CNAM, E911, VXCs).
  - New Features: One‑time activation charges for newly‑enabled features.
  - Usage Charges – Voice & Data: Quantity, average cost, total for call/data usage.
  - Usage Charges – Messaging: By country, including carrier fees.
  - Wireless – SIM Cards Summary: Monthly SIM and attached feature charges.
  - Ledger: Every balance change with service name, units, cost code/type, transaction type, timestamp.
- Exports: Generate Ledger & Billing Records, with breakdowns by Billing Groups or by Managed Accounts.
- Cost codes: A CSV with cost code descriptions is linked from the Invoice Overview article.

## Billing Groups
- Purpose: Categorize usage and end‑of‑month records for reporting.
- Create: Billing > Billing Groups, name and create; you can delete groups later.
- Assign:
  - Numbers: Set the Billing Group on each number.
  - Outbound Profiles: Assign in the Outbound Voice Profile’s Advanced Settings.
- Reporting: Use invoice Ledger & Billing Records to analyze spend by group.

## Channel Billing (Unlimited inbound minutes by channel)
- Concept: Pay a flat monthly fee per channel to support a set number of concurrent inbound calls. Each channel supports one simultaneous inbound call. Inbound per‑minute charges show as $0; the per‑channel fee appears in MRCs on your invoice.
- Mix & match: You can run some numbers on Channel Billing and others on pay‑per‑minute in the same account; only Channel‑billed numbers count against channel capacity.
- Sharing: Channels are shared across all eligible numbers configured for Channel Billing within the same Channel Zone. You can have more channels than numbers (e.g., 5 channels for one number to allow 5 concurrent inbound calls) or share a pool (e.g., 5 channels across 10 numbers, allowing 5 total concurrent inbound calls).
- Exhaustion behavior: When all channels are in use, new inbound calls receive “User Busy.”
- Eligibility & scope:
  - Available for eligible Telnyx numbers in supported Channel Zones; configure per number by setting Voice Billing Method to Channel in Numbers > Manage Numbers > Voice tab.
  - Not available for toll‑free numbers. Eligibility depends on supported countries per zone.
- Where to manage:
  - Reserve channels: Voice > Settings > Voice Channels.
  - Set number billing method: Numbers > Manage Numbers > edit number > Voice tab > Voice Billing Method = Channel (if eligible).

## Channel Billing Zones and Pricing
Per‑channel monthly costs vary by zone and scale with quantity (appears in MRCs; inbound calls themselves price at $0):
- US Zone: 0–10: $12; 10–50: $11; 50–250: $9; 250+: $8
- Zone A: 0–10: $15; 10–50: $14; 50–250: $12; 250+: $10
- Zone B: 0–10: $20; 10–50: $19; 50–250: $15; 250+: $14
- Zone C: 0–10: $25; 10–50: $23; 50–250: $19; 250+: $17
Supported countries include:
- US Zone: United States
- Zone A (selected): Much of Europe and UK (e.g., DE, FR, ES, IT, NL, SE, CH, UK) plus others like AR, GE.
- Zone B (selected): CA, MX, BR, AU, SG, ZA, TH, UA, PR/VI, and more across the Americas, EMEA, APAC.
- Zone C: IL, JP, NZ, SI
View the Voice Channels screen to see countries mapped to each zone and reserve capacity accordingly.
