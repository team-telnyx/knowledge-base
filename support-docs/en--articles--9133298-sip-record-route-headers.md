---
source_url: https://support.telnyx.com/en/articles/9133298-sip-record-route-headers
title: "SIP - Record Route Headers"
description: "Understanding the Importance of Route Headers. See Telnyx guidance and requirements Learn more about SIP - Record Route Headers with Telnyx."
scraped: 2026-07-08
content_hash: 7203a16ce63345259d343e127beaba410ca73e0c7020352c148bd70276fa7fde
---







# SIP - Record Route Headers

Understanding the Importance of Route Headers. See Telnyx guidance and requirements Learn more about SIP - Record Route Headers with Telnyx.




## **Why Do Some Calls Drop or Fail to Connect?**

Have you ever wondered why some calls drop unexpectedly or why media doesn't flow during a session? The answer often lies in the correct configuration and handling of SIP headers. In this article, we’ll explore two critical headers in the Session Initiation Protocol (SIP) — the **Via** and **Record-Route** headers. These headers play a pivotal role in routing SIP messages, ensuring seamless call setups and media exchanges across IP networks.

By understanding these headers, you’ll be better equipped to troubleshoot and configure SIP systems effectively, minimising call disruptions and improving the user experience.

## What Are SIP Headers?

SIP is a signaling protocol used to initiate, manage, and terminate real-time communication sessions like voice and video calls. Headers in SIP act like GPS markers, guiding messages through the network. Among these, the Via and Record-Route headers stand out for their role in ensuring messages and responses reach the intended destinations.

## Understanding Via and Record-Route Headers in SIP

The Record-Route and Via headers are fundamental components of the Session Initiation Protocol (SIP), which is a signalling protocol used for initiating, managing, and terminating real-time sessions that involve video, voice, messaging, and other communications applications across IP networks. Both headers play critical roles in SIP's operation, ensuring proper routing of requests and responses between SIP entities. Their development and use are closely tied to the history and evolution of SIP itself.

### Via Header

The Via header is used to track the path of request messages as they traverse through the network of SIP servers to reach the intended recipient. It also provides a route for the responses to follow back to the originator. Each SIP proxy or server that forwards a request adds its address to the top of the Via header list. When the response is generated, it travels back through the list of Via headers, ensuring it follows the same path back to the originator.

The Via header has been part of SIP since its inception. SIP was developed by the Internet Engineering Task Force (IETF) and first standardised in RFC 2543 in 1999. The Via header was designed to solve the problem of response routing in IP networks, where requests could traverse multiple nodes, and responses needed a way to navigate back through the same nodes.

### Record-Route Header

The Record-Route header is used by SIP proxies to ensure that the signalling for subsequent SIP messages (such as mid-dialog requests) follows the same path as the initial request. When a SIP proxy wants to stay in the path of future requests in a dialog, it adds a Record-Route header to the initial INVITE request. This ensures that all subsequent messages within the same dialog traverse through the recorded route, enabling features like billing, call recording, or session management to be applied consistently.

Like the Via header, the Record-Route header has been a part of SIP since its early days. It was introduced to address the need for maintaining the signalling path for the duration of a SIP session, especially in complex scenarios involving multiple proxies and network elements. The concept of recording the route was crucial for deploying SIP in real-world networks, where the control over media and signalling paths needed to be maintained for the functionality and security of communication sessions.

Both headers reflect SIP's flexibility and its ability to navigate the complexities of IP network architectures. Over the years, SIP has evolved through various RFCs (Request for Comments), with significant updates including RFC 3261 in 2002, which solidified many of the protocol's core operations, including the behaviours of the Via and Record-Route headers. These headers ensure that SIP can operate effectively over the diverse and distributed nature of the Internet, supporting the reliable delivery and routing of communication sessions across multiple hops and domains.

## Introduction

When managing SIP (Session Initiation Protocol) communications, ensuring seamless call setup and media flow is crucial for both service providers and their customers. A common issue encountered during SIP transactions is the failure of ACK messages to reach the end device, confirming the final response to the initial SIP INVITE. This can prevent the establishment of media sessions, leading to call setup failures and, ultimately, calls being dropped with a SIP BYE message and the reason as "**ack\_timeout.**" In this article, we'll delve into the intricacies of the Route headers in calls and explain why omitting these headers in a 200 OK response can cause such problems.

## Breaking Down the Via and Record-Route Headers

### **Via Header**

The **Via header** tracks the path of SIP request messages as they traverse the network and ensures responses follow the same path back to the originator. Each SIP proxy or server that forwards a request adds its address to the top of the Via header list. When a response is generated, it uses this list to navigate back to the originator. This mechanism ensures that SIP messages follow the same path in both directions, preventing misrouting.

Example:

* **Forward Path (Request)**: A Via header is added by each server as the request is forwarded.
* **Backward Path (Response)**: The response uses the Via headers to trace its way back.

