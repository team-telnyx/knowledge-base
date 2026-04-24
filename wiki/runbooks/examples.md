---
title: Examples
summary: Copy-paste code snippets for common edge function patterns.
sources:
  - url: https://developers.telnyx.com/docs/edge-compute/examples/index
    content_hash: 32f4f6c5e0f4fb99bdce6a656281c572efe5cb0d3d4c767c47bc6607602730a0
updated_at: 2026-04-10T00:00:00Z
---

# Examples

Copy-paste code snippets for common edge function patterns.

Bite-sized code snippets for common edge function patterns. Each example is self-contained — copy, paste, deploy.

## Return JSON

### JavaScript

    ```javascript theme={null}
    export async function handler(request) {
        const data = {
            success: true,
            data: { id: 123, name: "John" }
        };

        return new Response(JSON.stringify(data), {
            headers: { "Content-Type": "application/json" }
        });
    }
    ```

### Go

    ```go theme={null}
    func handler(w http.ResponseWriter, r *http.Request) {
        response := map[string]interface{}{
            "success": true,
            "data": map[string]interface{}{
                "id":   123,
                "name": "John",
            },
        }

        w.Header().Set("Content-Type", "application/json")
        json.NewEncoder(w).Encode(response)
    }
    ```

### Python

    ```python theme={null}
    def do_GET(self):
        response = {
            "success": True,
            "data": {"id": 123, "name": "John"}
        }

        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(response).encode())
    ```

### Java

    ```java theme={null}
    @GET
    @Produces(MediaType.APPLICATION_JSON)
    public Response getData() {
        return Response.ok(Map.of(
            "success", true,
            "data", Map.of("id", 123, "name", "John")
        )).build();
    }
    ```

## Return HTML

### JavaScript

    ```javascript theme={null}
    export async function handler(request) {
        const html = `
            <!DOCTYPE html>
            <html>
                <body><h1>Hello from Edge</h1></body>
            </html>
        `;

        return new Response(html, {
            headers: { "Content-Type": "text/html" }
        });
    }
    ```

### Go

    ```go theme={null}
    func handler(w http.ResponseWriter, r *http.Request) {
        html := `<html><body><h1>Hello from Edge</h1></body></html>`

        w.Header().Set("Content-Type", "text/html")
        w.WriteHeader(http.StatusOK)
        fmt.Fprint(w, html)
    }
    ```

### Python

    ```python theme={null}
    def do_GET(self):
        html = "<html><body><h1>Hello from Edge</h1></body></html>"

        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.end_headers()
        self.wfile.write(html.encode())
    ```

### Java

    ```java theme={null}
    @GET
    @Produces(MediaType.TEXT_HTML)
    public Response getHtml() {
        String html = "<html><body><h1>Hello from Edge</h1></body></html>";
        return Response.ok(html).build();
    }
    ```

## Return Binary

### JavaScript

    ```javascript theme={null}
    export async function handler(request) {
        const imageResponse = await fetch("https://your-bucket.s3.amazonaws.com/logo.png");
        const imageData = await imageResponse.arrayBuffer();

        return new Response(imageData, {
            headers: { "Content-Type": "image/png" }
        });
    }
    ```

### Go

    ```go theme={null}
    func handler(w http.ResponseWriter, r *http.Request) {
        imageData, err := os.ReadFile("logo.png")
        if err != nil {
            http.Error(w, "Image not found", http.StatusNotFound)
            return
        }

        w.Header().Set("Content-Type", "image/png")
        w.Write(imageData)
    }
    ```

### Python

    ```python theme={null}
    def do_GET(self):
        with open("logo.png", "rb") as f:
            image_data = f.read()

        self.send_response(200)
        self.send_header("Content-Type", "image/png")
        self.end_headers()
        self.wfile.write(image_data)
    ```

### Java

    ```java theme={null}
    @GET
    @Produces("image/png")
    public Response getImage() throws IOException {
        byte[] imageData = Files.readAllBytes(Path.of("logo.png"));
        return Response.ok(imageData).build();
    }
    ```

