---
source_url: https://support.telnyx.com/en/articles/15374685-telnyx-sip-trunking-fips-support
scraped: 2026-07-08
content_hash: 8e7f9b56993b8fe2606624e2f6c80b7f030957bfb427c068fb1fe2b9fa8ac7c1
---

Telnyx SIP Trunking FIPS Support | Telnyx Help Center

[Skip to main content](#main-content)

# Telnyx SIP Trunking FIPS Support

Written by Telnyx Engineering

June 4, 2026

Table of contents

## **Overview**

FIPS, or Federal Information Processing Standards, are U.S. government standards for security and cryptography. Customers with government, defense, healthcare, financial services, or other regulated workloads may need their voice infrastructure to use FIPS-aligned cryptographic behavior.

Telnyx supports FIPS-140-2/FIPS-140-3 on its SIP Trunking proxy infrastructure. In SIP Trunking, FIPS primarily affects the cryptographic components used by the SIP proxy, including TLS negotiation and restrictions on non-approved cryptographic algorithms.

---

## **How Telnyx supports FIPS**

Telnyx enables FIPS mode through OpenSSL on the Telephony Platform by default.

This means the SIP proxy instances are configured to avoid cryptographic options that are not allowed under FIPS mode.

For example:

* TLS 1.1 and earlier are not allowed.
* CHACHA20-POLY1305 cipher suites are not negotiated.
* FIPS-compatible AES cipher suites remain available.
* Minimum cryptographic key-length requirements apply.

---

## **SIP Proxy software**

At a high level, the Kamailio-based SIP proxy runs on Debian Linux and uses the OpenSSL FIPS module, all of them with latest versions as of June 2026.

Kamailio does not require a separate SIP configuration change for FIPS mode as it uses OpenSSL through its TLS module.  
​

Customers who require exact platform version details for vendor review, procurement, audit, or security assessment should contact Telnyx Technical Support for more information: [Telnyx Support](mailto:support@telnyx.com)  
​

**Note**: Telnyx supports FIPS-aligned cryptography on supported SIP proxy infrastructure, but the Telnyx SIP Trunking service is not FIPS 140-2 or FIPS 140-3 certified.

---

## **Customer requirements**

Customers using FIPS-enabled SIP Trunking infrastructure should ensure their SIP equipment supports compatible cryptographic settings, including:

* TLS 1.2 or later.
* FIPS-compatible cipher suites, such as AES-GCM or AES-CBC with HMAC cipher suites.
* Supported elliptic curves such as secp256r1. X25519 is not used in this configuration.

Customers should not require:

* TLS 1.1 or earlier.
* CHACHA20-POLY1305 cipher suites.
* SIP authentication behavior that depends on MD5 where a formal FIPS requirement applies.

---

## **Important limitation: SIP Digest authentication**

FIPS support in the SIP proxy stack does not automatically make every part of SIP Trunking fully FIPS compliant.  
​

A key limitation is SIP Digest authentication. Traditional SIP Digest authentication can use MD5, and MD5 is not allowed for FIPS cryptographic use.   
The current FIPS proxy configuration addresses the proxy cryptographic stack, but it does not by itself replace SIP Digest authentication with a FIPS-approved alternative.

Customers with formal FIPS requirements should validate their end-to-end SIP configuration, including authentication behavior, customer equipment, TLS settings, and internal compliance controls.

---

## **Scope**

Telnyx FIPS support for SIP Trunking applies to supported SIP proxy infrastructure where FIPS mode is enabled.

It does not mean that every component in every SIP call path is independently FIPS-certified, or that customer equipment automatically becomes FIPS-compliant by connecting to Telnyx.

---

## **How to verify compatibility**

Customers can validate basic compatibility by confirming that their SIP equipment can establish SIP over TLS using TLS 1.2 or later with FIPS-compatible cipher suites.

If a SIP TLS connection fails after FIPS mode is enabled, check whether the customer device is attempting to use:

* An unsupported TLS version.
* A prohibited cipher suite.
* An unsupported elliptic curve.
* An incompatible cryptographic setting.

---

## **Summary**

Telnyx supports FIPS mode for SIP Trunking on supported SIP proxy infrastructure. The implementation uses Telnyx-managed current platform components with the OpenSSL FIPS module.

This improves FIPS alignment for the SIP proxy cryptographic stack, while customers with formal FIPS obligations should still validate the full SIP path, especially SIP Digest authentication and customer-side equipment.

---

Related Articles

[Configuring Telnyx SIP Trunking with Avaya](https://support.telnyx.com/en/articles/1130695-configuring-telnyx-sip-trunking-with-avaya)[Wildix: SIP Trunk Setup](https://support.telnyx.com/en/articles/5799830-wildix-sip-trunk-setup)[Grandstream GRP260x: SIP Trunk](https://support.telnyx.com/en/articles/6169513-grandstream-grp260x-sip-trunk)[Grandstream GRP2612: SIP Trunk](https://support.telnyx.com/en/articles/6184147-grandstream-grp2612-sip-trunk)[Grandstream GXP1700: SIP Trunk](https://support.telnyx.com/en/articles/6184520-grandstream-gxp1700-sip-trunk)

Did this answer your question?

😞😐😃

Table of contents
