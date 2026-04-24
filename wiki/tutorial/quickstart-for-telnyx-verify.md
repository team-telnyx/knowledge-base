---
title: Quickstart for Telnyx Verify
summary: Telnyx Verify helps to deliver a 2FA token to any mobile number and verify that token using Telnyx V2 API.
sources:
  - url: https://developers.telnyx.com/docs/identity/verify/quickstart/index
    content_hash: e98558ae77f86acd9134ed67a8ea6b97d41cd4cfa79a0c56a305c3643c17293e
updated_at: 2026-04-10T00:00:00Z
---

# Quickstart for Telnyx Verify

Telnyx Verify helps to deliver a 2FA token to any mobile number and verify that token using Telnyx V2 API

In this tutorial, you'll learn how to deliver a 2FA token to any mobile number and verify that token using the Telnyx v2 API. Examples are provided in **curl**, **Node.js**, **Python**, **Ruby**, **Go**, **Java**, **.NET**, and **PHP**.

***

## Prerequisites

1. **Create a Telnyx account**

    Sign up at [telnyx.com](https://telnyx.com/sign-up) if you don't have an account yet.

2. **Get your API key**

    Follow the [API Keys guide](../reference/create-and-manage-api-keys.md) to generate an API key. Set it as an environment variable:

      ```bash macOS/Linux theme={null}
      export TELNYX_API_KEY="YOUR_API_KEY"
      ```

      ```powershell
      $env:TELNYX_API_KEY = "YOUR_API_KEY"
      ```

3. **Install an SDK (optional)**

    If you prefer using an SDK over curl, install one for your language:

      ```bash Node.js theme={null}
      npm install telnyx
      ```

      ```bash
      pip install telnyx
      ```

      ```bash
      gem install telnyx
      ```

      ```bash
      go get github.com/team-telnyx/telnyx-go
      ```

      ```bash
      composer require telnyx/telnyx-php
      ```

    For **Java** and **.NET**, the examples use the standard HTTP client libraries included with the platform.

## Methods of verification

There are currently three verification methods available:

* **`sms`** - the verification code is sent in a custom or default templated message.
* **`call`** - the code is spoken aloud in a custom or default templated message when the user answers the call.
* **`flashcall`** - the verification code is embedded in the caller ID of a brief "flash" call (the call rings once and hangs up). The user's app extracts the code automatically.

***

## Create a verify profile

A Verify Profile contains several important configurations that you'll use when sending 2-factor authentication messages and receiving responses. Before you send any 2FA messages, you need a profile to go with them.

Each profile can have one of each verification method configured. It is recommended that if you wish to configure multiple applications, you use a different profile for each one.

In the below example we will set up a verification profile that can use SMS using a selected message template and speech to text calling.

### Select a message template

  ```bash
  curl --location --request GET 'https://api.telnyx.com/v2/verify_profiles/templates' \
  --header 'Authorization: Bearer YOUR_API_KEY'
  ```

  ```javascript
  import Telnyx from 'telnyx';

  const client = new Telnyx({
    apiKey: process.env['TELNYX_API_KEY'],
  });

  const templates = await client.verifyProfiles.retrieveTemplates();

  for (const template of templates.data) {
    console.log(`${template.id}: ${template.text}`);
  }
  ```

  ```python
  import os
  from telnyx import Telnyx

  client = Telnyx(api_key=os.environ.get("TELNYX_API_KEY"))

  templates = client.verify_profiles.retrieve_templates()

  for template in templates.data:
      print(f"{template.id}: {template.text}")
  ```

  ```ruby
  require "telnyx"
  require "json"
  require "net/http"
  require "uri"

  uri = URI("https://api.telnyx.com/v2/verify_profiles/templates")
  req = Net::HTTP::Get.new(uri)
  req["Authorization"] = "Bearer #{ENV['TELNYX_API_KEY']}"

  res = Net::HTTP.start(uri.hostname, uri.port, use_ssl: true) { |http| http.request(req) }
  data = JSON.parse(res.body)

  data["data"].each do |template|
    puts "#{template['id']}: #{template['text']}"
  end
  ```

  ```go
  package main

  import (
    "context"
    "fmt"
    "os"

    "github.com/team-telnyx/telnyx-go"
    "github.com/team-telnyx/telnyx-go/option"
  )

  func main() {
    client := telnyx.NewClient(option.WithAPIKey(os.Getenv("TELNYX_API_KEY")))

    templates, err := client.VerifyProfiles.RetrieveTemplates(context.TODO())
    if err != nil {
      panic(err)
    }
    for _, t := range templates.Data {
      fmt.Printf("%s: %s\n", t.ID, t.Text)
    }
  }
  ```

  ```java
  package com.telnyx.example;

  import java.net.URI;
  import java.net.http.HttpClient;
  import java.net.http.HttpRequest;
  import java.net.http.HttpResponse;

  public final class ListTemplates {
      public static void main(String[] args) throws Exception {
          HttpClient httpClient = HttpClient.newHttpClient();

          HttpRequest request = HttpRequest.newBuilder()
              .uri(URI.create("https://api.telnyx.com/v2/verify_profiles/templates"))
              .header("Authorization", "Bearer " + System.getenv("TELNYX_API_KEY"))
              .GET()
              .build();

          HttpResponse response = httpClient.send(
              request, HttpResponse.BodyHandlers.ofString()
          );
          System.out.println(response.body());
      }
  }
  ```

  ```csharp .NET theme={null}
  using System.Net.Http.Headers;

  var httpClient = new HttpClient();
  httpClient.DefaultRequestHeaders.Authorization =
      new AuthenticationHeaderValue("Bearer", Environment.GetEnvironmentVariable("TELNYX_API_KEY"));

  var response = await httpClient.GetStringAsync(
      "https://api.telnyx.com/v2/verify_profiles/templates"
  );
  Console.WriteLine(response);
  ```

  ```php
  <?php
  require_once 'vendor/autoload.php';

  $apiKey = getenv('TELNYX_API_KEY');

  $ch = curl_init('https://api.telnyx.com/v2/verify_profiles/templates');
  curl_setopt_array($ch, [
      CURLOPT_RETURNTRANSFER => true,
      CURLOPT_HTTPHEADER => [
          "Authorization: Bearer $apiKey",
      ],
  ]);
  $response = curl_exec($ch);
  curl_close($ch);

  $data = json_decode($response, true);
  foreach ($data['data'] as $template) {
      echo "{$template['id']}: {$template['text']}\n";
  }
  ```

### Example response

```json theme={null}
{
    "data": [
        {
            "id": "0abb5b4f-459f-445a-bfcd-488998b7572d",
            "text": "Your {{app_name}} verification code is: {{code}}."
        },
        {
            "id": "2ca3f1da-5621-4aa6-ae56-df21caff79e0",
            "text": "{{code}} is your verification code for {{app_name}}."
        },
        {
            "id": "33dfb056-6c1b-40bd-920e-4243e01248a5",
            "text": "Your {{app_name}} verification code is: {{code}}. Do not share this code with anyone; our employees will never ask for the code."
        },
        {
            "id": "46acd63c-be57-4993-ae8d-0e4067ad1d57",
            "text": "Your {{app_name}} verification code is: {{code}}. This code will expire in {{default_verification_timeout_secs}} minutes."
        },
        {
            "id": "723ead5e-ada6-4c29-a962-349170866187",
            "text": "{{code}} is your verification code for {{app_name}}. This code will expire in {{default_verification_timeout_secs}} minutes."
        },
        {
            "id": "88d0781f-f4c7-4b78-8d0a-1f3e4de78b5e",
            "text": "Your {{app_name}} verification code is: {{code}}. This code will expire in {{default_verification_timeout_secs}} minutes. Do not share this code with anyone; our employees will never ask for the code."
        }
    ]
}
```

<Callout type="info">
  If not selected then the default template is "Your verification code is `{code}`."

<Callout type="success" title="Create custom branded templates">
  Want to use your own branded verification messages? You can now [create custom templates](../runbooks/custom-templates-for-telnyx-verify.md) that match your brand voice and compliance requirements.

### Create a verify profile

  ```bash
  curl --location --request POST 'https://api.telnyx.com/v2/verify_profiles' \
  --header 'Content-Type: application/json' \
  --header 'Authorization: Bearer YOUR_API_KEY' \
  --data-raw '{
      "name": "foobar-en-v1",
      "language": "en-US",
      "sms": {
          "messaging_template_id": "0abb5b4f-459f-445a-bfcd-488998b7572d",
          "whitelisted_destinations": ["US", "CA"],
          "default_timeout_secs": 300,
          "code_length": 5
      },
      "call": {
          "default_timeout_secs": 600
      }
  }'
  ```

  ```javascript
  import Telnyx from 'telnyx';

  const client = new Telnyx({
    apiKey: process.env['TELNYX_API_KEY'],
  });

  const profile = await client.verifyProfiles.create({
    name: 'foobar-en-v1',
    language: 'en-US',
    sms: {
      messaging_template_id: '0abb5b4f-459f-445a-bfcd-488998b7572d',
      whitelisted_destinations: ['US', 'CA'],
      default_timeout_secs: 300,
      code_length: 5,
    },
    call: {
      default_timeout_secs: 600,
    },
  });

  console.log('Profile ID:', profile.data.id);
  console.log('Profile name:', profile.data.name);
  ```

  ```python
  import os
  from telnyx import Telnyx

  client = Telnyx(api_key=os.environ.get("TELNYX_API_KEY"))

  profile = client.verify_profiles.create(
      name="foobar-en-v1",
      language="en-US",
      sms={
          "messaging_template_id": "0abb5b4f-459f-445a-bfcd-488998b7572d",
          "whitelisted_destinations": ["US", "CA"],
          "default_timeout_secs": 300,
          "code_length": 5,
      },
      call={
          "default_timeout_secs": 600,
      },
  )

  print(f"Profile ID: {profile.data.id}")
  print(f"Profile name: {profile.data.name}")
  ```

  ```ruby
  require "telnyx"
  require "json"
  require "net/http"
  require "uri"

  uri = URI("https://api.telnyx.com/v2/verify_profiles")
  req = Net::HTTP::Post.new(uri, "Content-Type" => "application/json")
  req["Authorization"] = "Bearer #{ENV['TELNYX_API_KEY']}"
  req.body = {
    name: "foobar-en-v1",
    language: "en-US",
    sms: {
      messaging_template_id: "0abb5b4f-459f-445a-bfcd-488998b7572d",
      whitelisted_destinations: ["US", "CA"],
      default_timeout_secs: 300,
      code_length: 5
    },
    call: {
      default_timeout_secs: 600
    }
  }.to_json

  res = Net::HTTP.start(uri.hostname, uri.port, use_ssl: true) { |http| http.request(req) }
  data = JSON.parse(res.body)

  puts "Profile ID: #{data['data']['id']}"
  puts "Profile name: #{data['data']['name']}"
  ```

  ```go
  package main

  import (
    "context"
    "fmt"
    "os"

    "github.com/team-telnyx/telnyx-go"
    "github.com/team-telnyx/telnyx-go/option"
  )

  func main() {
    client := telnyx.NewClient(option.WithAPIKey(os.Getenv("TELNYX_API_KEY")))

    profile, err := client.VerifyProfiles.Create(context.TODO(), telnyx.VerifyProfileCreateParams{
      Name:     "foobar-en-v1",
      Language: telnyx.String("en-US"),
      SMS: &telnyx.VerifyProfileSMSParams{
        MessagingTemplateID:    telnyx.String("0abb5b4f-459f-445a-bfcd-488998b7572d"),
        WhitelistedDestinations: []string{"US", "CA"},
        DefaultTimeoutSecs:     telnyx.Int64(300),
        CodeLength:             telnyx.Int64(5),
      },
      Call: &telnyx.VerifyProfileCallParams{
        DefaultTimeoutSecs: telnyx.Int64(600),
      },
    })
    if err != nil {
      panic(err)
    }
    fmt.Printf("Profile ID: %s\n", profile.Data.ID)
    fmt.Printf("Profile name: %s\n", profile.Data.Name)
  }
  ```

  ```java
  package com.telnyx.example;

  import java.net.URI;
  import java.net.http.HttpClient;
  import java.net.http.HttpRequest;
  import java.net.http.HttpResponse;

  public final class CreateVerifyProfile {
      public static void main(String[] args) throws Exception {
          String body = """
              {
                  "name": "foobar-en-v1",
                  "language": "en-US",
                  "sms": {
                      "messaging_template_id": "0abb5b4f-459f-445a-bfcd-488998b7572d",
                      "whitelisted_destinations": ["US", "CA"],
                      "default_timeout_secs": 300,
                      "code_length": 5
                  },
                  "call": {
                      "default_timeout_secs": 600
                  }
              }
              """;

          HttpClient httpClient = HttpClient.newHttpClient();
          HttpRequest request = HttpRequest.newBuilder()
              .uri(URI.create("https://api.telnyx.com/v2/verify_profiles"))
              .header("Content-Type", "application/json")
              .header("Authorization", "Bearer " + System.getenv("TELNYX_API_KEY"))
              .POST(HttpRequest.BodyPublishers.ofString(body))
              .build();

          HttpResponse response = httpClient.send(
              request, HttpResponse.BodyHandlers.ofString()
          );
          System.out.println(response.body());
      }
  }
  ```

  ```csharp .NET theme={null}
  using System.Net.Http.Headers;
  using System.Text;
  using System.Text.Json;

  var httpClient = new HttpClient();
  httpClient.DefaultRequestHeaders.Authorization =
      new AuthenticationHeaderValue("Bearer", Environment.GetEnvironmentVariable("TELNYX_API_KEY"));

  var payload = new
  {
      name = "foobar-en-v1",
      language = "en-US",
      sms = new
      {
          messaging_template_id = "0abb5b4f-459f-445a-bfcd-488998b7572d",
          whitelisted_destinations = new[] { "US", "CA" },
          default_timeout_secs = 300,
          code_length = 5
      },
      call = new { default_timeout_secs = 600 }
  };

  var content = new StringContent(
      JsonSerializer.Serialize(payload), Encoding.UTF8, "application/json"
  );
  var response = await httpClient.PostAsync(
      "https://api.telnyx.com/v2/verify_profiles", content
  );
  var body = await response.Content.ReadAsStringAsync();
  Console.WriteLine(body);
  ```

  ```php
  <?php
  require_once 'vendor/autoload.php';

  $apiKey = getenv('TELNYX_API_KEY');

  $payload = json_encode([
      'name' => 'foobar-en-v1',
      'language' => 'en-US',
      'sms' => [
          'messaging_template_id' => '0abb5b4f-459f-445a-bfcd-488998b7572d',
          'whitelisted_destinations' => ['US', 'CA'],
          'default_timeout_secs' => 300,
          'code_length' => 5,
      ],
      'call' => [
          'default_timeout_secs' => 600,
      ],
  ]);

  $ch = curl_init('https://api.telnyx.com/v2/verify_profiles');
  curl_setopt_array($ch, [
      CURLOPT_RETURNTRANSFER => true,
      CURLOPT_POST => true,
      CURLOPT_POSTFIELDS => $payload,
      CURLOPT_HTTPHEADER => [
          "Authorization: Bearer $apiKey",
          'Content-Type: application/json',
      ],
  ]);
  $response = curl_exec($ch);
  curl_close($ch);

  $data = json_decode($response, true);
  echo "Profile ID: " . $data['data']['id'] . "\n";
  echo "Profile name: " . $data['data']['name'] . "\n";
  ```

### Example response

```json theme={null}
{
    "data": {
        "id": "4900017a-e7c8-e79e-0a7c-0d98f49b09cc",
        "name": "foobar-en-v1",
        "created_at": "2024-03-27T11:45:41.292913",
        "updated_at": "2024-03-27T11:45:41.292913",
        "record_type": "verify_profile",
        "sms": {
            "messaging_template_id": "0abb5b4f-459f-445a-bfcd-488998b7572d",
            "whitelisted_destinations": ["US", "CA"],
            "default_timeout_secs": 300,
            "code_length": 5
        },
        "call": {
            "default_timeout_secs": 600
        },
        "language": "en-US"
    }
}
```

<Callout type="info">
  Don't forget to set your `TELNYX_API_KEY` environment variable or replace `YOUR_API_KEY` in the curl examples.

Take note of the profile's `id` that's returned to you, you'll need it to send 2FA verifications. At any time, you can access all of your created Verify Profiles [by API](https://developers.telnyx.com/api-reference/verify/list-all-verify-profiles) as well.

You are now ready to send 2-factor authentication messages!

## Trigger a verification request

To send a verification attempt, you need the Verify Profile ID, the phone number that will receive the message, and the verification type. Choose the method that best fits your use case:

### SMS

    SMS verification sends a code via text message. This is the most common method with the widest global coverage.

      ```bash
      curl -X POST \
        --header "Content-Type: application/json" \
        --header "Accept: application/json" \
        --header "Authorization: Bearer YOUR_API_KEY" \
        --data '{"phone_number":"+13035551234","verify_profile_id":"4900017a-e7c8-e79e-0a7c-0d98f49b09cc"}' \
        https://api.telnyx.com/v2/verifications/sms
      ```

      ```javascript
      import Telnyx from 'telnyx';

      const client = new Telnyx({
        apiKey: process.env['TELNYX_API_KEY'],
      });

      const verification = await client.verifications.triggerSMS({
        phone_number: '+13035551234',
        verify_profile_id: '4900017a-e7c8-e79e-0a7c-0d98f49b09cc'
      });

      console.log('Verification ID:', verification.data.id);
      console.log('Status:', verification.data.status); // "pending"
      ```

      ```python
      import os
      from telnyx import Telnyx

      client = Telnyx(api_key=os.environ.get("TELNYX_API_KEY"))

      verification = client.verifications.trigger_sms(
          phone_number="+13035551234",
          verify_profile_id="4900017a-e7c8-e79e-0a7c-0d98f49b09cc"
      )

      print(f"Verification ID: {verification.data.id}")
      print(f"Status: {verification.data.status}")  # "pending"
      ```

      ```ruby
      require "telnyx"

      client = Telnyx::Client.new(api_key: ENV["TELNYX_API_KEY"])

      verification = client.verifications.sms(
        phone_number: "+13035551234",
        verify_profile_id: "4900017a-e7c8-e79e-0a7c-0d98f49b09cc"
      )

      puts "Verification ID: #{verification.id}"
      puts "Status: #{verification.status}" # "pending"
      ```

      ```go
      package main

      import (
        "context"
        "fmt"
        "os"

        "github.com/team-telnyx/telnyx-go"
        "github.com/team-telnyx/telnyx-go/option"
      )

      func main() {
        client := telnyx.NewClient(option.WithAPIKey(os.Getenv("TELNYX_API_KEY")))

        verification, err := client.Verifications.SMS(context.TODO(), telnyx.VerificationSMSParams{
          PhoneNumber:     "+13035551234",
          VerifyProfileID: "4900017a-e7c8-e79e-0a7c-0d98f49b09cc",
        })
        if err != nil {
          panic(err)
        }
        fmt.Printf("Verification ID: %s\n", verification.Data.ID)
        fmt.Printf("Status: %s\n", verification.Data.Status) // "pending"
      }
      ```

      ```java
      package com.telnyx.example;

      import com.telnyx.sdk.client.TelnyxClient;
      import com.telnyx.sdk.client.okhttp.TelnyxOkHttpClient;
      import com.telnyx.sdk.models.verify.VerificationParams;
      import com.telnyx.sdk.models.verify.VerificationResponse;

      public final class Main {
          public static void main(String[] args) {
              TelnyxClient client = TelnyxOkHttpClient.fromEnv();

              VerificationParams params = VerificationParams.builder()
                  .phoneNumber("+13035551234")
                  .verifyProfileId("4900017a-e7c8-e79e-0a7c-0d98f49b09cc")
                  .build();

              VerificationResponse response = client.verifications().sms(params);
              System.out.println("Verification ID: " + response.getId());
              System.out.println("Status: " + response.getStatus()); // "pending"
          }
      }
      ```

      ```csharp .NET theme={null}
      using Telnyx;

      TelnyxConfiguration.SetApiKey(Environment.GetEnvironmentVariable("TELNYX_API_KEY"));

      var service = new VerificationService();
      var response = await service.SendSmsAsync(new VerificationSmsOptions
      {
          PhoneNumber = "+13035551234",
          VerifyProfileId = "4900017a-e7c8-e79e-0a7c-0d98f49b09cc"
      });

      Console.WriteLine($"Verification ID: {response.Data.Id}");
      Console.WriteLine($"Status: {response.Data.Status}"); // "pending"
      ```

      ```php
      <?php
      require_once 'vendor/autoload.php';

      \Telnyx\Telnyx::setApiKey(getenv('TELNYX_API_KEY'));

      $verification = \Telnyx\Verification::create([
          'phone_number' => '+13035551234',
          'verify_profile_id' => '4900017a-e7c8-e79e-0a7c-0d98f49b09cc',
          'type' => 'sms'
      ]);

      echo "Verification ID: " . $verification->id . "\n";
      echo "Status: " . $verification->status . "\n"; // "pending"
      ```

    **User experience:** The user receives a text message with a numeric code (e.g., "Your verification code is: 17686"). They enter this code in your application.

### Call

    Call verification speaks the code aloud when the user answers. Useful when the user cannot receive SMS (landlines, VoIP) or in regions with unreliable SMS delivery.

    **Profile configuration for call:**

    When creating your verify profile, include the `call` configuration:

    ```bash theme={null}
    curl --location --request POST 'https://api.telnyx.com/v2/verify_profiles' \
    --header 'Content-Type: application/json' \
    --header 'Authorization: Bearer YOUR_API_KEY' \
    --data-raw '{
        "name": "my-app-call-verify",
        "language": "en-US",
        "call": {
            "default_timeout_secs": 600
        }
    }'
    ```

    **Initiate a call verification:**

      ```bash
      curl -X POST \
        --header "Content-Type: application/json" \
        --header "Accept: application/json" \
        --header "Authorization: Bearer YOUR_API_KEY" \
        --data '{"phone_number":"+13035551234","verify_profile_id":"4900017a-e7c8-e79e-0a7c-0d98f49b09cc"}' \
        https://api.telnyx.com/v2/verifications/call
      ```

      ```javascript
      const verification = await client.verifications.triggerCall({
        phone_number: '+13035551234',
        verify_profile_id: '4900017a-e7c8-e79e-0a7c-0d98f49b09cc'
      });

      console.log('Verification ID:', verification.data.id);
      console.log('Type:', verification.data.type); // "call"
      ```

      ```python
      verification = client.verifications.trigger_call(
          phone_number="+13035551234",
          verify_profile_id="4900017a-e7c8-e79e-0a7c-0d98f49b09cc"
      )

      print(f"Verification ID: {verification.data.id}")
      print(f"Type: {verification.data.type}")  # "call"
      ```

      ```ruby
      verification = client.verifications.call(
        phone_number: "+13035551234",
        verify_profile_id: "4900017a-e7c8-e79e-0a7c-0d98f49b09cc"
      )

      puts "Verification ID: #{verification.id}"
      puts "Type: #{verification.type}" # "call"
      ```

      ```go
      verification, err := client.Verifications.Call(context.TODO(), telnyx.VerificationCallParams{
        PhoneNumber:     "+13035551234",
        VerifyProfileID: "4900017a-e7c8-e79e-0a7c-0d98f49b09cc",
      })
      if err != nil {
        panic(err)
      }
      fmt.Printf("Verification ID: %s\n", verification.Data.ID)
      ```

      ```java
      VerificationResponse response = client.verifications().call(
          VerificationParams.builder()
              .phoneNumber("+13035551234")
              .verifyProfileId("4900017a-e7c8-e79e-0a7c-0d98f49b09cc")
              .build()
      );
      System.out.println("Verification ID: " + response.getId());
      ```

      ```csharp .NET theme={null}
      var response = await service.SendCallAsync(new VerificationCallOptions
      {
          PhoneNumber = "+13035551234",
          VerifyProfileId = "4900017a-e7c8-e79e-0a7c-0d98f49b09cc"
      });

      Console.WriteLine($"Verification ID: {response.Data.Id}");
      ```

      ```php
      $verification = \Telnyx\Verification::create([
          'phone_number' => '+13035551234',
          'verify_profile_id' => '4900017a-e7c8-e79e-0a7c-0d98f49b09cc',
          'type' => 'call'
      ]);

      echo "Verification ID: " . $verification->id . "\n";
      ```

    **User experience:** The user receives a phone call. An automated voice reads the verification code aloud (e.g., "Your verification code is 1-7-6-8-6"). The code is repeated twice. The user then enters the code in your application.

    <Callout type="info">
      **DTMF confirmation:** You can optionally enable DTMF confirmation, where the user enters the code on their phone keypad during the call instead of typing it in your app. See the [DTMF Confirmation guide](../runbooks/dtmf-confirmation-verification.md) for details.

### Example response (all methods)

```json theme={null}
{
  "data": {
    "created_at": "2020-09-14T17:03:32.965812",
    "id": "12ade33a-21c0-473b-b055-b3c836e1c292",
    "phone_number": "+13035551234",
    "record_type": "verification",
    "status": "pending",
    "timeout_secs": 300,
    "verify_profile_id": "4900017a-e7c8-e79e-0a7c-0d98f49b09cc",
    "type": "sms",
    "updated_at": "2020-09-14T17:03:32.965812"
  }
}
```

## Choosing the right verification method

| Feature                | SMS                   | Call                          | Flashcall                       |
| ---------------------- | --------------------- | ----------------------------- | ------------------------------- |
| **Delivery speed**     | 1–5 seconds           | 10–20 seconds (ring + answer) | 2–5 seconds                     |
| **User interaction**   | Read code, type it in | Listen to code, type it in    | Automatic (app reads caller ID) |
| **Works on web**       | ✅ Yes                 | ✅ Yes                         | ❌ No (mobile only)              |
| **Works on landlines** | ❌ No                  | ✅ Yes                         | ❌ No                            |
| **Cost**               | Per-message rate      | Per-minute rate               | Per-call rate (very short)      |
| **Global coverage**    | Widest                | Wide                          | Limited                         |
| **Accessibility**      | Good                  | Best (audio)                  | App-dependent                   |
| **Best for**           | General purpose       | Landlines, accessibility      | Mobile apps with auto-read      |

<Callout type="tip">
  **Fallback strategy:** Configure multiple methods in your verify profile. Start with SMS (fastest and widest coverage), fall back to call if SMS fails. For mobile apps, consider flashcall as a zero-friction primary method with SMS as fallback.

## Verify a 2FA code

The user provides the code they received (via SMS or call). Submit it to Telnyx to verify it matches:

  ```bash
  curl -X POST \
    --header "Content-Type: application/json" \
    --header "Accept: application/json" \
    --header "Authorization: Bearer YOUR_API_KEY" \
    --data '{"code":"17686", "verify_profile_id": "4900017a-e7c8-e79e-0a7c-0d98f49b09cc"}' \
    https://api.telnyx.com/v2/verifications/by_phone_number/+13035551234/actions/verify
  ```

  ```javascript
  const result = await client.verifications.byPhoneNumber.actions.verify(
    '+13035551234',
    {
      code: '17686',
      verify_profile_id: '4900017a-e7c8-e79e-0a7c-0d98f49b09cc',
    }
  );

  if (result.data.response_code === 'accepted') {
    console.log('Verification successful!');
  } else {
    console.log('Verification failed:', result.data.response_code);
  }
  ```

  ```python
  result = client.verifications.by_phone_number.actions.verify(
      "+13035551234",
      code="17686",
      verify_profile_id="4900017a-e7c8-e79e-0a7c-0d98f49b09cc"
  )

  if result.data.response_code == "accepted":
      print("Verification successful!")
  else:
      print(f"Verification failed: {result.data.response_code}")
  ```

  ```ruby
  result = client.verifications.verify(
    "+13035551234",
    code: "17686",
    verify_profile_id: "4900017a-e7c8-e79e-0a7c-0d98f49b09cc"
  )

  if result.response_code == "accepted"
    puts "Verification successful!"
  else
    puts "Verification failed: #{result.response_code}"
  end
  ```

  ```go
  result, err := client.Verifications.Verify(context.TODO(), "+13035551234", telnyx.VerificationVerifyParams{
    Code:            "17686",
    VerifyProfileID: "4900017a-e7c8-e79e-0a7c-0d98f49b09cc",
  })
  if err != nil {
    panic(err)
  }
  if result.Data.ResponseCode == "accepted" {
    fmt.Println("Verification successful!")
  } else {
    fmt.Printf("Verification failed: %s\n", result.Data.ResponseCode)
  }
  ```

  ```java
  VerifyResponse result = client.verifications().verify(
      "+13035551234",
      VerifyParams.builder()
          .code("17686")
          .verifyProfileId("4900017a-e7c8-e79e-0a7c-0d98f49b09cc")
          .build()
  );

  if ("accepted".equals(result.getResponseCode())) {
      System.out.println("Verification successful!");
  } else {
      System.out.println("Verification failed: " + result.getResponseCode());
  }
  ```

  ```csharp .NET theme={null}
  var result = await service.VerifyAsync("+13035551234", new VerifyCodeOptions
  {
      Code = "17686",
      VerifyProfileId = "4900017a-e7c8-e79e-0a7c-0d98f49b09cc"
  });

  if (result.Data.ResponseCode == "accepted")
      Console.WriteLine("Verification successful!");
  else
      Console.WriteLine($"Verification failed: {result.Data.ResponseCode}");
  ```

  ```php
  $result = \Telnyx\Verification::verify('+13035551234', [
      'code' => '17686',
      'verify_profile_id' => '4900017a-e7c8-e79e-0a7c-0d98f49b09cc'
  ]);

  if ($result->response_code === 'accepted') {
      echo "Verification successful!\n";
  } else {
      echo "Verification failed: " . $result->response_code . "\n";
  }
  ```

### Example response

```json theme={null}
{
  "data": {
    "phone_number": "+13035551234",
    "response_code": "accepted"
  }
}
```

A `response_code` of `"accepted"` confirms the code matches. Other possible values:

| Response Code           | Meaning                                          |
| ----------------------- | ------------------------------------------------ |
| `accepted`              | Code is correct - verification successful        |
| `rejected`              | Code is incorrect                                |
| `expired`               | Verification timed out (exceeded `timeout_secs`) |
| `max_attempts_exceeded` | Too many incorrect attempts                      |

<Callout type="success" title="Use webhooks for real-time updates">
  Telnyx Verify supports webhooks to receive instant notifications when users complete verification, eliminating the need for polling. This enables event-driven workflows for faster user experiences.

  Learn more: [Receiving Webhooks for Telnyx Verify](../runbooks/receiving-webhooks-for-telnyx-verify.md#real-time-verification-status-updates)

## Next steps

Now that you've completed a basic verification flow, explore these guides to build a production-ready implementation:

  - [Custom Templates](../runbooks/custom-templates-for-telnyx-verify.md) — Create branded verification messages that match your app's voice and compliance requirements.

  - [Security Best Practices](../runbooks/verify-security-best-practices.md) — Protect against SMS pumping, brute force attacks, and other verification fraud.

  - [Webhooks](../runbooks/receiving-webhooks-for-telnyx-verify.md) — Receive real-time notifications when verifications complete or expire.

  - [Integration Examples](https://developers.telnyx.com/docs/identity/verify/integration-examples) — Complete login, registration, and payment verification flow implementations.


## Related Pages

- [Custom templates for Telnyx Verify](../runbooks/custom-templates-for-telnyx-verify.md)
- [Receiving Webhooks for Telnyx Verify](../runbooks/receiving-webhooks-for-telnyx-verify.md)
- [Quickstart for Number Lookup](../tutorial/quickstart-for-number-lookup.md)
