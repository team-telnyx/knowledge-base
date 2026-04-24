---
title: IVR Demo
summary: How to build an IVR using Telnyx Voice API.
sources:
  - url: https://developers.telnyx.com/docs/voice/programmable-voice/ivr-demo/index
    content_hash: 74674d838bd757ed8a0bf75e080c186f9e6631c4c2a0eb9eb497a834ac7c7e6b
updated_at: 2026-04-10T00:00:00Z
---

# IVR Demo

How to build an IVR using Telnyx Voice API. Start building on Telnyx today.

\| [Python](#python) | [Node](#node) | [Ruby](#ruby) |

***

## Python

⏱ **60 minutes build time || <a href="https://github.com/team-telnyx/ivr-demo-python">GithHub Repo</a>**

Telnyx IVR demo built on Voice API V2 and Python with Flask and Ngrok.

In this tutorial, you’ll learn how to:

1. Set up your development environment to use the Telnyx Voice API using Python and Flask.
2. Build a find me/follow me based app via IVR on the Telnyx Voice API using Python.

***

* [Prerequisites](#prerequisites-for-building-an-ivr-with-python)
* [Telnyx Voice API Basics](#telnyx-call-control-basics)

  * [Server and Webhook Setup](#server-and-webhook-setup)
  * [Receiving and Interpreting Webhooks](#receiving-and-interpreting-webhooks)
* [Call Commands](#call-commands)
* [Client State](#client-state)
* [Building the IVR](#building-the-ivr)
* [Creating the IVR](#creating-the-ivr)
* [Answering the Incoming Call](#answering-the-incoming-call)
* [Presenting Options](#presenting-options)
* [Interpreting Button Presses](#interpreting-button-presses)

***

### Prerequisites for building an IVR with Python

This tutorial assumes you've already [set up your developer account and environment](/development) and you know how to [send commands](sending-commands-for-programmable-voice.md) and [receive webhooks](receiving-webhooks-for-programmable-voice.md) using the Telnyx Voice API.

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

### Telnyx Voice API basics

For the Voice API application you’ll need to get a set of basic functions to perform Telnyx Voice API Commands. The below list of commands are just a few of the available commands available with the Telnyx Python SDK. We will be using a combination of Answer, Speak, and Gather Using Audio to create a base to support user interaction over the phone.

* [Voice API Bridge Calls](https://developers.telnyx.com/api-reference/call-commands/bridge-calls)
* [Voice API Dial](https://developers.telnyx.com/api-reference/call-commands/dial)
* [Voice API Speak Text](https://developers.telnyx.com/api-reference/call-commands/speak-text)
* [Voice API Gather Using Speak](https://developers.telnyx.com/api-reference/call-commands/gather-using-speak)
* [Voice API Hangup](https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/hangup/index#hangup)
* [Voice API Recording Start](https://developers.telnyx.com/api-reference/call-commands/recording-start)

You can get the full set of available Telnyx VoiceAPI Commands [here](https://developers.telnyx.com/api-reference/call-commands/dial).

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

The following environmental variables need to be set

<table>
  <tbody>
    <tr>
      <td>Variable</td>
      <td>Description</td>
    </tr>

    <tr>
      <td><code>TELNYX\_API\_KEY</code></td>
      <td>Your <a href="https://portal.telnyx.com/#/app/api-keys?utm_source=referral&utm_medium=github_referral&utm_campaign=cross-site-link">Telnyx API Key</a></td>
    </tr>

    <tr>
      <td><code>TELNYX\_PUBLIC\_KEY</code></td>
      <td>Your <a href="https://portal.telnyx.com/#/app/account/public-key?utm_source=referral&utm_medium=github_referral&utm_campaign=cross-site-link">Telnyx Public Key</a></td>
    </tr>
  </tbody>
</table>

#### .env file

This app uses the excellent <a href="https://github.com/theskumar/python-dotenv">python-dotenv</a> package to manage environment variables.

Make a copy of `.env.sample` and save as `.env` **📁 in the root directory** and update the variables to match your creds.

```
TELNYX_API_KEY=
TELNYX_PUBLIC_KEY=
```

<Callout type="info">
  After pasting the above content, Kindly check and remove any new line added

Before defining the flask application load the dotenv package and call the `load_dotenv()` function to set the environment variables.

```python theme={null}
from dotenv import load_dotenv

load_dotenv()
telnyx.api_key = os.getenv('TELNYX_API_KEY')
```

<Callout type="info">
  After pasting the above content, Kindly check and remove any new line added

### Server and Webhook setup

Flask is a great application for setting up local servers. However, in order to make our code public to be able to receive webhooks from Telnyx, we are going to need to use a tool called ngrok. Installation instructions can be found [here](../reference/ngrok.md#ngrok).

Now to begin our flask application, underneath the import and setup lines detailed above, we will add the following:

```python theme={null}
app = Flask(__name__)

@app.route('/Callbacks/Voice/Inbound', methods=['POST'])
def respond():
  ## Our code for handling the call control application will go here
  print(request.json[‘data’])
return Response(status=200)

if __name__ == '__main__':
    app.run()
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
$ python3 app.py
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

Once this is up and running, you should see the output URL in the command logs or located on the <a href="https://dashboard.ngrok.com/login">ngrok dashboard page</a>. This url is important because it will be where our Voice API Application will be sending webhooks to. Grab this url and head on over to the Telnyx Dashboard page. Navigate to your Call Control Application and add the URL to the section labeled "Send a webhook to the URL" as shown below. Add the ngrok url to that section and we are all set up to start our IVR!

<img alt="URL Webhook Section" />

### Receiving and interpreting webhooks

We will be configuring our respond function to handle certain incoming webhooks and execute call control commands based on what the values are. Flask catches the incoming webhooks and calls the respond() function every time a webhook is sent to the route we specified as ‘/webhook’. We can see the json value of the hook in the request.json object. Here is what a basic Telnyx Call Object looks like

```json theme={null}
{
  "data": {
    "event_type": "call.initiated",
    "id": "a2fa3fa6-4e8c-492d-a7a6-1573b62d0c56",
    "occurred_at": "2020-07-10T05:08:59.668179Z",
    "payload": {
      "call_control_id": "v2:rcSQADuW8cD1Ud1O0YVbFROiQ0_whGi3aHtpnbi_d34Hh6ELKvLZ3Q",
      "call_leg_id": "76b31010-c26b-11ea-8dd4-02420a0f6468",
      "call_session_id": "76b31ed4-c26b-11ea-a811-02420a0f6468",
      "caller_id_name": "+17578390228",
      "client_state": null,
      "connection_id": "1385617721416222081",
      "direction": "incoming",
      "from": "+14234567891",
      "start_time": "2020-07-10T05:08:59.668179Z",
      "state": "parked",
      "to": "+12624755500"
    },
    "record_type": "event"
  },
  "meta": {
    "attempt": 1,
    "delivered_to": "http://59d6dec27771.ngrok.io/webhook"
  }
}
```

<Callout type="info">
  After pasting the above content, Kindly check and remove any new line added

We want to first check and see if the incoming webhook is an event. To check that, we need to look at the record\_type using the following check:

```python theme={null}
def respond():
  ## Check record_type of object
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
  ##Check record_type of object
  data = request.json['data']
      if data.get('record_type') == 'event':
    ## Check event type
    event = data.get('event_type')
          print(event, flush=True)
          if event == "call_initiated":
              print("Incoming call", flush=True)

  print(request.json[‘data’])
return Response(status=200)
```

<Callout type="info">
  After pasting the above content, Kindly check and remove any new line added

As you can see, this check will print out “incoming call” whenever a call.initiated event is received by our application. We can even test it by giving the Phone Number associated with our Voice API application a call! Now we can start to implement some commands in response to this webhook.

### Call commands

A full reference to the call commands in every Telnyx SDK available can be found [here](https://developers.telnyx.com/api-reference/call-commands/dial)

### Client state

`Client State`: within some of the Telnyx Voice API Commands list we presented, you probably noticed we were including the `Client State` parameter. `Client State` is the key to ensure that we can perform functions only when very specific conditions are met on our App while consuming the same Voice API Events.

Because the Telnyx Voice API is stateless and async your application will be receiving several events of the same type, e.g. user just included `DTMF`. With `Client State` you enforce a unique ID to be sent back to Telnyx which be used within a particular Command flow and identifying it as being at a specific place in the call flow.

This app in particular will ask the user to make a selection from various Weather stations in the US. Upon their selection, they will be transfered to the city of choice.

The `client_state` is particularly useful during the transfer, as the outbound leg of the call will also emit status updates to the same endpoint as the inbound call.

Setting a value to the `client_state` will allow us to check the direction of the call for the gather IVR logic.

### Building the IVR

With all the basic Telnyx Voice API Commands set, we are ready to consume them and put them in the order that will create the IVR. For this tutorial we want to keep it simple with a flow that corresponds to the following IVR Logic:

1. Answer the incoming call
2. Present the options to the caller
3. Transfer the caller based on their selection

### Creating the IVR

In a separate file we can create a simple class to build the Gather strings based on a simple json configuration file. The objective is to separate the IVR functionality from the spoken sentence. This will allow the IVR prompts to be updated without changing Python code.

#### IVR class

```python theme={null}
class IVR:

  def __init__(self, intro, iterable, items, **kwargs):
      '''
      Creates the IVR object by generating the initial prompt

        Parameters:
          intro (string): The introduction sentence to the IVR
          iterable (string): A template string to be filled in by the items
          items (dict): A dictionary of items with a name and phone number
      '''
      self.intro = intro
      self.iterable = iterable
      self.items = items
      self.phone_number_table = {}
      self.valid_inputs = ''
      self.prompt = self.intro
      length = len(self.items)
      ## iterate over the items list and build the selection menu
      ## Sets the phone_number_table to lookup phone number from digit
      for i in range(length):
          itemName = self.items[i]['itemName']
          phone_number = self.items[i]['phoneNumber']
          digit = str(i+1) #cast to string and +1 (0-index)
          prompt = self.iterable % (itemName, digit)
          self.prompt = f'{self.prompt}, {prompt}'
          self.phone_number_table[digit] = phone_number
          self.valid_inputs = f'{self.valid_inputs}{digit}'

  def get_prompt(self):
      return self.prompt

  def get_valid_digits(self):
      return self.valid_inputs

  def get_phone_number_from_digit(self, digit):
      if (digit in self.phone_number_table):
          return self.phone_number_table[digit]
      else:
          return False
```

<Callout type="info">
  After pasting the above content, Kindly check and remove any new line added

#### Instantiating the IVR class

The app uses a basic JSON configuration file `ivrConfig.json`

```json theme={null}
{
    "intro": "Thank you for calling the Weather Hotline.",
    "iterable": "For weather in %s press %s",
    "items":  [
        {
            "itemName": "Chicago, Illinois",
            "phoneNumber": "+18158340675"
        },
        {
            "itemName": "Raleigh, North Carolina",
            "phoneNumber": "+19193261052"
        }
    ]
}
```

<Callout type="info">
  After pasting the above content, Kindly check and remove any new line added

To Instantiate the IVR class we'll need to:

1. Read the file
2. Covert the JSON to a dict
3. Create the class

```python theme={null}
import json

def open_IVR_config_json(file_name):
    with open(file_name) as json_file:
        data = json.load(json_file)
        return data

ivr_config = open_IVR_config_json('ivrConfig.json')
my_ivr = IVR(intro = ivr_config['intro'],
            iterable = ivr_config['iterable'],
            items = ivr_config['items'])
```

<Callout type="info">
  After pasting the above content, Kindly check and remove any new line added

We'll use the `my_ivr` as a global variable for the Flask route to generate prompt strings and check the user pressed digits.

```python theme={null}
import telnyx
import os
import base64
import json
from flask import Flask, request, Response
from dotenv import load_dotenv
from ivr import IVR

load_dotenv()
telnyx.api_key = os.getenv('TELNYX_API_KEY')

def open_IVR_config_json(file_name):
    with open(file_name) as json_file:
        data = json.load(json_file)
        return data

ivr_config = open_IVR_config_json('ivrConfig.json')
my_ivr = IVR(intro = ivr_config['intro'],
            iterable = ivr_config['iterable'],
            items = ivr_config['items'])

app = Flask(__name__)

@app.route('/Callbacks/Voice/Inbound', methods=['POST'])
def respond():
    global my_ivr
    data = request.json.get('data')
    print(data)

    if data.get('record_type') == 'event':
        # Check event type
        event = data.get('event_type')
        print(event, flush=True)
        call_control_id = data.get('payload').get('call_control_id')
        my_call = telnyx.Call()
        my_call.call_control_id = call_control_id
        if event == 'call.initiated':
            print("Incoming call", flush=True)

    return Response(status=200)
```

<Callout type="info">
  After pasting the above content, Kindly check and remove any new line added

### Answering the Incoming Call

Now, we can add a simple Call command to answer the incoming call. Underneath where we check if the event is `call_initiated`. To keep track of which call is which; we'll set the direction to the `client_state` using pythons native base64 encoding.

👀 At the **top** ⬆️ of the `app.py` file add `import base64`

```python theme={null}
if event == 'call.initiated':
    direction = data.get('payload').get('direction')
    if (direction == 'incoming'):
        encoded_client_state = base64.b64encode(direction.encode('ascii'))
        client_state_str = str(encoded_client_state, 'utf-8')
        res = my_call.answer(client_state=client_state_str)
        print(res, flush=True)
```

<Callout type="info">
  After pasting the above content, Kindly check and remove any new line added

This code snippet does a few things:

1. Base64encodes the direction value
2. Sets as client\_state
3. actually answers the call.

### Presenting options

Now that we have answered the call, we can use the `Gather Using Speak` command to present some options to the user. To do this, we will check the event **and** check to see that `client_state` exists. The outbound transferred call leg will also emit the `call.answered` event; however, the `client_state` value will be null. Otherwise, the called party would also be presented with the gather prompt.

```python theme={null}
elif event == 'call.answered':
    client_state = data.get('payload').get('client_state')
    if (client_state):
        speak_str = my_ivr.get_prompt()
        res = my_call.gather_using_speak(
            payload=speak_str,
            valid_digits=my_ivr.get_valid_digits(),
            language = 'en-US',
            voice = 'male')
        print(res, flush=True);
```

<Callout type="info">
  After pasting the above content, Kindly check and remove any new line added

Using the `my_ivr` object we created earlier, we can send `Gather Using Speak` audio to the number. This code present the caller with the generated prompt `my_ivr.get_prompt()`

### Interpreting button presses

Our next check will be to see what digit is pressed when the gather has completed & sends the `call.gather.ended` event. We'll extract the digits from the payload and use our instantiated IVR class to lookup the transfer number.

Finally, we'll send the transfer command to Telnyx to transfer the user to their destination.

```python theme={null}
