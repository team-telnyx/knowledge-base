---
title: Messaging Features
summary: Overview of Telnyx messaging features including short codes, smart encoding,
  MMS SMIL templates, and sticky sender for consistent number assignment.
sources:
- url: https://developers.telnyx.com/docs/messaging/messages/short-code/index
- url: https://developers.telnyx.com/docs/messaging/messages/smart-encoding/index
- url: https://developers.telnyx.com/docs/messaging/messages/smil-template
- url: https://developers.telnyx.com/docs/messaging/messages/sticky-sender/index
updated_at: 2026-08-05T13:57:46Z
---

# Messaging Features

*Part 3 of 3 — see also: [Part 1](messaging-features--part-1.md), [Part 2](messaging-features--part-2.md)*

Overview of Telnyx messaging features including short codes, smart encoding, MMS SMIL templates, and sticky sender for consistent number assignment.

## Modifying MMS SMIL Template

SMIL specifies how MMS media files are laid out in MMS. Telnyx generates SMIL automatically based on `media_urls` and `text` fields. Advanced users can add a `smil_template` parameter to the MMS message request. This template will then be used to generate a customized SMIL.

Example of SMIL template:

```
<smil>
	<head>
		<region id="Text" top="70%" left="0%" height="30%" width="100%" fit="scroll"/>
		<region id="Image" top="0%" left="0%" height="70%" width="100%" fit="meet"/>
	</head>
	<body>
		<par dur="10s">
			<text src="{{ text }}" region="Text" />
			<img src="{{ 0 }}" region="Image" />
		</par>
	</body>
</smil>
```

Note that the template has parameters enclosed in double braces `{{ }}`. During the construction of SMIL these parameters will be automatically replaced with locations of text and media contents. In case of media, `{{ 0 }}` will be replaced with the location of the first URL in the `media_urls` list, `{{ 1 }}` will be replaced with the location of the second URL in the `media_urls` list, and so on. `{{ text }}` will be replaced with the location of the `text` content.

The SMIL template must be set in `smil_template` parameter of the MMS request. It must be properly JSON-escaped:

```
{
	"from": "+13125551234",
	"to": "+18655551234",
	"text": "Hello from Telnyx",
	"media_urls": ["https://example.com/media.jpg"],
	"smil_template": "<smil>\n\t<head>\n\t\t<region id=\"Text\" top=\"70%\"..."
}
```

Please note that many modern handsets (most notably iPhones) ignore SMIL and use their own layout algorithm.

## Sticky Sender

Sticky Sender ensures the same phone number is used every time your application messages a particular recipient. This consistency builds familiarity — your customers see the same number each time, making your messages more recognizable and trustworthy.

Sticky Sender is part of **Number Pool** settings. You must have [Number Pool](number-pool.md) enabled to use Sticky Sender.

### When to use Sticky Sender

- **Customer Conversations** — Maintain consistent sender identity throughout multi-message conversations.
- **Recurring Notifications** — Appointment reminders, delivery updates, and alerts from a familiar number.
- **Support Interactions** — Customers can save your number knowing future messages will come from the same sender.
- **Brand Recognition** — Build trust by ensuring customers recognize your number over time.

### How it works

1. **First message:** Telnyx selects a number from your pool (using weights, geomatch, or availability)
2. **Mapping created:** The recipient-to-sender pairing is stored
3. **Future messages:** The same sender is automatically used for that recipient
4. **Mapping expires:** After 8 days of no messages, the mapping resets

**Mapping behavior:**

| Scenario | Behavior |
| --- | --- |
| Message sent within 8 days | Same sender reused, timer resets |
| No messages for 8+ days | Mapping expires, new sender assigned |
| Sticky Sender disabled | All mappings cleared immediately |
| Number removed from profile | Mappings to that number cleared |
| Sticky number unavailable | New number selected, new mapping created |

**Compare with Twilio:** Sticky Sender works similarly to Twilio's Messaging Services sticky sender feature. If you're migrating, the concept is the same — just configure it on your Messaging Profile instead.

