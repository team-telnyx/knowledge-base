---
source_url: https://support.telnyx.com/en/articles/4363904-sip-registration
title: "SIP Registration"
description: "This article explains the basic components involved in the SIP Registration process. See Telnyx guidance and requirements."
scraped: 2026-07-08
content_hash: 844e2617eb0eeda3fa4c93328213a8fe1cbaa3a93f66d973f020f6c0b0acc936
---







# SIP Registration

This article explains the basic components involved in the SIP Registration process. See Telnyx guidance and requirements.




How do service providers like Telnyx know where their users are located and how to make contact with them? Within the Session Initiation Protocol, there is a process called SIP Registration, which allows service providers to identify the phones of their customers, thus providing them insight into where to send phone calls. In other words, registration is the process by which service providers data mine their customers’ locations.

## **The Components of SIP Registration**

* **User Agent:** The SIP entity that interacts with the user e.g. soft phone.
* **SIP URI:** The SIP address that identifies a user – it usually consists of a username and domain name, similar to our email addresses. SIP: [bob@yourcompany.com](mailto:bob@yourcompany.com) i.e., SIP:[bob@8.8.8.8](mailto:bob@8.8.8.8)

  + Don't forget that the transport used (UDP, TCP or TLS) is configured within the user agent. Upon registration, the user agent will indicate to our SIP Registrar which transport it would like to use.
  + This is why you do not have the option to set a transport on SIP credential connections because it's defined and controlled by the user agent registering with our system.
* **SIP Registrar Server:** A server belonging to the service provider that accepts Register requests and will have a database that maintains all the user's registrations in a binding table. This server is usually collated with the proxy and redirect servers.
* **Location Server:** Registrar servers store their customers' locations to this server.
* **Binding table:** This table contains the details on where to reach the user such as numbers, IP address, Ports, etc.
* **Proxy Server:** A server that handles incoming invitations.
* **Redirect Server:** A server that provides alternative locations where the user can be reachable.
* **IP Authentication:** A check by the Registrar to confirm the user’s details.

