MANDATORY_NOT_FOUND error when the type field is missing

```json
{
  "email_notifications": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "message": "Required field is missing",
      "details": {
        "api_name": "type",
        "json_path": "$.email_notifications[*].recipients.to[*].type"
      },
      "status": "error"
    }
  ]
}
```
