---
source_url: https://support.telnyx.com/en/articles/5717957-zoiper-5-pro-telnyx-setup
scraped: 2026-06-11
---

Zoiper 5 Pro: Telnyx Setup | Telnyx Help Center

[Skip to main content](#main-content)

# Zoiper 5 Pro: Telnyx Setup

How to configure Zoiper 5 with a pro license to work with the Telnyx Mission Control portal.

C

Written by Customer Success

March 3, 2024

Table of contents

[Jump to Instructions](#h_4ff34ebbdc)

​ [Zoiper](https://support.telnyx.com/en/articles/6133517-zoiper-communicator) is a cross-platform VoIP softphone solution that supports voice calling, video calling, and instant messaging. Zoiper is available for Windows, Mac and Linux and offers companion apps for iOS, Android, and Windows Phone. Zoiper secures voice, text, and video calls through a choice of several encryption protocols. Contacts are pulled from a variety of frequently-used contact lists and arranged in an easily searchable way. Additionally, Zoiper offers call center functionality with features such as auto-answer, call transfer, recording, provisioning, and click-2-dial CRM integration. One of the powers of Zoiper is its ability to facilitate direct calls from email clients or web browsers.

|  |
| --- |
| ***Note:*** *This guide covers account configuration for Zoiper 5 Pro. Find free user license configuration instructions [here](https://app.intercom.com/a/apps/ltcafuzd/articles/articles/5717568/show).*    *If you're not sure what version is best for you, you can compare the free and pro versions [here](https://www.zoiper.com/en/products/zoiper5/features).* |

For Zoiper documentation, see:

* [Zoiper 5 user guide](https://www.zoiper.com/pdf/User%20Guide%20Zoiper%205%20v.1.0.7.pdf)

---

# Instructions for Configuring the All-New Zoiper 5 with Telnyx

1. [Configure your Telnyx Mission Control Portal](#h_dc5df9cfdf)
2. [Create your VoIP account on Zoiper](#h_d68a340083)
3. [Activating Zoiper 5 Pro offline](#h_7d1c24c1d7)
4. [Configure advanced options and features](#h_8a0117958d)

   1. [Audio codecs](#h_15e3d5415d)
   2. [Network settings](#h_a0cfa51b80)
   3. [Call encryption: TLS/SRTP](#h_75146962a7)
5. [Setting up a Caller ID](#h_3093a1dc1f)

**Video Walkthrough**

Coming soon! Check back frequently as we are updating our documentation.

**Pre-Requisites:**

* Have obtained [a license for Zoiper 5 Pro](https://www.zoiper.com/en/shop/buy/zoiper5?cid=main-nav).
* Have created a [credentials based connection](https://portal.telnyx.com/#/app/connections) on your Telnyx Mission Control Portal account, assigned this connection to a DID and outbound profile in order to make and receive outbound calls. This provides you with the username and password you will use to register Zoiper 5 with Telnyx  
  ​

## 1. Configure your Telnyx Mission Control Portal

For step by step instructions on each of the requirements on the Telnyx Mission Control Portal, please follow this [guide](https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account).

[Back to Top](#h_4ff34ebbdc)

## 2. Create your VoIP account on Zoiper

1. To activate your license, click **Activate your Premium license** and follow the instructions in the activation wizard. Note: Activation credentials are provided by Zoiper after you purchase your license. These are not your Telnyx credentials.  
   ​  
   If you don't have a license, you can [continue as a free user](https://app.intercom.com/a/apps/ltcafuzd/articles/articles/5717568/show).

   [![Activate a Zoiper 5 Pro license](https://downloads.intercomcdn.com/i/o/416321226/01660280f2e151c8d53b2f7e/Screenshot+2021-11-09+at+11.50.10+AM.png?expires=1781168400&signature=cb67848232d039d10eee3df5f7fdea666b0d967988896240d43cbb4835ec3124&req=cCEhFct%2Fn4NZFb4f3HP0gE2690fLbu3y6Um6sEZlcEv3ErPXIzHQIzDh5Gs6%0Azs0%3D%0A)](https://downloads.intercomcdn.com/i/o/416321226/01660280f2e151c8d53b2f7e/Screenshot+2021-11-09+at+11.50.10+AM.png?expires=1781168400&signature=cb67848232d039d10eee3df5f7fdea666b0d967988896240d43cbb4835ec3124&req=cCEhFct%2Fn4NZFb4f3HP0gE2690fLbu3y6Um6sEZlcEv3ErPXIzHQIzDh5Gs6%0Azs0%3D%0A)
2. You will be taken to the login screen. Click Activate online. If you need to activate offline, see these instructions.

   [![Zoiper activation login scene. ](https://downloads.intercomcdn.com/i/o/416324103/d3068b43eef3710625cb9c40/Screenshot+2021-11-09+at+11.51.39+AM.png?expires=1781168400&signature=b5a4b008119c43588b2aff8c93324a91a87b734967457e80448900a79e3bb4b0&req=cCEhFct6nIFcFb4f3HP0gLrsgNeD0amGf7HrfHHv55OSVTwp8oAff84KOXU1%0AbXM%3D%0A)](https://downloads.intercomcdn.com/i/o/416324103/d3068b43eef3710625cb9c40/Screenshot+2021-11-09+at+11.51.39+AM.png?expires=1781168400&signature=b5a4b008119c43588b2aff8c93324a91a87b734967457e80448900a79e3bb4b0&req=cCEhFct6nIFcFb4f3HP0gLrsgNeD0amGf7HrfHHv55OSVTwp8oAff84KOXU1%0AbXM%3D%0A)
3. You will be taken to the account creation wizard. Click **Create account**.

   [![Account creation wizard interface. ](https://downloads.intercomcdn.com/i/o/416325776/19614f78f7339dd337463b45/Screenshot+2021-11-09+at+11.51.51+AM.png?expires=1781168400&signature=a3a1680fb67b6e0111bbabe2795cdf103e994630ac304719a90bc96271f34d98&req=cCEhFct7moZZFb4f3HP0gFa9bdMBfE4iXPMHnQVGt2ADPqcidLbALRBMJnDy%0AxyQ%3D%0A)](https://downloads.intercomcdn.com/i/o/416325776/19614f78f7339dd337463b45/Screenshot+2021-11-09+at+11.51.51+AM.png?expires=1781168400&signature=a3a1680fb67b6e0111bbabe2795cdf103e994630ac304719a90bc96271f34d98&req=cCEhFct7moZZFb4f3HP0gFa9bdMBfE4iXPMHnQVGt2ADPqcidLbALRBMJnDy%0AxyQ%3D%0A)
4. Now, choose your location from the dropdown menu and select your country from the list. This will filter the available providers. Enter "Telnyx" in the next field to filter us out. Then select us as your provider.

   [![Account creation interface to filter Telnyx out. ](https://downloads.intercomcdn.com/i/o/416326302/33bd20e62b6e4e7062439e7c/zoiper5_3.png?expires=1781168400&signature=7c4ba939ba4d02f539baaa88319e041c1f9a59f6e143a27aae8c7dbf4958b259&req=cCEhFct4noFdFb4f3HP0gJKS5xBwOXxCsObmnlwHwJ7f1PDkKWzKZUnsz6aK%0AUAA%3D%0A)](https://downloads.intercomcdn.com/i/o/416326302/33bd20e62b6e4e7062439e7c/zoiper5_3.png?expires=1781168400&signature=7c4ba939ba4d02f539baaa88319e041c1f9a59f6e143a27aae8c7dbf4958b259&req=cCEhFct4noFdFb4f3HP0gJKS5xBwOXxCsObmnlwHwJ7f1PDkKWzKZUnsz6aK%0AUAA%3D%0A)
5. The wizard will automatically identify the proper protocols for your account. You'll see something like this. You can click **Next**.

   [![Tab to test various possible configurations. ](https://downloads.intercomcdn.com/i/o/416326869/1bda08787f1fc3211f0eec22/Screenshot+2021-11-09+at+11.52.00+AM.png?expires=1781168400&signature=3ab19ca819a768bf9346701344513a167203679e79482b5defc560785593a1c9&req=cCEhFct4lYdWFb4f3HP0gA%2FCsAcj21kW5SptcJyzUvC0RuNJqRC0Gqf3PaYy%0AhIw%3D%0A)](https://downloads.intercomcdn.com/i/o/416326869/1bda08787f1fc3211f0eec22/Screenshot+2021-11-09+at+11.52.00+AM.png?expires=1781168400&signature=3ab19ca819a768bf9346701344513a167203679e79482b5defc560785593a1c9&req=cCEhFct4lYdWFb4f3HP0gA%2FCsAcj21kW5SptcJyzUvC0RuNJqRC0Gqf3PaYy%0AhIw%3D%0A)
6. Once successfully authenticated, you'll have a new account on Zoiper 5. From here, you can set up your sound, video, and microphone settings (covered in [this guide](https://www.zoiper.com/pdf/User%20Guide%20Zoiper%205%20v.1.0.7.pdf) on page 16). Skip for now to confirm your account set up.

   [![Sound, video, and microphone settings interface on Zoiper. ](https://downloads.intercomcdn.com/i/o/416252684/012a3d1fdbcf2cf92606867e/zoiper5_5.png?expires=1781168400&signature=07b259d695165f031ad6950730c9f0f75f070eee430fa916b01e4e9be544f630&req=cCEhFMx8m4lbFb4f3HP0gLfaJCf5VDo37Ek4d8REJw3clsubXip2Os%2BvIjUE%0AGhw%3D%0A)](https://downloads.intercomcdn.com/i/o/416252684/012a3d1fdbcf2cf92606867e/zoiper5_5.png?expires=1781168400&signature=07b259d695165f031ad6950730c9f0f75f070eee430fa916b01e4e9be544f630&req=cCEhFMx8m4lbFb4f3HP0gLfaJCf5VDo37Ek4d8REJw3clsubXip2Os%2BvIjUE%0AGhw%3D%0A)
7. If you click on the account name, you'll be taken to the account settings page.

   [![Account settings page. ](https://downloads.intercomcdn.com/i/o/416355402/e48f5914cf6dad7d0d812e43/zoiper5_6.png?expires=1781168400&signature=dd894e50865cfb20eb8498292f3f4e2c6dd2f8c800d0436b6bef1dca17be8b2b&req=cCEhFcx7mYFdFb4f3HP0gEX4snzN56RPmInGKe%2B7TZuf%2FHxe%2Bu4LqohinNbt%0A01w%3D%0A)](https://downloads.intercomcdn.com/i/o/416355402/e48f5914cf6dad7d0d812e43/zoiper5_6.png?expires=1781168400&signature=dd894e50865cfb20eb8498292f3f4e2c6dd2f8c800d0436b6bef1dca17be8b2b&req=cCEhFcx7mYFdFb4f3HP0gEX4snzN56RPmInGKe%2B7TZuf%2FHxe%2Bu4LqohinNbt%0A01w%3D%0A)

If you want to configure more accounts in this manner, click the **Add** button and follow steps 3-6 again.

[Back to Top](#h_4ff34ebbdc)

## 3. Activating Zoiper 5 Pro offline

If you experience difficulty with your internet connect, or are unable to bypass your company firewall or other security settings to reach the Zoiper server, you can activate your account offline.

1. From the login screen, click **Activate offline**.

   [![Offline activation button on the login screen. ](https://downloads.intercomcdn.com/i/o/416344532/da58797922211014c0688fb6/DF53EAA0-4FA1-49A4-9075-716B711F54DE.png?expires=1781168400&signature=cf16830545aec1bb29cdc4ecd32ec90f6ab7cc157014dce7d92e6e3c691b8c14&req=cCEhFc16mIJdFb4f3HP0gOkD3CXQlAlUoucFBC458L1aB7s6udxHj224umNr%0AxEg%3D%0A)](https://downloads.intercomcdn.com/i/o/416344532/da58797922211014c0688fb6/DF53EAA0-4FA1-49A4-9075-716B711F54DE.png?expires=1781168400&signature=cf16830545aec1bb29cdc4ecd32ec90f6ab7cc157014dce7d92e6e3c691b8c14&req=cCEhFc16mIJdFb4f3HP0gOkD3CXQlAlUoucFBC458L1aB7s6udxHj224umNr%0AxEg%3D%0A)
2. This will generate a file named **Zoiper<ComputerName>.certificate** that contains information about your version of Zoiper and some details about your computer.

   1. If you have installed Zoiper for "all users", you can find the certificate folder within the \Zoiper5\ folder.
   2. If you have installed Zoiper for "the current user only", you can find the certificate folder in `%USERPROFILE%\AppData\Romaing\Zoiper5` on windows or either `~/Library/Application Support` or `~/Library/Preferences` on Mac.
3. Send **Zoiper<ComputerName>.certificate** to [register5@shop.zoiper.com](mailto:register5@shop.zoiper.com) who will send you back a certificate back.
4. Save this certificate in the same folder as 2.b.

|  |
| --- |
| ***Note:*** *By default, Windows hides known file extensions and may automatically append a file extension to the file when its saved. When you find it, right-click on the file, choose **Properties**, and remove any extension that Windows automatically may have added.* |

[Back to Top](#h_4ff34ebbdc)

## 4. Advanced setup and features

To adjust the advanced features of your Zoiper 5 account:

1. Click on **Advanced** from your account settings view.

   [![Advanced settings in the Accounts section. ](https://downloads.intercomcdn.com/i/o/416358648/7131d4e55090801c925efd38/zoiper5_7.png?expires=1781168400&signature=222042a2ae8f602be89f5c44039de84f9b32c1f781753216b33b6c57cc13a442&req=cCEhFcx2m4VXFb4f3HP0gLeXYXe1TNTvnXRY94ZcXd9m46ioZehHaCfsh2LB%0AtYI%3D%0A)](https://downloads.intercomcdn.com/i/o/416358648/7131d4e55090801c925efd38/zoiper5_7.png?expires=1781168400&signature=222042a2ae8f602be89f5c44039de84f9b32c1f781753216b33b6c57cc13a442&req=cCEhFcx2m4VXFb4f3HP0gLeXYXe1TNTvnXRY94ZcXd9m46ioZehHaCfsh2LB%0AtYI%3D%0A)

## **4.1. Audio Codecs**

1. From the Advanced settings, scroll down the page to the **[Audio Codecs](https://telnyx.com/resources/codecs-affect-voip-sound-quality)** section.
2. From here, you can hover over any codecs on the left and use the arrows to move them to the right.

[![Selected Codecs of the Audio codecs section. ](https://downloads.intercomcdn.com/i/o/416362656/8bd49bb42fdfbf5de81b04a9/codecs.png?expires=1781168400&signature=16ba2e064d3d3026060073fd70fbaf2a60813dbc2fe7acfd5e4728965979c292&req=cCEhFc98m4RZFb4f3HP0gKnMUbszUVixwYM%2FUl%2Fey4m6wbxWuoWwwBJREfPX%0AtOUXEwOL%2F0Nkddf9XQ%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/416362656/8bd49bb42fdfbf5de81b04a9/codecs.png?expires=1781168400&signature=16ba2e064d3d3026060073fd70fbaf2a60813dbc2fe7acfd5e4728965979c292&req=cCEhFc98m4RZFb4f3HP0gKnMUbszUVixwYM%2FUl%2Fey4m6wbxWuoWwwBJREfPX%0AtOUXEwOL%2F0Nkddf9XQ%3D%3D%0A)

[Back to Top](#h_4ff34ebbdc)

## **4.2. Network Settings**

You can set your Zoiper 5 softphone to run all the time with the following steps:

1. Scroll through the advanced settings page to the **Network Related** section.
2. Apply the following changes:

   * **Registration expire mode:** Custom
   * **Registration expiry:** 300
   * **NAT keep alive time-out:** Custom
   * **Keep alive custom interval:** 30

   [![Network settings page. ](https://downloads.intercomcdn.com/i/o/416365839/36921007979de523d48cb739/network.png?expires=1781168400&signature=fbdbd1bf3929b999040dc4f588bdcb3da1f9e7918f270c4351d58fce22440a4e&req=cCEhFc97lYJWFb4f3HP0gO165cwvb1ee8nygLzn%2FZ%2FCOLrRvUmxGjoupCri3%0AHEk%3D%0A)](https://downloads.intercomcdn.com/i/o/416365839/36921007979de523d48cb739/network.png?expires=1781168400&signature=fbdbd1bf3929b999040dc4f588bdcb3da1f9e7918f270c4351d58fce22440a4e&req=cCEhFc97lYJWFb4f3HP0gO165cwvb1ee8nygLzn%2FZ%2FCOLrRvUmxGjoupCri3%0AHEk%3D%0A)

[Back to Top](#h_4ff34ebbdc)

## **4.3. Call Encryption TLS/SRTP**

You can choose to use SIP TLS call encryption with your Zoiper 5 account. To do this:

1. Make sure your account has **Encrypted SIP Traffic** enabled. ***Keep in mind*** *that if this setting is enabled, but your device is sending UDP/TCP or RTP, this change will be rejected and you will get an error code (error code: 488).* Enable this setting here:

   [![Account settings page. ](https://downloads.intercomcdn.com/i/o/416368047/f712cfad27a7a6eb40d9a813/encrypt.png?expires=1781168400&signature=ea4feff43a40e80691379ecf847c64ed446d36150ed4cf05b4394da8387dcd8d&req=cCEhFc92nYVYFb4f3HP0gFTcTCl4QdBB6VNskudJeimywYQWSOVXyRl51bh5%0ANXE%3D%0A)](https://downloads.intercomcdn.com/i/o/416368047/f712cfad27a7a6eb40d9a813/encrypt.png?expires=1781168400&signature=ea4feff43a40e80691379ecf847c64ed446d36150ed4cf05b4394da8387dcd8d&req=cCEhFc92nYVYFb4f3HP0gFTcTCl4QdBB6VNskudJeimywYQWSOVXyRl51bh5%0ANXE%3D%0A)
2. If you're encrypting a sub-account, you can enable this in **Sub accounts>Manage sub-accounts>Advanced Options (click here to display)**

   [![ub accounts&gt;Manage sub-accounts&gt;Advanced Options page. ](https://downloads.intercomcdn.com/i/o/416370441/42e902ea9648fccffa34b875/subs.png?expires=1781168400&signature=674cf752641463d6d6f276c42ec4af59bf29a1815cee96c74a00c2164dfd4d48&req=cCEhFc5%2BmYVeFb4f3HP0gOcgditUGfQ8yDatnBg2bjcGBuByQb6rTwxFn5xp%0AKTU%3D%0A)](https://downloads.intercomcdn.com/i/o/416370441/42e902ea9648fccffa34b875/subs.png?expires=1781168400&signature=674cf752641463d6d6f276c42ec4af59bf29a1815cee96c74a00c2164dfd4d48&req=cCEhFc5%2BmYVeFb4f3HP0gOcgditUGfQ8yDatnBg2bjcGBuByQb6rTwxFn5xp%0AKTU%3D%0A)
3. Once you've enabled this setting in your desired account(s), you can set it up to send TLS and SRTP.
4. To enable TLS, find the **SIP Credentials** section in the **Advanced** section and fill in the following information:

   * **Domain:** sip.telnyx.com
   * **Username:** The name of your account/sub-account
   * **Password:** Your SIP password

   1. Scroll down the page to the **Network Related** section and set:

      1. **Transport:** TLS
5. To enable SRTP, scroll to the **Encryption** section and set the following:

   1. **SRTP Key Negotiation:** SDES

      [![Encryption settings page. ](https://downloads.intercomcdn.com/i/o/416376605/507ff101e742ce23e5c9f4db/srtp.png?expires=1781168400&signature=ff5b51f372d754ff364b56069fbec8d01d0431f58ed1ed9a00c099db5df6960e&req=cCEhFc54m4FaFb4f3HP0gG2OtPOe3dIMHxIPhwWG1eY8jaL8CcDzH8QF5RJw%0AYHk%3D%0A)](https://downloads.intercomcdn.com/i/o/416376605/507ff101e742ce23e5c9f4db/srtp.png?expires=1781168400&signature=ff5b51f372d754ff364b56069fbec8d01d0431f58ed1ed9a00c099db5df6960e&req=cCEhFc54m4FaFb4f3HP0gG2OtPOe3dIMHxIPhwWG1eY8jaL8CcDzH8QF5RJw%0AYHk%3D%0A)

Your account will now be secure. When you place a call, you will notice a green closed padlock next to your call profile, showing it's a secure call.

[![Call profile showing "secured" icon sign. ](https://downloads.intercomcdn.com/i/o/416377640/a3f59b1cf61ba83b93d2c6b0/600px-Zoiper5_CallTLS.png?expires=1781168400&signature=648d9fa806ba27d94d0fff0aa70bc808b9ddc426278aa1d44729c8c29caac473&req=cCEhFc55m4VfFb4f3HP0gFufhWGonX3odI%2FilggGMaJn%2FrelO9kKw%2FHsB5qO%0AMLK1aG7JaZWwi%2FCqIg%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/416377640/a3f59b1cf61ba83b93d2c6b0/600px-Zoiper5_CallTLS.png?expires=1781168400&signature=648d9fa806ba27d94d0fff0aa70bc808b9ddc426278aa1d44729c8c29caac473&req=cCEhFc55m4VfFb4f3HP0gFufhWGonX3odI%2FilggGMaJn%2FrelO9kKw%2FHsB5qO%0AMLK1aG7JaZWwi%2FCqIg%3D%3D%0A)

That's it, you've now completed the configuration of your Zoiper 5 (free version) softphone client and can now make and receive calls by using Telnyx as the SIP provider.

[Back to Top](#h_4ff34ebbdc)

## 5. Setting up a Caller ID

At Telnyx we have a very strict caller ID policy. Most softphones do not have a direct way to setup what is sent in the FROM header, sometimes you can setup a number as the Display NAME variable and that will be used as the caller id. In any case, you need to make sure your softphone is sending a valid caller id correctly formatted per our policies found [here](https://support.telnyx.com/en/articles/3546251-caller-id-number-policy?q=verified+#h_986dcc6763) and the number you're using is either a number you have in your account with Telnyx or it's a number that has been previously verified with Telnyx. Instructions on how to verify a number can be found [here](https://support.telnyx.com/en/articles/6988813-verified-numbers).

If you are still getting a 403 error about an invalid caller id after setting up a valid caller id in your softphone, the most usual issue is your softphone or system is not correctly passing the caller ID in one of the headers required. As a workaround you will need to setup a caller ID override in the outbound section of your sip connection settings. You can find the instructions in the caller id policy article [here](https://support.telnyx.com/en/articles/3546251-caller-id-number-policy?q=verified+#h_986dcc6763).

[Back to Top](#h_4ff34ebbdc)

---

## Additional Resources

Review our [getting started guide](https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account) to make sure your Telnyx Mission Control Portal account is set up correctly.

Check out the [Zoiper 5](https://www.zoiper.com/pdf/User%20Guide%20Zoiper%205%20v.1.0.7.pdf) user guide.

---

Related Articles

[Configuring Linphone with Telnyx](https://support.telnyx.com/en/articles/1130674-configuring-linphone-with-telnyx)[Zoiper 3: Telnyx Setup (Mac)](https://support.telnyx.com/en/articles/5720999-zoiper-3-telnyx-setup-mac)[Zoiper 3: Telnyx Setup (Linux)](https://support.telnyx.com/en/articles/5721766-zoiper-3-telnyx-setup-linux)[MicroSIP: Setup with Telnyx](https://support.telnyx.com/en/articles/6133145-microsip-setup-with-telnyx)[Zoiper Communicator](https://support.telnyx.com/en/articles/6133517-zoiper-communicator)

Did this answer your question?

😞😐😃

Table of contents
