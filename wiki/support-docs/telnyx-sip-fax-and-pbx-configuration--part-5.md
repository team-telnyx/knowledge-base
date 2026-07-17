---
title: Telnyx SIP, Fax, and PBX Configuration
summary: This page consolidates Telnyx support documentation covering fax service
  setup and error handling (T.38 and G.711), Programmable Fax API webhook and CDR
  error codes, FreeSWITCH and FusionPBX trunk configuration, SIP Trunking FIPS support,
  and the meaning of SIP 603+ carrier rejections.
sources:
- url: https://support.telnyx.com/en/articles/1130672-fax-service-with-telnyx-via-t-38-or-g711
- url: https://support.telnyx.com/en/articles/15374685-telnyx-sip-trunking-fips-support
- url: https://support.telnyx.com/en/articles/15395095-understanding-sip-603-carrier-rejections
- url: https://support.telnyx.com/en/articles/1616935-freeswitch-ip-trunk-setup
- url: https://support.telnyx.com/en/articles/1618801-freeswitch-credentials-trunk
- url: https://support.telnyx.com/en/articles/3220393-fusionpbx-telnyx-credentials
- url: https://support.telnyx.com/en/articles/4967498-fax-api-error-list
- url: https://support.telnyx.com/en/collections/3968239-telnyx-fax-configuration-errors
updated_at: 2026-07-17T09:05:45Z
---

# Telnyx SIP, Fax, and PBX Configuration

*Part 5 of 5 — see also: [Part 1](telnyx-sip-fax-and-pbx-configuration--part-1.md), [Part 2](telnyx-sip-fax-and-pbx-configuration--part-2.md), [Part 3](telnyx-sip-fax-and-pbx-configuration--part-3.md), [Part 4](telnyx-sip-fax-and-pbx-configuration--part-4.md)*

This page consolidates Telnyx support documentation covering fax service setup and error handling (T.38 and G.711), Programmable Fax API webhook and CDR error codes, FreeSWITCH and FusionPBX trunk configuration, SIP Trunking FIPS support, and the meaning of SIP 603+ carrier rejections.

## Understanding SIP 603+ Carrier Rejections

SIP 603+ is industry shorthand for a standardized use of the SIP 603 Decline response when a call is blocked on an IP network based on reasonable analytics for outbound calls in the U.S. It is not a separate SIP status code; the status code remains 603. The "+" indicates that the response includes additional standardized information, such as the *Network Blocked* reason phrase and related signaling details, to improve transparency and support redress.

In carrier voice networks, a SIP 603+ response may be generated when a terminating carrier, intermediate provider, downstream network, or call analytics provider determines that a call should be blocked before it reaches the intended recipient. The FCC adopted SIP 603+ in FCC 25-15 as a standardized notification mechanism for IP calls blocked based on reasonable analytics.

### What SIP 603 and SIP 603+ Mean

SIP response codes are three-digit codes. `603 Decline` is a SIP `6xx` global failure response, meaning the call was rejected rather than temporarily unavailable or unanswered.

SIP 603+ is not a new numeric response code. Under FCC 25-15 and the ATIS-1000099 standard, 603+ refers to a standardized notification format for analytics-based blocking on IP networks. In practice, the SIP response uses status code `603` and the reason phrase `Network Blocked`, with additional standardized information intended to help callers identify analytics-based blocking and pursue redress when appropriate.

A `603 Decline` or 603+ formatted rejection does not mean Telnyx rejected the call. The source of the rejection is always the terminating carrier for the call.

### Why Calls May Be Rejected or Blocked

Telnyx does not have visibility into the full decision logic used by terminating carriers, downstream providers, or analytics providers when they reject or block a call. The clearest signal available may be the SIP response itself, including any SIP "603+" metadata or "Reason" header returned with the call.

Common factors that may contribute to carrier analytics or reputation-based blocking:

- The calling number has a poor or unknown reputation.
- Calls from the number are being labeled as spam, scam, or unwanted.
- The calling pattern looks suspicious, such as sudden high volume, repeated retries, short call duration, or low answer rates.
- The number is new and has little call history.
- The traffic pattern resembles robocalling or unsolicited outreach.
- The recipient, terminating carrier, or analytics provider has policy-based blocking enabled.

These are potential contributing factors, not a definitive explanation for any specific call. The available SIP signaling, CDR fields, and call trace evidence should be used to determine what was actually returned for a given call.

### How Telnyx Surfaces the Rejection

When Telnyx receives a `SIP 603` response using the 603+ blocking format from a downstream or terminating carrier, Telnyx passes the downstream `603` response and its available blocking context toward your SIP trunking equipment as received from the downstream carrier.

A rejected call may include a SIP `Reason` header like this:

```
Reason: SIP;cause=603;text="v=analytics1;url=https://example.com";location=RLN
```

In this example:

- `cause=603` indicates the SIP failure cause.
- `text` includes:
  - `v=analytics1`, identifying analytics-based blocking.
  - At least one redress method such as `url`, `tel`, or `email`, which can be used to contact the terminating carrier to report invalid rejections.
  - `location` identifies where blocking occurred in the call path, using standardized values such as:
    - LN — originating network
    - TN — transit network
    - RLN — network serving the called party
    - LPN — originating private network
    - RPN — private network serving the called party

For SIP 603+-formatted rejections, Telnyx passes the downstream `603` response toward your SIP trunking equipment without any modifications. Reason headers are useful diagnostic signals but are not always standardized across carriers; the exact fields and wording can vary.

### Reducing the Chance of Rejection

Carrier analytics and reputation decisions are not controlled by Telnyx, but the following practices can help reduce false-positive blocking and improve call completion.

#### Use Appropriate Caller ID

- Avoid anonymous caller IDs.
- Use numbers owned by and associated with your account as the number owner. This always results in STIR/SHAKEN A attestation, which decreases the chance of the carrier blocking the call.
- A non-Telnyx caller ID that has been verified results in STIR/SHAKEN B attestation, which increases the chance of the carrier blocking the call.

#### Improve Number Identity and Reputation

- Configure accurate CNAM where applicable.
- Register legitimate outbound calling numbers and use cases with the [Free Caller Registry](https://freecallerregistry.com/fcr/).
- If the SIP `Reason` header includes a feedback URL, follow that link for any carrier-provided instructions about the rejected call.
- Enable [Branded Calling](https://support.telnyx.com/en/articles/15138152-making-calls-with-branded-calling) on the calling number.

#### Maintain Healthy Traffic Patterns

- Avoid sudden spikes in outbound call volume from new or low-history numbers.
- Avoid aggressive retry behavior after failed calls.
- Avoid rotating caller IDs to bypass reputation issues.
- Keep abandoned-call rates low.
- Use consent-based calling practices; if a recipient asks not to be called again, suppress that number from future outbound campaigns.
- For U.S. telemarketing traffic, review applicable [Do Not Call](http://donotcall.gov) requirements and [Telephone Consumer Protection Act](https://www.fcc.gov/sites/default/files/tcpa-rules.pdf) requirements.
- Warm up new numbers gradually with normal traffic.

### When to Contact Telnyx Support

Contact Telnyx Support if the guidance above has been followed and repeated `603+` rejections still occur. Include at least one recent example with:

- Date and time of each call, including timezone.
- Calling number.
- Destination number.

### What Telnyx Cannot Guarantee

Telnyx can help investigate and provide signaling evidence, but cannot guarantee that a terminating carrier or analytics provider will complete a call, remove a label, or clear a number's reputation. If a carrier or analytics provider blocks a call based on its own reputation or policy systems, remediation may require redress through that carrier, analytics vendor, or industry registration process.
