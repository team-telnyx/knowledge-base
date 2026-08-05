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

*Part 2 of 4 — see also: [Part 1](telnyx-messaging-configuration-errors-and-advanced-features--part-1.md), [Part 3](telnyx-messaging-configuration-errors-and-advanced-features--part-3.md), [Part 4](telnyx-messaging-configuration-errors-and-advanced-features--part-4.md)*

This page consolidates Telnyx messaging configuration guidance, including messaging profile setup, configurable spend limits, error code handling, the Vercel Chat SDK adapter, and Geomatch for area-code-based sender selection. It covers prerequisites, environment variables, webhook setup, capability matrices, and best practices for production SMS/MMS workloads.

## Messaging Error Code Reference

Complete reference for errors returned by the Telnyx Messaging API. Errors fall into three categories: **API request errors** (returned immediately), **delivery errors** (reported via webhooks), and **configuration errors** (number/profile issues).

### Delivery Errors (40xxx)

These errors occur after the message is accepted by the API but fails during delivery. They appear in message detail records and `message.finalized` webhooks.

#### Carrier Rejections

| Code | Error | Cause | Action |
| --- | --- | --- | --- |
| `40001` | Not routable | Destination is a landline or non-routable number | Verify the recipient can receive SMS/MMS |
| `40002` | Blocked as spam (temporary) | Carrier spam filter triggered | Reduce sending rate; review message content for spam patterns |
| `40003` | Blocked as spam (permanent) | Sending number permanently blocked by carrier | Use a different sending number; contact support for appeal |
| `40004` | Rejected by destination | Recipient carrier rejecting for unknown reason | Retry after delay; contact support if persistent |
| `40005` | Message expired | Message TTL expired before delivery | Increase validity period or check carrier delays |
| `40006` | Recipient unavailable | Recipient's carrier server is down | Retry with exponential backoff |
| `40008` | Undeliverable | Carrier did not accept the message | Check number validity; try alternate route |
| `40009` | Invalid message body | Message content rejected | Check for invalid characters or encoding issues |
| `40011` | Rate limit exceeded (upstream) | Exceeded carrier throughput limit | Reduce sending rate |
| `40012` | Invalid destination number | Carrier rejected the destination number | Verify E.164 format and number validity |
| `40013` | Invalid source number | Carrier rejected the sending number | Check that your number is active and messaging-enabled |
| `40014` | Expired in queue | Message sat in queue past validity period | Check for throughput bottlenecks; increase sending capacity |
| `40015` | Internal spam filter | Telnyx internal spam filter triggered | Review message content; contact support if false positive |

#### 10DLC-Specific Errors

| Code | Error | Cause | Action |
| --- | --- | --- | --- |
| `40010` | Not 10DLC registered | Sending number lacks 10DLC campaign registration | Register for 10DLC |
| `40016` | T-Mobile sending limit | Exceeded T-Mobile throughput for this campaign | Reduce rate or improve brand vetting score for higher limits |
| `40017` | AT&T spam rejection | AT&T flagged message as spam | Review content; avoid URL shorteners and spam-like patterns |
| `40018` | AT&T sending limit | Exceeded AT&T throughput for this campaign | Reduce rate or improve brand vetting score |
| `40019` | AT&T invalid tag data | Incorrect 10DLC tagging information | Verify campaign and number assignment |
| `40020` | Artificial traffic inflation | 2FA traffic blocked for 24 hours | Wait 24 hours; review for fraud patterns on your numbers |

#### Toll-Free Errors

| Code | Error | Cause | Action |
| --- | --- | --- | --- |
| `40329` | Toll-free not verified | Number hasn't passed toll-free verification | Complete toll-free verification |
| `40330` | Toll-free not provisioned | Number not fully provisioned for messaging | Wait for provisioning to complete; contact support |

### API Request Errors (403xx)

These errors are returned immediately in the API response when the message request is invalid.

#### Sender/Recipient Errors

