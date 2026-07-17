---
title: Telnyx Device Setup and Voice Features
summary: Step-by-step Telnyx setup guides for the Panasonic KX-TGP 550, Panasonic
  KX-HDV series, Konftel 300Wx, Konftel 300IPx, Snom M100 KLE, and Vtech VCS754 ErisStation,
  plus an overview of Telnyx Real-Time Transcription and the HD Voice Number Feature.
sources:
- url: https://support.telnyx.com/en/articles/5807663-panasonic-kx-tgp-550
- url: https://support.telnyx.com/en/articles/5807979-konftel-300wx-telnyx-setup
- url: https://support.telnyx.com/en/articles/5814406-panasonic-kx-hdv-telnyx-setup
- url: https://support.telnyx.com/en/articles/5822579-konftel-300ipx-telnyx-setup
- url: https://support.telnyx.com/en/articles/5822823-snom-m100-kle-telnyx-setup
- url: https://support.telnyx.com/en/articles/5822901-vtech-vcs754-telnyx-setup
- url: https://support.telnyx.com/en/articles/8292490-real-time-transcription
- url: https://support.telnyx.com/en/articles/8394071-hd-voice-number-feature
updated_at: 2026-07-17T09:10:29Z
---

# Telnyx Device Setup and Voice Features

*Part 3 of 3 — see also: [Part 1](telnyx-device-setup-and-voice-features--part-1.md), [Part 2](telnyx-device-setup-and-voice-features--part-2.md)*

Step-by-step Telnyx setup guides for the Panasonic KX-TGP 550, Panasonic KX-HDV series, Konftel 300Wx, Konftel 300IPx, Snom M100 KLE, and Vtech VCS754 ErisStation, plus an overview of Telnyx Real-Time Transcription and the HD Voice Number Feature.

## HD Voice Number Feature

The HD Voice Number Feature enhances audio quality for PSTN calls to and from eligible numbers in supported countries by leveraging wideband codecs such as AMR-WB, Opus, and G.722 instead of narrowband codecs like G.711.

### How HD Voice works

HD Voice requires both endpoints to support and negotiate a compatible wideband codec. The negotiation considers available bandwidth, device capabilities, and network conditions. If wideband support is unavailable, calls fall back to a suitable narrowband codec via transcoding.

### Supported carriers and regions

- **US:** AT&T, T-Mobile, Verizon
- **Germany:** Outbox
- **Austria:** Yuutel
- **Australia:** All major carriers

The call must originate or terminate on a mobile device that supports wideband codecs and is registered on a local 5G/LTE network.

### Codec requirements

Your Telnyx SIP connection must have at least one of the following wideband codecs enabled: **OPUS**, **G.722**, or **AMR-WB**. The SIP device involved in the call must also support the selected codec.

### Receiving a call with HD Voice

For inbound HD Voice calls:

1. The incoming call must originate on an AMR-WB-enabled device in at least 4G/LTE coverage from a supported carrier.
2. The call must be routed to a Telnyx number with HD Voice enabled.
3. The call must be routed to a SIP Connection configured with AMR-WB, G.722, or Opus.
4. The receiving SIP device must support one of those codecs.

Enable HD Voice in **Number Voice** settings:

![](_images/ad9d3a60561b6fcd.png)

The HD Voice option appears under the services column in the **My Numbers** overview:

![Services section.](_images/56ffd36dc30749d0.png)

HD-capable numbers can also be searched in the [Buy Numbers](https://portal.telnyx.com/#/numbers/buy-numbers) section:

![](_images/cb855811981dddaf.png)

### Making an outbound call with HD Voice

For outbound HD Voice calls:

1. The initiating SIP device must use AMR-WB, G.722, or Opus.
2. The receiving device must be AMR-WB-enabled and on at least 4G/LTE from a supported carrier.
3. The Telnyx number used (including CLI override) must have HD Voice enabled.

### Geographic availability

The feature is restricted to numbers in the supported coverage areas listed above.

### Frequently asked questions

- **"This number is not HD Voice capable" banner:** Appears for international, toll-free, and some +1 US longcode numbers. Currently supported only on +1 US longcode numbers, with expansion planned.
- **Recommended SIP devices:** Any SIP device supporting AMR-WB, G.722, or Opus.
- **Codec mismatch:** Calls are transcoded. Mismatches between two HD codecs retain HD quality; mismatches between an HD and non-HD codec fall back to narrowband.
- **Fallback to narrowband:** Performed via transcoding.
- **Interruptions:** None — codecs are negotiated at call start.
- **Bandwidth:** Variable bit rate; a high-speed internet connection is recommended.
- **Future expansion:** Additional carriers and countries will be added.
- **Device support:** Check the device user manual for supported codecs.
- **Billing:** As of July 2025, HD Voice is free with no monthly recurring charges.

## Additional Resources

- [Getting started with Mission Control](https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account)
- [Requesting numbers](https://support.telnyx.com/en/articles/3562148-requesting-numbers)
- [Enabling TLS to encrypt traffic](https://support.telnyx.com/en/articles/1130711-does-telnyx-encrypt-communication)
- [Panasonic KX-TGP 550 support](https://www.panasonic.com/in/support/phones-communication.html)
- [Panasonic KX-HDV130 Operating Instructions](https://na.panasonic.com/ns/235945_KX-HDV130_OI_2015-02.pdf)
- [Konftel 300Wx product data sheet](https://www.konftel.com/-/media/konftel/files/product-documentation/konftel-300wx/konftel300wx_datasheet_eng-low.pdf?la=en)
- [Konftel 300IPx user guide](https://www.konftel.com/-/media/konftel/files/user-guide/konftel-300ipx/konftel300ipx-ug_eng.pdf?la=en)
- [Snom M100 KLE datasheet](https://www.snomamericas.com/assets/0a504990-0017-40bf-a8d4-692cca8e7bc6/snom_M100-KLE_datasheet_en.pdf)
- [Vtech VCS754 admin and provisioning manual](https://cdn-web.vtp-media.com/media/p/document2/products/%7B7071581F-D65E-42DC-B684-036AA12E9853%7D/VTech_VCS754_Admin_Provisioning_Manual%20-%20Rev%204.pdf)
- [Voice API transcription reference](https://developers.telnyx.com/api-reference/call-commands/dial)
- [TeXML transcription reference](https://developers.telnyx.com/voice/texml/texml-translator)
