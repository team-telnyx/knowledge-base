---
title: SIP Connections
summary: This page covers Telnyx SIP Connections comprehensively, including connection
  types (credential, IP, FQDN, and Call Control authentication), telephony credentials
  (SIP Connection Credentials, On-Demand Credentials, and JSON Web Tokens), inbound
  and outbound settings (number formats, transport protocols, ringback, codecs, encryption,
  and timeouts), webhook configuration with Park Outbound Calls, AnchorSite® media
  anchoring, advanced settings (DTMF, T.38, comfort noise), RTCP settings, SIP URI
  Calling, Outbound Voice Profiles, concurrent outbound call limits, and the tagging
  feature for organizing services.
sources:
- url: https://support.telnyx.com/en/articles/1130706-sip-connection-number-formats
- url: https://support.telnyx.com/en/articles/1130717-limits-on-concurrent-outbound-calls
- url: https://support.telnyx.com/en/articles/1130721-distinguish-your-outbound-profiles-dids
- url: https://support.telnyx.com/en/articles/2925713-sip-uri-calling
- url: https://support.telnyx.com/en/articles/4245868-sip-connection-types
- url: https://support.telnyx.com/en/articles/4320411-more-about-outbound-voice-profiles
- url: https://support.telnyx.com/en/articles/4351104-sip-connection-settings
- url: https://support.telnyx.com/en/articles/4404448-sip-connection-inbound-outbound-settings
- url: https://support.telnyx.com/en/articles/7029684-telephony-credentials-types
updated_at: 2026-07-17T09:06:41Z
---

# SIP Connections

*Part 4 of 4 — see also: [Part 1](sip-connections--part-1.md), [Part 2](sip-connections--part-2.md), [Part 3](sip-connections--part-3.md)*

This page covers Telnyx SIP Connections comprehensively, including connection types (credential, IP, FQDN, and Call Control authentication), telephony credentials (SIP Connection Credentials, On-Demand Credentials, and JSON Web Tokens), inbound and outbound settings (number formats, transport protocols, ringback, codecs, encryption, and timeouts), webhook configuration with Park Outbound Calls, AnchorSite® media anchoring, advanced settings (DTMF, T.38, comfort noise), RTCP settings, SIP URI Calling, Outbound Voice Profiles, concurrent outbound call limits, and the tagging feature for organizing services.

## Outbound Voice Profiles

The Outbound Voice Profile section of your Telnyx portal is where you manage Service Plans, Billing Methods, and Traffic Types for outbound voice traffic. You can also view your Account Level Outbound Concurrent Call Limit at the top right of the page.

### Setting Up an Outbound Voice Profile

The Outbound Voice Profiles section is found on the left-hand list of portal modules. If it is your first time, you will be greeted with a blank section and a prompt to add a new profile.

### Outbound Profile Information

Enter a name and the profile will be created. You will see the name and the Profile ID, a unique string used to identify the voice profile for API calls, CDR reports, etc. You can also apply a "tag" to the profile for tracking, billing, and reporting purposes.

### International Allowed Destinations

Choose the international destinations you would like to allow calls to terminate to. There are 255 destinations broken down into 10 regions. You can add an entire region or pick individual countries. Many destinations require Level 2 verification before activation.

### Associated Connections and Applications

View the connections or applications assigned to the profile. Add them using "Add connections/apps to profile" and tick the box next to the desired Connections/Apps. FQDN connections cannot be assigned from here — you must assign them from the Connection's outbound settings in the SIP Connections section.

### Billing Method

The only billing method available is the "Rate Deck" option, where outbound calls are rated based on the destination number prefix. You can download and view the rate deck and request custom rates.

### Advanced Settings

- **Assign a Billing Group** — Select billing groups from a drop-down menu to manage customer sub-accounts and categorise usage reports and end-of-month invoice records.
- **Channel Limit** — Set a limit for outbound concurrent channels (1 call = 1 channel). If the limit is reached, additional calls will be rejected.
- **Max Destination Rate** — Maximum rate (price per minute) for a destination to be allowed when making outbound calls. Calls to destinations exceeding this rate will be rejected.
- **Enable Daily Spend Limit Per Connection** — Define the maximum amount that can be spent on outbound calls per day for each connection. A day resets at 00:00:00 UTC. Once spending exceeds the threshold, outbound calls are blocked and an email notification is sent to the account owner.

### Record Outbound Calls

Enable Call Recording for all outbound calls or only those with a specific ANI (from number). Choose between WAV and MP3 audio formats, and between Single Channel (mono with both parties on the same track) and Double Channel (stereo with caller on one track and callee on the other).

### Termination Endpoint

You may encounter the error "There is another Connection with the same IP address already assigned to an Outbound Voice Profile" when attempting to associate a SIP Connection with an Outbound Voice Profile. Connections should be unique so they can be properly identified. Connections can share the same IP address as long as they have a unique combination with either a Tech Prefix or a Token. The IP address port is not used for authentication purposes.

This is applicable in cases where customers use BYOC (Bring Your Own Carrier) with a fixed IP address. To solve this, specify an expert IP authentication method in the basic settings of your SIP Connection. The easiest method is the tech prefix, but the best way is to use a token, where you include `X-Telnyx-Token` as a header in your SIP INVITE with the token generated on your SIP Connection.

## Concurrent Outbound Call Limits

By default, new Telnyx accounts are set to a global value of 2 concurrent outbound calls. Upon approval for Level 2 verification, this increases to 10 concurrent calls. To increase beyond this, Level 2 verified accounts can reach out to support@telnyx.com. It is recommended to provide information on your use case if you wish to increase channels beyond 100.

When the concurrent outbound call channel limit has been reached, Telnyx returns the SIP error response: **403 User channel limit exceeded D1**. This relates to the global account concurrent call limit set in your outbound voice profile.

## Tagging Feature

Beyond using connections, Telnyx Mission Control has a Tagging feature for additional filtering and organization. On both the Numbers and Outbound Profile pages, you will see the Tag icon next to each record. Hovering over the icon shows all Tags associated with that service. Clicking the icon brings up the Tags Modal/Window to add/remove Tags. These tags can be used as filters when pulling CDRs and are included as part of the record within a CDR.

Common uses for tagging:

- Tagging services with the Department/End-User they belong to
- Tagging services with the Office Location they belong to
- Tagging Numbers with their purchase date
- Tagging services to group together all of a single client's services
- Tagging services before performing troubleshooting for easier identification

**Note:** For inbound calls where DIDs are tagged, the CDR report will show the DID's associated tag. For outbound calls, the CDR report will show the tag assigned to the outbound voice profile only, not the tag assigned at the DID.

## Testing Your Setup

The Telnyx WebRTC test application is built using the JavaScript WebRTC SDK to showcase the WebRTC platform and make it easier to test your setup.

- If testing using SIP Connection Credentials or On-Demand Credentials, set Authentication to "Credential" and enter your credential information.
- If testing using a JSON Web Token, set Authentication to "Token" and enter your token under "Login Token".

## WebRTC Applications

If you choose to build a WebRTC application, you can create a credential authentication-based connection. Once created, you will be provided with (or can edit) a username and password. You can then specify the DNIS number format as the SIP Username so that when inbound calls arrive toward your DIDs associated with the SIP Connection, Telnyx will send the username of the SIP Connection in the SIP INVITE.

Don't forget to select the VP8/9 codecs in the advanced settings of the inbound section of the SIP Connection. This allows Telnyx to send the SIP INVITE to your WebRTC application with these codecs in the media parameters, which are ideal for video.
