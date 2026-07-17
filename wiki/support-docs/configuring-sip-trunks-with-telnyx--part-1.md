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

*Part 1 of 3 — see also: [Part 2](configuring-sip-trunks-with-telnyx--part-2.md), [Part 3](configuring-sip-trunks-with-telnyx--part-3.md)*

Step-by-step Telnyx support documentation for configuring SIP trunks between Telnyx and a range of third-party platforms, including OSDial, GOautodial (IP-based and credentials-based), Xorcom CompletePBX, PBXes, Wildix, and PhoneSuite Voiceware, plus an overview of HIPAA, BAAs, and the conduit exception as it applies to Telnyx.

## Overview

This page consolidates Telnyx support documentation for configuring SIP trunks between Telnyx and a variety of third-party PBX, dialer, and contact-center platforms. Each section below covers a specific platform, the prerequisites for connecting it to Telnyx, and the step-by-step configuration required to make and receive calls.

Common prerequisites across most platforms include:

- A properly configured [Telnyx Mission Control Portal](telnyx-mission-control-portal.md) account
- A provisioned Telnyx DID assigned to a SIP connection
- An outbound voice profile
- A Telnyx SIP connection (IP-based or credentials-based, depending on the platform)
- TLS encryption is recommended where supported

The Telnyx SIP server hostname used in nearly every configuration is `sip.telnyx.com` (or `.ca`, `.au`, `.eu` depending on country). Telnyx supports the audio codecs `ulaw (g711u)`, `alaw (g711a)`, `g722`, and `g729`.

## OSDial

