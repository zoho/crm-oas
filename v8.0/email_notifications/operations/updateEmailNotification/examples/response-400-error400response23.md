INVALID_DATA error for incorrect data type on type field

```json
{
  "email_notifications": {
    "code": "INVALID_DATA",
    "message": "Invalid data type",
    "details": {
      "api_name": "type",
      "expected_data_type": "text",
      "json_path": "$.email_notifications[*].reply_to_address.type"
    },
    "status": "error"
  }
}
```
