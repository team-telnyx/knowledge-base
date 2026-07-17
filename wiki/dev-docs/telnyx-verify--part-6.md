---
title: Telnyx Verify
summary: The Telnyx Verify API enables robust two-factor authentication and phone-number
  verification using carrier-grade voice and messaging. This page consolidates the
  Verify quickstart, custom templates, DTMF confirmation, webhooks, security best
  practices, and rate-limiting/fraud-prevention guidance into a single reference covering
  SMS, call, flashcall, and DTMF confirm verification methods, profile configuration,
  code verification, and production hardening.
sources:
- url: https://developers.telnyx.com/docs/identity/number-lookup/quickstart/index
- url: https://developers.telnyx.com/docs/identity/verify/custom-templates
- url: https://developers.telnyx.com/docs/identity/verify/dtmf-confirm
- url: https://developers.telnyx.com/docs/identity/verify/index
- url: https://developers.telnyx.com/docs/identity/verify/quickstart/index
- url: https://developers.telnyx.com/docs/identity/verify/rate-limiting-fraud-prevention
- url: https://developers.telnyx.com/docs/identity/verify/receiving-webhooks
- url: https://developers.telnyx.com/docs/identity/verify/security-best-practices
updated_at: 2026-07-17T09:13:37Z
---

# Telnyx Verify

*Part 6 of 6 — see also: [Part 1](telnyx-verify--part-1.md), [Part 2](telnyx-verify--part-2.md), [Part 3](telnyx-verify--part-3.md), [Part 4](telnyx-verify--part-4.md), [Part 5](telnyx-verify--part-5.md)*

The Telnyx Verify API enables robust two-factor authentication and phone-number verification using carrier-grade voice and messaging. This page consolidates the Verify quickstart, custom templates, DTMF confirmation, webhooks, security best practices, and rate-limiting/fraud-prevention guidance into a single reference covering SMS, call, flashcall, and DTMF confirm verification methods, profile configuration, code verification, and production hardening.

## Rate limiting and fraud prevention

This section goes deeper on the operational side of protecting your Telnyx Verify integration — server-side rate limiting architectures, geo-fencing, anomaly detection, cost controls, and incident response.

### Architecture overview

A robust fraud prevention system layers multiple defenses:

```
User Request → CAPTCHA → IP Rate Limit → Phone Rate Limit → Geo-fence → Anomaly Check → Telnyx Verify API
```

Each layer catches different attack patterns. No single defense is sufficient on its own.

### Server-side rate limiting with Redis

Production rate limiting requires a distributed store. A sliding-window rate limiter using Redis sorted sets is a common pattern. A typical multi-layer implementation applies:

- IP rate limit (10/hour)
- Phone rate limit (3/10min)
- User rate limit (5/hour)

### Geo-fencing

Restrict verifications to countries where your service operates. This is the single most effective defense against SMS pumping.

#### Configure on Verify profile

```
curl -X PATCH "https://api.telnyx.com/v2/verify_profiles/YOUR_PROFILE_ID" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "sms": {
      "whitelisted_destinations": ["US", "CA", "GB", "AU"]
    }
  }'
```

#### Application-level geo-validation

Add server-side validation before calling the API as a defense-in-depth measure, using a library like `libphonenumber-js` (Node) or `phonenumbers` (Python) to parse the number and check its country code against an allowlist.

#### High-risk country codes

These country codes are frequently targeted for SMS pumping and toll fraud. Block or add extra scrutiny:

| Code | Country | Risk |
| --- | --- | --- |
| +232 | Sierra Leone | SMS pumping |
| +225 | Côte d'Ivoire | SMS pumping |
| +233 | Ghana | SMS pumping |
| +234 | Nigeria | Mixed (legitimate + fraud) |
| +260 | Zambia | SMS pumping |
| +256 | Uganda | SMS pumping |
| +880 | Bangladesh | Toll fraud |
| +855 | Cambodia | Toll fraud |
| +856 | Laos | Toll fraud |
| +960 | Maldives | Toll fraud |
| +592 | Guyana | Toll fraud |

