INVALID_DATA error for invalid data type in recipients field

```json
{
  "email_notifications": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "recipients",
        "expected_data_type": "jsonobject",
        "json_path": "$.email_notifications[*].recipients"
      },
      "status": "error"
    }
  ]
}
```
