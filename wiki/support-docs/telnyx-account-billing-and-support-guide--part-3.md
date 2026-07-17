---
title: Telnyx Account, Billing, and Support Guide
summary: This page consolidates Telnyx account, billing, and support guidance, covering
  account types (including Freemium and Managed Accounts), billing setup, payment
  methods, invoices, billing groups, notification settings, the AI Chat Support Assistant,
  feature requests, bug reports, security vulnerability disclosure, and sending test
  messages via the Learn and Build feature in the Mission Control Portal.
sources:
- url: https://support.telnyx.com/en/articles/1130644-do-i-have-to-sign-a-contract
- url: https://support.telnyx.com/en/articles/14327893-telnyx-freemium-accounts
- url: https://support.telnyx.com/en/articles/4277896-notification-settings
- url: https://support.telnyx.com/en/articles/4280500-billing-setup-billing-groups
- url: https://support.telnyx.com/en/articles/4283783-feature-requests
- url: https://support.telnyx.com/en/articles/4283906-bug-reports-guide
- url: https://support.telnyx.com/en/articles/4951492-managed-accounts
- url: https://support.telnyx.com/en/articles/6987563-invoice-overview
- url: https://support.telnyx.com/en/articles/8020222-mission-control-portal-ai-chat-support-assistant
- url: https://support.telnyx.com/en/articles/9767793-sending-a-test-message-with-learn-and-build
updated_at: 2026-07-17T09:04:25Z
---

# Telnyx Account, Billing, and Support Guide

*Part 3 of 5 — see also: [Part 1](telnyx-account-billing-and-support-guide--part-1.md), [Part 2](telnyx-account-billing-and-support-guide--part-2.md), [Part 4](telnyx-account-billing-and-support-guide--part-4.md), [Part 5](telnyx-account-billing-and-support-guide--part-5.md)*

This page consolidates Telnyx account, billing, and support guidance, covering account types (including Freemium and Managed Accounts), billing setup, payment methods, invoices, billing groups, notification settings, the AI Chat Support Assistant, feature requests, bug reports, security vulnerability disclosure, and sending test messages via the Learn and Build feature in the Mission Control Portal.

## Managed Accounts

Managed Accounts is a limited-release feature enabling qualifying users to create sub-accounts with advanced management features. A Managed Account is a sub-account created from within an existing Mission Control Portal account (the **manager** account). Manager accounts have advanced control over pricing, reporting, administration, and billing functionalities of Managed Accounts.

### Pricing and Reporting

- Managed Accounts inherit pricing from their manager accounts. If your organization has a committed use agreement for lower rates, your Managed Accounts will have those rates automatically.
- Pricing is hidden from Managed Accounts. Only manager accounts can view pricing.
- Managed Accounts can generate reports on their own usage without viewing their pricing.

### Administration

- Manager accounts can log into any of their Managed Accounts via the portal to view that account's usage and balance, and configure its settings.
- Manager accounts can create an API key associated with a Managed Account and control it via the Telnyx API.

### Billing

- Managed Accounts have their own account balances, payment methods, and invoices.
- Most providers and banks implement mechanisms to prevent carding attacks where multiple cards are used to frequently top up managed accounts on a daily basis. Payment attempts can be blocked for a period of time.
- These payment patterns are often construed as suspicious, so it is recommended to leverage "Rollup Billing" by using your own personal card now and again instead of regularly using your own card to top up individual managed accounts.
- If you prefer not to use Rollup Billing and instead use your own cards to top up individual managed account balances, avoid multiple top-ups with the same card every day. Instead, top up each account with a sufficient larger balance that lasts longer.

### Use Cases

Managed Accounts are an intuitive way of administering multiple accounts and users from one unified interface. Managed Service Providers can use Managed Accounts to easily manage each of their individual customers while allowing them the freedom to log into their Managed Account and configure their communications.

### Getting Started

Managed Accounts is included with **commit plans** — **Starter** and **Growth** — as well as **Enterprise**. It is **not** available on **Pay-as-you-go**.

- **Starter**: includes Managed Accounts with a $1,000 monthly minimum spend and quarterly billing (8% discount shown in the portal).
- **Growth**: includes Managed Accounts with a $2,000 monthly minimum spend and quarterly billing (15% discount shown in the portal).
- **Enterprise**: designed for $5,000+/month, includes Managed Accounts plus dedicated support and prioritized ticketing.

To enable it:

1. In the Telnyx Portal, go to Pricing plans.
2. Click **Get Plan** on **Starter** or **Growth** to start a self-serve commit, or click **Contact sales** for **Enterprise**.
3. After your plan is active, Managed Accounts will be available for your organization. If you don't see the Managed Accounts option where expected, reach out to Support/Sales.

### Creating a Managed Account

Once enabled, Managed Accounts can be created using the API (API v2 only), or from within the portal under the Managed Accounts Section. When an account is created using the API, you can specify a custom email address and password for that account to log in with. If an account is created using the portal, a temporary email address will be provided, and that user will not be able to log in until a password change is made from the General settings of the account.

### Enabling/Disabling a Managed Account

Managed Accounts can be enabled/disabled using the API v2, or from the Mission Control Portal.

### Managed Account Settings

- **Allow Custom Pricing**: Enabling this setting means the managed account will not inherit any pricing from your manager account and can have its own independent pricing. Contact your Telnyx customer success representative once the new account is created to have the desired pricing set.
- **Rollup Billing**: If set, the records of spend for this managed account will be written for the manager account. This value can't be changed after the account is created.

### Changing the Email of a Managed Account

The email for a managed account can be changed in the portal under the General settings. This can be changed by the account manager or user of the account.

### Managed Accounts vs. Multiple Environments

Managed Accounts are intended for businesses that manage multiple customer accounts — such as resellers, MSPs, and multi-tenant platforms. Each Managed Account is its own independent Telnyx organization with its own balance, API keys, usage, and settings.

If your goal is to have two environments (like production and staging) for your own internal use, Managed Accounts is not the correct tool. A single Telnyx account cannot belong to more than one organization, and you cannot split one organization into multiple environments internally. The workaround is to create two entirely separate Telnyx accounts, each with its own email address — one for production and one for staging or development.

### Notes

- Manager accounts, by default, can have a maximum limit of 1000 managed sub accounts. If your use case requires a higher limit, reach out to support@telnyx.com.
- Existing Telnyx user accounts cannot be migrated under a manager account. If an existing Telnyx user account would like to be placed under a manager account, they will need to reach out to support@telnyx.com to have their account cancelled and email removed. Any existing configurations will be lost.
