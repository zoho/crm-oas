INVALID_DATA name length exceeded error for webhook name

```json
{
  "webhooks": [
    {
      "code": "INVALID_DATA",
      "details": {
        "maximum_length": 250,
        "api_name": "name",
        "json_path": "$.webhooks[0].name"
      },
      "message": "The lenght of name has exceeded the limit",
      "status": "error"
    }
  ]
}
```
