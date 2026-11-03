INVALID_DATA error for invalid data type on id field

```json
{
  "email_notifications": {
    "code": "INVALID_DATA",
    "message": "Invalid data type",
    "details": {
      "api_name": "id",
      "expected_data_type": "bigint",
      "json_path": "$.email_notifications[*].recipients.to[*].details.id"
    },
    "status": "error"
  }
}
```
