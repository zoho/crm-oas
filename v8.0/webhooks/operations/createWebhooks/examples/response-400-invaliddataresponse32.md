Error response when http_method exceeds maximum length.

```json
{
  "webhooks": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "http_method",
        "maximum_length": 4,
        "json_path": "$.webhooks[*].http_method"
      },
      "status": "error"
    }
  ]
}
```
