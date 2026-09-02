Error response when headers exceeds maximum length in webhooks.

```json
{
  "webhooks": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "headers",
        "maximum_length": 2,
        "json_path": "$.webhooks[*].headers"
      },
      "status": "error"
    }
  ]
}
```
