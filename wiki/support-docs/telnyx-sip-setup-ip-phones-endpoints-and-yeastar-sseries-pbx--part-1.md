---
title: 'Telnyx SIP setup: IP phones, endpoints, and Yeastar S‑Series PBX'
summary: A consolidated quick-start for configuring popular IP phones, specialty endpoints,
  and Yeastar S‑Series PBX with Telnyx. It highlights core Telnyx parameters (servers,
  ports, timers, codecs), caller ID rules, TLS/SRTP, and device-specific shortcuts
  for Yealink, Polycom, Cisco, AudioCodes, Algo, Alcatel, BuddyTalk, and Positron,
  plus Yeastar trunk/routing, star codes, dial plans, and troubleshooting tips.
sources:
- url: https://support.telnyx.com/en/articles/3074710-yealink-setup-with-telnyx
  content_hash: 6bd3fdf01af5c0046a02e18c34928eb87a6f1c6fcdc673d892590473d3c714e4
- url: https://support.telnyx.com/en/articles/5748952-yeastar-s-series-telnyx-sip
  content_hash: 8097dcf7d76d24b4e3bf670d895e79bc0edeccbf1a3df48b37a1097face8609f
- url: https://support.telnyx.com/en/articles/5619617-polycom-setup-with-telnyx
  content_hash: 4dde609c89f8f3fdf539c01bff8eb27664df5b8d4126f2a68809193d78aa221b
- url: https://support.telnyx.com/en/articles/5820309-cisco-68xx-88xx-setup
  content_hash: dfc83f4e304b931dbd33cf46203d0a52773c2131f424602ed1c72d36b6b6f086
- url: https://support.telnyx.com/en/articles/5724344-cisco-linksys-star-codes
  content_hash: 87d95bc34c050b8c414c2f78ebd45004e206a11c029b45e0c05e48a2a6cec4dd
- url: https://support.telnyx.com/en/articles/5721953-linksys-dialplan-for-linksys-atas
  content_hash: c9efcba2bda6a2dd8c951e38d195432299e5b93c48012ad988a913c3aefa4ac6
- url: https://support.telnyx.com/en/articles/5819923-audiocodes-400hd
  content_hash: 180199af0742da6a8339523d153a2e1d3671c9da1fafa474a71f2043cc250e8d
- url: https://support.telnyx.com/en/articles/5790092-algo-8xxx-telnyx-endpoints
  content_hash: 50d113609f9c0b38057ba419e2c9268248ad9b347a77526b43d9b41cccb5c76e
- url: https://support.telnyx.com/en/articles/6281943-alcatel-sd601-sd602-sip-door
  content_hash: 0eb872a1ec009e112693bb3bcffaee93ed382ce678d3c9e429600f86076d7857
- url: https://support.telnyx.com/en/articles/5808185-buddytalk-bt110-bt120
  content_hash: 6ebce0de39763da5552ae522fbc45a47c3a704ab762deb790e08f14536065b9e
- url: https://support.telnyx.com/en/articles/5811761-positron-ip-phone
  content_hash: 264194ffab910315173f2b03e9acaeb61bb7e93f315e166d1e0b5e7dd92c6549
updated_at: 2026-05-20T15:12:59Z
---

# Telnyx SIP setup: IP phones, endpoints, and Yeastar S‑Series PBX

*Part 1 of 2 — see also: [Part 2](telnyx-sip-setup-ip-phones-endpoints-and-yeastar-sseries-pbx--part-2.md)*

A consolidated quick-start for configuring popular IP phones, specialty endpoints, and Yeastar S‑Series PBX with Telnyx. It highlights core Telnyx parameters (servers, ports, timers, codecs), caller ID rules, TLS/SRTP, and device-specific shortcuts for Yealink, Polycom, Cisco, AudioCodes, Algo, Alcatel, BuddyTalk, and Positron, plus Yeastar trunk/routing, star codes, dial plans, and troubleshooting tips.

## Core prerequisites
- Create and configure your Telnyx Mission Control Portal account, then:
  - Buy a DID and assign it to a SIP Connection (credentials-based or IP-based)
  - Create an Outbound Voice Profile
  - Recommended: enable TLS if you plan to encrypt signaling and media
