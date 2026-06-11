---
title: Telnyx Messaging
summary: Telnyx Messaging provides a comprehensive API for sending and receiving SMS
  and MMS messages, with features including messaging profiles, alphanumeric sender
  IDs, geomatching, group messaging, two-factor authentication, appointment reminders,
  advanced opt-in/out handling, configurable spend limits, hosted SMS, and detailed
  error handling.
sources:
- url: https://developers.telnyx.com/docs/messaging/messages/2fa/index
  content_hash: e660dfc64ea2a2d6911f7d1a970f5a932c04da65aae78776e3c1ca3b18448b6d
- url: https://developers.telnyx.com/docs/messaging/messages/advanced-opt-in-out/index
  content_hash: 5fd82d8d9312b6ac6e28c0c73d0a00bf774769a0dd423127c48f73f591d7b3b9
- url: https://developers.telnyx.com/docs/messaging/messages/alphanumeric-sender-id/index
  content_hash: abbae58584ee6800d04c5231b8e3b77d97f8af428a35e1c1433eb2378e318112
- url: https://developers.telnyx.com/docs/messaging/messages/appointment-reminder
  content_hash: 6985fd062cf97e7e1fbaad7066a3bf2314c4f3753dd0115043ce47f104d1701e
- url: https://developers.telnyx.com/docs/messaging/messages/configurable-spend-limits/index
  content_hash: 3debaf7e27ff822d9bbebe435006ae4d2d6d8b93ce63335ec32a07d69af3b79f
- url: https://developers.telnyx.com/docs/messaging/messages/configuration-and-usage/index
  content_hash: 1689fb1fb284ac9037440148c10c18cf7db9961ed4a23dc6b836eadbc54eb215
- url: https://developers.telnyx.com/docs/messaging/messages/error-codes/index
  content_hash: e1967e40b4a047d11b5125f1a52bc6d4e705bb3c9091fea33b0be3327dce7b6e
- url: https://developers.telnyx.com/docs/messaging/messages/geomatch
  content_hash: 482afc03676e3bc869ddc8ddcdc2e664b63ccf582eee0d99dc25181db71831b7
- url: https://developers.telnyx.com/docs/messaging/messages/group-messaging
  content_hash: 39a6ee872f771c4a346c0ea1af391c578a9a69489623cf565ace914e877ab528
- url: https://developers.telnyx.com/docs/messaging/messages/hosted-sms/index
  content_hash: 183a7b2c87a6b2c0609b46d90d10746ff0ec211ef8ba7a7b4d481130f51b73ba
- url: https://developers.telnyx.com/docs/messaging/messages/hosted-sms/internal-transfer
  content_hash: 178148332abbc910363f6baca179c2f8701f9fae87ddda430a5727b8c5bddc83
updated_at: 2026-06-11T10:36:31Z
---

# Telnyx Messaging

*Part 4 of 4 — see also: [Part 1](telnyx-messaging--part-1.md), [Part 2](telnyx-messaging--part-2.md), [Part 3](telnyx-messaging--part-3.md)*

Telnyx Messaging provides a comprehensive API for sending and receiving SMS and MMS messages, with features including messaging profiles, alphanumeric sender IDs, geomatching, group messaging, two-factor authentication, appointment reminders, advanced opt-in/out handling, configurable spend limits, hosted SMS, and detailed error handling.

## Error Codes

Errors fall into three categories: **API request errors** (returned immediately), **delivery errors** (reported via webhooks), and **configuration errors** (number/profile issues).

### Delivery Errors (40xxx)

**Carrier rejections:**

| Code | Error | Action |
|---|---|---|
| `40001` | Not routable | Verify recipient can receive SMS/MMS |
| `40002` | Blocked as spam (temporary) | Reduce sending rate; review content |
| `40003` | Blocked as spam (permanent) | Use a different number; contact support |
| `40004` | Rejected by destination | Retry after delay |
| `40005` | Message expired | Increase validity period |
| `40006` | Recipient unavailable | Retry with exponential backoff |
| `40008` | Undeliverable | Check number validity; try alternate route |
| `40009` | Invalid message body | Check for invalid characters or encoding |
| `40011` | Rate limit exceeded (upstream) | Reduce sending rate |
| `40012` | Invalid destination number | Verify E.164 format |
| `40013` | Invalid source number | Check number is active and messaging-enabled |
| `40014` | Expired in queue | Check throughput bottlenecks |
| `40015` | Internal spam filter | Review content; contact support if false positive |

