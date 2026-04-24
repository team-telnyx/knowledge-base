---
title: RCS Deeplinks
summary: Generate RCS deeplinks to start conversations from websites, QR codes, and email campaigns.
sources:
  - url: https://developers.telnyx.com/docs/messaging/messages/rcs-deeplinks/index
    content_hash: 06520953c35cc290342d043aff2fb1d495fb8c769c454ac684a2397f2d1eac3b
updated_at: 2026-04-10T00:00:00Z
---

# RCS Deeplinks

Generate RCS deeplinks to start conversations from websites, QR codes, and email campaigns.

> **Note:** RCS Deeplinks content has been consolidated into the [RCS Capabilities & Deeplinks](rcs-capabilities-deeplinks.md) guide. See the **RCS Deeplinks** section for full documentation including SDK examples and usage patterns.

## Quick reference

Generate a deeplink to start an RCS conversation:

```bash theme={null}
curl -s 'https://api.telnyx.com/v2/messages/rcs/deeplinks/{agent_id}?phone_number=%2B15554443333&body=hello%20world' \
  -H "Authorization: Bearer YOUR_API_KEY"
```

Response:

```json theme={null}
{
  "data": {
    "url": "sms:+18445550001?service_id=agent_id%40rbm.goog&body=hello%20world"
  }
}
```

For SDK examples, fallback configuration, and usage patterns (website buttons, QR codes, email campaigns), see:

- [RCS Capabilities & Deeplinks](rcs-capabilities-deeplinks.md) — Full guide including capability queries, adaptive sending, and deeplink generation.


## Related Pages

- [RCS Capabilities & Deeplinks](../runbooks/rcs-capabilities-deeplinks.md)
