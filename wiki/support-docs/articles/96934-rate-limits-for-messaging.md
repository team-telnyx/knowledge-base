---
title: "Rate Limits for Messaging"
summary: "​Important: Your account-specific messaging rate limits may differ from the default limits shown below. You can check your current limits in the Messagingsection of your Telnyx Portal."
sources:
- url: "https://support.telnyx.com/en/articles/96934-rate-limits-for-messaging"
updated_at: 2026-09-15T00:00:00Z
tags: [support-docs]
source_path: "support-docs/96934-rate-limits-for-messaging.md"
generated_by: incremental-support-docs-wiki
---
<!-- generated_from=support-docs/96934-rate-limits-for-messaging.md -->

# Rate Limits for Messaging

​**Important:** Your account-specific messaging rate limits may differ from the default limits shown below. You can check your current limits in the **[Messaging](https://portal.telnyx.com/#/programmable-messaging/rate-limits)**section of your Telnyx Portal.

|  |  |  |  |
| --- | --- | --- | --- |
| **Sender type** | **Default rate limit** | **Scope** | **Notes** |
| US long code, unregistered | 2 messages/min | Per long code number | For faster A2P throughput, [Register for 10DLC](https://support.telnyx.com/en/articles/6325731-register-for-10dlc-messaging) |
| Toll-free number | 1,200 messages/min | Per number | Throughput may depend on verification status |
| Alphanumeric sender ID | 60,000 messages/min | Per sender ID | — |
| Short code | 60,000 messages/min | Per number | — |

## What happens if you exceed your rate limit?

If you create messages faster than your allowed rate, Telnyx will queue the messages and send them at the allowed rate.
​

Queued messages that have not yet been sent will not appear in MDR reports.
​

Telnyx queues up to **4 hours’ worth of messages**. Messages that exceed this queue capacity will be dropped and will not be sent.

## Example

If you send messages from an unregistered US long code:

|  |  |
| --- | --- |
| Item | Value |
| Rate limit | 2 messages per minute |
| Queue window | 4 hours |
| Maximum queued messages | 480 messages |

**Calculation:** **`2 messages/minute × 60 minutes × 4 hours = 480 messages`**

Any messages beyond this queue capacity will be dropped and will not be sent.
​

**Need a higher limit?**

Contact **sales@telnyx.com** to discuss increasing your messaging rate limit.

Related resources
- [Long Code Deliverability Best Practices](https://support.telnyx.com/en/articles/1130617-sms-long-code-deliverability-best-practices)
- [Developer documentation - Messaging Rate Limiting](https://developers.telnyx.com/docs/messaging/messages/rate-limiting)

---

Related Articles

- [Short Message Peer-to-Peer Set-up Guide](https://support.telnyx.com/en/articles/1667062-short-message-peer-to-peer-set-up-guide)
- [Setting Up a Messaging Profile](https://support.telnyx.com/en/articles/3562059-setting-up-a-messaging-profile)
- [10DLC: Trust Scores & Use Cases](https://support.telnyx.com/en/articles/6325747-10dlc-trust-scores-use-cases)
- [Telnyx 10DLC Compliance Directory](https://support.telnyx.com/en/articles/6417677-telnyx-10dlc-compliance-directory)
- [Telnyx Messaging Error Codes](https://support.telnyx.com/en/articles/6505121-telnyx-messaging-error-codes)
