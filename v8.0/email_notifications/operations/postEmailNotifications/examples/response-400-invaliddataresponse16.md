INVALID_DATA error for the recipients field exceeding maximum length

```json
{
  "email_notifications": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "recipients",
        "maximum_length": 1,
        "json_path": "$.email_notifications[*].recipients"
      },
      "status": "error"
    }
  ]
}
```
