AMBIGUITY_DURING_PROCESSING error when a required field is missing

```json
{
  "email_notifications": [
    {
      "code": "AMBIGUITY_DURING_PROCESSING",
      "message": "required field not found",
      "status": "error",
      "details": {
        "ambiguity_due_to": [
          {
            "api_name": "id",
            "json_path": "$.email_notifications[0].module.id"
          },
          {
            "api_name": "api_name",
            "json_path": "$.email_notifications[0].module.api_name"
          }
        ]
      }
    }
  ]
}
```
