INVALID_DATA error for the name field exceeding maximum length

```json
{
  "email_notifications": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "name",
        "maximum_length": 100,
        "json_path": "$.email_notifications[*].name"
      },
      "status": "error"
    }
  ]
}
```
