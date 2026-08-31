Error response when description exceeds maximum length in webhooks.

```json
{
  "webhooks": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "description",
        "maximum_length": 250,
        "json_path": "$.webhooks[*].description"
      },
      "status": "error"
    }
  ]
}
```
