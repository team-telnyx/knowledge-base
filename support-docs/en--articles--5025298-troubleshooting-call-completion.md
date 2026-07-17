---
source_url: https://support.telnyx.com/en/articles/5025298-troubleshooting-call-completion
title: "Troubleshooting Call Completion"
description: "Identifying and resolving common issues with inbound and outbound… See Telnyx guidance and requirements."
scraped: 2026-07-08
content_hash: 9572a5fb4a41d00059dfd6b47ac6e1406f7dae75fa4f7ecc3d59091997b587e4
---







# Troubleshooting Call Completion

Identifying and resolving common issues with inbound and outbound… See Telnyx guidance and requirements.




## **Troubleshooting Outbound Call Failures**

Outbound calling, also known as “termination”, can be a tricky process to troubleshoot, but luckily, most termination issues are the result of a small handful of different causes. In this article, we will review the most common causes of call termination issues and illustrate what you can do to identify and resolve them.

## **Invalid caller ID**

Perhaps the most common cause of call termination problems, particularly when setting up a new SIP connection, is caller ID. Caller ID is the service responsible for displaying your phone number to the device you are trying to call. When a call is rejected due to an invalid caller ID, you will receive the SIP response message **“403 Caller Origination Number is Invalid D35”**.

## **Why is my caller ID invalid?**

Industry regulations mandate a strict policy regarding caller ID. For Telnyx to successfully terminate your call, we must pass a caller ID in **+E.164** format. The +E.164 format is made up “+”, the caller’s country code, and the caller’s full phone number. Many times, PBXs and softphones do not automatically pass a caller ID. The caller ID will often either be blank or, if you are using a credential-based SIP connection, your SIP username. As a result, your call will automatically get rejected because there is no valid caller ID number.

### **How do I append a valid caller ID?**

Unfortunately, this is where it varies. Each softphone and PBX has its own way of appending a caller ID to outbound calls. Fortunately, however, you can easily append a caller ID to any SIP connection using the **Caller ID Override** functionality within the Portal. To set a Caller ID Override, select the relevant SIP connection from the “SIP Connections” tab and select the “Outbound Options” icon to the right. From here, you can include a phone number that will be displayed on all outgoing calls made from this SIP connection.
​

## **Dialed number is not included in your whitelisted countries/regions**

By default, all Outbound Voice Profiles are configured to allow traffic only to destinations in the United States and Canada. If you attempt to place a call to a number outside of this region, you will receive the SIP response **“403 Dialed Number is not included in whitelisted countries D13”**.

In order to resolve this, you must whitelist the region in the Outbound Voice Profile associated with the relevant SIP connection. You can do so by selecting “Outbound Voice Profiles” from the Mission Control Portal, selecting the relevant Outbound Voice Profile, and clicking the “+” button next to the relevant region. You can select individual regions, full continents, or add all regions and countries.

