Error response when the http_method is missing.

```json
{
  "webhooks": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "message": "Required field is missing",
      "details": {
        "api_name": "http_method",
        "json_path": "$.webhooks[*].http_method"
      },
      "status": "error"
    }
  ]
}
```
