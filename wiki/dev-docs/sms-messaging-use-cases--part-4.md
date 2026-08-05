---
title: SMS Messaging Use Cases
summary: Practical guides for building common SMS workflows on the Telnyx Messaging
  API, including two-factor authentication, advanced opt-in/opt-out management, alphanumeric
  sender IDs, and automated appointment reminders.
sources:
- url: https://developers.telnyx.com/docs/messaging/messages/2fa/index
- url: https://developers.telnyx.com/docs/messaging/messages/advanced-opt-in-out/index
- url: https://developers.telnyx.com/docs/messaging/messages/alphanumeric-sender-id/index
- url: https://developers.telnyx.com/docs/messaging/messages/appointment-reminder
updated_at: 2026-08-05T13:55:24Z
---

# SMS Messaging Use Cases

*Part 4 of 5 — see also: [Part 1](sms-messaging-use-cases--part-1.md), [Part 2](sms-messaging-use-cases--part-2.md), [Part 3](sms-messaging-use-cases--part-3.md), [Part 5](sms-messaging-use-cases--part-5.md)*

Practical guides for building common SMS workflows on the Telnyx Messaging API, including two-factor authentication, advanced opt-in/opt-out management, alphanumeric sender IDs, and automated appointment reminders.

## Appointment Reminders via SMS

Reduce no-shows by sending automated SMS appointment reminders with the Telnyx Messaging API. This covers scheduling strategies, message templates, opt-out handling, and timing best practices.

### Send an appointment reminder

**Python**

```python
import os
from datetime import datetime

from telnyx import Telnyx

client = Telnyx(api_key=os.environ.get("TELNYX_API_KEY"))

def send_reminder(to: str, patient_name: str, appointment_time: datetime, location: str):
    formatted_time = appointment_time.strftime("%A, %B %d at %I:%M %p")
    response = client.messages.send(
        from_=os.environ.get("TELNYX_FROM_NUMBER"),
        to=to,
        text=(
            f"Hi {patient_name}, this is a reminder for your appointment "
            f"on {formatted_time} at {location}. "
            f"Reply CONFIRM to confirm or CANCEL to cancel."
        ),
    )
    return response.data
```

**Node**

```javascript
import Telnyx from 'telnyx';

const client = new Telnyx({ apiKey: process.env.TELNYX_API_KEY });

async function sendReminder(to, patientName, appointmentTime, location) {
  const formatted = appointmentTime.toLocaleDateString('en-US', {
    weekday: 'long', month: 'long', day: 'numeric',
    hour: 'numeric', minute: '2-digit',
  });
  const response = await client.messages.send({
    from: process.env.TELNYX_FROM_NUMBER,
    to,
    text: `Hi ${patientName}, this is a reminder for your appointment on ${formatted} at ${location}. Reply CONFIRM to confirm or CANCEL to cancel.`,
  });
  return response.data;
}
```

**Ruby**

```ruby
require "telnyx"

Telnyx.api_key = ENV["TELNYX_API_KEY"]

def send_reminder(to:, patient_name:, appointment_time:, location:)
  formatted = appointment_time.strftime("%A, %B %d at %I:%M %p")
  Telnyx::Message.create(
    from: ENV["TELNYX_FROM_NUMBER"],
    to: to,
    text: "Hi #{patient_name}, this is a reminder for your appointment " \
          "on #{formatted} at #{location}. " \
          "Reply CONFIRM to confirm or CANCEL to cancel."
  )
end
```

**Go**

```go
package main

import (
	"context"
	"fmt"
	"os"
	"time"

	"github.com/team-telnyx/telnyx-go"
	"github.com/team-telnyx/telnyx-go/option"
)

func sendReminder(client *telnyx.Client, to, name, location string, apptTime time.Time) error {
	formatted := apptTime.Format("Monday, January 2 at 3:04 PM")
	_, err := client.Messages.Send(context.TODO(), telnyx.MessageSendParams{
		From: os.Getenv("TELNYX_FROM_NUMBER"),
		To:   to,
		Text: fmt.Sprintf(
			"Hi %s, this is a reminder for your appointment on %s at %s. "+
				"Reply CONFIRM to confirm or CANCEL to cancel.",
			name, formatted, location),
	})
	return err
}
```

**Java**

```java
package com.telnyx.example;

import com.telnyx.sdk.client.TelnyxClient;
import com.telnyx.sdk.client.okhttp.TelnyxOkHttpClient;
import com.telnyx.sdk.models.messages.MessageSendParams;

import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;

public final class AppointmentReminder {
    private static final DateTimeFormatter FORMATTER =
        DateTimeFormatter.ofPattern("EEEE, MMMM d 'at' h:mm a");

    public static String sendReminder(String to, String name,
                                       LocalDateTime apptTime, String location) {
        TelnyxClient client = TelnyxOkHttpClient.fromEnv();
        String formatted = apptTime.format(FORMATTER);
        var params = MessageSendParams.builder()
            .from(System.getenv("TELNYX_FROM_NUMBER"))
            .to(to)
            .text(String.format(
                "Hi %s, this is a reminder for your appointment on %s at %s. " +
                "Reply CONFIRM to confirm or CANCEL to cancel.",
                name, formatted, location))
            .build();
        var response = client.messages().send(params);
        return response.data().id();
    }
}
```

