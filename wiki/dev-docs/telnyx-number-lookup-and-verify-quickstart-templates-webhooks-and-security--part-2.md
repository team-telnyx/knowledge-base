---
title: 'Telnyx Number Lookup and Verify: Quickstart, Templates, Webhooks, and Security'
summary: Learn how to look up phone number intelligence and implement multi-channel
  verification (SMS, call, flashcall, and Telnyx-only DTMF confirmation). This guide
  covers quickstarts, custom OTP templates, webhook handling, and production-grade
  security and fraud prevention.
sources:
- url: https://developers.telnyx.com/docs/identity/number-lookup/quickstart/index
  content_hash: fa80def3c3596ad186e98c49e0778e9a6bce97ed4dcc64aaf5f168f9bcc34d88
- url: https://developers.telnyx.com/docs/identity/verify/custom-templates
  content_hash: 51000d23488b95ad9217efb823ab288f11b2c71fe6477fcce924de1e28a613b7
- url: https://developers.telnyx.com/docs/identity/verify/dtmf-confirm
  content_hash: f4d003c0914ab3c0e385a6aa3a61eae3b51fd21299b8f7ec2386d11ea40f6a4c
- url: https://developers.telnyx.com/docs/identity/verify/index
  content_hash: b367b7777c5b0e46bc536202ca4a18dd4357703e82475e8c5d5f61bd690f2801
- url: https://developers.telnyx.com/docs/identity/verify/quickstart/index
  content_hash: 267f4f83abfcf6f42b649167ede4e4606307980e6af4396026396a17e22e75a2
- url: https://developers.telnyx.com/docs/identity/verify/rate-limiting-fraud-prevention
  content_hash: 878de37eced23fbc390cd86a24a3c4453e3469a30ffb678c2fbb8927181d8b33
- url: https://developers.telnyx.com/docs/identity/verify/receiving-webhooks
  content_hash: a984167ebdc1587a5a56e3bc926c8b3e10018b2647310177f0d9dc0b6fce7087
- url: https://developers.telnyx.com/docs/identity/verify/security-best-practices
  content_hash: 80b2801f7ba79ea32a3d65e2e570c513d49117f924b86b69968e63ffcc09bced
updated_at: 2026-05-20T08:27:44Z
---

# Telnyx Number Lookup and Verify: Quickstart, Templates, Webhooks, and Security

*Part 2 of 2 — see also: [Part 1](telnyx-number-lookup-and-verify-quickstart-templates-webhooks-and-security--part-1.md)*

Learn how to look up phone number intelligence and implement multi-channel verification (SMS, call, flashcall, and Telnyx-only DTMF confirmation). This guide covers quickstarts, custom OTP templates, webhook handling, and production-grade security and fraud prevention.

## Security, rate limiting, and fraud prevention
Layer defenses to stop SMS pumping, toll fraud, and brute-force attacks:

- Multi-layer flow: User → CAPTCHA → IP limit → Phone limit → Geo-fence → Anomaly checks → Telnyx Verify
- Recommended limits (typical): per-phone 3/10min, per-phone 5/hour, per-IP 10/hour; add per-account/session caps.
- Geo-fencing: Restrict destinations on your profile to served countries only:
```
curl -X PATCH "https://api.telnyx.com/v2/verify_profiles/YOUR_PROFILE_ID" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"sms": {"whitelisted_destinations": ["US","CA","GB","AU"]}}'
```
- High-risk country codes often targeted (review before enabling): +232, +225, +233, +234, +260, +256, +880, +855, +856, +960, +592.
- Code security: Use 5–6 digits; short timeouts (~300s); lock out after repeated failures.
- Prevent number enumeration: Return neutral responses and avoid revealing account existence.
- Channel fallback: Start with SMS, fall back to call; consider flashcall for supported mobile app flows.
- Anomaly detection: Monitor conversion rate (sent vs. verified), detect sequential number bursts, alert on volume spikes.
- Cost controls and incident response: Set spend alerts, implement circuit breakers, tighten allowlists/limits during incidents, and contact Telnyx Support.

Profile hardening example:
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
    "call": { "default_timeout_secs": 300 }
  }'
```

## Troubleshooting tips
- DTMF call hit voicemail → Expect status expired; retry later or fall back to SMS.
- Wrong DTMF key → Up to 3 attempts; then invalid. Trigger a new verification to retry.
- Stuck in pending → Ensure webhook endpoint is reachable; use polling as a fallback.
- Rate limit hits → Surface 429s with retry-after guidance; space out retries and enforce server-side limits.
