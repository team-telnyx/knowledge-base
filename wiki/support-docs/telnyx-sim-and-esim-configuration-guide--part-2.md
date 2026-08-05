---
title: Telnyx SIM and eSIM Configuration Guide
summary: This page consolidates Telnyx guidance on SIM and eSIM provisioning, activation,
  and security. It covers manual eSIM activation, QR-code eSIM setup, SIM theft prevention
  via IMEI authorization, manual IMSI selection for engineering troubleshooting, and
  the underlying VoIP/SIP/SDP/codec concepts that govern how Telnyx SIM-backed devices
  interoperate with the network.
sources:
- url: https://support.telnyx.com/en/articles/10067533-manual-esim-activation-guide
- url: https://support.telnyx.com/en/articles/1130723-voip-telecommunications-protocols
- url: https://support.telnyx.com/en/articles/3192298-audio-and-codecs
- url: https://support.telnyx.com/en/articles/4194697-oracle-acme-packet-sbc-setup
- url: https://support.telnyx.com/en/articles/4301888-sansay-sbc-vsxi-setup
- url: https://support.telnyx.com/en/articles/5761437-sim-card-theft-prevention
- url: https://support.telnyx.com/en/articles/8117401-how-to-setup-a-telnyx-esim-via-qr-code
- url: https://support.telnyx.com/en/articles/9183726-manual-imsi-selection-on-telnyx-sim
updated_at: 2026-08-05T13:24:33Z
---

# Telnyx SIM and eSIM Configuration Guide

*Part 2 of 4 — see also: [Part 1](telnyx-sim-and-esim-configuration-guide--part-1.md), [Part 3](telnyx-sim-and-esim-configuration-guide--part-3.md), [Part 4](telnyx-sim-and-esim-configuration-guide--part-4.md)*

This page consolidates Telnyx guidance on SIM and eSIM provisioning, activation, and security. It covers manual eSIM activation, QR-code eSIM setup, SIM theft prevention via IMEI authorization, manual IMSI selection for engineering troubleshooting, and the underlying VoIP/SIP/SDP/codec concepts that govern how Telnyx SIM-backed devices interoperate with the network.

## VoIP and Telecommunications Protocols

Telnyx SIM-backed devices and SIP trunks rely on a stack of standard protocols to deliver real-time voice and video over IP networks:

- **RTP (Real-time Transport Protocol)** — Application-layer protocol that delivers audio and video over IP networks. First published in 1996 as RFC 1889 and superseded by RFC 3550 in 2003.
- **UDP (User Datagram Protocol)** — Connectionless transport favored for real-time media because dropping packets is preferable to waiting on delayed packets.
- **TCP (Transmission Control Protocol)** — Connection-oriented transport that favors reliability over reduced latency.
- **SIP (Session Initiation Protocol)** — Signaling protocol used to establish, modify, and tear down multimedia sessions.
- **SDP (Session Description Protocol)** — Format used within SIP messages to describe multimedia session parameters.

RTP typically runs over UDP on the transport layer, though TCP can also be used. RTP carries the media stream and works in conjunction with SIP. A separate RTP session is established for each multimedia stream, identified by a port and IP address. Audio and video use separate media streams, so the receiver can deselect one or the other.

RTP typically uses UDP ports between 1024 and 65535. Ports are negotiated through SIP and SDP to form the session. Profiles and payloads are also defined; profiles specify the codecs used to encode the payload data. Audio payload formats include G.711U, G.711A, G.722, and OPUS. Typical video payload formats include H.263, H.264, and MPEG-4.

## Audio, Codecs, and SDP

When you send or receive an INVITE via SIP with Telnyx, the message body should have a content length greater than 0. This body contains the **Session Description Protocol (SDP)** parameters — the place where you define your multimedia session capabilities.

> SDP does not deliver any media. It is used in conjunction with RTP, which handles the delivery of media over IP networks.

