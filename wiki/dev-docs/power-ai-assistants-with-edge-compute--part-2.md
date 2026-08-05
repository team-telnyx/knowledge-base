---
title: Power AI Assistants with Edge Compute
summary: Walks through building a single Go Edge Compute function that serves as both
  the dynamic-variables webhook and a webhook tool backend for a Telnyx AI Assistant,
  including Ed25519 signature verification, body-shape dispatch, secret management,
  deployment, and end-to-end testing.
sources:
- url: https://developers.telnyx.com/docs/edge-compute/guides/ai-assistant-backend
updated_at: 2026-08-05T13:40:59Z
---

# Power AI Assistants with Edge Compute

*Part 2 of 3 — see also: [Part 1](power-ai-assistants-with-edge-compute--part-1.md), [Part 3](power-ai-assistants-with-edge-compute--part-3.md)*

Walks through building a single Go Edge Compute function that serves as both the dynamic-variables webhook and a webhook tool backend for a Telnyx AI Assistant, including Ed25519 signature verification, body-shape dispatch, secret management, deployment, and end-to-end testing.

## Step 3: Write the handler

The handler does three things:

1. Verifies the Telnyx Ed25519 signature on every request
2. Detects whether the request is a dynamic-variables webhook or a tool call
3. Returns the appropriate response

`handler.go`:

```go
package function

import (
	"crypto/ed25519"
	"encoding/base64"
	"encoding/json"
	"io"
	"log"
	"net/http"
	"os"
	"strconv"
	"time"
)

const maxSkew = 5 * time.Minute

var publicKey ed25519.PublicKey

func init() {
	raw := os.Getenv("TELNYX_PUBLIC_KEY")
	if raw == "" {
		log.Println("warning: TELNYX_PUBLIC_KEY is not set; all requests will be rejected")
		return
	}
	key, err := base64.StdEncoding.DecodeString(raw)
	if err != nil || len(key) != ed25519.PublicKeySize {
		log.Printf("warning: TELNYX_PUBLIC_KEY is invalid (len=%d, err=%v)", len(key), err)
		return
	}
	publicKey = ed25519.PublicKey(key)
}

func Handle(w http.ResponseWriter, r *http.Request) {
	// Health probes are handled by the platform — don't add custom health routes
	if r.Method != http.MethodPost {
		http.Error(w, "method not allowed", http.StatusMethodNotAllowed)
		return
	}

	body, err := io.ReadAll(r.Body)
	if err != nil {
		http.Error(w, "cannot read body", http.StatusBadRequest)
		return
	}

	if !verifyTelnyxSignature(r.Header, body) {
		http.Error(w, "invalid signature", http.StatusForbidden)
		return
	}

	// Dispatch on body shape: DV webhook has "data.event_type",
	// tool call is a flat args object
	if isDynamicVariablesRequest(body) {
		handleDynamicVariables(w, body)
		return
	}
	handleLookupOrder(w, body)
}

func isDynamicVariablesRequest(body []byte) bool {
	var probe struct {
		Data *struct {
			EventType string `json:"event_type"`
		} `json:"data"`
	}
	if err := json.Unmarshal(body, &probe); err != nil {
		return false
	}
	return probe.Data != nil
}

func verifyTelnyxSignature(h http.Header, body []byte) bool {
	if publicKey == nil {
		return false
	}

	sig := h.Get("telnyx-signature-ed25519")
	ts := h.Get("telnyx-timestamp")
	if sig == "" || ts == "" {
		return false
	}

	t, err := strconv.ParseInt(ts, 10, 64)
	if err != nil {
		return false
	}
	age := time.Since(time.Unix(t, 0))
	if age < -maxSkew || age > maxSkew {
		return false
	}

	s, err := base64.StdEncoding.DecodeString(sig)
	if err != nil {
		return false
	}

	signed := append([]byte(ts+"|"), body...)
	return ed25519.Verify(publicKey, signed, s)
}

// --- Dynamic Variables ---

type dvRequest struct {
	Data struct {
		EventType string `json:"event_type"`
		Payload   struct {
			Channel       string `json:"telnyx_conversation_channel"`
			AgentTarget   string `json:"telnyx_agent_target"`
			EndUserTarget string `json:"telnyx_end_user_target"`
			CallControlID string `json:"call_control_id"`
			AssistantID   string `json:"assistant_id"`
		} `json:"payload"`
	} `json:"data"`
}

type dvResponse struct {
	DynamicVariables map[string]any `json:"dynamic_variables"`
}

func handleDynamicVariables(w http.ResponseWriter, body []byte) {
	var req dvRequest
	if err := json.Unmarshal(body, &req); err != nil {
		http.Error(w, "bad json", http.StatusBadRequest)
		return
	}

	caller := req.Data.Payload.EndUserTarget

	resp := dvResponse{
		DynamicVariables: map[string]any{
			"customer_name":  lookupCustomerName(caller),
			"account_tier":   "premium",
			"open_order_id":  "ORD-10042",
			"support_region": "US",
		},
	}

	writeJSON(w, resp)
}

func lookupCustomerName(caller string) string {
	known := map[string]string{
		"+13128675309": "James Smith",
		"+15551234567": "Rachel Thomas",
	}
	if name, ok := known[caller]; ok {
		return name
	}
	return "there"
}

// --- Webhook Tool: lookup-order ---

type toolRequest struct {
	OrderID string `json:"order_id"`
}

type toolResponse struct {
	OrderID        string `json:"order_id"`
	Status         string `json:"status"`
	EstimatedDeliv string `json:"estimated_delivery"`
	Carrier        string `json:"carrier"`
}

func handleLookupOrder(w http.ResponseWriter, body []byte) {
	var req toolRequest
	if err := json.Unmarshal(body, &req); err != nil {
		http.Error(w, "bad json", http.StatusBadRequest)
		return
	}

	resp := toolResponse{
		OrderID:        req.OrderID,
		Status:         "shipped",
		EstimatedDeliv: "2025-04-10",
		Carrier:        "Telnyx Logistics",
	}

	writeJSON(w, resp)
}

func writeJSON(w http.ResponseWriter, v any) {
	w.Header().Set("Content-Type", "application/json")
	json.NewEncoder(w).Encode(v)
}
```

