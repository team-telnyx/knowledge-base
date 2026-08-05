---
title: Telnyx Mission Control Account Setup
summary: A consolidated guide to creating and configuring a Telnyx Mission Control
  account, covering sign-up, verification, Freemium and Managed Accounts, AI Assistants,
  messaging, voice, and the in-portal AI support assistant.
sources:
- url: https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account
- url: https://support.telnyx.com/en/articles/12232444-comprehensive-ai-assistants-configuration-walk-through
- url: https://support.telnyx.com/en/articles/14327893-telnyx-freemium-accounts
- url: https://support.telnyx.com/en/articles/4404409-resources-on-your-account
- url: https://support.telnyx.com/en/articles/4951492-managed-accounts
- url: https://support.telnyx.com/en/articles/5295540-how-to-sign-up-for-a-telnyx-account
- url: https://support.telnyx.com/en/articles/8020222-mission-control-portal-ai-chat-support-assistant
- url: https://support.telnyx.com/en/articles/8219294-messaging-in-mission-control
- url: https://support.telnyx.com/en/articles/9767793-sending-a-test-message-with-learn-and-build
- url: https://support.telnyx.com/en/collections/19623087-ai-assistant
updated_at: 2026-08-05T13:32:36Z
---

# Telnyx Mission Control Account Setup

*Part 4 of 5 — see also: [Part 1](telnyx-mission-control-account-setup--part-1.md), [Part 2](telnyx-mission-control-account-setup--part-2.md), [Part 3](telnyx-mission-control-account-setup--part-3.md), [Part 5](telnyx-mission-control-account-setup--part-5.md)*

A consolidated guide to creating and configuring a Telnyx Mission Control account, covering sign-up, verification, Freemium and Managed Accounts, AI Assistants, messaging, voice, and the in-portal AI support assistant.

## Managed Accounts

Managed Accounts are sub-accounts created from within an existing Mission Control Portal account (the **manager** account). Manager accounts have advanced control over pricing, reporting, administration, and billing of Managed Accounts.

### Pricing and Reporting

- Managed Accounts inherit pricing from their manager accounts. If the organisation has a committed use agreement for lower rates, Managed Accounts automatically receive those rates.
- Pricing is hidden from Managed Accounts. Only manager accounts can view pricing.
- Managed Accounts can generate reports on their own usage without viewing pricing.

### Administration

