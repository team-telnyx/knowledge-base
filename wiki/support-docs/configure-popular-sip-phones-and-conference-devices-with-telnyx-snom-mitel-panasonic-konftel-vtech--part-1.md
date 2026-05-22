---
title: Configure Popular SIP Phones and Conference Devices with Telnyx (Snom, Mitel,
  Panasonic, Konftel, VTech)
summary: A consolidated guide to register and secure popular SIP desk and conference
  phones with Telnyx, including Snom C520/D7xx/M100 KLE, Mitel 5320e/5330e/5340e and
  6800/6900, Panasonic KX-TGP 550 and KX‑HDV, Konftel 300Wx and 300IPx, and VTech
  VCS754.
sources:
- url: https://support.telnyx.com/en/articles/5815678-snom-c520-telnyx-setup
  content_hash: 75646789e7e67e4f7651f4605f8a17e73e1e0900c476afeb6c54d617cabb0a81
- url: https://support.telnyx.com/en/articles/5822706-snom-d7xx-telnyx-setup
  content_hash: 60621609e8e76ff10958b51baeca7977dee94a7dcb128d851c2c28997433b769
- url: https://support.telnyx.com/en/articles/5822823-snom-m100-kle-telnyx-setup
  content_hash: 4ddfcb00aaa75db844aa4d929b20063e4e533db128fab1f2dfd32e45730e52d0
- url: https://support.telnyx.com/en/articles/6244551-mitel-5320e-5330e-5340e-sip
  content_hash: 34d9f2aa29af158b48afb3106a695794bae839a0f108802fa1a744be5d498eff
- url: https://support.telnyx.com/en/articles/6249691-mitel-6800-6900-sip
  content_hash: dc8bed8636a3a31bb30b16f23eb273a5b64ad82977918eb6a901159f098333ed
- url: https://support.telnyx.com/en/articles/5807663-panasonic-kx-tgp-550
  content_hash: 1d878fa381b0d731ad7ccc2cdd136a855809ca306a898b9067c3a24e7f93a519
- url: https://support.telnyx.com/en/articles/5814406-panasonic-kx-hdv-telnyx-setup
  content_hash: c9f60161e3540f8faa9c127a80759f73f5f5910f46d7d0d8072010a3b83fea07
- url: https://support.telnyx.com/en/articles/5807979-konftel-300wx-telnyx-setup
  content_hash: ee9ad29b8d22624f13d9b9f8f41b4844ed0e1939a28a580f423d301e8a491a19
- url: https://support.telnyx.com/en/articles/5822579-konftel-300ipx-telnyx-setup
  content_hash: 61466601dc8f68a93d4785ff0a614d1575b14d2f50618f3cadc5829963f00e98
- url: https://support.telnyx.com/en/articles/5822901-vtech-vcs754-telnyx-setup
  content_hash: 2384f691b0153d466bf5fe66241fe7da746474b6e29792b94df3c2544860127a
updated_at: 2026-05-20T15:11:01Z
---

# Configure Popular SIP Phones and Conference Devices with Telnyx (Snom, Mitel, Panasonic, Konftel, VTech)

*Part 1 of 2 — see also: [Part 2](configure-popular-sip-phones-and-conference-devices-with-telnyx-snom-mitel-panasonic-konftel-vtech--part-2.md)*

A consolidated guide to register and secure popular SIP desk and conference phones with Telnyx, including Snom C520/D7xx/M100 KLE, Mitel 5320e/5330e/5340e and 6800/6900, Panasonic KX-TGP 550 and KX‑HDV, Konftel 300Wx and 300IPx, and VTech VCS754.

## Prerequisites
- Create and configure your Telnyx Mission Control Portal account and SIP Connection/subaccounts: https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account
- Recommended: Encrypt signaling/media with TLS/SRTP: https://support.telnyx.com/en/articles/1130711-does-telnyx-encrypt-communication and TLS/SRTP specifics: https://support.telnyx.com/en/articles/4404575-tls-and-srtp
- Have your Telnyx SIP credentials ready (SIP username/User ID and password). If using subaccounts, use the subaccount’s username/password.
- Ensure devices run current firmware (see each vendor’s manual/support links in the device sections).

