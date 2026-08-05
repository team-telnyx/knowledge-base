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

*Part 3 of 5 — see also: [Part 1](10dlc-onboarding-and-phone-number-assignment--part-1.md), [Part 2](10dlc-onboarding-and-phone-number-assignment--part-2.md), [Part 4](10dlc-onboarding-and-phone-number-assignment--part-4.md), [Part 5](10dlc-onboarding-and-phone-number-assignment--part-5.md)*

Comprehensive guide to registering brands, vetting, creating campaigns, and assigning phone numbers for 10DLC A2P messaging on Telnyx — covering both direct customer and ISV/reseller architectures, plus bulk operations, webhooks, appeals, and troubleshooting.

## Step 5: Assign phone numbers to the campaign

After your brand is registered and campaign is approved, assign phone numbers to the campaign before sending messages. Only numbers assigned to an active campaign can send 10DLC A2P messages.

### Requirements

| Requirement | Details |
| --- | --- |
| Number type | US long code (10-digit) numbers only |
| Messaging profile | Number must be assigned to a [messaging profile](messaging-profiles--part-1.md) first |
| Campaign status | Campaign must be `ACTIVE` (approved by carriers) |
| One campaign per number | Each number can only be assigned to one campaign at a time |

Numbers not assigned to an active 10DLC campaign will have messages filtered or blocked by carriers on AT&T, T-Mobile, and other major US networks.

### Assign a single number

```bash
curl -X POST https://api.telnyx.com/v2/10dlc/phoneNumberCampaign \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -d '{
    "phoneNumber": "+15551234567",
    "campaignId": "CAMPAIGN_ID"
  }'
```

```python
import os
import requests

API_KEY = os.environ.get("TELNYX_API_KEY")
headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json",
}

response = requests.post(
    "https://api.telnyx.com/v2/10dlc/phoneNumberCampaign",
    headers=headers,
    json={
        "phoneNumber": "+15551234567",
        "campaignId": "CAMPAIGN_ID",
    },
)
result = response.json()
print(f"Number: {result['data']['phoneNumber']}")
print(f"Status: {result['data']['status']}")
```

```javascript
const axios = require('axios');

const headers = {
  Authorization: `Bearer ${process.env.TELNYX_API_KEY}`,
  'Content-Type': 'application/json',
};

const response = await axios.post(
  'https://api.telnyx.com/v2/10dlc/phoneNumberCampaign',
  {
    phoneNumber: '+15551234567',
    campaignId: 'CAMPAIGN_ID',
  },
  { headers }
);

console.log(`Number: ${response.data.data.phoneNumber}`);
console.log(`Status: ${response.data.data.status}`);
```

Number-to-campaign assignment typically completes within minutes. A number can only be assigned to **one campaign at a time**. To reassign, remove the existing assignment first.

### Portal flow

