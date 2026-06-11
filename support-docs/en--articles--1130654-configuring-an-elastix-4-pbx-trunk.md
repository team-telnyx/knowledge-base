---
source_url: https://support.telnyx.com/en/articles/1130654-configuring-an-elastix-4-pbx-trunk
scraped: 2026-06-11
---

Configuring an Elastix 4 PBX Trunk | Telnyx Help Center

[Skip to main content](#main-content)

# Configuring an Elastix 4 PBX Trunk

In this article we will explain how to configure an Elastix 4 PBX Credentials Trunk with Telnyx.

C

Written by Customer Success

October 18, 2023

Table of contents

[Jump to Instructions](#h_4c1a32624c)

With [Elastix](https://www.3cx.com/) you can build the ideal PBX for your business whatever its size or requirements; you choose how to deploy depending on what you and your business needs from its communications platform. Whether you want an on-premise Linux PBX, to install on Windows, or you prefer to self host your phone system in YOUR cloud with your own cloud account, the choice is yours.

Additional documentation:

* [Elastix admin guide](https://www.3cx.com/docs/manual/)
* [Elastix user guide](https://www.3cx.com/user-manual/)
* [Elastix support](https://www.3cx.com/support/)

---

# Instructions for Configuring Elastix

In this activity you will:

1. [Install Elastix 4](#h_80adb3f251)
2. [Create a Telnyx SIP trunk](https://support.telnyx.com/en/articles/3284164-elastix-5-credentials-trunk#h_7ee5612075)
3. [Create inbound rules](https://support.telnyx.com/en/articles/3284164-elastix-5-credentials-trunk#h_165e1f85b4)
4. [Create outbound rules](https://support.telnyx.com/en/articles/3284164-elastix-5-credentials-trunk#h_35f616006a)

**Pre-requisites**

* Ensure that your [Telnyx Mission Command Portal is configured properly](https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account)
* [Purchase a DID](https://portal.telnyx.com/#/app/numbers/search-numbers)
* [Set up your Telnyx SIP connection](https://portal.telnyx.com/#/app/connections)
* [Provision your number](https://portal.telnyx.com/#/app/numbers/my-numbers) (Assign it to a SIP connection)
* [Create an outbound voice profile](https://portal.telnyx.com/#/app/outbound)
* Create a [credentials-based connection](https://portal.telnyx.com/#/app/connections) on your Telnyx Mission Control Portal
* RECOMMENDED: [Enable TLS to encrypt your traffic](https://support.telnyx.com/en/articles/1130711-does-telnyx-encrypt-communication)
* Download Elastix 4 ISO from [our dropbox.](https://www.dropbox.com/sh/rzrdrpu0ocumu95/AABJeNgKkOkDCYLkSrsIuD3Aa?dl=0) (V4 is no longer available through the provider)

  + Take note of any username/password combination you set during this activity. You'll need them at a later stage.

**Video walkthrough**

Setting up your Telnyx SIP portal account so you can make and receive calls:

Configuring Elastix 4

## 1. Install Elastix 4

As the provider no longer supports Elastix, we will provide you with an installation guide.

1. Run the Elastix installer.

   [![Elastix 4 installer page. ](https://downloads.intercomcdn.com/i/o/143526765/7dce85eb3f454cf58be3719e/elastix1.png?expires=1781167500&signature=72882bc77e998dcd9f78cb0eab8f47043551c562eeaf21e114dc5ee633145961&req=dSQkE8t4modaFb4f3HP0gDSBhZ27%2BCK73D6K%2F1%2FKgAK60nXBKL%2B%2FRsVyRsx6%0Aeog%3D%0A)](https://downloads.intercomcdn.com/i/o/143526765/7dce85eb3f454cf58be3719e/elastix1.png?expires=1781167500&signature=72882bc77e998dcd9f78cb0eab8f47043551c562eeaf21e114dc5ee633145961&req=dSQkE8t4modaFb4f3HP0gDSBhZ27%2BCK73D6K%2F1%2FKgAK60nXBKL%2B%2FRsVyRsx6%0Aeog%3D%0A)
2. Once you reach the Centos installation summary, provide the following information:

   1. **Date and Time** according to your time zone
   2. **Install Destination** (Select the Hard drive we created for this virtual machine)
   3. **Keyboard**
   4. **Network and Hostname** - make sure to turn this *on***.**

      [![Centos installation summary page. ](https://downloads.intercomcdn.com/i/o/143526831/4f304357799c72d5c4891b7b/elastix2.png?expires=1781167500&signature=38dfe467f843c07350a6dd9827c82de69153248578efbe519269ea5f9107ca58&req=dSQkE8t4lYJeFb4f3HP0gKA3IpVTekn0nGrot9LLY10SyvKOMeuYzmrvvN7%2F%0AqKQ%3D%0A)](https://downloads.intercomcdn.com/i/o/143526831/4f304357799c72d5c4891b7b/elastix2.png?expires=1781167500&signature=38dfe467f843c07350a6dd9827c82de69153248578efbe519269ea5f9107ca58&req=dSQkE8t4lYJeFb4f3HP0gKA3IpVTekn0nGrot9LLY10SyvKOMeuYzmrvvN7%2F%0AqKQ%3D%0A)
3. Once you've entered the appropriate configuration settings, click **Begin Installation** at the bottom.
4. You'll then be prompted to configure the user settings.

   [![Centos installation page for user settings. ](https://downloads.intercomcdn.com/i/o/143526974/46a9bd3ff6b59bc2dfe65f13/elastix3.png?expires=1781167500&signature=1ac0a08f20d3d903bd51b3c25306721a9b9684e8bde9eb132a366223b1112fd5&req=dSQkE8t4lIZbFb4f3HP0gE%2BWT%2F5T5ay7JMGIuJCTI2XXT6X3hSk09ANHrbRv%0Ao0U%3D%0A)](https://downloads.intercomcdn.com/i/o/143526974/46a9bd3ff6b59bc2dfe65f13/elastix3.png?expires=1781167500&signature=1ac0a08f20d3d903bd51b3c25306721a9b9684e8bde9eb132a366223b1112fd5&req=dSQkE8t4lIZbFb4f3HP0gE%2BWT%2F5T5ay7JMGIuJCTI2XXT6X3hSk09ANHrbRv%0Ao0U%3D%0A)
5. Make sure you enter a root password and create a user. You will need these for later on so please remember them.
6. While you complete these two options, the installation will continue as normal until it finishes.
7. Now enter your SQL root password and admin password which are used to login to the graphical user interface.

   [![SQL Administration credentials page. ](https://downloads.intercomcdn.com/i/o/143527396/1a1813a685f80e47424491bb/elastix4.png?expires=1781167500&signature=619b6b702c56a1840e3e2d122ace987c6347cb5a9a528ef113551f31b0cb8492&req=dSQkE8t5nohZFb4f3HP0gEFijur7a%2BjNK4yqtwhdVpi%2B8VU%2F24DJ6enThUnv%0A2z4%3D%0A)](https://downloads.intercomcdn.com/i/o/143527396/1a1813a685f80e47424491bb/elastix4.png?expires=1781167500&signature=619b6b702c56a1840e3e2d122ace987c6347cb5a9a528ef113551f31b0cb8492&req=dSQkE8t5nohZFb4f3HP0gEFijur7a%2BjNK4yqtwhdVpi%2B8VU%2F24DJ6enThUnv%0A2z4%3D%0A)

   [![SQL Administration credentials page 2. ](https://downloads.intercomcdn.com/i/o/143527412/124b50759784581e6d43b590/elastix5.png?expires=1781167500&signature=5c0450cde7fe93297d684acabaa6764a954083c44e2619a065cd1cb3a9d69fa6&req=dSQkE8t5mYBdFb4f3HP0gNXoVYQMOonuZO%2BqY4nAYQmx%2B79X9q72SzXFkzFz%0AAlg%3D%0A)](https://downloads.intercomcdn.com/i/o/143527412/124b50759784581e6d43b590/elastix5.png?expires=1781167500&signature=5c0450cde7fe93297d684acabaa6764a954083c44e2619a065cd1cb3a9d69fa6&req=dSQkE8t5mYBdFb4f3HP0gNXoVYQMOonuZO%2BqY4nAYQmx%2B79X9q72SzXFkzFz%0AAlg%3D%0A)
8. Now your virtual machine will reboot and you should now be able to login as root and Web GUI admin.

   [![Web GUI Admin page. ](https://downloads.intercomcdn.com/i/o/143527526/2b8ee6046cc86942b455a8c5/elastix6.png?expires=1781167500&signature=49f77eecaac305c63c1a29cf01864cb88a91c9723871c9cbf90e739dc3939a7e&req=dSQkE8t5mINZFb4f3HP0gCpRH%2BdMu%2BZrJLhj5NB2PlrPGJR6q6IhgSCZf6ot%0A790%3D%0A)](https://downloads.intercomcdn.com/i/o/143527526/2b8ee6046cc86942b455a8c5/elastix6.png?expires=1781167500&signature=49f77eecaac305c63c1a29cf01864cb88a91c9723871c9cbf90e739dc3939a7e&req=dSQkE8t5mINZFb4f3HP0gCpRH%2BdMu%2BZrJLhj5NB2PlrPGJR6q6IhgSCZf6ot%0A790%3D%0A)
9. To access your Elastix system, copy the URL which is displayed for you in the above picture. Input this URL into your browser to access the GUI.

   [![GUI credentials submission page. ](https://downloads.intercomcdn.com/i/o/143527634/571b0dba9ffeed48f80c90f9/elastix8.png?expires=1781167500&signature=5dbdbc634bee4b704a6c62c5869fe1c08184974ed1aaac750c754853351cf6c6&req=dSQkE8t5m4JbFb4f3HP0gP8z4xuSduNdtcVoIUMQJn%2Flqxnu%2B9B0GcgKuuUN%0AWd0%3D%0A)](https://downloads.intercomcdn.com/i/o/143527634/571b0dba9ffeed48f80c90f9/elastix8.png?expires=1781167500&signature=5dbdbc634bee4b704a6c62c5869fe1c08184974ed1aaac750c754853351cf6c6&req=dSQkE8t5m4JbFb4f3HP0gP8z4xuSduNdtcVoIUMQJn%2Flqxnu%2B9B0GcgKuuUN%0AWd0%3D%0A)
10. Once you enter your username and password, you'll be brought to the Elastix system.

[Back to Top](#h_4c1a32624c)

## 2. Add a SIP trunk

In this section, you'll configure your Elastix 4 PBX to work with Telnyx. You can follow these steps, or use the [video walkthrough](#h_9f0dbb7c3d).

1. Log into your Elastix GUI. You'll be on the homepage.

   [![Elastic GUI homepage. ](https://downloads.intercomcdn.com/i/o/143528080/0cc0e902a0bf88b7898f2077/elastix9.png?expires=1781167500&signature=623f502b764b8b39268666b33102e327fa8f84982a4309a0a7063943cdfe32c2&req=dSQkE8t2nYlfFb4f3HP0gKb1DE04eRoMWIdbjmgvG9fLaoFlrJDQJIifeqQ1%0AcgA%3D%0A)](https://downloads.intercomcdn.com/i/o/143528080/0cc0e902a0bf88b7898f2077/elastix9.png?expires=1781167500&signature=623f502b764b8b39268666b33102e327fa8f84982a4309a0a7063943cdfe32c2&req=dSQkE8t2nYlfFb4f3HP0gKb1DE04eRoMWIdbjmgvG9fLaoFlrJDQJIifeqQ1%0AcgA%3D%0A)
2. From the left-hand navigation, go to **PBX > Tools > Asterisk File Editor** and filter for the *sip\_nat.conf* file.
3. Enter in your own local network subnet and your external IP in the fields labeled:

   1. localnet=
   2. externip=
4. Click **Save** and then click **Reload Asterisk.**

   [![Asterisk file and reload page. ](https://downloads.intercomcdn.com/i/o/143528924/f87a698761725dc0399a33dc/elastix10.png?expires=1781167500&signature=9de4e7c748f8faf90dadb2d825da36ff633af8d4f90a93635f84b4ccf002a383&req=dSQkE8t2lINbFb4f3HP0gBlm1%2F1jePQqu9HQZ3IeOubwr6Jj2hI7go%2Fwi3G%2B%0A8RI%3D%0A)](https://downloads.intercomcdn.com/i/o/143528924/f87a698761725dc0399a33dc/elastix10.png?expires=1781167500&signature=9de4e7c748f8faf90dadb2d825da36ff633af8d4f90a93635f84b4ccf002a383&req=dSQkE8t2lINbFb4f3HP0gBlm1%2F1jePQqu9HQZ3IeOubwr6Jj2hI7go%2Fwi3G%2B%0A8RI%3D%0A)
5. Now make your way to **PBX > PBX Configurations > Extensions > Add SIP Extension** and enter the following information. Anything not specified can be left blank unless it's a requirement of yours.

   1. **User Extension:** The extension you wish to use for this trunk
   2. **Display Name:** Enter a name that makes sense.
   3. **Outbound CID:** The [number](https://portal.telnyx.com/#/app/numbers/my-numbers) you purchased with Telnyx that you want to assign for this extension. Please remember to use the user extension and password along with the internal IP of your Elastix server so you can then register this SIP extension.
   4. **Asterisk Dial Options:** *tr*
   5. **Queue State Detection:** *Use state*
   6. **Secret:** Your Telnyx account password for this extension
   7. **DTMFmode:** *RFC 2833*
   8. **NAT:** *No- RFC 3581*

      [![Page for adding SIP extension. ](https://downloads.intercomcdn.com/i/o/143529456/9df664b71af5933e8eec96ca/elastix11.png?expires=1781167500&signature=eeea1a58a8e0882b582df8a0cfb156e4d3d56dbae50e319bcf4ef77ddc5d06ae&req=dSQkE8t3mYRZFb4f3HP0gAG6PwD10Ul%2FVBDZNcIPJ1mlkQlgR9DLSm3NOdXe%0ATE0%3D%0A)](https://downloads.intercomcdn.com/i/o/143529456/9df664b71af5933e8eec96ca/elastix11.png?expires=1781167500&signature=eeea1a58a8e0882b582df8a0cfb156e4d3d56dbae50e319bcf4ef77ddc5d06ae&req=dSQkE8t3mYRZFb4f3HP0gAG6PwD10Ul%2FVBDZNcIPJ1mlkQlgR9DLSm3NOdXe%0ATE0%3D%0A)
6. Click **Submit**, then **Apply Config**.
7. From the left-hand navigation, stay on **PBX > PBX Configurations** and click on **Trunks**.
8. Add the following settings to you trunk details:  
   ​  
   ​**Outgoing SIP Settings for the trunk:**

   1. **Username:** Your Telnyx account username
   2. **Secret:** Your Telnyx account password
   3. **Host:** *sip.telnyx.com*
   4. **Type:** *friend*
   5. **Insecure:** *port, invite*
   6. **Qualify:** *Yes*
   7. **Disallow:** *All*
   8. **Allow:** *ulaw & alaw*

   **Inbound sip Settings for the trunk:**

   1. **Username:** Your Telnyx account username
   2. **Secret:** Your Telnyx account password
   3. **Fromdomain:** *sip.telnyx.com*
   4. **Host:** *sip.telnyx.com*
   5. **Type:** *friend*
   6. **Insecure:** *port,invite*
   7. **Qualify:** *Yes*
   8. **Disallow:** *All*
   9. **Allow:** *ulaw*
   10. **DTMFmode:** *RFC 2833*
   11. **NAT:** *force\_rport,comedia*
   12. **Registration string:** your\_username:your\_password@*sip.telnyx.com*
   13. **Dialed number manipulation rules:** prepend:*1*; match pattern: *NXXNXXXXXX*  
       prepend: blank; match pattern: *1NXXNXXXXXX*  
       ​  
       ​***Note:*** *The above dial patterns are for dialing 10 and 11 digit destinations, your own dial patterns may differ.*

       [![Inbound sip settings page for the trunk.](https://downloads.intercomcdn.com/i/o/143530081/c189fdd9890fed51af281525/elastix12.png?expires=1781167500&signature=72315a6f1b6fee8476d6d39315338069952b307ba45fcbabec7ff9e87591dd7a&req=dSQkE8p%2BnYleFb4f3HP0gIh8j9tlflkRpsDixid0QYF4LJCk%2F%2B3nd892%2BQ23%0AVfQ%3D%0A)](https://downloads.intercomcdn.com/i/o/143530081/c189fdd9890fed51af281525/elastix12.png?expires=1781167500&signature=72315a6f1b6fee8476d6d39315338069952b307ba45fcbabec7ff9e87591dd7a&req=dSQkE8p%2BnYleFb4f3HP0gIh8j9tlflkRpsDixid0QYF4LJCk%2F%2B3nd892%2BQ23%0AVfQ%3D%0A)
9. Click **Submit** and **Apply Config**.

[Back to Top](#h_4c1a32624c)

## 3. Configure outbound rules

In this section, you'll configure the outbound calling rules that will manage your outgoing calls.

1. From the left-hand navigation, make your way to **PBX > PBX Configurations** and click on **Outbound Routes**, then **Add Route** and provide the following information:

   1. **Route Name:** Choose a name that makes your route easily identifiable.
   2. **Route CID:** The [number](https://portal.telnyx.com/#/app/numbers/my-numbers) you purchased with Telnyx that you want to assign to this route.
   3. **Dial Patterns:** Enter your dial patterns here. Use as many as necessary.
   4. **Trunk Sequence:** *Telnyx*
   5. If you require configuration of any additional fields, you can configure these as needed.

      [![Outbound rules configuration portal. ](https://downloads.intercomcdn.com/i/o/143530248/ce343360b72fc86927cefe39/elastix13.png?expires=1781167500&signature=1286d25da22b814e2fc44f6895563626f67ed8932dc18ff67e80ae5abaccb78f&req=dSQkE8p%2Bn4VXFb4f3HP0gEtLZNcww2laFig%2B%2F33SAztGMTBzP0Ghh38lyGw6%0A2vo%3D%0A)](https://downloads.intercomcdn.com/i/o/143530248/ce343360b72fc86927cefe39/elastix13.png?expires=1781167500&signature=1286d25da22b814e2fc44f6895563626f67ed8932dc18ff67e80ae5abaccb78f&req=dSQkE8p%2Bn4VXFb4f3HP0gEtLZNcww2laFig%2B%2F33SAztGMTBzP0Ghh38lyGw6%0A2vo%3D%0A)
2. Click **Submit** and **Apply Config** to configure the trunk settings.

[Back to Top](#h_4c1a32624c)

## 4. Configure inbound rules

In this section, you'll configure the inbound calling rules that will manage your incoming calls.

1. From the left-hand navigation, make your way to **PBX > PBX Configurations** and click on **Inbound Routes**, then **Add Incoming Route** and provide the following information:

   1. **Description:** A description of your route that makes it easily identifiable
   2. **[DID Number](https://telnyx.com/resources/sip-did):** The [number](https://portal.telnyx.com/#/app/numbers/my-numbers) you purchased with Telnyx that you want to assign to handle inbound calls.
   3. **Extensions:** Any extensions that you need to register for your inbound calling.
   4. If you require configuration of any additional fields, you can configure these as needed.

      [![Inbound rules configuration portal.  ](https://downloads.intercomcdn.com/i/o/143530340/fe29f034a24e9c37b8c79391/elastix14.png?expires=1781167500&signature=3aa901286f70c0c6626a962e8b98122436813f2154b678984de153cd3eff9db5&req=dSQkE8p%2BnoVfFb4f3HP0gP%2B0y7q13eMDpgjn%2Bwypdxf%2FAv8I3GrXQuWjd7yC%0AEhs%3D%0A)](https://downloads.intercomcdn.com/i/o/143530340/fe29f034a24e9c37b8c79391/elastix14.png?expires=1781167500&signature=3aa901286f70c0c6626a962e8b98122436813f2154b678984de153cd3eff9db5&req=dSQkE8p%2BnoVfFb4f3HP0gP%2B0y7q13eMDpgjn%2Bwypdxf%2FAv8I3GrXQuWjd7yC%0AEhs%3D%0A)
2. Click **Submit** and **Apply Config.**

That's it, you've now completed the configuration of Elastix 4 IP-PBX Trunk and can now make and receive calls by using Telnyx as your SIP provider!

##

[Back to Top](#h_4c1a32624c)

---

## Additional Resources

Review our [getting started with guide](https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account) to make sure your Telnyx Mission Control Portal account is set up correctly.

Additionally, you can check out:

* [Elastix admin guide](https://www.3cx.com/docs/manual/)
* [Elastix user guide](https://www.3cx.com/user-manual/)
* [Elastix support](https://www.3cx.com/support/)

---

Related Articles

[Configuring an Elastix 4 PBX IP Trunk](https://support.telnyx.com/en/articles/1130622-configuring-an-elastix-4-pbx-ip-trunk)[How to configure a Thirdlane PBX](https://support.telnyx.com/en/articles/1130631-how-to-configure-a-thirdlane-pbx)[Configuring a FreePBX V13 Credentials Trunk](https://support.telnyx.com/en/articles/1130648-configuring-a-freepbx-v13-credentials-trunk)[Xorcom PBX: SIP Trunk](https://support.telnyx.com/en/articles/5754127-xorcom-pbx-sip-trunk)[How to configure Yeastar P-series](https://support.telnyx.com/en/articles/13375115-how-to-configure-yeastar-p-series)

Did this answer your question?

😞😐😃

Table of contents
