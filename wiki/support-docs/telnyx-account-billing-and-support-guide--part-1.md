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

*Part 1 of 5 — see also: [Part 2](telnyx-account-billing-and-support-guide--part-2.md), [Part 3](telnyx-account-billing-and-support-guide--part-3.md), [Part 4](telnyx-account-billing-and-support-guide--part-4.md), [Part 5](telnyx-account-billing-and-support-guide--part-5.md)*

This page consolidates Telnyx account, billing, and support guidance, covering account types (including Freemium and Managed Accounts), billing setup, payment methods, invoices, billing groups, notification settings, the AI Chat Support Assistant, feature requests, bug reports, security vulnerability disclosure, and sending test messages via the Learn and Build feature in the Mission Control Portal.

## Account Types and Contracts

Telnyx does not require customers to sign a contract. You can open an account for free whenever and for however long you want. World-class support is included for all customers, and there are no hidden fees.

### Freemium Accounts

A Freemium account lets developers try Telnyx AI products with no credit card, no payment setup, and no commitment. Sign up at [telnyx.com/sign-up](https://telnyx.com/sign-up) using your email address, then check your inbox for a magic link — a secure, one-time login URL sent to your email. Each time you sign in, you'll receive a new magic link instead of using a password.

Freemium accounts include:

- **$25 in AI credits** covering usage across the entire Telnyx AI product suite
- **One US local phone number** at no cost
- **Full access to AI products** including Telnyx Inference and AI Assistants

The $25 credit is applied automatically as a discount on AI product usage and covers up to $25 in total AI usage plus one US local phone number. You don't need to activate or redeem anything — it's already applied when you sign up. Freemium users can see how many AI credits they have left and how many days remain to use them.

Freemium accounts are limited to the Telnyx AI product suite and one US local phone number. Other Telnyx products (Voice, Messaging, Networking, etc.) require a full account. If you try to use a non-AI product on a Freemium account, the API call will typically return an error. Freemium accounts cannot top up their balance; to add funds, upgrade to a full Telnyx account.

### Upgrading to a Full Account

To upgrade from Freemium to a full account:

1. Log in to your [Telnyx Portal](https://portal.telnyx.com).
2. Click your profile icon in the top corner.
3. Go to **Account Level** and click **Upgrade**.
4. Verify your identity through **LinkedIn** or **GitHub**.

You have two verification attempts — one via LinkedIn and one via GitHub. If one method is rejected, you can try the other. Once approved, your account becomes a standard Telnyx trial account with access to all products. After upgrading, the $25 AI credit is replaced with a $5 full-credit that can be used with any Telnyx product and service.

If both verification methods are rejected, you can create a new Telnyx account using a business email address. If you've already tried both routes and used a business email, contact Telnyx Support for further assistance. Each LinkedIn or GitHub account can only be used to verify one Telnyx account.

### Cancelling a Freemium Account

To cancel a Freemium account, contact Telnyx Support. If you want to reuse your email address to create a full Telnyx business account instead, the support team can help with the transition.

## Billing Setup

The Mission Control Portal offers various functionalities to help keep track of billing information. The Billing section is where you primarily manage your balance, payment method, auto-recharge preferences, and access your invoices.

### Payment Information

You can view your current balance and add a payment method to set up recurring payments. PO Boxes are unsupported when saving a billing address for a payment method. Click **Make Payment** and fill out the required information.

### Scheduled Payments

When you activate scheduled payments using the toggle feature, you can specify a payment amount, choose a payment method, and select a preferred day each month for Telnyx to automatically process the payment. This ensures your account balance is topped up without manual intervention and helps avoid service disruption in case of a negative balance.

### Accepted Payment Methods

Telnyx allows customers to make payments with:

- Credit Card
- PayPal
- Bitcoin
- ACH Direct Debit

Your last payment method will be saved for future payments. Once you have a saved payment method, you will get the option to delete it. You will receive a payment receipt PDF upon successful transactions via Credit Card, PayPal, Bitcoin, or ACH done through either manual top-up or auto-recharge. In the event of a failed transaction attempt, you will be automatically alerted via email.

Starting July 3rd 2023, a 3% transaction fee applies on PayPal payments for customers who have access to ACH payments.

### Top Up Limits

New users can make payments up to $100 on day one of account creation. That limit increases by $50/day and applies as a whole across any payment method you use. To remove this limit, request Level 2 Verification.

### Payment Method Restrictions

New accounts are subject to a payment method review once a payment method is added. This review can take up to 48 hours, excluding weekends. Once the review is successful you will receive an email with the subject **Attention: Payment Method Allowed**. If the review is unsuccessful, you will receive an email **Attention: Suspension of Your Credit Card and PayPal Payment Methods** — contact support@telnyx.com for further review, which may require further KYC details.

The billing address you provide must match the country of the phone number you used to verify your account. This restriction can be removed if your account is Level 2 verified.

### Auto Recharge

When auto-recharge is triggered, Telnyx will always charge your saved payment method an amount that brings your balance up to the **Threshold + Recharge** amount. This may cause significantly higher charges than your set recharge amount if your balance falls far below your set threshold due to monthly charges.

Auto-recharge is limited to 10 times in a 24-hour period. You will experience service disruption if 10 recharges of your recharge amount cannot cover a day of usage. This limitation cannot be removed. The auto-recharge threshold is based on your available credit — once the available credit reaches the threshold amount set, the auto-recharge is triggered.

### Replacing a Saved Payment Method

Telnyx only saves one payment method, so to change your credit card you must first delete your current one by clicking the trash icon next to it. Once deleted, you can add a new payment method by making a payment. The minimum payment is $10 USD. To delete a saved ACH payment method, click the trash can icon to the right of the listed bank account.

### Service Address

Your Service Address is the location from where you consume service provided by Telnyx. Telnyx uses the service address to determine tax rates. If you do not fill in a service address, Telnyx will use the billing address.
