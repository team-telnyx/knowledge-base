---
title: Configure Popular Softphones and SIP Apps with Telnyx
summary: This guide consolidates Telnyx setup steps for leading softphones and SIP-enabled
  apps—including Bria (Solo/X‑Lite and Teams), Linphone, Zoiper (5, 3, Communicator),
  Acrobits Softphone/Groundwire, MicroSIP, NCH Express Talk, and Voice Elements—plus
  common settings, encryption, caller ID rules, and troubleshooting tips.
sources:
- url: https://support.telnyx.com/en/articles/1130645-configuring-bria-solo-a-k-a-x-lite
  content_hash: 5ffa27aa3960ff9511541b895ca53cd26ddc6b4fde104f4c993e8f57d278d1e6
- url: https://support.telnyx.com/en/articles/1130674-configuring-linphone-with-telnyx
  content_hash: bb73e2aa23460425afb8d6466d0bf01a466b6687fe573ad0b85ed291be63d18b
- url: https://support.telnyx.com/en/articles/5717957-zoiper-5-pro-telnyx-setup
  content_hash: b9fbfdc279acab96b3def6b427dc96db45d5330eb692386febdad33b92fbc43d
- url: https://support.telnyx.com/en/articles/5720999-zoiper-3-telnyx-setup-mac
  content_hash: 05ba6ad8ae13796ba4a4d8784f9ae8a0da57c56f4b903fa5ae113a4619014673
- url: https://support.telnyx.com/en/articles/5721766-zoiper-3-telnyx-setup-linux
  content_hash: c03bdbc5d9339777783a39190710d130f8b7c3f68b8811eed14091e76d048744
- url: https://support.telnyx.com/en/articles/5761112-acrobits-softphone
  content_hash: f42bac03e974d542663c7e4f74c2d07d7554e980e3e6fb44aa828aa627e60ac2
- url: https://support.telnyx.com/en/articles/5772825-counterpath-bria-teams-setup
  content_hash: bc75bab088bb5a37abc3c62e30b5f264d18876a7547c0b73b719c1317fc0e504
- url: https://support.telnyx.com/en/articles/5807457-nch-express-talk
  content_hash: 122d40f40befc4b1a56f576aa0df15acf19510905424dd3fdde2bb19754f43eb
- url: https://support.telnyx.com/en/articles/6133145-microsip-setup-with-telnyx
  content_hash: 8a789ac9aafa9fa96ccdec3c4d757d92d60eebe84733eca8609b349917e5c6fa
- url: https://support.telnyx.com/en/articles/6133517-zoiper-communicator
  content_hash: 152d4969f11ded9bcd9d29e01b04cd7f99c7634be2ca64f12d9e50db669e2af4
- url: https://support.telnyx.com/en/articles/6145484-voice-elements-telnyx-sip
  content_hash: 7de9f8944e3aad65da9b1da54feabc7d8b98eeffa336084069e0349990d85bbe
updated_at: 2026-05-20T15:14:48Z
---

# Configure Popular Softphones and SIP Apps with Telnyx

*Part 1 of 2 — see also: [Part 2](configure-popular-softphones-and-sip-apps-with-telnyx--part-2.md)*

This guide consolidates Telnyx setup steps for leading softphones and SIP-enabled apps—including Bria (Solo/X‑Lite and Teams), Linphone, Zoiper (5, 3, Communicator), Acrobits Softphone/Groundwire, MicroSIP, NCH Express Talk, and Voice Elements—plus common settings, encryption, caller ID rules, and troubleshooting tips.

## Common Telnyx SIP settings
- SIP domain (registrar/proxy): sip.telnyx.com
- Ports: 5060 (UDP/TCP), 5061 (TLS)
- Transport: UDP or TCP; use TLS with port 5061 for encrypted signaling
- Media encryption: SRTP (SDES) when using TLS
- Registration/keepalive (where configurable): Registration expiry ~300s; NAT keepalive ~30s
- Optional STUN: stun.telnyx.com:3478
- Supported audio codecs: G.711u (ulaw), G.711a (alaw), G.722, G.729