## Step 4: Ship the function

```
telnyx-edge ship
```

The ship process takes 2–3 minutes. After `uploaded successfully`, poll `telnyx-edge list` until the status shows `deploy_ok`. Don't trust a CLI timeout as a failure — the function may still be building server-side.

```
telnyx-edge list
# FUNC ID                          FUNCTION NAME    STATUS      INVOKE URL
# 917210e7-...                     telnyx-ai-edge   deploy_ok  https://telnyx-ai-edge-<org>.telnyxcompute.com
```

Save the invoke URL — you'll point the assistant at it next.

## Step 5: Configure the AI Assistant

Set the function URL as both the dynamic variables webhook URL and the webhook tool URL on the assistant.

### Dynamic variables webhook

In the [Portal](https://portal.telnyx.com/#/ai/assistants) or via the API:

| Field | Value |
| --- | --- |
| `dynamic_variables_webhook_url` | `https://telnyx-ai-edge-<org>.telnyxcompute.com/` |
| `dynamic_variables_webhook_timeout_ms` | `8000` |

Consider setting the timeout to 8,000 ms to give the function room on cold starts. The default 1,500 ms may be tight for a cold function.

### Template variables in the assistant

Use `{{variable_name}}` in the assistant's instructions and greeting to reference the variables your function returns:

```
instructions: "You are a support agent for Telnyx Logistics. The caller is {{customer_name}} (tier: {{account_tier}}). They may have open order {{open_order_id}}."
greeting: "Hi {{customer_name}}, thanks for calling Telnyx Logistics. How can I help you today?"
```

### Webhook tool

Add a webhook tool that points to the same function URL:

```json
{
  "type": "webhook",
  "webhook": {
    "name": "lookup-order",
    "description": "Look up the current status of a customer order by its order id.",
    "url": "https://telnyx-ai-edge-<org>.telnyxcompute.com/",
    "method": "POST",
    "body_parameters": {
      "type": "object",
      "properties": {
        "order_id": {
          "type": "string",
          "description": "The order id to look up, e.g. ORD-10042."
        }
      },
      "required": ["order_id"]
    }
  }
}
```

When the LLM decides to call `lookup-order`, Telnyx sends a POST with the tool arguments as the flat body (`{"order_id": "ORD-10042"}`), signed with the same Ed25519 key. Your function detects the body shape, handles it as a tool call, and returns the result.

## Step 6: Test end-to-end

1. **Call the function directly** (without a signature — it'll return 403, confirming it's live):

   ```
   curl -X POST https://telnyx-ai-edge-<org>.telnyxcompute.com/ \
     -H "Content-Type: application/json" \
     -d '{"order_id":"ORD-10042"}'
   # → 403 invalid signature  ← expected, signature verification is working
   ```
2. **Make a test call** to the assistant from the Portal or via the API:

   ```
   curl --request POST \
     --url https://api.telnyx.com/v2/texml/ai_calls/<texml_app_id> \
     --header "Authorization: Bearer $TELNYX_API_KEY" \
     --header 'Content-Type: application/json' \
     --data '{
       "From": "+13128675309",
       "To": "+15551234567",
       "AIAssistantId": "assistant-<id>"
     }'
   ```
3. **Verify in the conversation transcript** that:
   - The greeting includes the resolved `customer_name`
   - The assistant can call `lookup-order` and read back real order data
