---
source_url: https://support.telnyx.com/en/articles/8394071-hd-voice-number-feature
title: "HD Voice - Number Feature"
description: "Telnyx presents HD Voice, a number feature to enhance audio quality on PSTN calls made and received to eligible numbers… See Telnyx guidance and requirements."
scraped: 2026-07-08
content_hash: 6fa2966c0623147e084d3e4ffe9da2f570d08ece787566db1a4325c712304e8f
---







# HD Voice - Number Feature

Telnyx presents HD Voice, a number feature to enhance audio quality on PSTN calls made and received to eligible numbers… See Telnyx guidance and requirements.




## Overview

The HD Voice Number Feature enhances audio quality for PSTN calls made and received to and from eligible numbers within the United States and other supported countries.

## What is HD Voice? Feature Description

The HD Voice Number Feature enables customers to make and receive PSTN calls with high-definition (HD) audio quality.

In the context of HD Voice, which aims to enhance call quality by using wideband codecs, the codec negotiation process becomes even more crucial.

Unlike traditional PSTN calls that often use a fixed narrowband codec (such as G.711), HD Voice leverages wideband codecs like AMR-WB to deliver higher audio quality.

HD Voice calls require both endpoints to support and agree upon a compatible wideband codec during the negotiation process. This can be more complex when connection calls to PSTN, as not all networks or devices may be equipped to handle wideband codecs. Therefore, ensuring that both parties in a call support the same wideband codec is essential for a successful HD Voice call.

The negotiation process for HD Voice involves determining which wideband codec is supported by both ends of the call and selecting the highest quality option available. This negotiation considers factors like available bandwidth, device capabilities, and network conditions to optimize call quality.

While HD Voice offers superior audio quality, the challenge lies in ensuring that both ends of the call are equipped to handle wideband codecs.

This requires compatibility checks and, if necessary, fallback options to a suitable narrowband codec in case wideband support is not available.

## General Conditions for HD Voice Support

