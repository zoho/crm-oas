INVALID_DATA error for invalid data type in the type field

```json
{
  "email_notifications": {
    "code": "INVALID_DATA",
    "message": "Invalid data type",
    "details": {
      "api_name": "type",
      "expected_data_type": "text",
      "json_path": "$.email_notifications[*].from_address.type"
    },
    "status": "error"
  }
}
```
