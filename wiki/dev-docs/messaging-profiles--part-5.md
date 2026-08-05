---
title: Messaging Profiles
summary: A messaging profile is the central configuration object for Telnyx messaging.
  It groups phone numbers, defines webhook URLs, and controls features such as number
  pooling, smart encoding, MMS transcoding, MMS-to-SMS fallback, spend limits, and
  URL shortening. Every phone number used for messaging must be assigned to a messaging
  profile.
sources:
- url: https://developers.telnyx.com/docs/messaging/messages/messaging-profiles-overview/index
- url: https://developers.telnyx.com/docs/messaging/messages/mms-converter
- url: https://developers.telnyx.com/docs/messaging/messages/mms-transcoding/index
- url: https://developers.telnyx.com/docs/messaging/messages/number-pool/index
- url: https://developers.telnyx.com/docs/messaging/messages/phone-number-configuration/index
updated_at: 2026-08-05T13:56:37Z
---

# Messaging Profiles

*Part 5 of 6 — see also: [Part 1](messaging-profiles--part-1.md), [Part 2](messaging-profiles--part-2.md), [Part 3](messaging-profiles--part-3.md), [Part 4](messaging-profiles--part-4.md), [Part 6](messaging-profiles--part-6.md)*

A messaging profile is the central configuration object for Telnyx messaging. It groups phone numbers, defines webhook URLs, and controls features such as number pooling, smart encoding, MMS transcoding, MMS-to-SMS fallback, spend limits, and URL shortening. Every phone number used for messaging must be assigned to a messaging profile.

## Assign phone numbers

After creating a profile, assign phone numbers to it. You can also assign numbers in the [Telnyx Portal](https://portal.telnyx.com/#/app/messaging) by editing a messaging profile and selecting numbers.

```bash
curl -X POST https://api.telnyx.com/v2/messaging_profiles/{profile_id}/phone_numbers \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -d '{"phone_number_id": "your_phone_number_id"}'
```

```python
# List numbers on a profile
numbers = client.messaging_profiles.list_phone_numbers(
    "your_messaging_profile_id"
)

for number in numbers.data:
    print(f"{number.phone_number} ({number.type})")
```

```javascript
// List numbers on a profile
const numbers = await client.messagingProfiles.listPhoneNumbers(
  'your_messaging_profile_id'
);

numbers.data.forEach(n => {
  console.log(`${n.phone_number} (${n.type})`);
});
```

### List messaging-capable numbers

Find numbers on your account that support messaging:

```bash
curl -X GET "https://api.telnyx.com/v2/messaging_phone_numbers?page[size]=25" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

```python
import os
import requests

API_KEY = os.environ.get("TELNYX_API_KEY")
headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json",
}

response = requests.get(
    "https://api.telnyx.com/v2/messaging_phone_numbers",
    headers=headers,
    params={"page[size]": 25},
)
numbers = response.json()
for num in numbers.get("data", []):
    profile = num.get("messaging_profile_id") or "unassigned"
    print(f"{num['phone_number']} — profile: {profile}, features: {num.get('features', {})}")
```

```javascript
const axios = require('axios');

const headers = {
  Authorization: `Bearer ${process.env.TELNYX_API_KEY}`,
  'Content-Type': 'application/json',
};

const { data: numbers } = await axios.get(
  'https://api.telnyx.com/v2/messaging_phone_numbers',
  { headers, params: { 'page[size]': 25 } }
);

numbers.data.forEach(num => {
  const profile = num.messaging_profile_id || 'unassigned';
  console.log(`${num.phone_number} — profile: ${profile}`);
});
```

### Assign a number to a messaging profile

Link a phone number to a messaging profile to configure its webhook URLs and messaging behavior:

```bash
curl -X PATCH "https://api.telnyx.com/v2/messaging_phone_numbers/+15551234567" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -d '{
    "messaging_profile_id": "400174af-0a13-4e28-b4f5-example12345"
  }'
```

```python
phone_number = "+15551234567"
profile_id = "400174af-0a13-4e28-b4f5-example12345"

response = requests.patch(
    f"https://api.telnyx.com/v2/messaging_phone_numbers/{phone_number}",
    headers=headers,
    json={"messaging_profile_id": profile_id},
)
result = response.json()
print(f"Assigned {phone_number} to profile {result['data']['messaging_profile_id']}")
```

```javascript
const phoneNumber = '+15551234567';
const profileId = '400174af-0a13-4e28-b4f5-example12345';

