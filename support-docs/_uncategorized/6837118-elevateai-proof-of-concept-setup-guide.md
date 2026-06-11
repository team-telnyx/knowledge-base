---
source_url: https://support.telnyx.com/en/articles/6837118-elevateai-proof-of-concept-setup-guide
scraped: 2026-06-11
---

ElevateAI Proof-of-Concept Setup Guide | Telnyx Help Center

[Skip to main content](#main-content)

# ElevateAI Proof-of-Concept Setup Guide

Step-by-step guide to integrate Telnyx with ElevateAI for transcription and recording.

Written by Dillin

December 13, 2023

Table of contents

This article will provide you with a step by step guide to configure Telnyx & ElevateAI which can help demonstrate a sample application using Telnyx-Python transcription and recording functionality.

​

# **Step 1: Create a Call Control Application in the Telnyx Portal**

Once you have created your Telnyx account and you have successfully logged into your account click the **Voice** tab from the left side menu then click **Programmable Voice**.  
​  
Finally click on the **Add new App** button from the top right corner:

[![Add new App section. ](https://downloads.intercomcdn.com/i/o/638031938/684fd752ba19fe177de38592/1..png?expires=1781168400&signature=f2d5a553922f366181d32f2ec2cbe818d84d4328ff1898ebeba2ca9992f8e311&req=ciMvFsp%2FlIJXFb4f3HP0gA%2B73wofgWiGsjlKUdGOYhCNKD%2BFPaL8AfZk3Kna%0A1iF8OMHGILZm9W1gPw%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/638031938/684fd752ba19fe177de38592/1..png?expires=1781168400&signature=f2d5a553922f366181d32f2ec2cbe818d84d4328ff1898ebeba2ca9992f8e311&req=ciMvFsp%2FlIJXFb4f3HP0gA%2B73wofgWiGsjlKUdGOYhCNKD%2BFPaL8AfZk3Kna%0A1iF8OMHGILZm9W1gPw%3D%3D%0A)

Next, enter in your **application name**, **webhook URL** and then click **Save**:

[![Voice API application.](https://downloads.intercomcdn.com/i/o/638032685/26e5cfbd8ac06e23b9561a59/2..png?expires=1781168400&signature=355478e2423e8e92b07d316275d3ab9ec3c48618778033df74b64c28a2e776e7&req=ciMvFsp8m4laFb4f3HP0gHVeOD9Ughuh9%2F6mU%2BQ31qj2hZAPeW5AeB0K9f%2Bd%0As9jCMsf5kg8PQ46sPw%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/638032685/26e5cfbd8ac06e23b9561a59/2..png?expires=1781168400&signature=355478e2423e8e92b07d316275d3ab9ec3c48618778033df74b64c28a2e776e7&req=ciMvFsp8m4laFb4f3HP0gHVeOD9Ughuh9%2F6mU%2BQ31qj2hZAPeW5AeB0K9f%2Bd%0As9jCMsf5kg8PQ46sPw%3D%3D%0A)

## **Step 2: Purchase a Telnyx Phone Number**

Once you have created your Telnyx call control application, click the **Numbers** tab from the left side menu:

[![Numbers tab section. ](https://downloads.intercomcdn.com/i/o/638033202/9d24c9b2c679dc23b1afa336/3..png?expires=1781168400&signature=c62f2aa903614b7ec28f6e26d67ab6d76a306ca53678aaf5351ce89e460ece30&req=ciMvFsp9n4FdFb4f3HP0gP5eriJ7ycm3N5NLfFF3JXg6uDtOR0qh1880SqEC%0AAEQ4CCPqAC4roz52pg%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/638033202/9d24c9b2c679dc23b1afa336/3..png?expires=1781168400&signature=c62f2aa903614b7ec28f6e26d67ab6d76a306ca53678aaf5351ce89e460ece30&req=ciMvFsp9n4FdFb4f3HP0gP5eriJ7ycm3N5NLfFF3JXg6uDtOR0qh1880SqEC%0AAEQ4CCPqAC4roz52pg%3D%3D%0A)

Next, click the **Search & Buy Numbers** tab from the top menu and click **Search Numbers** once you have selected the correct **search type and region/area code**:

[![Search &amp; Buy Numbers tab. ](https://downloads.intercomcdn.com/i/o/638033728/f667f1713c27b3e959fb4b8b/4..png?expires=1781168400&signature=50d15eddee4d56223b5a29f21b1304f4893c3afb64e4c057fe02cd25b073af05&req=ciMvFsp9moNXFb4f3HP0gOl8F9wHNL98L0bkG6x7i9ba%2FV%2BGsLuf6lbhCbFK%0AcdRpsuRR%2FfEEsdKxug%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/638033728/f667f1713c27b3e959fb4b8b/4..png?expires=1781168400&signature=50d15eddee4d56223b5a29f21b1304f4893c3afb64e4c057fe02cd25b073af05&req=ciMvFsp9moNXFb4f3HP0gOl8F9wHNL98L0bkG6x7i9ba%2FV%2BGsLuf6lbhCbFK%0AcdRpsuRR%2FfEEsdKxug%3D%3D%0A)

Select the desired number and click **Add to Cart**, then click the **Cart** button from the top right corner:

[![Add to Cart section. ](https://downloads.intercomcdn.com/i/o/638034251/3ef7b0f03c0d2f95a825ab73/5..png?expires=1781168400&signature=6042c8441e71da28e9da4a01a2b209e651234291b36b0741097d596e8fbda2d0&req=ciMvFsp6n4ReFb4f3HP0gO53hHqizqIE07fKmaFIqZ4sdXzdrvKPJZz05eIh%0ArOanMk79cnGZ1aGA5w%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/638034251/3ef7b0f03c0d2f95a825ab73/5..png?expires=1781168400&signature=6042c8441e71da28e9da4a01a2b209e651234291b36b0741097d596e8fbda2d0&req=ciMvFsp6n4ReFb4f3HP0gO53hHqizqIE07fKmaFIqZ4sdXzdrvKPJZz05eIh%0ArOanMk79cnGZ1aGA5w%3D%3D%0A)

Under **Connections or Applications** select the ElevateAI call control application that was

created in the previous step. Click **Place Order**:

[![Connections or Applications section. ](https://downloads.intercomcdn.com/i/o/638034956/527aa13ec36b5848be03860a/6..png?expires=1781168400&signature=44498efa59344d982084d29d7239f5c79c74efbd085e9b5606bbcf1ce9ac67bf&req=ciMvFsp6lIRZFb4f3HP0gNdsTtvpuvZt55xNDym247BACiYZoFdfHGuClxCN%0Af8HOKpQietA%2FmmhfVw%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/638034956/527aa13ec36b5848be03860a/6..png?expires=1781168400&signature=44498efa59344d982084d29d7239f5c79c74efbd085e9b5606bbcf1ce9ac67bf&req=ciMvFsp6lIRZFb4f3HP0gNdsTtvpuvZt55xNDym247BACiYZoFdfHGuClxCN%0Af8HOKpQietA%2FmmhfVw%3D%3D%0A)

## **Step 3. Sign up for ElevateAI and get your ElevateAI API Key**

First navigate to [ElevateAI's website](https://www.elevateai.com/) and click **Get Started** from the top right corner.  
​

[![Sign Up button. ](https://downloads.intercomcdn.com/i/o/638035942/9a90b1b1d31f95eb83107004/7..png?expires=1781168400&signature=8933b28c7b724ee28f28557d6fe26a638d829e5f86273b5ba062996847716e96&req=ciMvFsp7lIVdFb4f3HP0gASejLnoE%2BrWniP7ePXJZNk1JCD6SDyIFtdwOQcA%0AQ4sFXdmKclKmCmlq5Q%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/638035942/9a90b1b1d31f95eb83107004/7..png?expires=1781168400&signature=8933b28c7b724ee28f28557d6fe26a638d829e5f86273b5ba062996847716e96&req=ciMvFsp7lIVdFb4f3HP0gASejLnoE%2BrWniP7ePXJZNk1JCD6SDyIFtdwOQcA%0AQ4sFXdmKclKmCmlq5Q%3D%3D%0A)

Click **Sign Up** to register for a ElevateAI account.

[![Sign Up button.   ](https://downloads.intercomcdn.com/i/o/638036399/54cf0ab60732aa34c06928fb/8..png?expires=1781168400&signature=c48c910634854db4f4448408252cbbeae0f0b4d08b143d0c3d96c625ac13e832&req=ciMvFsp4nohWFb4f3HP0gAegwBZh94W4Lw46ia%2BsZtPrpbFfkcWp0IUp9y3r%0ACXef89XwxX2ZSR5l0w%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/638036399/54cf0ab60732aa34c06928fb/8..png?expires=1781168400&signature=c48c910634854db4f4448408252cbbeae0f0b4d08b143d0c3d96c625ac13e832&req=ciMvFsp4nohWFb4f3HP0gAegwBZh94W4Lw46ia%2BsZtPrpbFfkcWp0IUp9y3r%0ACXef89XwxX2ZSR5l0w%3D%3D%0A)

Fill out the registration form and click **Sign Up**.

[![Sign Up button. ](https://downloads.intercomcdn.com/i/o/638038404/651b76c422666007b0c657a5/9..png?expires=1781168400&signature=6fbd7bd8489d0b38aef3afb8493c667b7b3c847725d79ebd636038d885c39ddb&req=ciMvFsp2mYFbFb4f3HP0gDsJ3bGAhjgpqm8Yf7ZbmmtZdwy8%2BLLIV5Hsasch%0ATVBBB5qEVdAJ0vkTCQ%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/638038404/651b76c422666007b0c657a5/9..png?expires=1781168400&signature=6fbd7bd8489d0b38aef3afb8493c667b7b3c847725d79ebd636038d885c39ddb&req=ciMvFsp2mYFbFb4f3HP0gDsJ3bGAhjgpqm8Yf7ZbmmtZdwy8%2BLLIV5Hsasch%0ATVBBB5qEVdAJ0vkTCQ%3D%3D%0A)

Once you verify your account, login to your Elevate account and click **Manage Keys**:

[![ Manage Keys section for inputing IP token. ](https://downloads.intercomcdn.com/i/o/638038928/776c038a6efed4ece318f7d8/10..png?expires=1781168400&signature=e6ed19f50127459e9d0f16c24f1dd457168fcaf7b3f755b7436529dfef720a71&req=ciMvFsp2lINXFb4f3HP0gPmbFGOWVMuQ3e0fDOuHKfWw71SGDpPuyZAJ%2BJM7%0AqPjARUGfEPj5OqWy9w%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/638038928/776c038a6efed4ece318f7d8/10..png?expires=1781168400&signature=e6ed19f50127459e9d0f16c24f1dd457168fcaf7b3f755b7436529dfef720a71&req=ciMvFsp2lINXFb4f3HP0gPmbFGOWVMuQ3e0fDOuHKfWw71SGDpPuyZAJ%2BJM7%0AqPjARUGfEPj5OqWy9w%3D%3D%0A)

Copy your **API token**, you will need to use it later:

[![ Manage Keys section for inputing API token. ](https://downloads.intercomcdn.com/i/o/638039360/f9cf381c9aece3b6d874f36b/11...png?expires=1781168400&signature=932f8f5facfa316c0af3409c3f2adbbd3e32c881adba0aa9bfb389f222c8976c&req=ciMvFsp3nodfFb4f3HP0gE8tosrAHjYWJG%2FJzFWwaWyYLWQ%2BC2abp78QL%2FN2%0AfbH99OWbPHzF0eTuPQ%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/638039360/f9cf381c9aece3b6d874f36b/11...png?expires=1781168400&signature=932f8f5facfa316c0af3409c3f2adbbd3e32c881adba0aa9bfb389f222c8976c&req=ciMvFsp3nodfFb4f3HP0gE8tosrAHjYWJG%2FJzFWwaWyYLWQ%2BC2abp78QL%2FN2%0AfbH99OWbPHzF0eTuPQ%3D%3D%0A)

## **Step 4: Clone the PoC project and follow the steps in Github**

Link: <https://github.com/team-telnyx/demo-python-telnyx/tree/master/flask-elevateai-transcription-call-control>

---

Related Articles

[E911 Setup Guide](https://support.telnyx.com/en/articles/1130683-e911-setup-guide)[Yealink: Setup with Telnyx](https://support.telnyx.com/en/articles/3074710-yealink-setup-with-telnyx)[Bicom: PBXware Setup](https://support.telnyx.com/en/articles/5138185-bicom-pbxware-setup)[Real-Time Transcription](https://support.telnyx.com/en/articles/8292490-real-time-transcription)[Twilio TwiML Conference on Telnyx](https://support.telnyx.com/en/articles/13389311-twilio-twiml-conference-on-telnyx)

Did this answer your question?

😞😐😃

Table of contents
