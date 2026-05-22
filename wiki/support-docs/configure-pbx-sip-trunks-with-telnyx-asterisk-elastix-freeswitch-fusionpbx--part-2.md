---
title: Configure PBX SIP Trunks with Telnyx (Asterisk, Elastix, FreeSWITCH, FusionPBX)
summary: End-to-end reference for configuring SIP trunks to Telnyx across popular
  open-source PBXs. Covers IP/FQDN and credentials-based trunks, core dialplans, NAT/media
  settings, and key UI steps for Asterisk (PJSIP), Elastix 4/5, FreeSWITCH, and FusionPBX.
sources:
- url: https://support.telnyx.com/en/articles/1130628-asterisk-configure-an-asterisk-ip-trunk
  content_hash: 3b217f8dcda4cc1ce92e979c87da493e275f46181a548436bafb888a7d4e6e9f
- url: https://support.telnyx.com/en/articles/1130676-configuring-an-asterisk-credentials-trunk
  content_hash: 7cdea4830a2f059adcf4db9b5a3e8481185928acc9e2aa3616264dd74790a988
- url: https://support.telnyx.com/en/articles/1130622-configuring-an-elastix-4-pbx-ip-trunk
  content_hash: 4c6826d06f469942d2b15aa3a549ec0526f0655caa97e98d0197c3307cadfdbf
- url: https://support.telnyx.com/en/articles/1130654-configuring-an-elastix-4-pbx-trunk
  content_hash: 2eb3c6221a7414a102b11246fae52db85fa1726a4d37a54d8762d1888499aa9d
- url: https://support.telnyx.com/en/articles/3284033-elastix-5-fqdn-trunk-setup
  content_hash: e6bc172f62a6c485ed9a3f2cf058975054143b9a85c4a7f67f70462eb43ef65f
- url: https://support.telnyx.com/en/articles/3284164-elastix-5-credentials-trunk
  content_hash: 72958bcb69aa49ab61586431ccfe0665ad1efeb5ca48466c02d634dfb62f1260
- url: https://support.telnyx.com/en/articles/1616935-freeswitch-ip-trunk-setup
  content_hash: 54f304f4ce582639e3240652718d0530e7e7193a6916d222976a23937db09950
- url: https://support.telnyx.com/en/articles/1618801-freeswitch-credentials-trunk
  content_hash: 888dffb21fcc96e834ae7296ea5259bbefe50c2a989d17799f99292e68bb2895
- url: https://support.telnyx.com/en/articles/3220393-fusionpbx-telnyx-credentials
  content_hash: 35b4ac6b35471383fade7b260ed27c26510d128abb1915bf31eb63c2cbe23a60
updated_at: 2026-05-20T14:55:25Z
---

# Configure PBX SIP Trunks with Telnyx (Asterisk, Elastix, FreeSWITCH, FusionPBX)

*Part 2 of 2 — see also: [Part 1](configure-pbx-sip-trunks-with-telnyx-asterisk-elastix-freeswitch-fusionpbx--part-1.md)*

End-to-end reference for configuring SIP trunks to Telnyx across popular open-source PBXs. Covers IP/FQDN and credentials-based trunks, core dialplans, NAT/media settings, and key UI steps for Asterisk (PJSIP), Elastix 4/5, FreeSWITCH, and FusionPBX.

## FreeSWITCH – Credentials trunk

Gateway (registration)
- File: conf/sip_profiles/external/telnyx.xml
```
<include>
  <gateway name="telnyx">
    <param name="realm" value="sip.telnyx.com"/>
    <param name="username" value="<your_username>"/>
    <param name="password" value="<your_password>"/>
    <param name="register" value="true"/>
  </gateway>
</include>
```

Outbound dial (conf/dialplan/default.xml)
```
<extension name="dial">
  <condition field="destination_number" expression="^(1{0,1}\d{10})$">
    <action application="set" data="effective_caller_id_number=13125489677"/>
    <action application="bridge" data="sofia/gateway/telnyx/$1"/>
  </condition>
</extension>
```

Inbound DID (conf/dialplan/public/13125489677.xml)
```
<include>
  <extension name="public_did">
    <condition field="destination_number" expression="^(13125489677)$">
      <action application="set" data="domain_name=$${domain}"/>
      <action application="transfer" data="1000 XML default"/>
    </condition>
  </extension>
</include>
```

Note: Some Linksys SPA devices require ptime 20 ms.

## FusionPBX – Credentials trunk

- After install, Accounts > Gateway:
  - Gateway: Telnyx
  - Username/Password: your Telnyx credentials
  - From User: your Telnyx username
  - From Domain: sip.telnyx.com
  - Proxy: sip.telnyx.com
  - Save and confirm registration.
- Create extensions (Accounts > Extensions). Optionally set Outbound Caller ID Number per extension.
- Inbound routing (Dialplan > Destinations): add your +E164 DID and route to an extension.
- Outbound routing (Dialplan > Outbound Routes):
  - Gateway: Telnyx; choose a regional dialplan expression (e.g., North America) and save.
- Register endpoints (Status > Registrations) with created extensions.

## DTMF, codecs, and media

- DTMF: Use RFC4733 (aka 2833). Elastix UI may label as RFC2833.
- Codecs: Prioritize G.711 (ulaw/alaw). G.729 and G.722 are commonly listed; ensure licensing/compatibility as needed.
- Asterisk PJSIP: enable rewrite_contact and force_rport for NAT; qualify as needed.
- Remove GSM-FR in Elastix 5 trunks; it’s not used with Telnyx.

## Security and best practices

- Change all default credentials (FreeSWITCH default_password, FusionPBX admin, Asterisk/phone passwords).
- Restrict allowed call destinations (e.g., country restrictions in Elastix/3CX) and apply least privilege.
- Keep PBX software updated; FreeSWITCH v1.8 is EOL.
- If sending CNAM: avoid special characters; many Canadian carriers limit to 15 chars; uppercase improves legibility. Review Telnyx caller ID policy: https://support.telnyx.com/en/articles/3546251-caller-id-number-policy

## Troubleshooting tips

- Registration vs IP trunk: Ensure your Telnyx connection type matches your PBX trunk (don’t attempt to register an IP-auth connection).
- DNS/targets: Use sip.telnyx.com or sip-anycast1.telnyx.com:5060 where appropriate.
- Number format: Send +E164 on outbound; configure inbound routes to match +E164.
- NAT: Set external_signaling/media addresses (Asterisk) or ext-sip-ip/ext-rtp-ip (FreeSWITCH). Confirm your Portal connection IP matches your public IP if using IP auth.
- Asterisk: Verify res_pjsip_config_wizard is loaded; pjsip set logger on can help trace.
- Tech prefix: If configured on IP connections, prepend it in the Asterisk dialplan.

## References

- Telnyx SIP Trunks: https://telnyx.com/products/sip-trunks
- Asterisk: https://www.asterisk.org/ and https://docs.asterisk.org/
- FreeSWITCH: https://signalwire.com/freeswitch and https://developer.signalwire.com/freeswitch/FreeSWITCH-Explained/
- Elastix/3CX docs: https://www.3cx.com/docs/manual/
- FusionPBX docs: https://docs.fusionpbx.com/en/latest/