### **Record-Route Header**

The **Record-Route header** is added by SIP proxies to ensure all subsequent messages in a session (e.g., mid-dialog requests like ACKs or BYEs) follow the same path as the initial INVITE. This is crucial for applying features like call recording, session management, or billing consistently.

Without Record-Route headers, subsequent messages might bypass critical network elements, potentially breaking functionality.

Example:

* A SIP proxy includes a Record-Route header in an INVITE request.
* This header is mirrored in the 200 OK response, ensuring future messages follow the same route.

When a callee sends a 200 OK response to accept an INVITE request, this response should include Route headers that mirror the path taken by the initial INVITE. This inclusion ensures that the ACK message, which confirms receipt of the 200 OK, is routed back through the same network elements, reaching the callee and signalling that the session can proceed with media exchange.

If the 200 OK omits these Route headers, the network may not have the necessary information to route the ACK back to the callee correctly. As a result, even though the call appears to be established from the perspective of the initiating party (such as Telnyx), the lack of ACK receipt at the callee's end means the session cannot transition to media exchange. Consequently, without media flow, the call is eventually terminated with a "**ack\_timeout**" hang-up cause.

---

## SIP Record Route Example

To provide a clear understanding, let's illustrate two examples based on the provided SIP INVITE and 200 OK messages. These examples aim to showcase the issue arising from the omission of Record-Route headers in the 200 OK response and how their inclusion ensures successful SIP call establishment.

### Example 1: Problematic Scenario Without Record-Route Headers

#### Telnyx SIP INVITE to Customer

```
INVITE sip:+12345678901@sip.example.com:5060 SIP/2.0
Record-Route: <sip:192.76.120.10;r2=on;lr;ftag=BUXDty7v06tXH>
Record-Route: <sip:10.255.0.1;r2=on;lr;ftag=BUXDty7v06tXH>
Via: SIP/2.0/UDP 192.76.120.10;branch=z9hG4bK2d69.8e8f5f5fb057db25a37e7b57b6da8e73.0
Via: SIP/2.0/UDP 10.13.177.4:6000;received=10.13.177.4;rport=6000;branch=z9hG4bKr588213p7Z0Sp
Max-Forwards: 60
From: "+19876543210" <sip:+19876543210@sip.telnyx.com>;tag=BUXDty7v06tXH To: <sip:+12345678901@sip.example.com:5060>
Call-ID: 684d7abc-1234-4567-891a-444dd7a7b77d
CSeq: 12123802 INVITE
Content-Type: application/sdp
...
```

#### Customer's 200 OK Response (Without Record-Route Headers)

```
SIP/2.0 200 OK
Via: SIP/2.0/UDP 192.76.120.10;branch=z9hG4bK2d69.8e8f5f5fb057db25a37e7b57b6da8e73.0
Via: SIP/2.0/UDP 10.13.177.4:6000;received=10.13.177.4;rport=6000;branch=z9hG4bKr588213p7Z0Sp
To: sip:+12345678901@sip.example.com:5060;tag=8b240ac5236e0c71
From: sip:+19876543210@sip.telnyx.com;tag=BUXDty7v06tXH
Call-ID: 684d7abc-1234-4567-891a-444dd7a7b77d
CSeq: 12123802 INVITE
Contact: <sip:+12345678901@another.example.com:5060>
Content-Type: application/sdp
...
```

Without the Record-Route headers in the 200 OK response, the ACK message sent by Telnyx might not follow the intended path, potentially failing to reach the customer's system. This misrouting can prevent the call from being fully established, leading to issues such as calls not connecting or being dropped unexpectedly.

---

### Example 2: Successful Scenario With Record-Route Headers

#### Telnyx SIP INVITE to Customer (Same as Example 1)

```
INVITE sip:+12345678901@sip.example.com:5060 SIP/2.0
Record-Route: <sip:192.76.120.10;r2=on;lr;ftag=BUXDty7v06tXH>
Record-Route: <sip:10.255.0.1;r2=on;lr;ftag=BUXDty7v06tXH>
Via: SIP/2.0/UDP 192.76.120.10;branch=z9hG4bK2d69.8e8f5f5fb057db25a37e7b57b6da8e73.0
Via: SIP/2.0/UDP 10.13.177.4:6000;received=10.13.177.4;rport=6000;branch=z9hG4bKr588213p7Z0Sp
Max-Forwards: 60
From: "+19876543210" <sip:+19876543210@sip.telnyx.com>;tag=BUXDty7v06tXH To: <sip:+12345678901@sip.example.com:5060>
Call-ID: 684d7abc-1234-4567-891a-444dd7a7b77d
CSeq: 12123802 INVITE
Content-Type: application/sdp
...
```

#### Customer's 200 OK Response (With Record-Route Headers)