## Parse Query Parameters

### JavaScript

    ```javascript theme={null}
    export async function handler(request) {
        const url = new URL(request.url);
        const name = url.searchParams.get("name") || "World";

        return new Response(JSON.stringify({
            message: `Hello ${name} from Telnyx Edge Compute!`,
            status: "success"
        }), {
            headers: { "Content-Type": "application/json" }
        });
    }
    ```

### Go

    ```go theme={null}
    func handler(w http.ResponseWriter, r *http.Request) {
        name := r.URL.Query().Get("name")
        if name == "" {
            name = "World"
        }

        response := Response{
            Message: fmt.Sprintf("Hello %s from Telnyx Edge Compute!", name),
            Status:  "success",
        }

        w.Header().Set("Content-Type", "application/json")
        json.NewEncoder(w).Encode(response)
    }
    ```

### Python

    ```python theme={null}
    from urllib.parse import urlparse, parse_qs

    def do_GET(self):
        query = parse_qs(urlparse(self.path).query)
        name = query.get("name", ["World"])[0]

        response = {
            "message": f"Hello {name} from Telnyx Edge Compute!",
            "status": "success"
        }

        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(response).encode())
    ```

### Java

    ```java theme={null}
    import jakarta.ws.rs.QueryParam;
    import jakarta.ws.rs.DefaultValue;

    @GET
    @Produces(MediaType.APPLICATION_JSON)
    public Response hello(@QueryParam("name") @DefaultValue("World") String name) {
        return Response.ok(Map.of(
            "message", "Hello " + name + " from Telnyx Edge Compute!",
            "status", "success"
        )).build();
    }
    ```

## Handle HTTP Methods

### JavaScript

    ```javascript theme={null}
    export async function handler(request) {
        const { method } = request;

        let message;
        let status = 200;

        switch (method) {
            case "GET":
                message = "Hello from GET request!";
                break;
            case "POST":
                message = "Data received via POST!";
                break;
            default:
                message = "Method not supported";
                status = 405;
        }

        return new Response(JSON.stringify({ message, status: status === 200 ? "success" : "error" }), {
            status,
            headers: { "Content-Type": "application/json" }
        });
    }
    ```

### Go

    ```go theme={null}
    func handler(w http.ResponseWriter, r *http.Request) {
        var response Response

        switch r.Method {
        case "GET":
            response = Response{Message: "Hello from GET request!", Status: "success"}
        case "POST":
            response = Response{Message: "Data received via POST!", Status: "success"}
        default:
            response = Response{Message: "Method not supported", Status: "error"}
            w.WriteHeader(http.StatusMethodNotAllowed)
        }

        w.Header().Set("Content-Type", "application/json")
        json.NewEncoder(w).Encode(response)
    }
    ```

### Python

    ```python theme={null}
    def do_GET(self):
        response = {"message": "Hello from GET request!", "status": "success"}
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(response).encode())

    def do_POST(self):
        response = {"message": "Data received via POST!", "status": "success"}
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(response).encode())
    ```

### Java

    ```java theme={null}
    @GET
    @Produces(MediaType.APPLICATION_JSON)
    public Response handleGet() {
        return Response.ok(Map.of(
            "message", "Hello from GET request!",
            "status", "success"
        )).build();
    }

    @POST
    @Produces(MediaType.APPLICATION_JSON)
    public Response handlePost(Map<String, Object> body) {
        return Response.ok(Map.of(
            "message", "Data received via POST!",
            "status", "success"
        )).build();
    }
    ```

## Read Request Body

### JavaScript

    ```javascript theme={null}
    export async function handler(request) {
        try {
            const body = await request.json();

            if (!body.email) {
                return new Response(JSON.stringify({ error: "Email is required" }), {
                    status: 400,
                    headers: { "Content-Type": "application/json" }
                });
            }

            return new Response(JSON.stringify({ status: "success", email: body.email }), {
                headers: { "Content-Type": "application/json" }
            });
        } catch {
            return new Response(JSON.stringify({ error: "Invalid JSON" }), {
                status: 400,
                headers: { "Content-Type": "application/json" }
            });
        }
    }
    ```

