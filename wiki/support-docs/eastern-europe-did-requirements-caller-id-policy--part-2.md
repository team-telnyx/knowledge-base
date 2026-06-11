---
title: Eastern Europe DID Requirements & Caller ID Policy
summary: Covers DID number purchasing requirements for Eastern European countries
  (Albania, Czech Republic, Hungary, Latvia, Romania, Russia, Slovakia, Ukraine) including
  identity, business, and address verification rules, along with Telnyx's Caller ID
  Number Policy for outbound calls.
sources:
- url: https://support.telnyx.com/en/articles/3739452-hungary-did-requirements
- url: https://support.telnyx.com/en/articles/3739496-latvia-did-requirements
- url: https://support.telnyx.com/en/articles/3739552-romania-did-requirements
- url: https://support.telnyx.com/en/articles/3739559-russia-did-requirements
- url: https://support.telnyx.com/en/articles/3739745-ukraine-did-requirements
- url: https://support.telnyx.com/en/articles/5463863-albania-did-requirements
- url: https://support.telnyx.com/en/articles/5464141-czech-republic-did-requirements
- url: https://support.telnyx.com/en/articles/5467032-slovakia-did-requirements
- url: https://support.telnyx.com/en/articles/3546251-caller-id-number-policy
updated_at: 2026-06-11T11:16:09Z
---

# Eastern Europe DID Requirements & Caller ID Policy

*Part 2 of 2 — see also: [Part 1](eastern-europe-did-requirements-caller-id-policy--part-1.md)*

Covers DID number purchasing requirements for Eastern European countries (Albania, Czech Republic, Hungary, Latvia, Romania, Russia, Slovakia, Ukraine) including identity, business, and address verification rules, along with Telnyx's Caller ID Number Policy for outbound calls.

## Caller ID Number Policy

Caller ID (CID) displays your phone number to the called party on outbound calls. Telnyx enforces a strict policy: all outbound calls with invalid Caller ID Numbers are rejected with SIP response code **403 Caller Origination Number is Invalid D35**.

### Supported Number Formats

When creating a SIP Connection, localisation defaults to USA. The system accepts calls in national, 11-digit, or +E.164 format for the localised country. Numbers outside the localised country must use +E.164 format only.

**Example — localisation set to United States:**

- US numbers accepted in national (3129457420), 11-digit (1312945720), or +E.164 (+1312945720).
- Irish numbers accepted in +E.164 only (+35318401234).

**Example — localisation set to Ireland:**

- Irish numbers accepted in national (840-1234 or 01-840-1234), 11-digit, or +E.164 (+35318401234).
- US numbers accepted in +E.164 only (+13129457420).

If a Connection's Caller ID Override is configured in Outbound settings, any format may be used.

### Localisation Handling

- The Localisation Country is set in the Telnyx Mission Control Portal under the Connection's Outbound Settings.
- If a Connection has no Localisation Country and the dialled number appears invalid, Telnyx attempts validation using USA as the default.
- If that also fails, Telnyx returns a 404 invalid destination response.

### SIP Headers for Caller ID

The following SIP headers are accepted for Caller ID, listed in priority order (highest to lowest):

1. `P-Preferred-Identity` User
2. `P-Asserted-Identity` User
3. `Remote-Party-Id` User
4. `From` User

If more than one header is provided, the highest-priority header is used.

### Anonymizing Caller ID

To anonymize Caller ID on an outbound call, include the SIP header:

```
Privacy: id
```

A valid origination number must still be provided alongside the Privacy header; Telnyx changes the caller ID to anonymous downstream. Calls without a valid caller ID are rejected with **403 Caller Origination Number is Invalid D35**.

**Toll-free and emergency numbers:** Caller ID is not anonymized when calling toll-free numbers, because the toll-free owner pays for the call and has the right to know the caller. The same applies to emergency numbers.

### EEA Destinations

Calls terminating into the European Economic Area (EEA) internationally must include a valid `P-Asserted-Identity` (PAI) header containing a real, dialable CLI. This is used by downstream carriers for origination-based routing (OBR) billing. If the PAI header is missing, contains an anonymous value, or contains an invalid number, the call may be rejected or subject to surcharges from the terminating carrier, which will be passed on to the customer. Anonymous or invalid CLIs on EEA routes are not supported and can result in significant additional costs.

### International Spoofing

Telnyx does not support caller ID spoofing on international routes. Outbound calls with spoofed caller IDs to international destinations are rejected, typically with a **503** error response, allowing route advance on the customer side.
