---
source_url: https://support.telnyx.com/en/articles/1270091-sms-opt-out-keywords-and-stop-words
scraped: 2026-06-11
---

SMS Opt-Out Keywords and Stop Words | Telnyx Help Center

[Skip to main content](#main-content)

# SMS Opt-Out Keywords and Stop Words

Learn more about how Telnyx processes SMS opt-outs and handles stop words

Written by Telnyx Engineering

Updated over 3 weeks ago

Table of contents

# **What are SMS Opt-Out Keywords?**

Telnyx automatically processes incoming messages and recognises **English language** stop words. Stop words are specific words such as STOP or UNSUBSCRIBE that signal that a person no longer wishes to receive messages from you.

When Telnyx identifies a stop word, the person's phone number is added to the opt-out list and you will no longer be able to send messages to that number.

## **What do opt outs at the messaging profile mean?**

This is default behaviour when you create an account**.** This means any further messages from numbers on the same messaging profile that are sent to a number on the opt-out list will not be processed. So if there are two messaging profiles: **X** and **Y**

* Messaging Profile X has the numbers [1-222-222-2222](tel:12222222222) & [1-333-333-3333](tel:13333333333) assigned with some other numbers also associated to the X messaging profile.
* Messaging Profile Y has the number [1-444-444-4444](tel:14444444444) assigned with some other numbers also associated to the X messaging profile.
* If the number [1-222-222-2222](tel:12222222222) from messaging profile X sends a text to [1-999-999-9999](tel:19999999999) and [1-999-999-9999](tel:19999999999) opts out by responding with STOP, then both [1-222-222-2222](tel:12222222222) & [1-333-333-3333](tel:13333333333) and any other number associated with that **messaging profile X** will not be able to text [1-999-999-9999](tel:19999999999) further.
* The number [1-444-444-4444](tel:14444444444) on **messaging profile Y** can still text [1-999-999-9999](tel:19999999999).

Coming soon: You will soon be able to retrieve all phone numbers that are on the opt-out list.

## **Telnyx recognizes the following English-language stop words:**

* stop
* stopall
* stop all
* unsubscribe
* cancel
* end
* quit

Please note that stop words are only recognized if they are the only words in the message. For example, "stop all" is recognized but "please stop all messages" would not be recognized.

## **To opt in again, the number that opted out has to send any of the following opt-in keywords to the exact same number they opted out from:**

* start
* unstop

## Number pool

Note that to be able to restart messages, the end user needs to send the opt in keywords above to the exact same number they opted out from. When using our number pool feature you might not get clarity as what number they opted out from since it you used several numbers to send messages out. You should be able to find the opt out SMS in your MDRs by filtering for number that opted out, this way you can easily determine the number where the opt in needs to be sent to.

## **Who handles the auto response from an opt out?**

By default, Telnyx will handle the auto response. If a user of your services decides to opt out via one of the above stop words towards your numbers, Telnyx will detect this and automatically send out a generic unsubscribed message from the number that received the opt out message.

## What is the auto response when someone texts "stop"

**Generic Messages**:

* "You have successfully been unsubscribed, you will not receive any more messages from this number. Reply START to re-subscribe."
* You have successfully been re-subscribed to this number. Reply STOP to unsubscribe. Msg&Data Rates May Apply.

However, It is possible to allow for custom block rules and auto responses on a per messaging profile basis but recommend contacting our sales team ([sales@telnyx.com](mailto:sales@telnyx.com)) to discuss this further.

## Keyword Management

Telnyx now offers the ability to add custom keywords for opt-in/out and help messages along with specifying the new keywords auto responses.

[This feature can be accessed on the portal here: https://portal.telnyx.com/#/programmable-messaging/keywords-management](https://portal.telnyx.com/#/programmable-messaging/keywords-management)

To set up custom keywords simply select your desired messaging profile form the keywords management menu where you will then be given the option to add keywords for the messaging profile globally (Country: Global). Or if you wish to specify keywords for particular countries you can click the **"Add keywords in other languages based on country selected"** button at the bottom of this list. This will then create a new rule set for custom keywords and allow you to select a specified country that these new rules should apply to from the drop down menu, then just fill in your new keywords and auto response and don't forget to hit the save button before closing the menu.

**Restrictions for the above:**

* You can add a maximum of 20 keywords

---

Related Articles

[Hosted SMS Messaging Process](https://support.telnyx.com/en/articles/5336668-hosted-sms-messaging-process)[Toll-Free Opt-Out Words](https://support.telnyx.com/en/articles/6989758-toll-free-opt-out-words)[Standards for US Short Code Keywords: HELP, STOP, and Opt-In Confirmation](https://support.telnyx.com/en/articles/9311492-standards-for-us-short-code-keywords-help-stop-and-opt-in-confirmation)

Did this answer your question?

😞😐😃

Table of contents
