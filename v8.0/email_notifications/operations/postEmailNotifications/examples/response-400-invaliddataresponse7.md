INVALID_DATA error when bulk_email field contains an incorrect data type

```json
{
  "email_notifications": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "bulk_email",
        "expected_data_type": "boolean",
        "json_path": "$.email_notifications[*].bulk_email"
      },
      "status": "error"
    }
  ]
}
```
