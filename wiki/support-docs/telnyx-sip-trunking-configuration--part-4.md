---
title: Telnyx SIP Trunking Configuration
summary: A comprehensive guide to configuring and managing SIP trunking with Telnyx,
  covering connection types, authentication methods, inbound/outbound settings, failover
  and retry logic, SRV record handling, number formats, SIP protocols, STUN/TURN servers,
  SIP URI calling, response codes, and advanced features such as SHAKEN/STIR, PRACK,
  and Record-Route headers.
sources:
- url: https://support.telnyx.com/en/articles/10666839-how-telnyx-handles-srv-records-for-sip-calls
  content_hash: 5336b5985fa0913e7af2de79105b8bbbc1f3cbb846981d704a7ff0224d8a61aa
- url: https://support.telnyx.com/en/articles/1130682-telnyx-stun-and-turn-server
  content_hash: ba7ff5ec0ec7e77fd1c8912a6804912e1470dbc9bc937fd3b8d6558c2d8fb90b
- url: https://support.telnyx.com/en/articles/1130705-sip-protocols-that-telnyx-uses
  content_hash: 46cc3f3d1bcbc1eca17597a21e7696d3b43edc8dee1e78f5b051c30ee339c516
- url: https://support.telnyx.com/en/articles/1130706-sip-connection-number-formats
  content_hash: ef78abc67f49329534f7f4ada45772b5ab64bd91ac90625c16b047ab548f9fa6
- url: https://support.telnyx.com/en/articles/1130715-register-multiple-devices-on-one-connection
  content_hash: 6e5e7522f82c82f4e181a1d36ef99eb765ba03f0b6911e5b6bff44e80f4a84a0
- url: https://support.telnyx.com/en/articles/1130717-limits-on-concurrent-outbound-calls
  content_hash: 5922c4b3028b0d7fd9850e5cfd442f62ebe0e2557b35bde4290290f7759aeb90
- url: https://support.telnyx.com/en/articles/11358700-what-is-the-u-s-reassigned-numbers-database
  content_hash: 330252b32ac1fb45a47251b787e1bc0544cb49b895132f43194e7468710374bb
- url: https://support.telnyx.com/en/articles/1176364-sip-connection-failover-guide-ip-fqdn-based
  content_hash: b6ad5a6fbf819ec53aa61ad285c4320f020e9b60e9841c08c1a7583284fd3994
- url: https://support.telnyx.com/en/articles/2602782-ip-authentication-with-tech-prefix
  content_hash: 64dda14685cddc1fcb163aaa34f9f7d32e88737d67bd655691779e914542affb
- url: https://support.telnyx.com/en/articles/2925713-sip-uri-calling
  content_hash: 3cb9214746855254d83c27a4e329fbecf530bb91d79cda3d10bf43ba6f011ff7
- url: https://support.telnyx.com/en/articles/4245868-sip-connection-types
  content_hash: 121f24b961c0971bf305ae76944014f708745fe2ac15f08670909000bc4908eb
- url: https://support.telnyx.com/en/articles/4304898-sip-trunking-methods-requests-responses
  content_hash: e16cf3db090ad672d0669dc9c568db73a6dddc9d007b64b29a7b70d9edb922d4
- url: https://support.telnyx.com/en/articles/4320364-sip-connection-fail-over-and-retries
  content_hash: 36988aa18169e77583bc8d547d59584dddf444027ca86e1ffcb71ff4829349f4
- url: https://support.telnyx.com/en/articles/4351104-sip-connection-settings
  content_hash: 0b31f4e550f422c6fc2ea735848b1e17bb39b55248fd5718a784c214a0a03071
- url: https://support.telnyx.com/en/articles/4363904-sip-registration
  content_hash: 405244c50457a2e39cfe8e60b1db43961179f4bbc3028609415ef8c5eb0b498e
- url: https://support.telnyx.com/en/articles/4404448-sip-connection-inbound-outbound-settings
  content_hash: 13555768a2d461956c3844d32092859b8fef4a0134829a70ca40ceffb478513e
- url: https://support.telnyx.com/en/articles/4409457-telnyx-sip-response-codes
  content_hash: 51d1300c62f3c37573b8043d8169495ff6dec4168a2fa26a1fa421b37b517e20
