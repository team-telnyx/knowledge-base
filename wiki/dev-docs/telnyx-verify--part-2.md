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

*Part 2 of 6 — see also: [Part 1](telnyx-verify--part-1.md), [Part 3](telnyx-verify--part-3.md), [Part 4](telnyx-verify--part-4.md), [Part 5](telnyx-verify--part-5.md), [Part 6](telnyx-verify--part-6.md)*

The Telnyx Verify API enables robust two-factor authentication and phone-number verification using carrier-grade voice and messaging. This page consolidates the Verify quickstart, custom templates, DTMF confirmation, webhooks, security best practices, and rate-limiting/fraud-prevention guidance into a single reference covering SMS, call, flashcall, and DTMF confirm verification methods, profile configuration, code verification, and production hardening.

## Custom templates

Telnyx Verify enables you to create and register your own verification message templates instantly. This feature allows you to build compliant, branded one-time password (OTP) messages that match your brand voice while maintaining security standards.

### When to use custom templates

**Use custom templates when:**
- You need branded verification messages that match your company's voice.
- Your industry requires specific compliance language in OTP messages.
- You want to include custom security warnings or instructions.
- You need different templates for different user segments or regions.

**Use pre-built templates when:**
- You're getting started quickly and don't need customization.
- Standard verification messages meet your requirements.
- You want to minimize setup time.

### Template variables

All verification templates support the following variables that are automatically replaced when sending verifications:

- `{{app_name}}` — Your application name as configured in the verify profile.
- `{{code}}` — The verification code sent to the user.

### Create a custom template

```
curl -L 'https://api.telnyx.com/v2/verify_profiles/templates' \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'Authorization: Bearer YOUR_API_KEY' \
  -d '{
    "text": "Your {{app_name}} verification code is {{code}}. Do not share this code."
  }'
```

Example response:

```
{
  "data": {
    "id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
    "text": "Your {{app_name}} verification code is {{code}}. Do not share this code."
  }
}
```

Save the template `id` returned in the response. You'll need this ID to reference the template when creating verify profiles. See the [Create Message Template API reference](https://developers.telnyx.com/api-reference/verify/create-message-template) for complete details.

### Real-world template examples

- **E-commerce and retail:** `Your {{app_name}} verification code is {{code}}. Complete your purchase securely.`
- **Banking and finance:** `{{code}} is your {{app_name}} security code. Never share this with anyone, including our staff.`
- **Healthcare and telemedicine:** `Your {{app_name}} appointment verification code: {{code}}. If you didn't request this, contact support immediately.`
- **Social media and gaming:** `Welcome to {{app_name}}! Your verification code is {{code}}. Start connecting with friends now.`
- **Delivery and logistics:** `Your {{app_name}} delivery confirmation code is {{code}}. Track your package now.`
- **Travel and hospitality:** `{{code}} is your {{app_name}} booking verification code.`

### Use a custom template in a verify profile

Reference the template's `id` in the `messaging_template_id` field when creating or updating a verify profile:

```
curl -L 'https://api.telnyx.com/v2/verify_profiles' \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
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

### Update a custom template

```
curl -L -X PATCH 'https://api.telnyx.com/v2/verify_profiles/templates/a1b2c3d4-e5f6-7890-abcd-ef1234567890' \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'Authorization: Bearer YOUR_API_KEY' \
  -d '{
    "text": "Your {{app_name}} verification code is {{code}}. Contact support if you did not request this."
  }'
```

Updating a template affects all verify profiles that reference it. Test template changes carefully before updating production templates. See the [Update Message Template API reference](https://developers.telnyx.com/api-reference/verify/update-message-template).

### Best practices for custom templates

- **Keep messages concise** — Stay under 160 characters when possible to avoid message splitting and additional costs.
- **Include security warnings** — For sensitive use cases like banking or healthcare, include warnings about not sharing codes.
- **Test before production** — Always test new templates in a development environment. Confirm variables are replaced correctly, formatting appears as expected, character count is within limits, and links or special characters display properly.
- **Follow compliance guidelines** — Ensure templates comply with industry regulations (HIPAA, PCI-DSS, GDPR, etc.), carrier requirements, local laws, and your organization's security policies.
- **Consider localization** — Create separate templates for different languages and cultures. Use the verify profile's `language` parameter to organize templates by locale.
