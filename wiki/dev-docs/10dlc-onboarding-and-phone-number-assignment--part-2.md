---
title: 10DLC Onboarding and Phone Number Assignment
summary: Comprehensive guide to registering brands, vetting, creating campaigns, and
  assigning phone numbers for 10DLC A2P messaging on Telnyx — covering both direct
  customer and ISV/reseller architectures, plus bulk operations, webhooks, appeals,
  and troubleshooting.
sources:
- url: https://developers.telnyx.com/docs/messaging/10dlc/isv-reseller-onboarding
- url: https://developers.telnyx.com/docs/messaging/10dlc/phone-number-assignment
- url: https://developers.telnyx.com/docs/messaging/10dlc/quickstart/index
updated_at: 2026-08-05T13:48:57Z
---

# 10DLC Onboarding and Phone Number Assignment

*Part 2 of 5 — see also: [Part 1](10dlc-onboarding-and-phone-number-assignment--part-1.md), [Part 3](10dlc-onboarding-and-phone-number-assignment--part-3.md), [Part 4](10dlc-onboarding-and-phone-number-assignment--part-4.md), [Part 5](10dlc-onboarding-and-phone-number-assignment--part-5.md)*

Comprehensive guide to registering brands, vetting, creating campaigns, and assigning phone numbers for 10DLC A2P messaging on Telnyx — covering both direct customer and ISV/reseller architectures, plus bulk operations, webhooks, appeals, and troubleshooting.

## Step 3: Create a campaign

A campaign defines your messaging use case and is required for each distinct type of messaging you do. Create one campaign per customer, selecting the use case that matches the actual message content your platform sends.

### Common use case types

| Use Case | Description |
| --- | --- |
| `MIXED` | Multiple message types (most common) |
| `MARKETING` | Promotional messages |
| `CUSTOMER_CARE` | Support and service messages |
| `DELIVERY_NOTIFICATION` | Order/delivery updates |
| `ACCOUNT_NOTIFICATION` | Account alerts |
| `2FA` | Two-factor authentication |
| `SECURITY_ALERT` | Security notifications |
| `POLLING_VOTING` | Surveys and polls |
| `CHARITY` | Nonprofit messaging |
| `POLITICAL` | Political campaigns |

### Create via API

```bash
curl -X POST https://api.telnyx.com/v2/10dlc/campaign \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "brandId": "BRAND_ID",
    "usecase": "CUSTOMER_CARE",
    "description": "Platform notifications sent on behalf of Customer Corp customers",
    "sample1": "Hi {name}, your appointment is confirmed for {date} at {time}. Reply STOP to opt out.",
    "sample2": "Your order #{order_id} has shipped! Track at {url}. Reply STOP to unsubscribe.",
    "messageFlow": "Users opt in via web form at customercorp.com/sms-signup with clear consent language. STOP/HELP keywords are honored.",
    "helpMessage": "Customer Corp support: help@customercorp.com or call 1-800-555-0123. Reply STOP to opt out.",
    "optinKeywords": "START,YES,SUBSCRIBE",
    "optoutKeywords": "STOP,CANCEL,UNSUBSCRIBE,QUIT,END",
    "helpKeywords": "HELP,INFO",
    "numberPool": false,
    "subscriberOptin": true,
    "subscriberOptout": true,
    "subscriberHelp": true,
    "embeddedLink": true,
    "embeddedPhone": false
  }'
```

```python
import telnyx
import os

telnyx.api_key = os.environ["TELNYX_API_KEY"]

campaign = telnyx.Campaign.create(
    brand_id="BRAND_ID",
    usecase="CUSTOMER_CARE",
    description="Platform notifications sent on behalf of Customer Corp customers",
    sample1="Hi {name}, your appointment is confirmed for {date} at {time}. Reply STOP to opt out.",
    sample2="Your order #{order_id} has shipped! Track at {url}. Reply STOP to unsubscribe.",
    message_flow="Users opt in via web form at customercorp.com/sms-signup with clear consent language. STOP/HELP keywords are honored.",
    help_message="Customer Corp support: help@customercorp.com or call 1-800-555-0123. Reply STOP to opt out.",
    subscriber_optin=True,
    subscriber_optout=True,
    subscriber_help=True,
    embedded_link=True,
    embedded_phone=False,
)
print(f"Campaign ID: {campaign.id}")
```

