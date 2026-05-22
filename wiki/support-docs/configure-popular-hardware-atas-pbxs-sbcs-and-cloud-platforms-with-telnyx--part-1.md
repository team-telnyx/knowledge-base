---
title: Configure popular hardware, ATAs, PBXs, SBCs, and cloud platforms with Telnyx
summary: A consolidated, field-proven setup guide that distills Telnyx best practices
  and device-specific steps for Cisco/Linksys SPA ATAs, Poly OBi300, Dinstar C60 phones,
  Mediatrix C7/4100 gateways, Synway UC‑200 PBX, UniFi Talk (credentials and IP auth),
  SBCs from Oracle, AudioCodes, Ribbon EdgeMarc, Sansay, and BYOC with Genesys Cloud.
sources:
- url: https://support.telnyx.com/en/articles/1130665-configuring-your-cisco-spa112-122-ata
  content_hash: c4325728624fcb8e04536b4e7c8049c6c59e57637f83950715702aba29e64746
- url: https://support.telnyx.com/en/articles/5733572-mediatrix-c7-4100-telnyx-setup
  content_hash: 3502e1dfc3ff7807260927643cc7df69868eda74eb078becb6993100818ab1fb
- url: https://support.telnyx.com/en/articles/5800399-synway-uc-200-telnyx-setup
  content_hash: f0c8d387b62d7159281ee84e30b6405e14416fb860a454fa65931f2e626aac3a
- url: https://support.telnyx.com/en/articles/5820183-plantronics-polycom-obi300-setup
  content_hash: bfc35c1dabfdf39c52b9d5d716c519223864f533dcb97322e9f6cb892335e132
- url: https://support.telnyx.com/en/articles/6128321-dinstar-c60-setup-config
  content_hash: de1f339304d492b274b24de066633eda330f163529c28d2fa3b30ee76b2154cf
- url: https://support.telnyx.com/en/articles/6122586-ubiquiti-trunk-unifi-talk-auth
  content_hash: 8c65d50a76c815c6f55be14f7cee494051006aa5ad4202a6cc448d32ab3a01ba
- url: https://support.telnyx.com/en/articles/6303467-ubiquiti-trunk-unifi-talk-ip-auth
  content_hash: 99f018c153b3358bf05400637cd0861f260a51326de291e52c65c578258be736
- url: https://support.telnyx.com/en/articles/4194697-oracle-acme-packet-sbc-setup
  content_hash: 918c23d032497661a47218cc726501110e4edfd3a93f35be1bc136c408ca2ad7
- url: https://support.telnyx.com/en/articles/4194841-audiocodes-sbc-setup
  content_hash: 490ed95c00bf064e8ce590a4d7e35ad57d8c518109754287eaeb21111ea7c4a5
- url: https://support.telnyx.com/en/articles/4215031-ribbon-edgemarc-6000-setup
  content_hash: e4be48e16b892d6cedaa7ab484e03799d0f4bcba6f8dad5308bf7a67cf4a58ae
- url: https://support.telnyx.com/en/articles/4301888-sansay-sbc-vsxi-setup
  content_hash: 3a6016736a376356454514de4c47f347cb91156c944aeca4bf6125c91913e378
- url: https://support.telnyx.com/en/articles/1130641-telnyx-recommended-hardware-configurations
  content_hash: bf7fd8f33557ad98ccc94e1aa81cd16197eaa2b8f369268639918b62203691fe
- url: https://support.telnyx.com/en/articles/8268122-byoc-telnyx-genesys
  content_hash: ccd7f016f119579449bee4575e7a976e4e734be1e3cebc275fe92752e14ecd28
updated_at: 2026-05-20T15:17:31Z
---

# Configure popular hardware, ATAs, PBXs, SBCs, and cloud platforms with Telnyx

*Part 1 of 2 — see also: [Part 2](configure-popular-hardware-atas-pbxs-sbcs-and-cloud-platforms-with-telnyx--part-2.md)*

A consolidated, field-proven setup guide that distills Telnyx best practices and device-specific steps for Cisco/Linksys SPA ATAs, Poly OBi300, Dinstar C60 phones, Mediatrix C7/4100 gateways, Synway UC‑200 PBX, UniFi Talk (credentials and IP auth), SBCs from Oracle, AudioCodes, Ribbon EdgeMarc, Sansay, and BYOC with Genesys Cloud.

## Overview and compatibility

