---
title: Configuring SIP Trunks with Telnyx
summary: Step-by-step Telnyx support documentation for configuring SIP trunks between
  Telnyx and a range of third-party platforms, including OSDial, GOautodial (IP-based
  and credentials-based), Xorcom CompletePBX, PBXes, Wildix, and PhoneSuite Voiceware,
  plus an overview of HIPAA, BAAs, and the conduit exception as it applies to Telnyx.
sources:
- url: https://support.telnyx.com/en/articles/1130636-configuring-an-ip-trunk-for-osdial
- url: https://support.telnyx.com/en/articles/1130649-configuring-a-goautodial-pbx-ip-trunk
- url: https://support.telnyx.com/en/articles/1130694-configuring-a-goautodial-pbx-sip-trunk
- url: https://support.telnyx.com/en/articles/3347891-hipaa-baas-and-the-conduit-exception
- url: https://support.telnyx.com/en/articles/5754127-xorcom-pbx-sip-trunk
- url: https://support.telnyx.com/en/articles/5798240-pbxes-connecting-a-pbxes-trunk-to-telnyx
- url: https://support.telnyx.com/en/articles/5799830-wildix-sip-trunk-setup
- url: https://support.telnyx.com/en/articles/5800936-phonesuite-voiceware
updated_at: 2026-07-17T09:04:18Z
---

# Configuring SIP Trunks with Telnyx

*Part 3 of 3 — see also: [Part 1](configuring-sip-trunks-with-telnyx--part-1.md), [Part 2](configuring-sip-trunks-with-telnyx--part-2.md)*

Step-by-step Telnyx support documentation for configuring SIP trunks between Telnyx and a range of third-party platforms, including OSDial, GOautodial (IP-based and credentials-based), Xorcom CompletePBX, PBXes, Wildix, and PhoneSuite Voiceware, plus an overview of HIPAA, BAAs, and the conduit exception as it applies to Telnyx.

## PhoneSuite Voiceware

[PhoneSuite](https://phonesuite.com/) provides hospitality-focused communications including the Voiceware software VoIP IP-PBX. Voiceware is scalable and flexible, with no need for expensive equipment or firmware upgrades.

### Configure the PBX

1. Open the PhoneSuite PBX Voiceware portal and click the **Advanced** tab. Set **DTMF Mode:** *Auto* (or update it in the Telnyx Mission Control Portal).

   ![PhoneSuite PBX Voiceware portal](_images/5c2a14d93577a0db.png)
2. Create a new SIP trunk with the following values:
   - **Type:** *SIP*
   - **Device Name:** Your device name
   - **Friendly Name:** e.g. *TelnyxTrunk*
   - **Secret:** Your Telnyx password
   - **Username:** Your Telnyx account number
   - **Insecure:** *Invite*
   - **Host:** *sip.telnyx.com*
   - **Port:** *5060*
   - **NAT:** Check this box
   - **Register?:** Check this box
   - **Audio Codecs:** Move `ulaw(g711u)`, `alaw(g711a)`, `g722`, `g729` from **Available** to **Allowed**
   - **Usable as Trunk:** Check this box
   - **Channels:** One channel per simultaneous call (see [What is a SIP trunk channel?](https://telnyx.com/resources/what-is-sip-trunk-channel))
   - **Credentials:** *Same as Above* (each channel may need its own credential)
   - **Reg. Username:** Your account number (same as the device name)
   - **Reg. Server:** *sip.telnyx.com*

   ![New SIP Trunk on the PhoneSuite PBX Voiceware portal.](_images/3821d4a45842ca21.png)

Additional PhoneSuite resources:

- [PhoneSuite inquiries](https://phonesuite.com/lets-get-started/)

## HIPAA, BAAs, and the Conduit Exception

The Health Insurance Portability & Accountability Act (HIPAA) governs the confidentiality and security of personal health information (PHI) within the United States for "covered entities" and their "business associates." HIPAA generally requires a covered entity to enter into a Business Associate Agreement (BAA) with third-party vendors that access, receive, transmit, or store PHI.

Some third-party vendors fall within the HIPAA **conduit exception** and are therefore not required to enter into a BAA. Telecommunications companies often fall within this exception. A BAA is not needed for an individual or organization that "acts merely as a conduit for protected health information, for example, the US Postal Service, certain private couriers, and their electronic equivalents." Temporarily storing PHI incident to a transmission does not disqualify such an individual or organization from the conduit exception. See [Department of Health and Human Services, 78 FR 5571-72](https://www.govinfo.gov/content/pkg/FR-2013-01-25/pdf/2013-01073.pdf).

In general, Telnyx's services fall within this conduit exception under HIPAA, and therefore there is no need for Telnyx to sign a BAA. Telnyx is happy to discuss further; contact [sales@telnyx.com](mailto:Sales@telnyx.com) with questions.

> *This is not, and is not a substitute for, obtaining legal advice.*

## Related Articles

- [Configuring an AVAYA IP trunk with Telnyx](configuring-an-avaya-ip-trunk-with-telnyx.md)
- [Asterisk: Configure an Asterisk IP trunk](asterisk-configure-an-asterisk-ip-trunk.md)
- [Configuring a Vicidial IP trunk with Telnyx](configuring-a-vicidial-ip-trunk-with-telnyx.md)
- [Configuring a GOautodial PBX IP Trunk](configuring-a-goautodial-pbx-ip-trunk.md)
- [Configuring a GoAutoDial PBX SIP Trunk](configuring-a-goautodial-pbx-sip-trunk.md)
- [Configuring an Elastix 4 PBX IP Trunk](configuring-an-elastix-4-pbx-ip-trunk.md)
- [Configuring an Elastix 4 PBX Trunk](configuring-an-elastix-4-pbx-trunk.md)
- [How to configure a Thirdlane PBX](how-to-configure-a-thirdlane-pbx.md)
- [Configuring Linphone with Telnyx](configuring-linphone-with-telnyx.md)
- [What is DTMF? and how to configure it on Telnyx](what-is-dtmf-and-how-to-configure-it-on-telnyx.md)
- [Port Request Rejected](port-request-rejected.md)
- [Managed Accounts](managed-accounts.md)
- [Toll-Free Messaging](toll-free-messaging.md)
- [FreePBX Trunk Settings With Telnyx](freepbx-trunk-settings-with-telnyx--part-1.md)
- [Configuring a FreePBX V13 Credentials Trunk](configuring-a-freepbx-v13-credentials-trunk.md)
- [Grandstream UCM6xxx: SIP Trunks](grandstream-ucm6xxx-sip-trunks.md)
- [Xorcom PBX: SIP Trunk](xorcom-pbx-sip-trunk.md)
- [BYOC: Telnyx & Genesys](byoc-telnyx-genesys.md)
- [Configuring a Cisco CUBE/CUCM SIP Trunk](configuring-a-cisco-cube-cucm-sip-trunk.md)
- [PhoneSuite Voiceware](phonesuite-voiceware.md)
- [Fanvil A32i: Telnyx Setup](fanvil-a32i-telnyx-setup.md)
- [ScopTEL IP PBX](scoptel-ip-pbx.md)
- [Grandstream GXV3370](grandstream-gxv3370.md)
- [Fanvil H2U: Compact IP](fanvil-h2u-compact-ip.md)
- [Yeastar S-Series: Telnyx SIP](yeastar-s-series-telnyx-sip.md)
- [How to configure Yeastar P-series](how-to-configure-yeastar-p-series.md)
