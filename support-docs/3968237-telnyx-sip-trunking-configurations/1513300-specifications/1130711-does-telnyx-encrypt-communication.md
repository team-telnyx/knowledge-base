---
source_url: https://support.telnyx.com/en/articles/1130711-does-telnyx-encrypt-communication
scraped: 2026-06-11
---

Does Telnyx encrypt communication? | Telnyx Help Center

[Skip to main content](#main-content)

# Does Telnyx encrypt communication?

Telnyx ensures secure calls with optional TLS signaling and SRTP media encryption.

Written by Telnyx Sales

January 29, 2026

Table of contents

# Does Telnyx encrypt communication?

By default, Telnyx does not encrypt calls. If your device supports TLS (Transport Layer Security) to encrypt signaling and SRTP to encrypt media, you can turn on these settings on your connection (see screenshots below) for end-to-end encryption.

Additionally, at Telnyx, we leverage our private network to pull your traffic off the public web and carry the media across our own fiber. By handling the media, we are able to ensure that your packets are exposed to as few public hops as possible.

For outbound calls, you can configure your device to use TLS and SRTP and make calls without further configuration on the Telnyx portal.

For inbound calls, you can enable TLS and SRTP in the [Connections page](https://portal.telnyx.com/#/voice/connections).

**Encrypting inbound signaling in the Telnyx portal:**  
On the Real-Time Communications tab, navigate to Voice -> SIP Trunking and to the Connection settings, and if IP/FQDN, you can encrypt the inbound signaling here:

[![](https://downloads.intercomcdn.com/i/o/ltcafuzd/2002284444/e7b53cb5d05ad0409d13c983346e/Screenshot+from+2026-01-28+21-55-22.png?expires=1781167500&signature=2fb959a62e7da761c0b64a2f5b7c7265ae99f4172165d357c8f0a4fd90fac885&req=diAnFMt2mYVbXfMW1HO4zRtVoSFaUewTVWR6PNkb9egoS%2BSxWbdQ9ncaOuCl%0ADamtNr2tQMqjAq9peiA%3D%0A)](https://downloads.intercomcdn.com/i/o/ltcafuzd/2002284444/e7b53cb5d05ad0409d13c983346e/Screenshot+from+2026-01-28+21-55-22.png?expires=1781167500&signature=2fb959a62e7da761c0b64a2f5b7c7265ae99f4172165d357c8f0a4fd90fac885&req=diAnFMt2mYVbXfMW1HO4zRtVoSFaUewTVWR6PNkb9egoS%2BSxWbdQ9ncaOuCl%0ADamtNr2tQMqjAq9peiA%3D%0A)

**Encrypting media in the Telnyx portal:**  
​  
In the same section as above:

[![](https://downloads.intercomcdn.com/i/o/ltcafuzd/2002372985/88e5af376e5f3d19747e62617a17/Screenshot+from+2026-01-28+22-28-36.png?expires=1781167500&signature=ea472a6f4ea5e453191d5807746b8f6e96bd4ee2918ed87a97dca9b967ffe6ae&req=diAnFMp5n4hXXPMW1HO4zX%2FzcSUgfd5mS1%2FCRK%2B7skM5CaijYzx4T%2BUbNpgM%0ATUUKV2%2BOiQdBsODGdfs%3D%0A)](https://downloads.intercomcdn.com/i/o/ltcafuzd/2002372985/88e5af376e5f3d19747e62617a17/Screenshot+from+2026-01-28+22-28-36.png?expires=1781167500&signature=ea472a6f4ea5e453191d5807746b8f6e96bd4ee2918ed87a97dca9b967ffe6ae&req=diAnFMp5n4hXXPMW1HO4zX%2FzcSUgfd5mS1%2FCRK%2B7skM5CaijYzx4T%2BUbNpgM%0ATUUKV2%2BOiQdBsODGdfs%3D%0A)

Read more about specific details of TLS [here](https://support.telnyx.com/en/articles/4404575-tls-and-srtp).

---

Related Articles

[Sansay: SBC VSXi Setup](https://support.telnyx.com/en/articles/4301888-sansay-sbc-vsxi-setup)[ScopTEL IP PBX](https://support.telnyx.com/en/articles/5803103-scoptel-ip-pbx)[Vtech VCS754: Telnyx Setup](https://support.telnyx.com/en/articles/5822901-vtech-vcs754-telnyx-setup)[MicroSIP: Setup with Telnyx](https://support.telnyx.com/en/articles/6133145-microsip-setup-with-telnyx)[BYOC: Telnyx & Genesys](https://support.telnyx.com/en/articles/8268122-byoc-telnyx-genesys)

Did this answer your question?

😞😐😃

Table of contents
