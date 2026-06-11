---
title: Configure SIP phones with Telnyx (Grandstream, Gigaset, FortiFone, Flyingvoice)
summary: End‑to‑end guide to register popular IP phones to Telnyx using a credentials‑based
  SIP connection. Includes universal settings, codecs and DTMF, TLS/SRTP options,
  voicemail and caller ID tips, plus device‑specific field mappings for Grandstream
  GXV3370, Gigaset A510/A690/DX800a, FortiFone FON‑570/375/175/H25, and Flyingvoice.
sources:
- url: https://support.telnyx.com/en/articles/6187576-grandstream-gxv3370
- url: https://support.telnyx.com/en/articles/6167480-gigaset-configuring-the-gigaset-dx800a
- url: https://support.telnyx.com/en/articles/5815209-gigaset-a510-telnyx-setup
- url: https://support.telnyx.com/en/articles/6060646-gigaset-a690-as690
- url: https://support.telnyx.com/en/articles/5811545-fortifone-setup-fon-375-175-h25
- url: https://support.telnyx.com/en/articles/5810226-fortifone-fon-570
- url: https://support.telnyx.com/en/articles/5810663-flyingvoice-telnyx-setup
updated_at: 2026-05-20T15:09:08Z
---

# Configure SIP phones with Telnyx (Grandstream, Gigaset, FortiFone, Flyingvoice)

*Part 2 of 2 — see also: [Part 1](configure-sip-phones-with-telnyx-grandstream-gigaset-fortifone-flyingvoice--part-1.md)*

End‑to‑end guide to register popular IP phones to Telnyx using a credentials‑based SIP connection. Includes universal settings, codecs and DTMF, TLS/SRTP options, voicemail and caller ID tips, plus device‑specific field mappings for Grandstream GXV3370, Gigaset A510/A690/DX800a, FortiFone FON‑570/375/175/H25, and Flyingvoice.

## Gigaset routing, dialing, and STUN tips
- Number assignment (multi‑handset): Settings > Telephony > Number Assignment
  - Select your Telnyx connection for outgoing and incoming on each handset
- Dial plans (optional): Settings > Dialing Plans
  - Create emergency rule (e.g., 911) tied to your Telnyx connection and mark Active
- STUN: typically not required on Gigaset when using standard NAT; if you enable it, set STUN server to stun.telnyx.com:3478

## Verify and troubleshoot
- Registration status should display Registered/OK on the device.
- Place an outbound test call; confirm audio both ways. If one‑way audio occurs:
  - Prefer RTP over the default port range; ensure NAT/firewall permits SIP and RTP. If using SRTP/TLS, allow 5061 and SRTP ports.
  - Consider disabling STUN unless required, or align STUN with your NAT design.
- If calls fail to route:
  - Confirm the DID is provisioned to your Telnyx SIP connection and your Outbound Voice Profile is assigned.
  - Verify transport/port (UDP 5060 vs TLS 5061) matches both device and Telnyx.
  - Recheck registration expiry (try 300s) and credentials.
- Codec issues: enable G.711 (ulaw/alaw) and G.722; try disabling non‑essential codecs if negotiating fails.
- DTMF: set RFC2833 for IVR/DTMF reliability.

External references
- Grandstream GXV3370 admin guide: https://documentation.grandstream.com/knowledge-base/gxv3370-administration-guide/
- Gigaset A510IP user guide: https://gse.gigaset.com/fileadmin/legacy-assets/A31008-M2230-R301-2-6019_en_US_CA.pdf
- Gigaset A690/AS690 docs: https://gse.gigaset.com/fileadmin/gigaset/images/CustomerCare/Manuals/A6xx/A690IP-AS690IP/A31008-M2813-R601-1a-TE19_en_IM-East-INT.pdf
- Gigaset DX800a user manual: https://gse.gigaset.com/fileadmin/legacy-assets/Gigaset%20DX800A%20all%20in%20one_Web_en_GBR.pdf
- FortiFone documentation: https://www.fortinet.com/search?q=fortifone
- Flyingvoice downloads and docs: https://www.flyingvoice.com/download.html
