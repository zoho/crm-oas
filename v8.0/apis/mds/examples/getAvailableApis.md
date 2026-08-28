# Examples: getAvailableApis

**GET /__apis**

## Parameter examples

### `filters` (query) — Sample

Filter by send_mail scope

```json
"{\n  \"field\": {\n    \"api_name\": \"operation_types.oauth_scope\"\n  },\n  \"comparator\": \"equals\",\n  \"value\": \"send_mail\"\n}"
```

## Response examples

### Status `200` — `application/json` — ApiResponse

List of Available APIs

```json
{
  "__apis": [
    {
      "path": "/crm/v8/Quotes/{{id}}/actions/send_mail",
      "operation_types": [
        {
          "method": "POST",
          "oauth_scope": "ZohoCRM.send_mail.quotes.CREATE",
          "max_credits": 20,
          "min_credits": 20
        },
        {
          "method": "PUT",
          "oauth_scope": "ZohoCRM.send_mail.quotes.CREATE",
          "max_credits": 20,
          "min_credits": 20
        }
      ]
    },
    {
      "path": "/crm/v8/Accounts/{{id}}/photo",
      "operation_types": [
        {
          "method": "GET",
          "oauth_scope": "ZohoCRM.modules.accounts.READ",
          "max_credits": 1,
          "min_credits": 1
        },
        {
          "method": "DELETE",
          "oauth_scope": "ZohoCRM.modules.accounts.DELETE",
          "max_credits": 1,
          "min_credits": 1
        },
        {
          "method": "POST",
          "oauth_scope": "ZohoCRM.modules.accounts.CREATE",
          "max_credits": 1,
          "min_credits": 1
        }
      ]
    },
    {
      "path": "/crm/v8/Deals/{{id}}/Attachments",
      "operation_types": [
        {
          "method": "POST",
          "oauth_scope": "ZohoCRM.modules.deals.CREATE",
          "max_credits": 1,
          "min_credits": 1
        },
        {
          "method": "GET",
          "oauth_scope": "ZohoCRM.modules.deals.READ",
          "max_credits": 1,
          "min_credits": 1
        },
        {
          "method": "PUT",
          "oauth_scope": "ZohoCRM.modules.deals.UPDATE",
          "max_credits": 1,
          "min_credits": 1
        },
        {
          "method": "DELETE",
          "oauth_scope": "ZohoCRM.modules.deals.DELETE",
          "max_credits": 1,
          "min_credits": 1
        }
      ]
    }
  ]
}
```

### Status `400` — `application/json` — Sample

You provided an invalid filter parameter.

```json
{
  "code": "BAD_REQUEST",
  "message": "The request parameters are invalid.",
  "status": "error",
  "details": {
    "field": "module",
    "issue": "Unknown module."
  }
}
```

### Status `401` — `application/json` — Sample

Include a valid access token in the request header to authorize the API call.

```json
{
  "code": "UNAUTHORIZED",
  "message": "Authentication required or token invalid.",
  "status": "error",
  "details": {}
}
```

### Status `403` — `application/json` — Sample

You do not have enough permission to access this resource.

```json
{
  "code": "FORBIDDEN",
  "message": "You do not have permission to access this resource.",
  "status": "error",
  "details": {}
}
```

### Status `404` — `application/json` — Sample

Refer to the URL section of the API and provide a valid version and endpoint. 

```json
{
  "code": "NOT_FOUND",
  "message": "The requested resource was not found.",
  "status": "error",
  "details": {}
}
```

### Status `429` — `application/json` — Sample

Your rate limit has been exceeded. Please try again after sometime. 

```json
{
  "code": "TOO_MANY_REQUESTS",
  "message": "Rate limit exceeded. Please retry after the specified time.",
  "status": "error",
  "details": {
    "trace_id": "rate-limit-trace-id-001",
    "retry_after": 60,
    "limit": 100,
    "window": 60
  }
}
```

### Status `500` — `application/json` — Sample

Unexpected server error. Contact the support team. 

```json
{
  "code": "INTERNAL_ERROR",
  "message": "An unexpected error occurred.",
  "status": "error",
  "details": {
    "trace_id": "abc123def456"
  }
}
```
