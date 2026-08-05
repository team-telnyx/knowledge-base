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

*Part 1 of 5 — see also: [Part 2](verify-security-rate-limiting-and-webhooks--part-2.md), [Part 3](verify-security-rate-limiting-and-webhooks--part-3.md), [Part 4](verify-security-rate-limiting-and-webhooks--part-4.md), [Part 5](verify-security-rate-limiting-and-webhooks--part-5.md)*

Operational guidance for protecting Telnyx Verify integrations: layered rate limiting, geo-fencing, anomaly detection, cost controls, incident response, code and channel security, and webhook handling for delivery and verification status updates.

## Threat overview

Verification flows are a high-value target for attackers. SMS pumping, toll fraud, brute-force code guessing, and social engineering can cost money and compromise user accounts.

| Threat | Description | Impact |
| --- | --- | --- |
| SMS pumping | Attackers trigger thousands of SMS verifications to premium-rate numbers | Inflated costs, sometimes $10K+ per incident |
| Toll fraud (IRSF) | Exploiting call verification to generate revenue on premium international numbers | Per-minute charges on fraudulent calls |
| Brute-force attacks | Systematically guessing verification codes | Account takeover |
| Code interception | SIM swapping, SS7 attacks, malware intercepting SMS | Account compromise |
| Enumeration | Using verification endpoints to check if phone numbers exist in your system | Privacy leak, targeted attacks |

## Architecture overview

A robust fraud prevention system layers multiple defenses:

```
User Request → CAPTCHA → IP Rate Limit → Phone Rate Limit → Geo-fence → Anomaly Check → Telnyx Verify API
```

Each layer catches different attack patterns. No single defense is sufficient on its own.

## Rate limiting

Rate limiting is the first line of defense against abuse. Apply limits at multiple layers.

### Per-phone-number limits

Restrict how many verification attempts a single phone number can trigger within a time window.

```javascript
import { RateLimiterMemory } from 'rate-limiter-flexible';

// Max 3 verification requests per phone number per 10 minutes
const phoneLimiter = new RateLimiterMemory({
  points: 3,
  duration: 600, // 10 minutes
});

async function requestVerification(phoneNumber) {
  try {
    await phoneLimiter.consume(phoneNumber);
    // Proceed with Telnyx Verify API call
  } catch (rejRes) {
    const retryAfter = Math.ceil(rejRes.msBeforeNext / 1000);
    throw new Error(`Too many attempts. Try again in ${retryAfter} seconds.`);
  }
}
```

```python
from datetime import datetime, timedelta

# Simple in-memory rate limiter (use Redis in production)
verification_attempts = {}

def check_rate_limit(phone_number, max_attempts=3, window_minutes=10):
    now = datetime.utcnow()
    cutoff = now - timedelta(minutes=window_minutes)

    # Clean old attempts
    attempts = verification_attempts.get(phone_number, [])
    attempts = [t for t in attempts if t > cutoff]

    if len(attempts) >= max_attempts:
        raise Exception(f"Too many attempts. Try again later.")

    attempts.append(now)
    verification_attempts[phone_number] = attempts
    return True
```

```go
package main

import (
	"fmt"
	"sync"
	"time"
)

type RateLimiter struct {
	mu       sync.Mutex
	attempts map[string][]time.Time
	max      int
	window   time.Duration
}

func NewRateLimiter(max int, window time.Duration) *RateLimiter {
	return &RateLimiter{
		attempts: make(map[string][]time.Time),
		max:      max,
		window:   window,
	}
}

func (rl *RateLimiter) Allow(key string) error {
	rl.mu.Lock()
	defer rl.mu.Unlock()

	cutoff := time.Now().Add(-rl.window)
	var valid []time.Time
	for _, t := range rl.attempts[key] {
		if t.After(cutoff) {
			valid = append(valid, t)
		}
	}

	if len(valid) >= rl.max {
		return fmt.Errorf("too many attempts, try again later")
	}

	rl.attempts[key] = append(valid, time.Now())
	return nil
}
```

### Per-IP address limits

Prevent a single IP from triggering verifications for many different numbers (a hallmark of SMS pumping):

```javascript
// Max 10 verification requests per IP per hour
const ipLimiter = new RateLimiterMemory({
  points: 10,
  duration: 3600,
});

app.post('/verify/request', async (req, res) => {
  const clientIp = req.ip;
  try {
    await ipLimiter.consume(clientIp);
    await phoneLimiter.consume(req.body.phone_number);
    // Proceed with verification
  } catch {
    res.status(429).json({ error: 'Too many requests' });
  }
});
```

```python
from flask import Flask, request, jsonify
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

app = Flask(__name__)
limiter = Limiter(app=app, key_func=get_remote_address)

@app.route("/verify/request", methods=["POST"])
@limiter.limit("10 per hour")
def request_verification():
    phone_number = request.json["phone_number"]
    check_rate_limit(phone_number)
    # Proceed with Telnyx Verify API call
    return jsonify(success=True)
```

### Recommended limits

| Scope | Limit | Window |
| --- | --- | --- |
| Per phone number | 3 attempts | 10 minutes |
| Per phone number | 5 attempts | 1 hour |
| Per IP address | 10 attempts | 1 hour |
| Per account/session | 5 attempts | 1 hour |
| Global (all numbers) | Monitor for spikes | Continuous |
