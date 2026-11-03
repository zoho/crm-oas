INVALID_DATA error for invalid data type in the from_address resource field

```json
{
  "email_notifications": {
    "code": "INVALID_DATA",
    "message": "Invalid data type",
    "details": {
      "api_name": "resource",
      "expected_data_type": "jsonobject",
      "json_path": "$.email_notifications[*].from_address.resource"
    },
    "status": "error"
  }
}
```
