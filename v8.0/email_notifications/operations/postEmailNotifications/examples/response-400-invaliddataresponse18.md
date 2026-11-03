INVALID_DATA error for the details field exceeding maximum length

```json
{
  "email_notifications": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "details",
        "maximum_length": 2,
        "json_path": "$.email_notifications[*].recipients.to[*].details"
      },
      "status": "error"
    }
  ]
}
```
