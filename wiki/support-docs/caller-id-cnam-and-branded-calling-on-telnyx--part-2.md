---
title: Caller ID, CNAM, and Branded Calling on Telnyx
summary: A consolidated reference covering how Telnyx handles Caller ID Number (CID),
  Caller ID Name (CNAM), Branded Calling, CLI/CLD validation, and related call-completion
  troubleshooting. It explains the differences between inbound and outbound CID and
  CNAM, how to configure each in Mission Control Portal, regional behavior in the
  US and Canada, supported number formats, anonymization, international spoofing restrictions,
  branded calling setup and limitations, and how to mitigate spam-likely flags and
  SIP errors.
sources:
- url: https://support.telnyx.com/en/articles/1130656-set-up-inbound-caller-id-name-incoming
- url: https://support.telnyx.com/en/articles/1130720-caller-id-outbound-vs-cnam
- url: https://support.telnyx.com/en/articles/15138152-making-calls-with-branded-calling
- url: https://support.telnyx.com/en/articles/3546251-caller-id-number-policy
- url: https://support.telnyx.com/en/articles/4088988-telnyx-how-to-handle-spam-scam-likely
- url: https://support.telnyx.com/en/articles/5025298-troubleshooting-call-completion
- url: https://support.telnyx.com/en/articles/6247033-cli-cld-validation-faq
updated_at: 2026-08-05T13:31:03Z
---

# Caller ID, CNAM, and Branded Calling on Telnyx

*Part 2 of 5 — see also: [Part 1](caller-id-cnam-and-branded-calling-on-telnyx--part-1.md), [Part 3](caller-id-cnam-and-branded-calling-on-telnyx--part-3.md), [Part 4](caller-id-cnam-and-branded-calling-on-telnyx--part-4.md), [Part 5](caller-id-cnam-and-branded-calling-on-telnyx--part-5.md)*

A consolidated reference covering how Telnyx handles Caller ID Number (CID), Caller ID Name (CNAM), Branded Calling, CLI/CLD validation, and related call-completion troubleshooting. It explains the differences between inbound and outbound CID and CNAM, how to configure each in Mission Control Portal, regional behavior in the US and Canada, supported number formats, anonymization, international spoofing restrictions, branded calling setup and limitations, and how to mitigate spam-likely flags and SIP errors.

## Caller ID Number Policy

Telnyx enforces a strict policy around the handling of Caller ID Numbers for outbound calls. All outbound calls with invalid Caller ID Numbers are rejected with the SIP response code **403 Caller Origination Number is Invalid D35**.

### Supported Number Formats

When creating a SIP Connection, the default localization is USA, which accepts calls in national, 11-digit, or +E.164 format.

For example, with localization set to **United States**:

- **United States** — accepted formats: national, 11-digit, and +E.164 (e.g., `3129457420`, `1312945720`, `+1312945720`).
- **Ireland** — accepted format: +E.164 only (e.g., `+353-1-840-1234`).

With localization set to **Ireland**:

- **Ireland** — accepted formats: national, 11-digit, and +E.164 (e.g., `840-1234`, `01-840-1234`, `+353-1-840-1234`).
- **United States** — accepted format: +E.164 only (e.g., `+13129457420`).

If the connection's Caller ID Override is set and used for an outbound call, any format can be sent.

### How Telnyx Handles the Caller ID Number

- The Localization Country is set through Mission Control Portal under the connection's Outbound Settings.
- If a connection has no Localization Country and the dialed number appears invalid, Telnyx attempts to validate the number using USA as the Localization Country.
- If that check fails, Telnyx returns a 404 invalid destination response.

### SIP Headers That Carry the Caller ID Number

The following SIP headers are accepted for Caller ID, ordered by priority (1 highest, 4 lowest):

1. `P-Preferred-Identity` User
2. `P-Asserted-Identity` User
3. `Remote-Party-Id` User
4. `FROM` User

If more than one header is provided, the highest-priority header is followed.

### Anonymizing Caller ID Number

To anonymize the caller ID on an outbound call, include the following SIP header along with a valid caller ID in a supported format:

```
Privacy: id
```

A valid origination number is still required. Telnyx changes the caller ID to anonymous. If no valid caller ID is received, calls are rejected with **403 Caller Origination Number is Invalid D35**.

Notes:

- The caller ID of an outbound call is anonymized downstream when the `Privacy: id` header is present.
- If the number being called anonymously is a toll-free number, the caller ID is not anonymized — the owner of the toll-free number is paying for the call and has the right to know who is calling. This also applies when dialing emergency numbers.

### EEA Destinations

Calls terminating into the EEA internationally must include a valid `P-Asserted-Identity` (PAI) header containing a real, dialable CLI. This is used by downstream carriers for origination-based routing (OBR) billing. If the PAI header is missing, contains an anonymous value, or contains an invalid number, the call may be rejected or subject to surcharges from the terminating carrier, which are passed on to the customer. Anonymous or invalid CLIs on these routes are not supported and can result in significant additional costs.

### International Spoofing

For outbound calls to international destinations, calls are rejected because Telnyx and many downstream carriers do not support international spoofing. A 503 error response is typically returned so that you can attempt route advance on your side.

## CLI and CLD Validation

On June 6, 2022, Telnyx enhanced its validation mechanism by adding checks to North American National Numbering databases for CLI and CLD.

- **CLI (Calling Line Identity)** — the number the call came from.
- **CLD (Calling Line Destination)** — the number that was dialed.

### Valid Number Format

The ITU assigned country code "1" to the NANP area. NANP numbers are ten-digit numbers consisting of a three-digit Numbering Plan Area (NPA) code followed by a seven-digit local number, formatted as `NXX-NXX-XXXX`, where N is any digit from 2 through 9 and X is any digit from 0 through 9.

### What Validation Does

If a CLI or CLD is in an invalid format or does not appear in the North American National Numbering databases, calls from that number are rejected.

### Scope

CLI and CLD validation is applied to all outbound calls between NANPA numbers, except toll-free numbers, from June 6, 2022. It applies to outbound calls from Telnyx customers to the PSTN between CLI and CLD from North American Numbering Plan geographies, including the United States and its territories, Canada, Bermuda, Anguilla, Antigua & Barbuda, the Bahamas, Barbados, the British Virgin Islands, the Cayman Islands, Dominica, the Dominican Republic, Grenada, Jamaica, Montserrat, Sint Maarten, St. Kitts and Nevis, St. Lucia, St. Vincent and the Grenadines, Trinidad and Tobago, and Turks & Caicos.

### Disabling Validation

CLI and CLD validation is enabled at the service level and cannot be turned off by customers.

### How Blocked Calls Are Indicated

- **CLI validation failure** — SIP 403: "The origination number does not have a subscriber assigned. The number is invalid."
- **CLD validation failure** — SIP 404: "The destination number does not have a subscriber assigned. The number is invalid."

You can check this information in Mission Control Portal through the [Telnyx Debugging Tools](telnyx-debugging-tools.md).

### Pre-Call Validation

You can verify whether numbers are CLI- and CLD-validated using the [Your Number Lookup Guide](your-number-lookup-guide.md) tool in the portal.

### Scope of CLI Validation

CLI validation applies to all numbers used to perform outbound calls through the Telnyx network, regardless of the number provider.

### False Positives

If a call is blocked by CLI/CLD validation but the CLI and CLD are valid, report the issue to Telnyx support.
