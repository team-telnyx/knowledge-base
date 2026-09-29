---
source_url: https://support.telnyx.com/en/articles/1130711-does-telnyx-encrypt-communication
title: "Does Telnyx encrypt communication?"
description: "Telnyx ensures secure calls with optional TLS signaling and SRTP media encryption. See Telnyx guidance and requirements."
scraped: 2026-07-08
content_hash: 51009604ff6492d1f0a3b80ad508788dee269986d8a2428d5745a494bd5b2a46
---







# Does Telnyx encrypt communication?

Telnyx ensures secure calls with optional TLS signaling and SRTP media encryption. See Telnyx guidance and requirements.




## Does Telnyx encrypt communication?

By default, Telnyx does not encrypt calls. If your device supports TLS (Transport Layer Security) to encrypt signaling and SRTP to encrypt media, you can turn on these settings on your connection (see screenshots below) for end-to-end encryption.

Additionally, at Telnyx, we leverage our private network to pull your traffic off the public web and carry the media across our own fiber. By handling the media, we are able to ensure that your packets are exposed to as few public hops as possible.

For outbound calls, you can configure your device to use TLS and SRTP and make calls without further configuration on the Telnyx portal.

For inbound calls, you can enable TLS and SRTP in the [Connections page](https://portal.telnyx.com/#/voice/connections).

**Encrypting inbound signaling in the Telnyx portal:**
On the Real-Time Communications tab, navigate to Voice -> SIP Trunking and to the Connection settings, and if IP/FQDN, you can encrypt the inbound signaling here:

![](_images/3cd951048a9333e3.png)

**Encrypting media in the Telnyx portal:**
​
In the same section as above:

![](_images/0cd5aa77a2df4bf2.png)

Read more about specific details of TLS [here](https://support.telnyx.com/en/articles/4404575-tls-and-srtp).
