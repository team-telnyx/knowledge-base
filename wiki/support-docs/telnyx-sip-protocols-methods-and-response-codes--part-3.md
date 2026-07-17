---
title: Telnyx SIP Protocols, Methods, and Response Codes
summary: This page consolidates Telnyx's SIP protocol documentation, covering supported
  transport protocols (UDP, TCP, TLS), the full set of SIP request methods and response
  classes defined in RFC 3261, Telnyx-specific custom response codes (D1X–D9X, PE,
  P0X, R1X, RG1, TV1, TM1), ISDN cause codes, the PRACK extension (RFC 3262), and
  step-by-step configuration of an Audiocodes 400HD IP phone with Telnyx Mission Control.
sources:
- url: https://support.telnyx.com/en/articles/1130705-sip-protocols-that-telnyx-uses
- url: https://support.telnyx.com/en/articles/4304898-sip-trunking-methods-requests-responses
- url: https://support.telnyx.com/en/articles/4409457-telnyx-sip-response-codes
- url: https://support.telnyx.com/en/articles/5819923-audiocodes-400hd
- url: https://support.telnyx.com/en/articles/6902981-understanding-sip-prack-protocol
updated_at: 2026-07-17T09:06:54Z
---

# Telnyx SIP Protocols, Methods, and Response Codes

*Part 3 of 5 — see also: [Part 1](telnyx-sip-protocols-methods-and-response-codes--part-1.md), [Part 2](telnyx-sip-protocols-methods-and-response-codes--part-2.md), [Part 4](telnyx-sip-protocols-methods-and-response-codes--part-4.md), [Part 5](telnyx-sip-protocols-methods-and-response-codes--part-5.md)*

This page consolidates Telnyx's SIP protocol documentation, covering supported transport protocols (UDP, TCP, TLS), the full set of SIP request methods and response classes defined in RFC 3261, Telnyx-specific custom response codes (D1X–D9X, PE, P0X, R1X, RG1, TV1, TM1), ISDN cause codes, the PRACK extension (RFC 3262), and step-by-step configuration of an Audiocodes 400HD IP phone with Telnyx Mission Control.

## Telnyx-Specific SIP Response Codes

Telnyx uses a number of custom SIP response codes to provide additional clarity on why calls may not complete as expected. The format of these codes is D1X, D2X, D3X...D9X, primarily covering 4xx response codes. There are also a few errors outside of the DX range such as PX, RX, TX, and VX.

### B3

- **488 Media Encryption Required B3** — The connection has been configured to use SRTP media encryption, but the INVITE being sent doesn't offer encrypted media. To correct this, either configure the SIP devices to offer encrypted media, or disable encrypted media for that SIP connection.

### D1X

