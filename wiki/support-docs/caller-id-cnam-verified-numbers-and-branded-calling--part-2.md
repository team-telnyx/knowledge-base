---
title: Caller ID, CNAM, Verified Numbers, and Branded Calling
summary: Learn how Telnyx handles Caller ID number and name (CNAM) for inbound and
  outbound calls, how to verify non‑Telnyx numbers for CLI use, when to use Branded
  Calling, how to mitigate “Spam Likely” flags, and the limits, headers, error codes,
  and propagation behaviors to expect.
sources:
- url: https://support.telnyx.com/en/articles/1130720-caller-id-outbound-vs-cnam
  content_hash: dd00c3b500e01915122a41df25a115bf5dce41b6a8aaaeaf9683ab306bf1f140
- url: https://support.telnyx.com/en/articles/1130721-distinguish-your-outbound-profiles-dids
  content_hash: c3310a35da8736c228ac12fc321b994fece0d57ed4b4b9fa1e47ab392db16ec7
- url: https://support.telnyx.com/en/articles/1130656-set-up-inbound-caller-id-name-incoming
  content_hash: 7ed4c3695720dfa03bb3eb9d0e6a3b4482435cae85a34339584b6cf20b3b18cd
- url: https://support.telnyx.com/en/articles/3199007-guide-to-using-our-traffic-type-feature
  content_hash: 6ee7563e902423b2190c4e495144e572d64a20d2026817495d1af0600e597543
- url: https://support.telnyx.com/en/articles/3546251-caller-id-number-policy
  content_hash: f9f883ecd6abe5f848b7e06352ff8969dc2f27342b4f8eb37856e6fbb5f716f0
- url: https://support.telnyx.com/en/articles/4320411-more-about-outbound-voice-profiles
  content_hash: 0e98513b74878e6b415c2a231fda36c870bf1cef823ad3fa34b837d0e5db10aa
- url: https://support.telnyx.com/en/articles/4088988-telnyx-how-to-handle-spam-scam-likely
  content_hash: ef975a113b3f9aff3e16b560784dc65ae39e164ac12d9a84558ff1e321d82dc7
- url: https://support.telnyx.com/en/articles/5941652-google-verified-calls-faq
  content_hash: bf8b23fb6eade0e9ed5d5cfa8cb64d90406f24f8f3688a963929771755aa9477
- url: https://support.telnyx.com/en/articles/6790265-verified-numbers-faq
  content_hash: 91b700ae3627be890dd0cb9f8ac2fa7b089ce289742650521036430c17761275
- url: https://support.telnyx.com/en/articles/6988813-verified-numbers
  content_hash: 02c93ada78c36152ee19b74c0b20f833f1db8cd4c325825eb28c0e4de066c482
- url: https://support.telnyx.com/en/articles/15138152-making-calls-with-branded-calling
  content_hash: ed8c0874d71606c6466945a7420ca07ce637f47e7cace07239ceee8f20b388a5
- url: https://support.telnyx.com/en/articles/1130717-limits-on-concurrent-outbound-calls
  content_hash: 2b414106d10c3c5b6fccd732adfd2894b2463b9dcdaa238beca204a12c513a68
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
