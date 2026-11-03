INVALID_DATA error for the recipients field with an incorrect data type

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
