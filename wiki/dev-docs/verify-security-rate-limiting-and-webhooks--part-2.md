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

*Part 2 of 5 — see also: [Part 1](verify-security-rate-limiting-and-webhooks--part-1.md), [Part 3](verify-security-rate-limiting-and-webhooks--part-3.md), [Part 4](verify-security-rate-limiting-and-webhooks--part-4.md), [Part 5](verify-security-rate-limiting-and-webhooks--part-5.md)*

Operational guidance for protecting Telnyx Verify integrations: layered rate limiting, geo-fencing, anomaly detection, cost controls, incident response, code and channel security, and webhook handling for delivery and verification status updates.

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
