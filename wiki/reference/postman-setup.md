---
title: Postman Setup
summary: Postman Setup for using Telnyx APIs.
sources:
  - url: https://developers.telnyx.com/development/development-tools/postman-setup/index
    content_hash: ef38170ce4201811e78e822abbc88347ac236a4c1259ba7c5ffbbfc6dae5d5a0
updated_at: 2026-04-10T00:00:00Z
---

# Postman Setup

Postman Setup for using Telnyx APIs

Postman is an API platform available as a web or desktop application. A great way to understand an API is to make requests and review the responses. Postman exactly  does that by providing a UI for testing and experimenting with API calls without the need to write code. Hence, we recommend using Postman to get started quickly and get the taste of Telnyx APIs. You can easily accomplish this by utilizing [our Postman collections](https://www.postman.com/telnyx-api?tab=collections).

Steps to use these collections:

* Configure your local environment
* Import a collection.
* Send a test request and inspect the responses.

## Configure environment

An environment is a set of [variables](https://learning.postman.com/docs/sending-requests/variables/) you can use in your Postman requests. You can use environments to group related sets of values together.

By the end of this tutorial, you would have imported and configured environment to use with Telnyx collections.

1. Create an API Key following the below steps.
   * [Sign up](https://telnyx.com/sign-up) for a free Telnyx account
   * Navigate to the [API Keys](https://portal.telnyx.com/#/app/api-keys) section and create an API Key by clicking **Create API Key**.

<Callout type="info">
  You need to obtain your API key so Telnyx can authenticate your [API requests](https://api.telnyx.com/v2/rooms).

Copy and save this key in a safe place and don't share it with anyone as it is a sensitive value.

2. Sign up at [Postman](https://identity.getpostman.com/signup) or [download](https://www.postman.com/downloads/) and install the Postman application.

3. Once signed in to Postman, select an existing workspace or create a new workspace for your Telnyx collections. If you are new to Postman, learn more about creating a workspace [here](https://learning.postman.com/docs/collaborating-in-postman/using-workspaces/creating-workspaces/).

4. Once you are in your desired workspace, click Import in the top left corner, select Link from the options and paste this link in the **Enter a URL** text box: `https://tlyx.co/telnyx-postman-environment`

   <img alt="Import Telnyx Postman Environment" />

   Then click continue and it should show basic details of the environment you are about to import. Click Import and you should see a success confirmation at the bottom right

   <img alt="Import Postman Confirmation" />

5. Go to Environments tab on the left and select `Telnyx Environment`

   <img alt="Postman Environment" />

   You should see list of variables with the ability to edit existing variables and add new variables. Please do the following steps here:

   * For the `customerApiKey` variable, in the **Initial Value** and **Current Value** columns, enter your API key that you created earlier in Step 1.
   * Click Save at the top right to save the value to the environment.

6. Click the box in the top right corner that has list of environments and select `Telnyx Environment` from the list. Initially it shows up as `No Environment`.

   Doing this will set the workspace to use `Telnyx Environment` moving forward.

   <img alt="Postman Environment" />

**You are all set with the Telnyx environment for Postman.**

## Import collections

Postman Collections are a group of saved requests.

We made it easy to import postman collections by adding a `Run in Postman` button in all the API reference pages that allows you to fork the collections, test API requests, and see the results immediately without writing any code.

For example, Use the **Run in Postman** button below to import the Phone Numbers API collection:

[![Run in Postman](https://run.pstmn.io/button.svg)](https://god.gw.postman.com/run-collection/19300194-3ed78399-2d3d-4a67-a4db-1d6bc07689a8?action=collection%2Ffork\&collection-url=entityId%3D19300194-3ed78399-2d3d-4a67-a4db-1d6bc07689a8%26entityType%3Dcollection%26workspaceId%3Dba40e23b-d67e-47e1-9174-d8c640348288)

Then, it should show a dialog box with some information on benefits of forking and links to view/import the collection instead of forking. Click `Fork Collection`

<img alt="Fork Collection" />

After clicking Fork Collection, you will see a small form with some details to fill before you fork:

* Fork label: Make sure you provide a relevant label for you to easily identify it.
  Eg: `telnyx's fork`
* Workspace: Choose which workspace you would like this collection to be part of.
* Watch original collection: Checking this box will notify you when updates are made to the collection so you can pull the latest changes made to the collection.

<img alt="Fork Details" />

Congratulations on forking the collection. You should now be able to see the collection under your selected workspace.

## Send request

As you've added your `API KEY` to the environment and imported a collection from the previous steps, you're now ready to send a request.

> `Note:` Make sure you have selected Telnyx Environment at the top right from the list of environments

As we have imported Phone Numbers API collection from previous steps, let us send a request to list the phone numbers in your account:

1. Once you are in your desired workspace where you imported this collection, Select the **Collections** tab in Postman on the left and expand the **Phone Numbers** collection.

2. Expand the **Number Configurations** folder and select **List phone numbers**. This loads the List phone numbers request into Postman, ready to send.

3. Click **Send**. The result pane automatically displays the results of your request.

4. In case you would like to use any filters, just select the checkbox for any filter you would like from the Params tab, set the value and click **Send**.

   <img alt="Send Request Sample" />

   If you receive an error, it's likely that one of the values in the environment isn't set correctly. Check the values and try again.

5. You can play with the API and if you want to save the request with the modified parameters or any other data, just click save and it should save your changes in the collection. This change would be local to you and would not effect the original collection you forked from.
   > If you would like to get the latest changes made to the original collection into your local collection, click on the Phone Numbers collection folder and then click on the three dots beside Save button which gives you a list of options. Select `Pull Changes` and it will fetch you the latest updates in that collection.
   >
   > <img alt="Pull Changes" />

Wohoo!! You have completed your first request with Telnyx API and now you're ready to explore what all the Telnyx API has to offer.

If you would like to see list of all collections, check [here](https://developers.telnyx.com/development/development-tools/postman-setup/collections-list)


## Related Pages

- [Portal Setup](../reference/portal-setup.md)
- [iOS Portal Setup](../reference/ios-portal-setup.md)
- [Android Portal Setup](../reference/android-portal-setup.md)
