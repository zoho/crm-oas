DEPENDENT_MISMATCH error when associated_to is not supported for the selected type

```json
{
  "email_notifications": [
    {
      "code": "DEPENDENT_MISMATCH",
      "details": {
        "dependee": {
          "api_name": "type",
          "json_path": "$.email_notifications[0].recipients.to[0].type"
        },
        "api_name": "associated_to",
        "json_path": "$.email_notifications[0].recipients.to[0].associated_to"
      },
      "message": "associated_to not supported for the selected type",
      "status": "error"
    }
  ]
}
```
