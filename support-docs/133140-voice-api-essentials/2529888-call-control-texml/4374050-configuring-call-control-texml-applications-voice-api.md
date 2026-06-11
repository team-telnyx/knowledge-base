---
source_url: https://support.telnyx.com/en/articles/4374050-configuring-call-control-texml-applications-voice-api
scraped: 2026-06-11
---

Configuring Call Control/TeXML Applications - Voice API | Telnyx Help Center

[Skip to main content](#main-content)

# Configuring Call Control/TeXML Applications - Voice API

This article describes the in-depth setup of Call Control / TeXML Applications on our Mission Control Portal.

Written by David

Updated over a month ago

Table of contents

# Configuration of Call Control/TeXML Voice Apps

The [Call Control / TeXML](https://portal.telnyx.com/#/app/next/call-control/applications) applications section is located on the left hand side of the portal under Voice > Programmable Voice.

Click on this button below and it will directly get you to the Voice Applications page.

[Call Control / TeXML Applications](https://portal.telnyx.com/#/app/next/call-control/applications)

---

## Voice Applications (Call Control Voice API Application)

[![](https://downloads.intercomcdn.com/i/o/ltcafuzd/2383361567/e8f1e8fcc27abad5e0e362da88be/image.png?expires=1781168400&signature=b3fa8e4c0136fe6347d8ccab99e564df348dadc31a52fef7643e7d2755c59905&req=diMvFcp4nIRZXvMW1HO4zRC74tNWaPxVNZSlryovt09KilYUL9zKv24cT%2BRd%0AWHRqoWb3lr3X1eXYb%2Bg%3D%0A)](https://downloads.intercomcdn.com/i/o/ltcafuzd/2383361567/e8f1e8fcc27abad5e0e362da88be/image.png?expires=1781168400&signature=b3fa8e4c0136fe6347d8ccab99e564df348dadc31a52fef7643e7d2755c59905&req=diMvFcp4nIRZXvMW1HO4zRC74tNWaPxVNZSlryovt09KilYUL9zKv24cT%2BRd%0AWHRqoWb3lr3X1eXYb%2Bg%3D%0A)

## Voice App Name

Click on " Create Voice App" and assign a name to this application to better manage the application.

**AnchorSite® Selection**

"Latency" directs Telnyx to route media through the site with the lowest round-trip time to the user's connection. Telnyx calculates this time using ICMP ping messages. This can be disabled by specifying a site to handle all media.

[![](https://downloads.intercomcdn.com/i/o/ltcafuzd/1312501393/0ebd7fa2ef41987fa00a2af6bfcf/image.png?expires=1781168400&signature=5fa4b3402147de078356266758fe7b13926a50614dfa114e70eb84bbe5a75e0c&req=dSMmFMx%2BnIJWWvMW1HO4zRcceddfHYoeqJokzpkFabqw1pV9J%2BifX0LBj34U%0AbRK%2BpVqd6dKGzCboj2s%3D%0A)](https://downloads.intercomcdn.com/i/o/ltcafuzd/1312501393/0ebd7fa2ef41987fa00a2af6bfcf/image.png?expires=1781168400&signature=5fa4b3402147de078356266758fe7b13926a50614dfa114e70eb84bbe5a75e0c&req=dSMmFMx%2BnIJWWvMW1HO4zRcceddfHYoeqJokzpkFabqw1pV9J%2BifX0LBj34U%0AbRK%2BpVqd6dKGzCboj2s%3D%0A)

[![](https://downloads.intercomcdn.com/i/o/ltcafuzd/1312499435/8d959b82778bb0a45aadd68b5e7a/image.png?expires=1781168400&signature=a702eb99d5cb2418102a9987320cd9ec9c1477e96e351b4fc31b1bd6aa84c76c&req=dSMmFM13lIVcXPMW1HO4zW5YQnLbB1fGzos%2BoRR1ED8Y8Nc6wvOLqtUhyOIf%0Ap031uzCJm7fWcIPGG1Q%3D%0A)](https://downloads.intercomcdn.com/i/o/ltcafuzd/1312499435/8d959b82778bb0a45aadd68b5e7a/image.png?expires=1781168400&signature=a702eb99d5cb2418102a9987320cd9ec9c1477e96e351b4fc31b1bd6aa84c76c&req=dSMmFM13lIVcXPMW1HO4zW5YQnLbB1fGzos%2BoRR1ED8Y8Nc6wvOLqtUhyOIf%0Ap031uzCJm7fWcIPGG1Q%3D%0A)

### Send a webhook to the URL

You will need to input a URL where all the [webhook](https://support.telnyx.com/en/articles/4334722-how-to-leverage-webhooks) events will be sent. Also, you can setup a fail-over URL. If two consecutive delivery attempts to the primary URL fail, Telnyx will attempt delivery to this URL. **NOTE**: Must include a scheme such as 'https'.

[![](https://downloads.intercomcdn.com/i/o/ltcafuzd/1312500377/9a9c0993cf3b5dcfffde3a530325/image.png?expires=1781168400&signature=44b9180cf67f49f0e28c31899f6d034f0da6110ae316628cba4d5863166b8f5d&req=dSMmFMx%2BnYJYXvMW1HO4zUvX1lILbCcewlUhCwJ4AT8gTLMYQpuawi8PzH4I%0AvSpCZx9Qnqlhguk8Kgc%3D%0A)](https://downloads.intercomcdn.com/i/o/ltcafuzd/1312500377/9a9c0993cf3b5dcfffde3a530325/image.png?expires=1781168400&signature=44b9180cf67f49f0e28c31899f6d034f0da6110ae316628cba4d5863166b8f5d&req=dSMmFMx%2BnYJYXvMW1HO4zUvX1lILbCcewlUhCwJ4AT8gTLMYQpuawi8PzH4I%0AvSpCZx9Qnqlhguk8Kgc%3D%0A)

### Use Webhook API version

Determines which webhook format will be used based on the API version V1 or V2.

We recommend using API V2, as it contains a richer feature set versus the initial version which will be deprecated in the future.

[![](https://downloads.intercomcdn.com/i/o/ltcafuzd/1312500441/e819eaf9bd31212c35932e8ec22e/image.png?expires=1781168400&signature=857384a42443e1e35d419ac3b9e297c3af7edfde073d73c67075df34e527cda2&req=dSMmFMx%2BnYVbWPMW1HO4zRdyQac310KTkfMGl7YO%2B4GMV60gy6jJ0EL1nc7z%0AiExQ384IrFbaIyhOilw%3D%0A)](https://downloads.intercomcdn.com/i/o/ltcafuzd/1312500441/e819eaf9bd31212c35932e8ec22e/image.png?expires=1781168400&signature=857384a42443e1e35d419ac3b9e297c3af7edfde073d73c67075df34e527cda2&req=dSMmFMx%2BnYVbWPMW1HO4zRdyQac310KTkfMGl7YO%2B4GMV60gy6jJ0EL1nc7z%0AiExQ384IrFbaIyhOilw%3D%0A)

### Enable "hang-up" on timeout

When enabled, you will specify the number of seconds Telnyx will wait for commands from your application before hanging up.

[![](https://downloads.intercomcdn.com/i/o/ltcafuzd/1312500671/3e518a4d7007723167e7997dc397/image.png?expires=1781168400&signature=f0e17341e297e440b25ae69628961c7c35e13b4a33dbcb5f9ebc29fc855a423f&req=dSMmFMx%2BnYdYWPMW1HO4zatHsERDcTa%2FGDbLpbCTrF1fHrYyb83Gn8ffnNDQ%0A%2F3dO6PkW3pvHVoTvXE8%3D%0A)](https://downloads.intercomcdn.com/i/o/ltcafuzd/1312500671/3e518a4d7007723167e7997dc397/image.png?expires=1781168400&signature=f0e17341e297e440b25ae69628961c7c35e13b4a33dbcb5f9ebc29fc855a423f&req=dSMmFMx%2BnYdYWPMW1HO4zatHsERDcTa%2FGDbLpbCTrF1fHrYyb83Gn8ffnNDQ%0A%2F3dO6PkW3pvHVoTvXE8%3D%0A)

### Custom webhook retry delay (seconds)

In this field, you will need to specify a delay in seconds for Telnyx to wait before retrying an unsuccessful webhook delivery attempt. If not set, Telnyx will retry immediately.

[![](https://downloads.intercomcdn.com/i/o/ltcafuzd/1312500887/9b1236a5120943c01fd87213362f/image.png?expires=1781168400&signature=0d5ad24a862105ba21d1c47d51f15f96687f092a2b425e7b2cb5fab45a113f30&req=dSMmFMx%2BnYlXXvMW1HO4zTlk1N2jye4t7VUz1gPnkU1eshGJPe%2Bq1lgd8HBp%0A6aPgvCDSpj8PKER4c7A%3D%0A)](https://downloads.intercomcdn.com/i/o/ltcafuzd/1312500887/9b1236a5120943c01fd87213362f/image.png?expires=1781168400&signature=0d5ad24a862105ba21d1c47d51f15f96687f092a2b425e7b2cb5fab45a113f30&req=dSMmFMx%2BnYlXXvMW1HO4zTlk1N2jye4t7VUz1gPnkU1eshGJPe%2Bq1lgd8HBp%0A6aPgvCDSpj8PKER4c7A%3D%0A)

### DTMF Type

There are three types in this field: RFC 2833, Inband and SIP INFO.

1. **RFC 2833**: Default and preferred setting for most use cases, not audible on the call audio.
2. **Inband**: Digits are passed along just like the rest of your voice as normal audio tones.
3. **SIP INFO**: Mainly used for SIP to SIP calls. [DTMF](https://support.telnyx.com/en/articles/1130710-what-is-dtmf) type is negotiated between parties on the call.

[![](https://downloads.intercomcdn.com/i/o/ltcafuzd/1312501823/c5babf45861a029aef4bcb3adbd7/image.png?expires=1781168400&signature=500e92cd1b8be6363ec938ed9c1e39b50afbffce2c68a75c4a89a598953a95b3&req=dSMmFMx%2BnIldWvMW1HO4zcDHiJgIOx%2FPW3cjXu7HiDm2MTPZEZPQBcDebxAP%0AfSatrMOBhCZ%2B%2BHZwfLQ%3D%0A)](https://downloads.intercomcdn.com/i/o/ltcafuzd/1312501823/c5babf45861a029aef4bcb3adbd7/image.png?expires=1781168400&signature=500e92cd1b8be6363ec938ed9c1e39b50afbffce2c68a75c4a89a598953a95b3&req=dSMmFMx%2BnIldWvMW1HO4zcDHiJgIOx%2FPW3cjXu7HiDm2MTPZEZPQBcDebxAP%0AfSatrMOBhCZ%2B%2BHZwfLQ%3D%0A)

### RTCP Capture

Enable capture of RTCP reports to build QoS Reports (found under Debugging > SIP Call Flow Tool). By default it's not enabled, clicked the "yes" radio button to enable it.

### Call Cost Webhook Event

Specify if the call cost webhook should be sent. By default it's not enabled, clicked the "yes" radio button to enable it.   
​

[![](https://downloads.intercomcdn.com/i/o/ltcafuzd/1312502117/e6491d31ff5224a7fdda1468f7cc/image.png?expires=1781168400&signature=211f8daa0cb7dfa639dbb14173dbfbc323cef3c7f915c1cc36af1698b8956084&req=dSMmFMx%2Bn4BeXvMW1HO4zZ851RsLGhjG9eMtxeyzHU%2BfUk1Xp%2B1INZ7pZTTV%0A3VuWPaf3eHrF77MADl0%3D%0A)](https://downloads.intercomcdn.com/i/o/ltcafuzd/1312502117/e6491d31ff5224a7fdda1468f7cc/image.png?expires=1781168400&signature=211f8daa0cb7dfa639dbb14173dbfbc323cef3c7f915c1cc36af1698b8956084&req=dSMmFMx%2Bn4BeXvMW1HO4zZ851RsLGhjG9eMtxeyzHU%2BfUk1Xp%2B1INZ7pZTTV%0A3VuWPaf3eHrF77MADl0%3D%0A)

---

## Inbound Settings

You can configure your global application settings for inbound calls over here.

[![](https://downloads.intercomcdn.com/i/o/ltcafuzd/1312502794/f0b85947dbcd51eb6819a02e93ac/image.png?expires=1781168400&signature=164f1bf5ad66f3eb05ebd3a458d58cabca5aac4fecefafc4e16de05e16698187&req=dSMmFMx%2Bn4ZWXfMW1HO4zaomr%2Fi2eGMFUJGYnNWLhxHL5rAjBfwP17wKzfM%2F%0AOnM4%2BKp15gk4NTHjb5A%3D%0A)](https://downloads.intercomcdn.com/i/o/ltcafuzd/1312502794/f0b85947dbcd51eb6819a02e93ac/image.png?expires=1781168400&signature=164f1bf5ad66f3eb05ebd3a458d58cabca5aac4fecefafc4e16de05e16698187&req=dSMmFMx%2Bn4ZWXfMW1HO4zaomr%2Fi2eGMFUJGYnNWLhxHL5rAjBfwP17wKzfM%2F%0AOnM4%2BKp15gk4NTHjb5A%3D%0A)

### Subdomain

Specify a **subdomain** that can be used to receive calls to a Connection, in the same way a phone number is used, from a SIP endpoint.

* Example: the subdomain "**example**.sip.telnyx.com" can be called from any SIP endpoint by using the SIP URI "sip:@**example**.sip.telnyx.com" where the user part can be any alphanumeric value.
* You only need to specify the subdomain in this field, there is no need to specify a Telnyx domain after it.
* **SIP subdomain receive settings**: In this field, either you setup your receive SIP subdomain connection from anyone or only connections.

### Inbound Channel Limit

You can limit the total number of inbound calls to phone numbers associated with this connection.

### Enable Shaken Stir headers

By default, the radio button for no is checked. Select yes and save your settings if you want receive attestation information in the webhooks for incoming calls.

### Codecs

Select the codes using the check mark boxes that you would like Telnyx to offer on your calls. You can force specific codecs by only checking one of the boxes.

---

## Outbound settings

You can configure your global application settings for outbound calls over here.

[![](https://downloads.intercomcdn.com/i/o/ltcafuzd/1312503228/43ec98de27196e6ff63280df6087/image.png?expires=1781168400&signature=cc22fc209dd3a36656b3b6ccaa28bf055a9c21fdd666255f67c7fea0d9e1fdb3&req=dSMmFMx%2BnoNdUfMW1HO4zXKjYg7z9KZu52BN8TL2XHDxFTL0Zqkx9ri81IiY%0A81dWg8Wr2n%2Fn%2Bva%2FGxQ%3D%0A)](https://downloads.intercomcdn.com/i/o/ltcafuzd/1312503228/43ec98de27196e6ff63280df6087/image.png?expires=1781168400&signature=cc22fc209dd3a36656b3b6ccaa28bf055a9c21fdd666255f67c7fea0d9e1fdb3&req=dSMmFMx%2BnoNdUfMW1HO4zXKjYg7z9KZu52BN8TL2XHDxFTL0Zqkx9ri81IiY%0A81dWg8Wr2n%2Fn%2Bva%2FGxQ%3D%0A)

### Outbound Voice Profile

Assign your application to an outbound voice profile in order to make outbound calls.

### Outbound Channel Limit

You can limit the total number of outbound calls to phone numbers associated with this connection.

---

## Where can I find my Call Control application or app id?

Once you've successfully created your Call Control application, it is given an application id that can be seen within the application settings as seen in the below picture.

## AnchorSite® Selection

"Latency" directs Telnyx to route media through the site with the lowest round-trip time to the user's connection. Telnyx calculates this time using ICMP ping messages. This can be disabled by specifying a site to handle all media.

[![](https://downloads.intercomcdn.com/i/o/ltcafuzd/1312504666/3da3fb0abacfea513080908d4841/image.png?expires=1781168400&signature=859e3565cfe778e691963c5b23ea4ce37d93a537607b37d221f1cb59ae029c62&req=dSMmFMx%2BmYdZX%2FMW1HO4zcOzpuIjpBUqR98pGXzF%2FWhSWyfVCLJ%2BF45a1%2Fey%0Adyj7JD6vHQh30v9wMkI%3D%0A)](https://downloads.intercomcdn.com/i/o/ltcafuzd/1312504666/3da3fb0abacfea513080908d4841/image.png?expires=1781168400&signature=859e3565cfe778e691963c5b23ea4ce37d93a537607b37d221f1cb59ae029c62&req=dSMmFMx%2BmYdZX%2FMW1HO4zcOzpuIjpBUqR98pGXzF%2FWhSWyfVCLJ%2BF45a1%2Fey%0Adyj7JD6vHQh30v9wMkI%3D%0A)

## Why do I need an Call Control application or app id?

The application id is used to reference or trigger your API calls programmatically. Don't forget to reference our [developer documentation](https://developers.telnyx.com/api-reference/call-commands/dial) to see how you can control your calls with the different API commands available.

---

## TeXML Applications

[![](https://downloads.intercomcdn.com/i/o/ltcafuzd/2383370401/b9f6c3a58b43cd61024c3158afbb/image.png?expires=1781168400&signature=95d75e1114f586ceed939802995f9caef01122d6bd34d199f8fc71353219b616&req=diMvFcp5nYVfWPMW1HO4zTU0DUpCZGl9I%2BXuUdVpvEkR25UHi6qEKlagbIXN%0AiiBEz%2BgJgmFZ4xywRu4%3D%0A)](https://downloads.intercomcdn.com/i/o/ltcafuzd/2383370401/b9f6c3a58b43cd61024c3158afbb/image.png?expires=1781168400&signature=95d75e1114f586ceed939802995f9caef01122d6bd34d199f8fc71353219b616&req=diMvFcp5nYVfWPMW1HO4zTU0DUpCZGl9I%2BXuUdVpvEkR25UHi6qEKlagbIXN%0AiiBEz%2BgJgmFZ4xywRu4%3D%0A)

## TeXML App Name

Click on " Create TeXML App" and assign a name to this application to better manage the application.  
​

[![](https://downloads.intercomcdn.com/i/o/ltcafuzd/1312508948/f66eefadd7bdd854f872e92efe59/image.png?expires=1781168400&signature=3bb74a5da52d743787adf78df009c1534ed629275b20d5575468e5c93f7f29a7&req=dSMmFMx%2BlYhbUfMW1HO4zbqy%2BJe3%2FQJBOH9AEEzBtNvOIBQKpv22RETbcZtI%0AYizWKXldHmOT8eqWP4k%3D%0A)](https://downloads.intercomcdn.com/i/o/ltcafuzd/1312508948/f66eefadd7bdd854f872e92efe59/image.png?expires=1781168400&signature=3bb74a5da52d743787adf78df009c1534ed629275b20d5575468e5c93f7f29a7&req=dSMmFMx%2BlYhbUfMW1HO4zbqy%2BJe3%2FQJBOH9AEEzBtNvOIBQKpv22RETbcZtI%0AYizWKXldHmOT8eqWP4k%3D%0A)

### Voice Method

In this field, HTTP request method Telnyx will use to interact with your XML Translator webhooks. Either "GET" or "POST".

[![](https://downloads.intercomcdn.com/i/o/ltcafuzd/1312507003/3e521ba1547c22f148e247ece3a5/image.png?expires=1781168400&signature=6b9575f2da4abfaaa1c78dc62da3f5aefd49771e1246f4b739213c190bf45fa5&req=dSMmFMx%2BmoFfWvMW1HO4zTXDc5EOv3K%2FB96ydQ1OMOrbP3kYlCDfYZLbR0Gl%0AN4Im74bs8zR2J9FwBnU%3D%0A)](https://downloads.intercomcdn.com/i/o/ltcafuzd/1312507003/3e521ba1547c22f148e247ece3a5/image.png?expires=1781168400&signature=6b9575f2da4abfaaa1c78dc62da3f5aefd49771e1246f4b739213c190bf45fa5&req=dSMmFMx%2BmoFfWvMW1HO4zTXDc5EOv3K%2FB96ydQ1OMOrbP3kYlCDfYZLbR0Gl%0AN4Im74bs8zR2J9FwBnU%3D%0A)

### Send a TeXML webhook to the URL

You will need to mention a URL where all the XML translator webhook events will be sent. Also, you can setup a fail-over URL. This URL to which Telnyx will deliver your XML Translator webhooks if we get an error response from your "Voice URL"

[![](https://downloads.intercomcdn.com/i/o/ltcafuzd/1312508092/cfc69a585c0cab95af6f4d2c46a5/image.png?expires=1781168400&signature=8484075c92418cdb14d5553d443720be900bc74feb072682230ce58b417607e6&req=dSMmFMx%2BlYFWW%2FMW1HO4zRu%2Bn7xHuFsz7llnJXxQ46bCNcf9lB3g9TWVoc3a%0AlVZb687tiDv7oFNAEck%3D%0A)](https://downloads.intercomcdn.com/i/o/ltcafuzd/1312508092/cfc69a585c0cab95af6f4d2c46a5/image.png?expires=1781168400&signature=8484075c92418cdb14d5553d443720be900bc74feb072682230ce58b417607e6&req=dSMmFMx%2BlYFWW%2FMW1HO4zRu%2Bn7xHuFsz7llnJXxQ46bCNcf9lB3g9TWVoc3a%0AlVZb687tiDv7oFNAEck%3D%0A)

### Status Callback Method

You will need to mention the HTTP request method Telnyx should use when requesting the "Status Callback" URL.

[![](https://downloads.intercomcdn.com/i/o/ltcafuzd/1312508282/e4e13dff5aad3c9075b93fc5d36f/image.png?expires=1781168400&signature=2441be19cd1b96097f92d3c9c5df74815f93c5d6e1a322e62557d6b039d20746&req=dSMmFMx%2BlYNXW%2FMW1HO4ze9qxtkd8F%2BIUE2yKrM%2BUPZvcDqGepJCRoHr879e%0AKc55hCEE2NzexwV7Gw4%3D%0A)](https://downloads.intercomcdn.com/i/o/ltcafuzd/1312508282/e4e13dff5aad3c9075b93fc5d36f/image.png?expires=1781168400&signature=2441be19cd1b96097f92d3c9c5df74815f93c5d6e1a322e62557d6b039d20746&req=dSMmFMx%2BlYNXW%2FMW1HO4ze9qxtkd8F%2BIUE2yKrM%2BUPZvcDqGepJCRoHr879e%0AKc55hCEE2NzexwV7Gw4%3D%0A)

### Send information about call progress events to the URL

Specify the URL for Telnyx to send requests to containing information about call progress events.

[![](https://downloads.intercomcdn.com/i/o/ltcafuzd/1312508602/53ef95e5808f7ea93906c5b24817/image.png?expires=1781168400&signature=82a5ee3c73325f23ebb5bb171a4ad47926677bf13bb963d9784d57b43e9534dc&req=dSMmFMx%2BlYdfW%2FMW1HO4zeaSyd6%2FnolO%2FZc4sPx3n5DLFsSUyGTF3TZMAikz%0AuswaQXrryIN5pra%2Bhrg%3D%0A)](https://downloads.intercomcdn.com/i/o/ltcafuzd/1312508602/53ef95e5808f7ea93906c5b24817/image.png?expires=1781168400&signature=82a5ee3c73325f23ebb5bb171a4ad47926677bf13bb963d9784d57b43e9534dc&req=dSMmFMx%2BlYdfW%2FMW1HO4zeaSyd6%2FnolO%2FZc4sPx3n5DLFsSUyGTF3TZMAikz%0AuswaQXrryIN5pra%2Bhrg%3D%0A)

### Enable "hang-up" on timeout

When enabled, you will specify the numbers of seconds to wait for actual application before hanging up.

[![](https://downloads.intercomcdn.com/i/o/ltcafuzd/1312508764/fc572d643e7c8c15c6e775826004/image.png?expires=1781168400&signature=ef6ecc70491a01688c1295da1385bccf4be74f31503f2374d444847ec5fde751&req=dSMmFMx%2BlYZZXfMW1HO4zYJvOQjZkdbkSU2k8W1JiWqQRm%2B8tjoC8BV7R54A%0AKuG9JjA0nW70HQdcxwM%3D%0A)](https://downloads.intercomcdn.com/i/o/ltcafuzd/1312508764/fc572d643e7c8c15c6e775826004/image.png?expires=1781168400&signature=ef6ecc70491a01688c1295da1385bccf4be74f31503f2374d444847ec5fde751&req=dSMmFMx%2BlYZZXfMW1HO4zYJvOQjZkdbkSU2k8W1JiWqQRm%2B8tjoC8BV7R54A%0AKuG9JjA0nW70HQdcxwM%3D%0A)

**DTMF Type**

There are three types in this field: RFC 2833, Inband and SIP INFO.

1. **RFC 2833**: Default and preferred setting for most use cases, not audible on the call audio.
2. **Inband**: Digits are passed along just like the rest of your voice as normal audio tones.
3. **SIP INFO**: Mainly used for SIP to SIP calls. [DTMF](https://support.telnyx.com/en/articles/1130710-what-is-dtmf) type is negotiated between parties on the call.

[![](https://downloads.intercomcdn.com/i/o/ltcafuzd/1312509388/e6eda186137cd769d956c397105e/image.png?expires=1781168400&signature=95232623f25b3d312f9fb83686a719c823759ce69ec2a8068f119856bab63b91&req=dSMmFMx%2BlIJXUfMW1HO4zXkscuW0ioVr7aI7COpbrESwCVkY0%2FAxGvvSTbiE%0ACrkSREVNnx6eF6tY1N8%3D%0A)](https://downloads.intercomcdn.com/i/o/ltcafuzd/1312509388/e6eda186137cd769d956c397105e/image.png?expires=1781168400&signature=95232623f25b3d312f9fb83686a719c823759ce69ec2a8068f119856bab63b91&req=dSMmFMx%2BlIJXUfMW1HO4zXkscuW0ioVr7aI7COpbrESwCVkY0%2FAxGvvSTbiE%0ACrkSREVNnx6eF6tY1N8%3D%0A)

### Call Cost Webhook Event

Specify if the call cost webhook should be sent. By default it's not enabled, clicked the "yes" radio button to enable it.   
​

[![](https://downloads.intercomcdn.com/i/o/ltcafuzd/1312510066/4c17a31800ad7b288e5b5eff7fc8/image.png?expires=1781168400&signature=e5708b48a26b5aa535691d62cae4bb7f19553c53896289dc439e13a79486d878&req=dSMmFMx%2FnYFZX%2FMW1HO4zVgeBw7IugJLJ1PkZRiYguvhLlCQuiQQsASbteMd%0AqmxrkqUPSs%2FCZxe2jX8%3D%0A)](https://downloads.intercomcdn.com/i/o/ltcafuzd/1312510066/4c17a31800ad7b288e5b5eff7fc8/image.png?expires=1781168400&signature=e5708b48a26b5aa535691d62cae4bb7f19553c53896289dc439e13a79486d878&req=dSMmFMx%2FnYFZX%2FMW1HO4zVgeBw7IugJLJ1PkZRiYguvhLlCQuiQQsASbteMd%0AqmxrkqUPSs%2FCZxe2jX8%3D%0A)

---

## Inbound Settings

You can configure your global application settings for inbound calls over here.

[![](https://downloads.intercomcdn.com/i/o/ltcafuzd/1312510596/32f36676ec4c9868b869566f2fbb/image.png?expires=1781168400&signature=6aada07862b8110eb34412a13fd9aca9d0e5a10da2c4aa6b0f0bd5e12e6a9cec&req=dSMmFMx%2FnYRWX%2FMW1HO4zcInz98iZTQivUelr0qQsdU9CdunBogZYXq1qc1T%0Adg7xAbb9eE7LVj2az94%3D%0A)](https://downloads.intercomcdn.com/i/o/ltcafuzd/1312510596/32f36676ec4c9868b869566f2fbb/image.png?expires=1781168400&signature=6aada07862b8110eb34412a13fd9aca9d0e5a10da2c4aa6b0f0bd5e12e6a9cec&req=dSMmFMx%2FnYRWX%2FMW1HO4zcInz98iZTQivUelr0qQsdU9CdunBogZYXq1qc1T%0Adg7xAbb9eE7LVj2az94%3D%0A)

### Subdomain

Specify a **subdomain** that can be used to receive calls to a Connection, in the same way a phone number is used, from a SIP endpoint.

* Example: the subdomain "**example**.sip.telnyx.com" can be called from any SIP endpoint by using the SIP URI "sip:@**example**.sip.telnyx.com" where the user part can be any alphanumeric value.
* You only need to specify the subdomain in this field, there is no need to specify a Telnyx domain after it.
* **SIP subdomain receive settings**: In this field, either you setup your receive SIP subdomain connection from anyone or only connections.

### Inbound Channel Limit

You can limit the total number of inbound calls to phone numbers associated with this connection.

### Enable Shaken Stir headers

By default, the radio button for no is checked. Select yes and save your settings if you want receive attestation information in the webhooks for incoming calls.

## Codecs

Select the codes using the check mark boxes that you would like Telnyx to offer on your calls. You can force specific codecs by only checking one of the boxes.

---

## Outbound settings

You can configure your global application settings for outbound calls over here.

[![Outbound settings page.](https://downloads.intercomcdn.com/i/o/840876618/b1a2158cb48f17003134fe4e/Screenshot+from+2023-09-28+10-27-30.png?expires=1781168400&signature=9d11da346c6998fbf0b162487c3905624dddc50137e2a69ed257781eac7c7554&req=fCQnHs54m4BXFb4f3HP0gF7U4tiiblso5Y%2BcVFyGeAHkMcPC4TJLtiHxkSbn%0AKdpiKnfxniQ9MzLRvA%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/840876618/b1a2158cb48f17003134fe4e/Screenshot+from+2023-09-28+10-27-30.png?expires=1781168400&signature=9d11da346c6998fbf0b162487c3905624dddc50137e2a69ed257781eac7c7554&req=fCQnHs54m4BXFb4f3HP0gF7U4tiiblso5Y%2BcVFyGeAHkMcPC4TJLtiHxkSbn%0AKdpiKnfxniQ9MzLRvA%3D%3D%0A)

### Outbound Voice Profile

Assign your application to an outbound voice profile in order to make outbound calls.

### Outbound Channel Limit

You can limit the total number of outbound calls to phone numbers associated with this connection.

[![](https://downloads.intercomcdn.com/i/o/ltcafuzd/1312510781/9bf7f581f08db6f99034518f6e4e/image.png?expires=1781168400&signature=d339602e9fd474a8958a68d46afdd28de5ec404fedfa9dba522413a107d395cb&req=dSMmFMx%2FnYZXWPMW1HO4zee%2F86wDq1TC8Qpas%2BM6UJUqcx3RLmtdaDnn8m%2BY%0AtaWNTSxkANfF%2FywlWmE%3D%0A)](https://downloads.intercomcdn.com/i/o/ltcafuzd/1312510781/9bf7f581f08db6f99034518f6e4e/image.png?expires=1781168400&signature=d339602e9fd474a8958a68d46afdd28de5ec404fedfa9dba522413a107d395cb&req=dSMmFMx%2FnYZXWPMW1HO4zee%2F86wDq1TC8Qpas%2BM6UJUqcx3RLmtdaDnn8m%2BY%0AtaWNTSxkANfF%2FywlWmE%3D%0A)

---

## Where can I find my TeXML application or app ID?

Once you've successfully created your TeXML application, it is given an application id that can be seen within the application settings as seen in the below picture.

[![](https://downloads.intercomcdn.com/i/o/ltcafuzd/1312511508/c7515bdb829c802aa76b919f6ae8/image.png?expires=1781168400&signature=8db98714997a038721bf0c770b78fe3378ec23fbf4f077d35ae056a3d302eb6c&req=dSMmFMx%2FnIRfUfMW1HO4ze1ZtX5uNzWebcFLGjwqpzhb6XnRqf9WfdSn1y3c%0AFWsa95L3%2Bsrjzy45e0Q%3D%0A)](https://downloads.intercomcdn.com/i/o/ltcafuzd/1312511508/c7515bdb829c802aa76b919f6ae8/image.png?expires=1781168400&signature=8db98714997a038721bf0c770b78fe3378ec23fbf4f077d35ae056a3d302eb6c&req=dSMmFMx%2FnIRfUfMW1HO4ze1ZtX5uNzWebcFLGjwqpzhb6XnRqf9WfdSn1y3c%0AFWsa95L3%2Bsrjzy45e0Q%3D%0A)

## Why do I need an TeXML application or app ID?

The application id is used to reference or trigger your API calls programmatically. Don't forget to reference our [developer documentation](https://developers.telnyx.com/docs/development/programmable-voice/texml-setup) to see how you can setup your XML instructions.

[![Breaking Line](https://downloads.intercomcdn.com/i/o/226483939/ed2cce9ed61fd46892a4a082/line.png?expires=1781168400&signature=cf4ff574480a4910c10f9dbc15623b32ab383e262e65c79dff7166141bc4a86b&req=diIhEsF9lIJWFb4f3HP0gLK9YgWB0hmnv1b6t%2BUbITS%2FJqOzeJ%2BGW47VUXMj%0ATzhhI2kdGNG%2B32RirQ%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/226483939/ed2cce9ed61fd46892a4a082/line.png?expires=1781168400&signature=cf4ff574480a4910c10f9dbc15623b32ab383e262e65c79dff7166141bc4a86b&req=diIhEsF9lIJWFb4f3HP0gLK9YgWB0hmnv1b6t%2BUbITS%2FJqOzeJ%2BGW47VUXMj%0ATzhhI2kdGNG%2B32RirQ%3D%3D%0A)

---

Related Articles

[Call Forwarding](https://support.telnyx.com/en/articles/1130657-call-forwarding)[What is DTMF? and how to configure it on Telnyx](https://support.telnyx.com/en/articles/1130710-what-is-dtmf-and-how-to-configure-it-on-telnyx)[Telnyx Debugging Tools](https://support.telnyx.com/en/articles/4304872-telnyx-debugging-tools)[SIP Connection: Settings](https://support.telnyx.com/en/articles/4351104-sip-connection-settings)[TeXML and Telnyx Voice API compatibility](https://support.telnyx.com/en/articles/8118086-texml-and-telnyx-voice-api-compatibility)

Did this answer your question?

😞😐😃

Table of contents