- Connect devices to a working network with Internet access (DHCP is fine unless you require static IP)
- Open necessary firewall paths (typically UDP/TCP 5060 for SIP; 5061 for SIP over TLS; associated RTP ranges per your environment)

## Telnyx essentials (use these across devices)
- SIP domain (proxy/registrar): sip.telnyx.com
- SIP ports:
  - 5060 for UDP/TCP
  - 5061 for TLS
- Registration/subscribe timers: 300 seconds is recommended
- NAT/keepalive: enable NAT mapping/keepalive; registrar keepalive around 50 seconds works well
- Codecs supported: G.711 µ‑law (ulaw), G.711 A‑law (alaw), G.722, G.729
- SRTP (when encrypted): AES‑128; many devices label this AES128 or AES_CM_128
- Voicemail callback (where applicable): *97

## Caller ID name conventions
- Use CAPITAL LETTERS for better legibility on some devices
- Avoid special characters; spaces are allowed
- Many Canadian providers show a maximum of 15 characters—shorten if needed
- Review the Telnyx caller ID number policy: https://support.telnyx.com/en/articles/3546251-caller-id-number-policy

## TLS/SRTP notes and certificate tip
- Set transport to TLS and SIP port to 5061; then enable SRTP (often “Required” or “SDES” depending on device)
- Some Cisco and other devices may need a trusted CA certificate. A commonly referenced chain: https://crt.sh/?id=1199354
- Algo 8301 requires uploading a client certificate/key as sipclient.pem to its certs store (see its Advanced Settings > File Manager)

## Registration timers, NAT, and reliability
- Set Register/Expires and Subscription Expires to 300 seconds
- Enable NAT Mapping / NAT Keep Alive (or “Registrar Keep Alive”) with a 50‑second period to keep bindings fresh on typical firewalls/NATs
- After changes, reboot or apply/save and wait for the device to show Registered before testing

## Yealink T Series (credentials-based)
- Access: find phone IP on the handset (Home/Menu > Status), browse to http://<phone IP>, default admin/admin
- Account > Account 1:
  - Activation: Enabled
  - Label/Display Name: your desired screen label/caller ID name (follow caller ID rules above)
  - Register Name / User Name: your Telnyx SIP username
  - Password: your Telnyx SIP password
  - Proxy/Server: sip.telnyx.com (port 5060 UDP or 5061 TLS)
- You can also provision via the keypad (Menu > Advanced > Accounts)

## Polycom VVX 300‑series
- Access: browse to https://<phone IP> (default password 456)
- Optional NTP: Simple Setup > Time Synchronization (e.g., north-america.pool.ntp.org)
- Settings > Lines (Line 1):
  - Identification: Display Name (caller ID), Address (Telnyx account/username), Label (line key text); SRTP set to No if not encrypting
  - Server 1: Address sip.telnyx.com, Port 5060 (UDP), Expires 300, Subscription Expires 300
  - Message Center: Callback Contact *97
- Restart the phone to apply

## Cisco 68xx/88xx (multiplatform)
- Access: http://<phone IP> (first login can often skip credentials)
- Voice > Extension tab:
  - General/NAT Settings: Line Enable Yes; NAT Mapping/Keep Alive Yes
  - SIP Settings: Transport UDP/TCP (or TLS if encrypting); SIP Port 5060 (5061 if TLS)
  - Proxy & Registration: Proxy and Outbound Proxy sip.telnyx.com; Register Yes; Register Expires 300
  - Subscriber Info: Display Name (caller ID), User ID/Auth ID (Telnyx username), Password (Telnyx password)
  - Audio: prioritize G.711u/alaw, G.722, G.729 as needed; if TLS/SRTP, Encryption Method AES128
- For TLS only: Voice > User > Secure Call Setting Yes; upload CA if required (Voice > Provisioning > Custom CA Rule with the certificate URL)

## AudioCodes 400HD
- Access: http://<phone IP> (admin/1234)
- Configuration > Quick Setup:
  - SIP Proxy and Registrar: Use SIP Proxy Enable; Proxy sip.telnyx.com; Port 5060 (or 5061 for TLS); “Use SIP Proxy IP and Port for Registration” Enable
  - Line Settings (Line 1): Display Name (caller ID), User ID/Auth User Name (Telnyx username), Authentication Password (Telnyx password)