```javascript
import Telnyx from "telnyx";

const telnyx = new Telnyx(process.env.TELNYX_API_KEY);

const { data: campaign } = await telnyx.messaging10dlc.campaigns.create({
  brandId: "BRAND_ID",
  usecase: "CUSTOMER_CARE",
  description: "Platform notifications on behalf of Customer Corp customers",
  sample1: "Hi {name}, your appointment is confirmed for {date} at {time}. Reply STOP to opt out.",
  sample2: "Your order #{order_id} has shipped! Track at {url}. Reply STOP to unsubscribe.",
  messageFlow: "Users opt in via web form with clear consent language. STOP/HELP honored.",
  helpMessage: "Customer Corp support: help@customercorp.com. Reply STOP to opt out.",
  subscriberOptin: true,
  subscriberOptout: true,
  subscriberHelp: true,
  embeddedLink: true,
  embeddedPhone: false,
});
console.log(`Campaign ID: ${campaign.id}`);
```

### ISV-specific requirements

- Sample messages must accurately reflect what your platform sends.
- Message flow must describe how **end users** (not your clients) consent to receive messages.
- Each campaign undergoes manual review by TCR — allow 5–10 business days.

### Portal flow

1. Go to [Campaigns](https://portal.telnyx.com/#/messaging-10dlc/campaigns) and click **Create New Campaign**.
2. Choose the use case that best matches your messaging purpose and click **Next**.
3. Review the carrier terms and your brand score. Click **Next**.
4. Add industry vertical, sample messages, and campaign attributes. Accept the terms and conditions.

Sample messages matter. Carriers review your sample messages during approval. Make them realistic and representative of your actual messaging, and include opt-out language (e.g., "Reply STOP to unsubscribe").

## Step 4: Share campaign to Telnyx (ISV only)

Once your campaign is approved at your upstream CSP, share it to Telnyx. The sharing process depends on your CSP, but the result is a campaign visible in the Telnyx Partner Campaigns API.

After sharing, verify the campaign appears on Telnyx:

```bash
# List all shared campaigns
curl -s https://api.telnyx.com/v2/10dlc/partner_campaigns \
  -H "Authorization: Bearer $TELNYX_API_KEY" | python3 -m json.tool

# Get a specific shared campaign
curl -s https://api.telnyx.com/v2/10dlc/partner_campaigns/{campaignId} \
  -H "Authorization: Bearer $TELNYX_API_KEY" | python3 -m json.tool
```

```python
import os
from telnyx import Telnyx

client = Telnyx(api_key=os.environ.get("TELNYX_API_KEY"))

# List all shared campaigns
page = client.messaging_10dlc.partner_campaigns.list()
for campaign in page.records:
    print(f"Campaign: {campaign.tcr_campaign_id} — Status: {campaign.campaign_status}")

# Get a specific campaign
campaign = client.messaging_10dlc.partner_campaigns.retrieve("CAMPAIGN_ID")
print(f"Brand: {campaign.brand_display_name}, Status: {campaign.campaign_status}")
```

```javascript
import Telnyx from "telnyx";

const client = new Telnyx(process.env.TELNYX_API_KEY);

// List all shared campaigns
for await (const campaign of client.messaging10dlc.partnerCampaigns.list()) {
  console.log(`Campaign: ${campaign.tcrCampaignId} — Status: ${campaign.campaignStatus}`);
}

// Get a specific campaign
const specific = await client.messaging10dlc.partnerCampaigns.retrieve("CAMPAIGN_ID");
console.log(`Brand: ${specific.brandDisplayName}`);
```
