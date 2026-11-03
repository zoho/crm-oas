INVALID_DATA error for incorrect data type on module field

```json
{
  "email_notifications": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "module",
        "expected_data_type": "jsonobject",
        "json_path": "$.email_notifications[*].module"
      },
      "status": "error"
    }
  ]
}
```
