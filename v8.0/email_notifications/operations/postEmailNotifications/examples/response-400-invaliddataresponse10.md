INVALID_DATA error for unsupported feature_type value

```json
{
  "email_notifications": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "feature_type",
        "supported_values": [
          "workflow"
        ],
        "json_path": "$.email_notifications[*].feature_type"
      },
      "status": "error"
    }
  ]
}
```
