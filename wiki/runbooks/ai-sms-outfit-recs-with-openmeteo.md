---
title: AI SMS Outfit Recs with OpenMeteo
summary: Telnyx Inference + AI offering SMS outfit recommendations using LLMs like Llama-3.1 based on the weather using OpenMeteo.
sources:
  - url: https://developers.telnyx.com/docs/inference/ai-outfit-recommender/index
    content_hash: ac4cc95bcc5b5b848488502d03b6ece4cbff055f5bbcebfc62f39316f97cd0f8
updated_at: 2026-04-10T00:00:00Z
---

# AI SMS Outfit Recs with OpenMeteo

Telnyx Inference + AI offering SMS outfit recommendations using LLMs like Llama-3.1 based on the weather using OpenMeteo

Today we will be making a fun script to text us a nice recommendation for outfits based on the weather every morning. It will look something like this at the end:

<img alt="Weather Recommendation Screenshot" />

This project has 3 main components:

1. Check the weather using the free OpenMeteo API
2. Pass the weather info to Telnyx Inference using the model of our choice
3. Send the recommendation to the user using Telnyx SMS

Let’s get started!

## Checking the weather with OpenMeteo

[OpenMeteo](https://open-meteo.com/) is a great free API that allows you to retrieve the forecast for the current day. They have a ton of options for what you can retrieve, but for this demo, we will stick with just the temperature and weather code (although feel free to experiment with other things like humidity!).

The following functions can be used to retrieve a weather\_description that we can feed into our Telnyx Inference model:

```python theme={null}
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

It looks like a lot of code, but the majority is just converting the weather codes to a nicely formatted string that the model will be able to understand. Notice also that the longitude and latitude are required to skip the need for an API key, so we will use Chicago’s latitude and longitude, 41.9 and 87.6 for this example.

## Getting our recommendation text from Telnyx Inference Meta-Llama-3.1-8B

Now that we have the current weather, let’s make a call to Telnyx Inference to generate a text to send to our user. There are [many state-of-the-art open source models available through the Telnyx API](https://telnyx.com/products/llm-library), so for this one we will select a powerful small model: [Meta's Llama-3.1-8B-Instruct](https://llama.meta.com/).

Let’s write a function to retrieve a good weather recommendation from Telnyx Inference. We will just use the `requests` library to not add an additional pip requirement, but the Telnyx LLM API is also compatible with the OpenAI Python and JS SDKs, see the [OpenAI Migration Guide Here](https://developers.telnyx.com/docs/inference/openai).

```python theme={null}
def get_clothing_recommendation(weather_data):
    url = "https://api.telnyx.com/v2/ai/chat/completions"
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
            "model": "meta-llama/Meta-Llama-3.1-8B-Instruct",
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

Make sure your `TELNYX_API_KEY` is set in your environment variables so that they can be loaded with `os.getenv(‘TELNYX_API_KEY’)`. The API spec for chat completions can be found here if you would prefer to use HTTP requests instead of the OpenAI client or want to play around with some of the LLM parameters offered.

The output of this function will be a string with our recommendation, for example:

“Good morning. Perfect day ahead. Why not try a light, pastel-colored short-sleeved shirt, paired with some beige or light-gray shorts? Add some loafers or sneakers, and you're all set for a sunny day. Have a great one!”

## Sending our text to the user

Great! Now that we have our weather and text recommendation, we can send the text to the user. Sending a message with Telnyx SMS is easy, follow the [tutorial here if you have not set up a Telnyx number yet](https://developers.telnyx.com/docs/messaging/messages/send-message). We can use the following snippet to send a text using Telnyx:

```python theme={null}
import telnyx
telnyx.api_key = os.getenv("TELNYX_API_KEY")

def send_sms(to_number, message):
    return telnyx.Message.create(
        from_=os.getenv("TELNYX_PHONE_NUMBER"),
        to=to_number,
        text=message,
    )
```

## Putting it all together

Now that we have all the pieces in place, let's run the script! We can use the following sequence to chain everything together:

```python theme={null}
latitude = 40.7128  # Chicago latitude
longitude = -74.0060  # Chicago longitude
