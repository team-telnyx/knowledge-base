---
title: Telnyx Platform Reference
summary: A comprehensive reference for the Telnyx platform, covering AI, API, and
  telecom glossaries, the Number Lookup service, and the Telnyx Verify API including
  its quickstart, verification methods, custom templates, DTMF confirmation, webhooks,
  security best practices, and rate limiting for fraud prevention.
sources:
- url: https://developers.telnyx.com/docs/glossary/ai-glossary/index
  content_hash: 7a88323f4a713c8e58298daafce9b14d653a74f185c4f7c58f7a2ee1f492be15
- url: https://developers.telnyx.com/docs/glossary/api-glossary
  content_hash: 95e55f121677445e076d3a94687445e427c1f325cee3191c13b1efc56b75310a
- url: https://developers.telnyx.com/docs/glossary/telecom-glossary
  content_hash: 2498ce6f1a3191b62ab4864d776679f05fc5ea49118135f1308f40be2520c82f
- url: https://developers.telnyx.com/docs/identity/number-lookup/quickstart/index
  content_hash: 87802d596c8ff6ec0fe7dad04a81717723f8bd71b802c6559f2ba5dae36b9c2d
- url: https://developers.telnyx.com/docs/identity/verify/custom-templates
  content_hash: 0e2f873503bba841a7e3e977a333e1f6428095c64ccf6ad6bf3ccb2facbdab03
- url: https://developers.telnyx.com/docs/identity/verify/dtmf-confirm
  content_hash: 012f00382a6f536741620745424a8626b375dec75a63b293d507ad49507bfbaa
- url: https://developers.telnyx.com/docs/identity/verify/index
  content_hash: 442d1361293b33b1a7246693f7192ebade7d8b0d41449245e64728db7339b55e
- url: https://developers.telnyx.com/docs/identity/verify/quickstart/index
  content_hash: d9b13cef30b58ef5d5c90894f58c87c2a73c0d19eeb3c5a4f03ba3eb541494d4
- url: https://developers.telnyx.com/docs/identity/verify/rate-limiting-fraud-prevention
  content_hash: 43412196dd8c24c7d7d865b29128485094e1f33bb3e1fb34e0a2c0b596f16763
- url: https://developers.telnyx.com/docs/identity/verify/receiving-webhooks
  content_hash: e27e6bdcd02aca7679e72ca7370c9e0134a17c5657fd817af2d88e4f032173bb
- url: https://developers.telnyx.com/docs/identity/verify/security-best-practices
  content_hash: 2566c9d73b33320007839c8312ecff04b03098e738ff18694901b63e39233692
updated_at: 2026-06-11T10:29:44Z
---

# Telnyx Platform Reference

*Part 4 of 4 — see also: [Part 1](telnyx-platform-reference--part-1.md), [Part 2](telnyx-platform-reference--part-2.md), [Part 3](telnyx-platform-reference--part-3.md)*

A comprehensive reference for the Telnyx platform, covering AI, API, and telecom glossaries, the Number Lookup service, and the Telnyx Verify API including its quickstart, verification methods, custom templates, DTMF confirmation, webhooks, security best practices, and rate limiting for fraud prevention.

## Telnyx Verify

The Telnyx Verify API enables robust two-factor authentication (2FA) and phone-number verification using carrier-grade voice and messaging. It supports multiple verification methods, custom templates, real-time webhooks, and comprehensive fraud-prevention tooling.

### Prerequisites

