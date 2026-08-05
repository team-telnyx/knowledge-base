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

*Part 4 of 7 — see also: [Part 1](sole-proprietor-10dlc-registration--part-1.md), [Part 2](sole-proprietor-10dlc-registration--part-2.md), [Part 3](sole-proprietor-10dlc-registration--part-3.md), [Part 5](sole-proprietor-10dlc-registration--part-5.md), [Part 6](sole-proprietor-10dlc-registration--part-6.md), [Part 7](sole-proprietor-10dlc-registration--part-7.md)*

Sole Proprietor registration enables individuals and small businesses without a federal Tax ID (EIN) to register for 10DLC messaging. This page covers the API workflow for creating Sole Proprietor brands, completing OTP verification, and managing campaigns programmatically, along with troubleshooting guidance for common failures.

## Create a Sole Proprietor Campaign

With a verified brand, create a campaign using the `SOLE_PROPRIETOR` usecase. Sample messages (`sample1`, `sample2`) are required for campaign approval — include realistic examples of messages you'll send.

```
curl -X POST https://api.telnyx.com/v2/10dlc/campaignBuilder \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -d '{
    "brandId": "f5586561-8ff0-4291-a0ac-84fe544797bd",
    "usecase": "SOLE_PROPRIETOR",
    "description": "Customer appointment reminders and booking confirmations for consulting services.",
    "messageFlow": "Customers opt-in via web form when booking appointments. They receive confirmation and reminder messages.",
    "helpMessage": "Reply HELP for assistance. Contact support@example.com",
    "optoutMessage": "Reply STOP to unsubscribe from messages.",
    "sample1": "Hi Jane, this is a reminder of your appointment tomorrow at 2pm.",
    "sample2": "Your booking for March 15th has been confirmed. Reply STOP to opt out.",
    "termsAndConditions": true
  }'
```

```
import Telnyx from 'telnyx';

const client = new Telnyx({
  apiKey: process.env['TELNYX_API_KEY'],
});

const campaign = await client.messaging10dlc.campaignBuilder.submit({
  brandId: 'f5586561-8ff0-4291-a0ac-84fe544797bd',
  usecase: 'SOLE_PROPRIETOR',
  description: 'Customer appointment reminders and booking confirmations for consulting services.',
  messageFlow: 'Customers opt-in via web form when booking appointments. They receive confirmation and reminder messages.',
  helpMessage: 'Reply HELP for assistance. Contact support@example.com',
  optoutMessage: 'Reply STOP to unsubscribe from messages.',
  sample1: 'Hi Jane, this is a reminder of your appointment tomorrow at 2pm.',
  sample2: 'Your booking for March 15th has been confirmed. Reply STOP to opt out.',
  termsAndConditions: true,
});

console.log(campaign.campaignId);
console.log(campaign.status);
```

```
import os
from telnyx import Telnyx

client = Telnyx(
    api_key=os.environ.get("TELNYX_API_KEY"),
)

campaign = client.messaging_10dlc.campaign_builder.submit(
    brand_id="f5586561-8ff0-4291-a0ac-84fe544797bd",
    usecase="SOLE_PROPRIETOR",
    description="Customer appointment reminders and booking confirmations for consulting services.",
    message_flow="Customers opt-in via web form when booking appointments. They receive confirmation and reminder messages.",
    help_message="Reply HELP for assistance. Contact support@example.com",
    optout_message="Reply STOP to unsubscribe from messages.",
    sample1="Hi Jane, this is a reminder of your appointment tomorrow at 2pm.",
    sample2="Your booking for March 15th has been confirmed. Reply STOP to opt out.",
    terms_and_conditions=True,
)

print(campaign.campaign_id)
```

```
require "telnyx"

client = Telnyx::Client.new(api_key: ENV["TELNYX_API_KEY"])

campaign = client.messaging_10dlc.campaign_builder.submit(
  brand_id: "f5586561-8ff0-4291-a0ac-84fe544797bd",
  usecase: "SOLE_PROPRIETOR",
  description: "Customer appointment reminders and booking confirmations for consulting services.",
  message_flow: "Customers opt-in via web form when booking appointments. They receive confirmation and reminder messages.",
  help_message: "Reply HELP for assistance. Contact support@example.com",
  optout_message: "Reply STOP to unsubscribe from messages.",
  sample1: "Hi Jane, this is a reminder of your appointment tomorrow at 2pm.",
  sample2: "Your booking for March 15th has been confirmed. Reply STOP to opt out.",
  terms_and_conditions: true
)

puts(campaign)
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
  campaign, err := client.Messaging10dlc.CampaignBuilder.Submit(context.TODO(), telnyx.Messaging10dlcCampaignBuilderSubmitParams{
    BrandID:            "f5586561-8ff0-4291-a0ac-84fe544797bd",
    Usecase:            "SOLE_PROPRIETOR",
    Description:        "Customer appointment reminders and booking confirmations for consulting services.",
    MessageFlow:        "Customers opt-in via web form when booking appointments. They receive confirmation and reminder messages.",
    HelpMessage:        "Reply HELP for assistance. Contact support@example.com",
    OptoutMessage:      "Reply STOP to unsubscribe from messages.",
    Sample1:            "Hi Jane, this is a reminder of your appointment tomorrow at 2pm.",
    Sample2:            "Your booking for March 15th has been confirmed. Reply STOP to opt out.",
    TermsAndConditions: true,
  })
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("Campaign ID: %s\n", campaign.CampaignID)
}
```

```
package com.telnyx.example;

import com.telnyx.sdk.client.TelnyxClient;
import com.telnyx.sdk.client.okhttp.TelnyxOkHttpClient;
import com.telnyx.sdk.models.messaging10dlc.campaign.TelnyxCampaignCsp;
import com.telnyx.sdk.models.messaging10dlc.campaignbuilder.CampaignBuilderSubmitParams;

public final class Main {
    public static void main(String[] args) {
        TelnyxClient client = TelnyxOkHttpClient.fromEnv();

        CampaignBuilderSubmitParams params = CampaignBuilderSubmitParams.builder()
            .brandId("f5586561-8ff0-4291-a0ac-84fe544797bd")
            .usecase("SOLE_PROPRIETOR")
            .description("Customer appointment reminders and booking confirmations for consulting services.")
            .messageFlow("Customers opt-in via web form when booking appointments. They receive confirmation and reminder messages.")
            .helpMessage("Reply HELP for assistance. Contact support@example.com")
            .optoutMessage("Reply STOP to unsubscribe from messages.")
            .sample1("Hi Jane, this is a reminder of your appointment tomorrow at 2pm.")
            .sample2("Your booking for March 15th has been confirmed. Reply STOP to opt out.")
            .termsAndConditions(true)
            .build();

        TelnyxCampaignCsp campaign = client.messaging10dlc().campaignBuilder().submit(params);
        System.out.println("Campaign ID: " + campaign.campaignId());
    }
}
```

### Response

```
{
  "campaignId": "c5e5e598-95b3-4076-bfe2-c7d2c58ec57f",
  "brandId": "f5586561-8ff0-4291-a0ac-84fe544797bd",
  "usecase": "SOLE_PROPRIETOR",
  "status": "ACTIVE",
  "description": "Customer appointment reminders and booking confirmations for consulting services.",
  "createdAt": "2026-02-03T12:30:00Z"
}
```
