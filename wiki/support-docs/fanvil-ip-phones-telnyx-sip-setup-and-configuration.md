---
title: 'Fanvil IP Phones: Telnyx SIP Setup and Configuration'
summary: Step-by-step guidance to register Fanvil desk and hospitality phones to Telnyx,
  including prerequisites, SIP line parameters, TLS/SRTP options, codec choices, and
  model-specific tips for X-, XU-, X7-, V-series, H-series, A32i, and X4/X4G devices.
sources:
- url: https://support.telnyx.com/en/articles/5811487-fanvil-x4g-telnyx-setup
  content_hash: 17f2a4970656ea857a6f94f32e0c3b53552d0de1e694b0090126d1a6c99f138f
- url: https://support.telnyx.com/en/articles/6056428-fanvil-a32i-telnyx-setup
  content_hash: 938490d773359b1a7d9a22f8d8514837e3fde549b86cbdc2c4519c76b58f65e0
- url: https://support.telnyx.com/en/articles/6202755-fanvil-h2u-compact-ip
  content_hash: 22c3e37375854366ab859831dd964953d8c60500e6c4fbfe715c8c07f4805170
- url: https://support.telnyx.com/en/articles/6202965-fanvil-h3-hotel-ip
  content_hash: 27c371778821e4cfb8af8c4b8cc5d336cf42757ad5535d29145f3fae62b5151e
- url: https://support.telnyx.com/en/articles/6203347-fanvil-h3w-h5w-wifi-ip
  content_hash: 887164a231604129da85f1c7428e538f0e6e0061dc7d64c65a19682566331c0b
- url: https://support.telnyx.com/en/articles/6203401-fanvil-h5-hotel-ip
  content_hash: 9d1937c059686aba572c6ea524cf591101f701d33e7a39738bf65fae7f84f398
- url: https://support.telnyx.com/en/articles/6206533-fanvil-x1-x1p-ip-phone
  content_hash: 1fd516c709d04f99a615d09c115f86c2c165c6c605b20da6e12edf1d8dd89118
- url: https://support.telnyx.com/en/articles/6206756-fanvil-x2cp-x2c-x2p-call-center-ip
  content_hash: 16aabe404b5e8854c2c7bb0a209a3068985b9bddaaa5525a8c24f376463df386
- url: https://support.telnyx.com/en/articles/6209215-fanvil-x7-series-ip-phones
  content_hash: 5ac8c1820c5eb192e8489a3e3b1450f37d9a7a8017440f984b2c2fd637442b01
- url: https://support.telnyx.com/en/articles/6209862-fanvil-v-series-ip-phones
  content_hash: 4a38f2406562c02c2ab7dc3504e1d75012ee67a0418a62b82173390df985b79c
- url: https://support.telnyx.com/en/articles/6209971-fanvil-x-series-ip-phone
  content_hash: 39e097df108211f54aa1c9dd2ede48b23232397350d67a628555ee540267fc1b
- url: https://support.telnyx.com/en/articles/6210147-fanvil-xu-series-ip-phone
  content_hash: 7c986534c5902f3be2f138941c826d4f49e2f601808ad826a389fcbd6db9c4e6
updated_at: 2026-05-20T15:04:34Z
---

# Fanvil IP Phones: Telnyx SIP Setup and Configuration

Step-by-step guidance to register Fanvil desk and hospitality phones to Telnyx, including prerequisites, SIP line parameters, TLS/SRTP options, codec choices, and model-specific tips for X-, XU-, X7-, V-series, H-series, A32i, and X4/X4G devices.

## Models covered and quick resources
The steps below apply to these Fanvil models (see each link for product docs/firmware):
- X4/X4G: https://www.fanvil.com/Product/info/id/72.html
- A32i: https://www.fanvil.com/Product/info/id/139.html
- H-series: H2U https://www.fanvil.com/Product/info/id/122.html, H3 https://www.fanvil.com/Product/info/id/78.html, H5 https://www.fanvil.com/Product/info/id/79.html, H3W https://www.fanvil.com/Product/info/id/138.html, H5W https://www.fanvil.com/Product/info/id/137.html
- X1/X1P: https://www.fanvil.com/Product/info/id/89.html
- X2CP/X2C/X2P: https://www.fanvil.com/Product/info/id/96.html and https://www.fanvil.com/Product/info/id/64.html
- X7 series: X7 https://www.fanvil.com/Product/info/id/93.html, X7C https://www.fanvil.com/Product/info/id/94.html, X7A https://www.fanvil.com/Product/info/id/124.html (with camera: https://www.fanvil.com/Product/info/id/125.html)
- V-series: V67 https://www.fanvil.com/Product/info/id/157.html, V65 https://www.fanvil.com/Product/info/id/158.html, V64 https://www.fanvil.com/Product/info/id/159.html, V62 https://www.fanvil.com/Product/info/id/160.html
- XU series: X6U https://www.fanvil.com/Product/info/id/106.html, X5U https://www.fanvil.com/Product/info/id/108.html (Red: https://www.fanvil.com/Product/info/id/118.html), X4U https://www.fanvil.com/Product/info/id/109.html, X3U https://www.fanvil.com/Product/info/id/110.html, X3U Pro https://www.fanvil.com/Product/info/id/142.html
- Generic X-series (all other X models): https://fanvil.com/products/p1/x/index.html

