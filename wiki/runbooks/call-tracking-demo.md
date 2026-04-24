---
title: Call Tracking Demo
summary: How to build a call tracking application using Telnyx Voice API.
sources:
  - url: https://developers.telnyx.com/docs/voice/programmable-voice/call-tracking/index
    content_hash: b3d09fe1c97bd32ffeec5529614d9c9b73a0be8d4668b4e06598131d1172cde1
updated_at: 2026-04-10T00:00:00Z
---

# Call Tracking Demo

How to build a call tracking application using Telnyx Voice API. Start building on Telnyx today.

\| [Python](#python) | [Node](#node) |

***

## Python

**⏱ 60 minutes build time.**

**🧰 Clone the sample application from our <a href="https://github.com/team-telnyx/demo-python-telnyx/tree/master/flask-call-tracking_call-control">GitHub repo</a>**

<hr />

In this tutorial, you'll learn how to build a **Call Tracking** application using the **Telnyx API**, and our **Python SDK**.

Call Control (the Telnyx Voice API), combined with our Numbers API, provides everything you need to build a robust number ordering and call tracking application:

* The Numbers API enables you to search the Telnyx phone number inventory in real time; filtering by Area Code, City/State, and more to find the perfect local number for your use-case.
* Call Control enables you to quickly setup dynamic forwarding numbers, toggle dual-channel recording, join/leave dynamic conferences, and pull post-call analytics.

By following this tutorial, you'll build an app that can:

> 1. Search and order phone numbers by a city and state combination.
> 2. Receive inbound calls to the Telnyx phone number.
> 3. Transfer calls using Call Control to your designated Forwarding Number.
> 4. Store all required information in a database of your choice.
> 5. Make a front-end that shows what's going on.

### Create a Telnyx mission control portal account

To get started, you'll need to <a href="https://telnyx.com/sign-up">create an account</a>. Verify your email address and you can log into the <a href="https://portal.telnyx.com">Mission Control Portal</a> to get started.

### Set up your local machine to receive webhooks from Telnyx

Next, you'll need a means of receiving webhooks sent by Telnyx to notify your application of call events. One of the easiest ways to accomplish this is to [use a tool like ngrok](../reference/ngrok.md#ngrok) to generate a tunnelling URL, which connects to a locally running application via a port on your machine.

In this example, port `8000` is used. After downloading and installing ngrok, run `./ngrok http 8000` and make note of the resultant **HTTPS Forwarding URL**.

### Create a Telnyx call control application

From the Portal, create a new <a href="https://portal.telnyx.com/#/app/call-control/applications">Call Control Application</a>
, and paste the **HTTPS Forwarding URL** from the previous steps to send webhooks from this application to your local machine via ngrok.

Ensure API v2 is selected, and save your application. We don't need to worry about any other application settings for now.

Select your application again to edit it, and make a note of the **ID**. This is how you'll identify your Call Control Application in your code.

### Create an Outbound Voice profile

From the Portal, create a new <a href="https://portal.telnyx.com/#/app/outbound-profiles">Outbound Voice Profile</a>. Click **Add connections/apps to profile** and select the Call Control Application you created in the previous step.

In the **International Allowed Destinations** section, ensure you have selected the region(s) in which you want your application to work.

### Initialize and install packages via pip

Initialize your call tracking application with the defaults presented to you and create a virtual environment.

```bash theme={null}
mkdir call-tracking
cd call-tracking
python3 -m venv /path/to/new/virtual/environment
```

<Callout type="info">
  After pasting the above content, Kindly check and remove any new line added

Then install the necessary packages for the call tracking application. They can be found in this <a href="https://github.com/team-telnyx/demo-python-telnyx/blob/master/flask-call-tracking_call-control/Pipfile">Pipfile</a> or manually install them:

```bash theme={null}
pip install flask
pip install flask-modus
pip install python-dotenv
pip install telnyx
pip install peewee
pip install pymysql
pip install werkzeug==0.16.1
```

<Callout type="info">
  After pasting the above content, Kindly check and remove any new line added

Brief explanation on the required packages:

<a href="https://flask.palletsprojects.com/en/1.1.x/">Flask</a>:

### Set up environment variables

The following environment variables need to be set for your call tracking application to work:

<table>
  <tbody>
    <tr>
      <td>Variable</td>
      <td>Description</td>
    </tr>

    <tr>
      <td><code>TELNYX\_API\_KEY</code></td>
      <td>Your <a href="https://portal.telnyx.com/#/app/api-keys">Telnyx API Key</a>, which can be created in the portal.</td>
    </tr>

    <tr>
      <td><code>TELNYX\_PUBLIC\_KEY</code></td>
      <td>Your <a href="https://portal.telnyx.com/#/app/account/public-key">Telnyx Public Key</a>, which is accessible via the portal.</td>
    </tr>

    <tr>
      <td><code>TELNYX\_CONNECTION\_ID</code></td>
      <td>The <strong>ID</strong> from your <a href="https://portal.telnyx.com/#/app/call-control/applications">Call Control Application</a></td>
    </tr>

    <tr>
      <td><code>MESSAGING\_PROFILE\_ID</code></td>
      <td>The <strong>ID</strong> from your <a href="https://portal.telnyx.com/#/app/messaging">Messaging Profile</a></td>
    </tr>

    <tr>
      <td><code>DATABASE\_HOST</code></td>
      <td>Connection of the host (ie. localhost or your local ip address)</td>
    </tr>

    <tr>
      <td><code>DATABASE\_USER</code></td>
      <td>Your database user name</td>
    </tr>

    <tr>
      <td><code>DATABASE\_PASSWORD</code></td>
      <td>Your database password</td>
    </tr>

    <tr>
      <td><code>DATABASE\_NAME</code></td>
      <td>Your database name</td>
    </tr>

    <tr>
      <td><code>DATABASE\_PORT</code></td>
      <td>Your database port</td>
    </tr>
  </tbody>
</table>

This app uses the excellent <a href="https://github.com/bkeepers/dotenv">dotenv</a> package to manage environment variables.

Make a copy of the file below, add your credentials, and save as `.env` in the root directory.

```bash theme={null}
TELNYX_API_KEY="YOUR_API_KEY"
TELNYX_CONNECTION_ID="YOUR_CALL_CONTROL_ID"
MESSAGING_PROFILE_ID="YOUR_MESSAGING_PROFILE_ID"

DATABASE_HOST="localhost"
DATABASE_USER="root"
DATABASE_PASSWORD=""
DATABASE_NAME="cctracker"
DATABASE_PORT=""
```

<Callout type="info">
  After pasting the above content, Kindly check and remove any new line added

### Create some folders and Python files to build our call tracking application

We'll use a few `.py` files to build the call tracking application.

* `app.py` as our entry point to the application
* `database.py` for our database
* `database_queries.py` for our database controller
* `telnyx_commands.py` to manage most of our telnyx related functions

We would also like to categorize and sort these in a practical sense, so we are going to be making a few folders to sort the files into:

* `model` to host our databse related quieries
* `static` for our css and js
* `templates` as our entry point to everything html and frontend that we would want

So let's create our folders and files:

```bash theme={null}
mkdir model
mkdir static
mkdir templates

touch app.py
touch telnyx_commands.py

touch model/database.py
touch model/database_queries.py
```

<Callout type="info">
  After pasting the above content, Kindly check and remove any new line added

This then should create the two files in our model directory, and two files in our base directory to get started

### Setup basic Telnyx commands

Here we will setup some basic commands to get ourselves going for the call tracking app. We will want the ability to procure some numbers via the API, have the capability to delete them, and look up some basic CNAM paramaters if we can.
As such, we will be creating some basic functions:

* telnyx\_number\_acquire(locality, administrative\_area): This will handle the number search and ordering portion of our app when given the specific arameters
  * We will be specifying locality and rate\_center which corresponds with City and State.
  * We will also go ahead and search for numbers that are SMS capable so we can future proof just in case we would want to be adding on an SMS component to this.
  * Setting limit as 1 to fetch and procure the first result
  * Making sure quickship is set as True, so we get numbers that are actively ready to go out of the box and will not have to wait for procurement.
  * We will want to return the `number_to_order` and `city_state_combo` to pass which number and from where exactly we procured this from

* telnyx\_number\_delete(number\_to\_delete): This will handle deleting phone numbers in our portal

* telnyx\_cnam\_lookup(calling\_number): This will handle using Telnyx Lookup service to see if we can get information on the number that's calling us
  * We will be returning the variable `cnam_info` with the result to use later on

* difference(start\_time, end\_time): This handles conversion of the webhook start/end times to get call durations
  * Webhook times are in full time format, so we will use the included datetime function to convert the time into seconds before doing the math to get the difference for the duration
  * We will be returning both `duration` and `date`

```python theme={null}
// In app.py
import telnyx
import os
import math
from flask import redirect, url_for, flash
from datetime import datetime

def telnyx_number_acquire(locality, administrative_area):
    city_state_combo = locality + ", " + administrative_area
    number_search = telnyx.AvailablePhoneNumber.list(filter={
        "locality": locality,
        "rate_center": administrative_area,
        "features": "sms",
        "limit": "1",
        "quickship": True,
    })
    # catch no result error
    if number_search.metadata.total_results != 1:
        flash("No results found for specified area, "
              "try again! Watch our for typos!")
        return redirect(url_for('index'))
    else:
        number_to_order = number_search.data[0]["phone_number"]
        number_order_response = telnyx.NumberOrder.create(
            phone_numbers=[
                {"phone_number": number_to_order,
                 },
            ],
            messaging_profile_id=os.getenv("MESSAGING_PROFILE_ID"),
            connection_id=os.getenv("TELNYX_CONNECTION_ID"),
        )
        return number_to_order, city_state_combo

def telnyx_number_delete(number_to_delete):
    retrieve = telnyx.PhoneNumber.retrieve(number_to_delete)
    retrieve.delete()

def telnyx_cnam_lookup(calling_number):
    resource = telnyx.NumberLookup.retrieve(calling_number)
    if resource.caller_name is None:
        cnam_info = "Not Available"
        return cnam_info
    else:
        cnam_info = resource.caller_name
        return cnam_info


## Related Pages

- [Call Center Demo](../runbooks/call-center-demo.md)
- [Conferencing Demo](../runbooks/conferencing-demo.md)