The full SDP specification is defined in [RFC 4566](https://tools.ietf.org/html/rfc4566). In VoIP, multimedia can consist of audio or video (and is not limited to these). This information is usually sent in RTP packets using UDP transport. The term "media" is often used interchangeably with audio, voice, or RTP.

A list of Telnyx media IPs and supported codecs is published on the [sip.telnyx.com](https://sip.telnyx.com/) webpage.

### Debugging SDP

The [SIP call flow debugging tool](https://portal.telnyx.com/#/app/debugging/sip-call-flow-tool) in Mission Control lets you view the SIP call flow and read the contents of SIP messages for granular insight into how signaling was established and with what parameters.

- The SDP can be located in the SIP INVITE message to your connection on an inbound call. Telnyx always provides an SDP in INVITEs on inbound calls (early offer), showing accepted capabilities ordered in ascending priority.
- The SDP can also be located in the 183 or 200 OK message on outbound calls. If you send an INVITE with no SDP (late offer), the 200 OK with SDP is sent back when the call is answered, and the caller's ACK then contains the SDP. With this change in SDP placement, the caller decides which codec is used for the session.

### Codecs

A codec (coder-decoder) converts analog voice signals to digital form and converts the compressed digital form back to the original analog voice signals for playback. Codecs may be free or licensed, and may be **lossless** (retaining everything in the original stream) or **lossy** (using lower bandwidth and compressing the stream, which reduces quality).

![Supported Codecs on Telnyx with their Bit-rates and descriptions.](_images/b577f4058b78dd2b.png)

#### DTMF notes

DTMF tones are not transported reliably in G.729 and cannot be expected to work under any conditions. They are also not expected to work reliably with G.722, but may do so. DTMF should always work perfectly in any G.711 stream, because DTMF tone frequencies were chosen to work with the PSTN and G.711 is the only codec in which no problems should be expected. Out-of-band DTMF tones can be used with any codec.

#### Fax notes

Fax tones work best with G.711 (uncompressed, for which they were designed). A fax call cannot work with G.729 because G.729 transports audio at 8 kbps while fax transmissions require higher bit rates. Faxes are also not expected to work over G.722. The only codecs for fax are G.711 mu-law and A-law. T.38 is sometimes a better option for fax transmissions. For PSTN-based calls, [prioritise G.711](https://support.telnyx.com/en/articles/4404448-sip-connection-inbound-outbound-settings) as the preferred codec if you wish to send and receive faxes through the Telnyx network.

### SDP message structure

In a SIP INVITE, the message body is SDP when specified as:

```
Content-Type: application/sdp
```

The body length is given by the `Content-Length` header, for example:

```
Content-Length: 344
```

Example SDP body:

```
v=0
o=Telnyx 1564556150 1564556151 IN IP4 64.16.248.213
s=Telnyx
c=IN IP4 64.16.248.213
t=0 0
m=audio 21250 RTP/AVP 9 0 8 18 101
a=rtpmap:9 G722/8000
a=rtpmap:0 PCMU/8000
a=rtpmap:8 PCMA/8000
a=rtpmap:18 G729/8000
a=fmtp:18 annexb=no
a=rtpmap:101 telephone-event/8000
a=fmtp:101 0-16
a=rtcp:21251 IN IP4 64.16.248.213
a=ptime:20
```

#### Version

`v=0` — The current version of SDP is 0.

#### Originator

`o=Telnyx 1564556150 1564556151 IN IP4 64.16.248.213` — Identifies the sender, the protocol used, and the sender's IP address. Here, Telnyx is the sender, using IPv4, at 64.16.248.213.

#### Session

`s=Telnyx` — The session title.

#### Connection information

`c=IN IP4 64.16.248.213` — Defines the connection type and address. Here, IPv4 is used and the sender's media address is 64.16.248.213.

#### Timing

`t=0 0` — Indicates the start and stop times for a session. Start and stop times of 0 indicate that the session is permanent and not bounded in time.

#### Media descriptor

`m=audio 21250 RTP/AVP 9 0 8 18 101` — A media line is present for each media type advertised within an SDP message. In this example, the media line informs the called party that the caller supports RTP audio on port 21250. The values 9, 0, 8, 18, and 101 are the various codecs described by attribute lines.

#### Attribute lines

```
a=rtpmap:9 G722/8000
a=rtpmap:0 PCMU/8000/1
a=rtpmap:8 PCMA/8000/1
a=rtpmap:18 G729/8000/1
a=fmtp:18 annexb=no
a=rtpmap:101 telephone-event/8000
a=fmtp:101 0-16
a=rtcp:21251 IN IP4 64.16.248.213
a=ptime:20
```

Each attribute line refers back to the media descriptor and the `<fmt>` values. With five formats (9, 0, 8, 18, 101), there are at least five attribute lines. Codec 18 describes itself twice, hence the two lines.

The format is `a=rtpmap:<payload type> <encoding name>/<clock rate> [/<encoding parameters>]`. In the example, the SDP advertises that the client supports G.722 at 8000 Hz, G.711 (PCMU and PCMA) at 8000 Hz, and G.729 at 8000 Hz.

The DTMF entries indicate that telephone events from RFC 2833 are available and that format 0–16 represents the ten digits plus `*`, `#`, A, B, D, E, and Flash.

The RTCP entry reports statistics about the ongoing call. Telnyx supports either RTCP+1 or RTCP mux at the connection level; RTCP+1 is most commonly used. In the example, the RTP port is 21250 and the RTCP port is 21251. RTCP mux multiplexes both RTP and RTCP through a single UDP port, simplifying NAT traversal. See [RFC 3550](https://tools.ietf.org/html/rfc3550) for more detail.

The `ptime` entry is the packetization interval. It is optional but recommended for encoding and packetization of the media. If no `ptime` is specified, the remote SIP entity uses its preferred packetization time. Telnyx generally specifies 20 ms, meaning RTP packets are sent and expected every 20 ms. Telnyx does not support other ptimes; specifying a different value may cause audio quality issues, so ensure ptimes match.
