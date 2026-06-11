---
title: Telnyx Inference
summary: Telnyx Inference provides an OpenAI-compatible API for large language model
  chat completions, function calling, embeddings, and clustering, alongside AI Insights
  for conversation analysis and Voice AI Assistants for telephony-based conversational
  agents. This page covers the core API, integrations, data residency, and practical
  tutorials.
sources:
- url: https://developers.telnyx.com/docs/inference/ai-insights/creating-insights/index
  content_hash: ff522f2e6bd1723aaae77aa0136c8445286d925413287656782da4be07d09f11
- url: https://developers.telnyx.com/docs/inference/ai-insights/insight-groups
  content_hash: 7b522bb1ea6820875819e42eeb02ef42c22beea5981ac6d32e5415b96292655b
- url: https://developers.telnyx.com/docs/inference/ai-insights/structured-insights
  content_hash: 50e16a3392164849e8db62587e0a7d5fdc2f38c5f7bf22efbf8816070480878f
- url: https://developers.telnyx.com/docs/inference/ai-insights/use-cases
  content_hash: 0bf1cdff1a2e68b76975f93b097d45c41337877c1dbbba2397ea493699f9fd35
- url: https://developers.telnyx.com/docs/inference/ai-outfit-recommender
  content_hash: 35e09b760fc2688800b0cbec4812a2b908b2893f4c2b014c4c85e4b020cfe572
- url: https://developers.telnyx.com/docs/inference/clusters
  content_hash: 2168a5dbf3b8c93576ac5ca7eb6daef42850a48d2787e29743f161a668bc6b0d
- url: https://developers.telnyx.com/docs/inference/crewai
  content_hash: bb1baccf1e6687a03af6f732aaceb0e310beb83d0b6ce6aa7f9cb934418a351b
- url: https://developers.telnyx.com/docs/inference/data-residency
  content_hash: 5ec98630f8132d215237b19167267f10bf0a0afc3879a204570c1e18258b6c5b
- url: https://developers.telnyx.com/docs/inference/embeddings
  content_hash: da55ec529bd85eaa5fbcc3baac0d1b3d0c01b0d70cc62a03854a507fe8accdf0
- url: https://developers.telnyx.com/docs/inference/functions
  content_hash: d8787dd1d761b9535b4b844287b039a25c7cc0a895592a3309b5da4b3f1ceb15
- url: https://developers.telnyx.com/docs/inference/getting-started/index
  content_hash: 91d21b775b382bcbd90ae079c0b93ca3854a5cfea589b985c25e9a151ea79b45
updated_at: 2026-06-11T10:33:19Z
---

# Telnyx Inference

*Part 6 of 6 — see also: [Part 1](telnyx-inference--part-1.md), [Part 2](telnyx-inference--part-2.md), [Part 3](telnyx-inference--part-3.md), [Part 4](telnyx-inference--part-4.md), [Part 5](telnyx-inference--part-5.md)*

Telnyx Inference provides an OpenAI-compatible API for large language model chat completions, function calling, embeddings, and clustering, alongside AI Insights for conversation analysis and Voice AI Assistants for telephony-based conversational agents. This page covers the core API, integrations, data residency, and practical tutorials.

## AI Outfit Recommender Tutorial

This tutorial combines the OpenMeteo weather API, Telnyx Inference, and Telnyx SMS to send daily outfit recommendations via text message.

### Step 1: Check the Weather

Use the free [OpenMeteo API](https://open-meteo.com/) to get the current temperature and weather code:

```python
import requests

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
        0: "Clear sky", 1: "Mainly clear", 2: "Partly cloudy", 3: "Overcast",
        45: "Fog", 48: "Depositing rime fog",
        51: "Light drizzle", 53: "Moderate drizzle", 55: "Dense drizzle",
        61: "Slight rain", 63: "Moderate rain", 65: "Heavy rain",
        71: "Slight snow fall", 73: "Moderate snow fall", 75: "Heavy snow fall", 77: "Snow grains",
        80: "Slight rain showers", 81: "Moderate rain showers", 82: "Violent rain showers",
        85: "Slight snow showers", 86: "Heavy snow showers",
        95: "Thunderstorm", 96: "Thunderstorm with slight hail", 99: "Thunderstorm with heavy hail",
    }
    return weather_codes.get(code, "Unknown")
```

### Step 2: Get a Recommendation from Telnyx Inference

```python
import os, json, requests

def get_clothing_recommendation(weather_data):
    url = "https://api.telnyx.com/v2/ai/openai/chat/completions"
    payload = json.dumps({
        "messages": [
            {"role": "system", "content": "You are a helpful assistant that texts me every morning with brief outfit recommendations based on the weather. Be friendly and brief."},
            {"role": "user", "content": f"The weather today is: {weather_data}. What should I wear?"},
        ],
        "model": "zai-org/GLM-5.1-FP8",
        "max_tokens": 100,
    })
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer {os.getenv('TELNYX_API_KEY')}",
    }
    response = requests.post(url, headers=headers, data=payload)
    return response.json()["choices"][0]["message"]["content"]
```

### Step 3: Send via Telnyx SMS

```python
import telnyx
telnyx.api_key = os.getenv("TELNYX_API_KEY"))

def send_sms(to_number, message):
    return telnyx.Message.create(
        from_=os.getenv("TELNYX_PHONE_NUMBER"),
        to=to_number,
        text=message,
    )
```

### Putting It Together

```python
latitude = 40.7128
longitude = -74.0060

weather_description = get_weather(latitude, longitude)
recommendation = get_clothing_recommendation(weather_description)
full_text = f"{recommendation}\n\n{weather_description}"
res = send_sms("+1YOUR_DESTINATION_NUMBER", full_text)
```

You can automate this with a cron job or task scheduler to send recommendations daily.
