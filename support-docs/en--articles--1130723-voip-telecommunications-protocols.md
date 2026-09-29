---
source_url: https://support.telnyx.com/en/articles/1130723-voip-telecommunications-protocols
title: "VoIP/telecommunications protocols"
description: "RTP, UDP, TCP, SIP, SDP... See Telnyx guidance and requirements Learn more about VoIP/telecommunications protocols with Telnyx."
scraped: 2026-07-08
content_hash: 7554241e63e3b1937197bf1f4aa7f4f5fe950b63f1c4a26b9d38741bcfb71aa9
---







# VoIP/telecommunications protocols

RTP, UDP, TCP, SIP, SDP... See Telnyx guidance and requirements Learn more about VoIP/telecommunications protocols with Telnyx.




## VoIP Telecommunications protocols

* **RTP: Real Time Transport Protocol**
* **UDP: User Datagram Protocl**
* **TCP: Transmission Control Protocol**
* **SIP: Session Initiation Protocol**
* **SDP: Session Description Protocol**

## Description

First published in 1996 as RFC-1889 and superseded by RFC 3550 in 2003, **RTP** is a network protocol at the application layer which delivers audio and video over IP networks.
​
It typically runs over the **UDP** transport protocol on the transport layer but **TCP** can also be used. RTP carries the media stream and works in conjunction with the **SIP** protocol. RTP was designed for real time transmission of audio and video. UDP is the favored protocol to deliver RTP as it favours real time transmission systems because dropping packets is preferable than waiting on delayed packets. TCP, on the contrary, favors more reliability than reduced latency.
​
A RTP session is established for each multimedia stream. A session includes a port and an IP address. As audio and video use separate media streams, the receiver can deselect one or the other when it reaches their side.
​
RTP typically use the UDP ports between 1024 - 65535. Ports are negotiated through the SIP and **SDP** in order to form the session. Profiles and payloads are defined as-well. The profiles will define the codecs to be used to encode the payload data. Audio payload formats that we offer to use are G.711U, G.711A, G.7229 and OPUS. Typically video payload formats would be H.263, H.264 and MPEG-4.