**10DLC-specific errors:**

| Code | Error | Action |
|---|---|---|
| `40010` | Not 10DLC registered | Register for 10DLC |
| `40016` | T-Mobile sending limit | Reduce rate or improve brand vetting score |
| `40017` | AT&T spam rejection | Review content; avoid URL shorteners |
| `40018` | AT&T sending limit | Reduce rate or improve brand vetting score |
| `40019` | AT&T invalid tag data | Verify campaign and number assignment |
| `40020` | Artificial traffic inflation | Wait 24 hours; review for fraud patterns |

**Toll-free errors:**

| Code | Error | Action |
|---|---|---|
| `40329` | Toll-free not verified | Complete toll-free verification |
| `40330` | Toll-free not provisioned | Wait for provisioning; contact support |

### API Request Errors (403xx)

**Sender/recipient errors:**

| Code | Error | Action |
|---|---|---|
| `40300` | Blocked (STOP) | Do not retry; wait for opt-back-in |
| `40301` | Unsupported message type | Check number type capabilities |
| `40305` | Invalid 'from' address | Assign number to messaging profile |
| `40306` | Alpha sender not configured | Configure on messaging profile |
| `40307` | Alpha sender mismatch | Use exact configured alpha sender |
| `40308` | Invalid 'from' for MMS | Use MMS-capable number |
| `40309` | Invalid destination region | Add region to profile whitelist |
| `40310` | Invalid 'to' address | Verify E.164 format |
| `40325` | Invalid alpha sender ID | Use 1–11 alphanumeric characters |

**Content errors:**

| Code | Error | Action |
|---|---|---|
| `40302` | Message too large | Shorten message or send as MMS |
| `40304` | Invalid content combination | Use `text` for SMS; `media_urls` for MMS |
| `40316` | No content | Include `text` and/or `media_urls` |
| `40317` | Invalid MMS content | Reduce to ≤10 URLs and ≤1 MB total |
| `40322` | Blocked content | Remove flagged content |

**Profile/configuration errors:**

| Code | Error | Action |
|---|---|---|
| `40311` | Invalid profile secret | Check `X-Profile-Secret` header |
| `40312` | Profile disabled | Re-enable in Mission Control |
| `40314` | Messaging disabled | Contact support |
| `40315` | Unhealthy sender | Check number success/spam rates |
| `40318` | Queue full | Back off and retry after delay |
| `40331` | Missing whitelist | Add destination regions to profile |
| `40333` | Spend limit reached | Increase limit or wait for reset |

### Number Provisioning Errors (401xx)

| Code | Error | Action |
|---|---|---|
| `40100` | Not messaging enabled | Enable messaging in Mission Control |
| `40150` | Not in voice registry | Contact support |
| `40151` | Enablement pending elsewhere | Wait for transfer to complete |
| `40155` | LOA required | Submit LOA through support |

### Retry Guidance

Most delivery errors require you to **change something before retrying** — blindly retrying will not resolve the issue.

| Category | Codes | Action |
|---|---|---|
| **Auto-retriable** | `40006`, `40008` | Carrier-side issue — retry with exponential backoff |
| **Retriable after intervention** | `40002`, `40005`, `40011`, `40014`, `40016`, `40017`, `40018`, `40318` | Fix rate/content/throughput first, then retry |
| **Temporary hold** | `40020`, `40320` | Wait (24 hours for `40020`; for provisioning for `40320`) |
| **Permanent** | `40001`, `40003`, `40010`, `40300`, `40314`, `40322` | Fix root cause before attempting again |
| **Action required** | `40010`, `40015`, `40019`, `40315`, `40329`, `40333` | Resolve configuration/compliance issue, then send again |