## Universal Telnyx settings (use across devices)
- Registrar/Proxy/Outbound Proxy/Domain/Server: sip.telnyx.com
- Transport and port:
  - UDP or TCP: 5060
  - TLS: 5061
- Registration interval/expiry: 300 seconds (Reregistration/Subscription timers often also 300)
- Keep-alive/registration retry: 10–15 seconds (device wording varies)
- Codecs supported by Telnyx (set in preferred order):
  - G.711u (ulaw), G.711a (alaw), G.722, G.729
- Caller ID display name tips:
  - Use CAPITAL LETTERS for better visibility on some devices
  - Avoid special characters (spaces allowed)
  - Some Canadian carriers show max ~15 characters
- Voicemail access (where applicable): *97
- NAT/Firewall: If available, enable NAT keep-alives; ensure your firewall allows the chosen SIP/RTP ranges.

## Security and TLS/SRTP notes
- When switching to TLS, change all server/registrar/outbound proxy ports to 5061 and set transport to TLS (some UIs label “TLS/TCP” or “SIP‑TLS”).
- Enable SRTP if encrypting media (device wording may be “SRTP Mode: SRTP”, “RTP Encryption: on”, “RTP/SAVP: Mandatory”, or “Enable Voice Encryption”).
- Mitel 6800/6900 supports TLS and Persistent TLS. Persistent TLS requires a trusted CA bundle; root/intermediate/local certs and private key files are optional for Persistent TLS but required for standard TLS on those phones. See Telnyx TLS docs above and the Mitel admin guide for file handling.

## Snom C520 conference phone: quick setup
- Find IP: Menu > Status > Network. Browse to http://IP. Default login: admin / admin (change after setup).
- System > SIP Account Management > select account:
  - General: Account Label (any), Display Name (your caller ID), User Identifier = Telnyx SIP username, Authentication Name = same, Authentication Password = SIP password, Dial Plan = x+P
  - SIP Server: Address sip.telnyx.com; Port 5060 (UDP/TCP) or 5061 (TLS)
  - Registration: Address sip.telnyx.com; Port 5060/5061; Expiration 300; Registration Freq 10
  - Outbound Proxy: Address sip.telnyx.com; Port 5060/5061
  - Backup Outbound Proxy: only for TLS; Address sip.telnyx.com; Port 5061
  - Audio: prioritize G.711u, G.711a, G.722, G.729 as needed
  - Signaling Settings: Local SIP Port 5060 (or 5061 TLS); Transport UDP/TCP (or TLS/TCP)

## Snom D7xx desk phones (D120/D717/D735/D785): quick setup
- Find IP: Settings > Information > System Information. Browse to http://IP. Default: admin / 0000.
- Select Identity 1 (or desired identity) > Login:
  - Displayname (caller ID), Account = Telnyx SIP username, Password = SIP password
  - Registrar = sip.telnyx.com (append :5061 if TLS)
  - Outbound Proxy = sip.telnyx.com (append :5061 if TLS)
  - Authentication Username = Telnyx SIP username
  - Mailbox = *97; Apply
- SIP tab: Dial-Plan String ^.$; Proposed Expiry 300; Subscription Expiry 300; Failed Subscription Retry Time 300; Apply
- Codecs: Order G.711u/a, G.722, G.729. If TLS: set RTP Encryption on and RTP/SAVP Mandatory; Save

## Snom M100 KLE base station: quick setup
- Find IP: Handset Menu/Select > Status > Network. Browse to http://IP. Default: admin / admin.
- System tab:
  - General Account Settings: User Identifier = Telnyx SIP username (main or sub), Authentication Name = same, Password = SIP password
  - SIP Server: Address sip.telnyx.com; Port 5060 (or 5061 TLS)
  - Registration: Address sip.telnyx.com; Port 5060/5061
- Status tab should show Registered.

