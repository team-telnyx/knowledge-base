---
title: "Transition of Canadian Numbers to from Global Channel Billing US Zone to Zone B"
summary: "There are a few steps to ensure a smooth transition to Zone B Channels."
sources:
- url: "https://support.telnyx.com/en/articles/9670281-transition-of-canadian-numbers-to-from-global-channel-billing-us-zone-to-zone-b"
updated_at: 2026-09-15T00:00:00Z
tags: [support-docs]
source_path: "support-docs/9670281-transition-of-canadian-numbers-to-from-global-channel-billing-us-zone-to-zone-b.md"
generated_by: incremental-support-docs-wiki
---
<!-- generated_from=support-docs/9670281-transition-of-canadian-numbers-to-from-global-channel-billing-us-zone-to-zone-b.md -->

# Transition of Canadian Numbers to from Global Channel Billing US Zone to Zone B

## **How do I transition Canadian numbers in the Global Channel Billing US Zone to Zone B?**

There are a few steps to ensure a smooth transition to Zone B Channels.

1. ### **Purchase Zone B Channels**

   Before the change takes effect, you need to purchase Zone B channels to accommodate your inbound traffic for Canada numbers. You can do this in the “My Numbers” section of the Mission Control Portal and selecting ‘Channels’.

   Read our [Global Channel Billing Guide](https://support.telnyx.com/en/articles/8428806-global-channel-billing) for more details on channel zones.
2. ### **Update API Integration**

   If your setup includes API integration, note that the API endpoint for updating Zone B channels differs from US Zone channels. You can find the new endpoint in our [API documentation](https://developers.telnyx.com/api/global-channel-billing/get-channel-zones).

## **What is the difference in pricing between the US Zone and Zone B?**

While Zone B channels are more expensive than US Zones, users should note that **Telnyx will maintain the same price for any existing numbers moved to Zone B channels.**

Any duplicated Monthly Recurring Charges (MRCs) resulting from overlapping active channels during the migration period will be refunded to ensure you are not double-billed.

Below is a summary of the pricing tiers and associated discounts for ranges across US Zone and Zone B.

|  |
| --- |
| **US Zone** |
| 0-10 channels: $12 |
| 11-50 channels: $11 |
| 51-250 channels: $9.00 |
| 250+ channels: $8.00 |

|  |
| --- |
| **Zone B** |
| 0-10 channels: $20 |
| 11-50 channels: $19 |
| 51-250 channels: $15 |
| 250+ channels: $14 |

## **Post-migration checks to ensure a seamless transition**

It is essential to actively monitor and adjust your channel configurations during and after the migration to avoid any additional charges. Please ensure that channels moved to Zone B are correctly configured and any unnecessary channels in Zone US are removed.

1. ### **Remove Channels from Zone US**

   Ensure that Canadian numbers are moved to Global Channel Billing Zone B channels, that channels are correctly configured, and that any unnecessary channels in US Zone are removed to avoid incurring charges for both zones.
2. ### Monitor Configurations

   Regularly review your channel configurations to meet traffic needs and avoid unnecessary charges.
3. ### **Ensure Availability**

   Ensure you have sufficient Zone B channels to handle your inbound traffic, as the absence of available channels in the given zone will result in calls to those numbers being rejected.

We appreciate your cooperation and understanding. If you have any questions or need assistance, please do not hesitate to contact our support team in the [Misson Control Portal](https://portal.telnyx.com).

---

Related Articles

- [Channel Billing](https://support.telnyx.com/en/articles/8428806-channel-billing)
