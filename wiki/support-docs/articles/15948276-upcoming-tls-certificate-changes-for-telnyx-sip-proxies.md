---
title: "Upcoming TLS Certificate Changes for Telnyx SIP Proxies"
summary: "During the remainder of 2026, we’ll be updating the TLS certificates used by our primary SIP proxy servers."
sources:
- url: "https://support.telnyx.com/en/articles/15948276-upcoming-tls-certificate-changes-for-telnyx-sip-proxies"
updated_at: 2026-09-15T00:00:00Z
tags: [support-docs]
source_path: "support-docs/15948276-upcoming-tls-certificate-changes-for-telnyx-sip-proxies.md"
generated_by: incremental-support-docs-wiki
---
<!-- generated_from=support-docs/15948276-upcoming-tls-certificate-changes-for-telnyx-sip-proxies.md -->

# Upcoming TLS Certificate Changes for Telnyx SIP Proxies

During the remainder of **2026**, we’ll be updating the TLS certificates used by our primary SIP proxy servers.

## **Planned Schedule**

|  |  |
| --- | --- |
| **Region** | **Planned migration** |
| Canada (sip.telnyx.ca) | September 4th 2026, 09:00 - 12:00 UTC |
| Australia (sip.telnyx.com.au) | September 4th 2026, 09:00 - 12:00 UTC |
| Europe (sip.telnyx.eu) | November 12th 2026, 17:00 - 19:00 UTC |
| United States (sip.telnyx.com) | November 13th 2026, 09:00 - 12:00 UTC |

This notification applies to customers using **SIP signaling** (including SIP Trunking and Programmable Voice SIP connections).

Media (RTP/SRTP) is **not** affected.

Other SIP regions already have these changes and don’t need to be upgraded at this time.

Most customers **do not need to take any action**.

The information below only applies if you manually manage trusted certificates on your SBC, PBX, gateway, desk phones, or other SIP devices, or if you use mutual TLS (mTLS).

We have two important changes to note.

## **1. Certificate Authority Migration to Let’s Encrypt**

The current certificates are issued by either **Sectigo** or **Digicert**, but we’re changing to **Let’s Encrypt**.

This is important for customers who use an SBC (or other appliance) and have our certificate (or the CA certificate) loaded into the SBC.

It may also apply to customers who use TLS with desk phones and have the certificate loaded there.

If this applies to you, please load all four **Let’s Encrypt ISRG root CA certificates** into your device(s) in preparation.

They’re available for download here:

<https://letsencrypt.org/certificates/>

When downloading these certificates, please install the **self-signed** versions of the ISRG root certificates, **not** the cross-signed versions.

We recommend installing all four current ISRG root certificates:

- ISRG Root X1
- ISRG Root X2
- ISRG Root YE
- ISRG Root YR

If it’s not possible to load all four, then please at least load the **ISRG Root X1** certificate.

As long as it remains practical (which we expect to be for at least the next one to two years), we’ll present a certificate chain that terminates at **ISRG Root X1** to maximize compatibility with existing deployments (including older or legacy clients).

## **2. Removal of the clientAuth EKU**

The **clientAuth Extended Key Usage (EKU)** is being deprecated, in line with changes to CA/Browser Forum standards.

Our new server certificates (and future certificates) for each proxy server won’t include this EKU.

This may affect devices that use **mutual TLS (mTLS)** with our proxy servers and reject TLS connections if the peer certificate does not contain the **clientAuth** EKU.

If you use mTLS, please configure your device or SBC so that it does **not** require the **clientAuth** EKU during inbound TLS certificate validation.

This will help prevent TLS handshake failures and ensure a seamless transition.

## **Impact**

If your deployment is affected by either of the changes above, it may impact both **inbound and outbound SIP signaling**, including calls established over TLS.

Customers who rely on the operating system’s default trusted certificate store and do not use mTLS are generally **not expected to require any changes**.

## **Future Certificate Renewal Notifications**

As certificate lifetimes continue to decrease, particularly as 47-day certificates become standard, we’ll continue to send Status Page notifications whenever:

- the trusted root CA changes,
- customer action is required, or
- another significant TLS compatibility change is planned.

Routine server certificate renewals and intermediate CA certificate changes that don’t require customer action will occur without prior notification.

## **Frequently Asked Questions**

**Do I need to take any action?**

Most customers do **not** need to take any action. If your systems use the operating system’s default trusted certificate store and you do not use mutual TLS (mTLS), no changes are expected to be required.

**Who needs to take action?**

You may need to update your configuration if you:

- Manually manage trusted certificates on your SBC, PBX, gateway, or SIP devices.
- Use mutual TLS (mTLS) for SIP signaling.

**What do I need to do if I manually manage trusted certificates?**

Install the current self-signed Let’s Encrypt ISRG root certificates on your devices before your region’s migration. If you cannot install all four, install at least **ISRG Root X1**.

**What do I need to do if I use mTLS?**

Update your device or SBC configuration so it does not require the clientAuth Extended Key Usage (EKU) in the server certificate during TLS validation.

**Will this affect media (RTP/SRTP)?**

No. These changes only affect SIP signaling over TLS. Media traffic is not impacted.

**What could happen if I don’t make the required changes?**

If your deployment is affected and the required updates are not made, SIP registrations, inbound calls, outbound calls, or other SIP signaling over TLS may fail after the migration.

**Can I test these changes before the migration?**

Yes. If you would like to validate your TLS configuration ahead of your region’s migration, you can test against our staging SIP proxy:

*sipstaging.telnyx.com*

This can help you verify that your deployment trusts the new certificate chain and that TLS connections are established successfully before the production migration.

**Where can I download the required Let’s Encrypt root certificates?**

The current self-signed Let’s Encrypt ISRG root certificates can be downloaded from the official Let’s Encrypt certificates page:

*<https://letsencrypt.org/certificates/>*

Please install the **self-signed** versions of the certificates, not the cross-signed versions.

**Why is Telnyx making these changes?**

These updates align with broader industry standards for public TLS certificates and are not specific to Telnyx.

- The removal of the **clientAuth Extended Key Usage (EKU)** follows changes adopted by public Certificate Authorities. Learn more from [Let’s Encrypt](https://letsencrypt.org/2025/05/14/ending-tls-client-authentication/)
- Public TLS certificate lifetimes are also being reduced across the industry, with a phased transition to **47-day certificates** as approved by the [CA/Browser Forum](https://cabforum.org/2025/04/11/ballot-sc081v3-introduce-schedule-of-reducing-validity-and-data-reuse-periods/).

---

Related Articles

- [Algo 8xxx: Telnyx Endpoints](https://support.telnyx.com/en/articles/5790092-algo-8xxx-telnyx-endpoints)
- [Voice Elements: Telnyx SIP](https://support.telnyx.com/en/articles/6145484-voice-elements-telnyx-sip)
- [Fanvil X1/X1P: IP Phone](https://support.telnyx.com/en/articles/6206533-fanvil-x1-x1p-ip-phone)
- [Mitel: 6800/6900 SIP](https://support.telnyx.com/en/articles/6249691-mitel-6800-6900-sip)
- [Telnyx SIP Trunking FIPS Support](https://support.telnyx.com/en/articles/15374685-telnyx-sip-trunking-fips-support)