## Caller ID requirements and verification
- Follow Telnyx caller ID policy and formatting rules: use a valid, E.164-formatted number you own or a Verified Number. See Telnyx Caller ID Number Policy and Verified Numbers.
- Many softphones use Display Name as the From/CID. Use CAPITAL LETTERS, avoid special characters, spaces allowed, and note some Canadian carriers show up to 15 characters.
- If you receive 403 invalid caller ID, ensure headers are correct or enable a caller ID override on your SIP Connection’s outbound settings (per policy instructions).

## Bria Solo (X‑Lite) quick setup
1. Open Bria Solo/X‑Lite > Softphone > Account Settings.
2. Fill fields:
   - User ID: your Telnyx SIP username
   - Domain: sip.telnyx.com
   - Password: your Telnyx SIP password
   - Authorization Name: only if provided by Telnyx
   - Register with domain and receive calls: checked (to receive calls)
   - Send outbound via: only if instructed; set address accordingly
3. Save; account should register and enable.

## Linphone setup and encryption
1. Launch Linphone > Account Assistant > Use a SIP account.
2. Enter:
   - Username: Telnyx SIP auth username
   - Display Name: your caller ID name (follow policy)
   - SIP Domain: sip.telnyx.com
   - Password: Telnyx SIP password
   - Transport: UDP or TCP
3. For encryption: set SIP Domain to sip.telnyx.com:5061 and Transport to TLS; then Preferences > Call and Chat > enable SRTP.

## Zoiper 5 Pro setup, keepalives, and TLS/SRTP
1. Activate Zoiper 5 Pro, then Create account; select Telnyx as provider and follow the wizard to authenticate.
2. Advanced > Audio Codecs: prioritize desired codecs (G.711u/a, G.722, G.729 supported).
3. Advanced > Network Related:
   - Registration expire mode: Custom; Registration expiry: 300
   - NAT keep alive time‑out: Custom; Keep alive custom interval: 30
4. TLS/SRTP:
   - In the Telnyx portal, enable Encrypted SIP Traffic for the account/sub‑account you’ll register.
   - Zoiper Advanced > SIP Credentials: Domain sip.telnyx.com; set Transport to TLS.
   - Encryption: SRTP key negotiation SDES.
   - Place a call; a green padlock indicates a secure call. If encryption is enforced in the portal but Zoiper sends UDP/TCP or RTP, you’ll get 488.

## Zoiper 3 (Mac/Linux) quick setup
1. Settings > Create a new account > SIP.
2. Enter your Telnyx SIP credentials; Domain/Outbound proxy: sip.telnyx.com.
3. Complete the wizard. If online activation is blocked, use offline activation to generate a certificate (Mac: ~/Library/Zoiper3/, Linux: ~/.Zoiper) and follow Zoiper’s instructions to submit it.

## Acrobits Softphone / Groundwire (iOS/Android)
- Note: Only voice calling is supported with Telnyx (SIP/SIMPLE for SMS/MMS is not supported).
1. Open app > Settings (gear) > SIP Accounts > New SIP Account.
2. Select Telnyx (or add manually), then:
   - Title: e.g., Telnyx
   - Username / Password: your Telnyx SIP credentials
   - Domain: sip.telnyx.com
3. Save and start calling. For caller ID name, prefer CAPITALS, no special characters, spaces allowed; some Canadian carriers limit to 15 characters.

## Bria Teams integration (portal)
1. Bria Portal > Voice and Video > Add Voice Configuration > Configure SIP Settings:
   - Service Label: your label
   - Domain: sip.telnyx.com
   - Port: 5060
   - Register with domain and receive calls: checked
   - Transport: Automatic
   - Keep Alive: Enabled
   - Voicemail number: *97
   - Service Options: require authorization username (checked)
   - (Optional) Firewall Method: STUN; Server URL: stun.telnyx.com:3478
