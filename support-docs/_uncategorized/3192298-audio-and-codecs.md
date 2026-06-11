---
source_url: https://support.telnyx.com/en/articles/3192298-audio-and-codecs
scraped: 2026-06-11
---

Audio and Codecs | Telnyx Help Center

[Skip to main content](#main-content)

# Audio and Codecs

Here we will explain session description protocol and how you can utilize them for your business.

Written by Dillin

April 4, 2024

Table of contents

# Introduction to SDP

When you send or receive an INVITE, via the SIP protocol with Telnyx, it should contain a message body that has content length greater than 0. This message body is where the parameters of the **session description protocol** (SDP) are located. In other words, this is where you define your multi-media session capabilities.   
​  
​**Note**: SDP does not deliver any media but is used in conjunction with the Real-time Transport Protocol (RTP), which handles the delivery of media over internet protocol (IP) networks.

We'll discuss some high level details about the media and codec parameters but you can always find the full details of the SDP in [RFC 4566](https://tools.ietf.org/html/rfc4566).

In Voice over IP (VoIP), multi-media can consist of either audio or video but are not limited to just these two. This information is usually sent in RTP packets using the user datagram protocol (UDP) transport.  
​  
You'll often find the term "media" used interchangeably with audio, voice or RTP.   
​  
You can see a list of our media IP's that we will send traffic from as-well as the codecs that we support on our [sip.telnyx.com](https://sip.telnyx.com/) webpage.

## Debugging Tool for SDP

Using the [debugging tool](https://portal.telnyx.com/#/app/debugging/sip-call-flow-tool) on your mission control portal account, you can view the SIP call flow along with reading the contents of the SIP messages. This provides more granular insight into how the SIP signalling was established and with what parameters.

The SDP can be located in our SIP INVITE message to your connection on an inbound call. Telnyx will always provide you with an SDP in our INVITEs on inbound calls, this is called early offer. This allows us to show you our accepted list capabilities and we will order them in ascending priority.  
​  
SDP can also be located in our 183 or 200 OK message on your outbound calls. If you send us an INVITE with no SDP, this is called a late offer. When the call is answered, a 200 OK with SDP is sent back to the caller and the caller responds with an ACK. Usually, the callers ACK will now contain the SDP that would generally be sent in the INVITE. With this change in SDP placement, the caller gets to decide which codec will be used for this session.

## Codecs

A Codec, short for **coder-decoder** converts analog voice signals to digital form and converts the compressed digital form to the original analog voice signals so that it can be replayed.  
​   
There are many different types of codecs available, some can be used freely while others require purchasing a license.  
​  
You can have **lossless** or **lossy** codecs; lossless codecs retain everything in the original stream while lossy codecs user lower bandwidth and will compress the stream which will reduce the quality of the audio stream.

[![Supported Codecs on Telnyx with their Bit-rates and descriptions. ](https://downloads.intercomcdn.com/i/o/137981711/27d043b7a5a75510e64793ea/Screenshot+from+2019-07-31+14-22-34.png?expires=1781168400&signature=c6e5959708a55c8dd926bcbe4d00b6fea6c4cd2ddbe25fe81197602bf0c087c6&req=dSMgH8F%2FmoBeFb4f3HP0gHbR1yjvgyPdJBO34RcQF4yOJbhVT%2Bw9IGiQ8AeV%0Afn5UFKkCp9UdKtYxyg%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/137981711/27d043b7a5a75510e64793ea/Screenshot+from+2019-07-31+14-22-34.png?expires=1781168400&signature=c6e5959708a55c8dd926bcbe4d00b6fea6c4cd2ddbe25fe81197602bf0c087c6&req=dSMgH8F%2FmoBeFb4f3HP0gHbR1yjvgyPdJBO34RcQF4yOJbhVT%2Bw9IGiQ8AeV%0Afn5UFKkCp9UdKtYxyg%3D%3D%0A)

### **Note on DTMF:**

The tones for [DTMF](https://support.telnyx.com/en/articles/1130710-what-is-dtmf) are not transported reliably in G.729 and cannot be expected to work under any conditions. They're also not expected to work reliably with G.722, but may do so. DTMF should always work perfectly in any G.711 stream. DTMF tone frequencies were chosen to work with the PSTN, so must work reliably when encoded with G.711, which is the only codec in which we should expect no problems.

Outband DTMF tones can be used with any codec.

### **Note on Fax:**

Fax tones work best with G.711 (for which they were designed - uncompressed). A fax call cannot work with G.729; as a thought experiment, note that G.729 transports audio at 8kbps but fax transmissions must work at higher bit rates; on that basis, it's simply impossible for a fax to work over G.729.

Faxes also are not expected to work over G.722. The only codecs for fax are G.711 mu-law and A-law. Better, sometimes, is for customers to use T.38 for fax transmissions. Some fax calls may work with G.722, but reliability should not be expected.

For PSTN based calls, please ensure that you [prioritise G.711](https://support.telnyx.com/en/articles/4404448-sip-connection-inbound-outbound-settings) as the preferred codec should you wish to send and receive faxes through our network.

## Session Description Protocol - SDP

In a SIP INVITE message, we know the message body is SDP when it's specified as

```
Content-Type: application/sdp
```

We know that the message body of this content type has length because it was specified in the **Content-Length** header such as

```
Content-Length: 344
```

Here is an example of the parameters of an SDP body message:

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

We'll now digest the above information and explain what each parameter means below.

### **Version**

v=0

The current version of SDP is 0 (zero).

### **Originator**

o=Telnyx 1564556150 1564556151 IN IP4 64.16.248.213

This section identifies the sender, the protocol the sender is using, and the sender’s IP address. In this case, Telnyx is the sender, using IPV4, and lives at 64.16.248.213.

### **Session**

s=Telnyx

This is the session title.

### **Connection Information**

c=IN IP4 64.16.248.213

This field defines the connection type and address. Here, were are using IPV4 and the sender’s media address is 64.16.248.213.

### **Timing**

t=0 0

Timing is used to indicate the start and stop times for a session. Start and stop times of 0 (zero) indicates that the session is permanent and not bounded time-wise.

### **Media Descriptor**

m=audio 21250 RTP/AVP 9 0 8 18 101

A media line will be present for each media type advertised within an SDP message. The format is:

*m=*

In this example, the media line informs the called party that the caller supports RTP audio on port 21250. The 9, 0, 8, 18, and 101 are the various codecs that will be described by attribute lines.

### **Attribute Lines**

a=rtpmap:9 G722/8000  
a=rtpmap:0 PCMU/8000/1  
a=rtpmap:8 PCMA/8000/1  
a=rtpmap:18 G729/8000/1  
a=fmtp:18 annexb=no   
a=rtpmap:101 telephone-event/8000   
a=fmtp:101 0-16   
a=rtcp:21251 IN IP4 64.16.248.213   
a=ptime:20

Each attribute line refers back to the Media Descriptor and the <fmt> values. Since we had five formats (9, 0, 8, 18, 101) we will have at least five attribute lines. Codec 18 describes itself twice, hence the two lines.

The format of these attributes is:

a=rtpmap:<payload type> <encoding name>/<clock rate> [/<encoding parameters>]

In our example, the SDP advertises that the client supports G722 at 8000 Hz, G.711 (PCMU and PCMA — pulse code modulation u-law and a-law) at 8000 Hz and G.729 at 8000 Hz.  
​  
The below entries indicate Dual Tone Multi-Frequency (DTMF). This informs the called party that telephone event from RFC 2833 is available and that the format 0-16 represents the ten digits plus \*, #, A, B, D, E, and Flash.

```
a=rtpmap:101 telephone-event/8000  
a=fmtp:101 0-16
```

The below entry is called Real-time Control Protocol (RTCP). As you already know, RTP is used to transmit media between endpoints. As the media traverses the endpoints, RTCP packets are generated periodically by both the caller and the called party.  
​  
However, unlike RTP, they don’t contain media. Instead, RTCP packets are used to report statistics about the ongoing call. Telnyx provides the ability to use either RTCP+1 or RTCP mux at the connection level.   
​  
Most of the time RTCP+1 is employed. You'll notice that our RTP port was 21250 in the m= attribute and that the RTCP port is 21251. Again, more specific details can be found in [RFC 3550](https://tools.ietf.org/html/rfc3550). RTCP mux is multiplexing both the RTP and RTCP through a single UDP port. One of the reasons why RTCP mux is used is for simplifying NAT traversal since only a single port is used for media and control messages.

```
a=rtcp:21251 IN IP4 64.16.248.213
```

The last entry relates to ptime. This is the packetization interval. It's an optional field but it is recommended for the encoding / packetization of the media. If no ptime is specified, it means that the remote SIP entity uses whatever packetization time it prefers. Telnyx generally specifies the packetization time of 20 ms. This means we will send and expect to receive RTP packets every 20 ms.

```
a=ptime:20
```

Telnyx does not support any other ptimes and if you specify any other ptime, you may experience audio quality issues. Please ensure ptimes match.  
​

## Conclusion

We've discussed a high level overview of the session description protocol along with codecs that Telnyx supports. This information should provide you with a good solid foundation that you can work from, especially when it comes to debugging any SIP or audio quality issues. Some special notes were included, especially around the disadvantages of using certain codecs over fax or dtmf.   
​  
If you have anymore questions, please feel free to reach out to our NOC team!

---

Related Articles

[Configuring a Cisco CUBE/CUCM IP Trunk](https://support.telnyx.com/en/articles/1130606-configuring-a-cisco-cube-cucm-ip-trunk)[Cisco: Configure a Cisco CME IP Trunk](https://support.telnyx.com/en/articles/1130612-cisco-configure-a-cisco-cme-ip-trunk)[Configuring a Cisco CME Credentials Trunk](https://support.telnyx.com/en/articles/1130668-configuring-a-cisco-cme-credentials-trunk)[Configuring a Cisco CUBE/CUCM SIP Trunk](https://support.telnyx.com/en/articles/1130673-configuring-a-cisco-cube-cucm-sip-trunk)[What is DTMF? and how to configure it on Telnyx](https://support.telnyx.com/en/articles/1130710-what-is-dtmf-and-how-to-configure-it-on-telnyx)

Did this answer your question?

😞😐😃

Table of contents
