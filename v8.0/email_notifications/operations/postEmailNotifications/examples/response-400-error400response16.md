INVALID_DATA error for invalid data type in the id field

```json
{
  "email_notifications": {
    "code": "INVALID_DATA",
    "message": "Invalid data type",
    "details": {
      "api_name": "id",
      "expected_data_type": "bigint",
      "json_path": "$.email_notifications[*].from_address.resource.id"
    },
    "status": "error"
  }
}
```
