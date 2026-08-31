Error response when name exceeds maximum length.

```json
{
  "webhooks": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "name",
        "maximum_length": 11,
        "json_path": "$.webhooks[*].name"
      },
      "status": "error"
    }
  ]
}
```
