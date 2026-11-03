INVALID_DATA error for invalid data type in reply_to_address

```json
{
  "email_notifications": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "reply_to_address",
        "expected_data_type": "jsonobject",
        "json_path": "$.email_notifications[*].reply_to_address"
      },
      "status": "error"
    }
  ]
}
```
