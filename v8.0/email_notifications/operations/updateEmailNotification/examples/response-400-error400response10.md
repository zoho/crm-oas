MANDATORY_NOT_FOUND error when a required field is missing from a nested recipient object

```json
{
  "email_notifications": {
    "code": "MANDATORY_NOT_FOUND",
    "message": "Required field is missing",
    "details": {
      "api_name": "to",
      "json_path": "$.email_notifications[*].recipients.to"
    },
    "status": "error"
  }
}
```
