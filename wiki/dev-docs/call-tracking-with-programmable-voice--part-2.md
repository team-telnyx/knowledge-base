---
title: Call Tracking with Programmable Voice
summary: A tutorial for building a Call Tracking application using the Telnyx Programmable
  Voice API and Numbers API, available in both Python (Flask) and Node.js (Express).
  The app searches and orders local phone numbers, forwards inbound calls to designated
  destinations, and stores call metadata. The page also covers command retry best
  practices for handling 5XX errors, latency, and duplicate webhooks.
sources:
- url: https://developers.telnyx.com/docs/voice/programmable-voice/call-tracking
- url: https://developers.telnyx.com/docs/voice/programmable-voice/command-retries
updated_at: 2026-08-05T14:03:06Z
---

# Call Tracking with Programmable Voice

*Part 2 of 4 — see also: [Part 1](call-tracking-with-programmable-voice--part-1.md), [Part 3](call-tracking-with-programmable-voice--part-3.md), [Part 4](call-tracking-with-programmable-voice--part-4.md)*

A tutorial for building a Call Tracking application using the Telnyx Programmable Voice API and Numbers API, available in both Python (Flask) and Node.js (Express). The app searches and orders local phone numbers, forwards inbound calls to designated destinations, and stores call metadata. The page also covers command retry best practices for handling 5XX errors, latency, and duplicate webhooks.

## Python implementation

### Install dependencies

Create a project directory and virtual environment, then install the required packages:

```
mkdir call-tracking
cd call-tracking
python3 -m venv /path/to/new/virtual/environment
```

```
pip install flask
pip install flask-modus
pip install python-dotenv
pip install telnyx
pip install peewee
pip install pymysql
pip install werkzeug==0.16.1
```