### Go

    ```go theme={null}
    func handler(w http.ResponseWriter, r *http.Request) {
        var data struct {
            Email string `json:"email"`
        }

        if err := json.NewDecoder(r.Body).Decode(&data); err != nil {
            w.Header().Set("Content-Type", "application/json")
            w.WriteHeader(http.StatusBadRequest)
            json.NewEncoder(w).Encode(map[string]string{"error": "Invalid JSON"})
            return
        }

        w.Header().Set("Content-Type", "application/json")
        json.NewEncoder(w).Encode(map[string]string{"status": "success", "email": data.Email})
    }
    ```

### Python

    ```python theme={null}
    def do_POST(self):
        try:
            content_length = int(self.headers.get('Content-Length', 0))
            body = self.rfile.read(content_length)
            data = json.loads(body)

            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"status": "success", "received": data}).encode())

        except json.JSONDecodeError:
            self.send_response(400)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"error": "Invalid JSON"}).encode())
    ```

### Java

    ```java theme={null}
    @POST
    @Consumes(MediaType.APPLICATION_JSON)
    @Produces(MediaType.APPLICATION_JSON)
    public Response handleRequest(Map<String, Object> data) {
        if (data == null || !data.containsKey("email")) {
            return Response.status(400)
                .entity(Map.of("error", "Email is required"))
                .build();
        }

        return Response.ok(Map.of("status", "success")).build();
    }
    ```

## Use Environment Variables

### JavaScript

    ```javascript theme={null}
    export async function handler(request) {
        const greeting = process.env.GREETING || "Hello";

        return new Response(JSON.stringify({
            message: `${greeting} from Telnyx Edge Compute!`,
            status: "success"
        }), {
            headers: { "Content-Type": "application/json" }
        });
    }
    ```

### Go

    ```go theme={null}
    func handler(w http.ResponseWriter, r *http.Request) {
        greeting := os.Getenv("GREETING")
        if greeting == "" {
            greeting = "Hello"
        }

        response := Response{
            Message: fmt.Sprintf("%s from Telnyx Edge Compute!", greeting),
            Status:  "success",
        }

        w.Header().Set("Content-Type", "application/json")
        json.NewEncoder(w).Encode(response)
    }
    ```

### Python

    ```python theme={null}
    import os

    def do_GET(self):
        greeting = os.environ.get("GREETING", "Hello")

        response = {
            "message": f"{greeting} from Telnyx Edge Compute!",
            "status": "success"
        }

        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(response).encode())
    ```

### Java

    ```java theme={null}
    import org.eclipse.microprofile.config.inject.ConfigProperty;

    @Path("/")
    public class HelloResource {

        @ConfigProperty(name = "GREETING", defaultValue = "Hello")
        String greeting;

        @GET
        @Produces(MediaType.APPLICATION_JSON)
        public Response hello() {
            return Response.ok(Map.of(
                "message", greeting + " from Telnyx Edge Compute!",
                "status", "success"
            )).build();
        }
    }
    ```

## Access Secrets

Secrets are injected as environment variables but stored encrypted. Use them for API keys, tokens, and credentials.

### JavaScript

    ```javascript theme={null}
    export async function handler(request) {
        const apiKey = process.env.EXTERNAL_API_KEY;

        if (!apiKey) {
            return new Response(JSON.stringify({ error: "API key not configured" }), {
                status: 500,
                headers: { "Content-Type": "application/json" }
            });
        }

        const response = await fetch("https://api.example.com/data", {
            headers: { "Authorization": `Bearer ${apiKey}` }
        });

        const data = await response.json();
        return new Response(JSON.stringify(data), {
            headers: { "Content-Type": "application/json" }
        });
    }
    ```

