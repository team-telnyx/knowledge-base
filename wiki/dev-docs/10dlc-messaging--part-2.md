---
title: 10DLC Messaging
summary: 10DLC (10-Digit Long Code) is the industry standard for application-to-person
  (A2P) messaging on US long code numbers. Registering your brand and campaigns with
  The Campaign Registry (TCR) through Telnyx provides higher throughput, better deliverability,
  and reduced carrier filtering. Your brand's vetting score directly determines your
  messaging throughput limits across AT&T, T-Mobile, and other carriers.
sources:
- url: https://developers.telnyx.com/docs/messaging/10dlc/10dlc-rate-limits/index
- url: https://developers.telnyx.com/docs/messaging/10dlc/brand-registration/index
- url: https://developers.telnyx.com/docs/messaging/10dlc/campaign-registration/index
- url: https://developers.telnyx.com/docs/messaging/10dlc/campaign-use-cases
- url: https://developers.telnyx.com/docs/messaging/10dlc/event-notifications/index
- url: https://developers.telnyx.com/docs/messaging/10dlc/isv-reseller-onboarding
- url: https://developers.telnyx.com/docs/messaging/10dlc/phone-number-assignment
- url: https://developers.telnyx.com/docs/messaging/10dlc/quickstart/index
- url: https://developers.telnyx.com/docs/messaging/10dlc/sole-proprietor/index
- url: https://developers.telnyx.com/docs/messaging/10dlc/troubleshooting/index
- url: https://developers.telnyx.com/docs/messaging/getting-started/choosing-your-sender-type/index
updated_at: 2026-06-11T10:36:45Z
---

# 10DLC Messaging

*Part 2 of 5 — see also: [Part 1](10dlc-messaging--part-1.md), [Part 3](10dlc-messaging--part-3.md), [Part 4](10dlc-messaging--part-4.md), [Part 5](10dlc-messaging--part-5.md)*

10DLC (10-Digit Long Code) is the industry standard for application-to-person (A2P) messaging on US long code numbers. Registering your brand and campaigns with The Campaign Registry (TCR) through Telnyx provides higher throughput, better deliverability, and reduced carrier filtering. Your brand's vetting score directly determines your messaging throughput limits across AT&T, T-Mobile, and other carriers.

## Campaign Registration

A 10DLC campaign defines your messaging use case — what you're sending, who you're sending to, and how recipients opted in. Every campaign must be registered with TCR and approved by mobile carriers before you can send messages at scale.

### Campaign Use Case Types

**Standard use cases:**

| Use Case | API Value | Description |
| --- | --- | --- |
| Customer Care | `CUSTOMER_CARE` | Support and service messages |
| Delivery Notification | `DELIVERY_NOTIFICATION` | Order and shipping updates |
| Account Notification | `ACCOUNT_NOTIFICATION` | Account alerts and changes |
| Marketing | `MARKETING` | Promotional content |
| 2FA | `2FA` | Two-factor authentication codes |
| Security Alert | `SECURITY_ALERT` | Security-related notifications |
| Polling & Voting | `POLLING_VOTING` | Surveys and polls |
| Charity | `CHARITY` | Nonprofit fundraising and awareness |
| Political | `POLITICAL` | Political campaigns and advocacy |
| Mixed | `MIXED` | Multiple message types (most common) |

**Special use cases:**

| Use Case | API Value | Requirements |
| --- | --- | --- |
| Low Volume | `LOW_VOLUME` | Under 6,000 messages/month; simplified registration |
| Sole Proprietor | `SOLE_PROPRIETOR` | Individual/small business without EIN |
| Emergency | `EMERGENCY` | Life-threatening alerts; must demonstrate emergency nature |
| Agents & Franchises | `AGENTS_FRANCHISES` | ISVs sending on behalf of clients |
| Sweepstakes | `SWEEPSTAKES` | Contests and giveaways; must include rules and terms |

Choose carefully — changing a campaign's use case after registration requires creating a new campaign. Carriers reject campaigns where sample messages don't match the declared use case.

### Creating a Campaign

**Required fields:** `brandId`, `usecase`, `description` (2–4 sentences), `sample1`, `sample2`, `messageFlow`, `helpMessage`, `optinKeywords`, `optoutKeywords`, `helpKeywords`.

**Optional fields:** `embeddedLink` (boolean), `embeddedPhone`, `numberPool`, `ageGated`, `directLending`, `subscriberOptin`, `subscriberOptout`, `subscriberHelp`, `sample3`–`sample5`.

