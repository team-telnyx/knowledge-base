---
title: PBX SIP Trunk Configuration with Telnyx
summary: Comprehensive guide for configuring SIP trunks between Telnyx and various
  open-source PBX platforms — including Asterisk, Vicidial, OSDial, FreeSWITCH, and
  FusionPBX — using either IP-based or credentials-based authentication.
sources:
- url: https://support.telnyx.com/en/articles/1130628-asterisk-configure-an-asterisk-ip-trunk
  content_hash: 3b217f8dcda4cc1ce92e979c87da493e275f46181a548436bafb888a7d4e6e9f
- url: https://support.telnyx.com/en/articles/1130632-configuring-a-vicidial-ip-trunk-with-telnyx
  content_hash: 571e092cc671b0ddd605cc1281e26d891dbd85c0d6033cefa49898d53fad873d
- url: https://support.telnyx.com/en/articles/1130636-configuring-an-ip-trunk-for-osdial
  content_hash: dfea424979422c26a7ec8400bf9e4d2b1045dd18b440b4801c1e125d85bf92df
- url: https://support.telnyx.com/en/articles/1130676-configuring-an-asterisk-credentials-trunk
  content_hash: 7cdea4830a2f059adcf4db9b5a3e8481185928acc9e2aa3616264dd74790a988
- url: https://support.telnyx.com/en/articles/1176353-vicidial-configure-vicidial-credentials
  content_hash: 142b9376b059e1523c0c1aafae30b5258a259e178de80247258eb56d134fd8df
- url: https://support.telnyx.com/en/articles/1616935-freeswitch-ip-trunk-setup
  content_hash: 19ac2b8bc5e75f97b93e2c0de29ff181b685f28a56ffa1b1c036774e7a195f89
- url: https://support.telnyx.com/en/articles/1618801-freeswitch-credentials-trunk
  content_hash: d2b04f8499ca8bd387a743c805e5d4aae159fa3771ac8a8fc509b304f68e3ad7
- url: https://support.telnyx.com/en/articles/3220393-fusionpbx-telnyx-credentials
  content_hash: 344b4a78795bcc1488a0ae24c40ba79931762e9987ca74be9d7ac992dc156524
updated_at: 2026-06-11T11:25:51Z
---

# PBX SIP Trunk Configuration with Telnyx

*Part 2 of 3 — see also: [Part 1](pbx-sip-trunk-configuration-with-telnyx-2--part-1.md), [Part 3](pbx-sip-trunk-configuration-with-telnyx-2--part-3.md)*

Comprehensive guide for configuring SIP trunks between Telnyx and various open-source PBX platforms — including Asterisk, Vicidial, OSDial, FreeSWITCH, and FusionPBX — using either IP-based or credentials-based authentication.

## OSDial

OSDial is a full-featured open-source predictive dialer. Its configuration is nearly identical to Vicidial's.

### IP-Based Trunk

In the OSDial web portal, go to **Admin → Carriers → Add new carrier** and enter:

| Field | Value |
|---|---|
| Carrier ID | Telnyx |
| Carrier Name | Telnyx |
| Registration String | *(leave blank)* |
| Template ID | None |
| Account Entry | Telnyx |
| Disallow | all |
| Allow | ulaw, G729 |
| Type | Peer |
| Insecure | port,invite |
| Host | sip.telnyx.com |
| DTMFMode | RFC 2833 |
| Context | default |
| Protocol | SIP |
| Global String | Telnyx=SIP/telnyx |

**Dial Plan:**

```
exten => _9NXXXXXXXXXX,1,AGI(agi://127.0.0.1:4577/call_log)
exten => _9NXXXXXXXXXX,2,Dial(${Telnyx}/${EXTEN:1},60,tTor)
exten => _9NXXXXXXXXXX,3,Hangup
```

Here, `9` is the dial prefix for the Telnyx trunk.

## FreeSWITCH

FreeSWITCH is a scalable, cross-platform telephony suite. FreeSWITCH v1.8 is end-of-life and must be upgraded before connecting to Telnyx.

### IP-Based Trunk

**Update default credentials:** Open `vars.xml` (typically in `/usr/local/freeswitch/conf/`) and change the default password:

```xml
<X-PRE-PROCESS cmd="set" data="default_password=YOUR_STRONG_PASSWORD"/>
```

**Update the external SIP profile:** In `sip_profiles/external.xml`, uncomment these lines:

