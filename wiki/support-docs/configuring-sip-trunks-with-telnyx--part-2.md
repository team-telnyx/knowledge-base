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

*Part 2 of 3 — see also: [Part 1](configuring-sip-trunks-with-telnyx--part-1.md), [Part 3](configuring-sip-trunks-with-telnyx--part-3.md)*

Step-by-step Telnyx support documentation for configuring SIP trunks between Telnyx and a range of third-party platforms, including OSDial, GOautodial (IP-based and credentials-based), Xorcom CompletePBX, PBXes, Wildix, and PhoneSuite Voiceware, plus an overview of HIPAA, BAAs, and the conduit exception as it applies to Telnyx.

## Xorcom CompletePBX

[Xorcom](https://www.xorcom.com/) designs and manufactures integrated business telephony solutions including IP PBX, Hotel Phone Systems, Virtual PBX, and Multi-tenant PBX. The following steps configure a SIP trunk in CompletePBX.

### Create the SIP trunk

1. From the left navigation bar, click **PBX > External > Trunks** and configure:

   **Technology**
   - **Technology:** *SIP*
   - **Description:** A description for this trunk
   - **Trunk CID:** CallerID Name in CAPITAL LETTERS, no special characters, max 15 characters. For US numbers, update the CNAM database via Telnyx support. Set **Overwrite CID:** *Always* if you want the Trunk CID to override extension/Outbound Route values.

   **Device for Outgoing Calls (Peer)**
   - **Outbound Username:** Your Telnyx username
   - **Host:** `sip.telnyx.com` (or `.ca`, `.au`, `.eu`)
   - **Port:** `5060`
   - **Remote Username:** Your Telnyx account username
   - **Remote Secret:** Your Telnyx account password
   - **From User:** Your Telnyx account username
   - **From Domain:** `sip.telnyx.com`
   - **Insecure:** *Port, Invite*
   - **Allow Inbound Calls:** *Yes*
   - **Qualify:** *Yes*

   **Register String**
   - **Use Default:** *Yes*

   ![CompletePBX configuration for SIP Trunk.](_images/ad56e5f98ae6fb00.png)
2. On the **Advanced** tab, set:
   - **Type:** *Peer*
   - **Parameter:** *sendrpid*
   - **Value:** *PAI*
   - **Enabled:** *On*

   ![XorCom advanced settings page.](_images/e0ff83fe0df2076f.png)

### Outbound route

1. Click **PBX > External > Outbound Routes** and configure:
   - **Description:** e.g. *TLS Calling Rule*
   - **Trunks:** Select the Telnyx trunk created above
   - **CID:** Company name in CAPITAL LETTERS, no special characters, max 15 characters
   - **Overwrite CID:** *Always* (trunk Overwrite CID must be set to *NEVER*)
   - **Prefix:** Optional, e.g. `9` (the prefix is not sent to Telnyx)
   - **Pattern:** e.g. `NXXNXXXXXX/1NXXNXXXXXX` for North American numbers

   ![Dial Patterns page.](_images/926e4f5dc1190f08.png)

   ![Dial pattern settings to set multiple matching patterns.](_images/5399a5869798b8c9.png)

### Inbound route

1. Click **PBX > External > Inbound Routes** and configure:
   - **Routing Method:** *Default*
   - **Description:** A description for the route
   - **DID Pattern:** Your DID number, excluding dots, parentheses, etc.
   - **Inbound Destination:** Destination to route the call when first answered

   ![A screenshot of a configured Xorcom CompletePBX to work with Telnyx.](_images/553cd723641f3246.png)

Each DID must be associated with an inbound route; multiple DIDs can share a route, but a single DID can only belong to one route.

Additional Xorcom resources:

- [CompletePBX 4.6 technical documentation](https://files.xorcom.com/techdocs/pm0618-completepbx-reference-guide.pdf)

## PBXes

[PBXes](https://www1.pbxes.com/iptel_virtuelle-telefonanlage.html) is a German PBX provider offering full operational service across installation, updates, and data backup. The PBXes website is in German; right-click and select **Translate to English** to read it in English.

### Add a SIP trunk

1. Log into pbxes.com and expand **Trunks > Add Trunk**, then click **Add SIP Trunk**.
2. In **General Settings**, provide:
   - **Trunk Name:** Any descriptive name
   - **Language:** Your language
   - **DTMF mode:** *Auto* or a specific configuration
   - **audio-bypass:** Your choice
   - **sendrpid:** *No*
3. In the **Account** section, provide:
   - **username:** Your Telnyx SIP account username
   - **password:** Your Telnyx SIP account password
   - **SIP server or proxy:** *sip.telnyx.com*
   - **domain:** *sip.telnyx.com*
   - **register:** *Yes (inbound and outbound calls)*

   ![PBXes online portal.](_images/91d34846a0763b4e.png)

### Inbound routing

1. Expand **Inbound Routing > Add Route**.
2. In **Options**, optionally set an Outbound Caller ID (CAPITAL LETTERS, no special characters, max 15 characters).
3. In **Dial Rules**, use the basic pattern `1+NXXNXXXXXX`.

   ![inbound routing dial rule section.](_images/490642a7d43514c6.png)

### Outbound routing

1. Expand **Outbound Routing > Add Route**.
2. In **Add Route**, set:
   - **Route Name:** e.g. *Telnyx_out*
   - **Trunk Sequence:** *SIP/Telnyx*
3. In **Set Destination**, set **Custom Dial Patterns:** *NXXNXXXXXX*.

   ![outbound routing dial rule section.](_images/b7ec3a8d02272793.png)

Additional PBXes resources:

- [PBXes premium account options](https://www1.pbxes.com/shop.php)
- [PBXes user documentation](https://www1.pbxes.com/community.php?display=wiki)
- [PBXes user forum](https://www1.pbxes.com/community.php?display=forum)

## Wildix

[Wildix](https://www.wildix.com/) provides a browser-based WebRTC VoIP PBX with presence, audio/video calls, conferencing, chat, fax, SMS, and desktop sharing.

### Basic SIP trunk settings

1. In the Wildix UI, go to **WMS > Trunks > Trunks** and click **+** under the SIP table.
2. On the **Basic Settings** tab, enter:
   - **Pricelist:**
   - **Title:** e.g. *Telnyx SIP trunk*
   - **Trunk name:** A descriptive name
   - **Auth login:** Your Telnyx SIP username
   - **From user:** Your Telnyx SIP username
   - **From domain:** Forced from domain header used in register and invite SIP messages
   - **Address or host name:** *sip.telnyx.com*
   - **Password:** Your Telnyx SIP password
   - **Dialplan:** Typically *main*
   - **Tone Zone:** Your country/region
   - **Country Code:** Country in which the trunk is being used
   - **Keep-Alive:** Enable periodic keep-alive messages
   - **Enable Registration:** Enable outgoing registration (enabled on the Client PBX SIP trunk, disabled on Server)
   - **Registration Proxy** (if enabled):
     - **Address or Host Name:** *sip.telnyx.com*
     - **Auth Login:** Your Telnyx SIP username
     - **Password:** Your Telnyx SIP password
     - **From user:** Your Telnyx SIP username

   ![Wildix portal section.](_images/5bc41697aa60be62.png)

### Advanced SIP trunk settings

Expand the **Advanced** section and configure:

- **Audio codecs:** `ulaw(g711u)`, `alaw(g711a)`, `g722`, `g729`
- **Video codecs:** H264 (if using video)
- **T38:** *Yes* (with maxdatagram parameters)
- **Session timer:** e.g. *min: 90, max: 600*
- **Registration expiry (sec):** *180*
- **UDP/TCP/TLS:** *UDP*
- **DTMF mode:** *RFC2833*

Additional Wildix resources:

- [Wildix licensing](https://www.wildix.com/product/licensing/)
- [Book a Wildix demo](https://www.wildix.com/try/)
- [Wildix technical documentation](https://wildix.atlassian.net/wiki/spaces)
- [Wildix custom config parameters](https://wildix.atlassian.net/wiki/spaces/DOC/pages/30285078/Custom+config+parameters+List)
