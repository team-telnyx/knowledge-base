---
title: Caller ID Policy
summary: Telnyx enforces strict caller ID validation to prevent spoofing and ensure compliance with telecommunications regulations.
sources:
  - url: https://developers.telnyx.com/docs/voice/sip-trunking/configuration/caller-id-policy/index
    content_hash: 2382fdef2c01e7c4a55dc7e9168e364facd5e8afc0e45fc3fab89ed0c82adac7
updated_at: 2026-04-10T00:00:00Z
---

# Caller ID Policy

Telnyx enforces strict caller ID validation to prevent spoofing and ensure compliance with telecommunications regulations. Invalid caller ID numbers are rejected with a `403 Caller Origination Number is Invalid D35` SIP response.

## Number format requirements

The accepted caller ID format depends on the connection's localization setting and call destination.

### USA localization

**Accepted formats:**

```
3129457420          # National format
13129457420         # 11-digit format
+13129457420        # E.164 format
```

### International localization

For non-USA localization (e.g., Ireland):

```
840-1234            # National format
01-840-1234         # Country-specific format
+353-1-840-1234     # E.164 format
```

### Cross-border calls

When calling outside the localization country, only E.164 format is accepted:

```
+1 (country code) + area code + number
```

**Example:** A connection with Ireland localization calling the USA must use `+13129457420`.

### Caller ID override

Connections with Caller ID Override enabled can send any format for outbound calls, bypassing standard validation rules.

## SIP header priority

Telnyx checks the following SIP headers in order to determine the caller ID:

1. `P-Preferred-Identity` (User part)
2. `P-Asserted-Identity` (User part)
3. `Remote-Party-Id` (User part)
4. `FROM` (User part)

When multiple headers are present, only the highest priority header is used.

## Caller ID anonymization

To anonymize the caller ID, include the `Privacy: id` header in the SIP request:

```
Privacy: id
```

**Requirements:**

* A valid origination number must still be provided
* Invalid numbers with this header trigger the D35 error
* Toll-free and emergency number calls cannot be anonymized

**Recipients always see the actual caller ID for:**

* Emergency services (911, etc.)
* Toll-free numbers

## International spoofing restrictions

Outbound calls to international destinations with spoofed caller IDs are rejected with a `503` error response. This allows implementing fallback routing logic on the client side.

## Validation behavior

If no localization is configured and a number appears invalid, Telnyx defaults to USA validation rules. Failed validation returns a `404 Invalid Destination` response.

## Configuration

Set the connection localization in the Mission Control Portal under Connection Outbound Settings, or via the API:

* [PATCH /v2/credential\_connections/](https://developers.telnyx.com/api-reference/credential-connections/update-a-credential-connection)
* [PATCH /v2/fqdn\_connections/](https://developers.telnyx.com/api-reference/fqdn-connections/update-an-fqdn-connection)
* [PATCH /v2/ip\_connections/](https://developers.telnyx.com/api-reference/ip-connections/update-an-ip-connection)

```json theme={null}
{
  "outbound": {
    "localization": "US"
  }
}
```

## Troubleshooting

| Error   | Cause                    | Solution                                                   |
| ------- | ------------------------ | ---------------------------------------------------------- |
| 403 D35 | Invalid caller ID format | Use E.164 format or match localization requirements        |
| 404     | Invalid destination      | Verify the called number is in E.164 format                |
| 503     | International spoofing   | Use a valid origination number for the destination country |