2. To enable encryption: Edit Configuration and set Port 5061, Transport TLS, SRTP Enabled, and keep “Register with Domain” checked.
3. Codecs: Configure and prioritize; Telnyx supports G.711u/a, G.722, G.729.
4. Dial plans: Configure as needed using Bria’s dial plan syntax (e.g., prepend 9, normalize prefixes).
5. Team members: Team Members > add member(s) and assign Voice Service plus:
   - SIP Username/Extension and SIP/Voice Password (Telnyx credentials)
   - Call Display (caller ID name best practices: CAPITALS, no special characters, up to 15 chars; spaces allowed)

## MicroSIP (Windows) setup and encryption
1. Open MicroSIP > arrow (top‑right) > Edit Account.
2. Enter:
   - Account Name: your choice
   - SIP Server: sip.telnyx.com
   - SIP Proxy: sip.telnyx.com
   - Username/Login: Telnyx SIP username (main or sub‑account)
   - Domain: sip.telnyx.com
   - Password: Telnyx SIP password
   - Display Name: caller ID name (follow formatting rules)
   - Transport: Auto (UDP/TCP) or TLS
   - Media Encryption: Disabled for UDP/TCP; choose Mandatory SRTP (RTP/SAVP) when using TLS
3. If encrypting: Settings > set Source Port to 5061; set RTP Ports to 10001–20000; Save.
4. Audio: Settings > enable preferred codecs (G.711u/a, G.722, G.729) and enable Echo Cancellation (EC).

## NCH Express Talk quick setup
1. Run Express Talk > File > Options > Lines tab.
2. Enter:
   - Friendly display name: your choice
   - Server (SIP Proxy or Virtual PBX): sip.telnyx.com
   - SIP Number (Username): Telnyx SIP username
   - Password: Telnyx SIP password
3. Save and place test calls.

## Zoiper Communicator quick setup
1. Open Zoiper Communicator > Settings > Create New Account.
2. Name the account, then on SIP Account Options enter:
   - Domain: sip.telnyx.com
   - Username / Password: Telnyx SIP credentials
   - Caller ID Name: follow formatting rules above
3. Save and test.

## Voice Elements with Telnyx (SIP trunk)
1. Open Voice Elements Wizard > Connectivity.
2. Carrier/Gateway/Devices: Other.
3. Location: External IP Authentication (SIP Carrier – Preferred).
4. Enter Telnyx details:
   - Destination IP/URL: sip.telnyx.com (use your regional signaling address if applicable)
   - Registrar IP/URL: sip:sip.telnyx.com
   - AuthURI: your_telnyx_username@sip.telnyx.com
   - Username / Pwd: Telnyx SIP credentials
   - Ports: 5060 for UDP/TCP; 5061 for TLS (ensure TLS/SRTP are enabled in the Telnyx portal if using encryption)
5. Firewall: Restrict SIP/RTP access to Telnyx IP ranges to mitigate SIP scanners; see Telnyx IP whitelisting guidance.

## Troubleshooting and tips
- Registration fails: verify sip.telnyx.com spelling, correct username/password, transport/port selection, and that “Register with domain” is enabled (where applicable). Check local firewall/NAT.
- Encryption errors (e.g., 488): ensure the Telnyx portal encryption setting matches device transport/media (TLS + SRTP).
- One‑way audio/NAT: enable keepalives, use STUN (optional), and confirm RTP port ranges are open.
- 403 invalid caller ID: send a valid Telnyx number or a previously Verified Number; if needed, set a caller ID override on your SIP Connection.
- Zoiper offline activation: if a certificate file is generated, save it in the path shown by Zoiper and follow Zoiper’s email/return instructions; on Windows, ensure file extensions aren’t auto‑changed by the OS.
