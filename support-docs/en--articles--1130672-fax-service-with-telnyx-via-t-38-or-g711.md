---
source_url: https://support.telnyx.com/en/articles/1130672-fax-service-with-telnyx-via-t-38-or-g711
scraped: 2026-06-11
---

Fax service with Telnyx (via T.38 or G711) | Telnyx Help Center

[Skip to main content](#main-content)

# Fax service with Telnyx (via T.38 or G711)

Learn more about setting up fax service with Telnyx using either T.38 or g711.

Written by Telnyx Sales

June 6, 2024

Table of contents

Setting up Fax on [Telnyx Mission Control](https://portal.telnyx.com) portal can be done with just a few clicks.

# Setting up Outbound Fax

### **Create a SIP Connection**

1. Visit the SIP Connections page via the navigation menu on the left
2. Click the Add SIP Connection button near the top right
3. Select your authentication method (User/Pass or IP Address) and input your information
4. Click CREATE

### **Create an Outbound Profile**

1. Visit the OUTBOUND page via the navigation menu on the left
2. Click the +ADD OUTBOUND PROFILE button near the top right
3. Give the OUTBOUND PROFILE a name
4. Select the connection you'd like to use for Fax traffic via the connection drop-down
5. Click ADD

**You are now all setup** for Outbound Fax with Telnyx. By default, Telnyx will send a T38 re-INVITE message once FAX tone is detected. If you wish to change this behavior, edit your connection by clicking on Outbound and clicking on the menu for "T.38 Re-invite Initiated By" a) Telnyx (Default), b) Customer or c) Disabled (enables G711 FAX calls)

## Setting up Inbound Fax

### **Create a SIP Connection**

1. Visit the CONNECTIONS page via the navigation menu on the left
2. Click the ADD CONNECTION button near the top right
3. Select your authentication method (User/Pass or IP Address) and input your information
4. Click CREATE

### **Purchase a number**

1. Visit the NUMBERS page via the navigation menu on the left
2. Go to the SEARCH NUMBERS tab and submit a search
3. There are multiple "Search Types" available that will enable you to search by Region, Are Code, Prefix, and more.Click +ADD TO CART to select the number(s) you would like and add it to your shopping cartClick on the Shopping Cart button on the right side of the page and checkout to purchase your number(s)

### **Assign a SIP Connection**

1. Visit the NUMBERS page via the navigation menu on the left
2. Go to the MY NUMBERS tab. You should see your purchased number listed
3. Click the Connection drop-down next to the number you'd like to use for fax
4. Select the connection you created for receiving Faxes

**You are now all setup** to receive Inbound Fax with Telnyx. By default, Telnyx expects the customer to send a T38 re-INVITE. If no re-INVITE is received, the FAX call will continue with G711 codec. Note: Unchecking "Enable T38 FAX gateway" option under Numbers page forces Telnyx to not accept a T38 reinvite.

### **Enable T.38 Re-Invites.**

1. Visit the NUMBERS page via the navigation menu on the left
2. Go to the MY NUMBERS tab. Find your number
3. Select Advanced Options button (gear icon) next to the number
4. Click on "Expert Configuration" to show additional options
5. Check the "Enable T.38 Fax Gateway" option

## Settings on your Fax Machine

Different fax machine manufacturers have some variance in their default fax transmission settings - most of which were likely originally designed with copper phone lines in mind, some of which can cause less than optimal experiences when using an ATA to transmit the fax tone using any VoIP service. The suggested settings below should help ensure your device is optimized for reliability when connected to an ATA.

Generally speaking, most fax machines on the market today should allow you to modify these suggested values without much difficulty. You should check with the user guide / documentation of your specific fax machine if you need to modify these values - which you should only need to do if you run into troubles when testing a properly configured ATA ready for faxing on your Telnyx account.

## **Fax Machine Settings**

* **Set the baud rate to 9600 or below**: Menu options might refer to setting as "transmission speed", "compatibility mode", or "VoIP mode". Slower speeds can help ensure more data gets to its destination. Higher speeds increase the chance of failure from packet loss, jitter, and/or latency. The more pages in the fax, the more impactful this setting can help increase reliability.
* **Disable Error Correction Mode (ECM):** ECM tells the machine to retransmit when noise, poor signal strength or packet loss is detected. But packet loss, jitter, and latency exist on the Internet normally, so the retransmits increase call duration, increasing instability of the fax signal. Disabling ECM prevents this retransmit signal.
* **Set fax resolution to "normal":** Using normal quality instead of high, fine, or ultra-fine can help increase fax speed and reliability. This reduces the amount of information (packets) that need to be transmitted.
* **Disable dial tone detection:** Note: Only change this setting if the fax machine fails to dial outbound properly.

**Please note that we do not support SRTP encryption when T.38 is enabled.**

##

---

Related Articles

[FreePBX Trunk Settings With Telnyx](https://support.telnyx.com/en/articles/1130620-freepbx-trunk-settings-with-telnyx)[Telnyx SIP Response Codes](https://support.telnyx.com/en/articles/4409457-telnyx-sip-response-codes)[Fax API - Error List](https://support.telnyx.com/en/articles/4967498-fax-api-error-list)[Grandstream HT802: Telnyx Setup](https://support.telnyx.com/en/articles/5725071-grandstream-ht802-telnyx-setup)[Gigaset A510: Telnyx Setup](https://support.telnyx.com/en/articles/5815209-gigaset-a510-telnyx-setup)

Did this answer your question?

😞😐😃

Table of contents
