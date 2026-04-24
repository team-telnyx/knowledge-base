---
title: Rate Limiting and Fraud Prevention for Verify
summary: Implement server-side rate limiting, geo-fencing, anomaly detection, and cost controls to protect your Telnyx Verify integration from SMS pumping and toll fraud.
sources:
  - url: https://developers.telnyx.com/docs/identity/verify/rate-limiting-fraud-prevention/index
    content_hash: a9abc06507bb5f1c9f2a417eb92e0cccbc1c7ddb30042a233af9f468a7fa009e
updated_at: 2026-04-10T00:00:00Z
---

# Rate Limiting and Fraud Prevention for Verify

Implement server-side rate limiting, geo-fencing, anomaly detection, and cost controls to protect your Telnyx Verify integration from SMS pumping and toll fraud.

This guide goes deep on the operational side of protecting your Telnyx Verify integration — server-side rate limiting architectures, geo-fencing, anomaly detection, cost controls, and incident response. For foundational security concepts, see the [Security Best Practices](verify-security-best-practices.md) guide.

## Architecture overview

A robust fraud prevention system layers multiple defenses:

```
User Request → CAPTCHA → IP Rate Limit → Phone Rate Limit → Geo-fence → Anomaly Check → Telnyx Verify API
```

Each layer catches different attack patterns. No single defense is sufficient on its own.

## Server-side rate limiting with Redis

Production rate limiting requires a distributed store. These examples use Redis for shared state across multiple application instances.

### Sliding window rate limiter

  ```javascript
  import Redis from 'ioredis';

  const redis = new Redis(process.env.REDIS_URL);

  /**
   * Sliding window rate limiter using Redis sorted sets.
   * @param {string} key - Rate limit key (e.g., phone number or IP)
   * @param {number} maxRequests - Maximum requests allowed
   * @param {number} windowMs - Time window in milliseconds
   * @returns {Promise<{allowed: boolean, remaining: number, retryAfterMs: number}>}
   */
  async function checkRateLimit(key, maxRequests, windowMs) {
    const now = Date.now();
    const windowStart = now - windowMs;
    const redisKey = `ratelimit:${key}`;

    const pipeline = redis.pipeline();
    pipeline.zremrangebyscore(redisKey, 0, windowStart);  // Remove expired
    pipeline.zcard(redisKey);                              // Count current
    pipeline.zadd(redisKey, now, `${now}-${Math.random()}`); // Add this request
    pipeline.expire(redisKey, Math.ceil(windowMs / 1000)); // Set TTL

    const results = await pipeline.exec();
    const currentCount = results[1][1];

    if (currentCount >= maxRequests) {
      // Remove the entry we just added
      await redis.zremrangebyscore(redisKey, now, now);
      const oldestEntry = await redis.zrange(redisKey, 0, 0, 'WITHSCORES');
      const retryAfterMs = oldestEntry.length > 1
        ? windowMs - (now - Number(oldestEntry[1]))
        : windowMs;

      return { allowed: false, remaining: 0, retryAfterMs };
    }

    return { allowed: true, remaining: maxRequests - currentCount - 1, retryAfterMs: 0 };
  }

  // Usage: Multi-layer rate limiting
  async function handleVerificationRequest(req) {
    const phone = req.body.phone_number;
    const ip = req.ip;
    const userId = req.user?.id;

    // Layer 1: IP rate limit (10/hour)
    const ipCheck = await checkRateLimit(`ip:${ip}`, 10, 3600000);
    if (!ipCheck.allowed) {
      return { status: 429, retryAfter: ipCheck.retryAfterMs };
    }

    // Layer 2: Phone rate limit (3/10min)
    const phoneCheck = await checkRateLimit(`phone:${phone}`, 3, 600000);
    if (!phoneCheck.allowed) {
      return { status: 429, retryAfter: phoneCheck.retryAfterMs };
    }

    // Layer 3: User rate limit (5/hour)
    if (userId) {
      const userCheck = await checkRateLimit(`user:${userId}`, 5, 3600000);
      if (!userCheck.allowed) {
        return { status: 429, retryAfter: userCheck.retryAfterMs };
      }
    }

    // All checks passed — send verification
    return await sendVerification(phone);
  }
  ```

  ```python
  import time
  import math
  import redis
  import os
  import random

  r = redis.Redis.from_url(os.environ.get("REDIS_URL", "redis://localhost:6379"))

  def check_rate_limit(key: str, max_requests: int, window_seconds: int) -> dict:
      """Sliding window rate limiter using Redis sorted sets."""
      now = time.time()
      window_start = now - window_seconds
      redis_key = f"ratelimit:{key}"

      pipe = r.pipeline()
      pipe.zremrangebyscore(redis_key, 0, window_start)
      pipe.zcard(redis_key)
      pipe.zadd(redis_key, {f"{now}-{random.random()}": now})
      pipe.expire(redis_key, window_seconds + 1)
      results = pipe.execute()

      current_count = results[1]

      if current_count >= max_requests:
          r.zremrangebyscore(redis_key, now, now)
          oldest = r.zrange(redis_key, 0, 0, withscores=True)
          retry_after = window_seconds - (now - oldest[0][1]) if oldest else window_seconds
          return {"allowed": False, "remaining": 0, "retry_after_seconds": math.ceil(retry_after)}

      return {"allowed": True, "remaining": max_requests - current_count - 1, "retry_after_seconds": 0}

  def handle_verification_request(phone_number: str, ip: str, user_id: str = None):
      # Layer 1: IP rate limit (10/hour)
      ip_check = check_rate_limit(f"ip:{ip}", 10, 3600)
      if not ip_check["allowed"]:
          return {"error": "Too many requests", "retry_after": ip_check["retry_after_seconds"]}

      # Layer 2: Phone rate limit (3/10min)
      phone_check = check_rate_limit(f"phone:{phone_number}", 3, 600)
      if not phone_check["allowed"]:
          return {"error": "Too many attempts for this number", "retry_after": phone_check["retry_after_seconds"]}

      # Layer 3: User rate limit (5/hour)
      if user_id:
          user_check = check_rate_limit(f"user:{user_id}", 5, 3600)
          if not user_check["allowed"]:
              return {"error": "Too many requests", "retry_after": user_check["retry_after_seconds"]}

      return send_verification(phone_number)
  ```

  ```ruby
  require "redis"

  redis = Redis.new(url: ENV["REDIS_URL"] || "redis://localhost:6379")

  def check_rate_limit(redis, key, max_requests, window_seconds)
    now = Time.now.to_f
    window_start = now - window_seconds
    redis_key = "ratelimit:#{key}"

    redis.pipelined do |pipe|
      pipe.zremrangebyscore(redis_key, 0, window_start)
      pipe.zcard(redis_key)
      pipe.zadd(redis_key, now, "#{now}-#{rand}")
      pipe.expire(redis_key, window_seconds + 1)
    end => [_, current_count, _, _]

    if current_count >= max_requests
      redis.zremrangebyscore(redis_key, now, now)
      oldest = redis.zrange(redis_key, 0, 0, with_scores: true)
      retry_after = oldest.any? ? window_seconds - (now - oldest[0][1]) : window_seconds
      { allowed: false, remaining: 0, retry_after: retry_after.ceil }
    else
      { allowed: true, remaining: max_requests - current_count - 1, retry_after: 0 }
    end
  end
  ```

  ```go
  package ratelimit

  import (
  	"context"
  	"fmt"
  	"math/rand"
  	"time"

  	"github.com/redis/go-redis/v9"
  )

  type Result struct {
  	Allowed      bool
  	Remaining    int
  	RetryAfterMs int64
  }

  func CheckRateLimit(ctx context.Context, rdb *redis.Client, key string, maxReqs int, window time.Duration) (*Result, error) {
  	now := time.Now()
  	windowStart := now.Add(-window)
  	redisKey := fmt.Sprintf("ratelimit:%s", key)

  	pipe := rdb.Pipeline()
  	pipe.ZRemRangeByScore(ctx, redisKey, "0", fmt.Sprintf("%f", float64(windowStart.UnixMilli())))
  	countCmd := pipe.ZCard(ctx, redisKey)
  	member := fmt.Sprintf("%d-%f", now.UnixMilli(), rand.Float64())
  	pipe.ZAdd(ctx, redisKey, redis.Z{Score: float64(now.UnixMilli()), Member: member})
  	pipe.Expire(ctx, redisKey, window+time.Second)
  	_, err := pipe.Exec(ctx)
  	if err != nil {
  		return nil, err
  	}

  	count := countCmd.Val()
  	if count >= int64(maxReqs) {
  		rdb.ZRem(ctx, redisKey, member)
  		return &Result{Allowed: false, Remaining: 0, RetryAfterMs: window.Milliseconds()}, nil
  	}

  	return &Result{Allowed: true, Remaining: maxReqs - int(count) - 1, RetryAfterMs: 0}, nil
  }
  ```