```
curl -X POST https://api.telnyx.com/v2/10dlc/campaignBuilder \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -d '{
    "brandId": "BRAND_ID",
    "usecase": "DELIVERY_NOTIFICATION",
    "description": "Order confirmation and delivery status updates for e-commerce customers.",
    "sample1": "Hi {{name}}, your order #{{orderId}} has been confirmed! Track at https://acme.com/track/{{orderId}} Reply STOP to opt out.",
    "sample2": "Your package is out for delivery and should arrive by 5 PM today. Reply STOP to unsubscribe.",
    "messageFlow": "Customers opt in at checkout by checking a consent box.",
    "helpMessage": "Acme Corp order updates. For help, visit https://acme.com/support. Reply STOP to cancel.",
    "optinKeywords": "START, YES, SUBSCRIBE",
    "optoutKeywords": "STOP, UNSUBSCRIBE, CANCEL, QUIT",
    "helpKeywords": "HELP, INFO",
    "embeddedLink": true
  }'
```

### Campaign Statuses

| Status | Meaning |
| --- | --- |
| `ACTIVE` | Approved and ready to send |
| `EXPIRED` | Campaign expired (renew required) |
| `SUSPENDED` | Suspended by carrier — contact support |

### MNO Provisioning Timeline

After TCR approves your campaign, each carrier provisions it independently:

| Carrier | Typical Timeline | Notes |
| --- | --- | --- |
| T-Mobile | Instant to 24 hours | Usually the fastest |
| AT&T | 1–3 business days | May require additional review |
| Verizon | 1–3 business days | — |
| US Cellular | 3–5 business days | Smaller carrier, longer provisioning |

Check provisioning status per carrier via the API: `GET /v2/10dlc/campaignBuilder/{campaignId}` and inspect `.data.mnoMetadata`.

### Campaign Status Lifecycle

**Success path:** `TCR_PENDING` → `TCR_ACCEPTED` → `MNO_PENDING` → `MNO_PROVISIONED`

**Failure and suspension statuses:**

| Status | Description |
| --- | --- |
| `TCR_FAILED` | Rejected by TCR during initial registration |
| `TELNYX_FAILED` | Rejected by Telnyx compliance review; can be appealed |
| `MNO_REJECTED` | Rejected by one or more MNOs; can be appealed |
| `TCR_SUSPENDED` | Suspended due to compliance issues |
| `TCR_EXPIRED` | Expired and no longer active |

## Campaign Use Cases and Sample Messages

Writing good sample messages is the #1 factor in getting your campaign approved. Carriers reject campaigns when samples don't match the declared use case, lack opt-out language, or look like spam.

### Sample Message Requirements

- Must match the declared use case type
- Must include opt-out language ("Reply STOP to opt out")
- Must represent actual messages you'll send
- Vague or generic samples get rejected
- Provide 2–5 diverse samples showing different message types

### Tips for Each Use Case

**2FA:** Keep messages under 160 characters, include the code prominently, add an expiry time, don't include marketing content or links, brand name should appear in the message.

**Customer Care:** Messages should be reactive (responding to customer actions), include ticket/order numbers, don't mix in promotional content, keep a helpful tone.

**Delivery Notifications:** Include order/tracking numbers, follow the order lifecycle, include delivery estimates, don't add promotional upsells.

**Account Notifications:** Focus on account changes the user initiated, include specific details (amounts, dates), provide a way to verify or dispute changes, never include marketing.

**Marketing:** Opt-in MUST be separate from Terms of Service (not buried in fine print). Include message frequency estimate. State "consent is not a condition of purchase." Link to privacy policy and terms. Every message must include opt-out language.

**Security Alerts:** Include specific details (device, location, time), always provide a way to take action, keep urgency appropriate.

**Polling & Voting:** Keep surveys short (1–2 questions per message), make responses simple (numbers, YES/NO, letters), don't disguise marketing as surveys.

**Charity / Nonprofit:** Clearly identify your nonprofit in every message, show impact not just ask for money, include donation receipts/acknowledgments.

**Mixed (most common):** Each sample should demonstrate a DIFFERENT message type. Opt-in must mention ALL types of messages (transactional + marketing). If you include marketing, follow marketing opt-in rules. This is the safest choice if you're unsure which use case to pick.

### Opt-Out Language Requirements

Every campaign must support these keywords:

| Keyword | Required Response |
| --- | --- |
| `STOP` | "You have been unsubscribed from [Brand] messages. No more messages will be sent. Reply START to resubscribe." |
| `HELP` | "[Brand] support: For help, visit [url] or call [number]. Msg & data rates may apply. Msg frequency varies. Reply STOP to cancel." |
| `START` / `UNSTOP` | "You have been resubscribed to [Brand] messages. Reply STOP to opt out, HELP for help." |

Telnyx handles STOP/START/HELP keyword processing automatically when Advanced Opt-Out is enabled on your messaging profile.

### Message Flow Description

Your campaign's `messageFlow` field should clearly describe: (1) the entry point — how the user provides their phone number, (2) the consent mechanism — how consent is captured, (3) confirmation — what happens after opt-in, (4) message types — what kinds of messages the user will receive.
