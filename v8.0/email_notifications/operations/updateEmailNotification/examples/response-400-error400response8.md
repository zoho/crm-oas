INVALID_DATA error response for type field value exceeding maximum length

```json
{
  "email_notifications": {
    "code": "INVALID_DATA",
    "message": "Invalid data",
    "details": {
      "api_name": "type",
      "maximum_length": 4,
      "json_path": "$.email_notifications[*].from_address.type"
    },
    "status": "error"
  }
}
```