- **D1 — 403 User channel limit exceeded** — The number of concurrent outbound calls for the account is over the limit. This relates to the global account concurrent call limit set in your [outbound voice profile](https://portal.telnyx.com/#/app/outbound-profiles) section. Contact support to have this increased.
- **D10 — 403 Forbidden** — The number of concurrent outbound calls for the user's account is over the limit.
- **D11 — 403 Destination Number #{destination_number} is invalid** — The outbound call was rejected as the destination number is invalid. Contact support if this issue occurs.
- **D12 — 403 Destination Number #{destination_number} is not allowed for service plan #{service_plan}** — The destination number is not authorized for the service plan of the OB profile associated with the connection making the call. The customer can change the service plan associated with the OB profile. This is a legacy code. An example is using a legacy service plan such as "US-48/CAN" and attempting to dial Alaska or Hawaii. The workaround is changing the service plan to International and including America as a whitelisted destination in the North American region.
- **D13 — 403 Dialed number #{e164} (pertinent countries: #{pertinent_countries}) is not included in whitelisted countries: #{whitelisted_countries}** — The dialled number is not from whitelisted countries present in the outbound voice profile associated with the connection making the call. Add the dialled number's country to the whitelist of the given outbound voice profile.
- **D14 — 404 Dialed number is not valid** — The number dialed is invalid. Verify that calls to this number can be reached outside of the Telnyx network. Google's [libphonenumber tool](https://libphonenumber.appspot.com/) can be used to validate whether a number is valid.
- **D15 — 403 Outbound Profile is disabled** — The outbound voice profile associated with the SIP Connection used to place the termination call is not active. Go to your [outbound voice profile](https://portal.telnyx.com/#/app/outbound-profiles) section and ensure the status of the profile is active and in green. If it is, refresh the status by toggling it off and back on again.
- **D16 — 403 Connection is disabled** — The SIP Connection used to place the termination call is not active. Go to your [SIP Connections](https://portal.telnyx.com/#/app/connections) page and ensure the status of the SIP Connection is active and in green. If it is, refresh the status by toggling it off and back on again.
- **D17 — 403 Account is disabled** — The Account used to place the termination call is blocked. Contact support so they can investigate the cause for the account block. If your account was blocked, you would have received an email to indicate why.
- **D18 — 404 Not found** — The SIP Connection used to receive the origination call is not active. Go to your [SIP Connections](https://portal.telnyx.com/#/app/connections) page and ensure the status of the SIP Connection is active and in green. If it is, refresh the status by toggling it off and back on again.
- **D19 — 404 Not found** — The Account used to receive the origination call is billing blocked. Check that your account is in positive balance; if not, top up your account to ensure services are restored.

### D2X

- **D2 — 403 OB profile channel limit exceeded** — The number of concurrent calls for the specific outbound voice profile is over the limit. This limit is configurable and can be adjusted by the customer in their outbound profile settings.
- **D21 — 480 Temporarily Unavailable** — The destination number has no associated destination, no other number to forward to has been found, or no IP destinations or credential authentication information have been found. This can occur when a SIP Connection is assigned to a number but either the SIP Connection is not registered to the system (if credential based) or the IPs/FQDNs are not set at the DID's routing settings.
- **D22 — 403 Channel limit exceeded** — User, outbound voice profile, or SIP Connection channel limits have been exceeded. Increase any channel limits specified on your DIDs (if using the channel billing method), SIP Connections, or Outbound Voice Profiles.
- **D24 — 403 Maximum destination rate limit exceeded** — The rate per minute for the dialled number exceeds the maximum rate per minute set on your outbound voice profile. Increase the rate per minute on your [outbound voice profile settings](https://portal.telnyx.com/#/app/outbound-profiles).
- **D25 — 403 Unable to locate an account/number using IP #{caller_ip} and username #{username}** — Telnyx is unable to locate an account/number with the IP and username used in your SIP INVITE. Contact support for further assistance.
- **D26 — 403 Connection for caller not present** — Caller does not have a connection present when attempting outbound calls. Check that a SIP Connection exists with the username and/or IP from which you are calling, and that it is associated with an outbound voice profile.
- **D29 — 403 Invalid X-Telnyx-Token #{telnyx_auth_token} or IP #{caller_ip}** — The SIP INVITE received contains an invalid X-Telnyx-Token with IP. Ensure the token matches what was set on the expert settings of the SIP Connection. Tokens are used to segregate traffic that comes where different SIP Connections share the same IP address.

### D3X

- **D3 — 403 Connection channel limit exceeded** — The number of concurrent calls for the Connection is over the limit; this limit can be adjusted by the customer in the SIP Connection outbound settings.
- **D30 — 403 Invalid SIP URI calling preference** — User SIP URI calling preference cannot be validated. This can apply on both inbound and outbound calls to SIP URIs. Make sure the SIP URI you are calling is valid.
- **D31 — 403 Invalid SIP Subdomain Receive Settings** — This can occur on outbound calls to SIP Subdomains where Telnyx was unable to validate the user's SIP Subdomain. Refresh the SIP Subdomain settings on the SIP Connections inbound settings and retry, otherwise contact support.
- **D34 — 403 Source country is not from EEA** — The customer's Outbound Voice Profile service plan is set to EEA but the caller ID in the SIP INVITE is not from EEA. This is a legacy code and will generally not be seen anymore.
- **D35 — 403 Invalid Caller Origination Number** — Caller Origination Number is invalid. The Caller ID in your SIP INVITE is not valid. See the [Caller ID Number Policy](https://support.telnyx.com/en/articles/3546251-caller-id-number-policy). In short, ensure your FROM/PAID/RPID headers contain +E.164 number formats.
- **D36 — 403 Forbidden** — You are attempting to make an outbound call with a caller ID of a number which belongs to another Telnyx user. Ensure you use your own DIDs as Caller ID on your outbound calls.
- **D37 — 403 Emergency calls not authorized with call control** — Emergency outbound calls aren't authorized using the call control product.
- **D38 — 403 Connection has no Outbound Profile assigned** — The connection has no Outbound Profile assigned. To resolve:
  1. Log into the [Telnyx Portal](https://portal.telnyx.com/).
  2. Navigate to **Voice Suite → SIP Trunking**.
  3. Select your SIP connection.
  4. Scroll down to the **Outbound Settings** section.
  5. Assign or create a new **Outbound Voice Profile**.
  6. Save your configuration. If "default" is the only available profile and you cannot create new profiles, your account may require further verification.
- **D39 — 403 International daily spent limit reached** — User's daily spent limit reached for international calling. Contact support.

### D4X

- **D4 — 486 User Busy** — The number of concurrent calls for the Connection is over the limit; the limit can be adjusted by the customer in SIP Connection inbound settings.
- **D40 — 404 Not Found** — For outbound calls, the destination exists but Telnyx was unable to find a route to connect the call. This usually applies to on-net calling. Contact support for further assistance.
- **D41 — 403 Forbidden** — The dialled number matches a prefix that is forbidden to be used. This is a fraud preventative measure, especially for prefixes that are known for revenue sharing and toll pumping. Contact support for further assistance.
- **D42 — 405 SIP Method Not Allowed** — Call transfer (SIP REFER method) not allowed.
- **D44 — 403 Invalid value for connection_id** — The requested connection_id is either invalid or does not exist.
- **D46 — 403 Originating number listed in do-not-originate registry** — An originating number was used to make an outbound call even though these numbers are used to only ever receive inbound calls.
- **D48 — 480 No IPs or FQDNs found for this number routing table** — Misconfigured Telnyx SIP connection with missing data.
- **D49 — 403 The originator number is invalid** — The origination number is from NANPA but does not have a valid LRN.

### D5X

- **D5 — 486 User Busy** — The number of concurrent calls for all numbers under Legacy Channel Billing is over the limit. The channel limit can be increased on the [channels page](https://portal.telnyx.com/#/app/numbers/channels). See [Channel Billing and How to Use It](https://support.telnyx.com/en/articles/1130678-channel-billing-and-how-to-use-it).
- **D50 — 404 The destination number is invalid** — The destination number is from NANPA but does not have a valid LRN.
- **D51 — 403 Unverified origination number** — A call attempt using a non-Telnyx number that [has not been verified](https://support.telnyx.com/en/articles/6988813-verified-numbers) will be rejected with a "403 Unverified Caller Origination Number D51" SIP error.
- **D52 — 603 Restricted origination number** — Inbound call was rejected by Inbound Call Screening feature.
- **D53 — 403 Forbidden (origin same as destination number)** — The origination number is the same as the destination number (loop prevention).
- **D54 — 403 Restricted origination number** — Outbound call rejection based on the originating caller ID number, which is currently restricted from originating outbound calls through Telnyx due to reputation concerns and risk validations. This restriction is based on multiple external reputation databases, which Telnyx uses to block spam traffic.
- **D56 — 486 User Busy** — The number of concurrent calls for all numbers under Global Channel Billing is over the limit; this is set by users in the [channels page](https://portal.telnyx.com/#/app/numbers/channels). See [Global Channel Billing](https://support.telnyx.com/en/articles/8428806-global-channel-billing).
- **D57 — 403 HD voice is disabled for this phone number** — You attempted to make a call with HD voice enabled, but this feature is not activated for the phone number you're using. To resolve, enable HD voice for your phone number in your Telnyx account settings.
- **D58 — 403 Restricted destination number** — Contact Telnyx support at [support@telnyx.com](mailto:support@telnyx.com).
- **D59 — 404 The special call is not supported** — This error occurs when a call to a short or special number is not supported by the originating number's country or region. For instance, a caller from France (+34xx) dialling 911 (a US emergency number) would trigger this error.

### D6X

- **D60 — 403 Can not make calls to non-verified numbers at this account level** — The user portal level doesn't allow this type of calls; upgrade the account to a higher level. The account's current tier does not permit calls to non-verified numbers. To resolve, verify the destination number or upgrade the account to a higher tier that permits these call types.
- **D61 — 486 Busy Here** — The user portal level doesn't allow this type of calls; upgrade the account to a higher level. The account's current tier does not permit this type of inbound call. To resolve, upgrade the account to a higher tier that permits these call types.
- **D63 — Origination number is not ported yet** — Outbound calls from Telnyx numbers with status 'port pending' are not allowed.
- **D64 — Origination number is not ready** — Outbound calls from Telnyx numbers with status `requirement-info-pending` or `requirement-info-under-review` are not allowed.
- **D65 — 486 User Busy** — Inbound calls to Telnyx numbers with status `requirement-info-pending` or `requirement-info-under-review` are allowed only 1 hour after the number has been purchased but play a preamble message that says the number is for testing purposes only. After that, calls are rejected with code D65.

### D7X

- **D7 — 403 Connection has no Outbound Profile assigned** — The SIP Connection does not have an outbound voice profile associated with it. Associate an [outbound voice profile](https://support.telnyx.com/en/articles/4320411-more-about-outbound-voice-profiles) in order for calls to be terminated.

### D8X

- **D8 — 404 Invalid caller ID number for emergency services** — An outbound call towards an emergency number where a valid caller ID number was not provided. Make sure you use the DIDs with E911 enabled on outbound calls toward emergency numbers. This is a legacy SIP response code. At this time, all calls to emergency numbers are processed, but if a caller ID is used that is not a DID on your account or is a DID on your account but without E911 enabled, there will be a surcharge of $100.

### D9X

- **D9 — 403 International destination rate limit reached** — The international destination rate limit has been reached. This is a legacy SIP response code but may apply when attempting to call the same international number several times within a 60 second period. Contact support to have this limit extended.

### PE Codes

- **PE1 — 503 Service Unavailable** — For outbound calls, Telnyx was unable to connect the call as no available routes were found. A 503 is returned to allow your system to failover to another carrier should you employ back-ups. If you do not employ back-ups, contact support. This is generally considered a normal temporary failure.
- **PE2, PE3, PE4, PE5, PE6 — 503 No Routes Found** — Telnyx's routing service could not find available routes to complete your call to the destination number. This is a temporary failure that indicates routing is unavailable for this destination at this time.

### P0X

- **P01 — 403 Forbidden** — The Telnyx SIP Proxy responds with this error when a request, such as a SIP BYE, contains an invalid R-URI. It typically occurs when the Telnyx SIP Proxy's own anycast IP address is specified in the R-URI instead of the contact header IP of the back-to-back user agent (see the 200 OK response).
  - Bad Example: `BYE sip:12313456789@192.76.120.10:5060;transport=tcp SIP/2.0`
  - Good Example: `BYE sip:12313456789@10.13.67.4:5070;transport=tcp SIP/2.0`

  This is sometimes tricky to resolve. Often it's caused by a customer's SIP server seeing the private IP address in Telnyx's SIP messages (which is perfectly fine and should not cause any problem) and presuming that it must be "fixed". It's also often caused by a customer's NAT/ALG, which can do the same thing. Sometimes, switching the UDP port used by the SIP server is enough to thwart the ALG.

  Another possible solution is to enable the "encode contact header" feature on your SIP Connection. This obscures the private IP address in the Contact address so that the ALG won't recognise it.

  When this error happens, it's often for BYE requests, but it also happens for ACK requests (when a call is answered). When this happens, the SIP transaction is broken and the result is a dropped call after 32 seconds.

  Lastly, it's also possible for the R-URI to be correct but still receive this error. Closely inspect your BYE and make sure the route headers are included in the same order as they were defined in Telnyx's SIP INVITE's record route headers. If the route headers are missing in your BYE request, then there is no way to ensure your request signalling traverses the same proxies used on Telnyx's side to handle the call. Reference: [RFC 3261 Section 12.1.1](https://www.rfc-editor.org/rfc/rfc3261.html#section-12.1.1).

- **P02 — 403 Forbidden** — This is a response to a CANCEL request. It means that the SIP proxy server can't find the INVITE. It's rare for this to happen, but can happen during maintenance periods, when the anycast IP address is moved from one server to another.
- **P03 — 403 Method Unsupported** — A SIP request is received and the method doesn't match one of the standard 14 request methods, so it is rejected. Also returned as "403 Forbidden" for a forbidden/unsupported request method.
- **P04 — 403 Forbidden** — A REGISTER request with a To tag is not supported and non-RFC-compliant, OR a CANCEL request is received but there's no INVITE transaction in memory to get CANCELed. To resolve, ensure your SIP client sends RFC-compliant REGISTER requests without To tags, and only send CANCEL requests for active call attempts.
- **P05 — 503 CPS Limit Reached** — The IP address or username being used to make new calls has reached the CPS limit, so gets rejected. Try again in a few seconds. To resolve, wait a few seconds and retry, reduce your call initiation rate, or contact Telnyx support if you need a higher CPS limit.
- **P06 — 513 Message Too Large** — A SIP request is received and it's over the 6144-byte limit in size, so it is rejected.
- **P14 — 403 Request-URI Too Long** — The RURI is too long, at over 512 bytes.
- **P15 — 503 CPS Limit Reached** — The IP address has exceeded the Calls Per Second (CPS) rate limit specifically for REGISTER requests. To resolve, wait a few seconds and retry, reduce your registration request rate, or contact Telnyx support if you need a higher CPS limit for registrations.
- **P16 — 403 Forbidden** — A REGISTER request with a To tag is not supported and non-RFC-compliant. To resolve, ensure your SIP client sends RFC-compliant REGISTER requests without To tags.
- **P18 — 403 Forbidden** — This happens when an INVITE is received that has an empty destination address in either the RURI or the To address. Such a request must be rejected.
- **P29 — 500 Internal Server Error** — REGISTER request failed to get processed at internal registrars. To resolve, retry your registration attempt. If the problem persists, contact Telnyx support immediately as this indicates a serious system issue.
- **P43 — 403 Forbidden** — A SIP request was received on the websocket port, without websocket protocol.
- **P51 — 403 Contact header field too long** — A request is received and the Contact length is over 512 bytes, so it is rejected.
- **R47 — 403 Too Many Contacts** (New in KSS v25, April 2025) — A REGISTER request attempts to add multiple Contact addresses, which is forbidden. To resolve, register only one Contact address per REGISTER request.
- **P81 U01 — 403 Forbidden** — This is a response that can be presented when attempting to send a SIP REGISTER request where the To-header user part contains 3 characters or less. SIP credential based Connection usernames must contain 4 or more alphanumeric characters, so shorter usernames can never work.
- **P82 U02 — 403 Forbidden** — This happens when a REGISTER request contains invalid characters in the username. Valid characters are letters (upper and lower case) and digits only.
- **P83 U02 — 483 Too Many Hops** — The call has had too many hops (loop prevention).
- **P93 — 403 Method Unsupported** — The method specified in the Request-Line is understood, but not allowed. An example is the MESSAGE method, which Telnyx does not currently support for sending messages through SIP.

### R1X

- **R14 — 403 Forbidden** — The authentication username is an empty string.
- **R16 — 403 Forbidden** — The authentication username has invalid characters in it.
- **R17 — 403 Forbidden** — The authentication username is shorter than four characters.
- **R18 — 403 Forbidden** — The authentication username does not match the TO and FROM user parts, which is a requirement of registration.

### RG1

- **RG1 — 480 Not Found** — User not registered. Telnyx could not connect the inbound call as the user's credential based SIP Connection is not registered.

### TV1

- **TV1 — 503 Service Unavailable** — Telnyx is unable to connect the call due to termination issues likely with multiple downstream carriers.

### TM1

- **TM1 — 403 No Rates Found** — Telnyx does not offer coverage for this destination, as there are no rates for this prefix in the user rate deck. To resolve, verify the destination number is correct, check if Telnyx offers coverage for this destination, or contact Telnyx support to inquire about coverage availability.
