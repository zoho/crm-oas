INVALID_DATA error — to field exceeds maximum length

```json
{
  "email_notifications": {
    "code": "INVALID_DATA",
    "message": "Invalid data",
    "details": {
      "api_name": "to",
      "maximum_length": 14,
      "json_path": "$.email_notifications[*].recipients.to"
    },
    "status": "error"
  }
}
```