Always update to the latest firmware from your model’s download page before configuring.

## Before you begin
- Set up your Telnyx Mission Control account and SIP Connection: https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account
- Recommended: Use TLS to encrypt signaling: https://support.telnyx.com/en/articles/1130711-does-telnyx-encrypt-communication
- Access the phone’s web GUI:
  - Most models ship with Username: admin, Password: admin (see your user manual if different).
  - X4/X4G: On the handset, OK > Status > IP Address, then browse to http://<that IP> and log in (default admin/admin).
  - A32i: You can also configure on-device via Phone Settings > Account > Line; default on-device PIN is 123.
- If you need regional/international Telnyx signaling addresses, see: https://sip.telnyx.com/#signaling-addresses

## Configure and register a SIP line
Do this in the web GUI unless noted otherwise.
1) Navigate to Line > SIP and select a Line to configure.
2) In Register/Basic Settings, set:
- Username: Your Telnyx SIP Connection username (or Telnyx portal main/sub-account username when applicable).
- Authentication Name/User: Same as the Username above.
- Authentication Password: Your Telnyx SIP password.
- Display Name (caller ID name shown by your phone): optional; see Caller ID guidelines below.
- Realm: Enter the realm associated with your SIP interface/connection as provided in your Telnyx credentials (if required).
- Server Name: sip.telnyx.com (use a regional address if you’re targeting a specific Telnyx region).
3) In SIP Server / Proxy settings, set:
- Server Address: sip.telnyx.com
- Server Port: 5060 if using UDP or TCP; 5061 if using TLS.
- Transport Protocol: Choose UDP or TCP; choose TLS only if you will encrypt signaling (see Encryption section).
- Outbound/Proxy/Backup Server (if present): sip.telnyx.com, with the same port as above.
- Optional: Configure SIP Server 2 as a secondary/backup using the same values.
4) Apply/Save, then refresh the page. The line should show Registered.

Model notes that map to the same fields above:
- X4/X4G: Also set Register Address, Proxy Server Address, and Backup Proxy to sip.telnyx.com; choose Register Port 5060 (UDP) or 5061 (TLS). Ensure the line is Activated, then Apply and refresh.

## Encryption (TLS and optional SRTP)
If you enable TLS on the phone and in Telnyx, also complete these steps.
- In Lines > SIP > Advanced (naming varies by model):
  - DTMF Type: RFC 2833
  - Transport/Transportation Protocol: TLS
  - If your model uses Dial Peer for port selection, set Lines > Dial Peer > Port to 5061.
  - SIP Encryption: Enable (if present on your model).
  - RTP Encryption (SRTP): Optional; enable if you want encrypted media and your environment supports it.
- Upload a TLS certificate file when required by your model UI:
  - Go to Line > Basic Settings (or similar) and in the STUN/Certificate section set TLS Certification File using a cert obtainable here: https://crt.sh/?id=1199354
  - Some UIs also reference an RTP/TLS Encryption Key; use the same certificate source above.

## Audio and video codec selection
Set codec priorities under Codecs/Audio-Video settings for the configured line. Telnyx supports:
- Audio: ulaw (G.711u), alaw (G.711a), G.722, G.729
- Video: H.264

## Caller ID name guidelines (Display Name field)
- Use capital letters for improved legibility on some devices.
- Do not use special characters; spaces are allowed.
- Some Canadian carriers display a maximum of 15 characters; consider abbreviations.

## Model-specific tips
- A32i: You may configure the line from the touchscreen (long-press a line key or Phone Settings > Account > Line). Default PIN: 123.
- H2U/H3/H5/H3W/H5W: Default web credentials are typically admin/admin; see each user manual for exact details and Wi-Fi setup on H3W/H5W.
- X1/X2/X7/V/XU series: If using TLS, upload the TLS certificate as described above. Manuals list the Web Management section containing the web login steps.
- X5/X7/V/XU variants include advanced features (Bluetooth, Wi-Fi, video, DSS keys) that do not change the Telnyx SIP parameters outlined here.

## Test and troubleshoot
- After saving, the line status should show Registered. If not:
  - Re-check Username/Authentication Name and Password.
  - Confirm Server Address matches your target region and Transport/Port pairing (UDP/TCP with 5060; TLS with 5061).
  - If using TLS/SRTP, ensure you uploaded the certificate and switched Dial Peer port to 5061 where applicable.
  - Verify DTMF Type is RFC 2833 and your chosen codecs include a Telnyx-supported option.
- Place a test call. If issues persist, reboot the phone after changes and confirm your network allows outbound connections to sip.telnyx.com on your chosen signaling port.
