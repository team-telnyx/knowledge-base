---
title: Telnyx SIP Trunking Configuration
summary: Telnyx SIP Trunking lets you use Telnyx as your inbound and outbound voice
  carrier with a compatible softphone, PBX, or contact center platform. This page
  consolidates the core configuration workflow (account setup, number purchase, SIP
  connection, authentication method, AnchorSite, and Outbound Voice Profile), explains
  the ~1–3 second configuration propagation window, and provides step-by-step integration
  guides for Avaya IP Office and Vicidial (both IP-based and credentials-based), along
  with pointers to the broader library of vendor configuration guides.
sources:
- url: https://support.telnyx.com/en/articles/1130627-configuring-an-avaya-ip-trunk-with-telnyx
- url: https://support.telnyx.com/en/articles/1130632-configuring-a-vicidial-ip-trunk-with-telnyx
- url: https://support.telnyx.com/en/articles/1130667-do-you-offer-service-to-call-centers
- url: https://support.telnyx.com/en/articles/1130695-configuring-telnyx-sip-trunking-with-avaya
- url: https://support.telnyx.com/en/articles/1130713-what-is-my-sip-account-connection-password
- url: https://support.telnyx.com/en/articles/1176353-vicidial-configure-vicidial-credentials
- url: https://support.telnyx.com/en/articles/12901901-understanding-configuration-propagation-delays-in-mission-control-portal-and-api
- url: https://support.telnyx.com/en/articles/8096455-how-to-configure-a-sip-trunk
- url: https://support.telnyx.com/en/collections/3968237-telnyx-sip-trunking-configurations
updated_at: 2026-07-17T09:03:27Z
---

# Telnyx SIP Trunking Configuration

*Part 3 of 3 — see also: [Part 1](telnyx-sip-trunking-configuration--part-1.md), [Part 2](telnyx-sip-trunking-configuration--part-2.md)*

Telnyx SIP Trunking lets you use Telnyx as your inbound and outbound voice carrier with a compatible softphone, PBX, or contact center platform. This page consolidates the core configuration workflow (account setup, number purchase, SIP connection, authentication method, AnchorSite, and Outbound Voice Profile), explains the ~1–3 second configuration propagation window, and provides step-by-step integration guides for Avaya IP Office and Vicidial (both IP-based and credentials-based), along with pointers to the broader library of vendor configuration guides.

## Additional Configuration Guides and Resources

Telnyx maintains a large library of vendor-specific configuration guides. Highlights include:

- **3CX** — [3CX Configurations with Telnyx](https://support.telnyx.com/en/collections/1512990-3cx-configurations-with-telnyx)
- **Asterisk** — [Asterisk Trunk Configuration Guides](https://support.telnyx.com/en/collections/1892172-asterisk-trunk-configuration-guides) (Credentials Trunk and IP trunk)
- **Avaya** — [Avaya SIP Trunk with Telnyx Setup](https://support.telnyx.com/en/collections/1513009-avaya-sip-trunk-with-telnyx-setup)
- **Cisco** — [Cisco SIP Trunk & Setup Guide](https://support.telnyx.com/en/collections/1513000-cisco-sip-trunk-setup-guide) (CME, CUBE, CUCM, SPA112/122)
- **FreePBX** — [FreePBX Setup & Configuration](https://support.telnyx.com/en/collections/1512996-freepbx-setup-configuration)
- **FreeSWITCH** — [FreeSWITCH Trunk Configurations](https://support.telnyx.com/en/collections/1513006-freeswitch-trunk-configurations)
- **GoAutoDial** — [GoAutoDial SIP Trunk Configurations](https://support.telnyx.com/en/collections/1513012-goautodial-sip-trunk-configurations)
- **Grandstream** — [Grandstream Devices & Telnyx Setup](https://support.telnyx.com/en/collections/1513008-grandstream-devices-telnyx-setup)
- **Linphone** — [Linphone Configuration with Telnyx](https://support.telnyx.com/en/collections/3249281-linphone-configuration-with-telnyx)
- **Microsoft Teams** — [Microsoft Teams](https://support.telnyx.com/en/collections/3421382-microsoft-teams) (Call2Teams, TLS & SIP warnings)
- **Vicidial** — [Vicidial Trunk Setups with Telnyx](https://support.telnyx.com/en/collections/1513007-vicidial-trunk-setups-with-telnyx)
- **Yealink & Yeastar** — [Yealink & Yeastar Telnyx Setup](https://support.telnyx.com/en/collections/1892168-yealink-yeastar-telnyx-setup)
- **Zoiper** — [Zoiper Configurations with Telnyx](https://support.telnyx.com/en/collections/1892167-zoiper-configurations-with-telnyx)

For general SIP information (response codes, PRACK protocol, caller ID policy, and more), see [Everything SIP](https://support.telnyx.com/en/collections/2484718-everything-sip). For technical specifications (whitelisting, SIP protocols, STUN server, DTMF, encryption), see [Specifications](https://support.telnyx.com/en/collections/1513300-specifications).

## Support

If you get stuck on any step, Telnyx offers 24/7 world-class support by phone at +1 888-980-9750 ext 2, by email at [support@telnyx.com](mailto:support@telnyx.com), or via chat by logging into your Mission Control Portal account. Feedback and integration requests can be sent to [community@telnyx.com](mailto:community@telnyx.com).
