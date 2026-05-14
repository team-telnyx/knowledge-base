---
title: 'Telnyx Number Lookup and Verify: Unified Guide'
summary: Build phone intelligence and secure user verification flows with Telnyx.
  This guide combines Number Lookup fundamentals with a practical, security‑hardened
  Verify implementation, including SMS/Call/Flashcall, DTMF Confirm, custom templates,
  webhooks, and fraud prevention.
sources:
- url: https://developers.telnyx.com/docs/identity/number-lookup/quickstart
- url: https://developers.telnyx.com/docs/identity/verify/custom-templates
- url: https://developers.telnyx.com/docs/identity/verify/dtmf-confirm
- url: https://developers.telnyx.com/docs/identity/verify/quickstart
- url: https://developers.telnyx.com/docs/identity/verify/rate-limiting-fraud-prevention
- url: https://developers.telnyx.com/docs/identity/verify/receiving-webhooks
- url: https://developers.telnyx.com/docs/identity/verify/security-best-practices
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
