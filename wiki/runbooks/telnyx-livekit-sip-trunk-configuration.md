---
title: 'Telnyx & LiveKit: SIP Trunk Configuration'
summary: Telnyx SIP Trunks integrate seamlessly with LiveKit for real-time audio and video applications.
sources:
  - url: https://developers.telnyx.com/docs/voice/sip-trunking/livekit-configuration-guide/index
    content_hash: cb03a216451ecdd148eb739d962fb4c14f65e3d6b2c73c26684849db7f4aa633
updated_at: 2026-04-10T00:00:00Z
---

# 'Telnyx & LiveKit: SIP Trunk Configuration'

Telnyx SIP Trunks integrate seamlessly with LiveKit for real-time audio and video applications. This guide walks you through the easy setup process, ensuring optimal performance with minimal configuration.

## Purpose of this document

This configuration guide is designed to help you establish and optimize a SIP Trunk between Telnyx, a global leader in VoIP communications, and LiveKit, a robust platform for building real-time audio and video applications.

The primary objective of this document is to provide a comprehensive, step-by-step approach for configuring your SIP Trunk setup. This guide caters to both beginners and experienced professionals, ensuring that all readers can effectively integrate these two powerful services. By the end of this guide, you will be able to:

\*\*1. Set Up Telnyx: \*\* Configure your Telnyx account and SIP Trunk settings to prepare for integration.

**2. Configure LiveKit:** Adjust your LiveKit settings to accept and manage Telnyx SIP Trunk communications.

**3. Add Custom X-Headers**: In your app set `X-Telnyx-Username: <username>` to ensure your calls are properly routed. `username` has to be same value as your authentication username.

**4. Debug and Optimize**: Troubleshoot common issues and fine-tune your configuration for optimal performance.

## Configuration in Telnyx Mission Control Portal

Follow the steps below to create a SIP connection to your LiveKit account.

Your checklist:

* 1. Have an account created on Telnyx portal
* 2. Complete L2 verification process
* 3. Purchase a number to be used for the voice calls

### 1. SIP Connection

* In the Telnyx Mission Control Portal choose a “Real-Time Communications” -> “Voice” ->  “SIP Trunking” menu on the left sidebar
* Click “Add SIP Connection” button

<img alt="SIP Connection in Mission Control Portal" />

* Provide a name for your new SIP Connection
* Select FQDN as a type of connection
* Create a sip connection

<img alt="Create SIP Connection" />

* Choose “FQDN” as a connection type
* Provide SIP URI obtained from your LiveKit account. You can find it in your project settings page.
* Save FQDN settings with “Add” button

<img alt="Add FQDN" />

* Switch to the “Outbound Calls Authentication” tab in the Authentication & Routing Configuration section
* Choose “Credentials” for the Authentication Method
* Provide your user name and password which will be used later for the LiveKit outbound trunk configuration

<img alt="Authentication & Routing Configuration" />

* On top of SIP Connection page switch to the Outbound tab
* Select an existing Outbound Voice Profile from a dropdown list.
* If no profile is available you can create a one with a “Create New Outbound Voice Profile” link

<img alt="Edit SIP Connection" />

* Finally save your sip connection with a “Save” button at the bottom of the page

<img alt="Save SIP Connection" />

### 2. Programmable Voice Applications

Integration over SIP trunk with LiveKit allows also to redirect voice calls originated from LiveKit to Telnyx Voice AP applicationsI. With that option you can implement advanced voice applications with the features like listed below:

* Call recording
* IVR (Interactive Voice Response)
* TTS (Text-To-Speech)
* STT (Speech-To-Text / Call transcription)
* Conversational AI (Voice bots with different AI models)
* and many more

To configure the voice application:

* Switch to  a “Real-Time Communications” -> “Voice” ->  “Programmable Voice” menu on the left sidebar
* Create a new application with an  “Add New App” button
* Provide a name for your application
* Configure webhooks URL to receive webhooks about call status changes

<img alt="Configure Your Voice API Applications in the Mission Control Portal" />

