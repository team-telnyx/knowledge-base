---
title: 'PBX/SBC SIP Trunking with Telnyx: Quick-start and Interop Recipes'
summary: A single, concise reference that unifies Telnyx-tested SIP trunk settings,
  NAT/security guidance, caller ID and dial plan tips, plus minimal working configs
  for popular PBXs and SBCs including Cisco CUBE/CUCM, Asterisk (PJSIP), FreeSWITCH,
  Avaya IP Office, Elastix 4, Vicidial/OSDial/GOautodial, Thirdlane, Skype for Business
  Server, and Yeastar P‑Series.
sources:
- url: https://support.telnyx.com/en/articles/1130606-configuring-a-cisco-cube-cucm-ip-trunk
- url: https://support.telnyx.com/en/articles/1130622-configuring-an-elastix-4-pbx-ip-trunk
- url: https://support.telnyx.com/en/articles/1130627-configuring-an-avaya-ip-trunk-with-telnyx
- url: https://support.telnyx.com/en/articles/1130628-asterisk-configure-an-asterisk-ip-trunk
- url: https://support.telnyx.com/en/articles/1130632-configuring-a-vicidial-ip-trunk-with-telnyx
- url: https://support.telnyx.com/en/articles/1130636-configuring-an-ip-trunk-for-osdial
- url: https://support.telnyx.com/en/articles/1130649-configuring-a-goautodial-pbx-ip-trunk
- url: https://support.telnyx.com/en/articles/1130654-configuring-an-elastix-4-pbx-trunk
- url: https://support.telnyx.com/en/articles/1130673-configuring-a-cisco-cube-cucm-sip-trunk
- url: https://support.telnyx.com/en/articles/1616935-freeswitch-ip-trunk-setup
- url: https://support.telnyx.com/en/articles/1130698-skype-set-up-skype-for-biz-sip-trunk
- url: https://support.telnyx.com/en/articles/1130695-configuring-telnyx-sip-trunking-with-avaya
- url: https://support.telnyx.com/en/articles/1130694-configuring-a-goautodial-pbx-sip-trunk
- url: https://support.telnyx.com/en/articles/1130631-how-to-configure-a-thirdlane-pbx
- url: https://support.telnyx.com/en/articles/13375115-how-to-configure-yeastar-p-series
updated_at: 2026-05-14T11:27:37Z
---

# PBX/SBC SIP Trunking with Telnyx: Quick-start and Interop Recipes

*Part 3 of 3 — see also: [Part 1](pbx-sbc-sip-trunking-with-telnyx-quick-start-and-interop-recipes--part-1.md), [Part 2](pbx-sbc-sip-trunking-with-telnyx-quick-start-and-interop-recipes--part-2.md)*

A single, concise reference that unifies Telnyx-tested SIP trunk settings, NAT/security guidance, caller ID and dial plan tips, plus minimal working configs for popular PBXs and SBCs including Cisco CUBE/CUCM, Asterisk (PJSIP), FreeSWITCH, Avaya IP Office, Elastix 4, Vicidial/OSDial/GOautodial, Thirdlane, Skype for Business Server, and Yeastar P‑Series.

## Verification and troubleshooting checklist
- Registration/Peer status is up (where applicable) and OPTIONS/qualify succeeds.
- Place an outbound call to a known good PSTN/mobile. Verify:
  - SDP/codec negotiated per plan (ulaw/alaw baseline); DTMF delivered via RFC2833.
  - Caller ID is valid or overridden per Connection policy.
- Receive an inbound call to your DID; ensure routing hits the intended extension/IVR.
- Behind NAT: confirm Contact/SDP show public IP (Asterisk/FreeSWITCH/CUBE rewrites in place).
- If using IP-auth with tech prefix, confirm it’s prepended in the outbound request URI.

## References
- Cisco CUBE/CUCM (IP/credentials): https://support.telnyx.com/en/articles/1130606-configuring-a-cisco-cube-cucm-ip-trunk and https://support.telnyx.com/en/articles/1130673-configuring-a-cisco-cube-cucm-sip-trunk
- Asterisk (PJSIP, IP-auth): https://support.telnyx.com/en/articles/1130628-asterisk-configure-an-asterisk-ip-trunk
- FreeSWITCH (IP trunk): https://support.telnyx.com/en/articles/1616935-freeswitch-ip-trunk-setup
- Avaya IP Office (overview) and Telnyx interop notes: https://support.telnyx.com/en/articles/1130627-configuring-an-avaya-ip-trunk-with-telnyx and https://ipofficekb.avaya.com/businesspartner/ipoffice/mergedProjects/appnotes/2022/Telnyx_IPO11.pdf
- Elastix 4 (IP and credentials): https://support.telnyx.com/en/articles/1130622-configuring-an-elastix-4-pbx-ip-trunk and https://support.telnyx.com/en/articles/1130654-configuring-an-elastix-4-pbx-trunk
- Vicidial: https://support.telnyx.com/en/articles/1130632-configuring-a-vicidial-ip-trunk-with-telnyx
- OSDial: https://support.telnyx.com/en/articles/1130636-configuring-an-ip-trunk-for-osdial
- GOautodial (IP and credentials): https://support.telnyx.com/en/articles/1130649-configuring-a-goautodial-pbx-ip-trunk and https://support.telnyx.com/en/articles/1130694-configuring-a-goautodial-pbx-sip-trunk
- Thirdlane PBX: https://support.telnyx.com/en/articles/1130631-how-to-configure-a-thirdlane-pbx
- Skype for Business Server: https://support.telnyx.com/en/articles/1130698-skype-set-up-skype-for-biz-sip-trunk
- Yeastar P‑Series: https://support.telnyx.com/en/articles/13375115-how-to-configure-yeastar-p-series
