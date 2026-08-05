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

*Part 1 of 7 — see also: [Part 2](sole-proprietor-10dlc-registration--part-2.md), [Part 3](sole-proprietor-10dlc-registration--part-3.md), [Part 4](sole-proprietor-10dlc-registration--part-4.md), [Part 5](sole-proprietor-10dlc-registration--part-5.md), [Part 6](sole-proprietor-10dlc-registration--part-6.md), [Part 7](sole-proprietor-10dlc-registration--part-7.md)*

Sole Proprietor registration enables individuals and small businesses without a federal Tax ID (EIN) to register for 10DLC messaging. This page covers the API workflow for creating Sole Proprietor brands, completing OTP verification, and managing campaigns programmatically, along with troubleshooting guidance for common failures.

## Overview

Sole Proprietor (SP) brands let individuals and small businesses without a federal Tax ID (EIN) register for 10DLC messaging. Compared to standard business brands, SP brands have tighter constraints:

| Constraint | Limit |
| --- | --- |
| Campaigns per brand | 1 |
| Phone numbers per campaign | 1 |
| Mobile phone reuse | Max 3 SP brands per mobile number |
| Throughput | Low-volume (varies by carrier) |

Sole Proprietor registration requires identity verification via SMS OTP before campaigns can be created. SP campaigns are typically auto-approved and become `ACTIVE` immediately, unlike standard campaigns which may require carrier review.

## Prerequisites

- Telnyx account with API access
- At least one US 10DLC phone number
- Valid US/CA mobile phone number for OTP verification
- Personal information: name, address, date of birth

## Registration Flow

The end-to-end flow is: create the SP brand → trigger OTP → check OTP delivery → verify the PIN → create the campaign → assign a phone number.

## Create a Sole Proprietor Brand

Create a brand with `entityType` set to `SOLE_PROPRIETOR`. Valid `vertical` values include `PROFESSIONAL`, `REAL_ESTATE`, `HEALTHCARE`, `RETAIL`, `ENTERTAINMENT`, `EDUCATION`, `NONPROFIT`, `GOVERNMENT`, and others — see the [Brand API Reference](brand-api-reference.md) for the full list.

```
curl -X POST https://api.telnyx.com/v2/10dlc/brand \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -d '{
    "entityType": "SOLE_PROPRIETOR",
    "firstName": "Jane",
    "lastName": "Smith",
    "displayName": "Jane Smith Consulting",
    "email": "jane@example.com",
    "phone": "+12025551234",
    "mobilePhone": "+12025559876",
    "street": "123 Main St",
    "city": "Austin",
    "state": "TX",
    "postalCode": "78701",
    "country": "US",
    "vertical": "PROFESSIONAL"
  }'
```

```
import Telnyx from 'telnyx';

const client = new Telnyx({
  apiKey: process.env['TELNYX_API_KEY'],
});

const brand = await client.messaging10dlc.brand.create({
  entityType: 'SOLE_PROPRIETOR',
  firstName: 'Jane',
  lastName: 'Smith',
  displayName: 'Jane Smith Consulting',
  email: 'jane@example.com',
  phone: '+12025551234',
  mobilePhone: '+12025559876',
  street: '123 Main St',
  city: 'Austin',
  state: 'TX',
  postalCode: '78701',
  country: 'US',
  vertical: 'PROFESSIONAL',
});

console.log(brand.brandId);
console.log(brand.identityStatus);
```

```
import os
from telnyx import Telnyx

client = Telnyx(
    api_key=os.environ.get("TELNYX_API_KEY"),
)

brand = client.messaging_10dlc.brand.create(
    entity_type="SOLE_PROPRIETOR",
    first_name="Jane",
    last_name="Smith",
    display_name="Jane Smith Consulting",
    email="jane@example.com",
    phone="+12025551234",
    mobile_phone="+12025559876",
    street="123 Main St",
    city="Austin",
    state="TX",
    postal_code="78701",
    country="US",
    vertical="PROFESSIONAL",
)

print(brand.brand_id)
print(brand.identity_status)
```

```
require "telnyx"

client = Telnyx::Client.new(api_key: ENV["TELNYX_API_KEY"])

brand = client.messaging_10dlc.brand.create(
  entity_type: :SOLE_PROPRIETOR,
  first_name: "Jane",
  last_name: "Smith",
  display_name: "Jane Smith Consulting",
  email: "jane@example.com",
  phone: "+12025551234",
  mobile_phone: "+12025559876",
  street: "123 Main St",
  city: "Austin",
  state: "TX",
  postal_code: "78701",
  country: "US",
  vertical: :PROFESSIONAL
)

puts(brand)
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
  brand, err := client.Messaging10dlc.Brand.New(context.TODO(), telnyx.Messaging10dlcBrandNewParams{
    EntityType:  telnyx.EntityTypeSoleProprietor,
    FirstName:   "Jane",
    LastName:    "Smith",
    DisplayName: "Jane Smith Consulting",
    Email:       "jane@example.com",
    Phone:       "+12025551234",
    MobilePhone: "+12025559876",
    Street:      "123 Main St",
    City:        "Austin",
    State:       "TX",
    PostalCode:  "78701",
    Country:     "US",
    Vertical:    telnyx.VerticalProfessional,
  })
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("Brand ID: %s\n", brand.BrandID)
  fmt.Printf("Identity Status: %s\n", brand.IdentityStatus)
}
```

```
package com.telnyx.example;

import com.telnyx.sdk.client.TelnyxClient;
import com.telnyx.sdk.client.okhttp.TelnyxOkHttpClient;
import com.telnyx.sdk.models.messaging10dlc.brand.BrandCreateParams;
import com.telnyx.sdk.models.messaging10dlc.brand.EntityType;
import com.telnyx.sdk.models.messaging10dlc.brand.TelnyxBrand;
import com.telnyx.sdk.models.messaging10dlc.brand.Vertical;

public final class Main {
    public static void main(String[] args) {
        TelnyxClient client = TelnyxOkHttpClient.fromEnv();

        BrandCreateParams params = BrandCreateParams.builder()
            .entityType(EntityType.SOLE_PROPRIETOR)
            .firstName("Jane")
            .lastName("Smith")
            .displayName("Jane Smith Consulting")
            .email("jane@example.com")
            .phone("+12025551234")
            .mobilePhone("+12025559876")
            .street("123 Main St")
            .city("Austin")
            .state("TX")
            .postalCode("78701")
            .country("US")
            .vertical(Vertical.PROFESSIONAL)
            .build();

        TelnyxBrand brand = client.messaging10dlc().brand().create(params);
        System.out.println("Brand ID: " + brand.brandId());
        System.out.println("Identity Status: " + brand.identityStatus());
    }
}
```

### Response

```
{
  "brandId": "f5586561-8ff0-4291-a0ac-84fe544797bd",
  "entityType": "SOLE_PROPRIETOR",
  "displayName": "Jane Smith Consulting",
  "firstName": "Jane",
  "lastName": "Smith",
  "identityStatus": "PENDING",
  "mobilePhone": "+12025559876",
  "createdAt": "2026-02-03T12:00:00Z"
}
```

The brand remains in `PENDING` identity status until OTP verification is completed. You cannot create campaigns until the brand is `VERIFIED`.
