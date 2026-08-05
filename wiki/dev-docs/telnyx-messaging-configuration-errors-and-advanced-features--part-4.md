---
title: Telnyx Messaging Configuration, Errors, and Advanced Features
summary: This page consolidates Telnyx messaging configuration guidance, including
  messaging profile setup, configurable spend limits, error code handling, the Vercel
  Chat SDK adapter, and Geomatch for area-code-based sender selection. It covers prerequisites,
  environment variables, webhook setup, capability matrices, and best practices for
  production SMS/MMS workloads.
sources:
- url: https://developers.telnyx.com/docs/messaging/messages/chat-sdk-adapter
- url: https://developers.telnyx.com/docs/messaging/messages/configurable-spend-limits/index
- url: https://developers.telnyx.com/docs/messaging/messages/configuration-and-usage/index
- url: https://developers.telnyx.com/docs/messaging/messages/error-codes/index
- url: https://developers.telnyx.com/docs/messaging/messages/geomatch
updated_at: 2026-08-05T13:55:16Z
---

# Telnyx Messaging Configuration, Errors, and Advanced Features

*Part 4 of 4 — see also: [Part 1](telnyx-messaging-configuration-errors-and-advanced-features--part-1.md), [Part 2](telnyx-messaging-configuration-errors-and-advanced-features--part-2.md), [Part 3](telnyx-messaging-configuration-errors-and-advanced-features--part-3.md)*

This page consolidates Telnyx messaging configuration guidance, including messaging profile setup, configurable spend limits, error code handling, the Vercel Chat SDK adapter, and Geomatch for area-code-based sender selection. It covers prerequisites, environment variables, webhook setup, capability matrices, and best practices for production SMS/MMS workloads.

## Geomatch

Geomatch automatically selects sender numbers that share the same area code as your recipients. When enabled, Telnyx matches your outbound messages with locally-recognized numbers — boosting trust and engagement with your customers.

Geomatch is part of **Number Pool** settings. You must have Number Pool enabled to use Geomatch.

### When to Use Geomatch

- **Local Presence** — Appear local to recipients; messages from familiar area codes are more likely to be read and trusted.
- **Higher Engagement** — Local numbers typically see better response rates than out-of-area or toll-free numbers.
- **Multi-Region Campaigns** — Automatically match senders across different geographic areas without manual routing logic.
- **Customer Support** — Build rapport with customers who prefer communicating with local business numbers.

**NANP only**: Geomatch currently supports only North American numbers (US, Canada, Caribbean). International numbers don't participate in geomatching.

### How It Works

1. **Message sent**: Your app sends a message without specifying a `from` number (using Number Pool)
2. **Area code lookup**: Telnyx identifies the recipient's area code
3. **Pool search**: Telnyx searches your number pool for a matching area code
4. **Selection**: If found, that number is used; otherwise, a number with a different area code is selected

### Prerequisites

- A Messaging Profile with Number Pool enabled
- Phone numbers from multiple area codes assigned to the profile (for effective geomatching)

### Configure Geomatch

Enable Geomatch by updating your Messaging Profile's `number_pool_settings`:

```
curl -X PATCH "https://api.telnyx.com/v2/messaging_profiles/YOUR_PROFILE_ID" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -d '{
    "number_pool_settings": {
      "long_code_weight": 1,
      "geomatch": true
    }
  }'
```

The examples include `long_code_weight` to ensure Number Pool is active. If you already have Number Pool configured, you can omit weight fields — PATCH requests merge with existing settings.

To configure via the portal: go to **Messaging**, click the edit icon next to your Messaging Profile, under **Outbound** toggle on **Number Pool**, check the **Geomatch** option, and click **Save**.

### Selection Behavior

#### Selection Priority

When both Geomatch and Sticky Sender are enabled:

| Priority | Condition | Behavior |
| --- | --- | --- |
| 1 | Sticky mapping exists | Use the mapped sender (geomatch ignored) |
| 2 | No mapping + matching area code available | Use geomatched number, create sticky mapping |
| 3 | No mapping + no matching area code | Use any available number, create sticky mapping |

