INVALID_DATA error for incorrect data type on name field

```json
{
  "email_notifications": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "name",
        "expected_data_type": "text",
        "json_path": "$.email_notifications[*].name"
      },
      "status": "error"
    }
  ]
}
```
