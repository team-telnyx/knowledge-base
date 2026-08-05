---
title: Sole Proprietor 10DLC Registration
summary: Sole Proprietor registration enables individuals and small businesses without
  a federal Tax ID (EIN) to register for 10DLC messaging. This page covers the API
  workflow for creating Sole Proprietor brands, completing OTP verification, and managing
  campaigns programmatically, along with troubleshooting guidance for common failures.
sources:
- url: https://developers.telnyx.com/docs/messaging/10dlc/sole-proprietor/index
- url: https://developers.telnyx.com/docs/messaging/10dlc/troubleshooting/index
updated_at: 2026-08-05T13:49:22Z
---

# Sole Proprietor 10DLC Registration

*Part 5 of 7 — see also: [Part 1](sole-proprietor-10dlc-registration--part-1.md), [Part 2](sole-proprietor-10dlc-registration--part-2.md), [Part 3](sole-proprietor-10dlc-registration--part-3.md), [Part 4](sole-proprietor-10dlc-registration--part-4.md), [Part 6](sole-proprietor-10dlc-registration--part-6.md), [Part 7](sole-proprietor-10dlc-registration--part-7.md)*

Sole Proprietor registration enables individuals and small businesses without a federal Tax ID (EIN) to register for 10DLC messaging. This page covers the API workflow for creating Sole Proprietor brands, completing OTP verification, and managing campaigns programmatically, along with troubleshooting guidance for common failures.

## Assign a Phone Number

Assign your 10DLC number to the campaign:

```
curl -X POST https://api.telnyx.com/v2/10dlc/phone_number_campaigns \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -d '{
    "phoneNumber": "+12025551234",
    "campaignId": "campaign_id_here"
  }'
```

```
import Telnyx from 'telnyx';

const client = new Telnyx({
  apiKey: process.env['TELNYX_API_KEY'],
});

const assignment = await client.messaging10dlc.phoneNumberCampaigns.create({
  phoneNumber: '+12025551234',
  campaignId: 'campaign_id_here',
});

console.log(assignment.campaignId);
```

```
import os
from telnyx import Telnyx

client = Telnyx(
    api_key=os.environ.get("TELNYX_API_KEY"),
)

assignment = client.messaging_10dlc.phone_number_campaigns.create(
    phone_number="+12025551234",
    campaign_id="campaign_id_here",
)

print(assignment.campaign_id)
```

```
require "telnyx"

client = Telnyx::Client.new(api_key: ENV["TELNYX_API_KEY"])

assignment = client.messaging_10dlc.phone_number_campaigns.create(
  phone_number: "+12025551234",
  campaign_id: "campaign_id_here"
)

puts(assignment)
```

```
package main

import (
  "context"
  "fmt"
  "os"

  "github.com/team-telnyx/telnyx-go"
  "github.com/team-telnyx/telnyx-go/option"
)

func main() {
  client := telnyx.NewClient(
    option.WithAPIKey(os.Getenv("TELNYX_API_KEY")),
  )
  assignment, err := client.Messaging10dlc.PhoneNumberCampaigns.New(context.TODO(), telnyx.Messaging10dlcPhoneNumberCampaignNewParams{
    PhoneNumberCampaignCreate: telnyx.PhoneNumberCampaignCreateParam{
      PhoneNumber: "+12025551234",
      CampaignID:  "campaign_id_here",
    },
  })
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("Assignment: %+v\n", assignment)
}
```

```
package com.telnyx.example;

import com.telnyx.sdk.client.TelnyxClient;
import com.telnyx.sdk.client.okhttp.TelnyxOkHttpClient;
import com.telnyx.sdk.models.messaging10dlc.phonenumbercampaigns.PhoneNumberCampaign;
import com.telnyx.sdk.models.messaging10dlc.phonenumbercampaigns.PhoneNumberCampaignCreate;

public final class Main {
    public static void main(String[] args) {
        TelnyxClient client = TelnyxOkHttpClient.fromEnv();

        PhoneNumberCampaignCreate params = PhoneNumberCampaignCreate.builder()
            .phoneNumber("+12025551234")
            .campaignId("campaign_id_here")
            .build();

        PhoneNumberCampaign assignment = client.messaging10dlc().phoneNumberCampaigns().create(params);
        System.out.println("Campaign ID: " + assignment.campaignId());
    }
}
```

Sole Proprietor campaigns can only have **one phone number** assigned. Attempting to assign additional numbers returns an error.

## Fees

| Item | Amount | Frequency |
| --- | --- | --- |
| Brand Registration | $4.00 | One-time (charged after verification) |
| Campaign Vetting | $15.00 | Per submission |
| Monthly Maintenance | $2.00 | Monthly |

## Webhooks

Subscribe to brand and campaign status updates via webhooks. See [10DLC Event Notifications](10dlc-event-notifications.md) for details on:

- `10dlc.brand.update` — Brand status and identity verification changes
- `10dlc.campaign.update` — Campaign approval/rejection
- `10dlc.phone_number.update` — Phone number assignment status

## Error Handling

### Common Errors

| Error | Cause | Solution |
| --- | --- | --- |
| `Sole Proprietor brands can only have one active campaign` | Attempting to create a second campaign | Delete or deactivate existing campaign first |
| `Sole Proprietor campaigns can only have one phone number assigned` | Attempting to assign multiple numbers | Use only one number per SP campaign |
| `Cannot associate campaign with brand in pending or failed status` | Brand not verified | Complete OTP verification first |
| `OTP PIN expired` | 24-hour verification window exceeded | Trigger a new OTP with `POST /10dlc/brand/{id}/smsOtp` |

### Retrying OTP

If the OTP expires or the user needs a new PIN, call the trigger endpoint again:

```
curl -X POST https://api.telnyx.com/v2/10dlc/brand/{brand_id}/smsOtp \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -d '{
    "pinSms": "Your new Telnyx verification code is @OTP_PIN@. This code expires in 24 hours.",
    "successSms": "Your Telnyx 10DLC brand has been verified successfully."
  }'
```
