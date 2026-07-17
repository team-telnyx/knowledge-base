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

*Part 5 of 6 — see also: [Part 1](telnyx-verify--part-1.md), [Part 2](telnyx-verify--part-2.md), [Part 3](telnyx-verify--part-3.md), [Part 4](telnyx-verify--part-4.md), [Part 6](telnyx-verify--part-6.md)*

The Telnyx Verify API enables robust two-factor authentication and phone-number verification using carrier-grade voice and messaging. This page consolidates the Verify quickstart, custom templates, DTMF confirmation, webhooks, security best practices, and rate-limiting/fraud-prevention guidance into a single reference covering SMS, call, flashcall, and DTMF confirm verification methods, profile configuration, code verification, and production hardening.

## Security best practices

Verification flows are a high-value target for attackers. SMS pumping, toll fraud, brute-force code guessing, and social engineering can cost you money and compromise user accounts.

### Threat overview

| Threat | Description | Impact |
| --- | --- | --- |
| SMS pumping | Attackers trigger thousands of SMS verifications to premium-rate numbers | Inflated costs, sometimes $10K+ per incident |
| Toll fraud (IRSF) | Exploiting call verification to generate revenue on premium international numbers | Per-minute charges on fraudulent calls |
| Brute-force attacks | Systematically guessing verification codes | Account takeover |
| Code interception | SIM swapping, SS7 attacks, malware intercepting SMS | Account compromise |
| Enumeration | Using verification endpoints to check if phone numbers exist in your system | Privacy leak, targeted attacks |

### Rate limiting

Rate limiting is your first line of defense against abuse. Apply limits at multiple layers.

#### Per-phone-number limits

Restrict how many verification attempts a single phone number can trigger within a time window. A typical pattern is 3 attempts per 10 minutes.

#### Per-IP address limits

Prevent a single IP from triggering verifications for many different numbers (a hallmark of SMS pumping). A typical pattern is 10 attempts per IP per hour.

#### Recommended limits

| Scope | Limit | Window |
| --- | --- | --- |
| Per phone number | 3 attempts | 10 minutes |
| Per phone number | 5 attempts | 1 hour |
| Per IP address | 10 attempts | 1 hour |
| Per account/session | 5 attempts | 1 hour |
| Global (all numbers) | Monitor for spikes | Continuous |

### SMS pumping prevention

SMS pumping is the most costly fraud vector for verification flows. Attackers abuse your send endpoint to generate SMS revenue on number ranges they control.

**Detection signals:**
- **Sequential numbers** — Verification requests for `+1234500001`, `+1234500002`, `+1234500003`…
- **Unusual country codes** — Spike in verifications to countries you don't serve.
- **High failure rate** — Many verifications triggered but never completed.
- **Burst traffic** — Sudden spike in verification requests from a single source.

**Defenses:**
1. **Restrict destination countries** — Configure `whitelisted_destinations` on your Verify profile to only allow countries where your users are.
2. **Require authentication before verification** — Don't expose your verification endpoint to unauthenticated users.
3. **Add CAPTCHA** — Place a CAPTCHA (reCAPTCHA, hCaptcha, Turnstile) before the phone number input to block automated submissions.
4. **Monitor and alert** — Set up alerts for unusual verification volume.

### Code security

#### Use appropriate code length

Longer codes are harder to brute-force but harder for users to enter. Balance security and usability:

| Code Length | Combinations | Brute-force time (3 attempts/min) | Recommendation |
| --- | --- | --- | --- |
| 4 digits | 10,000 | ~55 hours | Low security only |
| 5 digits | 100,000 | ~23 days | Default — good balance |
| 6 digits | 1,000,000 | ~231 days | High security applications |

Configure code length in your Verify profile:

```
curl -X PATCH "https://api.telnyx.com/v2/verify_profiles/YOUR_PROFILE_ID" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "sms": {
      "code_length": 6
    }
  }'
```

#### Set appropriate timeouts

Short timeouts reduce the window for brute-force attacks. A 5-minute timeout (300 seconds) works well for most applications. Shorter timeouts (120s) add security but may frustrate users on slow networks.

#### Limit verification attempts

Lock out after too many failed code entries to prevent brute-force. A common pattern is to lock out after 5 failed attempts.

### Prevent number enumeration

Don't reveal whether a phone number exists in your system through verification responses. Always return a consistent response and send the verification (or silently drop it) regardless of whether the number exists in your system.

**Vulnerable** — reveals whether the number is registered:

```
{ "error": "No account found for this phone number" }
```

**Secure** — same response regardless:

```
{ "message": "If this number is registered, you'll receive a verification code." }
```

### Channel fallback strategy

Use multiple verification channels to improve delivery and security:

1. **Primary: SMS** — Start with SMS verification — widest reach and fastest delivery.
2. **Fallback: Voice call** — If SMS isn't delivered within 30 seconds, offer a voice call option. This helps users on networks with delayed SMS delivery.
3. **Consider: Flashcall** — For supported markets, flashcall verification (where the phone number itself is the code) provides instant verification with no user input required.

### Webhook security

Secure your verification webhook endpoint to prevent spoofed delivery notifications:

1. **Allowlist Telnyx IPs** — Only accept webhooks from `192.76.120.192/27`.
2. **Use HTTPS** — Never use plain HTTP for webhook endpoints.
3. **Validate payload structure** — Check for expected fields before processing.
4. **Don't trust client-side status** — Always verify through webhooks or API, never trust client-reported verification status.

### Security checklist

**Rate limiting**
- Per-phone-number rate limit (3/10min)
- Per-IP rate limit (10/hour)
- Per-account/session rate limit
- Global volume monitoring and alerting

**Fraud prevention**
- Country allowlist configured on Verify profile
- CAPTCHA before verification trigger
- Authentication required before sending verification
- SMS pumping detection (sequential numbers, country spikes)

**Code security**
- Appropriate code length (5-6 digits)
- Short timeout (300 seconds or less)
- Max failed attempts lockout (5 attempts)
- Consistent responses (no number enumeration)

**Infrastructure**
- HTTPS webhook endpoints
- Telnyx IP allowlisting for webhooks
- Server-side verification only (never trust client)
- Logging and monitoring for anomalies