### Prerequisites

- A [Messaging Profile](messaging-profile.md) with [Number Pool](number-pool.md) enabled
- At least one phone number assigned to the profile

### Configure Sticky Sender

Enable Sticky Sender by updating your Messaging Profile's `number_pool_settings`.

The `PATCH` endpoint merges with your existing configuration — only the fields you include are updated. Your current weights and other Number Pool settings are preserved.

```
curl -X PATCH "https://api.telnyx.com/v2/messaging_profiles/YOUR_PROFILE_ID" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -d '{
    "number_pool_settings": {
      "sticky_sender": true
    }
  }'
```

The response confirms your settings:

```
{
  "data": {
    "id": "YOUR_PROFILE_ID",
    "record_type": "messaging_profile",
    "name": "My Profile",
    "number_pool_settings": {
      "sticky_sender": true,
      "geomatch": false,
      "long_code_weight": 1,
      "toll_free_weight": 0,
      "skip_unhealthy": false
    }
  }
}
```

To configure via the portal, go to [Messaging](https://portal.telnyx.com/#/app/messaging), click the edit icon next to your Messaging Profile, under **Outbound** toggle on **Number Pool**, check the **Sticky Sender** checkbox, and click **Save**.

### Disable Sticky Sender

To disable Sticky Sender, set the `sticky_sender` field to `false`. This immediately clears all existing mappings.

```
curl -X PATCH "https://api.telnyx.com/v2/messaging_profiles/YOUR_PROFILE_ID" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -d '{
    "number_pool_settings": {
      "sticky_sender": false
    }
  }'
```

Disabling Sticky Sender clears all recipient-to-sender mappings. Re-enabling it starts fresh — previous mappings are not restored.

### Combining with other features

Sticky Sender works alongside other Number Pool settings. The priority order for number selection is:

1. **Sticky Sender** (if enabled and mapping exists)
2. **Geomatch** (if enabled and matching area code available)
3. **Weight distribution** (long code vs. toll-free preference)
4. **Skip unhealthy** (exclude poor-performing numbers)

**Sticky Sender + Geomatch:**

When both are enabled:

- **First message:** Geomatch selects a number matching the recipient's area code
- **Future messages:** Sticky Sender reuses that same geomatched number

This combination provides both local presence and consistency.

```
{
  "number_pool_settings": {
    "sticky_sender": true,
    "geomatch": true
  }
}
```

**Sticky Sender + Skip Unhealthy:**

If a sticky sender mapping points to a number that becomes unhealthy:

- The mapping is preserved
- Messages still route through that number (`skip_unhealthy` doesn't override sticky mappings)

To force re-selection, temporarily disable and re-enable Sticky Sender to clear mappings.

### Troubleshooting

**Recipient receiving messages from different numbers**

Possible causes:

- Sticky Sender not enabled on the Messaging Profile
- Previous mapping expired (8+ days since last message)
- A phone number was removed from the profile

Solutions:

1. Verify Sticky Sender is enabled in your profile settings
2. Send messages more frequently to prevent mapping expiration
3. Check that all expected numbers are still assigned to the profile

**Mapping not updating after adding new numbers**

Cause: Sticky Sender preserves existing mappings — adding new numbers doesn't affect recipients who already have mappings.

Solution: If you want recipients to potentially use new numbers, temporarily disable Sticky Sender to clear mappings, then re-enable it. New messages will be distributed across all available numbers.

**Checking current Sticky Sender status**

Retrieve your Messaging Profile to see current settings:

```
curl "https://api.telnyx.com/v2/messaging_profiles/YOUR_PROFILE_ID" \
  -H "Authorization: Bearer YOUR_API_KEY" | jq '.data.number_pool_settings'
```

Response:

```
{
  "sticky_sender": true,
  "geomatch": false,
  "long_code_weight": 1,
  "toll_free_weight": 0,
  "skip_unhealthy": false
}
```
