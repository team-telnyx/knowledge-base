---
title: Telnyx SIP Trunking Configuration
summary: A comprehensive guide to configuring and managing SIP trunking with Telnyx,
  covering connection types, authentication methods, inbound/outbound settings, failover
  and retry logic, SRV record handling, number formats, SIP protocols, STUN/TURN servers,
  SIP URI calling, response codes, and advanced features such as SHAKEN/STIR, PRACK,
  and Record-Route headers.
sources:
- url: https://support.telnyx.com/en/articles/10666839-how-telnyx-handles-srv-records-for-sip-calls
- url: https://support.telnyx.com/en/articles/1130682-telnyx-stun-and-turn-server
- url: https://support.telnyx.com/en/articles/1130705-sip-protocols-that-telnyx-uses
- url: https://support.telnyx.com/en/articles/1130706-sip-connection-number-formats
- url: https://support.telnyx.com/en/articles/1130715-register-multiple-devices-on-one-connection
- url: https://support.telnyx.com/en/articles/1130717-limits-on-concurrent-outbound-calls
- url: https://support.telnyx.com/en/articles/11358700-what-is-the-u-s-reassigned-numbers-database
- url: https://support.telnyx.com/en/articles/1176364-sip-connection-failover-guide-ip-fqdn-based
- url: https://support.telnyx.com/en/articles/2602782-ip-authentication-with-tech-prefix
- url: https://support.telnyx.com/en/articles/2925713-sip-uri-calling
- url: https://support.telnyx.com/en/articles/4245868-sip-connection-types
- url: https://support.telnyx.com/en/articles/4304898-sip-trunking-methods-requests-responses
- url: https://support.telnyx.com/en/articles/4320364-sip-connection-fail-over-and-retries
- url: https://support.telnyx.com/en/articles/4351104-sip-connection-settings
- url: https://support.telnyx.com/en/articles/4363904-sip-registration
- url: https://support.telnyx.com/en/articles/4404448-sip-connection-inbound-outbound-settings
- url: https://support.telnyx.com/en/articles/4409457-telnyx-sip-response-codes
- url: https://support.telnyx.com/en/articles/4860170-ip-authentication-with-x-telnyx-token
- url: https://support.telnyx.com/en/articles/6169513-grandstream-grp260x-sip-trunk
- url: https://support.telnyx.com/en/articles/6902981-understanding-sip-prack-protocol
- url: https://support.telnyx.com/en/articles/7029684-telephony-credentials-types
- url: https://support.telnyx.com/en/articles/7421223-shaken-stir-parameters
- url: https://support.telnyx.com/en/articles/8096455-how-to-configure-a-sip-trunk
- url: https://support.telnyx.com/en/articles/9133298-sip-record-route-headers
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
