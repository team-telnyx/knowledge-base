---
source_url: https://support.telnyx.com/en/articles/8709331-porting-bundles
scraped: 2026-07-08
content_hash: 385eaf7ff1e177726482b7d66187a2172c6ec9888aee27bcc1f2fa79b74bc838
---

Porting + Bundles | Telnyx Help Center

[Skip to main content](#main-content)

# Porting + Bundles

Learn how to pre-configure your porting order with Bundles. Start building on Telnyx today.

Written by Telnyx Engineering

June 26, 2024

Table of contents

[Bundles](https://support.telnyx.com/en/articles/8340760-bundles-bundle-pricing) is a new pricing option being offered by Telnyx.

Here's how you can pre-configure your porting order with bundles:

---

# Couple of notes:

* You may pre-configure bundles on your porting order at any point as long as the order hasn't completed (i.e. it is in a `cancelled` or `ported` status)
* A bundle is not actually applied to a phone number until after the phone number ports in. After pre-configuring a bundle with a port order, be careful not to use that same bundle in a number order.
* If an order is already ported, you cannot use porting tooling to associate bundles
* Please ensure that the bundle is eligible for your port order (i.e. a US bundle being pre-configured with US phone numbers). If the bundle is not eligible for your port order (i.e. a US bundle being pre-configured with an Australian phone numbers), then you will be unable to pre-configure it.

---

# Through the Telnyx Portal

1. Navigate to the [Port Numbers page](https://portal.telnyx.com/#/app/numbers/port-numbers?status=both) in the Telnyx Portal
2. Click on any order that you would like to pre-configure bundles with.

   1. By clicking on the order, you will open up the `Port In Details` page for that order
3. Scroll to the bottom of the page `Port In Details` page.

   1. There should be a `Pre-configure Bundles` button.
   2. Click on that button  
      ​

      ![Porting requirements example](_images/2fbf81fa64ce45e1.png)

## **Preconfigure Bundles**

1. A modal will pop up on the page. There are 2 tabs on the modal: `List` and `Add`. By default, the modal will load on the `List` tab

   1. `List`: Lists the pre-configurations you have already created. If you haven't pre-configured any bundles on the order, it will be an empty table (like the image below)
   2. `Add`: Create new pre-configurations for bundles and phone numbers on your order.  
      ​

      ![Preconfiguring bundles](_images/d7156dcfc47c8ed4.png)
2. Click on the `Add` tab.  
   ​

   ![Pre configuring list add](_images/49fb52df462b56c8.png)
3. Specify a phone number from the port order, and the bundle you would like to pre-configure with it. Then click `Create`  
   ​
4. The pre-configuration will now appear on the `List` page.

   1. Repeat steps 5-6 for every phone number you wish to pre-configure a bundle with on your porting order
   2. If you want to change the bundle associated with a particular phone number, click on the trash can in the `Delete` column to delete the pre-configuration. And then repeat steps 5-6 for that phone number  
      ​

      ![Unique bundle ID example](_images/7f3436ac26ef92a8.png)
5. When your order ports, the pre-configured bundles will automatically be applied with the specified phone numbers. You are all set!

---

# Using the Porting API

You can follow [this developers guide](https://developers.telnyx.com/docs/numbers/porting/bundles-porting) to integrate with the porting API for pre-configuring bundles to port orders

---

Related Articles

[Porting Policy & Procedure](https://support.telnyx.com/en/articles/1130630-porting-policy-procedure)[Automating Ports With Programmatic API](https://support.telnyx.com/en/articles/5386351-automating-ports-with-programmatic-api)[Flyingvoice: Telnyx Setup](https://support.telnyx.com/en/articles/5810663-flyingvoice-telnyx-setup)[Porting away from Skype](https://support.telnyx.com/en/articles/10715399-porting-away-from-skype)[Twilio TwiML Conference on Telnyx](https://support.telnyx.com/en/articles/13389311-twilio-twiml-conference-on-telnyx)

Did this answer your question?

😞😐😃

Table of contents
