---
title: Conferencing Demo
summary: How to build a conferencing using Telnyx Voice API.
sources:
  - url: https://developers.telnyx.com/docs/voice/programmable-voice/conferencing-demo/index
    content_hash: b29e89a7d8406eb0caf798cc9c2d403fc820d86627745bb68eede3d0529be1bf
updated_at: 2026-04-10T00:00:00Z
---

# Conferencing Demo

How to build a conferencing using Telnyx Voice API. Start building on Telnyx today.

\| [Python](#python) | [PHP](#php) | [Node](#node) | [Ruby](#ruby) |

***

## Python

⏱ **60 minutes build time || <a href="https://github.com/team-telnyx/python-conferencing-demo">Github Repo</a>**

### Introduction

The [Voice API framework](https://developers.telnyx.com/api-reference/call-commands/dial), previously called Call Control, is a set of APIs that allow complete control of a call flow from the moment a call begins to the moment it is completed. In between, you will receive a number of [webhooks](receiving-webhooks-for-programmable-voice.md) for each step of the call, allowing you to act on these events and send commands using the Telnyx Library. A subset of the operations available in the Voice API is the [Conference](https://developers.telnyx.com/api-reference/conference-commands/conference-recording-start) API. This allows the user (you) to create and manage a conference programmatically upon receiving an incoming call, or when initiating an outgoing call.

The <a href="https://github.com/team-telnyx/telnyx-python">Telnyx Python Library</a>
is a convenient wrapper around the Telnyx REST API. It allows you to access and control call flows using an intuitive object-oriented library. This tutorial will walk you through creating a simple Flask and Ngrok server application that allows you to create and manage a conference.

### Setup

This tutorial assumes you've already [set up your developer account and environment](/development) and you know how to [send commands](sending-commands-for-programmable-voice.md) and [receive webhooks](receiving-webhooks-for-programmable-voice.md) using the Telnyx Voice API.

* make sure the *Webhook API Version* is **API v2**

You’ll also need to have `python` installed to continue. You can check this by running the following:

```bash theme={null}
$ python3 -v
```

<Callout type="info">
  After pasting the above content, Kindly check and remove any new line added

Now in order to receive the necessary webhooks for our IVR, we will need to set up a server. For this tutorial, we will be using <a href="https://palletsprojects.com/p/flask/">Flask</a>, a micro web server framework. A quickstart guide to flask can be found on their official website. For now, we will install flask using pip.

```bash theme={null}
$ pip install flask
```

<Callout type="info">
  After pasting the above content, Kindly check and remove any new line added

You can get the full set of available Telnyx Voice API Commands [here](https://developers.telnyx.com/api-reference/call-commands/dial).
You can also find the Conference Commands [here](https://developers.telnyx.com/api-reference/conference-commands/conference-recording-start)

For each Telnyx Voice API Command we will be using the Telnyx Python SDK. To execute this API we are using Python `telnyx`, so make sure you have it installed. If not you can install it with the following command:

```bash theme={null}
$ pip install telnyx
```

<Callout type="info">
  After pasting the above content, Kindly check and remove any new line added

After that you’ll be able to use ‘telnyx’ as part of your app code as follows:

```python theme={null}
import telnyx
```

<Callout type="info">
  After pasting the above content, Kindly check and remove any new line added

We will also import Flask in our application as follows:

```python theme={null}
from flask import Flask, request, Response
```

<Callout type="info">
  After pasting the above content, Kindly check and remove any new line added

And set our api key using the Python telnyx SDK:

```python theme={null}
telnyx.api_key = "YOUR_TELNYX_API_KEY"
```

<Callout type="info">
  After pasting the above content, Kindly check and remove any new line added

### Server and Webhook setup

Flask is a great application for setting up local servers. However, in order to make our code public to be able to receive webhooks from Telnyx, we are going to need to use a tool called ngrok. Installation instructions can be found [here](../reference/ngrok.md#ngrok).

Now to begin our flask application, underneath the import and setup lines detailed above, we will add the following:

```python theme={null}
app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def respond():
	//Our code for handling the call control application will go here
	print(request.json[‘data’])
return Response(status=200)
```

<Callout type="info">
  After pasting the above content, Kindly check and remove any new line added

This is the base Flask application code specified by their <a href="https://palletsprojects.com/p/flask/">documentation</a>. This is the minimum setup required to receive webhooks and manipulate the information received in json format. To complete our setup, we must run the following to set up the Flask environment (note YOUR\_FILE\_NAME will be whatever you .py file is named):

```bash theme={null}
$ export FLASK_APP=YOUR_FILE_NAME.py
```

<Callout type="info">
  After pasting the above content, Kindly check and remove any new line added

Now, we are ready to serve up our application to our local server. To do this, run:

```bash theme={null}
$ flash run
```

<Callout type="info">
  After pasting the above content, Kindly check and remove any new line added

A successful output log should look something like:

```bash theme={null}
 * Serving Flask app "main"
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

<Callout type="info">
  After pasting the above content, Kindly check and remove any new line added

Now that our Flask application is running on our local server, we can use ngrok to make this public to receive webhooks from Telnyx by running the following command wherever the ngrok executable is located (NOTE you may have to open another terminal window or push the Flask process to the background):

```bash theme={null}
$ ./ngrok http 5000
```

<Callout type="info">
  After pasting the above content, Kindly check and remove any new line added

Once this is up and running, you should see the output URL in the command logs or located on the <a href="https://dashboard.ngrok.com/login">ngrok dashboard page</a>. This url is important because it will be where our Voice API Application will be sending webhooks to. Grab this url and head on over to the Telnyx Dashboard page. Navigate to your Voice API Application and add the URL to the section labeled "Send a webhook to the URL" as shown below. Add the ngrok url to that section and we are all set up to start our IVR!

**Ensure that you append '/webhook' to the ngrok url as specified in our Flask Application**

![URL Webhook Section](https://images.ctfassets.net/4b49ta6b3nwj/5fWNOgoZnSwcSj28O1B5Ld/f951a6c0b7118f3a27d86aa5d5035d5e/call_control_url_webhook.PNG)

### Receiving and interpreting Webhooks

We will be configuring our respond function to handle certain incoming webhooks and execute Voice API commands based on what the values are. Flask catches the incoming webhooks and calls the respond() function every time a webhook is sent to the route we specified as ‘/webhook’. We can see the json value of the hook in the request.json object. Here is what a basic Telnyx Call Object looks like

```json theme={null}
{
	'data': {
		'event_type': 'call.initiated',
		'id': 'a2fa3fa6-4e8c-492d-a7a6-1573b62d0c56',
		'occurred_at': '2020-07-10T05:08:59.668179Z',
		'payload': {
			'call_control_id': 'v2:rcSQADuW8cD1Ud1O0YVbFROiQ0_whGi3aHtpnbi_d34Hh6ELKvLZ3Q',
			'call_leg_id': '76b31010-c26b-11ea-8dd4-02420a0f6468',
			'call_session_id': '76b31ed4-c26b-11ea-a811-02420a0f6468',
			'caller_id_name': '+17578390228',
			'client_state': None,
			'connection_id': '1385617721416222081',
			'direction': 'incoming',
			'from': '+14234567891',
			'start_time': '2020-07-10T05:08:59.668179Z',
			'state': 'parked',
			'to': '+12624755500'
		},
		'record_type': 'event'
	},
	'meta': {
		'attempt': 1,
		'delivered_to': 'http://59d6dec27771.ngrok.io/webhook'
	}
}
```

<Callout type="info">
  After pasting the above content, Kindly check and remove any new line added

We want to first check and see if the incoming webhook is an event. To check that, we need to look at the record\_type using the following check:

```python theme={null}
def respond():
	//Check record_type of object
	data = request.json['data']
    	if data.get('record_type') == 'event':

	print(request.json[‘data’])
return Response(status=200)
```

<Callout type="info">
  After pasting the above content, Kindly check and remove any new line added

Then, we can check and see what kind of event it is. In the case of the example json above, the event is call.initiated. We can get that value using the following added code:

```python theme={null}
def respond():
	//Check record_type of object
	data = request.json['data']
    	if data.get('record_type') == 'event':
		//Check event type
		event = data.get('event_type')
        	print(event, flush=True)
        	if event == "call.initiated":
            	print("Incoming call", flush=True)

	print(request.json[‘data’])
return Response(status=200)
```

<Callout type="info">
  After pasting the above content, Kindly check and remove any new line added

As you can see, this check will print out “incoming call” whenever a call.initiated event is received by our application. We can even test it by giving the Phone Number associated with our Voice API Application a call! Now we can start to implement some commands in response to this webhook.

### Receiving Webhooks & creating a conference

Below is the logic that will go inside our respond() function. When we receive a webhook, we extract the data from `request.json.get('data')` and we look at the `event_type` inside that object to determine a course of action.

```python theme={null}
calls = []
conference = None

class call_info:
    call_control_id: ''
    call_leg_id: ''

@app.route('/webhook', methods=['POST'])
def respond():

    # Activate global calls array
    global calls
    global conference

    # Get the data from the request
    data = request.json.get('data')
    # Check record_type
    if data.get('record_type') == 'event':
        # Check event type
        event = data.get('event_type')
        if event == "call.initiated":
            # Extract call information and store it in a new call_info() object
            new_call = call_info()
            new_call.call_control_id = data.get('payload').get('call_control_id')
            new_call.call_leg_id = data.get('payload').get('call_leg_id')
            calls.append(new_call)
            # Answer the call
            print(telnyx.Call.answer(new_call), flush=True)

        # When the call is answered, find the stored call and either add it 
        # to the conference or create a new one if one is not yet created
        elif event == "call.answered":
            call_id = data.get('payload').get('call_control_id')
            call_created = call_info()
            call_created.call_control_id = call_id

            for call in calls:
                if call.call_control_id == call_id:
                    if not conference:
                        conference = telnyx.Conference.create(beep_enabled="always",call_control_id=call_id, name="demo-conference")
                    else:
                        conference.join(call_control_id=call_id)

        # When a caller hangs up, remove that caller from the global calls array
        elif event == "call.hangup":
            call_id = data.get('payload').get('call_leg_id')
            for call in calls:
                if call.call_leg_id == call_id:
                    calls.remove(call)
    return Response(status=200)
```

<Callout type="info">
  After pasting the above content, Kindly check and remove any new line added

Pat youself on the back - that's a lot of code to go through! Now let's break it down even further and explain what it does. First, create an array for keeping track of the ongoing calls and define a variable for storing the conference object. Then, we create a small object class for call\_info, containing the call\_control\_id and call\_leg\_id. This will be useful for searching for calls in our calls array later, as well as using Conference Commands with those objects.

```python theme={null}
calls = []
conference = None

class call_info:
    call_control_id: ''
    call_leg_id: ''
```

<Callout type="info">
  After pasting the above content, Kindly check and remove any new line added

Next, we parse the data from our webhook in the respond() function. We first declare our global variables inside of the function so that the scope is consistent. Then, we extract the data from the reponse and check to ensure the `record_type` is `event`. Then, we extract the `event_type` itself and use logic to determine the action taken based on the `event`.

```python theme={null}
@app.route('/webhook', methods=['POST'])
def respond():
    # Activate global calls array
    global calls
    global conference
    # Get the data from the request
    data = request.json.get('data')
    #print(data, flush=True) #For testing purposes, you could print out the data object received
    # Check record_type
    if data.get('record_type') == 'event':
        # Check event type
        event = data.get('event_type')
```

<Callout type="info">
  After pasting the above content, Kindly check and remove any new line added

Here is where you will respond to a new call being initiated, which can be from either an inbound or outbound call. We create a new call\_info() object and assign the `call_control_id` and `call_leg_id` from the incoming data. We then use `telnyx.Call.answer(new_call)` to answer the call. This will trigger a webhook event `call.answered` which we will handle below.

```python theme={null}


## Related Pages

- [Call Tracking Demo](../runbooks/call-tracking-demo.md)
