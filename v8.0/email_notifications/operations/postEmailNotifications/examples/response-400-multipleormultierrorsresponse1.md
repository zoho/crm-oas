MULTIPLE_OR_MULTI_ERRORS response when selected recipients are unavailable

```json
{
  "email_notifications": [
    {
      "code": "MULTIPLE_OR_MULTI_ERRORS",
      "details": {
        "api_name": "recipients",
        "json_path": "$.email_notifications[0].recipients",
        "error": [
          {
            "code": "INVALID_DATA",
            "details": {
              "api_name": "api_name",
              "json_path": "$.email_notifications[0].recipients.to[0].resource.api_name"
            },
            "message": "Selected recipient is unavailable",
            "status": "error"
          }
        ]
      },
      "message": "Some selected recipients are not available",
      "status": "error"
    }
  ]
}
```
