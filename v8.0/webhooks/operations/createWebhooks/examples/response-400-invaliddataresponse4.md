Error response when http_method has invalid data type.

```json
{
  "webhooks": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "http_method",
        "json_path": "$.webhooks[0].http_method"
      },
      "message": "The method type given is invalid",
      "status": "error"
    }
  ]
}
```
