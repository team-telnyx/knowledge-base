---
source_url: https://support.telnyx.com/en/articles/8712528-dialing-emergency-services
scraped: 2026-06-11
---

Dialing Emergency Services | Telnyx Help Center

[Skip to main content](#main-content)

# Dialing Emergency Services

How to dial emergency services to the different countries we support. Start building on Telnyx today.

Written by David

June 26, 2024

Table of contents

# Telnyx PSTN Replacement: Global Emergency Services Support

Telnyx offers PSTN replacement for several countries, this includes being able to dial to emergency services in each of those countries.

The complete global coverage Telnyx supports can be found here

<https://telnyx.com/global-coverage>

Here you can find the complete list of [Supported Emergency Numbers](https://support.telnyx.com/en/articles/8797623-supported-emergency-numbers) on our platform.

In this article we will touch on the emergency services feature of the countries we support emergency services for.

## How Does Telnyx decide what country to dial Emergency services to?

A sip connection on your account is meant to be able to use several numbers for both inbound and outbound calls. If you have one connection for all your numbers from different countries how does Telnyx decide where to dial to?

This is a particularly important question when dealing to emergency numbers that are shared among different countries like with 911.

---

### **Telnyx will use the caller ID of each call to determine the emergency number to be dialed to.**

So for instance if you dial 911 using a Canadian Caller ID, the call will be sent to Canada. But if you dial 911 using a Mexican Caller ID the call will be sent to Mexico.

This way you can setup a single connection with all your numbers and have whatever localization you want on the connection while still being able to dial into each and every country's emergency services.

It's important to note that the "Localization Settings" in the outbound section of your sip connection settings will not affect dialing into Emergency Services. Localization settings are only used for normal local calling and not for Emergency Services.

---

## What number format should you use to dial Emergency Services?

Emergency service numbers are local numbers that were only planned to be available in each country and not available for international dialing. As such they do not support +E.164 or E.164 international formats.

**You should always dial the local emergency number by itself WITHOUT a + sign or country code.**

We'll return an invalid number error when you try to dial without the proper format.

So for instance, when dialing +1911 or 1911 your calls will fail with an invalid number error. The proper way to send the call is just dialing 911.

You can still use a tech prefix to dial so long as you're not including anything else. So for instance if your connection is setup to use the tech Prefix 1234, then you would dial 1234911.

---

## Make sure you register an Address on the number you'll be using as caller id to dial Emergency Services from.

**It's important to note that in some countries, calling emergency services from a number without a registered Emergency Service Address can result in being fined.**   
​  
​**The fine in the US, for example is $100 per call.**

So make sure you've registered an address for use in Emergency Services on all numbers you're going to use to use to dial Emergency Services from.

Per regulation we will always allow calls to Emergency Services regardless of the fact that they are dialing with or without a caller id that has a registered address. For security reasons you can't disable dialing to Emergency Numbers.

---

Related Articles

[How do I test E911 service?](https://support.telnyx.com/en/articles/1130709-how-do-i-test-e911-service)[Bulk Edit Numbers - Emergency Services](https://support.telnyx.com/en/articles/2819213-bulk-edit-numbers-emergency-services)[Supported Emergency Numbers](https://support.telnyx.com/en/articles/8797623-supported-emergency-numbers)[Emergency Services and IPND in Australia](https://support.telnyx.com/en/articles/9039036-emergency-services-and-ipnd-in-australia)[Twilio TwiML Conference on Telnyx](https://support.telnyx.com/en/articles/13389311-twilio-twiml-conference-on-telnyx)

Did this answer your question?

😞😐😃

Table of contents
