---
title: STIR/SHAKEN on Telnyx
summary: Telnyx implements STIR/SHAKEN call authentication for outbound and inbound
  calls, including attestation levels, certificate selection, call forwarding and
  transfer behavior, hosted certificate management, and the `verstat` parameter exposed
  on inbound SIP signaling.
sources:
- url: https://developers.telnyx.com/docs/voice/stir-shaken/attestation-behavior/index
- url: https://developers.telnyx.com/docs/voice/stir-shaken/hosted-cert
- url: https://developers.telnyx.com/docs/voice/stir-shaken/sip-header-parameters
updated_at: 2026-08-05T14:05:25Z
---

# STIR/SHAKEN on Telnyx

Telnyx implements STIR/SHAKEN call authentication for outbound and inbound calls, including attestation levels, certificate selection, call forwarding and transfer behavior, hosted certificate management, and the `verstat` parameter exposed on inbound SIP signaling.

## Attestation for outbound calls

Telnyx assigns STIR/SHAKEN attestation levels to outbound calls based on whether the calling number is owned by the account.

| Scenario | Attestation |
| --- | --- |
| Call from owned phone number | A |
| Call from non-owned or verified number | B |

## Certificate selection

The certificate used to sign an outbound call depends on the origin and destination of the call.

| Origin | Destination | Certificate |
| --- | --- | --- |
| US number | Any | US |
| Canadian number | Canadian number | Canadian |
| Canadian number | US number | US |

## Call forwarding

When call forwarding is enabled on a Telnyx number, the original STIR/SHAKEN passport is preserved or passed through, and a DIV (diversion) passport is added for the forwarded leg with **Attestation A**.

| Route | Certificate |
| --- | --- |
| US → US | US |
| Canada → Canada | Canadian |
| US ↔ Canada (cross-border) | US |

## Call transfers

Call transfer behavior depends on the mechanism used. In all cases the original passport is not preserved on the transferred leg.

| Method | Origination Number | Attestation | Original Passport |
| --- | --- | --- | --- |
| SIP REFER | Original caller | B | Not preserved |
| Call Control API (transfer) | Specified in request | A or B* | Not preserved |
| Call Control API (dial/bridge) | Specified in request | A or B* | Not preserved |
| TeXML `<Dial>` | Specified in request | A or B* | Not preserved |

*A if the from number is owned, B otherwise.

## Hosted STIR/SHAKEN certificate

Customers can use a self-hosted STIR/SHAKEN certificate to sign outbound calls.

### Requirements

- STIR/SHAKEN certificate from an authorized STI-CA
- Certificate hosted at a public HTTPS URL (`x5u`)
- Unencrypted PEM-format private key (EC-P256 or RSA-2048)
- Outbound voice profile
- US phone number (for validation)

### Upload certificate

`POST /v2/stir_shaken_certs`

```
{
  "x5u_url": "https://certificates.transnexus.com/xxx/xxxx.pem",
  "private_key": "-----BEGIN EC PRIVATE KEY-----[KEY]-----END EC PRIVATE KEY-----"
}
```

| Parameter | Description |
| --- | --- |
| `x5u_url` | Public URL to X.509 certificate (hosted by STI-CA or self-hosted) |
| `private_key` | PEM-formatted EC-P256 or RSA-2048 private key (no `\n` characters) |

### Associate with outbound voice profile

`PATCH /v2/outbound_voice_profiles/`

```
{
  "stir_shaken_cert_id": "e25c6e2e-4f77-42fb-b8d3-e5d8d0c7d019"
}
```

### Verify signing

To verify the certificate is signing calls:

1. Create an IP connection with "Receive SHAKEN/STIR Identity SIP header" enabled.
2. Assign a US phone number to this connection.
3. Place a call from a connection using the configured outbound voice profile.
4. Check the inbound INVITE for the `Identity` header:

```
Identity:[JWT];info=<https://[CERT_URL]>;alg=ES256;ppt="shaken"
```

### Cost

$100 per certificate per month.

| Policy | Description |
| --- | --- |
| Grace period | 7 days from upload before billing begins |
| Deletion | Cancels recurring charges |
| Billing scope | Per unique `x5u_url`, not per account |

## SIP header parameters

Telnyx provides call attestation information through the `verstat` parameter in the `P-Asserted-Identity` SIP header.

```
P-Asserted-Identity: "John Doe" <sip:+18889809750@sip.telnyx.com;verstat=TN-Validation-Passed>
```

| Value | Description |
| --- | --- |
| `TN-Validation-Passed` | Verification succeeded, A-level attestation |
| `TN-Validation-Passed-B` | Verification succeeded, B-level attestation |
| `TN-Validation-Passed-C` | Verification succeeded, C-level attestation |
| `TN-Validation-Failed` | Verification failed (invalid certificate) |
| `No-TN-Validation` | No Identity header provided |

### Call scope

The `verstat` parameter is included for:

- Inbound calls from the PSTN
- On-net calls between Telnyx customers
