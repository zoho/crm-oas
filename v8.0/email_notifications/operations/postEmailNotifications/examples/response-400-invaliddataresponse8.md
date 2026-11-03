INVALID_DATA error when feature_type field contains an incorrect data type

```json
{
  "email_notifications": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "feature_type",
        "expected_data_type": "text",
        "json_path": "$.email_notifications[*].feature_type"
      },
      "status": "error"
    }
  ]
}
```
