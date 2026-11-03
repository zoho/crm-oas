DEPENDENT_MISMATCH error when roles, groups, or territories are used as recipients with bulk_email enabled

```json
{
  "email_notifications": [
    {
      "code": "DEPENDENT_MISMATCH",
      "details": {
        "dependee": {
          "api_name": "bulk_email",
          "json_path": "$.email_notifications[0].bulk_email"
        },
        "dependent_field": {
          "api_name": "to",
          "json_path": "$.email_notifications[0].recipients.to"
        }
      },
      "message": "Roles, groups, and territories type emails in 'to' cannot be associated when bulk_email is true.",
      "status": "error"
    }
  ]
}
```
