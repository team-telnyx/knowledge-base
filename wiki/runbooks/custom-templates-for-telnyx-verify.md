---
title: Custom templates for Telnyx Verify
summary: Create and manage custom verification message templates for branded OTP communications with Telnyx Verify.
sources:
  - url: https://developers.telnyx.com/docs/identity/verify/custom-templates/index
    content_hash: c814d51e9a01a170b31e9fcd8a31e81c696b89c3af5d3cd3b4a465857fdc28d9
updated_at: 2026-04-10T00:00:00Z
---

# Custom templates for Telnyx Verify

Create and manage custom verification message templates for branded OTP communications with Telnyx Verify.

Telnyx Verify now enables you to create and register your own verification message templates instantly. This feature allows you to build compliant, branded one-time password (OTP) messages that match your brand voice while maintaining security standards.

## Overview

Custom templates give you complete control over your verification messaging. Instead of using pre-built templates, you can create personalized messages that:

* Align with your brand guidelines and tone of voice.
* Include industry-specific security warnings and disclaimers.
* Maintain compliance with regulatory requirements.
* Deploy instantly without manual approval processes.

## When to use custom templates

**Use custom templates when:**

* You need branded verification messages that match your company's voice.
* Your industry requires specific compliance language in OTP messages.
* You want to include custom security warnings or instructions.
* You need different templates for different user segments or regions.

**Use pre-built templates when:**

* You're getting started quickly and don't need customization.
* Standard verification messages meet your requirements.
* You want to minimize setup time.

## Template variables

All verification templates support the following variables that will be automatically replaced when sending verifications:

* `{{app_name}}` - Your application name as configured in the verify profile.
* `{{code}}` - The verification code sent to the user.

## Creating custom templates

Use the Telnyx API to create custom verification message templates.

### Create a custom template

```bash theme={null}
curl -L 'https://api.telnyx.com/v2/verify_profiles/templates' \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'Authorization: Bearer YOUR_API_KEY' \
  -d '{
    "text": "Your {{app_name}} verification code is {{code}}. Do not share this code."
  }'
```

### Example response

```json theme={null}
{
  "data": {
    "id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
    "text": "Your {{app_name}} verification code is {{code}}. Do not share this code."
  }
}
```

Save the template `id` returned in the response. You'll need this ID to reference the template when creating verify profiles.

For complete API details, see the [Create Message Template API reference](https://developers.telnyx.com/api-reference/verify/create-message-template).

## Real-world template examples

Here are industry-specific template examples to inspire your custom messaging:

### E-commerce and retail

```
Your {{app_name}} verification code is {{code}}. Complete your purchase securely.
```

### Banking and finance

```
{{code}} is your {{app_name}} security code. Never share this with anyone, including our staff.
```

### Healthcare and telemedicine

```
Your {{app_name}} appointment verification code: {{code}}. If you didn't request this, contact support immediately.
```

### Social media and gaming

```
Welcome to {{app_name}}! Your verification code is {{code}}. Start connecting with friends now.
```

### Delivery and logistics

```
Your {{app_name}} delivery confirmation code is {{code}}. Track your package now.
```

### Travel and hospitality

```
{{code}} is your {{app_name}} booking verification code.
```

## Using custom templates in verify profiles

Once you've created a custom template, reference its ID when creating or updating a verify profile.

### Example: Create verify profile with custom template

```bash theme={null}
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

## Updating custom templates

You can update existing custom templates to refine messaging or fix errors.

### Update a template

```bash theme={null}
curl -L -X PATCH 'https://api.telnyx.com/v2/verify_profiles/templates/a1b2c3d4-e5f6-7890-abcd-ef1234567890' \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'Authorization: Bearer YOUR_API_KEY' \
  -d '{
    "text": "Your {{app_name}} verification code is {{code}}. Contact support if you did not request this."
  }'
```

### Example response

```json theme={null}
{
  "data": {
    "id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
    "text": "Your {{app_name}} verification code is {{code}}. Contact support if you did not request this."
  }
}
```

<Callout type="warning">
  Updating a template affects all verify profiles that reference it. Test template changes carefully before updating production templates.

For complete API details, see the [Update Message Template API reference](https://developers.telnyx.com/api-reference/verify/update-message-template).

## Best practices

### Keep messages concise

SMS messages have character limits. Keep your templates under 160 characters when possible to avoid message splitting and additional costs.

### Include security warnings

For sensitive use cases like banking or healthcare, include warnings about not sharing codes:

```
Never share this code with anyone, including our staff.
If you didn't request this, contact support immediately.
```

### Test before production

Always test new templates in a development environment before using them in production verify profiles. Send test verifications to confirm:

* Variables are replaced correctly.
* Message formatting appears as expected.
* Character count is within limits.
* Links or special characters display properly.

### Follow compliance guidelines

Ensure your templates comply with:

* Industry regulations (HIPAA, PCI-DSS, GDPR, etc.).
* Carrier requirements for SMS messaging.
* Local laws regarding verification messages.
* Your organization's security policies.

### Consider localization

If you serve multiple regions, create separate templates for different languages and cultures. Use the verify profile's `language` parameter to organize templates by locale.

## Next steps

* Learn how to send verifications: [Telnyx Verify quickstart](../tutorial/quickstart-for-telnyx-verify.md)
* Configure webhooks for verification events: [Receiving webhooks](receiving-webhooks-for-telnyx-verify.md)
* View the complete Verify API reference: [Verify API documentation](https://developers.telnyx.com/api-reference/verify/create-a-verify-profile)


## Related Pages

- [Quickstart for Telnyx Verify](../tutorial/quickstart-for-telnyx-verify.md)
- [Receiving Webhooks for Telnyx Verify](../runbooks/receiving-webhooks-for-telnyx-verify.md)
