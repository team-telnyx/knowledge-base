---
title: Configuring Asterisk-Based PBX Systems with Telnyx SIP Trunking
summary: This page consolidates Telnyx guidance for connecting Asterisk-based PBX
  platforms — including bare Asterisk, FreePBX, and VitalPBX — to Telnyx SIP Trunking
  using either IP authentication or credentials-based authentication. It covers Mission
  Control Portal prerequisites, trunk configuration, PJSIP transport settings, dialplan/routing
  setup, and notes on FIPS-aligned cryptography for SIP Trunking.
sources:
- url: https://support.telnyx.com/en/articles/1130628-asterisk-configure-an-asterisk-ip-trunk
- url: https://support.telnyx.com/en/articles/1130676-configuring-an-asterisk-credentials-trunk
- url: https://support.telnyx.com/en/articles/15374685-telnyx-sip-trunking-fips-support
- url: https://support.telnyx.com/en/articles/5464056-setting-up-freepbx-v15-with-telnyx-api
- url: https://support.telnyx.com/en/articles/5754445-vitalpbx-configuring-your-vitalpbx
updated_at: 2026-08-05T13:28:37Z
---

# Configuring Asterisk-Based PBX Systems with Telnyx SIP Trunking

*Part 4 of 5 — see also: [Part 1](configuring-asterisk-based-pbx-systems-with-telnyx-sip-trunking--part-1.md), [Part 2](configuring-asterisk-based-pbx-systems-with-telnyx-sip-trunking--part-2.md), [Part 3](configuring-asterisk-based-pbx-systems-with-telnyx-sip-trunking--part-3.md), [Part 5](configuring-asterisk-based-pbx-systems-with-telnyx-sip-trunking--part-5.md)*

This page consolidates Telnyx guidance for connecting Asterisk-based PBX platforms — including bare Asterisk, FreePBX, and VitalPBX — to Telnyx SIP Trunking using either IP authentication or credentials-based authentication. It covers Mission Control Portal prerequisites, trunk configuration, PJSIP transport settings, dialplan/routing setup, and notes on FIPS-aligned cryptography for SIP Trunking.

## VitalPBX: Inbound Routes