The call must use a carrier route listed under [Local calling coverage](#local-calling-coverage). The PSTN endpoint must support a wideband codec available on that route. Mobile calls also require a compatible device and access to the carrier’s HD Voice service, typically over LTE or 5G.

Within the Telnyx portal, your SIP connection must have one of the following wideband codecs enabled: OPUS, G.722, or AMR-WB. Additionally, the SIP device involved in the call must also support the selected codec.

## Importance of codecs on HD Voice

Codecs, short for coder-decoder, are essential tools in voice communication.

They encode and decode audio signals, compressing them for efficient transmission or storage.

In a voice call, a codec converts analog audio (what you hear during a call) into a digital format for network transmission, and then back to analog at the receiving end.

Different codecs have varying compression levels, audio quality, and bandwidth requirements. Some prioritize high-quality audio, while others are designed to conserve bandwidth for efficient transmission over networks.

**Opus Codec**: Opus is known for its adaptability and efficiency. It dynamically adjusts to varying network conditions, delivering exceptional audio quality even under less-than-ideal circumstances.

**AMR-WB Codec**: Adaptive Multi-Rate Wideband provides a broader frequency range, capturing more natural tonal nuances in speech for higher fidelity audio.

**G.722 Codec**: G.722 is a standard for high-quality speech and audio compression. It offers an extended frequency response range, ensuring crisp and clear voice reproduction even at lower bitrates.

Choosing the right codec ensures that audio quality matches the capabilities of HD voice technology.

This means experiencing conversations with utmost clarity, even in challenging network conditions.

***Please note:*** *While these conditions significantly increase the probability of experiencing HD audio, it's important to acknowledge that HD audio cannot be guaranteed due to the unpredictable nature of PSTN networks.*

## Receiving a call with HD Voice

For inbound calls to have HD voice support, the following conditions must be met:

The incoming call must originate from a compatible endpoint on a supported local carrier route and reach an HD Voice-enabled Telnyx number.

HD Voice feature can be enabled on the *Number Voice* settings as depicted below:

![](_images/ad9d3a60561b6fcd.png)

In the *My Numbers* overview page, the HD Voice option will be enabled for that Number and is visible under the services column.

![Services section.](_images/56ffd36dc30749d0.png)

Customers can also search for HD Numbers in the [Buy Numbers](https://portal.telnyx.com/#/numbers/buy-numbers) section of the portal.

![](_images/cb855811981dddaf.png)

The call must be routed to a SIP Connection configured with AMR-WB, G.722, or Opus HD voice codecs.
​
You can configure SIP Connection codecs in the *SIP Trunking* > *SIP Connections* > *Inbound* configuration > *Expert Settings*:

The SIP device receiving the call must support one of the above-mentioned codecs.

## Making an Outbound Call with HD Voice

For outbound calls to have HD voice support, the following conditions must be met:

The SIP device initiating the call must use one of the following codecs: AMR-WB, G.722, or Opus.

The destination endpoint and local carrier route must support a compatible wideband codec.

The Telnyx number used to make the outbound call must have HD Voice-enabled (also applied to CLI override)
​

Instructions on how to enable a Telnyx number with HD voice can be found [here](https://docs.google.com/document/d/1qBMtyraDDdZzCb7ED1GNeoK8jU9bIkeZOEW2qJk3z7s/edit#bookmark=id.ok6q60t9lgbx).

## Local calling coverage

HD Voice is supported for inbound and outbound local calls on the carrier routes below. The codecs in this table apply to the carrier leg. Your SIP endpoint can use a compatible wideband codec configured on your SIP connection.

| Country | Supported carrier | Wideband codecs on the carrier leg |
| --- | --- | --- |
| Australia | Over the Wire | G.722 |
| Austria | Yuutel | AMR-WB, G.722 |
| Germany | Outbox | AMR-WB, G.722 |
| Netherlands | SpeakUp | G.722 |
| United States | AT&T | AMR-WB, G.722 |
| United States | T-Mobile | AMR-WB |
| United States | Verizon | AMR-WB |

HD Voice availability depends on the specific number, route, and endpoint. If the call negotiates a narrowband codec on either leg, the audio will be narrowband.

## Risks and Considerations

While the conditions specified significantly increase the likelihood of HD audio, it's important to note that HD audio is not guaranteed due to the inherent unpredictability of PSTN networks.

## Frequently Asked Questions

**I see a yellow banner above the toggle to enable the feature "This number is not HD Voice capable"?**

The banner indicates that the selected number is ineligible for HD Voice. Eligibility varies by number and number type. Check the HD Voice feature filter when searching for numbers in Mission Control.

![](_images/9ef1f5f0a13f1d2a.png)

**What carriers support HD Voice?**

See [Local calling coverage](#local-calling-coverage) for supported routes and carrier codecs.

**Are there any recommended SIP devices that are best suited for the HD Voice feature?**

Any SIP device that supports one of the 3 supported HD Voice codecs are recommended.

**What happens if a codec mismatch occurs during a call?**

The call will be transcoded. If the mismatch is between two HD codecs (i.e. OPUS and AMR-WB) then the the audio quality will still be HD, but if the mismatch is between an HD codec and a non-HD codec (i.e. PCMU-AMR-WB) then the audio quality won’t be HD.

**How will the system handle fallback to a narrowband codec if wideband support is unavailable?**

By transcoding the audio.

**Will there be any interruptions or will it be seamless?**

Codecs are negotiated at the start of the call, so no interruptions.

**What kind of bandwidth is required to comfortably use the HD Voice Feature?**

HD Voice codecs have variable bit rates, but a high-speed internet connection is required for best results.

**Are there plans to extend the list of carriers that support the HD Voice Feature in the future?**

Yes.

**Can I use HD Voice outside the United States?**

Yes. See [Local calling coverage](#local-calling-coverage) for supported countries and carrier routes.

**How can customers check if their mobile device supports wideband codecs?**

By reading the user manual and checking the section about supported codecs.

**Can the HD Voice feature be enabled mid-month and, if so, will the cost be prorated?**

As of July 2025, there are no MRC's (monthly recurring charges) associated with HD Voice, it's free!

**How will the billing be reflected on the customer's monthly statement, just an aggregate count of HD Voice-enabled?**

Since HD Voice is now free, it won't be charged on your monthly statement.