If your hardware is SIP‑compatible and supports common codecs (G.711 µ‑law/a‑law, G.729, Opus), it will work with Telnyx. Keep device firmware current and confirm local network/DNS reachability before registering trunks or endpoints.

## Common Telnyx settings and best practices

- SIP proxy/domain: sip.telnyx.com (use regional variants where applicable). Signaling and media IPs per region are published here: https://sip.telnyx.com/#signaling-addresses and https://sip.telnyx.com/#media
- Ports and transport:
  - UDP/TCP: 5060
  - TLS: 5061 (enable TLS/SRTP where supported)
- Registration/expiry: 120–300 seconds are common values (typical examples: 120 or 300).
- NAT and STUN:
  - Behind NAT: enable NAT mapping/keepalive features.
  - STUN server: stun.telnyx.com (enable STUN/Test where offered).
- TLS/SRTP:
  - Use TLS transport 5061 and enable SRTP if supported.
  - Some devices (e.g., Cisco SPA112/122) require importing a CA cert to use TLS.
- Number formats:
  - Outbound: Telnyx accepts called numbers in 10, 11, or +E.164 (+11) formats.
  - Caller ID policy: send calling numbers in +E.164.
  - For some ATAs, route inbound by SIP username: in your Telnyx inbound connection, set Number Format (DNIS) to SIP Username so calls deliver to the ATA’s registered username.
- Codecs:
  - North America/Japan: prefer G.711 µ‑law; disable a‑law where advised.
  - Packetization (ptime): 20–30 ms typical.
- DTMF and star codes: configure DTMF maps/dial plans so feature/star codes (e.g., *97) pass correctly. See what DTMF is and how to configure it: https://support.telnyx.com/en/articles/1130710-what-is-dtmf
- RTP tuning (example for devices that expose settings): RTP packet size 20 ms; sample port range 10000–20000 if you need to pin media ports.
- “Display Name” caveat on some ATAs (Cisco SPA): older firmware could send it as the username; leave blank if registration fails and set Caller ID override in the Telnyx portal outbound settings.

## Device quick‑config recipes

