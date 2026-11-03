INVALID_DATA error for exceeding maximum length of the to field

```json
{
  "email_notifications": {
    "code": "INVALID_DATA",
    "message": "Invalid data",
    "details": {
      "api_name": "to",
      "maximum_length": 12,
      "json_path": "$.email_notifications[*].recipients.to"
    },
    "status": "error"
  }
}
```
