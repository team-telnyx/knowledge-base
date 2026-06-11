---
source_url: https://support.telnyx.com/en/articles/7029684-telephony-credentials-types
scraped: 2026-06-11
---

Telephony Credentials: Types | Telnyx Help Center

[Skip to main content](#main-content)

# Telephony Credentials: Types

This article explains and describes how to setup and use SIP Connection Credentials, On-Demand Credentials and JSON Web Tokens.

Written by David

April 29, 2026

Table of contents

# Telephony Credentials: Types

We offer three different Telephony Credential types to authenticate your calls.

This article will show you how to configure each type of credential and explain their differences and the scenarios where each may be most appropriate for your business.

## SIP Connection Credential Authentication

#### 1. Click Voice -> SIP Trunking in the Mission Control Portal and select Create SIP Connection.

#### 2. Enter the name you want to give your SIP Connection and Select Credentials as the authentication type.

#### 3. Edit Username and Password

A username and password will automatically be generated, but you should consider changing them.

Follow [this article](https://support.telnyx.com/en/articles/4245868-sip-connection-types) to know how to create the SIP Connection

It is **highly recommended** that you choose a **strong password**.

1. **Length**: Passwords should be at least 12-16 characters long. The longer the password, the harder it is to crack.
2. **Complexity**: Include a mix of upper and lower case letters, numbers, and special characters (such as !, @, #, $, etc.).
3. **Avoid Common Words and Patterns**: Do not use easily guessed passwords like "password," "123456," sequences like "abcd" or "1234," or keyboard patterns like "qwerty."
4. **No Personal Information**: Avoid using easily accessible information such as birthdays, names of family members, pets, or favourite bands, as these can often be guessed or found through social engineering.
5. **Uniqueness**: Each account should have a unique password. Reusing passwords across multiple sites increases vulnerability; if one site is compromised, others may be at risk too.
6. **Use of Passphrases**: Consider using a passphrase that is a combination of unrelated words and additional characters, making it both easier to remember and hard to guess.

#### 4. Click Create and you'll now have access to use your new credentials SIP Connection!

### Why use SIP Connection Credentials?

SIP Connection Credentials allow you to get set up with a one-stop authentication service for managing your calls. The intuitive portal setup helps users separate their call traffic and allows for easy integration with soft-phone clients such as [Zoiper](https://support.telnyx.com/en/articles/5717957-zoiper-5-pro-telnyx-setup).

## On-Demand Credentials

On-Demand Credentials are created programmatically via our RESTful API.

#### 1. Gather your API key

* If you have not done so, you will need to generate a V2 key here in the [Keys & Credentials section](https://portal.telnyx.com/#/app/api-keys) under **Account Settings.**
* Ensure API Keys is selected in the horizontal menu bar.
* Click "Create API key".
* Copy the API key and save it somewhere safe.

#### 2. Gather your Connection ID

* This can be found in your SIP Connection's settings.

  [![](https://downloads.intercomcdn.com/i/o/ltcafuzd/2334015004/1bcc6e6c03afcde8e56ec07b21a6/image.png?expires=1781168400&signature=d4a8e1906a4a22110c740903c25802cc0656f60c13d49f7fb90cc57171472225&req=diMkEsl%2FmIFfXfMW1HO4zfKtCCBwW6zSRlfzaHV9NznYPLiNG3MEhNO2biZG%0A4nsY%0A)](https://downloads.intercomcdn.com/i/o/ltcafuzd/2334015004/1bcc6e6c03afcde8e56ec07b21a6/image.png?expires=1781168400&signature=d4a8e1906a4a22110c740903c25802cc0656f60c13d49f7fb90cc57171472225&req=diMkEsl%2FmIFfXfMW1HO4zfKtCCBwW6zSRlfzaHV9NznYPLiNG3MEhNO2biZG%0A4nsY%0A)
* You can also return a list of your SIP Connections programmatically using our RESTful API. More details can be found [here](https://developers.telnyx.com/api/connections/list-connections).

#### 3. POST the API request

* ```
  curl -i -X POST \  
    https://api.telnyx.com/v2/telephony_credentials \  
    -H 'Authorization: Bearer <YOUR_TOKEN_HERE>' \  
    -H 'Content-Type: application/json' \  
    -d '{  
      "connection_id": "1234567890",  
      "name": "My-new-credential"  
    }'
  ```

For more information on setting up On-Demand Credentials, please see our [Developer Docs](https://developers.telnyx.com/development/webrtc/js-sdk/quickstart).

### Why use On-Demand Credentials?

On-Demand Credentials helps you onboard new customers or team members under your SIP connection, allowing you to separate each user with their own security credentials. This solution is perfect for users looking to integrate WebRTC into their own platforms so that your back-end system can create outbound calls to each on demand generated credential.

Upmarket, a comprehensive sales platform, was able to get up and running with Telnyx in half the deployment time they expect.

For more details on this Customer Success Story, and others like it, please click [here](https://telnyx.com/customer-stories/upmarket).

### Are there limitations with on-demand credentials?

Yes, inbound calls directly to on-demand generated credential is not currently supported. The purpose for on demand generated credentials is purely for outbound calls.

The typical use case is a call center service. You have a programmable voice application associated with a number. When a call is received to that number, you see which agents are logged in with the on demand generated credentials and your call center service would use our call control API to dial each of the generated credentials to connect the caller with one of the available agents. These agents are typically using a WebRTC client that they use to log in with the on demand credentials you generated for them. Once they're logged in, you'd want to make sure your WebRTC client can inform your call center backend that the agents are registered so the backend has a list of agents it can dial each time an inbound call is received to the main number.

## JSON Web Tokens

JSON Web Tokens or JWTs can be created programmatically using our RESTful API.

These tokens are temporary and will expire after 24 hours.

To do this, you will first need to generate an On-Demand Credential, please see the setup tutorial above.

### Setup

#### 1. Gather your Credential ID.

* This will have been provided in the API response to your On-Demand Credential creation.
* If you have yet to create an On-Demand Credential please see the setup tutorial above.

#### 2. POST the API request.

* The following steps will assume the use of the API platform Postman, as before, but you can use whichever service you would like!
* In the Postman "Headers", set your "Authorization" to the API v2 secret key and the Key should be preceded with "Bearer".
* The "body" field can be left blank.
* POST to <https://api.telnyx.com/v2/telephony_credentials/<credential_id>/token> making sure to replace <credential\_id> with your generated Credential ID.

#### For more information on setting up JSON Web Tokens, please see our Developer Docs.

#### Note: The response body to your API request will be the JSON Web Token which will expire 24 hours after creation.

### Why use JSON Web Tokens?

JWTs provide much the same functionality as On-Demand Credentials while also providing additional security thanks to its default expiry time. This allows you to provide temporary access to onboarding users or guests while still giving them access to WebRTC and VoIP with Telnyx.

## Authenticate and Place a Test Call

After all that work you may be looking for a quick and easy way to test and verify that everything is working properly with your Telephony Credentials.

Luckily, Telnyx has you covered!

The [Telnyx WebRTC test application](https://webrtc.telnyx.com/) is built using our Javascript WebRTC SDK, to showcase our WebRTC platform and make it easier to test your setup.

If you are testing using your SIP Connection Credentials or On-Demand Credentials, simply set your Authentication to "Credential" and enter your credential information as below:

[![](https://downloads.intercomcdn.com/i/o/ltcafuzd/2334032792/92e4dcc764e2bc3063e3d89272c0/image.png?expires=1781168400&signature=d4cb892389a67b9724f644f7cb9370e16c135f9324f5c30f08680cd3e03494e4&req=diMkEsl9n4ZWW%2FMW1HO4zSByUcpBte03azk9sspbXin9S3Rur1RGewTXsm21%0AVZ4VIh4GPsIyIvomFgM%3D%0A)](https://downloads.intercomcdn.com/i/o/ltcafuzd/2334032792/92e4dcc764e2bc3063e3d89272c0/image.png?expires=1781168400&signature=d4cb892389a67b9724f644f7cb9370e16c135f9324f5c30f08680cd3e03494e4&req=diMkEsl9n4ZWW%2FMW1HO4zSByUcpBte03azk9sspbXin9S3Rur1RGewTXsm21%0AVZ4VIh4GPsIyIvomFgM%3D%0A)

If you are testing using your JSON Web Token, set your Authentication to "Token" and enter your token under "Login Token" as below:

[![](https://downloads.intercomcdn.com/i/o/ltcafuzd/2334034192/0038a25e46ad19765550d3c02136/image.png?expires=1781168400&signature=5c31262875203a97fdd8ff3e57c2cc0f4cd8b2a134930df7ca521bfc78a73a93&req=diMkEsl9mYBWW%2FMW1HO4zWLyHel8ZCSUSeqFxWwpkffKOEBYJMRaIbUhTLbl%0AHNDNJBdyB16SuePTqRU%3D%0A)](https://downloads.intercomcdn.com/i/o/ltcafuzd/2334034192/0038a25e46ad19765550d3c02136/image.png?expires=1781168400&signature=5c31262875203a97fdd8ff3e57c2cc0f4cd8b2a134930df7ca521bfc78a73a93&req=diMkEsl9mYBWW%2FMW1HO4zWLyHel8ZCSUSeqFxWwpkffKOEBYJMRaIbUhTLbl%0AHNDNJBdyB16SuePTqRU%3D%0A)

---

Related Articles

[Configuring a FreePBX V13 Credentials Trunk](https://support.telnyx.com/en/articles/1130648-configuring-a-freepbx-v13-credentials-trunk)[SIP Connection: Number Formats](https://support.telnyx.com/en/articles/1130706-sip-connection-number-formats)[Elastix 5: Credentials Trunk](https://support.telnyx.com/en/articles/3284164-elastix-5-credentials-trunk)[SIP Connection: Types](https://support.telnyx.com/en/articles/4245868-sip-connection-types)[SIP Connection: Settings](https://support.telnyx.com/en/articles/4351104-sip-connection-settings)

Did this answer your question?

😞😐😃

Table of contents
