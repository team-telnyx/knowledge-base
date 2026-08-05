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

*Part 8 of 8 — see also: [Part 1](10dlc-campaign-use-cases-and-event-notifications--part-1.md), [Part 2](10dlc-campaign-use-cases-and-event-notifications--part-2.md), [Part 3](10dlc-campaign-use-cases-and-event-notifications--part-3.md), [Part 4](10dlc-campaign-use-cases-and-event-notifications--part-4.md), [Part 5](10dlc-campaign-use-cases-and-event-notifications--part-5.md), [Part 6](10dlc-campaign-use-cases-and-event-notifications--part-6.md), [Part 7](10dlc-campaign-use-cases-and-event-notifications--part-7.md)*

Comprehensive guide to Telnyx 10DLC campaign use cases, sample messages, opt-in/opt-out requirements, and webhook event notifications for brands, campaigns, and phone numbers. Includes SDK examples, retry policies, and campaign appeal mechanisms.

## Webhook Delivery

### Retry Policy

If your webhook endpoint returns a non-2xx HTTP status code or times out, Telnyx will retry delivery. The `meta.attempt` field in the webhook payload indicates which delivery attempt this is (starting at 1).

- **Default retry attempts:** 5
- **Default retry interval:** 30 seconds between attempts

After 5 failed attempts, the webhook will be marked as failed and no further retries will be made.

### Best Practices

- **Return 2xx quickly**: Return a 200 response as soon as possible, then process the webhook asynchronously.
- **Handle duplicates**: Webhooks may be delivered more than once. Use the `id` field to deduplicate.
- **Use HTTPS**: Always use HTTPS endpoints to ensure webhook data is encrypted in transit.
- **Verify the source**: Consider implementing signature verification for added security.
- **Set up failover**: Configure a `webhookFailoverURL` to receive webhooks if your primary endpoint is unavailable.

### Testing Webhooks Locally

During development, you can use tunneling tools to expose your local server to the internet for webhook testing:

1. **ngrok**: Run `ngrok http 3000` to create a public URL that forwards to your local port 3000.
2. **Cloudflare Tunnel**: Use `cloudflared tunnel` for a similar tunneling solution.
3. **localtunnel**: Run `lt --port 3000` for a quick temporary URL.

Update your brand or campaign webhook URL to the tunnel URL, then monitor incoming webhooks as you trigger events in your 10DLC registration flow.

## Glossary

| Term | Definition |
| --- | --- |
| 10DLC | 10-Digit Long Code. Standard 10-digit phone numbers used for application-to-person (A2P) messaging. |
| CSP | Campaign Service Provider. A company authorized to submit and manage campaigns on behalf of brands with The Campaign Registry. |
| DCA | Direct Connect Aggregator. An entity that has a direct connection to mobile carriers for message delivery. |
| MNO | Mobile Network Operator. Wireless carriers such as T-Mobile, AT&T, and Verizon that deliver SMS/MMS messages to end users. |
| TCR | The Campaign Registry. The central registry that manages brand and campaign registration for 10DLC messaging in the United States. |

## Related Resources

- [10DLC Quickstart](10dlc-quickstart.md) — Get started with 10DLC brand and campaign registration.
- [10DLC Rate Limits](10dlc-rate-limits.md) — Understand throughput limits based on vetting scores.
- [Receive Webhooks](https://developers.telnyx.com/docs/messaging/messages/receive-message) — Set up a server to receive webhook notifications.
- [Message Detail Records](https://developers.telnyx.com/docs/messaging/messages/message-detail-records) — Track delivery status and troubleshoot issues.
- [10DLC Troubleshooting](10dlc-troubleshooting.md) — Fix registration and delivery issues.
