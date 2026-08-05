---
title: SIP Connections
summary: A consolidated reference for configuring Telnyx SIP Connections in the Mission
  Control Portal, covering connection types (Credentials, IP, FQDN, UAC), authentication
  and routing, inbound and outbound settings, number formats, SIP URI calling, AnchorSite®
  media anchoring, webhooks, advanced options, and DID assignment.
sources:
- url: https://support.telnyx.com/en/articles/1130706-sip-connection-number-formats
- url: https://support.telnyx.com/en/articles/1130713-what-is-my-sip-account-connection-password
- url: https://support.telnyx.com/en/articles/1177115-how-to-setup-a-did-to-sip-connection
- url: https://support.telnyx.com/en/articles/14805261-how-to-configure-sip-attach-using-a-uac-connection
- url: https://support.telnyx.com/en/articles/2925713-sip-uri-calling
- url: https://support.telnyx.com/en/articles/4245868-sip-connection-types
- url: https://support.telnyx.com/en/articles/4351104-sip-connection-settings
- url: https://support.telnyx.com/en/articles/4404448-sip-connection-inbound-outbound-settings
- url: https://support.telnyx.com/en/articles/5271423-guide-to-sip-anchorsite-settings
updated_at: 2026-08-05T13:31:54Z
---

# SIP Connections

*Part 5 of 5 — see also: [Part 1](sip-connections--part-1.md), [Part 2](sip-connections--part-2.md), [Part 3](sip-connections--part-3.md), [Part 4](sip-connections--part-4.md)*

A consolidated reference for configuring Telnyx SIP Connections in the Mission Control Portal, covering connection types (Credentials, IP, FQDN, UAC), authentication and routing, inbound and outbound settings, number formats, SIP URI calling, AnchorSite® media anchoring, webhooks, advanced options, and DID assignment.

## Advanced Settings

### Encode Contact Header

Encodes the SIP contact header sent by Telnyx to avoid issues with NAT and ALG scenarios.

### DTMF Types

The DTMF Type setting specifies the type of DTMF to be used on the call. There are three options:

- **RFC 2833 (Recommended)** — standards-based mechanism to send DTMF digits in-band (RTP), supported by many vendors.
- **Inband** — sending information within the same band or channel used for data such as voice or video. Most prone to issues.
- **SIP Info** — SIP network elements transmit digits out-of-band as telephone-events in a reliable manner independent of the media stream.

### Enable On-Net T.38 Passthrough

Enable on-net T.38 if you prefer the sender and receiver negotiating T.38 directly. If disabled, Telnyx will be able to use T.38 on just one leg of the call depending on each leg's settings.

### Enable Comfort Noise for Call on Hold

When checked, Telnyx generates comfort noise when you place a call on hold. If unchecked, you will need to generate comfort noise or on-hold music to avoid RTP timeouts.

## RTCP Settings

RTP is used to transmit media between endpoints. As media traverses the endpoints, RTCP packets are generated periodically by both the caller and the called party. Unlike RTP, they don't contain media — RTCP packets report statistics about the ongoing call. Telnyx provides the ability to use either **RTCP+1** or **RTCP mux** at the connection level. Checking the "RTCP Capture and Storage" option enables the feature.

- **Report Frequency** — interval in seconds between sending RTCP packets back to the user's media IP while the call is in progress.
- **RTCP Port** — defaults to **RTCP+1**. The other option, **RTCP mux**, multiplexes both RTP and RTCP through a single UDP port, simplifying NAT traversal.

## Assigning DIDs to a SIP Connection

A DID is needed in order to receive inbound calls from the Telnyx network. You must assign a registered connection to a DID in order to receive inbound calls.

### Assigning a Single DID

1. Hover over the box beneath the **SIP Connection/App** header and click the pencil icon.
2. Select the connection you want to assign to the DID from the dropdown.

### Assigning Multiple DIDs

1. Select the check box to the left of the DIDs you want to edit.
2. Click the **Bulk update** button.
3. Paste all the numbers you want to update, click **Continue**, then **Edit Voice Settings**.
4. Select the desired SIP Connection in the connection field.
5. Click **Save**.

