---
title: Telnyx Platform Reference
summary: A comprehensive reference for the Telnyx platform, covering AI, API, and
  telecom glossaries, the Number Lookup service, and the Telnyx Verify API including
  its quickstart, verification methods, custom templates, DTMF confirmation, webhooks,
  security best practices, and rate limiting for fraud prevention.
sources:
- url: https://developers.telnyx.com/docs/glossary/ai-glossary/index
- url: https://developers.telnyx.com/docs/glossary/api-glossary
- url: https://developers.telnyx.com/docs/glossary/telecom-glossary
- url: https://developers.telnyx.com/docs/identity/number-lookup/quickstart/index
- url: https://developers.telnyx.com/docs/identity/verify/custom-templates
- url: https://developers.telnyx.com/docs/identity/verify/dtmf-confirm
- url: https://developers.telnyx.com/docs/identity/verify/index
- url: https://developers.telnyx.com/docs/identity/verify/quickstart/index
- url: https://developers.telnyx.com/docs/identity/verify/rate-limiting-fraud-prevention
- url: https://developers.telnyx.com/docs/identity/verify/receiving-webhooks
- url: https://developers.telnyx.com/docs/identity/verify/security-best-practices
updated_at: 2026-06-11T10:29:44Z
---

# Telnyx Platform Reference

*Part 2 of 4 — see also: [Part 1](telnyx-platform-reference--part-1.md), [Part 3](telnyx-platform-reference--part-3.md), [Part 4](telnyx-platform-reference--part-4.md)*

A comprehensive reference for the Telnyx platform, covering AI, API, and telecom glossaries, the Number Lookup service, and the Telnyx Verify API including its quickstart, verification methods, custom templates, DTMF confirmation, webhooks, security best practices, and rate limiting for fraud prevention.

## API Glossary

| Term | Definition |
|---|---|
| API (Application Programming Interface) | A set of rules that allows software applications to communicate with each other. |
| API Documentation | Instructions and details on how to use an API. |
| API Key | A token passed in an API call to authenticate the client. |
| Basic Auth | Authentication method using a username and password encoded in base64. |
| Bearer Token | An access token used in the Authorization header. |
| DELETE | HTTP method to delete a resource. |
| Endpoint | A specific URL where an API can access the resources it needs. |
| Form Data | A way to send key-value pairs, often used with file uploads. |
| GET | HTTP method to retrieve data from a server. |
| GraphQL | A query language for APIs that enables clients to request specific data. |
| gRPC | A high-performance, open-source RPC framework by Google. |
| HTTP | Hypertext Transfer Protocol; the foundation of API communication. |
| HTTPS | Secure version of HTTP using encryption. |
| Header | Key-value pairs in HTTP requests and responses that provide metadata. |
| Idempotency | The property of an operation to have the same result no matter how many times it is applied. |
| JSON | JavaScript Object Notation; a lightweight data format used in API communication. |
| JWT (JSON Web Token) | A compact and self-contained method for securely transmitting information. |
| Multipart | A type of form data that allows multiple files or fields to be sent in a single request. |
| OAuth | An open-standard protocol for authorization. |
| OpenAPI | A specification for describing RESTful APIs. |
| PATCH | HTTP method to make partial updates to a resource. |
| POST | HTTP method to send data to a server. |
| PUT | HTTP method to update an existing resource. |
| Pagination | Splitting API responses into smaller parts or pages. |
| Payload | The actual data sent in a request or returned in a response. |
| REST | Representational State Transfer; an architecture for stateless communication. |
| RESTful API | An API that adheres to the REST architecture. |
| Rate Limiting | Restricting the number of API calls a client can make. |
| Request | An action initiated by a client to an API server. |
| Resource | An object or representation of something accessible via an API. |
| Response | The data sent back by the server after processing a request. |
| Route | The path portion of a URL used to access an API resource, excluding the domain and protocol. |
| SDK (Software Development Kit) | A collection of tools for building applications with an API. |
| Status Code | A number indicating the result of an HTTP request (e.g., 200, 404, 500). |
| Swagger | A set of tools for developing and documenting OpenAPI specifications. |
| Throttling | Intentionally slowing down the response rate from the API. |
| Versioning | Maintaining multiple iterations of an API (e.g., v1, v2). |
| Webhooks | Callbacks sent from the server to the client when an event occurs. |
| XML | Extensible Markup Language; another data format used in some APIs. |