## Geo-fencing

Restrict verifications to countries where your service operates. This is the single most effective defense against SMS pumping.

### Configure on Verify profile

```bash theme={null}
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

**High-risk country codes**

  | Code | Country       | Risk                       |
  | ---- | ------------- | -------------------------- |
  | +232 | Sierra Leone  | SMS pumping                |
  | +225 | Côte d'Ivoire | SMS pumping                |
  | +233 | Ghana         | SMS pumping                |
  | +234 | Nigeria       | Mixed (legitimate + fraud) |
  | +260 | Zambia        | SMS pumping                |
  | +256 | Uganda        | SMS pumping                |
  | +880 | Bangladesh    | Toll fraud                 |
  | +855 | Cambodia      | Toll fraud                 |
  | +856 | Laos          | Toll fraud                 |
  | +960 | Maldives      | Toll fraud                 |
  | +592 | Guyana        | Toll fraud                 |

  **Note:** These are statistical patterns, not blanket rules. If you serve users in these countries, implement stronger rate limiting rather than blocking.

---

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

```javascript theme={null}
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

## Cost controls

### Set spend alerts

Monitor your Telnyx account spending and set alerts at the account level through the [Telnyx Portal billing settings](https://portal.telnyx.com/#/app/billing).

### Implement circuit breakers

Automatically disable verifications when anomalies are detected:

```javascript theme={null}
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

1. **Immediately: Enable circuit breaker**

    Stop all verification sends to limit financial damage.

2. **Investigate: Check patterns**

    Look at the destination countries, IP addresses, and phone number patterns in your logs.

3. **Block: Update allowlists**

    Remove affected countries from your Verify profile's `whitelisted_destinations`.

4. **Recover: Tighten limits**

    Reduce rate limits, add CAPTCHA if not present, and re-enable verifications gradually.

5. **Contact Telnyx Support**

    Report the incident to [Telnyx Support](https://support.telnyx.com) for investigation and potential charge reversal.

## Configuration reference

Summary of all Verify profile settings relevant to fraud prevention:

| Setting                    | Endpoint                         | Purpose                             |
| -------------------------- | -------------------------------- | ----------------------------------- |
| `whitelisted_destinations` | `PATCH /v2/verify_profiles/{id}` | Restrict SMS to specific countries  |
| `code_length`              | `PATCH /v2/verify_profiles/{id}` | Set verification code length (4-10) |
| `default_timeout_secs`     | `PATCH /v2/verify_profiles/{id}` | Expiration time for codes           |

```bash theme={null}
