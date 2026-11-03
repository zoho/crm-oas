INVALID_DATA error when email notification name exceeds the maximum length

```json
{
  "email_notifications": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "name",
        "maximum_limit": 250,
        "json_path": "$.email_notifications[0].name"
      },
      "message": "The lenght of name has exceeded the limit",
      "status": "error"
    }
  ]
}
```
