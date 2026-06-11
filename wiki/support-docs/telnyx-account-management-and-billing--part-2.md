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

*Part 2 of 4 — see also: [Part 1](telnyx-account-management-and-billing--part-1.md), [Part 3](telnyx-account-management-and-billing--part-3.md), [Part 4](telnyx-account-management-and-billing--part-4.md)*

A comprehensive guide to setting up, verifying, managing, and billing for a Telnyx Mission Control Portal account, including organizations, payment methods, invoices, taxes, notifications, and account lifecycle.

## Organizations

User Organizations allow multiple accounts to be tied together under one umbrella entity, headed by a single organization owner. Sub-accounts (sub-members) have permissions managed at the group level.

An organization has only **one net running balance and payment method** — it is not designed for resellers to give customers direct account access. For that, use [Managed Accounts](managed-accounts.md).

A non-organization user can create an organization once they are **Level 1 verified**.

### Invitations

- Invite users by email; they must **not already have a Telnyx account**
- Limits: 10 invites per hour (including deleted/revoked), max 10 open invitations at any time, max 5 resends per invitation (every 5 minutes)
- Invitations can be revoked before acceptance
- To add an existing Telnyx user, they must cancel their existing account first (contact support@telnyx.com)

### Permission Groups

Permissions are assigned to groups (not individuals). A user in multiple groups always receives the **most permissions** across all their groups. Permissions come in two types:
- **Category permissions** — Grant access to a whole category of resources (e.g., all connections)
- **Entity permissions** — Grant access to a specific resource (initially only category permissions are available)

Each permission can be: **create**, **read**, **update**, or **delete**.

Available permission sets include:
- **Account Management** — Balance, pricing, auto-recharge, payment methods, invoices
- **Connection Management** — Create, read, update, delete connections/applications
- **Numbers** — Bulk updates, channel settings, DID settings, deletions, purchasing, TDI
- **Outbound** — Modify, read-only, or none for outbound profiles
- **Reporting** — Detail requests, usage reports, monthly charge reports
- **Number Porting** — Create/manage port requests
- **Managed Accounts** — Create and impersonate managed accounts
- **Networking** — Virtual Cross Connect requests
- **Messaging** — Messaging profiles CRUD
- **Organization Management** — Invite/cancel users, manage groups (admin-level permission)
- **Wireless** — SIM card orders, registration, decommissioning, gateways
- **Access Control List (ACL)** — CRUD on ACL entries
- **Call Recording** — CRUD on call recordings

Sub-members cannot "own" resources (numbers, connections, outbound profiles, etc.); they interact with resources owned by the organization owner. Sub-members also cannot have their own payment information.

### Limitations for Sub-Members

Some portal sections may show undesired results for sub-members due to the V2 migration. Telnyx recommends that sub-members leverage the **API key of their organization owner** for these sections: API Keys, Account (General, Organizations, Notifications), Advanced Features, Debugging Tools, Number Lookup, and Telnyx Storage. Sub-members **do not** have access to the verification or SSO pages.

### Transferring Numbers and Configurations

To transfer numbers to another account, submit a port-in request on the new account. Configurations cannot be transferred directly; recreate them on the new account during a maintenance window. SIP Connections must be unique — either set up expert authentication on the new connection or remove the old one first.

## Billing and Payments

Telnyx operates on a **pre-paid, pay-as-you-go** model. Post-paid service is not available. There are **no contracts** and **no cancellation fees**.

The [Billing section](https://portal.telnyx.com/#/app/billing/payment) is found under your profile icon → Manage Billing.

### Payment Methods

Telnyx supports the following payment methods:

- **Credit Card**
- **PayPal** (3% transaction fee for customers who have access to ACH payments; 3% convenience fee applies to credit card and PayPal payments)
- **Bitcoin** (BTC only, on the Bitcoin blockchain; no refunds; minimum $100 payment; QR code expires in 15 minutes; most transactions confirm in ~10 minutes)
- **ACH Direct Debit** — USD payments through a US bank account; no transaction fee; not yet a default method — email support@telnyx.com to enable access

Only **one payment method** is saved at a time. To change it, delete the current method first. The minimum payment is **$10 USD**.

#### ACH Direct Debit Details

| Transfer Initiation Time (US Central) | Settlement |
|---|---|
| Between 9 AM & 3 PM on a business day | Same day |
| After 3 PM on a business day | Next business day |

ACH payments are **not processed on weekends or bank holidays**. Auto-recharge with ACH will not run if a previous ACH charge is still pending. If ACH auto-recharge fails, the system will attempt Credit Card/PayPal as a fallback.

### Top-Up Limits

New users can make payments up to **$100 on day one**. The limit increases by $50/day across all payment methods. Request Level 2 Verification to remove this limit.

### Auto-Recharge

When auto-recharge triggers, the system charges enough to bring your balance up to the **Threshold + Recharge amount**. This may result in charges higher than your recharge amount if your balance has fallen significantly. Auto-recharge is limited to **10 times in a 24-hour period**; this limit cannot be removed.

### Scheduled Payment

Activate scheduled payments to specify a payment amount, payment method, and a preferred day each month for automatic processing.

### Payment Method Review

New accounts are subject to a payment method review once a payment method is added. This review takes up to **48 hours** (excluding weekends). You will receive an email with "Attention: Payment Method Allowed" if successful, or "Attention: Suspension of Your Credit Card and PayPal Payment Methods" if unsuccessful (contact support@telnyx.com for further review, which may require additional KYC details).

The billing address must match the country of the phone number used to verify your account. This restriction is removed with Level 2 verification.

### Service Address

Your Service Address is the location from where you consume Telnyx services. Telnyx uses it to determine tax rates. If not filled in, the billing/account address is used.

## Billing Increments

Voice calls are billed in **60/60 increments** (60-second rounding). A call of 11 seconds is charged as 60 seconds; a call of 96 seconds is charged as 120 seconds. International calling also uses 60-second increments in most cases but can vary by destination. 6-second billing increments are no longer offered.

Telnyx considers **4 decimal points** for billing (e.g., SMS rate of $0.0025 USD).

## Pricing

View current pricing in the portal under your profile icon → **Pricing**. The page offers five tabs: Voice, Numbers, Messaging, Telco Data, and Networking. Each tab has a toggle to adjust pricing based on volume.

Whenever a rate changes, Telnyx sends a rate update email to all customers.

## Billing Groups

Billing Groups let you categorize usage reports and end-of-month invoice records. A Billing Group can be assigned to **Numbers** and **Outbound Profiles**. Create groups in the Billing section and assign them via the number's billing group option or the Outbound Voice Profile's Advanced Settings.
