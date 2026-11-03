INVALID_DATA error for resource field exceeding maximum length

```json
{
  "email_notifications": {
    "code": "INVALID_DATA",
    "message": "Invalid data",
    "details": {
      "api_name": "resource",
      "maximum_length": 1,
      "json_path": "$.email_notifications[*].reply_to_address.resource"
    },
    "status": "error"
  }
}
```