1. In the left-hand menu, expand **Extensions** and select **Inbound Routes**, then provide:
   1. **Routing Method:** Either the Telephony channel for an analog port (FXO), or default for all other inbound routes like E1, T2, or SIP trunk. From version 2.3.8 onward, it is possible to route a DID range to an extension number. For example, with the DID range from 1 (305) 6724 7100 to 1 (305) 6724 7200, you can route the last four digits of the DID to the corresponding extension.
   2. **Description:** A brief description to identify this DID. This field is not parsed by VitalPBX.
   3. **DID Pattern:** The phone number of the DID to be matched. The [DID number](https://telnyx.com/resources/sip-did) must match the format in which the provider is sending the DID. Many providers send the DID as `+15555555555`, while others leave out the country code and send `5555555555`. If the DID entered does not exactly match the number sent by the provider, the inbound route will not be used. This field can be left blank to match calls from any DIDs. Patterns must begin with an underscore (`_`); within patterns, `X` matches 0–9 and specific numbers can be matched in square brackets (for example, `_555555123[45]`).
   4. **CID Pattern:** CID number or pattern to match. The CID must exactly match the format in which the provider is sending the CID. Providers may send 7, 10, or 11 digits; they may include a country code and the plus symbol. The field allows Private, Blocked, Unknown, Restricted, Anonymous, and Unavailable values. Leaving both DID Number and Caller ID Number blank creates a route that matches all calls.
   5. **Caller ID Modifier:** Modify the caller ID name/number.
   6. **CID Lookup:** Select a CID Lookup item to search the incoming caller number within a directory of a CRM or cloud directory.
   7. **Language:** Specifies the language for prompts on this route, provided the language is installed and voice prompts exist.
   8. **Music on Hold:** Select the music-on-hold for this route.
   9. **Alert Info:** Set a distinct ring for that inbound route.
   10. **Enable Recording:** Enable call recording on this route.
2. In the **Privacy Manager** section, configure:
   1. **Privacy Manager:** When enabled, incoming calls without an associated caller ID number will be prompted to enter their telephone number. Callers are given a number of attempts (defined in **Max attempts**) before being disconnected.
3. In the **Fax Settings** section, configure:
   1. **Fax Detection:** Determines whether faxes should be detected on this route. If enabled, additional parameters can be configured and a dropdown appears to select the extension to which inbound faxes will be directed. If disabled, fax calls are handled like voice calls.
4. In the **Destination** section, configure:
   - **Select Module:** Choose which module should be activated.
   - **Select Destination:** Call target where the module should be routed.

   ![Module and destination settings.](_images/a5410021c45ca0bf.png)

## Telnyx SIP Trunking FIPS Support

FIPS (Federal Information Processing Standards) are U.S. government standards for security and cryptography. Customers with government, defense, healthcare, financial services, or other regulated workloads may need their voice infrastructure to use FIPS-aligned cryptographic behavior.

Telnyx supports FIPS-140-2/FIPS-140-3 on its SIP Trunking proxy infrastructure. In SIP Trunking, FIPS primarily affects the cryptographic components used by the SIP proxy, including TLS negotiation and restrictions on non-approved cryptographic algorithms.

### How Telnyx Supports FIPS

Telnyx enables FIPS mode through OpenSSL on the Telephony Platform by default. The SIP proxy instances are configured to avoid cryptographic options that are not allowed under FIPS mode:

- TLS 1.1 and earlier are not allowed.
- CHACHA20-POLY1305 cipher suites are not negotiated.
- FIPS-compatible AES cipher suites remain available.
- Minimum cryptographic key-length requirements apply.

### SIP Proxy Software

The Kamailio-based SIP proxy runs on Debian Linux and uses the OpenSSL FIPS module, all with the latest versions as of June 2026. Kamailio does not require a separate SIP configuration change for FIPS mode, as it uses OpenSSL through its TLS module.

Customers who require exact platform version details for vendor review, procurement, audit, or security assessment should contact [Telnyx Support](mailto:support@telnyx.com).

> **Note:** Telnyx supports FIPS-aligned cryptography on supported SIP proxy infrastructure, but the Telnyx SIP Trunking service is not FIPS 140-2 or FIPS 140-3 certified.

### Customer Requirements

Customers using FIPS-enabled SIP Trunking infrastructure should ensure their SIP equipment supports compatible cryptographic settings, including:

- TLS 1.2 or later.
- FIPS-compatible cipher suites, such as AES-GCM or AES-CBC with HMAC cipher suites.
- Supported elliptic curves such as secp256r1. X25519 is not used in this configuration.

Customers should not require:

- TLS 1.1 or earlier.
- CHACHA20-POLY1305 cipher suites.
- SIP authentication behavior that depends on MD5 where a formal FIPS requirement applies.

### SIP Digest Authentication Limitation

FIPS support in the SIP proxy stack does not automatically make every part of SIP Trunking fully FIPS compliant. Traditional SIP Digest authentication can use MD5, and MD5 is not allowed for FIPS cryptographic use. The current FIPS proxy configuration addresses the proxy cryptographic stack, but it does not by itself replace SIP Digest authentication with a FIPS-approved alternative.

Customers with formal FIPS requirements should validate their end-to-end SIP configuration, including authentication behavior, customer equipment, TLS settings, and internal compliance controls.

### Verifying Compatibility

Customers can validate basic compatibility by confirming that their SIP equipment can establish SIP over TLS using TLS 1.2 or later with FIPS-compatible cipher suites.

If a SIP TLS connection fails after FIPS mode is enabled, check whether the customer device is attempting to use:

- An unsupported TLS version.
- A prohibited cipher suite.
- An unsupported elliptic curve.
- An incompatible cryptographic setting.

## Additional Resources

- [Get started with a Mission Control account](https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account)
- [Asterisk community help](https://community.asterisk.org/)
- [FreePBX support](https://www.freepbx.org/support/)
- [FreePBX documentation](https://wiki.freepbx.org/#all-updates)
- [VitalPBX user guide](https://wiki.vitalpbx.com/wiki-category/vitalpbx/)
- [VitalPBX manuals](https://www.vitalpbx.org/manuals/)
- [Does Telnyx encrypt communication](https://support.telnyx.com/en/articles/1130711-does-telnyx-encrypt-communication)
- [SIP connection number formats](https://support.telnyx.com/en/articles/1130706-sip-connection-number-formats)
- [Caller ID number policy](https://support.telnyx.com/en/articles/3546251-caller-id-number-policy)
