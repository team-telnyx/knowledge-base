---
title: 'Telnyx Number Lookup and Verify: Unified Guide'
summary: Build phone intelligence and secure user verification flows with Telnyx.
  This guide combines Number Lookup fundamentals with a practical, security‑hardened
  Verify implementation, including SMS/Call/Flashcall, DTMF Confirm, custom templates,
  webhooks, and fraud prevention.
sources:
- url: https://developers.telnyx.com/docs/identity/number-lookup/quickstart
  content_hash: fa80def3c3596ad186e98c49e0778e9a6bce97ed4dcc64aaf5f168f9bcc34d88
- url: https://developers.telnyx.com/docs/identity/verify/custom-templates
  content_hash: 51000d23488b95ad9217efb823ab288f11b2c71fe6477fcce924de1e28a613b7
- url: https://developers.telnyx.com/docs/identity/verify/dtmf-confirm
  content_hash: f4d003c0914ab3c0e385a6aa3a61eae3b51fd21299b8f7ec2386d11ea40f6a4c
- url: https://developers.telnyx.com/docs/identity/verify/quickstart
  content_hash: 267f4f83abfcf6f42b649167ede4e4606307980e6af4396026396a17e22e75a2
- url: https://developers.telnyx.com/docs/identity/verify/rate-limiting-fraud-prevention
  content_hash: 878de37eced23fbc390cd86a24a3c4453e3469a30ffb678c2fbb8927181d8b33
- url: https://developers.telnyx.com/docs/identity/verify/receiving-webhooks
  content_hash: a984167ebdc1587a5a56e3bc926c8b3e10018b2647310177f0d9dc0b6fce7087
- url: https://developers.telnyx.com/docs/identity/verify/security-best-practices
  content_hash: 80b2801f7ba79ea32a3d65e2e570c513d49117f924b86b69968e63ffcc09bced
updated_at: 2026-05-14T09:50:03Z
---

# Telnyx Number Lookup and Verify: Unified Guide

*Part 2 of 2 — see also: [Part 1](telnyx-number-lookup-and-verify-unified-guide--part-1.md)*

Build phone intelligence and secure user verification flows with Telnyx. This guide combines Number Lookup fundamentals with a practical, security‑hardened Verify implementation, including SMS/Call/Flashcall, DTMF Confirm, custom templates, webhooks, and fraud prevention.

## Rate limiting and fraud prevention architecture

Layered defenses (in order)
- CAPTCHA before submission
- IP rate limit → phone number rate limit → per-user/session limits
- Geo-fence to allowed destination countries on the Verify Profile
- Anomaly checks before calling the API (conversion rate, sequences, spikes)

Redis-backed sliding window rate limiting
- Use a distributed store (e.g., Redis) to enforce limits across app instances.
- Apply distinct keys for ip:, phone:, user: scopes with appropriate windows.

## Geo-fencing and risky destinations

Profile-level allowlist
```
curl -X PATCH "https://api.telnyx.com/v2/verify_profiles/PROFILE_ID" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"sms":{"whitelisted_destinations":["US","CA","GB","AU"]}}'
```

Application-layer validation
- Parse and validate the phone number’s country before calling the API; reject unsupported regions server-side.

Common high-risk country codes (add scrutiny or stronger limits)
- +232 Sierra Leone — SMS pumping
- +225 Côte d’Ivoire — SMS pumping
- +233 Ghana — SMS pumping
- +234 Nigeria — mixed risk
- +260 Zambia — SMS pumping
- +256 Uganda — SMS pumping
- +880 Bangladesh — toll fraud
- +855 Cambodia — toll fraud
- +856 Laos — toll fraud
- +960 Maldives — toll fraud
- +592 Guyana — toll fraud

## Anomaly detection and monitoring

Signals to watch
- Conversion rate drop: sustained <20% verified/sent can indicate abuse
- Sequential or patterned numbers in recent requests
- Bursty traffic from a single IP or region

What to track
- Per-hour sent vs. verified counts and alert on thresholds
- Recent destination numbers for sequences/increments

## Cost controls and incident response

Cost controls
- Set spend alerts in the Telnyx Portal
- Implement a circuit breaker to halt sends when hourly/global thresholds are exceeded

Incident response playbook
- Trip the circuit breaker immediately to cap exposure
- Investigate logs: countries, IPs, number patterns
- Tighten allowlists (whitelisted_destinations) and rate limits; add CAPTCHA
- Re-enable gradually; notify Telnyx Support for assistance

## Configuration quick reference

Key Verify Profile settings for security and UX
- sms.whitelisted_destinations — restrict where SMS can be sent
- sms.code_length — OTP length (4–10)
- sms.default_timeout_secs — OTP validity window
- call.default_timeout_secs — call verification timeout window
- flashcall.default_timeout_secs — flashcall timeout window
- dtmf_confirm.default_timeout_secs — DTMF Confirm window
- language — controls TTS voice language and localization

## Choosing the right method (at a glance)

- SMS: fastest start, widest coverage; user types code.
- Call: works for landlines and accessibility; code read aloud.
- Flashcall: mobile-app flows with auto-read; no manual code entry.
- DTMF Confirm: press 1 to confirm; Telnyx-only, ideal for caller ID/landlines; no verify action call required.