- TLS/SRTP: Voice Over IP > Signaling Protocols: TLS transport, TLS port 5061; Voice Over IP > Media Streaming: SRTP Require Encryption, Method AES_CM_128, Negotiation Basic
- Keepalive/registration: Voice Over IP > Signaling Protocols: Enable Registrar Keep Alive; Period 50s; Registration Expires 300s
- Codecs: Voice Over IP > Media Streaming: order G.711u/alaw, G.722, G.729 as desired

## Algo 8xxx (paging, speakers, strobe, etc.)
- Access: browse to the device IP; Basic Settings > SIP:
  - SIP Domain (Proxy Server): sip.telnyx.com
  - Base/Page Extension, Authentication ID: Telnyx username
  - Authentication Password: Telnyx password
  - Display Name: caller ID name (required for outbound calling)
- Multiple functions (page/ring/emergency) need unique SIP credentials per extension
- Encryption (optional): Advanced Settings > Advanced SIP: Transport TLS; SDP SRTP Offer Standard (mandatory) or Optional (fallback to clear if peer lacks SRTP)
- Special case: Algo 8301 needs sipclient.pem client cert placed in certs folder for TLS
- Verify: Status > Device Status shows SIP Registration Successful
- Optional codec: Basic Settings > Features > G‑722 Support Enable

## Alcatel SD601/SD602 SIP door phones
- Access: press/hold # for IP announcement; browse to http://<IP> (admin/admin)
- SYSTEM > SIP Accounts:
  - Phone number: your Telnyx DID
  - Display name: caller ID name
  - Authentication Name/Password: Telnyx username/password
  - Activate: checked
  - SIP Proxy: sip.telnyx.com, Port 5060
- DHCP by default; a DSS long‑press sequence can toggle fixed IP if needed

## BuddyTalk BT110/BT120 (Alexa‑enabled speakerphones)
- In the BuddyTalk Setup App > Setup Telephony:
  - Name (caller ID; follow naming rules), Account ID/Auth ID (Telnyx username), Password, Domain sip.telnyx.com
  - Outbound proxy optional: sip.telnyx.com
  - Local SIP Port 5060; Preferred Transport UDP (or TLS if encrypting)
- After registration, the phone icon turns green; in the Web Console you can set Preferred Transport TLS and Secure RTP to SDES
- Alexa voice examples: “Alexa, call <number/name>”, “Alexa, answer call”, “Alexa, hang up”

## Positron IP phones (IP304/IP304C/IP408/IP410C/IP410G)
- Access: find IP via Menu > Status > Information; browse to http://<IP> (admin/admin). Change defaults afterward for security
- Web portal: Account > Basic
  - Account Active Yes; Primary SIP Server sip.telnyx.com
  - SIP Transport UDP (or TLS if encrypting)
  - SIP User ID / Authentication ID: Telnyx username; Authentication Password: Telnyx password
- On‑phone alternative: Menu > Settings > Advanced Settings > Accounts and enter identical values (Proxy optional)
- TLS certificates (optional): Management > TLS Certs upload
- Change default admin password: Menu > Settings > Advanced Settings > Password

## Yeastar S‑Series (Cloud PBX/S‑Series PBX)
- Register trunk (credentials‑based): Settings > PBX > Trunks > Add
  - Country: General; Trunk Type: Register Trunk
  - Hostname/IP and Domain: sip.telnyx.com
  - Username/Password: Telnyx credentials; Authentication Name (if required); From User: Telnyx username
  - If DID differs from auth name: Advanced > add DID(s) and optional DNIS labels
  - Save/Apply; PBX Monitor should show Registered
  - PBX > General > SIP: set Default Registration Time to 300
- Peer trunk (IP‑based): Trunk Type Peer Trunk; set Hostname/IP/Domain per Telnyx peering details; Save/Apply; verify status
- Outbound routing: Call Control > Outbound Routes > Add
  - Route name, Dial Patterns (e.g., prefix 8 then Strip 1), Member Extensions, Member Trunks (Telnyx)
- Inbound routing: Call Control > Inbound Routes > Add
  - Name, Member Trunks (Telnyx), Destination (extension/IVR/ring group, etc.)
