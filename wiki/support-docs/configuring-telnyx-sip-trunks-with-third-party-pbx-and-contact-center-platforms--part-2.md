---
title: Configuring Telnyx SIP Trunks with Third-Party PBX and Contact Center Platforms
summary: This page consolidates Telnyx guidance for configuring SIP trunks between
  the Telnyx Mission Control Portal and a range of third-party PBX, dialer, and contact
  center platforms, including Avaya, Vicidial, OSDial, and GOautodial. It covers both
  IP-based and credentials-based authentication, dialplan setup, outbound and inbound
  campaign configuration, and lead import for contact center use cases, alongside
  notes on reseller support, call center service availability, Linksys ATA dialplan
  syntax, and the deprecation of the legacy Access Control List feature.
sources:
- url: https://support.telnyx.com/en/articles/1130627-configuring-an-avaya-ip-trunk-with-telnyx
- url: https://support.telnyx.com/en/articles/1130632-configuring-a-vicidial-ip-trunk-with-telnyx
- url: https://support.telnyx.com/en/articles/1130636-configuring-an-ip-trunk-for-osdial
- url: https://support.telnyx.com/en/articles/1130649-configuring-a-goautodial-pbx-ip-trunk
- url: https://support.telnyx.com/en/articles/1130655-can-i-resell-your-services
- url: https://support.telnyx.com/en/articles/1130667-do-you-offer-service-to-call-centers
- url: https://support.telnyx.com/en/articles/1130694-configuring-a-goautodial-pbx-sip-trunk
- url: https://support.telnyx.com/en/articles/1130695-configuring-telnyx-sip-trunking-with-avaya
- url: https://support.telnyx.com/en/articles/1176353-vicidial-configure-vicidial-credentials
- url: https://support.telnyx.com/en/articles/5721953-linksys-dialplan-for-linksys-atas
- url: https://support.telnyx.com/en/articles/5730689-access-control-list
updated_at: 2026-08-05T13:28:15Z
---

# Configuring Telnyx SIP Trunks with Third-Party PBX and Contact Center Platforms

*Part 2 of 4 — see also: [Part 1](configuring-telnyx-sip-trunks-with-third-party-pbx-and-contact-center-platforms--part-1.md), [Part 3](configuring-telnyx-sip-trunks-with-third-party-pbx-and-contact-center-platforms--part-3.md), [Part 4](configuring-telnyx-sip-trunks-with-third-party-pbx-and-contact-center-platforms--part-4.md)*

This page consolidates Telnyx guidance for configuring SIP trunks between the Telnyx Mission Control Portal and a range of third-party PBX, dialer, and contact center platforms, including Avaya, Vicidial, OSDial, and GOautodial. It covers both IP-based and credentials-based authentication, dialplan setup, outbound and inbound campaign configuration, and lead import for contact center use cases, alongside notes on reseller support, call center service availability, Linksys ATA dialplan syntax, and the deprecation of the legacy Access Control List feature.

## OSDial IP Trunk Configuration

OSDial is a popular full-featured predictive dialer that uses Open Source licenses to greatly reduce cost without sacrificing quality or functionality.

Log into the OSDial web portal and go to **Admin → Carriers → Add new carrier**, then provide the following information:

1. **Carrier ID:** *Telnyx*
2. **Carrier Name:** *Telnyx*
3. **Registration String:** leave blank
4. **Template ID:** None
5. **Account Entry:** *Telnyx*
6. **Disallow:** *all*
7. **Allow:** *ulaw*
8. **Allow:** *G 729*
9. **Type:** *Peer*
10. **Insecure:** *port,invite*
11. **Host:** *sip.telnyx.com*
12. **DTMFMode:** *RFC 2833*
13. **Context:** *default*
14. **Protocol:** *SIP*
15. **Global String:** *Telnyx=SIP/telnyx*
16. **Dial Plan:**
    ```
    exten => _9NXXXXXXXXXX,1,AGI(agi://127.0.0.1:4577/call_log)
    exten => _9NXXXXXXXXXX,2,Dial(${Telnyx}/${EXTEN:1},60,tTor)
    exten => _9NXXXXXXXXXX,3,Hangup
    ```
    In this case, 9 is the prefix that will be dialed to send calls to Telnyx's trunk.

Additional resources: [OSDial support](https://osdial.com/support/), [OSDial community](https://osdial.com/sitemap/), [Build an OSDial server](https://osdial.com/sitemap/), and [OSDial training sessions](https://osdial.com/support/).
