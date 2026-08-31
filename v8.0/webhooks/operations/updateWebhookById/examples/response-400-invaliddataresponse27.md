Field value fails validation for a webhook property

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
