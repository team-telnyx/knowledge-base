---
source_url: https://support.telnyx.com/en/articles/9718403-microsoft-teams-emergency-call-routing
scraped: 2026-06-11
---

Microsoft Teams Emergency Call Routing | Telnyx Help Center

[Skip to main content](#main-content)

# Microsoft Teams Emergency Call Routing

Written by Telnyx Engineering

December 1, 2025

Table of contents

In today's fast-paced digital world, ensuring that emergency calls are routed accurately and efficiently is more critical than ever.

Whether you're managing a large enterprise or a small business, having a reliable system that directs emergency calls to the correct Public Safety Answering Point (PSAP) can make all the difference in critical situations.

Microsoft Teams, a leading communication platform, integrates advanced technologies to support emergency services, ensuring that when a call is made to emergency numbers, it is quickly and correctly routed.

One key component in this process is the use of [**Dynamic Location Routing**](https://learn.microsoft.com/en-us/microsoftteams/configure-dynamic-emergency-calling).

This feature ensures that emergency calls made through Microsoft Teams are directed to the right location, taking into account the caller's current position.

This article will walk you through how Microsoft Teams, in collaboration with Telnyx, uses Dynamic Location Routing to enhance the accuracy and reliability of emergency call handling.

We’ll explore how precise location information is embedded within the call data, enabling seamless communication with emergency services.

##

## Microsoft Teams Operator Connect and Direct Routing Dynamic Location Routing: Technical Overview

**PIDF-LO** (Presence Information Data Format Location Object) is a standardized protocol crucial for enhancing the effectiveness of emergency calls by embedding precise location data.

This information is essential for VoIP providers, enabling them to route calls accurately to the appropriate Emergency Public Safety Answering Point (PSAP).

Given the critical importance of emergency services, PIDF-LO supports multiple implementations.

Currently, Telnyx leverages Microsoft's **Dynamic Location Routing** to ensure rapid and accurate routing of emergency calls.

In this implementation, Microsoft Teams includes emergency address details within the SIP INVITE MIME part.

Telnyx then processes this information to route the call accurately to the appropriate emergency PSAP.

Below is an example of the metadata included in a Microsoft Teams SIP INVITE when an emergency call is placed to an emergency number from a country that supports Dynamic Location Routing:

```
<?xml version="1.0" encoding="utf-8"?>  
<presence xmlns:xsd="http://www.w3.org/2001/XMLSchema"   
          xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"   
          entity="-"   
          xmlns="urn:ietf:params:xml:ns:pidf">  
    
  <tuple id="tuple0">  
    <status>  
      <geopriv xmlns="urn:ietf:params:xml:ns:pidf:geopriv10">  
          
        <location-info>  
          <Point srsName="urn:ogc:def:crs:EPSG::4326" xmlns="http://www.opengis.net/gml">  
            <pos>33.38075 -111.75344</pos>  
          </Point>  
          <civicAddress xmlns="urn:ietf:params:xml:ns:pidf:geopriv10:civicAddr">  
            <country>US</country>  
            <A1>AZ</A1>  
            <A3>Mesa</A3>  
            <PRD/>  
            <RD>South Val Vista Drive</RD>  
            <STS/>  
            <POD/>  
            <HNO>1939</HNO>  
            <HNS/>  
            <LOC/>  
            <NAM>Default Directory</NAM>  
            <PC>85204</PC>  
            <ELIN/>  
          </civicAddress>  
        </location-info>  
          
        <usage-rules>  
          <retransmission-allowed xmlns="urn:ietf:params:xml:ns:pidf:geopriv10:basicPolicy">  
            true  
          </retransmission-allowed>  
        </usage-rules>  
          
        <method>ASSIST</method>  
          
        <confidence pdf="normal" xmlns="urn:ietf:params:xml:ns:geopriv:conf">  
          low  
        </confidence>  
          
      </geopriv>  
    </status>  
  </tuple>  
    
</presence>
```

The current method for PIDFLO supported are LIS or ASSIST This XML data is processed by Telnyx to determine the correct PSAP for routing the emergency call.

By leveraging this sophisticated technology, Microsoft Teams and Telnyx ensure that every emergency call is handled with the utmost accuracy, providing peace of mind for users who rely on these services in critical moments.

---

Related Articles

[E911 Setup Guide](https://support.telnyx.com/en/articles/1130683-e911-setup-guide)[How do I test E911 service?](https://support.telnyx.com/en/articles/1130709-how-do-i-test-e911-service)[SIP URI Calling](https://support.telnyx.com/en/articles/2925713-sip-uri-calling)[Configuring Telnyx with Microsoft Teams Direct Routing](https://support.telnyx.com/en/articles/5253876-configuring-telnyx-with-microsoft-teams-direct-routing)[Operator Connect Guide - Microsoft Teams](https://support.telnyx.com/en/articles/7260976-operator-connect-guide-microsoft-teams)

Did this answer your question?

😞😐😃

Table of contents
