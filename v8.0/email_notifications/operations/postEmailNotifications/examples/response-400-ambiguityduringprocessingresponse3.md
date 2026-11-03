AMBIGUITY_DURING_PROCESSING error when BCC recipients are added without enabling bulk_email

```json
{
  "email_notifications": [
    {
      "code": "AMBIGUITY_DURING_PROCESSING",
      "message": "Set bulk_email as true to pass cc",
      "status": "error",
      "details": {
        "ambiguity_due_to": [
          {
            "api_name": "id",
            "json_path": "$.email_notifications[0].bulk_email"
          },
          {
            "api_name": "api_name",
            "json_path": "$.email_notifications[0].recipients.cc"
          }
        ]
      }
    }
  ]
}
```
