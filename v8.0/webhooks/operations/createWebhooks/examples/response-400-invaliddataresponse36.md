Error response when the authentication exceeds maximum length.

```json
{
  "webhooks": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "authentication",
        "maximum_length": 1,
        "json_path": "$.webhooks[*].authentication"
      },
      "status": "error"
    }
  ]
}
```
