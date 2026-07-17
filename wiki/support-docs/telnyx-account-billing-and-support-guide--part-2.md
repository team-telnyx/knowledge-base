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

*Part 2 of 5 — see also: [Part 1](telnyx-account-billing-and-support-guide--part-1.md), [Part 3](telnyx-account-billing-and-support-guide--part-3.md), [Part 4](telnyx-account-billing-and-support-guide--part-4.md), [Part 5](telnyx-account-billing-and-support-guide--part-5.md)*

This page consolidates Telnyx account, billing, and support guidance, covering account types (including Freemium and Managed Accounts), billing setup, payment methods, invoices, billing groups, notification settings, the AI Chat Support Assistant, feature requests, bug reports, security vulnerability disclosure, and sending test messages via the Learn and Build feature in the Mission Control Portal.

## Invoices

Account invoices can be accessed through the Billing section of the Mission Control Portal within the Invoices tab. Click your profile icon in the upper right corner of the Telnyx Portal, then select **Manage Billing** from the menu, and open the **Invoices** tab. You can download and view invoices for past months. Invoices for the previous month will appear during the first few days of the new month and can be sorted by status (Paid, Unpaid). All prices within the invoice are in USD.

To be notified via email when a new invoice is available, set up a notification in the portal.

### Invoice Sections

At the top of the invoice, you'll see your company name, first and last name, address, the date of issuance, and the time-span it pertains to.

- **Summary** — A brief overview of your account balance including total charges, total account top-ups, the balance due at the beginning and end of the month, and convenience fees related to the 3% charge for using credit card or PayPal.
- **Numbers Summary** — Charges pertaining to all owned numbers, including normal and pro-rated Monthly Recurring Charges, One Time Costs from purchases, and fees for Port-Ins and Port-Outs.
- **Existing Features** — Recurring charges for features enabled before the month of the invoice, such as inbound channels, CNAM, emergency services, and VXCs.
- **New Features** — One Time Charges received upon activation of features.
- **Usage Charges - Voice & Data** — All incurred costs from voice and data traffic, broken down into quantity, average cost, and total amount charged.
- **Usage Charges - Messaging** — Costs from messaging traffic for the month, broken down by associated countries, with any carrier fees listed.
- **Wireless - SIM Cards Summary** — Monthly recurring costs for SIM cards in your account, along with any features linked to each SIM card, such as voice services.
- **Ledger** — All changes to your portal balance over the course of the month, with a service name, charge amount, units used, cost code, cost type, transaction type, and timestamp.

A CSV list of cost codes and their descriptions is available for download. For any queries or concerns regarding your invoice, contact billing@telnyx.com.

## Billing Groups

The Telnyx Mission Control Portal lets you create and assign Billing Groups to categorize usage reports and end-of-month invoice records. A Billing Group can be assigned to Numbers and Outbound Profiles.

To create a billing group, enter the desired name and click create. You can delete created Billing Groups in the section below creation. To add a Billing Group to a number, select the billing group option on your number and choose the group to associate. Adding a Billing Group to an Outbound Profile can be done in the Advanced Settings of your Outbound Voice Profile.

## Payment History

The Payment History page allows you to view payments made in the last 12 months on the portal, along with an option to download payment receipts. You can select the payment type used to individually see your credit card receipts, PayPal receipts, or bitcoin receipts.

## Notification Settings

Notification Settings are typically configurable only by account organization owners. They can be found under **Account Settings > Advanced Settings** in the left-hand side of your Portal.

### Types of Notifications

There are two types of notifications:

1. **Low Balance Notifications** — Choose how often you would like to be reminded about this notification when unresolved, and the amount of balance needed to trigger the notification. Changes are auto-saved and automatic emails are sent to the account owner's email address.
2. **Event Notifications** — Configure and customize notifications for events related to your account.

### Supported Event Notifications

- **Send Newly Available Invoice** — A new invoice is available in the portal. Only email notifications are supported.
- **When a Number Order Completes** — A number order you submitted has completed (success, failure, or partial success). Only webhook notifications are supported.
- **Low Available Credit** — Sent when available credit is below the configured threshold. This is the same as the Low Balance Notification but allows configuration of other channels to send to several people or through several channels.
- **Port In Notification** — Telnyx has received a port-in request from your account, with updates on the process.
- **Port Out Notification** — Telnyx has received a port-out notification for a number on your account.
- **SIM Card Status Change** — Each time one of your SIM cards changes status, a notification is triggered.
- **Data Usage Notification** — Sent when a SIM reaches the usage threshold set for data usage notifications.
- **Suspicious Outbound Voice Traffic** — If the system detects unusual outbound voice traffic patterns, you'll receive an email notification immediately. Examples include multiple calls concurrently or in quick succession to the same destination prefix, multiple ongoing calls to the same high-cost destination, and multiple long-lived concurrent calls.

### Notification Setup

1. **Notification Profiles** — Define groups for your notifications and select which profile you want to be notified. Click **New Profile** and enter the name. Manage profiles in the drop-down beside new profile.
2. **Notification Channels** — Define how you want to be notified through SMS, Voice, Email, or Webhook. Click **New Channel**, then select which Notification Profile to notify, how to notify (SMS, Voice, etc.), and to what destination (DID, email, etc.).
3. **Notification Settings** — Manage your notifications and select which events you want to be notified about and to which Notifications Profile. Click **New Settings** to select an event and a Notifications Profile.
