Error response when the body exceeds maximum length in webhooks.

```json
{
  "webhooks": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "body",
        "maximum_length": 3,
        "json_path": "$.webhooks[*].body"
      },
      "status": "error"
    }
  ]
}
```