These are statistical patterns, not blanket rules. If you serve users in these countries, implement stronger rate limiting rather than blocking.

### Anomaly detection

Build automated detection for suspicious patterns beyond simple rate limits.

#### Conversion rate monitoring

A healthy verification flow has a 60-80% conversion rate (codes sent vs. codes verified). A rate below 20% may indicate an attack. Track sent and verified counts per hour in Redis and alert when the rate drops below the threshold.

#### Sequential number detection

SMS pumping often uses sequential phone numbers. Detect and block this pattern by sorting recent numbers and checking for runs of consecutive values.

### Cost controls

#### Set spend alerts

Monitor your Telnyx account spending and set alerts at the account level through the [Telnyx Portal billing settings](https://portal.telnyx.com/#/app/billing).

#### Implement circuit breakers

Automatically disable verifications when anomalies are detected. A typical pattern tracks total verifications per hour and trips a circuit breaker when a threshold (e.g., 500/hour) is exceeded.

### Incident response

When you detect a fraud attack in progress:

1. **Immediately: Enable circuit breaker** — Stop all verification sends to limit financial damage.
2. **Investigate: Check patterns** — Look at the destination countries, IP addresses, and phone number patterns in your logs.
3. **Block: Update allowlists** — Remove affected countries from your Verify profile's `whitelisted_destinations`.
4. **Recover: Tighten limits** — Reduce rate limits, add CAPTCHA if not present, and re-enable verifications gradually.
5. **Contact Telnyx Support** — Report the incident to [Telnyx Support](https://support.telnyx.com) for investigation and potential charge reversal.

### Configuration reference

Summary of all Verify profile settings relevant to fraud prevention:

| Setting | Endpoint | Purpose |
| --- | --- | --- |
| `whitelisted_destinations` | `PATCH /v2/verify_profiles/{id}` | Restrict SMS to specific countries |
| `code_length` | `PATCH /v2/verify_profiles/{id}` | Set verification code length (4-10) |
| `default_timeout_secs` | `PATCH /v2/verify_profiles/{id}` | Expiration time for codes |

Example production-hardened Verify profile:

```
curl -X PATCH "https://api.telnyx.com/v2/verify_profiles/YOUR_PROFILE_ID" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "sms": {
      "whitelisted_destinations": ["US", "CA"],
      "default_timeout_secs": 300,
      "code_length": 6
    },
    "call": {
      "default_timeout_secs": 300
    }
  }'
```

## Troubleshooting

### DTMF confirmation

- **Call reaches voicemail** — Verification times out with status `expired`. Implement a retry with delay, or fall back to SMS.
- **Wrong digit pressed** — Up to 3 attempts per call. After 3 failures, status is `invalid`. Trigger a new verification to retry.
- **Stuck in pending** — Call was not answered and no webhook received. Verify the webhook URL is configured and reachable. Poll the status endpoint as fallback.
- **Custom TTS prompt** — The prompt is fixed to the standard verification message. Voice and language are determined by the Verify Profile's `language` setting. Custom prompt text is not yet supported.
- **Rate limits** — Standard Verify API rate limits apply. Avoid triggering multiple concurrent verifications for the same phone number — the previous call must complete or time out first.

## Next steps

- [Custom templates for Telnyx Verify](custom-templates-for-telnyx-verify.md) — Branded verification messages for SMS and call types.
- [DTMF Confirmation Verification](dtmf-confirmation-verification.md) — Single-keypress confirmation for landlines and caller ID verification.
- [Receiving Webhooks for Telnyx Verify](receiving-webhooks-for-telnyx-verify.md) — Real-time verification status updates.
- [Verify Security Best Practices](verify-security-best-practices.md) — Foundational security concepts for Verify.
- [Rate Limiting and Fraud Prevention for Verify](rate-limiting-and-fraud-prevention-for-verify.md) — Advanced fraud prevention strategies.
- [Verify API reference](https://developers.telnyx.com/api-reference/verify/create-a-verify-profile) — Full API specification.
