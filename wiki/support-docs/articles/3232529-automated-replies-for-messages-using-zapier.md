---
title: "Automated Replies for Messages using Zapier"
summary: "Setup an automated reply for all inbound SMS messages to your Telnyx number using… See Telnyx guidance and requirements."
sources:
- url: "https://support.telnyx.com/en/articles/3232529-automated-replies-for-messages-using-zapier"
updated_at: 2026-07-08T00:00:00Z
tags: [support-docs]
source_path: "support-docs/en--articles--3232529-automated-replies-for-messages-using-zapier.md"
generated_by: incremental-support-docs-wiki
---
<!-- generated_from=support-docs/en--articles--3232529-automated-replies-for-messages-using-zapier.md -->

# Automated Replies for Messages using Zapier

Setup an automated reply for all inbound SMS messages to your Telnyx number using… See Telnyx guidance and requirements.




## **Step-by-Step Guide to Setting up Automated Reply**

Visit [Zapier's Telnyx integration page](https://zapier.com/apps/telnyx/integrations) to connect your Telnyx account.

In this example, we'll setup a very basic auto-reply for incoming messages to your Telnyx number.

* Let's go ahead and make a Make a Zap!.
* Choose Telnyx as the trigger App. Then under Choose Trigger Event, click on Receive a Message and click Continue.
* Click on the account you'd like to use for receiving messages.

*Note that all messages received by another number associated with the messaging profile will be used for this Zap. For this reason we highly recommend only attaching a single number to a messaging profile you use for Zaps.*

* Click Continue and click Find Message on the next page to pull in a sample inbound message webhook to use to setup the action stage.
* Moving onto the action stage. Search for Telnyx and choose Send SMS under the Choose Action Event dropdown and click Continue.
* Now choose the account you'd like to use for sending the message and click Continue.
* Now we'll use information from the incoming message again to populate some of these fields.
* Under source number, enter the number you'd like to send from.
* Under Destination Number, click the drop down and click on From Phone Number. What we've done here is make the source number that sent the original message the receiver of the message that we're going to send out now.
* Under Message Content enter the automated message you'd like to send out.

**Note:** If you're sending automated SMS replies to US numbers, ensure your Telnyx number is associated with a registered 10DLC campaign and an active messaging profile. Unregistered A2P traffic may be filtered or blocked by carriers.

Hi there, this is an automated reply!

* Click Continue and then then Send Test. You're all set now. Make sure the Zap is on, then go ahead and send a message to the Telnyx number you entered in the Source Number Field.

You should see your reply come through automatically!

## Final step, turn Zap on!

**Turn your Zap on** and you're all set! You've set up a quick way to auto-reply to inbound messages to your Telnyx number!
