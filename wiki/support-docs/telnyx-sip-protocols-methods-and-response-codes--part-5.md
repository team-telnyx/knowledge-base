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

*Part 5 of 5 — see also: [Part 1](telnyx-sip-protocols-methods-and-response-codes--part-1.md), [Part 2](telnyx-sip-protocols-methods-and-response-codes--part-2.md), [Part 3](telnyx-sip-protocols-methods-and-response-codes--part-3.md), [Part 4](telnyx-sip-protocols-methods-and-response-codes--part-4.md)*

This page consolidates Telnyx's SIP protocol documentation, covering supported transport protocols (UDP, TCP, TLS), the full set of SIP request methods and response classes defined in RFC 3261, Telnyx-specific custom response codes (D1X–D9X, PE, P0X, R1X, RG1, TV1, TM1), ISDN cause codes, the PRACK extension (RFC 3262), and step-by-step configuration of an Audiocodes 400HD IP phone with Telnyx Mission Control.

## Configuring an Audiocodes 400HD with Telnyx

The [AudioCodes 400HD](https://www.audiocodes.com/media/3063/audiocodes-400hd-ip-phones.pdf) series of IP phones includes a range of easy-to-use, feature-rich products for the service provider, hosted services, unified communications, enterprise IP telephony, and contact center markets. The setup and configuration of the Audiocodes 400HD is almost identical to that of the [Grandstream GXP](https://support.telnyx.com/en/articles/5815720-grandstream-gxp-telnyx-setup).

Additional documentation:

- [User manual](https://www.audiocodes.com/media/9627/ltrt-11939-430hd-and-440hd-ip-phone-for-microsoft-skype-for-business-users-manual-ver-301.pdf)
- [Admin manual](https://www.audiocodes.com/media/13525/400hd-series-ip-phone-for-microsoft-skype-for-business-administrators-manual-ver-312.pdf)

### Pre-requisites

- Ensure that your [Telnyx Mission Control Portal is configured properly](https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account).
- RECOMMENDED: [Enable TLS to encrypt your traffic](https://support.telnyx.com/en/articles/1130711-does-telnyx-encrypt-communication).

### Step 1: Get the Device IP Address and Log In

1. From the phone, navigate to **Menu > Device Status > Network Settings > IP Address** and take note of the IP address.
2. On a computer connected to the same network, open a web browser and type `http://` followed by the phone's IP address into the address bar.
3. Log into the portal. Out of the box, the default credentials are:
   - **Username:** `admin`
   - **Password:** `1234`

   ![Credential entry boxes.](_images/82bbb92cc9e86b1f.png)

4. The landing page appears:

   ![Audio Codec landing page.](_images/58499ce6283eb240.png)

### Step 2: Configure the 400HD

1. From the left-hand navigation, make sure you're on the **Configuration** tab and click the **+ Quick Setup** folder to expand it.
2. Find the **SIP Proxy and Registrar** section and provide the following information:
   - **Use SIP Proxy:** *Enable*
   - **Proxy IP Address or Host Name:** `sip.telnyx.com`
   - **Proxy Port:** `5060` if you have not enabled TLS encryption. If you have, choose `5061`.
   - **Use SIP Proxy IP and Port for Registration:** *Enable*
   - **Use SIP Registrar:** *Disable*

   ![Signaling protocol.](_images/fbe19b914d565564.png)

   *This screenshot shows a UDP setup.*

3. Find the **Line Settings** section and provide the following information:
   - **Line Number:** `1`
   - **Line 1 Activate:** *Enable*
   - **Line 1 Display Name:** Your caller ID. Caller ID Name should be in capital letters. Do not use any special characters, as they will not be displayed. Spaces are allowed. Some regular Canadian providers will not show more than 15 characters, so consider shrinking or adapting your caller ID.
   - **Line 1 User ID:** Your Telnyx account ID
   - **Line 1 Authentication User Name:** Your Telnyx account ID
   - **Line 1 Authentication Password:** Your Telnyx account password

   ![Quick Setup section.](_images/8af49a15b01628a1.png)

### Step 3: Network Settings (TLS Encryption Only)

Follow this section only if you are using TLS encryption on your account. Ensure that you have [enabled TLS to encrypt your traffic](https://support.telnyx.com/en/articles/1130711-does-telnyx-encrypt-communication) on your Telnyx portal.

1. Navigate to **Voice Over IP > Signaling Protocols** and enter the following information:
   - **SIP Transport Protocol:** *TLS*
   - **TLS Port:** `5061`
   - **SIP Local Port:** `5081`
   - **Proxy IP Address or Host Name:** `sip.telnyx.com:5061`
   - **Proxy Port:** `5061`
   - **Use SIP Proxy IP and Port for Registration:** *Disable*
   - **Use SIP Outbound Proxy:** *Disable*

   ![SIP general.](_images/620124a57195cc9c.png)

2. Enable SRTP. Navigate to **Voice Over IP > Media Streaming** and enter the following information:
   - **SRTP Encryption and Authentication:** *REQUIRE ENCRYPTION*
   - **Method:** *AES_CM_128_ALL_METHODS*
   - **Negotiation mode:** *Basic*
   - **ARIA:** *Disable*

   ![Media streaming section.](_images/9f1e2f1c342cb378.png)

### Step 4: Configure Registration Time and NAT Keep Alive

1. From the left-hand panel, go to **Voice Over IP > Signaling Protocols** and enter the following information:
   - **Enable Registrar Keep Alive:** *Enable*
   - **Registrar Keep Alive Period:** `50 Seconds`
   - **Registration Expires:** `300 Seconds`

   ![Signaling protocol section.](_images/4ee3650c380c92d5.png)

### Step 5: Configure Audio Codecs

Go to **Voice Over IP > Media Streaming** and set your codecs in priority sequence that meets your needs.

Telnyx supports the following codecs:

1. `ulaw` (g711u)
2. `alaw` (g711a)
3. `g722`
4. `g729`

## Debugging and Further Reading

For debugging SIP call flows, see the [Telnyx Debugging Tools](https://support.telnyx.com/en/articles/4304872-telnyx-debugging-tools) available on your account.

Further reading on PRACK:

- [DUCKS GO QUACK. SIP GOES PRACK](https://andrewjprokop.wordpress.com/2013/10/02/ducks-go-quack-sip-goes-prack/) by Andrew J Prokop.
- [What the Prack?!](https://www.youtube.com/watch?v=NCH06mYUajQ) by Lalo Nunez.

Further reading on SIP responses and trunking:

- [SIP Response Codes: Need to Know in 2 Minutes](https://telnyx.com/resources/sip-response-codes-need-know-2-minutes)
- [SIP Trunking Explained](https://telnyx.com/resources/sip-trunking-explained)

## Final Notes

Telnyx SIP response codes are subject to change and may be updated in the future. Most errors are self-explanatory and following the workaround suggestions and/or making the appropriate changes or refreshes on your account will generally resolve these issues. If you have attempted to resolve these issues but still have difficulty, contact Telnyx support providing example calls, SIP message logs, or SIP Call ID. Leverage the [Telnyx Debugging Tools](https://support.telnyx.com/en/articles/4304872-telnyx-debugging-tools) to help provide insight into the SIP logs and the exact responses.
