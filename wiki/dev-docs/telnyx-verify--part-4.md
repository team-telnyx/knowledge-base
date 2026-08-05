---
title: Telnyx Verify
summary: The Telnyx Verify API delivers carrier-grade two-factor authentication over
  SMS, voice, flash call, and DTMF confirmation. This page covers the verification
  methods, how to create verify profiles, send and verify codes, build branded custom
  templates, and handle results via webhooks.
sources:
- url: https://developers.telnyx.com/docs/identity/verify/custom-templates
- url: https://developers.telnyx.com/docs/identity/verify/dtmf-confirm
- url: https://developers.telnyx.com/docs/identity/verify/index
- url: https://developers.telnyx.com/docs/identity/verify/quickstart/index
updated_at: 2026-08-05T13:43:44Z
---

# Telnyx Verify

*Part 4 of 4 — see also: [Part 1](telnyx-verify--part-1.md), [Part 2](telnyx-verify--part-2.md), [Part 3](telnyx-verify--part-3.md)*

The Telnyx Verify API delivers carrier-grade two-factor authentication over SMS, voice, flash call, and DTMF confirmation. This page covers the verification methods, how to create verify profiles, send and verify codes, build branded custom templates, and handle results via webhooks.

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

All verification templates support the following variables that will be automatically replaced when sending verifications:

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

Save the template `id` returned in the response. You'll need this ID to reference the template when creating verify profiles.

### Real-world template examples

- **E-commerce and retail:** `Your {{app_name}} verification code is {{code}}. Complete your purchase securely.`
- **Banking and finance:** `{{code}} is your {{app_name}} security code. Never share this with anyone, including our staff.`
- **Healthcare and telemedicine:** `Your {{app_name}} appointment verification code: {{code}}. If you didn't request this, contact support immediately.`
- **Social media and gaming:** `Welcome to {{app_name}}! Your verification code is {{code}}. Start connecting with friends now.`
- **Delivery and logistics:** `Your {{app_name}} delivery confirmation code is {{code}}. Track your package now.`
- **Travel and hospitality:** `{{code}} is your {{app_name}} booking verification code.`

### Use a custom template in a verify profile

Reference the template ID when creating or updating a verify profile:

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

The `messaging_template_id` field references your custom template. When you send verifications using this profile, your custom template will be used instead of the default.

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

Example response:

```
{
  "data": {
    "id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
    "text": "Your {{app_name}} verification code is {{code}}. Contact support if you did not request this."
  }
}
```

Updating a template affects all verify profiles that reference it. Test template changes carefully before updating production templates.

### Best practices

- **Keep messages concise** — SMS messages have character limits. Keep your templates under 160 characters when possible to avoid message splitting and additional costs.
- **Include security warnings** — For sensitive use cases like banking or healthcare, include warnings about not sharing codes, for example:
  ```
  Never share this code with anyone, including our staff.
  If you didn't request this, contact support immediately.
  ```
- **Test before production** — Always test new templates in a development environment before using them in production verify profiles. Send test verifications to confirm:
  - Variables are replaced correctly.
  - Message formatting appears as expected.
  - Character count is within limits.
  - Links or special characters display properly.
- **Follow compliance guidelines** — Ensure your templates comply with:
  - Industry regulations (HIPAA, PCI-DSS, GDPR, etc.).
  - Carrier requirements for SMS messaging.
  - Local laws regarding verification messages.
  - Your organization's security policies.
- **Consider localization** — If you serve multiple regions, create separate templates for different languages and cultures. Use the verify profile's `language` parameter to organize templates by locale.

## Next steps

- [Receiving Webhooks](receiving-webhooks.md) — Real-time verification status updates.
- [Custom Templates](custom-templates.md) — Branded verification messages for SMS and call types.
- Verify API Reference — Full API specification.
- Verify Quickstart — SMS and call verification guide.