### Go

    ```go theme={null}
    func handler(w http.ResponseWriter, r *http.Request) {
        apiKey := os.Getenv("EXTERNAL_API_KEY")
        if apiKey == "" {
            http.Error(w, "API key not configured", http.StatusInternalServerError)
            return
        }

        req, _ := http.NewRequest("GET", "https://api.example.com/data", nil)
        req.Header.Set("Authorization", "Bearer "+apiKey)

        resp, err := http.DefaultClient.Do(req)
        if err != nil {
            http.Error(w, "External API error", http.StatusBadGateway)
            return
        }
        defer resp.Body.Close()

        w.Header().Set("Content-Type", "application/json")
        io.Copy(w, resp.Body)
    }
    ```

### Python

    ```python theme={null}
    import os
    import httpx

    def do_GET(self):
        api_key = os.environ.get("EXTERNAL_API_KEY")
        if not api_key:
            self.send_error(500, "API key not configured")
            return

        response = httpx.get(
            "https://api.example.com/data",
            headers={"Authorization": f"Bearer {api_key}"}
        )

        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(response.content)
    ```

### Java

    ```java theme={null}
    @ApplicationScoped
    public class SecureResource {

        @ConfigProperty(name = "EXTERNAL_API_KEY")
        String apiKey;

        @Inject
        @RestClient
        ExternalApiClient client;

        @GET
        @Produces(MediaType.APPLICATION_JSON)
        public Response fetchData() {
            var data = client.getData(apiKey);
            return Response.ok(data).build();
        }
    }
    ```

## KV Read/Write

  **Coming Soon** — KV storage is in development. The examples below show the expected API pattern.

