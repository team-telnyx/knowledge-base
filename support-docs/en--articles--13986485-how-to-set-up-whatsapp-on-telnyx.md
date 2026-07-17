---
source_url: https://support.telnyx.com/en/articles/13986485-how-to-set-up-whatsapp-on-telnyx
title: "How to Set Up WhatsApp on Telnyx"
description: "Step-by-step guide to setting up WhatsApp Business on Telnyx using the Embedded Signup flow. See Telnyx guidance and requirements."
scraped: 2026-07-08
content_hash: b9ca1b42fad01cb5e8d456c64f5fcffe912ea4340988c5c059337afc0df07b99
---







# How to Set Up WhatsApp on Telnyx

Step-by-step guide to setting up WhatsApp Business on Telnyx using the Embedded Signup flow. See Telnyx guidance and requirements.




## Prerequisites

* A Telnyx account ([portal.telnyx.com](https://portal.telnyx.com))
* A Meta Business Manager account ([business.facebook.com](https://business.facebook.com))
* A phone number to register with WhatsApp (cannot be currently used with personal WhatsApp)

## Step 1: Start Embedded Signup

1. Log in to the [Telnyx Portal](https://portal.telnyx.com)
2. Navigate to **Messaging → WhatsApp** in the sidebar
3. Click **Get Started** or **Add WhatsApp Business Account**
4. You will be redirected to Facebook/Meta to authenticate

## Step 2: Connect Meta Business Manager

1. Log in with your Facebook account that has admin access to your Meta Business Manager
2. Select your existing Meta Business Manager or create a new one
3. Grant Telnyx the required permissions to manage your WABA
4. Select or create a WhatsApp Business Account

## Step 3: Register a Phone Number

1. Enter the phone number you want to use with WhatsApp
2. Choose a display name for your business (this will be visible to customers)
3. Verify the number via **phone call** or **SMS**

**Tip:** If you are registering a landline number, choose phone call verification. SMS delivery to landline numbers can be unreliable.

**Important:** The embedded signup flow currently requires a Telnyx-owned number with an active messaging profile. Bring-your-own-number (non-Telnyx numbers) is not yet supported through the portal signup flow.

**Important:** The phone number cannot be currently active on the WhatsApp consumer app or WhatsApp Business App. If it is, you will need to delete that WhatsApp account first.

## Step 4: Complete Setup

Once verification is complete, your WhatsApp Business Account will appear in the Telnyx Portal under **Messaging → WhatsApp**. From here you can:

* View your WABA details and phone numbers
* Configure webhook URLs for inbound messages and delivery statuses
* Manage your business profile via Meta Business Manager (description, address, website, etc.)
* Create and manage message templates

## Step 5: Create Your First Template

Before you can send business-initiated messages, you need at least one approved template. Use the Telnyx API to create a template and wait for Meta's approval (typically 24–48 hours).

## Step 6: Send Your First Message

Once your template is approved, you can send your first WhatsApp message via the Telnyx API. See the [Quickstart Guide](https://developers.telnyx.com/docs/messaging/whatsapp/quickstart) for a complete walkthrough.

## Troubleshooting

* **Signup flow fails** — Ensure your Facebook account has admin access to the Meta Business Manager. Try clearing browser cookies and restarting the flow.
* **Phone verification fails** — Wait a few minutes and try again. If using SMS, try the phone call option instead.
* **Number already in use** — The number is registered with WhatsApp consumer or Business App. Delete that account first from the phone.

---

Related Articles

[What is WhatsApp Business Platform?](https://support.telnyx.com/en/articles/13986480-what-is-whatsapp-business-platform)[WhatsApp Pricing on Telnyx](https://support.telnyx.com/en/articles/13986484-whatsapp-pricing-on-telnyx)[WhatsApp FAQ](https://support.telnyx.com/en/articles/13986488-whatsapp-faq)[WhatsApp Troubleshooting Guide](https://support.telnyx.com/en/articles/13986489-whatsapp-troubleshooting-guide)[Enabling WhatsApp Business Calling on Telnyx Numbers](https://support.telnyx.com/en/articles/14668631-enabling-whatsapp-business-calling-on-telnyx-numbers)

Did this answer your question?

😞😐😃