### Cisco/Linksys SPA112/122 ATA
- Status: End‑of‑sale (Cisco EOL/EOS announced; basic support through 2025). Prefer Chrome/IE for config (Firefox issues reported).
- Telnyx portal: Inbound connection Number Format (DNIS) = SIP Username to route inbound to the ATA’s username.
- Voice > SIP (NAT): STUN Enable Yes; STUN Server stun.telnyx.com; STUN Test Yes.
- Quick Setup: Proxy sip.telnyx.com; User ID = Telnyx SIP username; Password = SIP password; Display Name blank if registration issues; Dial Plan per Linksys guidance: https://support.telnyx.com/en/articles/5721953-linksys-dialplan-for-linksys-atas
- Voice > Line 1: Line Enable Yes; SIP Port 5060 (or 5061 when using TLS); Register Expires 300; Use DNS SRV No; NAT Mapping/Keep Alive Yes when behind NAT; T.38 Fax Enable Yes if needed.
- Codecs: prefer G.711u or G.729.
- Audio optimization: SIP T1 = 1s; RTP Packet Size = 0.02; RTP Port Min/Max = 10000/20000.
- TLS/Secure calling: Supplementary Service Settings > Secure Call Setting Yes; SIP Transport TLS and Port 5061; import CA (Provisioning > CA Settings > Custom CA URL: https://crt.sh/?id=1199354). Secure‑call beep can be disabled under Voice > Regional > Call Progress Tones (clear Secure Call Indication Tone).

### Poly (Plantronics) OBi300 ATA
- Disable auto‑provisioning/OBiTALK (to avoid portal conflicts):
  - System Management > Auto Provisioning: disable Auto Firmware Update, ITSP Provisioning, OBiTALK Provisioning; Voice Services > OBiTALK Service: uncheck Enable.
- ITSP Profile > General: set Name; adjust DigitMap to your dialing plan (include local area code as needed).
- ITSP Profile > SIP: AuthUserName = Telnyx username; AuthPassword = password; Proxy/Registrar/Outbound Proxy ports 5060 (UDP/TCP) or 5061 (TLS); RegisterExpires 300.
- If using TLS: Voice Services > Service X: X_KeepAliveServerPort 5061; X_SRTP = Use SRTP Only.
- Codecs: ulaw (g711u), alaw (g711a), g722, g729 (order to preference).

### Dinstar C60 IP phone
- Obtain IP (OK > IPv4) and browse to it; default login admin/admin.
- Account > Basic Page:
  - Account: main or sub‑account ID; Active Enabled; Display Label/Name as desired (avoid special characters; keep under ~15 chars for some Canadian providers; use capitals for legibility).
  - Register Name/Username/Password = Telnyx SIP credentials.
- SIP Server: Server IP sip.telnyx.com; Port 5060; Registration Expires 120.

### Mediatrix C7/4100 gateway
- Network: ETH1/WAN uses DHCP; ETH2/LAN mgmt IP 192.168.1.2. Dial *#*0 on an attached phone to hear the IP.
- Default GUI login: username public, empty password.
- SIP > Servers: Registrar Host = sip.telnyx.com; Proxy Host = sip.telnyx.com; Apply, then Restart Required Services.
- SIP > Registrations: per FXS/port, set Username (Telnyx), Friendly Name, Register Enabled.
- SIP > Authentications: Edit All; Criteria Endpoint; Validate Realm Disabled; set Username/Password; Apply & Refresh Registration.
- Call Router > Auto‑routing: Enable; Criteria Type = SIP Username; verify routes in Call Router > Status.
- Codecs (NA/JP): Media > Codecs: disable G.711 a‑law; for G.711 µ‑law set ptime min 20 ms, max 30 ms.
- Telephony > DTMF Maps: add DTMF Map “*xx” with Transformation “x” for star codes.
- Optional SNTP: Network > Host: SNTP Configuration Source Static; Primary SNTP pool.ntp.org.

### Synway UC‑200 PBX
- Default login: admin/admin (change immediately).
- System > Network Settings: set Default interface LAN and LAN/DNS as needed.
- PBX > Trunks > Create Trunk: Type SIP; Transport UDP; Register Yes; Username/Password; Trunk IP/Domain sip.telnyx.com:5060; enable “Keep Inbound CallerID” if required.
- Outbound Routes: name, Dial/DID regex pattern; use Strip to remove access digits (e.g., 9) and Prepend for area code or country code; add Member Extensions and Member Gateways (the new trunk).
- Inbound Routes: name, DID pattern, Destination (e.g., extension/IVR), Member Trunks (Telnyx trunk).
- Test: dial extension 1000 (echo/call test) and verify CDR.

## SBC quick‑config recipes

### Oracle Acme Packet (ESBC)
- sip‑interface: realm (e.g., OUTSIDE); listen address/port 5060; transport UDP/TCP/TLS; allow‑anonymous agents‑only.
- session‑agent: hostname sip.telnyx.com; port 5060 (or 5061 for TLS); transport UDP/TCP/TLS; realm‑id OUTSIDE; allow‑next‑hop‑lp enabled.
- Number translation: ensure calling number is +E.164. Create a translation rule to add “+1” where needed and apply to the appropriate realm.
- Codec policy: prefer PCMU (G.711u) for client realms if targeting NA.

Reference: Oracle ESBC docs https://docs.oracle.com/cd/E95619_01/html/esbc_ecz810_configuration/

### AudioCodes SBC
- Define IP Group with SIPGroupName sip.telnyx.com.
- Proxy IPs: add Telnyx signaling IPs (example: 192.76.120.10:5060, 64.16.250.10:5060) per your region.
- Coders: G.711u (64k) ptime 20 ms. Add additional coders as needed for your environment.
- Note: configure IP profiles/routing/local policies to suit your topology.

### Ribbon EdgeMarc 6000
- VoIP > SIP: SIP Server Address sip.telnyx.com; Port 5060; Transport UDP; Use Custom Domain sip.telnyx.com; limit inbound/outbound to listed proxies.
- VoIP > SIP > B2BUA > Trunking Devices: add PBX as IP with transport UDP/TCP (or TLS 5061), port 5060/5061.
- B2BUA > Match rules: create default Inbound rule (Action Inbound) and Outbound rule (pattern on Calling as needed; Action Outbound); Update/Submit.

### Sansay VSXi
- Create two Resources (Inbound and Outbound), Protocol SIP, SIP profile for peering.
- General: Remote Port 5060; Service State inservice; Direction Both; Direct Media No; Group Policy Round Robin; appropriate timeouts and capacity/CPS limits.
- Codecs: enforce G.711u64k (add more if required).
- FQDNs: populate Telnyx signaling/media IPs for your region (https://sip.telnyx.com/#signaling-addresses, https://sip.telnyx.com/#media). Ensure caller ID is +E.164.
