---
title: Telnyx SIP, Fax, and PBX Configuration
summary: This page consolidates Telnyx support documentation covering fax service
  setup and error handling (T.38 and G.711), Programmable Fax API webhook and CDR
  error codes, FreeSWITCH and FusionPBX trunk configuration, SIP Trunking FIPS support,
  and the meaning of SIP 603+ carrier rejections.
sources:
- url: https://support.telnyx.com/en/articles/1130672-fax-service-with-telnyx-via-t-38-or-g711
- url: https://support.telnyx.com/en/articles/15374685-telnyx-sip-trunking-fips-support
- url: https://support.telnyx.com/en/articles/15395095-understanding-sip-603-carrier-rejections
- url: https://support.telnyx.com/en/articles/1616935-freeswitch-ip-trunk-setup
- url: https://support.telnyx.com/en/articles/1618801-freeswitch-credentials-trunk
- url: https://support.telnyx.com/en/articles/3220393-fusionpbx-telnyx-credentials
- url: https://support.telnyx.com/en/articles/4967498-fax-api-error-list
- url: https://support.telnyx.com/en/collections/3968239-telnyx-fax-configuration-errors
updated_at: 2026-07-17T09:05:45Z
---

# Telnyx SIP, Fax, and PBX Configuration

*Part 4 of 5 — see also: [Part 1](telnyx-sip-fax-and-pbx-configuration--part-1.md), [Part 2](telnyx-sip-fax-and-pbx-configuration--part-2.md), [Part 3](telnyx-sip-fax-and-pbx-configuration--part-3.md), [Part 5](telnyx-sip-fax-and-pbx-configuration--part-5.md)*

This page consolidates Telnyx support documentation covering fax service setup and error handling (T.38 and G.711), Programmable Fax API webhook and CDR error codes, FreeSWITCH and FusionPBX trunk configuration, SIP Trunking FIPS support, and the meaning of SIP 603+ carrier rejections.

## SIP Trunking FIPS Support

FIPS (Federal Information Processing Standards) are U.S. government standards for security and cryptography. Customers with government, defense, healthcare, financial services, or other regulated workloads may require voice infrastructure with FIPS-aligned cryptographic behavior.

Telnyx supports FIPS 140-2/FIPS 140-3 on its SIP Trunking proxy infrastructure. In SIP Trunking, FIPS primarily affects the cryptographic components used by the SIP proxy, including TLS negotiation and restrictions on non-approved cryptographic algorithms.

### How Telnyx Supports FIPS

Telnyx enables FIPS mode through OpenSSL on the Telephony Platform by default. The SIP proxy instances are configured to avoid cryptographic options not allowed under FIPS mode:

- TLS 1.1 and earlier are not allowed.
- CHACHA20-POLY1305 cipher suites are not negotiated.
- FIPS-compatible AES cipher suites remain available.
- Minimum cryptographic key-length requirements apply.

### SIP Proxy Software

The Kamailio-based SIP proxy runs on Debian Linux and uses the OpenSSL FIPS module, all on current versions as of June 2026. Kamailio does not require a separate SIP configuration change for FIPS mode because it uses OpenSSL through its TLS module.

Customers who require exact platform version details for vendor review, procurement, audit, or security assessment should contact [Telnyx Support](mailto:support@telnyx.com).

Telnyx supports FIPS-aligned cryptography on supported SIP proxy infrastructure, but the Telnyx SIP Trunking service is not FIPS 140-2 or FIPS 140-3 certified.

### Customer Requirements

Customers using FIPS-enabled SIP Trunking infrastructure should ensure their SIP equipment supports compatible cryptographic settings:

- TLS 1.2 or later.
- FIPS-compatible cipher suites, such as AES-GCM or AES-CBC with HMAC cipher suites.
- Supported elliptic curves such as `secp256r1`. X25519 is not used in this configuration.

Customers should not require:

- TLS 1.1 or earlier.
- CHACHA20-POLY1305 cipher suites.
- SIP authentication behavior that depends on MD5 where a formal FIPS requirement applies.

### SIP Digest Authentication Limitation

FIPS support in the SIP proxy stack does not automatically make every part of SIP Trunking fully FIPS compliant. Traditional SIP Digest authentication can use MD5, which is not allowed for FIPS cryptographic use. The current FIPS proxy configuration addresses the proxy cryptographic stack but does not by itself replace SIP Digest authentication with a FIPS-approved alternative.

Customers with formal FIPS requirements should validate their end-to-end SIP configuration, including authentication behavior, customer equipment, TLS settings, and internal compliance controls.

### Scope

Telnyx FIPS support for SIP Trunking applies to supported SIP proxy infrastructure where FIPS mode is enabled. It does not mean that every component in every SIP call path is independently FIPS-certified, or that customer equipment automatically becomes FIPS-compliant by connecting to Telnyx.

### Verifying Compatibility

Validate basic compatibility by confirming that SIP equipment can establish SIP over TLS using TLS 1.2 or later with FIPS-compatible cipher suites. If a SIP TLS connection fails after FIPS mode is enabled, check whether the customer device is attempting to use:

- An unsupported TLS version.
- A prohibited cipher suite.
- An unsupported elliptic curve.
- An incompatible cryptographic setting.
