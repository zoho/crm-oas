Error response when the module exceeds maximum length in webhooks.

```json
{
  "webhooks": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "module",
        "maximum_length": 2,
        "json_path": "$.webhooks[*].module"
      },
      "status": "error"
    }
  ]
}
```