```
SIP/2.0 200 OK
Via: SIP/2.0/UDP 192.76.120.10;branch=z9hG4bK2d69.8e8f5f5fb057db25a37e7b57b6da8e73.0
Via: SIP/2.0/UDP 10.13.177.4:6000;received=10.13.177.4;rport=6000;branch=z9hG4bKr588213p7Z0Sp
Record-Route: <sip:192.76.120.10;r2=on;lr;ftag=BUXDty7v06tXH>
Record-Route: <sip:10.255.0.1;r2=on;lr;ftag=BUXDty7v06tXH>
To: sip:+12345678901@sip.example.com:5060;tag=8b240ac5236e0c71
From: sip:+19876543210@sip.telnyx.com;tag=BUXDty7v06tXH
Call-ID: 684d7abc-1234-4567-891a-444dd7a7b77d
CSeq: 12123802 INVITE
Contact: <sip:+12345678901@another.example.com:5060>
Content-Type: application/sdp
...
```

By including the Record-Route headers in the 200 OK response, the customer ensures that the ACK message sent by Telnyx correctly follows the predefined path through any intermediate proxies.

---

### Example 3: Problematic Scenario Without Record-Route Headers

#### Customer's SIP INVITE to Telnyx

This scenario illustrates what happens when a client initiates a SIP INVITE to Telnyx, and subsequent SIP messages (like ACK) fail due to misconfigured or reordered **Route headers** in the client’s response.

```
INVITE sip:+12345678901@sip.telnyx.com:5060 SIP/2.0
Via: SIP/2.0/UDP 10.1.1.1:5060;branch=z9hG4bKclient1234
Max-Forwards: 70
From: "+19876543210" <sip:+19876543210@client.example.com>;tag=clienttag123
To: <sip:+12345678901@sip.telnyx.com>
Call-ID: 1234abcd@client.example.com
CSeq: 100 INVITE
Contact: <sip:+19876543210@10.1.1.1:5060>
Content-Type: application/sdp
...
```

#### Telnyx’s 200 OK Response (With Correct Record-Route Headers)

```
SIP/2.0 200 OK
Via: SIP/2.0/UDP 10.1.1.1:5060;branch=z9hG4bKclient1234
Record-Route: <sip:192.76.120.10;r2=on;lr;ftag=telnyxtag1>
Record-Route: <sip:10.255.0.1;r2=on;lr;ftag=telnyxtag2>
To: <sip:+12345678901@sip.telnyx.com>;tag=telnyx123
From: "+19876543210" <sip:+19876543210@client.example.com>;tag=clienttag123
Call-ID: 1234abcd@client.example.com
CSeq: 100 INVITE
Contact: <sip:+12345678901@telnyx.com:5060>
Content-Type: application/sdp
...
```

In this response, Telnyx includes **Record-Route headers** to ensure subsequent requests follow the same path through the SIP proxies. The client must reverse the order of these headers and construct the correct **Route headers** in its ACK.

#### **Problematic ACK From Client**

```
ACK sip:+12345678901@telnyx-200-ok-contact-header-ip-address:5060 SIP/2.0
Route: <sip:10.255.0.1;r2=on;lr;ftag=telnyxtag2>
...
```

#### **Why This Fails**

The client incorrectly omits or reorders the Route headers. The correct order, based on the reversed Record-Route headers from the 200 OK, should be:

```
Route: <sip:192.76.120.10;r2=on;lr;ftag=telnyxtag1>
Route: <sip:10.255.0.1;r2=on;lr;ftag=telnyxtag2>
```

**Successful ACK**

```
ACK sip:+12345678901@telnyx.com:5060 SIP/2.0
Route: <sip:192.76.120.10;r2=on;lr;ftag=telnyxtag1>
Route: <sip:10.255.0.1;r2=on;lr;ftag=telnyxtag2>
...
```

**Why This Succeeds**

* The ACK follows the correct path through Telnyx’s proxies.
* The Route headers preserve the routing logic established in the 200 OK.
* Telnyx processes the ACK successfully, and media can flow between endpoints.

---

## Implications for Telnyx Customers

From Telnyx's perspective, when a call faces such an issue, it remains in a "call in progress" state until the **ack\_timeout** occurs. Customers might observe calls being dropped with "ack\_timeout" as the hang-up cause.

## Is the order in the record route headers important in the customers 200 OK?

Yes, the order of Record-Route headers in the customer's 200 OK response is important and has specific implications for SIP message routing. Record-Route headers are used by intermediate SIP proxies to insert themselves into the path of the request and its subsequent responses within a dialog, like Telnyx's SIP Proxy, ensuring that the signalising messages for the entire session traverse through these proxies.

When the Telnyx SIP proxy adds a Record-Route header to an INVITE request, it's essentially saying that all subsequent SIP messages within this dialog (such as ACKs and BYEs) should route through this proxy. The order in which these headers are added dictates the path that these messages will take:

* **Forward Path (INVITE)**: For the initial INVITE request, Record-Route headers are added in the order the request passes through each proxy. The first proxy the request encounters adds its Record-Route header first, and so on. This order determines the path that the initial request takes through the network.
* **Backward Path (Responses):** For responses, such as the 200 OK, SIP messages traverse the proxies in reverse order, following the "Via" headers back to the originator. However, for subsequent requests within the dialog (like ACK and BYE), the order of the Record-Route headers dictates the path.

  + The UAC constructs the "Route" header field for these messages based on the Record-Route headers it received in the first final response (e.g., 200 OK). It reverses the order of the Record-Route headers to ensure that subsequent messages follow the path back through the proxies in the correct sequence.

Therefore, the order of Record-Route headers in the 200 OK is crucial because it sets the route that all subsequent messages within the dialog will follow. If the headers were reordered incorrectly, it could lead to SIP messages taking an inefficient path through the network or, worse, not reaching their destination at all due to misrouting.

## My ACK has the correct R-URI and route headers, why is the call still failing?

#### A malformed ACK packet missing carriage return lines (CRLF)

Which can lead to issues in processing the message. In SIP communications, as well as many other Internet protocols, the carriage return (CR) followed by a line feed (LF) characters (\r\n) are essential for delineating the end of a line in the message header and the beginning of the message body or separating headers. If these aren't properly included, the receiving system might not recognise the end of one line and the start of another, leading to parsing errors or the message being ignored altogether.

The solution in such cases is to ensure that the message formatting strictly adheres to the protocol specifications, including the use of carriage return line feeds (CRLF) to properly structure the message. Correcting the formatting issue in the ACK packet should resolve the problem and allow the message to be processed as intended.

#### CSeq Mismatch

Another often-overlooked header—**CSeq (Sequence Number)**—is just as critical to the successful establishment of SIP calls. The **CSeq header** maintains synchronisation between SIP requests and responses by indicating the order of transactions. Each new SIP request within the same dialog must increment the CSeq number. A mismatch between the CSeq numbers in the **INVITE, 200 OK, and ACK** can lead to issues such as dropped calls or failures to establish media, even when the **Record-Route and Via headers are correct**.

Consider the following call flow:

1. A client sends an **INVITE** with `CSeq: 2 INVITE`.
2. The server responds with `407 Proxy Authentication Required`, challenging the request.
3. The client resends the **INVITE**, this time with authentication credentials and an incremented `CSeq: 3 INVITE`.
4. The server processes the request and replies with `200 OK` containing `CSeq: 3 INVITE`.
5. **Problem**: The client then sends an ACK with the previous sequence number, `CSeq: 2 ACK`, instead of the correct `CSeq: 3 ACK`.

In this case, the server is expecting `CSeq: 3 ACK` to confirm the `200 OK`. When it receives `CSeq: 2 ACK`, it considers the transaction incomplete and does not establish media. This mismatch leads to a "ack\_timeout" disconnect, despite all other headers being correctly configured.

## Best Practices for SIP Call Configuration

To prevent such issues and ensure reliable call setup and media flow, it's essential for customers and their network administrators to:

* Check the configuration of your SIP infrastructure, including SIP proxies and Session Border Controllers (SBCs), to ensure they are correctly including Route headers in 200 OK responses.
* Utilise SIP tracing and logging tools to monitor call flows and diagnose issues with SIP message routing. Comparing successful and unsuccessful call logs can help identify discrepancies in Route header handling.
* Familiarise yourself with the intricacies of SIP signalling and how different network elements interact. A deeper understanding can aid in troubleshooting and configuring your environment for optimal performance.

## Conclusion

The correct handling of Route headers in SIP communications is crucial for ensuring that calls are set up successfully and that media can flow between endpoints. By adhering to best practices and ensuring that your network is correctly configured to handle SIP messages, you can minimise disruptions and provide a seamless communication experience for your users. If you encounter persistent issues, working closely with your SIP service provider can help resolve these challenges effectively.

---

Related Articles

[SIP Connection: Fail-over and Retries](https://support.telnyx.com/en/articles/4320364-sip-connection-fail-over-and-retries)[SIP Registration](https://support.telnyx.com/en/articles/4363904-sip-registration)[Understanding SIP PRACK Protocol](https://support.telnyx.com/en/articles/6902981-understanding-sip-prack-protocol)[How Telnyx Handles SRV Records for SIP Calls](https://support.telnyx.com/en/articles/10666839-how-telnyx-handles-srv-records-for-sip-calls)[How to Configure SIP Attach using a UAC Connection](https://support.telnyx.com/en/articles/14805261-how-to-configure-sip-attach-using-a-uac-connection)

Did this answer your question?

😞😐😃