## Mitel 5320e/5330e/5340e SIP: quick setup
- Find IP: press/hold volume keys then follow on-screen Network > Current Network Params; note Phone IP Address. Browse to http://IP. Default admin / model number (5320e or 5330e or 5340e).
- Admin Tools > User List Config:
  - User ID/Extension = Telnyx SIP username; User Display Name (caller ID)
  - SIP Authentication Username = Telnyx SIP username; SIP Authentication Password = SIP password
  - Line Type = SIP
  - SIP Proxy/Registry/Outbound Server = sip.telnyx.com; Port 5060 (UDP/TCP) or 5061 (TLS); Scheme UDP/TCP or TLS
- Submit/OK and verify registration/status.

## Mitel 6800/6900 SIP series: quick setup
- Find IP: Phone Status > IP & MAC (6863i/6865i/6905/6910) or Network > IP Address (6867i/6869i/6873i/6920/6930/6940/6970). Browse to http://IP.
  - Admin default: admin / 22222. User default: user / (blank).
- Configure via Web UI:
  - Advanced Settings > Global SIP for global auth, or Advanced Settings > Line X for per-line auth
  - Auth fields (global or per-line): Screen/Display Name (caller ID), Phone Number/User Name = Telnyx SIP username, Authentication Name = Telnyx SIP username, Password = SIP password; optional voicemail number *97
  - Network (global or per-line): Proxy/Outbound/Registrar = sip.telnyx.com; Proxy Port 5060 (UDP/TCP) or 5061 (TLS)
- TLS/Persistent TLS (optional): set Transport Protocol = TLS, then supply Trusted Certificate file (required); Root/Intermediate, Local Certificate, and Private Key as required per mode. See Telnyx TLS docs above and the Mitel admin guide for file parameters.

## Panasonic KX‑TGP 550/500/551: quick setup
- Register handsets to base (Menu > Initial Settings > Registration > Register Handset; hold ALL on base 4 seconds; confirm on handset).
- Find IP and enable web: Handset Menu > IP Service > Network Setting > IP Setting (note IP). Then Network Setting > Embedded Web = On. Browse to http://IP. Default: admin / adminpass.
- VoIP tab:
  - Phone Number = your DID (optional label on some UIs)
  - Line ID = Telnyx SIP username
  - Registrar/Proxy/Service Domain = sip.telnyx.com; Ports 5060 (or 5061 TLS where supported)
  - Presence/Source Port (if shown): 5060
  - Authentication ID = Telnyx SIP username; Authentication Password = SIP password
  - Keep Alive Interval ~15
- Save and verify registration.

## Panasonic KX‑HDV130/230/330: quick setup
- Enable web and get IP: Basic Settings > Other Options > Embedded Web = On; then System Settings > Status > IPv4 Settings > IP Address. Browse to http://IP. Default: admin / adminpass.
- VoIP tab > SIP Settings > Line 1 (similar for other lines):
  - Phone Number = Telnyx SIP username (main or subaccount)
  - Registrar/Proxy/Presence/Outbound Proxy/Service Domain = sip.telnyx.com; Ports 5060 (UDP) or 5061 (TLS)
  - Authentication ID = Telnyx SIP username; Authentication Password = SIP password
  - Advanced: REGISTER Expires 300; Transport UDP (or TLS if enabled). If TLS, set TLS Mode to SIP‑TLS and under VoIP Settings > Line 1 Advanced set SRTP Mode = SRTP
- Codecs: enable only G.711u, G.711a, G.722, G.729; order to preference. Save.

## Konftel 300Wx: quick setup
- Find IP: Menu > Status > Network. Browse to http://IP. Default: admin / admin.
- Server > Add Server:
  - Alias (any); NAT Adaption = Enabled; Registrar = sip.telnyx.com; Outbound Proxy = sip.telnyx.com
  - Reregistration Time = 300; SIP Transport = TCP (or TLS with matching settings)
  - Keep Alive = Enabled; Codec Priority = Telnyx codecs list
  - If encrypting: Secure RTP = Enabled; Secure RTP Auth = Enabled
- Extensions > Add Extension:
  - Extension = your DID (label); Authentication Username = Telnyx SIP username; Authentication Password = SIP password; Server = the server above; assign device and Save
- Verify: Extensions page State should show SIP Registered.