1. Navigate to [Campaigns](https://portal.telnyx.com/#/messaging-10dlc/campaigns) and select the campaign you want to assign numbers to.
2. Click the **Assign Numbers** panel within your campaign details.
3. Choose the messaging profile that contains the numbers you want to assign.
4. Enter or select the phone numbers to assign to this campaign and click **Assign**.

### Bulk assignment

When assigning multiple numbers to the same campaign, loop through your numbers programmatically:

```python
import os
import requests
import time

API_KEY = os.environ.get("TELNYX_API_KEY")
headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json",
}

campaign_id = "CAMPAIGN_ID"
phone_numbers = [
    "+15551234567",
    "+15551234568",
    "+15551234569",
    "+15551234570",
    "+15551234571",
]

results = {"success": [], "failed": []}

for number in phone_numbers:
    try:
        response = requests.post(
            "https://api.telnyx.com/v2/10dlc/phoneNumberCampaign",
            headers=headers,
            json={"phoneNumber": number, "campaignId": campaign_id},
        )
        if response.status_code in (200, 201):
            results["success"].append(number)
            print(f"✓ {number} assigned")
        else:
            error = response.json().get("errors", [{}])[0].get("detail", "Unknown")
            results["failed"].append({"number": number, "error": error})
            print(f"✗ {number}: {error}")
    except Exception as e:
        results["failed"].append({"number": number, "error": str(e)})
    time.sleep(0.5)  # Rate limit safety

print(f"\nAssigned: {len(results['success'])}, Failed: {len(results['failed'])}")
```

```bash
#!/bin/bash
# Bulk assign numbers to a campaign
CAMPAIGN_ID="CAMPAIGN_ID"
NUMBERS=("+15551234567" "+15551234568" "+15551234569")

for NUM in "${NUMBERS[@]}"; do
  RESULT=$(curl -s -w "\n%{http_code}" -X POST \
    https://api.telnyx.com/v2/10dlc/phoneNumberCampaign \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer $TELNYX_API_KEY" \
    -d "{\"phoneNumber\": \"$NUM\", \"campaignId\": \"$CAMPAIGN_ID\"}")

  HTTP_CODE=$(echo "$RESULT" | tail -1)
  if [ "$HTTP_CODE" = "200" ] || [ "$HTTP_CODE" = "201" ]; then
    echo "✓ $NUM assigned"
  else
    echo "✗ $NUM failed (HTTP $HTTP_CODE)"
  fi
  sleep 0.5
done
```

### Number pool integration

If you are using [Number Pool](number-pool.md), numbers in the pool must also be assigned to a 10DLC campaign. The number pool distributes sending across multiple numbers, but each number still needs campaign registration.

1. Register your campaign via the [Campaign Registration](campaign-registration.md) guide.
2. Configure your [messaging profile](messaging-profiles--part-1.md) with number pool enabled.
3. Every number in the pool must be assigned to the same campaign. Use the bulk assignment method above.
4. List all numbers assigned to your campaign to confirm all pool numbers are included.

If a number in your pool is **not** assigned to a campaign, messages sent from that number will be filtered by carriers. This creates inconsistent delivery — some messages succeed, others fail depending on which pool number is selected.

### List assigned numbers

```bash
curl -s "https://api.telnyx.com/v2/10dlc/phoneNumberCampaign?filter[campaignId]=CAMPAIGN_ID" \
  -H "Authorization: Bearer YOUR_API_KEY" | jq '.data[] | {phoneNumber, status}'
```

```python
response = requests.get(
    "https://api.telnyx.com/v2/10dlc/phoneNumberCampaign",
    headers=headers,
    params={"filter[campaignId]": campaign_id},
)
numbers = response.json()["data"]
for n in numbers:
    print(f"{n['phoneNumber']} | {n['status']}")
```

### Remove a number from a campaign

```bash
curl -X DELETE "https://api.telnyx.com/v2/10dlc/phoneNumberCampaign/+15551234567" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

```python
response = requests.delete(
    "https://api.telnyx.com/v2/10dlc/phoneNumberCampaign/+15551234567",
    headers=headers,
)
print(f"Status: {response.status_code}")  # 200 = success
```

Removing a number from a campaign means it can no longer send 10DLC messages. You can reassign it to a different campaign afterward.

## Step 6: Check sharing status (ISV only)

Monitor whether Telnyx has accepted the shared campaign:

```bash
curl -s https://api.telnyx.com/v2/10dlc/partnerCampaign/{campaignId}/sharing \
  -H "Authorization: Bearer $TELNYX_API_KEY" | python3 -m json.tool
```

| Status | Meaning |
| --- | --- |
| `PENDING` | Campaign shared, awaiting Telnyx acceptance |
| `ACCEPTED` | Telnyx accepted — you can assign numbers and send traffic |
| `DECLINED` | Telnyx declined the sharing request |

## Step 7: Send messages

Once numbers are assigned to the accepted campaign, send messages using the standard [Send Message](send-message.md) API:

```bash
curl -X POST https://api.telnyx.com/v2/messages \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "from": "+12025551234",
    "to": "+13035551234",
    "text": "Hi Jane, your appointment is confirmed for March 15 at 2:00 PM. Reply STOP to opt out.",
    "messaging_profile_id": "YOUR_MESSAGING_PROFILE_ID"
  }'
```
