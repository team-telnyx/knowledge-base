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

*Part 3 of 5 — see also: [Part 1](verify-security-rate-limiting-and-webhooks--part-1.md), [Part 2](verify-security-rate-limiting-and-webhooks--part-2.md), [Part 4](verify-security-rate-limiting-and-webhooks--part-4.md), [Part 5](verify-security-rate-limiting-and-webhooks--part-5.md)*

Operational guidance for protecting Telnyx Verify integrations: layered rate limiting, geo-fencing, anomaly detection, cost controls, incident response, code and channel security, and webhook handling for delivery and verification status updates.

## Geo-fencing

Restrict verifications to countries where the service operates. This is the single most effective defense against SMS pumping.

### Configure on Verify profile

```bash
curl -X PATCH "https://api.telnyx.com/v2/verify_profiles/YOUR_PROFILE_ID" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "sms": {
      "whitelisted_destinations": ["US", "CA", "GB", "AU"]
    }
  }'
```

### Application-level geo-validation

Add server-side validation before calling the API as a defense-in-depth measure:

```javascript
import { parsePhoneNumber } from 'libphonenumber-js';

const ALLOWED_COUNTRIES = new Set(['US', 'CA', 'GB', 'AU']);

function validatePhoneCountry(phoneNumber) {
  const parsed = parsePhoneNumber(phoneNumber);
  if (!parsed || !parsed.country) {
    throw new Error('Invalid phone number');
  }
  if (!ALLOWED_COUNTRIES.has(parsed.country)) {
    throw new Error('Verification not available in this region');
  }
  return parsed.country;
}
```

```python
import phonenumbers

ALLOWED_COUNTRIES = {"US", "CA", "GB", "AU"}

def validate_phone_country(phone_number: str) -> str:
    parsed = phonenumbers.parse(phone_number)
    country = phonenumbers.region_code_for_number(parsed)
    if country not in ALLOWED_COUNTRIES:
        raise ValueError("Verification not available in this region")
    return country
```

### High-risk country codes

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

## SMS pumping prevention

SMS pumping is the most costly fraud vector for verification flows. Attackers abuse the send endpoint to generate SMS revenue on number ranges they control.

### Detection signals

Watch for these patterns:

- **Sequential numbers** — Verification requests for `+1234500001`, `+1234500002`, `+1234500003`…
- **Unusual country codes** — Spike in verifications to countries you don't serve
- **High failure rate** — Many verifications triggered but never completed
- **Burst traffic** — Sudden spike in verification requests from a single source

### Defenses

1. **Restrict destination countries** — Configure `whitelisted_destinations` on your Verify profile to only allow countries where your users are.
2. **Require authentication before verification** — Don't expose the verification endpoint to unauthenticated users. Require at least a session or account to trigger a verification.
3. **Add CAPTCHA** — Place a CAPTCHA (reCAPTCHA, hCaptcha, Turnstile) before the phone number input to block automated submissions.
4. **Monitor and alert** — Set up alerts for unusual verification volume:

```javascript
// Track verification requests per minute
const verifyCount = new Map();

function trackVerification() {
  const minute = Math.floor(Date.now() / 60000);
  verifyCount.set(minute, (verifyCount.get(minute) || 0) + 1);

  if (verifyCount.get(minute) > 100) {
    // Alert: possible SMS pumping attack
    alertOps('Verification spike detected: ' + verifyCount.get(minute) + '/min');
  }
}
```

## Anomaly detection

Build automated detection for suspicious patterns beyond simple rate limits.

### Conversion rate monitoring

A healthy verification flow has a 60-80% conversion rate (codes sent vs. codes verified). A rate below 20% may indicate an attack.

```javascript
class ConversionMonitor {
  constructor(redis, alertCallback) {
    this.redis = redis;
    this.alertCallback = alertCallback;
  }

  async trackSent(phoneNumber) {
    const hour = Math.floor(Date.now() / 3600000);
    await this.redis.incr(`verify:sent:${hour}`);
    await this.redis.expire(`verify:sent:${hour}`, 7200);
  }

  async trackVerified(phoneNumber) {
    const hour = Math.floor(Date.now() / 3600000);
    await this.redis.incr(`verify:verified:${hour}`);
    await this.redis.expire(`verify:verified:${hour}`, 7200);
  }

  async checkConversionRate() {
    const hour = Math.floor(Date.now() / 3600000);
    const sent = parseInt(await this.redis.get(`verify:sent:${hour}`)) || 0;
    const verified = parseInt(await this.redis.get(`verify:verified:${hour}`)) || 0;

    if (sent < 10) return; // Too few samples

    const rate = verified / sent;
    if (rate < 0.2) {
      this.alertCallback({
        message: `Low verification conversion rate: ${(rate * 100).toFixed(1)}%`,
        sent,
        verified,
        hour: new Date(hour * 3600000).toISOString(),
      });
    }
  }
}
```

```python
import time
import redis as redis_lib

class ConversionMonitor:
    def __init__(self, redis_client, alert_callback):
        self.redis = redis_client
        self.alert = alert_callback

    def _hour_key(self):
        return int(time.time() // 3600)

    def track_sent(self):
        hour = self._hour_key()
        self.redis.incr(f"verify:sent:{hour}")
        self.redis.expire(f"verify:sent:{hour}", 7200)

    def track_verified(self):
        hour = self._hour_key()
        self.redis.incr(f"verify:verified:{hour}")
        self.redis.expire(f"verify:verified:{hour}", 7200)

    def check_conversion_rate(self):
        hour = self._hour_key()
        sent = int(self.redis.get(f"verify:sent:{hour}") or 0)
        verified = int(self.redis.get(f"verify:verified:{hour}") or 0)

        if sent < 10:
            return

        rate = verified / sent
        if rate < 0.2:
            self.alert({
                "message": f"Low verification conversion rate: {rate:.1%}",
                "sent": sent,
                "verified": verified,
            })
```

### Sequential number detection

SMS pumping often uses sequential phone numbers. Detect and block this pattern:

```javascript
function detectSequentialNumbers(recentNumbers, threshold = 5) {
  if (recentNumbers.length < threshold) return false;

  // Sort by numeric value
  const sorted = recentNumbers
    .map(n => BigInt(n.replace(/\D/g, '')))
    .sort((a, b) => (a < b ? -1 : 1));

  // Check for sequences
  let sequential = 1;
  for (let i = 1; i < sorted.length; i++) {
    if (sorted[i] - sorted[i - 1] <= 3n) {
      sequential++;
      if (sequential >= threshold) return true;
    } else {
      sequential = 1;
    }
  }

  return false;
}
```
