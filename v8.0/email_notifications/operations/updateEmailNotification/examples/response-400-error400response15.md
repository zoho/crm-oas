INVALID_DATA error for exceeding maximum length of the api_name field

```json
{
  "email_notifications": {
    "code": "INVALID_DATA",
    "message": "Invalid data",
    "details": {
      "api_name": "api_name",
      "maximum_length": 20,
      "json_path": "$.email_notifications[*].recipients.to[*].details.api_name"
    },
    "status": "error"
  }
}
```
