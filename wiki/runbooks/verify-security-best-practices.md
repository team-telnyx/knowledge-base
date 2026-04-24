---
title: Verify Security Best Practices
summary: Protect your verification flows from fraud, abuse, and common attack vectors with these security best practices for Telnyx Verify.
sources:
  - url: https://developers.telnyx.com/docs/identity/verify/security-best-practices/index
    content_hash: bdc775e8f356ba01c48601ddb5ab034ea209c566bf00ade87c44b2a32fd89c6a
updated_at: 2026-04-10T00:00:00Z
---

# Verify Security Best Practices

Protect your verification flows from fraud, abuse, and common attack vectors with these security best practices for Telnyx Verify.

Verification flows are a high-value target for attackers. SMS pumping, toll fraud, brute-force code guessing, and social engineering can cost you money and compromise user accounts. This guide covers practical defenses you should implement alongside Telnyx Verify.

## Threat overview

| Threat                  | Description                                                                       | Impact                                        |
| ----------------------- | --------------------------------------------------------------------------------- | --------------------------------------------- |
| **SMS pumping**         | Attackers trigger thousands of SMS verifications to premium-rate numbers          | Inflated costs, sometimes \$10K+ per incident |
| **Toll fraud (IRSF)**   | Exploiting call verification to generate revenue on premium international numbers | Per-minute charges on fraudulent calls        |
| **Brute-force attacks** | Systematically guessing verification codes                                        | Account takeover                              |
| **Code interception**   | SIM swapping, SS7 attacks, malware intercepting SMS                               | Account compromise                            |
| **Enumeration**         | Using verification endpoints to check if phone numbers exist in your system       | Privacy leak, targeted attacks                |

## Rate limiting

Rate limiting is your first line of defense against abuse. Apply limits at multiple layers.

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

| Scope                | Limit              | Window     |
| -------------------- | ------------------ | ---------- |
| Per phone number     | 3 attempts         | 10 minutes |
| Per phone number     | 5 attempts         | 1 hour     |
| Per IP address       | 10 attempts        | 1 hour     |
| Per account/session  | 5 attempts         | 1 hour     |
| Global (all numbers) | Monitor for spikes | Continuous |

## SMS pumping prevention

SMS pumping is the most costly fraud vector for verification flows. Attackers abuse your send endpoint to generate SMS revenue on number ranges they control.

### Detection signals

Watch for these patterns:

* **Sequential numbers** — Verification requests for `+1234500001`, `+1234500002`, `+1234500003`...
* **Unusual country codes** — Spike in verifications to countries you don't serve
* **High failure rate** — Many verifications triggered but never completed
* **Burst traffic** — Sudden spike in verification requests from a single source

### Defenses

1. **Restrict destination countries**

    Configure `whitelisted_destinations` on your Verify profile to only allow countries where your users are:

    ```bash theme={null}
    curl -X PATCH "https://api.telnyx.com/v2/verify_profiles/YOUR_PROFILE_ID" \
      -H "Authorization: Bearer YOUR_API_KEY" \
      -H "Content-Type: application/json" \
      -d '{
        "sms": {
          "whitelisted_destinations": ["US", "CA", "GB"]
        }
      }'
    ```

2. **Require authentication before verification**

    Don't expose your verification endpoint to unauthenticated users. Require at least a session or account to trigger a verification.

3. **Add CAPTCHA**

    Place a CAPTCHA (reCAPTCHA, hCaptcha, Turnstile) before the phone number input to block automated submissions.

4. **Monitor and alert**

    Set up alerts for unusual verification volume:

    ```javascript theme={null}
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

## Code security

### Use appropriate code length

Longer codes are harder to brute-force but harder for users to enter. Balance security and usability:

| Code Length | Combinations | Brute-force time (3 attempts/min) | Recommendation             |
| ----------- | ------------ | --------------------------------- | -------------------------- |
| 4 digits    | 10,000       | \~55 hours                        | Low security only          |
| 5 digits    | 100,000      | \~23 days                         | Default — good balance     |
| 6 digits    | 1,000,000    | \~231 days                        | High security applications |

Configure code length in your Verify profile:

```bash theme={null}
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

