---
title: Verify Security, Rate Limiting, and Webhooks
summary: 'Operational guidance for protecting Telnyx Verify integrations: layered
  rate limiting, geo-fencing, anomaly detection, cost controls, incident response,
  code and channel security, and webhook handling for delivery and verification status
  updates.'
sources:
- url: https://developers.telnyx.com/docs/identity/verify/rate-limiting-fraud-prevention
- url: https://developers.telnyx.com/docs/identity/verify/receiving-webhooks
- url: https://developers.telnyx.com/docs/identity/verify/security-best-practices
updated_at: 2026-08-05T13:44:10Z
---

# Verify Security, Rate Limiting, and Webhooks

*Part 4 of 5 — see also: [Part 1](verify-security-rate-limiting-and-webhooks--part-1.md), [Part 2](verify-security-rate-limiting-and-webhooks--part-2.md), [Part 3](verify-security-rate-limiting-and-webhooks--part-3.md), [Part 5](verify-security-rate-limiting-and-webhooks--part-5.md)*

Operational guidance for protecting Telnyx Verify integrations: layered rate limiting, geo-fencing, anomaly detection, cost controls, incident response, code and channel security, and webhook handling for delivery and verification status updates.

## Code security

### Use appropriate code length

Longer codes are harder to brute-force but harder for users to enter. Balance security and usability:

| Code Length | Combinations | Brute-force time (3 attempts/min) | Recommendation |
| --- | --- | --- | --- |
| 4 digits | 10,000 | ~55 hours | Low security only |
| 5 digits | 100,000 | ~23 days | Default — good balance |
| 6 digits | 1,000,000 | ~231 days | High security applications |

Configure code length in your Verify profile:

```bash
curl -X PATCH "https://api.telnyx.com/v2/verify_profiles/YOUR_PROFILE_ID" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "sms": {
      "code_length": 6
    }
  }'
```

### Set appropriate timeouts

Short timeouts reduce the window for brute-force attacks:

```bash
curl -X PATCH "https://api.telnyx.com/v2/verify_profiles/YOUR_PROFILE_ID" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "sms": {
      "default_timeout_secs": 300
    },
    "call": {
      "default_timeout_secs": 300
    }
  }'
```

A 5-minute timeout (300 seconds) works well for most applications. Shorter timeouts (120s) add security but may frustrate users on slow networks.

### Limit verification attempts

Lock out after too many failed code entries to prevent brute-force:

```javascript
const failedAttempts = new Map();

async function verifyCode(phoneNumber, code) {
  const attempts = failedAttempts.get(phoneNumber) || 0;

  if (attempts >= 5) {
    throw new Error('Too many failed attempts. Request a new code.');
  }

  const response = await fetch(
    `https://api.telnyx.com/v2/verifications/by_phone_number/${phoneNumber}/actions/verify`,
    {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${process.env.TELNYX_API_KEY}`,
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ code, verify_profile_id: PROFILE_ID }),
    }
  );
  const result = await response.json();

  if (result.data.response_code === 'accepted') {
    failedAttempts.delete(phoneNumber);
    return true;
  }

  failedAttempts.set(phoneNumber, attempts + 1);
  return false;
}
```

```python
import requests
import os

failed_attempts = {}  # Use Redis in production

def verify_code(phone_number, code, profile_id):
    attempts = failed_attempts.get(phone_number, 0)

    if attempts >= 5:
        raise Exception("Too many failed attempts. Request a new code.")

    response = requests.post(
        f"https://api.telnyx.com/v2/verifications/by_phone_number/{phone_number}/actions/verify",
        headers={"Authorization": f"Bearer {os.environ['TELNYX_API_KEY']}"},
        json={"code": code, "verify_profile_id": profile_id},
    )
    result = response.json()

    if result["data"]["response_code"] == "accepted":
        failed_attempts.pop(phone_number, None)
        return True

    failed_attempts[phone_number] = attempts + 1
    return False
```

## Prevent number enumeration

Don't reveal whether a phone number exists in your system through verification responses.

**Vulnerable** — reveals whether the number is registered:

```json
{ "error": "No account found for this phone number" }
```

**Secure** — same response regardless:

```json
{ "message": "If this number is registered, you'll receive a verification code." }
```

Always return a consistent response and send the verification (or silently drop it) regardless of whether the number exists in your system.

## Channel fallback strategy

Use multiple verification channels to improve delivery and security:

1. **Primary: SMS** — Start with SMS verification for widest reach and fastest delivery.
2. **Fallback: Voice call** — If SMS isn't delivered within 30 seconds, offer a voice call option. This helps users on networks with delayed SMS delivery.
3. **Consider: Flashcall** — For supported markets, flashcall verification (where the phone number itself is the code) provides instant verification with no user input required.

Configure all three channels on your Verify profile:

```bash
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
    },
    "flashcall": {
      "default_timeout_secs": 300
    }
  }'
```

## Cost controls

### Set spend alerts

Monitor your Telnyx account spending and set alerts at the account level through the [Telnyx Portal billing settings](https://portal.telnyx.com/#/app/billing).

### Implement circuit breakers

Automatically disable verifications when anomalies are detected:

```javascript
class VerificationCircuitBreaker {
  constructor(redis, maxPerHour = 500) {
    this.redis = redis;
    this.maxPerHour = maxPerHour;
    this.tripped = false;
  }

  async canSend() {
    if (this.tripped) return false;

    const hour = Math.floor(Date.now() / 3600000);
    const count = parseInt(await this.redis.get(`verify:total:${hour}`)) || 0;

    if (count >= this.maxPerHour) {
      this.tripped = true;
      // Alert operations team
      console.error(`Circuit breaker tripped: ${count} verifications in current hour`);
      return false;
    }

    await this.redis.incr(`verify:total:${hour}`);
    await this.redis.expire(`verify:total:${hour}`, 7200);
    return true;
  }

  reset() {
    this.tripped = false;
  }
}
```

## Incident response

When you detect a fraud attack in progress:

1. **Immediately: Enable circuit breaker** — Stop all verification sends to limit financial damage.
2. **Investigate: Check patterns** — Look at the destination countries, IP addresses, and phone number patterns in your logs.
3. **Block: Update allowlists** — Remove affected countries from your Verify profile's `whitelisted_destinations`.
4. **Recover: Tighten limits** — Reduce rate limits, add CAPTCHA if not present, and re-enable verifications gradually.
5. **Contact Telnyx Support** — Report the incident to [Telnyx Support](https://support.telnyx.com) for investigation and potential charge reversal.

## Configuration reference

Summary of all Verify profile settings relevant to fraud prevention:

| Setting | Endpoint | Purpose |
| --- | --- | --- |
| `whitelisted_destinations` | `PATCH /v2/verify_profiles/{id}` | Restrict SMS to specific countries |
| `code_length` | `PATCH /v2/verify_profiles/{id}` | Set verification code length (4-10) |
| `default_timeout_secs` | `PATCH /v2/verify_profiles/{id}` | Expiration time for codes |

```bash
# Example: Production-hardened Verify profile
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
