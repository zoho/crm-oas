DEPENDENT_FIELD_MISSING error when required details field is absent

```json
{
  "email_notifications": [
    {
      "code": "DEPENDENT_FIELD_MISSING",
      "message": "Dependent field is missing",
      "details": {
        "dependee": {
          "api_name": "type",
          "json_path": "$.email_notifications[*].recipients.to[*].type"
        },
        "api_name": "details",
        "json_path": "$.email_notifications[*].recipients.to[*].email_notifications.recipients.to.details"
      },
      "status": "error"
    }
  ]
}
```