```bash theme={null}
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

<Callout type="tip">
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

Don't reveal whether a phone number exists in your system through verification responses:

**Vulnerable vs. secure response patterns**

  **❌ Vulnerable** — reveals whether the number is registered:

  ```json theme={null}
  { "error": "No account found for this phone number" }
  ```

  **✅ Secure** — same response regardless:

  ```json theme={null}
  { "message": "If this number is registered, you'll receive a verification code." }
  ```

---

Always return a consistent response and send the verification (or silently drop it) regardless of whether the number exists in your system.

## Channel fallback strategy

Use multiple verification channels to improve delivery and security:

5. **Primary: SMS**

    Start with SMS verification — widest reach and fastest delivery.

6. **Fallback: Voice call**

    If SMS isn't delivered within 30 seconds, offer a voice call option. This helps users on networks with delayed SMS delivery.

7. **Consider: Flashcall**

    For supported markets, flashcall verification (where the phone number itself is the code) provides instant verification with no user input required.

Configure all three channels on your Verify profile:

```bash theme={null}
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

## Webhook security for Verify

Secure your verification webhook endpoint to prevent spoofed delivery notifications:

1. **Allowlist Telnyx IPs** — Only accept webhooks from `192.76.120.192/27`
2. **Use HTTPS** — Never use plain HTTP for webhook endpoints
3. **Validate payload structure** — Check for expected fields before processing
4. **Don't trust client-side status** — Always verify through webhooks or API, never trust client-reported verification status

  ```javascript
  import { createServer } from 'http';
  import { networkInterfaces } from 'os';

  const TELNYX_WEBHOOK_CIDR = '192.76.120.192/27';

  function isFromTelnyx(ip) {
    // In production, use a proper CIDR matching library
    const parts = ip.split('.').map(Number);
    return parts[0] === 192 && parts[1] === 76 &&
           parts[2] === 120 && parts[3] >= 192 && parts[3] <= 223;
  }

  app.post('/webhooks/verify', (req, res) => {
    const clientIp = req.headers['x-forwarded-for']?.split(',')[0] || req.ip;

    if (!isFromTelnyx(clientIp)) {
      console.warn(`Rejected webhook from unauthorized IP: ${clientIp}`);
      return res.sendStatus(403);
    }

    // Process webhook
    const event = req.body.data;
    if (event.event_type === 'verify.delivered') {
      console.log(`Verification delivered to ${event.payload.phone_number}`);
    }

    res.sendStatus(200);
  });
  ```

  ```python
  import ipaddress
  from flask import Flask, request, jsonify

  TELNYX_WEBHOOK_SUBNET = ipaddress.ip_network("192.76.120.192/27")

  @app.route("/webhooks/verify", methods=["POST"])
  def handle_verify_webhook():
      client_ip = ipaddress.ip_address(
          request.headers.get("X-Forwarded-For", request.remote_addr).split(",")[0].strip()
      )

      if client_ip not in TELNYX_WEBHOOK_SUBNET:
          return jsonify(error="Forbidden"), 403

      event = request.json["data"]
      if event["event_type"] == "verify.delivered":
          print(f"Verification delivered to {event['payload']['phone_number']}")

      return jsonify(success=True), 200
  ```

## Security checklist

Use this checklist when implementing Telnyx Verify in production:

**Rate limiting**

    * [ ] Per-phone-number rate limit (3/10min)
    * [ ] Per-IP rate limit (10/hour)
    * [ ] Per-account/session rate limit
    * [ ] Global volume monitoring and alerting

---

**Fraud prevention**

    * [ ] Country allowlist configured on Verify profile
    * [ ] CAPTCHA before verification trigger
    * [ ] Authentication required before sending verification
    * [ ] SMS pumping detection (sequential numbers, country spikes)

---

**Code security**

    * [ ] Appropriate code length (5-6 digits)
    * [ ] Short timeout (300 seconds or less)
    * [ ] Max failed attempts lockout (5 attempts)
    * [ ] Consistent responses (no number enumeration)

---

**Infrastructure**

    * [ ] HTTPS webhook endpoints
    * [ ] Telnyx IP allowlisting for webhooks
    * [ ] Server-side verification only (never trust client)
    * [ ] Logging and monitoring for anomalies

---

## Next steps

  - [Verify Quickstart](../tutorial/quickstart-for-telnyx-verify.md) — Set up your first verification flow

  - [Custom Templates](custom-templates-for-telnyx-verify.md) — Brand your verification messages

  - [Verify Webhooks](receiving-webhooks-for-telnyx-verify.md) — Receive real-time verification status updates

  - [Rate Limiting & Fraud Prevention](rate-limiting-and-fraud-prevention-for-verify.md) — Advanced fraud prevention strategies


## Related Pages

- [Best Practices](../runbooks/best-practices.md)
