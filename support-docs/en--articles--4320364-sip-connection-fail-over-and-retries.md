---
source_url: https://support.telnyx.com/en/articles/4320364-sip-connection-fail-over-and-retries
title: "SIP Connection: Fail-over and Retries"
description: "In this article we will explain fail-over and retries and how they are used to make Telnyx so reliable. See Telnyx guidance and requirements."
scraped: 2026-07-08
content_hash: 14803d517e7ad7548e17a6895b5947b3408d505f0d3f3a4502fe23049762cc2d
---







# SIP Connection: Fail-over and Retries

In this article we will explain fail-over and retries and how they are used to make Telnyx so reliable. See Telnyx guidance and requirements.




The Telnyx Mission Control SIP Connections allow users to define multiple retries in case a call fails to connect. The policy for fail-over and retries is designed to make sure that calls always connect regardless of issues on Telnyx or the user side.

This policy depends on the type of Connection and other settings, and to explain how it works we need to define the following concepts:

## **Fail-over and Retry Concepts**

![Breaking Line](_images/682991ade0be9812.png)

1. **IP1:** Primary Signaling IP address of the **SIP Region** (e.g. for US SIP Region it's 192.76.120.10)
2. **IP2:** Secondary Signaling IP address of the **SIP Region** (e.g. for US SIP Region it's 64.16.250.10)
3. **Routes:** Each Connection can have **multiple routes**, for IP Auth connections each IP address is a route, for FQDN connections each FQDN is a route.
4. **Route preferences:** If a Connection routing method is **Sequential** then each route can be set as either Primary, Secondary, or Tertiary. Please note that this is also set at the Number level, and the Number settings **override** the Connection settings. If a Connection routing method is **Round Robin** then each route is attempted in random order.
5. **Call Connected:** A call attempt is considered "connected" (not to be confused with "answered") if it gets one of the following results:

* 486 Busy
* 404 Not Found
* 603 Declined
* Call rings (180/183) but it's not answered
* Call is answered (200 OK)

## Why does Telnyx keep sending SIP INVITEs when I reject the inbound calls?

If you do not wish to retry SIP INVITE's on inbound calls, please return a **603 declined response** as this is the SIP response code we honour for not retrying.

## **Inbound Call to Connection with only one route**

![Breaking Line](_images/682991ade0be9812.png)

1. Telnyx sends an attempt from IP1 to the single route of the Connection.
2. If the call attempt doesn't connect then Telnyx retries from IP2.

## **Inbound Call to Connection with multiple routes**

![Breaking Line](_images/682991ade0be9812.png)

1. Telnyx sends a call attempt from IP1 to the first route of the Connection.
2. If the call attempt doesn't connect then Telnyx sends an attempt from IP1 to the second route of the Connection.
3. If the call attempt doesn't connect then Telnyx sends an attempt from IP1 to the third route of the Connection.
4. If the call attempt doesn't connect then Telnyx sends an attempt from IP2 to the first route of the Connection.
5. If the call attempt doesn't connect then Telnyx sends an attempt from IP2 to the second route of the Connection.
6. If the call attempt doesn't connect then Telnyx sends an attempt from IP2 to the third route of the Connection.

## **Inbound Call to Cred Auth Connection**

![Breaking Line](_images/682991ade0be9812.png)

Please note that Telnyx will send call attempts to Cred Auth Connections only from the IP that the SIP device registered to, which can be either IP1 or IP2, and that SIP device can be configured to register against:

1. An IP address (either IP1 or IP2)
2. An FQDN that points only to IP1 (for US SIP region sip-anycast1.telnyx.com)
3. An FQDN that points only to IP2 (for US SIP region sip-anycast2.telnyx.com)
4. An FQDN with SRV records that point to IP1 as primary and IP2 as secondary (sip.telnyx.com) -> In this case the SIP device might end up registering to either IP1 or IP2 depending on its internal tests.

Also call attempts to Cred Auth connections go through a KSS (SIP registrar) for which there are 3 instances on each US region.

1. Telnyx sends a call attempt from primary KSS and then through IP1/2 to the Cred Auth Connection.
2. If the call attempt doesn't connect then Telnyx sends a call attempt from secondary KSS and then through IP1/2 to the Cred Auth Connection.
3. If the call attempt doesn't connect then Telnyx sends a call attempt from tertiary KSS and then through IP1/2 to the Cred Auth Connection.

## **Inbound Call to Connection and Number with Call Forward On Failure**

![Breaking Line](_images/682991ade0be9812.png)

Please note that Telnyx will send call attempts to Cred Auth Connections only from the IP that the SIP device registered to, which can be either IP1 or IP2, and that SIP device can be configured to register against:

1. Telnyx sends a call attempt from IP1 to the first route of the Connection.
2. If the call attempt doesn't connect then Telnyx sends an attempt from IP1 to the second route of the Connection.
3. If the call attempt doesn't connect then Telnyx sends an attempt from IP1 to the third route of the Connection.
4. If the call attempt doesn't connect then Telnyx sends an attempt to the Call Forward PSTN Number through the first Termination Carrier in route.
5. If the call attempt doesn't connect then Telnyx sends an attempt to the Call Forward PSTN Number through the second Termination Carrier in route.
6. If the call attempt doesn't connect then Telnyx sends an attempt to the Call Forward PSTN Number through the "n" Termination Carrier in route (max 10 termination carriers).

## **Inbound Call to Number with Call Forward Always**

![Breaking Line](_images/682991ade0be9812.png)

1. Telnyx sends a call attempt to the PSTN Number through the first Termination Carrier in route.
2. If the call attempt doesn't connect then Telnyx sends an attempt to the PSTN Number through the second Termination Carrier in route.
3. If the call attempt doesn't connect then Telnyx sends an attempt to the PSTN Number through the "n" Termination Carrier in route (max 10 termination carriers).

## **Inbound Call to Connection with SRV records**

![Breaking Line](_images/682991ade0be9812.png)

When an inbound call is routed to an FQDN Connection that uses SRV records, Telnyx will honor the SRV records as long as no port is specified in the SIP URI.

Telnyx will perform an SRV lookup and route the call based on the priority and weight returned by DNS. SRV records can be used for load balancing and failover across multiple SIP targets. If the first SRV target fails with a SIP 503 response, Telnyx will attempt the next highest priority target in the SRV list.

If no SRV record exists, Telnyx will fall back to an A-record lookup and use the default SIP port, 5060 for UDP/TCP or 5061 for TLS. If the domain cannot be resolved, the call will fail with SIP 478 Unresolvable Destination.

Important: if a port is included in the SIP URI, Telnyx bypasses SRV lookup and performs an A-record lookup instead. To use SRV failover, configure the FQDN without a port.

For more details, see: [How Telnyx Handles SRV Records for SIP Calls.](https://support.telnyx.com/en/articles/10666839-how-telnyx-handles-srv-records-for-sip-calls)

## **Outbound Call to PSTN Number**

![Breaking Line](_images/682991ade0be9812.png)

1. Telnyx sends a call attempt to the PSTN Number through the first Termination Carrier in route.
2. If the call attempt doesn't connect then Telnyx sends an attempt to the PSTN Number through the second Termination Carrier in route.
3. If the call attempt doesn't connect then Telnyx sends an attempt to the PSTN Number through the "n" Termination Carrier in route (max 10 termination carriers).

## How to configure primary and secondary proxies for Inbound and Outbound failover and redundancy

![Breaking Line](_images/682991ade0be9812.png)

1. **Inbound**

   1. Please ensure your SIP endpoints and network ACLs or failovers allow calls from not only the primary but also the secondary Telnyx SIP proxy IP.
2. **Outbound**

   1. If you are using IP addresses please use the IP address 192.76.120.10 as primary and 64.16.250.10 as secondary for the US region.
   2. If you are using FQDNs with A DNS record resolution please use sip.telnyx.com as the primary FQDN and sip-anycast2.telnyx.com as the failover for the US region.
   3. If you are using FQDNs with SRV DNS record resolution (**RECOMMENDED**) please use the FQDN [sip.telnyx.com](https://sip.telnyx.com/) for the US region and failover will be automatically configured.
3. For other regions (sip.telnyx.eu, sip.telnyx.ca, sip.telnyx.com.au etc) please change the domain accordingly.

   1. You can see all available regions here: <https://sip.telnyx.com/>

---

Related Articles

[SIP Connection: Types](https://support.telnyx.com/en/articles/4245868-sip-connection-types)[SIP Connection: Inbound & Outbound Settings](https://support.telnyx.com/en/articles/4404448-sip-connection-inbound-outbound-settings)[Telnyx SIP Response Codes](https://support.telnyx.com/en/articles/4409457-telnyx-sip-response-codes)[How Telnyx Handles SRV Records for SIP Calls](https://support.telnyx.com/en/articles/10666839-how-telnyx-handles-srv-records-for-sip-calls)[How to Configure SIP Attach using a UAC Connection](https://support.telnyx.com/en/articles/14805261-how-to-configure-sip-attach-using-a-uac-connection)

Did this answer your question?

😞😐😃
