INVALID_DATA error for invalid data type on details field

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
