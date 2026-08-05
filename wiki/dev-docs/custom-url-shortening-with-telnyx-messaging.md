---
title: Custom URL Shortening with Telnyx Messaging
summary: Telnyx provides a URL Shortening service that converts links in outbound
  SMS messages into custom-branded short URLs, helping improve brand awareness and
  bypass spam filters that block common URL shorteners. The feature is configured
  per Messaging Profile and supports engagement reporting and click webhooks.
sources:
- url: https://developers.telnyx.com/docs/messaging/messages/url-shortening/index
- url: https://developers.telnyx.com/docs/messaging/messages/zapier-integration
updated_at: 2026-08-05T13:57:18Z
---

# Custom URL Shortening with Telnyx Messaging

Telnyx provides a URL Shortening service that converts links in outbound SMS messages into custom-branded short URLs, helping improve brand awareness and bypass spam filters that block common URL shorteners. The feature is configured per Messaging Profile and supports engagement reporting and click webhooks.

## Overview

Telnyx provides a URL Shortening service with custom links in order to improve brand awareness and bypass spam filters that block most popular URL shortening sites. Any message that contains URLs with the supported domains will be converted into one of Telnyx's custom shortened URLs.

If you are interested in activating this feature, please reach out to the Telnyx Sales Team. After the feature is activated for your account, you can configure it following the steps below.

## How it works

When URL Shortening is turned on, any messages that contain base URLs from the supported URLs will be converted to a URL with a base domain of your choosing. Custom shortened URLs give brand exposure, are more memorable, and boost your audience's trust.

For example, a message payload like:

```
{
  ...
  "text": "Your shift is starting soon: https://bit.ly/78ejf9n"
  ...
}
```

will be delivered as:

```
{
    ...
    "text": "Your shift is starting soon: http://scdlchg.cc/b20",
    ...
}
```

## Supported domains in shortened URLs

By default, if URL Shortening is enabled on the messaging profile, only URLs with the following domains will be converted:

- bit.do
- bit.ly
- carebank.site
- drvline.site
- eatngage.com
- goo.gl
- healthsettle.pw
- ht.ly
- is.gd
- ow.ly
- rebrand.ly
- t.co
- tiny.cc
- tinyurl.com
- x.co

You have the option of expanding URL shortening for all domains by disabling the `Replace Blacklist Only` setting in the URL Shortener settings on your messaging profile.

## Message engagement reports

In addition to custom URL shortening, you can also view how often recipients of your messages have opened the link via the [Message Engagement Report](https://portal.telnyx.com/?_gl=1*1iw3cdz*_ga*MTgyNTcxMzMwNy4xNjQ3MjMyNDY4*_ga_ZPM4K1DLND*MTY3NjU0MTg5OC4xNzEuMS4xNjc2NTQyMzM2LjU5LjAuMA..#/login/sign-in).

1. Select a Start Date and End Date for the time range you wish to report on.
2. Select the Messaging Profiles you wish to report on.
3. Click on **Generate Messaging Report**.
4. (Optionally) You can also download a detailed view of the clicks.

## Receiving link click webhooks

If you want to track user engagement with your custom shortened URL in real time, you have the option of receiving webhooks when a shortened link is clicked. Webhooks can be enabled on a per messaging profile basis and will be sent to the webhooks already configured on the messaging profile.

## Creating a custom shortened URL via Mission Control

Custom URL Shortening is enabled per Messaging Profile. If you send SMS via phone numbers under this profile, and they contain any URLs that are part of the list of supported URLs, then they will be replaced with links that the URL Shortener service generates.

Please reach out to customer support so that they can work internally to create your customer URL shortener. Provide the following information so customer support can process your request:

1. Your customer ID
2. Your custom domains (or let us know if you need us to provide the domains for you)
3. The profile IDs that you need the link shortener assigned to

Any domains that you provide need to be set up with AAA records.

## Configuring URL Shortening via the API

URL Shortening is enabled per Messaging Profile. The examples below enable the URL shortener service with a specific domain and a custom identifying prefix, enable the service for all domains (not just the supported domains listed above), and enable receiving webhooks for link clicks.

### cURL

```
curl -X PATCH \
  --header "Content-Type: application/json" \
  --header "Accept: application/json" \
  --header "Authorization: Bearer YOUR_API_KEY" \
  --data '{"url_shortener_settings":
    {"domain": "arv.fyi",
    "prefix":"custom_prefix",
    "replace_blacklist_only": false,
    "send_webhooks": true}}' \
  "https://api.telnyx.com/v2/messaging_profiles/{YOUR_MESSAGING_PROFILE_ID}"
```

### Python

```
import telnyx
telnyx.api_key = "YOUR_API_KEY"

mp = telnyx.MessagingProfile.retrieve("YOUR_MESSAGING_PROFILE_ID")

# turn on number pool
mp.url_shortener_settings = {
  "domain": "arv.fyi",
  "prefix":"custom_prefix",
  "replace_blacklist_only": False,
  "send_webhooks": True
}
mp.save()
```

### Ruby

```
require "telnyx"
Telnyx.api_key = "YOUR_API_KEY"

mp = Telnyx::MessagingProfile.retrieve("YOUR_MESSAGING_PROFILE_ID")

# turn on number pool

mp.number_pool_settings = {
  domain: "arv.fyi",
  prefix: "custom_prefix",
  replace_blacklist_only: false,
  send_webhooks: true
}

mp.save
```

### Node

```
import Telnyx from 'telnyx';

const telnyx = new Telnyx("YOUR_API_KEY");

const { data : messagingProfile } = await telnyx.messagingProfiles.update(
  'YOUR_MESSAGING_PROFILE_ID',
  {
    "url_shortener_settings": {
      "domain": "arv.fyi",
      "prefix":"custom_prefix",
      "replace_blacklist_only": false,
      "send_webhooks": true
    }
  }
)
```

### PHP

```
\Telnyx\Telnyx::setApiKey('YOUR_API_KEY');

\Telnyx\MessagingProfile::Update("YOUR_MESSAGING_PROFILE_ID", ["url_shortener_settings" => {
  "domain": "arv.fyi",
  "prefix":"custom_prefix",
  "replace_blacklist_only": false,
   "send_webhooks": true
}]);
```

### .NET

```
using System;
using Telnyx.net.Services.VerifyAPI;
private static string TELNYX_API_KEY ="TELNYX_API_KEY";

Telnyx.TelnyxConfiguration.SetApiKey(TELNYX_API_KEY);
VerificationService verifyService = new VerificationService();

string webhookURL = "";
string domain = "";
string prefix = "";

var messagingProfile = new Telnyx.MessagingProfileService()
var stuff = new Telnyx.MessagingProfileUpdate
  {
     UrlShortenerSettings = {
       Domain = doomain,
       Prefix = prefix,
       ReplaceBlackListOnly = true,
       SendWebhooks = false
     }
  };
messagingProfile.Update(webhookURL, stuff);
```

## Related resources

- [Messaging Profiles](messaging-profiles--part-1.md)
- [Send Your First Message](send-your-first-message.md)
- [Webhooks](webhooks.md)
- [Message Detail Records](message-detail-records.md)
- [Rate Limiting](rate-limiting.md)
- [Configurable Spend Limits](configurable-spend-limits.md)
- [Telnyx on Zapier](https://zapier.com/apps/telnyx/integrations)
