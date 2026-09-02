Field value fails validation in webhook request

```json
{
  "webhooks": {
    "code": "INVALID_DATA",
    "message": "Invalid data",
    "details": {
      "api_name": "format",
      "maximum_length": 4,
      "json_path": "$.webhooks[*].body.format"
    },
    "status": "error"
  }
}
```
