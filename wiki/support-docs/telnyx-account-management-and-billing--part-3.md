---
title: Telnyx Account Management and Billing
summary: A comprehensive guide to setting up, verifying, managing, and billing for
  a Telnyx Mission Control Portal account, including organizations, payment methods,
  invoices, taxes, notifications, and account lifecycle.
sources:
- url: https://support.telnyx.com/en/articles/1130595-account-verification
- url: https://support.telnyx.com/en/articles/1130639-what-is-your-refund-policy
- url: https://support.telnyx.com/en/articles/1130643-is-there-a-cancellation-fee
- url: https://support.telnyx.com/en/articles/1130644-do-i-have-to-sign-a-contract
- url: https://support.telnyx.com/en/articles/1130655-can-i-resell-your-services
- url: https://support.telnyx.com/en/articles/1130658-how-do-i-know-if-a-rate-has-changed
- url: https://support.telnyx.com/en/articles/1130659-billing-increments
- url: https://support.telnyx.com/en/articles/1130661-does-telnyx-offer-post-paid-service
- url: https://support.telnyx.com/en/articles/1130689-how-do-i-cancel-my-account
- url: https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account
- url: https://support.telnyx.com/en/articles/1189141-get-started-with-organizations
- url: https://support.telnyx.com/en/articles/14327893-telnyx-freemium-accounts
- url: https://support.telnyx.com/en/articles/2185372-where-can-i-see-pricing-options
- url: https://support.telnyx.com/en/articles/3317613-billing-decimal-values-considered
- url: https://support.telnyx.com/en/articles/3562148-requesting-numbers
- url: https://support.telnyx.com/en/articles/4277896-notification-settings
- url: https://support.telnyx.com/en/articles/4280500-billing-setup-billing-groups
- url: https://support.telnyx.com/en/articles/4280610-how-to-setup-your-account-settings
- url: https://support.telnyx.com/en/articles/4404409-resources-on-your-account
- url: https://support.telnyx.com/en/articles/5295540-how-to-sign-up-for-a-telnyx-account
- url: https://support.telnyx.com/en/articles/6420959-sales-gst-telecommunication-taxes-usf-fees-trf
- url: https://support.telnyx.com/en/articles/6987563-invoice-overview
- url: https://support.telnyx.com/en/articles/7045419-ach-direct-debit-payment-method
- url: https://support.telnyx.com/en/articles/7984661-how-to-reset-your-password
- url: https://support.telnyx.com/en/articles/8228452-email-notification-international-spend-limit
- url: https://support.telnyx.com/en/articles/8340760-bundles-bundle-pricing
- url: https://support.telnyx.com/en/articles/8379618-bitcoin-payment-method
- url: https://support.telnyx.com/en/articles/8648864-what-happens-with-my-numbers-after-my-account-gets-abolished-for-negative-balance
updated_at: 2026-06-11T11:32:58Z
---

# Telnyx Account Management and Billing

*Part 3 of 4 — see also: [Part 1](telnyx-account-management-and-billing--part-1.md), [Part 2](telnyx-account-management-and-billing--part-2.md), [Part 4](telnyx-account-management-and-billing--part-4.md)*

A comprehensive guide to setting up, verifying, managing, and billing for a Telnyx Mission Control Portal account, including organizations, payment methods, invoices, taxes, notifications, and account lifecycle.

## Invoices

