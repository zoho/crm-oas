Field value fails validation for the specified webhook property

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