From here, you may be prompted to request level 2 verification, which authorizes you to make international calls. You can request this by hovering over your initials in the top right of the Portal, selecting “My Account”, and clicking the “Verifications” tab. Alternatively, you can find this page [here](https://portal.telnyx.com/#/app/account/verifications). For more information on account verification, please see our [Account Verification article](https://support.telnyx.com/en/articles/1130595-account-verification).
​

## **403 - Forbidden**

Slightly less common than the two issues above, a **“403 Forbidden”** can be returned to a caller for a variety of reasons. The most straight-forward cause of this SIP response is a failure to authenticate your SIP connection. If you are using the incorrect credentials on a credential-based connection or you are attempting to place a call from an IP address that has not yet been added to an IP-based connection, Telnyx will return a “403 Forbidden” and reject the call in order to protect your account from being charged for unauthorized use.

**What if I am sure that I’m authenticated properly?**

While an authentication issue is the most common cause of a “403 Forbidden”, it is not the only one. Other potential causes include:

* Your Telnyx account is negative in balance.
* The connection you are using to place the calls does not have an Outbound Voice Profile configured.
* A token or tech prefix, if enabled on your FQDN/IP-based connection, does not match the token or tech prefix supplied in your SIP INVITE.
* The caller origination number (caller ID) is a phone number that belongs to another Telnyx user.

## **503 - No routes found (or service unavailable)**

While less common than a “403” error, a “503” error generally points to a routing issue for the specific destination. If you receive a 5xx response code, it’s advisable to contact support by starting a chat from the chat bubble on the lower right-hand corner of the Portal or by emailing [support@telnyx.com](mailto:support@telnyx.com), as this tends to require manual intervention. When contacting support, please provide a call example with the source and destination numbers as well as an approximate timestamp so that the relevant call can be located.

* There are a few cases where 503's are expected such as in the event where you attempt to spoof caller ID on your outbound calls to international destinations.

---

## General Hangup Reasons

In SIP errors response, there is a reason header that includes the a high level reason for why the error occurred and may be accompanied with a cause code as well.

### **NORMAL\_CLEARING (16)**

For "NORMAL CLEARING" with the cause code "16", this generally implies:

* The call was terminated in a regular, expected manner.
* No errors or unexpected issues occurred during the call's lifetime.

In layman's terms, if you see "NORMAL\_CLEARING (16)" in a call log or a system message, it's typically an indication that the call ended as it should, often because one of the parties hung up the phone or ended the call in a standard way.

### **USER\_BUSY (17):**

The term "USER BUSY" followed by the number "17" corresponds to a specific SIP response code. In this context:

* "USER BUSY" is a descriptive phrase that means the called party is currently engaged in another call and cannot accept new incoming calls.
* "17" is the cause code associated with this specific scenario.

When a SIP endpoint (like a VoIP phone or a softphone) receives an incoming call while it's already on another call, it may return the "USER\_BUSY" signal to the calling party, indicating that the call cannot be completed at that time due to the busy status of the recipient.

### **INCOMPATIBLE\_DESTINATION (88):**

The INCOMPATIBLE DESTINATION with the cause code "88" generally means:

* The destination was not suitable or compatible for the call.
* The calling party's channel was incompatible with the channel type requested at the destination.

This is generally related to session description protocol (SDP) from the SIP INVITEs or 200 OK responses . In practical terms, it could indicate a situation where, for example, you're trying to make a voice call to a fax machine or there's a mismatch in the communication protocols or codecs between the two endpoints.

It essentially points out that the call could not proceed because the two endpoints (or some intermediate equipment) could not agree on a common set of capabilities or characteristics to establish the call.

The most common scenario we see is that a user has enabled encryption on their Telnyx SIP connection, like SRTP, but has not done anything to enable it on their device. For example, in an outbound call, they might have SRTP enabled on their SIP connection, yet they send us an INVITE without any crypto attributes in the SDP. Similarly, in an inbound call, they might send us a 200 OK without any crypto attributes. Less commonly, if SRTP is disabled altogether, they might have their SIP connection configured to only offer codecs that aren't supported by their device.

### **MANAGER\_REQUEST (16):**

The "MANAGER REQUEST" with the cause code "16" generally means:

* Telnyx's system terminated your call.
* This could have been done manually or automatically.

  + Manually when potential fraud is observed to limit further high cost call usage.
  + Automatically in cases where your account balance has gone negative, calls may be terminated.

---

## **Inbound Hangup Reasons**

### **RECOVERY\_ON\_TIMER\_EXPIRE (102)**

"RECOVERY ON TIMER EXPIRE (102)" generally indicates:

* The call or session was terminated due to a specific timer expiration.
* A necessary response was not received before the timer expired, leading to the termination or rejection of the session.

This can happen in scenarios where a SIP entity sends out a request (like an INVITE to initiate a call) and waits for a specific period for a response. If the response isn't received within that time frame, the session or call might be terminated to prevent endless waiting and to ensure resources are not wasted.

Such timer-based mechanisms are crucial in network protocols like SIP to manage resources efficiently and ensure that sessions do not hang indefinitely due to network issues or non-responsive endpoints.

For example, this occurs with inbound calls after Telnyx sends three SIP INVITEs to a customer's SIP Connection where no response is received. This is usually indicative of a firewall or NAT issue on the customer's end. We would advise to double check that our IP's are [whitelisted](https://support.telnyx.com/en/articles/1130687-whitelisting-telnyx-ip-addresses) and ensure that their IP address is listening on the port they've specified

### **MANDATORY\_IE\_MISSING (96)**

In SIP, there are certain headers that are mandatory for certain types of messages. For instance:

* The INVITE message, which is used to initiate a call, must include the **`To`**, **`From`**, **`CSeq`**, **`Call-ID`**, and **`Max-Forwards`** headers.
* The ACK message, which is used to acknowledge receipt of final responses to INVITE requests, also requires certain headers.

* "MANDATORY\_IE": This stands for "Mandatory Information Element".
* "MISSING": This indicates that the required element is not present.

In essence, the "MANDATORY IE MISSING" cause code signifies that a mandatory information element was expected in a message but was not present. Information elements are fundamental components of signaling messages that carry specific pieces of information. If a mandatory piece of information is missing from a message, then the message cannot be properly processed or interpreted, leading to call setup or processing failures.

This kind of error typically indicates an issue with the system or equipment sending the message, as it's not conforming to the expected protocol standards. However, we have seen this occur on inbound calls to customer devices, where Telnyx would send the SIP INVITE and the customer device would respond with a 407 proxy authentication. This suggests that the customer device is not expecting communication from our SIP Proxy IP addresses.

### **UNALLOCATED\_NUMBER (1)**

"UNALLOCATED NUMBER (1)" signifies:

* The called number is not assigned to any user or service.
* The number might not exist or may have been decommissioned.

This cause code is used to indicate that the dialed number is not currently in use. For the person trying to make the call, it typically results in a notification or tone suggesting that the number dialed is not valid or does not exist. In many cases, this is the same error you'd encounter when you mistakenly dial a phone number that hasn't been assigned to anyone, and you hear an automated message like "The number you have dialed is not in service."

For **inbound** calls, where Telnyx receives such a reason, typically in a 404 not found SIP response, this means that the number is either:

* Not assigned to a SIP connection.
* Or the SIP connection that the number is assigned to is credentials-based and is not currently registered.
* Or we're receiving a valid response from the customers system where the number is not currently assigned to any extension. Consider checking the inbound rules of your device to make sure you are expecting the number in a particular dialled format (10, 11 or +E.164 digits). See [Number Formats](https://support.telnyx.com/en/articles/1130706-sip-connection-number-formats).

### **PROGRESS\_TIMEOUT (16)**

"PROGRESS TIMEOUT (16)" signifies:

When Telnyx does not receive ringback from the customer's phone system. By default, the call times out if we don't receive a 180/183 from the customer within 5 seconds.

The customer can modify this time by changing the "No Ringback Timeout" parameter in the SIP connection's inbound options. See [SIP Connection Settings](https://support.telnyx.com/en/articles/4404448-sip-connection-inbound-outbound-settings).

### ALLOTTED\_TIMEOUT (602)

"ALLOTTED TIMEOUT (602)" signifies:

This cause means that the server canceled the call because the destination channel took too long to answer. The allotted\_timeout error is generally seen in the SIP BYE or CANCEL reason headers.

**Reason:SIP;cause=602;text="ALLOTTED\_TIMEOUT"**

This allotted\_timeout error will occur when there is a timeout reached.

For example, for the answer timeout setting on your SIP Connections inbound settings. If the call isn't answered within the defined time allotted.

The same timeout can apply using our call control voice API product where you can set
​**Enable "hang-up" on timeout** on yourcall control application which tells Telnyx how long to wait for your call to be answered before hanging up due to the timeout set being reached.

---

## **Outbound Hangup Examples**

### **CALL\_REJECTED (21)**

"CALL REJECTED (21)" signifies:

This usually affects outbound calls, when our SIP proxy returns a 4xx error code (usually 403) to the customer. If you investigate the SIP signalling, you should see the specific reason why this call was rejected. This could be an invalid caller ID, the destination not being whitelisted in their outbound profile, etc. See [SIP Responses](https://support.telnyx.com/en/articles/4409457-telnyx-sip-response-codes).

### **NORMAL\_TEMPORARY\_FAILURE (41)**

"NORMAL TEMPORARY FAILURE (41)" signifies:

This are usually associated with us returning a 5xx error code to the customer, often the result of a routing issue with our downstream carriers. Please contact Telnyx support for these instances.

---

###

## **Further troubleshooting using the Debugging Tool**

An exhaustive list of our SIP response codes can be found [here](https://support.telnyx.com/en/articles/4409457-telnyx-sip-response-codes). In general, a 403 error is the result of a discrepancy between what you are attempting to do and what your Telnyx account or PBX is configured to do. Other 4xx response codes, such as “404 Not Found” or “486 User Busy” generally indicate that there is an issue with the destination device. Alternatively, 5xx errors, while much less common, are often the result of a routing issue.

To gain additional insight when troubleshooting, you can leverage the debugging tool within the Portal to view the SIP logs and call flow for a specific call. For more information on using this tool, please see our [Debugging](https://support.telnyx.com/en/articles/4304872-telnyx-debugging-tools) article. The Debugging menu contains other features, such as the Web Dialer, which can be used to make calls directly from the Portal.

You can find more information on different reasons and cause codes [here](https://developer.signalwire.com/freeswitch/FreeSWITCH-Explained/Troubleshooting-Debugging/Hangup-Cause-Code-Table_3964945/).
​

---

## **Troubleshooting Inbound Call Failures**

Fortunately, inbound calls are susceptible to fewer problems than outbound calls; However, they can still be difficult to troubleshoot. If you are not receiving calls when you know you should be, this is generally an issue with either SIP registration or the authentication method selected when setting up your SIP connection.
​

## **SIP Registration (for credential-based connections)**

Much like other SIP providers, Telnyx maintains a registrar of the devices associated with SIP connections. When you authenticate your SIP credentials on your softphone or PBX, a SIP REGISTER request is sent from your device to Telnyx, which tells Telnyx where to send the calls that are directed to your SIP URI.

If you are not receiving any inbound calls on a credential-based SIP connection, it is likely that we are not receiving the SIP REGISTER requests from your device. Please ensure that you have whitelisted traffic to and from the IP addresses and subnets listed in our *[What IPs do I need to whitelist?](https://support.telnyx.com/en/articles/1130687-whitelisting-telnyx-ip-addresses)* article.
​

## **IP and FQDN authentication**

If you have configured your SIP connection to use IP- or FQDN-based authentication, then calls destined for your SIP URI will be sent to the user-provided IP address(es) along with the provided network ports. If there is a discrepancy in the IP address/port provided and the IP address/port your PBX is actively listening on, then the calls will not make it to your PBX.

Firewall and NAT configuration can also have an effect on inbound calls. Please ensure that you have whitelisted the traffic to and from the IP addresses and subnets listed in our *[What IPs do I need to whitelist?](https://support.telnyx.com/en/articles/1130687-whitelisting-telnyx-ip-addresses)* article. If you are using IP or FQDN authentication, it’s advisable that either your PBX is publicly exposed or that your router has the necessary port forwarding configuration enabled (for both the signaling (SIP) stream and the media (RTP) stream.

---

​

## **Further troubleshooting**

If further troubleshooting is necessary, you can leverage the debugging tool within the Portal to view the SIP logs and call flow for a specific call, including those that were destined for your SIP URI but never reached your end device. For more information on using this tool, please see our [Debugging](https://support.telnyx.com/en/articles/4304872-telnyx-debugging-tools) article. You can also contact support by starting a chat from the chat bubble on the lower right-hand corner of the Portal or by emailing [support@telnyx.com](mailto:support@telnyx.com).

---

Related Articles

[Caller ID Number Policy](https://support.telnyx.com/en/articles/3546251-caller-id-number-policy)[SIP Connection: Inbound & Outbound Settings](https://support.telnyx.com/en/articles/4404448-sip-connection-inbound-outbound-settings)[Telnyx SIP Response Codes](https://support.telnyx.com/en/articles/4409457-telnyx-sip-response-codes)[PBXes: Connecting a PBXes Trunk to Telnyx](https://support.telnyx.com/en/articles/5798240-pbxes-connecting-a-pbxes-trunk-to-telnyx)[Calls Per Second (CPS) Limits](https://support.telnyx.com/en/articles/15668484-calls-per-second-cps-limits)

Did this answer your question?

😞😐😃