1. Create a Telnyx account at [telnyx.com](https://telnyx.com/sign-up).
2. Generate an API key and set the environment variable: `export TELNYX_API_KEY="YOUR_API_KEY"`.
3. Optionally install an SDK (`npm install telnyx`, `pip install telnyx`, `gem install telnyx`, etc.).

### Verification methods

| Feature | SMS | Call | Flash Call | DTMF Confirm |
|---|---|---|---|---|
| **User action** | Type code | Listen + type code | None (app reads caller ID) | Press 1 |
| **Code generated** | Yes | Yes | Yes (caller ID) | No |
| **Verify endpoint required** | Yes | Yes | Yes | No |
| **Landline support** | No | Yes | No | Yes |
| **Delivery speed** | 1–5 seconds | 10–20 seconds | 2–5 seconds | ~10–20 seconds |
| **Works on web** | Yes | Yes | No (mobile only) | No |
| **Global coverage** | Widest | Wide | Limited | Wide |
| **Fraud risk** | SIM swap, interception | Low | Low | Low |
| **Competitor support** | Twilio, Vonage | Twilio, Vonage | Twilio | Telnyx only |

**Fallback strategy:** Configure multiple methods in your verify profile. Start with SMS (fastest and widest coverage), fall back to call if SMS fails. For mobile apps, consider flashcall as a zero-friction primary method with SMS as fallback.

### Create a verify profile

A Verify Profile holds configuration for one or more verification methods. Each profile can have one of each method configured. Use a different profile for each application.

First, list available message templates:

```bash
curl -X GET 'https://api.telnyx.com/v2/verify_profiles/templates' \
  -H 'Authorization: Bearer YOUR_API_KEY'
```

Templates use variables `{{app_name}}` and `{{code}}` (and `{{default_verification_timeout_secs}}` in some). If no template is selected, the default is `"Your verification code is {code}."`

Create the profile:

```bash
curl -X POST 'https://api.telnyx.com/v2/verify_profiles' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer YOUR_API_KEY' \
  -d '{
    "name": "my-app-verify",
    "language": "en-US",
    "sms": {
      "messaging_template_id": "0abb5b4f-459f-445a-bfcd-488998b7572d",
      "whitelisted_destinations": ["US", "CA"],
      "default_timeout_secs": 300,
      "code_length": 5
    },
    "call": {
      "default_timeout_secs": 600
    }
  }'
```

Save the returned profile `id` — you need it to trigger verifications.

### Trigger a verification

**SMS:**

```bash
curl -X POST https://api.telnyx.com/v2/verifications/sms \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -d '{"phone_number":"+13035551234","verify_profile_id":"YOUR_PROFILE_ID"}'
```

**Call:**

```bash
curl -X POST https://api.telnyx.com/v2/verifications/call \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -d '{"phone_number":"+13035551234","verify_profile_id":"YOUR_PROFILE_ID"}'
```

Both return a verification object with `status: "pending"`, an `id`, and the `type`.

### Verify a code

The user submits the code they received. Post it to the verify endpoint:

```bash
curl -X POST https://api.telnyx.com/v2/verifications/by_phone_number/+13035551234/actions/verify \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -d '{"code":"17686","verify_profile_id":"YOUR_PROFILE_ID"}'
```

The `response_code` field indicates the result:

| Response Code | Meaning |
|---|---|
| `accepted` | Code is correct — verification successful |
| `rejected` | Code is incorrect |
| `expired` | Verification timed out |
| `max_attempts_exceeded` | Too many incorrect attempts |

### DTMF confirmation

DTMF confirmation is a Telnyx-exclusive verification method. It calls the phone number, plays a TTS prompt, and collects a single keypress (`1`) to confirm ownership. No verification code is generated — the keypress itself is the confirmation. The `POST /verifications/{id}/actions/verify` endpoint is **not used**; verification completes on the call.

This method reduces user friction, works on landlines, and is ideal for caller ID verification, account recovery, and accessibility scenarios where typing a code is impractical.

**Flow and outcomes:**

| Outcome | Trigger | Status |
|---|---|---|
| Confirmed | Digit `1` pressed | `accepted` |
| Rejected | Wrong digit | `invalid` |
| Timed out | No keypress (10 s) | `expired` |
| Failed | Call not answered | `error` |

Up to 3 attempts per call. After 3 wrong digits, the call ends with status `invalid`.

**Create a profile with DTMF confirm:**

```bash
curl -X POST https://api.telnyx.com/v2/verify_profiles \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -d '{
    "name": "dtmf-verification",
    "language": "en-US",
    "dtmf_confirm": { "default_timeout_secs": 300 }
  }'
```

**Trigger DTMF verification:**

```bash
curl -X POST https://api.telnyx.com/v2/verifications/dtmf_confirm \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -d '{
    "phone_number": "+13035551234",
    "verify_profile_id": "YOUR_PROFILE_ID"
  }'
```

The default TTS prompt reads: *"This is a verification call to confirm that this phone number is going to be used as a Caller ID for outbound calls. If you did not request this verification, or if someone is asking you to accept this call, please ignore this message. If you did request this verification, please press 1."* The language is set by the profile's `language` field.

Results are delivered via webhooks (event type `verification.complete` with status `accepted` or `invalid`). You can also poll `GET /v2/verifications/{verification_id}`.

**Troubleshooting:**

| Issue | Solution |
|---|---|
| Call reaches voicemail | Status becomes `expired`. Retry with delay or fall back to SMS. |
| Wrong digit pressed | 3 attempts per call; after 3 failures, status is `invalid`. Trigger a new verification. |
| Stuck in pending | Verify webhook URL is configured and reachable. Poll the status endpoint as fallback. |
| Custom TTS prompt | Not yet supported. Voice and language come from the profile `language` setting. |
| Rate limits | Standard Verify API rate limits apply. Avoid concurrent verifications for the same number. |

### Custom templates

Custom templates let you create branded, compliant OTP messages that deploy instantly without manual approval.

**When to use custom templates:**
- Branded messages matching your company voice
- Industry-specific compliance language (HIPAA, PCI-DSS, etc.)
- Custom security warnings or instructions
- Different templates for different segments or regions

**When to use pre-built templates:**
- Quick setup with no customization needed
- Standard messages meet requirements

**Template variables:** `{{app_name}}` and `{{code}}` are automatically replaced when sending.

**Create a custom template:**

```bash
curl -L 'https://api.telnyx.com/v2/verify_profiles/templates' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer YOUR_API_KEY' \
  -d '{
    "text": "Your {{app_name}} verification code is {{code}}. Do not share this code."
  }'
```

Save the returned template `id`. Reference it when creating or updating a verify profile via the `messaging_template_id` field:

```bash
curl -L 'https://api.telnyx.com/v2/verify_profiles' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer YOUR_API_KEY' \
  -d '{
    "name": "my-app-verification",
    "language": "en-US",
    "sms": {
      "messaging_template_id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
      "whitelisted_destinations": ["US", "CA"],
      "default_timeout_secs": 300,
      "code_length": 6
    }
  }'
```

**Update a template:**

```bash
curl -L -X PATCH 'https://api.telnyx.com/v2/verify_profiles/templates/YOUR_TEMPLATE_ID' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer YOUR_API_KEY' \
  -d '{
    "text": "Your {{app_name}} verification code is {{code}}. Contact support if you did not request this."
  }'
```

Updating a template affects all verify profiles that reference it. Test changes carefully before updating production templates.

**Industry-specific examples:**

- **E-commerce:** `Your {{app_name}} verification code is {{code}}. Complete your purchase securely.`
- **Banking:** `{{code}} is your {{app_name}} security code. Never share this with anyone, including our staff.`
- **Healthcare:** `Your {{app_name}} appointment verification code: {{code}}. If you didn't request this, contact support immediately.`
- **Social media:** `Welcome to {{app_name}}! Your verification code is {{code}}. Start connecting with friends now.`
- **Delivery:** `Your {{app_name}} delivery confirmation code is {{code}}. Track your package now.`
- **Travel:** `{{code}} is your {{app_name}} booking verification code.`

**Best practices:**
- Keep messages under 160 characters to avoid SMS splitting and extra costs.
- Include security warnings for sensitive use cases (banking, healthcare).
- Test in a dev environment before production — verify variable replacement, formatting, character count, and special characters.
- Ensure compliance with industry regulations (HIPAA, PCI-DSS, GDPR), carrier requirements, and local laws.
- Create separate templates for different languages/locales; organize by the profile's `language` parameter.

### Webhooks

Configure webhooks on your verify profile to receive real-time notifications, eliminating the need for polling.

**Delivery status events:** `verify.sent`, `verify.failed`, `verify.delivered`

**Delivery statuses:**

| Delivery Status | Description |
|---|---|
| `sent` | Verification sent to upstream provider. |
| `delivered` | Upstream provider confirmed delivery. |
| `sending_failed` | Telnyx failed to send to upstream provider. |
| `delivery_failed` | Upstream provider failed to deliver to receiver. |
| `delivery_unconfirmed` | No indication whether the verification reached the receiver. |

**Verification completion events** use `event_type: "verification.complete"` with a payload containing `id`, `phone_number`, `status`, `type`, and `verify_profile_id`.

**Telnyx webhook IPs:** Allowlist `192.76.120.192/27` if you use an ACL or firewall.

### Security best practices

Verification flows are high-value targets. Major threats include:

| Threat | Impact |
|---|---|
| SMS pumping | Inflated costs, sometimes $10K+ per incident |
| Toll fraud (IRSF) | Per-minute charges on fraudulent calls |
| Brute-force attacks | Account takeover |
| Code interception | Account compromise |
| Enumeration | Privacy leak, targeted attacks |

#### Rate limiting

Apply limits at multiple layers:

| Scope | Recommended Limit | Window |
|---|---|---|
| Per phone number | 3 attempts | 10 minutes |
| Per phone number | 5 attempts | 1 hour |
| Per IP address | 10 attempts | 1 hour |
| Per account/session | 5 attempts | 1 hour |
| Global | Monitor for spikes | Continuous |

For distributed production environments, use Redis-based sliding window rate limiters across IP, phone number, and user ID dimensions.

#### SMS pumping prevention

Detection signals: sequential phone numbers, unusual country codes, high failure rates, burst traffic.

Defenses:
1. Restrict destination countries via `whitelisted_destinations` on the verify profile.
2. Require authentication before triggering verification.
3. Add CAPTCHA before the phone number input.
4. Monitor and alert on unusual volume.

#### Code security

- **Code length:** 4 digits for low security only (10K combinations), 5 digits for default (100K), 6 digits for high security (1M). Configure via `code_length` on the profile.
- **Timeouts:** 300 seconds (5 minutes) recommended. Shorter timeouts reduce brute-force windows but may frustrate users on slow networks.
- **Failed attempt lockout:** Lock out after 5 failed code entries.

#### Prevent number enumeration

Always return a consistent response regardless of whether the number exists in your system. Never reveal registration status through error messages.

**❌ Vulnerable:** `{ "error": "No account found for this phone number" }`
**✅ Secure:** `{ "message": "If this number is registered, you'll receive a verification code." }`

#### Channel fallback strategy

1. **Primary: SMS** — widest reach, fastest delivery.
2. **Fallback: Voice call** — if SMS isn't delivered within 30 seconds; helps on networks with delayed SMS.
3. **Consider: Flashcall** — zero user input in supported markets.

#### Webhook security

1. Allowlist Telnyx IPs (`192.76.120.192/27`).
2. Use HTTPS only for webhook endpoints.
3. Validate payload structure before processing.
4. Never trust client-side verification status — always verify via webhooks or API.

### Rate limiting and fraud prevention (advanced)

A robust fraud prevention system layers multiple defenses:

```
User Request → CAPTCHA → IP Rate Limit → Phone Rate Limit → Geo-fence → Anomaly Check → Telnyx Verify API
```

#### Geo-fencing

The single most effective defense against SMS pumping. Restrict verifications to countries where your service operates via `whitelisted_destinations` on the verify profile. Add server-side validation as defense-in-depth using a library like `libphonenumber-js` to parse the country code from the phone number.

**High-risk country codes** frequently targeted for SMS pumping and toll fraud:

| Code | Country | Risk |
|---|---|---|
| +232 | Sierra Leone | SMS pumping |
| +225 | Côte d'Ivoire | SMS pumping |
| +233 | Ghana | SMS pumping |
| +234 | Nigeria | Mixed (legitimate + fraud) |
| +260 | Zambia | SMS pumping |
| +256 | Uganda | SMS pumping |
| +880 | Bangladesh | Toll fraud |
| +855 | Cambodia | Toll fraud |
| +856 | Laos | Toll fraud |
| +960 | Maldives | Toll fraud |
| +592 | Guyana | Toll fraud |

If you serve users in these countries, implement stronger rate limiting rather than blanket blocking.

#### Anomaly detection

**Conversion rate monitoring:** A healthy verification flow has a 60–80% conversion rate (codes sent vs. verified). A rate below 20% may indicate an attack.

**Sequential number detection:** SMS pumping often uses sequential phone numbers. Detect sequences by sorting recent numbers and checking for numeric runs with small gaps (≤ 3 digits apart). Flag when a threshold (e.g., 5 sequential numbers) is reached.

#### Cost controls

- **Spend alerts:** Monitor account spending and set alerts via the [Telnyx Portal billing settings](https://portal.telnyx.com/#/app/billing).
- **Circuit breakers:** Automatically disable verifications when anomaly thresholds are exceeded (e.g., > 500 verifications per hour). Alert the operations team and require manual reset.

#### Incident response

1. **Immediately:** Enable circuit breaker to stop all verification sends.
2. **Investigate:** Check destination countries, IP addresses, and phone number patterns in logs.
3. **Block:** Remove affected countries from `whitelisted_destinations`.
4. **Recover:** Tighten rate limits, add CAPTCHA if absent, re-enable verifications gradually.
5. **Contact Telnyx Support:** Report the incident at [support.telnyx.com](https://support.telnyx.com) for investigation and potential charge reversal.

### Security checklist

**Rate limiting:**
- Per-phone-number rate limit (3/10 min)
- Per-IP rate limit (10/hour)
- Per-account/session rate limit
- Global volume monitoring and alerting

**Fraud prevention:**
- Country allowlist configured on verify profile
- CAPTCHA before verification trigger
- Authentication required before sending verification
- SMS pumping detection (sequential numbers, country spikes)

**Code security:**
- Appropriate code length (5–6 digits)
- Short timeout (300 seconds or less)
- Max failed attempts lockout (5 attempts)
- Consistent responses (no number enumeration)

**Infrastructure:**
- HTTPS webhook endpoints
- Telnyx IP allowlisting for webhooks
- Server-side verification only (never trust client)
- Logging and monitoring for anomalies