- Manager accounts can log into any Managed Account via the portal to view usage and balance, and configure settings.
- Manager accounts can create an API key associated with a Managed Account and control it via the [Telnyx API](https://developers.telnyx.com/api-reference/managed-accounts/lists-accounts-managed-by-the-current-user).

### Billing

- Managed Accounts have their own balances, payment methods, and invoices.
- Most providers and banks implement mechanisms to prevent carding attacks (multiple cards used to frequently top up managed accounts daily). Payment attempts can be blocked for a period of time.
- These patterns are often construed as suspicious. Leveraging **Rollup Billing** by using a personal card occasionally is recommended over regularly topping up individual managed accounts.
- If not using Rollup Billing, avoid multiple top-ups with the same card every day. Instead, top up each account with a sufficient larger balance that lasts longer to avoid temporary blocks.

### Use Cases

Managed Accounts are an intuitive way of administering multiple accounts and users from one unified interface. Managed Service Providers can use Managed Accounts to manage each customer while allowing them the freedom to log in and configure their communications.

### Getting Started

Managed Accounts is included with **commit plans** — **Starter** and **Growth** — as well as **Enterprise**. It is **not** available on **Pay-as-you-go**.

- **Starter** — Managed Accounts with a **$1,000 monthly minimum spend** and **quarterly billing** (8% discount shown in the portal).
- **Growth** — Managed Accounts with a **$2,000 monthly minimum spend** and **quarterly billing** (15% discount shown in the portal).
- **Enterprise** — designed for **$5,000+/month**, includes Managed Accounts plus dedicated support and prioritised ticketing.

To enable:

1. In the Telnyx Portal, go to [Pricing plans](https://portal.telnyx.com/#/pricing/plans).
2. Click **Get Plan** on **Starter** or **Growth** to start a self-serve commit, or click **Contact sales** for **Enterprise**.
3. After the plan is active, Managed Accounts will be available. If the option is not visible, contact Support or Sales to confirm activation.

### Creating a Managed Account

Once enabled, Managed Accounts can be created using the [create managed account API](https://developers.telnyx.com/api-reference/managed-accounts/create-a-new-managed-account) (API v2 only), or from within the portal under the [Managed Accounts Section](https://portal.telnyx.com/#/advanced-features/managed-accounts). When created via the API, a custom email address and password can be specified. When created via the portal, a temporary email address is provided and the user cannot log in until a password change is made from the [General](https://portal.telnyx.com/#/account/general) settings.

### Enabling and Disabling

Managed Accounts can be enabled or disabled using API v2 — [enable](https://developers.telnyx.com/api-reference/managed-accounts/enables-a-managed-account) and [disable](https://developers.telnyx.com/api-reference/managed-accounts/disables-a-managed-account) — or from the Mission Control portal.

### Managed Account Settings

- **Allow Custom Pricing** — the managed account does not inherit pricing from the manager account and can have its own independent pricing. Contact the Telnyx customer success representative after creation to set the desired pricing.
- **Rollup Billing** — if set, the records of spend for this managed account are written for the manager account. This value cannot be changed after the account is created.

### Changing the Email of a Managed Account

The email can be changed in the portal under [General](https://portal.telnyx.com/#/account/general) settings, by either the account manager or the user of the account.

### Managed Accounts vs Multiple Environments

Managed Accounts are intended for businesses that manage multiple customer accounts — resellers, MSPs, and multi-tenant platforms. Each Managed Account is its own independent Telnyx organisation with its own balance, API keys, usage, and settings, overseen by the Manager Account.

For separating production and staging environments for internal use, Managed Accounts is not the correct tool. A single Telnyx account cannot belong to more than one organisation, and an organisation cannot be split into multiple environments internally. The workaround is to create two entirely separate Telnyx accounts (one for production, one for staging or development), each with its own email, organisation, resources, and API keys. Each login and billing must be managed independently.

### Notes

- Manager accounts have a default maximum of 1000 managed sub-accounts. For higher limits, contact [support@telnyx.com](mailto:support@telnyx.com).
- Existing Telnyx user accounts cannot be migrated under a manager account. To place an existing account under a manager account, contact [support@telnyx.com](mailto:support@telnyx.com) to cancel the account and remove the email. Existing configurations will be lost.

## Single Sign-On

Business accounts can use Single Sign-On via SAML providers including [Auth0](https://support.telnyx.com/en/articles/5355953-auth0-sso-integration-with-telnyx), [Microsoft Azure Active Directory](https://support.telnyx.com/en/articles/5355800-azure-ad-saml-identity-setup), [Okta](https://support.telnyx.com/en/articles/5335562-okta-saml-identity-setup), [Google GSuite](https://support.telnyx.com/en/articles/5361846-gsuite-sso-integration-with-telnyx), [OneLogin](https://support.telnyx.com/en/articles/5316578-onelogin-saml-identity-setup), and [LastPass](https://support.telnyx.com/en/articles/5341506-lastpass-saml-identity-setup). An Organisation must be created within the portal first.

### Portal Configuration

From the Telnyx Portal homepage, navigate to **My Account → Single Sign-On** and click **Enable Single Sign-On**. Enter the relevant details from the SAML provider and click **Import IdP Settings & Save**. Note the values for **Assertion Consumer Service URL**, **Service Provider Entity ID**, and **Name Identifier Format** to provide within the SAML app. After providing these details back to the provider, click the **Enable Single Sign-On** box and **Save Changes**. All users in the organisation receive an email informing them that SSO is enabled. Users can still log in with username and password for 72 hours; after that, SSO is required.

### Logging in with SSO

Navigate to the [sign-in](https://portal.telnyx.com/#/login/sign-in) page and click the **Single Sign-On** tab. Enter the relevant login details.