## Telecom Glossary

| Term | Definition |
|---|---|
| ACD | Average Call Duration — Mean time a call lasts. |
| ANI | Automatic Number Identification — Identifies the caller's number. |
| ASR | Answer-Seizure Ratio — Ratio of answered to attempted calls. |
| B2BUA | Back-to-Back User Agent — VoIP architecture for media and signaling control. |
| CDR | Call Detail Record — Metadata generated for a telecom transaction. |
| CLD | Calling Line Destination — Identifies the called party's number in a VoIP call setup. |
| CLI | Calling Line Identification — Displays the caller's phone number. |
| CNAM | Caller Name — Displays the name associated with the caller's number. |
| CPE | Customer Premises Equipment — Devices installed at a customer's location. |
| CPaaS | Communications Platform as a Service — Telecom services offered via cloud. |
| Codec | Audio compression methods (G.711, G.729, Opus) used in VoIP. |
| DID | Direct Inward Dialing — Allows external callers to reach an internal extension. |
| DNIS | Dialed Number Identification Service — Identifies the number dialed by the caller, used for routing inbound VoIP calls. |
| DS0/DS1/DS3 | Digital Signal Levels — T-carrier transmission system levels (e.g., DS1 = T1 line). |
| DTLS | Datagram TLS — Used in WebRTC encryption. |
| DTMF | Dual Tone Multi-Frequency — Signals used for dialing and input (touch-tone). |
| E.164 | Numbering Format — International telephone numbering standard. |
| E911 | Enhanced 911 — Provides caller location info to emergency services. |
| ENUM | Telephone Number Mapping — Converts phone numbers to Internet addresses. |
| FAS | False Answer Supervision — Fraudulent call charge without real connection. |
| ICE | Interactive Connectivity Establishment — Helps with NAT traversal in VoIP. |
| IVR | Interactive Voice Response — Automated telephony system for user interaction. |
| Jitter | Variation in packet arrival time that can affect voice quality. |
| Jitter Buffer | Helps to smooth audio variations in VoIP packets. |
| LATA | Local Access and Transport Area — Geographic area for call routing. |
| LEC | Local Exchange Carrier — Provides local phone service. |
| LNP | Local Number Portability — Keep phone numbers when changing providers. |
| Latency | Delay between sending and receiving data. |
| MOS | Mean Opinion Score — Subjective quality rating of voice (1–5). |
| NPA-NXX | Numbering format: NPA = area code; NXX = central office code. |
| PBX | Private Branch Exchange — Internal phone switching system in organizations. |
| PDD | Post Dial Delay — Time from call initiation to ringing. |
| POTS | Plain Old Telephone Service — Basic analog phone service. |
| PRI | Primary Rate Interface — ISDN line with multiple voice/data channels. |
| PSTN | Public Switched Telephone Network — Traditional circuit-switched network. |
| QoS | Quality of Service — Measures reliability and performance of telecom service. |
| RTP | Real-Time Transport Protocol — Used for transmitting audio/video streams. |
| Rate Center | A geographic area used to determine local vs. long-distance calls. |
| SBC | Session Border Controller — Secures and manages VoIP traffic. |
| SDC | Short Duration Calling — Often used in VoIP fraud detection and SIP trunk analysis. |
| SHAKEN/STIR | Caller ID verification to prevent spoofing. |
| SIP | Session Initiation Protocol — Initiates and manages VoIP calls. |
| SIP Proxy | A SIP server that routes and forwards SIP requests, enforcing policy and facilitating call setup. |
| SIP Trunk | Virtual VoIP trunk line — Replaces traditional PRI. |
| SIPS | SIP over TLS — Secure VoIP signaling. |
| SRTP | Secure RTP — Encrypts RTP media streams. |
| STUN/TURN | Servers to support NAT traversal in real-time communications. |
| T.38 | Protocol for Fax over IP (FoIP). |
| TLS | Transport Layer Security — Encrypts communications over IP. |
| UCaaS | Unified Communications as a Service — Integrated voice, video, messaging. |
| VoIP | Voice over Internet Protocol — Sends voice over IP networks. |
| WebRTC | Web Real-Time Communication — Browser-based real-time media exchange. |
