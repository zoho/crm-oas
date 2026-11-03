INVALID_DATA error when feature_type field contains an invalid value

```json
{
  "email_notifications": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "feature_type",
        "maximum_length": 8,
        "json_path": "$.email_notifications[*].feature_type"
      },
      "status": "error"
    }
  ]
}
```
