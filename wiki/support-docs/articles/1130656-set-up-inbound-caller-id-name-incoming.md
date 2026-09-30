---
title: "Set up Inbound Caller ID Name (incoming)"
summary: "In this article we will walk you through setting up caller ID name for your numbers. See Telnyx guidance and requirements."
sources:
- url: "https://support.telnyx.com/en/articles/1130656-set-up-inbound-caller-id-name-incoming"
updated_at: 2026-07-08T00:00:00Z
tags: [support-docs]
source_path: "support-docs/en--articles--1130656-set-up-inbound-caller-id-name-incoming.md"
generated_by: incremental-support-docs-wiki
---
<!-- generated_from=support-docs/en--articles--1130656-set-up-inbound-caller-id-name-incoming.md -->

# Set up Inbound Caller ID Name (incoming)

In this article we will walk you through setting up caller ID name for your numbers. See Telnyx guidance and requirements.




This feature is located on the Real-Time Communications column in your [numbers section](https://portal.telnyx.com/#/app/numbers/my-numbers) of your Mission Control Portal account.
​
Enabling this feature on your DID will allow for Telnyx to DIP the CNAM databases, to determine if there is a name associated with the callers number on your inbound calls. If there is, we'll pass this along in our SIP INVITES to your connection.
​

## **Guide to Configuring Inbound Caller ID Name**

1. On the number you want to enable inbound CNAM, click on the business card icon.

![](_images/855d4a661907cb0b.png)

2. Visit the section with **CNAM Caller ID Lookup** and toggle the option to enable the setting.

![](_images/d62ca55dca4decc4.png)

3. Accept the MRC (Monthly Recurring Charge) for this feature and click save changes at the bottom.
