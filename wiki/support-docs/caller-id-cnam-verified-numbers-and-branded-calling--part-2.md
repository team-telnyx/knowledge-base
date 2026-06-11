---
title: Caller ID, CNAM, Verified Numbers, and Branded Calling
summary: Learn how Telnyx handles Caller ID number and name (CNAM) for inbound and
  outbound calls, how to verify non‑Telnyx numbers for CLI use, when to use Branded
  Calling, how to mitigate “Spam Likely” flags, and the limits, headers, error codes,
  and propagation behaviors to expect.
sources:
- url: https://support.telnyx.com/en/articles/1130720-caller-id-outbound-vs-cnam
- url: https://support.telnyx.com/en/articles/1130721-distinguish-your-outbound-profiles-dids
- url: https://support.telnyx.com/en/articles/1130656-set-up-inbound-caller-id-name-incoming
- url: https://support.telnyx.com/en/articles/3199007-guide-to-using-our-traffic-type-feature
- url: https://support.telnyx.com/en/articles/3546251-caller-id-number-policy
- url: https://support.telnyx.com/en/articles/4320411-more-about-outbound-voice-profiles
- url: https://support.telnyx.com/en/articles/4088988-telnyx-how-to-handle-spam-scam-likely
- url: https://support.telnyx.com/en/articles/5941652-google-verified-calls-faq
- url: https://support.telnyx.com/en/articles/6790265-verified-numbers-faq
- url: https://support.telnyx.com/en/articles/6988813-verified-numbers
- url: https://support.telnyx.com/en/articles/15138152-making-calls-with-branded-calling
- url: https://support.telnyx.com/en/articles/1130717-limits-on-concurrent-outbound-calls
updated_at: 2026-05-20T14:37:38Z
---

# Caller ID, CNAM, Verified Numbers, and Branded Calling

*Part 2 of 2 — see also: [Part 1](caller-id-cnam-verified-numbers-and-branded-calling--part-1.md)*

Learn how Telnyx handles Caller ID number and name (CNAM) for inbound and outbound calls, how to verify non‑Telnyx numbers for CLI use, when to use Branded Calling, how to mitigate “Spam Likely” flags, and the limits, headers, error codes, and propagation behaviors to expect.

## Common errors and diagnostics
- 403 Caller Origination Number is Invalid D35: CLI format/validity failed. Ensure a real, dialable number per localization and headers.
- 403 Unverified Caller Origination Number D51: Using a non‑Telnyx CLI that hasn’t been verified.
- 503 on international routes: Often returned when attempting unsupported international CLI spoofing.
- 404 invalid destination: Number failed validation (including after USA fallback when no localization set).
- 608 Rejected: Terminating carrier blocked as suspected fraud (not universal; some carriers use other 6XX codes).
- Frequent 480/486 Busy Here: Possible call labeling/blocking by destination analytics.
- CNAM status checks: Use your Telnyx Number Lookup tool to confirm CNAM updates.

## Deprecated: Google Verified Calls
- Google Verified Calls is no longer available through Telnyx (product sunset by Google).

## Practical tips
- Keep outbound CNAM within 15 characters, alphanumeric plus spaces, and consistent with your brand.
- For Canada, include your display name in SIP From/PAI where supported; in the US, rely on CNAM database listings and consider Branded Calling for supported mobiles.
- Verify any non‑Telnyx numbers before using them as CLI, and send them in the highest‑priority SIP header you support.
- Set Localization Country on connections to control accepted numbering formats and reduce invalid‑destination rejections.
- Use profile‑level limits (channels, rate caps, daily spend) to protect against runaway costs or misuse.
- Expect propagation time for CNAM and Branded Calling; ultimate display is controlled by the receiving carrier/device.