### DID Services

There are 7 different services offered on DIDs:

- e911
- Call Forwarding
- Caller ID Name Listing
- Caller ID Name (Incoming)
- Inbound Call Recording
- HD Voice
- Inbound Call Screening

## Managing Connections

### Connection ID

Once a connection is created, you can find the unique connection ID just below the settings sub tab of the SIP Connection. The [SIP Connections API](https://developers.telnyx.com/docs/voice/sip-trunking/configuration-guides/index#sip-trunking-configuration-guides) can be used to programmatically update SIP Connection settings.

### Deactivating or Disabling a SIP Connection

To deactivate or disable a SIP Connection, visit the SIP Connections page, select **Edit** on your desired SIP Connection, and click the toggle under the **Status** option. This deactivates the SIP Connection so inbound and outbound calls will not be processed.

## Troubleshooting UAC Connections

Before troubleshooting call routing, check the **Registration status** section on the UAC Connection.

- If status is *registered* but calls don't route, check the PBX dial plan and the Internal SIP URI configured in Telnyx.
- If status is *trying*, wait for the registration attempt to complete, then click **Refresh**. If it remains *trying* for several minutes or changes to *failed*, review **Last registration response**.
- If status is *failed*, review **Last registration response** and check the SIP username, password, auth username, proxy, transport, and PBX registrar settings.
- If status is *connection_disabled*, confirm the UAC Connection is enabled.
- After making changes, click **Refresh** to confirm the latest registration state.

### Connection Stuck in "Registering"

- Verify your PBX is reachable at the Proxy address from the public internet.
- Check that the port is correct (5060 for UDP/TCP, 5061 for TLS).
- Confirm no firewall is blocking SIP traffic from the Telnyx UAC IP.
- Verify the Transport setting matches what your PBX expects (UDP, TCP, or TLS).

### Registration Succeeds but Calls Don't Route

- On the PBX side: verify your PBX dial plan routes calls to the registered extension correctly and the extension is assigned to the right user or hunt group.
- On the Telnyx Mission Control Portal: confirm **Receive SIP Subdomain calls** is set correctly in Step 2 and your telephony resource (AI Assistant, Call Control Application) is correctly linked to this connection with the Internal SIP URI pointing to it.
- Verify the Internal SIP URI uses the correct extension-dialing format: `<extension>@<applicationFQDN>.sip.telnyx.com`. If set to a generic SIP URI such as `assistant-<id>@sip.telnyx.com`, registration may succeed but calls from the PBX will not route to the intended Telnyx application.
- If media (audio) isn't flowing, confirm your firewall allows RTP from the same UAC IP (Telnyx uses the same IP for signaling and media on UAC connections).

### Registration Expires Frequently

If your PBX rate-limits registrations or you see frequent re-registration cycles:

1. Edit the connection in the Mission Control Portal.
2. Increase the **Expiration (sec)** value in Step 2 (e.g., from 3600 to 7200).
3. Check your PBX's minimum and maximum registration interval settings — some PBX systems override the requested expiry.

## Related Articles

- [SIP Connection: Number Formats](sip-connection-number-formats.md)
- [SIP Connection: Types](sip-connection-types.md)
- [SIP Connection: Settings](sip-connection-settings.md)
- [SIP Connection: Inbound & Outbound Settings](sip-connection-inbound-outbound-settings.md)
- [SIP URI Calling](sip-uri-calling.md)
- [Guide to SIP AnchorSite® Settings](guide-to-sip-anchorsite-settings.md)
- [How to Configure SIP Attach using a UAC Connection](how-to-configure-sip-attach-using-a-uac-connection.md)
- [Telnyx SIP Response Codes](https://support.telnyx.com/en/articles/4409457-telnyx-sip-response-codes)
- [SIP Registration](https://support.telnyx.com/en/articles/4363904-sip-registration)
- [How to Configure a SIP Trunk](https://support.telnyx.com/en/articles/8096455-how-to-configure-a-sip-trunk)
