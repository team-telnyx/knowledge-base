---
title: Request & Response Handling
summary: Universal patterns for making requests and handling responses across all Telnyx APIs.
sources:
  - url: https://developers.telnyx.com/development/api-fundamentals/request-response/index
    content_hash: ba0f06f9ef079b7594f86cc30bb5be1f11964ae1629e825cdf3a6e31d20f92d3
updated_at: 2026-04-10T00:00:00Z
---

# Request & Response Handling

Universal patterns for making requests and handling responses across all Telnyx APIs.

Understanding common request and response patterns will help you build robust integrations across all Telnyx services. This guide covers the universal HTTP concepts that apply to Voice, Messaging, Cloud Storage, IoT, and all other Telnyx APIs.

## HTTP Methods

Telnyx APIs follow RESTful conventions using standard HTTP methods:

### **GET** - Retrieve Resources

Used to fetch information without making changes:

```bash theme={null}
GET /v2/messaging_profiles
GET /v2/calls/{call_id}
GET /v2/storage/buckets
```

### **POST** - Create Resources

Used to create new resources or trigger actions:

```bash theme={null}
POST /v2/calls          # Make a phone call
POST /v2/messages       # Send a message  
POST /v2/storage/objects # Upload a file
```

### **PATCH** - Update Resources

Used to modify existing resources:

```bash theme={null}
PATCH /v2/messaging_profiles/{id} # Update profile
PATCH /v2/phone_numbers/{id}      # Update phone number settings
```

### **DELETE** - Remove Resources

Used to delete resources:

```bash theme={null}
DELETE /v2/messaging_profiles/{id}     # Delete messaging profile
DELETE /v2/telephony_credentials/{id}  # Delete telephony credential
```

## Request Format

### Content-Type Headers

Most Telnyx APIs expect JSON payloads:

```bash theme={null}
Content-Type: application/json
```

For file uploads or form data:

```bash theme={null}
Content-Type: multipart/form-data
Content-Type: application/x-www-form-urlencoded
```

### Request Structure

```bash theme={null}
curl -X POST \
  --header "Authorization: Bearer YOUR_API_KEY" \
  --header "Content-Type: application/json" \
  --data '{
    "to": "+1234567890",
    "from": "+0987654321", 
    "text": "Hello World"
  }' \
  "https://api.telnyx.com/v2/messages"
```

## Response Format

### Standard Response Structure

Most Telnyx APIs return JSON responses with consistent structure:

```json theme={null}
{
  "data": {
    "id": "resource_id",
    "record_type": "resource_type",
    // ... resource properties
  },
  "meta": {
    "page_number": 1,
    "page_size": 20,
    "total_pages": 5,
    "total_results": 100
  }
}
```

### Success Responses

* **200 OK**: Request successful, data returned
* **201 Created**: Resource successfully created
* **202 Accepted**: Request accepted, processing asynchronously
* **204 No Content**: Request successful, no data to return

### Error Responses

Error responses include details to help troubleshoot issues:

```json theme={null}
{
  "errors": [
    {
      "code": "10001",
      "title": "Invalid parameter",
      "detail": "The 'to' field is required",
      "source": {
        "pointer": "/data/attributes/to"
      }
    }
  ]
}
```

### Telnyx API Error Codes

For a comprehensive list of all Telnyx-specific error codes and their meanings, see the [API Error Codes reference](api-error-codes.md). This resource provides detailed explanations for each error code to help you troubleshoot and handle API errors effectively.

Common error patterns include:

* **10xxx codes**: Parameter validation errors
* **20xxx codes**: Authentication and authorization errors
* **30xxx codes**: Resource not found or unavailable errors
* **40xxx codes**: Rate limiting and quota errors
* **50xxx codes**: Server-side errors

## HTTP Status Codes

### Client Errors (4xx)

* **400 Bad Request**: Invalid request format or parameters
* **401 Unauthorized**: Authentication failed
* **403 Forbidden**: Authentication succeeded but access denied
* **404 Not Found**: Resource doesn't exist
* **422 Unprocessable Entity**: Valid request format but logical errors
* **429 Too Many Requests**: Rate limit exceeded

### Server Errors (5xx)

* **500 Internal Server Error**: Unexpected server error
* **502 Bad Gateway**: Upstream service error
* **503 Service Unavailable**: Service temporarily unavailable
* **504 Gateway Timeout**: Request timeout

## Common Headers

### Request Headers

```bash theme={null}
Authorization: Bearer YOUR_API_KEY    # Authentication
Content-Type: application/json       # Request format
Accept: application/json             # Expected response format
User-Agent: YourApp/1.0             # Client identification
```

### Response Headers

```bash theme={null}
Content-Type: application/json      # Response format
X-RateLimit-Limit: 100             # Rate limit maximum
X-RateLimit-Remaining: 75          # Remaining requests
X-RateLimit-Reset: 1640995200      # Rate limit reset time
```

## Pagination

For endpoints that return lists, Telnyx uses consistent pagination:

### Request Parameters

```bash theme={null}
GET /v2/messages?page[number]=2&page[size]=50
```

### Response Metadata

```json theme={null}
{
  "data": [...],
  "meta": {
    "page_number": 2,
    "page_size": 50,
    "total_pages": 10,
    "total_results": 500
  }
}
```

## Filtering and Sorting

### Common Filter Patterns

```bash theme={null}
