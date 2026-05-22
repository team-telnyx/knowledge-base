---
title: Telnyx Billing, Payments, Channel Billing, Bundles, Invoices, and Managed Accounts
summary: 'End‑to‑end guide to Telnyx billing: funding your account, invoices and records,
  Billing Groups, Channel Billing (concepts, setup, zones, and pricing), Bundles for
  Operator Connect and Zoom Phone, and Managed Accounts options for multi-tenant administration.'
sources:
- url: https://support.telnyx.com/en/articles/1130678-channel-billing-and-how-to-use-it
- url: https://support.telnyx.com/en/articles/4280500-billing-setup-billing-groups
- url: https://support.telnyx.com/en/articles/6987563-invoice-overview
- url: https://support.telnyx.com/en/articles/7045419-ach-direct-debit-payment-method
- url: https://support.telnyx.com/en/articles/8340760-bundles-bundle-pricing
- url: https://support.telnyx.com/en/articles/8379618-bitcoin-payment-method
- url: https://support.telnyx.com/en/articles/8428806-channel-billing
- url: https://support.telnyx.com/en/articles/4951492-managed-accounts
updated_at: 2026-05-20T14:52:16Z
---

# Telnyx Billing, Payments, Channel Billing, Bundles, Invoices, and Managed Accounts

*Part 2 of 2 — see also: [Part 1](telnyx-billing-payments-channel-billing-bundles-invoices-and-managed-accounts--part-1.md)*

End‑to‑end guide to Telnyx billing: funding your account, invoices and records, Billing Groups, Channel Billing (concepts, setup, zones, and pricing), Bundles for Operator Connect and Zoom Phone, and Managed Accounts options for multi-tenant administration.

## Bundles (Operator Connect and Zoom Phone)
- What’s included:
  - Basic Bundle: 1 US local number + E911; inbound/outbound calls billed pay‑as‑you‑go (Bundles rate deck applies).
  - Standard Bundle: 1 US local number + E911 + up to 1000 minutes of US inbound and outbound calling; international calling billed pay‑as‑you‑go (Bundles rate deck).
- Notes:
  - On‑net calls consume included minutes.
  - Programmed voice calls are billed separately and do not reduce included minutes.
  - Premium numbers are not eligible.
  - Currently limited to Operator Connect and Zoom Phone users; US numbers/calls only at this time.
- How to buy:
  - Portal > Bundles, choose Basic or Standard, add to cart.
  - Search and buy/select a number, then link it to the bundle in your cart.
  - Associate the number under Voice > External Voice Integrations with your chosen integration to start calling.

## Managed Accounts and Rollup Billing
- Definition: Sub‑accounts created and administered by a manager account for multi‑tenant/customer management.
- Availability: Included with commit plans (Starter, Growth) and Enterprise; not on Pay‑as‑you‑go. Enable under Pricing Plans, then use Advanced Features > Managed Accounts or the API (v2) to create.
- Pricing & reporting:
  - Managed Accounts inherit manager pricing (hidden from the Managed Account user). They can generate usage reports without seeing rates.
- Administration:
  - Managers can log in to any Managed Account via portal, or manage via API keys scoped to that account.
- Billing:
  - Each Managed Account has its own balance, payment methods, and invoices.
  - Banks may block repeated small top‑ups (anti‑carding); prefer Rollup Billing or larger, less frequent top‑ups per account.
  - Rollup Billing option writes spend records of a Managed Account to the manager account (irreversible setting on creation).
- Custom pricing: You can allow custom pricing on a Managed Account (does not inherit manager pricing); coordinate with your Telnyx representative to set rates.
- Enable/disable: Via portal or API (v2).
- Limits & caveats:
  - Default limit: up to 1000 Managed Accounts (contact support to request more).
  - Existing Telnyx organizations can’t be migrated under a manager account; they must be cancelled and recreated.
- Environments note: Managed Accounts are for managing customers, not staging/production separation. For separate environments, create two distinct Telnyx organizations (separate logins, balances, and billing).

## Service Address and Taxes
- Your Service Address is where you consume Telnyx services and is used to determine tax rates. If not provided, Telnyx uses your account/billing address. See the taxes article for more detail.

## Tips, Limits, and Notifications
- Configure low‑balance and invoice‑ready email alerts in Advanced Features > Notifications.
- Invoices and Payment History are accessible from the Billing area for downloads and auditing.
- Auto‑recharge best practice: Choose a threshold/recharge pairing that comfortably covers peak daily usage within the 10‑runs/24‑hours cap.
- Keep a backup payment method on file to avoid service disruption if your primary method is unavailable or pending (e.g., ACH delays).
