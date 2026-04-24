---
title: ngrok
summary: Telnyx's ngrok setup guide allows developers to easily create secure tunnels to their local development environment.
sources:
  - url: https://developers.telnyx.com/development/development-tools/ngrok-setup/index
    content_hash: 8ac64e1a417c0441231bc4ae977abf7ff851c598602857c353a2b1bdcb30f757
updated_at: 2026-04-10T00:00:00Z
---

# ngrok

Telnyx's ngrok setup guide allows developers to easily create secure tunnels to their local development environment.

This guide walks through how to get ngrok up and running on your machine. To test it out with Telnyx webhooks, you'll need to [sign up](https://telnyx.com/sign-up). If you'd like to test out your ngrok instance by receiving a webhook associated with an API-enabled phone call, jump to our [Receiving Webhooks in Voice API](https://developers.telnyx.com/docs/voice/programmable-voice/receiving-webhooks) after you complete these steps!

[ngrok](https://ngrok.com) is a popular tunneling tool used to expose a locally running application to the internet. You can download it for free with all of the functionality you need [here](https://ngrok.com/download). This is useful for receiving webhooks to your local applications for testing.

For the sake of this tutorial, we'll assume that your local application is running locally on port `5000`. Now you’ll need the ability to send a request to that port from Telnyx. You can easily do this using ngrok when developing your application.

Sign up for ngrok and follow the setup and installation steps to get up and running. The final step in the process is to start an HTTP tunnel to your application. The instructions specify `$ ./ngrok http 80`, which will tunnel traffic to port `80` on your machine. As our application is running on port `5000`, you should use that instead: `$ ./ngrok http 5000`.

When you run this command, you should see output similar to the following:

```bash theme={null}
ngrok by @inconshreveable

Session Status                online
Account                       Little Bobby Tables (Plan: Free)
Version                       2.3.28
Region                        United States (us)
Web Interface                 http://127.0.0.1:4040
Forwarding                    http://ead8b6b4.ngrok.io -> localhost:5000
Forwarding                    https://ead8b6b4.ngrok.io -> localhost:5000

Connections                   ttl     opn     rt1.   rt5     p50     p90
                              0       0       0.00    0.00    0.00    0.00
```

## ngrok forwarding address

The forwarding addresses will be different for you, but they should still point to `localhost:5000`. Copy the https forwarding address, as you'll need it to configure your Mission Control Portal.

## Messaging With ngrok

For messaging, webhooks set the webhook URL on your messaging profile from the Telnyx Portal Messaging dashboard. Edit your Messaging Profile by clicking the “Basic Options” button \[✎]. Select the “Inbound” section and paste the forwarding address from ngrok into the Webhook URL field. Append `/webhooks` to the end of the URL to direct the request to the webhook endpoint in your local application.

## Resending webhooks

For now, you'll leave “Failover URL” blank, but if you wanted to have Telnyx resend the webhook — if sending to the Webhook URL fails — you can specify an alternate address in this field.

## Next steps

We hope this guide helped you understand how to use ngrok. Next, why not dive into our API and start sending text messages and making API-enabled phone calls? [Create an account](https://telnyx.com/sign-up) and enjoy Telnyx APIs!
