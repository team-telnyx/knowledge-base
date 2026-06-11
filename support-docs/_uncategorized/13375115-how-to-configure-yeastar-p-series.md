---
source_url: https://support.telnyx.com/en/articles/13375115-how-to-configure-yeastar-p-series
scraped: 2026-06-11
---

How to configure Yeastar P-series | Telnyx Help Center

[Skip to main content](#main-content)

# How to configure Yeastar P-series

Learn how to configure both a Yeastar P-Series IP or Credentials trunk to work with your Telnyx Mission Control Portal.

Written by Cameron Fitzpatrick

January 13, 2026

Table of contents

There are two types of SIP trunks you can configure:

* A VoIP Register Trunk: Uses a credentials based authentication
* A VoIP Peer Trunk: Uses an IP address and PBX port based authentication

In this article we will:

1. [Set up a sip registration based trunk](#h_47c29b1298)
2. [Set up a peer/IP authentication trunk](#h_f620eb1582)
3. [Set up outgoing calls](#h_02ab83b3b2)
4. [Set up incoming calls](#h_0dae3ac15a)

​**Additional documentation**  
​

* **Yeastar Cloud PBX(PCE):**   
  ​[PBX server administrator guide](https://help.yeastar.com/en/p-series-cloud-edition/administrator-guide/about-this-guide.html)

  [Linkus server administrator guide](https://help.yeastar.com/en/p-series-linkus-cloud-edition/linkus-server-admin-guide/linkus-overview.html)  
  ​
* **Yeastar P-Series Self-hosted PBX(PSE):**  
  ​[Installation guide](https://help.yeastar.com/en/p-series-software-edition/software-installation-guide/about-this-guide.html)

  [PBX server administrator guide](https://help.yeastar.com/en/p-series-software-edition/administrator-guide/about-this-guide.html)

### **Pre-Requisites:**

* Have an active, and properly configured, Telnyx Mission Control Portal.
* Review our [getting started guide](https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account) to make sure your Telnyx Mission Control Portal account is set up correctly.  
  ​
* Have DIDs in your Mission Control Portal ready to use.  
  ​
* Install Yeastar PBX and work through the first 3 sub-sections of the Yeastar Getting Started Guide.   
  ​
* When you reach the Set up VoIP trunks section, return here and begin at step 1 below for a Telnyx-specific configuration.

## Set up a SIP registration based trunk

In this step, you'll add a peer SIP trunk in your Yeastar PBX.

Note: A register trunk uses a username/password combination (credentials) to authenticate.

1. **Add a SIP Trunk in P-Series PBX System**  
   After you get the SIP trunk account, you need to add a SIP trunk in Yeastar P-Series PBX System. Go to Extension and Trunk > Trunk, click Add.  
   ​

   [![](https://downloads.intercomcdn.com/i/o/ltcafuzd/1936301773/415a3c00870d574bde19c2edb93f/2ae6542a-aad8-492d-aa05-5f9f9cd8d37e?expires=1781167500&signature=d8264d68281c3cc3eae3650c620e2db25a9a1f77d28d15adc391d92f4ef0ed41&req=dSkkEMp%2BnIZYWvMW1HO4zcdIst3FQsXKvfW8lNtKIE4PPkZ1WRBsu7e%2BwCwV%0AqKAd%0A)](https://downloads.intercomcdn.com/i/o/ltcafuzd/1936301773/415a3c00870d574bde19c2edb93f/2ae6542a-aad8-492d-aa05-5f9f9cd8d37e?expires=1781167500&signature=d8264d68281c3cc3eae3650c620e2db25a9a1f77d28d15adc391d92f4ef0ed41&req=dSkkEMp%2BnIZYWvMW1HO4zcdIst3FQsXKvfW8lNtKIE4PPkZ1WRBsu7e%2BwCwV%0AqKAd%0A)

   ​
2. **Configure the trunk**  
   ​

   Basic Configuration:  
   ​  
   - Name: Enter a name for the SIP trunk to help you identify   
   ​  
   - Telnyx is a Yeastar certified SIP trunk provider, so you can select "Select ITSP Template" from the drop-down list first and choose the countru of the ITSP. Then select the Telnyx "ITSP" name in the right box. All of the parameters are embedded except the account registration information  
   ​  
   - Make sure the trunk status is "Enabled"  
   ​

   [![](https://downloads.intercomcdn.com/i/o/ltcafuzd/1936310443/b4ebed8a893a9ba05b94fdf1d892/57fa81d7-e14e-4b33-a85d-e6b84ae06477?expires=1781167500&signature=3b387708ff0329bcb3f3d58c3d112017594ba633d72f6bb110b67b7c8a5f016b&req=dSkkEMp%2FnYVbWvMW1HO4zZg%2BR%2BqPum8LPxPmnuinCevB9KlPlrOEg%2Fzhjd2k%0AJ7Mk%0A)](https://downloads.intercomcdn.com/i/o/ltcafuzd/1936310443/b4ebed8a893a9ba05b94fdf1d892/57fa81d7-e14e-4b33-a85d-e6b84ae06477?expires=1781167500&signature=3b387708ff0329bcb3f3d58c3d112017594ba633d72f6bb110b67b7c8a5f016b&req=dSkkEMp%2FnYVbWvMW1HO4zZg%2BR%2BqPum8LPxPmnuinCevB9KlPlrOEg%2Fzhjd2k%0AJ7Mk%0A)

   Detailed Configuration:  
   ​  
   The parameters of the certified ITSP template are embedded. You don’t have to figure out Trunk Type, Transport, Hostname, Port, Domain.  
   ​  
   However, if you need to change it you can refer to <https://sip.telnyx.com/> for information of Telnyx proxies, transport or port.

* Username: your Telnyx username.
* Password: your Telnyx password.
* Authentication Name: the same as the username.
* Enable Outbound Proxy: the same as hostname

[![](https://downloads.intercomcdn.com/i/o/ltcafuzd/1936312460/923bf3b0639f837e7bc49dc6560c/6494d707-4721-4ce9-88be-3987e1f7ccbf?expires=1781167500&signature=c7ed14200b3a6f18f81e63d867f9472e486b999bed8c595c3b8f3501e38af5bf&req=dSkkEMp%2Fn4VZWfMW1HO4zVQ2cHoBG7EJMILI%2FlDmE7CTEhNNMV9nCJPCAWz9%0AODKyVbPPtoBCWD9tCmY%3D%0A)](https://downloads.intercomcdn.com/i/o/ltcafuzd/1936312460/923bf3b0639f837e7bc49dc6560c/6494d707-4721-4ce9-88be-3987e1f7ccbf?expires=1781167500&signature=c7ed14200b3a6f18f81e63d867f9472e486b999bed8c595c3b8f3501e38af5bf&req=dSkkEMp%2Fn4VZWfMW1HO4zVQ2cHoBG7EJMILI%2FlDmE7CTEhNNMV9nCJPCAWz9%0AODKyVbPPtoBCWD9tCmY%3D%0A)

3. **Check the Trunk status**

Click Save and Apply. Check if the trunk is conneced in Status, indicated by the checkmark.   
asic Configuration:  
​  
- Name: Enter a name for the SIP trunk to help you identify   
​  
- Telnyx is a Yeastar certified SIP trunk provider, so you can select "Select ITSP Template" from the drop-down list first and choose the country of the ITSP. Then select the Telnyx "ITSP" name in the right box. All of the parameters are embedded except the account registration information  
​  
- Make sure the trunk status is "Enabled"

[![](https://downloads.intercomcdn.com/i/o/ltcafuzd/1936310443/b4ebed8a893a9ba05b94fdf1d892/57fa81d7-e14e-4b33-a85d-e6b84ae06477?expires=1781167500&signature=3b387708ff0329bcb3f3d58c3d112017594ba633d72f6bb110b67b7c8a5f016b&req=dSkkEMp%2FnYVbWvMW1HO4zZg%2BR%2BqPum8LPxPmhOyhANFpepJKpUltFMqLh1AZ%0AtzZG8RxYjWVOkBDaxUs%3D%0A)](https://downloads.intercomcdn.com/i/o/ltcafuzd/1936310443/b4ebed8a893a9ba05b94fdf1d892/57fa81d7-e14e-4b33-a85d-e6b84ae06477?expires=1781167500&signature=3b387708ff0329bcb3f3d58c3d112017594ba633d72f6bb110b67b7c8a5f016b&req=dSkkEMp%2FnYVbWvMW1HO4zZg%2BR%2BqPum8LPxPmhOyhANFpepJKpUltFMqLh1AZ%0AtzZG8RxYjWVOkBDaxUs%3D%0A)

## **Set up a Peer/IP authentication trunk**

In this step, you'll add a peer SIP trunk into your Yeastar PBX. A peer trunk uses IP authentication.

1. Login to the PBX web portal, go to Extension and Trunk > Trunk, click Add.  
   ​
2. In the Basic section, configure the following settings:  
   ​**Name:** Enter a name to help you identify the trunk.  
   ​**Trunk Status:** Select Enabled  
   ​**Select ITSP Template:** Select General  
   ​

In the Detailed Configuration section, select the trunk type and enter the SIP information that is provided by the ITSP.  
​  
​**Trunk Type:** Peer Trunk (Port Based)

The Static IP Address and Port of the PBX will be displayed on the web page. This needs to be added in the Telnyx Mission control portal under SIP Trunking> Edit the IP type connection> Authentication and routing> IP addresses.

**Transport:** UDP/ TCP/ TLS.

**Hostname/IP:** Enter the Telnyx domain name or IP address

**Port:** Enter the Telnyx SIP port.

**Domain:** Enter the domain in SIP URI of a specific header like From, To header same as Hostname/IP field.

​

[![](https://downloads.intercomcdn.com/i/o/ltcafuzd/1936335577/7fee7a096b089939424aefe87f87/2caefd40-fa14-4187-b22f-47c9a8595e7b?expires=1781167500&signature=aed0aa89d8be73b60ec1c1624dcb4f85b033f5a4941a3eb806068ffb8123b628&req=dSkkEMp9mIRYXvMW1HO4zTpq6IJoDtsKHUDvUQSdawb7s7fooKfalo9xl%2Bd3%0AXWkTdueIgKgzIkCO%2FmI%3D%0A)](https://downloads.intercomcdn.com/i/o/ltcafuzd/1936335577/7fee7a096b089939424aefe87f87/2caefd40-fa14-4187-b22f-47c9a8595e7b?expires=1781167500&signature=aed0aa89d8be73b60ec1c1624dcb4f85b033f5a4941a3eb806068ffb8123b628&req=dSkkEMp9mIRYXvMW1HO4zTpq6IJoDtsKHUDvUQSdawb7s7fooKfalo9xl%2Bd3%0AXWkTdueIgKgzIkCO%2FmI%3D%0A)

## **Set up Outgoing Calls**

To make outbound calls via the newly created SIP trunk, you need to configure an outbound route for the trunk.

1. **Create an Outbound Route**  
   Go to Call Control > Outbound Route, click Add.

   [![](https://downloads.intercomcdn.com/i/o/ltcafuzd/1936338491/1bad529c3e29ad72e74146c27523/27303bc0-f6de-4292-a3d5-d250b66e02f5?expires=1781167500&signature=7dd2de3fca9524cf883cba86999bd5ed062c76344324e06583cd034a7fd22321&req=dSkkEMp9lYVWWPMW1HO4zZJm11Ej3seon50BipR718L8CJGsx6PC%2Fzgsv9%2FY%0A%2ByvH%0A)](https://downloads.intercomcdn.com/i/o/ltcafuzd/1936338491/1bad529c3e29ad72e74146c27523/27303bc0-f6de-4292-a3d5-d250b66e02f5?expires=1781167500&signature=7dd2de3fca9524cf883cba86999bd5ed062c76344324e06583cd034a7fd22321&req=dSkkEMp9lYVWWPMW1HO4zZJm11Ej3seon50BipR718L8CJGsx6PC%2Fzgsv9%2FY%0A%2ByvH%0A)
2. **Configure the Outbound Route**

The system compares the number with the pattern that you have defined in your route 1. If it matches, it will initiate the call using the selected trunks. If it does not, it will compare the number with the pattern you have defined in route 2 and so on. The outbound route which is in a higher position will be matched firstly.

You can adjust the outbound route sequence by clicking these buttons:

[![](https://downloads.intercomcdn.com/i/o/ltcafuzd/1936337262/f03a8a4b98f9ac65bc2ad868929b/26cab2e9-5f59-4c74-8a48-bf23ce46691a?expires=1781167500&signature=f55873fce834b7ea738c0f258ccb85adb6a7c1a830e787f7a580ecbb4567bef8&req=dSkkEMp9moNZW%2FMW1HO4zV1M1RBsiWslcEDnYzvgag8cyxhRBOuwX4R9e2IS%0ACBlYjSlofLRrblJ51%2F0%3D%0A)](https://downloads.intercomcdn.com/i/o/ltcafuzd/1936337262/f03a8a4b98f9ac65bc2ad868929b/26cab2e9-5f59-4c74-8a48-bf23ce46691a?expires=1781167500&signature=f55873fce834b7ea738c0f258ccb85adb6a7c1a830e787f7a580ecbb4567bef8&req=dSkkEMp9moNZW%2FMW1HO4zV1M1RBsiWslcEDnYzvgag8cyxhRBOuwX4R9e2IS%0ACBlYjSlofLRrblJ51%2F0%3D%0A)

* **Name:** give this outbound route a name to help you identify it.  
  ​
* **Role:** select the role that can use this outbound route to make outbound calls.  
  ​
* **Dial Patterns:** set the dial patterns. As the settings below, to make calls via the SIP trunk, you need to precede the number to be dialed with the prefix 8.  
  ​
* **Dial Pattern:** 8.  
  ​
* **Strip:** 1  
  ​
* **Trunk:** select the Telnyx SIP trunk.  
  ​
* **Outbound Route Password:** you can prompt users for a password before allowing calls to progress.  
  ​
* **Extension/Extension Group:** select the extensions or extension groups that are allowed to make calls through the outbound route.  
  ​
* **Time condition:** select time condition to allow this outbound route.

[![](https://downloads.intercomcdn.com/i/o/ltcafuzd/1936365981/bdca641f2edc0300480e7771b4e8/132c210e-3108-434b-a103-42307d902787?expires=1781167500&signature=b28d8ad093c98265b5494d7f8b3a7938297cffbac0afaee7a17f31e9a41687ce&req=dSkkEMp4mIhXWPMW1HO4zd1Bmf8pmS2RHuT8PyFq61APboXnSf7%2BtGGUrYr%2F%0AS2uXmhGBrFHYuZylNyQ%3D%0A)](https://downloads.intercomcdn.com/i/o/ltcafuzd/1936365981/bdca641f2edc0300480e7771b4e8/132c210e-3108-434b-a103-42307d902787?expires=1781167500&signature=b28d8ad093c98265b5494d7f8b3a7938297cffbac0afaee7a17f31e9a41687ce&req=dSkkEMp4mIhXWPMW1HO4zd1Bmf8pmS2RHuT8PyFq61APboXnSf7%2BtGGUrYr%2F%0AS2uXmhGBrFHYuZylNyQ%3D%0A)

​

**3. Click Save and Apply**

Now you can make outbound calls through the SIP trunk. As the dial patterns configured above, you need to dial “8” before the destination number.

For example, to call the number “01234567”, you need to dial “801234567” on your phone.

## **Set up incoming calls**

In this step, you'll get Yeastar ready to take incoming calls by configuring an inbound route for the SIP trunk.

1. **Create an Inbound Route**  
   Go to Call Control > Inbound Route, click Add.

   [![](https://downloads.intercomcdn.com/i/o/ltcafuzd/1936344352/c4590187916185145c407decede4/8c73c964-e974-4ba7-bf01-8d581309a79f?expires=1781167500&signature=945ccb4cbc8695a9515c92d6fa07ff077a8b7a45471949b3c2ff176d5319eebe&req=dSkkEMp6mYJaW%2FMW1HO4zSLrWY2O23Pd3RDKx7Y4H6R2hgpjvkkqhbVF6svP%0AQDp1%0A)](https://downloads.intercomcdn.com/i/o/ltcafuzd/1936344352/c4590187916185145c407decede4/8c73c964-e974-4ba7-bf01-8d581309a79f?expires=1781167500&signature=945ccb4cbc8695a9515c92d6fa07ff077a8b7a45471949b3c2ff176d5319eebe&req=dSkkEMp6mYJaW%2FMW1HO4zSLrWY2O23Pd3RDKx7Y4H6R2hgpjvkkqhbVF6svP%0AQDp1%0A)
2. **Configure the Inbound Route**

[![](https://downloads.intercomcdn.com/i/o/ltcafuzd/1936343003/0d4fd6e4e60622c7e862af013799/55795967-2bbf-4608-a3cc-dd83253d3ae2?expires=1781167500&signature=587cf791a3b7c24c4327cd7a3de67e0cc477632ca1ac109f0f8d0b611e9bcb59&req=dSkkEMp6noFfWvMW1HO4zQqTNWpNxYofRSDj%2F6nGzjcfBIl8eEUo07v0L3rM%0AV0HsZ97tvGzYhT8ndn4%3D%0A)](https://downloads.intercomcdn.com/i/o/ltcafuzd/1936343003/0d4fd6e4e60622c7e862af013799/55795967-2bbf-4608-a3cc-dd83253d3ae2?expires=1781167500&signature=587cf791a3b7c24c4327cd7a3de67e0cc477632ca1ac109f0f8d0b611e9bcb59&req=dSkkEMp6noFfWvMW1HO4zQqTNWpNxYofRSDj%2F6nGzjcfBIl8eEUo07v0L3rM%0AV0HsZ97tvGzYhT8ndn4%3D%0A)

* **Name:** give this inbound route a name to help you identify it.  
  ​
* **DID Pattern:** specify the did pattern to match and pass the incoming call through this inbound route.  
  ​
* **Caller ID Pattern:** define the caller ID number that is allowed to call through this inbound route.  
  ​
* **Trunk:** choose the Telnyx SIP trunk.  
  ​
* **Default Destination:** select the default destination or set with Time Condition.

**3. Click Save and Apply**

When you call in the SIP trunk, the call will be routed to the destination configured on the inbound route.

You have now set up your SIP trunk in Yeastar PBX and configured it to work with Telnyx.

---

Related Articles

[Configuring an Elastix 4 PBX IP Trunk](https://support.telnyx.com/en/articles/1130622-configuring-an-elastix-4-pbx-ip-trunk)[Configuring a FreePBX V13 Credentials Trunk](https://support.telnyx.com/en/articles/1130648-configuring-a-freepbx-v13-credentials-trunk)[Configuring an Elastix 4 PBX Trunk](https://support.telnyx.com/en/articles/1130654-configuring-an-elastix-4-pbx-trunk)[Yeastar S-Series: Telnyx SIP](https://support.telnyx.com/en/articles/5748952-yeastar-s-series-telnyx-sip)[Xorcom PBX: SIP Trunk](https://support.telnyx.com/en/articles/5754127-xorcom-pbx-sip-trunk)

Did this answer your question?

😞😐😃

Table of contents
