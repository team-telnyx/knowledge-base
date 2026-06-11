---
title: 'Fanvil IP Phones: Telnyx Setup'
summary: Configure a Telnyx SIP trunk on Fanvil IP phones across the H-series (H2U,
  H3, H3W, H5W, H5), A32i, X-series (X1/X1P, X2CP/X2C/X2P, X7, general X-series),
  XU-series (X3U/X4U/X5U/X6U), and V-series (V62/V64/V65/V67). All models share the
  same core SIP settings, codec preferences, and optional TLS configuration, though
  the web GUI layout and field names vary slightly between firmware generations.
sources:
- url: https://support.telnyx.com/en/articles/6056428-fanvil-a32i-telnyx-setup
- url: https://support.telnyx.com/en/articles/6202755-fanvil-h2u-compact-ip
- url: https://support.telnyx.com/en/articles/6202965-fanvil-h3-hotel-ip
- url: https://support.telnyx.com/en/articles/6203347-fanvil-h3w-h5w-wifi-ip
- url: https://support.telnyx.com/en/articles/6203401-fanvil-h5-hotel-ip
- url: https://support.telnyx.com/en/articles/6206533-fanvil-x1-x1p-ip-phone
- url: https://support.telnyx.com/en/articles/6206756-fanvil-x2cp-x2c-x2p-call-center-ip
- url: https://support.telnyx.com/en/articles/6209215-fanvil-x7-series-ip-phones
- url: https://support.telnyx.com/en/articles/6209862-fanvil-v-series-ip-phones
- url: https://support.telnyx.com/en/articles/6209971-fanvil-x-series-ip-phone
- url: https://support.telnyx.com/en/articles/6210147-fanvil-xu-series-ip-phone
updated_at: 2026-06-11T11:29:47Z
---

# Fanvil IP Phones: Telnyx Setup

*Part 2 of 2 — see also: [Part 1](fanvil-ip-phones-telnyx-setup--part-1.md)*

Configure a Telnyx SIP trunk on Fanvil IP phones across the H-series (H2U, H3, H3W, H5W, H5), A32i, X-series (X1/X1P, X2CP/X2C/X2P, X7, general X-series), XU-series (X3U/X4U/X5U/X6U), and V-series (V62/V64/V65/V67). All models share the same core SIP settings, codec preferences, and optional TLS configuration, though the web GUI layout and field names vary slightly between firmware generations.

## Additional Resources

- [Fanvil FAQ](https://www.fanvil.com/Support/index.html)
- [Fanvil training videos](https://www.fanvil.com/Support/trainingVideo.html)
- [Fanvil support / ticket system](https://www.fanvil.com/Support/ticket.html)

### Firmware Downloads

| Model | Firmware Link |
|---|---|
| A32i | [A32i firmware](https://www.fanvil.com/Support/download/id/139.html) |
| H2U | [H2U firmware](https://www.fanvil.com/Support/download/id/122.html) |
| H3 | [H3 firmware](https://www.fanvil.com/Support/download/id/78.html) |
| H3W | [H3W firmware](https://www.fanvil.com/Support/download/id/138.html) |
| H5W | [H5W firmware](https://www.fanvil.com/Support/download/id/137.html) |
| H5 | [H5 firmware](https://www.fanvil.com/Support/download/id/79.html) |
| X1/X1P | [X1/XP firmware](https://www.fanvil.com/Support/download/id/89.html) |
| X2CP | [X2CP firmware](https://www.fanvil.com/Support/download/id/96.html) |
| X2C/X2P | [X2C/X2P firmware](https://www.fanvil.com/Support/download/id/64.html) |
| X7 | [X7 firmware](http://fanvil.com/Support/download/id/93.html) |
| X7C | [X7C firmware](https://www.fanvil.com/Support/download/id/94.html) |
| X7A | [X7A firmware](https://www.fanvil.com/Support/download/id/124.html) |
| X7A (camera) | [X7A camera firmware](https://www.fanvil.com/Support/download/id/125.html) |
| X-series (general) | [X-series firmware & manuals](https://fanvil.com/service/doc/file/p1/x1/x7agaoduanchupinghuaji/index.html) |
| X6U | [X6U firmware](https://www.fanvil.com/Support/download/id/106.html) |
| X5U | [X5U firmware](https://www.fanvil.com/Support/download/id/108.html) |
| X5U-R | [X5U-R firmware](https://www.fanvil.com/Support/download/id/118.html) |
| X4U | [X4U firmware](https://www.fanvil.com/Support/download/id/109.html) |
| X3U | [X3U firmware](https://www.fanvil.com/Support/download/id/110.html) |
| X3U Pro | [X3U Pro firmware](https://www.fanvil.com/Support/download/id/142.html) |
| V64 | [V64 firmware](https://www.fanvil.com/Support/download/id/159.html) |
| V62 | [V62 firmware](https://www.fanvil.com/Support/download/id/160.html) |
| V67 | See section 10.7.5 of the [V67 user manual](https://www.fanvil.com/Uploads/Temp/download/20220310/6229a2f42d58f.pdf) |
| V65 | See section 10.7.5 of the [V64/V65 user manual](https://www.fanvil.com/Uploads/Temp/download/20220412/62555c3e41d94.pdf) |

### User Manuals

| Model(s) | Manual Link |
|---|---|
| A32i | [A32i user manual](https://fanvil.com.hk/wp-content/uploads/2021/09/A32i-Android-Console-IP-Phone-A32i-User-Manual.pdf) |
| H2U / H3 | [H2U/H3 user manual](https://www.fanvil.com/Uploads/Temp/download/20210421/607fcc2424c72.pdf) |
| H3W / H5W | [H3W/H5W user manual](https://www.fanvil.com/Uploads/Temp/download/20210608/60bf0ca559890.pdf) |
| H5 | [H5 user manual](https://www.fanvil.com/Uploads/Temp/download/20201110/5faa5e5b85b05.pdf) |
| X1/X1P | [X1/XP user manual](https://www.fanvil.com/Uploads/Temp/download/20201109/5fa90afc7ca32.pdf) |
| X2CP | [X2CP user manual](https://www.fanvil.com/Uploads/Temp/download/20200109/5e16c3554c22d.pdf) |
| X2C/X2P | [X2C/X2P user manual](https://www.fanvil.com/Uploads/Temp/download/20200109/5e16c31bac331.pdf) |
| X7 | [X7 user manual](https://www.fanvil.com/Uploads/Temp/download/20210106/5ff5946b8b78e.pdf) |
| X7C | [X7C user manual](https://www.fanvil.com/Uploads/Temp/download/20210106/5ff594a2412cf.pdf) |
| X7A | [X7A user manual](https://www.fanvil.com/Uploads/Temp/download/20210112/5ffd956d5a486.pdf) |
| X7A (camera) | [X7A camera user manual](https://www.fanvil.com/Uploads/Temp/download/20210112/5ffd95117fb3f.pdf) |
| XU-series (all) | [XU user manual](https://www.fanvil.com/Uploads/Temp/download/20210225/60371ccc639f2.pdf) |
| V67 | [V67 user manual](https://www.fanvil.com/Uploads/Temp/download/20220310/6229ab6b347e3.pdf) |
| V64/V65 | [V64/V65 user manual](https://www.fanvil.com/Uploads/Temp/download/20220412/62555c3e41d94.pdf) |
| V62 | [V62 user manual](https://www.fanvil.com/Uploads/Temp/download/20220310/6229ab6b347e3.pdf) |
