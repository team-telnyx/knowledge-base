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

*Part 2 of 7 — see also: [Part 1](sole-proprietor-10dlc-registration--part-1.md), [Part 3](sole-proprietor-10dlc-registration--part-3.md), [Part 4](sole-proprietor-10dlc-registration--part-4.md), [Part 5](sole-proprietor-10dlc-registration--part-5.md), [Part 6](sole-proprietor-10dlc-registration--part-6.md), [Part 7](sole-proprietor-10dlc-registration--part-7.md)*

Sole Proprietor registration enables individuals and small businesses without a federal Tax ID (EIN) to register for 10DLC messaging. This page covers the API workflow for creating Sole Proprietor brands, completing OTP verification, and managing campaigns programmatically, along with troubleshooting guidance for common failures.

## Trigger OTP Verification

Send an OTP PIN to the mobile phone associated with the brand:

```
curl -X POST https://api.telnyx.com/v2/10dlc/brand/{brand_id}/smsOtp \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -d '{
    "pinSms": "Your Telnyx verification code is @OTP_PIN@. This code expires in 24 hours.",
    "successSms": "Your Telnyx 10DLC brand has been verified successfully."
  }'
```

```
import Telnyx from 'telnyx';

const client = new Telnyx({
  apiKey: process.env['TELNYX_API_KEY'],
});

const response = await client.messaging10dlc.brand.triggerSMSOtp(
  'f5586561-8ff0-4291-a0ac-84fe544797bd',
  {
    pinSms: 'Your Telnyx verification code is @OTP_PIN@. This code expires in 24 hours.',
    successSms: 'Your Telnyx 10DLC brand has been verified successfully.',
  }
);

console.log(response.referenceId);
```

```
import os
from telnyx import Telnyx

client = Telnyx(
    api_key=os.environ.get("TELNYX_API_KEY"),
)

response = client.messaging_10dlc.brand.trigger_sms_otp(
    brand_id="f5586561-8ff0-4291-a0ac-84fe544797bd",
    pin_sms="Your Telnyx verification code is @OTP_PIN@. This code expires in 24 hours.",
    success_sms="Your Telnyx 10DLC brand has been verified successfully.",
)

print(response.reference_id)
```

```
require "telnyx"

client = Telnyx::Client.new(api_key: ENV["TELNYX_API_KEY"])

response = client.messaging_10dlc.brand.trigger_sms_otp(
  "f5586561-8ff0-4291-a0ac-84fe544797bd",
  pin_sms: "Your Telnyx verification code is @OTP_PIN@. This code expires in 24 hours.",
  success_sms: "Your Telnyx 10DLC brand has been verified successfully."
)

puts(response)
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
  response, err := client.Messaging10dlc.Brand.TriggerSMSOtp(
    context.TODO(),
    "f5586561-8ff0-4291-a0ac-84fe544797bd",
    telnyx.Messaging10dlcBrandTriggerSMSOtpParams{
      PinSMS:     "Your Telnyx verification code is @OTP_PIN@. This code expires in 24 hours.",
      SuccessSMS: "Your Telnyx 10DLC brand has been verified successfully.",
    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("Reference ID: %s\n", response.ReferenceID)
}
```

```
package com.telnyx.example;

import com.telnyx.sdk.client.TelnyxClient;
import com.telnyx.sdk.client.okhttp.TelnyxOkHttpClient;
import com.telnyx.sdk.models.messaging10dlc.brand.BrandTriggerSmsOtpParams;
import com.telnyx.sdk.models.messaging10dlc.brand.BrandTriggerSmsOtpResponse;

public final class Main {
    public static void main(String[] args) {
        TelnyxClient client = TelnyxOkHttpClient.fromEnv();

        BrandTriggerSmsOtpParams params = BrandTriggerSmsOtpParams.builder()
            .brandId("f5586561-8ff0-4291-a0ac-84fe544797bd")
            .pinSms("Your Telnyx verification code is @OTP_PIN@. This code expires in 24 hours.")
            .successSms("Your Telnyx 10DLC brand has been verified successfully.")
            .build();

        BrandTriggerSmsOtpResponse response = client.messaging10dlc().brand().triggerSmsOtp(params);
        System.out.println("Reference ID: " + response.referenceId());
    }
}
```

### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| `pinSms` | string | Yes | SMS message containing `@OTP_PIN@` placeholder (max 500 chars) |
| `successSms` | string | Yes | Confirmation SMS sent after successful verification (max 500 chars) |

### Response

```
{
  "brandId": "f5586561-8ff0-4291-a0ac-84fe544797bd",
  "referenceId": "OTP8A3B2C"
}
```

The `@OTP_PIN@` placeholder in `pinSms` is replaced with the actual 6-digit PIN when the SMS is sent.

## Check OTP Status

Poll the OTP status to confirm delivery:

```
curl -X GET https://api.telnyx.com/v2/10dlc/brand/{brand_id}/smsOtp \
  -H "Authorization: Bearer YOUR_API_KEY"
```

```
import Telnyx from 'telnyx';

const client = new Telnyx({
  apiKey: process.env['TELNYX_API_KEY'],
});

const status = await client.messaging10dlc.brand.retrieveSMSOtpStatus(
  'f5586561-8ff0-4291-a0ac-84fe544797bd'
);

console.log(status.deliveryStatus);
console.log(status.verifyDate);
```

```
import os
from telnyx import Telnyx

client = Telnyx(
    api_key=os.environ.get("TELNYX_API_KEY"),
)

status = client.messaging_10dlc.brand.retrieve_sms_otp_status(
    "f5586561-8ff0-4291-a0ac-84fe544797bd",
)

print(status.delivery_status)
print(status.verify_date)
```

```
require "telnyx"

client = Telnyx::Client.new(api_key: ENV["TELNYX_API_KEY"])

status = client.messaging_10dlc.brand.retrieve_sms_otp_status(
  "f5586561-8ff0-4291-a0ac-84fe544797bd"
)

puts(status)
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
  status, err := client.Messaging10dlc.Brand.RetrieveSMSOtpStatus(
    context.TODO(),
    "f5586561-8ff0-4291-a0ac-84fe544797bd",
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("Delivery Status: %s\n", status.DeliveryStatus)
}
```

```
package com.telnyx.example;

import com.telnyx.sdk.client.TelnyxClient;
import com.telnyx.sdk.client.okhttp.TelnyxOkHttpClient;
import com.telnyx.sdk.models.messaging10dlc.brand.BrandSmsOtpStatus;

public final class Main {
    public static void main(String[] args) {
        TelnyxClient client = TelnyxOkHttpClient.fromEnv();

        BrandSmsOtpStatus status = client.messaging10dlc()
            .brand()
            .retrieveSmsOtpStatus("f5586561-8ff0-4291-a0ac-84fe544797bd");

        System.out.println("Delivery Status: " + status.deliveryStatus());
    }
}
```

### Response

```
{
  "brandId": "f5586561-8ff0-4291-a0ac-84fe544797bd",
  "referenceId": "OTP8A3B2C",
  "mobilePhone": "+12025559876",
  "requestDate": "2026-02-03T12:05:00Z",
  "verifyDate": null,
  "deliveryStatus": "DELIVERED_HANDSET",
  "deliveryStatusDate": "2026-02-03T12:05:02Z",
  "deliveryStatusDetails": "Delivered to handset"
}
```

### Delivery Status Values

| Status | Description |
| --- | --- |
| `PENDING` | OTP request submitted, awaiting delivery |
| `DELIVERED_HANDSET` | SMS delivered to the mobile device |
| `DELIVERY_FAILED` | SMS delivery failed |
| `VERIFIED` | OTP PIN successfully verified |
| `EXPIRED` | OTP PIN expired (24-hour window) |