**.NET**

```csharp
using Telnyx;

TelnyxConfiguration.SetApiKey(Environment.GetEnvironmentVariable("TELNYX_API_KEY"));

async Task SendReminderAsync(string to, string name, DateTime apptTime, string location)
{
    var formatted = apptTime.ToString("dddd, MMMM d 'at' h:mm tt");
    var service = new MessageService();
    await service.SendAsync(new MessageSendOptions
    {
        From = Environment.GetEnvironmentVariable("TELNYX_FROM_NUMBER"),
        To = to,
        Text = $"Hi {name}, this is a reminder for your appointment on {formatted} at {location}. " +
               "Reply CONFIRM to confirm or CANCEL to cancel."
    });
}
```

**PHP**

```php
require_once 'vendor/autoload.php';

\Telnyx\Telnyx::setApiKey(getenv('TELNYX_API_KEY'));

function sendReminder(string $to, string $name, DateTime $apptTime, string $location): void
{
    $formatted = $apptTime->format('l, F j \a\t g:i A');
    \Telnyx\Message::Create([
        'from' => getenv('TELNYX_FROM_NUMBER'),
        'to' => $to,
        'text' => "Hi {$name}, this is a reminder for your appointment "
            . "on {$formatted} at {$location}. "
            . "Reply CONFIRM to confirm or CANCEL to cancel.",
    ]);
}
```

### Scheduling strategies

Choose a scheduling approach based on your application's requirements.

**Telnyx Scheduled Messages.** The simplest approach — use the Telnyx API's built-in [scheduled messaging](scheduled-messaging.md) feature. No external scheduler needed.

```python
from datetime import datetime, timedelta, timezone

reminder_time = appointment_time - timedelta(hours=24)

response = client.messages.send(
    from_=os.environ.get("TELNYX_FROM_NUMBER"),
    to="+15559876543",
    text="Reminder: You have an appointment tomorrow at 2:30 PM.",
    send_at=reminder_time.astimezone(timezone.utc).isoformat(),
)
```

Pros: No infrastructure needed, simple API call. Cons: Limited to a single scheduled time per API call, max 7 days in advance.

**Cron / Job Scheduler.** Run a periodic job (e.g., every hour) that queries your database for upcoming appointments and sends reminders.

```python
from datetime import datetime, timedelta

def send_pending_reminders():
    now = datetime.now()
    window_start = now + timedelta(hours=23)
    window_end = now + timedelta(hours=25)

    appointments = db.query(
        "SELECT * FROM appointments "
        "WHERE start_time BETWEEN %s AND %s "
        "AND reminder_sent = FALSE",
        (window_start, window_end)
    )

    for appt in appointments:
        send_reminder(
            to=appt.phone,
            patient_name=appt.name,
            appointment_time=appt.start_time,
            location=appt.location,
        )
        db.execute(
            "UPDATE appointments SET reminder_sent = TRUE WHERE id = %s",
            (appt.id,)
        )
```

Pros: Full control, supports multiple reminder windows, database-driven. Cons: Requires job scheduler infrastructure (cron, Celery, Bull, etc.).

**Event-Driven Queue.** Schedule individual reminder jobs when appointments are created using a task queue like Celery (Python), Bull (Node), or Sidekiq (Ruby).

```python
from celery import Celery
from datetime import timedelta

celery_app = Celery('reminders', broker='redis://localhost:6379')

@celery_app.task
def send_scheduled_reminder(phone, name, time_str, location):
    appointment_time = datetime.fromisoformat(time_str)
    send_reminder(to=phone, patient_name=name,
                  appointment_time=appointment_time, location=location)

def on_appointment_created(appointment):
    reminder_time = appointment.start_time - timedelta(hours=24)
    send_scheduled_reminder.apply_async(
        args=[appointment.phone, appointment.name,
              appointment.start_time.isoformat(), appointment.location],
        eta=reminder_time,
    )
```

Pros: Precise timing, scalable, handles cancellations. Cons: Requires message queue infrastructure (Redis, RabbitMQ).

### Handle replies (confirm / cancel)

Set up a webhook to receive replies and update appointment status:

**Python (Flask)**

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/webhooks/messaging", methods=["POST"])
def handle_webhook():
    data = request.json["data"]
    if data["event_type"] != "message.received":
        return jsonify({"status": "ignored"}), 200

    payload = data["payload"]
    from_number = payload["from"]["phone_number"]
    text = payload["text"].strip().upper()

    if text == "CONFIRM":
        db.execute(
            "UPDATE appointments SET status = 'confirmed' WHERE phone = %s "
            "AND start_time > NOW()",
            (from_number,)
        )
        client.messages.send(
            from_=os.environ.get("TELNYX_FROM_NUMBER"),
            to=from_number,
            text="Your appointment has been confirmed. See you then!",
        )
    elif text == "CANCEL":
        db.execute(
            "UPDATE appointments SET status = 'cancelled' WHERE phone = %s "
            "AND start_time > NOW()",
            (from_number,)
        )
        client.messages.send(
            from_=os.environ.get("TELNYX_FROM_NUMBER"),
            to=from_number,
            text="Your appointment has been cancelled. "
                 "Please call us to reschedule.",
        )
    return jsonify({"status": "ok"}), 200