Sticky Sender takes precedence over Geomatch. Once a recipient is mapped to a sender, that sender is used regardless of area code matching.

#### Coverage Planning

For effective geomatching, ensure your number pool covers the area codes where your recipients are located:

| Coverage Level | Description | Example |
| --- | --- | --- |
| **Full coverage** | Numbers in all target area codes | Pool: 415, 212, 312, 305 for SF, NYC, Chicago, Miami campaigns |
| **Regional coverage** | Numbers per region, not every area code | Pool: 415 for CA, 212 for NY, 312 for IL |
| **Minimal coverage** | Single area code | Pool: Only 415 numbers (geomatch rarely activates) |

Use the Phone Numbers API to audit your pool's area code coverage. Search for numbers in missing area codes to improve geomatch rates.

### Disable Geomatch

To disable Geomatch while keeping Number Pool active:

```
curl -X PATCH "https://api.telnyx.com/v2/messaging_profiles/YOUR_PROFILE_ID" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -d '{
    "number_pool_settings": {
      "geomatch": false
    }
  }'
```

### Related Features

Geomatch works best combined with other Number Pool features:

- **Sticky Sender** — Maintain the same sender for each recipient. When combined with Geomatch, the first message uses geomatch selection and subsequent messages use the "stuck" sender (even if area code no longer matches).
- **Skip Unhealthy Numbers** — Exclude poorly performing numbers from the pool. A geomatched number will be skipped if `skip_unhealthy: true` is enabled and the number's deliverability rate is below 25% OR spam ratio exceeds 75%. The next best geomatch candidate is used instead.
- **Number Pool Weights** — Control the ratio of long codes to toll-free numbers. Geomatch respects these weights — if you weight toll-free higher, toll-free numbers are preferred even when long codes have matching area codes.

### Troubleshooting

**Messages not coming from matching area codes**

Possible causes:

- Geomatch not enabled on the profile
- No numbers with matching area code in your pool
- Sticky Sender is enabled and recipient already has a mapping to a different number
- Matching number is unhealthy and `skip_unhealthy` is enabled

Solution: Verify Geomatch is enabled, then check your pool's area code coverage. Use the portal or API to list numbers assigned to your messaging profile.

**Geomatch not working for international numbers**

Cause: Geomatch only supports NANP (North American Numbering Plan) numbers — US, Canada, and Caribbean. Solution: For international messaging, use explicit `from` numbers or rely on weight-based Number Pool selection.

**Geomatch not activating**

Possible causes:

- Number Pool is not enabled (Geomatch requires Number Pool)
- Only one number in the pool (nothing to match against)
- Sending with explicit `from` number (bypasses Number Pool entirely)

Solution: Ensure Number Pool is enabled with at least one weight > 0, verify multiple numbers are assigned to the profile, and omit `from` when sending to use the pool.

## Related Resources

- [Messaging Profiles API](https://developers.telnyx.com/docs/messaging/messages/messaging-profiles-overview/index)
- [Message Detail Records](https://developers.telnyx.com/docs/messaging/messages/message-detail-records/index)
- [Rate Limiting](https://developers.telnyx.com/docs/messaging/messages/rate-limiting/index)
- [Webhooks](https://developers.telnyx.com/docs/messaging/messages/webhooks/index)
- [Number Pool](https://developers.telnyx.com/docs/messaging/messages/number-pool)
- [Sticky Sender](https://developers.telnyx.com/docs/messaging/messages/sticky-sender)
- [10DLC Quickstart](https://developers.telnyx.com/docs/messaging/10dlc/quickstart/index)
- [Toll-Free Verification](https://developers.telnyx.com/docs/messaging/toll-free-verification)
- [Message Encoding](https://developers.telnyx.com/docs/messaging/messages/message-encoding/index)
- [API Error Codes](https://developers.telnyx.com/development/api-fundamentals/api-errors/index)
- [`@telnyx/chat-sdk-adapter` on npm](https://www.npmjs.com/package/@telnyx/chat-sdk-adapter)
- [Vercel Chat SDK adapter directory](https://chat-sdk.dev/adapters)
- [Chat SDK docs](https://chat-sdk.dev/docs)
