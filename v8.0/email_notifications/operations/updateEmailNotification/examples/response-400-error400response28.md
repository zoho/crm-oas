INVALID_DATA error for notification name exceeding maximum length

```json
{
  "email_notifications": {
    "code": "INVALID_DATA",
    "message": "Invalid data",
    "details": {
      "api_name": "name",
      "maximum_length": 14,
      "json_path": "$.email_notifications[*].template.name"
    },
    "status": "error"
  }
}
```
