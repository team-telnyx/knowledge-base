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

*Part 3 of 7 — see also: [Part 1](sole-proprietor-10dlc-registration--part-1.md), [Part 2](sole-proprietor-10dlc-registration--part-2.md), [Part 4](sole-proprietor-10dlc-registration--part-4.md), [Part 5](sole-proprietor-10dlc-registration--part-5.md), [Part 6](sole-proprietor-10dlc-registration--part-6.md), [Part 7](sole-proprietor-10dlc-registration--part-7.md)*

Sole Proprietor registration enables individuals and small businesses without a federal Tax ID (EIN) to register for 10DLC messaging. This page covers the API workflow for creating Sole Proprietor brands, completing OTP verification, and managing campaigns programmatically, along with troubleshooting guidance for common failures.

## Verify OTP PIN

After the user receives and provides the PIN, verify it:

```
curl -X PUT https://api.telnyx.com/v2/10dlc/brand/{brand_id}/smsOtp \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -d '{
    "otpPin": "123456"
  }'
```

```
import Telnyx from 'telnyx';

const client = new Telnyx({
  apiKey: process.env['TELNYX_API_KEY'],
});

await client.messaging10dlc.brand.verifySMSOtp(
  'f5586561-8ff0-4291-a0ac-84fe544797bd',
  { otpPin: '123456' }
);

console.log('Brand verified successfully');
```

```
import os
from telnyx import Telnyx

client = Telnyx(
    api_key=os.environ.get("TELNYX_API_KEY"),
)

client.messaging_10dlc.brand.verify_sms_otp(
    brand_id="f5586561-8ff0-4291-a0ac-84fe544797bd",
    otp_pin="123456",
)

print("Brand verified successfully")
```

```
require "telnyx"

client = Telnyx::Client.new(api_key: ENV["TELNYX_API_KEY"])

client.messaging_10dlc.brand.verify_sms_otp(
  "f5586561-8ff0-4291-a0ac-84fe544797bd",
  otp_pin: "123456"
)

puts("Brand verified successfully")
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
  err := client.Messaging10dlc.Brand.VerifySMSOtp(
    context.TODO(),
    "f5586561-8ff0-4291-a0ac-84fe544797bd",
    telnyx.Messaging10dlcBrandVerifySMSOtpParams{
      OtpPin: "123456",
    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Println("Brand verified successfully")
}
```

```
package com.telnyx.example;

import com.telnyx.sdk.client.TelnyxClient;
import com.telnyx.sdk.client.okhttp.TelnyxOkHttpClient;
import com.telnyx.sdk.models.messaging10dlc.brand.BrandVerifySmsOtpParams;

public final class Main {
    public static void main(String[] args) {
        TelnyxClient client = TelnyxOkHttpClient.fromEnv();

        BrandVerifySmsOtpParams params = BrandVerifySmsOtpParams.builder()
            .brandId("f5586561-8ff0-4291-a0ac-84fe544797bd")
            .otpPin("123456")
            .build();

        client.messaging10dlc().brand().verifySmsOtp(params);
        System.out.println("Brand verified successfully")
    }
}
```

Upon successful verification:

- The brand `identityStatus` changes to `VERIFIED`
- The `successSms` message is sent to the mobile phone
- The brand registration fee is charged
- You can now create campaigns
