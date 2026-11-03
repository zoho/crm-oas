INVALID_DATA error for invalid data type on api_name field

```json
{
  "email_notifications": {
    "code": "INVALID_DATA",
    "message": "Invalid data type",
    "details": {
      "api_name": "api_name",
      "expected_data_type": "text",
      "json_path": "$.email_notifications[*].module.api_name"
    },
    "status": "error"
  }
}
```
