---
title: 10DLC Campaign Use Cases and Event Notifications
summary: Comprehensive guide to Telnyx 10DLC campaign use cases, sample messages,
  opt-in/opt-out requirements, and webhook event notifications for brands, campaigns,
  and phone numbers. Includes SDK examples, retry policies, and campaign appeal mechanisms.
sources:
- url: https://developers.telnyx.com/docs/messaging/10dlc/campaign-use-cases
- url: https://developers.telnyx.com/docs/messaging/10dlc/event-notifications/index
updated_at: 2026-08-05T13:49:31Z
---

# 10DLC Campaign Use Cases and Event Notifications

*Part 3 of 8 — see also: [Part 1](10dlc-campaign-use-cases-and-event-notifications--part-1.md), [Part 2](10dlc-campaign-use-cases-and-event-notifications--part-2.md), [Part 4](10dlc-campaign-use-cases-and-event-notifications--part-4.md), [Part 5](10dlc-campaign-use-cases-and-event-notifications--part-5.md), [Part 6](10dlc-campaign-use-cases-and-event-notifications--part-6.md), [Part 7](10dlc-campaign-use-cases-and-event-notifications--part-7.md), [Part 8](10dlc-campaign-use-cases-and-event-notifications--part-8.md)*

Comprehensive guide to Telnyx 10DLC campaign use cases, sample messages, opt-in/opt-out requirements, and webhook event notifications for brands, campaigns, and phone numbers. Includes SDK examples, retry policies, and campaign appeal mechanisms.

## Special Use Cases

### Low Volume

For brands sending fewer than 6,000 messages per month. Simplified registration with reduced documentation.

**Sample messages:** Same as whatever your primary use case is — low volume is about throughput, not content type. Use samples from the relevant standard use case above.

**Tips for approval:**

- Best for small businesses with limited messaging needs
- Lower throughput limits (75 messages/minute on T-Mobile)
- Cannot be upgraded to standard — must create a new campaign
- Still requires compliant opt-in and opt-out

### Sole Proprietor

For individuals or small businesses without an EIN. See the full [Sole Proprietor](sole-proprietor.md) guide.

### Emergency

For life-safety alerts. Requires demonstrating genuine emergency nature.

**Sample messages:**

```
EMERGENCY ALERT: Severe weather warning for your area. Tornado watch until 8 PM. Seek shelter immediately. Details: alerts.example.com. Reply STOP to opt out.
```

```
SafeAlert: Building evacuation in progress at 123 Main St. Exit via stairwell B. Do NOT use elevators. All clear will be sent when safe. Reply STOP to opt out.
```

**Tips for approval:**

- Must be genuinely life-safety related
- Carriers may grant higher throughput
- Don't abuse this category — misuse leads to suspension

## Writing Compliant Sample Messages

### Do's and Don'ts

**Do:**

- Include your brand name in every message
- Add opt-out language (STOP to opt out)
- Use specific, realistic content
- Match samples to your declared use case
- Show the actual format you'll send
- Include 3 distinct sample messages

**Don't:**

- Use generic placeholder text ("Hello, this is a test")
- Mix marketing into transactional use cases
- Use ALL CAPS for entire messages
- Include URL shorteners (bit.ly, tinyurl)
- Copy samples from other brands
- Submit identical or near-identical samples

### Opt-Out Language Requirements

Every campaign must support these keywords:

| Keyword | Required Response |
| --- | --- |
| `STOP` | "You have been unsubscribed from [Brand] messages. No more messages will be sent. Reply START to resubscribe." |
| `HELP` | "[Brand] support: For help, visit [url] or call [number]. Msg & data rates may apply. Msg frequency varies. Reply STOP to cancel." |
| `START` / `UNSTOP` | "You have been resubscribed to [Brand] messages. Reply STOP to opt out, HELP for help." |

Telnyx handles STOP/START/HELP keyword processing automatically when [Advanced Opt-Out](advanced-opt-out.md) is enabled on your messaging profile.

### Message Flow Description

Your campaign's `message_flow` field should clearly describe how users opt in. Carriers look for:

1. **Entry point** — How does the user first provide their phone number? (Website form, checkout, text-to-join keyword, etc.)
2. **Consent mechanism** — How is consent captured? (Checkbox, keyword reply, verbal confirmation, etc.)
3. **Confirmation** — What happens after opt-in? (Welcome message, double opt-in confirmation, etc.)
4. **Message types** — What kinds of messages will the user receive?

**Example message flow:**

```
Customers opt in by checking a consent checkbox during online checkout at
acme.com/checkout. After opting in, they receive a welcome message confirming
their subscription. They then receive order confirmations, shipping updates,
and delivery notifications related to their purchases. Customers can opt out
at any time by replying STOP.
```

## Common Rejection Reasons

| Rejection Reason | Fix |
| --- | --- |
| Sample messages don't match use case | Rewrite samples to clearly demonstrate your declared use case |
| Missing opt-out language | Add "Reply STOP to opt out" to every sample |
| Vague or generic samples | Use specific, realistic content with your brand name |
| Inadequate opt-in description | Detail the exact opt-in flow (where, how, what users see) |
| URL shorteners used | Use full branded URLs (acme.com/track, not bit.ly/abc) |
| Samples too similar | Make each sample distinctly different |
| Marketing content in non-marketing use case | Remove promotional language or switch to MIXED use case |

For detailed troubleshooting of campaign rejections, see the [10DLC Troubleshooting](10dlc-troubleshooting.md) guide.
