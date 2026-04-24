---
title: Hosted STIR/SHAKEN Certificate
summary: Use a self-hosted STIR/SHAKEN certificate to sign outbound calls.
sources:
  - url: https://developers.telnyx.com/docs/voice/stir-shaken/hosted-cert/index
    content_hash: 1643a7ff2835889abd076f823970f4cf76be3cc703eb184f4f42f32f9ed1d772
updated_at: 2026-04-10T00:00:00Z
---

# Hosted STIR/SHAKEN Certificate

Use a self-hosted STIR/SHAKEN certificate to sign outbound calls.

## Requirements

* STIR/SHAKEN certificate from an authorized STI-CA
* Certificate hosted at a public HTTPS URL (`x5u`)
* Unencrypted PEM-format private key (EC-P256 or RSA-2048)
* Outbound voice profile
* US phone number (for validation)

## Upload certificate

`POST /v2/stir_shaken_certs`

```json theme={null}
{
  "x5u_url": "https://certificates.transnexus.com/xxx/xxxx.pem",
  "private_key": "-----BEGIN EC PRIVATE KEY-----[KEY]-----END EC PRIVATE KEY-----"
}
```

| Parameter     | Description                                                        |
| ------------- | ------------------------------------------------------------------ |
| `x5u_url`     | Public URL to X.509 certificate (hosted by STI-CA or self-hosted)  |
| `private_key` | PEM-formatted EC-P256 or RSA-2048 private key (no `\n` characters) |

## Associate with outbound voice profile

[PATCH /v2/outbound\_voice\_profiles/](https://developers.telnyx.com/api-reference/outbound-voice-profiles/updates-an-existing-outbound-voice-profile)

```json theme={null}
{
  "stir_shaken_cert_id": "e25c6e2e-4f77-42fb-b8d3-e5d8d0c7d019"
}
```

## Verify signing

To verify the certificate is signing calls:

1. Create an IP connection with "Receive SHAKEN/STIR Identity SIP header" enabled
2. Assign a US phone number to this connection
3. Place a call from a connection using the configured outbound voice profile
4. Check the inbound INVITE for the `Identity` header:

```
Identity:[JWT];info=<https://[CERT_URL]>;alg=ES256;ppt="shaken"
```

## Cost

\$100 per certificate per month.

| Policy        | Description                              |
| ------------- | ---------------------------------------- |
| Grace period  | 7 days from upload before billing begins |
| Deletion      | Cancels recurring charges                |
| Billing scope | Per unique `x5u_url`, not per account    |
