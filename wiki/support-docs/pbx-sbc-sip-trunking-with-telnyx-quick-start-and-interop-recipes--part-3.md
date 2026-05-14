---
title: 'PBX/SBC SIP Trunking with Telnyx: Quick-start and Interop Recipes'
summary: A single, concise reference that unifies Telnyx-tested SIP trunk settings,
  NAT/security guidance, caller ID and dial plan tips, plus minimal working configs
  for popular PBXs and SBCs including Cisco CUBE/CUCM, Asterisk (PJSIP), FreeSWITCH,
  Avaya IP Office, Elastix 4, Vicidial/OSDial/GOautodial, Thirdlane, Skype for Business
  Server, and Yeastar P‑Series.
sources:
- url: https://support.telnyx.com/en/articles/1130606-configuring-a-cisco-cube-cucm-ip-trunk
  content_hash: 9f53070e318f4093db77f45d208a88ba442f8fc6b701289748e7f2d81bf11e1c
- url: https://support.telnyx.com/en/articles/1130622-configuring-an-elastix-4-pbx-ip-trunk
  content_hash: dded1de05c3838b03411e9aa62a1144cbda8a24987bf947d3808354093d97c11
- url: https://support.telnyx.com/en/articles/1130627-configuring-an-avaya-ip-trunk-with-telnyx
  content_hash: c6c5e5131bc60074f16759deefae79b98a1fcb8c1a915b63451194442070e61c
- url: https://support.telnyx.com/en/articles/1130628-asterisk-configure-an-asterisk-ip-trunk
  content_hash: 3b217f8dcda4cc1ce92e979c87da493e275f46181a548436bafb888a7d4e6e9f
- url: https://support.telnyx.com/en/articles/1130632-configuring-a-vicidial-ip-trunk-with-telnyx
  content_hash: 5decfe53ed448f801e5c00c5cc5c50eb60e28a09a62e721028c4fb31712a3130
- url: https://support.telnyx.com/en/articles/1130636-configuring-an-ip-trunk-for-osdial
  content_hash: dfea424979422c26a7ec8400bf9e4d2b1045dd18b440b4801c1e125d85bf92df
- url: https://support.telnyx.com/en/articles/1130649-configuring-a-goautodial-pbx-ip-trunk
  content_hash: fb6206633129388f28a46f38e7577136df001e4cd1c8f241453aa22af2ae7546
- url: https://support.telnyx.com/en/articles/1130654-configuring-an-elastix-4-pbx-trunk
  content_hash: 1c36db7486037b6bbefd0e463d6b43e43d8afacc512cba12ab452abf59112d61
- url: https://support.telnyx.com/en/articles/1130673-configuring-a-cisco-cube-cucm-sip-trunk
  content_hash: 3821a9503cf5d598ce4e3b201645f3ef0e525c14937189bd5fdc65c84b80eade
- url: https://support.telnyx.com/en/articles/1616935-freeswitch-ip-trunk-setup
  content_hash: 491050152de3c00b2555d6274b24f24f56489deec00b596e1874b81a6f3e4559
- url: https://support.telnyx.com/en/articles/1130698-skype-set-up-skype-for-biz-sip-trunk
  content_hash: 0dfe7f2b81bbf490e5e98ea38746a59589267cfa143edc01da3463aaf150281e
- url: https://support.telnyx.com/en/articles/1130695-configuring-telnyx-sip-trunking-with-avaya
  content_hash: 506da1ae0116580fc385b9c5b3b9bd94bafdcbba149cbf92e629668e4277ad37
- url: https://support.telnyx.com/en/articles/1130694-configuring-a-goautodial-pbx-sip-trunk
  content_hash: 94469eae51325a30cf2132a0359c4d9e81acd794edf94a66e65b0aa5fcc53f7b
- url: https://support.telnyx.com/en/articles/1130631-how-to-configure-a-thirdlane-pbx
  content_hash: 2fda58148c5886b060222b93e15b0cd1f68ba3ed50540a45090ed5b845aae24e
- url: https://support.telnyx.com/en/articles/13375115-how-to-configure-yeastar-p-series
  content_hash: 080d5dbc997c73bc8bd10c55ccff05485fdb594b6476223386102b3a27170f01
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