```

**Node (Express)**

```javascript
import express from 'express';

const app = express();
app.use(express.json());

app.post('/webhooks/messaging', async (req, res) => {
  const { data } = req.body;
  if (data.event_type !== 'message.received') {
    return res.json({ status: 'ignored' });
  }
  const fromNumber = data.payload.from.phone_number;
  const text = data.payload.text.trim().toUpperCase();

  if (text === 'CONFIRM') {
    await db.query(
      `UPDATE appointments SET status = 'confirmed'
       WHERE phone = $1 AND start_time > NOW()`,
      [fromNumber]
    );
    await client.messages.send({
      from: process.env.TELNYX_FROM_NUMBER,
      to: fromNumber,
      text: 'Your appointment has been confirmed. See you then!',
    });
  } else if (text === 'CANCEL') {
    await db.query(
      `UPDATE appointments SET status = 'cancelled'
       WHERE phone = $1 AND start_time > NOW()`,
      [fromNumber]
    );
    await client.messages.send({
      from: process.env.TELNYX_FROM_NUMBER,
      to: fromNumber,
      text: 'Your appointment has been cancelled. Please call us to reschedule.',
    });
  }
  res.json({ status: 'ok' });
});
```

### Opt-out handling

You must honor opt-out requests. Telnyx automatically handles STOP/UNSTOP keywords for 10DLC and Toll-Free numbers, but you should also track opt-outs in your application.

**Automatic opt-out (Telnyx managed).** Telnyx automatically handles standard opt-out keywords (`STOP`, `UNSUBSCRIBE`, `CANCEL`, `END`, `QUIT`) for US long codes and toll-free numbers. When a user texts STOP:

1. Telnyx sends an automatic reply confirming the opt-out
2. Future messages to that number are blocked at the carrier level
3. You receive a `message.received` webhook with the STOP keyword

See [Advanced Opt-In/Out](advanced-opt-in-out.md) for customization options.

**Application-level opt-out tracking.** In addition to Telnyx's automatic handling, track opt-outs in your database to prevent scheduling reminders for opted-out users:

```python
def handle_opt_out(phone_number: str):
    db.execute(
        "UPDATE patients SET sms_opted_out = TRUE WHERE phone = %s",
        (phone_number,)
    )
    db.execute(
        "DELETE FROM scheduled_reminders WHERE phone = %s AND sent = FALSE",
        (phone_number,)
    )

def can_send_reminder(phone_number: str) -> bool:
    result = db.query(
        "SELECT sms_opted_out FROM patients WHERE phone = %s",
        (phone_number,)
    )
    return result and not result.sms_opted_out
```

### Timing best practices

1. **Send reminders at appropriate times.**
   - 24 hours before: primary reminder — enough time to cancel/reschedule
   - 2–3 hours before: final reminder for same-day appointments
   - Avoid late night/early morning: only send between 9 AM and 8 PM in the recipient's local time zone

2. **Use multiple reminder windows.** For high-value appointments (medical, legal), send two reminders: 48 or 24 hours before (gives time to reschedule) and 2–3 hours before (final confirmation). For routine appointments (salon, auto service), a single reminder 24 hours before is usually sufficient.

3. **Respect time zones.** Always calculate reminder times in the recipient's local time zone. Sending a reminder at 3 AM is worse than not sending one at all.

```python
from zoneinfo import ZoneInfo

patient_tz = ZoneInfo(patient.timezone)  # e.g., "America/New_York"
local_time = reminder_time.astimezone(patient_tz)

if 9 <= local_time.hour < 20:
    send_reminder(...)
else:
    next_9am = local_time.replace(hour=9, minute=0)
    if next_9am < local_time:
        next_9am += timedelta(days=1)
    schedule_reminder_at(next_9am, ...)
```

4. **Keep messages concise.** SMS has character limits. Keep reminders under 160 characters (1 segment) when possible to minimize costs. Include only essential info: patient name, date and time, location (short form), and reply instructions.

### Message templates

Example templates for different industries:

**Healthcare:**

```
Hi {name}, reminder: your appointment with Dr. {provider} is on {date} at {time}.
Reply CONFIRM or CANCEL. Call {phone} to reschedule.
```

**Dental:**

```
{name}, your dental cleaning at {practice} is tomorrow at {time}.
Please arrive 10 min early. Reply C to confirm, X to cancel.
```

**Salon / Spa:**

```
Hi {name}! Your {service} appointment is {date} at {time}.
Reply YES to confirm or call {phone} to reschedule.
```

**Auto Service:**

```
{name}, your vehicle service at {shop} is scheduled for {date} at {time}.
Reply OK to confirm.
```

**Legal / Financial:**

```
Reminder: Your meeting with {advisor} is on {date} at {time} at {location}.
Please bring required documents. Reply CONFIRM to confirm.
```