* In the Inbound section provide a subdomain name (later you need to use it in a LiveKit outbound trunk setup)
* In the Outbound section select an outbound voice profile
* Save the voice app configuration

<img alt="Inbound & Outbound Settings" />

### 3. Outbound Voice Profile

* Switch to  a “Real-Time Communications” -> “Voice” ->  “Outbound Voice Profile” menu on the left sidebar
* Add a new Profile and provide a name for it
* Or you can adjust the existing profile with clicking on the  edit icon

<img alt="Configure Your Outbound Voice Profiles in the Mission Control Portal" />

* Select the destinations which should be allowed to make outbound calls to
* Click “Save” button to confirm your configuration

<img alt="Edit Your Outbound Voice Profile" />

### 4. Number configuration

* Switch to  a “Real-Time Communications” -> “Voice” ->  “My Numbers” menu on the left sidebar
* For the number(s) you would like to use for the LiveKit voice participants, select your LiveKit sip connection from a dropdown list presented in the “SIP connections” column
* Update your configuration with a “Save” button
* You can purchase additional numbers in a “Buy Numbers” menu
* The same SIP connection may be assigned to multiple numbers

<img alt="My Numbers in the Mission Control Portal" />

#

## Configuration in LiveKit

Follow the steps below to configure a SIP trunk for your LiveKit account.

Your checklist:

* 1. SIP URI is available in your project settings
* 2. LiveKit CLI is installed on your computer
* 3. ENV variables have been configured

