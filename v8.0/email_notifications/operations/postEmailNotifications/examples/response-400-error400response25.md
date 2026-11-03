INVALID_DATA error — invalid data type for id field

```json
{
  "email_notifications": {
    "code": "INVALID_DATA",
    "message": "Invalid data type",
    "details": {
      "api_name": "id",
      "expected_data_type": "bigint",
      "json_path": "$.email_notifications[*].reply_to_address.resource.id"
    },
    "status": "error"
  }
}
```
