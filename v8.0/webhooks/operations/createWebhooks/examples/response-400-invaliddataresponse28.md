Shows the error response when URL exceeds maximum length.

```json
{
  "webhooks": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "url",
        "maximum_length": 57,
        "json_path": "$.webhooks[*].url"
      },
      "status": "error"
    }
  ]
}
```
