INVALID_DATA error for invalid data type in resource ID field

```json
{
  "email_notifications": {
    "code": "INVALID_DATA",
    "message": "Invalid data type",
    "details": {
      "api_name": "id",
      "expected_data_type": "bigint",
      "json_path": "$.email_notifications[*].template.id"
    },
    "status": "error"
  }
}
```