Please refer to LiveKit [Quick Start](https://docs.livekit.io/sip/quickstart/) page for detailed SIP configuration instructions

### 1. Create Inbound SIP Trunk

* Create a json file (inboundTrunk.json) with the configuration of your inbound sip trunk
* Provide a name for your trunk and a number to be used (or an array of the comma delimited numbers)

```json theme={null}
{
   "trunk": {
       "name": "Demo Inbound Trunk",
       "numbers": ["1234567890"]
   }
}
```

* Run LiveKit CLI command to create an inbound trunk

```
lk sip inbound create inboundTrunk.json
```

* In the response you will receive a trunk ID

```
SIPTrunkID: <your-trunk-id>
```

### 2. Create Inbound Dispatch Rule

* Create a json file (dispatchRule.json)
* Provide a name for your rule, a trunk ID from the previous step and room name to which incoming calls should be connected

```json theme={null}
{
   "name": "Demo Dispatch Rule",
   "trunk_ids": ["<your-trunk-id>"],
   "rule": {
       "dispatchRuleDirect": {
           "roomName": "my-sip-room",
           "pin": ""
       }
   }
}
```

* Run LiveKit CLI command to create a dispatch rule

```
lk sip dispatch create dispatchRule.json
```

### 3. Create Outbound SIP Trunk

* Create a json file (outboundTrunk.json) with the configuration of your outbound sip trunk
* Provide a name for your trunk
* In the address parameter provide “sip.telnyx.com” if you configured a SIP connection on Telnyx side
* If you want to make calls to the configured Voice App, for the address parameter provide a subdomain configured in the Inbound section of your voice application
* Provide username and password you set in your sip trunk configuration for the Outbound Calls Authentication.
* Credentials should be left blank when connecting to the subdomain of your Voice App.

```json theme={null}
{
   "trunk": {
       "name": "Demo Outbound Trunk",
       "address": "sip.telnyx.com",
       "numbers": ["1234567890"],
       "auth_username": "<outbound-user>",
       "auth_password": "<outbound-pass>"
   }
}
```

* Run LiveKit CLI command to create an outbound trunk

```
lk sip outbound create outboundTrunk.json
```

* In the response you will receive a trunk ID

```
SIPTrunkID: <your-trunk-id>
```

### **4. Set custom headers when sending SIP INVITEs**

To make sure **every outbound call is authenticated against *your* Telnyx SIP trunk and account**, you should send your Telnyx SIP username in a custom SIP header on the **very first** `INVITE`.

**Why this is important**\
Telnyx supports two ways to authenticate SIP calls:

1. **Credential (SIP digest) authentication**
2. Using a username and password.
3. **IP-based authentication**
4. Matching calls by their source IP address.

By default, LiveKit sends the first `INVITE` **without** a username. In that case, Telnyx will:

1. Try to match the call to any existing **SIP IP connection** whose IP matches the source IP.
2. Only send a `407 Proxy Authentication Required` challenge if no matching IP connection is found.

In shared or cloud environments (like LiveKit Cloud), it’s possible for the same IP address to be associated with more than one Telnyx connection (even across different customers). If Telnyx finds a matching IP connection:

* It **won’t send the 407 challenge.**
* It will treat the call as authenticated as **that other connection**, not your FQDN trunk.
* This can lead to calls being billed or routed under the wrong trunk/account.

By always including **your unique Telnyx SIP username** in a header, you force Telnyx to use **credential-based authentication** for your FQDN connection and avoid any accidental IP-based [matches. ](http://matches.How)

[**How**](http://matches.How)\*\* it works\*\*

1. LiveKit sends an `INVITE` to Telnyx with your username in a custom header.
2. Telnyx sees the username and responds with `407 Proxy Authentication Required` .
3. LiveKit sends a second `INVITE` with the username + encrypted password.
4. Telnyx validates the credentials and authenticates the call against **your** FQDN connection.

> **Important:** The header value **must exactly match** the username you configured for credential authentication on your Telnyx FQDN connection (for example, the one you set in the Telnyx Portal or via the API).

Example configuration (LiveKit trunk JSON)

```

{
  "trunk": {
    "name": "My outbound trunk",
    "address": "sip.telnyx.com",
    "numbers": ["+15555555555"],
    "authUsername": "<your_telnyx_username>",
    "authPassword": "<your_telnyx_password>",

    "headers_to_attributes": {
      "X-Telnyx-Username": "authUsername"
    }
  }
}
```

In this example:

* `authUsername` is your **unique Telnyx SIP username**
* `X-Telnyx-Username` is the custom SIP header Telnyx will read
* The `headers_to_attributes` mapping tells LiveKit to populate `X-Telnyx-Username` with the same value as `authUsername`

### 5. Testing Outbound Calls

* To test an outbound call you can initiate a call with a CLI command
* Create a json file (sipParticipant.json) providing outbound trunk ID obtained in the previous step
* Provide a number to be called in a sip\_call\_to parameter
* Provide a room name, participant identity and name

```json theme={null}
{
	"sip_trunk_id": "<your-trunk-id>",
	"sip_call_to": "<phone-number-to-dial>",
	"room_name": "my-sip-room",
	"participant_identity": "sip-test",
	"participant_name": "Test Call"
}
```

* Run LiveKit CLI command to make an outbound call

```
lk sip participant create sipParticipant.json
```

#

## Troubleshooting

In Telnyx Mission Control Portal we are providing debugging tools where you can troubleshoot any issues with your SIP trunk communication checking SIP call flows, QoS stats and communication to a defined webhooks.

### 1. Debugging tool

* Go to the “Debugging” menu under “Reporting” in the left menu
* Select “SIP Call Flow Tool” on the top bar
* Specify your search criteria and press “Search CDRs” button
* From the list of listed calls select a one with “Call Data Debugging” button

<img alt="Debugging SIP Call Flow Tool in the Mission Control Portal" />

Now you can review SIP call flow with all detailed data for each of the SIP request

<img alt="Call Data Debugging" />

<img alt="Debugging Message" />

You can also check “Session Info” on the next tab or export PCAP data on the “Export” tab.

<img alt="Call Data Debugging - Session Info" />

#

## References

* 1. Telnyx SIP trunk configuration data - [https://sip.telnyx.com](https://sip.telnyx.com)
* 2. Telnyx SIP trunk setup - [https://support.telnyx.com/en/articles/8096455-how-to-configure-a-sip-trunk](https://support.telnyx.com/en/articles/8096455-how-to-configure-a-sip-trunk)
* 3. LiveKit SIP configuration - [https://docs.livekit.io/sip/](https://docs.livekit.io/sip/)


## Related Pages

- [SIP Trunking Configuration Guides](../runbooks/sip-trunking-configuration-guides.md)
