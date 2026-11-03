INVALID_DATA error for id field value exceeding maximum length

```json
{
  "email_notifications": {
    "code": "INVALID_DATA",
    "message": "Invalid data",
    "details": {
      "api_name": "id",
      "maximum_length": 19,
      "json_path": "$.email_notifications[*].recipients.to[*].details.id"
    },
    "status": "error"
  }
}
```
