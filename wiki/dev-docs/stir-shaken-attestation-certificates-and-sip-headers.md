---
title: 'STIR/SHAKEN: Attestation, Certificates, and SIP Headers'
summary: How Telnyx assigns STIR/SHAKEN attestation on outbound calls, selects signing
  certificates, handles forwarding and transfers, how to bring and use your own certificate
  (including verification and billing), and how attestation is surfaced via SIP headers
  on inbound/on‑net calls.
sources:
- url: https://developers.telnyx.com/docs/voice/stir-shaken/attestation-behavior/index
- url: https://developers.telnyx.com/docs/voice/stir-shaken/hosted-cert
- url: https://developers.telnyx.com/docs/voice/stir-shaken/sip-header-parameters
updated_at: 2026-05-20T09:51:21Z
---

# STIR/SHAKEN: Attestation, Certificates, and SIP Headers

How Telnyx assigns STIR/SHAKEN attestation on outbound calls, selects signing certificates, handles forwarding and transfers, how to bring and use your own certificate (including verification and billing), and how attestation is surfaced via SIP headers on inbound/on‑net calls.

## Outbound attestation levels

| Scenario | Attestation |
| --- | --- |
| Call from a Telnyx-owned phone number | A |
| Call from a non-owned or only verified number | B |

## Certificate selection for signing by geography

| Originating Caller ID | Destination | Certificate used |
| --- | --- | --- |
| US number | Any destination | US certificate |
| Canadian number | Canadian number | Canadian certificate |
| Canadian number | US number | US certificate |

## Call forwarding behavior and passports

When forwarding is enabled on a Telnyx number:

- The original STIR/SHAKEN PASSporT is preserved/passed through.
- A DIV (Diversion) PASSporT is added for the forwarded leg with Attestation A.

| Forwarding route | Certificate used |
| --- | --- |
| US → US | US certificate |
| Canada → Canada | Canadian certificate |
| US ↔ Canada (cross‑border) | US certificate |

## Call transfer methods and attestation

| Method | Origination number used | Attestation on new leg | Original PASSporT preserved? |
| --- | --- | --- | --- |
| SIP REFER | Original caller | B | No |
| Call Control API (transfer) | Number specified in request | A if number is owned; otherwise B | No |
| Call Control API (dial/bridge) | Number specified in request | A if number is owned; otherwise B | No |
| TeXML <Dial> | Number specified in request | A if number is owned; otherwise B | No |

## Bring your own hosted STIR/SHAKEN certificate

Requirements:

- A valid STIR/SHAKEN certificate from an authorized STI‑CA.
- Certificate hosted at a public HTTPS URL (x5u).
- Unencrypted PEM private key (EC‑P256 or RSA‑2048). Provide it as a single line string (no literal \n characters).
- An outbound voice profile (calls sign with the profile’s associated certificate). See [Outbound Voice Profiles for SIP trunking](outbound-voice-profiles-for-sip-trunking.md).
- A US phone number (for validation).

## Upload a certificate

Endpoint: POST /v2/stir_shaken_certs

Parameters:

- x5u_url: Public URL to the X.509 certificate (hosted by the STI‑CA or self‑hosted).
- private_key: PEM‑formatted EC‑P256 or RSA‑2048 private key, unencrypted, provided without newline escape characters.

Example values:

- x5u_url: https://certificates.example.com/path/cert.pem
- private_key: -----BEGIN EC PRIVATE KEY-----…-----END EC PRIVATE KEY-----

## Associate the certificate with an outbound voice profile

Endpoint: PATCH /v2/outbound_voice_profiles/{id}

Body field:

- stir_shaken_cert_id: The ID returned when you uploaded your certificate. After association, outbound calls placed using this profile are signed with your hosted certificate.

## Verify signing on a test call

1. Create an IP connection and enable the setting to receive the SHAKEN/STIR Identity SIP header.
2. Assign a US phone number to that connection.
3. Place a call from a connection that uses the outbound voice profile associated with your certificate.
4. Inspect the inbound INVITE on the test connection for an Identity header similar to:

```
Identity: [JWT];info=<https://your.cert.host/path/cert.pem>;alg=ES256;ppt="shaken"
```

## Billing for hosted certificates

- Price: $100 per certificate per month.
- Grace period: 7 days from upload before billing starts.
- Deletion: Cancels recurring charges.
- Billing scope: Charged per unique x5u_url (not per account).

## SIP verstat parameter on inbound and on‑net calls

Telnyx surfaces verification results via the verstat parameter in the P‑Asserted‑Identity header on inbound PSTN calls and on‑net calls between Telnyx customers.

Example:

```
P-Asserted-Identity: "John Doe" <sip:+18889809750@sip.telnyx.com;verstat=TN-Validation-Passed>
```

| verstat value | Meaning |
| --- | --- |
| TN-Validation-Passed | Verification succeeded; A‑level attestation |
| TN-Validation-Passed-B | Verification succeeded; B‑level attestation |
| TN-Validation-Passed-C | Verification succeeded; C‑level attestation |
| TN-Validation-Failed | Verification failed (invalid certificate) |
| No-TN-Validation | No Identity header present |

Notes:

- For Telnyx‑originated outbound calls, attestation is assigned as A or B per the rules above. You may still observe “‑C” in verstat on calls received from external carriers.