const { data: result } = await axios.patch(
  `https://api.telnyx.com/v2/messaging_phone_numbers/${encodeURIComponent(phoneNumber)}`,
  { messaging_profile_id: profileId },
  { headers }
);
console.log(`Assigned ${phoneNumber} to profile ${result.data.messaging_profile_id}`);
```

### Retrieve number configuration

Check the current messaging configuration for a specific number:

```bash
curl -X GET "https://api.telnyx.com/v2/messaging_phone_numbers/+15551234567" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

```python
response = requests.get(
    f"https://api.telnyx.com/v2/messaging_phone_numbers/{phone_number}",
    headers=headers,
)
config = response.json()["data"]
print(f"Number: {config['phone_number']}")
print(f"Profile: {config['messaging_profile_id']}")
print(f"Features: {config.get('features', {})}")
print(f"Health: {config.get('health', {})}")
```

```javascript
const { data: config } = await axios.get(
  `https://api.telnyx.com/v2/messaging_phone_numbers/${encodeURIComponent(phoneNumber)}`,
  { headers }
);
console.log('Number:', config.data.phone_number);
console.log('Profile:', config.data.messaging_profile_id);
console.log('Features:', config.data.features);
```

Response fields include `phone_number` (E.164 formatted), `messaging_profile_id`, `type` (`long_code`, `toll_free`, `short_code`), `country_code`, `features` (enabled features such as SMS, MMS), `health` (number health indicators like message success rate), and `eligible_messaging_products`.

### Bulk assignment

Assign multiple numbers to a messaging profile at once by iterating over the assignment endpoint:

```bash
for number in "+15551234567" "+15559876543" "+15551112222"; do
  curl -X PATCH "https://api.telnyx.com/v2/messaging_phone_numbers/$number" \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer YOUR_API_KEY" \
    -d '{"messaging_profile_id": "400174af-0a13-4e28-b4f5-example12345"}'
done
```

```python
numbers_to_assign = ["+15551234567", "+15559876543", "+15551112222"]
profile_id = "400174af-0a13-4e28-b4f5-example12345"

for number in numbers_to_assign:
    response = requests.patch(
        f"https://api.telnyx.com/v2/messaging_phone_numbers/{number}",
        headers=headers,
        json={"messaging_profile_id": profile_id},
    )
    if response.status_code == 200:
        print(f"✓ Assigned {number}")
    else:
        print(f"✗ Failed {number}: {response.json().get('errors', [])}")
```

```javascript
const numbersToAssign = ['+15551234567', '+15559876543', '+15551112222'];
const profileId = '400174af-0a13-4e28-b4f5-example12345';

for (const number of numbersToAssign) {
  try {
    await axios.patch(
      `https://api.telnyx.com/v2/messaging_phone_numbers/${encodeURIComponent(number)}`,
      { messaging_profile_id: profileId },
      { headers }
    );
    console.log(`✓ Assigned ${number}`);
  } catch (error) {
    console.log(`✗ Failed ${number}: ${error.response?.data?.errors}`);
  }
}
```

### Unassign a number from a profile

Remove a number's messaging profile assignment by setting `messaging_profile_id` to `null`. Unassigning a number means it will no longer receive inbound message webhooks or be available for outbound messaging through that profile.

```bash
curl -X PATCH "https://api.telnyx.com/v2/messaging_phone_numbers/+15551234567" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -d '{
    "messaging_profile_id": null
  }'
```

```python
response = requests.patch(
    f"https://api.telnyx.com/v2/messaging_phone_numbers/{phone_number}",
    headers=headers,
    json={"messaging_profile_id": None},
)
print(f"Unassigned {phone_number} from messaging profile")
```

```javascript
await axios.patch(
  `https://api.telnyx.com/v2/messaging_phone_numbers/${encodeURIComponent(phoneNumber)}`,
  { messaging_profile_id: null },
  { headers }
);
console.log(`Unassigned ${phoneNumber} from messaging profile`);
```

### Messaging enablement by number type

Different number types have different requirements before they can send messages:

| Number Type | Messaging Ready? | Additional Steps Required |
| --- | --- | --- |
| **Long code (US)** | After 10DLC registration | Register brand + campaign |
| **Toll-free (US/CA)** | After verification | Submit toll-free verification |
| **Short code** | After provisioning | Short code setup |
| **Long code (non-US)** | Typically immediate | Check country-specific requirements |
| **Alphanumeric sender ID** | After registration | Alphanumeric ID setup |

US long codes without 10DLC registration will experience carrier filtering and potential message blocking. Always complete 10DLC registration before sending A2P messages on US long codes.
