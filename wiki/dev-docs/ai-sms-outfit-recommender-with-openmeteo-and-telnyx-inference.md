---
title: AI SMS Outfit Recommender with OpenMeteo and Telnyx Inference
summary: A walkthrough of building a Python script that texts the user a daily outfit
  recommendation based on the local weather, combining the free OpenMeteo forecast
  API, Telnyx Inference (chat completions), and Telnyx SMS.
sources:
- url: https://developers.telnyx.com/docs/inference/ai-outfit-recommender
updated_at: 2026-08-05T13:45:33Z
---

# AI SMS Outfit Recommender with OpenMeteo and Telnyx Inference

A walkthrough of building a Python script that texts the user a daily outfit recommendation based on the local weather, combining the free OpenMeteo forecast API, Telnyx Inference (chat completions), and Telnyx SMS.

## Overview

This project combines three services into a single daily-morning workflow:

1. Fetch the current weather from the free [OpenMeteo](https://open-meteo.com/) API.
2. Pass the weather description to [Telnyx Inference](telnyx-inference.md) to generate a brief outfit recommendation.
3. Send the recommendation to the user via [Telnyx SMS](telnyx-sms.md).

The end result is an SMS like the one shown below:

![Weather Recommendation Screenshot](https://mintcdn.com/telnyx/M104dP2YWeqFiyN4/img/telnyx-weather-sms-rec.jpg?fit=max&auto=format&n=M104dP2YWeqFiyN4&q=85&s=8b961bc50a8708a1dd32cb58742d5cc9)

## Checking the weather with OpenMeteo

[OpenMeteo](https://open-meteo.com/) is a free API that returns the current forecast for a given latitude and longitude. For this demo we only request the temperature and the WMO weather code, but other fields (humidity, wind, etc.) are available if you want to experiment.

The two helper functions below turn the raw API response into a human-readable `weather_description` string that the LLM can interpret. The weather-code dictionary maps WMO codes to plain-English conditions such as "Clear sky", "Heavy rain", or "Thunderstorm with heavy hail".

```python
def get_weather(latitude, longitude):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m,weathercode&temperature_unit=fahrenheit&timezone=auto"
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        current = data["current"]
        temperature = current["temperature_2m"]
        weathercode = current["weathercode"]
        weather_description = get_weather_description(weathercode)

        return f"Temperature: {temperature}°F, {weather_description}"
    else:
        return "Failed to fetch weather data"

def get_weather_description(code):
    weather_codes = {
        0: "Clear sky",
        1: "Mainly clear",
        2: "Partly cloudy",
        3: "Overcast",
        45: "Fog",
        48: "Depositing rime fog",
        51: "Light drizzle",
        53: "Moderate drizzle",
        55: "Dense drizzle",
        61: "Slight rain",
        63: "Moderate rain",
        65: "Heavy rain",
        71: "Slight snow fall",
        73: "Moderate snow fall",
        75: "Heavy snow fall",
        77: "Snow grains",
        80: "Slight rain showers",
        81: "Moderate rain showers",
        82: "Violent rain showers",
        85: "Slight snow showers",
        86: "Heavy snow showers",
        95: "Thunderstorm",
        96: "Thunderstorm with slight hail",
        99: "Thunderstorm with heavy hail",
    }
    return weather_codes.get(code, "Unknown")
```

Because OpenMeteo is keyed by coordinates, no API key is required. The example uses Chicago's coordinates (41.9, -87.6), but any latitude/longitude pair works.

## Getting the recommendation from Telnyx Inference

With the weather string in hand, the next step is to call [Telnyx Inference](telnyx-inference.md) to generate the outfit recommendation. Telnyx exposes a wide catalog of open-source models through its [LLM library](https://telnyx.com/products/llm-library); this example uses `zai-org/GLM-5.2` from Zhipu AI. The chat-completions endpoint is OpenAI-compatible, so the same call shape works with the official OpenAI Python or JS SDKs — see the [OpenAI Migration Guide](openai-migration-guide.md) for details.

```python
def get_clothing_recommendation(weather_data):
    url = "https://api.telnyx.com/v2/ai/openai/chat/completions"
    payload = json.dumps(
        {
            "messages": [
                {
                    "role": "system",
                    "content": "You are a helpful assistant that texts me every morning with a brief outfit recommendations based on the weather. Be friendly and brief.",
                },
                {
                    "role": "user",
                    "content": f"The weather today is: {weather_data}. What should I wear?",
                },
            ],
            "model": "zai-org/GLM-5.2",
            "max_tokens": 100,
        }
    )
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer {os.getenv('TELNYX_API_KEY')}",
    }
    response = requests.post(url, headers=headers, data=payload)
    return response.json()["choices"][0]["message"]["content"]
```

Make sure `TELNYX_API_KEY` is exported in your environment so `os.getenv('TELNYX_API_KEY')` can load it. A typical response looks like:

> "Good morning. Perfect day ahead. Why not try a light, pastel-colored short-sleeved shirt, paired with some beige or light-gray shorts? Add some loafers or sneakers, and you're all set for a sunny day. Have a great one!"

## Sending the SMS

The final step is delivering the recommendation to the user's phone. The official `telnyx` Python SDK wraps the [Telnyx SMS](telnyx-sms.md) Messages API in a single call. If you have not yet provisioned a Telnyx number, follow the [Send an SMS message](send-an-sms-message.md) tutorial first.

```python
import telnyx
telnyx.api_key = os.getenv("TELNYX_API_KEY")

def send_sms(to_number, message):
    return telnyx.Message.create(
        from_=os.getenv("TELNYX_PHONE_NUMBER"),
        to=to_number,
        text=message,
    )
```

`TELNYX_PHONE_NUMBER` should be set to the Telnyx-owned number that will appear as the sender.

## Putting it all together

The driver script chains the three helpers: fetch the weather, ask the LLM for an outfit, then send the combined message.

```python
latitude = 40.7128  # Chicago latitude
longitude = -74.0060  # Chicago longitude

# Get weather data
print("Getting weather data...")
weather_description = get_weather(latitude, longitude)
print(f"Description received: {weather_description}")
to_number = "+1YOUR_DESTINATION_NUMBER"  # Example phone number

# Get clothing recommendation
print("Getting clothing recommendation...")
recommendation = get_clothing_recommendation(weather_description)
print(f"Recommendation received: {recommendation}")

full_text = f"{recommendation}\n\n{weather_description}"

# Send SMS
print("Sending SMS...")
res = send_sms(to_number, full_text)
print("SMS sent!")
```

Sample console output:

```
Getting weather data...
Description received: Temperature: 81.8°F, Clear sky

Getting clothing recommendation...
Recommendation received: Good morning. Perfect day ahead. Why not try a light, pastel-colored short-sleeved shirt, paired with some beige or light-gray shorts? Add some loafers or sneakers, and you're all set for a sunny day. Have a great one!

Sending SMS...
SMS sent!
```

## Next steps and ideas

- Add more weather attributes (humidity, wind, UV index) to the OpenMeteo request to give the model richer context.
- Tune the system prompt so the model knows your personal style, wardrobe, or dress code.
- Schedule the script to run every morning using `cron`, a task scheduler, or a serverless function.
- Swap `zai-org/GLM-5.2` for any other model in the [Telnyx Inference](telnyx-inference.md) catalog to compare tone and length.
