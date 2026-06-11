---
source_url: https://support.telnyx.com/en/articles/4287554-sms-setup-with-postman
scraped: 2026-06-11
---

SMS Setup with POSTMAN | Telnyx Help Center

[Skip to main content](#main-content)

# SMS Setup with POSTMAN

This article gives an overview of how you can get started with Telnyx SMS product

Written by Shubam

June 6, 2024

Table of contents

Make sure you've configured your account, such as purchasing a number, creating a messaging profile, and associating that messaging profile with that number.   
​  
More details for [sending SMS using POSTMAN here](https://developers.telnyx.com/docs/messaging/messages/mission-control-portal-set-up) and for [specific error codes](https://developers.telnyx.com/api/errors) here.  
​  
POSTMAN is a RESTful HTTP client and can be downloaded from here: <https://www.postman.com/downloads/>  
​  
​

[![Breaking Line](https://downloads.intercomcdn.com/i/o/226483939/ed2cce9ed61fd46892a4a082/line.png?expires=1781168400&signature=cf4ff574480a4910c10f9dbc15623b32ab383e262e65c79dff7166141bc4a86b&req=diIhEsF9lIJWFb4f3HP0gLK9YgWB0hmnv1b6t%2BUbITS%2FJqOzeJ%2BGW47VUXMj%0ATzhhI2kdGNG%2B32RirQ%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/226483939/ed2cce9ed61fd46892a4a082/line.png?expires=1781168400&signature=cf4ff574480a4910c10f9dbc15623b32ab383e262e65c79dff7166141bc4a86b&req=diIhEsF9lIJWFb4f3HP0gLK9YgWB0hmnv1b6t%2BUbITS%2FJqOzeJ%2BGW47VUXMj%0ATzhhI2kdGNG%2B32RirQ%3D%3D%0A)

# **Sending SMS Via API v1**

At this stage, you are ready to send SMS.

1. Open up, [Postman](https://www.postman.com/postman). "POST" to "<https://sms.telnyx.com/messages>"
2. In "Headers", set your "x-profile-secret" to the secret under your Messaging Profile.
3. In the "Body", you can paste in the following:

```
{  
"from": "+1[your messaging-enabled number]",  
"to": "+1[intended recipient]",  
"body": "Hello World"  
}
```

## **Video demo showing sending SMS via Postman using API v1**

Yay! You have sent your first SMS using API V1.

[![Breaking Line](https://downloads.intercomcdn.com/i/o/226483939/ed2cce9ed61fd46892a4a082/line.png?expires=1781168400&signature=cf4ff574480a4910c10f9dbc15623b32ab383e262e65c79dff7166141bc4a86b&req=diIhEsF9lIJWFb4f3HP0gLK9YgWB0hmnv1b6t%2BUbITS%2FJqOzeJ%2BGW47VUXMj%0ATzhhI2kdGNG%2B32RirQ%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/226483939/ed2cce9ed61fd46892a4a082/line.png?expires=1781168400&signature=cf4ff574480a4910c10f9dbc15623b32ab383e262e65c79dff7166141bc4a86b&req=diIhEsF9lIJWFb4f3HP0gLK9YgWB0hmnv1b6t%2BUbITS%2FJqOzeJ%2BGW47VUXMj%0ATzhhI2kdGNG%2B32RirQ%3D%3D%0A)

## **Sending SMS Via API V2**

Open up, Postman. "POST" to "<https://api.telnyx.com/v2/messages>"

Now you need to generate API V2 secret Key

For using API V2 to send out SMS, you need to generate V2 key here in the [API Keys Section](https://portal.telnyx.com/#/app/api-keys)

[![API keys section on the mission control portal. ](https://downloads.intercomcdn.com/i/o/234687069/baecc6616221b79321d16525/Screenshot+2020-08-09+at+7.41.33+pm.png?expires=1781168400&signature=074d67185a9d1dcee642946f3377f87d59933f741de5a5109a834c74a9821fe5&req=diMjEMF5nYdWFb4f3HP0gPnTWGGQpD%2F%2FAGZqktk3o%2FuH%2BhoVCv1GxY1SV0P8%0A1EAuzlYX70GcWYjqyA%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/234687069/baecc6616221b79321d16525/Screenshot+2020-08-09+at+7.41.33+pm.png?expires=1781168400&signature=074d67185a9d1dcee642946f3377f87d59933f741de5a5109a834c74a9821fe5&req=diMjEMF5nYdWFb4f3HP0gPnTWGGQpD%2F%2FAGZqktk3o%2FuH%2BhoVCv1GxY1SV0P8%0A1EAuzlYX70GcWYjqyA%3D%3D%0A)

* Click on create API key on top

[![Create API key tab. ](https://downloads.intercomcdn.com/i/o/234687261/e5a10befa015fd22473ed51e/Screenshot+2020-08-09+at+7.43.06+pm.png?expires=1781168400&signature=03e079ac9776d94f48701c05230728d9b6b68119f3ed7d9587eaf72cc1b8c090&req=diMjEMF5n4deFb4f3HP0gApDrUMOmKfBLfI%2B5%2FXP9NmtU%2FfXtl42PdTzG%2Fsz%0Aw3VTCaZfZEzBBEQXBQ%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/234687261/e5a10befa015fd22473ed51e/Screenshot+2020-08-09+at+7.43.06+pm.png?expires=1781168400&signature=03e079ac9776d94f48701c05230728d9b6b68119f3ed7d9587eaf72cc1b8c090&req=diMjEMF5n4deFb4f3HP0gApDrUMOmKfBLfI%2B5%2FXP9NmtU%2FfXtl42PdTzG%2Fsz%0Aw3VTCaZfZEzBBEQXBQ%3D%3D%0A)

* This will be the new API v2 key that will be used while sending SMS

[![API keys options section. ](https://downloads.intercomcdn.com/i/o/234687367/b2e075e6f5a7b2839e1a6e0d/Screenshot+2020-08-09+at+7.44.05+pm.png?expires=1781168400&signature=3925e187ae197942dc2209ddf0986a78b16bb2d2e907b966fe36ec36ecc35202&req=diMjEMF5nodYFb4f3HP0gDb334T4p2Ervia%2BNr1lLzI6QJXmXYBxqZEU5tx1%0AdKsygR2aWOQ1UB8Gbw%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/234687367/b2e075e6f5a7b2839e1a6e0d/Screenshot+2020-08-09+at+7.44.05+pm.png?expires=1781168400&signature=3925e187ae197942dc2209ddf0986a78b16bb2d2e907b966fe36ec36ecc35202&req=diMjEMF5nodYFb4f3HP0gDb334T4p2Ervia%2BNr1lLzI6QJXmXYBxqZEU5tx1%0AdKsygR2aWOQ1UB8Gbw%3D%3D%0A)

* In the Postman "Headers", set your "Authorization" to the API v2 secret key and the Key should be preceded with "Bearer".

[![Authorization button. ](https://downloads.intercomcdn.com/i/o/234688601/bf29a2df7c8bde5b6e41e2cc/Screenshot+2020-08-09+at+7.58.32+pm.png?expires=1781168400&signature=977fa34f70e2667302b1a4806ae13616313bd93e96d10721b88d860844cd1897&req=diMjEMF2m4FeFb4f3HP0gFxW80juc7LE9jWlFiaZvS0eUYX%2FFc3Aa3%2FBVwtO%0AJfLkqPy0jdNx8cBPzA%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/234688601/bf29a2df7c8bde5b6e41e2cc/Screenshot+2020-08-09+at+7.58.32+pm.png?expires=1781168400&signature=977fa34f70e2667302b1a4806ae13616313bd93e96d10721b88d860844cd1897&req=diMjEMF2m4FeFb4f3HP0gFxW80juc7LE9jWlFiaZvS0eUYX%2FFc3Aa3%2FBVwtO%0AJfLkqPy0jdNx8cBPzA%3D%3D%0A)

* In the "Body", you can paste in the following:

```
{  
"from": "+1[your messaging-enabled number]",  
"to": "+1[intended recipient]",  
"text": "Hello World"  
}
```

## **Video demo showing sending SMS via Postman using API V2**

Kudos! now you know how to send SMS using API V2  
​

[![Breaking Line](https://downloads.intercomcdn.com/i/o/226483939/ed2cce9ed61fd46892a4a082/line.png?expires=1781168400&signature=cf4ff574480a4910c10f9dbc15623b32ab383e262e65c79dff7166141bc4a86b&req=diIhEsF9lIJWFb4f3HP0gLK9YgWB0hmnv1b6t%2BUbITS%2FJqOzeJ%2BGW47VUXMj%0ATzhhI2kdGNG%2B32RirQ%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/226483939/ed2cce9ed61fd46892a4a082/line.png?expires=1781168400&signature=cf4ff574480a4910c10f9dbc15623b32ab383e262e65c79dff7166141bc4a86b&req=diIhEsF9lIJWFb4f3HP0gLK9YgWB0hmnv1b6t%2BUbITS%2FJqOzeJ%2BGW47VUXMj%0ATzhhI2kdGNG%2B32RirQ%3D%3D%0A)

---

Related Articles

[MMS Sending and Receiving](https://support.telnyx.com/en/articles/3102823-mms-sending-and-receiving)[Forwarding SMS to Your Mobile Number](https://support.telnyx.com/en/articles/3231942-forwarding-sms-to-your-mobile-number)[Sending Alphanumeric SMS - Sender ID](https://support.telnyx.com/en/articles/4371498-sending-alphanumeric-sms-sender-id)[Telnyx Verify: 2FA made easy](https://support.telnyx.com/en/articles/5701653-telnyx-verify-2fa-made-easy)[Bot-to-Bot Support API: Ask Telnyx Knowledge Agent](https://support.telnyx.com/en/articles/15455646-bot-to-bot-support-api-ask-telnyx-knowledge-agent)

Did this answer your question?

😞😐😃

Table of contents
