---
source_url: https://support.telnyx.com/en/articles/7020727-account-compromise-what-to-do
scraped: 2026-06-11
---

Account Compromise: What to Do | Telnyx Help Center

[Skip to main content](#main-content)

# Account Compromise: What to Do

Was your account compromised? Here are the steps to take to secure your account.

Written by David

January 26, 2026

Table of contents

# What to do after my account got compromised?

We understand that there are individuals who may attempt to gain unauthorised access to your Telnyx account, which can compromise your security. If you suspect that someone has accessed your account without your permission, there are some important steps you can take to protect your account and prevent future unauthorised access.

There are many ways a bad actor can gain access to your account, either because the same password was used in a another platform whose information was released or some creative social engineering. However it's imperative to take crucial steps to ensure said bad actor is not only prevented from accessing your account again but also does not have access to the API or voice products.

## **These are the specific steps needed to take to ensure your account is secure after somebody gained access to your Mission Control Portal:**

* **Change login password for the compromised user in your organization**. This can be done under the [general settings](https://portal.telnyx.com/#/app/account/general) of account.
* **Change credentials for all of your credential authentication based SIP connections**. This can be done in the [Sip Trunking](https://portal.telnyx.com/#/voice/connections) page in the Voice section of your account. You also need to update the credentials on your phone system for it to be able to access the Sip trunk with the new credentials. [Here's more information About Sip Connections](https://support.telnyx.com/en/articles/4245868-sip-connection-types) on the Mission Control Portal. Make sure all the SIP connections in your account where setup by you and not the bad actor.
* **Check the configuration of all your [IP authentication connections](https://portal.telnyx.com/#/voice/connections)** to make sure all the IPs in said connections are your IPs and not ones setup by the bad actor to run traffic from their own systems. Again refer [to this article](https://support.telnyx.com/en/articles/4245868-sip-connection-types) to check into specific guide on how to check your sip connections.
* **Regenerate the [messaging profile](https://portal.telnyx.com/#/app/programmable-messaging/profiles) secret for any messaging profiles** using v1 of our API. This can be done in the Programmable Messaging page in the Messaging section of the portal by going into the messaging profile settings. You also need to update your messaging applications with the new secret. More information about messaging profiles on your Mission Control Portal can be [found here.](https://support.telnyx.com/en/articles/3562059-setting-up-a-messaging-profile)
* **Delete any [API Key](https://portal.telnyx.com/#/app/api-keys) you currently had active** when the bad actor accessed your account. You need to go into the Account Settings section then into the Keys and Credentials page and delete all then generate new API keys for your applications. You need to update the API keys of your applications for them to continue to have access to our products.
* **Check forwarding on [all numbers](https://portal.telnyx.com/#/app/numbers/my-numbers) in your account** to make sure the bad actor has not setup forwarding to expensive numbers that could run bad traffic from your account even after securing it. You can read more about [setting up forwarding in this article.](https://support.telnyx.com/en/articles/1130657-call-forwarding)
* **Check all your [Programmable Voice API Applications](https://portal.telnyx.com/#/app/call-control/applications) and [TeXML Applications](https://portal.telnyx.com/#/app/call-control/texml)** to make sure they are actually yours and not applications configured by the bad actor that could automatically be running traffic on your account. Disabling the API key would prevent traffic through Voice API Applications but not TeXML Applications. So make sure you check into these too.

### **There are several steps you can take to prevent this happening in the future but the single most powerful thing you can do is [enabling 2 factor authentication](https://support.telnyx.com/en/articles/3739748-2fa-totp-setup). You can do this by going into the My Account page in the Account Settings section of the portal.**

If a bad actor has gained access to your system but not your account they can still have stolen the credentials for your sip connection, the messaging profile secret or the API keys if you had those setup in your system so make sure to update them in your Mission Control Portal.

For more information on other options to prevent fraud on your account like setting up limits please follow [this guide.](https://support.telnyx.com/en/articles/3610162-prevent-telnyx-account-fraud)

---

Related Articles

[Prevent Telnyx Account Fraud](https://support.telnyx.com/en/articles/3610162-prevent-telnyx-account-fraud)[SIP Connection: Settings](https://support.telnyx.com/en/articles/4351104-sip-connection-settings)[Telephony Credentials: Types](https://support.telnyx.com/en/articles/7029684-telephony-credentials-types)[Android Push Notification Setup](https://support.telnyx.com/en/articles/8268140-android-push-notification-setup)[Telnyx + Vapi Integration](https://support.telnyx.com/en/articles/12538402-telnyx-vapi-integration)

Did this answer your question?

😞😐😃

Table of contents