```xml
<param name="ext-rtp-ip" value="$${external_rtp_ip}"/>
<param name="ext-sip-ip" value="$${external_sip_ip}"/>
```

**Create the SIP gateway:** Create a file at `sip_profiles/external/telnyx.xml`:

```xml
<include>
  <gateway name="telnyx">
    <param name="proxy" value="sip.telnyx.com"/>
    <param name="register" value="false"/>
    <param name="caller-id-in-from" value="true"/>
    <param name="username" value="not-used"/>
    <param name="password" value="not-used"/>
  </gateway>
</include>
```

**Create an outbound dialplan:** In `/usr/local/freeswitch/conf/dialplan/public/`, remove existing files and create a new XML dialplan. Example:

```xml
<include>
  <extension name="public_did">
    <condition field="destination_number" expression="^(1{0,1}\d{10})$">
      <action application="set" data="effective_caller_id_number=13125489677"/>
      <action application="bridge" data="sofia/gateway/telnyx/$1"/>
    </condition>
  </extension>

  <extension name="local.com">
    <condition field="destination_number" expression="^(\d{7})$">
      <action application="set" data="effective_caller_id_number=${outbound_caller_id_number}"/>
      <action application="set" data="effective_caller_id_name=${outbound_caller_id_name}"/>
      <action application="bridge" data="sofia/gateway/telnyx/+1${default_areacode}$1"/>
    </condition>
  </extension>

  <extension name="domestic.com">
    <condition field="destination_number" expression="^(\d{11})$">
      <action application="set" data="effective_caller_id_number=${outbound_caller_id_number}"/>
      <action application="set" data="effective_caller_id_name=${outbound_caller_id_name}"/>
      <action application="bridge" data="sofia/gateway/telnyx/+$1"/>
    </condition>
  </extension>

  <extension name="international.com">
    <condition field="destination_number" expression="^(011\d+)$">
      <action application="set" data="effective_caller_id_number=${outbound_caller_id_number}"/>
      <action application="set" data="effective_caller_id_name=${outbound_caller_id_name}"/>
      <action application="bridge" data="sofia/gateway/telnyx/+$1"/>
    </condition>
  </extension>
</include>
```

### Credentials-Based Trunk

**Extension configuration:** It is recommended to change the default password in `directory/default/1000.xml`:

```xml
<param name="password" value="abcd1234"/>
```

**Create the SIP gateway:** Create `sip_profiles/external/telnyx.xml`:

```xml
<include>
  <gateway name="telnyx">
    <param name="realm" value="sip.telnyx.com"/>
    <param name="username" value="freesuser"/>
    <param name="password" value="freespass"/>
    <param name="register" value="true"/>
  </gateway>
</include>
```

Replace `freesuser` and `freespass` with your Telnyx portal credentials.

**Note:** If you are using a Linksys device (SPA2102, SPA5xx series), you must set the RTP packet size (ptime) to 20ms (0.020) in the phone's configuration, as these devices reject calls with a ptime of 30ms.

**Outbound dialplan:** Edit `dialplan/default.xml`:

```xml
<extension name="dial">
  <condition field="destination_number" expression="^(1{0,1}\d{10})$">
    <action application="set" data="effective_caller_id_number=13125489677"/>
    <action application="bridge" data="sofia/gateway/telnyx/$1"/>
  </condition>
</extension>
```

**Inbound dialplan (DID):** Create a file at `dialplan/public/` named after your DID (e.g., `3125489677.xml`):

```xml
<include>
  <extension name="public_did">
    <condition field="destination_number" expression="^(13125489677)$">
      <action application="set" data="domain_name=$${domain}"/>
      <action application="transfer" data="1000 XML default"/>
    </condition>
  </extension>
</include>
```

Replace `13125489677` with the DID you purchased from Telnyx.

### FreeSWITCH Network Configuration

To use the same SIP profile for both internal and external communication, tell FreeSWITCH when to use the local IP versus the external IP. The `autonat:` prefix activates dynamic switching based on the local-network-acl:

```xml
<param name="ext-sip-ip" value="autonat:$${external_sip_ip}"/>
```

If FreeSWITCH fails to recognize your public IP, you can force a static public IP by modifying `sip_profiles/external.xml`:

```xml
<param name="ext-rtp-ip" value="8.8.8.8"/>
<param name="ext-sip-ip" value="8.8.8.8"/>
```

Replace `8.8.8.8` with your actual public IP address.
