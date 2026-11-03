INVALID_DATA error for the details field with an incorrect data type

```json
{
  "email_notifications": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "details",
        "expected_data_type": "jsonobject",
        "json_path": "$.email_notifications[*].recipients.to[*].details"
      },
      "status": "error"
    }
  ]
}
```