The full dependency list is in the [Pipfile](https://github.com/team-telnyx/demo-python-telnyx/blob/master/flask-call-tracking_call-control/Pipfile) on GitHub.

### Environment variables

Create a `.env` file in the project root with the following values:

| Variable | Description |
| --- | --- |
| `TELNYX_API_KEY` | Your [Telnyx API Key](https://portal.telnyx.com/#/app/api-keys) |
| `TELNYX_PUBLIC_KEY` | Your [Telnyx Public Key](https://portal.telnyx.com/#/app/account/public-key) |
| `TELNYX_CONNECTION_ID` | The ID from your Call Control Application |
| `MESSAGING_PROFILE_ID` | The ID from your [Messaging Profile](https://portal.telnyx.com/#/app/messaging) |
| `DATABASE_HOST` | Database host (e.g. `localhost`) |
| `DATABASE_USER` | Database username |
| `DATABASE_PASSWORD` | Database password |
| `DATABASE_NAME` | Database name |
| `DATABASE_PORT` | Database port |

Example `.env`:

```
TELNYX_API_KEY="YOUR_API_KEY"
TELNYX_CONNECTION_ID="YOUR_CALL_CONTROL_ID"
MESSAGING_PROFILE_ID="YOUR_MESSAGING_PROFILE_ID"

DATABASE_HOST="localhost"
DATABASE_USER="root"
DATABASE_PASSWORD=""
DATABASE_NAME="cctracker"
DATABASE_PORT=""
```

### Project structure

Create the following folders and files:

```
mkdir model
mkdir static
mkdir templates

touch app.py
touch telnyx_commands.py

touch model/database.py
touch model/database_queries.py
```

- `app.py` — application entry point and Flask routes
- `telnyx_commands.py` — Telnyx helper functions
- `model/database.py` — database schema
- `model/database_queries.py` — database controller
- `static/` — CSS and JS assets
- `templates/` — HTML templates

### Telnyx helper functions

In `telnyx_commands.py`, define functions for number acquisition, deletion, CNAM lookup, and call duration calculation:

```python
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
    if number_search.metadata.total_results != 1:
        flash("No results found for specified area, try again! Watch out for typos!")
        return redirect(url_for('index'))
    number_to_order = number_search.data[0]["phone_number"]
    telnyx.NumberOrder.create(
        phone_numbers=[{"phone_number": number_to_order}],
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
        return "Not Available"
    return resource.caller_name

def difference(start_time, end_time):
    end_time = ''.join(end_time)
    start_time = ''.join(start_time)
    d1 = datetime.strptime(end_time, '%Y-%m-%dT%H:%M:%S.%fZ')
    d2 = datetime.strptime(start_time, '%Y-%m-%dT%H:%M:%S.%fZ')
    duration = math.ceil((d1 - d2).total_seconds())
    date = d2.date()
    return duration, date
```

### Database schema

In `model/database.py`, use [peewee](https://github.com/coleifer/peewee) to define two tables — `CallTracker` for call records and `ForwardedPhoneNumbers` for number-to-destination bindings:

```python
import os
from dotenv import load_dotenv
from peewee import *

load_dotenv()

mysql_db = MySQLDatabase(
    os.getenv('DATABASE_NAME'),
    user=os.getenv('DATABASE_USER'),
    password=os.getenv('DATABASE_PASSWORD'),
    host=os.getenv('DATABASE_HOST'),
    port=int(os.getenv('DATABASE_PORT')),
)

class BaseModel(Model):
    class Meta:
        database = mysql_db

class CallTracker(BaseModel):
    from_cnam_lookup = CharField()
    from_number = CharField()
    purchased_number = CharField()
    forward_number = CharField()
    date = CharField()
    duration_of_call = CharField()

class ForwardedPhoneNumbers(BaseModel):
    purchased_number = CharField()
    city_state = CharField()
    forward_number = CharField()
    tag = TextField()

if __name__ == "__main__":
    mysql_db.connect()
    mysql_db.create_tables([CallTracker, ForwardedPhoneNumbers])
    print('Created tables! (or they already exist)')
```

Run `python model/database.py` once to create the tables. Make sure the MySQL schema exists first (for example, in MySQL Workbench).

### Flask routes

In `app.py`, define five routes:

- `/` — homepage that renders `index.html`
- `/number/` — search and order a number (`POST`)
- `/number/<id>/` — update or delete a binding (`PATCH` / `DELETE`)
- `/call/<id>/` — delete a call record (`DELETE`)
- `/call-control/inbound` — handle inbound call webhooks
- `/call-control/outbound` — handle outbound leg webhooks

[Flask-modus](https://github.com/rhyselsmore/flask-modus) is used to enable `PATCH` and `DELETE` methods natively.

```python
import telnyx
import os
import json
from dotenv import load_dotenv
from flask import Flask, render_template, request, Response, redirect, url_for, flash
from flask_modus import Modus
from urllib.parse import urlunsplit
from model.database_queries import (
    db_fetch_data, db_number_insert, db_number_update,
    db_number_row_identifier, db_number_delete, db_call_delete,
    db_number_forward_fetch, db_call_insert,
)
from telnyx_commands import (
    telnyx_number_acquire, telnyx_number_delete,
    telnyx_cnam_lookup, difference,
)

load_dotenv()

app = Flask(__name__)
modus = Modus(app)
app.secret_key = "SecretKey"

@app.route('/')
def index():
    all_phone_numbers, all_call_data = db_fetch_data()
    return render_template('index.html',
                           all_phone_numbers=all_phone_numbers,
                           all_call_data=all_call_data)

@app.route("/number/", methods=['POST'])
def acquire():
    locality = request.form["city"]
    administrative_area = request.form["state"]
    forward_number = request.form["forward_number"]
    tag = request.form["tag"]
    city_state_combo = locality + ", " + administrative_area

    number_to_order, city_state_combo = telnyx_number_acquire(locality, administrative_area)
    db_number_insert(number_to_order, city_state_combo, forward_number, tag)
    flash("Phone Number: " + number_to_order + " Was Purchased Successfully!")
    return redirect(url_for('index'))

@app.route("/number/<id>/", methods=['PATCH', 'DELETE'])
def update(id):
    try:
        if request.method == b'PATCH':
            id = request.form.get('id')
            updated_forward_number = request.form["forward_number"]
            updated_tag = request.form["tag"]
            phone_number = db_number_update(id, updated_forward_number, updated_tag)
            flash("Phone Number " + phone_number + " Was Updated Successfully")
        elif request.method == b'DELETE':
            number_to_delete = db_number_row_identifier(id)
            telnyx_number_delete(number_to_delete)
            db_number_delete(id)
            flash("Phone Number " + number_to_delete + " Successfully Deleted")
    except Exception as e:
        print("Error updating database")
        print(e)
    return redirect(url_for('index'))

@app.route("/call/<id>/", methods=['DELETE'])
def delete_call(id):
    if request.method == b'DELETE':
        db_call_delete(id)
        flash("Call Record Successfully Deleted!")
    return redirect(url_for('index'))

def handle_call_answered(call, called_number):
    number_to_forward_to = db_number_forward_fetch(called_number)
    webhook_url = urlunsplit((request.scheme, request.host, "/call-control/outbound", "", ""))
    call.transfer(to=number_to_forward_to, webhook_url=webhook_url)

@app.route("/call-control/inbound", methods=["POST"])
def inbound_call():
    body = json.loads(request.data)
    calling_number = body["data"]["payload"]["from"]
    called_number = body["data"]["payload"]["to"]
    call_control_id = body["data"]["payload"]["call_control_id"]
    call_session_id = body["data"]["payload"]["call_session_id"]
    call_leg_id = body["data"]["payload"]["call_leg_id"]
    event_type = body["data"]["event_type"]

    call = telnyx.Call()
    call.call_control_id = call_control_id

    try:
        if event_type == "call.initiated":
            call = telnyx.Call(connection_id=os.getenv("TELNYX_CONNECTION_ID"))
            call.call_control_id = body["data"]["payload"]["call_control_id"]
            call.answer()
        elif event_type == "call.answered":
            handle_call_answered(call, called_number)
        elif event_type == "call.hangup":
            cnam_info = telnyx_cnam_lookup(calling_number)
            end_time = ''.join(body["data"]["payload"]["end_time"])
            start_time = ''.join(body["data"]["payload"]["start_time"])
            duration, date = difference(start_time, end_time)
            forward_number = db_number_forward_fetch(called_number)
            db_call_insert(cnam_info, calling_number, called_number, forward_number, date, duration)
    except Exception as e:
        print("Error processing webhook")
        print(e)
    return Response(status=200)

@app.route("/call-control/outbound", methods=["POST"])
def outbound_call():
    body = json.loads(request.data)
    call_leg_id = body["data"]["payload"]["call_leg_id"]
    print(f"Received call_control event with call_leg_id: {call_leg_id}")
    return Response(status=200)

if __name__ == "__main__":
    telnyx.api_key = os.getenv("TELNYX_API_KEY")
    app.run(port=8000)
```

The `/call-control/inbound` route is the heart of the app — it [answers the inbound call](/api-reference/call-commands/answer-call), [transfers it](/api-reference/call-commands/transfer-call#transfer-call) to the destination stored in the database, and persists the [hangup event](https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/hangup/index#hangup) for analytics. Saving `call_control_id` and `call_session_id` is useful when troubleshooting with Telnyx support.

### Front-end

The reference UI uses [Bootstrap](https://getbootstrap.com/) and [Nunjucks](https://mozilla.github.io/nunjucks/). The full templates and assets are in the [static](https://github.com/team-telnyx/demo-python-telnyx/tree/master/flask-call-tracking_call-control/static) and [templates](https://github.com/team-telnyx/demo-python-telnyx/tree/master/flask-call-tracking_call-control/templates) folders on GitHub.

### Run the Python app

1. Launch ngrok: `./ngrok http 8000`
2. In the Portal, edit your Call Control Application and set the webhook URL to `<ngrok-url>/call-control/inbound`.
3. Start the server: `python app.py`

You can now search and purchase numbers, bind them to forwarding numbers, and view call records in the UI.
