---
title: "Set up a hosted STIR/SHAKEN certificate"
summary: "Use your own certificate to sign outbound calls through Telnyx’s hosted signing service."
sources:
- url: "https://support.telnyx.com/en/articles/2026093001-set-up-a-hosted-stir-shaken-certificate"
updated_at: 2026-09-30T16:47:17Z
tags: [support-docs]
source_path: "support-docs/en--articles--2026093001-set-up-a-hosted-stir-shaken-certificate.md"
generated_by: incremental-support-docs-wiki
---
<!-- generated_from=support-docs/en--articles--2026093001-set-up-a-hosted-stir-shaken-certificate.md -->

# Set up a hosted STIR/SHAKEN certificate

Use your own certificate to sign outbound calls through Telnyx’s hosted signing service.

## Before you begin

You’ll need:

- A certificate from an authorized STI-CA, hosted at a public HTTPS URL.
- An unencrypted PEM private key using EC-P256 or RSA-2048.
- An outbound voice profile.
- A US phone number for testing.

## 1. Add your certificate in Mission Control Portal

1. Sign in to the [Mission Control Portal](https://portal.telnyx.com/).
2. Open the **STIR/SHAKEN Hosted Certificates** tab beside **Outbound Voice Profiles**.
3. Click **Create**.

![STIR/SHAKEN Hosted Certificates tab with the Create button](_images/stir-shaken-hosted-certificates.png)

4. In **X5U url**, enter the public HTTPS URL where your certificate is hosted.
5. Under **Private key**, drag and drop your private key file or click **Browse files** to select it.
6. Click **Complete** to submit.

![Create STIR/SHAKEN Hosted Certificate form with the certificate URL and private key upload fields](_images/stir-shaken-create-hosted-certificate.png)

### API alternative

Send `POST /v2/stir_shaken_certs`:

```json
{
  "x5u_url": "https://example.com/certificate.pem",
  "private_key": "<YOUR_PEM_PRIVATE_KEY>"
}
```

For API requests, supply the key without `\n` characters.

## 2. Associate the certificate with an outbound voice profile

Send `PATCH /v2/outbound_voice_profiles/{id}` using your profile ID:

```json
{
  "stir_shaken_cert_id": "<YOUR_CERTIFICATE_ID>"
}
```

## 3. Verify signing

1. Create an IP connection with **Receive SHAKEN/STIR Identity SIP header** enabled.
2. Assign a US number to it.
3. Call that number using the configured outbound voice profile.
4. Check that the inbound SIP `INVITE` contains an `Identity` header referencing your certificate URL.

## Billing

Each certificate costs **$100 per month**, with a seven-day grace period after upload. Charges apply per unique `x5u_url`. Deletion cancels recurring charges.

Reference: [Telnyx hosted certificate documentation](https://developers.telnyx.com/docs/voice/stir-shaken/hosted-cert/index#hosted-stir-shaken-certificate).
