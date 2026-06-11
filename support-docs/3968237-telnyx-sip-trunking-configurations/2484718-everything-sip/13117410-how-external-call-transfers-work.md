---
source_url: https://support.telnyx.com/en/articles/13117410-how-external-call-transfers-work
scraped: 2026-06-11
---

How External Call Transfers Work | Telnyx Help Center

[Skip to main content](#main-content)

# How External Call Transfers Work

Written by Telnyx Engineering

April 10, 2026

Table of contents

The External Call Transfer scenario happens when your SIP endpoint receives an inbound call from PSTN through Telnyx and then transfers that call to an outside number, keeping the original PSTN number as the originator.

From a Telnyx perspective, these are two different calls, and the transferred call by itself is considered an outbound call from a non-Telnyx number.

Telnyx has implemented a mechanism to handle External Call Transfer scenarios so that these outbound calls are automatically allowed and routed to the destination.

This guide explains how Telnyx validates these transfers to keep your calls secure and properly authenticated.

# Overview

If you receive calls via your SIP endpoint through a Telnyx SIP trunk and need to transfer a caller to an external destination, your endpoint will initiate a **new outbound call** to that number. Telnyx then verifies that this outbound call is tied to the original inbound call.

---

# How the Flow Works

How the Flow Works

1. Caller A dials your Telnyx number B.
2. The call is delivered by Telnyx to your SIP endpoint, from A to B.
3. Your SIP endpoint decides to transfer the call to number C.
4. Your endpoint places a new outbound call, from A to C.
5. This outbound call must include proper diversion information to indicate that it’s a transfer of the original inbound call from A to B for it to be automatically allowed by Telnyx.

---

# What Telnyx Checks

To allow the External Call Transfer, Telnyx performs two validations when it receives an outbound call attempt:

1. Active inbound call match.

   1. Telnyx confirms that there is an active inbound call from A to B.
2. Presence of Diversion Headers.

   1. The new outbound call from A to C must include a SIP Diversion header showing B.

Example of an accepted call flow.   
​

[![](https://downloads.intercomcdn.com/i/o/ltcafuzd/2144680188/7caf0f180e729729a81b351b87d1/image.png?expires=1781167500&signature=db0595af7b41dfcf5a19a26d1bdf8eae0531fa5b0244e8a280467ad4f21fd238&req=diEjEs92nYBXUfMW1HO4zeLS4cGENgEXsxFVTvCk5CVxPmM3XrxZA2gdizaU%0AH1ozOSKDpMgB75OPRUA%3D%0A)](https://downloads.intercomcdn.com/i/o/ltcafuzd/2144680188/7caf0f180e729729a81b351b87d1/image.png?expires=1781167500&signature=db0595af7b41dfcf5a19a26d1bdf8eae0531fa5b0244e8a280467ad4f21fd238&req=diEjEs92nYBXUfMW1HO4zeLS4cGENgEXsxFVTvCk5CVxPmM3XrxZA2gdizaU%0AH1ozOSKDpMgB75OPRUA%3D%0A)

---

# When the Transfer Is Rejected

If the Diversion header is missing or incorrect, or Telnyx cannot match the outbound call to an active inbound call, Telnyx will reject the request by default with `403 Unverified origination number D51`.  
This prevents unauthorized or spoofed calls from being placed using your number.

Example of a rejected flow.  
​

[![](https://downloads.intercomcdn.com/i/o/ltcafuzd/2144678498/e5d13f9859d85e36d62d5f2bfcae/image.png?expires=1781167500&signature=cf9906ff2f3bc3e7988758aea774778bd795e694694e90719f9c42e507e36657&req=diEjEs95lYVWUfMW1HO4zSX0C8AzQb4Vwo1178HzTSv5Nz2p2fMqi%2BSqXqmQ%0AHv57sRGcx%2F3ZYH9qgTQ%3D%0A)](https://downloads.intercomcdn.com/i/o/ltcafuzd/2144678498/e5d13f9859d85e36d62d5f2bfcae/image.png?expires=1781167500&signature=cf9906ff2f3bc3e7988758aea774778bd795e694694e90719f9c42e507e36657&req=diEjEs95lYVWUfMW1HO4zSX0C8AzQb4Vwo1178HzTSv5Nz2p2fMqi%2BSqXqmQ%0AHv57sRGcx%2F3ZYH9qgTQ%3D%0A)

---

# Programmable Voice

It is possible to transfer an inbound call to the Telnyx network to an external PSTN number using Programmable Voice while preserving the non-Telnyx origination number, and there are different mechanisms to do this:

## Voice API Transfer Command

A Voice API Transfer command instructs Telnyx to transfer an established inbound call to a new destination. In that case the non-Telnyx origination number is allowed.

## Voice API Dial + Bridge

A Voice API Dial request triggers a new outbound call, and if that request is bridged to an existing inbound call then the non-Telnyx origination number is allowed.

For the Dial request to be considered a bridge it should contain the following parameters:

* `link_to` parameter set to `call_control_id` of the bridging call
* `bridge_intent` parameter set to `true`

## TeXML <Dial> Command

TeXML `<Dial>` instructs Telnyx to place a new outbound call and connect it to the existing inbound call. In that case the non-Telnyx origination number is allowed.

---

Related Articles

[Call Forwarding](https://support.telnyx.com/en/articles/1130657-call-forwarding)[SIP Connection: Fail-over and Retries](https://support.telnyx.com/en/articles/4320364-sip-connection-fail-over-and-retries)[Configuring Call Control/TeXML Applications - Voice API](https://support.telnyx.com/en/articles/4374050-configuring-call-control-texml-applications-voice-api)[SIP Connection: Inbound & Outbound Settings](https://support.telnyx.com/en/articles/4404448-sip-connection-inbound-outbound-settings)[Understanding SIP PRACK Protocol](https://support.telnyx.com/en/articles/6902981-understanding-sip-prack-protocol)

Did this answer your question?

😞😐😃

Table of contents