Access [KV storage](https://developers.telnyx.com/docs/edge-compute/kv) for low-latency key-value data.

### JavaScript

    ```javascript theme={null}
    const KV_ID = process.env.KV_MY_STORE_ID;
    const API_KEY = process.env.TELNYX_API_KEY;
    const BASE_URL = `https://api.telnyx.com/v2/storage/kvs/${KV_ID}`;

    async function kvGet(key) {
        const response = await fetch(`${BASE_URL}/keys/${key}`, {
            headers: { "Authorization": `Bearer ${API_KEY}` }
        });
        if (response.status === 404) return null;
        const data = await response.json();
        return data.value;
    }

    async function kvPut(key, value, ttl) {
        await fetch(`${BASE_URL}/keys/${key}`, {
            method: "PUT",
            headers: {
                "Authorization": `Bearer ${API_KEY}`,
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ value, ttl })
        });
    }

    export async function handler(request) {
        const cachedValue = await kvGet("user:123");

        if (cachedValue) {
            return new Response(cachedValue, {
                headers: { "Content-Type": "application/json" }
            });
        }

        const userData = JSON.stringify({ id: 123, name: "Alice" });
        await kvPut("user:123", userData, 3600);

        return new Response(userData, {
            headers: { "Content-Type": "application/json" }
        });
    }
    ```

### Go

    ```go theme={null}
    var (
        kvID   = os.Getenv("KV_MY_STORE_ID")
        apiKey = os.Getenv("TELNYX_API_KEY")
    )

    func kvGet(key string) (string, error) {
        url := fmt.Sprintf("https://api.telnyx.com/v2/storage/kvs/%s/keys/%s", kvID, key)
        req, _ := http.NewRequest("GET", url, nil)
        req.Header.Set("Authorization", "Bearer "+apiKey)

        resp, err := http.DefaultClient.Do(req)
        if err != nil {
            return "", err
        }
        defer resp.Body.Close()

        if resp.StatusCode == 404 {
            return "", nil
        }

        var result struct {
            Value string `json:"value"`
        }
        json.NewDecoder(resp.Body).Decode(&result)
        return result.Value, nil
    }

    func kvPut(key, value string, ttl int) error {
        url := fmt.Sprintf("https://api.telnyx.com/v2/storage/kvs/%s/keys/%s", kvID, key)
        body, _ := json.Marshal(map[string]interface{}{"value": value, "ttl": ttl})

        req, _ := http.NewRequest("PUT", url, bytes.NewReader(body))
        req.Header.Set("Authorization", "Bearer "+apiKey)
        req.Header.Set("Content-Type", "application/json")

        _, err := http.DefaultClient.Do(req)
        return err
    }

    func handler(w http.ResponseWriter, r *http.Request) {
        cached, _ := kvGet("user:123")

        if cached != "" {
            w.Header().Set("Content-Type", "application/json")
            fmt.Fprint(w, cached)
            return
        }

        userData := `{"id": 123, "name": "Alice"}`
        kvPut("user:123", userData, 3600)

        w.Header().Set("Content-Type", "application/json")
        fmt.Fprint(w, userData)
    }
    ```

### Python

    ```python theme={null}
    import os
    import httpx

    KV_ID = os.getenv("KV_MY_STORE_ID")
    API_KEY = os.getenv("TELNYX_API_KEY")
    BASE_URL = f"https://api.telnyx.com/v2/storage/kvs/{KV_ID}"

    def kv_get(key):
        response = httpx.get(
            f"{BASE_URL}/keys/{key}",
            headers={"Authorization": f"Bearer {API_KEY}"}
        )
        if response.status_code == 404:
            return None
        return response.json().get("value")

    def kv_put(key, value, ttl=None):
        httpx.put(
            f"{BASE_URL}/keys/{key}",
            headers={"Authorization": f"Bearer {API_KEY}"},
            json={"value": value, "ttl": ttl}
        )

    def do_GET(self):
        cached = kv_get("user:123")

        if cached:
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(cached.encode())
            return

        user_data = '{"id": 123, "name": "Alice"}'
        kv_put("user:123", user_data, 3600)

        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(user_data.encode())
    ```

### Java

    ```java theme={null}
    public class KVClient {
        private final String kvId = System.getenv("KV_MY_STORE_ID");
        private final String apiKey = System.getenv("TELNYX_API_KEY");
        private final HttpClient client = HttpClient.newHttpClient();

        public String get(String key) throws Exception {
            HttpRequest request = HttpRequest.newBuilder()
                .uri(URI.create("https://api.telnyx.com/v2/storage/kvs/" + kvId + "/keys/" + key))
                .header("Authorization", "Bearer " + apiKey)
                .GET()
                .build();

            HttpResponse response = client.send(request, HttpResponse.BodyHandlers.ofString());
            if (response.statusCode() == 404) return null;
            return response.body();
        }

        public void put(String key, String value, int ttl) throws Exception {
            String body = String.format("{\"value\":\"%s\",\"ttl\":%d}", value, ttl);
            HttpRequest request = HttpRequest.newBuilder()
                .uri(URI.create("https://api.telnyx.com/v2/storage/kvs/" + kvId + "/keys/" + key))
                .header("Authorization", "Bearer " + apiKey)
                .header("Content-Type", "application/json")
                .PUT(HttpRequest.BodyPublishers.ofString(body))
                .build();

            client.send(request, HttpResponse.BodyHandlers.ofString());
        }
    }
    ```

## Cron Trigger

  **Coming Soon** — Native cron triggers are planned. The examples below show the expected pattern. Until then, use an external scheduler (GitHub Actions, AWS EventBridge) to call your function's HTTP endpoint.

Functions can be triggered on a schedule via [cron triggers](https://developers.telnyx.com/docs/edge-compute/configuration/cron-triggers). The request includes cron metadata.

### JavaScript

    ```javascript theme={null}
    export async function handler(request) {
        const isCron = request.headers.get("X-Telnyx-Cron") === "true";
        const scheduleName = request.headers.get("X-Telnyx-Cron-Schedule");

        if (isCron) {
            console.log(`Cron job triggered: ${scheduleName}`);

            await cleanupExpiredSessions();
            await sendDailyReport();

            return new Response(JSON.stringify({ status: "cron completed" }), {
                headers: { "Content-Type": "application/json" }
            });
        }

        return new Response(JSON.stringify({ status: "ok" }), {
            headers: { "Content-Type": "application/json" }
        });
    }

    async function cleanupExpiredSessions() {
        // Your cleanup logic
    }

    async function sendDailyReport() {
        // Your reporting logic
    }
    ```

### Go

    ```go theme={null}
    func handler(w http.ResponseWriter, r *http.Request) {
        isCron := r.Header.Get("X-Telnyx-Cron") == "true"
        scheduleName := r.Header.Get("X-Telnyx-Cron-Schedule")

        if isCron {
            log.Printf("Cron job triggered: %s", scheduleName)

            cleanupExpiredSessions()
            sendDailyReport()

            w.Header().Set("Content-Type", "application/json")
            json.NewEncoder(w).Encode(map[string]string{"status": "cron completed"})
            return
        }

        w.Header().Set("Content-Type", "application/json")
        json.NewEncoder(w).Encode(map[string]string{"status": "ok"})
    }
    ```

### Python

    ```python theme={null}
    def do_GET(self):
        is_cron = self.headers.get("X-Telnyx-Cron") == "true"
        schedule_name = self.headers.get("X-Telnyx-Cron-Schedule")

        if is_cron:
            print(f"Cron job triggered: {schedule_name}")

            cleanup_expired_sessions()
            send_daily_report()

            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"status": "cron completed"}).encode())
            return

        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps({"status": "ok"}).encode())
    ```

### Java

    ```java theme={null}
    @GET
    @Produces(MediaType.APPLICATION_JSON)
    public Response handler(@HeaderParam("X-Telnyx-Cron") String isCron,
                            @HeaderParam("X-Telnyx-Cron-Schedule") String scheduleName) {

        if ("true".equals(isCron)) {
            System.out.println("Cron job triggered: " + scheduleName);

            cleanupExpiredSessions();
            sendDailyReport();

            return Response.ok(Map.of("status", "cron completed")).build();
        }

        return Response.ok(Map.of("status", "ok")).build();
    }
    ```

## WebSocket Handling

  **Coming Soon** — WebSocket support is planned. The examples below show the expected pattern.

Handle WebSocket connections for real-time communication.

### Go

    ```go theme={null}
    import (
        "github.com/gorilla/websocket"
    )

    var upgrader = websocket.Upgrader{
        CheckOrigin: func(r *http.Request) bool { return true },
    }

    func handler(w http.ResponseWriter, r *http.Request) {
        conn, err := upgrader.Upgrade(w, r, nil)
        if err != nil {
            http.Error(w, "WebSocket upgrade failed", http.StatusBadRequest)
            return
        }
        defer conn.Close()

        conn.WriteJSON(map[string]interface{}{
            "type":      "connected",
            "timestamp": time.Now().Unix(),
        })

        for {
            var msg map[string]interface{}
            if err := conn.ReadJSON(&msg); err != nil {
                break
            }

            conn.WriteJSON(map[string]interface{}{
                "type":       "echo",
                "original":   msg,
                "serverTime": time.Now().Unix(),
            })
        }
    }
    ```

### Python

    ```python theme={null}
    import asyncio
    import websockets
    import json
    import time

    async def handler(websocket, path):
        await websocket.send(json.dumps({
            "type": "connected",
            "timestamp": int(time.time())
        }))

        async for message in websocket:
            data = json.loads(message)
            print(f"Received: {data}")

            await websocket.send(json.dumps({
                "type": "echo",
                "original": data,
                "serverTime": int(time.time())
            }))

    start_server = websockets.serve(handler, "0.0.0.0", 8080)
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()
    ```

### Java

    ```java theme={null}
    import jakarta.websocket.*;
    import jakarta.websocket.server.ServerEndpoint;

    @ServerEndpoint("/ws")
    public class WebSocketHandler {

        @OnOpen
        public void onOpen(Session session) {
            System.out.println("Client connected: " + session.getId());
            session.getAsyncRemote().sendText(
                "{\"type\":\"connected\",\"timestamp\":" + System.currentTimeMillis() + "}"
            );
        }

        @OnMessage
        public void onMessage(String message, Session session) {
            System.out.println("Received: " + message);

            String response = String.format(
                "{\"type\":\"echo\",\"original\":%s,\"serverTime\":%d}",
                message, System.currentTimeMillis()
            );
            session.getAsyncRemote().sendText(response);
        }

        @OnClose
        public void onClose(Session session) {
            System.out.println("Client disconnected: " + session.getId());
        }
    }
    ```

## Service-to-Service Calls

Call other edge functions or external services with proper error handling and timeouts.

### JavaScript

    ```javascript theme={null}
    const INTERNAL_SERVICE_URL = process.env.USER_SERVICE_URL;

    export async function handler(request) {
        const { userId } = await request.json();

        try {
            const controller = new AbortController();
            const timeout = setTimeout(() => controller.abort(), 5000);

            const userResponse = await fetch(`${INTERNAL_SERVICE_URL}/users/${userId}`, {
                headers: {
                    "Authorization": request.headers.get("Authorization"),
                    "X-Request-ID": request.headers.get("X-Request-ID") || crypto.randomUUID()
                },
                signal: controller.signal
            });

            clearTimeout(timeout);

            if (!userResponse.ok) {
                return new Response(JSON.stringify({ error: "User service error" }), {
                    status: userResponse.status,
                    headers: { "Content-Type": "application/json" }
                });
            }

            const user = await userResponse.json();

            return new Response(JSON.stringify({ user }), {
                headers: { "Content-Type": "application/json" }
            });

        } catch (error) {
            if (error.name === "AbortError") {
                return new Response(JSON.stringify({ error: "Service timeout" }), {
                    status: 504,
                    headers: { "Content-Type": "application/json" }
                });
            }
            throw error;
        }
    }
    ```

### Go

    ```go theme={null}
    var httpClient = &http.Client{
        Timeout: 5 * time.Second,
    }

    func handler(w http.ResponseWriter, r *http.Request) {
        var input struct {
            UserID string `json:"userId"`
        }
        json.NewDecoder(r.Body).Decode(&input)

        userServiceURL := os.Getenv("USER_SERVICE_URL")
        req, _ := http.NewRequest("GET", userServiceURL+"/users/"+input.UserID, nil)
        req.Header.Set("Authorization", r.Header.Get("Authorization"))
        req.Header.Set("X-Request-ID", r.Header.Get("X-Request-ID"))

        userResp, err := httpClient.Do(req)
        if err != nil {
            w.WriteHeader(http.StatusGatewayTimeout)
            json.NewEncoder(w).Encode(map[string]string{"error": "Service timeout"})
            return
        }
        defer userResp.Body.Close()

        if userResp.StatusCode != 200 {
            w.WriteHeader(userResp.StatusCode)
            json.NewEncoder(w).Encode(map[string]string{"error": "User service error"})
            return
        }

        var user map[string]interface{}
        json.NewDecoder(userResp.Body).Decode(&user)

        w.Header().Set("Content-Type", "application/json")
        json.NewEncoder(w).Encode(map[string]interface{}{"user": user})
    }
    ```

### Python

    ```python theme={null}
    import os
    import httpx

    USER_SERVICE_URL = os.getenv("USER_SERVICE_URL")
    TIMEOUT = 5.0

    async def handler(request):
        data = await request.json()
        user_id = data.get("userId")

        async with httpx.AsyncClient(timeout=TIMEOUT) as client:
            try:
                user_response = await client.get(
                    f"{USER_SERVICE_URL}/users/{user_id}",
                    headers={
                        "Authorization": request.headers.get("Authorization"),
                        "X-Request-ID": request.headers.get("X-Request-ID", "")
                    }
                )
                user_response.raise_for_status()
                user = user_response.json()

                return {"user": user}

            except httpx.TimeoutException:
                return {"error": "Service timeout"}, 504
            except httpx.HTTPStatusError as e:
                return {"error": "User service error"}, e.response.status_code
    ```

### Java

    ```java theme={null}
    @ApplicationScoped
    public class AggregatorResource {

        private final HttpClient client = HttpClient.newBuilder()
            .connectTimeout(Duration.ofSeconds(5))
            .build();

        @ConfigProperty(name = "USER_SERVICE_URL")
        String userServiceUrl;

        @POST
        @Consumes(MediaType.APPLICATION_JSON)
        @Produces(MediaType.APPLICATION_JSON)
        public Response aggregate(Map<String, String> input,
                                  @HeaderParam("Authorization") String auth,
                                  @HeaderParam("X-Request-ID") String requestId) {

            String userId = input.get("userId");

            try {
                HttpRequest request = HttpRequest.newBuilder()
                    .uri(URI.create(userServiceUrl + "/users/" + userId))
                    .header("Authorization", auth)
                    .header("X-Request-ID", requestId)
                    .timeout(Duration.ofSeconds(5))
                    .GET()
                    .build();

                HttpResponse response = client.send(request,
                    HttpResponse.BodyHandlers.ofString());

                if (response.statusCode() != 200) {
                    return Response.status(response.statusCode())
                        .entity(Map.of("error", "User service error"))
                        .build();
                }

                return Response.ok(Map.of("user", response.body())).build();

            } catch (Exception e) {
                return Response.status(504)
                    .entity(Map.of("error", "Service timeout"))
                    .build();
            }
        }
    }
    ```

## Connection Reuse

Initialize HTTP clients once at module level to reuse connections across requests.

### JavaScript

    ```javascript theme={null}
    // Module-level client (reused across requests)
    const httpClient = {
        baseUrl: "https://api.example.com",
        headers: {
            "Authorization": `Bearer ${process.env.API_KEY}`,
            "Content-Type": "application/json"
        }
    };

    export async function handler(request) {
        const response = await fetch(`${httpClient.baseUrl}/data`, {
            headers: httpClient.headers
        });

        return new Response(await response.text(), {
            headers: { "Content-Type": "application/json" }
        });
    }
    ```

### Go

    ```go theme={null}
    // Package-level client (reused across requests)
    var httpClient = &http.Client{
        Timeout: 10 * time.Second,
        Transport: &http.Transport{
            MaxIdleConns:        100,
            MaxIdleConnsPerHost: 10,
            IdleConnTimeout:     90 * time.Second,
        },
    }

    func handler(w http.ResponseWriter, r *http.Request) {
        resp, err := httpClient.Get("https://api.example.com/data")
        if err != nil {
            http.Error(w, "External API error", http.StatusBadGateway)
            return
        }
        defer resp.Body.Close()

        w.Header().Set("Content-Type", "application/json")
        io.Copy(w, resp.Body)
    }
    ```

### Python

    ```python theme={null}
    import urllib3

    # Module-level connection pool (reused across requests)
    http_pool = urllib3.PoolManager(
        num_pools=10,
        maxsize=10,
        timeout=urllib3.Timeout(total=10.0)
    )

    def do_GET(self):
        response = http_pool.request('GET', 'https://api.example.com/data')

        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(response.data)
    ```

### Java

    ```java theme={null}
    @ApplicationScoped
    public class EdgeResource {

        @Inject
        @RestClient
        ExternalApiClient apiClient;

        @GET
        @Produces(MediaType.APPLICATION_JSON)
        public Response handler() {
            var data = apiClient.fetchData();
            return Response.ok(data).build();
        }
    }
    ```


## Related Pages

- [Examples](../runbooks/examples-2.md)
- [Examples](../runbooks/examples-3.md)
- [Examples](../runbooks/examples-4.md)
