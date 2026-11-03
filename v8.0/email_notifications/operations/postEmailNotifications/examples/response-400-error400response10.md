INVALID_DATA error for invalid api_name value

```json
{
  "email_notifications": {
    "code": "INVALID_DATA",
    "message": "Invalid data",
    "details": {
      "api_name": "api_name",
      "maximum_length": 100,
      "json_path": "$.email_notifications[*].recipients.to[*].details.api_name"
    },
    "status": "error"
  }
}
```