[OSDial](https://osdial.com/) is a full-featured open-source predictive dialer. To connect OSDial to Telnyx, log into the OSDial web portal and go to **Admin > Carriers > Add new carrier**, then provide the following values:

- **Carrier ID:** *Telnyx*
- **Carrier Name:** *Telnyx*
- **Registration String:** leave blank
- **Template ID:** None
- **Account Entry:** *Telnyx*
- **Disallow:** *all*
- **Allow:** *ulaw*
- **Allow:** *G 729*
- **Type:** *Peer*
- **Insecure:** *port,invite*
- **Host:** *sip.telnyx.com*
- **DTMFMode:** *RFC 2833*
- **Context:** *default*
- **Protocol:** *SIP*
- **Global String:** *Telnyx=SIP/telnyx*
- **Dial Plan:**

```
exten => _9NXXXXXXXXXX,1,AGI(agi://127.0.0.1:4577/call_log)
exten => _9NXXXXXXXXXX,2,Dial(${Telnyx}/${EXTEN:1},60,tTor)
exten => _9NXXXXXXXXXX,3,Hangup
```

In this dial plan, `9` is the prefix that must be dialed to send calls out through the Telnyx trunk.

Additional OSDial resources:

- [OSDial support](https://osdial.com/support/)
- [OSDial community](https://osdial.com/sitemap/)
- [Build an OSDial server](https://osdial.com/sitemap/)
- [OSDial training sessions](https://osdial.com/support/)

## GOautodial (IP-Based Trunk)

[GOautodial](https://goautodial.com/) is a free, enterprise-grade open-source omni-channel contact center system supporting predictive, preview, and manual dialing, plus inbound IVR and ACD. The IP-based trunk configuration authenticates by IP address rather than username/password.

### Configure the SIP trunk

1. In the GOautodial dashboard, expand **Settings** and click **Carriers**, then click the **+** to add a new carrier.

   ![The GOautodial dashboard page.](_images/d50821b09198a6d3.png)
2. Choose carrier type *Manual*.
3. In the Add New Carrier wizard, provide:
   - **Carrier ID:** *Telnyx*
   - **Carrier Name:** *Telnyx*
   - **Carrier Description:** e.g. *Telnyx Trunk*
   - **User Group:** *All User Groups*
   - **Authentication:** *IP-Based*
   - **SIP Server:** *sip.telnyx.com*
   - **Dial Prefix:** as required by your telephone system
   - **Codecs:** `ulaw(g711u)`, `alaw(g711a)`, `g722`, `g729`
   - **DTMF Mode:** *RFC2833*
   - **Protocol:** *SIP*
   - **Server IP:** see [IP authentication with X-Telnyx-Token](https://support.telnyx.com/en/articles/4860170-ip-authentication-with-x-telnyx-token)
   - **Active:** *Yes*

   ![The GOautodial dashboard page 2 for new carrier wizard.](_images/d92701b9bba8559f.png)

   ![The GOautodial dashboard page 2 for new carrier wizard.](_images/36f6ea82723682f9.png)

### Account entry and dial plan

Open **Advance Configuration** on the Carrier page and provide:

```
Account Entry: [telnyx]
disallow=all
allow=ulaw
allow=alaw
type=friend
dtmfmode=rtc2833
qualify=yes
nat=yes
host=sip.telnyx.com
insecure=invite
```

```
exten => _X.,1,AGI(agi://127.0.0.1:4577/call_log)
exten => _NXXNXXXXXX.,1,Dial(SIP/${EXTEN}@telnyx)
exten => _1NXXNXXXXXX.,1,Dial(SIP/${EXTEN}@telnyx)
exten => _6468688074,1,Dial(SIP/8001@default)
exten => _16468688074,1,Dial(SIP/8001@default)
```

### Outbound campaign

1. As an administrator, expand **Telephony** and click **Campaigns**.

   ![An administrator portal to set up an outbound campaign.](_images/e1fa11c180978e19.png)
2. Click **+** and choose **Campaign Type:** *Outbound*.

   ![An administrator portal to set up an outbound campaign 2.](_images/ba619d9db9a57b2b.png)
3. On the **Basic Settings** tab, set:
   - **Dial Method:** *Manual, Auto_Dial* or *Predictive*
   - **Auto Dial Level:** *Slow*, *Normal*, *Max*, or *High*
   - **Carrier to use for this Campaign:** *Telnyx*

   ![An administrator portal to set up an outbound campaign 3.](_images/90f8e9ae76b97002.png)
4. Click **Update**.

### Inbound campaign

1. Expand **Telephony** and click **Campaigns**, then click **+** and choose **Campaign Type:** *Inbound*.

   ![Administrator portal to set up an inbound campaign.](_images/e1fa11c180978e19.png)

   ![Administrator portal to set up an inbound campaign 4.](_images/ba619d9db9a57b2b.png)
2. In the **Campaign Wizard > Inbound**, set **Call Route:** *Ingroup (default)*.

   ![Campaign Wizard > Inbound sections.](_images/60e8e41df0a4d862.png)
3. On the **Basic Settings** tab, set **Carrier to use for this Campaign:** *Telnyx*.

   ![Advanced settings section.](_images/5521ce1fb1bc1aa6.png)
4. On the **Advanced Settings** tab, select the required **INBOUND GROUPS** and **Allowed Transfer Groups** (e.g. *AGENTDIRECT* and *AGENTDIRECT_CHAT*).

   ![Administrator portal to set up an inbound campaign in Advanced Settings.](_images/ca000b06f7b07d8a.png)

> **Note:** Agents must always select the ingroup on the **INBOUND CAMPAIGN** when they log in.

### Import call leads

1. Expand **Telephony** and click **List**, then click **+** to add a new list.

   ![Goautodial dashboard page to import your list of call leads.](_images/ff7872a473abe1c2.png)
2. Upload a `.csv` file in the required lead file format.

   ![Context menu in the Goautodial dashboard page.](_images/f0811ae42dc459d7.png)
3. Click **OK** once the upload completes.

   ![Goautodial dashboard page for lead status.](_images/696f76764395ae4a.png)

Additional GOautodial resources:

- [GOautodial documentation](https://goautodial.org/projects/goautodialce/wiki)
- [GOautodial forums](https://goautodial.org/projects/goautodialce/boards)
- [GOautodial github](https://goautodial.org/)
- [GOautodial system structure](https://goautodial.org/projects/goautodialce/wiki/GOautodial_System_Structure)
- [FAQ](https://goautodial.org/projects/goautodialce/wiki/FAQ)

## GOautodial (Credentials-Based SIP Trunk)

The credentials-based variant of the GOautodial trunk uses a Telnyx username and password instead of IP authentication. The setup mirrors the IP-based flow with these differences in the Add New Carrier wizard:

- **Authentication:** *Registration*
- **Username:** Your Telnyx account username
- **Password:** Your Telnyx account password
- **Server IP/Host:** *sip.telnyx.com*
- **Port:** *5060* (or *5061* if TLS is enabled)

![Add New Carrier wizard page on GOautodial portal.](_images/b8343a44a5d5924c.png)

![Goautodial DTMF entry point.](_images/36f6ea82723682f9.png)

The **Account Entry** and **Dialplan Entry** values, as well as the outbound/inbound campaign and lead import steps, are identical to the IP-based configuration above.
