---
source_url: https://support.telnyx.com/en/articles/3546251-caller-id-number-policy
scraped: 2026-06-11
---

Caller ID Number Policy | Telnyx Help Center

[Skip to main content](#main-content)

# Caller ID Number Policy

A comprehensive guide to the Caller ID Number Policy for Outbound Calls.

Written by Alex Conroy

April 28, 2026

Table of contents

Caller ID Number *(CID)* is a service that displays your phone number to the phone of the individual you are calling on an outbound call. Telnyx upholds a strict policy around the handling of Caller ID Numbers for outbound calls.

All outbound calls with Caller ID Numbers that are not valid will be rejected with a SIP response code of “403 Caller Origination Number is Invalid D35”.

# **Supported Number Formats:**

When creating a SIP Connection, by default, localisation is set to USA. This means our system will accept calls in national, 11 digit or +E.164 format.   
​

**Examples:**  
​  
If my **localisation** is set to **United States** and I primarily want to reach destinations in Ireland and the USA, I would be allowed dial the following formats.   
​  
​**United States:**   
Accepted dialing formats - **national, 11 digit** and **+E.164**.

* 3129457420
* 1312945720
* +1312945720

**Ireland:**

Accepted dialling formats - **+E.164 only**.

* +353-1-840-1234

If the **localisation** was set to **Ireland** and I wanted to dial Irish and American numbers:  
​  
​**Ireland:**   
Accepted dialing formats - **national**, **11 digit** and **+E.164**.

* 840-1234
* 01-840-1234
* +353-1-840-1234

**United States:**

Accepted dialling formats - **+E.164 only**.

* +13129457420

**If the Connection’s Caller ID Override is set and used for an outbound call**

1. Send any format if you setup override in your Connection's Outbound settings.

[![](https://downloads.intercomcdn.com/i/o/ltcafuzd/1312870655/bc96d65a9cb7e6340a2072f1d9da/image.png?expires=1781167500&signature=2e48e50bff7f16c2fbe9fda0780294e3b7c1a0ff1085592c79b3e22f9a688152&req=dSMmFMF5nYdaXPMW1HO4zYu4v%2FShac9gnjTf2Jv1xVCKVSZEmINU58F8HR%2Fs%0AcCIPMbbg6J1XlVBCIIc%3D%0A)](https://downloads.intercomcdn.com/i/o/ltcafuzd/1312870655/bc96d65a9cb7e6340a2072f1d9da/image.png?expires=1781167500&signature=2e48e50bff7f16c2fbe9fda0780294e3b7c1a0ff1085592c79b3e22f9a688152&req=dSMmFMF5nYdaXPMW1HO4zYu4v%2FShac9gnjTf2Jv1xVCKVSZEmINU58F8HR%2Fs%0AcCIPMbbg6J1XlVBCIIc%3D%0A)

## **How Telnyx handles the Caller ID Number:**

* The Localisation Country can be set through the Telnyx Mission Control Portal under the Connection's Outbound Settings.
* If a Connection does not have a Localisation Country and the number dialled appears to be invalid, Telnyx will attempt to validate the number using USA as the Localisation Country.
* If the previous check failed, Telnyx will return a 404 invalid destination response.

## Which headers from the SIP INVITE can carry the Caller ID Number?

Below listed is the following SIP headers that are accepted for Caller ID, ordered by priority *(1 highest and 4 lowest priority)*

```
1. P-Preferred-Identity User  
2. P-Asserted-Identity User  
3. Remote-Party-Id User  
4. FROM User
```

***In the case that more than one header is provided the highest priority header is followed.***

## **How to Anonymize Caller ID Number**

The following SIP header needs to be provided on any outbound call that you want to anonymize. The header needs to be provided along with a valid caller ID with a number format that obeys the specifications described in the points above

```
Privacy: id
```

You are still required to send a valid origination number with the Privacy header. We will in turn change the caller ID to anonymous. However if we do not receive a valid caller ID the calls will be rejected with the error **403 Caller Origination Number is Invalid D35.**

**⚠️ Important - EEA Destinations:**  
Calls terminating into the EEA internationally must include a valid P-Asserted-Identity (PAI) header containing a real, dialable CLI. This is used by downstream carriers for origination-based routing (OBR) billing.  
​  
If the PAI header is:  
​  
• Missing  
• Contains an anonymous value  
• Contains an invalid number  
​  
...the call may be rejected or subject to surcharges from the terminating carrier which will be passed onto the customer. Anonymous or invalid CLIs on these routes are not supported and can result in significant additional costs.

​***Notes:***

* The Caller ID of an outbound call will be anonymized downstream as the "Privacy: id" SIP Header is present.
* If the number you wish to call anonymously is a toll-free number, your Caller ID number will not be anonymized. The owner of the toll free number will be paying for the call and therefore has the right to know who is calling them. This also applies when dialling emergency numbers.

## **Do you support caller ID spoofing on international routes?**

* For outbound calls to international destinations, calls will be rejected as we, and many of the downstream carriers, do not support international spoofing.
* You can typically expect a 503 error response under this scenario so that you can attempt to route advance on your side.

---

Related Articles

[Set up Inbound Caller ID Name (incoming)](https://support.telnyx.com/en/articles/1130656-set-up-inbound-caller-id-name-incoming)[SIP Connection: Number Formats](https://support.telnyx.com/en/articles/1130706-sip-connection-number-formats)[Caller ID Outbound vs CNAM](https://support.telnyx.com/en/articles/1130720-caller-id-outbound-vs-cnam)[SIP Connection: Inbound & Outbound Settings](https://support.telnyx.com/en/articles/4404448-sip-connection-inbound-outbound-settings)[Troubleshooting Call Completion](https://support.telnyx.com/en/articles/5025298-troubleshooting-call-completion)

Did this answer your question?

😞😐😃

Table of contents
