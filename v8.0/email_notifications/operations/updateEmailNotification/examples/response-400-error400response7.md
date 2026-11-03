INVALID_DATA error response for invalid data type on the type field

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