A more in depth procedure of SIP Registration can be read [here](https://andrewjprokop.wordpress.com/2014/05/29/understanding-sip-registration/), courtesy of Andrew J Prokop.

## **A Failed SIP Registration Example**

![SIP connections options section. ](_images/4b61cf31c85e8fec.png)

Above is a SIP credentials authenticated connection, with the username and password of our choosing. We will be using the Zoiper softphone client to register to sip.telnyx.com (US Region).

The registration attempt will come from the public IP 80.111.117.202 of [sip.telnyx.com](https://sip.telnyx.com/) which translates to the Telnyx anycast IP of 192.76.120.10.

### **SNGREP**

Below is an [sngrep](https://github.com/irontec/sngrep) trace of a register attempt from a User Agent ([Zoiper](https://support.telnyx.com/en/articles/6133517-zoiper-communicator)) configured with the credentials shown above.

![A Sngrep trace showing some credentials. ](_images/201471a28077eb45.png)

1. 80.111.117.202 -> 192.76.120.10 REGISTER sip:sip.telnyx.com;transport=UDP SIP/2.0
2. 192.76.120.10 -> 80.111.117.202 401 Unauthorized
3. 80.111.117.202 ->192.76.120.10 REGISTER sip:sip.telnyx.com;transport=UDP SIP/2.0
4. 192.76.120.10 -> 80.111.117.202 401 Unauthorized

![A 401 unauthorized feedback page. ](_images/98e4a5566e2157e0.png)

As you can see, attempts to register are met with a “401 Unauthorized”. This is because the registrar server attempts to know more information about the User Agent. At that point, the User Agent will send another REGISTER message. If we get another “401 Unauthorized” it means that we did not configure our parameters properly i.e. **username or password**. In this example, the password was incorrect and registration was unsuccessful.

Until registration has been completed successfully, your numbers are unable to receive inbound calls as we won't have the **address of record** on file in our SIP Registrar, to know where to send calls to.

## **A Successful SIP Registration Example**

![Breaking Line](_images/682991ade0be9812.png)

![A Sngrep trace page. ](_images/17a1ebb3c560b771.png)

1. 80.111.117.202 -> 192.76.120.10 REGISTER sip:sip.telnyx.com;transport=UDP SIP/2.0
2. 192.76.120.10 -> 80.111.117.202 401 Unauthorized
3. 80.111.117.202 ->192.76.120.10 REGISTER sip:sip.telnyx.com;transport=UDP SIP/2.0
4. 192.76.120.10 -> 80.111.117.202 200 OK

![A 401 unauthorized page. ](_images/9776d86ad486848c.png)

As you can see, attempts to register are met with a “401 Unauthorized”. This is because the registrar server attempts to know more information about the User Agent. At that point, the User Agent will send another REGISTER message. This time, we get a 200 OK response which means the registration was successful. This is because the password was correctly inputted this time.

## **SIP URI Calling**

![Breaking Line](_images/682991ade0be9812.png)

If you are expecting to receive inbound calls via SIP URI calling from another service to your credential based SIP Connections, please ensure you specify your contact header as the username you created on your SIP Connection. Most systems, when Telnyx sends the SIP INVITE, will expect the SIP INVITE URI to contact username@ipaddress of your system. If the username differs from that of the username of your SIP Connection, your system may reject calls.

## **SIP Registration using TCP or TLS**

![Breaking Line](_images/682991ade0be9812.png)

For TCP and TLS (which runs over TCP), Telnyx re-uses the TCP connection established by the User Agent. Telnyx uses the port 5060 for TCP. Further information on support for Transport Protocols and their ports can be found [here.](https://sip.telnyx.com/)

User Agents are unlikely to establish connections from port 5060 to port 5060 and are more likely to use an ephemeral port to send from (RFC 6056 states that the range for ephemeral ports should be 1024–65535).

When a User Agent sends a REGISTER message to Telnyx and the IP address and port in the contact header do not match the IP address and port the message was received from, Telnyx will add an "alias" to the AOR (Address of Record) on file.

This can be seen in the 200OK Telnyx sends back to the User Agent.

If the REGISTER request uses port 5060 in its contact header and the message is received from an ephemeral port, Telnyx will "alias" the address. Therefore, future INVITEs sent to the User Agent after Registration will have port 5060 in the Request-URI but will re-use the existing TCP connection.

It is important to note this when setting up your firewall and port settings. If it is required that port 5060 is used for TCP with a User Agent it will be necessary to register directly from port 5060.

## **SIP Registration via siphv.telnyx.com**

![Breaking Line](_images/682991ade0be9812.png)

**[THIS PRODUCT IS NO LONGER AVAILABLE](https://support.telnyx.com/en/articles/6461350-hvsd-outbound-profile-end)**

Our high volume short duration product (<https://siphv.telnyx.com/>) does not currently support SIP Registration for inbound calls. If you want to receive inbound calls please register with our other FQDN's: sip.telnyx.com, sip.telnyx.ca, sip.telnyx.eu & sip.telnyx.com.au.
​
If you attempt to register via our high volume short duration domain, you will receive a **SIP 405 Method Not Allowed** response.

## **Special Notes on SIP Registration**

![Breaking Line](_images/682991ade0be9812.png)

Please remember that SIP registration is required only for receiving **inbound calls**. You may come across scenarios where you are able to make outbound calls from your numbers associated with the credential based SIP Connection but outbound calling does not require SIP registration. To receive inbound calls, please ensure your system is registered to our SIP domains and use a low expiry refresh of around 180 seconds. This allows more frequent SIP Register requests so we can know where you are and where to route calls (via the address of record AOR on file). At the same time, you should monitor the trunks status and attempt a soft reload of the system in-case you are seeing the trunk status as down. Once a SIP Registrations expiry time is met, and we do not receive further SIP Register requests, we will no longer hold the AOR on file and can not route inbound calls to you. This is why we recommend a lower expiry time set. Often, a full restart of the phone system can resolve SIP Registration problems as well. It's always a good idea to take a network capture trace on the LAN in order to review the SIP behaviour - we'd be happy to help review the captures if you can share them.
​
Outbound calling requires **SIP authentication** for credential based SIP Connections. When you make an outbound call from a credential based SIP Connection, our system will issue a SIP 407 proxy authentication response - challenging you to verify who you are. You verify who you are by sending a new SIP INVITE with your SIP Connections credentials (username + password) hashed. Once we can verify the hash, we'll allow your outbound calls to proceed. This is a great [article](https://andrewjprokop.wordpress.com/2015/01/27/understanding-sip-authentication/) that discusses the authentication process in-depth.
​
Again, inbound and outbound are decoupled and use different methods to receive and make calls.

---

Related Articles

[SIP Connection: Fail-over and Retries](https://support.telnyx.com/en/articles/4320364-sip-connection-fail-over-and-retries)[Telnyx SIP Response Codes](https://support.telnyx.com/en/articles/4409457-telnyx-sip-response-codes)[Mitel: 5320E/5330E/5340E SIP](https://support.telnyx.com/en/articles/6244551-mitel-5320e-5330e-5340e-sip)[How Telnyx Handles SRV Records for SIP Calls](https://support.telnyx.com/en/articles/10666839-how-telnyx-handles-srv-records-for-sip-calls)[How to Configure SIP Attach using a UAC Connection](https://support.telnyx.com/en/articles/14805261-how-to-configure-sip-attach-using-a-uac-connection)

Did this answer your question?

😞😐😃
