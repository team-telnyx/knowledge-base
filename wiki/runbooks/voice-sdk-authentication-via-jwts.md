---
title: Voice SDK Authentication via JWTs
summary: The following API request will generate a JWT.
sources:
  - url: https://developers.telnyx.com/docs/voice/webrtc/auth/jwt/index
    content_hash: 909e531af704e6cadbff9dbec0649aef37fa64d303426f8cd9b804c911a99de4
updated_at: 2026-04-10T00:00:00Z
---

# Voice SDK Authentication via JWTs

## Prerequisites

* An active telephony credential

## Create a Token

The following API request will generate a JWT.

```http theme={null}
POST /v2/telephony_credentials/:id/token HTTP/1.1
Host: api.telnyx.com
Authorization: Bearer XXX
```

This JWT is valid until:

* 24 hours after its creation or
* the parent telephony credential is expired

whichever comes first

## SDK Authentication

SDKs are authenticated with the JWT.

## Limits

Currently, there exists

* No limit on count of tokens on a telephony credential,
* Nor any limit on the aggregate count of tokens on a single account.

## Additional Resources

* [JWT API Reference](https://developers.telnyx.com/docs/voice/webrtc/auth/jwt/index#create-a-token)


## Related Pages

- [Voice SDK Authentication via Telephony Credentials](../runbooks/voice-sdk-authentication-via-telephony-credentials.md)
- [Voice SDK Authentication via Credential Based SIP Connections](../runbooks/voice-sdk-authentication-via-credential-based-sip-connections.md)
- [SIP Authentication Methods](../runbooks/sip-authentication-methods.md)
- [IP Authentication Token](../runbooks/ip-authentication-token.md)
- [Two-Factor Authentication (2FA) via SMS](../runbooks/two-factor-authentication-2fa-via-sms.md)
