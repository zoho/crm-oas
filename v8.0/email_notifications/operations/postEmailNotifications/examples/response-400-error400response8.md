MANDATORY_NOT_FOUND error — required field missing in notification payload

```json
{
  "email_notifications": {
    "code": "MANDATORY_NOT_FOUND",
    "message": "Required field is missing",
    "details": {
      "api_name": "api_name",
      "json_path": "$.email_notifications[*].recipients.to[*].details.api_name"
    },
    "status": "error"
  }
}
```
