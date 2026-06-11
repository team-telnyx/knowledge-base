---
source_url: https://support.telnyx.com/en/articles/4409457-telnyx-sip-response-codes
scraped: 2026-06-11
---

Telnyx SIP Response Codes | Telnyx Help Center

[Skip to main content](#main-content)

# Telnyx SIP Response Codes

This article highlights the SIP response codes Telnyx uses and their unique meanings!

Written by David

May 6, 2026

Table of contents

At Telnyx, we have many different situations and settings that can result in a particular SIP response code sent back to your client. We realized that there are so many situations that may result in the same response code, it was necessary to distinguish them so our customers can have further clarity on why some of their calls did not complete as expected.

The aim of this article is to list all the SIP response codes that can be expected and expand on their meaning, along with providing feedback on how to workaround them. We'll also discuss some special cases and include ISDN cause codes and their related hangup reasons.

# SIP Response Codes

The format of the response codes is as follows: D1X, D2X, D3X...D9X

These mainly cover 4XX response codes from Telnyx. There are a few errors outside of the DX range such as PX, RX, TX, VX.

---

## B3

### 488 Media Encryption Required B3

The connection has been configured to use SRTP media encryption, but the INVITE they are sending doesn't offer encrypted media. To correct this, either configure their SIP devices to offer encrypted media, or disable encrypted media for that SIP connection.

## D1X

### D1 - 403 User channel limit exceeded D1

The number of concurrent **outbound** calls for the account is over the limit. This relates to the global account concurrent call limit set in your [outbound voice profile](https://portal.telnyx.com/#/app/outbound-profiles) section. Should you need this increased, please reach out to our support team.

### D10 - 403 Forbidden D10

The number of concurrent outbound calls for the user's account is over the limit.

### D11 - 403 Destination Number #{destination\_number} is invalid D11

The outbound call was rejected as the destination number is invalid. Please reach out to support if this issue occurs.

### D12 - 403 Destination Number #{destination\_number} is not allowed for service plan #{service\_plan} D12

The destination number is not authorized for the service plan of the OB profile associated with the connection making the call. The customer can change the service plan associated with the OB profile. This is a legacy code and will not be used moving forward. An example is using a legacy service plan such as "US-48/CAN" and attempting to dial Alaska or Hawaii, two states not considered apart of this service plan. The workaround is changing the service plan to International and including America as whitelisted destination in the North American region.

### D13 - 403 Dialed number #{e164} (pertinent countries: #{pertinent\_countries}) is not included in whitelisted countries: #{whitelisted\_countries} D13

The dialled number is not a number from whitelisted countries present in the outbound voice profile associated with the connection making the call. To solve this, the customer can add the dialled numbers country to the whitelist of the given outbound voice profile.

### D14 - 404 Dialed number is not valid D14

Simple put, the number dialed is invalid. We ask that the user verify that calls to this number can be reached outside of our network. There is also this great open source [tool by google](https://libphonenumber.appspot.com/) which can be used to validate whether a number is valid or not.

### D15 - 403 Outbound Profile is disabled D15

The outbound voice profile associated with the SIP Connection used to place the termination call is not active. Go to your [outbound voice profile](https://portal.telnyx.com/#/app/outbound-profiles) section and ensure the status of the profile is active and in green. If it is, please refresh the status by toggling it off and back on again.

### D16 - 403 Connection is disabled D16

The SIP Connection used to place the termination call is not active. Go to your [SIP Connections](https://portal.telnyx.com/#/app/connections) page and ensure the status of the SIP Connection is active and in green. If it is, please refresh the status by toggling it off and back on again.

### D17 - 403 Account is disabled D17

The Account used to place the termination call is blocked. Please contact support so they can investigate the cause for the account block. If your account was blocked, you would have received an email to indicate why.

### D18 - 404 Not found D18

The SIP Connection used to receive the origination call is not active. Go to your [SIP Connections](https://portal.telnyx.com/#/app/connections) page and ensure the status of the SIP Connection is active and in green. If it is, please refresh the status by toggling it off and back on again.

### D19 - 404 Not found D19

The Account used to receive the origination call is billing blocked. Have you checked that your account is in positive balance, if not please top up your account to ensure services are restored.

---

## D2X

### D2 - 403 OB profile channel limit exceeded D2

The number of concurrent calls for the specific outbound voice profile is over the limit. This limit is configurable can be adjusted by customer in their outbound profile settings.

### D21 - 480 Temporarily Unavailable D21

The destination number has no associated destination, no other number to forward to has been found or no IP destinations or credential authentication information have been found. This can occur when a SIP Connection is assigned to a number but either the SIP Connection is not registered to our system (if credential based) or the IP's/FQDN's are not set at the DID's routing settings.

### D22 - 403 Channel limit exceeded D22

User, outbound voice profile or SIP Connection **channel limits** have been exceeded. Please increase any channel limits specified on your DID's if using the channel billing method, SIP Connections or Outbound Voice Profiles.

### D24 - 403 Maximum destination rate limit exceeded D24

This is when you dial a number in which the rate per minute exceeds the maximum rate per minute set on your outbound voice profile. Please increase the rate per minute on your [outbound voice profile settings](https://portal.telnyx.com/#/app/outbound-profiles).

### D25 - 403 Unable to locate an account/number using IP #{caller\_ip} and username #{username} D25

We are unable to locate account/number with the IP and username used in your SIP INVITE to our system. Please reach out to support for further assistance.

### D26 - 403 Connection for caller not present D26

Caller does not have a connection present when attempting outbound calls. Please check that a SIP Connection exists with the username and/or IP from which you are calling, and that it is associated with an outbound voice profile.

### D29 - 403 Invalid X-Telnyx-Token #{telnyx\_auth\_token} or IP #{caller\_ip} D29

The SIP INVITE we received contains an Invalid X-Telnyx-Token with IP. Please ensure the token matches what was set on the expert settings of the SIP Connection. Tokens are used to segregate traffic that come where different SIP Connections share the same IP address.

---

## D3X

### D3 - 403 Connection channel limit exceeded D3

The number of concurrent calls for the Connection is over the limit, this limit can be adjusted by the customer in the SIP Connection outbound settings.

### D30 - 403 Invalid SIP URI calling preference D30

User SIP URI calling preference cannot be validated. This can apply on both inbound and outbound calls to SIP URI's. Please make sure the SIP URI you are calling is valid.

### D31 - 403 Invalid SIP Subdomain Receive Settings D31

This can occur on outbound calls to SIP Subdomains where we were unable to validate the users SIP Subdomain. The user should refresh their SIP Subdomain settings on the SIP Connections inbound settings and retry - otherwise contact support for further assistance.

### D34 - 403 Source country is not from EEA D34

The customers Outbound Voice Profile service plan is set to EEA but the caller ID in the SIP INVITE is not from EEA. This is a legacy code and will generally not be seen anymore as our service plans have since changed on our outbound voice profile offering.

### D35 - 403 Invalid Caller Origination Number D35

Caller Origination Number is Invalid. The Caller ID in your SIP INVITE is not valid. Our caller ID policy is explained in more detail [here](https://support.telnyx.com/en/articles/3546251-caller-id-number-policy). In short, please make sure your FROM/PAID/RPID headers contain +E.164 number formats.

### D36 - 403 Forbidden D36

You are attempting to make an outbound call with a caller ID of a number which belongs to another Telnyx user. Please ensure you use your own DID's as Caller ID on your outbound calls.

### D37 - 403 Emergency calls not authorized with call control D37

Emergency outbound calls aren't authorized using our call control product.

### D38 - 403 Connection has no Outbound Profile assigned D38

Connection has no Outbound Profile assigned D38

1. Log into the [Telnyx Portal](https://portal.telnyx.com/).
2. navigate to **Voice Suite → SIP Trunking**.
3. Select your SIP connection.
4. Scroll down to the **Outbound Settings** section.
5. Assign or create a new **Outbound Voice Profile**.
6. Save your configuration. If "default" is the only available profile and you cannot create new profiles, your account may require further verification.

### D39 - 403 International daily spent limit reached D39

User's daily spent limit reached for international calling. Please reach out to support.

---

## D4X

### D4 - 486 User Busy D4

The number of concurrent calls for the Connection is over the limit, the limit can be adjusted by the customer in SIP Connection inbound settings.

### D40 - 404 Not Found D40

For outbound calls, we know the destination exists but we were unable to find a route to connect the call. This usually applies to on-net calling. Please contact support for further assistance so they can advise.

### D41 - 403 Forbidden D41

The dialled number matches a prefix that is forbidden to be used. This is a fraud preventative measure, especially for prefixes that are known for revenue sharing and toll pumping. Please contact support for further assistance.

### D42 - 405 SIP Method Not Allowed D42

Call transfer (SIP REFER method) not allowed.

### D44 - 403 Invalid value for connection\_id D44

The requested connection\_id is either invalid or does not exist.

### D46 - 403 Originating number listed in do-not-originate registry D46

An originating number was used to make an outbound call even even though these numbers are used to only ever receive inbound calls.

### D48 - 480 No IPs or FQDNs found for this number routing table D48

Misconfigured Telnyx SIP connection with missing data.

### D49 - 403 The originator number is invalid D49

The origination number is from NANPA but does not have a valid LRN.

---

## D5X

### D5 - 486 User Busy D5

The number of concurrent calls for all numbers under Legacy Channel Billing is over the limit. The channel limit can be increased on the [channels page](https://portal.telnyx.com/#/app/numbers/channels). More information regarding channel billing is available [here](https://support.telnyx.com/en/articles/1130678-channel-billing-and-how-to-use-it).

### D50 - 404 The destination number is invalid. D50

The destination number is from NANPA but does not have a valid LRN.

### D51 - 403 Unverified origination number D51

A call attempt using a non-Telnyx number that [has not been verified](https://support.telnyx.com/en/articles/6988813-verified-numbers) will be rejected with a "403 Unverified Caller Origination Number D51" SIP error.

### D52 - 603 Restricted origination number D52

Inbound call was rejected by Inbound Call Screening feature.

### D53 - 403 Forbidden D53 origin same as destination number

The origination number is the same as the destination number (loop prevention).

### D54 - 403 Restricted origination number D54

Outbound call rejection based on the originating caller ID number, which is currently restricted from originating outbound calls through Telnyx due to reputation concerns and risk validations. This restriction is based on multiple external reputation databases, which Telnyx uses to block spam traffic.

### D56 - 486 User Busy D56

The number of concurrent calls for all numbers under **Global Channel Billing** is over the limit, this is set by users in the [channels page](https://portal.telnyx.com/#/app/numbers/channels). More information regarding global channel billing is available [here](https://support.telnyx.com/en/articles/8428806-global-channel-billing).

**D57 - 403 HD voice is disabled for this phone number**

This error happens when HD voice is disabled.  
You attempted to make a call with HD voice enabled, but this feature is not activated for the phone number you're using.

To resolve, enable HD voice for your phone number in your Telnyx account settings.

### D58 - 403 Restricted destination number D58

Please contact Telnyx support at [support@telnyx.com](mailto:support@telnyx.com) .

**D59 -** *404 The special call is not supported D59*

This error occurs when a call to a short or special number is not supported by the originating number’s country or region. For instance, a caller from France (+34xx) dialing 911 (a US emergency number) would trigger this error, as 911 is not recognized as a valid number for French origin numbers.

---

## D6X

# D60 - 403 Can not make calls to non-verified numbers at this account level

The user portal level doesn't allow this type of calls, they should upgrade their account to a higher level.

Your account's current tier does not permit calls to non-verified numbers.

To resolve, verify the destination number or upgrade your account to a higher tier that permits these call types.

# D61: "486 Busy Here D61"

The user portal level doesn't allow this type of calls, they should upgrade their account to a higher level.

Your account's current tier does not permit this type of inbound call.

To resolve, upgrade your account to a higher tier that permits these call types.

## D63 - Origination number is not ported yet D63

Outbound calls from Telnyx numbers with status 'port pending' are not allowed.

## D64 - Origination number is not ready D64

Outbound calls from Telnyx numbers with status `requirement-info-pending` or `requirement-info-under-review are not allowed

## D65 - 486 User Busy D65

Inbound calls calls to Telnyx numbers with status `requirement-info-pending` or `requirement-info-under-review are allowed only 1 hour after the number has been purchased but playing a preamble message that says the number is for testing purposes only. After that calls are rejected with code D65

---

## D7X

### D7 - 403 Connection has no Outbound Profile assigned D7

The SIP Connection does not have an outbound voice profile associated with it. Please ensure you associate an [outbound voice profile](https://support.telnyx.com/en/articles/4320411-more-about-outbound-voice-profiles) in order for calls to be terminated.

---

## D8X

### D8 - 404 Invalid caller ID number for emergency services D8

An outbound call towards an emergency number where an valid caller ID number was not provided. Please make sure you use the DID's with E911 enabled on outbound calls toward emergency numbers. This is a legacy sip response code. At this time, we process all calls to emergency numbers but if a caller ID is used that is not a DID on your account or is a DID on your account but without E911 enabled, there will be a surcharge of $100.

---

## D9X

### D9 - 403 International destination rate limit reached D9

The international destination rate limit has been reached. This is a legacy SIP response code but may apply when attempting to call the same international number several times within a 60 second period. Please reach out to support to have this limit extended.

---

## PE1

### PE1 - 503 Service Unavailable

For outbound calls, we were unable to connect your call as no available routes were found. A 503 is returned in this instance to allow your system to failover to another carrier should you employ back ups. If you do not employ back ups, please reach out to our support team for assistance. This is generally considered a normal temporary failure.

## PE2, PE3, PE4, PE5, PE6

***503 no routes found***

Telnyx's routing service could not find available routes to complete your call to the destination number. This is a temporary failure that indicates routing is unavailable for this destination at this time

---

## P0X

### P01 - 403 Forbidden P01

The Telnyx SIP Proxy responds with this error message when a request, such as a SIP BYE, contains an invalid R-URI. It typically occurs when the **Telnyx SIP Proxy's own anycast IP address** is specified in the R-URI instead of the contact header IP of our back to back user agent (see the 200 OK response).

* Bad Example: BYE sip:12313456789@**192.76.120.10:5060**;transport=tcp SIP/2.0
* Good Example: BYE sip:12313456789@**10.13.67.4**:**5070**;transport=tcp SIP/2.0

This is sometimes a tricky one to resolve. Often it's caused by a customer's SIP server seeing the private IP address in our SIP messages (which is perfectly fine and should not cause any problem) and presuming that it must be "fixed". It's also often caused by a customer's NAT/ALG, which can do the same thing. Sometimes, switching the UDP port used by the SIP server is enough to thwart the ALG.

Another possible solution to this problem is to enable the "encode contact header" feature on your SIP Connection. This obscures the private IP address in our Contact address so that the ALG won't recognise it.

When this error happens, it's often for BYE requests, as mentioned above, but it also happens for ACK requests (when a call is answered). When this happens, the SIP transaction is broken and the result is a dropped call after 32 seconds.

Lastly, it's also possible for the R-URI to be correct but still receive this error. Closely inspect your BYE and make sure the **route** headers are included in the same order as they were defined in our SIP INVITE's **record route** headers. If the route headers are missing in your BYE request, then we have no way to ensure your request signalling traverses the same proxies used on our side to handle the call.

Reference: <https://www.rfc-editor.org/rfc/rfc3261.html#section-12.1.1>

### P02 - 403 Forbidden P02

This is a response to a CANCEL request. It means that our SIP proxy server can't find the INVITE. It's rare for this to happen, but can happen during maintenance periods, when our anycast IP address is moved from one server to another.

### P03 - 403 Method Unsupported P03

A SIP request is received and the method doesn't match one of the standard 14 request methods, so it is rejected.

### P03 - 403 Forbidden P03

A forbidden/unsupported request method is received

**P04 - 403 Forbidden**

A REGISTER request with a To tag is not supported and non-RFC-compliant. OR A CANCEL request is received but there's no INVITE transaction in memory to

get CANCELed.

You sent either a REGISTER request with a To tag (which violates RFC standards and is rejected for security reasons), or a CANCEL request for a call that doesn't exist in the system.

To resolve, ensure your SIP client sends RFC-compliant REGISTER requests without To tags, and only send CANCEL requests for active call attempts.

**P05 - 503 CPS Limit Reached**

The IP address or username being used to make new calls has reached the CPS limit, so gets rejected. Please try again in a few seconds.

Your IP address or credential username has exceeded the Calls Per Second (CPS) rate limit.

To resolve, wait a few seconds and retry, reduce your call initiation rate, or contact Telnyx support if you need a higher CPS limit.

### P06 - 513 Message too large P06

A SIP request is received and it's over the 6144-byte limit in size, so it is rejected.

---

## P14

### 403 Request-URI Too Long P14

The RURI is too long, at over 512 bytes.

---

# P15

**503 CPS Limit reached**

The IP address or username being used to make new calls has reached the CPS limit, so gets rejected. Please try again in a few seconds.

Your IP address has exceeded the Calls Per Second (CPS) rate limit specifically for REGISTER requests.

To resolve, wait a few seconds and retry, reduce your registration request rate, or contact Telnyx support if you need a higher CPS limit for registrations.

---

# P16

**403 Forbidden**

A REGISTER request with a To tag is not supported and non-RFC-compliant.

You sent a REGISTER request with a To tag, which violates RFC standards and is rejected for security reasons.

To resolve, ensure your SIP client sends RFC-compliant REGISTER requests without To tags.

---

## P18

### 403 Forbidden P18

This happens when we receive an INVITE that has an empty destination address in either the RURI or the To address. We must reject such a request that has no destination number.

---

## P29

**500 Internal Server Error**

REGISTER request failed to get processed at internal registrars.

Your REGISTER request could not be processed by Telnyx's internal registration servers. This may be due to timeouts, server maintenance, or system failures.

To resolve, retry your registration attempt. If the problem persists, contact Telnyx support immediately as this indicates a serious system issue.

---

## P43

### 403 Forbidden P43

A SIP request was received on the websocket port, without websocket protocol.

---

## P43

### 403 Contact header field too long P51

A request is received and the Contact lenght is over 512 bytes, so it is rejected.

---

# R47

**403 Too Many Contacts**

**New in KSS v25 (April 2025)**

A REGISTER request attempts to add multiple Contact addresses, which is forbidden.

Your REGISTER request tried to register multiple Contact addresses simultaneously, which is not allowed.

To resolve, register only one Contact address per REGISTER request.

## P81 UO1

### 403 Forbidden P81 U01

This is a response that can be presented when attempting to send a SIP REGISTER request where the To-header user part contains 3 characters or less. SIP credential based Connection usernames must contain 4 or more alphanumeric characters, so shorter usernames can never work.

---

## P82 UO2

### 403 Forbidden P82 UO2

This happens when a REGISTER request contains invalid characters in the username. Valid characters are letters (upper and lower case) and digits only.

---

## P83 UO2

### 483 Too Many Hops P83

The call has had too many hops (lop prevention).

---

## P93

### 403 Method unsupported P93

The method specified in the Request-Line is understood, but not allowed. An example is the **MESSAGE** method, which we do not currently support for sending messages through SIP.

---

## PE1, PE2, PE3 & PE4

### 503 Service Unavailable or 503 No Routes Found

This error is returned when Telnyx could not identify an available route to terminate a customers outbound call. Please contact Telnyx support for assistance with this error.

---

## R14, R16, R17 & R18

### 403 Forbidden R14

The authentication username is an empty string.

### 403 Forbidden R16

The authentication username has invalid characters in it.

### 403 Forbidden R17

The authentication username is shorter than four characters.

### 403 Forbidden R18

The authentication username does not match the TO and FROM user parts, which is a requirement of registration.

---

## RG1

### 480 Not Found RG1

User not registered. We could not connect the inbound call as the users credential based SIP Connection is not registered.

---

## TV1

### 503 Service Unavailable TV1

Telnyx is unable to connect the call due to termination issues likely with multiple downstream carriers.

---

# TM1

**403 No Rates Found**

Telnyx does not offer coverage for this destination, as there are no rates for this prefix in the user rate deck.

The destination you're trying to call is not covered by Telnyx, or there are no pricing rates configured for this destination prefix in your rate deck.

To resolve, verify the destination number is correct, check if Telnyx offers coverage for this destination, or contact Telnyx support to inquire about coverage availability.

---

## IDSN Cause Codes & Hangup Reasons

ISDN cause codes are used to describe reasons for hang up, they are PSTN based codes which are included in the "Reason" header of SIP response. When the ISDN network or remote user disconnects a call for any reason, the cause might be reported by any ISDN-aware application. They don't necessarily indicate an error as cause codes are shown at the end of normally terminated calls as-well. They are simply guidelines and are implementation-dependent.  
​  
An example is: ***Reason: Q.850;cause=21;text="CALL\_REJECTED"***, where the ISDN cause code is 21 and the hangup reason is call rejected. This generally maps to a SIP 403 response.

Please reference this [page](https://developer.signalwire.com/freeswitch/FreeSWITCH-Explained/Troubleshooting-Debugging/Hangup-Cause-Code-Table_3964945/) which provides a detailed breakdown for each cause code, their relevant hangup reason and associated SIP response mapping.

---

## Special Notes on SIP Response Code 488

At this moment in time, and specifically for **488 not acceptable** responses with the reason header incompatible destination, we do not explicitly highlight the reasons for them. We list certain scenarios below where this response code can be seen and why it can occur.

At a high level, this error code generally relates to a misconfiguration in your ***SIP INVITEs SDP***, ***183 with SDP***, ***200 OK with SDP***, ***ACK with SDP*** for late negotiation or a misconfiguration with a setting on your Telnyx account.

**Example scenarios in which you may receive this response code if:**

1. You send a private IP address in your SDP

   1. For example: **c=10.10.10.10**
2. You send a re-invite for T.38 on inbound calls but do not have the T.38 fax gateway setting enabled on your DID's expert settings.
3. You send a re-invite for T.38 on your outbound calls but do not have the T.38 fax setting set to "Customer" or have it set to "Disabled" on your SIP Connections outbound settings.
4. You send a SIP INVITE with an IPV6 media IP address, something we do not currently support. Please ensure media IP address are IPV4.
5. You send a SIP INVITE, on your outbound calls, with a codec we do not currently support. For a list of supported codecs, please see this [page](https://sip.telnyx.com/#codecs).
6. You send a 200 OK, on your inbound calls, with a codec we do not currently support. In this scenario, we'll actually send a BYE with a hangup cause of INCOMPATIBLE\_DESTINATION and an ISDN cause code of 88.
7. You send a SIP INVITE, on your outbound calls, **with** encryption media attributes in the SDP but have not specified the encryption type on your SIP Connections outbound settings such as SRTP.
8. You send a SIP INVITE, on your outbound calls, **without** encryption media attributes in the SDP but have specified the encryption type on your SIP Connections outbound settings such as SRTP. In this scenario, we'll actually send a BYE with a hangup cause of INCOMPATIBLE\_DESTINATION and an ISDN cause code of 88.
9. You send a 183 or 200 OK, on your inbound calls, **with** encryption media attributes in the SDP but have not specified the encryption type on your SIP Connection inbound settings such as SRTP. In this scenario, we'll actually send a BYE with a hangup cause of INCOMPATIBLE\_DESTINATION and an ISDN cause code of 88.
10. You send a 183 or 200 OK, on your inbound calls, **without** encryption media attributes in the SDP but have specified the encryption type on your SIP Connection inbound settings such as SRTP. In this scenario, we'll actually send a BYE with a hangup cause of INCOMPATIBLE\_DESTINATION and an ISDN cause code of 88.

---

## Final Notes on SIP Response codes

These errors are subject to change and may be updated in the future.

Most of these errors are self explanatory and following the above workaround suggestions and/or making the appropriate changes or refreshes on your account, will generally resolve these issues.

If you have attempted to resolve these issues but still have difficulty, please contact our support team providing example calls, SIP message logs or SIP Call ID. As a reminder, please leverage your [debugging tool](https://support.telnyx.com/en/articles/4304872-telnyx-debugging-tools) which can help provide insight into the SIP logs and the exact responses.

---

---

Related Articles

[Configuring a Cisco CUBE/CUCM SIP Trunk](https://support.telnyx.com/en/articles/1130673-configuring-a-cisco-cube-cucm-sip-trunk)[SIP Connection: Settings](https://support.telnyx.com/en/articles/4351104-sip-connection-settings)[How to Configure a SIP Trunk](https://support.telnyx.com/en/articles/8096455-how-to-configure-a-sip-trunk)[BYOC: Telnyx & Genesys](https://support.telnyx.com/en/articles/8268122-byoc-telnyx-genesys)[Telnyx + Vapi Integration](https://support.telnyx.com/en/articles/12538402-telnyx-vapi-integration)

Did this answer your question?

😞😐😃

Table of contents