| Code | Error | Cause | Action |
| --- | --- | --- | --- |
| `40300` | Blocked (STOP) | Recipient sent STOP — opt-out in effect | Do not retry; wait for recipient to opt back in |
| `40301` | Unsupported message type | Cannot send between these number types | Check source and destination number capabilities |
| `40305` | Invalid 'from' address | Sending number not associated with messaging profile | Assign the number to your messaging profile |
| `40306` | Alpha sender not configured | Alphanumeric sender ID not set on profile | Configure alpha sender on your messaging profile |
| `40307` | Alpha sender mismatch | From address doesn't match configured alpha sender | Use the exact alpha sender configured on the profile |
| `40308` | Invalid 'from' for MMS | MMS requires US long code or short code | Use an MMS-capable number |
| `40309` | Invalid destination region | Destination country not in profile whitelist | Add the destination region to your messaging profile |
| `40310` | Invalid 'to' address | Destination number is invalid | Verify E.164 format: `+[country code][number]` |
| `40319` | Incompatible message type | Source and destination types incompatible | Check number type compatibility |
| `40320` | Temporarily unusable sender | Sending number in pending/transitional state | Wait for number provisioning to complete |
| `40321` | No usable numbers in pool | Number pool empty or all numbers unhealthy | Add numbers to pool or check number health |
| `40325` | Invalid alpha sender ID | Alphanumeric sender ID format is invalid | Use 1–11 alphanumeric characters |

#### Content Errors

| Code | Error | Cause | Action |
| --- | --- | --- | --- |
| `40302` | Message too large | SMS exceeds maximum segment count | Shorten message or send as MMS |
| `40304` | Invalid content combination | Mixed SMS/MMS content parameters | Use `text` for SMS; `media_urls` (with optional `text`) for MMS |
| `40316` | No content | Message has no text or media | Include `text` and/or `media_urls` |
| `40317` | Invalid MMS content | Too many media items or total size > 1 MB | Reduce to ≤10 URLs and ≤1 MB total |
| `40322` | Blocked content | Message contains prohibited content | Remove flagged content |
| `40328` | SMS too large (warning) | Message splits into too many parts | Consider sending as MMS instead |

#### Profile/Configuration Errors

| Code | Error | Cause | Action |
| --- | --- | --- | --- |
| `40311` | Invalid profile secret | `X-Profile-Secret` header is wrong | Check your messaging profile secret |
| `40312` | Profile disabled | Messaging profile is disabled | Re-enable in Mission Control |
| `40313` | Missing profile secret | `X-Profile-Secret` header required but not sent | Include the header in your request |
| `40314` | Messaging disabled | Messaging disabled on your account | Contact Telnyx support |
| `40315` | Unhealthy sender | Sending number has poor health metrics | Check number success/spam rates; consider replacing |
| `40318` | Queue full | Internal message queue at capacity | Back off and retry after a delay |
| `40323` | Activation failed | Could not enable messaging on number | Contact support |
| `40331` | Missing whitelist | No whitelisted destinations on profile | Add destination regions to your messaging profile |
| `40333` | Spend limit reached | Messaging profile cost limit hit | Increase spend limit or wait for reset |

### Number Provisioning Errors (401xx)

| Code | Error | Cause | Action |
| --- | --- | --- | --- |
| `40100` | Not messaging enabled | Number not configured for messaging | Enable messaging in Mission Control |
| `40150` | Not in voice registry | Toll-free number missing from registry | Contact support |
| `40151` | Enablement pending elsewhere | Another provider is enabling messaging | Wait for transfer to complete |
| `40155` | LOA required | Letter of Authorization needed | Submit LOA through support |

### Retriable vs Permanent Errors

Most delivery errors require you to **change something before retrying** — blindly retrying the same message with the same configuration will not resolve the issue and may result in further blocking.

| Category | Codes | Action |
| --- | --- | --- |
| **Auto-retriable** (genuinely temporary) | `40006`, `40008` | Carrier-side issue — retry with exponential backoff (1s, 2s, 4s, 8s…). `40006`: recipient carrier is down. `40008`: general undeliverable, may resolve on retry. |
| **Retriable after intervention** (fix first) | `40002`, `40005`, `40011`, `40014`, `40016`, `40017`, `40018`, `40318` | These errors indicate a problem with your sending rate, content, or throughput. Reduce sending rate, review message content for spam patterns, or resolve queue pressure **before** retrying. Automatic retry without changes will likely fail again. |
| **Temporary hold** | `40020`, `40320` | `40020`: 2FA traffic blocked for 24 hours — wait, do not retry. `40320`: sender in transitional state — wait for provisioning to complete. |
| **Permanent** (do not retry) | `40001`, `40003`, `40010`, `40300`, `40314`, `40322` | Fix root cause before attempting again. These will not resolve on their own. |
| **Action required** (config/compliance) | `40010`, `40015`, `40019`, `40315`, `40329`, `40333` | Resolve the underlying configuration or compliance issue, then send again. |
