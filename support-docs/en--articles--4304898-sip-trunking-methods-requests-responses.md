---
source_url: https://support.telnyx.com/en/articles/4304898-sip-trunking-methods-requests-responses
scraped: 2026-07-08
content_hash: e16cf3db090ad672d0669dc9c568db73a6dddc9d007b64b29a7b70d9edb922d4
---

SIP Trunking - Methods/Requests & Responses | Telnyx Help Center

[Skip to main content](#main-content)

# SIP Trunking - Methods/Requests & Responses

Here we will explain different SIP trunking methods/requests and responses.

Written by Dillin

September 20, 2023

Table of contents

# **What is SIP Trunking?**

[SIP Trunking](https://telnyx.com/products/sip-trunks) is a popular form of voice/fax communications over the Internet. It's always a good idea to know the different **SIP Methods / Requests** and the **Responses** at a high level to understand the behaviour of a SIP Call Session.   
​  
The SIP specification can be reviewed in detail in [RFC 3261](https://tools.ietf.org/html/rfc3261). It describes Session Initiation Protocol (SIP), an application-layer control (signalling) protocol for creating, modifying, and terminating sessions with one or more participants. These sessions include Internet telephone calls, multimedia distribution, and multimedia conferences.

They serve as a foundational reference for professionals in the field. RFC 3261 specifically describes the Session Initiation Protocol (SIP), an application-layer control (signaling) protocol used for establishing, modifying, and terminating sessions with one or more participants. These sessions can range from Internet phone calls to multimedia distributions and conferences.  
​  
In this article, we give you an overview of what to expect when interacting with SIP.

## **What are SIP Methods / Requests?**

### **There are fourteen SIP Request methods of which the first six are the most basic request / method types:**

* ### **INVITE:**

  Establishes a session.
* ### **ACK**:

  Confirms an INVITE request.
* ### **BYE**:

  Ends a session.
* ### **CANCEL**:

  Cancels establishing of a session.
* ### **REGISTER**:

  Communicates user location (host name, IP).
* ### **OPTIONS**:

  Communicates information about the capabilities of the calling and receiving SIP phones.
* ### **PRACK:**

  Provisional Acknowledgement.
* ### **SUBSCRIBE:**

  Subscribes for Notification from the notifier.
* ### **NOTIFY:**

  Notifies the subscriber of a new event.
* ### **PUBLISH:**

  Publishes an event to the Server.
* ### **INFO:**

  Sends mid session information.
* ### **MESSAGE:**

  Transports Instant Messages.
* ### **UPDATE:**

  Modifies the state of a session.

## **What are SIP Responses?**

### There are six classes of SIP Responses. The responses give you an idea on how a call is progressing and whether it's been established or whether there were any failures.

* ### **1xx**:

  These provisional responses give feedback on the progression of a session establishment. For example, when a SIP INVITE request is made, a 180 Ringing response indicates that the recipient's device is alerting them of an incoming call. It's akin to hearing a ringtone when calling someone on a regular phone.
* ### **2xx**:

  This class indicates that a request, like a call initiation, has been successful. A 200 OK response, for instance, indicates that the initial request was successful and the call will be connected. Think of it as the moment when you hear "Hello" on the other end of the line.
* ### **3xx**:

  3xx responses inform the requester about a change in the recipient's location or provide alternative contacts. For example, a 301 Moved Permanently response informs the sender that the recipient has changed their address, similar to a "forwarding address" notification when someone moves residences.
* ### **4XX**:

  These responses indicate various client errors. The 404 Not Found response, for instance, is akin to dialling a phone number that's no longer in service.
* ### **5xx**:

  These error responses signify that the server has encountered an issue processing the request. An example is the 503 Service Unavailable, which is like trying to call someone, but their phone is turned off or out of service range.
* ### **6xx**:

  Global failure responses convey that a server has definitive information about a particular user, not just the current session. An example is the 603 Decline, which is somewhat analogous to someone seeing an incoming call and choosing to decline it.  
  ​

## **1XX = Informational SIP Responses**

### Information responses usually occur when a SIP INVITE request was made to the SIP endpoint. The SIP endpoint can respond with multiple 1XX responses to inform the requester on how the call is progressing.

* #### **100 Trying**:

  Extended search is being performed so a forking proxy must send a 100 Trying response.
* #### **180 Ringing**:

  The Destination User Agent has received the INVITE message and is alerting the user of call.
* #### **181 Call Is Being Forwarded**:

  Optional, send by Server to indicate a call is being forwarded.
* #### **182 Queued**:

  Destination was temporarily unavailable, the server has queued the call until the destination is available.
* #### **183 Session Progress**:

  This response may be used to send extra information for a call which is still being set up.
* #### **199 Early Dialog Terminated**:

  Send by the User Agent Server to indicate that an early dialogue has been terminated.  
  ​

## **2XX = Success Responses**

### **Success responses, much like the HTTP protocol, usually occur when a the SIP endpoint has received confirmation that the INVITE request was successful and that the call will be answered.**

* #### **200 OK**:

  Shows that the request was successful.
* #### **202 accepted**:

  Indicates that the request has been accepted for processing, mainly used for referrals.
* #### **204 No Notification**:

  Indicates that the request was successful but no response will be received.

## **3XX = Redirection Responses**

### **3xx responses give information about the SIP endpoints new location (redirection), or about alternative services that might be able to satisfy the call.**

* #### **300 Multiple Choices**:

  The address resolved to one of several options for the user or client to choose between.
* #### **301 Moved Permanently**:

  The original Request URI is no longer valid, the new address is given in the Contact header.
* #### **302 Moved Temporarily**:

  The client should try at the address in the Contact field.  
  ​**Note: This SIP response is not accepted by Telnyx at this time.**
* #### **305 Use Proxy**:

  The Contact field details a proxy that must be used to access the requested destination.
* #### **380 Alternative Service**:

  The call failed, but alternatives are detailed in the message body.

## **4XX = Request Failures**

### **The 4xx responses are the Client Error responses. They are used to indicate that something went wrong while processing the INVITE request. The most frequent request seen is generally a 404 not found. Where the SIP endpoint doesn't believe the destination you are trying to reach exists.**

* #### **400 Bad Request**:

  The request could not be understood due to malformed syntax.
* #### **401 Unauthorized:**

  The request requires user authentication. This response is issued by UASs and registrars.
* #### **402 Payment Required:**

  (Reserved for future use).
* #### **403 Forbidden**:

  The server understood the request, but is refusing to fulfil it.
* #### **404 Not Found**:

  The server has definitive information that the user does not exist at the (User not found).
* #### **405 Method Not Allowed**:

  The method specified in the Request-Line is understood, but not allowed.
* #### **406 Not Acceptable**:

  The resource is only capable of generating responses with unacceptable content.
* #### **407 Proxy Authentication Required**:

  The request requires user authentication.
* #### **408 Request Timeout**:

  Couldn’t find the user in time.
* #### **409 Conflict**:

  User already registered (deprecated)
* #### **410 Gone**:

  The user existed once but is not available here any more.
* #### **411 Length Required**:

  The server will not accept the request without a valid content length (deprecated).
* #### **412 Conditional Request Failed:**

  The given precondition has not been met.
* #### **413 Request Entity Too Large**:

  Request body too large.
* #### **414 Request URI Too Long**:

  Server refuses to service the request, the Req-URI is longer than the server can interpret.
* #### **415 Unsupported Media Type**:

  Request body is in a non-supported format.
* #### **416 Unsupported URI Scheme**:

  Request-URI is unknown to the server.
* #### **417 Uknown Resource-Priority**:

  There was a resource-priority option tag, but no Resource-Priority header.
* #### **420 Bad Extension**:

  Bad SIP Protocol Extension used, not understood by the server.
* #### **421 Extension Required**:

  The server needs a specific extension not listed in the Supported header.
* #### **422 Session Interval Too Small**:

  The request contains a Session-Expires header field with a duration below the minimum.
* #### **423 Interval Too Brief**:

  Expiration time of the resource is too short.
* #### **424 Bad Location Information**:

  The request’s location content was malformed or otherwise unsatisfactory.
* #### **428 Use Identity Header**:

  The server policy requires an Identity header, and one has not been provided.
* #### **429 Provide Referrer Identity**:

  The server did not receive a valid Referred-By token on the request.
* #### **430 Flow Failed:**

  A specific flow to a user agent has failed, although other flows may succeed.
* #### **433 Anonymity Disallowed**:

  The request has been rejected because it was anonymous.
* #### **436 Bad Identity Info**:

  The request has an Identity-Info header and the URI scheme contained cannot be de-referenced.
* #### **437 Unsupported Certificate**:

  The server was unable to validate a certificate for the domain that signed the request.
* #### **438 Invalid Identity Header**:

  Server obtained a valid certificate used to sign a request, was unable to verify the signature.
* #### **439 First Hop Lacks Outbound Support**:

  The first outbound proxy doesn’t support the “outbound” feature.
* #### **440 Max-Breadth Exceeded:**

  If a SIP proxy determined a response context had insufficient Incoming Max-Breadth to carry out a desired parallel fork, and the proxy is unwilling/unable to compensate by forking serially or sending a redirect, that proxy MUST return a 440 response. A client receiving a 440 response can infer that its request did not reach all possible destinations.
* #### **469 Bad Info Package:**

  If a SIP UA receives an INFO request associated with an Info Package that the UA has not indicated willingness to receive, the UA MUST send a 469 response, which contains a Recv-Info header field with Info Packages for which UA is willing to receive INFO requests.
* #### **470 Consent Needed**:

  The source of the request did not have the permission of the recipient to make such a request.
* #### **480 Temporarily Unavailable**:

  Callee currently unavailable.
* #### **481 Call/Transaction Does Not Exist**:

  Server received a request that does not match any dialogue or transaction.
* #### **482 Loop Detected**:

  Server has detected a loop.
* #### **483 Too Many Hops**:

  Max-Forwards header has reached the value ‘0’.
* #### **484 Address Incomplete**:

  Request-URI incomplete.
* #### **485 Ambiguous**:

  Request-URI is ambiguous.
* #### **486 Busy Here**:

  Callee is busy.
* #### **487 Request Terminated**:

  Request has terminated by bye or cancel.
* #### **488 Not Acceptable Here**:

  Some aspects of the session description of the Request-URI are not acceptable. If you are using SRTP check out this [example](https://support.telnyx.com/en/articles/4404575-tls-and-srtp#h_f545f23a76) for further details in case of a configuration issue. You can find more examples in this [article](https://support.telnyx.com/en/articles/4409457-telnyx-sip-response-codes#special-notes-on-sip-response-codes) as well.
* #### **489 Bad Event**:

  The server did not understand an event package specified in an Event header field.
* #### **491 Request Pending**:

  Server has some pending request from the same dialogue.
* #### **493 Undecipherable**:

  Undecipherable Request contains an encrypted MIME body, which recipient can not decrypt.
* #### **494 Security Agreement Required**:

  The server has received a request that requires a negotiated security mechanism.

## **5XX = Server Errors**

### **The 5xx responses are the "Server Error" responses. They are generated by the likes of proxy servers, location servers, and redirect servers.**

* #### **500 Server Internal Error:**

  The server could not fulfil the request due to some unexpected condition.
* #### **501 Not Implemented**:

  The SIP request method is not implemented here.
* #### **502 Bad Gateway:**

  The server, received an invalid response from a downstream server while trying to fulfil a request.
* #### 503 Service Unavailable:

  The server is in maintenance or is temporarily overloaded and cannot process the request.
* #### 504 Server Time-out:

  The server tried to access another server while trying to process a request, no timely response.
* #### **505 Version Not Supported**:

  The SIP protocol version in the request is not supported by the server.
* #### **513 Message Too Large**:

  The request message length is longer than the server can process.
* #### **555 Push Notification Service Not Supported:**

  The server does not support the push notification serviced specified in the pn-provider SIP URI parameter.
* #### **580 Precondition Failure**:

  The server is unable or unwilling to meet some constraints specified in the offer.

## **6XX = Request Failures**

### **The 6xx responses are the "Global Error" responses. They indicate that a server has definitive information about a particular user and not just the particular instance indicated by the Request-URI.**

* #### **600 Busy Everywhere**:

  All possible destinations are busy.
* #### **603 Decline**:

  Destination cannot/don't wish to participate in the call, no alternative destinations.
* #### **604 Does Not Exist Anywhere**:

  The server has authoritative information that the requested user does not exist anywhere.
* #### **606 Not Acceptable**:

  The user’s agent was contacted successfully but some aspects of the session description were not acceptable.
* #### **607 Unwanted:**

  The called party did not want his call from the calling party. Future attempts from the calling party are likely to be similarly rejected.   
  ​
* **608 Rejected:**

  SIP Code 608 is a specific status code used in the Session Initiation Protocol (SIP) to indicate that the terminating carrier has blocked a call due to suspected fraud, preventing it from reaching the intended end user. Read more about how to improve this [here](https://support.telnyx.com/en/articles/4088988-telnyx-how-to-handle-spam-scam-likely).

## **Examples**

Imagine you're using a digital phone (VoIP) to call a friend. When you dial their number, behind the scenes, your phone sends an INVITE request. Your friend's phone, upon receiving this, sends back an informational 180 Ringing response, which corresponds to the ringing you hear. Once your friend answers, a 200 OK success response is communicated, and the call is connected. If your friend was busy and didn't answer, after some time, a 408 Request Timeout might be sent. Similarly, if you dialled a number that didn't exist, you'd get a 404 Not Found error, just as if you'd dialled an incorrect or disconnected number on a traditional phone.

## **NOTES**

**SIP Options**

* Used to determine if a user agent (e.g., a SIP phone or server) is available or reachable.
* To query the capabilities of the user agent, like which methods it supports.

Telnyx's systems do not send SIP Options to our customers SIP Connections but Telnyx does accept and respond to SIP Options requests to our SIP Proxies from our customers user agents.

We like to expand our knowledge across our website and you can view further information on SIP Responses [here](https://telnyx.com/resources/sip-response-codes-need-know-2-minutes) & SIP trunking explained [here](https://telnyx.com/resources/sip-trunking-explained).

Looking to debug your SIP Call flows? Look no further than our own [debugging tool](https://support.telnyx.com/en/articles/4304872-telnyx-debugging-tools) available on your account.

---

Related Articles

[Configuring a Cisco CUBE/CUCM SIP Trunk](https://support.telnyx.com/en/articles/1130673-configuring-a-cisco-cube-cucm-sip-trunk)[SIP Registration](https://support.telnyx.com/en/articles/4363904-sip-registration)[Telnyx SIP Response Codes](https://support.telnyx.com/en/articles/4409457-telnyx-sip-response-codes)[Wildix: SIP Trunk Setup](https://support.telnyx.com/en/articles/5799830-wildix-sip-trunk-setup)[Grandstream GRP260x: SIP Trunk](https://support.telnyx.com/en/articles/6169513-grandstream-grp260x-sip-trunk)

Did this answer your question?

😞😐😃

Table of contents