- url: https://support.telnyx.com/en/articles/4860170-ip-authentication-with-x-telnyx-token
  content_hash: e5e100fcae875b6de79eb0856aa249445b813d50d3ccfdc70811011ad0f4a8da
- url: https://support.telnyx.com/en/articles/6169513-grandstream-grp260x-sip-trunk
  content_hash: ee2ab10a3b5059edd8c19cb6ca4c4e81c8cb94a40cf9a220b9a0ca41028ccb2f
- url: https://support.telnyx.com/en/articles/6902981-understanding-sip-prack-protocol
  content_hash: bb7aacbe5432b5ccb06087b93b7a52de14bdf49dc306bfecad67330620bd917f
- url: https://support.telnyx.com/en/articles/7029684-telephony-credentials-types
  content_hash: c3560f0e76972b8af4a3004d3ac523645b3b6e3798b3165ae14e029445c33b9d
- url: https://support.telnyx.com/en/articles/7421223-shaken-stir-parameters
  content_hash: c046bb41d844fe4c70629bd7afd01ab5819661455fb182a876a212d5a2607585
- url: https://support.telnyx.com/en/articles/8096455-how-to-configure-a-sip-trunk
  content_hash: 4440cdca8094dd344bcd02ba9cb8d2ded23ed9100c2aca3e64653cde9cfa27cc
- url: https://support.telnyx.com/en/articles/9133298-sip-record-route-headers
  content_hash: 81dfd46b008a8cd6c4683c97567afe552e35a2af269cd81a96901b3f0e0607f6
updated_at: 2026-06-11T11:25:41Z
---

# Telnyx SIP Trunking Configuration

*Part 4 of 4 — see also: [Part 1](telnyx-sip-trunking-configuration--part-1.md), [Part 2](telnyx-sip-trunking-configuration--part-2.md), [Part 3](telnyx-sip-trunking-configuration--part-3.md)*

A comprehensive guide to configuring and managing SIP trunking with Telnyx, covering connection types, authentication methods, inbound/outbound settings, failover and retry logic, SRV record handling, number formats, SIP protocols, STUN/TURN servers, SIP URI calling, response codes, and advanced features such as SHAKEN/STIR, PRACK, and Record-Route headers.

## U.S. Reassigned Numbers Database (RND)

The FCC-authorized RND tracks permanently disconnected U.S. phone numbers that may have been reassigned. Telnyx submits monthly reports of disconnected numbers (with a 15-day reclaim window before reporting).

### Querying the RND

Registered callers query a number with a date of last consent and receive:
- **Yes** — Number has been permanently disconnected since that date (likely reassigned).
- **No** — Number has not been disconnected (grants TCPA safe harbor).
- **No Data** — No record exists (no safe harbor applies).

### Who Must Use the RND

Any business making outbound calls/texts to U.S. numbers based on prior consumer consent — including contact centers, CPaaS providers, sales/marketing platforms, debt collectors, and auto-dialer operators. Failure to check can result in TCPA penalties of $500–$1,500 per call.

### Registering

1. Go to [reassigned.us](https://www.reassigned.us) and email [support@reassigned.us](mailto:support@reassigned.us) to request a login.
2. Choose a prepaid subscription tier (1–12 months) based on expected query volume.
3. The RND Administrator (SomosGov) will guide you through the process.

## Getting Started with SIP Trunking

1. **Create an account** at [telnyx.com/sign-up](https://telnyx.com/sign-up).
2. **Add funds** via the Mission Control portal.
3. **Purchase a phone number** from the [search section](https://portal.telnyx.com/#/voice/my-numbers/buy).
4. **Choose your system** — softphone (e.g., Zoiper, MicroSIP), PBX (e.g., FreePBX), CRM, or other compatible system.
5. **Configure your SIP Connection** — Go to Voice → SIP Trunking → Create SIP Connection. Choose your authentication method (Credentials, IP Address, or FQDN) and AnchorSite.
6. **Configure your Outbound Voice Profile** — Go to Outbound Voice Profiles → Add New Profile. Add a SIP Connection, set allowed destinations, and configure spend limits.
7. **Plug in your authentication details** to your chosen softphone, PBX, or system.
8. **Start calling and receiving calls.**
