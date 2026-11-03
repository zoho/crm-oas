INVALID_DATA error for invalid data in the recipient type field

```json
{
  "email_notifications": {
    "code": "INVALID_DATA",
    "message": "Invalid data",
    "details": {
      "api_name": "type",
      "maximum_length": 4,
      "json_path": "$.email_notifications[*].reply_to_address.type"
    },
    "status": "error"
  }
}
```