Invoices are accessible under **Billing → Invoices** ([direct link](https://portal.telnyx.com/#/app/billing/invoices)). Invoices for the previous month appear during the **first few days of the new month** and can be sorted by status (Paid, Unpaid). All prices are in USD.

An invoice includes these sections:
- **Summary** — Total charges, top-ups, balance due, convenience fees
- **Numbers Summary** — Monthly Recurring Charges, one-time costs, port fees
- **Existing Features** — Recurring charges for features enabled before the invoice month
- **New Features** — One-time activation charges for new features
- **Usage Charges – Voice & Data** — Quantity, average cost, and total for voice/data traffic
- **Usage Charges – Messaging** — Messaging costs by country and carrier fees
- **Wireless – SIM Cards Summary** — Monthly recurring costs for SIM cards
- **Ledger** — All balance changes with service name, charge amount, units, cost code, cost type, transaction type, and timestamp

You can generate **Ledger Records** (breakdown by Billing Groups) and **Billing Records** (breakdown by Managed Accounts) for past months. A CSV list of cost codes and descriptions is available from the invoice overview.

For invoice queries, contact billing@telnyx.com.

## Payment History

The [Payment History](https://portal.telnyx.com/#/billing/history) page shows payments from the last 12 months with downloadable receipts, filterable by payment type (credit card, PayPal, Bitcoin, ACH).

## Taxes and Fees

### US Sales and Telecommunications Taxes

Telnyx collects applicable state and local taxes based on the customer's **service address**, tax regulations, product types consumed, and customer tax status. Taxes are calculated and applied **daily**, deducted from the balance on the following calendar day.

The tax breakdown appears on the monthly invoice. Tax estimates are not available in advance. Customers cannot add a Tax ID or VAT number directly in the portal — contact support@telnyx.com to have one added to invoices. Previously issued invoices cannot be updated.

For **tax exemptions**, contact tax@telnyx.com with appropriate certificates. Address updates do not trigger retroactive tax recalculation.

### USF Fees

The Universal Service Fund (USF) is a federal program requiring contributions from providers of interconnected VoIP and telecommunications services. USF fees apply to telecom/VoIP consumption and Programmable Voice (US Outbound & Inbound), specifically the Interconnected VoIP portion. The fee appears as a line item on your invoice under the tax section.

Companies that file FCC Form 499-A and contribute to USF directly may qualify for an exemption — contact tax@telnyx.com with documentation. Exemption certificates must be renewed annually.

### TRS Fees

The Telecommunications Relay Service (TRS) Fund supports telephone transmission services for hearing or speech challenged individuals. TRS fees apply to the same services as USF. Exemptions follow the same process (contact tax@telnyx.com; annual renewal required).

## Refund Policy

Telnyx **does not offer refunds** for Bitcoin payments or for payments that are **180 or more days old**. For other funds, send a refund request to billing@telnyx.com. Services already consumed under the pay-as-you-go model are not refundable.

## Notifications

The [Notifications](https://portal.telnyx.com/#/app/advanced-features/notifications) section is found under **Account Settings > Advanced Settings**. Typically, only organization owners can configure notifications.

### Low Balance Notifications

Configure a balance threshold that triggers automatic email alerts to the account owner. Changes are auto-saved.

### Event Notifications

Supported event types:
- **Send Newly Available Invoice** — Email only
- **Number Order Completes** — Webhook only
- **Low Available Credit** — Multi-channel support
- **Port In Notification** — Port-in request received and updates
- **Port Out Notification** — Port-out request received
- **SIM Card Status Change** — Any SIM status change
- **Data Usage Notification** — When a SIM reaches the configured data usage threshold
- **Suspicious Outbound Voice Traffic** — Email notification for unusual patterns (concurrent calls to the same destination, calls to high-cost destinations, long-lived concurrent calls)

### Setup

Notifications are configured through three components:
1. **Notification Profiles** — Define groups for notifications
2. **Notification Channels** — Set delivery method (SMS, Voice, Email, Webhook) and destination per profile
3. **Notification Settings** — Map events to notification profiles

## International Spend Limit

Telnyx monitors international voice spend during every **24-hour period**. If your account exceeds **$700** in international calling, you will receive an email notification and further international calls will be blocked (local calls remain unaffected). The limit resets at **00:00 UTC** daily.

The SIP error code returned is **403 International daily spent limit reached D39**. This default limit cannot be adjusted from the portal, but Telnyx Support can increase or decrease it for your use case.

## Bundles

Bundles offer per-user pricing ideal for Operator Connect and Zoom Phone users. Two bundle types are available:
- **Basic** — 1 US number + E911; inbound and outbound calling billed pay-as-you-go
- **Standard** — 1 US number + E911 + up to 1,000 minutes of US inbound/outbound calling; international calling billed pay-as-you-go

On-net calls consume included minutes; programmed voice calls are charged separately. Premium numbers are not eligible for bundles. Purchase bundles via the [Bundles page](https://portal.telnyx.com/#/app/bundles/order) in the portal.

## Requesting Numbers

If no phone numbers appear in your search, you can submit a direct DID request via the **"Request Number"** button. This creates an **Advanced Order** with a unique ID, trackable via the [portal](https://portal.telnyx.com/#/numbers/advanced-orders) or the [Advanced Order API](https://developers.telnyx.com/docs/numbers/phone-numbers/advanced-orders).

The Number Operations team reviews requests within **3–5 business days**. Requests are best-effort and fulfillment is not guaranteed. If regulatory requirements apply, the order remains pending until you provide the required information using a requirement group.

You can set up webhook and/or email notifications for advanced order events.

## Account Cancellation

- To **remove an organization member**, go to [Organization and Members](https://portal.telnyx.com/#/advanced-features/members)
- To **cancel your own account**, email support@telnyx.com with your **Security Passphrase**
- Cancellation actions can only be approved from the **account owner's email address**
- To **re-enable a cancelled account**, email support@telnyx.com from the relevant email address

## Account Abolishment and Number Recovery

If your account holds a negative balance for **1 month**, an abolishment process begins and all numbers are deleted from the account.

The number recovery process follows three stages:
1. **Hold** (2 weeks) — Only you can search for and purchase the numbers
2. **Aging** (2 weeks) — No one (including you) can buy the numbers; required by the FCC
3. **Released** — Numbers become generally available to all Telnyx customers

If your account was abolished, simply adding balance does **not** restore your numbers. You must repurchase them during the Hold phase. During the Aging phase, contact the numbering team (numbering@telnyx.com) or support (support@telnyx.com) for recovery.

This same process applies to accidentally deleted numbers. To prevent negative balances from Monthly Recurring Charges, set up auto-recharge and configure notifications.
