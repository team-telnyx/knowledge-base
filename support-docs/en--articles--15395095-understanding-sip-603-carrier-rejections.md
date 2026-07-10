---
source_url: https://support.telnyx.com/en/articles/15395095-understanding-sip-603-carrier-rejections
scraped: 2026-07-08
content_hash: ce6fad672c0115207c418a4a67dde28f35ff6f22f5c7ffe1f24497f85179375c
---

Understanding SIP 603+ carrier rejections | Telnyx Help Center

[Skip to main content](#main-content)

# Understanding SIP 603+ carrier rejections

Written by Telnyx Engineering

June 5, 2026

Table of contents

SIP 603+ is an industry shorthand for a standardized use of the SIP 603 Decline response when a call is blocked on an IP network based on reasonable analytics for outbound calls in the U.S. It is not a separate SIP status code, the status code remains 603.

The “+” indicates that the response includes additional standardized information, such as the *Network Blocked* reason phrase and related signaling details, to improve transparency and support redress.

In carrier voice networks, a SIP 603+ response may be generated when a terminating carrier, intermediate provider, downstream network, or call analytics provider determines that a call should be blocked before it reaches the intended recipient.

The FCC adopted SIP 603+ in FCC 25-15 as a standardized notification mechanism for IP calls blocked based on reasonable analytics. Rather than leaving callers to interpret a generic 603 Decline response, SIP 603+ is intended to clearly identify analytics-based network blocking and provide a more consistent framework for transparency, troubleshooting, and redress when legitimate calls are blocked in error.

This article explains what SIP 603+ means, how it differs from a standard SIP 603 Decline response, why carriers and analytics providers may return it, what information may be available in SIP signaling, and the steps organizations can take to reduce the likelihood that legitimate calls are blocked or labeled as unwanted.

## **What do SIP 603 and SIP 603+ mean?**

SIP response codes are three-digit codes. `603 Decline` is a SIP `6xx` global failure response, which means the call was rejected rather than temporarily unavailable or unanswered.

SIP 603+ is not a new numeric response code. Under FCC 25-15 and the ATIS-1000099 standard, 603+ refers to a standardized notification format for analytics-based blocking on IP networks. In practice, the SIP response uses status code `603` and the reason phrase `Network Blocked`, with additional standardized information intended to help callers identify analytics-based blocking and pursue redress when appropriate.

A `603 Decline` or 603+ formatted rejection does not mean Telnyx rejected the call. The source of the rejection is always the terminating carrier for the call.

## **Why these calls may be rejected or blocked by carriers**

Telnyx does not have visibility into the full decision logic used by terminating carriers, downstream providers, or analytics providers when they reject or block a call.

The clearest signal available may be the SIP response itself, including any SIP “603+” metadata or “Reason” header returned with the call.

The following are common factors that may contribute to carrier analytics or reputation-based blocking:

* The calling number has a poor or unknown reputation.
* Calls from the number are being labeled as spam, scam, or unwanted.
* The calling pattern looks suspicious, such as sudden high volume, repeated retries, short call duration, or low answer rates.
* The number is new and has little call history.
* The traffic pattern resembles robocalling or unsolicited outreach.
* The recipient, terminating carrier, or analytics provider has policy-based blocking enabled.

These are potential contributing factors, not a definitive explanation for any specific call.

The available SIP signaling, CDR fields, and call trace evidence should be used to determine what was actually returned for a given call.

## **How Telnyx surfaces the rejection**

When Telnyx receives a `SIP 603` response using the 603+ blocking format from a downstream or terminating carrier, Telnyx passes the downstream `603` response and its available blocking context toward your SIP trunking equipment as received from the downstream carrier.

A rejected call may include a SIP `Reason` header like this:

```
Reason: SIP;cause=603;text="v=analytics1;url=https://example.com";location=RLN
```

In this example:

* `cause=603` indicates the SIP failure cause.
* `text` includes

  + `v=analytics1`, identifying analytics-based blocking
  + at least one redress method such as `url`, tel, or `email`, which can be used to contact the terminating carrier to report invalid rejections.
  + `location` identifies where blocking occurred in the call path, using standardized values such as:

    - LN — originating network
    - TN — transit network
    - RLN — network serving the called party
    - LPN — originating private network
    - RPN — private network serving the called party

For SIP 603+-formatted rejections, Telnyx passes the downstream `603` response toward your SIP trunking equipment **without any modifications**.

Reason headers are useful diagnostic signals, but they are not always standardized across carriers. The exact fields and wording can vary.

## **How to reduce the chance of rejection**

Carrier analytics and reputation decisions are not controlled by Telnyx, but the following practices can help reduce false-positive blocking and improve call completion.

#### **Use appropriate caller ID**

* Avoid anonymous caller IDs.  
  ​
* Use numbers that you own and that are associated with your account as the number owner. This case will always result in STIR/SHAKEN A attestation which decreases the chances of the carrier blocking the call.  
  ​
* If you use a non-Telnyx caller ID that has been verified, it will result in STIR/SHAKEN B attestation, which increases the chances of the carrier blocking the call.

#### **Improve number identity and reputation**

* Configure accurate CNAM where applicable.
* Register legitimate outbound calling numbers and use cases with the [Free Caller Registry](https://freecallerregistry.com/fcr/).
* If the SIP `Reason` header includes a feedback URL, follow that link for any carrier-provided instructions about the rejected call.
* Enable [Branded Calling](https://support.telnyx.com/en/articles/15138152-making-calls-with-branded-calling) on your calling number.

#### **Maintain healthy traffic patterns**

* Avoid sudden spikes in outbound call volume from new or low-history numbers.
* Avoid aggressive retry behavior after failed calls.
* Avoid rotating caller IDs to bypass reputation issues.
* Keep abandoned-call rates low.
* Use consent-based calling practices, if a recipient asks not to be called again, the caller should suppress that number from future outbound campaigns.
* For U.S. telemarketing traffic, review applicable [Do Not Call](http://donotcall.gov) requirements and [Telephone Consumer Protection Act](https://www.fcc.gov/sites/default/files/tcpa-rules.pdf) requirements.
* Warm up new numbers gradually with normal traffic.

## **When to contact Telnyx Support**

Contact Telnyx Support if you have followed the guidance in this document and still see repeated `603+` rejections.

Include at least one recent examples when possible:

* Date and time of each call, including timezone
* Calling number
* Destination number

## **What Telnyx cannot guarantee**

Telnyx can help investigate and provide signaling evidence, but Telnyx cannot guarantee that a terminating carrier or analytics provider will complete a call, remove a label, or clear a number’s reputation.

If a carrier or analytics provider blocks a call based on its own reputation or policy systems, remediation may require redress through that carrier, analytics vendor, or industry registration process.

---

Related Articles

[Telnyx - How to Handle Spam Scam Likely](https://support.telnyx.com/en/articles/4088988-telnyx-how-to-handle-spam-scam-likely)[SIP Connection: Fail-over and Retries](https://support.telnyx.com/en/articles/4320364-sip-connection-fail-over-and-retries)[SIP Connection: Inbound & Outbound Settings](https://support.telnyx.com/en/articles/4404448-sip-connection-inbound-outbound-settings)[Telnyx SIP Response Codes](https://support.telnyx.com/en/articles/4409457-telnyx-sip-response-codes)[Understanding SIP PRACK Protocol](https://support.telnyx.com/en/articles/6902981-understanding-sip-prack-protocol)

Did this answer your question?

😞😐😃

Table of contents
