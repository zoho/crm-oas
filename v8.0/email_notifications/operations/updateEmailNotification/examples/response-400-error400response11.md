INVALID_DATA error for invalid data type in the to field

```json
{
  "email_notifications": {
    "code": "INVALID_DATA",
    "message": "Invalid data type",
    "details": {
      "api_name": "to",
      "expected_data_type": "jsonarray",
      "json_path": "$.email_notifications[*].recipients.to"
    },
    "status": "error"
  }
}
```
