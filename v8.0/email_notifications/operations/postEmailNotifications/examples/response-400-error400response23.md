INVALID_DATA error for resource field with invalid data type

```json
{
  "email_notifications": {
    "code": "INVALID_DATA",
    "message": "Invalid data type",
    "details": {
      "api_name": "resource",
      "expected_data_type": "jsonobject",
      "json_path": "$.email_notifications[*].reply_to_address.resource"
    },
    "status": "error"
  }
}
```
