---
source_url: https://support.telnyx.com/en/articles/6837118-elevateai-proof-of-concept-setup-guide
title: "ElevateAI Proof-of-Concept Setup Guide"
description: "Step-by-step guide to integrate Telnyx with ElevateAI for transcription and recording. See Telnyx guidance and requirements."
scraped: 2026-07-08
content_hash: d93bcb7fd70fd84b0ba388734ba3b2d36fe35db4d7a8c4f207934755a3563576
---







# ElevateAI Proof-of-Concept Setup Guide

Step-by-step guide to integrate Telnyx with ElevateAI for transcription and recording. See Telnyx guidance and requirements.




This article will provide you with a step by step guide to configure Telnyx & ElevateAI which can help demonstrate a sample application using Telnyx-Python transcription and recording functionality.

​

## **Step 1: Create a Call Control Application in the Telnyx Portal**

Once you have created your Telnyx account and you have successfully logged into your account click the **Voice** tab from the left side menu then click **Programmable Voice**.
​
Finally click on the **Add new App** button from the top right corner:

![Add new App section. ](_images/e62edad978fad8e2.png)

Next, enter in your **application name**, **webhook URL** and then click **Save**:

![Voice API application.](_images/2a6ec9ac09086917.png)

## **Step 2: Purchase a Telnyx Phone Number**

Once you have created your Telnyx call control application, click the **Numbers** tab from the left side menu:

![Numbers tab section. ](_images/a16c7c4738714091.png)

Next, click the **Search & Buy Numbers** tab from the top menu and click **Search Numbers** once you have selected the correct **search type and region/area code**:

![Search &amp; Buy Numbers tab. ](_images/fb9ae0e20e752d4e.png)

Select the desired number and click **Add to Cart**, then click the **Cart** button from the top right corner:

![Add to Cart section. ](_images/0469442229288ca9.png)

Under **Connections or Applications** select the ElevateAI call control application that was

created in the previous step. Click **Place Order**:

![Connections or Applications section. ](_images/b30e62f64b2acd67.png)

## **Step 3. Sign up for ElevateAI and get your ElevateAI API Key**

First navigate to [ElevateAI's website](https://www.elevateai.com/) and click **Get Started** from the top right corner.
​

![Sign Up button. ](_images/441f60395743ae0e.png)

Click **Sign Up** to register for a ElevateAI account.

![Sign Up button.   ](_images/7d011627c10adea1.png)

Fill out the registration form and click **Sign Up**.

![Sign Up button. ](_images/82f54c217e09a070.png)

Once you verify your account, login to your Elevate account and click **Manage Keys**:

![ Manage Keys section for inputing IP token. ](_images/0f4d0b386eb1ffb0.png)

Copy your **API token**, you will need to use it later:

![ Manage Keys section for inputing API token. ](_images/d3e544f42e6f8f60.png)

## **Step 4: Clone the PoC project and follow the steps in Github**

Link: <https://github.com/team-telnyx/demo-python-telnyx/tree/master/flask-elevateai-transcription-call-control>

---

Related Articles

[E911 Setup Guide](https://support.telnyx.com/en/articles/1130683-e911-setup-guide)[Yealink: Setup with Telnyx](https://support.telnyx.com/en/articles/3074710-yealink-setup-with-telnyx)[Bicom: PBXware Setup](https://support.telnyx.com/en/articles/5138185-bicom-pbxware-setup)[Configuring Telnyx with Microsoft Teams Direct Routing](https://support.telnyx.com/en/articles/5253876-configuring-telnyx-with-microsoft-teams-direct-routing)[Real-Time Transcription](https://support.telnyx.com/en/articles/8292490-real-time-transcription)

Did this answer your question?

😞😐😃
