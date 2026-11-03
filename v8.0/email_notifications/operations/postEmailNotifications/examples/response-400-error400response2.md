INVALID_DATA error for api_name field exceeding maximum length

```json
{
  "email_notifications": {
    "code": "INVALID_DATA",
    "message": "Invalid data",
    "details": {
      "api_name": "api_name",
      "maximum_length": 100,
      "json_path": "$.email_notifications[*].module.api_name"
    },
    "status": "error"
  }
}
```
